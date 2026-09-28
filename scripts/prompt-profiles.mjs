import fs from 'node:fs';
import path from 'node:path';

// Dieselbe versionierte Konfiguration wie prompt_profiles.py.
const config = JSON.parse(fs.readFileSync(new URL('./prompt-profiles.json', import.meta.url), 'utf8'));
if (config.schema_version !== 1 || !config.plugins || typeof config.plugins !== 'object') {
  throw new Error('Ungültige Promptprofil-Konfiguration');
}
const profiles = config.plugins;
const kinds = ['werkstatt', 'schnellstart', 'hauptproblem'];
export function promptEnabled(slug, kind) {
  const profile = profiles[slug];
  return kind === 'megaprompt' ? (profile?.megaprompt ?? true) : (profile?.standalone ?? kinds).includes(kind);
}
export function promptKinds(slug) { return profiles[slug]?.standalone ?? kinds.slice(0, 2); }
export function promptFormats(slug) { return profiles[slug]?.formats ?? ['md']; }

export function promptProfileErrors(directory, slug, root) {
  if (!profiles[slug]) return [];
  const errors = [];
  const expected = new Set(promptKinds(slug).flatMap(kind => promptFormats(slug).map(ext => `${slug}-${kind}.${ext}`)));
  for (const name of expected) {
    const file = path.join(directory, name);
    if (!fs.existsSync(file) || !fs.statSync(file).isFile() || !fs.statSync(file).size) errors.push(`${slug}: Prompt fehlt oder ist leer: ${name}`);
  }
  for (const name of fs.readdirSync(directory)) {
    if (/-(werkstatt|schnellstart|hauptproblem)\.(md|txt|docx|pdf)$/.test(name) && !expected.has(name)) errors.push(`${slug}: Prompt laut Profil nicht vorgesehen: ${name}`);
  }
  if (promptFormats(slug).includes('txt')) {
    for (const kind of promptKinds(slug)) {
      const md = path.join(directory, `${slug}-${kind}.md`);
      const txt = path.join(directory, `${slug}-${kind}.txt`);
      if (fs.existsSync(md) && fs.existsSync(txt) && !fs.readFileSync(md).equals(fs.readFileSync(txt))) errors.push(`${slug}: TXT und Markdown sind nicht byteidentisch: ${kind}`);
    }
  }
  if (!promptEnabled(slug, 'megaprompt') && fs.existsSync(path.join(root, 'testakten/megaprompts', `${slug}.md`))) errors.push(`${slug}: Megaprompt laut Profil nicht vorgesehen`);
  return errors;
}
