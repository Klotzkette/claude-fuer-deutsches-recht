#!/usr/bin/env node
import fs from 'node:fs';
import path from 'node:path';

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

function walk(dir, predicate, out = []) {
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    if (['.git', 'node_modules', 'dist', '__pycache__'].includes(entry.name)) continue;
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) walk(full, predicate, out);
    else if (!predicate || predicate(full)) out.push(full);
  }
  return out;
}

function count(text, needle) {
  return text.split(needle).length - 1;
}

function regexpEscape(value) {
  return value.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
}

function assert(condition, message) {
  if (!condition) errors.push(message);
}

const marketplace = readJson(path.join(root, '.claude-plugin', 'marketplace.json'));
if (!marketplace) process.exit(1);

const pluginNames = marketplace.plugins.map((plugin) => plugin.name);
const sortedNames = [...pluginNames].sort((a, b) => a.localeCompare(b, 'de'));
assert(JSON.stringify(pluginNames) === JSON.stringify(sortedNames), 'Marketplace: Plugins sind nicht alphabetisch sortiert');
assert(new Set(pluginNames).size === pluginNames.length, 'Marketplace: doppelte Plugin-Namen');
assert(/^\d+\.\d+\.\d+$/.test(String(marketplace.version || '')), 'Marketplace: Version ist kein striktes x.y.z');

const oldReadmePhrases = [
  'Alternative ohne Plugin-Setup',
  'höchstens 7500 Zeichen',
  'hoechstens 7500 Zeichen',
  'Spar-Alternative',
];

const pluginSources = [];
for (const entry of marketplace.plugins) {
  assert(/^[a-z0-9-]{1,64}$/.test(entry.name), `Marketplace:${entry.name}: ungültiger Slug`);
  assert(entry.version === marketplace.version, `Marketplace:${entry.name}: Version passt nicht zu ${marketplace.version}`);
  assert(typeof entry.source === 'string' && entry.source.startsWith('./'), `Marketplace:${entry.name}: source muss mit ./ beginnen`);
  assert(typeof entry.description === 'string' && entry.description.length <= 300, `Marketplace:${entry.name}: description zu lang`);

  const pluginRoot = path.resolve(root, entry.source || '');
  pluginSources.push(pluginRoot);
  assert(pluginRoot.startsWith(root + path.sep), `Marketplace:${entry.name}: source verlässt das Repository`);
  assert(fs.existsSync(pluginRoot), `Marketplace:${entry.name}: source fehlt`);

  const manifestPath = path.join(pluginRoot, '.claude-plugin', 'plugin.json');
  const manifest = fs.existsSync(manifestPath) ? readJson(manifestPath) : null;
  assert(Boolean(manifest), `${entry.name}: plugin.json fehlt`);
  if (manifest) {
    assert(manifest.name === entry.name, `${rel(manifestPath)}: name passt nicht zum Marketplace`);
    assert(manifest.version === marketplace.version, `${rel(manifestPath)}: Version passt nicht zum Marketplace`);
    assert(manifest.description === entry.description, `${rel(manifestPath)}: description passt nicht zum Marketplace`);
    assert(typeof manifest.description === 'string' && manifest.description.length <= 300, `${rel(manifestPath)}: description zu lang`);
  }

  const werkstatt = path.join(pluginRoot, `${entry.name}-werkstatt.md`);
  const schnellstart = path.join(pluginRoot, `${entry.name}-schnellstart.md`);
  assert(fs.existsSync(werkstatt), `${entry.name}: Werkstatt-Markdown fehlt`);
  assert(fs.existsSync(schnellstart), `${entry.name}: Schnellstart-Markdown fehlt`);
  if (fs.existsSync(werkstatt)) {
    const size = fs.statSync(werkstatt).size;
    assert(size >= 12 * 1024 && size <= 22 * 1024, `${rel(werkstatt)}: Werkstatt-Größe außerhalb Zielkorridor (${size} Bytes)`);
  }
  if (fs.existsSync(schnellstart)) {
    const size = fs.statSync(schnellstart).size;
    assert(size <= 7500, `${rel(schnellstart)}: Schnellstart ist größer als 7500 Bytes`);
  }

  const readme = path.join(pluginRoot, 'README.md');
  assert(fs.existsSync(readme), `${entry.name}: README.md fehlt`);
  if (fs.existsSync(readme)) {
    const text = readText(readme);
    const begin = '<!-- BEGIN direkt-loslegen (autogen) -->';
    const end = '<!-- END direkt-loslegen (autogen) -->';
    assert(count(text, begin) === 1 && count(text, end) === 1, `${rel(readme)}: Direkt-loslegen-Block nicht eindeutig`);
    for (const phrase of oldReadmePhrases) {
      assert(!text.includes(phrase), `${rel(readme)}: alter Direkt-loslegen-Text gefunden`);
    }
    const releaseBase = 'https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download';
    const rawBase = 'https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main';
    const relSource = entry.source.replace(/^\.\//, '');
    const pluginZip = `${releaseBase}/${entry.name}.zip`;
    const werkstattUrl = `${rawBase}/${relSource}/${entry.name}-werkstatt.md`;
    const schnellstartUrl = `${rawBase}/${relSource}/${entry.name}-schnellstart.md`;
    assert(text.includes(pluginZip), `${rel(readme)}: Plugin-ZIP-Link fehlt`);
    assert(new RegExp(`<a href="${regexpEscape(werkstattUrl)}" download><code>${regexpEscape(entry.name)}-werkstatt\\.md</code></a>`).test(text), `${rel(readme)}: Werkstatt-Download-Tag fehlt`);
    assert(new RegExp(`<a href="${regexpEscape(schnellstartUrl)}" download><code>${regexpEscape(entry.name)}-schnellstart\\.md</code></a>`).test(text), `${rel(readme)}: Schnellstart-Download-Tag fehlt`);
    for (const match of text.matchAll(/<code>(.*?)<\/code>/g)) {
      assert(!/[^\x00-\x7F]/.test(match[1]), `${rel(readme)}: <code>-Tag enthält Nicht-ASCII-Text`);
    }
  }

  const pluralTestakten = path.join(pluginRoot, 'testakten');
  assert(!fs.existsSync(pluralTestakten), `${entry.name}: Plugin nutzt testakten/ statt testakte/`);
}

const markdownFiles = walk(root, (file) => file.endsWith('.md'));
for (const file of markdownFiles) {
  const text = readText(file);
  assert(!/\[[^\]]+\]\(\)/.test(text), `${rel(file)}: leerer Markdown-Link`);
  for (const phrase of oldReadmePhrases) {
    assert(!text.includes(phrase), `${rel(file)}: alter Download-Text gefunden`);
  }
}

const forbiddenFetchWords = ['scra' + 'pe', 'scra' + 'ping', 'cra' + 'wl', 'cra' + 'wling'];
for (const file of walk(root)) {
  const bytes = fs.readFileSync(file);
  const lowered = bytes.toString('latin1').toLowerCase();
  if (forbiddenFetchWords.some((word) => lowered.includes(word))) {
    errors.push(`${rel(file)}: verbotene Abruf-Wortform gefunden`);
  }
}

const workflow = readText(path.join(root, '.github', 'workflows', 'release-plugin-zips.yml'));
for (const needle of [
  'build-werkstatt-schnellstart-sammelzips.py',
  'alle-werkstatt-prompts.zip',
  'alle-schnellstart-prompts.zip',
  'testakte-*-einzelpdfs.zip',
]) {
  assert(workflow.includes(needle), `.github/workflows/release-plugin-zips.yml: ${needle} fehlt`);
}

if (errors.length) {
  console.error(`audit-release-readiness: ${errors.length} Fehler`);
  for (const error of errors) console.error(`  FEHLER: ${error}`);
  process.exit(1);
}

console.log(`audit-release-readiness OK (${pluginNames.length} Plugins, ${markdownFiles.length} Markdown-Dateien)`);
