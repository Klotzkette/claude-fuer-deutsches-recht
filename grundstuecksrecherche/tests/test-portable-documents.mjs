// node tests/test-portable-documents.mjs [--browser]
// Optional: PYTHON, PLAYWRIGHT_MODULE, PLAYWRIGHT_CHANNEL, PORTABLE_TEST_OUTPUT.
import assert from 'node:assert/strict';
import { readFileSync, existsSync, mkdtempSync, writeFileSync, mkdirSync, rmSync, openSync, closeSync } from 'node:fs';
import { dirname, join, resolve } from 'node:path';
import { pathToFileURL, fileURLToPath } from 'node:url';
import { tmpdir } from 'node:os';
import { execFileSync } from 'node:child_process';
import { createHash } from 'node:crypto';
import vm from 'node:vm';

const root = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const staticRoot = join(root, 'app/static');
const bundled = join(process.env.HOME, '.cache/codex-runtimes/codex-primary-runtime/dependencies');
const python = process.env.PYTHON || (existsSync(join(bundled, 'python/bin/python3')) ? join(bundled, 'python/bin/python3') : 'python3');
const py = (script, input) => {
  // A regular input file avoids large Unicode pipe stalls in synchronous child processes.
  const temp = mkdtempSync(join(tmpdir(), 'portable-parity-'));
  const source = join(temp, 'input.json');
  writeFileSync(source, input === undefined ? '' : JSON.stringify(input));
  const fd = openSync(source, 'r');
  try {
    return execFileSync(python, ['-c', script], { cwd: root, stdio: [fd, 'pipe', 'pipe'], encoding: 'utf8', timeout: 60000, maxBuffer: 64 * 1024 * 1024 });
  } finally { closeSync(fd); rmSync(temp, { recursive: true, force: true }); }
};
const templateScript = py('from app.portable_templates import template_script; print(template_script(), end="")');
assert.ok(!templateScript.includes('</script'));
assert.equal(templateScript, py('from app.portable_templates import template_script; print(template_script(), end="")'));
globalThis.window = globalThis;
const forbiddenNetwork = () => { throw new Error('Unexpected network access'); };
globalThis.fetch = forbiddenNetwork;
globalThis.XMLHttpRequest = forbiddenNetwork;
globalThis.WebSocket = forbiddenNetwork;
globalThis.Worker = forbiddenNetwork;
for (const file of ['vendor/docx.iife.js', 'vendor/fflate.iife.js']) vm.runInThisContext(readFileSync(join(staticRoot, file), 'utf8'), { filename: file });
vm.runInThisContext(templateScript, { filename: 'generated-templates.js' });
vm.runInThisContext(readFileSync(join(staticRoot, 'portable-documents.js'), 'utf8'), { filename: 'portable-documents.js' });
const engine = globalThis.PortableDocuments;
const ids = ['uebergabe', 'kataster', 'grundbuch', 'notar'];
const output = process.env.PORTABLE_TEST_OUTPUT;
if (output) mkdirSync(output, { recursive: true });
let assertions = 0;
const check = async (name, body) => { await body(); assertions++; console.log(`OK ${name}`); };

await check('package/CLI template imports, process cache, safe serialization and fail-closed compiler', () => {
  const result = py(`
import ast, sys
from unittest.mock import patch
from app import portable_templates as p
first=p.template_script()
with patch.object(p, 'template_data', side_effect=AssertionError('cache miss')):
    assert p.template_script() is first
sys.path.insert(0, 'app')
import portable_templates as cli
assert cli.template_script()==first
for source in ('open("/etc/passwd")', '__import__("os")', 'value.__class__', '1 * 2'):
    try: p._encode(ast.parse(source, mode='eval').body)
    except ValueError: pass
    else: raise AssertionError(source)
p.documents.TITLES['uebergabe']='</script><img src=x onerror=1>&'
p.template_data.cache_clear(); p.template_script.cache_clear()
script=p.template_script()
assert '<' not in script and '>' not in script and '&' not in script
print('OK')
`);
  assert.equal(result.trim(), 'OK');
});

function parcel(index = 0) {
  return {
    stable_id: `technical-selection-${index}`, provider_id: 'technical-provider',
    municipality: `Pruefgemeinde ${index}`, municipality_code: '05515000', district_name: `Gemarkung ${index}`,
    district_code: '007', flur: '001', numerator: `${index + 1}`.padStart(5, '0'), denominator: '0002',
    official_parcel_reference: `TECHNISCH-KEIN-AMTLICHES-KENNZEICHEN-${index}`,
    area_value: 123.5, area_unit: 'm\u00b2', location_text: `Nur technischer Lagehinweis ${index}`,
    source_url: 'https://example.org/kataster', source_date: '2026-10-01', retrieved_at: '2026-10-06T09:00:00Z',
    identification_status: 'manuell_ergaenzt', geometry: { type: 'Point', coordinates: [7, 51] },
    grundbuchblatt: '17', grundbuchblaetter: ['19', '23'], grundbuchbezirk: 'Pruefbezirk',
    grundbuchblatt_source: 'Technischer Nachweis', grundbuchblatt_date: '2026-10-01',
  };
}
function caseData(count = 2) {
  return {
    case_id: 'TECHNISCHER-TEST', purpose: 'Technischer Test.', specific_interest: 'Keine Berechtigung behauptet!',
    requested_information_scope: 'Einfache Abschrift?', sender_organisation: 'Prueforganisation',
    sender_address: 'Erste Zeile\nZweite Zeile\tAnschrift', contact_person: 'Pruefkontakt',
    legal_department_contact: 'Pruefstelle Recht', attachments: '/etc/passwd (nur Text)',
    recipients: { kataster: 'Kataster Pruefanschrift', grundbuch: 'Grundbuch Pruefanschrift', notar: 'Notar Pruefanschrift' },
    created_at: '2026-10-01', updated_at: '2026-10-06', selected_parcels: Array.from({ length: count }, (_, index) => parcel(index)),
    profile: {
      name: 'Pruefgemeinde', state: 'Nordrhein-Westfalen', municipality_code: '05515000', center: [51, 7],
      bounds: [6, 50, 8, 52], verification_state: 'verifiziert', verified_at: '2099-01-01', data_date: '2026-01-01',
      source_url: 'https://example.org/ort', district: 'Pruefkreis', district_source_url: 'https://example.org/kreis',
      source_urls: ['https://example.org/additional'], warnings: ['Offene Zust\u00e4ndigkeit.', 'Noch zu pruefen!'],
      authorities: [{ type: 'Kataster', authority_type: 'kataster', official_name: 'Technische Stelle',
        jurisdiction: 'Unbekannte Zustaendigkeit', postal_address: 'Postanschrift', visitor_address: 'Besucheranschrift',
        verification_state: 'verifiziert', status: 'eingeschraenkt', verified_at: '2026-01-01',
        source_url: 'https://example.org/amt', evidence_urls: ['https://example.org/evidence-a', 'https://example.org/evidence-b'],
        official_website: 'https://example.org/verfahren', official_form_url: 'https://example.org/formular',
        submission_information: 'Kontakt-E-Mail ist kein Einreichungsweg', note: 'Technische Eingabe',
      }],
      providers: [{ provider_id: 'technical-provider', catalog_source_url: 'https://example.org/katalog',
        service_url: 'https://example.org/wfs', verification_state: 'verified', status: 'active',
        test_result: 'Nicht aktuell geprueft', verified_at: '2026-01-01', license: 'Prueflizenz', attribution: 'Pruefherkunft',
        coverage: { country: 'DE', state_codes: ['05'], bounds: [[6, 50, 8, 52]] }, requires_host_approval: true, crs: ['EPSG:4326'],
      }],
      evidence: [{ title: 'Profilnachweis', url: 'https://example.org/fallback', source_url: 'https://example.org/nachweis',
        verification_state: 'verifiziert', status: 'belegt', verified_at: null, checked_at: '2026-01-01', retrieved_at: '2026-01-02' }],
    },
  };
}
const fixtures = [{}, { profile: null }, { selected_parcels: [{}] }, caseData(), caseData(5)];
for (const state of ['Hessen', 'Berlin', 'NRW', ' nw ', 'DE-NW', '\ufeffNRW']) {
  const data = caseData(1); data.profile.state = state; fixtures.push(data);
}
const conflict = caseData(); conflict.selected_parcels[1].municipality_code = '03159016'; fixtures.push(conflict);
const zero = caseData(1); zero.selected_parcels[0].area_value = 0; zero.selected_parcels[0].denominator = ''; fixtures.push(zero);
for (const status of ['location_hint', 'LAGEHINWEIS', 'amtlich_identifiziert', 'MANUAL', '']) {
  const data = caseData(1); data.selected_parcels[0].identification_status = status; fixtures.push(data);
}
const incomplete = caseData(1); delete incomplete.selected_parcels[0].official_parcel_reference; incomplete.profile.authorities[0].evidence_urls = []; incomplete.profile.authorities[0].type = ''; fixtures.push(incomplete);
const injection = caseData(); injection.purpose = '</script><img src=x onerror="alert(1)">&\'\"\n\u{1f9ea}'; injection.sender_address = '<w:t>fake</w:t>\n\t'; fixtures.push(injection);
const whitespace = { purpose: '\ufeff', specific_interest: ' \t\n ', attachments: 'Punkt.   ', selected_parcels: [{ area_value: 0.000001 }] }; fixtures.push(whitespace);
const maximum = caseData(200); fixtures.push(maximum);

const expected = JSON.parse(py(`
import json, sys
from app import documents as d
cases = json.load(sys.stdin)
print(json.dumps([{'html': d.build_documents(case), 'combined': d.export_document(case, 'html')[0].decode(),
                  'drafts': [{'id': item.id, 'title': item.title, 'blocks': item.blocks} for item in d._drafts(d._validate(case, imported=False))],
                  'validated': d.validate_case(case), 'sources': d._sources(case).decode()} for case in cases], ensure_ascii=True))
`, fixtures));

await check('every HTML byte matches Python for empty, NRW/other, qualified profiles, 200 parcels and hostile text', () => {
  fixtures.forEach((data, index) => {
    const before = JSON.stringify(data);
    assert.deepEqual(engine.build(data), expected[index].html, `HTML fixture ${index}`);
    assert.deepEqual(engine.validate(data), expected[index].validated, `validation fixture ${index}`);
    assert.equal(JSON.stringify(data), before, 'input not mutated');
  });
});
await check('runtime edits and all profile qualifications are retained without stale draft state', () => {
  const data = caseData(); const before = engine.build(data);
  data.purpose = 'AENDERUNG NACH DEM OEFFNEN'; data.profile.warnings.push('NEUER OFFENER PRUEFPUNKT');
  data.selected_parcels.push(parcel(3)); data.recipients.notar = 'NEUE NOTARAUSWAHL';
  const after = engine.build(data);
  assert.notEqual(after[0].html, before[0].html);
  after.forEach((draft) => { assert.match(draft.html, /AENDERUNG NACH DEM OEFFNEN/); assert.match(draft.html, /3\.3\. Auswahlposition 3/); });
  assert.match(after[0].html, /NEUER OFFENER PRUEFPUNKT/);
  assert.match(after[3].html, /NEUE NOTARAUSWAHL/);
  for (const term of ['Prueflizenz', 'Pruefherkunft', 'Nicht aktuell geprueft', 'Besucheranschrift', 'eingeschraenkt', 'Profilnachweis', '2099-01-01']) assert.ok(after[0].html.includes(term), term);
});

const invalid = [null, [], 'text', true, 1, { purpose: null }, { case_id: 1 }, { attachments: [] },
  { selected_parcels: {} }, { selected_parcels: [null] }, { selected_parcels: [{ area_value: -1 }] },
  { profile: [] }, { recipients: { email: 'x' } }, { profile: { providers: [{ crs: {} }] } },
  JSON.parse('{"__proto__":{}}'), { selected_parcels: [{ owner: 'Forbidden' }] },
  { selected_parcels: [parcel(), parcel()] }, caseData(201), { purpose: 'x'.repeat(20001) },
  ...['\0', '\x0b', '\x7f', '\u0085', '\ud800', '\udfff', '\ufffe', '\uffff'].map((purpose) => ({ purpose })),
  ...['file:///etc/passwd', 'javascript:alert(1)', 'https://user:pass@example.org', 'https://localhost',
    'https://localhost.', 'http://a.local', 'http://a.internal', 'http://127.0.0.1', 'http://10.0.0.1',
    'http://192.168.1.1', 'http://169.254.169.254', 'http://100.64.0.1', 'http://[::1]', 'http://[fc00::1]',
    'http://[::ffff:127.0.0.1]', 'http://[2001::1]', 'http://[2001:100::1]', 'http://[2001:db8::1]',
    'http://0177.0.0.1', 'http://0x08080808', 'https://%65xample.org',
    'https://example.org:0', 'https://example.org:65536', 'https://example.org/with space',
    'https://example.org/<x>', 'https://example.org/"', 'https://example.org/\\',
  ].map((source_url) => ({ profile: { source_url } })),
  { profile: { center: [200, 0] } }, { profile: { center: { latitude: 0 } } }, { profile: { bounds: [1, 1, 0, 0] } },
  ...[{ type: 'Feature', coordinates: [] }, { type: 'Point', coordinates: [181, 0] },
    { type: 'LineString', coordinates: [[0, 0]] }, { type: 'Polygon', coordinates: [[[0, 0], [1, 0], [1, 1], [0, 1]]] },
    { type: 'MultiPoint', coordinates: [] }, { type: 'Point', coordinates: [0, 0], extra: true },
  ].map((geometry) => ({ selected_parcels: [{ geometry }] })),
];
const tooBig = caseData(200); tooBig.selected_parcels.forEach((value) => { value.location_text = '\u00e4'.repeat(6000); }); invalid.push(tooBig);
const tooManyPoints = { type: 'MultiPoint', coordinates: Array.from({ length: 10001 }, () => [1, 2]) };
invalid.push({ selected_parcels: [{ geometry: tooManyPoints }] });
invalid.push({ selected_parcels: Array.from({ length: 5 }, () => ({ geometry: { type: 'MultiPoint', coordinates: Array.from({ length: 9000 }, () => [1, 2]) } })) });
await check('Python/browser rejection parity, bounded geometry, size limits and prototype safety', () => {
  const rejected = JSON.parse(py(`
import json, sys
from app.documents import validate_case
result=[]
for case in json.load(sys.stdin):
    try: validate_case(case); result.append(False)
    except ValueError: result.append(True)
print(json.dumps(result))
`, invalid));
  invalid.forEach((data, index) => { assert.equal(rejected[index], true, `Python rejection ${index}`); assert.throws(() => engine.build(data), undefined, `Browser rejection ${index}`); });
  for (const value of [NaN, Infinity, -Infinity, undefined, () => {}, new Date(), new Map()]) assert.throws(() => engine.build({ purpose: value }));
  const cyclic = {}; cyclic.profile = cyclic; assert.throws(() => engine.build(cyclic));
  assert.throws(() => engine.build({ get purpose() { throw new Error('getter executed'); } }), (error) => !/getter executed/.test(error.message));
  assert.equal({}.polluted, undefined);
});

await check('all supported geometry types and Unicode code points remain valid', () => {
  const ring = [[1, 2], [2, 2], [2, 3], [1, 2]];
  const geometries = [null, { type: 'Point', coordinates: [1, 2, 3] }, { type: 'MultiPoint', coordinates: [[1, 2]] },
    { type: 'LineString', coordinates: [[1, 2], [3, 4]] }, { type: 'MultiLineString', coordinates: [[[1, 2], [3, 4]]] },
    { type: 'Polygon', coordinates: [ring] }, { type: 'MultiPolygon', coordinates: [[ring], [ring]] }];
  const data = { purpose: '\u{1f9ea}'.repeat(11000), profile: { center: { latitude: 51, longitude: 7 } }, selected_parcels: geometries.map((geometry) => ({ geometry })) };
  assert.deepEqual(engine.validate(data), data);
});

await check('true DOCX/ZIP exports match Python text, XML styles and safe sources', async () => {
  for (const index of [0, 3, 5, 11, fixtures.indexOf(injection), fixtures.length - 1]) {
    const data = fixtures[index];
    const bundle = await engine.export(data, 'zip');
    assert.equal(bundle.type, 'application/zip');
    const bytes = new Uint8Array(await bundle.arrayBuffer());
    const entries = fflate.unzipSync(bytes);
    assert.deepEqual(Object.keys(entries).sort(), [...ids.flatMap((id) => [`${id}.docx`, `${id}.html`]), 'vorgang.json', 'quellen.txt'].sort());
    assert.deepEqual(JSON.parse(fflate.strFromU8(entries['vorgang.json'])), data);
    assert.equal(fflate.strFromU8(entries['quellen.txt']), expected[index].sources);
    const docxFiles = [];
    for (const [order, id] of ids.entries()) {
      assert.equal(fflate.strFromU8(entries[`${id}.html`]), expected[index].html[order].html);
      docxFiles.push({ id, bytes: Buffer.from(entries[`${id}.docx`]).toString('base64') });
    }
    const individual = await engine.export(data, 'docx', 'kataster');
    assert.equal(individual.type, 'application/vnd.openxmlformats-officedocument.wordprocessingml.document');
    assert.deepEqual(new Uint8Array(await individual.arrayBuffer()), entries['kataster.docx'], 'deterministic individual/ZIP export');
    const combined = await engine.export(data, 'docx');
    docxFiles.push({ id: 'all', bytes: Buffer.from(await combined.arrayBuffer()).toString('base64') });
    const inspection = JSON.parse(py(`
import base64, json, sys
from io import BytesIO
from zipfile import ZipFile
from xml.etree import ElementTree as E
from docx import Document
from app import documents as d
payload = json.load(sys.stdin)
case = payload['case']
results=[]
ns={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
q=lambda name: '{'+ns['w']+'}'+name
for file in payload['files']:
    blob=base64.b64decode(file['bytes'])
    document=Document(BytesIO(blob))
    reference=Document(BytesIO(d.export_document(case, 'docx', None if file['id']=='all' else file['id'])[0]))
    assert [p.text for p in document.paragraphs] == [p.text for p in reference.paragraphs], file['id']
    with ZipFile(BytesIO(blob)) as z:
        assert z.testzip() is None
        assert '[Content_Types].xml' in z.namelist() and 'word/document.xml' in z.namelist()
        for name in z.namelist():
            assert not name.startswith('/') and '..' not in name.split('/')
            assert z.getinfo(name).date_time == (1980,1,1,0,0,0)
            if name.endswith(('.xml','.rels')): E.fromstring(z.read(name))
            if name.endswith('.rels'): assert b'TargetMode="External"' not in z.read(name)
        styles=E.fromstring(z.read('word/styles.xml'))
        for styleid in ('Normal','Title','Heading1','Heading2','Header','Footer'):
            style=styles.find(f'w:style[@w:styleId="{styleid}"]',ns)
            fonts=style.find('w:rPr/w:rFonts',ns)
            assert all(fonts.get(q(k))=='Times New Roman' for k in ('ascii','hAnsi','eastAsia','cs')), styleid
            assert style.find('w:rPr/w:sz',ns).get(q('val'))=='22'
            assert style.find('w:pPr/w:pBdr',ns) is None
        headings=[p.text for p in document.paragraphs if p.style.style_id.startswith('Heading')]
        assert all(text[0].isdigit() for text in headings)
        section=document.sections[0]
        assert abs(section.page_width.mm-210)<0.1 and abs(section.page_height.mm-297)<0.1
        assert abs(section.left_margin.mm-22)<0.1 and abs(section.top_margin.mm-20)<0.1
        assert section.header.paragraphs[0].text == d.DRAFT_MARKER
        core=z.read('docProps/core.xml').decode()
        assert core.count('2000-01-01T00:00:00Z') == 2
    results.append({'id':file['id'],'paragraphs':len(document.paragraphs)})
print(json.dumps(results))
`, { case: data, files: docxFiles }));
    assert.equal(inspection.length, 5);
    assert.equal(await (await engine.export(data, 'html')).text(), expected[index].combined);
    assert.deepEqual(JSON.parse(await (await engine.export(data, 'json')).text()), data);
    if (output && index === 3) {
      writeFileSync(join(output, 'technical-documents.zip'), bytes);
      for (const id of ids) writeFileSync(join(output, `${id}.docx`), entries[`${id}.docx`]);
    }
  }
});
await check('format/ID restrictions, dependency errors and no network or attachment path reads', async () => {
  for (const format of ['doc', 'pdf', '../../etc/passwd', null, [], 1]) await assert.rejects(engine.export({}, format));
  for (const id of ['../../etc/passwd', 'unknown', [], 1, '__proto__', 'constructor']) await assert.rejects(engine.export({}, 'docx', id));
  for (const format of ['zip', 'json']) await assert.rejects(engine.export({}, format, 'notar'));
  const saved = globalThis.docx; globalThis.docx = undefined;
  try { await assert.rejects(engine.export({}, 'docx'), /Bibliotheken/); assert.equal(engine.build({}).length, 4); }
  finally { globalThis.docx = saved; }
  const templates = globalThis.PortableDocumentTemplates; globalThis.PortableDocumentTemplates = undefined;
  try { assert.throws(() => engine.build({}), /Dokumentvorlagen/); } finally { globalThis.PortableDocumentTemplates = templates; }
});
await check('vendored build integrity and license coverage', () => {
  const manifest = JSON.parse(readFileSync(join(staticRoot, 'vendor/docx-vendor-manifest.json')));
  for (const [name, info] of Object.entries(manifest.files)) {
    const bytes = readFileSync(join(staticRoot, 'vendor', name));
    assert.equal(bytes.length, info.bytes); assert.equal(createHash('sha256').update(bytes).digest('hex'), info.sha256);
  }
  for (const name of ['docx', 'jszip', 'fflate', 'pako', 'nanoid']) assert.ok(manifest.packages.some((pkg) => pkg.name === name));
});

if (process.argv.includes('--browser')) await check('file:// browser, offline edits, four real downloads and no injected markup', async () => {
  const module = process.env.PLAYWRIGHT_MODULE || pathToFileURL(join(bundled, 'node/node_modules/playwright/index.mjs')).href;
  const { chromium } = await import(module);
  const directory = mkdtempSync(join(tmpdir(), 'portable-documents-offline-'));
  const browser = await chromium.launch({ headless: true, channel: process.env.PLAYWRIGHT_CHANNEL || 'chrome' });
  try {
    writeFileSync(join(directory, 'templates.js'), templateScript);
    const scripts = ['vendor/docx.iife.js', 'vendor/fflate.iife.js'].map((file) => pathToFileURL(join(staticRoot, file)).href);
    scripts.push(pathToFileURL(join(directory, 'templates.js')).href, pathToFileURL(join(staticRoot, 'portable-documents.js')).href);
    writeFileSync(join(directory, 'index.html'), `<!doctype html><meta charset="utf-8"><title>Offline document engine test</title>
      <label>Purpose<textarea id="purpose"></textarea></label><button id="download">DOCX</button><iframe id="preview" style="width:95%;height:800px"></iframe>
      ${scripts.map((src) => `<script src="${src}"></script>`).join('')}`);
    const context = await browser.newContext({ offline: true, acceptDownloads: true });
    const page = await context.newPage(); const network = [], errors = [];
    page.on('request', (request) => { if (/^https?:/.test(request.url())) network.push(request.url()); });
    page.on('pageerror', (error) => errors.push(error.message));
    await page.goto(pathToFileURL(join(directory, 'index.html')).href);
    await page.evaluate((data) => {
      window.testCase = data; window.testId = 'uebergabe';
      document.querySelector('#purpose').addEventListener('input', (event) => {
        testCase.purpose = event.target.value;
        document.querySelector('#preview').srcdoc = PortableDocuments.build(testCase)[0].html;
      });
      document.querySelector('#download').addEventListener('click', async () => {
        const blob = await PortableDocuments.export(testCase, testId === 'zip' ? 'zip' : 'docx', testId === 'zip' ? null : testId);
        const url = URL.createObjectURL(blob), a = document.createElement('a');
        a.href = url; a.download = `${testId}.${testId === 'zip' ? 'zip' : 'docx'}`; a.click();
        setTimeout(() => URL.revokeObjectURL(url), 1000);
      });
    }, caseData());
    await page.locator('#purpose').fill('OFFLINE GE\u00c4NDERT <img src=x onerror=alert(1)>');
    await page.frameLocator('#preview').locator('body').waitFor();
    assert.equal(await page.frameLocator('#preview').locator('img,script,[onerror]').count(), 0);
    for (const id of [...ids, 'zip']) {
      await page.evaluate((id) => { window.testId = id; }, id);
      const pending = page.waitForEvent('download'); await page.locator('#download').click(); const download = await pending;
      const bytes = readFileSync(await download.path()); assert.equal(bytes.subarray(0, 2).toString(), 'PK');
      const entries = fflate.unzipSync(bytes);
      if (id !== 'zip') assert.match(fflate.strFromU8(entries['word/document.xml']), /OFFLINE GE\u00c4NDERT/);
      else assert.equal(Object.keys(entries).filter((name) => name.endsWith('.docx')).length, 4);
    }
    assert.deepEqual(network, []); assert.deepEqual(errors, []);
    if (output) await page.screenshot({ path: join(output, 'offline-preview.png'), fullPage: true });
  } finally { await browser.close(); rmSync(directory, { recursive: true, force: true }); }
});
console.log(`Passed ${assertions} portable document test groups (${fixtures.length} parity fixtures, ${invalid.length} invalid inputs).`);
