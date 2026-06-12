# Megaprompt: bgb-bt-pruefer

## Zusammensetzung

Dieser Megaprompt enthaelt top-8 von 101 Skills (gekuerzt fuer Chat-Fenster) des Plugins `bgb-bt-pruefer`.

## Inhaltsverzeichnis

1. **kaltstart-triage** — Einstieg, Schnelltriage und Skill-Routing für BGB-BT-Fälle: Anspruchsziel, Vertragstyp, gesetzliches Schuldverhältnis, S…
2. **amtlicher-bgb-auftrag-unentgeltliche** — Amtlicher Normcheck für BGB-BT-Fälle: prüft Vertragstypen, Leistungsstörung, AGB, Verbraucherrecht, digitale Produkte, K…
3. **dokumente-intake** — Dokumentenintake für BGB Besonderer Teil — Prüfungsschemata: sortiert Verträge, Lieferscheine, Rechnungen, prüft Datum, …
4. **arbeitsnaher-dienstvertrag-bauvertrag** — Prüft zivilrechtliche Dienstleistungsverhältnisse mit Arbeitsrechtsnähe, Scheinselbstständigkeit und Vergütungsfragen na…
5. **goa-entgegenstehender-wille-paragraphen-678-679** — Prüft GoA gegen den Willen des Geschäftsherrn §§ 678 und 679 BGB: erhöhte Haftung und Ausnahmen bei Erfüllung gesetzlich…
6. **deliktsrecht-sonstiges-tierhalter-gebaeude** — Prüft sonstige Rechte nach § 823 Abs. 1 BGB: allgemeines Persönlichkeitsrecht, Recht am Gewerbebetrieb und Immaterialgüt…
7. **kaufrecht-ware-leasing-schnittstelle** — Prüft Kaufvertrag über Ware mit digitalen Elementen § 475b BGB: Mangelfreiheit, Updatepflichten und Verhältnis zu §§ 327…
8. **arbeitsnaher-dienstvertrag-bgb** — Prüft zivilrechtliche Dienstleistungsverhältnisse mit Arbeitsrechtsnähe, Scheinselbstständigkeit und Vergütungsfragen na…

---

## Skill: `kaltstart-triage`

_Einstieg, Schnelltriage und Skill-Routing für BGB-BT-Fälle: Anspruchsziel, Vertragstyp, gesetzliches Schuldverhältnis, Störung, Beweise, Fristen und Output._

# BGB BT Kommandocenter

## Aktenstart statt Formularstart

Wenn zu **Kaltstart Triage** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde fuer **Bgb Bt Pruefer** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Sofortstart

1. Kläre Rolle, Ziel, Gegner, Frist, Dokumente und gewünschtes Arbeitsprodukt.
2. Zerlege den Fall in Tatsachen, Normen, Streitpunkte, Beweisfragen und methodische Wertungen.
3. Liefere zuerst eine Kurzantwort mit Risikoampel, danach den Prüfpfad.
4. Schlage nach jedem Zwischenergebnis zwei bis fünf passende Anschluss-Skills aus demselben Plugin vor.

## Rechts- und Quellenanker

BGB amtlich prüfen: https://www.gesetze-im-internet.de/bgb/. Je nach Skill insbesondere §§ 241 ff., 249 ff., 280 ff., 433 ff., 488 ff., 535 ff., 581 ff., 611 ff., 631 ff., 662 ff., 675 ff., 677 ff., 765 ff., 812 ff., 823 ff. BGB.
Bei tragenden Normfragen `amtlicher-bgb-bt-normcheck` zuschalten; er nutzt den neuen BGB-BT-Normkern und routet in ZPO-Durchsetzung, wenn ein Klage-, Mahn- oder Eilprodukt entstehen soll.

## Stoppschilder

- Keine Kommentar-, Aufsatz- oder BeckRS/Juris-Blindzitate.
- Tragende Gesetzesstände live gegen amtliche/frei zugängliche Quellen prüfen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und überprüfbarer Quelle verwenden.
- Bei Unsicherheit die Annahme ausdrücklich markieren und eine Rückfrage oder Quellenprüfung auslösen.

## Quellen

- https://www.gesetze-im-internet.de/bgb/
- https://www.bundesgerichtshof.de/
- https://dejure.org/gesetze/BGB

---

## Skill: `amtlicher-bgb-auftrag-unentgeltliche`

_Amtlicher Normcheck für BGB-BT-Fälle: prüft Vertragstypen, Leistungsstörung, AGB, Verbraucherrecht, digitale Produkte, Kauf, Miete, Dienst, Werk, Auftrag, GoA, Bürgschaft, Bereicherung und Delikt gegen die aktuelle BGB-Fassung im BGB BT._

# Amtlicher BGB-BT-Normcheck

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: BGB §§ 535-577a, BetrKV, WEG §§ 24, 25, 27, BGB §§ 558, 558a, 558b, 573, 573c — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Prüfroute

1. Vertragliche Beziehung bestimmen: Kauf, Miete, Darlehen, Dienst, Werk, Auftrag/Geschäftsbesorgung, Bürgschaft, Vergleich oder Mischvertrag.
2. Gesetzliche Beziehung bestimmen: GoA, Bereicherung, Delikt, Gesamtschuld/Regress.
3. BGB AT als Vorfrage prüfen: Vertragsschluss, Form, Stellvertretung, Anfechtung, Verjährung.
4. Aktuelle Norm live prüfen, wenn sie trägt.
5. ZPO-Durchsetzung prüfen, wenn ein Schriftsatz, Mahnbescheid, Eilantrag oder Beweisverfahren entstehen soll.

## Normlandkarte

| Bereich | Normen | Typischer Output |
| --- | --- | --- |
| Leistungsstörung | §§ 241, 249, 253, 275-304 BGB | Pflichtverletzungs- und Schadensmatrix |
| AGB | §§ 305-310 BGB | Klauselampel |
| Verbraucher/Fernabsatz | §§ 312 ff. BGB | Informations-/Widerrufscheck |
| Digitale Produkte | §§ 327 ff. BGB | Bereitstellungs- und Updateprüfung |
| Kauf | §§ 433-479 BGB | Mängelrechte, Nacherfüllung, Rücktritt, Minderung, Schadensersatz |
| Ware mit digitalen Elementen | §§ 475b, 475c, 476, 477 BGB | Update-, Beweislast- und Abweichungsvereinbarung |
| Miete/Pacht | §§ 535 ff., 581 ff. BGB | Gebrauch, Mangel, Minderung, Kündigung, § 550 BGB |
| Dienst/Behandlung | §§ 611, 611a, 630a ff. BGB | Dienstpflicht, Arbeitnehmerabgrenzung, Behandlungsvertrag |
| Werk/Bau | §§ 631 ff. BGB | Abnahme, Mängelrechte, Kündigung, Vergütung |
| Auftrag/Geschäftsbesorgung | §§ 662 ff., 675 ff. BGB | unentgeltlich/entgeltlich, Geschäftsbesorgung, Zahlungsschnittstelle |
| GoA | §§ 677-687 BGB | berechtigte/unberechtigte/unechte GoA |
| Bürgschaft | §§ 765 ff. BGB | Akzessorietät, Schriftform, Einreden |
| Bereicherung | §§ 812-822 BGB | Leistung/Nichtleistung, Rechtsgrund, Entreicherung |
| Delikt | §§ 823-853 BGB | Rechtsgut, Schutzgesetz, § 826, Verrichtungsgehilfe, Gefährdungsnähe |

## Referenz

Nutze `references/amtlicher-bgb-bt-normkern.md`.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 3 ProdHaftG
- Art. 32 DSGVO
- § 4 ProdHaftG
- § 8 ProdHaftG
- § 2 ProdHaftG
- § 1 ProdHaftG
- § 10 ProdHaftG
- § 9 ProdHaftG
- § 2 WoVermG
- Art. 82 DSGVO

### Leitentscheidungen

- BVerfGE Band 6 Rn 32 (Lüth, Drittwirkung der Grundrechte)
- BVerwG 6 C 12.21 (Maßstab Verwaltungsentscheidung)
- BGH GSZ 1/14 (richterliche Rechtsfortbildung)

---

## Skill: `dokumente-intake`

_Dokumentenintake für BGB Besonderer Teil — Prüfungsschemata: sortiert Verträge, Lieferscheine, Rechnungen, prüft Datum, Absender, Frist und Beweiswert (Urkunden, Zeugen); markiert Lücken; berücksichtigt Mandatsgeheimnis § 43a BRAO._

# Dokumentenintake

## Aktenstart statt Formularstart

Wenn zu **Dokumente Intake** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde fuer **Bgb Bt Pruefer** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Einsatzlage

Dieser Dokumenten-Intake für **Bgb Bt Prüfer** ordnet Anlagen, Registerdaten, Korrespondenz, Bescheide, Fristen und Beleglücken zu einer belastbaren Arbeitsakte.

## Fachlandkarte dieses Plugins

- `amtlicher-bgb-auftrag-unentgeltliche` — Amtlicher BGB Auftrag Unentgeltliche
- `anfangercoach-schuldrecht-anspruchslandkarte` — Anfangercoach Schuldrecht Anspruchslandkarte
- `anfangercoach-schuldrecht-bt` — Anfangercoach Schuldrecht BT
- `anspruchslandkarte-vertragstypen` — Anspruchslandkarte Vertragstypen
- `arbeitsnaher-dienstvertrag-bauvertrag` — Arbeitsnaher Dienstvertrag Bauvertrag
- `arbeitsnaher-dienstvertrag-bgb` — Arbeitsnaher Dienstvertrag BGB
- `auftrag-und-unentgeltliche-taetigkeit` — Auftrag und Unentgeltliche Taetigkeit
- `bauvertrag-und-verbraucherbauvertrag` — Bauvertrag und Verbraucherbauvertrag
- `bereicherungsrecht-entreicherung-saldotheorie` — Bereicherungsrecht Entreicherung Saldotheorie
- `bereicherungsrecht-entreicherung-und-saldotheorie` — Bereicherungsrecht Entreicherung und Saldotheorie
- `bereicherungsrecht-leistungskondiktion` — Bereicherungsrecht Leistungskondiktion
- `bereicherungsrecht-nichtleistungskondiktion` — Bereicherungsrecht Nichtleistungskondiktion
- `beweislast-belegmatrix` — Beweislast Belegmatrix

## Arbeitsweg

- Eingangsdokumente nach Typ ordnen: Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets.
- Pro Dokument prüfen: Datum, Absender, Empfänger, Zustellungsnachweis, Fristwirkung, Beweiswert für die Bgb Bt Pruefer-Frage.
- Lücken, Widersprüche, fehlende Anlagen und ungeklärte Zustellungen markieren; bei Original-Beweisbedarf auf Beweissicherung achten.
- Tragende Normen vorläufig zuordnen: BGB — Endfeststellung erst nach Live-Check.
- Sensible Daten nach Berufsrecht, DSGVO und Mandatsgeheimnis behandeln; Akteneinsichts- und Herausgabepflichten gegenüber Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen prüfen.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

---

## Skill: `arbeitsnaher-dienstvertrag-bauvertrag`

_Prüft zivilrechtliche Dienstleistungsverhältnisse mit Arbeitsrechtsnähe, Scheinselbstständigkeit und Vergütungsfragen nach §§ 611 ff. BGB im BGB BT._

# Arbeitsnaher Dienstvertrag im BGB

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: BGB §§ 535-577a, BetrKV, WEG §§ 24, 25, 27, BGB §§ 558, 558a, 558b, 573, 573c — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: Arbeitsnaher Dienstvertrag im BGB
- **Normen-/Quellenanker:** BGB Besonderer Teil: Kaufrecht, Werk-/Dienstvertrag, Auftrag/Geschäftsbesorgung, Miet-/Leasingnähe, GoA, Bereicherung, Delikt, Verjährung und AGB-Schnittstellen.
- **Entscheidende Weiche:** Anspruchsgrundlage, Vertragstyp/Mischvertrag, Pflichtverletzung, Vertretenmüssen, Schaden, Einwendung und Beweisfrage sauber trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.

## Normanker

- §§ 611–630h BGB: Dienstvertrag, Vergütung, Kündigung, Behandlungsvertrag
- § 611a BGB: Arbeitnehmer-Definition, Weisungsgebundenheit
- § 612 BGB: Vergütung ohne ausdrückliche Abrede
- § 621 BGB: Kündigungsfristen bei Dienstverhältnissen
- §§ 157 und 242 BGB: Auslegung und Treu und Glauben
- Sozialversicherungsrecht: § 7 SGB IV (Beschäftigung und Scheinselbstständigkeit)
- BAG-Rechtsprechung zu Arbeitnehmereigenschaft: nur nach Live-Prüfung mit Aktenzeichen zitieren

## Intake

- Welche Parteien und welche Leistungspflichten sind vereinbart?
- Liegt ein schriftlicher Vertrag vor; welche Bezeichnung wurde gewählt?
- Wie ist die tatsächliche Durchführung: Weisungen, Arbeitszeit, Arbeitsort, Eingliederung?
- Welche Vergütung wurde vereinbart und wie wird abgerechnet?
- Ist eine Kündigung ausgesprochen oder beabsichtigt; welche Fristen gelten?
- Gibt es Hinweise auf Scheinselbstständigkeit oder laufende Statusfeststellungsverfahren?

## Prüfraster

1. Vertragstyp bestimmen: Dienst-, Arbeits-, Werk- oder Auftragsverhältnis?
2. Abgrenzungskriterien nach § 611a BGB prüfen: persönliche Abhängigkeit, Weisungsgebundenheit, Eingliederung
3. Tatsächliche Durchführung der Leistung mit Vertragslage vergleichen (substance over form)
4. Vergütungsanspruch nach § 612 BGB prüfen, wenn keine ausdrückliche Vereinbarung besteht
5. Kündigungsfristen nach § 621 BGB berechnen; bei Arbeitsverhältnis § 622 BGB anwenden
6. Scheinselbstständigkeit: sozialversicherungsrechtliche Folgen nach § 7 SGB IV berücksichtigen
7. Haftungsfragen bei fehlerhafter Leistung prüfen: §§ 280 und 241 Abs. 2 BGB
8. Verjährung der Vergütungsansprüche nach §§ 195 und 199 BGB

## Fallstricke

- Vertragliche Bezeichnung als „freier Mitarbeiter" schützt nicht vor Umqualifizierung durch Gerichte.
- Faktische Weisungsgebundenheit begründet Arbeitnehmereigenschaft unabhängig vom Vertragstext.
- Vergütungsansprüche können nach § 612 BGB entstehen, auch wenn kein Betrag vereinbart wurde.
- Sozialversicherungsrechtliche Nachforderungen können rückwirkend vier Jahre betragen.

## Stoppschilder

- Keine Kommentar-, Aufsatz- oder BeckRS/Juris-Blindzitate.
- Tragende Gesetzesstände live gegen amtliche/frei zugängliche Quellen prüfen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und überprüfbarer Quelle verwenden.
- Bei Unsicherheit die Annahme ausdrücklich markieren und eine Rückfrage oder Quellenprüfung auslösen.

## Anschluss-Skills

- dienstvertrag-und-behandlungsvertrag
- werk-dienst-abgrenzung-erfolg
- geschaeftsbesorgung-auftrag-mandat
- workflow-anfangercoach-schuldrecht-bt

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 3 ProdHaftG
- Art. 32 DSGVO
- § 4 ProdHaftG
- § 8 ProdHaftG
- § 2 ProdHaftG
- § 1 ProdHaftG
- § 10 ProdHaftG
- § 9 ProdHaftG
- § 2 WoVermG
- Art. 82 DSGVO

### Leitentscheidungen

- BVerfGE Band 6 Rn 32 (Lüth, Drittwirkung der Grundrechte)
- BVerwG 6 C 12.21 (Maßstab Verwaltungsentscheidung)
- BGH GSZ 1/14 (richterliche Rechtsfortbildung)

---

## Skill: `goa-entgegenstehender-wille-paragraphen-678-679`

_Prüft GoA gegen den Willen des Geschäftsherrn §§ 678 und 679 BGB: erhöhte Haftung und Ausnahmen bei Erfüllung gesetzlicher Pflichten im BGB BT._

# GoA: Entgegenstehender Wille §§ 678 und 679 BGB

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: BGB §§ 535-577a, BetrKV, WEG §§ 24, 25, 27, BGB §§ 558, 558a, 558b, 573, 573c — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: GoA: Entgegenstehender Wille §§ 678 und 679 BGB
- **Normen-/Quellenanker:** BGB Besonderer Teil: Kaufrecht, Werk-/Dienstvertrag, Auftrag/Geschäftsbesorgung, Miet-/Leasingnähe, GoA, Bereicherung, Delikt, Verjährung und AGB-Schnittstellen.
- **Entscheidende Weiche:** Anspruchsgrundlage, Vertragstyp/Mischvertrag, Pflichtverletzung, Vertretenmüssen, Schaden, Einwendung und Beweisfrage sauber trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.

## Normanker

- § 677 BGB: Pflichten des Geschäftsführers
- § 678 BGB: Übernahme gegen den Willen des Geschäftsherrn (erhöhte Haftung)
- § 679 BGB: Ausnahmen vom entgegenstehenden Willen (Pflicht liegt im öffentlichen Interesse oder gesetzliche Unterhaltspflicht)
- § 680 BGB: Geschäftsführung zur Gefahrenabwehr
- § 683 BGB: Aufwendungsersatz bei berechtigter GoA
- § 684 BGB: Bereicherungsanspruch bei unberechtigter GoA

## Intake

- Hat der Geschäftsführer von einem entgegenstehenden Willen des Geschäftsherrn gewusst oder musste er davon ausgehen?
- War der entgegenstehende Wille nach § 679 BGB unbeachtlich (Erfüllung gesetzlicher Pflicht, Notfall)?
- Liegt eine Geschäftsführung zur Abwehr einer dringenden Gefahr nach § 680 BGB vor?
- Welche Aufwendungen sind entstanden und wer soll sie ersetzen?

## Prüfraster

1. GoA-Grundschema: fremdes Geschäft, Fremdgeschäftsführungswille, ohne Auftrag oder Berechtigung
2. Entgegenstehender Wille des Geschäftsherrn: ausdrücklich oder konkludent; Kenntnis des Geschäftsführers
3. Erhöhte Haftung nach § 678 BGB: auch für Zufall, wenn entgegenstehender Wille bekannt war
4. Ausnahmen nach § 679 BGB: öffentlich-rechtliche Pflicht, gesetzliche Unterhaltspflicht des Geschäftsherrn
5. Gefahrenabwehr nach § 680 BGB: nur Haftung für Vorsatz und grobe Fahrlässigkeit
6. Aufwendungsersatz: bei berechtigter GoA (§ 683 BGB); bei unberechtigter nur Bereicherungsanspruch (§ 684 BGB)
7. Herausgabepflicht des Geschäftsführers nach § 681 BGB
8. Verjährung: §§ 195 und 199 BGB

## Fallstricke

- Erhöhte Haftung nach § 678 BGB greift nur bei Kenntnis oder Kennenmüssen des entgegenstehenden Willens.
- § 679 BGB ist restriktiv auszulegen; bloße Nützlichkeit der Handlung genügt nicht.
- Gefahrenabwehr nach § 680 BGB setzt unmittelbare Gefahr für Person oder Sache voraus.
- Aufwendungsersatz nach § 684 BGB ist ein Bereicherungsanspruch, kein Schadensersatz.

## Stoppschilder

- Keine Kommentar-, Aufsatz- oder BeckRS/Juris-Blindzitate.
- Tragende Gesetzesstände live gegen amtliche/frei zugängliche Quellen prüfen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und überprüfbarer Quelle verwenden.
- Bei Unsicherheit die Annahme ausdrücklich markieren und eine Rückfrage oder Quellenprüfung auslösen.

## Anschluss-Skills

- goa-grundschema-paragraph-677
- unechte-goa-paragraph-687
- auftrag-und-unentgeltliche-taetigkeit
- bereicherungsrecht-leistungskondiktion

## Quellen

- https://www.gesetze-im-internet.de/bgb/__678.html
- https://www.gesetze-im-internet.de/bgb/__679.html
- https://www.gesetze-im-internet.de/bgb/__677.html

---

## Skill: `deliktsrecht-sonstiges-tierhalter-gebaeude`

_Prüft sonstige Rechte nach § 823 Abs. 1 BGB: allgemeines Persönlichkeitsrecht, Recht am Gewerbebetrieb und Immaterialgüterrechte im BGB BT._

# Deliktsrecht: Sonstiges Recht

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: BGB §§ 535-577a, BetrKV, WEG §§ 24, 25, 27, BGB §§ 558, 558a, 558b, 573, 573c — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: Deliktsrecht: Sonstiges Recht
- **Normen-/Quellenanker:** BGB Besonderer Teil: Kaufrecht, Werk-/Dienstvertrag, Auftrag/Geschäftsbesorgung, Miet-/Leasingnähe, GoA, Bereicherung, Delikt, Verjährung und AGB-Schnittstellen.
- **Entscheidende Weiche:** Anspruchsgrundlage, Vertragstyp/Mischvertrag, Pflichtverletzung, Vertretenmüssen, Schaden, Einwendung und Beweisfrage sauber trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.

## Normanker

- § 823 Abs. 1 BGB: sonstige Rechte (Auffangtatbestand für absolute Rechte)
- Art. 1 Abs. 1 und Art. 2 Abs. 1 GG: allgemeines Persönlichkeitsrecht als Verfassungsgrundlage
- § 12 BGB: Namensrecht
- § 1004 BGB analog: quasi-negatorischer Unterlassungsanspruch
- UrhG, MarkenG, PatG: spezialgesetzliche Deliktsregeln, die § 823 BGB verdrängen können
- BGH-Linie zum APR: nur nach Live-Prüfung zitieren

## Intake

- Welches Recht ist verletzt: APR, Recht am Gewerbebetrieb, Urheberrecht, Marke?
- Ist das betroffene Recht ein sonstiges Recht im Sinne des § 823 Abs. 1 BGB?
- Greift eine spezialgesetzliche Regelung (UrhG, MarkenG), die § 823 BGB verdrängt?
- Ist ein immaterieller Schaden entstanden (APR-Verletzung: Geldentschädigung)?
- Besteht ein Unterlassungsanspruch nach § 1004 BGB analog?

## Prüfraster

1. Einordnung: absolutes Recht, das den Charakter eines sonstigen Rechts hat
2. APR-Verletzung: Eingriff in Kernbereich der Persönlichkeit, Abwägung mit anderen Grundrechten
3. Recht am Gewerbebetrieb: unmittelbarer betriebsbezogener Eingriff erforderlich (restriktiv)
4. Immaterialgüterrechte: Abgrenzung zu spezialgesetzlichen Haftungsregeln (UrhG, MarkenG)
5. Rechtswidrigkeit: Güter- und Interessenabwägung bei APR besonders relevant
6. Verschulden: Vorsatz oder Fahrlässigkeit
7. Schadensersatz: materielle Schäden und Geldentschädigung bei schwerwiegender APR-Verletzung
8. Unterlassungsanspruch nach § 1004 BGB analog

## Fallstricke

- Reiner Vermögensschaden (z.B. entgangener Gewinn ohne Betriebseingriff) ist kein sonstiges Recht.
- Recht am Gewerbebetrieb ist subsidiär; spezialgesetzliche Regelungen haben Vorrang.
- APR-Verletzung erfordert erheblichen Eingriff; geringfügige Beeinträchtigungen reichen nicht.
- Geldentschädigung wegen APR-Verletzung ist keine Schadenshöhe, sondern eigenständige Anspruchsvoraussetzung.

## Stoppschilder

- Keine Kommentar-, Aufsatz- oder BeckRS/Juris-Blindzitate.
- Tragende Gesetzesstände live gegen amtliche/frei zugängliche Quellen prüfen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und überprüfbarer Quelle verwenden.
- Bei Unsicherheit die Annahme ausdrücklich markieren und eine Rückfrage oder Quellenprüfung auslösen.

## Anschluss-Skills

- deliktsrecht-paragraph-823-1
- deliktsrecht-paragraph-826-sittenwidrige-schaedigung
- delikt-vertrag-konkurrenz
- workflow-output-gutachten-klage-brief

## Quellen

- https://www.gesetze-im-internet.de/bgb/__823.html
- https://www.gesetze-im-internet.de/bgb/__12.html
- https://www.gesetze-im-internet.de/bgb/__1004.html

---

## Skill: `kaufrecht-ware-leasing-schnittstelle`

_Prüft Kaufvertrag über Ware mit digitalen Elementen § 475b BGB: Mangelfreiheit, Updatepflichten und Verhältnis zu §§ 327 ff. BGB im BGB BT._

# Kaufrecht: Ware mit digitalen Elementen § 475b BGB

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: BGB §§ 535-577a, BetrKV, WEG §§ 24, 25, 27, BGB §§ 558, 558a, 558b, 573, 573c — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: Kaufrecht: Ware mit digitalen Elementen § 475b BGB
- **Normen-/Quellenanker:** BGB Besonderer Teil: Kaufrecht, Werk-/Dienstvertrag, Auftrag/Geschäftsbesorgung, Miet-/Leasingnähe, GoA, Bereicherung, Delikt, Verjährung und AGB-Schnittstellen.
- **Entscheidende Weiche:** Anspruchsgrundlage, Vertragstyp/Mischvertrag, Pflichtverletzung, Vertretenmüssen, Schaden, Einwendung und Beweisfrage sauber trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.

## Normanker

- § 475b BGB: Ware mit digitalen Elementen (Definition und Sonderregeln)
- § 434 Abs. 3 Nr. 3 BGB: Updatepflicht als Teil der objektiven Anforderungen
- §§ 327–327u BGB: Verträge über digitale Produkte
- § 476 BGB: Abweichungen von Verbrauchsgüterkauf-Anforderungen
- Richtlinie (EU) 2019/771 Art. 7 und 8: Konformitätsanforderungen für Ware mit digitalen Elementen

## Intake

- Welche digitalen Elemente sind in der Ware enthalten (Firmware, App, eingebettete Software)?
- Sind die digitalen Elemente für die Hauptfunktion notwendig oder optional?
- Welche Updatepflichten hat der Verkäufer/Hersteller übernommen?
- Gelten gleichzeitig Regeln aus § 327 BGB für den digitalen Teil?
- Wie ist das Verhältnis von Kaufrecht und digitalem Produktrecht?

## Prüfraster

1. Einordnung: Ware mit digitalen Elementen nach § 475b BGB oder reines digitales Produkt nach § 327 BGB?
2. Mangelfreiheit der physischen Ware und der digitalen Elemente gleichzeitig prüfen
3. Anforderungen an digitale Elemente: § 434 BGB plus spezifische digitale Anforderungen
4. Updatepflichten nach § 475b Abs. 3 BGB: Zeitraum, Umfang, Sicherheitsupdates
5. Integration der digitalen Elemente: dauerhaft integriert oder separat bereitgestellt?
6. Rechtsverhältnis Käufer-Anbieter der digitalen Elemente (Drittanbieter)?
7. Verbraucherschutz: § 476 BGB gilt auch für digitale Elemente der Ware
8. Verjährung und Beweislast beim gemischten Produkt

## Fallstricke

- Für digitale Elemente können gleichzeitig Kaufrecht und §§ 327 ff. BGB gelten; Abgrenzung ist komplex.
- Drittanbieter-Dienste, die mit der Ware verbunden sind, können eigene Mängelansprüche begründen.
- Updatepflicht kann über den Gewährleistungszeitraum hinausgehen.
- Fehlende Integration der digitalen Elemente kann allein Sachmangel begründen.

## Stoppschilder

- Keine Kommentar-, Aufsatz- oder BeckRS/Juris-Blindzitate.
- Tragende Gesetzesstände live gegen amtliche/frei zugängliche Quellen prüfen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und überprüfbarer Quelle verwenden.
- Bei Unsicherheit die Annahme ausdrücklich markieren und eine Rückfrage oder Quellenprüfung auslösen.

## Anschluss-Skills

- kaufrecht-updates-sicherheitsupdates-327f-475b
- kaufrecht-dauerhafte-bereitstellung-digitaler-elemente-475c
- verbrauchsgueterkauf-digitales
- workflow-livequellen-rechtsstand

## Quellen

- https://www.gesetze-im-internet.de/bgb/__475b.html
- https://www.gesetze-im-internet.de/bgb/__327.html
- https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32019L0771

---

## Skill: `arbeitsnaher-dienstvertrag-bgb`

_Prüft zivilrechtliche Dienstleistungsverhältnisse mit Arbeitsrechtsnähe, Scheinselbstständigkeit und Vergütungsfragen nach §§ 611 ff. BGB._

# Arbeitsnaher Dienstvertrag im BGB

## Fachkern: Arbeitsnaher Dienstvertrag im BGB
- **Normen-/Quellenanker:** BGB Besonderer Teil: Kaufrecht, Werk-/Dienstvertrag, Auftrag/Geschäftsbesorgung, Miet-/Leasingnähe, GoA, Bereicherung, Delikt, Verjährung und AGB-Schnittstellen.
- **Entscheidende Weiche:** Anspruchsgrundlage, Vertragstyp/Mischvertrag, Pflichtverletzung, Vertretenmüssen, Schaden, Einwendung und Beweisfrage sauber trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.

## Normanker

- §§ 611–630h BGB: Dienstvertrag, Vergütung, Kündigung, Behandlungsvertrag
- § 611a BGB: Arbeitnehmer-Definition, Weisungsgebundenheit
- § 612 BGB: Vergütung ohne ausdrückliche Abrede
- § 621 BGB: Kündigungsfristen bei Dienstverhältnissen
- §§ 157 und 242 BGB: Auslegung und Treu und Glauben
- Sozialversicherungsrecht: § 7 SGB IV (Beschäftigung und Scheinselbstständigkeit)
- BAG-Rechtsprechung zu Arbeitnehmereigenschaft: nur nach Live-Prüfung mit Aktenzeichen zitieren

## Intake

- Welche Parteien und welche Leistungspflichten sind vereinbart?
- Liegt ein schriftlicher Vertrag vor; welche Bezeichnung wurde gewählt?
- Wie ist die tatsächliche Durchführung: Weisungen, Arbeitszeit, Arbeitsort, Eingliederung?
- Welche Vergütung wurde vereinbart und wie wird abgerechnet?
- Ist eine Kündigung ausgesprochen oder beabsichtigt; welche Fristen gelten?
- Gibt es Hinweise auf Scheinselbstständigkeit oder laufende Statusfeststellungsverfahren?

## Prüfraster

1. Vertragstyp bestimmen: Dienst-, Arbeits-, Werk- oder Auftragsverhältnis?
2. Abgrenzungskriterien nach § 611a BGB prüfen: persönliche Abhängigkeit, Weisungsgebundenheit, Eingliederung
3. Tatsächliche Durchführung der Leistung mit Vertragslage vergleichen (substance over form)
4. Vergütungsanspruch nach § 612 BGB prüfen, wenn keine ausdrückliche Vereinbarung besteht
5. Kündigungsfristen nach § 621 BGB berechnen; bei Arbeitsverhältnis § 622 BGB anwenden
6. Scheinselbstständigkeit: sozialversicherungsrechtliche Folgen nach § 7 SGB IV berücksichtigen
7. Haftungsfragen bei fehlerhafter Leistung prüfen: §§ 280 und 241 Abs. 2 BGB
8. Verjährung der Vergütungsansprüche nach §§ 195 und 199 BGB

## Fallstricke

- Vertragliche Bezeichnung als „freier Mitarbeiter" schützt nicht vor Umqualifizierung durch Gerichte.
- Faktische Weisungsgebundenheit begründet Arbeitnehmereigenschaft unabhängig vom Vertragstext.
- Vergütungsansprüche können nach § 612 BGB entstehen, auch wenn kein Betrag vereinbart wurde.
- Sozialversicherungsrechtliche Nachforderungen können rückwirkend vier Jahre betragen.

## Stoppschilder

- Keine Kommentar-, Aufsatz- oder BeckRS/Juris-Blindzitate.
- Tragende Gesetzesstände live gegen amtliche/frei zugängliche Quellen prüfen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und überprüfbarer Quelle verwenden.
- Bei Unsicherheit die Annahme ausdrücklich markieren und eine Rückfrage oder Quellenprüfung auslösen.

## Anschluss-Skills

- dienstvertrag-und-behandlungsvertrag
- werk-dienst-abgrenzung-erfolg
- geschaeftsbesorgung-auftrag-mandat
- workflow-anfangercoach-schuldrecht-bt

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 3 ProdHaftG
- Art. 32 DSGVO
- § 4 ProdHaftG
- § 8 ProdHaftG
- § 2 ProdHaftG
- § 1 ProdHaftG
- § 10 ProdHaftG
- § 9 ProdHaftG
- § 2 WoVermG
- Art. 82 DSGVO

### Leitentscheidungen

- BVerfGE Band 6 Rn 32 (Lüth, Drittwirkung der Grundrechte)
- BVerwG 6 C 12.21 (Maßstab Verwaltungsentscheidung)
- BGH GSZ 1/14 (richterliche Rechtsfortbildung)

---

## Anwendungshinweise

1. Diesen Megaprompt als Kontext in den Chat einfuegen oder als Datei hochladen.
2. Den eigentlichen juristischen Fall beschreiben.
3. Den Chat-Agent bitten, sich anhand der oben aufgefuehrten Skills zu orientieren.
4. Bei Zitaten Quellenhygiene beachten: keine Modellwissens-Halluzinationen; alle Rspr. live verifizieren.

