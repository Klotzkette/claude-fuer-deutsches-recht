/* Browser-only adapter. No automatic setup, storage restore, proxy or case download. */
'use strict';

(() => {
  if (!window.PORTABLE_BUNDLE) return;

  const MiB = 1024 * 1024;
  const LIMIT = Object.freeze({ case: 2 * MiB, geometry: 256 * 1024, positions: 10000, totalPositions: 40000, parcels: 200, pageSize: 200, pages: 5, timeout: 15000 });
  const STALE = 'Vorbereitetes oder importiertes Profil; keine aktuelle Quellen- oder Zuständigkeitsprüfung. Angaben vor Verwendung prüfen.';
  const OFFLINE = 'Direktabruf nicht möglich (offline, CORS oder Dienstfehler). Bei file:// kann der Browser amtliche Dienste sperren. Manuelle Erfassung und GeoJSON-Import bleiben verfügbar; für weitere Dienste den lokalen Server verwenden. Es wird kein öffentlicher Proxy verwendet.';
  const GML = new Set(['http://www.opengis.net/gml', 'http://www.opengis.net/gml/3.2']);
  const WFS = new Set(['http://www.opengis.net/wfs', 'http://www.opengis.net/wfs/2.0']);
  const STATES = ['', 'Schleswig-Holstein', 'Hamburg', 'Niedersachsen', 'Bremen', 'Nordrhein-Westfalen', 'Hessen', 'Rheinland-Pfalz', 'Baden-Württemberg', 'Bayern', 'Saarland', 'Berlin', 'Brandenburg', 'Mecklenburg-Vorpommern', 'Sachsen', 'Sachsen-Anhalt', 'Thüringen'];
  // The bundle allowlist is intersected with these implemented official services.
  const SERVICES = Object.freeze({
    'bkg-places': 'https://sgx.geodatenzentrum.de/wfs_vg250',
    'bkg-topplus-open': 'https://sgx.geodatenzentrum.de/wms_topplus_open',
    'nrw-abk': 'https://www.wms.nrw.de/geobasis/wms_nw_abk',
    'nrw-dop': 'https://www.wms.nrw.de/geobasis/wms_nw_dop',
    'nrw-alkis': 'https://www.wfs.nrw.de/geobasis/wfs_nw_alkis_vereinfacht',
    'sn-webatlas': 'https://geodienste.sachsen.de/wms_geosn_webatlas-sn/guest',
    'sn-dop': 'https://geodienste.sachsen.de/wms_geosn_dop-rgb/guest'
  });
  const CASE_TEXT = 'case_id purpose specific_interest requested_information_scope sender_organisation sender_address contact_person legal_department_contact attachments created_at updated_at'.split(' ');
  const PARCEL_TEXT = 'stable_id provider_id municipality municipality_code district_name district_code flur numerator denominator official_parcel_reference area_unit location_text source_url source_date retrieved_at identification_status grundbuchblatt grundbuchbezirk grundbuchblatt_source grundbuchblatt_date'.split(' ');
  const PROFILE_TEXT = 'id profile_id name state state_code district municipality_code verification_state center_method attribution license verified_at data_date source_url district_source_url'.split(' ');
  const PROVIDER_TEXT = 'id provider_id owner title role protocol version axis_order license attribution access_requirements test_result status verification_state name layer type_name reason format verified_at catalog_source_url service_url source_url tested_url'.split(' ');
  const AUTHORITY_TEXT = 'type authority_type official_name jurisdiction postal_address visitor_address submission_information verification_state status note verified_at official_website official_form_url source_url'.split(' ');
  const EVIDENCE_TEXT = 'title name kind description note status verification_state official_name verified_at checked_at retrieved_at source_date matched returned url source_url tested_url'.split(' ');
  const clone = (value) => JSON.parse(JSON.stringify(value));
  const bytes = (value) => new TextEncoder().encode(typeof value === 'string' ? value : JSON.stringify(value)).byteLength;
  const record = (value) => value !== null && typeof value === 'object' && !Array.isArray(value);
  const fail = (message) => { throw new Error(message); };
  const abort = () => new DOMException('Anfrage abgebrochen.', 'AbortError');
  const checkSignal = (signal) => { if (signal?.aborted) throw abort(); };
  const now = () => new Date().toISOString();
  const fold = (value) => value.normalize('NFKC').toLocaleLowerCase('de').replace(/\s+/g, ' ').trim();
  const agsOK = (value) => typeof value === 'string' && /^\d{8}$/.test(value) && !!STATES[Number(value.slice(0, 2))];
  const catalogs = clone(window.PORTABLE_BUNDLE.catalogs || {});
  const prepared = window.PORTABLE_BUNDLE.profile ? clone(window.PORTABLE_BUNDLE.profile) : null;
  const places = new Map(), profiles = new Map();
  let sequence = 0;

  function boundedJSON(value, maxBytes = LIMIT.case, maxText = 20000) {
    let nodes = 0;
    function visit(item, depth) {
      if (++nodes > 150000 || depth > 16) fail('JSON-Struktur zu groß oder zu tief verschachtelt.');
      if (typeof item === 'string') {
        if (item.length > maxText || /[\u0000-\u0008\u000b\u000c\u000e-\u001f\u007f]/.test(item)) fail('Text zu lang oder ungültige Steuerzeichen.');
      } else if (typeof item === 'number') {
        if (!Number.isFinite(item) || Math.abs(item) > 1e15) fail('Ungültige Zahl.');
      } else if (Array.isArray(item)) {
        for (const child of item) visit(child, depth + 1);
      } else if (record(item)) {
        for (const [key, child] of Object.entries(item)) {
          if (['__proto__', 'prototype', 'constructor'].includes(key)) fail('Unzulässiger JSON-Feldname.');
          visit(key, depth + 1); visit(child, depth + 1);
        }
      } else if (item !== null && typeof item !== 'boolean') fail('Nur JSON-Datentypen sind erlaubt.');
    }
    visit(value, 0);
    if (bytes(value) > maxBytes) fail('Import/Vorgang überschreitet das Größenbudget.');
  }

  function texts(value, fields) {
    if (!record(value)) fail('JSON-Objekt erforderlich.');
    const output = {};
    for (const key of fields) if (Object.hasOwn(value, key)) {
      if (value[key] === null && /(?:_at|data_date)$/.test(key)) output[key] = null;
      else if (typeof value[key] === 'string') output[key] = value[key];
      else fail(`Text erwartet: ${key}.`);
    }
    return output;
  }

  function list(value, limit) {
    if (value === undefined) return [];
    if (!Array.isArray(value) || value.length > limit) fail('Liste überschreitet das Eintragsbudget.');
    return value;
  }

  function stringList(value, limit) {
    return list(value, limit).map((item) => typeof item === 'string' ? item : fail('Textliste erforderlich.'));
  }

  function bounds(value) {
    if (!Array.isArray(value) || value.length !== 4 || !value.every(Number.isFinite)) fail('Ungültiger Kartenausschnitt.');
    const [w, s, e, n] = value;
    if (!(-180 <= w && w < e && e <= 180 && -90 <= s && s < n && n <= 90)) fail('Kartenausschnitt liegt außerhalb WGS84 oder ist leer.');
    return [...value];
  }

  function center(value) {
    if (!Array.isArray(value) || value.length !== 2 || !value.every(Number.isFinite) || Math.abs(value[0]) > 90 || Math.abs(value[1]) > 180) fail('Kartenzentrum muss WGS84 [Breite, Länge] enthalten.');
    return [...value];
  }

  function geometry(value, budget, pointAllowed = false) {
    if (!record(value) || Object.keys(value).some((key) => !['type', 'coordinates'].includes(key))) fail('GeoJSON-Geometrie nur mit type und coordinates in WGS84.');
    const depth = { Polygon: 2, MultiPolygon: 3, ...(pointAllowed ? { Point: 0 } : {}) }[value.type];
    if (depth === undefined) fail('Nur Polygon/MultiPolygon-Flurstücke in WGS84 sind importierbar.');
    if (bytes(value) > LIMIT.geometry) fail('Geometrie überschreitet 256 KiB.');
    let count = 0;
    function walk(item, level) {
      if (!Array.isArray(item) || !item.length || item.length > LIMIT.positions) fail('Leere oder zu große Geometrie.');
      if (!level) {
        if (++count > LIMIT.positions || ++budget.count > LIMIT.totalPositions) fail('Zu viele Geometriepositionen (10000 je Geometrie, 40000 insgesamt).');
        if (![2, 3].includes(item.length) || !item.every(Number.isFinite) || Math.abs(item[0]) > 180 || Math.abs(item[1]) > 90) fail('GeoJSON benötigt gültige WGS84-Koordinaten als Länge/Breite.');
        return [...item];
      }
      const parts = item.map((part) => walk(part, level - 1));
      if (level === 1 && (parts.length < 4 || JSON.stringify(parts[0]) !== JSON.stringify(parts.at(-1)))) fail('Polygonring muss geschlossen sein und mindestens vier Positionen enthalten.');
      return parts;
    }
    return { type: value.type, coordinates: walk(value.coordinates, depth) };
  }

  function area(value) {
    if (value == null || value === '') return null;
    if ((typeof value !== 'number' && typeof value !== 'string') || (typeof value === 'string' && !/^(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?$/.test(value.trim()))) fail('Ungültige Flächenangabe.');
    const number = Number(value);
    if (!Number.isFinite(number) || number < 0 || number > 1e15) fail('Ungültige Flächenangabe.');
    return number;
  }

  function sanitizeProfile(raw) {
    const output = texts(raw, PROFILE_TEXT);
    if (raw.center != null) output.center = center(raw.center);
    if (raw.bounds != null) output.bounds = bounds(raw.bounds);
    output.source_urls = stringList(raw.source_urls, 30);
    output.warnings = [...stringList(raw.warnings, 99).filter((item) => item !== STALE), STALE];
    output.verification_state = 'gefunden_ungeprueft';
    output.authorities = list(raw.authorities, 30).map((item) => ({ ...texts(item, AUTHORITY_TEXT), evidence_urls: stringList(item.evidence_urls, 30), verification_state: 'gefunden_ungeprueft', status: 'gefunden_ungeprueft', note: STALE }));
    output.evidence = list(raw.evidence, 100).map((item) => ({ ...texts(item, EVIDENCE_TEXT), verification_state: 'gefunden_ungeprueft', status: 'gefunden_ungeprueft', note: STALE }));
    output.providers = list(raw.providers, 50).map((item) => {
      const provider = { ...texts(item, PROVIDER_TEXT), verification_state: 'gefunden_ungeprueft', status: 'gefunden_ungeprueft', test_result: STALE };
      for (const key of ['layers', 'crs']) if (item[key] !== undefined) provider[key] = Array.isArray(item[key]) ? stringList(item[key], 100) : texts(item, [key])[key];
      return provider;
    });
    return output;
  }

  function exactService(id, value) {
    if (typeof value !== 'string' || value !== SERVICES[id]) return null;
    const url = new URL(value);
    return catalogs.allowed_hosts?.[url.hostname]?.includes(url.pathname) ? url.href : null;
  }

  function catalogProvider(id) {
    const found = catalogs.providers?.find((provider) => provider.provider_id === id);
    if (!found || !exactService(id, found.service_url)) return null;
    if (id === 'nrw-alkis') return found.protocol === 'WFS' && found.type_name === 'ave:Flurstueck' ? found : null;
    return found.protocol === 'WMS' && found.crs === 'EPSG:3857' && typeof found.layers === 'string' && /^[\w,.-]+$/.test(found.layers) ? found : null;
  }

  function profileFor(raw, trustedPlace = false) {
    const profile = sanitizeProfile(raw);
    profile.profile_id = `portable-${++sequence}`;
    profile.center = center(profile.center);
    const code = agsOK(profile.municipality_code) ? profile.municipality_code.slice(0, 2) : '';
    profile.state_code = code;
    const imported = profile.providers;
    profile.providers = [];
    for (const item of list(catalogs.providers, 50)) {
      const coverage = item.coverage;
      if (coverage?.country !== 'DE' || !Array.isArray(coverage.state_codes) || (coverage.state_codes.length && !coverage.state_codes.includes(code))) continue;
      const provider = catalogProvider(item.provider_id);
      const supported = !!provider && (provider.protocol === 'WMS' || trustedPlace);
      const safe = sanitizeProfile({ providers: [item] }).providers[0];
      profile.providers.push({ ...safe, portable: supported, verification_state: supported ? 'browser_available' : 'eingeschraenkt', status: supported ? 'browser_available' : 'eingeschraenkt', test_result: supported ? 'Kuratierter amtlicher Direktdienst; Browserabruf möglich, abhängig von Netz/CORS. Keine aktuelle Verifikation.' : 'Kein freigegebener Browseradapter für diesen Dienst/Ort. Lokalen Server oder manuellen Import verwenden.' });
    }
    for (const item of imported) if (!profile.providers.some((known) => known.provider_id === item.provider_id)) profile.providers.push({ ...item, portable: false });
    profile.providers = profile.providers.slice(0, 50);
    if (!profile.providers.some((item) => item.protocol === 'WFS' && item.portable)) profile.warnings.push('Kein unterstützter Flurstück-Direktabruf. Manuell erfassen oder WGS84-GeoJSON importieren.');
    profiles.set(profile.profile_id, clone(profile));
    while (profiles.size > 20) profiles.delete(profiles.keys().next().value);
    return profile;
  }

  function mapURL(provider) {
    if (!record(provider) || provider.portable !== true || provider.verification_state !== 'browser_available') return null;
    const known = catalogProvider(provider.provider_id);
    if (!known || known.protocol !== 'WMS' || provider.protocol !== 'WMS') return null;
    for (const key of ['service_url', 'layers', 'crs', 'role']) if (provider[key] !== known[key]) return null;
    return exactService(known.provider_id, provider.service_url);
  }

  function getProfile(id) {
    const profile = profiles.get(id);
    if (!profile) fail('Ortsprofil nicht aktiv. Ort erneut auswählen oder Vorgang importieren.');
    return profile;
  }

  async function fetchText(service, params, maxBytes, signal) {
    const base = service === 'bkg-places' ? exactService(service, catalogs.places?.service_url) : catalogProvider(service)?.service_url;
    if (!base) fail('Amtlicher Dienst ist nicht im portablen Katalog freigegeben.');
    checkSignal(signal);
    const url = new URL(base);
    for (const [key, value] of Object.entries(params)) url.searchParams.set(key, String(value));
    const controller = new AbortController();
    let timer, rejectAbort, reader;
    const stopped = new Promise((_, reject) => { rejectAbort = reject; });
    const onAbort = () => { controller.abort(); rejectAbort(abort()); };
    signal?.addEventListener('abort', onAbort, { once: true });
    timer = setTimeout(() => { controller.abort(); rejectAbort(new Error(`Zeitbudget des Direktabrufs erreicht. ${OFFLINE}`)); }, LIMIT.timeout);
    try {
      const run = async () => {
        const response = await fetch(url.href, { method: 'GET', credentials: 'omit', redirect: 'error', mode: 'cors', referrerPolicy: 'no-referrer', cache: 'no-store', signal: controller.signal, headers: { Accept: service === 'bkg-places' ? 'application/json' : 'application/xml,text/xml' } });
        if (response.redirected || response.type === 'opaque' || (response.url && response.url !== url.href)) fail('Weiterleitungen und undurchsichtige Antworten sind gesperrt.');
        if (!response.ok) fail(`Amtlicher Dienst: HTTP ${response.status}.`);
        if (Number(response.headers.get('content-length')) > maxBytes) fail('Dienstantwort überschreitet das Größenbudget.');
        // Never use unbounded response.text(): a stream is required even without Content-Length.
        if (!response.body?.getReader) fail('Browser unterstützt keinen begrenzten Datenstrom. Lokalen Server verwenden.');
        reader = response.body.getReader();
        const decoder = new TextDecoder('utf-8', { fatal: true });
        const chunks = [];
        let size = 0;
        while (true) {
          const { value, done } = await reader.read();
          checkSignal(controller.signal);
          if (done) break;
          size += value.byteLength;
          if (size > maxBytes) fail('Dienstantwort überschreitet das Größenbudget.');
          chunks.push(decoder.decode(value, { stream: true }));
        }
        chunks.push(decoder.decode());
        return chunks.join('');
      };
      return await Promise.race([run(), stopped]);
    } catch (error) {
      checkSignal(signal);
      if (error instanceof TypeError) throw new Error(OFFLINE);
      throw error;
    } finally {
      clearTimeout(timer); signal?.removeEventListener('abort', onAbort);
      controller.abort();
      if (reader) reader.cancel().catch(() => {});
    }
  }

  function remember(candidate) {
    places.set(candidate.id, clone(candidate));
    while (places.size > 100) places.delete(places.keys().next().value);
    return candidate;
  }

  async function searchPlaces(query, signal) {
    if (typeof query !== 'string') fail('Gemeindename oder achtstelligen AGS eingeben.');
    query = query.normalize('NFC').replace(/\s+/g, ' ').trim();
    if (query.length < 2 || query.length > 100 || /[%_*\\<>\u0000-\u001f]/.test(query)) fail('Gemeindename mit 2 bis 100 Zeichen, ohne Suchoperatoren eingeben.');
    if (prepared && ((prepared.name && fold(prepared.name).startsWith(fold(query))) || prepared.municipality_code === query)) {
      const candidate = { ...sanitizeProfile(prepared), id: `prepared:${prepared.municipality_code || 'place'}` };
      center(candidate.center);
      return { candidates: [remember(candidate)], warnings: [STALE] };
    }
    const literal = query.replace(/'/g, "''");
    const text = await fetchText('bkg-places', { service: 'WFS', version: '2.0.0', request: 'GetFeature', typeNames: 'vg250:vg250_gem', outputFormat: 'application/json', srsName: 'EPSG:4326', count: 40, startIndex: 0, cql_filter: /^\d{8}$/.test(query) ? `ags = '${literal}'` : `gen ILIKE '${literal}%'`, sortBy: 'gen A,ags A' }, 4 * MiB, signal);
    let raw;
    try { raw = JSON.parse(text); } catch { fail('BKG liefert kein gültiges GeoJSON.'); }
    if (!record(raw) || raw.type !== 'FeatureCollection' || !Array.isArray(raw.features) || raw.features.length > 40) fail('Unerwartete oder zu große BKG-Trefferliste.');
    const found = new Map();
    for (const feature of raw.features) {
      const props = feature?.properties;
      if (!record(props) || !agsOK(props.ags) || typeof props.gen !== 'string' || !props.gen.trim() || props.gen.length > 200) continue;
      if (/^\d{8}$/.test(query) ? props.ags !== query : !fold(props.gen).startsWith(fold(query))) continue;
      const box = bounds(feature.bbox);
      if (found.has(props.ags)) {
        const previous = found.get(props.ags).bounds;
        found.get(props.ags).bounds = [Math.min(previous[0], box[0]), Math.min(previous[1], box[1]), Math.max(previous[2], box[2]), Math.max(previous[3], box[3])];
        continue;
      }
      found.set(props.ags, { id: `ags:${props.ags}`, name: props.gen, municipality_code: props.ags, state_code: props.ags.slice(0, 2), state: STATES[Number(props.ags.slice(0, 2))], district: '', bounds: box, source_url: SERVICES['bkg-places'], attribution: catalogs.places.attribution || 'BKG VG250', license: catalogs.places.license || '', verification_state: 'browser_available', data_date: typeof props.wsk === 'string' ? props.wsk : '', warnings: ['Gemeinde aus amtlichem BKG-Direktabruf; generalisierte Grenzen, kein Kataster. Kreis und Zuständigkeiten nicht geprüft.', ...(raw.features.length === 40 ? ['Treffer begrenzt. Mit vollständigem Namen oder AGS erneut suchen.'] : [])] });
    }
    const candidates = [...found.values()].slice(0, 25).map((item) => {
      const [w, s, e, n] = item.bounds;
      return remember({ ...item, center: [(s + n) / 2, (w + e) / 2], center_method: 'Mittelpunkt der generalisierten BKG-Gemeindegrenzen, kein Amtssitz' });
    });
    return { candidates };
  }

  async function setup(submitted, signal) {
    if (!record(submitted)) fail('Bitte zuerst einen Ort auswählen.');
    boundedJSON(submitted);
    if (prepared && ((agsOK(prepared.municipality_code) && submitted.municipality_code === prepared.municipality_code) || (submitted.id && submitted.id === prepared.id))) return { profile: profileFor(prepared, true) };
    const saved = profiles.get(submitted.profile_id);
    if (saved && saved.municipality_code === submitted.municipality_code) return { profile: profileFor(saved, saved.providers.some((item) => item.portable && item.protocol === 'WFS')) };
    const candidate = places.get(submitted.id);
    if (candidate) return { profile: profileFor(candidate, true) };
    try {
      const result = await searchPlaces(agsOK(submitted.municipality_code) ? submitted.municipality_code : submitted.name, signal);
      const match = result.candidates.find((item) => agsOK(submitted.municipality_code) ? item.municipality_code === submitted.municipality_code : fold(item.name) === fold(submitted.name));
      if (match) return { profile: profileFor(match, true) };
    } catch (error) {
      checkSignal(signal);
      if (!submitted.center) throw error;
    }
    const profile = profileFor(submitted, false);
    profile.warnings.push('Ort nicht aktuell amtlich zugeordnet. Importiertes Kartenzentrum nur als Lagehinweis; manuelle Bearbeitung bleibt möglich.');
    profiles.set(profile.profile_id, clone(profile));
    return { profile };
  }

  function example() {
    const reference = prepared?.municipality_code === '05515000' ? prepared : { name: 'Münster', municipality_code: '05515000', state_code: '05', state: 'Nordrhein-Westfalen', district: '', authorities: [], providers: [] };
    return { profile: profileFor({ ...reference, center: [51.9607, 7.6261], center_method: 'Explizite Münster-Referenzposition; kein Eigentums- oder Flurstücksnachweis', warnings: [...(reference.warnings || []), 'Münster-Referenz ohne voreingestellten Absender, Organisation oder Flurstückauswahl.'] }, true) };
  }

  function parseXML(text) {
    if (/<!\s*(?:DOCTYPE|ENTITY)\b/i.test(text)) fail('DTD und externe XML-Entitäten sind gesperrt.');
    const root = new DOMParser().parseFromString(text, 'application/xml').documentElement;
    if (!root || root.localName === 'parsererror' || root.getElementsByTagNameNS('*', 'parsererror').length) fail('Ungültiges GML/XML.');
    if (/Exception/.test(root.localName)) fail('Der Geodatendienst meldet einen Dienstfehler statt Nutzdaten.');
    if (!WFS.has(root.namespaceURI) || root.localName !== 'FeatureCollection') fail('Keine WFS-Flurstücksammlung.');
    return root;
  }

  const children = (node) => Array.from(node.children || []);
  const gmlNodes = (node, names) => Array.from(node.getElementsByTagNameNS('*', '*')).filter((item) => GML.has(item.namespaceURI) && names.includes(item.localName));
  function inherited(node, key, stop) {
    for (let current = node; current && current !== stop.parentElement; current = current.parentElement) if (current.hasAttribute(key)) return current.getAttribute(key);
    return '';
  }

  function gmlGeometry(feature, budget) {
    const polygons = gmlNodes(feature, ['Polygon', 'PolygonPatch']);
    if (!polygons.length) fail('Keine unterstützte Flurstückgeometrie.');
    const parts = polygons.map((polygon) => {
      const rings = [];
      let exterior;
      for (const boundary of children(polygon)) {
        if (!GML.has(boundary.namespaceURI)) continue;
        const outer = ['exterior', 'outerBoundaryIs'].includes(boundary.localName);
        if (!outer && !['interior', 'innerBoundaryIs'].includes(boundary.localName)) continue;
        const points = [];
        const lists = gmlNodes(boundary, ['posList']);
        const positions = lists.length ? lists : gmlNodes(boundary, ['pos', 'coordinates']);
        for (const node of positions) {
          const crs = inherited(node, 'srsName', feature);
          const latFirst = ['urn:ogc:def:crs:EPSG::4326', 'urn:ogc:def:crs:EPSG:6.9:4326', 'http://www.opengis.net/def/crs/EPSG/0/4326'].includes(crs);
          const lonFirst = ['urn:ogc:def:crs:OGC:1.3:CRS84', 'http://www.opengis.net/def/crs/OGC/1.3/CRS84'].includes(crs);
          if (!latFirst && !lonFirst) fail('GML braucht eindeutiges WGS84-CRS mit Achsenangabe. Andere/mehrdeutige CRS über den lokalen Server importieren.');
          const dimension = Number(inherited(node, 'srsDimension', feature) || 2);
          if (![2, 3].includes(dimension)) fail('Ungültige GML-Dimension.');
          const tokens = node.textContent.trim();
          if (!tokens) fail('Leere GML-Koordinaten.');
          const values = node.localName === 'coordinates' ? tokens.split(/\s+/).map((part) => part.split(',')) : [tokens.split(/\s+/)];
          for (const components of values) {
            if (components.some((part) => !/^[+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?$/.test(part))) fail('Ungültige GML-Zahl.');
            const step = node.localName === 'coordinates' || node.localName === 'pos' ? components.length : dimension;
            if (![2, 3].includes(step) || components.length % step || (node.localName === 'pos' && components.length !== dimension)) fail('Unvollständige GML-Koordinaten.');
            for (let i = 0; i < components.length; i += step) {
              const tuple = components.slice(i, i + step).map(Number);
              if (!tuple.every(Number.isFinite)) fail('Ungültige GML-Zahl.');
              points.push(latFirst ? [tuple[1], tuple[0]] : [tuple[0], tuple[1]]);
              if (points.length > LIMIT.positions) fail('Zu viele GML-Positionen.');
            }
          }
        }
        if (outer) { if (exterior) fail('Mehrere äußere GML-Ringe.'); exterior = points; }
        else rings.push(points);
      }
      if (!exterior) fail('Flurstück ohne äußeren Polygonring.');
      return [exterior, ...rings];
    });
    return geometry({ type: 'MultiPolygon', coordinates: parts }, budget);
  }

  function parseParcels(text, provider, profile, page) {
    const root = parseXML(text);
    const members = children(root).filter((node) => (WFS.has(node.namespaceURI) && node.localName === 'member') || (GML.has(node.namespaceURI) && node.localName === 'featureMember'));
    if (members.length > LIMIT.pageSize) fail('Die Flurstückantwort überschreitet 200 Einträge.');
    const features = [], seen = new Set(), budget = { count: 0 };
    const fieldMap = { municipality: 'gemeinde', municipality_code: 'gmdschl', district_name: 'gemarkung', district_code: 'gemaschl', flur: 'flur', numerator: 'flstnrzae', denominator: 'flstnrnen', official_parcel_reference: 'flstkennz', location_text: 'lagebeztxt', source_date: 'aktualit' };
    for (const member of members) {
      if (children(member).length !== 1) fail('Ungültiges WFS-Feature.');
      const feature = children(member)[0];
      if (feature.localName !== 'Flurstueck' || !feature.namespaceURI || GML.has(feature.namespaceURI) || WFS.has(feature.namespaceURI)) fail('Nicht unterstütztes WFS-Flurstückschema.');
      const fields = Object.create(null);
      for (const node of children(feature)) if (node.namespaceURI === feature.namespaceURI && children(node).length === 0) {
        if (Object.hasOwn(fields, node.localName)) fail('Mehrdeutiges WFS-Feld.');
        fields[node.localName] = node.textContent.trim();
        if (fields[node.localName].length > 20000) fail('WFS-Feld zu lang.');
      }
      if (fields.gmdschl !== profile.municipality_code) continue;
      const officialId = fields.idflurst || fields.flstkennz;
      if (!officialId || officialId.length > 500) fail('Flurstück ohne eindeutige amtliche Kennung.');
      const id = `${provider.provider_id}:${officialId}`;
      if (seen.has(id)) fail('Doppelte amtliche Flurstückkennung.');
      seen.add(id);
      const properties = Object.fromEntries(Object.entries(fieldMap).map(([key, source]) => [key, fields[source] || '']));
      Object.assign(properties, { stable_id: id, provider_id: provider.provider_id, area_value: area(fields.flaeche), area_unit: 'm²', source_url: provider.service_url, retrieved_at: now(), identification_status: 'amtliche_flurstuecksdaten' });
      features.push({ type: 'Feature', id, properties, geometry: gmlGeometry(feature, budget) });
    }
    const matched = root.getAttribute('numberMatched');
    const truncated = /^\d+$/.test(matched || '') ? Number(matched) > page * LIMIT.pageSize + members.length : members.length >= LIMIT.pageSize;
    return { type: 'FeatureCollection', features, truncated, next_page: truncated && members.length === LIMIT.pageSize && page + 1 < LIMIT.pages ? page + 1 : null, warnings: truncated ? ['Ausschnitt enthält möglicherweise weitere Flurstücke; näher heranzoomen oder nächste Seite laden.'] : [] };
  }

  async function parcels(params, signal) {
    const profile = getProfile(params.get('profile_id'));
    const provider = profile.providers.find((item) => item.provider_id === 'nrw-alkis' && item.portable && item.verification_state === 'browser_available');
    if (!provider || !agsOK(profile.municipality_code)) fail('Kein unterstützter Browser-Flurstückdienst. Manuell erfassen, GeoJSON importieren oder lokalen Server verwenden.');
    const raw = params.get('bbox') || '';
    if (!raw || raw.split(',').some((part) => !part.trim())) fail('Ungültiger Kartenausschnitt.');
    const [w, s, e, n] = bounds(raw.split(',').map(Number));
    if (e - w > .025 || n - s > .025) fail('Bitte näher heranzoomen; Flurstücke nur für kleine Ausschnitte laden.');
    const pageText = params.get('page') || '0';
    if (!/^[0-4]$/.test(pageText)) fail('Höchstens fünf Seiten je Ausschnitt.');
    const page = Number(pageText);
    const text = await fetchText('nrw-alkis', { SERVICE: 'WFS', VERSION: '2.0.0', REQUEST: 'GetFeature', TYPENAMES: 'ave:Flurstueck', SRSNAME: 'urn:ogc:def:crs:EPSG::4326', BBOX: `${s},${w},${n},${e},urn:ogc:def:crs:EPSG::4326`, COUNT: LIMIT.pageSize, STARTINDEX: page * LIMIT.pageSize }, 8 * MiB, signal);
    return parseParcels(text, provider, profile, page);
  }

  async function importGeo(content, profile, signal) {
    if (typeof content !== 'string' || bytes(content) > LIMIT.case) fail('Geometrieimport ist auf 2 MiB begrenzt.');
    if (content.trimStart().startsWith('<')) fail('GML-Dateiimport in dieser portablen Fassung nicht unterstützt. Den lokalen Server verwenden oder nach WGS84-GeoJSON konvertieren.');
    let raw;
    try { raw = JSON.parse(content); } catch { fail('Keine gültige GeoJSON-Datei.'); }
    boundedJSON(raw);
    if (!record(raw) || Object.hasOwn(raw, 'crs')) fail('GeoJSON nur in WGS84 ohne CRS-Angabe importieren.');
    const source = raw.type === 'FeatureCollection' ? raw.features : [raw];
    if (!Array.isArray(source) || !source.length || source.length > LIMIT.parcels) fail('Import muss zwischen 1 und 200 Flurstücken enthalten.');
    const budget = { count: 0 }, seen = new Set(), features = [];
    for (const feature of source) {
      checkSignal(signal);
      if (!record(feature) || feature.type !== 'Feature' || Object.hasOwn(feature, 'crs')) fail('WGS84-GeoJSON-Feature erforderlich.');
      if (!record(feature.geometry) || Object.hasOwn(feature.geometry, 'crs')) fail('GeoJSON-Geometrie nur in WGS84 ohne CRS-Angabe importieren.');
      const shape = geometry({ type: feature.geometry.type, coordinates: feature.geometry.coordinates }, budget);
      const props = feature.properties == null ? {} : feature.properties;
      if (!record(props)) fail('GeoJSON-properties muss ein Objekt sein.');
      const properties = {};
      for (const key of ['district_name', 'district_code', 'flur', 'numerator', 'denominator', 'official_parcel_reference', 'area_unit', 'location_text', 'source_date']) {
        if (props[key] != null && !['string', 'number'].includes(typeof props[key])) fail(`Ungültige Importangabe: ${key}.`);
        properties[key] = props[key] == null ? '' : String(props[key]).slice(0, 500);
      }
      const digest = await crypto.subtle.digest('SHA-256', new TextEncoder().encode(JSON.stringify(shape)));
      const id = 'import:' + Array.from(new Uint8Array(digest), (byte) => byte.toString(16).padStart(2, '0')).join('').slice(0, 20);
      if (seen.has(id)) fail('Doppelte Geometrie im Import.');
      seen.add(id);
      Object.assign(properties, { area_value: area(props.area_value), stable_id: id, provider_id: 'import', municipality: profile.name || '', municipality_code: profile.municipality_code || '', source_url: '', retrieved_at: now(), identification_status: 'manuell_ergaenzt' });
      features.push({ type: 'Feature', id, geometry: shape, properties });
    }
    return { type: 'FeatureCollection', features, truncated: false, next_page: null, warnings: ['Importierte Angaben sind nicht amtlich verifiziert. Gemeindezuordnung und Flurstückkennzeichen prüfen.'] };
  }

  function normalizeCase(raw, imported) {
    boundedJSON(raw);
    if (!record(raw) || Object.keys(raw).some((key) => ![...CASE_TEXT, 'profile', 'selected_parcels', 'recipients'].includes(key))) fail('Vorgang enthält nicht erlaubte Felder.');
    const result = texts(raw, CASE_TEXT), budget = { count: 0 }, seen = new Set();
    result.recipients = texts(raw.recipients || {}, ['kataster', 'grundbuch', 'notar']);
    if (raw.profile != null) {
      const saved = profiles.get(raw.profile.profile_id);
      result.profile = !imported && saved && saved.municipality_code === raw.profile.municipality_code ? clone(saved) : sanitizeProfile(raw.profile);
    } else result.profile = null;
    result.selected_parcels = list(raw.selected_parcels, LIMIT.parcels).map((item) => {
      if (!record(item) || Object.keys(item).some((key) => ![...PARCEL_TEXT, 'area_value', 'geometry', 'grundbuchblaetter'].includes(key))) fail('Flurstück enthält nicht erlaubte Felder.');
      const parcel = texts(item, PARCEL_TEXT);
      parcel.geometry = item.geometry == null ? null : geometry(item.geometry, budget, true);
      parcel.area_value = area(item.area_value);
      if (item.grundbuchblaetter !== undefined) parcel.grundbuchblaetter = stringList(item.grundbuchblaetter, 50);
      if (parcel.stable_id) {
        const id = JSON.stringify([parcel.provider_id, parcel.stable_id]);
        if (seen.has(id)) fail('Eine Auswahl-ID ist doppelt vorhanden.');
        seen.add(id);
      }
      if (parcel.geometry?.type === 'Point' || parcel.identification_status === 'location_hint') parcel.identification_status = 'location_hint';
      else if (imported) parcel.identification_status = 'manuell_ergaenzt';
      return parcel;
    });
    return imported && typeof window.PortableDocuments?.validate === 'function' ? window.PortableDocuments.validate(result) : result;
  }

  async function documentRequest(path, body, signal) {
    const engine = window.PortableDocuments;
    if (!engine) fail('Lokales Dokumentmodul fehlt. ZIP vollständig entpacken und erneut öffnen.');
    const data = normalizeCase(body.case, false);
    // The flag is a UI activation capability, not part of the saved document schema.
    for (const item of data.profile?.providers || []) delete item.portable;
    if (path === '/api/documents') {
      if (typeof engine.build !== 'function') fail('Lokaler Dokumentgenerator nicht verfügbar.');
      const documents = await engine.build(data);
      checkSignal(signal);
      return { documents, warnings: data.profile?.warnings || [] };
    }
    if (!['docx', 'html', 'zip', 'json'].includes(body.format)) fail('Nicht unterstütztes Exportformat.');
    if (typeof engine.export !== 'function') fail('Lokaler Dokumentexport nicht verfügbar.');
    const blob = await engine.export(data, body.format, body.document_id);
    checkSignal(signal);
    if (!(blob instanceof Blob)) fail('Dokumentexport lieferte keine Datei.');
    return blob;
  }

  async function boundedDocumentRequest(path, body, signal) {
    let timer, rejectAbort;
    const stopped = new Promise((_, reject) => { rejectAbort = reject; });
    const onAbort = () => rejectAbort(abort());
    checkSignal(signal);
    signal?.addEventListener('abort', onAbort, { once: true });
    timer = setTimeout(() => rejectAbort(new Error('Zeitbudget der lokalen Dokumenterstellung erreicht. Auswahl verkleinern und erneut versuchen.')), 30000);
    try {
      return await Promise.race([documentRequest(path, body, signal), stopped]);
    } finally {
      clearTimeout(timer); signal?.removeEventListener('abort', onAbort);
    }
  }

  async function request(path, { body, signal, binary = false } = {}) {
    checkSignal(signal);
    if (typeof path !== 'string' || path.length > 4096 || !/^\/api\/[a-z-]+(?:\?[^#]*)?$/.test(path)) fail('Unzulässiger portabler API-Pfad.');
    const url = new URL(path, 'https://portable.invalid');
    if (binary && url.pathname !== '/api/export') fail('Binärdaten nur beim Dokumentexport.');
    if (body !== undefined) {
      if (!record(body)) fail('JSON-Anfrage erforderlich.');
      boundedJSON(body, 3 * MiB, 2 * MiB);
    }
    let result;
    switch (url.pathname) {
      case '/api/config': result = { csrf_token: 'portable-local-no-server', max_parcels: LIMIT.parcels, min_parcel_zoom: 17, portable: true }; break;
      case '/api/places': result = await searchPlaces(url.searchParams.get('q'), signal); break;
      case '/api/setup': result = await setup(body?.place, signal); break;
      case '/api/example': result = example(); break;
      case '/api/import': result = { case: normalizeCase(body?.case, true) }; break;
      case '/api/import-geo': result = await importGeo(body?.content, getProfile(body?.profile_id), signal); break;
      case '/api/parcels': result = await parcels(url.searchParams, signal); break;
      case '/api/address': fail('Adresssuche ist in der portablen Fassung nicht eingerichtet. Karte/Lagehinweis oder lokalen Server verwenden; es werden keine Adressen an Drittanbieter gesendet.'); break;
      case '/api/documents': case '/api/export': result = await boundedDocumentRequest(url.pathname, body || {}, signal); break;
      default: fail('Portable Schnittstelle nicht vorhanden.');
    }
    checkSignal(signal);
    return result;
  }

  async function preparedCase() {
    const included = window.PORTABLE_BUNDLE.case;
    if (included) {
      const data = normalizeCase(included, true);
      if (!data.profile && !prepared) fail('Beigefügter Vorgang enthält keinen Ort.');
      const matching = prepared && (!data.profile || (agsOK(prepared.municipality_code) && data.profile.municipality_code === prepared.municipality_code));
      data.profile = profileFor(matching ? { ...data.profile, ...prepared } : data.profile || prepared, !!matching);
      return data;
    }
    if (!prepared) fail('Kein vorbereitetes Ortsprofil in diesem Paket.');
    return { profile: profileFor(prepared, true), selected_parcels: [], recipients: {} };
  }

  window.PortableApp = Object.freeze({ request, mapURL, prepared: preparedCase });
})();
