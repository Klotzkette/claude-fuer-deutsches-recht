---
name: aktenabschluss-archivierung
description: "Aktenabschluss Archivierung: bearbeitet den maßgeblichen Prüfpfad und erzeugt den nächsten belastbaren Output im Mandat."
---

# Aktenabschluss Archivierung

## Arbeitsbereich

Dieser Skill arbeitet **Aktenabschluss Archivierung** als zusammenhängenden Arbeitsgang im Plugin Notariat Alltag ab — nach Aktenlage, Frist, Zuständigkeit, Beweislast und gewünschtem Output priorisiert.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `notariat-065-aktenabschluss-archivierung-und-offene-vollzugsrest` | Notariat im Alltag: Aktenabschluss, Archivierung und offene Vollzugsreste. Ordnungsgemäßer Abschluss eines Vorgangs nach vollständigem Vollzug, Archivierungsanforderungen und Behandlung offener Vollzugsreste. |

## Arbeitsweg

Im Plugin Notariat Alltag gilt für **Aktenabschluss Archivierung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `notariat-065-aktenabschluss-archivierung-und-offene-vollzugsrest`

**Fokus:** Notariat im Alltag: Aktenabschluss, Archivierung und offene Vollzugsreste. Ordnungsgemäßer Abschluss eines Vorgangs nach vollständigem Vollzug, Archivierungsanforderungen und Behandlung offener Vollzugsreste.

# Notariat im Alltag: Aktenabschluss, Archivierung, offene Vollzugsreste

## Zweck und Anwendungsbereich

Der Aktenabschluss ist der letzte Schritt eines Urkundsvorgangs. Er setzt voraus, dass alle Vollzugshandlungen abgeschlossen sind, alle Kosten bezahlt wurden und keine offenen Restpunkte mehr existieren. Dieser Skill strukturiert den ordnungsgemäßen Abschlussprozess.

Rechtsgrundlagen: DONot §§ 9–56 (Aktenführung, Aufbewahrung), § 18 BNotO (Aufbewahrungspflicht), §§ 44–64 BeurkG (Urkundensammlung), GwG § 8 (5-Jahres-Aufbewahrung), DSGVO Art. 17 (Löschungsrecht), GNotKG § 19 (Kostenforderung), GBO § 35 (Vollständigkeit der Grundbucheintragungen).

## Aktenabschluss: Voraussetzungen

Ein Vorgang kann nur abgeschlossen werden, wenn:
- [ ] Alle Vollzugshandlungen durchgeführt (Grundbucheintragung, HR-Anmeldung, Genehmigungen)
- [ ] Alle Bestätigungen eingegangen (Eintragungsnachricht Grundbuchamt, HR-Eintragungsnachweis)
- [ ] Steuerliche Meldungen erledigt (GrESt-Anzeige, ErbSt-Meldung)
- [ ] Kosten vollständig bezahlt
- [ ] GwG-Dokumentation vollständig und archiviert
- [ ] Alle Originalunterlagen in die Urkundensammlung eingefügt
- [ ] Alle Ausfertigungen und beglaubigte Abschriften an Berechtigte versandt

## Abschlussprotokoll

Ein Aktenabschlussprotokoll bestätigt, dass alle Punkte erfüllt sind. Inhalt:
- Urkundenrolle-Nummer
- Datum des Abschlusses
- Vollzugshandlungen im Überblick
- Archivierungs-Verweise
- Verantwortliche Person

## Archivierung

**Urkundensammlung (§ 9 DONot):**
- Urschriften: dauerhaft beim Notar oder nach Amtsende beim Amtsgericht
- Aufbewahrungsfrist: 100 Jahre
- Keine Vernichtung zulässig

**Nebenakten (§ 50 DONot):**
- Schriftverkehr, Entwürfe, Vollzugsdokumentation
- Aufbewahrungsfrist: 30 Jahre

**GwG-Dokumentation (§ 8 Abs. 4 GwG):**
- Identifizierungsnachweise, Risikovermerk, Transparenzregister-Abfrage
- Aufbewahrungsfrist: 5 Jahre
- Getrennt archivierbar (§ 8 Abs. 4 S. 2 GwG)

## Offene Vollzugsreste

Manchmal ist ein Vorgang formal abgeschlossen, aber es gibt noch offene Punkte (z.B. Nießbrauchsrückübertragung nach Todesfall). Diese müssen im System als „Wiedervorlage nach Ereignis" markiert werden.

**Typische offene Vollzugsreste:**
- Auflage aus familiengerichtlicher Genehmigung erfüllt?
- Löschung des Nießbrauchs nach Tod des Berechtigten
- Bedingungseintritt bei aufschiebend bedingten Verträgen
- Rückforderungsklausel-Aktivierung prüfen

## Mandantenschlusskorrespondenz

Nach Aktenabschluss erhält der Mandant:
- Bestätigung des Vollzugsabschlusses
- Originalunterlagen (soweit auszuhändigen)
- Hinweis auf Aufbewahrungsempfehlung
- Hinweis auf künftige Ereignisse (Nießbrauch-Löschung nach Tod, Nachmeldepflichten)

## DSGVO beim Aktenabschluss

Nach Ablauf der gesetzlichen Aufbewahrungsfristen sind personenbezogene Daten grundsätzlich zu löschen (DSGVO Art. 17). Dies gilt nicht für Urschriften (gesetzliche Aufbewahrungspflicht geht vor). Für Nebenakten: nach 30 Jahren löschen (soweit keine aktive Forderung mehr).

## Prüfprogramm

- Alle Vollzugsvoraussetzungen erfüllt und bestätigt?
- Kostenrechnung bezahlt?
- GwG-Dokumentation komplett und archiviert?
- Abschlussprotokoll erstellt?
- Mandant über Abschluss informiert?
- Offene Vollzugsreste als Wiedervorlage gesetzt?

## Typische Fallen

- Akte vorzeitig abgeschlossen, Eintragungsnachweis fehlt noch.
- Kosten nicht vollständig eingenommen → Aktenabschluss unvollständig.
- GwG-Dokumentation nicht separat archiviert → 5-Jahres-Frist unklar.
- Nießbrauchsrückfall nach Tod vergessen → Grundbuch bleibt belastet.
- DSGVO-Löschungsrecht nach Aufbewahrungsfrist nicht umgesetzt.

## Rechtsquellen

- DONot §§ 9–56: https://www.bnotk.de/notare/berufsrecht/dienstordnung/
- § 18 BNotO: https://dejure.org/gesetze/BNotO/18.html
- GwG § 8: https://dejure.org/gesetze/GwG/8.html
- DSGVO Art. 17: https://dejure.org/gesetze/DSGVO/17.html
- GNotKG § 19: https://dejure.org/gesetze/GNotKG/19.html
- BNotK Archivierungshinweise: https://www.bnotk.de

## Output-Formate

- **Aktenabschluss-Protokoll** (Muster)
- **Abschluss-Checkliste** (alle Voraussetzungen)
- **Archivierungs-Fristen-Übersicht** (Urschrift / Nebenakte / GwG)
- **Mandanten-Schlussschreiben** (mit Aufbewahrungshinweis)
- **Wiedervorlage-Offene-Reste** (Tabelle für Folgeereignisse)

Quellen für Live-Check: https://dejure.org | https://openjur.de | https://www.gesetze-im-internet.de | https://www.bnotk.de | https://www.bgh.de | https://www.bverfg.de
