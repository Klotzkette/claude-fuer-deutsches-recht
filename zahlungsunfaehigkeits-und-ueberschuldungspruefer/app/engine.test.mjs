import assert from 'node:assert/strict'
import test from 'node:test'
import { readFileSync } from 'node:fs'
import { analyzeCase } from './engine.mjs'

const sample = () => JSON.parse(readFileSync(new URL('beispiel.json', import.meta.url)))
const checkDay = '2026-03-15'

function cash(id, amountCents, availableOn, decision = 'include') {
  return { id, description: 'Bank oder Zufluss', source: 'B1 Zeile 10', amountCents,
    kind: availableOn > checkDay ? 'inflow' : 'cash', availableOn, decision,
    reason: decision === 'exclude' ? 'Laut Bankbrief nicht frei verfügbar.' : '' }
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

test('Unter zehn Prozent verlangt die Zukunftsausnahme eine Verschärfung auf mehr als zehn Prozent', () => {
  const trend = { result: 'worsening_above_threshold', source: 'P2, Finanzplan Folgemonat',
    reason: 'Ohne weitere Finanzierung wächst die Lücke demnächst auf zwölf Prozent.' }
  const result = liquidity([cash('B', 95, checkDay)], [liability('P', 100, checkDay)], { gapTrend: trend })
  assert.equal(result.result, 'zu_candidate_worsening')
  assert.equal(result.totals.thresholdMet, false)
  assert.throws(() => liquidity([cash('B', 95, checkDay)], [liability('P', 100, checkDay)], {
    gapTrend: { ...trend, result: 'worsening_to_threshold' },
  }), /worsening_above_threshold/)
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
  delete row.overindebtedness.forecast.failureOn
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
  forecast.failureOn = '2027-02-01'
  assert.equal(analyzeCase(example).firstCandidate.overindebtedness, null)
  forecast.failureOn = '2027-01-31'
  assert.equal(analyzeCase(example).firstCandidate.overindebtedness.date, '2026-01-31')
})

test('Eine negative Jahresplanung unterstellt keinen konkreten Ausfalltag', () => {
  const example = sample()
  delete example.dates[0].overindebtedness.forecast.failureOn
  const report = analyzeCase(example)
  assert.equal(report.firstCandidate.overindebtedness, null)
  assert.equal(report.results[0].overindebtedness.forecast.failureOn, null)
  assert.match(report.results[0].overindebtedness.detail, /konkrete Zeitpunkt/)
})

const cessation = () => ({ result: 'established', source: 'Gläubiger-Mail G7 vom 15.03.2026',
  reason: 'Die Geschäftsführung erklärt dem Lieferanten, die erhebliche fällige Forderung binnen drei Wochen auch nicht ratenweise zahlen zu können.',
  establishedOn: checkDay, externalConduct: 'Erklärung der Geschäftsführerin an die Kreditorenabteilung des Lieferanten zu dessen fälliger Rechnung G7.',
  counterEvidence: 'Das zugesagte Bankgespräch enthält keine Kreditzusage. Eine allgemeine Wiederaufnahme der Zahlungen ist nicht belegt.' })

test('Zahlungseinstellung trägt einen getrennten Vermutungsbefund bei unvollständiger Rechnung', () => {
  const result = liquidity([], [], { complete: false, paymentCessation: cessation() })
  assert.equal(result.result, 'zu_candidate_cessation')
  assert.equal(result.arithmetic.result, 'open')
  assert.equal(result.paymentCessation.establishedOn, checkDay)
})

test('Widersprechende Beweiswege ergeben keine automatische Zahlungsunfähigkeit', () => {
  const result = liquidity([cash('B', 100, checkDay)], [liability('P', 100, checkDay)],
    { paymentCessation: cessation() })
  assert.equal(result.result, 'conflicting_evidence')
  assert.equal(result.arithmetic.result, 'covered_on_date')
  const second = liquidity([cash('B', 50, checkDay)], [liability('P', 100, checkDay)], {
    nearClosure: { result: 'not_established', source: 'B5', reason: 'Zusage fehlt.' },
    paymentCessation: { ...cessation(), result: 'rebutted', reason: 'Vollständige Wiederaufnahme wird behauptet.' },
  })
  assert.equal(second.result, 'conflicting_evidence')
  assert.equal(second.arithmetic.result, 'zu_candidate')
})

test('Zahlungseinstellung verlangt Außenverhalten, Gegenindizien und zeitgerechten Beleg', () => {
  assert.throws(() => liquidity([], [], { complete: false, paymentCessation: {
    ...cessation(), externalConduct: '', source: 'Nur interne Geschäftsführernotiz',
  } }), /externalConduct/)
  assert.throws(() => liquidity([], [], { complete: false, paymentCessation: {
    ...cessation(), counterEvidence: '',
  } }), /counterEvidence/)
  assert.throws(() => liquidity([], [], { complete: false, paymentCessation: {
    ...cessation(), establishedOn: '2026-03-16',
  } }), /erst später/)
})

test('Eine bloße Ratenbitte als offene Würdigung ersetzt keine Liquiditätsbilanz', () => {
  const result = liquidity([], [], { complete: false, paymentCessation: { result: 'open',
    source: 'Bitte um Ratenzahlung vom 15.03.2026', reason: 'Kein belegter Unfähigkeitsgrund.',
  } })
  assert.equal(result.result, 'open')
})

test('Historische Stichtage erhalten keinen ungeprüften Zwölfmonatshorizont', () => {
  const example = sample()
  example.dates = [example.dates[0]]
  const row = example.dates[0]
  row.date = '2023-06-01'
  row.overindebtedness.forecast = { result: 'negative', through: '2024-06-01', failureOn: '2023-11-01',
    source: 'Plan P1', reason: 'Ungedeckter Bedarf ab November 2023.' }
  let result = analyzeCase(example).results[0].overindebtedness
  assert.equal(result.result, 'open')
  assert.equal(result.forecast.requiredThrough, null)
  row.overindebtedness.historicalPeriod = { through: '2023-10-01',
    source: '§ 4 Abs. 2 SanInsKG, historische Fassung', reason: 'Für den Stichtag gilt der Viermonatszeitraum.' }
  result = analyzeCase(example).results[0].overindebtedness
  assert.equal(result.result, 'open')
  assert.equal(result.forecast.requiredThrough, '2023-10-01')
  row.overindebtedness.forecast.failureOn = '2023-10-01'
  assert.equal(analyzeCase(example).results[0].overindebtedness.result, 'ue_candidate')
})

test('Aktuelle Prognosezeiträume dürfen nicht durch historische Eingaben verkürzt werden', () => {
  const example = sample()
  example.dates[0].overindebtedness.historicalPeriod = { through: '2026-05-31', source: 'Altvorlage', reason: 'Vier Monate.' }
  assert.throws(() => analyzeCase(example), /nur für Stichtage vor 2024/)
})

test('Ausschluss einer Forderung verlangt eine konkrete Begründung', () => {
  const excluded = liability('P', 100, checkDay, 'exclude')
  assert.throws(() => liquidity([], [excluded]), /reason/)
  excluded.reason = 'Die Forderung wurde vor dem Stichtag durch dokumentierte Aufrechnung erfüllt.'
  assert.equal(liquidity([], [excluded]).totals.P1, 0)
})

test('Fehlender Kontoauszug überstimmt eine pauschale Vollständigkeitsbestätigung', () => {
  const result = liquidity([cash('B', 100, checkDay)], [liability('P', 100, checkDay)], {
    evidence: [{ id: 'BK2', description: 'Zweites Geschäftskonto', status: 'missing', reason: 'Auszug nicht übergeben.' }],
  })
  assert.equal(result.declaredComplete, true)
  assert.equal(result.complete, false)
  assert.equal(result.result, 'open')
  assert.match(result.detail, /BK2/)
})

test('Lücken bei Prognose und Vermögensstatus werden getrennt behandelt', () => {
  const example = sample()
  const section = example.dates[0].overindebtedness
  section.forecast = { result: 'positive', through: '2027-01-31', source: 'Plan P1', reason: 'Durchfinanzierung eingegeben.' }
  section.evidence = [{ id: 'FIN', description: 'Finanzierungszusage', scope: 'forecast', status: 'partial', reason: 'Unterschriebene Annahme fehlt.' }]
  assert.equal(analyzeCase(example).results[0].overindebtedness.result, 'open')
  section.evidence = [{ id: 'WERT', description: 'Maschinenbewertung', scope: 'positions', status: 'missing', reason: 'Bewertung noch nachzufordern.' }]
  assert.equal(analyzeCase(example).results[0].overindebtedness.result, 'positive_forecast')
  section.forecast.result = 'open'
  assert.equal(analyzeCase(example).results[0].overindebtedness.result, 'open')
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
