---
name: ausloesendes-ereignis-erfassen
description: "Für Auslösendes Ereignis erfassen: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt."
---

# Auslösendes Ereignis erfassen

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: zwölfmonatige Fortführungsprognose nach Paragraf 19 Absatz 2 InsO; Antrag nach Paragraf 15a InsO ohne schuldhaftes Zögern, spätestens binnen drei Wochen bei Zahlungsunfähigkeit und sechs Wochen bei Überschuldung; Drei-Wochen-Liquiditätsstatus für Paragraf 17 InsO.
- Tragende Normen verifizieren: Paragraf 19 Absatz 2 InsO, Paragraf 252 Absatz 1 Nummer 2 HGB sowie Paragrafen 1 und 102 StaRUG. Berufsständische Standards nur aus bereitgestellter oder lizenzierter aktueller Fassung verwenden. Paragraf 102 StaRUG setzt einen Jahresabschlussauftrag, offenkundige Anhaltspunkte und vermutete Unkenntnis des Mandanten voraus.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Geschäftsführer, Steuerberater, Wirtschaftsprüfer, Restrukturierungsberater, IV (falls beauftragt), Bank, Gesellschafter.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Fortbestehensprognose-Bericht, Integrierte Planung (P&L, BS, CF) 12+ Monate, Stresstest-Szenarien, Sanierungskonzept IDW S 6, Sanierungsgutachten, GF-Erklärung — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Zweck

Die Fortbestehensprognose ist kein Selbstzweck — sie ist die Antwort auf einen konkreten Anlass. Der Anlass wird dokumentiert weil **er Beweis ist**: bei späteren Haftungsfragen (§ 15b InsO, § 43 GmbHG, § 826 BGB ggue Gläubigern) zeigt die Dokumentation dass der Geschäftsführer **zeitnah** auf Anzeichen reagiert hat.

## Typische Auslöser

### 1. Möglicher Hinweis bei Jahresabschlusserstellung

Paragraf 102 StaRUG verpflichtet einen dort genannten Berufsträger bei der Erstellung eines Jahresabschlusses zum Hinweis auf einen möglichen Insolvenzgrund und die daran anknüpfenden Organpflichten, wenn die Anhaltspunkte offenkundig sind und er annehmen muss, dass dem Mandanten die mögliche Insolvenzreife nicht bewusst ist. Eine BWA, laufende Buchführung oder sonstige Beratung löst die Norm für sich allein nicht aus.

- Datum des Hinweises (schriftlich / mündlich / im Gespräch)
- Wortlaut wenn schriftlich
- Konkrete Anhaltspunkte die der StB genannt hat
- Quittierung des Hinweises durch den Mandanten

### 2. Hinweis des Wirtschaftsprüfers

Bei prüfungspflichtigen Gesellschaften (mittelgroße oder große KapGes nach § 267 HGB) kann der Prüfer im Rahmen des Jahresabschlusses einen **Hinweis zur Going-Concern-Annahme** geben oder den Bestätigungsvermerk einschraenken oder versagen.

### 3. Eigene Feststellung bei der Bilanzaufstellung

- **Eigenkapital negativ** (Aktiva kleiner als Passiva).
- **Wesentliche stille Lasten** im Status (z. B. Pensionsrückstellungen außerbilanziell).
- **Erhebliche außergewöhnliche Verluste** im laufenden Geschäftsjahr.

### 4. Liquiditätsengpass

- Mahnungen Gerichtsbeschlüsse oder Zahlungsverzug bei wesentlichen Gläubigern.
- Kreditlinie ausgeschoepft Kontoüberziehung.
- Lohn- und Gehaltszahlungen knapp.
- Steuer- und Sozialversicherungsabgaben nicht puenktlich.

### 5. Gesellschafterhinweis

- Brief oder E-Mail des Gesellschafters mit Sorge über Lage.
- Gesellschafterbeschluss zur Prüfung der Fortbestehensprognose.

### 6. Eigene Sorge des Geschäftsführers

- Subjektive Wahrnehmung dass die Lage kritisch wird.
- Wichtig: auch ohne externen Hinweis muss der Geschäftsführer aktiv prüfen — Sorgfaltspflicht § 43 GmbHG, § 93 AktG.

### 7. Externes Ereignis

- Wegfall Hauptkunde.
- Kreditlinien-Kündigung der Bank.
- Markteinbruch.
- Insolvenz eines wesentlichen Lieferanten / Abnehmers.

## Dokumentation

```yaml
fall-id: FP-2026-0001
stichtag-pruefung: 2026-05-20
ausloeser:
 typ: hinweis-steuerberater # hinweis-steuerberater / hinweis-wp / eigene-feststellung-bilanz / liquiditätsengpass / gesellschafterhinweis / eigene-sorge / externes-ereignis
 datum: 2026-05-15
 hinweisgeber: Steuerberater Mueller, Kanzlei XYZ
 mitteilungsform: schriftlich # schriftlich / muendlich / e-mail
 wortlaut: |
 "Bei der Erstellung des Jahresabschlusses 2025 sind die nachfolgend
 bezeichneten Anhaltspunkte für einen möglichen Insolvenzgrund offenkundig
 geworden. Da nach der bisherigen Korrespondenz anzunehmen ist, dass Ihnen
 die mögliche Insolvenzreife nicht bewusst ist, weisen wir Sie nach
 Paragraf 102 StaRUG auf den möglichen Insolvenzgrund und die daran
 anknüpfenden Organpflichten hin."
 konkrete-anhaltspunkte:
 - Eigenkapital negativ 82.000 EUR Stichtag 31.12.2025
 - SuSa weist Lieferantenverbindlichkeiten 410.000 EUR (Vorjahr 180.000)
 - Sozialversicherungsbeitraege drei Monate offen 45.000 EUR
 reaktion-geschaeftsfuehrung:
 erste-reaktion-am: 2026-05-20
 schritte:
 - Beauftragung Erstellung Fortbestehensprognose
 - Aktivierung Plugin fortbestehensprognose
 - Termin mit Insolvenzanwalt vereinbart für 2026-05-27 als Sicherheit
```

## Pflichthinweis Frist

Mit Eintritt der Insolvenzreife nach Paragraf 17 oder 19 InsO entsteht die Antragspflicht des Paragrafen 15a InsO. Der Antrag ist ohne schuldhaftes Zögern zu stellen. Die Fortführungsprognose ist kein Aufschub, sondern ein Tatbestandselement der Überschuldungsprüfung.

- Zahlungsunfähigkeit: höchstens drei Wochen nach Eintritt.
- Überschuldung: höchstens sechs Wochen nach Eintritt.

Bei belastbaren Anzeichen unverzüglich spezialisierten Rechtsrat einholen; die Höchstzeiträume dürfen nicht als reguläre Bearbeitungsfristen ausgeschöpft werden.

## Ausgabe

- `ausloesendes-ereignis.yaml` mit allen Pflichtfeldern.
- Erste Risikobewertung (grün / gelb / rot).
- Empfehlung: bei rot direkt zu `wenn-prognose-negativ-naechste-schritte` und Insolvenzanwalt einschalten — diese Prüfung kann fortgesetzt werden aber nicht ohne anwaltliche Begleitung.

## Paragrafenkette Ausloesende Ereignisse

Paragraf 102 StaRUG (begrenzter Hinweis bei Jahresabschlusserstellung) → Paragraf 19 InsO (Überschuldung) → Paragraf 15a InsO (Antrag ohne schuldhaftes Zögern, Höchstzeiträume drei beziehungsweise sechs Wochen) → Paragraf 15b InsO (Zahlungen nach Insolvenzreife) → Paragraf 43 GmbHG (Organhaftung)

## Triage — Ausloesende Ereignisse

1. **Wer hat das Signal gesandt?** Berufsträger bei Jahresabschlusserstellung, Wirtschaftsprüfer, Geschäftsleitung, Bank oder anderer Hinweisgeber?
2. **Datum des Signals?** Taggenau dokumentieren; das Signal ist ein Beweisdatum, bestimmt aber nicht automatisch den objektiven Eintritt der Insolvenzreife.
3. **Schriftliche Dokumentation?** E-Mail, Aktenvermerk, Protokoll vorhanden?
4. **Sofortmassnahmen?** Liquiditaetsplanung starten, Anwalt einschalten, Steuerberater beauftragen?

> Quellenregel: Entscheidungen nur nach Prüfung einer amtlichen oder frei zugänglichen Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage ausgeben.
