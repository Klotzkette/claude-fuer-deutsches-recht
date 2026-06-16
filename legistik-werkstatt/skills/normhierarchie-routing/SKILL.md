---
name: normhierarchie-routing
description: "Richtige Startbahn und Normebene für ein legistisches Vorhaben bestimmen: Bundesgesetz, Landesgesetz, Rechtsverordnung, Satzung, Verwaltungsvorschrift, parlamentarischer Antrag oder Entschliessungsantrag. Anwendungsfall politische Vorgabe liegt vor und unklar ist, ob Bundesministerium, Bundestag,..."
---

# Normhierarchie-Routing

> Entscheidet: Wer kann handeln, auf welcher Ebene und in welchem Verfahren?

## Eingabe

Auftragsblatt aus `legistik-auftragsaufnahme`.

## Prüfraster

### Vorfrage - Welcher institutionelle Pfad?

| Pfad | Wann naheliegend? | Nächster Skill |
|---|---|---|
| Bundesministerium / Bundesregierung | Bundeskompetenz, Regierungsprogramm, Kabinettspfad, Rechtsverordnung des Bundes | `referentenentwurf-bauen`, `gesetzesentwurf-kabinett`, `verordnungsermaechtigung-art80` |
| Bundestag / Fraktion / Abgeordnete | Parlamentarischer Gesetzentwurf, Änderungsantrag, Entschließungsantrag oder Antrag | `formulierungshilfe-bauen` |
| Landesministerium / Landesregierung | Landeskompetenz, Landesvollzug, Landesverordnung, Landesgesetz | `referentenentwurf-bauen`, danach landesspezifische Kabinetts-/Landtagsprüfung |
| Landtag / Landtagsfraktion | Landesparlamentarischer Antrag oder Gesetzentwurf aus der Mitte des Landtags | `formulierungshilfe-bauen` |
| Kommune / Kammer / Hochschule / sonstige Körperschaft | Selbstverwaltungs- oder Fachsatzung, Beschlussvorlage, Bekanntmachung | `satzungskompetenz-pruefen` |

Wenn ein Vorhaben nur eine politische Position, Prüfbitte oder Aufforderung an Regierung/Verwaltung enthält, kann ein Antrag oder Entschließungsantrag richtiger sein als ein Gesetz.

### A - Ist es überhaupt eine zu kodifizierende Materie?

Wenn die politische Vorgabe nur Verwaltungspraxis ändern soll, reicht ein Erlass / eine Verwaltungsvorschrift. Kein Norm-Schritt noetig.

### B - Wenn Gesetz: Bund oder Land?

1. Prüfung **ausschließliche Gesetzgebung Bund** (Art. 71 und 73 GG): auswärtige Angelegenheiten, Verteidigung, Staatsangehoerigkeit, Wahrungseinheit, Bundeseisenbahnen, Luftverkehr, Postwesen, Telekommunikation, Bundeskriminalpolizei, Zoelle, Schutz deutsches Kulturgut.
2. Prüfung **konkurrierende Gesetzgebung** (Art. 72 und 74 GG): Bürgerliches Recht, Strafrecht, Gerichtsverfassung, Aufenthaltsrecht, Sozialrecht, Wirtschaftsrecht, Arbeitsrecht, Straßenverkehr, öffentliche Fürsorge, Recht der Wirtschaft, etc. Prüfung **Erforderlichkeitsklausel** Art. 72 Abs. 2 GG bei den dort genannten Materien.
3. Wenn weder Art. 71 noch Art. 73 noch Art. 74: **Landeszuständigkeit** Art. 70 Abs. 1 GG (Auffangkompetenz).

Bei Landeszuständigkeit:

- Bundesland ausdrücklich benennen.
- Landesverfassung, Geschäftsordnung der Landesregierung und Geschäftsordnung des Landtags als Prüfquellen markieren.
- Prüfen, ob eine landesrechtliche Verordnung oder Satzung genügt oder ein Landesgesetz erforderlich ist.

### C - Wenn Gesetz oder Rechtsverordnung?

- **Wesentlichkeitstheorie BVerfG**: Grundrechtsrelevante Regelungen müssen vom parlamentarischen Gesetzgeber selbst getroffen werden. Faustregel: Wer betrifft den Bürger in seinen Grundrechten erheblich, muss als Gesetz geregelt werden.
- **Strafgesetz und Bußgeldgesetz**: nur Gesetz (Art. 103 Abs. 2 GG iVm Wesentlichkeitstheorie).
- **Detailregelungen technischer Art**: Rechtsverordnung kommt in Betracht.

### D - Wenn Rechtsverordnung Bund: Gibt es Ermaechtigungsgrundlage Art. 80 GG?

Prüfen mit Skill `verordnungsermaechtigung-art80`. Wenn keine ausreichende Ermaechtigung vorhanden: zunächst Gesetz ändern, um Ermaechtigung zu schaffen, dann VO erlassen.

### E - Wenn Satzung: Gibt es Satzungskompetenz?

- Kommunale Satzungen: Selbstverwaltungsgarantie Art. 28 Abs. 2 GG plus Gemeindeordnung des Landes plus ggf. spezielle Fachgesetze (z.B. BauGB für Bebauungspläne, KAG für Beitragssatzungen, BImSchG für Laermsatzungen).
- Berufsstaendische Satzungen: Kammerngesetz (z.B. BRAO, BAeO, IHK-Gesetz) plus Vorbehalt des Gesetzes BVerfG E 33 / 125 (Facharzt).
- Hochschulsatzungen: Hochschulgesetz Land plus Selbstverwaltung Art. 5 Abs. 3 GG.
- Sozialversicherungsträger: Satzungsbefugnis nach SGB IV.
- Rundfunkanstalten: Rundfunkstaatsvertrag plus Landesrundfunkgesetze.

### F - Wenn Mehrebenen-Vorhaben

Manchmal braucht es: Bundesgesetz (Rahmen), Bundesverordnung (Details), Landesgesetz (Umsetzung), Verwaltungsvorschrift (Vollzug). Dann ist eine Tabelle der Ebenen zu erstellen.

### G - Wenn parlamentarischer Antrag ohne Normtext

Ein Antrag, Entschließungsantrag oder Prüfauftrag ist naheliegend, wenn:

- das Parlament die Regierung zu einem Bericht, Entwurf oder Verhalten auffordern soll,
- ein politischer Alternativvorschlag ohne sofortigen Normtext gebraucht wird,
- die Gesetzgebungskompetenz unsicher ist und zuerst ein Prüfauftrag sinnvoller ist,
- eine Oppositionsfraktion ein Thema parlamentarisch sichtbar machen will.

Dann zu `formulierungshilfe-bauen` routen, aber als Antrag/Entschließungsantrag, nicht als Normtext.

## Arbeitsgrundlagen

- Art. 70-74 GG: Kompetenzverteilung Bund/Länder.
- Art. 76-78 GG: Bundesgesetzgebungsverfahren und Einbringungswege.
- Art. 80 GG: Anforderungen an Rechtsverordnungsermächtigungen.
- Art. 28 Abs. 2 GG: Kommunale Selbstverwaltung als Ausgangspunkt für Satzungen.
- Art. 31 GG: Bundesrecht bricht Landesrecht.
- GO-BT und Landtags-Geschäftsordnungen: parlamentarische Vorlagen, Anträge und Änderungsanträge.
- Landesverfassungen und Verkündungsrecht: landesspezifischer Pfad.
- EU-Recht: Anwendungsvorrang und Umsetzungsbedarf im jeweiligen Fachskill prüfen.

## Zentrale Normen (Paragrafenkette)

Art. 70-74 GG — Art. 76-78 GG — Art. 80 GG — Art. 28 Abs. 2 GG — Art. 31 GG — Art. 1 Abs. 3 GG — Art. 93 Abs. 1 Nr. 2 GG — Art. 100 GG — Art. 288 AEUV — GO-BT — jeweilige Landesverfassung und Landtags-GO

## Ausgabe

- Entscheidung institutionelle Startbahn
- Entscheidung Norm-Ebene oder parlamentarischer Antragstyp
- drei Sätze Begründung
- offene landesspezifische oder geschäftsordnungsrechtliche Punkte
- Verweis auf nächsten Skill `gesetzgebungskompetenz-pruefen`, `verordnungsermaechtigung-art80`, `satzungskompetenz-pruefen`, `referentenentwurf-bauen` oder `formulierungshilfe-bauen`

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig. Diese Regel folgt der zentralen Vorgabe in der `CLAUDE.md` des Repos und gilt ausnahmslos.
<!-- END ausformulierungspflicht (autogen) -->

## Stolperfallen

- Goldplating durch Wahl der falschen Ebene (Bund regelt, was Land regeln duerfte): prüfen unter `goldplating-vermeiden`
- Wesentlichkeitstheorie wird oft übersehen, wenn das Ministerium "schnell per VO" regeln will
- Subsidiaritaetsprinzip EU bei Kompetenzfragen mitdenken
