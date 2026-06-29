---
name: pfueb-bank
description: "Gläubiger pfändet Bankkonto per PfÜB: Titel, Antrag, Drittschuldnerbank, P-Konto, Drittschuldnererklärung und digitale Zustellung an Kreditinstitute ab 2027."
---

# PfÜB Bankkonto

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: §§ 704 ff. ZPO; § 802l Kontensuche, Vermögensauskunft, Räumung; § 800 ZPO Notar; § 201 InsO, ZVG, EU-Kontenpfändung VO 655; § 765a Härtefall, Schuldnerschutz — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Startet bei

- Vollstreckbarer Titel liegt vor (Drei-Säulen-Prüfung grün – sonst zurück an `zv-titel-klausel-zustellung`).
- Bankverbindung des Schuldners bekannt **oder** zu ermitteln (dann erst `zv-kontensuche-drittschuldner`).
- Schuldner nicht in Insolvenz (Paragraf 89 InsO – sonst Stop).

## Rechtsgrundlagen

- Paragraf 829 ZPO – Pfändung einer Geldforderung
- Paragraf 835 ZPO – Überweisung an Zahlungs statt oder zur Einziehung
- Paragraf 833a ZPO – Pfändung eines Kontoguthabens, Moratorium von vier Wochen
- Paragraf 850k ZPO – Pfändungsschutzkonto (P-Konto)
- Paragraf 850c ZPO – Pfändungsfreigrenze für Arbeitseinkommen (mittelbar bei Lohnüberweisung)
- Paragraf 840 ZPO – Drittschuldnererklärung
- Paragraf 829a ZPO n.F. – elektronischer Antrag mit elektronisierten Titelunterlagen
- Paragraf 829 Absatz 5 ZPO n.F. – strukturierter XML-Datensatz für PfÜB-Anträge ab 1.1.2027
- Paragraf 173 Absatz 2 Nummer 1 ZPO n.F. – sichere Übermittlungswege der Kreditinstitute ab 1.6.2027
- Pfändungsfreigrenzenbekanntmachung 2025

## Workflow

1. **Titel + Klausel + Zustellung** prüfen lassen.
2. **Drittschuldner** identifizieren: Bank, IBAN reicht nicht – Bank ist der Drittschuldner, IBAN nur Bezeichnung des Anspruchs.
3. **Antrag bauen** an das Vollstreckungsgericht am Wohnsitz des Schuldners (Paragraf 828 Absatz 2 ZPO). Pflichtangaben:
 - Gläubiger, Schuldner, Drittschuldner-Bank
 - Forderungsaufstellung (Hauptforderung, Zinsen, Kosten, Verzugskosten)
 - genaue Bezeichnung der gepfändeten Forderung ("gesamtes Guthaben sowie alle künftigen Eingänge auf jedem Konto, das der Schuldner bei der Drittschuldnerin unterhält")
 - Auskunftsersuchen nach Paragraf 840 ZPO
4. **Formular** verwenden – Pflichtformular der ZVFV. Ab 1.10.2026 die reformierten elektronischen Antragswege und Titelunterlagen nach Paragraf 829a ZPO n.F. beachten.
5. **Einreichen** beim Vollstreckungsgericht: Papier oder elektronisch über beA/eBO; ab 1.1.2027 kann der Antrag nach Paragraf 829 Abs. 5 ZPO n.F. als strukturierter maschinenlesbarer XML-Datensatz übermittelt werden. Wenn PDF und XML parallel eingereicht werden, ist der XML-Datensatz für die gerichtliche Prüfung führend.
6. **Zustellung an Drittschuldner** und Schuldner:
 - bis 31.5.2027: per Gerichtsvollzieher papierförmig, postalisch oder freiwillig elektronisch, je nach sicherem Übermittlungsweg und Auftrag
 - ab 1.6.2027: Kreditinstitute müssen einen sicheren Übermittlungsweg nach Paragraf 173 Abs. 2 Nr. 1 ZPO n.F. eröffnen; Gerichtsvollzieher können Pfändungsbeschlüsse an Banken regelmäßig elektronisch zustellen
 - die Aufforderung zur Drittschuldnererklärung nach Paragraf 840 ZPO muss zusammen mit dem Pfändungsbeschluss übermittelt werden
 - der Zustellungsauftrag nennt den gewünschten elektronischen Weg, den Drittschuldner, den Zustellungsnachweis und den Rücklauf der Drittschuldnererklärung ausdrücklich; ohne eindeutigen Zustellungsnachweis wird keine Auskehrfrist berechnet
7. **Drittschuldnererklärung nach Paragraf 840 ZPO** abwarten (zwei Wochen). Reaktion auswerten: gepfändet, gesperrt, P-Konto, andere Pfändung vorrangig, Kontobeziehung beendet oder keine Geschäftsverbindung.
8. **P-Konto-Schutz prüfen**: Schuldner kann binnen vier Wochen nach Zustellung Umwandlung zum P-Konto verlangen, dann bleibt der Sockelbetrag nach Paragraf 850k ZPO frei. Erhöhungsbeträge nach Paragraf 850k Absatz 2 ZPO.
9. **Auszahlung** ggf. nach Ablauf des Moratoriums nach Paragraf 833a ZPO (vier Wochen) veranlassen; Verbraucher kann in dieser Zeit Vollstreckungsschutz beantragen.

## Reform-Stand Digitalisierung der Zwangsvollstreckung (BGBl. 2026 I Nr. 152)

| Datum | Was ändert sich |
| --- | --- |
| 1.10.2026 | Grundreform tritt in Kraft; elektronischer PfÜB-Antrag nach Paragraf 829a ZPO n.F. mit elektronisierten Titel-, Klausel- und Nachweisunterlagen. |
| 1.1.2027 | PfÜB-Formulare können bei elektronischer Einreichung als strukturierter XML-Datensatz nach Paragraf 829 Abs. 5 ZPO n.F. übermittelt werden; XML ist bei Doppeleinreichung führend. |
| 1.6.2027 | Kreditinstitute werden in Paragraf 173 Abs. 2 Nr. 1 ZPO n.F. einbezogen und müssen einen sicheren Übermittlungsweg eröffnen; elektronische Zustellung durch den Gerichtsvollzieher an Banken wird der Regelfall. |
| dauerhaft | Drittschuldnererklärung binnen zwei Wochen ab Zustellung; Aufforderung nach Paragraf 840 ZPO zusammen mit dem Pfändungsbeschluss übermitteln. |

Rechtsquellen: Gesetz zur weiteren Digitalisierung der Zwangsvollstreckung, BGBl. 2026 I Nr. 152; BT-Drs. 21/3737 und 21/4816.

## Leitentscheidungen

- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Ausgabeformat

```
PFÜB BANK [Mandant] gegen [Schuldner], Az [Gericht]

Titel: [Art, Datum, Aussteller]
Forderung: EUR Haupt + EUR Zinsen + EUR Kosten = EUR gesamt
Drittschuldner: [Bank], BIC [...]
Gepfändet: gesamtes Guthaben + künftige Eingänge / nur Habensaldo / ...
Antragsweg: Papier / beA / ab 1.1.2027 XML-Datensatz nach Paragraf 829 Abs. 5 ZPO n.F.
Zustellung Drittsch.: GV Papier / Post / freiwillig elektronisch / ab 1.6.2027 regelmäßig elektronisch an Kreditinstitut
P-Konto-Hinweis: [ja / nein – Schuldner kann Schutz nach Paragraf 850k ZPO beantragen]
Moratorium Paragraf 833a ZPO: [4 Wochen – Auszahlung frühestens am DD.MM.JJJJ]

NÄCHSTER SCHRITT: Drittschuldnererklärung in 2 Wochen abwarten
WIEDERVORLAGE: DD.MM.JJJJ
```

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht und Formatstandard.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig.
>
> **Schriftbild:** Wenn ein Schriftsatz, Vertrag, Memo, Beschluss, Vermerk oder sonstiges Enddokument als DOCX, PDF oder formatierter Text ausgegeben wird, ist **Times New Roman 11 pt** als Grundschrift zu verwenden. Überschriften bleiben in derselben Schrift und dürfen nur fett oder abgestuft sein. Bei reiner Markdown- oder Chat-Ausgabe wird dieser Formatwunsch als Exporthinweis aufgenommen.
>
> **Nummerierung:** Gliederung ausschließlich dezimal (`1`, `1.1`, `1.1.1` und so weiter). Keine römischen Ziffern, keine Buchstaben- oder Mischgliederung.
<!-- END ausformulierungspflicht (autogen) -->

## Qualitätsgates

- Niemals Pfändung der IBAN als Forderung – Drittschuldner ist die Bank.
- Niemals den Sockelbetrag P-Konto unter den aktuellen Wert legen.
- Niemals vor Ablauf des Moratoriums nach Paragraf 833a ZPO Auszahlung verlangen.
- Bei Pfändungsversuch trotz bekannter Insolvenz: STOPP nach Paragraf 89 InsO.
- Ab 1.6.2027 bei Kreditinstituten sicheren Übermittlungsweg prüfen und elektronische Zustellung dokumentieren; Papier oder Post nur begründen.
