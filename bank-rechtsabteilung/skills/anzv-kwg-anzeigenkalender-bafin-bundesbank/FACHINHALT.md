---
name: anzv-kwg-anzeigenkalender-bafin-bundesbank
description: "Für AnzV/KWG-Anzeigenkalender BaFin und Bundesbank: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt."
---

# AnzV/KWG-Anzeigenkalender BaFin und Bundesbank

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Worum es geht

Erstellt einen operativen Anzeigenkalender für KWG-Institute nach der Anzeigenverordnung (AnzV) und § 24 KWG. Er deckt alle meldepflichtigen Ereignisse ab: Organpersonenwechsel, qualifizierte Beteiligungen, enge Verbindungen, Auslagerungen, Vergütungssysteme, Millionenkredite und LEI-Aktualisierungen. Einreichweg (BaFin-Portal oder Bundesbank-Meldewesen) und Unterlagen werden für jede Anzeige konkret benannt.

## Kernnormen

- **§ 24 Abs. 1 KWG** – laufende Anzeigepflichten: Nr. 1 Organpersonen (sofort), Nr. 11 qualifizierte Beteiligung (vor Vollzug), Nr. 12 Unterschreiten 10 % (unverzüglich), Nr. 14 enge Verbindungen, Nr. 16 Beteiligungen an Unternehmen, Nr. 19 wesentliche IT-Auslagerungen
- **§ 24 Abs. 1a KWG** – Geschäftsführer-Änderungen bei Finanzholdings; Abs. 3a Finanzkonglomerate
- **AnzV §§ 1–21** – Formvorschriften für jede Anzeigeart: § 4 Organpersonen, § 5 Beteiligungen, § 11 Millionenkredite (§ 14 KWG-Anzeige), § 13 Auslagerungen, § 21 Vergütungssystem
- **§ 14 KWG** – Millionenkreditmeldung: Meldegrenze 1 Mio. Euro, vierteljährliche Meldung an Bundesbank, COREP-Schnittstelle
- **Paragraf 25h KWG** – interne Sicherungsmaßnahmen von Instituten; die Verdachtsmeldepflicht folgt aus Paragraf 43 GwG, das weitere Meldeverfahren aus Paragrafen 43 bis 48 GwG
- **§ 2c KWG** – Inhaberkontrolle: Anzeige Erwerb (60-Werktage-Frist), Veräußerung, Überschreiten jeder Schwelle (10/20/30/50 %); InhKontrollV-Formulare
- **AnzV § 11 i.V.m. § 14 KWG** – Millionenkreditregister; monatliche Meldung bei Überschreitung, Korrekturen bis zum 10. des Folgemonats
- **Bundesbank FINREP/COREP** – aufsichtliche Finanz- und Eigenmittelmeldungen; Turnus quartalsweise, jährlich; XML-Schema EBA-XBRL

## Prüfschritte

1. **Anlass identifizieren**: Organwechsel, Beteiligungsänderung, Auslagerung, Vergütungsänderung, Kreditschwelle – welche AnzV-Norm greift?
2. **Institut-Typ** (§ 1 Abs. 1 KWG, CRR): CRR-Kreditinstitut, Finanzdienstleistungsinstitut, Finanzholding, gemischte Finanzholding – unterschiedliche Meldepflichten.
3. **Frist berechnen**: § 24 KWG Nr. 1 (sofortige Anzeige), § 2c (60 Werktage vor Vollzug), § 14 KWG (10. des Folgequartals).
4. **Einreichweg**: BaFin-Meldung über MVPportal (Organpersonen, Beteiligungen), Bundesbank-Meldewesen (FINREP/COREP, Millionenkredite); bei SSM-Instituten: EZB-Direktmeldung.
5. **Unterlagen zusammenstellen** (AnzV §§ 4, 5, 13): Lebenslauf, Führungszeugnis, Selbstauskunft, Organigramm, Vertragsauszüge.
6. **Vergütungssystem** (AnzV § 21, InstVergV): Jährliche Anzeige bei wesentlicher Änderung; Offenlegungspflicht nach CRR Art. 450.
7. **Vollständigkeitskontrolle**: Hemmt unvollständige Anzeige BaFin-Fristlauf (§ 2c Abs. 1b KWG)?

## Typische Fallkonstellationen

- CFO-Wechsel: § 24 Abs. 1 Nr. 1 KWG sofortige Anzeige, AnzV § 4 Formular, Fit-and-Proper-Unterlagen § 25c KWG
- Investor überschreitet 20 %: § 2c KWG Inhaberkontrolle vor Vollzug, InhKontrollV-Formular, BaFin 60-Tage-Prüfung
- Neue Cloud-Auslagerung Kernbank: § 24 Abs. 1 Nr. 19 KWG, AnzV § 13, Risikoanalyse § 25b KWG
- Kreditlinie erstmals über 1 Mio. Euro: § 14 KWG Millionenkreditmeldung, Bundesbank-Formular, Meldetermin quartalsweise
- Vergütungssystem-Änderung (Bonus-Caps): AnzV § 21, InstVergV, EBA-Leitlinie EBA/GL/2021/04
