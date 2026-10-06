// Rebuild with a small external dependency directory; no npm/runtime in the ZIP.
// npm ci --prefix /tmp/portable-documents-build --ignore-scripts --no-audit --no-fund
// (Use docx-build-package.json and docx-build-package-lock.json there.)
// node docx-build-source.mjs /tmp/portable-documents-build
// API references: https://docx.js.org/api/classes/index.Packer.html
// https://github.com/101arrowz/fflate#zip-archives
// https://esbuild.github.io/api/#global-name
import { createRequire } from 'node:module';
import { readFile, writeFile, readdir } from 'node:fs/promises';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import { createHash } from 'node:crypto';

const output = dirname(fileURLToPath(import.meta.url));
const dependencies = resolve(process.argv[2] || '/tmp/portable-documents-build');
const require = createRequire(join(dependencies, 'package.json'));
const esbuild = require('esbuild');
const versions = { docx: '9.8.1', fflate: '0.8.3', esbuild: '0.28.2' };
for (const [name, version] of Object.entries(versions)) {
  const pkg = JSON.parse(await readFile(join(dependencies, 'node_modules', name, 'package.json')));
  if (pkg.version !== version) throw new Error(`Expected ${name}@${version}, found ${pkg.version}`);
}
for (const [name, contents] of [
  ['docx', 'export { Document, Paragraph, TextRun, Header, Tab, Packer } from "docx";'],
  ['fflate', 'export { zipSync, unzipSync, strToU8, strFromU8 } from "fflate";'],
]) {
  await esbuild.build({
    stdin: { contents, resolveDir: dependencies, sourcefile: `${name}-entry.js` },
    outfile: join(output, `${name}.iife.js`), bundle: true, platform: 'browser',
    format: 'iife', globalName: name, target: ['es2020'], minify: true,
    legalComments: 'inline', banner: { js: `/* ${name}@${versions[name]}; bundled by esbuild@${versions.esbuild}. See docx-vendor-LICENSES.txt. */` },
  });
}
const packages = [];
async function inventory(directory) {
  for (const entry of await readdir(directory, { withFileTypes: true })) {
    if (!entry.isDirectory() || entry.name.startsWith('.')) continue;
    const path = join(directory, entry.name);
    if (entry.name.startsWith('@')) { await inventory(path); continue; }
    const pkg = JSON.parse(await readFile(join(path, 'package.json')));
    if (pkg.name.startsWith('@esbuild/')) continue; // Build-host binary, never shipped.
    const licenses = (await readdir(path)).filter((name) => /^(licen[cs]e|copying|copyright|notice)(\.|$)/i.test(name));
    const licenseText = [];
    for (const filename of licenses.sort()) licenseText.push(`${filename}\n${await readFile(join(path, filename), 'utf8')}`);
    if (!licenses.length) {
      const readme = (await readdir(path)).find((name) => /^readme(?:\.md)?$/i.test(name));
      const contents = readme ? await readFile(join(path, readme), 'utf8') : '';
      const license = contents.match(/^#+ LICENSE\s*\n[\s\S]*$/im)?.[0];
      if (!license || !/copyright/i.test(license)) throw new Error(`Missing license: ${pkg.name}`);
      licenseText.push(`${readme} (license section)\n${license}`);
    }
    packages.push({ name: pkg.name, version: pkg.version, license: pkg.license, text: licenseText.join('\n') });
  }
}
await inventory(join(dependencies, 'node_modules'));
packages.sort((a, b) => a.name.localeCompare(b.name, 'en'));
await writeFile(join(output, 'docx-vendor-LICENSES.txt'), packages.map((pkg) => `${pkg.name}@${pkg.version} (${pkg.license})\n${'='.repeat(72)}\n${pkg.text}\n`).join('\n'));
const manifest = { versions, packages: packages.map(({ text, ...pkg }) => pkg), files: {} };
for (const name of ['docx.iife.js', 'fflate.iife.js', 'docx-vendor-LICENSES.txt']) {
  const bytes = await readFile(join(output, name));
  manifest.files[name] = { bytes: bytes.length, sha256: createHash('sha256').update(bytes).digest('hex') };
}
await writeFile(join(output, 'docx-vendor-manifest.json'), `${JSON.stringify(manifest, null, 2)}\n`);
for (const [source, target] of [['package.json', 'docx-build-package.json'], ['package-lock.json', 'docx-build-package-lock.json']]) {
  await writeFile(join(output, target), await readFile(join(dependencies, source)));
}
console.log(JSON.stringify(manifest.files, null, 2));
