---
name: orientierung-drafting-triage
description: "Einstiegs- und Triage-Skill fuer juristisches Drafting. Klaert in maximal zwei Rueckfragen Dokumenttyp (Vertrag, Klage, NDA, AGB, Memo, Anwaltsschreiben), Stadium (Term Sheet, Erstentwurf, Review, Markup, Unterzeichnungsreife) und Adressat (Mandant, Gegenseite, Gericht, Behoerde), erstellt eine Mandatsmatrix und verweist auf die einschlaegigen Spezial-Skills im Plugin juristisches-drafting."
---

# Orientierung und Drafting-Triage

## Zweck

Jeder Drafting-Auftrag beginnt mit einer Triage. Bevor Sie eine Klausel schreiben, eine Klage entwerfen oder einen Schriftsatz strukturieren, muessen drei Dinge feststehen: welches Dokument, welches Stadium, welcher Adressat. Dieser Skill bringt Sie in zwei Rueckfragen dorthin und legt sofort die Mandatsmatrix offen. Er ist der Einstiegspunkt fuer das Plugin `juristisches-drafting`.

Er ersetzt nicht die spezialisierten Skills, sondern verweist auf sie. Wenn Sie schon wissen, was Sie brauchen, gehen Sie direkt zum Spezial-Skill. Wenn nicht, beginnen Sie hier.

Der Skill arbeitet schnell und liefert sofort ein Arbeitsergebnis. Er haelt keinen Vortrag zur Drafting-Theorie. Sobald die drei Triagefragen beantwortet sind, erzeugt er eine Mandatsmatrix und schlaegt die naechsten Skills vor.

## Eingaben

- Kurze Beschreibung des Mandats oder des Dokuments (ein bis drei Saetze reichen)
- Falls vorhanden: Entwurf, Vorlage, Eingangspost der Gegenseite
- Vorgabe zu Frist, Adressat, Rolle (Verteidigung, Klaegerseite, beratend)
- Praeferenz fuer Stil (Mandantenbrief eher knapp, Schriftsatz urteilsstil, Memo gutachtenstil)

## Rechtlicher und methodischer Rahmen

- Anwaltsrecht: Mandatsgegenstand und Adressat klaeren ist Teil des anwaltlichen Sorgfaltsmassstabs gemaess § 43a BRAO.
- Vertraulichkeit: § 43a Abs. 2 BRAO, § 203 StGB. Vor Eingabe von Mandantendaten in Cloud-Tools Auftragsverarbeitung pruefen.
- Standardmethode: Gutachtenstil fuer interne Memos, Urteilsstil fuer Schriftsaetze und operative Klauseln. Siehe `references/methodik-buergerliches-recht.md`.
- Quellen: keine Pflicht fuer diese Triagephase. Belege folgen in den Spezial-Skills nach `references/zitierweise.md`.

## Ablauf / Checkliste

1. **Erkennen Sie das Dokument.** Erste Rueckfrage falls unklar: handelt es sich um Vertrag, Schriftsatz, Anwaltsschreiben, Memo oder AGB.
2. **Bestimmen Sie das Stadium.** Term Sheet, Erstentwurf, Review fremden Entwurfs, Markup, Unterzeichnungsreife. Diese Information bestimmt, wie tief gedraftet wird.
3. **Identifizieren Sie den Adressaten.** Mandant, Gegenseite, Gericht, Behoerde, interne Rechtsabteilung. Bestimmt Register und Stil.
4. **Pruefen Sie die Frist.** Frist ist Drafting-Treiber Nummer eins. Notieren Sie sie in der Matrix.
5. **Pruefen Sie das Risiko.** Pauschal: niedrig, mittel, hoch. Auch ohne tiefe Pruefung ist eine erste Einordnung moeglich.
6. **Erstellen Sie die Mandatsmatrix.** Tabelle, hoechstens zehn Zeilen. Siehe Beispiel unten.
7. **Verweisen Sie weiter.** Nennen Sie zwei bis vier Skills aus dem Plugin, die als naechste anzuwenden sind.
8. **Liefern Sie bei klarer Faktenlage einen Skelettentwurf.** Wenn alle drei Triagefragen klar sind, kann ein erster Strukturentwurf direkt mitgeliefert werden.

### Triage-Tabelle Dokumenttyp zu Skill

| Dokument | Stadium | Empfohlene Skills |
|---|---|---|
| Vertrag | Erstentwurf | `dokumentstruktur-makroebene-vertrag-und-schriftsatz`, `definitionen-klauseln-stringent`, `boilerplate-klauseln-katalog` |
| Vertrag | Review | `verweis-und-querverweis-technik`, `haftungsausschluss-und-haftungsbegrenzung` |
| Klage | Erstentwurf | `klage-drafting-253-zpo`, `dokumentstruktur-makroebene-vertrag-und-schriftsatz` |
| Klageerwiderung | Erstentwurf | `klageerwiderung-substantiiertes-bestreiten` |
| NDA | Eingehend | `geheimhaltung-nda-vertraulichkeit`, `boilerplate-klauseln-katalog` |
| AGB | Erstentwurf | `agb-konforme-klauseln-305-310-bgb`, `transparenzgebot-307-bgb` |
| Anwaltsschreiben | Erstmahnung | `anwaltsschreiben-aussergerichtlich`, `stil-und-ton-juristische-texte` |
| Memo | Intern | `gutachten-memo-internes-drafting` |

## Typische Drafting-Fehler

- **Direkter Start ohne Triage.** Fuehrt zu falschem Register, falschem Adressaten, falscher Tiefe.
- **Stadium ignoriert.** Ein Term Sheet bekommt keine Boilerplate-Salven; ein Endentwurf hat keine offenen Platzhalter.
- **Adressat falsch.** Mandantenbriefe in Schriftsatzsprache; Schriftsaetze im Coaching-Ton.
- **Frist nicht erfasst.** Drafting ohne Frist ist akademisch.
- **Kein Verweis auf Spezial-Skills.** Triage-Skill versucht selbst, alle Aspekte zu loesen, statt zu uebergeben.

## Ausgabeformat

- Mandatsmatrix als Tabelle.
- Liste der naechsten zwei bis vier Skills.
- Optional: Skelettentwurf mit Platzhaltern in eckigen Klammern.

## Beispiel

**Anfrage:** "Wir verhandeln eine Lieferantenvereinbarung mit einem mittelgrossen Werkzeugbauer. Der Lieferant hat einen Entwurf geschickt. Wir wollen Markup zurueckspielen, Frist eine Woche."

**Mandatsmatrix:**

| Punkt | Auspraegung |
|---|---|
| Dokumenttyp | Lieferantenvereinbarung (Vertrag) |
| Stadium | Review fremden Entwurfs mit Markup |
| Rolle | Bestellerseite |
| Adressat des Markups | Gegenseite ueber unsere Rechtsabteilung |
| Frist | eine Woche |
| Schwerpunkt | Haftungsregime, Maengelhaftung, Schriftform |
| Risiko | mittel |

**Naechste Skills:**

1. `haftungsausschluss-und-haftungsbegrenzung` fuer das Haftungsregime.
2. `definitionen-klauseln-stringent` fuer den Defined-Terms-Apparat im Lieferantenvertrag.
3. `verweis-und-querverweis-technik` fuer Anlagen und interne Verweise.
4. `boilerplate-klauseln-katalog` fuer Schriftform, Gerichtsstand, Rechtswahl.

## Querverweise

- `dokumentstruktur-makroebene-vertrag-und-schriftsatz`
- `drafting-prinzipien-klarheit-bestimmtheit-praezision`
- `stil-und-ton-juristische-texte`

## Quellen (Stand 05/2026)

- § 43a BRAO und § 203 StGB fuer Vertraulichkeit; gesetze-im-internet.de.
- `references/methodik-buergerliches-recht.md` fuer Stilwahl Gutachtenstil und Urteilsstil.
- Spezial-Skills im Plugin `juristisches-drafting` als Folgeartefakt; vom Nutzer zu validieren, falls die genannten Skills im konkreten Setup nicht aktiviert sind.
