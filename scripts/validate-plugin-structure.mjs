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
      for (const pdf of ['BGH_II_ZR_88-16_vom_2017-12-19.pdf', 'BGH_II_ZR_112-21_vom_2022-06-28.pdf', 'BGH_IX_ZR_48-21_vom_2022-04-28.pdf', 'BGH_IX_ZR_229-22_vom_2025-01-23.pdf', 'BGH_II_ZR_139-23_vom_2025-03-11.pdf']) {
        if (!exists(path.join(pluginRoot, 'references', 'rechtsprechung', pdf))) errors.push(`${plugin.name}: missing BGH PDF references/rechtsprechung/${pdf}`);
      }
    }
  }
}

function checkSkills() {
  const skills = walk(root, f => path.basename(f) === 'SKILL.md');
  for (const skill of skills) {
    const fm = parseFrontmatter(skill);
    if (!fm) continue;
    if (!topLevelField(fm, 'name')) errors.push(`${rel(skill)}: missing name`);
    if (!topLevelField(fm, 'description')) errors.push(`${rel(skill)}: missing description`);
    if (topLevelField(fm, 'triggers')) errors.push(`${rel(skill)}: use when_to_use instead of triggers`);
    const nameMatch = fm.match(/^name\s*:\s*['"]?([^\r\n'"]+)/m);
    if (nameMatch && !/^[a-z0-9-]{1,64}$/.test(nameMatch[1].trim())) {
      errors.push(`${rel(skill)}: invalid skill name ${nameMatch[1].trim()}`);
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
checkManagedAgentReferences();
checkMarkdownLinks();
checkSuspiciousCharacters();

if (errors.length) {
  console.error(`validate-plugin-structure failed with ${errors.length} issue(s):`);
  for (const error of errors) console.error(`- ${error}`);
  process.exit(1);
}

console.log('validate-plugin-structure OK');
