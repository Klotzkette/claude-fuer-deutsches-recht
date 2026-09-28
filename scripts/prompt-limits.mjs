import fs from 'node:fs';
export const promptLimits = JSON.parse(fs.readFileSync(new URL('./prompt-limits.json', import.meta.url), 'utf8'));
export function miniWithinLimits(slug, data) {
  const custom = promptLimits.mini_by_plugin?.[slug] ?? {};
  const byteLimit = custom.max_bytes ?? promptLimits.mini_max_bytes;
  const charLimit = custom.max_characters ?? promptLimits.mini_max_bytes;
  return data.length > 0 && data.length <= byteLimit && Array.from(data.toString('utf8')).length <= charLimit;
}
