---
name: anfechtungsrechte-antragspflicht-15a
description: "Anfechtungsrechte Antragspflicht 15A: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Anfechtungsrechte Antragspflicht 15A

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Anfechtungsrechte Antragspflicht 15A** im Plugin Insolvenzrecht (InsO). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `anfechtungsrechte-pruefen` | Insolvenzverwalter klagt auf Rückgewaehr einer Zahlung vor Insolvenz oder Gläubiger muss Insolvenzanfechtung abwehren. Prüfraster §§ 129 ff. InsO kongruente Deckung § 130 inkongruente Deckung § 131 vorsaetzliche Benachteiligung § 133 unentgeltliche Leistung § 134 Gesellschafterdarlehen § 135. Anfechtungsfrist drei Monate bis zehn Jahre Bargeschäfts-Privileg § 142 InsO. Berechnung Anfechtungsansprüche Beweislast Hin- und Herwirkung Forderungsanmeldung. Output Anfechtungs-Prüf-Memo mit Tatbestands-Checkliste Betrag und Verteidigungslinien. Abgrenzung: vorsatzanfechtung-133-inso für vertiefte § 133-Prüfung. |
| `antragspflicht-15a-inso` | Analysiert die Insolvenzantragspflicht des Geschäftsleiters nach § 15a InsO, die Haftung wegen Insolvenzverschleppung (§ 823 Abs. 2 BGB iVm § 15a InsO) sowie das Zahlungsverbot nach § 15b InsO. Lädt, wenn Schlagwörter wie "Antragspflicht", "Insolvenzverschleppung", "3-Wochen-Frist", "Zahlungsverbot" oder "§ 15a InsO" auftreten. |
| `auslaendischer-insolvenzverwalter-register-und-grundbuch` | Register- und Grundbuchvollzug bei ausländischer Insolvenz: GmbH-Anteile, Gesellschafterliste, Handelsregister, Grundbuch, Notar, § 29 GBO, § 346 InsO und Nachweis der Rechtsmacht ausländischer office holder. |
| `forderungsanmeldung-glaeubiger-174-177-inso` | Gläubiger meldet Forderung im Insolvenzverfahren an §§ 174-177 InsO: Fristen Form Anlagen Rang § 39 InsO Vorsatz § 174 Abs. 2 InsO nachtraegliche Anmeldung § 177 InsO Prüfungstermin § 176 Bestreiten § 178 Tabelle § 179 InsO. Mit Mustertexten und Fehlerkatalog. |

## Arbeitsweg

Im Plugin Insolvenzrecht (InsO) gilt für **Anfechtungsrechte Antragspflicht 15A**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `anfechtungsrechte-pruefen`

**Fokus:** Insolvenzverwalter klagt auf Rückgewaehr einer Zahlung vor Insolvenz oder Gläubiger muss Insolvenzanfechtung abwehren. Prüfraster §§ 129 ff. InsO kongruente Deckung § 130 inkongruente Deckung § 131 vorsaetzliche Benachteiligung § 133 unentgeltliche Leistung § 134 Gesellschafterdarlehen § 135. Anfechtungsfrist drei Monate bis zehn Jahre Bargeschäfts-Privileg § 142 InsO. Berechnung Anfechtungsansprüche Beweislast Hin- und Herwirkung Forderungsanmeldung. Output Anfechtungs-Prüf-Memo mit Tatbestands-Checkliste Betrag und Verteidigungslinien. Abgrenzung: vorsatzanfechtung-133-inso für vertiefte § 133-Prüfung.

# Insolvenzanfechtungsrechte prüfen

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Insolvenzanfechtungsrechte prüfen` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Zweck

Das wichtigste Werkzeug des Insolvenzverwalters zur Massevermehrung. Bei Mandanten-Seite (Anfechtungs-Gegner) das Werkzeug zur Verteidigung.

## Eingaben

- Insolvenzantrags-Datum
- Insolvenzeröffnungs-Datum
- Eröffnungs-Beschluss
- Liste der zurückgeforderten Zahlungen / Vermögens-Bewegungen
- Buchhaltung Schuldner
- Korrespondenz Schuldner / Anfechtungs-Gegner
- Vertragsbasis (Werkvertrag Kaufvertrag Darlehen)
- Wissen des Anfechtungs-Gegners über Zahlungs-Schwierigkeiten

## Schritt 1 — Allgemeine Anfechtungs-Voraussetzungen § 129 InsO

- **Rechtshandlung** vor Verfahrenseröffnung
- **Gläubiger-Benachteiligung** (Aktivenminderung Passivmehrung)
- Beweislast für Benachteiligung beim Insolvenzverwalter

## Schritt 2 — Spezielle Anfechtungs-Tatbestände

### § 130 InsO — Kongruente Deckung

- Rechtshandlung in **letzten drei Monaten** vor Antrag
- Schuldner **zahlungsunfähig**
- Anfechtungs-Gegner **kannte** Zahlungsunfähigkeit oder Umstände die zwingend darauf schließen lassen
- "Kongruent" — Anfechtungs-Gegner hatte vertraglichen Anspruch auf das Erlangte

### § 131 InsO — Inkongruente Deckung

- Rechtshandlung in **letztem Monat** vor Antrag oder danach (Abs. 1 Nr. 1)
- In letzten drei Monaten — wenn Schuldner zahlungsunfähig (Abs. 1 Nr. 2)
- In letzten drei Monaten — wenn Anfechtungs-Gegner Benachteiligungs-Wissen (Abs. 1 Nr. 3)
- "Inkongruent" — Anfechtungs-Gegner hatte **keinen** vertraglichen Anspruch (Aufrechnungs-Möglichkeit Sicherheit-Leistung Vorauszahlung)

### § 132 InsO — Unmittelbar nachteilige Rechtshandlung

- Rechtshandlung in letzten drei Monaten
- Schuldner zahlungsunfähig
- Anfechtungs-Gegner kannte oder Anhaltspunkte für Zahlungsunfähigkeit Benachteiligungsvorsatz

### § 133 InsO — Vorsätzliche Benachteiligung

- Rechtshandlung in **letzten zehn Jahren** (vier Jahre für Deckungs-Konstellationen seit 2017-Reform)
- Schuldner mit **Vorsatz** Gläubiger zu benachteiligen
- Anfechtungs-Gegner kannte den Vorsatz

**Vermutung § 133 Abs. 1 Satz 2 InsO** — Vorsatzkenntnis vermutet wenn Anfechtungs-Gegner Zahlungsunfähigkeit drohende Zahlungsunfähigkeit und Gläubigerbenachteiligung kannte.

**BGH-Rechtsprechung dazu** restriktiver geworden mit § 133-Reform 2017 — bestätigt und konkretisiert:

- **BGH IX ZR 72/20 vom 06.05.2021** (Grundsatzentscheidung Neuausrichtung) — bloße objektive Zahlungsunfähigkeit lässt keinen automatischen Schluss auf Vorsatz zu.
- **BGH IX ZR 129/22 vom 18.04.2024** — Bestätigung der Linie: bei verifizierter Zahlungsunfähigkeit ist konkret darzulegen, ob der Schuldner wusste oder billigend in Kauf nahm, dass andere Gläubiger zu späterer Zeit nicht vollständig befriedigt werden können.
 Quelle: <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=18.04.2024&Aktenzeichen=IX+ZR+129/22>
- Seit 2017 Vorsatz-Anfechtung gestaffelt:
 - **Vier Jahre** für Deckungs-Konstellationen (§ 133 Abs. 2 InsO) — kongruent
 - **Zehn Jahre** für sonstige Konstellationen (§ 133 Abs. 1 InsO)

### § 134 InsO — Unentgeltliche Leistung

- Rechtshandlung in **letzten vier Jahren**
- Unentgeltliche Leistung (Schenkung Verzicht)
- **Schenkung Verwandter** — auch Mittel-/Mittelbar
- Geringe Geschenke ausgenommen

### § 135 InsO — Gesellschafterdarlehen-Rückgewähr

- **Rückgewähr Gesellschafterdarlehen** im letzten Jahr vor Antrag
- **Anfechtbar auch bei Erfüllung** ohne weitere Voraussetzungen
- Auch wirtschaftlich gleichgestellte Forderungen

## Schritt 3 — Bargeschäft § 142 InsO

### Ausschluss der Anfechtung

- Bargeschäft = **gleichwertige Gegenleistung in unmittelbarem zeitlichem Zusammenhang**
- Anfechtbarkeit ausgeschlossen — außer bei Vorsatzanfechtung § 133 InsO; dann nur, wenn der Schuldner **unlauter** handelte und der andere Teil dies erkannte (§ 142 Abs. 1 Hs. 2 InsO).

### Unlauterkeit (BGH IX ZR 122/23 vom 05.12.2024)

Erstmalige höchstrichterliche Konkretisierung: Unlauterkeit erfordert ein gezielt schädigendes Verhalten gegenüber den übrigen Gläubigern; die Transaktion muss bewusst zur Benachteiligung anderer oder zur gezielten Bevorzugung des Empfängers genutzt werden. Bloße dauerhafte Verlustsituation genügt nicht.
Quelle: <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=05.12.2024&Aktenzeichen=IX+ZR+122/23>

### Anwendung

- Tausch sofortig
- Bezahlung gegen Lieferung
- Lohnzahlung gegen Arbeit (kein starres 30-Tage-Limit; enger zeitlicher Zusammenhang erforderlich, BGH IX ZR 122/23)

## Schritt 4 — Rechtshandlung Definition

- **Rechtsgeschäft** Vertrag Anfechtung Zustimmung
- **Realakt** mit rechtlicher Bedeutung (Ausübungs-Erklärung Vollstreckungs-Maßnahme)
- **Zwangsvollstreckung** zählt als Rechtshandlung § 131 Abs. 1 Nr. 1 / 2 InsO

## Schritt 5 — Bösgläubigkeit Anfechtungs-Gegner

### Kenntnis-Element

- **Tatsächliche Kenntnis** Zahlungs-Unfähigkeit
- **Umstände die zwingend darauf schließen lassen** § 130 Abs. 2 InsO
- Bei Geschäftspartnern mit häufigen Kontakten beobachtbar

### Bei Banken

- Sonderbeobachtung — Bank hat über Zahlungsverhalten Konto-Information
- Kündigung Kreditlinie → Bank musste Kenntnis haben

### Bei Steuerbehörden

- BGH-Linie: Vollstreckungs-Druck der Finanzbehörde indiziert regelmäßig Kenntnis der Zahlungsunfähigkeit
- §§ 130, 131 anwendbar bei Steuer-Beitreibung; konkrete BGH-Entscheidung (Datum, Aktenzeichen) vor Ausgabe über dejure.org/openjur.de verifizieren

## Schritt 6 — Rechtsfolge

### Verpflichtungs-Wirkung § 143 InsO

- **Rückgewähr** in Natur oder Wertersatz
- **Zinsen** gegen Anfechtungs-Gegner ab Eröffnung

### Rückforderung Gläubiger-Stellung § 144 InsO

- Anfechtungs-Gegner kann Forderung wieder geltend machen
- Anmeldung zur Insolvenz-Tabelle
- Insolvenzquote auf wieder aufgelebte Forderung

## Schritt 7 — Verjährung § 146 InsO

- **Drei Jahre** ab Verfahrenseröffnung
- Hemmung-Vorschriften BGB

## Schritt 8 — Strategische Überlegung — Insolvenzverwalter-Sicht

- **Vermögen-Aufnahme** vollständig
- **Identifikation Anfechtungs-Tatbestände** Massevergleich
- **Verfolgungs-Reihenfolge** je Aussicht
- **Vergleichs-Strategie** vs. Klage
- **Beweislast-Konstellation** Bereich § 133 InsO erschwert seit 2017
- **Anfechtungs-Klagen** zur Bestätigung Quote

## Schritt 9 — Strategische Überlegung — Anfechtungs-Gegner-Sicht

- **Bargeschäft-Verteidigung** prüfen
- **Kenntnis-Bestreitung**
- **Vergleichs-Verhandlung** häufig erfolgreich (50–70 Prozent Quote als Verhandlungsstand)
- **Sicherungseigentum** vs. unentgeltliche Leistung
- **Verjährung** § 146 InsO drei Jahre häufig vergessen

## Schritt 10 — Sonderfälle

### Anfechtbarkeit von Lohnzahlungen

- Arbeitnehmer-Lohn als Bargeschäft typisch
- Aber Vorausziehungen Sonderzahlungen ggf. anfechtbar

### Anfechtung Konzernsachverhalten

- Cash-Pool-Verbund
- Konzerndarlehen → Gesellschafterdarlehen § 135

### Anfechtung Familien-Übertragung

- Häufig § 134 — unentgeltliche Leistung Verwandter
- Vier-Jahres-Frist

## Schritt 11 — Anfechtungsklage

- Sachlich LG zuständig § 71 GVG
- Klageschrift mit Anfechtungs-Tatbestand
- Beweislast Insolvenzverwalter
- Beklagter: Anfechtungs-Gegner

## Ausgabe

- `anfechtung-pruefung.md` mit Anfechtungstatbestand-für-Tatbestand
- Tabelle der angefochtenen Vorgänge mit Erfolgsaussicht
- Bei Verteidigung: Bargeschäft-Analyse Kenntnis-Bestreitung
- Klageschrift-Entwurf oder Verteidigungs-Schriftsatz
- Frist im Fristenbuch (drei Jahre § 146 InsO)
- Vergleichs-Verhandlungs-Vorbereitung

## Quellen

- InsO §§ 129–147
- **BGH IX ZR 122/23 vom 05.12.2024** — Unlauterkeit beim Bargeschäft § 142 InsO
 <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=05.12.2024&Aktenzeichen=IX+ZR+122/23>
- **BGH IX ZR 129/22 vom 18.04.2024** — Neuausrichtung Vorsatzanfechtung
 <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=18.04.2024&Aktenzeichen=IX+ZR+129/22>
- **BGH IX ZR 239/22 vom 18.04.2024** — Anfechtung wegen gesellschafterähnlicher Stellung (§ 135 InsO)
 <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=18.04.2024&Aktenzeichen=IX+ZR+239/22>
- Ältere Leitentscheidungen (insb. BGH IX ZR 72/20 vom 06.05.2021, Liquiditätsstatus-Beweislast, § 138 InsO nahestehende Personen): vor Ausgabe konkretes Datum, Aktenzeichen, Randnummer in offener Quelle (dejure.org, openjur.de, bundesgerichtshof.de) prüfen.
- Literatur und Handbücher nur bei vorhandenem Live-Zugriff.


## Triage — Anfechtungs-Erstcheck

Bevor losgelegt wird, klaere:

1. **Tatbestandsbereich?** § 130/131 (3 Monate), § 132 (3 Monate), § 133 Abs. 1 (10 Jahre) / Abs. 2 (4 Jahre), § 134 (4 Jahre), § 135 (1 Jahr).
2. **Verjährung § 146 InsO?** 3 Jahre ab Kenntnis des IV, max. 10 Jahre ab Rechtshandlung — Frist sofort prüfen!
3. **Nahestehende Person § 138 InsO?** Gesellschafter >25%, GF, Ehegatte → Beweislastumkehr zugunsten IV.
4. **Bargeschäft § 142 InsO?** Bei kongruenten unmittelbaren Austauschen: Bargeschäft prüfen; Unlauterkeit nach BGH IX ZR 122/23 separat darlegen.
5. **Vorsatz § 133 InsO?** Nach BGH IX ZR 129/22 (18.04.2024): konkrete Bedrohungslage und Erwartung dauerhafter Unterdeckung, nicht bloß drohende ZU.

## 2. `antragspflicht-15a-inso`

**Fokus:** Analysiert die Insolvenzantragspflicht des Geschäftsleiters nach § 15a InsO, die Haftung wegen Insolvenzverschleppung (§ 823 Abs. 2 BGB iVm § 15a InsO) sowie das Zahlungsverbot nach § 15b InsO. Lädt, wenn Schlagwörter wie "Antragspflicht", "Insolvenzverschleppung", "3-Wochen-Frist", "Zahlungsverbot" oder "§ 15a InsO" auftreten.

# § 15a InsO — Antragspflicht, Insolvenzverschleppung und § 15b InsO Zahlungsverbot

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `§ 15a InsO — Antragspflicht, Insolvenzverschleppung und § 15b InsO Zahlungsverbot` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Zweck

Dieser Skill unterstützt bei der Prüfung, ob und wann der Geschäftsleiter einer
juristischen Person (insbesondere GmbH, AG, GmbH & Co. KG) zur Stellung eines
Insolvenzantrags verpflichtet ist, welche zivilrechtlichen und strafrechtlichen
Haftungsfolgen bei Pflichtverletzung drohen und welche Zahlungspflichten nach
§ 15b InsO gelten. Der Skill legt den Fokus auf die Antrags­fristen, die
Haftungsstruktur gegenüber Neu- und Altgläubigern sowie die Dokumentations-
pflichten des Geschäftsleiters.

## Eingaben

- Rechtsform der Gesellschaft (GmbH, AG, GmbH & Co. KG, etc.)
- Festgestellter oder streitiger Eröffnungsgrund (Zahlungsunfähigkeit, drohende
 Zahlungsunfähigkeit, Überschuldung) — ggf. Verweis auf Schwester-Skills
 § 17 InsO und § 19 InsO
- Zeitpunkt des Eintritts des Eröffnungsgrundes (tatsächlich oder vorgeworfen)
- Zeitpunkt der Antragstellung bzw. deren Unterlassen
- Vorhandensein von Sanierungsbemühungen (StaRUG, außergerichtliche Einigung,
 Sanierungsmoderation § 94 ff. StaRUG) und deren Dokumentationsstand
- Zahlungen nach Eintritt des Eröffnungsgrundes (Art, Betrag, Datum)
- D&O-Versicherungsschutz (soweit relevant)

## Rechtlicher Rahmen

### § 15a InsO — Gesetzliche Grundlage

**Abs. 1:** Mitglieder des Vertretungsorgans einer juristischen Person sind
verpflichtet, ohne schuldhaftes Zögern, spätestens aber innerhalb von drei
Wochen nach Eintritt der Zahlungsunfähigkeit oder sechs Wochen nach Eintritt
der Überschuldung, Insolvenzantrag zu stellen. Die verlängerte Sechswochenfrist
für Überschuldung wurde durch das Sanierungs- und Insolvenzrechtsfortentwick-
lungsgesetz (SanInsFoG) zum 01.01.2021 eingeführt (zuvor ebenfalls drei
Wochen). Beide Fristen sind **Höchstfristen**, kein "Recht zu warten": Der
Antrag ist zu stellen, sobald ein Eröffnungsgrund vorliegt und ernsthafte,
objektiv erfolgversprechende Sanierungsbemühungen nicht nachgewiesen werden
können.

**Abs. 2:** Bei führerloser Gesellschaft (kein organschaftlicher Vertreter mehr
bestellt) trifft die Antragspflicht jeden Gesellschafter (GmbH) bzw. jedes
Mitglied des Aufsichtsrats (AG).

**Abs. 3:** Antragspflicht gilt entsprechend für Gesellschaften ohne
Rechtspersönlichkeit (GmbH & Co. KG), wenn keine natürliche Person unbeschränkt
haftet.

**Abs. 4–6 — Strafbarkeit:**
- Abs. 4: Vorsätzliche Verletzung der Antragspflicht — Freiheitsstrafe bis zu
 drei Jahren oder Geldstrafe.
- Abs. 5: Fahrlässige Verletzung — Freiheitsstrafe bis zu einem Jahr oder
 Geldstrafe.
- Abs. 6: Strafbarkeitsmilderung bei nachgeholtem Antrag; Abs. 4 bleibt
 Offizialdelikt.

### § 15b InsO — Zahlungsverbot (seit SanInsFoG 01.01.2021)

§ 15b InsO hat die vormaligen gesellschaftsrechtlichen Regelungen
(§ 64 GmbHG a.F., § 92 Abs. 2 AktG a.F., § 130a HGB a.F.) in einer
einheitlichen Norm konsolidiert.

**Abs. 1 S. 1:** Nach Eintritt der Zahlungsunfähigkeit oder Überschuldung darf
der Geschäftsleiter keine Zahlungen mehr leisten, die mit der Sorgfalt eines
ordentlichen und gewissenhaften Geschäftsleiters unvereinbar sind.

**Abs. 1 S. 2 (Sorgfaltsausnahme):** Zahlungen, die mit der gebotenen Sorgfalt
vereinbar sind, bleiben zulässig. Hierzu zählen insbesondere betriebsnotwendige
Zahlungen zur Aufrechterhaltung der Betriebsbereitschaft (Löhne, Miete,
Energie) im Antragszeitraum, sofern realistisch Masse erhalten wird.

**Abs. 8:** Steuerzahlungen und Zahlungen an die Sozialversicherungsträger
können auch nach Eintritt der Insolvenzreife privilegiert sein, wenn die
Nichtleistung zur persönlichen Haftung des Geschäftsführers (§ 69 AO) führen
würde.

> Hinweis: Die Privilegierung des § 15b Abs. 8 InsO (Steuerzahlungen,
> Sozialversicherungsbeiträge) ist eng auszulegen und schützt nicht vor
> Erstattungsansprüchen des Insolvenzverwalters, wenn die Zahlungen die Masse
> schmälern und keine gleichwertige Gegenleistung erlangt wurde.
> Verifizierung der konkreten BGH-Linie erforderlich (dejure.org, openjur.de): keine Entscheidung aus Modellwissen zitieren; Gericht, Datum, Aktenzeichen, Randnummer vor Ausgabe prüfen.

### Kanonische und aktuelle Rechtsprechung (Stand Mai 2026)

**BGH II ZR 206/22 vom 23.07.2024** — Fortwirkende Haftung des
ausgeschiedenen Geschäftsführers. Der II. Zivilsenat hat entschieden, dass ein
nach § 823 Abs. 2 BGB iVm § 15a InsO haftender ausgeschiedener
Geschäftsführer grundsätzlich auch für Neugläubigerschäden einzustehen hat,
die erst nach seinem Ausscheiden entstehen, sofern die durch seine
Antragspflichtverletzung geschaffene Gefährdungslage zum
Schadensentstehungszeitpunkt fortbesteht. Bruch der Kausalkette nur bei
nachhaltiger Sanierung. Praxisfolge: Haftung endet nicht mit der Amtsniederlegung.
Quelle: <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=23.07.2024&Aktenzeichen=II+ZR+206/22>

**BGH 5 StR 287/24 vom 27.02.2025** — Faktischer Geschäftsführer / Firmenbestattung.
Der 5. Strafsenat hat den Kriterienkatalog der faktischen Geschäftsführung iSd
§ 283 StGB / § 15a InsO neu kalibriert. Auch Hintermänner im
Firmenbestatter-Modell können als Täter haften, wenn sie die tatsächliche
Geschäftsführung ausüben; das bloße Nicht-Auftreten nach außen schließt
Strafbarkeit nicht aus.
Quelle: <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=27.02.2025&Aktenzeichen=5+StR+287/24>

**BGH IV ZR 66/25 vom 19.11.2025** — D&O-Versicherung / Wissentlichkeitsausschluss.
Der IV. Zivilsenat hat klargestellt, dass der D&O-Versicherer für jeden
einzelnen verbotswidrigen Zahlungsvorgang gesondert darlegen und beweisen
muss, dass der Geschäftsleiter positive Kenntnis von der konkreten
Pflichtverletzung hatte. Die Verletzung der Insolvenzantragspflicht
(§ 15a InsO) indiziert nicht automatisch eine wissentliche Verletzung der
Masseerhaltungspflicht (§ 15b InsO); ein "Aufkoppeln" verschiedener
Pflichtverletzungen ist unzulässig.
Quelle: Bundesgerichtshof Pressemitteilung 2025; <https://www.noerr.com/de/insights/bgh-zum-do-versicherungsschutz-verletzung-der-insolvenzantragspflicht-durch-geschaftsleiter-indiziert-keine-wissentliche-verletzung-der-masseerhaltungspflicht>

> **Grundsätze (aus älterer BGH-Rspr., vor Ausgabe live verifizieren):**
> - § 15a InsO ist Schutzgesetz iSd § 823 Abs. 2 BGB. Neugläubiger können
> ihren vollen Vertrauensschaden ersetzt verlangen; Altgläubiger sind auf
> den Quotenschaden beschränkt.
> - Feststellung der Zahlungsunfähigkeit über Liquiditätsbilanz; die
> Dreiwochenfrist dient nur der Abgrenzung zur vorübergehenden
> Zahlungsstockung — keine "Schonfrist".
> - Der Geschäftsführer muss die wirtschaftliche Lage laufend im Blick
> behalten; fahrlässige Unkenntnis schützt nicht.
> Verifizierung erforderlich: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe Gericht, Entscheidungsform, Datum, Aktenzeichen und tragende Aussage über offizielle oder frei zugängliche Quelle (dejure.org, openjur.de, bundesgerichtshof.de) prüfen.

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
### IDW-Standard

**IDW S 11 (Beurteilung des Vorliegens von Insolvenzeröffnungsgründen),
Tz. 7 ff.:** Der Standard definiert den Prüfungsauftrag und das methodische
Vorgehen für die Feststellung von Zahlungsunfähigkeit und Überschuldung. Der
IDW S 11 ist Maßstab für die Beurteilung, ob und wann ein Eröffnungsgrund
objektiv vorlag — mit unmittelbarer Relevanz für die Bestimmung des
Fristbeginns nach § 15a Abs. 1 InsO. Tz. 8 ff. regeln den Stichtag der
Feststellung; Tz. 16 ff. die Fortbestehensprognose im Überschuldungskontext.

## Ablauf

**Vorab:** Der untenstehende ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der ist Leitfaden, nicht Pflichtprogramm.

1. **Feststellung des Eröffnungsgrundes**
 Zunächst ist zu klären, ob Zahlungsunfähigkeit (§ 17 InsO — s. Schwester-
 Skill) oder Überschuldung (§ 19 InsO — s. Schwester-Skill) vorliegt.
 Maßgeblicher Zeitpunkt ist der objektive Eintritt; für die Haftung genügt
 Kennenmüssen (fahrlässige Unkenntnis). IDW S 11 liefert den methodischen
 Rahmen.

2. **Beginn der Antragsfrist**
 Die Frist beginnt mit dem objektiven Eintritt des Eröffnungsgrundes,
 frühestens jedoch mit dem Zeitpunkt, in dem der Geschäftsleiter diesen
 kannte oder bei pflichtgemäßer Sorgfalt kennen musste (fahrlässige
 Unkenntnis schützt nicht). Dreiwochenfrist bei Zahlungsunfähigkeit,
 Sechswochenfrist bei Überschuldung (seit 01.01.2021, SanInsFoG).
 Konkrete BGH-Entscheidungen zur Erkennbarkeit der Insolvenzreife vor Ausgabe verifizieren (dejure.org, openjur.de).

3. **Sanierungsversuche dokumentieren**
 Sanierungsbemühungen können den Fristablauf nicht hemmen, senken aber das
 Verschulden und können im Einzelfall belegen, dass keine Pflicht­verletzung
 vorlag. Voraussetzung ist ein belastbares Sanierungskonzept mit konkreter
 Erfolgsaussicht. Geeignete Instrumente: außergerichtliche Einigung,
 Sanierungsmoderation (§§ 94 ff. StaRUG), vorläufiger Restrukturierungs­rahmen
 (§§ 29 ff. StaRUG). Jede Maßnahme ist schriftlich mit Datum, Beteiligten und
 Ergebnis zu dokumentieren (Vorstands-/Geschäftsführerprotokoll).

4. **Antragstellung spätestens mit Ablauf der Höchstfrist**
 Bei Zahlungsunfähigkeit: Antrag spätestens am 21. Tag nach Fristbeginn.
 Bei Überschuldung: spätestens am 42. Tag. Jeder Tag der Überschreitung
 verlängert den Haftungszeitraum. Fristversäumnis begründet zugleich
 Strafbarkeit nach § 15a Abs. 4 oder Abs. 5 InsO.

5. **Haftungsdokumentation Geschäftsführer**
 Für die Haftungsabwehr ist eine lückenlose Dokumentation erforderlich:
 Bilanzen, Liquiditätspläne, Beratungsmandate (Steuerberater, Sanierungsberater),
 Gesellschafter­beschlüsse, Korrespondenz mit Gläubigern und Kreditinstituten.
 Bei Beauftragung eines Insolvenzberaters: Mandat, Stellungnahme und zeitlicher
 Ablauf festhalten. Bestehende D&O-Versicherungspolice prüfen (Coverage,
 Selbstbehalt, Ausschlussklauseln für wissentliche Pflichtverletzungen).

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Antragspflicht § 15a InsO pruefend und Beratungsschreiben erstellen | Beratungsschreiben nach Pruefschema; Template unten |
| Variante A — Insolvenzreife strittig Gutachten noetig | Sachverstaendigen-Gutachten zuerst; Beratungsschreiben nach Klaerunm |
| Variante B — Sanierung noch moeglich StaRUG als Alternative | StaRUG-Option parallel pruefen; Antrag nicht zwingend sofort |
| Variante C — Gesellschafter kennen Lage bereits Haftungsrisiko | Haftungs-Beratung separat; Antragspflicht und Haftung unterscheiden |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

## Ausgabeformat

Ausgabe in strukturierter Prosa oder tabellarischer Form, jeweils bestehend aus:

- **Sachverhaltszusammenfassung:** Eröffnungsgrund, Datum des Eintritts,
 Fristbeginn und -ende (konkrete Daten).
- **Haftungsprüfung:** Pflicht­verletzung (ja/nein, Begründung), Verschulden
 (Vorsatz/Fahrlässigkeit), Schaden (Neugläubiger: Vertrauensschaden;
 Altgläubiger: Quotenschaden). Bei ausgeschiedenem GF: BGH II ZR 206/22
 prüfen (fortwirkende Gefährdungslage).
- **Zahlungsverbot-Prüfung (§ 15b InsO):** Verbotene Zahlungen mit Datum und
 Betrag; Ausnahmen (§ 15b Abs. 1 S. 2, Abs. 8).
- **Strafrechtliches Risiko:** § 15a Abs. 4 oder Abs. 5 InsO; bei faktischer
 Geschäftsführung BGH 5 StR 287/24 vom 27.02.2025 beachten.
- **Handlungsempfehlungen:** Nachholung des Antrags, Dokumentation,
 D&O-Deckungsprüfung (BGH IV ZR 66/25 vom 19.11.2025: positive Kenntnis pro
 Pflichtverletzung erforderlich).
- **Belege:** Mindestens zwei einschlägige BGH-Entscheidungen mit Randnummer
 aus offener Quelle (dejure.org, openjur.de, bundesgerichtshof.de), IDW S 11.

## Beispiel

**Sachverhalt:** Geschäftsführer Müller der Müller Handels-GmbH erkennt am
22.04.2026, dass die Gesellschaft dauerhaft zahlungsunfähig ist (§ 17 InsO).
Ein Insolvenzantrag wird erst am 02.06.2026 gestellt.

**Fristberechnung:**
- Fristbeginn: 22.04.2026 (Kenntnis des Eröffnungsgrundes)
- Höchstfrist (3 Wochen): **13.05.2026**
- Antragstellung: 02.06.2026 — **Überschreitung um 20 Tage**

**Haftungsfolgen:**

1. *Zivilrechtlich (§ 823 Abs. 2 BGB iVm § 15a InsO):*
 Neugläubiger, die zwischen dem 13.05.2026 und dem 02.06.2026 Vertragsbeziehungen
 mit der GmbH eingegangen sind, können ihren Vertrauensschaden (vollständiger
 Forderungsausfall abzüglich etwaiger Insolvenzquote) von Müller persönlich
 ersetzt verlangen. Altgläubiger können den Quotenschaden geltend machen.
 Sollte Müller vor dem 02.06.2026 ausscheiden, bleibt nach **BGH II ZR 206/22
 vom 23.07.2024** die Haftung für danach hinzutretende Neugläubigerschäden
 bestehen, solange die ursprünglich geschaffene Gefährdungslage fortbesteht.

2. *Zahlungsverbot (§ 15b InsO):*
 Zahlungen, die Müller nach dem 22.04.2026 veranlasst hat und die nicht unter
 § 15b Abs. 1 S. 2 oder Abs. 8 fallen, sind erstattungsfähig. Der
 Insolvenzverwalter kann Müller auf Rückzahlung in Anspruch nehmen.

3. *Strafrechtlich (§ 15a Abs. 4 InsO):*
 Bei nachgewiesenem Vorsatz (Müller kannte den Eröffnungsgrund seit 22.04.2026):
 Freiheitsstrafe bis zu drei Jahren oder Geldstrafe. Bei Fahrlässigkeit
 (§ 15a Abs. 5 InsO): Freiheitsstrafe bis zu einem Jahr oder Geldstrafe.

## Risiken und typische Fehler

**1. Fristbeginn bei "wusste oder musste wissen"**
Der Fristbeginn ist objektiv. Es genügt, dass der Geschäftsleiter bei
pflichtgemäßer Sorgfalt — d.h. bei Führung einer ordnungsgemäßen Buchhaltung
und zeitnäher Aufstellung von Liquiditätsplänen — den Eröffnungsgrund hätte
erkennen müssen. Berufung auf Unkenntnis infolge mangelhafter interner
Kontrolle schützt nicht. Konkrete BGH-Linie über offene Quellen verifizieren.

**2. Sanierungsverhandlungen hemmen den Fristlauf nicht automatisch**
Der bloße Umstand, dass Gespräche mit Gläubigern oder Banken laufen,
unterbricht die Antragsfrist nicht. Nur ein belastbares, realistisches
Sanierungskonzept mit konkreter Finanzierungszusage kann im Einzelfall das
Verschulden mindern. Fehlt das Konzept, bleibt die Frist unberührt.

**3. Faktischer Geschäftsführer ist antragspflichtig**
§ 15a InsO erfasst auch faktische Geschäftsführer, d.h. Personen, die ohne
formale Bestellung die typischen Aufgaben der Geschäftsleitung tatsächlich
ausüben — z.B. Strohmann-Konstellationen, Firmenbestatter-Modelle, oder
Gesellschafter, die die Geschäfte an sich gezogen haben.
**BGH 5 StR 287/24 vom 27.02.2025** hat die Kriterien neu kalibriert: Auch
Hintermänner ohne Außenauftritt können als faktische Geschäftsführer haften;
maßgeblich ist die tatsächliche Ausübung leitender Tätigkeit.
Quelle: <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=27.02.2025&Aktenzeichen=5+StR+287/24>

**4. D&O-Versicherung — Deckungslücken**
Typische Ausschlüsse in D&O-Policen: wissentliche Pflichtverletzung,
vorsätzliche Tatbegehung, unrichtige Zusicherungen.
**BGH IV ZR 66/25 vom 19.11.2025** hat die Position des versicherten
Geschäftsleiters gestärkt: Der D&O-Versicherer muss für jede einzelne
verbotswidrige Zahlung gesondert positive Kenntnis des Geschäftsleiters von
der konkreten Pflichtverletzung darlegen und beweisen. Die Verletzung der
Antragspflicht (§ 15a InsO) indiziert nicht automatisch eine wissentliche
Verletzung der Masseerhaltungspflicht (§ 15b InsO); ein "Aufkoppeln"
verschiedener Pflichtverletzungen ist unzulässig.
Frühzeitige Anzeige an den D&O-Versicherer und Einholung einer
Deckungsbestätigung sind weiterhin unverzichtbar.
Quelle: <https://www.noerr.com/de/insights/bgh-zum-do-versicherungsschutz-verletzung-der-insolvenzantragspflicht-durch-geschaftsleiter-indiziert-keine-wissentliche-verletzung-der-masseerhaltungspflicht> (Aktenzeichen über offene Quelle verifizieren)

**5. Versäumnis bei mehrköpfiger Geschäftsführung**
In einer GmbH mit mehreren Geschäftsführern ist jeder einzeln antragspflichtig;
die Pflicht ist nicht delegierbar. Der ressortfremde Geschäftsführer kann sich
nicht auf den Ressortzuschnitt berufen, sondern muss sich ein eigenes Bild von
der Vermögens- und Liquiditätslage verschaffen. Konkrete BGH-Entscheidung über
offene Quelle (dejure.org) verifizieren.

**6. § 15b InsO — Irrtum über zulässige Zahlungen**
Verbreiteter Fehler: Geschäftsleiter nehmen an, Gehaltszahlungen an sich selbst
oder Darlehensrückführungen an Gesellschafter seien stets zulässig. Nach Eintritt
der Insolvenzreife sind auch diese Zahlungen vom Verbot erfasst, sofern sie
nicht unter die Ausnahmen fallen.

## Quellenpflicht

Bei jeder Ausgabe zu diesem Skill sind mindestens folgende Belege anzugeben (offene Quelle, vor Ausgabe live prüfen):

- BGH II ZR 206/22 vom 23.07.2024 (Fortwirkende Haftung des ausgeschiedenen Geschäftsführers für Neugläubigerschäden)
 <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=23.07.2024&Aktenzeichen=II+ZR+206/22>
- BGH 5 StR 287/24 vom 27.02.2025 (Faktischer Geschäftsführer / Firmenbestattung)
 <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=27.02.2025&Aktenzeichen=5+StR+287/24>
- BGH IV ZR 66/25 vom 19.11.2025 (D&O-Versicherung; wissentliche Pflichtverletzung erfordert positive Kenntnis pro Pflichtverletzung)
 Bundesgerichtshof Pressemitteilung 2025 (Verifikation über bundesgerichtshof.de / dejure.org)
- Altere BGH-Linie zur Antragspflichthaftung (Schutzgesetz, Vertrauensschaden Neugläubiger, Quotenschaden Altgläubiger) und zur Feststellung der Zahlungsunfähigkeit (Liquiditätsbilanz, Aktiva II / Passiva II): vor Ausgabe Gericht, Datum, Aktenzeichen, Randnummer in offener Quelle prüfen.
- IDW S 11 (Beurteilung des Vorliegens von Insolvenzeröffnungsgründen), Tz. 7 ff.
- Literatur nur bei vom Nutzer bereitgestellter oder lizenziert live geprüfter Quelle; keine Kommentarblindzitate.

---
*Dieser Skill ersetzt keine konkrete anwaltliche Beratung im Einzelfall.*

## Triage — Antragspflicht § 15a InsO

Bevor losgelegt wird, klaere:

1. **Rechtsform?** § 15a InsO gilt fuer GmbH, AG, UG, GmbH & Co. KG; natuerliche Personen: keine Antragspflicht, nur Antragsrecht.
2. **Eröffnungsgrund?** ZU § 17 InsO: Frist 3 Wochen. Ueberschuldung § 19 InsO: Frist 6 Wochen. Frist-Uhr laeuft ab erstem Kenntnistag.
3. **Faktischer Geschäftsführer?** Auch ohne formale Bestellung haftet, wer die Geschäftsführung tatsächlich ausübt — neu kalibriert durch BGH 5 StR 287/24 vom 27.02.2025 (Firmenbestattung). Hintermänner ohne Außenauftritt nicht ausgeschlossen.
4. **Sanierungsversuch?** Antragspflicht wird durch echten Sanierungsversuch NICHT beseitigt; Frist laeuft weiter; Eigenantrag sichert Sanierungszeit.
5. **Zahlungen nach Insolvenzreife?** § 15b InsO: Zahlungen nach Insolvenzreife von GF persoenlich erstattten; Ausnahme nur Betriebskostenentgeltsatz ohne Massebeeintraechtigung.
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Output-Template Beratungsschreiben Antragspflicht

**Adressat:** Geschaeftsfuehrung [FIRMA] — Tonfall: klar-warnend mit Handlungsempfehlung

```
VERTRAULICH — ANWALTLICHES SCHREIBEN
[KANZLEI]
[DATUM]

Betreff: Dringende Hinweis — Insolvenzantragspflicht § 15a InsO

Sehr geehrte/r Frau/Herr [NAME],

nach unserer heutigen Beratung weise ich Sie ausdruecklich darauf hin:

Es besteht [Zahlungsunfaehigkeit § 17 InsO / Ueberschuldung § 19 InsO].
Die Antragsfrist des § 15a Abs. 1 InsO laeuft am [DATUM] ab.

Bei Ueberschreitung dieser Frist drohen:
- Strafbarkeit nach § 15a Abs. 4 InsO (Freiheitsstrafe bis 3 Jahre)
- Persoenliche Haftung nach § 15b InsO fuer alle Zahlungen nach Insolvenzreife
- Schadensersatzhaftung gegenueber Glaeubigern

Ich empfehle die sofortige Stellung des Insolvenzantrags, idealerweise mit Antrag auf
[Eigenverwaltung / Schutzschirm / Regelverfahren].

Bitte bestaetigen Sie schriftlich, dass Sie diesen Hinweis erhalten haben.

[UNTERSCHRIFT ANWALT]
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Durchsetzung des Anspruchs / Vergleich / Reputationsschutz / schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestforderung / Zeitrahmen / Formerfordernis]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgesprach / Einigung vor Fristablauf]

Schlussabsatz Variante A (kooperativ):
Wir regen eine guetliche Einigung an und stehen fuer ein klaerenden Gesprach zur Verfuegung. Eine einvernehmliche Loesung erspart beiden Seiten Zeit und Kosten.

Schlussabsatz Variante B (formal-streng):
Eine aussergerichtliche Einigung kommt nur in Betracht wenn die Gegenseite innerhalb von [X] Tagen einen akzeptablen Vorschlag unterbreitet. Anderenfalls werden wir alle rechtlichen Schritte einleiten.

<!-- AUDIT Mai 2026 — Update Bundle 034 —
 Update aufgenommen: BGH II ZR 206/22 (23.07.2024) fortwirkende Haftung ausgeschiedener GF,
 BGH 5 StR 287/24 (27.02.2025) faktischer GF,
 BGH IV ZR 66/25 (19.11.2025) D&O-Wissentlichkeit.
 Rechtsprechung weiterhin live prüfen: dejure.org, openjur.de, bundesgerichtshof.de.
-->

## 3. `auslaendischer-insolvenzverwalter-register-und-grundbuch`

**Fokus:** Register- und Grundbuchvollzug bei ausländischer Insolvenz: GmbH-Anteile, Gesellschafterliste, Handelsregister, Grundbuch, Notar, § 29 GBO, § 346 InsO und Nachweis der Rechtsmacht ausländischer office holder.

# Ausländischer Insolvenzverwalter — Register und Grundbuch

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Ausländischer Insolvenzverwalter — Register und Grundbuch` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Aufgabe

Dieser Skill macht aus einer grenzüberschreitenden Insolvenz einen deutschen Vollzugspfad. Er hilft, wenn ein ausländischer trustee, debtor in possession, monitor, receiver, liquidator oder administrator in Deutschland GmbH-Anteile, Grundstücke, Konten, Forderungen oder Registerpositionen bewegen will.

## Schnellweichen

1. **Asset gehört wem?**
 - deutsches Grundstück des ausländischen Schuldners;
 - GmbH-Anteile des ausländischen Schuldners an einer deutschen GmbH;
 - Vermögen der deutschen Tochtergesellschaft selbst;
 - Forderung/Bankkonto/IP-Recht des ausländischen Schuldners;
 - streitige Zuordnung im Konzern.
2. **Welche deutsche Form?**
 - GmbH-Anteil: § 15 Abs. 3/4 GmbHG, notarielle Form;
 - neue Gesellschafterliste: § 40 GmbHG, notarielle Einreichungslogik;
 - Grundstück: §§ 873, 925 BGB, § 311b BGB, Grundbuchverfahren;
 - Grundbuchnachweis: § 29 GBO;
 - Insolvenzvermerk bei ausländischem Verfahren: § 346 InsO.
3. **Welche ausländische Befugnis?**
 - Verfahrenseröffnung, office holder appointment, debtor-in-possession status;
 - Einschränkungen durch stay, plan, court approval, creditor consent;
 - Befugnis gerade zur Verfügung über dieses Asset.

## GmbH-Anteile und Gesellschafterliste

Prüfe in dieser Reihenfolge:

1. **Anteilseigentum:** Ist der ausländische Schuldner in der aktuellen Gesellschafterliste als Gesellschafter eingetragen oder gibt es eine abweichende Treuhand-/Nominee-/Verpfändungslage?
2. **Ausländische Verfahrenswirkung:** Hat der office holder nach dem Insolvenzstatut die Befugnis, Anteile zu veräußern oder Gesellschafterrechte auszuüben?
3. **Deutsche Form:** Abtretung von GmbH-Anteilen notariell beurkunden; die Anerkennung des ausländischen Verfahrens ersetzt § 15 GmbHG nicht.
4. **Gesellschafterliste:** Der Notar reicht die geänderte Liste ein; das Registergericht prüft nicht wirtschaftlich wie ein Prozessgericht, aber formale Plausibilität und Einreichungsbefugnis müssen passen.
5. **Deutsche Tochter bleibt getrennt:** Ist die deutsche GmbH selbst nicht Schuldnerin, kann der ausländische office holder nicht unmittelbar deren Grundstücke, Konten oder Forderungen verkaufen. Er kann nur über die Gesellschafterposition einwirken, soweit Gesellschaftsrecht und Satzung das zulassen.

## Grundstücke und Grundbuch

Prüfe in dieser Reihenfolge:

1. **Sachenrechtliche Form:** Auflassung und Eintragung nach deutschem Recht; bei Kaufvertrag zusätzlich § 311b BGB.
2. **Nachweis:** § 29 GBO verlangt öffentliche oder öffentlich beglaubigte Urkunden; fremdrechtliche Rechtsmacht muss grundbuchtauglich belegt werden.
3. **Insolvenzvermerk:** § 346 InsO ermöglicht bei anerkanntem ausländischem Verfahren ein Ersuchen des Insolvenzgerichts an das Grundbuchamt zur Eintragung der Verfahrenseröffnung und Art der Verfügungsbeschränkung. Der Antrag setzt Glaubhaftmachung der Anerkennungsvoraussetzungen voraus.
4. **Zuständigkeit:** § 348 InsO für Entscheidungen nach §§ 344 bis 346 InsO: Insolvenzgericht am Niederlassungs- oder Vermögensort.
5. **Praktischer Engpass:** Das Grundbuchamt wird keinen wirtschaftlichen Deal retten; wenn Urkundenkette, Übersetzung, Apostille/Legalisation oder Befugnis nicht grundbuchtauglich sind, bleibt der Vollzug hängen.

## Dokumentenmatrix für Notar und Register

| Dokument | Zweck | Risiko |
| --- | --- | --- |
| Eröffnungsentscheidung / order for relief / appointment order | Belegt Verfahren und Amt | unklare Zuständigkeit, fehlende Beglaubigung |
| Certificate der zuständigen Stelle | Nachweis der Stellung | nicht passend zur konkreten Transaktion |
| Foreign-law memo | erklärt Befugnis und Grenzen | bloße Parteibehauptung genügt oft nicht |
| Court approval / sale order | sichert außergewöhnliche Verfügung | fehlt bei non-ordinary-course transaction |
| Übersetzung | Verständlichkeit für deutsche Stelle | unbeglaubigt oder unvollständig |
| Apostille/Legalisation | Echtheitskette | je nach Staat/Urkunde/Treaty prüfen |
| Deutsche Vollmacht | Notar-/Registervollzug | Vollmachtgeber selbst unklar legitimiert |

## Formulierung für eine Vollzugsnotiz

> Die handelnde Person stützt ihre Vertretungs- und Verfügungsbefugnis nicht auf eine deutsche Bestellung, sondern auf die Wirkungen des ausländischen Insolvenzverfahrens. Für Deutschland ist deshalb zuerst die Anerkennung nach §§ 335 ff., 343 InsO zu prüfen. Sodann ist getrennt zu prüfen, ob die konkrete Handlung nach dem ausländischen Insolvenzstatut gedeckt und nach deutschem Form-, Register- und Sachenrecht vollziehbar ist.

## Output

- Register-/Grundbuch-Checkliste;
- Dokumentenanforderung an ausländische counsel;
- Notarvermerk;
- Anschreiben an Registergericht/Grundbuchamt;
- Risikoampel für Vollzug heute, Nachlieferung, gerichtlichen Antrag oder Deal-Stopp.

## Quellenregel

Tragende Normen live prüfen: InsO §§ 335, 343, 346 bis 348, GBO § 29, GmbHG §§ 15, 40, BGB §§ 873, 925, 311b. Rechtsprechung nur verifiziert mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.

## 4. `forderungsanmeldung-glaeubiger-174-177-inso`

**Fokus:** Gläubiger meldet Forderung im Insolvenzverfahren an §§ 174-177 InsO: Fristen Form Anlagen Rang § 39 InsO Vorsatz § 174 Abs. 2 InsO nachtraegliche Anmeldung § 177 InsO Prüfungstermin § 176 Bestreiten § 178 Tabelle § 179 InsO. Mit Mustertexten und Fehlerkatalog.

# Forderungsanmeldung im Insolvenzverfahren — Gläubiger-Sicht (§§ 174-177 InsO)

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Forderungsanmeldung im Insolvenzverfahren — Gläubiger-Sicht (§§ 174-177 InsO)` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Zweck

Sobald das Insolvenzverfahren über das Vermögen des Schuldners eröffnet ist, müssen Insolvenzgläubiger ihre Forderungen beim Insolvenzverwalter zur Tabelle anmelden. Erst durch die Anmeldung wird die Forderung Teil der Verteilung. Dieser Skill führt Schritt für Schritt durch Form, Frist, Inhalt, Rangfragen, Besonderheiten (vorsätzliche unerlaubte Handlung, nachträgliche Anmeldung) und Reaktionsmöglichkeiten im Prüfungstermin.

---

## PFLICHT-DISCLAIMER

**Keine Rechtsberatung. Mechanischer Workflow.** Konkrete Anmeldung ist im Einzelfall mit Fachanwalt für Insolvenzrecht abzustimmen.

---

## Teil A — Vor-Frage: Bin ich überhaupt Insolvenzgläubiger?

Nicht jeder Anspruch gehört in die Tabelle. Erst klären, **welcher Forderungstyp** vorliegt:

| Forderungstyp | Anmeldung zur Tabelle? | Rechtsgrundlage |
|---|---|---|
| **Insolvenzforderung** (Anspruch entstanden vor Eröffnung) | ja, §§ 174 ff. InsO | § 38 InsO |
| **Nachrangige Insolvenzforderung** (Zinsen ab Eröffnung, Geldbußen, Schenkungsversprechen, Gesellschafterdarlehen) | ja, aber nur auf besondere Aufforderung des Gerichts | § 174 Abs. 3, § 39 InsO |
| **Massegläubiger** (Anspruch aus der Verwaltung der Masse, vom Verwalter begründet) | **nein**, direkt vom Verwalter zu zahlen | §§ 53, 55 InsO |
| **Aussonderungsberechtigter** (Eigentum am Gegenstand) | **nein**, Herausgabeanspruch direkt | § 47 InsO |
| **Absonderungsberechtigter** (Sicherungsrecht an Massegegenstand) | nur Ausfall anmelden | §§ 49-52, 190-191 InsO |
| **Aufrechnungsberechtigter** | keine Anmeldung erforderlich, Aufrechnung kraft Gesetzes | §§ 94-96 InsO |
| **Unterhalts-/Familienforderungen** (laufender Unterhalt nach Eröffnung) | nein, kein Insolvenzanspruch | § 40 InsO |

**Faustregel:** Anmeldung nur bei Insolvenzforderung (§ 38 InsO) und nachrangiger Insolvenzforderung (§ 39 InsO). Bei gemischter Forderung (z.B. Insolvenz- und Massebestandteil) getrennt geltend machen.

→ Querverweis: `mandat-triage-insolvenzrecht`, `insolvenzrecht-kaltstart-interview`.

---

## Teil B — Anmeldefrist

### B.1 Reguläre Anmeldefrist (§ 28 Abs. 1, § 174 Abs. 1 InsO)

- Das **Insolvenzgericht** setzt im Eröffnungsbeschluss eine Frist zur Anmeldung.
- Frist: regelmäßig zwischen **zwei Wochen und drei Monaten** ab Eröffnung.
- Die Frist ist im Eröffnungsbeschluss konkret benannt und im Bundesanzeiger und auf `www.insolvenzbekanntmachungen.de` veröffentlicht.
- Wirkung der Frist: keine **Ausschlussfrist** im engen Sinn, aber Anmeldungen danach lösen Mehrkosten aus (§ 177 InsO) und können vom Prüfungstermin ausgenommen werden.

### B.2 Verspätete Anmeldung — § 177 InsO

| Konstellation | Folge |
|---|---|
| Anmeldung nach Ablauf der Frist, vor Prüfungstermin | wird im Prüfungstermin geprüft, Mehrkosten Gläubiger |
| Anmeldung nach Prüfungstermin | besonderer Prüfungstermin auf Antrag, Kosten gemäß § 177 Abs. 3 InsO |
| Anmeldung nach Schlusstermin (§ 197 InsO) | grundsätzlich ausgeschlossen, nur noch über Nachtragsverteilung § 203 InsO |
| Anmeldung nach Aufhebung des Verfahrens | nicht mehr möglich |

**Faustregel:** Anmeldung so früh wie möglich, jedenfalls vor dem allgemeinen Prüfungstermin.

### B.3 Fristbeginn und Fristberechnung

- Fristbeginn: Tag nach Eröffnung (§ 187 BGB).
- Fristberechnung nach §§ 187-193 BGB.
- Auch elektronische Anmeldung möglich (§ 14 Abs. 4 InsO i.V.m. ERVV).

---

## Teil C — Form und Inhalt der Anmeldung

### C.1 Formal — § 174 Abs. 1, 4 InsO

- **schriftlich** oder elektronisch beim **Insolvenzverwalter** (nicht beim Gericht!)
- in zweifacher Ausfertigung
- Angabe des Aktenzeichens des Verfahrens
- klare Forderungsbezeichnung

### C.2 Pflichtangaben — § 174 Abs. 2 InsO

| Angabe | Inhalt |
|---|---|
| Gläubiger | Name, Anschrift, Bankverbindung, Vertretung (falls Anwalt) |
| Schuldner | Name, Anschrift, Insolvenz-Aktenzeichen |
| Forderungssumme | Hauptforderung in Euro |
| Forderungsgrund | Sachverhalt, der den Anspruch trägt — knapp aber identifizierbar |
| Rechtsgrundlage | konkrete Anspruchsnormen (z.B. § 433 Abs. 2 BGB; § 280 Abs. 1 BGB; § 631 Abs. 1 BGB) |
| Belege | Anlagen-Konvolut (Vertrag, Rechnung, Mahnungen, Vollstreckungstitel, Korrespondenz) |
| Zinsen | nur bis zum Tag der Eröffnung (danach § 39 Abs. 1 Nr. 1 InsO nachrangig) |
| Kosten | nur vor Eröffnung entstandene Kosten (Mahnkosten, Anwaltskosten, Gerichtskosten) |
| Rang | wenn nachrangig: ausdrücklich § 39 InsO benennen |
| Aussonderungs-/Absonderungsrechte | falls gleichzeitig bestehend, Hinweis zur Information |

### C.3 Besondere Pflichtangabe — Vorsatz § 174 Abs. 2 InsO

**Wichtig:** Wenn die Forderung aus einer **vorsätzlich begangenen unerlaubten Handlung** stammt (§ 823 ff. BGB i.V.m. § 826 BGB) oder aus einer vorsätzlich pflichtwidrig nicht gewährten gesetzlichen Unterhaltszahlung oder einer im Zusammenhang mit Steuerhinterziehung pflichtwidrig nicht gezahlten Steuer (§ 174 Abs. 2 InsO):

- **ausdrücklich** unter Angabe des Tatbestands anmelden
- Bedeutung: solche Forderungen sind von der **Restschuldbefreiung ausgeschlossen** (§ 302 Nr. 1 InsO) — Gläubiger kann nach Beendigung des Insolvenzverfahrens weiter vollstrecken
- Anforderungen an die Individualisierung (Sachverhaltsdarstellung, keine schlüssige Rechtsbegründung erforderlich): vgl. **BGH IX ZR 114/23 vom 19.12.2024** zur Anmeldung abgetretener Forderungen.
 Quelle: <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=19.12.2024&Aktenzeichen=IX+ZR+114/23>

Beispiele Vorsatz-Forderungen:
- Schadensersatz aus Betrug (§ 263 StGB), Untreue (§ 266 StGB), Unterschlagung (§ 246 StGB)
- vorsätzliche Körperverletzung (§ 223 StGB) mit Schmerzensgeld-Anspruch
- Schadensersatz aus vorsätzlich falscher Bilanz (§ 331 HGB)
- Schadensersatz aus Steuerhinterziehung des Geschäftsführers (§ 71 AO)
- vorsätzlich nicht gezahlter Kindesunterhalt (§ 1601 BGB i.V.m. § 170 StGB)

→ Querverweis: `vorsatzanfechtung-133-inso` (verwandte Norm).

### C.4 Belege und Anlagen

- in Kopie, geordnet, durchnummeriert
- nicht im Original (Verlust-Risiko)
- besonders wichtig: **rechtskräftige Titel** (Urteil, Vollstreckungsbescheid, Vergleich, notarielle Urkunde)
- bei Mahnungen: Beweis des Zugangs sichern

### C.5 Anmeldung mit Anwaltsvertretung

- Verfahrensbevollmächtigter ist anzugeben
- Vollmacht in Kopie beilegen
- Zustellungen erfolgen an den Anwalt

---

## Teil D — Sondersituationen

### D.1 Gesicherte Forderung mit Absonderungsrecht (§§ 49-52 InsO)

Wer eine gesicherte Forderung hat (Pfand, Hypothek, Sicherungsübereignung), darf den **Ausfall** anmelden — also den Teil der Forderung, der nicht durch die Sicherheit gedeckt ist.

**Vorgehen:**
1. Anmeldung der vollen Forderung beim Verwalter mit Hinweis auf Sicherungsrecht
2. Sicherheit verwerten (§§ 165-173 InsO)
3. nach Verwertung Mitteilung an Verwalter, welcher Betrag durch Verwertung gedeckt ist
4. **Ausfall** wird in der Tabelle festgestellt

**Achtung:** Frist zur Mitteilung des Ausfalls in § 190 Abs. 2 InsO (drei Wochen nach Schlussverteilungsterminbestimmung).

→ Querverweis (Plugin `insolvenzplan-starug-planwerkstatt`): `ips-sicherheiten-drittsicherheiten`.

### D.2 Bedingte oder noch nicht fällige Forderung — § 191 InsO

- bedingt: Anmeldung möglich, Berücksichtigung nur bei Eintritt
- nicht fällig: Anmeldung in voller Höhe, Auswirkung auf Verteilung erst bei Fälligkeit
- aufschiebend befristet: Anmeldung mit Hinweis auf Befristung

### D.3 Wechselkursforderung / Auslandsforderung — § 45 InsO

- Umrechnung in Euro **zum Stichtag der Eröffnung**
- amtlicher Kurs der Europäischen Zentralbank
- bei Forderung in Drittland-Währung: Beleg über Wechselkurs am Eröffnungstag

### D.4 Solidargesamtgläubiger und Gesamtschuldner-Konstellationen — § 43 InsO

- jeder Gläubiger meldet seine eigene Forderung an
- bei Bürgschaft: Hauptgläubiger meldet, Bürge ggf. mit eigenem Regress-Anspruch nach Zahlung (§ 774 BGB)
- bei Gesamtschuld auf Schuldnerseite: gegen jeden Gesamtschuldner gesondert anmelden, Doppel-Erlangung mindert (§ 422 BGB)

### D.5 Arbeitnehmer-Forderungen

- Arbeitnehmer mit Lohnansprüchen **vor** Eröffnung: Insolvenzgläubiger, aber **Insolvenzgeld** für die letzten drei Monate vor Eröffnung über die Bundesagentur für Arbeit (§ 165 SGB III)
- Anmeldung nur, soweit Insolvenzgeld nicht greift oder darüber hinausgehend
- → Querverweis: `insolvenzgeld-165-sgb-iii`.

### D.6 Steuer- und Sozialversicherungsforderungen

- Finanzamt und Sozialversicherungsträger melden eigenständig an
- bei Geschäftsführer-Haftungsbescheiden: getrennt anmelden, ggf. mit Vorsatz-Hinweis (Steuerhinterziehung)

### D.7 Forderungen aus Dauerschuldverhältnissen

- Anteil bis Eröffnung: Insolvenzforderung
- Anteil nach Eröffnung: Masseverbindlichkeit (§ 55 InsO), falls Verwalter wählt Erfüllung (§ 103 InsO), sonst Nichterfüllungsschaden als Insolvenzforderung (§ 103 Abs. 2 InsO)

### D.8 Forderung gegen Gesellschafter aus Gesellschafterdarlehen

- nachrangig (§ 39 Abs. 1 Nr. 5 InsO)
- Anmeldung nur auf besondere Aufforderung des Gerichts
- Achtung: bei Sanierungsdarlehen Privileg § 39 Abs. 4 InsO prüfen

---

## Teil E — Prüfungstermin (§§ 176-178 InsO)

### E.1 Was passiert im Prüfungstermin

- öffentliche Sitzung des Insolvenzgerichts
- Verwalter prüft jede angemeldete Forderung nach Grund, Höhe und Rang
- Schuldner kann jeder Forderung widersprechen
- Insolvenzgläubiger können jeder Forderung widersprechen

### E.2 Mögliche Ergebnisse

| Status | Wirkung |
|---|---|
| **Festgestellt** (kein Widerspruch) | Forderung wirkt wie rechtskräftiges Urteil (§ 178 Abs. 3 InsO) |
| **Bestritten Verwalter** | Gläubiger muss Klage erheben § 179 InsO |
| **Bestritten Schuldner** | Forderung dennoch festgestellt, aber kein Vollstreckungstitel gegen Schuldner nach Verfahrensaufhebung (§ 201 InsO) |
| **Bestritten Mit-Gläubiger** | Gläubiger muss Klage erheben § 179 InsO |
| **Vorsatz-Charakter bestritten** | Klage auf Feststellung Vorsatz § 184 InsO |

### E.3 Reaktion auf Bestreitung

- Klage auf **Feststellung zur Tabelle** beim Prozessgericht (nicht Insolvenzgericht!)
- Antragsfassung: "es wird festgestellt, dass die unter lfd. Nr. X zur Tabelle angemeldete Forderung in Höhe von ... Euro besteht"
- Gerichtsstand: Sitz des Schuldners oder allgemeiner Gerichtsstand
- Bei Vorsatz: separate Klage auf Feststellung des Vorsatz-Charakters § 184 InsO

**Frist:** keine gesetzliche Klagefrist, aber Verzögerung führt zu Nicht-Berücksichtigung in Verteilung — daher zügig.

→ Querverweis: `glaeubigerausschuss-mitwirkung` (falls Gläubiger im Ausschuss).

---

## Teil F — Nachträgliche Schritte

### F.1 Nachtragsverteilung (§ 203 InsO)

Wenn nach Schlusstermin (§ 197 InsO) noch Masse oder Forderungen auftauchen:
- Antrag auf Nachtragsverteilung beim Gericht
- nachträglich angemeldete Forderungen werden quotal befriedigt

### F.2 Restschuldbefreiungsverfahren beachten

- Schuldnerantrag auf Restschuldbefreiung läuft parallel
- Vorsatz-Forderungen mit ausdrücklicher Anmeldung sind von Restschuldbefreiung ausgeschlossen (§ 302 Nr. 1 InsO)
- Anfechtungsmöglichkeiten gegen Restschuldbefreiung (§§ 290, 296, 297 InsO) zeitlich beachten

### F.3 Anfechtungsforderungen des Verwalters

- separater Vorgang
- führt bei Erfolg zu Massezufluss, der quotal verteilt wird
- Gläubiger profitieren mittelbar

→ Querverweis: `anfechtungsrechte-pruefen`, `vorsatzanfechtung-133-inso`.

---

## Teil G — Muster

### G.1 Anmeldeschreiben (verkürzt)

> **An den Insolvenzverwalter**
> [Name und Adresse Verwalter]
>
> **Insolvenzverfahren über das Vermögen [Schuldner], AZ: [Aktenzeichen Insolvenzgericht]**
>
> **Forderungsanmeldung gemäß § 174 InsO**
>
> Sehr geehrte Damen und Herren,
>
> namens und in Vollmacht der [Gläubigerin], [Anschrift], melden wir zur Insolvenztabelle folgende Forderung an:
>
> **Hauptforderung:** [Betrag in Euro]
> **Zinsen bis Eröffnung am [Datum]:** [Betrag] (auf Hauptforderung in Höhe von [Betrag] vom [Beginn] bis [Eröffnung] zu [Zinssatz] % p.a.)
> **Vorgerichtliche Kosten:** [Betrag] (Mahnkosten, vorgerichtliche Anwaltskosten 1,3 RVG)
> **Gerichtskosten Mahnverfahren:** [Betrag]
> **Vollstreckungskosten:** [Betrag]
>
> **Gesamt:** [Summe]
>
> **Forderungsgrund:** [knappe Sachverhaltsdarstellung — z.B. "Kaufpreisanspruch aus Lieferung von Maschinenkomponenten gemäß Auftragsbestätigung Nr. 2025/0815 vom 14.3.2025, Rechnung Nr. 2025-0432 vom 28.3.2025, fällig zum 27.4.2025. Mahnung 15.5.2025; gerichtlicher Mahnbescheid vom 8.7.2025, AZ ...; Vollstreckungsbescheid vom 22.7.2025."]
>
> **Rechtsgrundlage:** § 433 Abs. 2 BGB; Zinsen § 286 Abs. 3 BGB i.V.m. § 288 Abs. 2 BGB; Kosten § 286 BGB.
>
> **Rang:** allgemeine Insolvenzforderung (§ 38 InsO).
>
> **Anlagenkonvolut** (Anlagen K1-K8): [Liste].
>
> **Bankverbindung für Verteilungen:** IBAN ..., BIC ...
>
> Mit freundlichen Grüßen
> [Anwalt]

### G.2 Anmeldeschreiben Vorsatz-Forderung (verkürzt)

> [...]
>
> **Forderungsgrund:** Schadensersatzanspruch aus **vorsätzlich begangener unerlaubter Handlung** des Schuldners. Der Schuldner hat als Geschäftsführer der [...] GmbH im Zeitraum [...] vorsätzlich Gelder der Mandantin zweckwidrig auf ein eigenes Konto überwiesen (siehe rechtskräftiges Urteil LG ..., AZ ..., Anlage K1, sowie Strafurteil AG ..., AZ ..., Anlage K2 — Verurteilung wegen Untreue § 266 StGB).
>
> **Rechtsgrundlage:** §§ 826, 31 BGB; § 823 Abs. 2 BGB i.V.m. § 266 StGB.
>
> **Ausdrücklicher Hinweis nach § 174 Abs. 2 InsO:** Die Forderung resultiert aus einer **vorsätzlich begangenen unerlaubten Handlung**. Im Falle der Restschuldbefreiung des Schuldners ist die Forderung gemäß § 302 Nr. 1 InsO von der Restschuldbefreiung ausgenommen.
>
> **Rang:** § 38 InsO. [...]

---

## Teil H — Häufige Fehlerquellen (Checkliste)

| Fehler | Folge | Abhilfe |
|---|---|---|
| Anmeldung beim Insolvenzgericht statt Verwalter | nicht fristwahrend | Verwalter-Adresse aus Eröffnungsbeschluss übernehmen |
| Frist versäumt | Mehrkosten, Verzögerung | so früh wie möglich anmelden |
| Vorsatz-Charakter nicht ausdrücklich benannt | Privileg § 302 Nr. 1 InsO verloren | im Anmeldeschreiben prominent unter eigener Überschrift hinweisen |
| Zinsen über Eröffnung hinaus angemeldet | als nachrangig zurückgestuft | klar bis Eröffnungstag berechnen |
| Anwaltskosten nach Eröffnung mit angemeldet | nachrangig | nur vor Eröffnung |
| keine Belege beigelegt | bestritten im Prüfungstermin | Anlagenkonvolut sauber zusammenstellen |
| Original-Vollstreckungstitel verschickt | Verlust-Risiko | nur Kopie, Original behalten |
| keine Aussagen zu Sicherheiten | Doppel-Erlangung droht | Sicherheiten offenlegen und nur Ausfall geltend machen |
| Auslandswährung nicht umgerechnet | Verzögerung | EZB-Kurs Eröffnungstag verwenden |
| Gesellschafterdarlehen ohne Hinweis auf § 39 Abs. 4 angemeldet | Privileg-Verlust | Sanierungsprivileg prüfen |
| Bestreitung nicht beachtet | Tabellen-Eintragung scheitert | Klage § 179 InsO innerhalb angemessener Frist |
| Klage beim Insolvenzgericht eingereicht | unzuständig | Klage beim regulären Prozessgericht |
| Bankverbindung vergessen | Verteilungen kommen nicht an | IBAN/BIC im Anmeldeschreiben |
| Anmeldung ohne Aktenzeichen | Verwechslung | Aktenzeichen prominent im Briefkopf |

---

## Querverweise

Innerhalb des `insolvenzrecht`-Plugins:

- `mandat-triage-insolvenzrecht` — Eingangstriage
- `insolvenzrecht-kaltstart-interview` — Sachverhaltsaufnahme
- `anfechtungsrechte-pruefen` — Anfechtungsschiene
- `vorsatzanfechtung-133-inso` — verwandte Norm
- `glaeubigerantrag-pruefung` — Antragstellung des Gläubigers
- `glaeubigerausschuss-mitwirkung` — Mitwirkung im Ausschuss
- `insolvenzgeld-165-sgb-iii` — Arbeitnehmer-Sonderschiene
- `uebertragende-sanierung-und-asset-deals` — Plan-/Verfahrenswahl

Verwandte Plugins:

- `insolvenzforderungsanmeldungspruefung` — Verwalter-Prüfung im Detail
- `insolvenzverwaltung/iv-forderungsanmeldung-pruefung` — Verwalter-Workflow
- `insolvenzverwaltung/iv-tabelle-pruefungstermin` — Tabellen-Mechanik

---

## Mini-Checkliste vor Versand der Anmeldung

- [ ] Forderungstyp geklärt (Insolvenz § 38 / nachrangig § 39 / Masse § 53)
- [ ] Anmeldefrist im Eröffnungsbeschluss notiert
- [ ] Anmeldung an Verwalter (nicht Gericht!) adressiert
- [ ] Hauptforderung, Zinsen bis Eröffnung, vorgerichtliche Kosten getrennt ausgewiesen
- [ ] Rechtsgrundlage konkret benannt
- [ ] Forderungsgrund knapp aber identifizierbar dargestellt
- [ ] Bei Vorsatz: ausdrücklicher Hinweis nach § 174 Abs. 2 InsO mit Tatbestand
- [ ] Anlagenkonvolut beigefügt und durchnummeriert
- [ ] Sicherungsrechte offengelegt (Aussonderung/Absonderung)
- [ ] Wechselkurs zum Eröffnungstag (falls Auslandswährung)
- [ ] Vollmacht beigefügt
- [ ] Bankverbindung angegeben
- [ ] Zweifache Ausfertigung
- [ ] Eingangsbestätigung erbitten
- [ ] Termin Prüfungstermin notiert

---

Hinweis: Keine Rechtsberatung. Mechanische Strukturhilfe für Forderungsanmeldung im Insolvenzverfahren. Konkrete Anmeldung im Einzelfall mit Fachanwalt für Insolvenzrecht abstimmen.

## Weitere Leitentscheidungen — Forderungsanmeldung

- **BGH IX ZR 114/23 vom 19.12.2024** — Anforderungen an die Individualisierung der Forderungsanmeldung; bei Abtretung muss Zedent und Zessionar die abgetretene Forderung jeweils gesondert anmelden und prüfen lassen.
 <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=19.12.2024&Aktenzeichen=IX+ZR+114/23>
- **BGH IX ZR 127/24 vom 13.11.2025** (Wirecard) — Kapitalmarktrechtliche Schadensersatzforderungen geschädigter Aktionäre sind in der Insolvenz der Aktiengesellschaft *keine* einfachen Insolvenzforderungen iSd § 38 InsO; sie treten hinter die einfachen Insolvenzgläubiger zurück. Bedeutung: bei Anmeldung solcher Forderungen ausdrücklich die Rangfrage adressieren.
 Quelle: Bundesgerichtshof Pressemitteilung 2025/211; <https://www.lto.de/recht/kanzleien-unternehmen/k/bgh-ixzr12724-wirecard-insolvenzmasse-forderungen-aktionaere-urteil>
- Ältere Leitentscheidungen zur Individualisierung und Vorsatzanmeldung über dejure.org/openjur.de verifizieren.

---

<!-- AUDIT 27.05.2026 -->
## Audit-Hinweis (27.05.2026)
