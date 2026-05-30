# Forschungszulage-Antragstellung

Plugin für die steuerliche Forschungsförderung nach dem Forschungszulagengesetz: Fördercheck, BSFZ-Bescheinigung, Projektbeschreibung, FuE-Abgrenzung, Bemessungsgrundlage, Finanzamt-Antrag, Auszahlung, Verlust-/Krisenlage, Dokumentation für Außenprüfung, Kumulierung und Nachbesserung.

Das Plugin ist für Unternehmen, Start-ups, Mittelstand, Steuerberaterinnen, Rechtsanwälte, CFOs und Produkt-/Entwicklungsteams gebaut. Es übersetzt technische Entwicklung in die Sprache, die BSFZ und Finanzamt brauchen: Neuheit, Risiko, systematisches Vorgehen, förderfähige Aufwendungen und saubere Belege.

## Quellen-Gate

Vor jeder belastbaren Ausgabe live prüfen:

- Forschungszulagengesetz auf `gesetze-im-internet.de`, insbesondere §§ 1 bis 7 und § 10 FZulG.
- BSFZ-Antragsverfahren: zweistufig, erst FuE-Bescheinigung bei der BSFZ, dann Antrag beim Finanzamt.
- BMF-Forschungszulage und BMF-Schreiben vom 07.02.2023, soweit noch nicht durch ein neues finales Schreiben ersetzt.
- Änderungen ab 2026: Bemessungsgrundlagenhöchstbetrag 12 Mio. Euro, 20-%-Pauschale für Gemein- und Betriebskosten bei nach dem 31.12.2025 begonnenen Vorhaben, Eigenleistung 100 Euro pro Stunde bis max. 40 Stunden/Woche.

## ⬇️ Direkt-Download (einzelnes ZIP)

| Plugin | Direkt-Download |
| --- | --- |
| Forschungszulage-Antragstellung (`forschungszulage-antragstellung`) | [forschungszulage-antragstellung.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/forschungszulage-antragstellung.zip) |

Die URL ist stabil und zeigt immer auf die neueste Version.

### Installation

1. ZIP herunterladen.
2. Claude Code oder Cowork → **Customize Plugins** → **Install from .zip**.
3. In einer neuen Unterhaltung starten mit:

```text
/forschungszulage-antragstellung:allgemein
```

## Skill-Matrix

| Skill | Wofür? |
| --- | --- |
| `allgemein` | Einstieg, Triage, Förderroute und Projektaufnahme |
| `fz-foerdercheck-kaltstart` | Anspruchsberechtigung, Projektart, Jahre, Risiken, Sofortpotenzial |
| `fz-bsfz-bescheinigung-projektbeschreibung` | BSFZ-Antrag, Vorhabenbeschreibung, technische Neuheit, Risiko |
| `fz-fue-definition-frascati-abgrenzung` | Grundlagenforschung, industrielle Forschung, experimentelle Entwicklung |
| `fz-bemessungsgrundlage-2026` | Personal, Eigenleistung, Auftragsforschung, Wirtschaftsgüter, 12-Mio.-Grenze |
| `fz-finanzamt-festsetzung-auszahlung` | Antrag beim Finanzamt, Anrechnung, Auszahlung, Vorauszahlungssenkung |
| `fz-insolvenz-verlust-liquiditaet` | Krise, Verlustjahr, Insolvenz, Forderungs-/Masseblick, Liquidität |
| `fz-dokumentationspaket-betriebspruefung` | Stundenzettel, Projektakte, Kostenbelege, Prüferpaket |
| `fz-kumulierung-beihilfen-agvo` | Doppelförderung, AGVO, andere Zuschüsse, EU/EWR-Auftragsforschung |
| `fz-ablehnung-nachbesserung-einspruch` | BSFZ-Nachforderung, Ablehnung, Finanzamt-Einspruch, Reparatur |
| `fz-roadmap-mehrjahresantrag` | Mehrjahresstrategie, rückwirkende Jahre, Jahreswechsel, Portfolio |

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 11 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `allgemein` | Einstieg, Schnelltriage und Workflow-Routing im Forschungszulage-Antragstellung-Plugin. Klärt Unternehmen, FuE-Vorhaben, Jahre, Kosten, BSFZ-Status, Finanzamt-Antrag, Verlust-/Insolvenzlage, Dokumentation und passenden Spezialskill. |
| `fz-ablehnung-nachbesserung-einspruch` | Ablehnung oder Nachforderung bei Forschungszulage bearbeiten: BSFZ-Rückfrage, negative Bescheinigung, Finanzamt-Kürzung, Einspruch, Begründung, neue Tatsachen, Beleg- und Textreparatur. |
| `fz-bemessungsgrundlage-2026` | Bemessungsgrundlage der Forschungszulage ab 2026 berechnen: Personalaufwand, Eigenleistung 100 Euro/Stunde, Auftragsforschung 70 Prozent EU/EWR, Wirtschaftsgüter, 20-Prozent-Gemeinkostenpauschale, 12-Mio.-Grenze, KMU-Erhöhung. |
| `fz-bsfz-bescheinigung-projektbeschreibung` | BSFZ-Antrag und FuE-Projektbeschreibung erstellen: Ausgangsproblem, Stand der Technik, Neuheit, technisches Risiko, systematisches Vorgehen, Arbeitspakete und verständliche Prüferlogik. |
| `fz-dokumentationspaket-betriebspruefung` | Dokumentationspaket Forschungszulage für Finanzamt und Außenprüfung erstellen: Projektakte, Stundenzettel, Kostenbelege, Auftragsunterlagen, Wirtschaftsgüter, BSFZ-Bescheid, Änderungslog und Prüfermappe. |
| `fz-finanzamt-festsetzung-auszahlung` | Forschungszulage beim Finanzamt beantragen: Festsetzung, Anrechnung auf Einkommen- oder Körperschaftsteuer, Auszahlung eines Überschusses, Vorauszahlungssenkung, ELSTER-/Steuerverfahrenslogik. |
| `fz-foerdercheck-kaltstart` | Schneller Fördercheck Forschungszulage: Anspruchsberechtigung, FuE-Kategorie, Projektjahre, Kostenarten, BSFZ-/Finanzamt-Status, Ausschlussrisiken und Sofortpotenzial. |
| `fz-fue-definition-frascati-abgrenzung` | FuE-Definition für Forschungszulage prüfen: Grundlagenforschung, industrielle Forschung, experimentelle Entwicklung, Frascati-Kriterien, AGVO, Abgrenzung zu Routineentwicklung, Customizing, Bugfixing und Serienpflege. |
| `fz-insolvenz-verlust-liquiditaet` | Forschungszulage in Verlust-, Krisen- und Insolvenzlagen prüfen: Auszahlung statt bloßer Steuerersparnis, Massezugehörigkeit, Antragstellung, Aufrechnung, Abtretung, Liquiditätsplanung und Haftungsrisiken. |
| `fz-kumulierung-beihilfen-agvo` | Kumulierung Forschungszulage mit anderen Förderungen und Beihilfen prüfen: AGVO, EU/EWR-Auftragsforschung, ZIM, Landesprogramme, De-minimis-Nähe, Doppelförderung, Nachweis- und Abzugslogik. |
| `fz-roadmap-mehrjahresantrag` | Mehrjahresstrategie Forschungszulage: rückwirkende Jahre, Jahreswechsel 2025/2026, Projektportfolio, wiederkehrende BSFZ-Anträge, Dokumentationsroutine, Liquiditätsplanung und Fristenkontrolle. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
