import { analyzeCase } from './engine.mjs'

const input = document.querySelector('#input')
const file = document.querySelector('#file')
const output = document.querySelector('#output')
const feedback = document.querySelector('#feedback')
const results = document.querySelector('#results')
const money = new Intl.NumberFormat('de-DE', { style: 'currency', currency: 'EUR' })
const percent = new Intl.NumberFormat('de-DE', { style: 'percent', minimumFractionDigits: 2 })
let report = null

function amount(cents) {
  if (cents === null || cents === undefined) return 'offen'
  const total = BigInt(Math.abs(cents))
  const euros = total / 100n
  const fraction = String(total % 100n).padStart(2, '0')
  return (cents < 0 ? '−' : '') + money.formatToParts(euros)
    .map(part => part.type === 'fraction' ? fraction : part.value).join('')
}

function date(value) {
  return value ? value.split('-').reverse().join('.') : 'offen'
}

function node(tag, text, className) {
  const element = document.createElement(tag)
  if (text) element.textContent = text
  if (className) element.className = className
  return element
}

function feedbackText(text, error = false) {
  feedback.hidden = !text
  feedback.classList.toggle('error', error)
  feedback.textContent = text
}

function table(columns, rows, numeric = []) {
  const wrapper = node('div', '', 'scroll')
  const grid = node('table')
  const header = node('tr')
  columns.forEach((text, index) => {
    const heading = node('th', text, numeric.includes(index) ? 'money-heading' : '')
    heading.scope = 'col'
    header.append(heading)
  })
  const head = node('thead')
  head.append(header)
  const body = node('tbody')
  rows.forEach(row => {
    const line = node('tr')
    row.forEach((text, index) => line.append(node('td', text, numeric.includes(index) ? 'money' : '')))
    body.append(line)
  })
  grid.append(head, body)
  wrapper.append(grid)
  return wrapper
}

function collapsible(title, className) {
  const panel = node('details', '', className)
  panel.append(node('summary', title))
  return panel
}

function candidate(title, value) {
  const card = node('article', '', 'card')
  card.append(node('h3', title))
  card.append(node('p', value ? date(value.date) : 'Kein stützender Stichtag', 'date-value'))
  if (value?.previousExaminedDate && value.previousExaminedDate !== value.previousContraryDate) {
    card.append(node('p', `Zuvor geprüft am ${date(value.previousExaminedDate)}.`, 'muted'))
  }
  if (value?.previousContraryDate) {
    card.append(node('p', `Letzter gegenläufiger Befund am ${date(value.previousContraryDate)}.`, 'muted'))
  }
  return card
}

const groups = {
  A1: 'A1',
  P1: 'P1',
  A2: 'A2',
  P2: 'P2',
  open: 'Offen',
  outside_window: 'Nach dem Fenster',
}
const decisions = { include: 'Angesetzt', exclude: 'Ausgeschlossen', open: 'Offen' }
const liquidityLabels = {
  A1: 'A1 · Verfügbare Mittel am Stichtag',
  P1: 'P1 · Fällige Pflichten am Stichtag',
  A2: 'A2 · Verfügbarkeit in den folgenden 21 Tagen',
  P2: 'P2 · Weitere Fälligkeiten in den folgenden 21 Tagen',
}

function findingPanel(kind, finding) {
  const content = node('section')
  content.append(node('h3', kind), node('p', finding.label, 'finding'), node('p', finding.detail))
  if (!finding.totals) return content
  const totals = finding.totals
  if (!finding.complete) content.append(node('p', 'Die folgenden Summen umfassen nur die bislang erfassten Positionen.', 'muted'))
  if (finding.timeline) {
    if (finding.result !== finding.arithmetic.result) content.append(node('p', `Rechenbefund: ${finding.arithmetic.label}. ${finding.arithmetic.detail}`))
    const cessationLabels = { established: 'Als festgestellt und nicht widerlegt eingegeben', rebutted: 'Vermutung als widerlegt eingegeben', open: 'Gesonderte Würdigung offen' }
    const cessation = finding.paymentCessation
    content.append(node('p', `Zahlungseinstellung: ${cessationLabels[cessation.result]}.`))
    if (cessation.source) content.append(node('p', `${cessation.reason} Quelle: ${cessation.source}.`),
      node('p', `Gegenindizien und Wiederaufnahme: ${cessation.counterEvidence}`))
    if (cessation.externalConduct) content.append(node('p', `Außenverhalten am ${date(cessation.establishedOn)}: ${cessation.externalConduct}`))
    const ratio = totals.remainingGapBasisPoints === null ? '—'
      : percent.format(totals.remainingGapBasisPoints / 10_000)
    const moneyRows = Object.entries(liquidityLabels).map(([key, label]) => [label, amount(totals[key])])
    moneyRows.push(['Lücke am Stichtag', amount(totals.immediateGapCents)],
      ['Rechnerische Restlücke', amount(totals.remainingGapCents)],
      ['Restlücke / (P1 + P2), gerundet', ratio],
      ['Schwelle im Dreiwochenfenster', totals.remainingGapBasisPoints === null ? '—'
        : totals.thresholdMet ? 'Erreicht' : 'Unter 10 %'])
    content.append(node('p', `Dreiwochenfenster bis ${date(finding.windowThrough)}`),
      table(['Position', 'Ergebnis'], moneyRows, [1]))
    const timeline = collapsible('Tagesverlauf des Dreiwochenfensters')
    timeline.append(table(['Datum', 'Neue Mittel', 'Neue Fälligkeiten', 'Kumulierte Lücke'],
      finding.timeline.map(row => [date(row.date), amount(row.assetsCents), amount(row.liabilitiesCents),
        amount(row.gapCents)]), [1, 2, 3]))
    content.append(timeline)
    for (const value of [finding.nearClosure, finding.gapTrend]) {
      if (value.source) content.append(node('p', `Quelle zum Befund: ${value.source}`, 'muted'))
    }
  } else {
    content.append(table(['Position', 'Ergebnis'], [
      ['Vermögenswerte', amount(totals.assetsCents)],
      ['Verbindlichkeiten', amount(totals.liabilitiesCents)],
      ['Unterdeckung', amount(totals.uncoveredCents)],
    ], [1]))
    if (finding.forecast.source) {
      content.append(node('p', `Prognose bis ${date(finding.forecast.through)}. Quelle ${finding.forecast.source}.`))
    }
    if (finding.forecast.failureOn) content.append(node('p', `Erfasste späteste zeitliche Grenze des erwarteten Finanzierungsabbruchs: ${date(finding.forecast.failureOn)}.`))
    content.append(node('p', `Rechtlich zugrunde gelegtes Prognoseende: ${date(finding.forecast.requiredThrough)}.`, 'muted'),
      node('p', `Zeitraum: ${finding.period.source}. ${finding.period.reason}`, 'muted'))
  }
  const openCount = finding.items.filter(row => row.decision === 'open').length
  const excludedCount = finding.items.filter(row => row.decision === 'exclude').length
  content.append(node('p', `${finding.items.length} Positionen, davon ${openCount} offen und ${excludedCount} ausgeschlossen. Erfassungsumfang ${finding.complete ? 'als vollständig bestätigt' : 'unvollständig'}.`, 'muted'))
  if (finding.evidence.length) {
    const inventory = collapsible('Eingangsunterlagen und offene Nachforderungen')
    const states = { present: 'Vorhanden', partial: 'Unvollständig', missing: 'Fehlt' }
    inventory.append(table(['Unterlage', 'Prüfbereich', 'Stand', 'Fundstelle oder fehlender Teil'],
      finding.evidence.map(row => [`${row.id} · ${row.description}`, row.scope === 'forecast' ? 'Fortbestehensprognose' : 'Rechenpositionen',
        states[row.status], [row.source, row.reason].filter(Boolean).join(' · ')])))
    content.append(inventory)
  }
  for (const note of finding.notes) content.append(node('p', note, 'muted'))
  const positions = collapsible('Positionen und Quellen')
  positions.append(table(['Belegposition', 'Kategorie', 'Betrag', 'Ansatz', 'Fundstelle und Begründung'],
    finding.items.map(row => [
      `${row.id} · ${row.description}`,
      groups[row.group] ?? (row.side === 'assets' ? 'Vermögen' : 'Verbindlichkeit'),
      amount(row.amountCents), decisions[row.decision], [row.source, row.reason].filter(Boolean).join(' · '),
    ]), [2]))
  content.append(positions)
  return content
}

function render(value) {
  const intro = node('div', '', 'candidates')
  intro.append(candidate('§ 17 · Zahlungsunfähigkeit', value.firstCandidate.liquidity),
    candidate('§ 19 · Überschuldung', value.firstCandidate.overindebtedness))
  results.replaceChildren(node('h3', value.caseName), intro, node('p', value.interpretation, 'muted'))
  value.results.forEach((item, index) => {
    const panel = collapsible(`${date(item.date)} · ${item.liquidity.label} · ${item.overindebtedness.label}`, 'card')
    panel.open = index === value.results.length - 1
    panel.append(findingPanel('§ 17 · Zahlungsunfähigkeit', item.liquidity),
      findingPanel('§ 19 · Überschuldung', item.overindebtedness))
    results.append(panel)
  })
  output.hidden = false
}

function clearReport() {
  report = null
  output.hidden = true
  results.replaceChildren()
}

file.addEventListener('change', async () => {
  if (!file.files.length) return
  try {
    input.value = await file.files[0].text()
    input.scrollTop = 0
    clearReport()
    feedbackText('JSON-Datei geladen. Starten Sie die Berechnung.')
  } catch (error) {
    feedbackText(`Datei konnte nicht gelesen werden. ${error.message}`, true)
  }
})

input.addEventListener('input', () => {
  clearReport()
  feedbackText('')
})

document.querySelector('#sample').addEventListener('click', async () => {
  try {
    const response = await fetch('./beispiel.json')
    if (!response.ok) throw new Error(`HTTP ${response.status}`)
    input.value = await response.text()
    input.scrollTop = 0
    clearReport()
    feedbackText('Beispiel geladen. Starten Sie die Berechnung.')
  } catch (error) {
    feedbackText(`Beispiel konnte nicht geladen werden. ${error.message}`, true)
  }
})

document.querySelector('#blank').addEventListener('click', () => {
  input.value = JSON.stringify({ caseName: 'Fallbezeichnung eintragen', dates: [{ date: new Date().toISOString().slice(0, 10),
    liquidity: { complete: false, assets: [], liabilities: [], notes: ['Bankkonten, Kreditlinien, Fälligkeiten und Zuflüsse aus der Grundakte noch erfassen.'],
      evidence: [{ id: 'BANK', description: 'Kontoauszüge sämtlicher Konten', status: 'missing', reason: 'Noch nicht gesichtet und abgestimmt.' }],
      paymentCessation: { result: 'open' } },
    overindebtedness: { complete: false, assets: [], liabilities: [], forecast: { result: 'open' },
      evidence: [{ id: 'PLAN', description: 'Datierte Finanzplanung und Finanzierungszusagen', scope: 'forecast', status: 'missing', reason: 'Prognosegrundlagen noch nicht gesichtet.' }],
      notes: ['Eigentum, Verwertungswerte, Verbindlichkeiten und Fortbestehensprognose noch belegen.'] },
  }] }, null, 2)
  input.scrollTop = 0
  clearReport()
  feedbackText('Leere Arbeitsdatei angelegt. Fallbezeichnung und Stichtag anpassen, dann Belegpositionen ergänzen. Unvollständige Abschnitte bleiben offen.')
})

document.querySelector('#calculate').addEventListener('click', () => {
  try {
    report = analyzeCase(JSON.parse(input.value.replace(/^\uFEFF/, '')))
    render(report)
    feedbackText(`${report.results.length} ${report.results.length === 1 ? 'Stichtag' : 'Stichtage'} berechnet.`)
  } catch (error) {
    clearReport()
    feedbackText(`Prüfung abgebrochen. ${error.message}`, true)
  }
})

document.querySelector('#download').addEventListener('click', () => {
  if (!report) return
  const blob = new Blob([JSON.stringify(report, null, 2) + '\n'], { type: 'application/json' })
  const url = URL.createObjectURL(blob)
  const link = node('a')
  link.href = url
  link.download = 'insolvenzpruefung.json'
  link.click()
  setTimeout(() => URL.revokeObjectURL(url), 1000)
})
