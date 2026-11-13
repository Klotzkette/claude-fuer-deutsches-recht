const DAY_MS = 86_400_000
const WINDOW_DAYS = 21

const decisions = ['include', 'exclude', 'open']
const closureResults = ['established', 'not_established', 'open']
const trendResults = ['worsening_to_threshold', 'not_expected', 'open']
const forecasts = ['positive', 'negative', 'open']

const labels = {
  open: 'Befund offen',
  covered_on_date: 'Fällige Pflichten am Stichtag gedeckt',
  covered_in_window: 'Rechnerische Deckung im Dreiwochenfenster',
  zu_candidate: 'Stichtag spricht für Zahlungsunfähigkeit',
  zu_candidate_worsening: 'Stichtag spricht wegen absehbarer Verschlechterung für Zahlungsunfähigkeit',
  near_closure_exception: 'Belegte Ausnahme trotz Lücke von mindestens zehn Prozent',
  near_closure_open: 'Ausnahme wegen kurzfristiger Schließung noch zu prüfen',
  below_threshold: 'Restlücke unter zehn Prozent und kein absehbares Anwachsen auf die Schwelle',
  below_threshold_open: 'Restlücke unter zehn Prozent, Entwicklung offen',
  positive_forecast: 'Belegte positive Fortbestehensprognose',
  assets_cover: 'Vermögen deckt Verbindlichkeiten zu den angesetzten Werten',
  ue_candidate: 'Stichtag spricht für insolvenzrechtliche Überschuldung',
}

function record(value, path) {
  if (!value || typeof value !== 'object' || Array.isArray(value)) {
    throw new Error(`${path}: Objekt erwartet.`)
  }
  return value
}

function string(value, path, { optional = false } = {}) {
  if (optional && (value === undefined || value === null)) return ''
  if (typeof value !== 'string' || (!optional && value.trim() === '')) {
    throw new Error(`${path}: ${optional ? 'Text' : 'Nicht leerer Text'} erwartet.`)
  }
  return value.trim()
}

function choice(value, options, path) {
  if (!options.includes(value)) {
    throw new Error(`${path}: Erlaubt sind ${options.join(', ')}.`)
  }
  return value
}

function list(value, path) {
  if (!Array.isArray(value)) throw new Error(`${path}: Liste erwartet.`)
  return value
}

function boolean(value, path) {
  if (typeof value !== 'boolean') throw new Error(`${path}: true oder false erwartet.`)
  return value
}

function cents(value, path, optional = false) {
  if (optional && (value === null || value === undefined)) return null
  if (!Number.isSafeInteger(value) || value < 0) {
    throw new Error(`${path}: Nicht negativer, ganzzahliger Centbetrag erwartet.`)
  }
  return value
}

function date(value, path, optional = false) {
  if (optional && (value === null || value === undefined)) return null
  const day = typeof value === 'string' ? Date.parse(`${value}T00:00:00Z`) / DAY_MS : NaN
  if (!/^\d{4}-\d{2}-\d{2}$/.test(value) || !Number.isInteger(day) || isoDay(day) !== value
      || value < '0001-01-01' || value >= '9999-01-01') {
    throw new Error(`${path}: Kalenderdatum im Format JJJJ-MM-TT erwartet.`)
  }
  return day
}

function isoDay(day) {
  return new Date(day * DAY_MS).toISOString().slice(0, 10)
}

function oneYearAfter(day) {
  const [year, month, dayOfMonth] = isoDay(day).split('-').map(Number)
  const monthText = String(month).padStart(2, '0')
  const nextYear = String(year + 1).padStart(4, '0')
  const lastDay = new Date(`${nextYear}-${monthText}-28T00:00:00Z`)
  lastDay.setUTCMonth(month, 0)
  const nextDay = String(Math.min(dayOfMonth, lastDay.getUTCDate())).padStart(2, '0')
  return Date.parse(`${nextYear}-${monthText}-${nextDay}T00:00:00Z`) / DAY_MS
}

function readRows(value, path, timing = null) {
  const ids = new Set()
  return list(value, path).map((item, index) => {
    const at = `${path}[${index}]`
    const row = record(item, at)
    const id = string(row.id, `${at}.id`)
    if (ids.has(id)) throw new Error(`${at}.id: Doppelte Position ${id}.`)
    ids.add(id)
    const decision = choice(row.decision, decisions, `${at}.decision`)
    const open = decision === 'open'
    const source = string(row.source, `${at}.source`, { optional: open })
    const result = {
      id,
      description: string(row.description, `${at}.description`),
      amountCents: cents(row.amountCents, `${at}.amountCents`, open),
      decision,
      source,
      reason: string(row.reason, `${at}.reason`, { optional: true }),
    }
    if (timing === 'availableOn') result.kind = choice(row.kind, ['cash', 'inflow'], `${at}.kind`)
    if (timing) result.day = date(row[timing], `${at}.${timing}`, open)
    return result
  })
}

function assessment(value, options, path) {
  if (value === undefined || value === null) return { result: 'open', source: '', reason: '' }
  const entry = record(value, path)
  const result = choice(entry.result, options, `${path}.result`)
  const optional = result === 'open'
  return {
    result,
    source: string(entry.source, `${path}.source`, { optional }),
    reason: string(entry.reason, `${path}.reason`, { optional }),
  }
}

function notes(value, path) {
  if (value === undefined) return []
  return list(value, path).map((note, index) => string(note, `${path}[${index}]`))
}

function safeSum(a, b) {
  const sum = a + b
  if (!Number.isSafeInteger(sum)) throw new Error('Summe überschreitet den exakten Centbereich.')
  return sum
}

function percentBasisPoints(gap, liabilities) {
  if (liabilities === 0) return null
  return Number((BigInt(gap) * 10_000n + BigInt(liabilities) / 2n) / BigInt(liabilities))
}

function status(code, detail) {
  return { result: code, label: labels[code], detail }
}

function liquidityStatus(totals, missing, nearClosure, gapTrend) {
  if (missing.length) return status('open', missing.join(' '))
  const { A1, P1, immediateGapCents, remainingGapCents, thresholdMet } = totals
  if (immediateGapCents === 0) {
    return status('covered_on_date', A1 > 0 || P1 > 0
      ? 'Die fälligen Pflichten sind am Stichtag gedeckt. Eine spätere Lücke ist separat zu prüfen.'
      : 'Für den Stichtag sind keine fälligen Pflichten erfasst. Prüfen Sie spätere Fälligkeitstermine separat.')
  }
  if (remainingGapCents === 0) {
    return status('covered_in_window', 'Die belegten Mittel decken die Pflichten im Dreiwochenfenster. Prüfen Sie bei Widersprüchen den tagesgenauen Verlauf und Belege für eine Zahlungseinstellung.')
  }
  if (!thresholdMet) {
    if (gapTrend.result === 'worsening_to_threshold') {
      return status('zu_candidate_worsening', gapTrend.reason)
    }
    if (gapTrend.result === 'not_expected') return status('below_threshold', gapTrend.reason)
    return status('below_threshold_open', 'Prüfen Sie, ob ein zeitnahes Anwachsen der Restlücke auf mindestens zehn Prozent absehbar war.')
  }
  if (nearClosure.result === 'established') return status('near_closure_exception', nearClosure.reason)
  if (nearClosure.result === 'not_established') return status('zu_candidate', nearClosure.reason)
  return status('near_closure_open', 'Prüfen Sie, ob eine baldige nahezu vollständige Schließung mit an Sicherheit grenzender Wahrscheinlichkeit zu erwarten war und den Gläubigern das Zuwarten zumutbar war.')
}

function calculateLiquidity(input, day, path) {
  const section = record(input, path)
  const complete = boolean(section.complete, `${path}.complete`)
  const horizon = day + WINDOW_DAYS
  const totals = { A1: 0, P1: 0, A2: 0, P2: 0 }
  const daily = Array.from({ length: WINDOW_DAYS + 1 }, () => ({ assetsCents: 0, liabilitiesCents: 0 }))
  const missing = complete ? [] : ['Die Erfassung des Dreiwochenfensters ist unvollständig.']
  const nearClosure = assessment(section.nearClosure, closureResults, `${path}.nearClosure`)
  const gapTrend = assessment(section.gapTrend, trendResults, `${path}.gapTrend`)
  const items = ['assets', 'liabilities'].flatMap((side) => {
    const asset = side === 'assets'
    const timing = asset ? 'availableOn' : 'dueOn'
    return readRows(section[side], `${path}.${side}`, timing).map(({ day: rowDay, ...row }) => {
      const timeGroup = rowDay === null ? 'open' : rowDay > horizon ? 'outside_window'
        : (asset ? 'A' : 'P') + (rowDay <= day ? '1' : '2')
      if (row.decision === 'open' && timeGroup !== 'outside_window') {
        missing.push(`Position ${row.id} ist offen.`)
      }
      if (row.decision === 'include' && asset && row.kind === 'inflow' && rowDay <= day) {
        throw new Error(`${path}: Position ${row.id} als verfügbaren Bestand am Stichtag erfassen oder als Zufluss nach dem Stichtag datieren.`)
      }
      if (row.decision === 'include' && timeGroup !== 'outside_window') {
        totals[timeGroup] = safeSum(totals[timeGroup], row.amountCents)
        const flow = daily[Math.max(0, rowDay - day)]
        const field = asset ? 'assetsCents' : 'liabilitiesCents'
        flow[field] = safeSum(flow[field], row.amountCents)
      }
      return { ...row, [timing]: rowDay === null ? null : isoDay(rowDay), group: timeGroup, side }
    })
  })
  const windowAssetsCents = safeSum(totals.A1, totals.A2)
  const windowLiabilitiesCents = safeSum(totals.P1, totals.P2)
  const remainingGapCents = Math.max(0, windowLiabilitiesCents - windowAssetsCents)
  Object.assign(totals, {
    windowAssetsCents,
    windowLiabilitiesCents,
    immediateGapCents: Math.max(0, totals.P1 - totals.A1),
    remainingGapCents,
    remainingGapBasisPoints: percentBasisPoints(remainingGapCents, windowLiabilitiesCents),
    thresholdMet: windowLiabilitiesCents > 0 && BigInt(remainingGapCents) * 10n >= BigInt(windowLiabilitiesCents),
  })
  let available = 0
  let due = 0
  const timeline = daily.map((flow, index) => {
    available = safeSum(available, flow.assetsCents)
    due = safeSum(due, flow.liabilitiesCents)
    return { date: isoDay(day + index), ...flow, cumulativeAssetsCents: available,
      cumulativeLiabilitiesCents: due, gapCents: Math.max(0, due - available) }
  })
  return {
    ...liquidityStatus(totals, missing, nearClosure, gapTrend),
    complete,
    windowThrough: isoDay(horizon),
    totals,
    items,
    timeline,
    nearClosure,
    gapTrend,
    notes: notes(section.notes, `${path}.notes`),
  }
}

function calculateOverindebtedness(input, day, path) {
  const section = record(input, path)
  const complete = boolean(section.complete, `${path}.complete`)
  const requiredThrough = oneYearAfter(day)
  const forecast = assessment(section.forecast, forecasts, `${path}.forecast`)
  const forecastDay = date(section.forecast?.through, `${path}.forecast.through`, forecast.result === 'open')
  const failureDay = date(section.forecast?.failureOn, `${path}.forecast.failureOn`, true)
  if (forecastDay !== null && forecastDay < day) {
    throw new Error(`${path}.forecast.through: Das Prognosedatum muss am oder nach dem Stichtag liegen.`)
  }
  if (failureDay !== null && (forecast.result !== 'negative' || failureDay < day || failureDay > forecastDay)) {
    throw new Error(`${path}.forecast.failureOn: Der belegte Abbruch muss innerhalb der negativen Prognose liegen.`)
  }
  const effectiveFailureDay = forecast.result === 'negative' ? (failureDay ?? forecastDay) : null
  const items = ['assets', 'liabilities'].flatMap((side) =>
    readRows(section[side], `${path}.${side}`).map(row => ({ ...row, side })),
  )
  const sumSide = (side) => items
    .filter(row => row.side === side && row.decision === 'include')
    .reduce((sum, row) => safeSum(sum, row.amountCents), 0)
  const assetsCents = sumSide('assets')
  const liabilitiesCents = sumSide('liabilities')
  const uncoveredCents = Math.max(0, liabilitiesCents - assetsCents)
  const openRows = items.filter(row => row.decision === 'open')
  let finding
  if (forecast.result === 'positive' && forecastDay >= requiredThrough) {
    finding = status('positive_forecast', forecast.reason)
  } else if (!complete || openRows.length) {
    const gaps = openRows.length ? `Offene Positionen: ${openRows.map(row => row.id).join(', ')}.` : ''
    finding = status('open', `Die Vermögensdeckung ist noch nicht vollständig belegt. ${gaps}`.trim())
  } else if (uncoveredCents === 0) {
    finding = status('assets_cover', 'Der Status ergibt zu den belegten Ansätzen keine Unterdeckung.')
  } else if (effectiveFailureDay !== null && effectiveFailureDay <= requiredThrough) {
    finding = status('ue_candidate', forecast.reason)
  } else {
    let detail = 'Die belegte Unterdeckung genügt bei offener Fortbestehensprognose noch nicht für einen Befund.'
    if (forecast.result === 'positive') detail = `Die positive Prognose deckt den Zeitraum bis ${isoDay(requiredThrough)} nicht ab.`
    if (forecast.result === 'negative') detail = `Der angegebene Finanzierungsabbruch liegt nach dem Prognosehorizont bis ${isoDay(requiredThrough)}.`
    finding = status('open', detail)
  }
  return {
    ...finding,
    complete,
    totals: { assetsCents, liabilitiesCents, uncoveredCents, netAssetsCents: assetsCents - liabilitiesCents },
    forecast: { ...forecast, through: forecastDay === null ? null : isoDay(forecastDay),
      failureOn: effectiveFailureDay === null ? null : isoDay(effectiveFailureDay), requiredThrough: isoDay(requiredThrough) },
    items,
    notes: notes(section.notes, `${path}.notes`),
  }
}

function earliestCandidate(results, field, codes) {
  const index = results.findIndex(row => codes.includes(row[field].result))
  if (index < 0) return null
  const earlier = results.slice(0, index)
  const previousExamined = earlier.findLast(row => row[field].totals)
  const contrary = field === 'liquidity'
    ? ['covered_on_date', 'covered_in_window', 'near_closure_exception', 'below_threshold']
    : ['positive_forecast', 'assets_cover']
  const previousContrary = earlier.findLast(row => contrary.includes(row[field].result))
  return {
    date: results[index].date,
    previousExaminedDate: previousExamined?.date ?? null,
    previousExaminedResult: previousExamined?.[field].result ?? null,
    previousContraryDate: previousContrary?.date ?? null,
    previousContraryResult: previousContrary?.[field].result ?? null,
  }
}

export function analyzeCase(input) {
  const data = record(input, 'Eingabe')
  const caseName = string(data.caseName, 'caseName')
  const seen = new Set()
  const results = list(data.dates, 'dates').map((value, index) => {
    const path = `dates[${index}]`
    const row = record(value, path)
    const day = date(row.date, `${path}.date`)
    if (seen.has(day)) throw new Error(`${path}.date: Der Stichtag wurde doppelt erfasst.`)
    seen.add(day)
    return {
      date: row.date,
      liquidity: row.liquidity == null
        ? status('open', 'Für diesen Stichtag fehlt der Liquiditätsstatus.')
        : calculateLiquidity(row.liquidity, day, `${path}.liquidity`),
      overindebtedness: row.overindebtedness == null
        ? status('open', 'Für diesen Stichtag fehlt die Prüfung der Überschuldung.')
        : calculateOverindebtedness(row.overindebtedness, day, `${path}.overindebtedness`),
    }
  }).sort((a, b) => a.date.localeCompare(b.date))
  if (!results.length) throw new Error('dates: Mindestens ein Stichtag ist erforderlich.')
  return {
    caseName,
    interpretation: 'Kandidaten sind die frühesten stützenden geprüften Stichtage. Dazwischenliegende und frühere Tage sind separat anhand der Belege zu prüfen.',
    firstCandidate: {
      liquidity: earliestCandidate(results, 'liquidity', ['zu_candidate', 'zu_candidate_worsening']),
      overindebtedness: earliestCandidate(results, 'overindebtedness', ['ue_candidate']),
    },
    results,
  }
}
