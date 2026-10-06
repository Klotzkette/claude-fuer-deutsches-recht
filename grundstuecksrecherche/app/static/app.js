/* global L */
'use strict';

(() => {
  const $ = (id) => document.getElementById(id);
  const STORAGE_KEY = 'grundstuecksrecherche.case.v1';
  const FIELDS = ['case_id', 'purpose', 'specific_interest', 'requested_information_scope', 'sender_organisation', 'sender_address', 'contact_person', 'legal_department_contact', 'attachments'];
  const RECIPIENTS = ['kataster', 'grundbuch', 'notar'];
  const PARCEL_FIELDS = ['municipality', 'municipality_code', 'district_name', 'district_code', 'flur', 'numerator', 'denominator', 'official_parcel_reference', 'area_value', 'area_unit', 'location_text', 'source_url', 'source_date'];
  const PROPERTY_FIELDS = ['stable_id', 'provider_id', ...PARCEL_FIELDS, 'retrieved_at', 'identification_status', 'grundbuchblatt', 'grundbuchbezirk', 'grundbuchblatt_source', 'grundbuchblatt_date'];
  const state = { profile: null, selected: new Map(), available: new Map(), providers: new Map(), created: '', updated: '', dirty: false, revision: 0, changing: false, documents: [], documentCase: null, activeDocument: 0, nextPage: null, bbox: '', mapEpoch: 0 };
  const requests = new Map();
  let csrfToken = '', map, availableLayer, selectedLayer, baseLayer, pointGeometry = null;
  let parcelTimer, placeTimer, addressTimer, manualSequence = 0, documentReady = false;

  function node(tag, text, className) {
    const element = document.createElement(tag);
    if (text !== undefined && text !== null) element.textContent = String(text);
    if (className) element.className = className;
    return element;
  }
  function textValue(value) { return value == null ? '' : typeof value === 'object' ? JSON.stringify(value) : String(value); }
  function statusLabel(value) {
    return ({ verifiziert: 'Geprüft', amtlich_verifiziert: 'Amtliche Quelle geprüft', amtliche_flurstuecksdaten: 'Amtliche Flurstücksdaten', gefunden_ungeprueft: 'Gefunden, noch ungeprüft', eingeschraenkt: 'Eingeschränkt', nicht_verfuegbar: 'Nicht verfügbar', manuell_ergaenzt: 'Manuell ergänzt', manual_unverified: 'Manuell erfasst, ungeprüft', unverified: 'Ungeprüft', location_hint: 'Lagehinweis, kein Flurstücksnachweis', zu_pruefen: 'Noch zu prüfen', offen: 'Offen' })[value] || textValue(value);
  }
  function escapeHTML(value) { return textValue(value).replace(/[&<>"']/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' })[c]); }
  function safeURL(value) {
    try { const url = new URL(value); return ['http:', 'https:'].includes(url.protocol) ? url.href : null; } catch { return null; }
  }
  function link(value, title = 'Quelle öffnen') {
    const url = safeURL(value);
    if (!url) return node('span', value || 'Keine Quellen-URL', 'muted');
    const a = node('a', title); a.href = url; a.target = '_blank'; a.rel = 'noopener noreferrer'; return a;
  }
  function notice(message, kind = 'info') { $('notice').textContent = message; $('notice').dataset.kind = kind; $('notice').hidden = !message; }
  function mapStatus(message, error = false) { $('map-status').textContent = message; $('map-status').parentElement.dataset.kind = error ? 'error' : 'info'; }
  function warningList(container, values) {
    container.replaceChildren();
    for (const value of Array.isArray(values) ? values : []) container.append(node('p', textValue(value), 'warning'));
  }
  function cancel(slot) { requests.get(slot)?.controller.abort(); requests.delete(slot); }
  function abortError() { return new DOMException('Anfrage ersetzt.', 'AbortError'); }
  function isAbort(error) { return error?.name === 'AbortError'; }
  async function api(slot, path, { body, binary = false, timeout = 25000 } = {}) {
    cancel(slot);
    const controller = new AbortController();
    const request = { controller, timedOut: false };
    requests.set(slot, request);
    const timer = setTimeout(() => { request.timedOut = true; controller.abort(); }, timeout);
    try {
      if (body !== undefined && !csrfToken) throw new Error('Lokale Verbindung nicht bereit. Bitte Seite neu laden.');
      const response = await fetch(path, {
        method: body === undefined ? 'GET' : 'POST', credentials: 'same-origin', mode: 'same-origin', signal: controller.signal,
        headers: body === undefined ? { Accept: 'application/json' } : { 'Content-Type': 'application/json', 'X-Local-Token': csrfToken },
        ...(body === undefined ? {} : { body: JSON.stringify(body) })
      });
      if (!response.ok) {
        const detail = await response.json().catch(() => null);
        throw new Error(textValue(detail?.message || detail?.error || detail?.detail) || `Anfrage fehlgeschlagen (HTTP ${response.status}).`);
      }
      const result = binary ? await response.blob() : await response.json();
      if (controller.signal.aborted || requests.get(slot) !== request) throw abortError();
      return result;
    } catch (error) {
      if (request.timedOut) throw new Error('Zeitüberschreitung beim Dienst. Bitte erneut versuchen.');
      if (controller.signal.aborted || requests.get(slot) !== request) throw abortError();
      throw error;
    } finally {
      clearTimeout(timer);
      if (requests.get(slot) === request) requests.delete(slot);
    }
  }
  function query(path, values) { return `${path}?${new URLSearchParams(values)}`; }
  function validCenter(value) { return Array.isArray(value) && value.length >= 2 && Number.isFinite(value[0]) && Number.isFinite(value[1]) && Math.abs(value[0]) <= 90 && Math.abs(value[1]) <= 180; }
  function validBounds(value) { return Array.isArray(value) && value.length === 4 && value.every(Number.isFinite) && value[0] < value[2] && value[1] < value[3] && value[0] >= -180 && value[2] <= 180 && value[1] >= -90 && value[3] <= 90; }
  function validGeometry(geometry) {
    if (!geometry || !['Polygon', 'MultiPolygon', 'Point'].includes(geometry.type)) return null;
    const position = (p) => Array.isArray(p) && p.length >= 2 && Number.isFinite(p[0]) && Number.isFinite(p[1]) && Math.abs(p[0]) <= 180 && Math.abs(p[1]) <= 90;
    const ring = (r) => Array.isArray(r) && r.length >= 4 && r.every(position) && r[0][0] === r.at(-1)[0] && r[0][1] === r.at(-1)[1];
    const polygon = (p) => Array.isArray(p) && p.length > 0 && p.every(ring);
    const valid = geometry.type === 'Point' ? position(geometry.coordinates) : geometry.type === 'Polygon' ? polygon(geometry.coordinates) : Array.isArray(geometry.coordinates) && geometry.coordinates.length > 0 && geometry.coordinates.every(polygon);
    return valid ? structuredClone(geometry) : null;
  }
  function normalizeParcel(properties, geometry) {
    const parcel = {};
    for (const field of PROPERTY_FIELDS) parcel[field] = ['string', 'number'].includes(typeof properties?.[field]) ? String(properties[field]) : '';
    parcel.area_value = properties?.area_value === '' || properties?.area_value == null ? null : Number(properties.area_value);
    if (!Number.isFinite(parcel.area_value) || parcel.area_value < 0) parcel.area_value = null;
    if (Array.isArray(properties?.grundbuchblaetter)) parcel.grundbuchblaetter = properties.grundbuchblaetter.filter((value) => typeof value === 'string');
    parcel.geometry = validGeometry(geometry);
    if (parcel.geometry?.type === 'Point') parcel.identification_status = 'location_hint';
    if (!parcel.identification_status) parcel.identification_status = 'unverified';
    return parcel;
  }
  function parcelKey(parcel) {
    if (parcel.stable_id) return JSON.stringify(['stable', parcel.provider_id, parcel.stable_id]);
    if (parcel.official_parcel_reference) return JSON.stringify(['reference', parcel.municipality_code || parcel.municipality, parcel.official_parcel_reference]);
    // This key is browser-only and never becomes an official parcel identifier.
    return `local-${++manualSequence}`;
  }
  function parcelTitle(parcel) {
    if (parcel.identification_status === 'location_hint') return 'Lagehinweis · kein Flurstücksnachweis';
    const number = textValue(parcel.numerator) + (parcel.denominator ? `/${parcel.denominator}` : '');
    return [parcel.district_name, parcel.flur ? `Flur ${parcel.flur}` : '', number ? `Flurstück ${number}` : parcel.official_parcel_reference || 'Flurstück (Angaben unvollständig)'].filter(Boolean).join(' · ');
  }
  function collectCase() {
    return { ...Object.fromEntries(FIELDS.map((field) => [field, $(field).value])), profile: state.profile,
      selected_parcels: [...state.selected.values()], recipients: Object.fromEntries(RECIPIENTS.map((role) => [role, $(`recipient-${role}`).value])),
      created_at: state.created, updated_at: state.updated };
  }
  function touch() {
    state.updated = new Date().toISOString(); state.dirty = true; state.revision += 1;
    state.documents = []; state.documentCase = null;
    $('save-status').textContent = 'Ungespeicherte Änderungen.';
    syncControls();
  }
  function syncControls() {
    const enabled = !!state.profile && !state.changing;
    $('case-fields').disabled = !enabled;
    for (const id of ['manual-parcel', 'import-geo', 'save-case', 'download-case', 'refresh-profile']) $(id).disabled = !enabled;
    $('clear-selection').disabled = !enabled || !state.selected.size;
    $('generate-documents').disabled = !enabled || !state.selected.size || !csrfToken;
    $('new-case').disabled = state.changing;
    $('example').disabled = state.changing || !csrfToken;
    $('change-place').disabled = state.changing;
    $('place-form').querySelector('button').disabled = state.changing;
    $('change-place').hidden = !state.profile;
    $('cancel-place').hidden = !state.profile;
  }
  function confirmReplace() { return !state.profile || window.confirm('Neuen Vorgang beginnen? Der aktuelle Vorgang wird ersetzt. Ungespeicherte Angaben gehen verloren.'); }
  function resetMap() {
    clearTimeout(parcelTimer); clearTimeout(addressTimer); cancel('parcels'); cancel('address'); cancel('documents'); cancel('geo'); cancel('export');
    state.mapEpoch += 1; state.available.clear(); state.providers.clear(); state.nextPage = null; state.bbox = '';
    map?.remove(); map = null; availableLayer = null; selectedLayer = null; baseLayer = null;
    $('map').replaceChildren(); $('map-toolbar').hidden = true;
    $('address-query').value = ''; $('address-results').replaceChildren(); $('address-results').hidden = true;
    $('pick-mode').checked = false; $('parcels-visible').checked = true; $('map').classList.remove('pick-mode');
    $('more-parcels').hidden = true; $('reload-parcels').hidden = true;
    $('provider-status').replaceChildren(); $('profile-warnings').replaceChildren(); $('profile-evidence').replaceChildren(); $('sources').classList.remove('has-error');
    mapStatus('Noch keine Karte geladen.');
  }
  function clearForm() {
    for (const field of FIELDS) $(field).value = '';
    for (const role of RECIPIENTS) $(`recipient-${role}`).value = '';
    $('authorities').replaceChildren();
  }
  function blankCase() {
    resetMap(); clearForm(); state.profile = null; state.selected.clear(); state.documents = []; state.documentCase = null;
    state.created = ''; state.updated = ''; state.dirty = false; state.revision += 1;
    $('place-name').textContent = 'Kein Ort ausgewählt'; $('place-panel').hidden = false; $('place-query').value = '';
    $('place-results').replaceChildren(); $('place-status').textContent = ''; $('save-status').textContent = 'Noch nicht gespeichert.';
    renderSelection(); syncControls(); $('place-query').focus();
  }
  function applyCase(data) {
    if (!data?.profile?.profile_id || !validCenter(data.profile.center)) throw new Error('Das Ortsprofil enthält keine gültige Kartenposition oder Profil-ID.');
    resetMap(); clearForm(); state.profile = data.profile; state.selected.clear();
    state.created = data.created_at || new Date().toISOString(); state.updated = data.updated_at || state.created;
    for (const field of FIELDS) {
      if (field === 'requested_information_scope' && data[field] && ![...$(field).options].some((option) => option.value === data[field])) {
        const option = node('option', textValue(data[field])); option.value = textValue(data[field]); $(field).append(option);
      }
      $(field).value = textValue(data[field]);
    }
    for (const role of RECIPIENTS) $(`recipient-${role}`).value = textValue(data.recipients?.[role]);
    for (const item of Array.isArray(data.selected_parcels) ? data.selected_parcels : []) {
      const parcel = normalizeParcel(item, item.geometry); state.selected.set(parcelKey(parcel), parcel);
    }
    $('place-name').textContent = [data.profile.name, data.profile.state].filter(Boolean).join(' · ');
    $('place-panel').hidden = true; $('place-results').replaceChildren(); $('place-status').textContent = '';
    renderAuthorities(); renderSources(); initMap(); renderSelection(); touch();
  }
  async function changeCase(loader, setup = false, replace = true) {
    if (state.changing || (replace && !confirmReplace())) return;
    state.changing = true; syncControls(); $('place-status').textContent = 'Ortsprofil wird vorbereitet …';
    try {
      const result = await loader();
      const data = setup ? { profile: result.profile, selected_parcels: [], recipients: {} } : result.case || result;
      if (setup) for (const authority of data.profile?.authorities || []) {
        if (RECIPIENTS.includes(authority.authority_type)) data.recipients[authority.authority_type] = [authority.official_name, textValue(authority.postal_address)].filter(Boolean).join('\n');
      }
      applyCase(data); notice('');
    } catch (error) { if (!isAbort(error)) { notice(error.message, 'error'); $('place-status').textContent = error.message; } }
    finally { state.changing = false; syncControls(); }
  }
  async function revalidateCase(data) {
    const normalized = await api('case', '/api/import', { body: { case: data }, timeout: 60000 });
    const imported = normalized.case || normalized;
    try {
      const result = await api('case', '/api/setup', { body: { place: imported.profile }, timeout: 60000 });
      return { ...imported, profile: result.profile };
    } catch (error) {
      if (isAbort(error) || !validCenter(imported.profile?.center)) throw error;
      imported.profile.profile_id ||= `offline-${Date.now()}`;
      imported.profile.verification_state = 'gefunden_ungeprueft';
      for (const provider of imported.profile.providers || []) provider.verification_state = 'gefunden_ungeprueft';
      for (const authority of imported.profile.authorities || []) authority.verification_state = 'gefunden_ungeprueft';
      (imported.profile.warnings ||= []).push(`Vorgang ohne aktuelle Quellenprüfung geöffnet: ${error.message} Auswahl und Dokumentenbearbeitung bleiben verfügbar. Quellen vor Verwendung erneut prüfen.`);
      return imported;
    }
  }

  async function searchPlaces() {
    clearTimeout(placeTimer); cancel('places');
    const q = $('place-query').value.trim(); $('place-results').replaceChildren();
    if (q.length < 2) { $('place-status').textContent = 'Mindestens zwei Zeichen eingeben.'; return; }
    $('place-status').textContent = 'Orte werden gesucht …';
    try {
      const result = await api('places', query('/api/places', { q }));
      const candidates = (result.candidates || []).filter((item) => validCenter(item.center));
      $('place-status').textContent = candidates.length ? `${candidates.length} Ort${candidates.length === 1 ? '' : 'e'} gefunden.` : 'Kein passender Ort gefunden.';
      for (const candidate of candidates) {
        const button = node('button'); button.type = 'button';
        button.append(node('strong', candidate.name), node('small', [candidate.district, candidate.state, candidate.municipality_code, statusLabel(candidate.verification_state)].filter(Boolean).join(' · ')));
        button.addEventListener('click', () => changeCase(() => api('case', '/api/setup', { body: { place: candidate }, timeout: 60000 }), true));
        $('place-results').append(button);
      }
    } catch (error) { if (!isAbort(error)) $('place-status').textContent = error.message; }
  }
  async function searchAddresses() {
    clearTimeout(addressTimer); cancel('address'); $('address-results').replaceChildren(); $('address-results').hidden = true;
    const q = $('address-query').value.trim(); if (!state.profile || q.length < 3) return;
    try {
      const result = await api('address', query('/api/address', { profile_id: state.profile.profile_id, q }));
      const candidates = (result.candidates || []).filter((candidate) => validCenter(candidate.center));
      $('address-results').hidden = false;
      if (!candidates.length) $('address-results').append(node('p', 'Keine passende Adresse gefunden.', 'muted'));
      for (const candidate of candidates) {
        const button = node('button', candidate.label); button.type = 'button';
        button.addEventListener('click', () => { map?.setView(candidate.center, 18); $('address-results').hidden = true; $('address-query').value = candidate.label; });
        $('address-results').append(button);
      }
    } catch (error) { if (!isAbort(error)) { $('address-results').hidden = false; $('address-results').append(node('p', error.message, 'error')); } }
  }

  function renderSources() {
    $('provider-status').replaceChildren();
    for (const provider of state.profile?.providers || []) {
      const item = node('li'); item.append(node('strong', provider.title || provider.provider_id));
      item.append(node('p', [provider.protocol, statusLabel(provider.verification_state), textValue(provider.test_result)].filter(Boolean).join(' · ')));
      item.append(node('p', [textValue(provider.attribution), textValue(provider.license)].filter(Boolean).join(' · ')));
      item.append(link(provider.service_url, 'Dienstquelle'));
      const status = node('p', '', 'provider-live-status'); item.append(status);
      $('provider-status').append(item); state.providers.set(provider.provider_id, { provider, status, layer: null });
    }
    if (!state.providers.size) $('provider-status').append(node('li', 'Keine Kartendienste im Ortsprofil.', 'error'));
    warningList($('profile-warnings'), state.profile?.warnings);
    const evidence = Array.isArray(state.profile?.evidence) ? state.profile.evidence : [];
    for (const entry of evidence) {
      const item = node('p');
      if (typeof entry === 'string') item.append(safeURL(entry) ? link(entry, entry) : node('span', entry));
      else { item.append(node('span', [entry.title || entry.description, entry.verification_state].filter(Boolean).join(' · ') + ' ')); if (entry.url || entry.source_url) item.append(link(entry.url || entry.source_url)); }
      $('profile-evidence').append(item);
    }
  }
  function renderAuthorities() {
    $('authorities').replaceChildren();
    for (const authority of state.profile?.authorities || []) {
      const section = node('section', null, 'authority');
      section.append(node('h3', authority.official_name || authority.authority_type));
      section.append(node('p', `Prüfstatus: ${statusLabel(authority.verification_state) || 'Offen'}${authority.verified_at ? ` · ${authority.verified_at}` : ''}`));
      if (authority.visitor_address) section.append(node('p', `Besucheranschrift: ${textValue(authority.visitor_address)}`));
      if (authority.submission_information) section.append(node('p', textValue(authority.submission_information)));
      for (const url of authority.evidence_urls || []) { section.append(link(url), document.createTextNode(' ')); }
      $('authorities').append(section);
    }
    if (!(state.profile?.authorities || []).length) $('authorities').append(node('p', 'Zuständige Stellen noch nicht verifiziert.', 'warning'));
  }
  function providerStatus(id, message, error = false) {
    const entry = state.providers.get(id); if (!entry) return;
    entry.status.textContent = message; entry.status.classList.toggle('provider-error', error);
    if (error) { $('sources').classList.add('has-error'); notice(`${entry.provider.title || id}: ${message}`, 'error'); }
  }
  function fitPlace() {
    if (!map || !state.profile) return;
    // Cadastral base maps can be scale-limited; retain bounds as metadata, not as the initial zoom.
    map.setView(state.profile.center, 17);
  }
  function initMap() {
    if (!window.L) { mapStatus('Leaflet fehlt unter /vendor/. Formulare und manuelle Erfassung bleiben verfügbar.', true); return; }
    try {
      map = L.map('map', { maxZoom: 22, minZoom: 3, zoomControl: true });
      map.createPane('selection'); map.getPane('selection').style.zIndex = '450';
      availableLayer = L.layerGroup().addTo(map); selectedLayer = L.layerGroup().addTo(map);
      map.attributionControl.setPrefix(false);
      $('map-toolbar').hidden = false; $('base-layer').replaceChildren();
      const blank = node('option', 'Ohne Kartenbild'); blank.value = ''; $('base-layer').append(blank);
      for (const [id, entry] of state.providers) {
        const provider = entry.provider;
        if (provider.verification_state !== 'verifiziert') {
          providerStatus(id, 'Nicht freigegeben. Es werden keine Daten von diesem Dienst geladen.');
          continue;
        }
        if (!/wms/i.test(provider.protocol || '')) {
          providerStatus(id, provider.role === 'parcels' ? 'Flurstücke über den Geodatendienst.' : 'Dieses Kartenprotokoll wird nicht unterstützt.', provider.role !== 'parcels');
          continue;
        }
        const url = query('/api/map', { profile_id: state.profile.profile_id, provider_id: id });
        const minimumZoom = id === 'nrw-abk' || /wms_nw_abk/.test(provider.service_url || '') ? 17 : 3;
        const layer = L.tileLayer.wms(url, { layers: Array.isArray(provider.layers) ? provider.layers.join(',') : provider.layers || '', format: provider.format || 'image/png', transparent: provider.role === 'parcels', version: '1.3.0', crs: L.CRS.EPSG3857, tileSize: 256, minZoom: minimumZoom, maxZoom: 22, zIndex: provider.role === 'parcels' ? 200 : 100, attribution: escapeHTML(provider.attribution || provider.title || '') });
        entry.layer = layer;
        let tileFailures = 0;
        layer.on('loading', () => { tileFailures = 0; providerStatus(id, 'Kartenkacheln werden geladen …'); });
        layer.on('tileerror', () => { tileFailures += 1; providerStatus(id, 'Kartenkacheln konnten nicht geladen werden.', true); });
        layer.on('load', () => { if (!tileFailures) providerStatus(id, 'Kartenkacheln geladen.'); });
        if (provider.role === 'parcels') layer.addTo(map);
        else { const option = node('option', provider.title || id); option.value = id; $('base-layer').append(option); }
      }
      const preferred = [...state.providers].find(([, entry]) => entry.layer && entry.provider.role === 'base') || [...state.providers].find(([, entry]) => entry.layer && entry.provider.role === 'aerial');
      if (preferred) { $('base-layer').value = preferred[0]; baseLayer = preferred[1].layer; baseLayer.addTo(map); }
      map.on('movestart', () => { cancel('parcels'); state.mapEpoch += 1; clearTimeout(parcelTimer); state.nextPage = null; $('more-parcels').hidden = true; });
      map.on('moveend', scheduleParcels);
      map.on('zoomend', () => {
        if (!baseLayer || map.getZoom() >= baseLayer.options.minZoom) return;
        const fallback = [...state.providers].find(([, entry]) => entry.layer && entry.provider.role !== 'parcels' && entry.layer.options.minZoom <= map.getZoom());
        if (fallback) { map.removeLayer(baseLayer); baseLayer = fallback[1].layer; baseLayer.addTo(map); $('base-layer').value = fallback[0]; }
        else { map.setZoom(baseLayer.options.minZoom); notice('Das gewählte Kartenbild ist nur im Detailmaßstab verfügbar.'); }
      });
      map.on('click', (event) => { if ($('pick-mode').checked && !state.changing) openManual({ type: 'Point', coordinates: [event.latlng.lng, event.latlng.lat] }); });
      fitPlace(); map.invalidateSize(); scheduleParcels();
    } catch (error) { mapStatus(`Karte konnte nicht initialisiert werden: ${error.message}`, true); }
  }
  function scheduleParcels() {
    clearTimeout(parcelTimer); cancel('parcels'); state.mapEpoch += 1;
    state.nextPage = null; $('more-parcels').hidden = true; $('reload-parcels').hidden = true;
    availableLayer?.clearLayers(); state.available.clear(); renderAvailable();
    if (!map || !$('parcels-visible').checked) { mapStatus('Flurstücke ausgeblendet. Die Auswahl bleibt erhalten.'); return; }
    if (![...state.providers.values()].some((entry) => entry.provider.role === 'parcels' && entry.provider.verification_state === 'verifiziert' && /^WFS$/i.test(entry.provider.protocol))) {
      mapStatus('Kein geprüfter Flurstücksdienst verfügbar. Manuelle Erfassung und Geodatenimport sind möglich.', true); return;
    }
    if (map.getZoom() < 17) { mapStatus('Flurstücke ab Zoomstufe 17. Auswahl bleibt erhalten.'); $('reload-parcels').hidden = true; return; }
    mapStatus('Flurstücke werden geladen …');
    parcelTimer = setTimeout(() => loadParcels(false), 350);
  }
  async function loadParcels(more) {
    clearTimeout(parcelTimer);
    if (!map || !state.profile || !$('parcels-visible').checked || map.getZoom() < 17) return;
    const epoch = state.mapEpoch;
    const bounds = map.getBounds();
    if (bounds.getEast() - bounds.getWest() > .025 || bounds.getNorth() - bounds.getSouth() > .025) {
      mapStatus('Kartenausschnitt zu groß für den Flurstücksdienst. Bitte weiter hineinzoomen.'); return;
    }
    const bbox = more ? state.bbox : [bounds.getWest(), bounds.getSouth(), bounds.getEast(), bounds.getNorth()].join(',');
    const page = more ? state.nextPage : 0;
    if (more && (page === null || page === undefined)) return;
    $('more-parcels').disabled = true; $('reload-parcels').hidden = true; mapStatus('Flurstücke werden geladen …');
    try {
      const result = await api('parcels', query('/api/parcels', { profile_id: state.profile.profile_id, bbox, page }));
      if (epoch !== state.mapEpoch) return;
      if (result.type !== 'FeatureCollection' || !Array.isArray(result.features)) throw new Error('Geodatendienst liefert keine gültige Flurstückssammlung.');
      if (!more) state.available.clear();
      let invalid = 0;
      for (const feature of result.features) {
        const parcel = normalizeParcel(feature.properties, feature.geometry);
        if (!parcel.geometry) { invalid += 1; continue; }
        state.available.set(parcelKey(parcel), parcel);
      }
      state.bbox = bbox; state.nextPage = result.next_page ?? null;
      if (String(state.nextPage) === String(page)) state.nextPage = null;
      $('more-parcels').hidden = state.nextPage === null;
      const warnings = [...(result.warnings || [])];
      if (result.truncated) warnings.push('Ausschnitt unvollständig. Weitere laden oder näher heranzoomen.');
      if (invalid) warnings.push(`${invalid} Geometrien sind ungültig und wurden nicht angezeigt.`);
      mapStatus(`${state.available.size} Flurstücke im Ausschnitt.${warnings.length ? ' ' + warnings.map(textValue).join(' ') : ''}`, !!warnings.length);
      drawAvailable(); renderAvailable();
    } catch (error) {
      if (!isAbort(error) && epoch === state.mapEpoch) {
        mapStatus(`Flurstücksdienst: ${error.message}`, true); $('reload-parcels').hidden = false;
        for (const [id, entry] of state.providers) if (entry.provider.role === 'parcels') providerStatus(id, error.message, true);
      }
    } finally { if (epoch === state.mapEpoch) $('more-parcels').disabled = false; }
  }
  function parcelLayer(parcel, selected, onClick) {
    return L.geoJSON({ type: 'Feature', properties: {}, geometry: parcel.geometry }, {
      pane: selected ? 'selection' : 'overlayPane',
      style: { color: selected ? '#17663e' : '#286e9f', weight: selected ? 3 : 1.5, fillColor: selected ? '#4ca774' : '#368dbd', fillOpacity: selected ? .24 : .04 },
      pointToLayer: (_, latlng) => L.circleMarker(latlng, { pane: selected ? 'selection' : 'overlayPane', radius: 7, color: '#95621a', fillColor: '#edbd63', fillOpacity: .7, dashArray: '4 3' }),
      onEachFeature: (_, layer) => { layer.bindTooltip(node('span', parcelTitle(parcel))); layer.on('click', (event) => { if (event.originalEvent) L.DomEvent.stopPropagation(event.originalEvent); if (!$('pick-mode').checked) onClick(); }); }
    });
  }
  function drawAvailable() {
    if (!availableLayer) return;
    availableLayer.clearLayers();
    for (const [key, parcel] of state.available) if (!state.selected.has(key)) parcelLayer(parcel, false, () => toggleParcel(key, parcel)).addTo(availableLayer);
  }
  function renderAvailable() {
    $('available-list').replaceChildren(); $('available-count').textContent = state.available.size; $('available-section').hidden = !state.available.size;
    for (const [key, parcel] of state.available) {
      const button = node('button', parcelTitle(parcel)); button.type = 'button'; button.setAttribute('aria-pressed', String(state.selected.has(key)));
      button.addEventListener('click', () => toggleParcel(key, parcel)); $('available-list').append(button);
    }
  }
  function toggleParcel(key, parcel) {
    if (state.changing) return;
    if (state.selected.has(key)) state.selected.delete(key);
    else if (state.selected.size >= 200) { notice('Die Auswahl ist auf 200 Objekte begrenzt.', 'error'); return; }
    else state.selected.set(key, parcel);
    touch(); renderSelection();
  }
  function renderSelection() {
    $('selection-count').textContent = state.selected.size; $('selection-empty').hidden = !!state.selected.size; $('selection-list').replaceChildren(); selectedLayer?.clearLayers();
    for (const [key, parcel] of state.selected) {
      const item = node('li', null, `parcel${parcel.identification_status === 'location_hint' ? ' location-hint' : ''}`);
      const title = parcelTitle(parcel); item.append(node('strong', title));
      const remove = node('button', '×', 'icon-button remove'); remove.type = 'button'; remove.title = 'Aus Auswahl entfernen'; remove.setAttribute('aria-label', `${title} entfernen`);
      remove.addEventListener('click', () => toggleParcel(key, parcel)); item.append(remove);
      item.append(node('span', [parcel.location_text, parcel.area_value != null ? `${parcel.area_value} ${parcel.area_unit || '(Einheit offen)'}` : ''].filter(Boolean).join(' · '), 'muted'));
      item.append(node('span', `Identifikation: ${statusLabel(parcel.identification_status)}`, 'muted'));
      const details = node('details'); details.append(node('summary', 'Identifikation und Quelle')); const list = node('dl');
      for (const [label, value] of [['Kennzeichen', parcel.official_parcel_reference], ['Quellen-ID', parcel.stable_id], ['Gemeindeschlüssel', parcel.municipality_code], ['Gemarkungsschlüssel', parcel.district_code], ['Datenstand', parcel.source_date], ['Abruf', parcel.retrieved_at]]) {
        list.append(node('dt', label), node('dd', value || 'Nicht belegt'));
      }
      details.append(list); if (parcel.source_url) details.append(link(parcel.source_url)); item.append(details);
      if (parcel.geometry && selectedLayer) {
        const layer = parcelLayer(parcel, true, () => toggleParcel(key, parcel)).addTo(selectedLayer);
        const locate = node('button', 'Auf Karte anzeigen', 'locate'); locate.type = 'button';
        locate.addEventListener('click', () => { map.fitBounds(layer.getBounds(), { maxZoom: 19, padding: [30, 30] }); if (matchMedia('(max-width: 760px)').matches) $('map').scrollIntoView({ block: 'center' }); });
        item.append(locate);
      }
      $('selection-list').append(item);
    }
    drawAvailable(); renderAvailable(); syncControls();
  }
  function openManual(geometry = null) {
    if (!state.profile || state.changing) return;
    pointGeometry = geometry; $('parcel-form').reset(); $('parcel-error').hidden = true;
    $('parcel-municipality').value = state.profile.name || ''; $('parcel-municipality_code').value = state.profile.municipality_code || '';
    $('parcel-dialog-title').textContent = geometry ? 'Lagehinweis erfassen' : 'Flurstück manuell erfassen';
    $('parcel-note').textContent = geometry ? 'Nur ein Kartenpunkt, kein amtlicher Flurstücksnachweis. Kennzeichen werden nicht aus der Position abgeleitet.' : 'Manuelle Angabe, nicht amtlich verifiziert. Unbekannte Kennzeichen bleiben leer.';
    if (geometry) $('parcel-location_text').value = `Kartenpunkt: ${geometry.coordinates[1].toFixed(6)}, ${geometry.coordinates[0].toFixed(6)}`;
    $('parcel-dialog').showModal();
  }
  function submitManual(event) {
    event.preventDefault();
    const values = Object.fromEntries(PARCEL_FIELDS.map((field) => [field, $(`parcel-${field}`).value.trim() || null]));
    if (!pointGeometry && !values.numerator && !values.official_parcel_reference) {
      $('parcel-error').textContent = 'Bitte eine belegte Flurstücksnummer oder ein amtliches Kennzeichen angeben. Für eine bloße Position einen Lagehinweis auf der Karte setzen.'; $('parcel-error').hidden = false; return;
    }
    if (values.source_url && !safeURL(values.source_url)) { $('parcel-error').textContent = 'Die Quellen-URL muss mit https:// oder http:// beginnen.'; $('parcel-error').hidden = false; return; }
    const parcel = normalizeParcel({ ...values, area_value: values.area_value === null ? null : Number(values.area_value), identification_status: pointGeometry ? 'location_hint' : 'manual_unverified' }, pointGeometry);
    const key = parcelKey(parcel);
    if (!state.selected.has(key) && state.selected.size >= 200) { $('parcel-error').textContent = 'Die Auswahl ist auf 200 Objekte begrenzt.'; $('parcel-error').hidden = false; return; }
    state.selected.set(key, parcel); touch(); renderSelection(); $('parcel-dialog').close();
    $('pick-mode').checked = false; $('map').classList.remove('pick-mode');
  }

  function storageAvailable() {
    try { const exists = !!localStorage.getItem(STORAGE_KEY); $('restore-case').disabled = !exists; $('forget-case').disabled = !exists; }
    catch { $('restore-case').disabled = true; $('forget-case').disabled = true; }
  }
  function download(blob, filename) {
    const url = URL.createObjectURL(blob); const a = node('a'); a.href = url; a.download = filename; a.hidden = true; document.body.append(a); a.click(); a.remove(); setTimeout(() => URL.revokeObjectURL(url), 30000);
  }
  async function importFile(input, geo = false) {
    const file = input.files?.[0]; if (!file) return;
    const revision = state.revision;
    try {
      if (file.size > 2 * 1024 * 1024) throw new Error('Die Datei überschreitet die Importgrenze von 2 MB.');
      const content = await file.text();
      if (revision !== state.revision) throw new Error('Vorgang zwischenzeitlich geändert. Datei bitte erneut auswählen.');
      if (geo) {
        if (!state.profile || state.changing) throw new Error('Zuerst einen Ort auswählen.');
        const result = await api('geo', '/api/import-geo', { body: { profile_id: state.profile.profile_id, content }, timeout: 60000 });
        if (revision !== state.revision) throw new Error('Vorgang zwischenzeitlich geändert. Geodaten bitte erneut importieren.');
        if (result.type !== 'FeatureCollection' || !Array.isArray(result.features)) throw new Error('Import liefert keine gültige Geodatensammlung.');
        if (result.features.length > 200) throw new Error('Ein Import darf höchstens 200 Objekte enthalten.');
        let count = 0; const imported = new Map(state.selected);
        for (const feature of result.features) {
          const parcel = normalizeParcel(feature.properties, feature.geometry);
          if (!parcel.geometry) continue;
          imported.set(parcelKey(parcel), parcel); count += 1;
        }
        if (imported.size > 200) throw new Error('Die gesamte Auswahl würde 200 Objekte überschreiten. Import nicht übernommen.');
        state.selected = imported;
        touch(); renderSelection(); notice(`${count} Geometrien importiert.${result.warnings?.length ? ' ' + result.warnings.map(textValue).join(' ') : ''}`, result.warnings?.length ? 'error' : 'info');
      } else {
        const parsed = JSON.parse(content);
        await changeCase(() => revalidateCase(parsed.case || parsed));
      }
    } catch (error) { if (!isAbort(error)) notice(`Import: ${error.message}`, 'error'); }
    finally { input.value = ''; }
  }

  function safeDocument(html) {
    // Preview keeps printable formatting, but never executes provider HTML or loads remote resources.
    const doc = new DOMParser().parseFromString(String(html || ''), 'text/html');
    const allowed = new Set('HTML HEAD BODY TITLE STYLE P DIV SPAN BR HR H1 H2 H3 H4 H5 H6 B STRONG I EM U S SMALL SUB SUP BLOCKQUOTE PRE CODE OL UL LI TABLE THEAD TBODY TFOOT TR TH TD CAPTION COLGROUP COL DL DT DD SECTION ARTICLE HEADER FOOTER MAIN ADDRESS A IMG'.split(' '));
    for (const element of [...doc.querySelectorAll('*')]) {
      if (!allowed.has(element.tagName)) { element.remove(); continue; }
      for (const attribute of [...element.attributes]) {
        const name = attribute.name.toLowerCase();
        const safeImage = element.tagName === 'IMG' && name === 'src' && /^data:image\/(png|jpeg|gif|webp);base64,/i.test(attribute.value);
        if (!safeImage && !['style', 'class', 'id', 'lang', 'dir', 'colspan', 'rowspan', 'width', 'height', 'align', 'scope', 'alt'].includes(name)) element.removeAttribute(attribute.name);
      }
    }
    const meta = doc.createElement('meta'); meta.httpEquiv = 'Content-Security-Policy';
    meta.content = "default-src 'none'; script-src 'none'; style-src 'unsafe-inline'; img-src data:; font-src 'none'; connect-src 'none'; form-action 'none'; base-uri 'none'; frame-src 'none'";
    doc.head.prepend(meta);
    const style = doc.createElement('style'); style.textContent = 'body{font:11pt/1.45 "Times New Roman",serif;margin:24px;overflow-wrap:anywhere}img,table{max-width:100%}@media print{body{margin:0}}'; doc.head.append(style);
    return '<!doctype html>' + doc.documentElement.outerHTML;
  }
  function showDocument(index, focus = false) {
    const current = state.documents[index]; if (!current) return;
    state.activeDocument = index; documentReady = false; $('print-document').disabled = true;
    const tabs = [...$('document-tabs').children];
    tabs.forEach((tab, i) => { tab.setAttribute('aria-selected', String(index === i)); tab.tabIndex = index === i ? 0 : -1; });
    $('preview-panel').setAttribute('aria-labelledby', tabs[index].id); $('document-preview').title = current.title || `Entwurf ${index + 1}`;
    $('document-preview').srcdoc = safeDocument(current.html);
    if (focus) tabs[index].focus();
  }
  async function generateDocuments() {
    if (!state.selected.size || state.changing) return;
    const revision = state.revision; const snapshot = structuredClone(collectCase());
    $('generate-documents').disabled = true; $('generate-documents').textContent = 'Entwürfe werden erstellt …';
    try {
      const result = await api('documents', '/api/documents', { body: { case: snapshot }, timeout: 60000 });
      if (revision !== state.revision) throw new Error('Vorgang wurde geändert. Bitte Entwürfe erneut erstellen.');
      if (!Array.isArray(result.documents) || result.documents.length !== 4 || result.documents.some((item) => !item.id || typeof item.html !== 'string')) throw new Error('Der Dokumentendienst hat nicht die vier erwarteten Entwürfe geliefert.');
      state.documents = result.documents; state.documentCase = snapshot; $('document-tabs').replaceChildren(); $('export-status').textContent = '';
      result.documents.forEach((document, index) => {
        const tab = node('button', document.title || `Entwurf ${index + 1}`); tab.type = 'button'; tab.id = `document-tab-${index}`; tab.setAttribute('role', 'tab'); tab.setAttribute('aria-controls', 'preview-panel');
        tab.addEventListener('click', () => showDocument(index));
        tab.addEventListener('keydown', (event) => {
          if (!['ArrowLeft', 'ArrowRight', 'Home', 'End'].includes(event.key)) return;
          event.preventDefault(); showDocument(event.key === 'Home' ? 0 : event.key === 'End' ? 3 : (index + (event.key === 'ArrowRight' ? 1 : -1) + 4) % 4, true);
        }); $('document-tabs').append(tab);
      });
      warningList($('document-warnings'), result.warnings); $('preview-dialog').showModal(); showDocument(0);
    } catch (error) { if (!isAbort(error)) notice(error.message, 'error'); }
    finally { $('generate-documents').textContent = 'Entwürfe erstellen'; syncControls(); }
  }
  async function exportDocuments(format) {
    const current = state.documents[state.activeDocument]; if (!current || !state.documentCase) return;
    $('export-docx').disabled = true; $('export-zip').disabled = true; $('export-status').textContent = 'Download wird vorbereitet …';
    try {
      const blob = await api('export', '/api/export', { body: { case: state.documentCase, format, ...(format === 'zip' ? {} : { document_id: current.id }) }, binary: true, timeout: 60000 });
      if (!blob.size) throw new Error('Der Export enthält keine Daten.');
      const filename = format === 'zip' ? 'grundstuecksrecherche.zip' : `${String(current.id).replace(/[^a-zA-Z0-9_-]/g, '_') || 'entwurf'}.docx`;
      download(blob, filename); $('export-status').textContent = 'Download bereit.';
    } catch (error) { if (!isAbort(error)) $('export-status').textContent = `Export fehlgeschlagen: ${error.message}`; }
    finally { $('export-docx').disabled = false; $('export-zip').disabled = false; }
  }

  $('place-form').addEventListener('submit', (event) => { event.preventDefault(); searchPlaces(); });
  $('place-query').addEventListener('input', () => { clearTimeout(placeTimer); cancel('places'); $('place-results').replaceChildren(); $('place-status').textContent = ''; if ($('place-query').value.trim().length >= 2) placeTimer = setTimeout(searchPlaces, 400); });
  $('example').addEventListener('click', () => changeCase(() => api('case', '/api/example', { body: {}, timeout: 60000 }), true));
  $('change-place').addEventListener('click', () => { $('place-panel').hidden = false; $('place-query').focus(); });
  $('cancel-place').addEventListener('click', () => { cancel('places'); clearTimeout(placeTimer); $('place-panel').hidden = true; });
  $('new-case').addEventListener('click', () => { if (confirmReplace()) { cancel('places'); clearTimeout(placeTimer); blankCase(); notice(''); } });
  $('address-form').addEventListener('submit', (event) => { event.preventDefault(); searchAddresses(); });
  $('address-query').addEventListener('input', () => { clearTimeout(addressTimer); cancel('address'); $('address-results').hidden = true; if ($('address-query').value.trim().length >= 3) addressTimer = setTimeout(searchAddresses, 450); });
  $('address-query').addEventListener('keydown', (event) => { if (event.key === 'Escape') { cancel('address'); clearTimeout(addressTimer); $('address-results').hidden = true; } });
  $('base-layer').addEventListener('change', () => { if (!map) return; if (baseLayer) map.removeLayer(baseLayer); baseLayer = state.providers.get($('base-layer').value)?.layer; if (baseLayer && map.getZoom() < baseLayer.options.minZoom) map.setZoom(baseLayer.options.minZoom); baseLayer?.addTo(map); });
  $('parcels-visible').addEventListener('change', () => {
    if (!map) return;
    for (const entry of state.providers.values()) if (entry.provider.role === 'parcels' && entry.layer) { if ($('parcels-visible').checked) entry.layer.addTo(map); else map.removeLayer(entry.layer); }
    scheduleParcels();
  });
  $('pick-mode').addEventListener('change', () => { $('map').classList.toggle('pick-mode', $('pick-mode').checked); if ($('pick-mode').checked) mapStatus('Lagehinweis: Kartenpunkt ist kein amtlicher Flurstücksnachweis.'); else scheduleParcels(); });
  $('fit-place').addEventListener('click', fitPlace);
  $('refresh-profile').addEventListener('click', () => { const snapshot = structuredClone(collectCase()); changeCase(async () => { const result = await api('case', '/api/setup', { body: { place: snapshot.profile }, timeout: 60000 }); return { ...snapshot, profile: result.profile }; }, false, false); });
  $('reload-parcels').addEventListener('click', () => loadParcels(false)); $('more-parcels').addEventListener('click', () => loadParcels(true));
  $('manual-parcel').addEventListener('click', () => openManual()); $('parcel-form').addEventListener('submit', submitManual);
  $('clear-selection').addEventListener('click', () => { if (window.confirm('Gesamte Flurstücksauswahl leeren?')) { state.selected.clear(); touch(); renderSelection(); } });
  $('case-form').addEventListener('submit', (event) => event.preventDefault()); $('case-form').addEventListener('input', touch); $('case-form').addEventListener('change', touch);
  $('save-case').addEventListener('click', () => {
    try { localStorage.setItem(STORAGE_KEY, JSON.stringify(collectCase())); state.dirty = false; $('save-status').textContent = 'In diesem Browser gespeichert.'; notice('Vorgang lokal gespeichert. Die Wiederherstellung erfolgt nur auf Anforderung.'); storageAvailable(); }
    catch { notice('Browser-Speicherung nicht möglich. Den Vorgang als JSON herunterladen.', 'error'); }
  });
  $('restore-case').addEventListener('click', () => changeCase(() => { const data = JSON.parse(localStorage.getItem(STORAGE_KEY) || 'null'); if (!data) throw new Error('Kein gespeicherter Vorgang vorhanden.'); return revalidateCase(data); }));
  $('forget-case').addEventListener('click', () => {
    if (!window.confirm('Den gespeicherten Vorgang aus diesem Browser löschen?')) return;
    try { localStorage.removeItem(STORAGE_KEY); storageAvailable(); if (state.profile) { state.dirty = true; $('save-status').textContent = 'Nicht lokal gespeichert.'; } notice('Lokale Speicherung gelöscht.'); } catch { notice('Lokale Speicherung konnte nicht gelöscht werden.', 'error'); }
  });
  $('download-case').addEventListener('click', () => download(new Blob([JSON.stringify(collectCase(), null, 2)], { type: 'application/json' }), 'grundstuecksrecherche-vorgang.json'));
  $('import-case').addEventListener('click', () => $('case-file').click()); $('case-file').addEventListener('change', () => importFile($('case-file')));
  $('import-geo').addEventListener('click', () => $('geo-file').click()); $('geo-file').addEventListener('change', () => importFile($('geo-file'), true));
  $('generate-documents').addEventListener('click', generateDocuments);
  $('export-docx').addEventListener('click', () => exportDocuments('docx')); $('export-zip').addEventListener('click', () => exportDocuments('zip'));
  $('document-preview').addEventListener('load', () => { documentReady = !!state.documents.length; $('print-document').disabled = !documentReady; });
  $('print-document').addEventListener('click', () => { if (documentReady) { try { $('document-preview').contentWindow.focus(); $('document-preview').contentWindow.print(); } catch { $('export-status').textContent = 'Drucken wurde vom Browser blockiert. Bitte DOCX herunterladen.'; } } });
  document.querySelectorAll('[data-close]').forEach((button) => button.addEventListener('click', () => $(button.dataset.close).close()));
  document.querySelectorAll('.file-actions button').forEach((button) => button.addEventListener('click', () => document.querySelector('.file-menu').removeAttribute('open')));
  window.addEventListener('beforeunload', (event) => { if (state.dirty) { event.preventDefault(); event.returnValue = ''; } });
  window.addEventListener('storage', storageAvailable);
  new ResizeObserver(() => map?.invalidateSize({ pan: false })).observe($('map'));
  syncControls(); storageAvailable();
  api('config', '/api/config').then((config) => { if (!config.csrf_token) throw new Error('Lokales Sicherheitstoken fehlt.'); csrfToken = config.csrf_token; syncControls(); }).catch((error) => notice(`Lokaler Server: ${error.message}`, 'error'));
})();
