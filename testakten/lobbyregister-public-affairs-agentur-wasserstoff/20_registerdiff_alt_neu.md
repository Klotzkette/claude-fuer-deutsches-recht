# Registerdiff alt/neu

**Bearbeitung:** Frederik Holst (Compliance Spreebogen), abgestimmt mit Dr. Annegret Beimer
**Stand:** 26.05.2026

## Alte Formulierung (verworfen, Stand 16.05.2026)

> "Spreebogen Regulatory vertritt die deutsche Wasserstoffwirtschaft bei Gesetzgebungsvorhaben."

**Begründung der Verwerfung:**

1. Verletzt § 5 des Mandatsvertrags HansaH2 (keine Branchenrepräsentation).
2. Überspannt die tatsächliche Mandatslage; Spreebogen hat nur zwei Auftraggeber zum WBG.
3. Verstoesst gegen Anlage 2 LobbyRG (Verhaltenskodex), weil das vertretene Interesse nicht spezifisch beschrieben wird.
4. Die Verwendung dieser Formulierung in der OpenGrid-Einladung (Fassung 1 vom 21.05.2026) hat einen Compliance-Vorfall ausgelöst.

## Neue Formulierung (Stand 26.05.2026)

> "Interessenvertretung im Auftrag einzelner Unternehmen und eines Konsortiums zur gesetzlichen Beschleunigung und regulatorischen Behandlung von Wasserstoffspeichern und Elektrolyseuren im Rahmen des geplanten Wasserstoffbeschleunigungsgesetzes (WBG)."

**Begründung der neuen Formulierung:**

1. Erfüllt § 5 des Mandatsvertrags HansaH2 (keine Branchenrepräsentation; konkrete Mandantinnen werden im Auftraggeberfeld genannt).
2. Beschreibt das Vorhaben konkret: "Wasserstoffbeschleunigungsgesetz (WBG)" statt "Wasserstoffwirtschaft allgemein".
3. Differenziert die Interessen: Speicher (HansaH2) und Elektrolyse (Konsortium).
4. Vermeidet "Branchenmandat"-Sprache und ist mit der Auftraggeberseite konsistent.

## Diff im JSON

| Feld | Alt | Neu |
|---|---|---|
| `taetigkeit.kurzbeschreibung` | "Spreebogen Regulatory vertritt die deutsche Wasserstoffwirtschaft bei Gesetzgebungsvorhaben." | "Interessenvertretung im Auftrag einzelner Unternehmen und eines Konsortiums zur gesetzlichen Beschleunigung und regulatorischen Behandlung von Wasserstoffspeichern und Elektrolyseuren im Rahmen des geplanten Wasserstoffbeschleunigungsgesetzes (WBG)." |
| `taetigkeit.ausschluss` | nicht vorhanden | "Spreebogen vertritt keine Branchen, keine Verbände und keine Konsortien jenseits der ausdrücklich genannten Auftraggeber. Eine Aussenkommunikation 'im Namen der deutschen Wasserstoffindustrie' ist ausdrücklich ausgeschlossen." |
| `auftraggeber[0].interesse` | "Speicherprivilegierung und Planungsbeschleunigung" | "Speicherprivilegierung, Planungsbeschleunigung, Klarstellung Duldungspflichten, Übergangsfristen für bestehende Speicherprojekte" |
| `auftraggeber[1].interesse` | "Anschlussprivileg für Elektrolyseure" | "Netzentgeltprivileg für Elektrolyseure mit Volllaststundenrahmen, Flächenzugang an Offshore-Anbindungspunkten, technologieoffene Förderung, Pilotprojekte ohne uneinheitliche Länderpraxis" |
| `unterauftragnehmer` | nicht vorhanden / nur "prüfen" | OpenGrid Events UG mit Compliance-Hinweis und Vertragsergänzung |
| `stellungnahmen` | nur Eintrag aus 16.05.2026 ohne Veroeffentlichungs-URL | zwei vollständige Einträge mit Versanddatum, Quartal und Veroeffentlichungs-URL |

## Genehmigungsstand

| Genehmigungsstelle | Status | Datum |
|---|---|---|
| HansaH2 Storage AG (Christine Luehrs) | freigegeben mit Änderungen am 26.05.2026 | 26.05.2026 |
| Nordsee Elektrolyse Konsortium GbR (Konsortialbeschluss) | freigegeben | 19.05.2026 |
| Stern & Partner mbB (Dr. Beimer) | freigegeben mit RFS-Vorbehalt | 26.05.2026 |
| Spreebogen Geschäftsführung (Mara Wendt) | freigegeben | 26.05.2026 |

## Einspieltermin

30.05.2026, vor dem Fachgespräch am 12.06.2026 und vor dem Q2-Upload am 30.06.2026.
