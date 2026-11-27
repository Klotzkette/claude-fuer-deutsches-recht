import path from 'node:path';

// Änderungsprotokolle enthalten wortgetreue Vorher-/Nachher-Ausschnitte.
// Ihre relativen Links gehören zur protokollierten Quelldatei, nicht zum
// JSON-Verzeichnis. Alte Ausschnitte sind historische Belege; aktuelle Links
// werden im Nachher-Text und nochmals in der wirklichen Quelldatei geprüft.
export function auditLinkContexts(file, text, root) {
  const relative = path.relative(root, file).split(path.sep).join('/');
  if (relative === 'scripts/data/skill-cap-registry.json') {
    const data = JSON.parse(text);
    if (data.schema_version !== 1 || !Array.isArray(data.plugins)) throw new Error('Ungültige Skill-Registry');
    const contexts = [];
    for (const plugin of data.plugins) {
      if (typeof plugin.source !== 'string' || path.isAbsolute(plugin.source) || !Array.isArray(plugin.routes)) {
        throw new Error('Ungültiger Pluginpfad oder fehlende Arbeitswege in der Registry');
      }
      const pluginDir = path.resolve(root, plugin.source);
      if (!pluginDir.startsWith(path.resolve(root) + path.sep)) throw new Error('Pluginpfad verlässt das Repository');
      for (const route of plugin.routes) {
        if (typeof route.slug !== 'string' || !/^[a-z0-9]+(?:-[a-z0-9]+)*$/.test(route.slug)) {
          throw new Error('Ungültiger Arbeitsweg in der Registry');
        }
        const skill = path.join(pluginDir, 'skills', route.slug, 'SKILL.md');
        contexts.push({ file: skill, text: JSON.stringify(route) });
      }
      plugin.routes = [];
    }
    return [{ file, text: JSON.stringify(data) }, ...contexts];
  }
  const sourceMap = /^quality\/skill-consolidation\/\d{4}-\d{2}-\d{2}\/source-map\.json$/.test(relative);
  const miniAudit = /^quality\/source-audits\/\d{4}-\d{2}-\d{2}\/mini-laengenredaktion\.json$/.test(relative);
  const procurementAudit = /^quality\/skill-consolidation\/\d{4}-\d{2}-\d{2}\/vergaberecht-followup\.json$/.test(relative);
  if (!sourceMap && !miniAudit && !procurementAudit) return [{ file, text }];
  const data = JSON.parse(text);
  const rows = procurementAudit ? data.changes : data.files;
  if (!Array.isArray(rows) || ((sourceMap || procurementAudit) && data.schema_version !== 1)
      || (miniAudit && (typeof data.date !== 'string' || typeof data.method !== 'string'))) {
    throw new Error('Ungültiges Quellenänderungsprotokoll');
  }
  const contexts = [];
  for (const row of rows) {
    if (!row.edits) continue;
    if (!Array.isArray(row.edits) || typeof row.path !== 'string' || path.isAbsolute(row.path)) {
      throw new Error('Änderungsprotokoll benötigt einen relativen Quellpfad und Edits');
    }
    const source = path.resolve(root, row.path);
    if (!source.startsWith(path.resolve(root) + path.sep)) throw new Error('Quellpfad verlässt das Repository');
    for (const edit of row.edits) {
      const before = edit[miniAudit ? 'old' : 'before'];
      const after = edit[miniAudit ? 'new' : 'after'];
      if (typeof before !== 'string' || typeof after !== 'string') throw new Error('Vorher-/Nachher-Text fehlt');
      contexts.push({ file: source, text: after });
    }
    row.edits = [];
  }
  if (procurementAudit && data.renderer_delta) {
    // Dies ist Python-Quellcode, kein Markdown-Dokument. Seine erzeugten
    // Verweise werden oben an jedem betroffenen gerenderten Skill geprüft.
    if (data.renderer_delta.path !== 'scripts/consolidate-skill-cap.py'
        || !Array.isArray(data.renderer_delta.edits)
        || data.renderer_delta.edits.some(e => typeof e.before !== 'string' || typeof e.after !== 'string')) {
      throw new Error('Ungültiger dokumentierter Renderer-Codepatch');
    }
    data.renderer_delta.edits = [];
  }
  // Sonstige JSON-Felder bleiben der allgemeinen Linkkontrolle unterworfen.
  return [{ file, text: JSON.stringify(data) }, ...contexts];
}
