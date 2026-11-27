// Hashbindungen der Marketplace-Prüfprofile an die bytegenaue Werkstatt-Vorfassung.
import { createHash } from 'node:crypto';
import fs from 'node:fs';
import path from 'node:path';
import { gunzipSync } from 'node:zlib';

const pin = JSON.parse(fs.readFileSync(new URL('./data/werkstatt-vorfassungen-20261127.json', import.meta.url)));
const digest = data => createHash('sha256').update(data).digest('hex');

export function workshopReviews(root) {
  const archive = path.join(root, pin.path);
  if (!fs.existsSync(archive)) {
    if (fs.existsSync(path.dirname(archive))) throw new Error('Prüfbeleg der Werkstatttexte fehlt');
    return {};
  }
  const data = gunzipSync(fs.readFileSync(archive));
  if (digest(data) !== pin.sha256) throw new Error('Prüfbeleg der Werkstatttexte verändert');
  return JSON.parse(data).files;
}

export function reviewedWorkshop(records, relative, plugin, content, expected) {
  const hash = digest(content);
  const row = records[relative];
  if (!row) return expected === hash;
  if (row.plugin !== plugin || hash !== row.after_sha256) return false;
  if (expected === hash) return true;
  if (expected !== row.before_sha256) return false;
  const parts = [];
  let cursor = 0;
  for (const [start, end, previous] of row.reverse) {
    if (!Number.isInteger(start) || !Number.isInteger(end)
        || start < cursor || end < start || end > content.length) return false;
    parts.push(content.subarray(cursor, start), Buffer.from(previous, 'utf8'));
    cursor = end;
  }
  parts.push(content.subarray(cursor));
  return digest(Buffer.concat(parts)) === expected;
}
