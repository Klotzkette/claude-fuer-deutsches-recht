import assert from 'node:assert/strict'
import test from 'node:test'
import { readFileSync } from 'node:fs'
import { analyzeCase } from './engine.mjs'

const sample = () => JSON.parse(readFileSync(new URL('beispiel.json', import.meta.url)))
const checkDay = '2026-03-15'

function cash(id, amountCents, availableOn, decision = 'include') {
  return { id, description: 'Bank oder Zufluss', source: 'B1 Zeile 10', amountCents,
    kind: availableOn > checkDay ? 'inflow' : 'cash', availableOn, decision }
}

function liability(id, amountCents, dueOn, decision = 'include') {
  return { id, description: 'Forderung', source: 'Rechnung R1 S. 1', amountCents, dueOn, decision }
}

function liquidity(assets, liabilities, additions = {}) {
  return analyzeCase({ caseName: 'Testfall', dates: [{ date: checkDay, liquidity: {
    complete: true, assets, liabilities, ...additions,
  } }] }).results[0].liquidity
}

test('Die beiden frühesten stützenden Tage sind getrennt und chronologisch', () => {
  const example = sample()
  example.dates.reverse()
  const report = analyzeCase(example)
  assert.equal(report.firstCandidate.liquidity.date, '2026-03-15')
  assert.equal(report.firstCandidate.overindebtedness.date, '2026-01-31')
  assert.equal(report.firstCandidate.liquidity.previousExaminedDate, null)
  assert.equal(report.results[0].overindebtedness.totals.uncoveredCents, 2000000)
})

test('Passiva II und der 21. Tag zählen, der 22. Tag bleibt sichtbar außerhalb', () => {
  const result = liquidity(
    [cash('B', 80, checkDay), cash('K', 50, '2026-04-05'), cash('L', 100, '2026-04-06')],
    [liability('V1', 100, checkDay), liability('V2', 50, '2026-04-05'), liability('V3', 200, '2026-04-06')],
  )
  assert.deepEqual(result.totals, { A1: 80, P1: 100, A2: 50, P2: 50, windowAssetsCents: 130,
    windowLiabilitiesCents: 150, immediateGapCents: 20, remainingGapCents: 20,
    remainingGapBasisPoints: 1333, thresholdMet: true })
  assert.equal(result.result, 'near_closure_open')
  assert.equal(result.items.find(row => row.id === 'L').group, 'outside_window')
  assert.equal(result.timeline.length, 22)
  assert.equal(result.timeline.at(-1).gapCents, 20)
})

test('Die Zehnprozentgrenze entscheidet exakt auch bei Rundung auf denselben Prozentwert', () => {
  const finding = { nearClosure: { result: 'not_established', source: 'B5', reason: 'Zusage fehlt.' } }
  const exactly = liquidity([cash('B', 90_000, checkDay)], [liability('P', 100_000, checkDay)], finding)
  const justBelow = liquidity([cash('B', 90_001, checkDay)], [liability('P', 100_000, checkDay)], finding)
  assert.equal(exactly.result, 'zu_candidate')
  assert.equal(exactly.totals.remainingGapBasisPoints, 1000)
  assert.equal(justBelow.totals.remainingGapBasisPoints, 1000)
  assert.equal(justBelow.totals.thresholdMet, false)
  assert.equal(justBelow.result, 'below_threshold_open')
})

test('Eine bloß zukünftige Fälligkeit gibt am Stichtag keinen §-17-Kandidaten', () => {
  const result = liquidity([], [liability('P', 1000, '2026-03-16')])
  assert.equal(result.result, 'covered_on_date')
  assert.equal(result.totals.remainingGapCents, 1000)
})

test('Offene Position im Fenster hemmt den Befund, ausgeschlossene Mittel fließen nicht ein', () => {
  const result = liquidity([cash('B', 20, checkDay), cash('U', 80, '2026-03-16', 'exclude')],
    [liability('P', 100, checkDay), liability('O', null, null, 'open')])
  assert.equal(result.totals.A2, 0)
  assert.equal(result.result, 'open')
  assert.match(result.detail, /Position O/)
})

test('Belegte Nachrang-Einordnung gilt nur in ihrem Abschnitt', () => {
  const example = sample()
  const row = example.dates[0].overindebtedness.liabilities[1]
  const liquidRow = { ...row, decision: 'include', dueOn: example.dates[1].date }
  example.dates[1].liquidity.liabilities.push(liquidRow)
  const report = analyzeCase(example)
  assert.equal(report.results[0].overindebtedness.totals.liabilitiesCents, 17000000)
  assert.equal(report.results[1].liquidity.totals.P1, 7000000)
})

test('Positive Prognose muss das volle Jahr abdecken, einschließlich Schaltjahr', () => {
  const example = sample()
  const row = example.dates[0]
  row.date = '2024-02-29'
  row.overindebtedness.forecast.result = 'positive'
  row.overindebtedness.forecast.through = '2025-02-27'
  assert.equal(analyzeCase(example).results[0].overindebtedness.result, 'open')
  row.overindebtedness.forecast.through = '2025-02-28'
  assert.equal(analyzeCase(example).results[0].overindebtedness.result, 'positive_forecast')
})

test('Fehlende Vermögensposition oder offene Prognose verhindert einen Überschuldungskandidaten', () => {
  const example = sample()
  const section = example.dates[0].overindebtedness
  section.assets[0].decision = 'open'
  assert.equal(analyzeCase(example).firstCandidate.overindebtedness, null)
  section.assets[0].decision = 'include'
  section.forecast = { result: 'open' }
  assert.equal(analyzeCase(example).firstCandidate.overindebtedness, null)
})

test('Abbruch nach dem Zwölfmonatshorizont trägt keinen negativen Befund', () => {
  const example = sample()
  const forecast = example.dates[0].overindebtedness.forecast
  forecast.through = '2027-02-01'
  assert.equal(analyzeCase(example).firstCandidate.overindebtedness, null)
  forecast.failureOn = '2027-01-31'
  assert.equal(analyzeCase(example).firstCandidate.overindebtedness.date, '2026-01-31')
})

test('Frühere offene und frühere gegenläufige Befunde bleiben unterscheidbar', () => {
  const example = sample()
  example.dates.push({ date: '2026-03-13', liquidity: {
    complete: true, assets: [], liabilities: [],
  } }, { date: '2026-03-14', liquidity: {
    complete: false, assets: [], liabilities: [],
  } })
  const candidate = analyzeCase(example).firstCandidate.liquidity
  assert.equal(candidate.previousExaminedDate, '2026-03-14')
  assert.equal(candidate.previousExaminedResult, 'open')
  assert.equal(candidate.previousContraryDate, '2026-03-13')
})

test('Doppelte Positionen und ungültige Daten brechen nachvollziehbar ab', () => {
  const row = cash('X', 10, checkDay)
  assert.throws(() => liquidity([row, row], []), /Doppelte Position X/)
  assert.throws(() => liquidity([{ ...row, amountCents: 1.2 }], []), /Centbetrag/)
  assert.throws(() => liquidity([{ ...row, availableOn: '2026-02-30' }], []), /Kalenderdatum/)
  assert.throws(() => liquidity([{ ...row, kind: 'inflow' }], []), /verfügbaren Bestand/)
})
