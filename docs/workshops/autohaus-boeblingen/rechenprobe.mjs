import assert from 'node:assert/strict'
import {readFileSync} from 'node:fs'
import vm from 'node:vm'
import {analyzeCase} from '../../../zahlungsunfaehigkeits-und-ueberschuldungspruefer/app/engine.mjs'

const read = relative => readFileSync(new URL(relative, import.meta.url), 'utf8')
const plan = JSON.parse(read('./kontrolle-liquiditaetsplaner.json'))
const status = JSON.parse(read('./kontrolle-insolvenzreife.json'))
const html = read('../../../liquiditaetsplanung/assets/padlet/liquiditaets-padlet.html')
const script = html.match(/<script>([\s\S]*?)<\/script>/)[1].replace(/\binit\(\);\s*$/, '')
const runtime = vm.createContext({Intl, Date, Number, JSON})
vm.runInContext(script, runtime)
runtime.loadState(plan)
const result = vm.runInContext('calculateLiquidity(state)', runtime)
const separated = analyzeCase(status).results[0]
assert.equal(result.missing.length, 0)
assert.deepEqual(Array.from(result.liqE), [-9500, -16000, -16000])
assert.equal(result.luecke, 16000)
assert.equal(result.quote, 16000 / 130000)
for (const [key, appValue] of Object.entries({A1:result.aI, A2:result.aII, P1:result.pI, P2:result.pII})) {
  assert.equal(separated.liquidity.totals[key], appValue * 100)
}
assert.equal(separated.liquidity.totals.remainingGapCents, result.luecke * 100)
assert.equal(separated.liquidity.result, 'zu_candidate')
assert.equal(separated.overindebtedness.result, 'ue_candidate')
assert.equal(separated.overindebtedness.totals.uncoveredCents, 7700000)
assert.equal(separated.overindebtedness.forecast.requiredThrough, '2027-09-25')
console.log('Beide Importe stimmen bei allen vier Rechengrößen überein. Liquiditätslücke 16.000 Euro, Unterdeckung 77.000 Euro.')
