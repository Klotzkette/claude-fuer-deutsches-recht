// Run: node grundstuecksrecherche/tests/test-portable-runtime.mjs
// Uses a real file:// Chromium page; remote services are deterministic bounded fixtures.
import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import { execFileSync } from 'node:child_process';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';

const project = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const staticRoot = join(project, 'app/static');
const runtimePath = join(staticRoot, 'portable-runtime.js');
const source = await readFile(runtimePath, 'utf8');
const catalogs = JSON.parse(await readFile(join(project, 'app/catalogs.json'), 'utf8'));
let playwright;
try { playwright = await import(process.env.PLAYWRIGHT_MODULE || 'playwright'); }
catch (error) {
  if (process.env.PLAYWRIGHT_MODULE) throw error;
  playwright = await import(pathToFileURL(join(process.env.HOME, '.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright/index.mjs')).href);
}
const browser = await playwright.chromium.launch({ headless: true, channel: process.env.PLAYWRIGHT_CHANNEL || 'chrome' });
const page = await browser.newPage();
const unintended = [], pageErrors = [];
await page.route('https://**/*', (route) => { unintended.push(route.request().url()); return route.abort(); });
page.on('pageerror', (error) => pageErrors.push(error.message));
const prepared = { name: 'M\u00fcnster', state: 'Nordrhein-Westfalen', municipality_code: '05515000', center: [51.9607, 7.6261], bounds: [7.45, 51.80, 7.85, 52.10] };
const shape = { type: 'Polygon', coordinates: [[[7, 51], [8, 51], [8, 52], [7, 51]]] };
const manual = { stable_id: '', provider_id: '', district_name: 'Testgemarkung', numerator: '71', area_value: null, geometry: null, identification_status: 'manual_unverified' };
const geo = { type: 'Feature', geometry: shape, properties: { district_name: 'Testgemarkung', numerator: '71', area_value: null } };
const collection = (members, matched = 'unknown') => `<w:FeatureCollection xmlns:w="http://www.opengis.net/wfs/2.0" xmlns:g="http://www.opengis.net/gml/3.2" xmlns:a="http://repository.gdi-de.org/schemas/adv/produkt/alkis-vereinfacht/1.0" numberMatched="${matched}">${members}</w:FeatureCollection>`;
const polygon = (points = '51 7 51 8 52 8 51 7') => `<g:Polygon><g:exterior><g:LinearRing><g:posList>${points}</g:posList></g:LinearRing></g:exterior><g:interior><g:LinearRing><g:posList>51.1 7.2 51.1 7.3 51.2 7.3 51.1 7.2</g:posList></g:LinearRing></g:interior></g:Polygon>`;
const member = (id = 'ID001', ags = '05515000') => `<w:member><a:Flurstueck><a:idflurst>${id}</a:idflurst><a:gmdschl>${ags}</a:gmdschl><a:gemeinde>Muenster</a:gemeinde><a:gemarkung>Muenster</a:gemarkung><a:gemaschl>055001</a:gemaschl><a:flur>1</a:flur><a:flstnrzae>24</a:flstnrzae><a:flstnrnen>0</a:flstnrnen><a:flstkennz>05500100100024______</a:flstkennz><a:flaeche>123.5</a:flaeche><a:geometrie><g:MultiSurface srsName="urn:ogc:def:crs:EPSG::4326"><g:surfaceMember>${polygon()}</g:surfaceMember><g:surfaceMember>${polygon('51 9 51 10 52 10 51 9')}</g:surfaceMember></g:MultiSurface></a:geometrie></a:Flurstueck></w:member>`;
const gml = collection(member());
const vg = (name = 'Berlin', ags = '11000000', bbox = [13.1, 52.3, 13.7, 52.7]) => ({ type: 'Feature', bbox, properties: { ags, gen: name, wsk: '2025-01-01' } });

async function reset(overrides = {}) {
  await page.goto(pathToFileURL(runtimePath).href);
  await page.evaluate((bundle) => {
    window.PORTABLE_BUNDLE = bundle;
    window.net = [];
    window.reply = { mode: 'cors' };
    window.fetch = async (url, options) => {
      window.net.push({ url, credentials: options.credentials, redirect: options.redirect, mode: options.mode, referrerPolicy: options.referrerPolicy, method: options.method });
      const response = window.reply;
      if (response.mode === 'cors') throw new TypeError('Failed to fetch');
      if (response.mode === 'hang') return new Promise(() => {});
      if (response.mode === 'stream-hang') return new Response(new ReadableStream({ start() {} }));
      if (response.mode === 'large-stream') return new Response(new ReadableStream({ start(controller) { controller.enqueue(new Uint8Array(8 * 1024 * 1024 + 1)); controller.close(); } }));
      if (response.mode === 'redirect') return { ok: true, redirected: true, type: 'cors', url: 'https://evil.invalid/', headers: new Headers() };
      return new Response(response.text || '', { status: response.status || 200, headers: response.headers || {} });
    };
  }, { catalogs, profile: prepared, case: null, ...overrides });
  await page.addScriptTag({ content: source });
}
const request = (path, body) => page.evaluate(async ({ path, body }) => window.PortableApp.request(path, body === undefined ? {} : { body }), { path, body });
const reply = (text, extra = {}) => page.evaluate((value) => { window.reply = value; }, { mode: 'text', text, ...extra });
const setup = async () => (await request('/api/setup', { place: prepared })).profile;
const parcelPath = (profile, suffix = '') => `/api/parcels?profile_id=${profile.profile_id}&bbox=7,51,7.001,51.001${suffix}`;
const check = async (name, fn) => { await reset(); await fn(); console.log(`OK ${name}`); };

try {
  await check('empty file:// first start, including embedded case and stale localStorage', async () => {
    await reset({ case: { profile: prepared, sender_organisation: 'NEVER AUTO', selected_parcels: [manual] } });
    await page.evaluate(() => localStorage.setItem('grundstuecksrecherche.case.v1', JSON.stringify({ sender_organisation: 'STALE' })));
    const config = await request('/api/config');
    assert.equal(config.max_parcels, 200); assert.ok(config.csrf_token); assert.equal(config.portable, true);
    assert.equal(config.profile, undefined); assert.equal(config.case, undefined);
    assert.deepEqual(await page.evaluate(() => window.net), []);
    await assert.rejects(request('/api/parcels?profile_id=portable-1&bbox=7,51,7.001,51.001'), /nicht aktiv/);
    const data = await page.evaluate(() => window.PortableApp.prepared());
    assert.equal(data.sender_organisation, 'NEVER AUTO'); assert.equal(data.selected_parcels.length, 1);
    assert.equal(data.selected_parcels[0].identification_status, 'manuell_ergaenzt');
    await reset();
    const empty = await page.evaluate(() => window.PortableApp.prepared());
    assert.deepEqual(empty.selected_parcels, []); assert.deepEqual(empty.recipients, {});
    assert.equal(empty.sender_organisation, undefined); assert.equal(empty.profile.name, prepared.name);
    await reset({ profile: null, case: { profile: { ...prepared, name: 'Offline Imported City', municipality_code: '11000000' }, selected_parcels: [manual] } });
    const included = await page.evaluate(() => window.PortableApp.prepared());
    assert.equal(included.profile.name, 'Offline Imported City');
    assert.deepEqual(await page.evaluate(() => window.net), []);
  });

  await check('prepared city works offline; example is explicit and has no owner/organisation preset', async () => {
    const result = await request('/api/places?q=M%C3%BCnster');
    assert.equal(result.candidates.length, 1); assert.notEqual(result.candidates[0].verification_state, 'verifiziert');
    const profile = (await request('/api/setup', { place: result.candidates[0] })).profile;
    assert.deepEqual(profile.center, prepared.center);
    assert.ok(profile.providers.some((item) => item.provider_id === 'nrw-alkis' && item.portable));
    assert.ok(profile.providers.every((item) => item.verification_state !== 'verifiziert'));
    assert.ok(profile.warnings.some((warning) => /keine aktuelle/.test(warning)));
    const sample = await request('/api/example', {});
    assert.deepEqual(sample.profile.center, [51.9607, 7.6261]);
    assert.match(sample.profile.center_method, /Referenz/);
    assert.deepEqual(Object.keys(sample), ['profile']);
    assert.deepEqual(await page.evaluate(() => window.net), []);
  });

  await check('catalog-only WMS selection rejects adversarial URLs and mutated layers', async () => {
    const profile = await setup();
    const provider = profile.providers.find((item) => item.provider_id === 'nrw-abk');
    const map = (item) => page.evaluate((value) => window.PortableApp.mapURL(value), item);
    assert.equal(await map(provider), provider.service_url);
    for (const service_url of [
      'http://www.wms.nrw.de/geobasis/wms_nw_abk', 'https://www.wms.nrw.de.evil.invalid/geobasis/wms_nw_abk',
      'https://www.wms.nrw.de@evil.invalid/geobasis/wms_nw_abk', 'https://user:pass@www.wms.nrw.de/geobasis/wms_nw_abk',
      'https://127.0.0.1/geobasis/wms_nw_abk', 'https://[::1]/geobasis/wms_nw_abk', 'https://www.wms.nrw.de:444/geobasis/wms_nw_abk',
      'https://www.wms.nrw.de/geobasis/wms_nw_abk?url=https://evil.invalid', 'https://www.wms.nrw.de/geobasis/wms_nw_abk#x',
      'https://www.wms.nrw.de/geobasis/wms_nw_abk/../private', 'https://www.wms.nrw.de/geobasis/%77ms_nw_abk',
      'https://www.wms.nrw.de/geobasis/wms_nw_abk/extra', 'https://www.wms.nrw.de./geobasis/wms_nw_abk',
      'https://www.wms.nrw.de\\@evil.invalid/geobasis/wms_nw_abk', 'javascript:alert(1)', '//www.wms.nrw.de/geobasis/wms_nw_abk'
    ]) assert.equal(await map({ ...provider, service_url }), null, service_url);
    for (const change of [{ portable: false }, { verification_state: 'verifiziert' }, { layers: 'evil' }, { role: 'parcels' }, { protocol: 'WFS' }, { crs: 'EPSG:4326' }]) assert.equal(await map({ ...provider, ...change }), null);
    assert.equal(await map({ ...provider, provider_id: 'unlisted' }), null);
    const attack = { ...prepared, providers: [{ ...provider, service_url: 'https://evil.invalid/wms' }] };
    const imported = await request('/api/import', { case: { profile: attack, selected_parcels: [manual] } });
    assert.equal(await map(imported.case.profile.providers[0]), null);
    const clean = (await request('/api/setup', { place: imported.case.profile })).profile;
    assert.equal(clean.providers.find((item) => item.provider_id === 'nrw-abk').service_url, provider.service_url);
    assert.deepEqual(await page.evaluate(() => window.net), []);
    const poisoned = structuredClone(catalogs);
    poisoned.providers.find((item) => item.provider_id === 'nrw-abk').service_url = 'https://evil.invalid/wms';
    poisoned.allowed_hosts['evil.invalid'] = ['/wms'];
    await reset({ catalogs: poisoned });
    const disabled = (await setup()).providers.find((item) => item.provider_id === 'nrw-abk');
    assert.equal(disabled.portable, false); assert.equal(await map(disabled), null);
  });

  await check('official BKG lookup, grouping, quoted literal and unsupported WFS disclosure', async () => {
    await reply(JSON.stringify({ type: 'FeatureCollection', features: [vg(), vg('Berlin', '11000000', [13.0, 52.2, 13.8, 52.8])] }));
    const found = await request('/api/places?q=Berlin');
    assert.equal(found.candidates.length, 1); assert.deepEqual(found.candidates[0].bounds, [13.0, 52.2, 13.8, 52.8]);
    assert.deepEqual(found.candidates[0].center, [52.5, 13.4]);
    const profile = (await request('/api/setup', { place: { ...found.candidates[0], center: [0, 0], providers: [{ service_url: 'https://evil.invalid/' }] } })).profile;
    assert.deepEqual(profile.center, [52.5, 13.4]);
    const berlin = profile.providers.find((item) => item.provider_id === 'be-alkis');
    assert.equal(berlin.portable, false); assert.equal(berlin.verification_state, 'eingeschraenkt');
    await assert.rejects(request(parcelPath(profile)), /Kein unterstützter/);
    const calls = await page.evaluate(() => window.net);
    assert.equal(calls.length, 1);
    assert.equal(new URL(calls[0].url).origin + new URL(calls[0].url).pathname, catalogs.places.service_url);
    assert.equal(calls[0].credentials, 'omit'); assert.equal(calls[0].redirect, 'error'); assert.equal(calls[0].mode, 'cors'); assert.equal(calls[0].referrerPolicy, 'no-referrer');
    await reply(JSON.stringify({ type: 'FeatureCollection', features: [] }));
    await request('/api/places?q=O%27Brien');
    const last = new URL((await page.evaluate(() => window.net)).at(-1).url);
    assert.equal(last.searchParams.get('cql_filter'), "gen ILIKE 'O''Brien%'");
    await assert.rejects(request('/api/places?q=Berlin%25'), /Suchoperatoren/);
    await assert.rejects(request('/api/places?q=Be%2Alin'), /Suchoperatoren/);
  });

  await check('file CORS/offline fallback preserves imported manual work without proxies', async () => {
    await assert.rejects(request('/api/places?q=Berlin'), /offline, CORS.*file:\/\//);
    const incoming = { profile: { name: 'Privater Ortshinweis', municipality_code: '11000000', center: [52.5, 13.4], verification_state: 'verifiziert', authorities: [{ authority_type: 'kataster', official_name: 'Ungepruefte Stelle', verification_state: 'verifiziert' }], providers: [{ provider_id: 'custom', protocol: 'WFS', service_url: 'https://evil.invalid/wfs', verification_state: 'verifiziert', portable: true }] }, selected_parcels: [manual], sender_organisation: 'Mein Absender' };
    const data = (await request('/api/import', { case: incoming })).case;
    const profile = (await request('/api/setup', { place: data.profile })).profile;
    assert.equal(data.sender_organisation, incoming.sender_organisation); assert.equal(data.selected_parcels.length, 1);
    assert.equal(profile.authorities[0].verification_state, 'gefunden_ungeprueft');
    assert.equal(profile.providers.find((item) => item.provider_id === 'custom').portable, false);
    assert.ok(profile.warnings.some((warning) => /nicht aktuell amtlich/.test(warning)));
    const before = (await page.evaluate(() => window.net)).length;
    await assert.rejects(request(`/api/address?profile_id=${profile.profile_id}&q=Privatstrasse`), /keine Adressen an Drittanbieter/);
    assert.equal((await page.evaluate(() => window.net)).length, before);
    assert.ok((await page.evaluate(() => window.net)).every((call) => new URL(call.url).hostname === 'sgx.geodatenzentrum.de'));
  });

  await check('NRW namespace-aware GML swaps axes, keeps holes/multipart, normalizes ogc fields', async () => {
    const profile = await setup(); await reply(gml);
    const result = await request(parcelPath(profile));
    const feature = result.features[0];
    assert.equal(feature.id, 'nrw-alkis:ID001'); assert.equal(feature.properties.area_value, 123.5);
    assert.equal(feature.properties.area_unit, 'm\u00b2'); assert.equal(feature.properties.official_parcel_reference, '05500100100024______');
    assert.equal(feature.properties.identification_status, 'amtliche_flurstuecksdaten');
    assert.equal(feature.geometry.type, 'MultiPolygon'); assert.equal(feature.geometry.coordinates.length, 2);
    assert.equal(feature.geometry.coordinates[0].length, 2);
    assert.deepEqual(feature.geometry.coordinates[0][0][0], [7, 51]); assert.deepEqual(feature.geometry.coordinates[0][1][0], [7.2, 51.1]);
    const url = new URL((await page.evaluate(() => window.net))[0].url);
    assert.equal(url.searchParams.get('BBOX'), '51,7,51.001,7.001,urn:ogc:def:crs:EPSG::4326');
    assert.equal(url.searchParams.get('COUNT'), '200'); assert.equal(url.searchParams.get('STARTINDEX'), '0');
    await reply(collection(member('OTHER', '12345678')));
    assert.deepEqual((await request(parcelPath(profile))).features, []);
    await reply(collection(member(), 1000));
    const short = await request(parcelPath(profile)); assert.equal(short.truncated, true); assert.equal(short.next_page, null); assert.ok(short.warnings.length);
    await reply(collection(Array.from({ length: 200 }, (_, i) => member(String(i))).join(''), 1200));
    const full = await request(parcelPath(profile)); assert.equal(full.next_page, 1); assert.equal(full.features.length, 200);
    const last = await request(parcelPath(profile, '&page=4')); assert.equal(last.truncated, true); assert.equal(last.next_page, null);
  });

  await check('GML parser rejects ambiguous CRS, XML entities, spoofed namespaces and malformed rings', async () => {
    const profile = await setup();
    for (const invalid of [
      gml.replace('urn:ogc:def:crs:EPSG::4326', 'EPSG:4326'),
      gml.replace('urn:ogc:def:crs:EPSG::4326', 'urn:ogc:def:crs:EPSG::25832'),
      gml.replace('srsName="urn:ogc:def:crs:EPSG::4326"', ''),
      gml.replace('http://www.opengis.net/gml/3.2', 'https://evil.invalid/gml'),
      gml.replace('http://www.opengis.net/wfs/2.0', 'https://evil.invalid/wfs'),
      gml.replace('51 7 51 8 52 8 51 7', '51 7 51 8 52 8 52 7'),
      gml.replace('51 7 51 8 52 8 51 7', 'Infinity 7 51 8 52 8 Infinity 7'),
      gml.replace('<a:flaeche>123.5', '<a:flaeche>-1'),
      gml.replace('<a:idflurst>ID001</a:idflurst>', '').replace('<a:flstkennz>05500100100024______</a:flstkennz>', ''),
      '<!DOCTYPE x [<!ENTITY x SYSTEM "file:///etc/passwd">]><x>&x;</x>',
      '<ExceptionReport><Exception>Denied</Exception></ExceptionReport>', '<invalid',
      collection(member() + member()), collection(Array.from({ length: 201 }, (_, i) => member(String(i))).join(''))
    ]) { await reply(invalid); await assert.rejects(request(parcelPath(profile))); }
    await reply(gml.replace('<a:gmdschl>05515000</a:gmdschl>', '<x:gmdschl xmlns:x="https://evil.invalid">05515000</x:gmdschl>'));
    assert.deepEqual((await request(parcelPath(profile))).features, []);
    const before = (await page.evaluate(() => window.net)).length;
    for (const path of [`/api/parcels?profile_id=${profile.profile_id}&bbox=7,51,9,52`, parcelPath(profile, '&page=5'), parcelPath(profile, '&page=1e0'), `/api/parcels?profile_id=${profile.profile_id}&bbox=7,,8,52`]) await assert.rejects(request(path));
    assert.equal((await page.evaluate(() => window.net)).length, before);
  });

  await check('strict stream size, redirects, aborts and header/body timeout budgets', async () => {
    const profile = await setup();
    await reply('', { headers: { 'content-length': String(8 * 1024 * 1024 + 1) } });
    await assert.rejects(request(parcelPath(profile)), /Größenbudget/);
    await reply('', { mode: 'large-stream' }); await assert.rejects(request(parcelPath(profile)), /Größenbudget/);
    await reply('', { mode: 'redirect' }); await assert.rejects(request(parcelPath(profile)), /Weiterleitungen/);
    await reply('', { status: 503 }); await assert.rejects(request(parcelPath(profile)), /HTTP 503/);
    const before = (await page.evaluate(() => window.net)).length;
    const aborted = await page.evaluate(async () => {
      const controller = new AbortController(); controller.abort();
      try { await window.PortableApp.request('/api/places?q=Berlin', { signal: controller.signal }); } catch (error) { return error.name; }
    });
    assert.equal(aborted, 'AbortError'); assert.equal((await page.evaluate(() => window.net)).length, before);
    await reply('', { mode: 'hang' });
    const name = await page.evaluate(async () => {
      const controller = new AbortController();
      const promise = window.PortableApp.request('/api/places?q=Berlin', { signal: controller.signal });
      controller.abort();
      try { await promise; } catch (error) { return error.name; }
    });
    assert.equal(name, 'AbortError');
    await page.clock.install();
    for (const mode of ['hang', 'stream-hang']) {
      await reply('', { mode });
      await page.evaluate(() => { window.pending = window.PortableApp.request('/api/places?q=Berlin').then(() => 'unexpected', (error) => error.message); });
      await page.clock.fastForward(15001);
      assert.match(await page.evaluate(() => window.pending), /Zeitbudget/);
    }
    await page.clock.resume();
  });

  await check('WGS84 import, deterministic IDs, stripped owner/provider claims and hard budgets', async () => {
    const profile = await setup();
    const imported = { ...geo, properties: { ...geo.properties, owner: 'Do not retain', provider_id: 'nrw-alkis', source_url: 'https://evil.invalid', identification_status: 'verifiziert' } };
    const load = (value) => request('/api/import-geo', { profile_id: profile.profile_id, content: JSON.stringify(value) });
    const one = await load(imported), two = await load(imported);
    assert.equal(one.features[0].id, two.features[0].id); assert.match(one.features[0].id, /^import:[a-f\d]{20}$/);
    const properties = one.features[0].properties;
    assert.equal(properties.owner, undefined); assert.equal(properties.provider_id, 'import'); assert.equal(properties.source_url, ''); assert.equal(properties.identification_status, 'manuell_ergaenzt'); assert.equal(properties.area_value, null);
    const withBBox = await load({ ...geo, geometry: { ...shape, bbox: [7, 51, 8, 52], owner: 'ignored metadata' } });
    assert.deepEqual(withBBox.features[0].geometry, shape);
    for (const value of [
      { ...geo, crs: null }, { type: 'FeatureCollection', crs: { name: 'EPSG:25832' }, features: [geo] },
      { ...geo, geometry: { ...shape, crs: 'EPSG:4326' } },
      { ...geo, geometry: { type: 'Point', coordinates: [7, 51] } },
      { ...geo, geometry: { type: 'Polygon', coordinates: [[[400000, 5700000], [400001, 5700000], [400001, 5700001], [400000, 5700000]]] } },
      { ...geo, properties: { area_value: true } }, { ...geo, properties: { area_value: '-1' } },
      { type: 'FeatureCollection', features: [] }, { type: 'FeatureCollection', features: [geo, geo] },
      { type: 'FeatureCollection', features: Array(201).fill(geo) },
      { ...geo, geometry: { type: 'Polygon', coordinates: [Array(10001).fill([7, 51])] } }
    ]) await assert.rejects(load(value));
    const dense = Array.from({ length: 5 }, (_, i) => ({ ...geo, geometry: { type: 'Polygon', coordinates: [Array(9000).fill([7 + i / 10, 51])] } }));
    await assert.rejects(load({ type: 'FeatureCollection', features: dense }), /positionen/);
    await assert.rejects(request('/api/import-geo', { profile_id: profile.profile_id, content: gml }), /GML-Dateiimport.*lokalen Server/);
    await assert.rejects(request('/api/import-geo', { profile_id: profile.profile_id, content: ' '.repeat(2 * 1024 * 1024 + 1) }), /lang|MiB/);
    await assert.rejects(request('/api/import', { case: { selected_parcels: Array(201).fill(manual) } }), /Eintragsbudget/);
    const hint = (await request('/api/import', { case: { selected_parcels: [{ ...manual, geometry: { type: 'Point', coordinates: [7, 51] }, identification_status: 'verifiziert' }] } })).case;
    assert.equal(hint.selected_parcels[0].identification_status, 'location_hint');
    const closed = await request('/api/import', { case: { selected_parcels: Array.from({ length: 200 }, (_, i) => ({ ...manual, numerator: String(i) })) } });
    assert.equal(closed.case.selected_parcels.length, 200);
    assert.deepEqual(await page.evaluate(() => window.net), []);
  });

  await check('API paths cannot be used as arbitrary fetch and included schema is bounded', async () => {
    for (const path of ['https://evil.invalid/api/config', '//evil.invalid/api/config', '/api/config#x', '/api/../config', '/api/%63onfig', '/api/map']) await assert.rejects(request(path));
    await assert.rejects(page.evaluate(() => window.PortableApp.request('/api/import', { body: { case: JSON.parse('{"__proto__":{"polluted":true}}') } })), /Feldname/);
    await assert.rejects(request('/api/import', { case: { case_id: 'x'.repeat(20001) } }), /Text zu lang/);
    await assert.rejects(request('/api/import', { case: { case_id: 'x', owner: 'unrequested' } }), /nicht erlaubte/);
    assert.deepEqual(await page.evaluate(() => window.net), []);
  });

  await check('document cancellation and deadline do not return stale output', async () => {
    await page.evaluate(() => { window.PortableDocuments = { export: () => new Promise(() => {}) }; });
    const result = await page.evaluate(async () => {
      const controller = new AbortController();
      const pending = window.PortableApp.request('/api/export', { body: { case: {}, format: 'zip' }, signal: controller.signal });
      controller.abort();
      try { await pending; } catch (error) { return error.name; }
    });
    assert.equal(result, 'AbortError');
    await page.clock.install();
    await page.evaluate(() => { window.pending = window.PortableApp.request('/api/export', { body: { case: {}, format: 'zip' } }).then(() => 'unexpected', (error) => error.message); });
    await page.clock.fastForward(30001);
    assert.match(await page.evaluate(() => window.pending), /Zeitbudget der lokalen Dokumenterstellung/);
    await page.clock.resume();
  });

  await check('fresh document engine passthrough, JSON/HTML content and real DOCX/ZIP', async () => {
    const templateSource = execFileSync(process.env.PYTHON || 'python3', ['-c', 'from app.portable_templates import template_script; print(template_script(), end="")'], { cwd: project, maxBuffer: 4 * 1024 * 1024 }).toString();
    for (const file of ['vendor/docx.iife.js', 'vendor/fflate.iife.js']) await page.addScriptTag({ content: await readFile(join(staticRoot, file), 'utf8') });
    await page.addScriptTag({ content: templateSource });
    await page.addScriptTag({ content: await readFile(join(staticRoot, 'portable-documents.js'), 'utf8') });
    const profile = await setup();
    const input = { profile, selected_parcels: [manual], recipients: {}, case_id: 'FIRST-RUNTIME-CASE', sender_organisation: 'Initial Sender' };
    const preview = await request('/api/documents', { case: input });
    assert.equal(preview.documents.length, 4); assert.ok(preview.documents.every((item) => item.html.includes('FIRST-RUNTIME-CASE')));
    const result = await page.evaluate(async (data) => {
      data.case_id = 'FRESH-RUNTIME-CASE'; data.sender_organisation = 'Fresh Sender';
      const original = window.PortableDocuments, seen = [];
      window.PortableDocuments = { ...original, export: async (...args) => {
        const blob = await original.export(...args); seen.push({ args: args.slice(1), blob }); return blob;
      } };
      const html = await window.PortableApp.request('/api/export', { body: { case: data, format: 'html', document_id: 'kataster' }, binary: true });
      const docx = await window.PortableApp.request('/api/export', { body: { case: data, format: 'docx', document_id: 'kataster' }, binary: true });
      const zip = await window.PortableApp.request('/api/export', { body: { case: data, format: 'zip' }, binary: true });
      const json = await window.PortableApp.request('/api/export', { body: { case: data, format: 'json' }, binary: true });
      const unzip = async (blob) => window.fflate.unzipSync(new Uint8Array(await blob.arrayBuffer()));
      const decode = (bytes) => new TextDecoder().decode(bytes);
      const word = await unzip(docx), entries = await unzip(zip);
      return { html: await html.text(), word: decode(word['word/document.xml']), entries: Object.keys(entries), case: JSON.parse(decode(entries['vorgang.json'])), json: JSON.parse(await json.text()), passthrough: seen[0].blob === html && seen[1].blob === docx && seen[2].blob === zip && seen[3].blob === json, args: seen.map((item) => item.args), docxType: docx.type, zipType: zip.type };
    }, input);
    assert.equal(result.passthrough, true); assert.match(result.html, /FRESH-RUNTIME-CASE/); assert.doesNotMatch(result.html, /FIRST-RUNTIME-CASE/);
    assert.match(result.word, /FRESH-RUNTIME-CASE/); assert.match(result.word, /Fresh Sender/);
    assert.equal(result.case.case_id, 'FRESH-RUNTIME-CASE'); assert.equal(result.case.sender_organisation, 'Fresh Sender');
    assert.equal(result.json.case_id, 'FRESH-RUNTIME-CASE');
    assert.equal(result.entries.filter((name) => name.endsWith('.docx')).length, 4);
    assert.equal(result.entries.filter((name) => name.endsWith('.html')).length, 4);
    assert.ok(result.entries.includes('quellen.txt')); assert.equal(result.zipType, 'application/zip');
    assert.equal(result.docxType, 'application/vnd.openxmlformats-officedocument.wordprocessingml.document');
    assert.deepEqual(result.args, [['html', 'kataster'], ['docx', 'kataster'], ['zip', undefined], ['json', undefined]]);
    assert.deepEqual(await page.evaluate(() => window.net), []);
  });

  assert.deepEqual(unintended, []); assert.deepEqual(pageErrors, []);
  console.log('All portable runtime tests passed, with no unintended network requests.');
} finally {
  await browser.close();
}
