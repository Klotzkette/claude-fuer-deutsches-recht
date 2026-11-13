import { readFileSync } from 'node:fs'
import { analyzeCase } from './engine.mjs'

const args = process.argv.slice(2)
if (args.includes('--help')) {
  process.stdout.write('Aufruf: node app/cli.mjs <fall.json|->\nOhne Dateinamen oder mit - liest der Rechner JSON über stdin.\n')
} else {
  try {
    if (args.length > 1) throw new Error('Genau einen Dateinamen oder - angeben.')
    const file = args[0] ?? '-'
    const input = JSON.parse(readFileSync(file === '-' ? 0 : file, 'utf8').replace(/^\uFEFF/, ''))
    process.stdout.write(JSON.stringify(analyzeCase(input), null, 2) + '\n')
  } catch (error) {
    process.stderr.write(`Prüfung abgebrochen: ${error.message}\n`)
    process.exitCode = 1
  }
}
