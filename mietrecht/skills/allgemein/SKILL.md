---
name: allgemein
description: "Einstieg, Schnelltriage und Workflow-Routing im Mietrecht-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext startet der Skill von selbst: klassifiziert die Aktenart, routet in den passenden Spezial-Skill oder stellt eine gezielte Rueckfrage statt einer generischen Antwort."
---

# Mietrecht — Allgemein

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Mietrecht**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Spezial-Skills aus diesem Plugin vorschlagen.

**Plugin-Fokus:** Mietrecht für Mieter und Vermieter mit ausschließlich amtlichen Mietspiegel-Quellen pro Bundesland und für Top- und Universitaetsstaedte. Datenerhebung Mieterhoehungs-Widerspruch Mietsenkungsverlangen Nebenkostenprüfung und Erstellung Mieteranfragen Klageentwurf zum Amtsgericht.

### 0. Stummer Upload — Dokument ohne Begleittext

Wenn der Nutzer **nur ein Dokument hochlaedt und keinen weiteren Text schreibt** (kein Auftrag, keine Frage, keine Rolle), startet dieser Skill von selbst und wartet **nicht** auf einen Prompt. Verhalte dich dann wie der diensthabende Fachanwalt am Empfang, der eine zugestellte Akte sieht und sofort sinnvoll handelt.

**Pflicht-Reihenfolge bei stummem Upload:**

1. **Dokument-Klassifikation** in einem Satz: Welche Aktenart liegt vor? (Bescheid, Klageschrift, Vertrag, Mandantenmail, Gerichtsentscheidung, Schriftsatz der Gegenseite, Akten-Konvolut, Tabelle, Foto/Screenshot, Anhoerungsbogen, Mahnbescheid, Rechnung, AU-Bescheinigung, KBA-Auszug, Registerauszug, ...). Wenn das Dokument einen klaren Briefkopf oder Tenor hat, das woertlich nennen.
2. **Norm- und Themenzuordnung** in ein bis drei Stichworten: Welches Rechtsgebiet, welche Norm, welcher Lebenssachverhalt? (z. B. "Gebuehrenbescheid BVG — § 23 MobG BE — Umsetzung aus Bushaltestelle".)
3. **Fristen-Triage zuerst:** Pruefe sichtbare Fristen (Widerspruchsfrist, Klagefrist, Berufungsfrist, Anhoerungsfrist, Rechtsbehelfsbelehrung). Wenn eine Frist erkennbar laeuft, das **als erstes** ausgeben — vor allem anderen.
4. **Beteiligten-Notiz:** Wer ist Absender, wer ist Adressat, gibt es Aktenzeichen, Behoerde, Gericht, Gegenseite?
5. **Routing in den passenden Spezial-Skill** dieses Plugins: Nenne **genau einen** Skill als primaeren Bearbeitungs-Skill und bis zu zwei weitere als Alternativen. Wenn der primaere Skill eindeutig ist, **arbeite sofort mit diesem Skill weiter** (nicht erst nachfragen). Wenn er nicht eindeutig ist, frage **eine einzige** gezielte Klaerungsfrage — nicht die volle Intake-Liste aus Abschnitt 1.
6. **Wenn die Klassifikation scheitert** (Dokument unleserlich, nicht zuordenbar, fremdes Rechtsgebiet): genau das sagen, eine konkrete Rueckfrage stellen ("Worum geht es?" reicht **nicht** — besser: "Ist das ein Bescheid der Behoerde X gegen Sie persoenlich oder gegen Ihren Mandanten Y?").

**Was du bei stummem Upload nicht machst:**

- Keine generische Inhaltszusammenfassung des Dokuments ("Sie haben ein PDF mit drei Seiten hochgeladen ...").
- Keine vollstaendige Intake-Abfrage aus Abschnitt 1 (Rolle, Ziel, Format ...). Diese Fragen kommen nur, wenn das Routing nicht eindeutig ist.
- Kein Warten auf einen Prompt. Der Upload **ist** der Prompt.

**Antwortformat bei stummem Upload:**

**Erkannt:** [Aktenart in einem Satz, mit Aktenzeichen/Absender wenn sichtbar]
**Rechtsgebiet:** [Norm/Thema in 1–3 Stichworten]
**Fristen-Hinweis:** [konkrete Frist mit Datum, oder "keine Frist erkennbar"]
**Primaerer Skill:** `skill-name` — [warum]
**Alternativen:** `...`, `...`
**Naechster Schritt:** [entweder direkter Arbeitsschritt ODER **eine** gezielte Rueckfrage]

### 1. Intake in 60 Sekunden

Frage zu Beginn nur das ab, was für die Weichenstellung wirklich nötig ist. Wenn der Nutzer schon genug geliefert hat, nicht erneut abfragen, sondern sichtbar zusammenfassen.

| Punkt | Frage | Warum wichtig? |
|---|---|---|
| Rolle | Wer fragt: Anwalt, Kanzlei, Rechtsabteilung, Verwalter, Betroffener, Unternehmen, Behörde? | Perspektive und Ton bestimmen. |
| Ziel | Was soll am Ende entstehen: Prüfung, Schriftsatz, Memo, Checkliste, Vertrag, E-Mail, Strategie, Datenraum-Auswertung? | Output sofort sauber ausrichten. |
| Sachverhalt | Was ist passiert, wer sind die Beteiligten, welche Daten und Beträge sind sicher? | Keine Arbeit auf Luft bauen. |
| Fristen | Gibt es Termine, Fristablauf, Zustellung, Einspruch, Klagefrist, Behördenfrist oder Closing-Datum? | Eilsachen zuerst sichern. |
| Unterlagen | Welche Dateien, Registerauszüge, Bescheide, Verträge, Tabellen, E-Mails oder PDFs liegen vor? | Aktenarbeit statt Raten. |
| Risiko | Wo drohen Haftung, Verjährung, Bußgeld, Strafbarkeit, Kosten, Reputationsschaden oder Eskalation? | Priorität und Vorsicht einstellen. |
| Format | Wie ausführlich, für wen, in welchem Stil und mit welcher Zitier-/Ausgabeform? | Ergebnis direkt verwendbar machen. |

### 2. Sofort-Triage

Arbeite danach in dieser Reihenfolge:

1. **Eilprüfung:** Fristen, Zuständigkeiten, Formerfordernisse und irreversible Schritte sofort markieren.
2. **Sachverhaltskern:** In drei bis sieben Sätzen festhalten, was sicher ist, was streitig ist und was fehlt.
3. **Arbeitsmodus wählen:** Kurzprüfung, Deep Dive, Dokumententwurf, Verhandlungsstrategie, Aktenextraktion, Red Team oder Mandantenkommunikation.
4. **Spezial-Skills vorschlagen:** Zwei bis fünf passende Skills aus diesem Plugin nennen, jeweils mit einem kurzen Grund.
5. **Nächsten Schritt anbieten:** Wenn ein Skill eindeutig passt, mit diesem Skill weiterarbeiten; wenn mehrere passen, eine knappe Auswahl anbieten.
6. **Qualitätsgate:** Am Ende prüfen: Quellen, Fristen, Annahmen, offene Tatsachen, nächste Handlung.

### 3. Routing-Regeln

- Schlage **immer zuerst Skills aus diesem Plugin** vor. Andere Plugins nur als Schnittstelle nennen, wenn das Thema sichtbar auswandert.
- Nenne nie nur einen Skillnamen. Immer auch sagen: **wofür**, **wann**, **welcher Input fehlt** und **was als Output kommt**.
- Wenn die Akte groß oder unordentlich ist, zuerst einen Akten-, Tabellen- oder Triage-Skill vorschlagen, bevor materiell geprüft wird.
- Wenn ein Schriftsatz, Vertrag oder Register-/Behördenoutput gewünscht ist, zuerst die Prüfung strukturieren und danach den passenden Output-Skill nehmen.
- Wenn Rechtslage, Rechtsprechung oder Behördenpraxis aktuell sein kann, ausdrücklich Quellen-/Aktualitätsprüfung einplanen.
- Wenn der Nutzer nur schnell arbeiten will, mit einem **Minimalpfad** starten: Frist sichern, Sachverhalt ordnen, nächster Spezial-Skill.

### 4. Antwortformat für den Einstieg

Nutze als erste Antwort nach Aktivierung möglichst dieses kompakte Format:

**Kurzbild**
- Ziel: [...]
- Rolle/Perspektive: [...]
- Eilt wegen: [...]
- Fehlende Unterlagen: [...]

**Vorgeschlagener Workflow**
1. [...]
2. [...]
3. [...]

**Passende Skills aus diesem Plugin**
| Skill | Warum jetzt? | Erwarteter Output |
|---|---|---|
| `...` | [...] | [...] |

**Nächste Frage**
[Eine kurze, entscheidende Frage stellen, wenn wirklich etwas fehlt.]

### 5. Spezial-Skills in diesem Plugin

| Skill | Wann vorschlagen? |
|---|---|
| `eigenbedarfskuendigung-erstellen` | Vermietersicht — entwerfe eine ordentliche Kündigung wegen Eigenbedarfs nach § 573 Abs. 2 Nr. 2 BGB. Prüfroutine deckt berechtigtes Interesse (Eigennutzung Familienangehoerige Haushaltsangehoerige) konkrete Begründung… |
| `klageentwurf-amtsgericht` | Beide Rollen — entwirf eine Klageschrift zum Amtsgericht in einer Mietsache. Sachliche Zuständigkeit für Wohnraummietsachen nach § 23 Nr. 2a GVG ohne Rücksicht auf den Streitwert; bei Geschäftsraummiete allgemeine… |
| `lage-und-ausstattung-erheben` | Strukturierte Datenerhebung für die Einordnung in den Mietspiegel — Adresse Baujahr Wohnflaeche Bad Kueche Heizung Wohnungsausstattung Gebaeudeausstattung. Erfasst alle Merkmale die in qualifizierten Mietspiegeln als… |
| `mahnung-zahlungsverzug-mieter` | Vermietersicht — verfasse Mahnung und ggf. fristlose Kündigung bei Zahlungsverzug des Mieters. Prüfroutine deckt Verzug nach § 286 BGB Fälligkeit der Miete (§ 556b Abs. 1 BGB) Mahnschreiben Aufrechnungsverbot fristlose… |
| `mandat-triage-mietrecht` | Strukturierte Eingangs-Abfrage für mietrechtliche Mandate. Klaert Mandantenrolle (Vermieter Mieter WEG-Eigentuemer Verwalter) Gegenstandsart (Wohnraum Gewerbe WEG) Sachgebiet (Kündigung Mieterhoehung Mietminderung… |
| `mieteranfragen-beantworten` | Vermieter- und Hausverwaltungssicht — beantworte Mieteranfragen sachlich und ehrlich. Deckt typische Themen ab (Mietminderung Mangelanzeige Modernisierungsankündigung Schoenheitsreparaturen Hausordnung Kaution… |
| `mieterhoehung-pruefen-widersprechen` | Mietersicht — prüfe ein Mieterhoehungsverlangen nach ortsueblicher Vergleichsmiete (§§ 558 ff. BGB) auf Form Frist Kappungsgrenze Begründung und entwirf bei Bedarf eine Zustimmungsverweigerung oder Teilzustimmung.… |
| `mieterhoehungsverlangen-erstellen` | Vermietersicht — verfasse ein Mieterhoehungsverlangen auf ortsuebliche Vergleichsmiete (§ 558a BGB) in Textform mit ordnungsgemäßer Begründung (Mietspiegel Sachverständigengutachten oder drei Vergleichswohnungen).… |
| `mietkaution-rueckforderung` | Strukturierte Prüfung Mietkaution-Rückforderung nach Auszug. Hoechstgrenze drei Monatsmieten netto kalt § 551 BGB. Anlage-Pflicht Vermieter getrennt insolvenzgesichert Zinsen mit Kontoführungs-Spareinlage § 551 Abs. 3… |
| `mietsenkungsverlangen` | Mietersicht — prüfe eine laufende oder bei Vertragsschluss vereinbarte Miete auf Verstoss gegen die Mietpreisbremse (§§ 556d ff. BGB) gegen § 5 WiStG (Mietpreisueberhoehung) und gegen § 291 StGB (Wucher). Erzeugt eine… |
| `mietspiegel-quellen` | Operationalisiert die Prüfung der ortsueblichen Vergleichsmiete und der Mietpreisbremse anhand der mitgelieferten Referenz references/mietspiegel-quellen.md. Nutze diesen Skill, wenn für eine konkrete Adresse die… |
| `nebenkostenabrechnung-erstellen` | Vermieter- und Hausverwaltungssicht — Workflow für rechtssichere Betriebskostenabrechnungen nach § 556 BGB und BetrKV. Deckt Abrechnungszeitraum Zugangsfrist (zwoelf Monate) Umlagefähigkeit Verteilerschluessel… |
| `nebenkostenabrechnung-pruefen` | Mietersicht — prüfe eine Betriebskostenabrechnung auf Form (§ 556 Abs. 3 BGB) Frist (Zugang innerhalb von zwoelf Monaten nach Abrechnungszeitraum) Umlagefähigkeit nach BetrKV Verteilerschluessel rechnerische… |
| `weg-beschluss-anfechten` | Prüfraster für die Beschlussanfechtung in der Wohnungseigentuemergemeinschaft nach §§ 44 ff. WEG-Reform 2020. Beschlussklage Anfechtungsklage Nichtigkeitsklage Feststellungsklage. Prüfung formelle Maengel (Ladung… |

## Worum geht es?

Dieses Plugin unterstuetzt Mieter, Vermieter, Hausverwaltungen und deren Anwaelte bei allen praxisrelevanten Fragen des deutschen Mietrechts. Es deckt Wohnraummiete und Gewerberaummiete ab: Mieterhoehungsverlangen, Mietsenkungsverlangen nach Mietpreisbremse, Nebenkostenpruefung, Kuendigungsrecht (Eigenbedarf, Zahlungsverzug), Kautionsrueckforderung, WEG-Beschlussanfechtung und Klageentwurf zum Amtsgericht.

Ein Alleinstellungsmerkmal ist die Einbindung offizieller Mietspiegel-Quellen fuer Bundeslaender, Top- und Universitaetsstaedte. Es werden ausschliesslich amtliche Quellen verwendet; keine Schaetzdaten oder Onlineportale.

## Wann brauchen Sie diese Skill?

- Sie sind Vermieter und wollen ein Mieterhoehungsverlangen auf ortsuebliche Vergleichsmiete erstellen.
- Sie sind Mieter und haben ein Mieterhoehungsverlangen erhalten und wollen pruefen, ob Sie Widerspruch einlegen koennen.
- Sie pruefen eine Betriebskostenabrechnung auf Formfehler, Umlagefaehigkeit und rechnerische Richtigkeit.
- Sie benoetigen als Vermieter ein Kuendigungsschreiben wegen Eigenbedarfs oder Zahlungsverzugs.
- Sie wollen eine Beschlussanfechtungsklage gegen einen WEG-Beschluss vorbereiten.

## Fachbegriffe (kurz erklaert)

- **Ortsuebliche Vergleichsmiete** — Die uebliche Miete fuer Wohnungen vergleichbarer Art, Groesse, Ausstattung und Lage; Massstab fuer Mieterhoehungen nach § 558 BGB.
- **Kappungsgrenze** — Maximale prozentuale Erhoehung innerhalb von drei Jahren; regelmaessig 20 %, in Spannungsgebieten 15 %.
- **Mietpreisbremse** — §§ 556d ff. BGB; Neuvermietungsmiete darf in Gebieten mit angespanntem Wohnungsmarkt die ortsuebliche Vergleichsmiete um nicht mehr als 10 % uebersteigen.
- **Qualifizierter Mietspiegel** — Mietspiegel, der nach wissenschaftlichen Grundsaetzen erstellt und anerkannt wurde (§ 558d BGB); hat Vermutungswirkung.
- **Betriebskosten** — Laufende Kosten des Gebaeudebetriebs, die nach Betriebskostenverordnung (BetrKV) umlagefaehig sind.
- **Schonfristzahlung** — Zahlung aller Mietruckstaende durch den Mieter innerhalb von zwei Monaten nach Zustellung der Raeumungsklage; heilt fristlose Kuendigung (§ 569 Abs. 3 BGB).
- **WEG** — Wohnungseigentuemergemeindschaft; geregelt im Wohnungseigentumsgesetz (WEG) in der Fassung nach der Reform 2020.

## Rechtsgrundlagen

- §§ 535-580 BGB — Mietvertrag allgemein
- §§ 556-556g BGB — Betriebskosten und Mietpreisbremse
- §§ 558-558e BGB — Mieterhoehung auf ortsuebliche Vergleichsmiete
- § 558d BGB — Qualifizierter Mietspiegel
- §§ 543, 569 BGB — Ausserordentliche Kuendigung
- § 573 BGB — Ordentliche Kuendigung durch Vermieter (Eigenbedarf)
- § 573c BGB — Kuendigungsfristen
- § 551 BGB — Begrenzung und Anlage der Mietkaution
- §§ 44 ff. WEG — Beschlussanfechtung und -klage (nach WEG-Reform 2020)
- § 29a ZPO — Ausschliessliche Zustaendigkeit Amtsgericht bei Wohnraum

## Schritt-fuer-Schritt: Einstieg ins Plugin

1. Mandantenkonstellation klaeren: Vermieter oder Mieter, Wohnraum oder Gewerbe, Bestandsmiete oder Neuabschluss.
2. Phase des Mandats bestimmen: Mieterhoehung, Nebenkostenstreit, Kuendigung, Kaution, WEG oder Klage.
3. Passenden Skill auswaehlen (siehe Skill-Tour).
4. Eilfristen pruefen: WEG-Anfechtungsklage (§ 45 WEG: ein Monat), Kuendigungsfristen (§ 573c BGB), Mieterhoehungs-Zustimmungsfrist (zwei Monate § 558b BGB).
5. Anschluss-Skill bestimmen: nach Mietspiegel-Ermittlung typischerweise Mieterhoehungsverlangen oder Widerspruch; nach Kuendigung ggf. Klageentwurf.

## Skill-Tour (was gibt es hier?)

**Einstieg und Triage**

- `mandat-triage-mietrecht` — Eingangs-Abfrage: Mandantenrolle, Gegenstandsart, Sachgebiet und Fristen-Sofort-Check.

**Datenerhebung**

- `lage-und-ausstattung-erheben` — Strukturierte Datenerhebung fuer Mietspiegel-Einordnung: Adresse, Baujahr, Wohnflaeche, Ausstattungsmerkmale.
- `mietspiegel-quellen` — Prueft ortsuebliche Vergleichsmiete anhand amtlicher Mietspiegel-Quellen pro Bundesland und Stadttyp.

**Mieterhoehung (Vermieter)**

- `mieterhoehungsverlangen-erstellen` — Mieterhoehungsverlangen nach § 558a BGB mit Begruendung durch Mietspiegel oder Vergleichswohnungen.

**Mieterhoehung (Mieter)**

- `mieterhoehung-pruefen-widersprechen` — Mieterhoehungsverlangen auf Form, Frist, Kappungsgrenze und Begruendung pruefen; Widerspruchs- oder Teilzustimmungs-Entwurf.
- `mietsenkungsverlangen` — Miete auf Mietpreisbremse (§§ 556d ff. BGB), § 5 WiStG und § 291 StGB pruefen; qualifizierte Ruege erstellen.

**Nebenkostenabrechnung**

- `nebenkostenabrechnung-erstellen` — Rechtssichere Betriebskostenabrechnung fuer Vermieter nach § 556 BGB und BetrKV.
- `nebenkostenabrechnung-pruefen` — Betriebskostenabrechnung auf Frist, Form, Umlagefaehigkeit, Verteilerschluessel und HeizkostenV pruefen.

**Kuendigung**

- `mahnung-zahlungsverzug-mieter` — Mahnung und fristlose Kuendigung wegen Zahlungsverzugs nach § 543 Abs. 2 Nr. 3 BGB; gestuftes Schreibenpaket.
- `eigenbedarfskuendigung-erstellen` — Ordentliche Kuendigung wegen Eigenbedarfs nach § 573 Abs. 2 Nr. 2 BGB mit konkreter Begruendung und Fristen.

**Kaution**

- `mietkaution-rueckforderung` — Prueft Rueckforderungsanspruch: Hoechstgrenze, Anlagepflicht, Abrechnungsfrist, Einbehalt und Verjaehrung.

**Kommunikation und WEG**

- `mieteranfragen-beantworten` — Beantwortung von Mieteranfragen sachlich und rechtlich korrekt fuer Vermieter und Hausverwaltungen.
- `weg-beschluss-anfechten` — Prueft Beschlussanfechtungs- und Nichtigkeitsklage nach §§ 44 ff. WEG 2020 mit Monatsfrist.

**Klage**

- `klageentwurf-amtsgericht` — Klageschrift zum Amtsgericht in Mietsachen: Zustaendigkeit, Streitwert, Antraege und Beweisangebote.

## Worauf besonders achten

- **Ausschliesslich amtliche Mietspiegel verwenden.** Das Plugin nutzt nur offiziell anerkannte Quellen; Onlineportale sind keine zulaessige Begruendung fuer Mieterhoehungsverlangen.
- **Kappungsgrenze gilt relativ zum letzten Mieterhoehungsverlangen.** Dreijahresfrist und prozentuale Grenze sind getrennt zu pruefen; Kappungsgrenze in Spannungsgebieten 15 % nach Landesrecht.
- **Kuendigungsbegruendung bei Eigenbedarf muss konkret sein.** Zu abstrakte Begruendungen fuehren zur Unwirksamkeit der Kuendigung; Skill `eigenbedarfskuendigung-erstellen` sichert den Mindestinhalt.
- **WEG-Anfechtungsfrist laeuft hart.** Ein Monat nach Beschlussfassung (§ 45 WEG); danach nur noch Nichtigkeitsklage bei gravierenden Maengeln.
- **Nebenkostenabrechnung muss innerhalb von 12 Monaten zugehen.** Spaeterer Zugang fuehrt zur Unwirksamkeit der Abrechnung und Verlust von Nachzahlungsanspruechen.

## Typische Fehler

- Mieterhoehungsverlangen wird ohne ordnungsgemaesse Begruendung versandt; Mieter kann Zustimmung verweigern und Klage ist unbegrendet.
- Fristlose Kuendigung wird ausgesprochen ohne hilfsweise ordentliche Kuendigung; hilfsweise Kuendigung sichert Rueckfall ab.
- Betriebskostenabrechnung enthaelt nicht umlagefaehige Positionen (z.B. Verwaltungskosten); Mieter kann Rueckforderung geltend machen.
- Mietkaution wird nicht getrennt vom Vermoegen des Vermieters angelegt; bei Insolvenz des Vermieters geht Mieter leer aus.
- WEG-Anfechtungsfrist wird verpasst; nur Nichtigkeitsklage bei sehr schweren Maengeln verbleibt als Option.

## Querverweise

- `subsumtions-pruefer` — Fuer vertiefte Normanwendung bei Einzelfragen (z.B. Tatbestandsmerkmale § 543 BGB).
- `gesellschaftsrecht` — Wenn Vermieter eine GmbH oder AG ist und gesellschaftsrechtliche Fragen relevant werden.
- `mittelstand-corporate-ma` — Wenn Gewerberaummiete im Kontext einer Unternehmenstransaktion steht (Change of Control, Betriebsuebergang).

## Quellen und Aktualitaet

- Stand: 05/2026
- Gesetzesfassungen zum Stand-Datum (BGB, BetrKV, HeizkostenV, WEG, ZPO, WiStG)
