import assert from 'node:assert/strict'
import test from 'node:test'
import { readFileSync } from 'node:fs'
import { analyzeCase } from '../zahlungsunfaehigkeits-und-ueberschuldungspruefer/app/engine.mjs'

const fixturePath = new URL('./data/zu-insolvenzfaelle.json', import.meta.url)
const { cases } = JSON.parse(readFileSync(fixturePath, 'utf8'))
const order = ['CB', 'BZ', 'PR']
const casesByPrefix = new Map(cases.map(c => [c.prefix, c]))

const variants = {
  CB: {
    liquidity: [['CB-BANK-02', 9_450_000, 'zu_candidate'], ['CB-PAT-01', 0, 'covered_on_date']],
    overindebtedness: [['CB-NR-01', 4_455_650, 'assets_cover']],
  },
  BZ: {
    liquidity: [['BZ-BANK-01', 9_000_000, 'zu_candidate'], ['BZ-PAT-01', 0, 'covered_on_date']],
    overindebtedness: [['BZ-NR-01', -28_660_000, 'ue_candidate'], ['BZ-INV-01', 24_840_000, 'assets_cover']],
  },
  PR: {
    liquidity: [['PR-RES-01', 11_445_000, 'zu_candidate'], ['PR-PAT-02', 0, 'covered_on_date']],
    overindebtedness: [['PR-INV-02', 161_200_000, 'assets_cover']],
  },
}

function findings(caseInput, date) {
  const result = analyzeCase(caseInput).results.find(item => item.date === date)
  assert.ok(result, 'Erwarteter Stichtag fehlt')
  return result
}

test('Fallbestand und Belegketten der zwei Bankjahre', () => {
  assert.deepEqual([...casesByPrefix.keys()].sort(), [...order].sort())
  for (const caseData of cases) {
    const bank = new Map()
    let balance = caseData.opening_bank_balance_cents
    let previousDay = caseData.history_start
    for (const row of caseData.transactions) {
      assert.ok(row.date >= previousDay && row.date <= caseData.history_end, row.id)
      previousDay = row.date
      assert.equal(bank.has(row.id), false, row.id)
      bank.set(row.id, row)
      balance += row.amount_cents
      assert.equal(balance, row.balance_cents, row.id)
    }
    assert.equal(new Set([...bank.values()].map(row => row.date.slice(0, 7))).size, 24)
    for (const [rows, dateKey, sign] of [
      [caseData.obligations, 'paid_on', -1], [caseData.receivables, 'received_on', 1],
    ]) {
      for (const row of rows.filter(record => record.payment_id)) {
        const payment = bank.get(row.payment_id)
        assert.ok(payment, row.id)
        assert.equal(payment.amount_cents, sign * row.amount_cents, row.id)
        assert.equal(payment.value_on, row[dateKey], row.id)
      }
    }
  }
})

test('Getrennte Erstbefunde, davor geprüfte Tage und erwartete Centwerte', () => {
  for (const caseData of cases) {
    const control = caseData.control
    const report = analyzeCase(control.engine_input)
    const label = caseData.prefix
    const publicControlName = caseData.slug.replace(/^insolvenzreife-/, '') + '-recheninput.json'
    const publicControlPath = new URL('../quality/insolvenzreife/' + publicControlName, import.meta.url)
    assert.deepEqual(JSON.parse(readFileSync(publicControlPath, 'utf8')), control.engine_input, label)
    assert.deepEqual(report.results.map(r => r.date), [...caseData.status_dates].sort(), label)
    assert.equal(report.firstCandidate.liquidity.date, control.first_zu, label)
    assert.equal(report.firstCandidate.overindebtedness.date, control.first_ue, label)
    assert.notEqual(control.first_zu, control.first_ue, label)
    for (const candidate of Object.values(report.firstCandidate)) {
      assert.ok(candidate.previousContraryDate < candidate.date, label)
      assert.ok(candidate.date < caseData.procedure.petition_on, label)
      assert.ok(caseData.procedure.petition_on < caseData.procedure.opened_on, label)
    }
    for (const { date, liquidity, overindebtedness } of report.results) {
      const expected = control.amounts[date]
      if ('aktiva_1_cents' in expected) {
        const { A1, A2, P1, P2, remainingGapCents } = liquidity.totals
        assert.deepEqual([A1, A2, P1, P2], [
          expected.aktiva_1_cents, expected.aktiva_2_cents, expected.passiva_1_cents, expected.passiva_2_cents,
        ], label)
        assert.equal(remainingGapCents, Math.max(0, P1 + P2 - A1 - A2), label)
        assert.equal(liquidity.timeline.at(-1).gapCents, remainingGapCents, label)
      }
      if ('vermoegen_cents' in expected) {
        assert.equal(overindebtedness.totals.assetsCents, expected.vermoegen_cents, label)
        assert.equal(overindebtedness.totals.liabilitiesCents, expected.verbindlichkeiten_cents, label)
      }
    }
  }
})

test('Banklinien, Patronat, Nachrang und Verwertung ändern nur den gewählten Prüfzweig', () => {
  for (const caseData of cases) {
    const { engine_input: input, first_zu: firstZU, first_ue: firstUE } = caseData.control
    const alternatives = variants[caseData.prefix]
    for (const [field, date, comparison] of [
      ['liquidity', firstZU, 'overindebtedness'],
      ['overindebtedness', firstUE, 'liquidity'],
    ]) {
      const baseline = findings(input, date)
      for (const [id, amount, result] of alternatives[field]) {
        const changed = structuredClone(input)
        const section = changed.dates.find(entry => entry.date === date)[field]
        const position = [...section.assets, ...section.liabilities].find(item => item.id === id)
        assert.ok(position, id)
        if (id === 'BZ-INV-01') {
          const prev = input.dates.find(entry => entry.date < date
            && entry.overindebtedness?.assets.some(row => row.id === id))
          position.amountCents = prev.overindebtedness.assets.find(row => row.id === id).amountCents
        } else if (id === 'PR-INV-02') {
          position.amountCents = 210000000
          position.decision = 'include'
        } else {
          position.decision = position.decision === 'exclude' ? 'include' : 'exclude'
        }
        const scenario = findings(changed, date)
        const total = scenario[field].totals
        assert.equal(total.remainingGapCents ?? total.netAssetsCents, amount, id)
        assert.equal(scenario[field].result, result, id)
        assert.deepEqual(scenario[comparison], baseline[comparison], id)
      }
    }
  }
})
