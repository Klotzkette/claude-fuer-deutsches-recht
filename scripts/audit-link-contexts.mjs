import path from 'node:path';

// Änderungsprotokolle enthalten wortgetreue Vorher-/Nachher-Ausschnitte.
// Ihre relativen Links gehören zur protokollierten Quelldatei, nicht zum
// JSON-Verzeichnis. Alte Ausschnitte sind historische Belege; aktuelle Links
// werden im Nachher-Text und nochmals in der wirklichen Quelldatei geprüft.
export function auditLinkContexts(file, text, root) {
  const relative = path.relative(root, file).split(path.sep).join('/');
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
