---
name: aktenauszug-erstellen
description: "Für Aktenauszug Erstellen — Hauptworkflow: ordnet Akte, Belege und Lücken; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt."
---

# Aktenauszug Erstellen — Hauptworkflow

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: StPO § 147 Akteneinsicht im Ermittlungsverfahren auf Antrag, § 385 Abs. 3 Nebenkläger, ZPO § 299 jederzeit für Parteien, Bearbeitung i.d.R. 2-4 Wochen.
- Tragende Normen verifizieren: ZPO §§ 299, 299a, StPO §§ 147, 385, 406e, VwGO § 100, SGG § 120, FamFG § 13, BORA § 19 (Akteneinsicht), Aktenordnung (AktO), AnwGH-Bescheinigungen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Anwalt, Geschäftsstelle, Verteidiger, Nebenklägervertreter, Beigeordneter, ggf. Sachverständiger.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Akteneinsichtsantrag, Aktenauszug (chronologisch), Aktenvermerk, Aktenspiegel, Beweismittelübersicht, Zeitachse, Vollmacht — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Leitidee

Wer ein Gerichtsverfahren schnell erfassen muss — sei es beim Mandatswechsel, bei der Einarbeitung eines neuen Sachbearbeiters oder bei der Vorbereitung auf eine mündliche Verhandlung — benötigt einen strukturierten Überblick. Dieser Skill nimmt die gesamte Akte entgegen und erzeugt einen vollständigen Aktenauszug mit allen sechs Bausteinen.

## Triage zu Beginn — kläre vor Erstellung des Aktenauszugs

1. Welche Verfahrensart liegt vor? (Zivilprozess, Arbeitsgericht, Verwaltungsgericht, Sozialrecht, Strafprozess)
2. In welcher Instanz befindet sich das Verfahren? (Erstinstanz, Berufung, Revision)
3. Liegen alle wesentlichen Schriftsätze vor oder nur Teilakten?
4. Gibt es bereits einen Termin, dessen Vorbereitung im Vordergrund steht?
5. Soll der Aktenauszug intern (anwaltlich) oder zur Übergabe an Mandant dienen?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist für den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Zentrale Normen (Prozessrecht)

- §§ 128-134 ZPO — Schriftliches und mündliches Verfahren, Schriftsätze
- §§ 253-261 ZPO — Klageerhebung und Verfahrenseinleitung
- §§ 355-455 ZPO — Beweisaufnahme (Sachverstaendige, Zeugen, Augenschein, Urkunden)
- §§ 495a, 522, 540 ZPO — Vereinfachtes Verfahren, Berufungsverwerfung, Berufungsurteil
- §§ 704-945 ZPO — Zwangsvollstreckung (Abschnitt relevant für Vollstreckungstitel in Akte)
- § 91a ZPO — Kosten bei Erledigterklärung
- § 139 ZPO — Materielle Prozessleitung, richterliche Hinweispflicht

## Voraussetzungen

- Gerichtliche Akte oder wesentliche Teile davon (PDF, Word, maschinenlesbar)
- Optional: Inhaltsverzeichnis der Akte
- Optional: Hinweis auf die Verfahrensart (Zivil, Straf, Verwaltung, Arbeit, Sozial)

## Sechs Bausteine des Aktenauszugs

### Baustein 1 — Verfahrensidentifikation

Gericht, Kammer/Senat, Aktenzeichen, Streitwert, Parteien mit Anwälten, Instanz, Verfahrensart.

### Baustein 2 — Einleitungssatz

Ein bis zwei Sätze, die den Kern des Rechtsstreits nennen: Wer streitet mit wem worüber, welche Hauptnorm ist einschlägig.

### Baustein 3 — Zusammenfassung (Absatz)

Acht bis zehn Sätze: Hintergrund, Streitstand, prozessuale Lage, anstehende Verfahrenshandlungen.

### Baustein 4 — Sachverhaltschronologie

Chronologische Bullet-Liste aller wesentlichen außerprozessualen Tatsachen. Datum fettgedruckt vorangestellt.

### Baustein 5 — Verfahrenschronologie

Chronologische Bullet-Liste der prozessualen Schritte. Fristen und Termine werden hervorgehoben.

### Baustein 6 — Tabellen (Parteivortrag / Beweismittel / Rechtsargumente)

Drei separate Tabellen im Markdown-Format mit Spalten für Klägerseite und Beklagtenseite.

## Schritt-für-Schritt-Workflow

1. **Akte sichten** — Inhaltsverzeichnis oder Seitenstruktur erfassen; fehlende Seiten markieren
2. **Verfahrensart bestimmen** — aktiviere passenden Modus-Skill (Zivil/ArbG/VerwG/Sozial/Straf)
3. **Verfahrensidentifikation extrahieren** (→ Skill `verfahrensidentifikation`)
4. **Einleitungssatz formulieren** (→ Skill `einleitungssatz-generator`)
5. **Zusammenfassungsabsatz schreiben** (→ Skill `verfahrenszusammenfassung-absatz`)
6. **Sachverhalt chronologisch ordnen** (→ Skill `sachverhaltschronologie`)
7. **Verfahrensschritte chronologisch ordnen** (→ Skill `verfahrenschronologie`)
8. **Fristen hervorheben** (→ Skill `fristen-und-terminkalender`) — alle Notfristen mit ⚠️
9. **Parteivortrag gegenüberstellen** (→ Skill `parteivortrag-gegenueberstellung`)
10. **Beweismittel tabellarisch erfassen** (→ Skill `beweismittel-gegenueberstellung`)
11. **Rechtsargumente tabellarisch erfassen** (→ Skill `rechtsargumente-gegenueberstellung`)
12. **Neutralitätsprüfung** (→ Skill `neutralitaetspruefung`)
13. **Strukturprüfung** (→ Skill `aktenauszug-strukturpruefung`)

## Entscheidungsbaum — Verfahrensart

```
Liegt Akte vor?
 → Ja: Verfahrensart prüfen
 → Arbeitsgericht? → Skill arbeitsgerichtsverfahren-modus aktivieren
 → Verwaltungsgericht? → Skill verwaltungsprozess-modus aktivieren
 → Strafgericht? → Skill strafprozess-modus aktivieren
 → Sozialgericht? → Skill sozialgerichtsverfahren-modus aktivieren
 → Zivilgericht (LG/AG/OLG)? → Skill zivilprozess-modus aktivieren
 → Nein: Fehlende Unterlagen beim Mandanten anfordern; Notfrist prüfen
```

## Output-Format

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht und Formatstandard.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig.
>
> **Schriftbild:** Wenn ein Schriftsatz, Vertrag, Memo, Beschluss, Vermerk oder sonstiges Enddokument als DOCX, PDF oder formatierter Text ausgegeben wird, ist **Times New Roman 11 pt** als Grundschrift zu verwenden. Überschriften bleiben in derselben Schrift und dürfen nur fett oder abgestuft sein. Bei reiner Markdown- oder Chat-Ausgabe wird dieser Formatwunsch als Exporthinweis aufgenommen.
>
> **Nummerierung:** Gliederung ausschließlich dezimal (`1`, `1.1`, `1.1.1` und so weiter). Keine römischen Ziffern, keine Buchstaben- oder Mischgliederung.
<!-- END ausformulierungspflicht (autogen) -->

```markdown
### Aktenauszug — [Aktenzeichen]
## Verfahrensidentifikation
...

## Einleitungssatz
...

## Zusammenfassung
...

## Sachverhaltschronologie
- **TT.MM.JJJJ** Beschreibung
- **TT.MM.JJJJ** Beschreibung

## Verfahrenschronologie
- **TT.MM.JJJJ** Beschreibung
- ⚠️ **TT.MM.JJJJ — FRIST:** Beschreibung

## Parteivortrag

| Punkt | Klägerseite | Beklagtenseite |
|---|---|---|

## Beweismittel

| Beweismittel | Klägerseite | Beklagtenseite |
|---|---|---|

## Rechtsargumente

| Aspekt | Klägerseite | Beklagtenseite |
|---|---|---|
```

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu prüfen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — strukturierter Aktenauszug für Gericht | Vollformat nach den sechs Bausteinen unten |
| Variante A — nur interne Einarbeitung noetig | Kurzform ohne Verfahrenschronologie; Bausteine 1-3 genügen |
| Variante B — Eilsache; Zeit fehlt für vollstaendigen Auszug | Einleitungssatz + Sachverhaltschronologie priorisieren; Rest nachliefern |
| Variante C — Parteivertreter hat bereits Zusammenfassung geliefert | Kritische Prüfung und Ergaenzung statt Neuerstellung |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

## Output-Template Übergabevermerk (intern)

**Adressat:** Sachbearbeiter / aufnehmender Anwalt — Tonfall: sachlich-juristisch

```
ÜBERGABEVERMERK — [AKTENZEICHEN]
Bearbeiter bisher: [NAME]
Stand: [DATUM]

Verfahren: [KURZBEZEICHNUNG]
Nächste Frist: [DATUM + BEZEICHNUNG]
Nächster Termin: [DATUM + ORT]
Offene Aufgaben: [LISTE]

Besonderheiten: [z.B. Beweissicherungsantrag gestellt, SV noch nicht bestellt]
```

--- vor Versand klären ---
1. Welches Verhandlungsziel hat der Mandant? [Bestand / Abfindung / Reputation / Schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestabfindung / Freistellung / Zeugnisformulierung]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgespraech / Settlement vor Klageerhebung]

## Qualitätsgrundsätze

- Keine Erfolgsprognose
- Neutrale Sprache ohne Wertung
- Alle Fristen und Termine hervorgehoben
- Keine KI-Terminologie im Output

## Hinweis

Der Aktenauszug ersetzt nicht die eigene Aktenlektüre. Er ist ein strukturiertes Arbeits- und Kommunikationsmittel für den anwaltlichen Alltag und bedarf der Prüfung durch den verantwortlichen Rechtsanwalt.

## Quellenkontrolle

Ein Aktenauszug übernimmt Rechtsprechung nicht als bloße Aktenzeichenliste. Jede Entscheidung wird mit Gericht, Datum, Aktenzeichen, Fundstelle, Streitfrage, tragender Aussage und prozessualer Bedeutung erfasst. Akteneinsicht und Aktenzugang richten sich nach dem konkreten Verfahren, insbesondere Paragraf 299 ZPO, Paragraf 147 StPO, Paragraf 100 VwGO, Paragraf 120 SGG oder Paragraf 13 FamFG; Normen verschiedener Rechtswege nicht vermischen.

> Quellenregel: Entscheidungen nur nach Prüfung einer amtlichen oder frei zugänglichen Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage ausgeben.
