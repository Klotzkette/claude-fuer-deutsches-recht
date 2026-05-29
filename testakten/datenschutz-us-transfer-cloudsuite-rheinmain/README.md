# Testakte Datenschutz: US-Transfer CloudSuite Assist

## ⬇️ Direkt-Download

| Testakte | Direkt-Download |
| --- | --- |
| `testakte-datenschutz-us-transfer-cloudsuite-rheinmain` (diese Akte) | [testakte-datenschutz-us-transfer-cloudsuite-rheinmain.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-datenschutz-us-transfer-cloudsuite-rheinmain.zip) |

Die Testakte ist **kein Teil des Plugins** und wird separat als ZIP-Datei aus dem GitHub-Release geladen. Das ZIP enthält die Originalformate für realistische Tests.

**Fiktive Testakte.** Alle Personen, Unternehmen, Aktenzeichen, Vertragsdaten und Dienste sind erfunden. Die Akte dient dazu, die Datenschutz-Skills zu US-Transfers, DPF-Listing, SCC, TIA und Behördenkommunikation realistisch zu testen.

## Kurzsachverhalt

Die RheinMain Präzisionstechnik GmbH aus Frankfurt am Main nutzt seit Januar 2025 die SaaS-Plattform **CloudSuite Assist** für CRM, Supporttickets und KI-gestützte Antwortvorschläge. Vertragspartner im Rahmenvertrag ist die CloudSuite Ireland Ltd.; technische Betreiberin und US-Importeurin ist nach DPA und Security-Anhang die CloudSuite Assist Inc., Delaware/San José. Die produktiven Kundendaten liegen laut Vertrag in Frankfurt und Dublin, aber der 2nd-Level-Support, Telemetrieauswertung, Abuse-Detection und einzelne KI-Logfragmente werden in den USA verarbeitet.

Im Mai 2026 fragt die hessische Datenschutzaufsicht nach, auf welcher Grundlage die US-Transfers laufen. Der Einkauf hat bislang nur eine Anbieter-Mail "we are DPF certified" abgelegt. Die Rechtsabteilung findet außerdem SCC, aber nicht vollständig ausgefüllte Annex-II- und Annex-III-Anlagen. Die Testakte enthält bewusst kleine Reibungen: Konzernnamen weichen voneinander ab, der DPF-Scope ist unklar, HR-Daten dürfen eigentlich nicht in Tickets landen, und ein Subprozessor ist erst im April 2026 ergänzt worden.

## Enthaltene Unterlagen

| Datei | Inhalt |
|---|---|
| `01_behoerdenanfrage_hbdi_2026-05-12.md` | Fiktive Anfrage der hessischen Datenschutzaufsicht |
| `02_anbieterprofil_cloudsuite_assist.md` | Anbieter-, Vertrags- und Datenflussprofil |
| `03_dpf_pruefvermerk_listung_und_luecken.md` | Interner Vermerk zum behaupteten DPF-Listing |
| `04_transferregister_vvt_auszug.md` | Auszug aus Transferregister und VVT |
| `05_scc_modul_2_annex_i_bis_iii_arbeitsfassung.md` | Arbeitsfassung SCC-Modulwahl und Anlagen |
| `06_tia_us_transfer_cloudsuite.md` | Transfer Impact Assessment |
| `07_tom_verschluesselung_key_management.md` | TOMs und ergänzende Maßnahmen |
| `08_subprocessor_map.csv` | Subprozessoren und Weiterübermittlungen |
| `09_antwortentwurf_aufsichtsbehoerde.md` | Antwortentwurf an die Behörde |
| `10_massnahmenplan_reviewkalender.md` | Maßnahmenplan und Wiedervorlage |

## Vorführziele

- Mit `us-transfer-tia-dokumentation` prüfen, ob DPF als alleinige Grundlage reicht.
- Mit `standardvertragsklauseln-scc-paket` SCC-Modul 2 und Annex I-III nachziehen.
- Mit `drittlandtransfer-behoerdenpaket-output` ein druckfähiges Behördenpaket erstellen.
- Die Akte zeigt, warum "Anbieter sagt DPF" nicht genügt, wenn Rechtsträger, Produkt, Datenkategorien oder Subprozessoren nicht sauber belegt sind.
