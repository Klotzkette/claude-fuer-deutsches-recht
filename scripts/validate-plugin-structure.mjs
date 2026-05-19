#!/usr/bin/env node
import fs from 'node:fs';
import path from 'node:path';

const root = process.cwd();
const textExt = new Set(['.md', '.json', '.yaml', '.yml', '.py', '.sh']);
const errors = [];

function rel(file) {
  return path.relative(root, file).replaceAll(path.sep, '/');
}

function read(file) {
  return fs.readFileSync(file, 'utf8');
}

function exists(file) {
  return fs.existsSync(file);
}

function walk(dir, predicate, out = []) {
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    if (entry.name === '.git') continue;
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) walk(full, predicate, out);
    else if (!predicate || predicate(full)) out.push(full);
  }
  return out;
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

function checkMarketplace() {
  const marketplacePath = path.join(root, '.claude-plugin', 'marketplace.json');
  const marketplace = parseJson(marketplacePath);
  if (!marketplace) return;
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
    if (plugin.name === 'liquiditaetsplanung') {
      // liquiditaetsplanung is the standalone Power-Plugin Liquiditätsvorschau.
      // It MUST work without insolvenzrecht/steuerberater-werkzeuge. Dependencies are
      // therefore optional (recommended companions, not required), but its own skills
      // must exist and be self-contained.
      const skills = walk(path.join(pluginRoot, 'skills'), f => path.basename(f) === 'SKILL.md');
      if (skills.length === 0) errors.push(`${plugin.name}: expected autark Liquiditätsvorschau skills`);
      for (const required of ['liquiditaetsvorschau-3wochen', 'liquiditaetsvorschau-3-6-12-monate', 'liquiditaetsvorschau-insolvenzrechtlich']) {
        const sp = path.join(pluginRoot, 'skills', required, 'SKILL.md');
        if (!exists(sp)) errors.push(`${plugin.name}: missing required standalone skill ${required}`);
      }
      for (const asset of ['assets/excel/Liquiditaetsplan-Wochenbasis.xlsx', 'assets/padlet/liquiditaets-padlet.html', 'assets/markdown/liquiditaets-artefakt-vorlage.md']) {
        if (!exists(path.join(pluginRoot, asset))) errors.push(`${plugin.name}: missing standalone asset ${asset}`);
      }
      const generator = 'skills/liquiditaetsvorschau-3-6-12-monate/werkzeuge/build_liquiditaetsplan.py';
      if (!exists(path.join(pluginRoot, generator))) errors.push(`${plugin.name}: missing standalone generator ${generator}`);
      // BGH-Volltexte werden NICHT mehr als PDF mitgeliefert (verstößt gegen Cowork-Upload-Limit ~1 MB).
      // Stattdessen ist eine INDEX.md mit Online-Verweisen auf die BGH-Datenbank Pflicht.
      const idx = path.join(pluginRoot, 'references', 'rechtsprechung', 'INDEX.md');
      if (!exists(idx)) errors.push(`${plugin.name}: missing references/rechtsprechung/INDEX.md (BGH-Onlinequellenverzeichnis)`);
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
  const skills = walk(root, f => path.basename(f) === 'SKILL.md');
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
    }
  }
}

function checkPluginManifests() {
  // Strenge Semver-Prüfung für plugin.json: x.y.z ohne Pre-Release-Suffix.
  const manifests = walk(root, f => f.endsWith(path.join('.claude-plugin', 'plugin.json')));
  for (const m of manifests) {
    const data = parseJson(m);
    if (!data) continue;
    if (data.version && !/^\d+\.\d+\.\d+$/.test(data.version)) {
      errors.push(`${rel(m)}: version '${data.version}' must be strict semver x.y.z (no pre-release suffix)`);
    }
    if (data.name && !/^[a-z0-9-]+$/.test(data.name)) {
      errors.push(`${rel(m)}: name '${data.name}' must be kebab-case`);
    }
  }
}

function checkManagedAgentReferences() {
  const base = path.join(root, 'verwaltete-agentenrezepte');
  if (!exists(base)) return;
  const files = walk(base, f => ['.yaml', '.yml'].includes(path.extname(f)));
  const refPattern = /\b(from_plugin|path|manifest):\s*([^}\r\n]+)/g;
  for (const file of files) {
    const text = read(file);
    for (const match of text.matchAll(refPattern)) {
      let target = match[2].trim().replace(/,$/, '').trim().replace(/^["']|["']$/g, '');
      if (!target.startsWith('.')) continue;
      const resolved = path.resolve(path.dirname(file), target);
      if (!exists(resolved)) errors.push(`${rel(file)}: ${match[1]} target missing: ${target}`);
    }
  }
}

function checkMarkdownLinks() {
  const files = walk(root, f => ['.md', '.yaml', '.yml', '.json'].includes(path.extname(f)));
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

function checkSuspiciousCharacters() {
  const suspicious = /[\u0400-\u04ff\u200b-\u200f\u202a-\u202e\u2066-\u2069]/;
  for (const file of walk(root, f => textExt.has(path.extname(f)))) {
    const lines = read(file).split(/\r?\n/);
    lines.forEach((line, index) => {
      if (suspicious.test(line)) errors.push(`${rel(file)}:${index + 1}: suspicious unicode character`);
    });
  }
}

checkMarketplace();
checkSkills();
checkPluginManifests();
checkManagedAgentReferences();
checkMarkdownLinks();
checkSuspiciousCharacters();

if (errors.length) {
  console.error(`validate-plugin-structure failed with ${errors.length} issue(s):`);
  for (const error of errors) console.error(`- ${error}`);
  process.exit(1);
}

console.log('validate-plugin-structure OK');
