#!/usr/bin/env node
import fs from 'node:fs';
import path from 'node:path';
import { promptEnabled, promptKinds, promptFormats, promptProfileErrors } from './prompt-profiles.mjs';

// Dateischutz für eigenständige Downloads; Skill- und Modellbudgets bleiben getrennt.
import { promptLimits, miniWithinLimits } from './prompt-limits.mjs';
const root = process.cwd();
const errors = [];

function rel(file) {
  return path.relative(root, file).replaceAll(path.sep, '/');
}

function readText(file) {
  return fs.readFileSync(file, 'utf8');
}

function readJson(file) {
  try {
    return JSON.parse(readText(file));
  } catch (error) {
    errors.push(`${rel(file)}: JSON kann nicht gelesen werden: ${error.message}`);
    return null;
  }
}

function walk(dir, out = []) {
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    if (['.git', '.venv', 'node_modules', 'dist', '__pycache__'].includes(entry.name)) continue;
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) walk(full, out);
    else out.push(full);
  }
  return out;
}

function count(text, needle) {
  return text.split(needle).length - 1;
}

// Die GFM-Navigation wird separat gerendert. Hier vergleichen wir die
// veröffentlichten Release-URLs exakt, ohne Kommentare und Codebeispiele.
function withoutCode(text) {
  return text.replace(/^ {0,3}(`{3,}|~{3,})[^\n]*\n[^]*?^ {0,3}\1[`~]*[ \t]*\r?$/gm, '')
    .replace(/(`+)[^`\n]*?\1/g, '');
}

function readmeProse(text) {
  return withoutCode(text).replace(/<!--[^]*?-->/g, '');
}

function downloadUrls(text) {
  return new Set(readmeProse(text).match(/https?:\/\/[^\s<>"'`\])]+/g) || []);
}

function checkEntryMarkers(text, readme, primaryUrls) {
  let marked = false;
  for (const name of ['direkt-loslegen', 'plugin-sofort-download-section']) {
    const begin = `<!-- BEGIN ${name} (autogen) -->`;
    const end = `<!-- END ${name} (autogen) -->`;
    if (!text.includes(begin) && !text.includes(end)) continue;
    const valid = !marked && count(text, begin) === 1 && count(text, end) === 1 && text.indexOf(begin) < text.indexOf(end);
    assert(valid, `${rel(readme)}: Downloadblock ${name} unvollständig, mehrfach oder falsch angeordnet`);
    if (valid) {
      const block = text.slice(text.indexOf(begin) + begin.length, text.indexOf(end));
      const urls = downloadUrls(block);
      assert(primaryUrls.every(url => urls.has(url)), `${rel(readme)}: Einstiegslinks im Downloadblock fehlen`);
    }
    marked = true;
  }
  if (!marked) {
    const prose = readmeProse(text);
    assert(/^#[ \t]+\S/m.test(prose) && /^##[ \t]+\S/m.test(prose),
      `${rel(readme)}: gegliederter Einstieg in die Benutzung fehlt`);
  }
}

function checkPluralCases(directory) {
  if (!fs.existsSync(directory)) return;
  if (!fs.statSync(directory).isDirectory()) {
    errors.push(`${rel(directory)}: Aktenverzeichnis erwartet`);
    return;
  }
  const entries = fs.readdirSync(directory, { withFileTypes: true });
  const catalog = path.join(directory, 'aktenbestand.json');
  if (fs.existsSync(catalog)) {
    const inventory = readJson(catalog);
    const slugs = inventory && typeof inventory === 'object' && !Array.isArray(inventory) ? Object.keys(inventory) : [];
    const folders = entries.filter(entry => entry.isDirectory()).map(entry => entry.name);
    assert(fs.statSync(path.join(directory, 'README.md'), { throwIfNoEntry: false })?.isFile()
      && slugs.length > 0 && slugs.length === folders.length && slugs.every(slug => {
        if (!folders.includes(slug)) return false;
        const folder = path.join(directory, slug);
        const exports = inventory[slug]?.sha256;
        return fs.statSync(path.join(folder, 'README.md'), { throwIfNoEntry: false })?.isFile()
          && exports && typeof exports === 'object' && !Array.isArray(exports) && Object.keys(exports).length > 0
          && Object.entries(exports).every(([filename, hash]) => /^[a-f0-9]{64}$/.test(hash)
            && path.resolve(folder, filename).startsWith(folder + path.sep)
            && fs.statSync(path.join(folder, filename), { throwIfNoEntry: false })?.isFile());
      }), `${rel(directory)}: Fallverzeichnisse, README und Aktenbestand stimmen nicht überein`);
    return;
  }
  // Ein Depot verzeichneter Einzel-PDF-ZIPs gehört zu den zentralen Akten.
  const proof = path.join(directory, 'pruefung/bestand.json');
  if (fs.existsSync(proof)) {
    const inventory = readJson(proof);
    const downloads = path.join(directory, 'downloads');
    const assets = fs.statSync(downloads, { throwIfNoEntry: false })?.isDirectory() ? fs.readdirSync(downloads) : [];
    const cases = inventory?.cases;
    assert(inventory?.schema_version === 1 && Array.isArray(cases) && cases.length > 0
      && entries.length === 2 && assets.length === cases.length && new Set(cases.map(row => row?.slug)).size === cases.length
      && cases.every(row => {
        const name = `testakte-${row?.slug}-einzelpdfs.zip`;
        const file = path.join(downloads, name);
        return assets.includes(name) && row?.pdf_zip?.path === rel(file) && fs.statSync(file).isFile();
      }), `${rel(directory)}: PDF-Depot und Aktennachweis stimmen nicht überein`);
    return;
  }
  errors.push(`${rel(directory)}: Einzelakte unter testakte/ ablegen oder eine Aktensammlung mit Bestand ausweisen`);
}

function assert(condition, message) {
  if (!condition) errors.push(message);
}

const marketplace = readJson(path.join(root, '.claude-plugin', 'marketplace.json'));
if (!marketplace) process.exit(1);
const scopedPath = path.join(root, 'scripts', 'scoped-release-assets.json');
const scoped = fs.existsSync(scopedPath) ? readJson(scopedPath) : { schema_version: 1, assets: {} };
assert(scoped?.schema_version === 1 && scoped.assets && typeof scoped.assets === 'object' && !Array.isArray(scoped.assets), 'Komponentenregistrierung ungültig');

function componentTag(entry) {
  const tag = scoped?.assets?.[`${entry.name}.zip`];
  return typeof tag === 'string' && /^[a-z0-9][a-z0-9.-]*$/.test(tag) ? tag : null;
}

const pluginNames = marketplace.plugins.map((plugin) => plugin.name);
const sortedNames = [...pluginNames].sort((a, b) => a.localeCompare(b, 'de'));
assert(JSON.stringify(pluginNames) === JSON.stringify(sortedNames), 'Marketplace: Plugins sind nicht alphabetisch sortiert');
assert(new Set(pluginNames).size === pluginNames.length, 'Marketplace: doppelte Plugin-Namen');
assert(/^\d+\.\d+\.\d+$/.test(String(marketplace.version || '')), 'Marketplace: Version ist kein striktes x.y.z');

const oldReadmePhrases = [
  'Alternative ohne Plugin-Setup',
  'Spar-Alternative',
];

function hasObsoleteLengthInstruction(text) {
  // Dateigrößen beschreiben den Prompt, nicht die Länge seiner Fachantwort.
  const artifactTables = text.replace(
    /^(\| (?:Mini-Prompt|Schnellstart \/ Mini|Hauptproblem(?:-Prompt)?) \| [^|\r\n]*), h(?:ö|oe)chstens 7500 Zeichen und UTF-8-Bytes\.(?= \| [^\r\n]*download\.html\?path=[^\s)]+-(?:schnellstart|hauptproblem)\.(?:md|txt)\))/gmu,
    '$1.',
  );
  const withoutArtifactLimits = artifactTables.replace(
    /\b(?:Hauptproblem-Prompts?|Markdown-Prompts?|Markdown-Downloads?|Schnellstart-Prompts?)\s+mit\s+h(?:ö|oe)chstens 7500 Zeichen(?: und Bytes)?/gu,
    '',
  );
  return /h(?:ö|oe)chstens 7500 Zeichen/u.test(withoutArtifactLimits);
}

for (const entry of marketplace.plugins) {
  assert(/^[a-z0-9-]{1,64}$/.test(entry.name), `Marketplace:${entry.name}: ungültiger Slug`);
  assert(/^\d+\.\d+\.\d+$/.test(String(entry.version || '')) && (entry.version === marketplace.version || componentTag(entry)?.endsWith(`-v${entry.version}`)), `Marketplace:${entry.name}: Version ohne passendes Komponentenrelease`);
  assert(typeof entry.source === 'string' && entry.source.startsWith('./'), `Marketplace:${entry.name}: source muss mit ./ beginnen`);
  assert(typeof entry.description === 'string' && entry.description.length <= 300, `Marketplace:${entry.name}: description zu lang`);

  const pluginRoot = path.resolve(root, entry.source || '');
  assert(pluginRoot.startsWith(root + path.sep), `Marketplace:${entry.name}: source verlässt das Repository`);
  assert(fs.existsSync(pluginRoot), `Marketplace:${entry.name}: source fehlt`);

  const manifestPath = path.join(pluginRoot, '.claude-plugin', 'plugin.json');
  const manifest = fs.existsSync(manifestPath) ? readJson(manifestPath) : null;
  assert(Boolean(manifest), `${entry.name}: plugin.json fehlt`);
  if (manifest) {
    assert(manifest.name === entry.name, `${rel(manifestPath)}: name passt nicht zum Marketplace`);
    assert(manifest.version === entry.version, `${rel(manifestPath)}: Version passt nicht zum Marketplace-Eintrag`);
    assert(manifest.description === entry.description, `${rel(manifestPath)}: description passt nicht zum Marketplace`);
    assert(typeof manifest.description === 'string' && manifest.description.length <= 300, `${rel(manifestPath)}: description zu lang`);
  }

  errors.push(...promptProfileErrors(pluginRoot, entry.name, root));
  const werkstatt = path.join(pluginRoot, `${entry.name}-werkstatt.md`);
  const schnellstart = path.join(pluginRoot, `${entry.name}-schnellstart.md`);
  if (promptEnabled(entry.name, "werkstatt")) assert(fs.existsSync(werkstatt), `${entry.name}: Werkstatt-Markdown fehlt`);
  if (promptEnabled(entry.name, "schnellstart")) assert(fs.existsSync(schnellstart), `${entry.name}: Schnellstart-Markdown fehlt`);
  if (fs.existsSync(werkstatt)) {
    const size = fs.statSync(werkstatt).size;
    assert(size <= promptLimits.workshop_max_bytes, `${rel(werkstatt)}: Werkstatt ist größer als ${promptLimits.workshop_max_bytes} Bytes (${size} Bytes)`);
    // Technische Struktur prüfen, nicht Textvolumen als Fachqualität ausgeben.
    const text = readText(werkstatt);
    assert(text.startsWith('# ') && (text.match(/^# /gm) || []).length === 1,
      `${rel(werkstatt)}: eindeutige H1 am Dateianfang fehlt`);
    const sections = text.split(/^## [^\r\n]+\r?$/m).slice(1);
    assert(sections.length > 0 && sections.every((section) => section.replace(/<!--[^]*?-->/g, '').replace(/^#{1,6} .*$/gm, '').trim()),
      `${rel(werkstatt)}: gegliederter Abschnitt mit Inhalt fehlt`);
  }
  if (fs.existsSync(schnellstart)) {
    const size = fs.statSync(schnellstart).size;
    assert(miniWithinLimits(entry.name, fs.readFileSync(schnellstart)), `${rel(schnellstart)}: Schnellstart überschreitet Byte-/Zeichengrenze`);
  }

  const readme = path.join(pluginRoot, 'README.md');
  assert(fs.existsSync(readme), `${entry.name}: README.md fehlt`);
  if (fs.existsSync(readme)) {
    const text = readText(readme);
    const visibleVersion = text.match(/\*\*Version:\*\*\s*`?(\d+\.\d+\.\d+)`?/);
    assert(
      !visibleVersion || visibleVersion[1] === entry.version,
      `${rel(readme)}: sichtbare Version ${visibleVersion?.[1]} passt nicht zu ${entry.version}`,
    );
    const urls = downloadUrls(text);
    for (const phrase of oldReadmePhrases) {
      assert(!text.includes(phrase), `${rel(readme)}: alter Direkt-loslegen-Text gefunden`);
    }
    const releaseBase = 'https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download';
    const downloadBase = 'https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=';
    const relSource = entry.source.replace(/^\.\//, '');
    const tag = componentTag(entry);
    const pluginZip = tag ? `https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/${tag}/${entry.name}.zip` : `${releaseBase}/${entry.name}.zip`;
    const werkstattUrl = `${downloadBase}${relSource}/${entry.name}-werkstatt.md`;
    const schnellstartUrl = `${downloadBase}${relSource}/${entry.name}-schnellstart.md`;
    const primaryUrls = [pluginZip];
    if (promptEnabled(entry.name, "werkstatt")) primaryUrls.push(werkstattUrl);
    if (promptEnabled(entry.name, "schnellstart")) primaryUrls.push(schnellstartUrl);
    checkEntryMarkers(withoutCode(text), readme, primaryUrls);
    assert(urls.has(pluginZip), `${rel(readme)}: Plugin-ZIP-Link fehlt`);
    if (promptEnabled(entry.name, "werkstatt")) assert(urls.has(werkstattUrl), `${rel(readme)}: Werkstatt-Direktdownload fehlt`);
    if (promptEnabled(entry.name, "schnellstart")) assert(urls.has(schnellstartUrl), `${rel(readme)}: Schnellstart-Direktdownload fehlt`);
    for (const kind of promptKinds(entry.name)) {
      for (const ext of promptFormats(entry.name)) {
        assert(urls.has(`${downloadBase}${relSource}/${entry.name}-${kind}.${ext}`), `${rel(readme)}: ${kind}-${ext}-Direktdownload fehlt`);
      }
    }
    for (const match of text.matchAll(/<code>(.*?)<\/code>/g)) {
      assert(!/[^\x00-\x7F]/.test(match[1]), `${rel(readme)}: <code>-Tag enthält Nicht-ASCII-Text`);
    }
  }

  checkPluralCases(path.join(pluginRoot, 'testakten'));
}

// v393 entfernte diese Pfade und die daraus gebildeten Akten-Downloads.
// Das Wort „Scraping“ ist weiterhin ein Gegenstand der juristischen Prüfung.
const retiredSlugs = new Set([
  'beweissicherung-durch-testcrawler', 'db-006-scraping-website-datenbank-und-robots-txt',
  'db-016-preisvergleich-crawler-und-plattformvertrag', 'db-024-stellenanzeigen-jobportal-und-scraping',
  'db-027-verletzung-doku-hashlog-screenshot-crawl-protokoll', 'db-045-beweissicherung-durch-testcrawler',
  'preisvergleich-crawler-lizenzanalogie', 'stellenanzeigen-jobportal-und-scraping',
  'unwesentliche-teile-scraping-website-ki', 'verletzung-dokumentieren-hashlog-screenshot-crawl-protoko',
  'scraping-website-datenbank-und-robots-txt', 'scraping-api-terms', 'reseller-oem-sbom-software-scraping-api',
]);
const retiredCase = 'datenbankrecht-scraping-plattform-investitionsschutz';
function retiredPath(target) {
  if (!/scrap|crawl/i.test(target)) return false;
  return target.split(/[/?#=&]/).some(part => retiredSlugs.has(part)
    || part === retiredCase || part === `${retiredCase}_gesamt.pdf`
    || part === `testakte-${retiredCase}.zip` || part === `testakte-${retiredCase}-einzelpdfs.zip`);
}

function retiredLink(target) {
  const repository = '/Klotzkette/claude-fuer-deutsches-recht/';
  if (!/^(?:[a-z][a-z\d+.-]*:|\/\/)/i.test(target)) return retiredPath(target);
  let url;
  try {
    url = new URL(target, 'https://klotzkette.github.io/claude-fuer-deutsches-recht/');
  } catch {
    return false;
  }
  if (url.hostname === 'github.com' || url.hostname === 'raw.githubusercontent.com') {
    if (!url.pathname.toLowerCase().startsWith(repository.toLowerCase())) return false;
    const route = url.pathname.slice(repository.length);
    // Quellen auf historische Commits und Tags behalten ihren damaligen Pfad.
    if (!/^(?:(?:blob|tree|raw)\/(?:refs\/heads\/)?main\/|(?:refs\/heads\/)?main\/|releases\/(?:latest\/)?download\/)/.test(route)) return false;
  } else if (url.hostname !== 'klotzkette.github.io' || !url.pathname.startsWith('/claude-fuer-deutsches-recht/')) {
    return false;
  }
  return retiredPath(url.searchParams.get('path') || url.pathname);
}

for (const name of Object.keys(scoped?.assets || {})) {
  assert(!retiredPath(name), `${rel(scopedPath)}: abgelöstes Release-Asset ${name}`);
}
const files = walk(root);
const markdownFiles = files.filter(file => file.endsWith('.md'));
for (const name of files.map(rel).filter(retiredPath)) errors.push(`${name}: abgelöster Akten- oder Skillpfad`);
for (const file of markdownFiles) {
  const text = readText(file);
  assert(!/\[[^\]]+\]\(\)/.test(text), `${rel(file)}: leerer Markdown-Link`);
  for (const phrase of oldReadmePhrases) {
    assert(!text.includes(phrase), `${rel(file)}: alter Download-Text gefunden`);
  }
  assert(!hasObsoleteLengthInstruction(text), `${rel(file)}: alte Ausgabekürzung auf 7500 Zeichen gefunden`);
  if (/scrap|crawl/i.test(text)) {
    const targets = readmeProse(text).matchAll(/(?:\]\(\s*<?|^ {0,3}\[[^\]\n]+\]:\s*<?|href=["']|<(https?:\/\/))([^\s<>()"']+)/gim);
    for (const [, scheme = '', target] of targets) {
      const link = scheme + target;
      assert(!retiredLink(link), `${rel(file)}: Verweis auf abgelösten Akten- oder Skillpfad ${link}`);
    }
  }
}

const workflow = readText(path.join(root, '.github', 'workflows', 'release-plugin-zips.yml'));
for (const needle of [
  'testakte-*-einzelpdfs.zip',
]) {
  assert(workflow.includes(needle), `.github/workflows/release-plugin-zips.yml: ${needle} fehlt`);
}
for (const forbidden of [
  'alle-werkstatt-prompts.zip',
  'alle-schnellstart-prompts.zip',
]) {
  assert(!workflow.includes(forbidden), `.github/workflows/release-plugin-zips.yml: unerlaubtes Prompt-ZIP ${forbidden}`);
}
assert(
  !fs.existsSync(path.join(root, 'scripts', 'build-werkstatt-schnellstart-sammelzips.py')),
  'Sammel-ZIP-Builder für Werkstatt- und Schnellstart-Prompts ist nicht zulässig',
);

if (errors.length) {
  console.error(`audit-release-readiness: ${errors.length} Fehler`);
  for (const error of errors) console.error(`  FEHLER: ${error}`);
  process.exit(1);
}

console.log(`audit-release-readiness OK (${pluginNames.length} Plugins, ${markdownFiles.length} Markdown-Dateien)`);
