# Zahlungsunfähigkeits- und Überschuldungsprüfer

Für Insolvenzverwaltung, Kanzlei und Rechnungswesen. Rekonstruieren Sie aus Kontoauszügen, offenen Posten und Finanzierungsunterlagen, ab wann Zahlungsunfähigkeit nach § 17 InsO und insolvenzrechtliche Überschuldung nach § 19 InsO jeweils belegbar sind. Halten Sie pro Insolvenzgrund den ersten belastbaren Stichtag, die zeitliche Beweislücke und die Bedeutung für die später zu prüfenden Überweisungen fest.

## 1. Einstieg

| Arbeitsweg | Datei oder Download |
| --- | --- |
| Plugin für die laufende Arbeit | [Plugin-ZIP herunterladen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/zahlungsunfaehigkeits-und-ueberschuldungspruefer-v1.2.0/zahlungsunfaehigkeits-und-ueberschuldungspruefer.zip) |
| ChatGPT oder Claude ohne Plugin | [Werkstatt-Prompt als Markdown herunterladen](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=zahlungsunfaehigkeits-und-ueberschuldungspruefer/zahlungsunfaehigkeits-und-ueberschuldungspruefer-werkstatt.md) |
| Schneller erster Arbeitsstand | [Mini-Prompt als Markdown herunterladen](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=zahlungsunfaehigkeits-und-ueberschuldungspruefer/zahlungsunfaehigkeits-und-ueberschuldungspruefer-schnellstart.md) |
| Einzelne Arbeitsschritte | [Alle elf Skills](../skills-index/zahlungsunfaehigkeits-und-ueberschuldungspruefer.md) |

Laden Sie den Werkstatt-Prompt und zunächst nur den Ordner `Grundakte` in den Chat. Beginnen Sie mit dem Auftrag „Ordne den Eingang, gleiche die Konten und offenen Posten ab und zeige mir, welche Unterlagen und Tatsachen für die erste Prüfung fehlen.“ Danach lassen Sie die Stichtage mit ihrem Beweisstand untersuchen. Kontoauszüge allein zeigen keine vollständige Fälligkeitslage und tragen keine Fortbestehensprognose. Die Skills verbinden deshalb die Geldbewegungen mit Rechnungen, Zahlungsvereinbarungen, Verträgen, Planunterlagen und Vermögensnachweisen.

Im Originalformat-ZIP bleiben die Verfahrensunterlagen in `10_Verfahren` gesondert zugänglich. Das Grundakten-Sammelpaket enthält ausschließlich die Eingangsunterlagen der drei Unternehmen. Die unausgefüllten Wordvorlagen liegen außerhalb der Grundakte in `20_Vorlagen`. Rechtliche Vergleichsunterlagen und Recheneingaben zur Nachbesprechung liegen in einem eigenen Paket.

## 2. Applet und Kommandozeile

Starten Sie nach dem Entpacken des Plugin-ZIPs im Plugin-Ordner `node app/server.mjs`. Öffnen Sie die im Terminal genannte lokale Adresse. Das Applet verarbeitet strukturierte Stichtagsdaten im Browser. Es zeigt Aktiva I und II, Passiva I und II, die rechnerische Deckungslücke, den Verwertungsstatus und offene Eingaben. Rechts- und Beweisbewertungen wie die überwiegende Wahrscheinlichkeit der Fortführung werden mit ihren Quellen erfasst.

Für dieselbe Rechnung im Terminal verwenden Sie `node app/cli.mjs Eingabe.json`. Der [Eingabevertrag mit Beispiel](app/FORMAT.md) erklärt die Felder und die Anforderungen an Fundstellen. Eine exportierte JSON-Datei lässt sich zusammen mit den Originalbelegen im Chat gegenprüfen.

## 2.1. Anfechtungsschreiben und Klage vorbereiten

Der Ordner `Grundakte/09_Zahlungskomplex` enthält pro Unternehmen die Unterlagen zu ausgewählten Zahlungen oder Verrechnungen. Gleichen Sie diese mit den ursprünglichen Kontoauszügen ab und prüfen Sie Anspruchsgegner, maßgeblichen Antrag, Handlungszeitpunkt, Gläubigerbenachteiligung und Kenntnis. Die ausgewählten Vorgänge sind Prüfaufträge; ein Rückgewähranspruch wird dadurch nicht vorweggenommen.

Die Wordvorlagen enthalten ausgearbeitete Begründungsvarianten und beschriftete Eingabefelder. Wählen Sie die passenden Absätze aus und ersetzen Sie die Felder durch belegte Tatsachen. Antragsteller, Insolvenzverwalter und Schuldner haben getrennte Felder. Zinsen, Tilgung und Gegenleistung sowie Verrechnung und Erfüllungsanspruch werden gesondert behandelt. Interne Auswahlhinweise und die [Quellenprüfung](references/anfechtung-vorlagen-quellen.md) unterstützen die Bearbeitung.

| Arbeitsprodukt | Bearbeitbare Vorlage |
| --- | --- |
| Außergerichtliches Anfechtungsschreiben | [Word-Datei herunterladen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/zahlungsunfaehigkeits-und-ueberschuldungspruefer-v1.2.0/01_Anfechtungsschreiben.docx) |
| Anfechtungsklage einschließlich alternativer Forderungsklage | [Word-Datei herunterladen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/zahlungsunfaehigkeits-und-ueberschuldungspruefer-v1.2.0/02_Anfechtungsklage.docx) |
| Beide Vorlagen und Ausfüllhilfe | [Vorlagenpaket herunterladen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/zahlungsunfaehigkeits-und-ueberschuldungspruefer-v1.2.0/Insolvenzanfechtung_Vorlagen.zip) |

## 3. Testakten zur Vorbereitung einer Insolvenzanfechtung

> Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.
>
> This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

| Fall | Originalakten und Lesefassungen |
| --- | --- |
| Keramikfabrik Cottbus | [Aktenseite](../testakten/insolvenzreife-keramikfabrik-cottbus/README.md) · [Originalformat-ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/zahlungsunfaehigkeits-und-ueberschuldungspruefer-v1.2.0/testakte-insolvenzreife-keramikfabrik-cottbus.zip) |
| Metallbau Berlin-Zehlendorf | [Aktenseite](../testakten/insolvenzreife-metallbau-berlin-zehlendorf/README.md) · [Originalformat-ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/zahlungsunfaehigkeits-und-ueberschuldungspruefer-v1.2.0/testakte-insolvenzreife-metallbau-berlin-zehlendorf.zip) |
| Hubschrauberbetrieb Prenzlau | [Aktenseite](../testakten/insolvenzreife-hubschrauber-prenzlau/README.md) · [Originalformat-ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/zahlungsunfaehigkeits-und-ueberschuldungspruefer-v1.2.0/testakte-insolvenzreife-hubschrauber-prenzlau.zip) |
| Nur die drei Grundakten | [Grundakten-Sammel-ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/zahlungsunfaehigkeits-und-ueberschuldungspruefer-v1.2.0/Insolvenzreife_Drei_Grundakten.zip) |
| Alle drei Originalakten | [Sammel-ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/zahlungsunfaehigkeits-und-ueberschuldungspruefer-v1.2.0/Insolvenzreife_Drei_Originalakten.zip) |


Die drei Fälle verbinden 24 monatliche Bankauszüge pro Unternehmen mit Buchungsdaten, offenen Posten, Geschäftskorrespondenz und den zugehörigen Belegen. Papierartige Briefe und Rechnungen, E-Mails mit Anlagen, Excel und CSV bleiben als Originaldateien erhalten. Die Akten verlangen insbesondere die Prüfung von Verfügbarkeit, Fälligkeit, Durchsetzbarkeit, Bewertungsannahmen und dem damaligen Kenntnisstand.

## 4. Nachbesprechung

> Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.
>
> This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

[Stichtagskontrolle und Recheneingaben herunterladen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/zahlungsunfaehigkeits-und-ueberschuldungspruefer-v1.2.0/Stichtagskontrolle_Nachbesprechung.zip)

[Rechtsquellen und Aussagegrenzen](references/insolvenzreife-quellen.md) · [Versionshinweise](../docs/releases/zahlungsunfaehigkeits-und-ueberschuldungspruefer-v1.2.0.md)

[Insolvenzrecht](../insolvenzrecht/README.md) · [Insolvenzanfechtung](../insolvenzanfechtung/README.md) · [Testakten](../testakten/README.md) · [Download-Index](../ASSET_INDEX.md) · [Alle Skills im Repository](../SKILLS.md) · [Plugin-Dateien](.) · [Repository](../README.md)


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 11 Skills in diesem Plugin. Jeder Skillname und der Downloadlink laden den unveränderten Inhalt der zugehörigen `SKILL.md` als Markdown-Datei. Der eindeutige Dateiname enthält Plugin und Skill; Beschreibungen stammen aus dem jeweiligen `description`-Feld.

English: Complete list of all 11 skills in this plugin. Both links in each row download the unchanged `SKILL.md` content as a Markdown file with a unique plugin-and-skill filename.

| Skill | Beschreibung | Markdown-Download |
| --- | --- | --- |
| [`anfechtungsstichtage-aufbereiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=zahlungsunfaehigkeits-und-ueberschuldungspruefer/skills/anfechtungsstichtage-aufbereiten/SKILL.md) | Ordnet Zahlungen und Verrechnungen den Stichtagsbefunden und Antragsdaten zu. Prüft Tatbestand, Belege und Gegenargumente und erstellt auf Auftrag ein Anfechtungsschreiben oder eine Klage anhand ausfüllbarer Vorlagen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=zahlungsunfaehigkeits-und-ueberschuldungspruefer/skills/anfechtungsstichtage-aufbereiten/SKILL.md) |
| [`dreiwochenstatus-nachrechnen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=zahlungsunfaehigkeits-und-ueberschuldungspruefer/skills/dreiwochenstatus-nachrechnen/SKILL.md) | Berechnet den stichtagsbezogenen Status und die Liquiditätslücke aus Aktiva I, Aktiva II, Passiva I und Passiva II. Prüft Tagesverlauf, Zehnprozentregel, ihre beiden Ausnahmen und alternative Darlegungswege. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=zahlungsunfaehigkeits-und-ueberschuldungspruefer/skills/dreiwochenstatus-nachrechnen/SKILL.md) |
| [`eintrittszeitpunkte-eingrenzen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=zahlungsunfaehigkeits-und-ueberschuldungspruefer/skills/eintrittszeitpunkte-eingrenzen/SKILL.md) | Ermittelt aus Vergleichsstichtagen und datierten Ereignissen den frühesten belegten Eintritt oder einen belastbaren Zeitraum. Trennt spätere Bestätigung, damalige Erkennbarkeit und mögliche Erholung für beide Insolvenzgründe. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=zahlungsunfaehigkeits-und-ueberschuldungspruefer/skills/eintrittszeitpunkte-eingrenzen/SKILL.md) |
| [`fortbestehensprognose-rekonstruieren`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=zahlungsunfaehigkeits-und-ueberschuldungspruefer/skills/fortbestehensprognose-rekonstruieren/SKILL.md) | Rekonstruiert für den historischen Stichtag die überwiegende Wahrscheinlichkeit einer Unternehmensfortführung über zwölf Monate. Prüft Fortführungswillen, Finanzierung, Absatz, Kapazitäten und den Zeitpunkt eines Prognoseumschwungs. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=zahlungsunfaehigkeits-und-ueberschuldungspruefer/skills/fortbestehensprognose-rekonstruieren/SKILL.md) |
| [`insolvenzreife-stichtagsbezogen-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=zahlungsunfaehigkeits-und-ueberschuldungspruefer/skills/insolvenzreife-stichtagsbezogen-pruefen/SKILL.md) | Ermittelt aus Bankauszügen, Buchhaltung und Verträgen den nachweisbaren Eintritt von Zahlungsunfähigkeit und insolvenzrechtlicher Überschuldung. Liefert zwei getrennte Stichtagsbefunde und eine Belegmatrix für die Anfechtung. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=zahlungsunfaehigkeits-und-ueberschuldungspruefer/skills/insolvenzreife-stichtagsbezogen-pruefen/SKILL.md) |
| [`konto-buchungen-abgleichen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=zahlungsunfaehigkeits-und-ueberschuldungspruefer/skills/konto-buchungen-abgleichen/SKILL.md) | Ordnet Kontoauszüge, Buchungsjournal, offene Posten und Zahlungsbelege nach Bankkonto, Vorgang und Stichtag. Prüft Anfangs- und Endsalden, interne Umbuchungen, Rücklastschriften und fehlende Gegenbelege. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=zahlungsunfaehigkeits-und-ueberschuldungspruefer/skills/konto-buchungen-abgleichen/SKILL.md) |
| [`liquide-mittel-und-zufluesse-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=zahlungsunfaehigkeits-und-ueberschuldungspruefer/skills/liquide-mittel-und-zufluesse-pruefen/SKILL.md) | Ermittelt frei verfügbare Bankbestände, sofort abrufbare Kreditmittel und belastbare Zuflüsse innerhalb von drei Wochen. Prüft Sperren, Kreditbedingungen, Cashpooling und Drittmittel nach Zeitpunkt und Zahlweg. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=zahlungsunfaehigkeits-und-ueberschuldungspruefer/skills/liquide-mittel-und-zufluesse-pruefen/SKILL.md) |
| [`rangruecktritt-und-patronat-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=zahlungsunfaehigkeits-und-ueberschuldungspruefer/skills/rangruecktritt-und-patronat-pruefen/SKILL.md) | Prüft wirksamen Rangrücktritt, Stillhalteabreden und harte oder weiche Patronatserklärungen. Bestimmt die Folgen für fällige Zahlungspflichten, den Zwölfmonatsplan und den Überschuldungsstatus. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=zahlungsunfaehigkeits-und-ueberschuldungspruefer/skills/rangruecktritt-und-patronat-pruefen/SKILL.md) |
| [`ueberschuldungsstatus-bewerten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=zahlungsunfaehigkeits-und-ueberschuldungspruefer/skills/ueberschuldungsstatus-bewerten/SKILL.md) | Überführt Bilanz- und Anlagenunterlagen in einen stichtagsbezogenen Überschuldungsstatus. Prüft Verwertungswerte, stille Reserven und Lasten, Sicherheiten, Fremdeigentum und rangrücktrittsbedingte Korrekturen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=zahlungsunfaehigkeits-und-ueberschuldungspruefer/skills/ueberschuldungsstatus-bewerten/SKILL.md) |
| [`verbindlichkeiten-und-faelligkeit-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=zahlungsunfaehigkeits-und-ueberschuldungspruefer/skills/verbindlichkeiten-und-faelligkeit-pruefen/SKILL.md) | Prüft einzelne fällige und im Dreiwochenfenster neu fällige Verbindlichkeiten anhand von OPOS, Verträgen, Lohn- und Abgabenunterlagen. Bewertet Stundung, Einwendungen, Steueraufschub und Titel nach ihrer Wirkung. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=zahlungsunfaehigkeits-und-ueberschuldungspruefer/skills/verbindlichkeiten-und-faelligkeit-pruefen/SKILL.md) |
| [`zahlungseinstellung-wuerdigen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=zahlungsunfaehigkeits-und-ueberschuldungspruefer/skills/zahlungseinstellung-wuerdigen/SKILL.md) | Würdigt Rückstände, Mahnungen, abgebrochene Ratenpläne, Vollstreckungen und Gläubigerkommunikation für die gesetzliche Vermutung der Zahlungsunfähigkeit. Prüft Gegenindizien und eine allgemeine Wiederaufnahme. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=zahlungsunfaehigkeits-und-ueberschuldungspruefer/skills/zahlungseinstellung-wuerdigen/SKILL.md) |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
