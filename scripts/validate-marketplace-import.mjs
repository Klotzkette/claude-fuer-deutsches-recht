#!/usr/bin/env node
import fs from 'node:fs';
import path from 'node:path';

const root = process.cwd();
const errors = [];
const warnings = [];

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
    if (entry.name === '.git' || entry.name === 'node_modules' || entry.name === 'dist') continue;
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) walk(full, predicate, out);
    else if (!predicate || predicate(full)) out.push(full);
  }
  return out;
}

function hasEmoji(text) {
  return /[\u{1F000}-\u{1FAFF}\u{2600}-\u{27BF}]/u.test(text);
}

function checkDescription(label, value, limit) {
  if (typeof value !== 'string' || value.trim() === '') {
    errors.push(`${label}: description fehlt oder ist leer`);
    return;
  }
  if (value.length > limit) errors.push(`${label}: description zu lang (${value.length} > ${limit})`);
  if (/[0-9]\s*,\s*[0-9]/.test(value)) errors.push(`${label}: description enthält Zahl-Komma-Zahl`);
  if (/[<>]/.test(value)) errors.push(`${label}: description enthält spitze Klammern`);
  if (hasEmoji(value)) errors.push(`${label}: description enthält Emoji oder Symbolbild`);
}

function parseSkillFrontmatter(file) {
  const text = readText(file);
  const match = text.match(/^---\r?\n([\s\S]*?)\r?\n---\r?\n/);
  if (!match) {
    errors.push(`${rel(file)}: Frontmatter fehlt oder ist nicht terminiert`);
    return null;
  }
  const fields = {};
  for (const line of match[1].split(/\r?\n/)) {
    const field = line.match(/^([A-Za-z][A-Za-z0-9-]*)\s*:\s*(.*)$/);
    if (!field) continue;
    fields[field[1]] = field[2].trim().replace(/^['"]|['"]$/g, '');
  }
  const allowed = new Set(['name', 'description']);
  for (const key of Object.keys(fields)) {
    if (!allowed.has(key)) errors.push(`${rel(file)}: unerlaubtes Frontmatter-Feld ${key}`);
  }
  if (!fields.name) errors.push(`${rel(file)}: name fehlt`);
  if (!fields.description) errors.push(`${rel(file)}: description fehlt`);
  return fields;
}

function checkSkillFile(file) {
  const fields = parseSkillFrontmatter(file);
  if (!fields) return;
  const folder = path.basename(path.dirname(file));
  if (!/^[a-z0-9-]{1,64}$/.test(fields.name)) {
    errors.push(`${rel(file)}: Skill-Name ist kein gültiger Slug`);
  }
  if (fields.name !== folder) {
    errors.push(`${rel(file)}: Skill-Name entspricht nicht dem Ordnernamen`);
  }
  if (fields.description.length < 80) {
    warnings.push(`${rel(file)}: description ist kurz (${fields.description.length} Zeichen)`);
  }
  checkDescription(rel(file), fields.description, 1024);
}

const marketplacePath = path.join(root, '.claude-plugin', 'marketplace.json');
const marketplace = readJson(marketplacePath);
if (!marketplace) process.exit(1);

checkDescription('.claude-plugin/marketplace.json', marketplace.description, 300);
if (!/^\d+\.\d+\.\d+$/.test(String(marketplace.version || ''))) {
  errors.push('.claude-plugin/marketplace.json: version ist kein striktes x.y.z');
}
if (!Array.isArray(marketplace.plugins) || marketplace.plugins.length === 0) {
  errors.push('.claude-plugin/marketplace.json: plugins fehlt oder ist leer');
}

const seen = new Set();
let lastName = '';
let skillCount = 0;
let readmeCount = 0;

for (const entry of marketplace.plugins || []) {
  if (!entry.name || !/^[a-z0-9-]+$/.test(entry.name)) {
    errors.push(`Marketplace: ungültiger Plugin-Name ${entry.name}`);
    continue;
  }
  if (seen.has(entry.name)) errors.push(`Marketplace: doppelter Plugin-Name ${entry.name}`);
  seen.add(entry.name);
  if (lastName && lastName.localeCompare(entry.name) > 0) {
    errors.push(`Marketplace: Sortierung verletzt bei ${lastName} vor ${entry.name}`);
  }
  lastName = entry.name;
  checkDescription(`Marketplace:${entry.name}`, entry.description, 300);
  if (entry.version !== marketplace.version) {
    errors.push(`Marketplace:${entry.name}: Version ${entry.version} passt nicht zu ${marketplace.version}`);
  }
  if (typeof entry.source !== 'string' || !entry.source.startsWith('./')) {
    errors.push(`Marketplace:${entry.name}: source muss mit ./ beginnen`);
    continue;
  }
  const pluginRoot = path.resolve(root, entry.source);
  if (!pluginRoot.startsWith(root + path.sep)) {
    errors.push(`Marketplace:${entry.name}: source verlässt das Repository`);
    continue;
  }
  if (!fs.existsSync(pluginRoot) || !fs.statSync(pluginRoot).isDirectory()) {
    errors.push(`Marketplace:${entry.name}: source fehlt`);
    continue;
  }
  const manifestPath = path.join(pluginRoot, '.claude-plugin', 'plugin.json');
  const manifest = readJson(manifestPath);
  if (!manifest) continue;
  if (manifest.name !== entry.name) errors.push(`${rel(manifestPath)}: name passt nicht zum Marketplace`);
  if (manifest.version !== marketplace.version) errors.push(`${rel(manifestPath)}: Version passt nicht zum Marketplace`);
  checkDescription(rel(manifestPath), manifest.description, 300);
  if (!manifest.author || manifest.author.name !== 'Klotzkette') errors.push(`${rel(manifestPath)}: author.name fehlt oder ist falsch`);
  if (!manifest.author || manifest.author.email !== '39582916+Klotzkette@users.noreply.github.com') {
    errors.push(`${rel(manifestPath)}: author.email fehlt oder ist falsch`);
  }
  const skillsDir = path.join(pluginRoot, 'skills');
  if (!fs.existsSync(skillsDir)) errors.push(`${entry.name}: skills/ fehlt`);
  const skillFiles = fs.existsSync(skillsDir) ? walk(skillsDir, (file) => path.basename(file) === 'SKILL.md') : [];
  if (skillFiles.length === 0) errors.push(`${entry.name}: keine Skills gefunden`);
  for (const skill of skillFiles) checkSkillFile(skill);
  skillCount += skillFiles.length;
  const suspiciousSkillPaths = fs.existsSync(skillsDir)
    ? walk(skillsDir, (file) => /(?:schnellstart|megaprompt|miniprompt)/i.test(file))
    : [];
  for (const suspicious of suspiciousSkillPaths) {
    errors.push(`${rel(suspicious)}: Schnellstart- oder Prompt-Datei liegt unter skills/`);
  }
  const werkstatt = path.join(pluginRoot, `${entry.name}-werkstatt.md`);
  const schnellstart = path.join(pluginRoot, `${entry.name}-schnellstart.md`);
  if (!fs.existsSync(werkstatt)) errors.push(`${entry.name}: Werkstatt-Markdown fehlt`);
  if (!fs.existsSync(schnellstart)) errors.push(`${entry.name}: Schnellstart-Markdown fehlt`);
  if (fs.existsSync(schnellstart) && fs.statSync(schnellstart).size > 7500) {
    errors.push(`${rel(schnellstart)}: Schnellstart ist größer als 7500 Bytes`);
  }
  if (fs.existsSync(werkstatt)) {
    const size = fs.statSync(werkstatt).size;
    if (size < 12 * 1024 || size > 22 * 1024) errors.push(`${rel(werkstatt)}: Werkstatt-Größe außerhalb Zielkorridor (${size} Bytes)`);
  }
  const readme = path.join(pluginRoot, 'README.md');
  if (!fs.existsSync(readme)) {
    errors.push(`${entry.name}: README.md fehlt`);
  } else {
    readmeCount += 1;
    const text = readText(readme);
    const sourceRel = String(entry.source || `./${entry.name}`).replace(/^\.\//, '');
    const werkstattRaw = `https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/${sourceRel}/${entry.name}-werkstatt.md`;
    const schnellstartRaw = `https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/${sourceRel}/${entry.name}-schnellstart.md`;
    if (!text.includes(werkstattRaw) || !new RegExp(`<a href="${werkstattRaw.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')}" download>`).test(text)) {
      errors.push(`${rel(readme)}: Werkstatt-Direktdownload fehlt oder ist nicht als download markiert`);
    }
    if (!text.includes(schnellstartRaw) || !new RegExp(`<a href="${schnellstartRaw.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')}" download>`).test(text)) {
      errors.push(`${rel(readme)}: Schnellstart-Direktdownload fehlt oder ist nicht als download markiert`);
    }
    for (const line of text.split(/\r?\n/)) {
      const cells = line.startsWith('|') ? line.split('|').slice(1, -1).map((cell) => cell.trim()) : [];
      if (cells.length >= 3 && /(?:Prompt|Werkstatt|Schnellstart)/i.test(cells[0]) && /^ZIP$/i.test(cells[1])) {
        errors.push(`${rel(readme)}: Werkstatt- oder Schnellstart-Prompt wird als ZIP angeboten`);
      }
    }
  }
}

const manifestCount = walk(root, (file) => file.endsWith(`${path.sep}.claude-plugin${path.sep}plugin.json`)).length;
if (manifestCount !== seen.size) {
  errors.push(`Manifestanzahl ${manifestCount} passt nicht zur Marketplace-Anzahl ${seen.size}`);
}

console.log(`Marketplace-Importprüfung: ${seen.size} Plugins, ${skillCount} Skills, ${readmeCount} README-Dateien`);
if (warnings.length) {
  console.log(`Warnungen: ${warnings.length}`);
  for (const warning of warnings.slice(0, 20)) console.log(`  WARN: ${warning}`);
}
if (errors.length) {
  console.error(`Fehler: ${errors.length}`);
  for (const error of errors) console.error(`  FEHLER: ${error}`);
  process.exit(1);
}
console.log('OK');
