// Run: node grundstuecksrecherche/tests/test-ui.mjs
// Optional: PLAYWRIGHT_MODULE=/absolute/path/to/playwright/index.mjs UI_SCREENSHOTS=/tmp/ui
import assert from 'node:assert/strict';
import { createServer } from 'node:http';
import { readFile, mkdir } from 'node:fs/promises';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';

const root = resolve(dirname(fileURLToPath(import.meta.url)), '../app/static');
let playwright;
try { playwright = await import(process.env.PLAYWRIGHT_MODULE || 'playwright'); }
catch (error) {
  if (process.env.PLAYWRIGHT_MODULE) throw error;
  playwright = await import(pathToFileURL(join(process.env.HOME, '.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright/index.mjs')).href);
}
const { chromium } = playwright;
const screenshots = process.env.UI_SCREENSHOTS || '/tmp/grundstuecksrecherche-ui';
if (process.argv.includes('--live')) {
  const browser = await chromium.launch({ headless: true, channel: process.env.PLAYWRIGHT_CHANNEL || 'chrome' });
  const page = await browser.newPage({ viewport: { width: 1440, height: 1000 }, acceptDownloads: true });
  const pageErrors = [];
  page.on('pageerror', (error) => pageErrors.push(error.message));
  page.on('response', async (response) => { if (response.url().includes('/api/') && !response.ok()) console.log('API', response.status(), new URL(response.url()).pathname, (await response.text()).slice(0, 200)); });
  try {
    await mkdir(screenshots, { recursive: true });
    await page.goto(process.env.UI_BASE_URL || 'http://127.0.0.1:8765');
    assert.equal(await page.locator('#selection-count').textContent(), '0');
    await page.screenshot({ path: join(screenshots, 'real-desktop-empty.png'), fullPage: true });
    await page.locator('#example').click();
    await page.waitForFunction(() => !document.getElementById('map-toolbar').hidden || document.getElementById('notice').dataset.kind === 'error', {}, { timeout: 90000 });
    assert.equal(await page.locator('#map-toolbar').isVisible(), true, await page.locator('#notice').textContent());
    await page.waitForFunction(() => Number(document.getElementById('available-count').textContent) > 0 || document.getElementById('map-status').parentElement.dataset.kind === 'error', {}, { timeout: 45000 });
    console.log('Karte:', await page.locator('#map-status').textContent());
    assert.ok(Number(await page.locator('#available-count').textContent()) > 0, 'Echte Münster-Flurstücke erwartet');
    await page.locator('#available-section summary').click();
    await page.locator('#available-list button').nth(3).click();
    await page.locator('#case_id').fill('UI-PRUEFUNG');
    await page.locator('#purpose').fill('Technischer Funktionstest ohne Versand.');
    await page.locator('#specific_interest').fill('Testdaten; keine tatsächliche Auskunft beantragt.');
    await page.locator('#requested_information_scope').selectOption({ label: 'Eigentümerauskunft' });
    await page.locator('#sender_organisation').fill('Lokaler UI-Test');
    await page.waitForFunction(() => [...document.querySelectorAll('#map img.leaflet-tile')].some((image) => image.complete && image.naturalWidth > 0) && [...document.querySelectorAll('#map img.leaflet-tile')].every((image) => image.complete), {}, { timeout: 30000 });
    await page.evaluate(() => window.scrollTo(0, 0));
    await page.screenshot({ path: join(screenshots, 'real-desktop-map.png'), fullPage: true });
    await page.locator('#generate-documents').click();
    await page.waitForFunction(() => document.getElementById('preview-dialog').open || !document.getElementById('generate-documents').disabled, {}, { timeout: 60000 });
    assert.equal(await page.locator('#preview-dialog').isVisible(), true, await page.locator('#notice').textContent());
    assert.equal(await page.locator('[role="tab"]').count(), 4);
    await page.locator('#document-preview').contentFrame().locator('body').waitFor();
    await page.screenshot({ path: join(screenshots, 'real-desktop-preview.png') });
    for (const [button, extension] of [['#export-docx', '.docx'], ['#export-zip', '.zip']]) {
      const downloadPromise = page.waitForEvent('download'); await page.locator(button).click(); const file = await downloadPromise;
      assert.ok(file.suggestedFilename().endsWith(extension)); const bytes = await readFile(await file.path()); assert.equal(bytes.subarray(0, 2).toString(), 'PK'); console.log('Export:', extension, bytes.length, 'Bytes');
    }
    await page.locator('[data-close="preview-dialog"]').click();
    await page.setViewportSize({ width: 390, height: 844 });
    await page.waitForFunction(() => Number(document.getElementById('available-count').textContent) > 0, {}, { timeout: 30000 });
    await page.evaluate(() => window.scrollTo(0, 0));
    assert.equal(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth), true);
    await page.screenshot({ path: join(screenshots, 'real-mobile-map.png'), fullPage: true });
    await page.locator('#generate-documents').click(); await page.locator('#preview-dialog').waitFor(); await page.screenshot({ path: join(screenshots, 'real-mobile-preview.png') });
    await page.locator('[data-close="preview-dialog"]').click();
    await page.locator('.file-menu summary').click(); await page.locator('#save-case').click();
    await page.reload(); assert.equal(await page.locator('#selection-count').textContent(), '0');
    await page.locator('.file-menu summary').click(); await page.locator('#restore-case').click();
    await page.waitForFunction(() => document.getElementById('case_id').value === 'UI-PRUEFUNG', {}, { timeout: 90000 });
    assert.equal(await page.locator('#selection-count').textContent(), '1');
    assert.deepEqual(pageErrors, []); console.log('OK Live-Server: Flurstücke, Auswahl, vier Dokumente, echte DOCX/ZIP, Wiederherstellung, Desktop und Mobil.');
    console.log(`Screenshots: ${screenshots}`);
  } finally { await browser.close(); }
  process.exit(0);
}
const csrf = 'ui-test-token';
const requests = [];
let mapFailure = false, parcelFailure = false, setupFailure = false, parcelDelay = 0, sequence = 0;
const candidate = { id: 'muenster', name: 'Münster', state: 'Nordrhein-Westfalen', district: 'Kreisfreie Stadt', municipality_code: '05515000', center: [51.9607, 7.6261], bounds: [7.45, 51.80, 7.85, 52.10], source_url: 'https://example.org/ort', verification_state: 'verifiziert' };
const profile = () => ({ ...candidate, profile_id: `profile-${++sequence}`, providers: [
  { provider_id: 'base', title: 'Amtliche Karte', role: 'base', protocol: 'WMS', layers: 'test', format: 'image/png', service_url: 'https://example.org/wms', verification_state: 'verifiziert', attribution: 'Amtliche Testkarte', license: 'Testdaten', test_result: 'Erreichbar' },
  { provider_id: 'aerial', title: 'Luftbild', role: 'aerial', protocol: 'WMS', layers: 'aerial', format: 'image/png', service_url: 'https://example.org/aerial', verification_state: 'verifiziert', attribution: 'Testluftbild' },
  { provider_id: 'parcels', title: 'Flurstücksdienst', role: 'parcels', protocol: 'WFS', service_url: 'https://example.org/wfs', verification_state: 'verifiziert' },
  { provider_id: 'blocked', title: 'Nicht freigegebene Karte', role: 'base', protocol: 'WMS', service_url: 'https://example.org/blocked', verification_state: 'gefunden_ungeprueft' }
], authorities: [{ authority_type: 'kataster', official_name: 'Katasteramt Teststadt', postal_address: 'Teststraße 1\n00000 Teststadt', visitor_address: 'Besucherstraße 2', evidence_urls: ['https://example.org/amt'], verification_state: 'verifiziert', submission_information: 'Postanschrift verwenden.' }], evidence: [], warnings: [] });
const feature = (id, offset = 0) => ({ type: 'Feature', id, geometry: { type: 'Polygon', coordinates: [[[7.6255 + offset, 51.9604], [7.626 + offset, 51.9604], [7.626 + offset, 51.9609], [7.6255 + offset, 51.9609], [7.6255 + offset, 51.9604]]] }, properties: { stable_id: id, provider_id: 'parcels', municipality: 'Münster', municipality_code: '05515000', district_name: 'Münster', district_code: '055001', flur: '1', numerator: id === 'a' ? '24' : '25', denominator: '', official_parcel_reference: `BELEGT-${id}`, area_value: 123, area_unit: 'm²', location_text: 'Teststraße', source_url: 'https://example.org/flurstueck', source_date: '2026-10-06', retrieved_at: '2026-10-06T10:00:00Z', identification_status: 'verifiziert' } });
const collection = (features, extras = {}) => ({ type: 'FeatureCollection', features, truncated: false, next_page: null, warnings: [], ...extras });
const documents = ['Katasteramt', 'Grundbuchamt', 'Notariat', 'Übergabevermerk'].map((title, index) => ({ id: `document-${index}`, title, html: `<!doctype html><html><head><title>${title}</title></head><body><h1>${title}</h1><p>Vollständig formulierter Testentwurf.</p><script>parent.__injected = true</script><img src="https://malicious.invalid/image" onerror="parent.__injected=true"><a href="javascript:alert(1)">Beleg</a><iframe src="https://malicious.invalid/frame"></iframe></body></html>` }));
// A locally generated solid PNG fixture keeps the test independent of remote tile services.
const png = Buffer.from('iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNk+A8AAQUBAScY42YAAAAASUVORK5CYII=', 'base64');
const server = createServer(async (req, res) => {
  try {
    const url = new URL(req.url, 'http://localhost');
    const chunks = []; for await (const chunk of req) chunks.push(chunk);
    const body = chunks.length ? JSON.parse(Buffer.concat(chunks)) : null;
    requests.push({ path: url.pathname, query: Object.fromEntries(url.searchParams), body, token: req.headers['x-local-token'] });
    const json = (data, status = 200) => { res.writeHead(status, { 'Content-Type': 'application/json' }); res.end(JSON.stringify(data)); };
    if (req.method === 'POST' && req.headers['x-local-token'] !== csrf) return json({ error: 'CSRF fehlt' }, 403);
    if (url.pathname === '/api/config') return json({ csrf_token: csrf, max_parcels: 200, min_parcel_zoom: 17 });
    if (url.pathname === '/api/places') {
      if (url.searchParams.get('q') === 'Langsam') await new Promise((done) => setTimeout(done, 1000));
      return json({ candidates: [{ ...candidate, name: url.searchParams.get('q') === 'Langsam' ? 'Veralteter Treffer' : candidate.name }] });
    }
    if (['/api/setup', '/api/example'].includes(url.pathname)) return setupFailure ? json({ error: 'Amtliche Quelle ist nicht erreichbar.' }, 400) : json({ profile: profile() });
    if (url.pathname === '/api/import') return json({ case: body.case });
    if (url.pathname === '/api/address') return json({ candidates: [{ label: 'Rothenburg 1, Münster', center: candidate.center }] });
    if (url.pathname === '/api/parcels') {
      if (parcelDelay) await new Promise((done) => setTimeout(done, parcelDelay));
      if (parcelFailure) return json({ error: 'Katasterdienst ist nicht erreichbar.' }, 400);
      return json(url.searchParams.get('page') === '1' ? collection([feature('b', .0007)]) : collection([feature('a')], { truncated: true, next_page: 1 }));
    }
    if (url.pathname === '/api/import-geo') return json(collection([feature('imported', -.0008)], { warnings: ['Importierte Angaben sind ungeprüft.'] }));
    if (url.pathname === '/api/documents') return json({ documents, warnings: ['Entwürfe vor Versand prüfen.'] });
    if (url.pathname === '/api/export') { res.writeHead(200, { 'Content-Type': 'application/octet-stream' }); return res.end('TEST-EXPORT'); }
    if (url.pathname === '/api/website') { res.writeHead(200, { 'Content-Type': 'application/zip' }); return res.end('TEST-WEBSITE'); }
    if (url.pathname === '/api/map') { if (mapFailure) return json({ error: 'Kartendienst nicht erreichbar' }, 400); res.writeHead(200, { 'Content-Type': 'image/png' }); return res.end(png); }
    const pathname = url.pathname === '/' ? 'index.html' : decodeURIComponent(url.pathname.slice(1));
    const file = resolve(root, pathname); if (!file.startsWith(root + '/')) return json({ error: 'Pfad gesperrt' }, 403);
    const content = await readFile(file);
    res.writeHead(200, { 'Content-Type': file.endsWith('.html') ? 'text/html; charset=utf-8' : file.endsWith('.js') ? 'text/javascript' : file.endsWith('.css') ? 'text/css' : 'application/octet-stream', 'Content-Security-Policy': "default-src 'self'; connect-src 'self'; img-src 'self' data: blob:; style-src 'self' 'unsafe-inline'; script-src 'self'; frame-src 'self' blob:; object-src 'none'; base-uri 'none'" });
    res.end(content);
  } catch (error) { if (!res.headersSent) res.writeHead(500); res.end(error.message); }
});
await new Promise((done) => server.listen(0, '127.0.0.1', done));
const origin = `http://127.0.0.1:${server.address().port}`;
const browser = await chromium.launch({ headless: true, channel: process.env.PLAYWRIGHT_CHANNEL || 'chrome' });
const context = await browser.newContext({ viewport: { width: 1440, height: 1000 }, acceptDownloads: true });
const page = await context.newPage();
const errors = []; page.on('pageerror', (error) => errors.push(error.message));
const remote = []; page.on('request', (request) => { if (/^https?:/.test(request.url()) && !request.url().startsWith(origin)) remote.push(request.url()); });
const check = async (name, test) => { await test(); console.log(`OK ${name}`); };
const menu = async (id) => { await page.locator('.file-menu summary').click(); await page.locator(id).click(); };
const visible = async (selector) => { await page.locator(selector).waitFor({ state: 'visible' }); };
const noOverflow = async () => assert.equal(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth), true);
const savedCase = { case_id: 'ALT-42', profile: { ...profile(), profile_id: 'expired-profile' }, selected_parcels: [{ ...feature('saved').properties, geometry: feature('saved').geometry, grundbuchblatt: '47', grundbuchblaetter: ['47', '48'], grundbuchbezirk: 'Belegter Bezirk', grundbuchblatt_source: 'Mitgeteilter Beleg', grundbuchblatt_date: '2026-10-06' }], sender_organisation: 'Gespeicherter Absender', recipients: {}, purpose: 'Gespeicherter Zweck' };

try {
  await mkdir(screenshots, { recursive: true });
  await context.addInitScript((data) => { if (!localStorage.getItem('ui-seeded')) { localStorage.setItem('grundstuecksrecherche.case.v1', JSON.stringify(data)); localStorage.setItem('ui-seeded', 'yes'); } }, savedCase);
  await page.goto(origin);
  await check('Leerer Erststart trotz gespeicherter Daten', async () => {
    await page.waitForFunction(() => !document.getElementById('example').disabled);
    assert.equal(await page.locator('#case_id').inputValue(), ''); assert.equal(await page.locator('#sender_organisation').inputValue(), '');
    assert.equal(await page.locator('#selection-count').textContent(), '0');
    assert.equal(requests.filter((r) => ['/api/setup', '/api/example', '/api/import', '/api/map', '/api/parcels'].includes(r.path)).length, 0);
    await noOverflow(); await page.screenshot({ path: join(screenshots, 'desktop-empty.png'), fullPage: true });
  });
  await check('Explizite Wiederherstellung mit erneuerter Profil-ID', async () => {
    await menu('#restore-case'); await visible('#map-toolbar');
    assert.equal(await page.locator('#case_id').inputValue(), 'ALT-42');
    assert.equal(await page.locator('#sender_organisation').inputValue(), 'Gespeicherter Absender');
    assert.equal(await page.locator('#selection-count').textContent(), '1');
    await page.waitForFunction(() => document.getElementById('available-count').textContent === '1');
    assert.ok(requests.some((r) => r.path === '/api/setup' && r.body.place.profile_id === 'expired-profile'));
    assert.ok(requests.filter((r) => r.path === '/api/map').every((r) => r.query.profile_id !== 'expired-profile'));
    const tile = requests.find((r) => r.path === '/api/map');
    assert.equal(tile.query.version, '1.3.0'); assert.equal(tile.query.crs, 'EPSG:3857'); assert.equal(tile.query.width, '256');
    assert.ok(tile.query.bbox.split(',').every((n) => Math.abs(Number(n)) > 180));
    assert.equal(requests.some((r) => r.path === '/api/map' && r.query.provider_id === 'blocked'), false);
    await menu('#save-case'); const saved = await page.evaluate(() => JSON.parse(localStorage.getItem('grundstuecksrecherche.case.v1')));
    assert.deepEqual(saved.selected_parcels[0].grundbuchblaetter, ['47', '48']); assert.equal(saved.selected_parcels[0].grundbuchblatt, '47');
  });
  await check('Website-Download nur mit ausdrücklicher Vorgangsaufnahme', async () => {
    await menu('#download-website');
    assert.equal(await page.locator('#website-include-case').isChecked(), false);
    const first = page.waitForEvent('download'); await page.locator('#website-submit').click();
    assert.equal((await first).suggestedFilename(), 'grundstuecksrecherche-website.zip');
    assert.equal(requests.filter((r) => r.path === '/api/website').at(-1).body.include_case, false);
    await page.locator('#website-submit').waitFor({state:'visible'});
    await page.locator('#website-include-case').check();
    const second = page.waitForEvent('download'); await page.locator('#website-submit').click(); await second;
    assert.equal(requests.filter((r) => r.path === '/api/website').at(-1).body.include_case, true);
    await page.locator('[data-close="website-dialog"]').first().click();
  });
  await check('Neuer Vorgang nur nach Bestätigung, Beispiel ohne Absender und Auswahl', async () => {
    page.once('dialog', (dialog) => dialog.dismiss()); await page.locator('#new-case').click(); assert.equal(await page.locator('#case_id').inputValue(), 'ALT-42');
    page.once('dialog', (dialog) => dialog.accept()); await page.locator('#new-case').click(); await visible('#place-panel');
    await page.locator('#example').click(); await visible('#map-toolbar');
    assert.equal(await page.locator('#sender_organisation').inputValue(), ''); assert.equal(await page.locator('#selection-count').textContent(), '0');
    await page.waitForFunction(() => document.getElementById('available-count').textContent === '1');
  });
  await check('Auswahl und separate Geometrie bleiben bei Kartenbewegung erhalten', async () => {
    await page.locator('#available-section summary').click(); await page.locator('#available-list button').first().click();
    assert.equal(await page.locator('#selection-count').textContent(), '1');
    assert.equal(await page.locator('.leaflet-selection-pane path').count(), 1);
    await page.locator('#map').focus(); await page.keyboard.press('ArrowRight');
    await page.waitForFunction(() => document.getElementById('available-count').textContent === '1');
    assert.equal(await page.locator('#selection-count').textContent(), '1'); assert.equal(await page.locator('.leaflet-selection-pane path').count(), 1);
    await page.locator('#more-parcels').click(); await page.waitForFunction(() => document.getElementById('available-count').textContent === '2');
  });
  await check('Manuelle Angaben ohne erfundene amtliche IDs', async () => {
    await page.locator('#manual-parcel').click(); await page.locator('#parcel-form button[type="submit"]').click(); await visible('#parcel-error');
    await page.locator('#parcel-numerator').fill('71'); await page.locator('#parcel-district_name').fill('<img src=x onerror=alert(1)>');
    await page.locator('#parcel-form button[type="submit"]').click(); assert.equal(await page.locator('#selection-count').textContent(), '2');
    assert.equal(await page.locator('#selection-list img').count(), 0);
    await menu('#save-case'); const data = await page.evaluate(() => JSON.parse(localStorage.getItem('grundstuecksrecherche.case.v1')));
    const manual = data.selected_parcels.find((item) => item.numerator === '71'); assert.equal(manual.stable_id, ''); assert.equal(manual.official_parcel_reference, ''); assert.equal(manual.geometry, null);
  });
  await check('Lagehinweis ist ausdrücklich kein Flurstücksnachweis', async () => {
    await page.locator('#pick-mode').check(); await page.locator('#map').click({ position: { x: 150, y: 150 } }); await visible('#parcel-dialog');
    assert.match(await page.locator('#parcel-note').textContent(), /kein amtlicher/);
    await page.locator('#parcel-form button[type="submit"]').click(); assert.match(await page.locator('#selection-list').textContent(), /Lagehinweis · kein Flurstücksnachweis/);
  });
  await check('Vier sichere Vorschautabs, DOCX, ZIP und Druck', async () => {
    await page.locator('#purpose').fill('Konkretes Testvorhaben'); await page.locator('#generate-documents').click(); await visible('#preview-dialog');
    assert.equal(await page.locator('[role="tab"]').count(), 4);
    await page.locator('#document-tab-0').focus(); await page.keyboard.press('ArrowRight'); assert.equal(await page.locator('#document-tab-1').getAttribute('aria-selected'), 'true');
    await page.waitForFunction(() => !document.getElementById('print-document').disabled);
    const frame = page.frameLocator('#document-preview'); assert.equal(await frame.locator('script, iframe, [onerror]').count(), 0); assert.equal(await page.evaluate(() => window.__injected), undefined);
    await page.locator('#document-preview').evaluate((iframe) => { iframe.contentWindow.print = () => { iframe.dataset.printed = 'yes'; }; });
    await page.locator('#print-document').click(); assert.equal(await page.locator('#document-preview').getAttribute('data-printed'), 'yes');
    let downloaded = page.waitForEvent('download'); await page.locator('#export-docx').click(); assert.equal((await downloaded).suggestedFilename(), 'document-1.docx');
    downloaded = page.waitForEvent('download'); await page.locator('#export-zip').click(); assert.equal((await downloaded).suggestedFilename(), 'grundstuecksrecherche.zip');
    assert.equal(requests.findLast((r) => r.path === '/api/export').body.format, 'zip');
    await page.screenshot({ path: join(screenshots, 'desktop-preview.png') }); await page.locator('[data-close="preview-dialog"]').click();
  });
  await check('Geodatenimport, Größenlimit und explizite Fehler', async () => {
    await page.locator('#geo-file').setInputFiles({ name: 'test.geojson', mimeType: 'application/json', buffer: Buffer.from(JSON.stringify(collection([feature('imported')])) ) });
    await page.waitForFunction(() => document.getElementById('notice').textContent.includes('1 Geometrien importiert'));
    await page.locator('#geo-file').setInputFiles({ name: 'zu-gross.gml', mimeType: 'application/xml', buffer: Buffer.alloc(2 * 1024 * 1024 + 1, 'x') });
    await page.waitForFunction(() => document.getElementById('notice').textContent.includes('2 MB'));
    parcelFailure = true; await page.locator('#map').focus(); await page.keyboard.press('ArrowRight');
    await page.waitForFunction(() => document.getElementById('map-status').textContent.includes('nicht erreichbar') && !document.getElementById('reload-parcels').hidden);
    assert.match(await page.locator('#map-status').textContent(), /nicht erreichbar/);
    parcelFailure = false; await page.locator('#reload-parcels').click(); await page.waitForFunction(() => document.getElementById('reload-parcels').hidden);
    mapFailure = true; await page.locator('#base-layer').selectOption('aerial');
    await page.waitForFunction(() => document.getElementById('notice').textContent.includes('Kartenkacheln konnten nicht'));
    assert.match(await page.locator('#sources').getAttribute('class'), /has-error/); mapFailure = false; await page.locator('#base-layer').selectOption('base');
  });
  await check('Veraltete Suchantworten werden verworfen', async () => {
    await page.locator('#change-place').click(); await page.locator('#place-query').fill('Langsam');
    await page.waitForRequest((request) => request.url().includes('q=Langsam'));
    await page.locator('#place-query').fill('Münster'); await page.locator('#place-results button').waitFor();
    await page.waitForTimeout(1100); assert.doesNotMatch(await page.locator('#place-results').textContent(), /Veralteter/);
    page.once('dialog', (dialog) => dialog.dismiss()); await page.locator('#place-results button').click(); assert.notEqual(await page.locator('#selection-count').textContent(), '0');
    await page.locator('#cancel-place').click();
  });
  await check('Desktop und Mobil ohne horizontalen Überlauf', async () => {
    await page.locator('#sources').evaluate((element) => { element.open = false; });
    await noOverflow(); await page.screenshot({ path: join(screenshots, 'desktop-workspace.png'), fullPage: true });
    await page.setViewportSize({ width: 390, height: 844 }); await noOverflow(); await page.screenshot({ path: join(screenshots, 'mobile-workspace.png'), fullPage: true });
    await page.locator('#generate-documents').click(); await visible('#preview-dialog'); await noOverflow(); await page.screenshot({ path: join(screenshots, 'mobile-preview.png') }); await page.keyboard.press('Escape');
    await page.setViewportSize({ width: 320, height: 700 }); await noOverflow();
    assert.deepEqual(errors, []); assert.deepEqual(remote, []);
    assert.ok(requests.filter((r) => r.body).every((r) => r.token === csrf));
  });
  await check('Zeitüberschreitung wird sichtbar und verändert keine Auswahl', async () => {
    let pending;
    await page.route('**/api/address?**', (route) => { pending = route; });
    await page.clock.install();
    const requestStarted = page.waitForRequest((request) => request.url().includes('/api/address?'));
    await page.locator('#address-query').fill('Zeitüberschreitung'); await page.locator('#address-form button').click();
    await requestStarted;
    await page.clock.fastForward(26000);
    await page.waitForFunction(() => document.getElementById('address-results').textContent.includes('Zeitüberschreitung'));
    await pending.abort(); await page.unroute('**/api/address?**'); await page.clock.resume();
    assert.notEqual(await page.locator('#selection-count').textContent(), '0');
  });
  await check('Wiederherstellung bei Quellenausfall erhält Auswahl und Entwürfe', async () => {
    const count = await page.locator('#selection-count').textContent();
    await menu('#save-case'); setupFailure = true;
    await page.reload(); await menu('#restore-case'); await visible('#map-toolbar');
    assert.equal(await page.locator('#selection-count').textContent(), count);
    assert.match(await page.locator('#profile-warnings').textContent(), /ohne aktuelle Quellenprüfung geöffnet/);
    await page.locator('#generate-documents').click(); await visible('#preview-dialog');
    assert.equal(await page.locator('[role="tab"]').count(), 4);
  });
  console.log(`Screenshots: ${screenshots}`);
} finally {
  await browser.close(); server.closeAllConnections(); await new Promise((done) => server.close(done));
}
