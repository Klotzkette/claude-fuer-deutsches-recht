import path from 'node:path';
import { existsSync, statSync } from 'node:fs';
import { createRequire } from 'node:module';
import { pathToFileURL } from 'node:url';

const configured = process.env.AKTEN_NODE_MODULES;
if (configured && (!existsSync(configured) || !statSync(configured).isDirectory())) {
  throw new Error('AKTEN_NODE_MODULES muss auf ein vorhandenes node_modules-Verzeichnis zeigen.');
}
const resolvers = configured
  ? [createRequire(path.join(path.resolve(configured), '_runtime.cjs'))]
  : [
      createRequire(import.meta.url),
      createRequire(path.resolve(path.dirname(process.execPath), '../node_modules/_runtime.cjs')),
    ];
const packages = ['@oai/artifact-tool', 'jszip', 'xml-js'];
let runtime;
for (const candidate of resolvers) {
  try {
    for (const name of packages) candidate.resolve(name);
    runtime = candidate;
    break;
  } catch {
    // Erst den normalen Paketpfad, danach die laufzeitnahe Installation prüfen.
  }
}
if (!runtime) {
  throw new Error('Tabellenwerkzeuge fehlen: @oai/artifact-tool, jszip und xml-js im lokalen node_modules bereitstellen oder AKTEN_NODE_MODULES auf ein vorhandenes node_modules-Verzeichnis setzen.');
}
export const requireRuntime = runtime;
export const { Workbook, SpreadsheetFile } = await import(pathToFileURL(runtime.resolve('@oai/artifact-tool')).href);
if (process.argv.includes('--check-runtime')) {
  console.log('Tabellenlaufzeit verfügbar; keine Akten verändert.');
  process.exit(0);
}
