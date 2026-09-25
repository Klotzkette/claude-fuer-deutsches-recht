import fs from 'node:fs';
import path from 'node:path';

// Fachlandkarten nennen Geschwister-Skills des jeweiligen Plugins. Ein
// gleichnamiger Skill in einem anderen Plugin repariert ein fehlendes Ziel nicht.
export function validateSkillMapReferences(skillFile, text) {
  const skillsRoot = path.dirname(path.dirname(skillFile));
  const errors = [];
  let mapDepth = null;
  let fence = null;

  for (const [index, line] of text.split(/\r?\n/).entries()) {
    const delimiter = line.match(/^\s*(`{3,}|~{3,})/);
    if (delimiter) {
      if (!fence) fence = delimiter[1];
      else if (delimiter[1][0] === fence[0] && delimiter[1].length >= fence.length) fence = null;
      continue;
    }
    if (fence) continue;

    const heading = line.match(/^(#{1,6})\s+(.+)$/);
    if (heading) {
      if (mapDepth !== null && heading[1].length <= mapDepth) mapDepth = null;
      if (/^(?:\d+(?:\.\d+)*\.?\s+)?Fachlandkarte\b/.test(heading[2])) mapDepth = heading[1].length;
      continue;
    }
    if (mapDepth === null) continue;

    const prefix = /^\s*(?:[-*+]\s+|\|\s*)/;
    if (!prefix.test(line)) continue;
    const entry = line.replace(prefix, '');
    const slug = entry.match(/^`([^`]+)`/);
    const link = entry.match(/^\[[^\]]+\]\(([^)]+)\)/);
    if (!slug && !link) continue;

    let target;
    let label;
    if (slug) {
      label = slug[1];
      if (!/^[a-z0-9-]{1,64}$/.test(label)) {
        errors.push(`Zeile ${index + 1}: Fachlandkarte enthält ungültigen Skill-Slug ${label}`);
        continue;
      }
      target = path.join(skillsRoot, label, 'SKILL.md');
    } else {
      label = link[1];
      target = path.resolve(path.dirname(skillFile), label.split('#', 1)[0]);
      if (!target.startsWith(skillsRoot + path.sep) || path.basename(target) !== 'SKILL.md') {
        errors.push(`Zeile ${index + 1}: Fachlandkarte muss auf einen Skill desselben Plugins zeigen: ${label}`);
        continue;
      }
    }
    if (!fs.existsSync(target) || !fs.statSync(target).isFile()) {
      errors.push(`Zeile ${index + 1}: Fachlandkarten-Ziel fehlt: ${label}`);
    }
  }
  return errors;
}
