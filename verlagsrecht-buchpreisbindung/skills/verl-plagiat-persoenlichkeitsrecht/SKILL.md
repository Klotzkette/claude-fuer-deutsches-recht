---
name: verl-plagiat-persoenlichkeitsrecht
description: "Verl 020 Plagiat Manuskript Und Quellenpruefung, Verl 021 Persoenlichkeitsrecht Im Sachbuch: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Verl 020 Plagiat Manuskript Und Quellenpruefung, Verl 021 Persoenlichkeitsrecht Im Sachbuch

## Arbeitsbereich

Dieser Skill bündelt **Verl 020 Plagiat Manuskript Und Quellenpruefung, Verl 021 Persoenlichkeitsrecht Im Sachbuch** zu einem konkreten Arbeitsgang. Starte mit dem Modul, das die Tatsachen der Akte trägt; weitere Module nur hinzunehmen, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output betreffen.

## Arbeitsmodule

| Arbeitsmodul | Fokus |
| --- | --- |
| `verl-020-plagiat-manuskript-und-quellenpruefung` | Verlagsrecht: Plagiat im Manuskript — Rechtliche Grundlagen, Prüfverfahren, Vertragsklauseln, Haftung des Autors, Reaktion bei Plagiatsfund und Rückruf nach Erscheinen. |
| `verl-021-persoenlichkeitsrecht-im-sachbuch` | Verlagsrecht: Persönlichkeitsrechte im Sachbuch — allgemeines Persönlichkeitsrecht, Recht am eigenen Bild, Gegendarstellung, Unterlassung und Haftung von Autor und Verlag. |

## Arbeitsweg

Für **Verl 020 Plagiat Manuskript Und Quellenpruefung, Verl 021 Persoenlichkeitsrecht Im Sachbuch** zuerst das Arbeitsmodul wählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `verlagsrecht-buchpreisbindung` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; Module nur kombinieren, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Arbeitsmodule im Detail

## 1. `verl-020-plagiat-manuskript-und-quellenpruefung`

**Fokus:** Verlagsrecht: Plagiat im Manuskript — Rechtliche Grundlagen, Prüfverfahren, Vertragsklauseln, Haftung des Autors, Reaktion bei Plagiatsfund und Rückruf nach Erscheinen.

# Verl-020 · Plagiat, Manuskript und Quellenprüfung

## Zweck dieses Skills

Plagiate in Verlagswerken können zum **Vertragsrücktritt, Haftungsansprüchen, Titelrückruf und Reputationsschäden** führen. Dieser Skill klärt die rechtliche Einordnung von Plagiaten, die Prüfpflichten von Autor und Verlag, die vertraglichen Absicherungen und die Reaktionskette bei einem Plagiatsfund.

## Rechtsgrundlagen

| Norm | Inhalt | Quelle |
|------|--------|-------|
| UrhG § 2 | Urheberrechtsverletzung durch unerlaubte Übernahme | https://dejure.org/gesetze/UrhG/2.html |
| UrhG § 97 | Unterlassung und Schadensersatz bei UrhG-Verletzung | https://dejure.org/gesetze/UrhG/97.html |
| UrhG § 98 | Vernichtungsanspruch: Rückruf und Einziehung | https://dejure.org/gesetze/UrhG/98.html |
| BGB §§ 280, 311 | Schadensersatz bei Pflichtverletzung des Autors | https://dejure.org/gesetze/BGB/280.html |
| VerlG § 2 | Mängelfreiheitspflicht: Manuskript ohne Rechtsverletzungen | https://www.gesetze-im-internet.de/verlg/__2.html |
| StGB § 263 | Betrug: Wenn Plagiat bei Vertragsschluss verschwiegen | https://dejure.org/gesetze/StGB/263.html |

## Was ist ein Plagiat?

### Rechtliche Definition
- **Plagiat** im urheberrechtlichen Sinne: Übernahme urheberrechtlich geschützter Werkteile ohne Genehmigung und ohne Quellenangabe.
- Nicht jede Übernahme ist eine Urheberrechtsverletzung: Das Zitatrecht (§ 51 UrhG) erlaubt begrenzte Übernahmen.
- Auch paraphrasierte Übernahmen ohne Quellenangabe können Plagiat sein (geistiger Diebstahl ohne exaktes Kopieren).

### Abgrenzung
- **Selbstplagiat**: Autor übernimmt eigene frühere Texte ohne Kennzeichnung → urheberrechtlich unproblematisch (Rechteinhaber ist derselbe), aber wissenschaftlich / verlegerisch problematisch.
- **Ideendiebstahl**: Übernahme von Ideen und Konzepten ohne Zitat → Ideen sind nicht schutzfähig; kein Urheberrechtsproblem, aber ggf. akademische Redlichkeitsanforderung verletzt.
- **Ghostwriting**: Ghostwriter schreibt unter fremdem Namen; Einverständnis des nominellen Autors → keine Verletzung des Ghostwriters; aber Transparenzfragen für Leser.

## Prüfpflichten

### Autor (VerlG § 2)
- Autor schuldet dem Verlag ein **rechtsmängelfreies Manuskript**: keine Urheberrechtsverletzungen, keine unbefugten Entlehnungen.
- Eigenverantwortliche Quellenprüfung vor Abgabe.
- Freistellungsklausel im Verlagsvertrag: Autor stellt Verlag von Ansprüchen Dritter frei.

### Verlag
- Kein gesetzliches Plagiats-Prüfungsgebot für Verlage, aber:
- **Sorgfaltspflicht**: Verlag muss bei begründeten Zweifeln prüfen; bekannte Plagiatsprobleme ignorieren → Mitverantwortung.
- Praxis-Standard: Plagiatsprüfung bei wissenschaftlichen Verlagen üblich (iThenticate, Turnitin); bei Belletristik seltener.

## Technische Plagiatsprüfung

### Tools
- **iThenticate** / Turnitin: Professionelle Plagiatssoftware für Wissenschaftsverlag; vergleicht mit globalem Textkorpus.
- **PlagScan, Copyscape**: Für Online-Texte und allgemeine Prüfung.
- **Gratis-Tools** (Plagiarism Checker, PlagAware): Weniger umfassend; für einfache Überprüfung.

### Interpretation der Ergebnisse
- Ähnlichkeit-Prozentsatz allein ist kein Rechtsbefund; Kontext entscheidend.
- Erlaubte Zitate (§ 51 UrhG), Common-Knowledge-Sätze, Definitionen → können trotz Ähnlichkeit unproblematisch sein.
- Rechtliche Bewertung muss durch Mensch erfolgen.

## Plagiatsfund vor Erscheinen

### Reaktionskette Verlag → Autor
1. Schriftlicher Hinweis an Autor mit Fundstellennachweis.
2. Fristsetzung zur Stellungnahme und Klärung.
3. Wenn Plagiat bestätigt: Fristsetzung zur Beseitigung (Überarbeitung, Quellenangaben, Kürzen).
4. Bei erheblichem Plagiat oder Verweigerung: Rücktritt vom Verlagsvertrag (§ 8 VerlG), Schadensersatzanspruch.

### Rückzahlung des Vorschusses
- Bei Rücktritt wegen Plagiat (Autorenverschulden): Vorschussrückzahlung üblich; vertragliche Regelung maßgeblich.

## Plagiatsfund nach Erscheinen

### Urheberrechtliche Ansprüche des geschädigten Urhebers gegen Verlag und Autor
- Unterlassung (§ 97 Abs. 1 UrhG): Verbot des weiteren Vertriebs.
- Schadensersatz (§ 97 Abs. 2 UrhG): Lizenzanalogie, entgangener Gewinn, Verletzergewinn.
- Vernichtung (§ 98 UrhG): Rückruf aller Exemplare, Einziehung des Lagerbestands.

### Titelrückruf
- Öffentlicher Rückruf aller Exemplare aus dem Handel.
- Kostspielig; schadet Ruf des Verlags und des Autors erheblich.
- Alternative: Berichtigung in Neuauflage, wenn Plagiat auf einzelne Passagen beschränkt.

### Freistellungsanspruch des Verlags gegen Autor
- Hat der Autor die Freistellungsklausel im Vertrag akzeptiert → Verlag kann alle Kosten (Schadensersatz, Rückrufkosten, Anwaltskosten) vom Autor einfordern.
- Praktischer Wert beschränkt, wenn Autor mittellos ist.

## Wissenschaftliche Verlage — Besonderheiten

- Peer Review als erste Prüflinie: Gutachter können Plagiate erkennen.
- Retraction: Standardprozess in der Wissenschaftspublizistik; Artikel oder Buch wird zurückgezogen; Retraction-Datenbank (Retraction Watch) dokumentiert.
- Akademische Folgen für Autor: Disziplinarmaßnahmen durch Hochschule.

## Typische Fallen

- **Passagen aus Wikipedia**: Häufig unerkannte Selbstplagiat-Quelle; Wikipedia-Text ist meist CC BY-SA → Nutzung im kommerziellen Buch ohne ShareAlike-Klausel problematisch.
- **Übersetzungsplagiart**: Autor übersetzt fremdsprachigen Text ohne Genehmigung des Originalverlags und eigene Übersetzernennung → Urheberrechtsverletzung.
- **Kumulierte Kurzübernahmen**: Jede einzelne Passage wäre als Zitat zulässig, aber die Masse der Übernahmen ergibt de facto ein Plagiat.
- **Selbstplagiat bei Dissertation → Buchfassung**: Dissertation war mit CC-Lizenz open access; Buchausgabe muss dieselbe Lizenz tragen (ShareAlike) oder darf keine CC BY-SA-Inhalte enthalten.

## Checkliste Plagiatsprüfung

- [ ] Plagiatsprüfungs-Tool für das Manuskript genutzt (iThenticate / PlagScan)
- [ ] Ergebnis durch Mensch bewertet (nicht nur Prozentsatz)
- [ ] Alle Zitate nach § 51 UrhG korrekt belegt (Quelle, Seite)
- [ ] Bildrechte-Freigabe für übernommene Abbildungen vorhanden
- [ ] Autorenvertrag enthält Freistellungsklausel für Plagiatsfälle
- [ ] Bei Verdacht: Schriftliche Anfrage an Autor vor Erscheinen

## Quellenreferenzen

- UrhG §§ 97, 98: https://dejure.org/gesetze/UrhG/97.html
- UrhG § 51 (Zitatrecht): https://dejure.org/gesetze/UrhG/51.html
- VerlG § 2: https://www.gesetze-im-internet.de/verlg/__2.html
- Retraction Watch: https://retractionwatch.com
- BGH „Plagiat" I ZR 224/17: https://www.bgh.de

## Output-Formate

- **Plagiatsprüfungsbericht**: Fundstellen mit Quellenvergleich und Bewertung
- **Reaktionsschreiben an Autor**: Fundstellennotiz und Fristsetzung
- **Rücktrittsschreiben** (bei erheblichem Plagiat)
- **Titelrückruf-Protokoll**: Rückrufverfahren, Händleranschreiben
- **Freistellungs-Rechnung** an Autor nach Plagiatshaftung

## 2. `verl-021-persoenlichkeitsrecht-im-sachbuch`

**Fokus:** Verlagsrecht: Persönlichkeitsrechte im Sachbuch — allgemeines Persönlichkeitsrecht, Recht am eigenen Bild, Gegendarstellung, Unterlassung und Haftung von Autor und Verlag.

# Verl-021 · Persönlichkeitsrecht im Sachbuch

## Zweck dieses Skills

Sachbücher, Biographien, Reportagen und journalistische Werke berühren häufig das **Persönlichkeitsrecht** lebender Personen: durch Namensnennung, Abbildungen, private Informationen und wertende Äußerungen. Dieser Skill klärt die Schutzgrenzen des allgemeinen Persönlichkeitsrechts, des Rechts am eigenen Bild und die Haftungsrisiken für Autor und Verlag.

## Rechtsgrundlagen

| Norm | Inhalt | Quelle |
|------|--------|-------|
| GG Art. 2 Abs. 1 i.V.m. Art. 1 Abs. 1 | Allgemeines Persönlichkeitsrecht als Grundrecht | https://www.gesetze-im-internet.de/gg/art_2.html |
| GG Art. 5 | Meinungs- und Pressefreiheit; Kunstfreiheit | https://www.gesetze-im-internet.de/gg/art_5.html |
| BGB § 823 Abs. 1 | Haftung für Verletzung des APR | https://dejure.org/gesetze/BGB/823.html |
| KUG §§ 22–24 | Recht am eigenen Bild | https://dejure.org/gesetze/KunstUrhG/22.html |
| StGB § 186 | Üble Nachrede | https://dejure.org/gesetze/StGB/186.html |
| StGB § 187 | Verleumdung | https://dejure.org/gesetze/StGB/187.html |
| BDSG / DSGVO Art. 85 | Datenschutz und journalistisch-literarische Verarbeitung | https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32016R0679 |
| § 14 UrhG | Entstellungsverbot des Autors selbst | https://dejure.org/gesetze/UrhG/14.html |

## Schutzgegenstände des allgemeinen Persönlichkeitsrechts

### Kernbereiche (absolut geschützt)
- Privatsphäre: Familienleben, Sexualleben, Gesundheit, finanzielle Situation.
- Intimsphäre: Tagebücher, Privatgespräche, medizinische Daten.
- Selbstdarstellung: Kein unrichtiges Licht werfen; keine falschen Zitate.

### Sozialsphäre (eingeschränkt geschützt)
- Berufliches Verhalten, öffentliche Äußerungen, Vereinstätigkeit.
- Berichterstattung über berufliche Angelegenheiten grundsätzlich zulässig.
- Kritik an unternehmerischen Entscheidungen: Weitgehend erlaubt.

### Öffentlichkeitssphäre
- Politiker, Prominente, Personen des öffentlichen Lebens: Weitgehend reduzierter Schutz im Bereich der öffentlichen Rolle.
- Privatbereich auch von Prominenten: Voll geschützt.

## Tatsachenbehauptung vs. Meinungsäußerung

- **Tatsachenbehauptung**: Überprüfbare Aussage über Fakten; unwahre Tatsachenbehauptung → Persönlichkeitsrechtsverletzung, ggf. Verleumdung.
- **Meinungsäußerung**: Werturteil; selbst scharfe Kritik zulässig, solange keine „Schmähkritik" (d.h. kein Angriff ohne Sachkern).
- Gemischte Äußerungen: Meinungsäußerung mit Tatsachengrundlage → Wahrheitskern des Tatsachenanteils prüfen.

## Recht am eigenen Bild (KUG §§ 22–24)

- Foto, Abbildung oder sonstige Darstellung einer Person bedarf deren Einwilligung (KUG § 22).
- **Ausnahmen** (KUG § 23):
 - Personen der Zeitgeschichte (Politiker, Prominente) im Rahmen ihrer öffentlichen Tätigkeit
 - Personen als Beiwerk einer Landschaft/Szenerie
 - Versammlungen, Aufzüge, öffentliche Ereignisse
- Grenze: Auch bei Ausnahmen kein Eingriff in berechtigte Interessen (KUG § 23 Abs. 2).

## Haftung von Autor und Verlag

### Autor
- Primärhaftung: Autor als Verfasser der persönlichkeitsrechtsverletzenden Aussagen.
- Vertragliche Absicherung: Verlag hat i.d.R. Freistellungsklausel im Autorenvertrag.
- Strafrechtlich: § 186 StGB (üble Nachrede), § 187 StGB (Verleumdung) → Strafanzeige durch Betroffene möglich.

### Verlag
- Störerhaftung: Verlag haftet als Verbreiter, auch wenn er den Inhalt nicht verfasst hat.
- Prüfungspflicht: Verlage müssen bei offensichtlichen Persönlichkeitsrechtsverletzungen einschreiten.
- Mitverantwortung: Wenn Verlag trotz Kenntnis druckt.

## Reaktionen auf Persönlichkeitsrechtsverletzungen

### Gegendarstellung (Pressegesetz)
- Landesmediengesetze geben Betroffenen Recht auf Gegendarstellung in Periodika (nicht in Büchern).
- Bei Büchern: Kein gesetzlicher Gegendarstellungsanspruch, aber ggf. zivilrechtliche Richtigstellung.

### Unterlassung (§ 1004 BGB analog i.V.m. § 823 BGB)
- Einstweilige Verfügung auf Unterlassung: Schnellstes Mittel; innerhalb von Tagen.
- Vollstreckung: Ordnungsgeld bis 250.000 €, Ordnungshaft (§ 890 ZPO).
- Nach Hauptsacheklage: Dauerhafte Unterlassungsverpflichtung.

### Vernichtung und Rückruf
- Bei schwerwiegender Verletzung: Vernichtung der Auflagen (§ 98 UrhG analog, oder allgemeines Beseitigungsanspruch).
- Selten angeordnet, aber möglich.

### Schadensersatz / Geldentschädigung
- Immaterieller Schadensersatz (Geldentschädigung): Nur bei schwerwiegender Verletzung des Persönlichkeitsrechts (BGH „Caroline"-Entscheidungen).
- Höhe: 5.000 – 100.000+ € je nach Schwere und Verbreitung.

## Präventive Maßnahmen im Verlagsprozess

1. **Rechts-Read**: Alle potenziell verletzenden Passagen vor Druck anwaltlich prüfen.
2. **Gegenlesen lassen**: Betroffene Personen über Darstellung informieren (nicht immer nötig oder möglich).
3. **Anonymisierung**: Bei sensitiven Sachverhalten Namen ändern, wenn publizistisches Interesse nicht entgegensteht.
4. **Einwilligungen einholen**: Bei identifizierenden Passagen über Privatpersonen.
5. **Autorenvertrag**: Freistellungsklausel, Zusicherung der Richtigkeit der Tatsachenbehauptungen.

## Typische Fallen

- **Wahre Tatsachen in der Intimsphäre**: Auch wahre Informationen über Privatleben können Persönlichkeitsrechte verletzen.
- **„Nach wahren Begebenheiten"**: Formulierung schützt nicht vor Persönlichkeitsrechtsklagen, wenn Personen identifizierbar.
- **Vergessenes Gegenlesen**: Autor gibt Interview-Zitate wieder, ohne die zitierte Person zu befragen → Gefahr falscher Zuschreibung.
- **Bild aus Social Media**: Öffentlich gepostetes Foto ist nicht automatisch zur Veröffentlichung im Buch freigegeben.

## Checkliste Persönlichkeitsrecht

- [ ] Alle identifizierenden Passagen über lebende Personen anwaltlich geprüft
- [ ] Tatsachenbehauptungen mit Quellen belegt
- [ ] Fotos im Buch mit Einwilligung der Abgebildeten (KUG § 22)
- [ ] Autorenvertrag: Freistellungsklausel für Persönlichkeitsrechtsverletzungen
- [ ] Bei sensitiven Darstellungen: Anonymisierungsbedarf erwogen

## Quellenreferenzen

- BGB § 823: https://dejure.org/gesetze/BGB/823.html
- KUG §§ 22–23: https://dejure.org/gesetze/KunstUrhG/22.html
- BVerfG „Caroline I", BVerfGE 101, 361: https://www.bverfg.de
- BGH „Willy-Brandt-Biografie", VI ZR 36/17: https://www.bgh.de
- StGB §§ 186, 187: https://dejure.org/gesetze/StGB/186.html

## Output-Formate

- **Persönlichkeitsrechts-Audit**: Alle sensitiven Passagen mit Risikobewertung
- **Einwilligungsformular**: Für abgebildete und zitierte Personen
- **Unterlassungserklärung** bei empfangener Abmahnung
- **Anwalts-Briefing** für Rechts-Read
- **Anonymisierungsprotokoll**: Geänderte Namen und Darstellungen dokumentiert
