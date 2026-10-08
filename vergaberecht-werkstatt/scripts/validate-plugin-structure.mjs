#!/usr/bin/env node
import fs from 'node:fs';
import path from 'node:path';

const root = process.cwd();
const textExt = new Set(['.md', '.json', '.yaml', '.yml', '.py', '.sh']);
const errors = [];

function rel(file) {
  return path.relative(root, file).replaceAll(path.sep, '/');
}

// Lese-Cache: jede Datei wird genau einmal von der Platte gelesen, egal wie
// viele Checks sie anfassen (Links, Wortfamilien, Unicode, Frontmatter).
const readCache = new Map();
function read(file) {
  let text = readCache.get(file);
  if (text === undefined) {
    text = fs.readFileSync(file, 'utf8');
    readCache.set(file, text);
  }
  return text;
}

// Zeilen-Cache fuer die zeilenweisen Checks (verbotene Begriffe, Unicode).
const linesCache = new Map();
function linesOf(file) {
  let lines = linesCache.get(file);
  if (lines === undefined) {
    lines = read(file).split(/\r?\n/);
    linesCache.set(file, lines);
  }
  return lines;
}

function exists(file) {
  return fs.existsSync(file);
}

function walk(dir, predicate, out = []) {
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    if (entry.name === '.git') continue;
    if (entry.name === '.venv') continue;
    if (entry.name === 'dist') continue;
    if (entry.name === 'tmp') continue;
    if (entry.name === 'node_modules') continue;
    if (entry.name === '__pycache__') continue;
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) walk(full, predicate, out);
    else if (!predicate || predicate(full)) out.push(full);
  }
  return out;
}

// Der Baum wird genau einmal traversiert; alle Checks filtern diese Liste.
// Reihenfolge ist identisch zur bisherigen Einzel-Traversierung (readdirSync,
// rekursiv), daher bleiben Fehlerreihenfolge und -inhalt unveraendert.
const allFiles = walk(root);
function filesWhere(predicate) {
  return allFiles.filter(predicate);
}

function parseJson(file) {
  try {
    return JSON.parse(read(file));
  } catch (err) {
    errors.push(`${rel(file)}: invalid JSON: ${err.message}`);
    return null;
  }
}

function parseFrontmatter(file) {
  const text = read(file);
  const match = text.match(/^---\r?\n([\s\S]*?)\r?\n---\r?\n/);
  if (!match) {
    errors.push(`${rel(file)}: missing YAML frontmatter`);
    return null;
  }
  return match[1];
}

function topLevelField(frontmatter, field) {
  return new RegExp(`^${field}\\s*:`, 'm').test(frontmatter);
}

// Pfeile, Dingbats/Symbole, Sterne, Emoji. Paragraf-Zeichen wird separat geprueft.
const FORBIDDEN_SYMBOL_RE = /[←-⇿☀-➿⬀-⯿\u{1F000}-\u{1FAFF}]/u;

// Zentrale Pruefung fuer alle description-Felder (plugin.json, marketplace.json).
// Spiegelt die Marketplace-Regeln: Laengenlimit, keine Zahl-Komma-Zahl, keine
// spitzen Klammern, keine doppelten Anfuehrungszeichen, kein Paragraf-Zeichen,
// keine Emoji/Sonderzeichen-Symbole.
function checkDescription(label, desc, maxLen) {
  if (typeof desc !== 'string') {
    errors.push(`${label}: description must be a string`);
    return;
  }
  if (desc.length > maxLen) {
    errors.push(`${label}: description exceeds ${maxLen} chars (${desc.length})`);
  }
  if (/\d\s*,\s*\d/.test(desc)) {
    errors.push(`${label}: description darf keine Zahl-Komma-Zahl-Sequenz enthalten (Cowork-Validator bricht); nutze 'Rn', 'und' oder '/'`);
  }
  if (/[<>]/.test(desc)) {
    errors.push(`${label}: description enthaelt spitze Klammern (eckige Klammern verwenden)`);
  }
  if (desc.includes('"')) {
    errors.push(`${label}: description enthaelt doppelte Anfuehrungszeichen (einfache verwenden)`);
  }
  if (desc.includes('§')) {
    errors.push(`${label}: description enthaelt Paragraf-Zeichen (ausschreiben: Paragraf)`);
  }
  if (FORBIDDEN_SYMBOL_RE.test(desc)) {
    errors.push(`${label}: description enthaelt Emoji oder Sonderzeichen-Symbol (ausschreiben)`);
  }
}

function checkMarketplace() {
  const marketplacePath = path.join(root, '.claude-plugin', 'marketplace.json');
  const marketplace = parseJson(marketplacePath);
  if (!marketplace) return;
  if (!marketplace.version || !/^\d+\.\d+\.\d+$/.test(marketplace.version)) {
    errors.push('.claude-plugin/marketplace.json: version must be strict semver x.y.z');
  }
  if (marketplace.description !== undefined) {
    checkDescription('.claude-plugin/marketplace.json [top]', marketplace.description, 300);
  }
  if (!Array.isArray(marketplace.plugins) || marketplace.plugins.length === 0) {
    errors.push('.claude-plugin/marketplace.json: plugins must be a non-empty array');
    return;
  }
  const names = new Set();
  for (const plugin of marketplace.plugins) {
    if (!plugin.name || !/^[a-z0-9-]+$/.test(plugin.name)) {
      errors.push(`.claude-plugin/marketplace.json: invalid plugin name ${plugin.name}`);
    }
    if (names.has(plugin.name)) {
      errors.push(`.claude-plugin/marketplace.json: duplicate plugin name ${plugin.name}`);
    }
    names.add(plugin.name);
    if (plugin.description !== undefined) {
      checkDescription(`.claude-plugin/marketplace.json [${plugin.name}]`, plugin.description, 300);
    }
    if (!plugin.version || !/^\d+\.\d+\.\d+$/.test(plugin.version)) {
      errors.push(`.claude-plugin/marketplace.json [${plugin.name}]: version must be strict semver x.y.z`);
    } else if (marketplace.version && plugin.version !== marketplace.version) {
      errors.push(`.claude-plugin/marketplace.json [${plugin.name}]: version ${plugin.version} differs from marketplace version ${marketplace.version}`);
    }
    if (typeof plugin.source !== 'string' || !plugin.source.startsWith('./')) {
      errors.push(`${plugin.name}: source must be a relative path starting with ./`);
      continue;
    }
    const pluginRoot = path.resolve(root, plugin.source);
    if (!exists(pluginRoot)) errors.push(`${plugin.name}: source path missing: ${plugin.source}`);
    const manifestPath = path.join(pluginRoot, '.claude-plugin', 'plugin.json');
    if (!exists(manifestPath)) {
      errors.push(`${plugin.name}: missing .claude-plugin/plugin.json`);
      continue;
    }
    const manifest = parseJson(manifestPath);
    if (!manifest) continue;
    if (manifest.name !== plugin.name) {
      errors.push(`${rel(manifestPath)}: name does not match marketplace entry ${plugin.name}`);
    }
    if (manifest.version && plugin.version && manifest.version !== plugin.version) {
      errors.push(`${rel(manifestPath)}: version ${manifest.version} differs from marketplace entry ${plugin.version}`);
    }
    if (!manifest.version || typeof manifest.version !== 'string') {
      errors.push(`${rel(manifestPath)}: missing string version`);
    }
    if (manifest.author && (typeof manifest.author !== 'object' || Array.isArray(manifest.author) || !manifest.author.name)) {
      errors.push(`${rel(manifestPath)}: author must be an object with name`);
    }
    for (const unsupported of ['language', 'rechtsgebiet', 'adapted_from']) {
      if (Object.hasOwn(manifest, unsupported)) {
        errors.push(`${rel(manifestPath)}: unsupported manifest key ${unsupported}`);
      }
    }
    const legacyAgentsDir = path.join(pluginRoot, 'agenten');
    if (exists(legacyAgentsDir)) {
      errors.push(`${plugin.name}: use agents/ instead of legacy agenten/`);
    }
    if (manifest.agents) {
      for (const agentPath of Array.isArray(manifest.agents) ? manifest.agents : [manifest.agents]) {
        const resolved = path.resolve(pluginRoot, agentPath);
        if (!exists(resolved)) errors.push(`${rel(manifestPath)}: agents path missing: ${agentPath}`);
      }
    }
  }
}

function checkSkills() {
  // Offiziell von Claude Code/Cowork akzeptierte Frontmatter-Felder.
  // Quelle: code.claude.com/docs/en/plugins-reference und anthropics/skills.
  // Strikt: nur name + description; alles andere wird abgelehnt.
  const ALLOWED_SKILL_FIELDS = new Set([
    'name', 'description',
  ]);
  const skills = filesWhere(f => path.basename(f) === 'SKILL.md');
  for (const skill of skills) {
    const fm = parseFrontmatter(skill);
    if (!fm) continue;
    if (!topLevelField(fm, 'name')) errors.push(`${rel(skill)}: missing name`);
    if (!topLevelField(fm, 'description')) errors.push(`${rel(skill)}: missing description`);
    // Verbotene Felder explizit benennen für klare Fehlermeldung.
    for (const forbidden of ['triggers', 'when_to_use', 'language', 'rechtsgebiet',
                              'license', 'argument-hint', 'user-invocable',
                              'related_skills', 'allowed-tools', 'version']) {
      if (topLevelField(fm, forbidden)) {
        errors.push(`${rel(skill)}: forbidden frontmatter field '${forbidden}' — merge into description or remove`);
      }
    }
    // Unbekannte Top-Level-Felder erkennen (zusätzliche Sicherung).
    for (const line of fm.split(/\r?\n/)) {
      const m = line.match(/^([A-Za-z][\w-]*)\s*:/);
      if (!m) continue;
      if (!ALLOWED_SKILL_FIELDS.has(m[1])) {
        // Nur wenn nicht schon als forbidden gemeldet.
        const already = errors.some(e => e.includes(`'${m[1]}'`) && e.startsWith(rel(skill)));
        if (!already) {
          errors.push(`${rel(skill)}: unknown frontmatter field '${m[1]}' (only allowed: name, description)`);
        }
      }
    }
    const nameMatch = fm.match(/^name\s*:\s*['"]?([^\r\n'"]+)/m);
    if (nameMatch && !/^[a-z0-9-]{1,64}$/.test(nameMatch[1].trim())) {
      errors.push(`${rel(skill)}: invalid skill name ${nameMatch[1].trim()}`);
    }
    // description muss einzeilig sein (Cowork-Parser-Bug bei Multi-Line).
    const descMatch = fm.match(/^description\s*:\s*(.*)$/m);
    if (descMatch) {
      const v = descMatch[1].trim();
      if (v === '|' || v === '>' || v.startsWith('|') || v.startsWith('>')) {
        errors.push(`${rel(skill)}: description must be single-line (no | or > block style)`);
      }
      if (!['"', "'"].includes(v[0]) && /:\s/.test(v)) {
        errors.push(`${rel(skill)}: quote description because plain YAML scalars cannot safely contain ": "`);
      }
      if (v.length > 1024) {
        errors.push(`${rel(skill)}: description exceeds 1024 chars (${v.length})`);
      }
      if (/[<>]/.test(v)) {
        errors.push(`${rel(skill)}: description contains forbidden XML-style brackets`);
      }
      // Cowork-Validator bricht bei Zahl-Komma-Zahl-Sequenzen in description (z. B. 'BGHZ 217, 129').
      if (/\d\s*,\s*\d/.test(v)) {
        errors.push(`${rel(skill)}: description darf keine Zahl-Komma-Zahl-Sequenz enthalten (Cowork-Validator bricht); nutze 'Rn', 'und' oder '/'`);
      }
    }
  }
}

function checkPluginManifests() {
  // Strenge Semver-Prüfung für plugin.json: x.y.z ohne Pre-Release-Suffix.
  const manifests = filesWhere(f => f.endsWith(path.join('.claude-plugin', 'plugin.json')));
  for (const m of manifests) {
    const data = parseJson(m);
    if (!data) continue;
    if (data.version && !/^\d+\.\d+\.\d+$/.test(data.version)) {
      errors.push(`${rel(m)}: version '${data.version}' must be strict semver x.y.z (no pre-release suffix)`);
    }
    if (data.name && !/^[a-z0-9-]+$/.test(data.name)) {
      errors.push(`${rel(m)}: name '${data.name}' must be kebab-case`);
    }
    // Zentrale Description-Pruefung: Laenge (300), Zahl-Komma-Zahl, spitze
    // Klammern, doppelte Anfuehrungszeichen, Paragraf-Zeichen, Emoji/Symbole.
    if (data.description !== undefined) {
      checkDescription(rel(m), data.description, 300);
    }
  }
}

function checkMarkdownLinks() {
  const files = filesWhere(f => ['.md', '.yaml', '.yml', '.json'].includes(path.extname(f)));
  const linkPattern = /\[[^\]]*]\(([^)]+)\)/g;
  for (const file of files) {
    const text = read(file);
    for (const match of text.matchAll(linkPattern)) {
      const target = match[1].trim();
      if (/^(https?:|mailto:|#|\/)/.test(target)) continue;
      const clean = target.split('#')[0].replaceAll('%20', ' ');
      if (!clean || /^[A-Za-z]+:/.test(clean)) continue;
      const resolved = path.resolve(path.dirname(file), clean);
      if (!exists(resolved)) errors.push(`${rel(file)}: relative markdown link missing: ${target}`);
    }
  }
}

function checkForbiddenTerms() {
  // Regel 4: keine verbotenen Abruf-/Auslese-Wortfamilien in nutzerseitigem Inhalt.
  // Meta- und Tooling-Dateien sind ausgenommen, da sie die Regel selbst
  // dokumentieren; scripts/ enthaelt den Pruef-Code mit den Begriffen.
  const exempt = new Set(['CLAUDE.md', 'AGENTS.md', 'CODEX.md', 'CONTRIBUTING.md', 'CODE_OF_CONDUCT.md']);
  const terms = [
    's' + 'crape',
    's' + 'crapes',
    's' + 'craped',
    's' + 'craping',
    'cr' + 'awl',
    'cr' + 'awls',
    'cr' + 'awled',
    'cr' + 'awling',
  ];
  const term = new RegExp(`\\b(${terms.join('|')})\\b`, 'i');
  for (const file of filesWhere(f => path.extname(f) === '.md')) {
    if (rel(file).startsWith('scripts/')) continue;
    if (exempt.has(path.basename(file))) continue;
    const lines = linesOf(file);
    lines.forEach((line, index) => {
      if (term.test(line)) {
        errors.push(`${rel(file)}:${index + 1}: verbotener Abruf-/Auslese-Begriff — umformulieren (extrahieren, auslesen, abrufen, lesen)`);
      }
    });
  }
}

function checkSuspiciousCharacters() {
  const suspicious = /[\u0400-\u04ff\u200b-\u200f\u202a-\u202e\u2066-\u2069]/;
  for (const file of filesWhere(f => textExt.has(path.extname(f)))) {
    const lines = linesOf(file);
    lines.forEach((line, index) => {
      if (suspicious.test(line)) errors.push(`${rel(file)}:${index + 1}: suspicious unicode character`);
    });
  }
}

function checkTestaktenReadme() {
  const testaktenDir = path.join(root, 'testakten');
  if (!exists(testaktenDir)) return;
  const zipOptionalFolders = new Set(['megaprompts']);
  const readmePath = path.join(testaktenDir, 'README.md');
  if (!exists(readmePath)) {
    errors.push('testakten/README.md fehlt');
    return;
  }
  const entries = fs.readdirSync(testaktenDir, { withFileTypes: true });
  const folders = entries
    .filter(e => e.isDirectory() && !e.name.startsWith('.') && !zipOptionalFolders.has(e.name))
    .map(e => e.name)
    .sort();
  const readme = read(readmePath);
  const missing = [];
  for (const folder of folders) {
    const escaped = folder.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
    const linkPattern = new RegExp('\\(\\./' + escaped + '/(?:README\\.md)?\\)');
    if (!linkPattern.test(readme)) missing.push(folder);
  }
  if (missing.length) {
    errors.push(`testakten/README.md: ${missing.length} Akten-Ordner fehlen in der Tabelle: ${missing.join(', ')}`);
  }
  const tableMatches = [...readme.matchAll(/^\|[^\n]*\]\(\.\/([a-z0-9][a-z0-9-]*)\/README\.md\)/gm)];
  const tableFolders = new Set(tableMatches.map(match => match[1]));
  if (tableFolders.size !== folders.length) {
    errors.push(`testakten/README.md: ${tableFolders.size} Tabellen-Zeilen vs. ${folders.length} Ordner auf dem Dateisystem (Drift)`);
  }
  const zipPattern = /testakte-([a-z0-9][a-z0-9-]*)\.zip/g;
  const zipNames = new Set();
  for (const m of readme.matchAll(zipPattern)) zipNames.add(m[1]);
  const zipMissing = folders.filter(f => !zipNames.has(f) && !zipOptionalFolders.has(f));
  if (zipMissing.length) {
    errors.push(`testakten/README.md: ${zipMissing.length} Akten ohne ZIP-Download-Eintrag: ${zipMissing.join(', ')}`);
  }
}

function checkLocalSuffixArtifacts() {
  const suffixPattern = / [2-9](?:\.[^/.]+)?$/;
  for (const file of allFiles) {
    if (suffixPattern.test(path.basename(file))) {
      errors.push(`${rel(file)}: lokales Finder-/Sync-Suffixartefakt entfernen oder in die echte Zieldatei integrieren`);
    }
  }
}

function failIfErrors() {
  if (!errors.length) return;
  console.error(`validate-plugin-structure failed with ${errors.length} issue(s):`);
  for (const error of errors) console.error(`- ${error}`);
  process.exit(1);
}

checkLocalSuffixArtifacts();
failIfErrors();
checkMarketplace();
checkSkills();
checkPluginManifests();
checkMarkdownLinks();
checkForbiddenTerms();
checkSuspiciousCharacters();
checkTestaktenReadme();
failIfErrors();

console.log('validate-plugin-structure OK');
