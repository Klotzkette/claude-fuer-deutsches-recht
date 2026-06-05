---
name: db-agb-auskunft-rechnungslegung
description: "Db Datenbankrecht Agb Klauseln / Db Auskunft Rechnungslegung Schadensschaetzung / Db Datenqualitaet Haftung Gewaehrleistung: führt durch diese fachlich verbundenen Arbeitsmodule, wählt den passenden Prüfpfad und erzeugt den nächsten belastbaren Output."
---

# Db Datenbankrecht Agb Klauseln / Db Auskunft Rechnungslegung Schadensschaetzung / Db Datenqualitaet Haftung Gewaehrleistung

## Arbeitsbereich

Dieser Skill bündelt **Db Datenbankrecht Agb Klauseln / Db Auskunft Rechnungslegung Schadensschaetzung / Db Datenqualitaet Haftung Gewaehrleistung**. Wähle zuerst das Modul, dessen Tatsachen die Akte tragen; kombiniere weitere Module nur, wenn dieselbe Frist, Zuständigkeit, Beweislast oder derselbe Output dadurch wirklich klarer wird.

## Arbeitsmodule

| Arbeitsmodul | Fokus |
| --- | --- |
| `db-042-datenbankrecht-in-agb-klauseln` | Gestaltung und Prüfung datenbankrechtsrelevanter AGB-Klauseln: § 307 BGB-Inhaltskontrolle für Nutzungsverbote, Scraping-Verbote, Datenbankrechts-Zuweisung, Haftungsausschlüsse und TDM-Opt-out-Klauseln. Analysiert Wirksamkeit von Standardklauseln gegenüber Verbrauchern und B2B-Kunden sowie Schranken nach §§ 87c 44b UrhG. Erstellt AGB-Muster für Datenbankbetreiber. |
| `db-029-auskunft-rechnungslegung-schadensschaetzung` | Auskunft, Rechnungslegung und Schadensschätzung im Datenbankrecht nach §§ 97 101 UrhG: Dreigliedrige Schadensberechnung (konkreter Schaden, Herausgabe Verletzergewinn, Lizenzanalogie), Auskunftsanspruch gegen Verletzer und ISP, Rechnungslegungsvollstreckung sowie Besonderheiten bei Datenbankschutz nach §§ 87a-87e UrhG. Erstellt Schadensberechnung und Klageanträge. |
| `db-041-datenqualitaet-haftung-und-gewaehrleistung` | Haftung und Gewährleistung für Datenbankqualität: §§ 434 437 BGB Sachmängelhaftung bei fehlerhaften Datenbankdaten, Deliktshaftung (§ 823 BGB) bei falschen Einträgen, DSGVO-Berichtigungspflichten (Art. 16 DSGVO) und vertragliche Haftungsbegrenzungen. Bewertet Schadensersatzansprüche bei Falschauskunft aus Datenbanken und Disclaimer-Klauseln. |

## Arbeitsweg

Für **Db Datenbankrecht Agb Klauseln / Db Auskunft Rechnungslegung Schadensschaetzung / Db Datenqualitaet Haftung Gewaehrleistung** zuerst das Arbeitsmodul wählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `datenbankrecht` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; Module nur kombinieren, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Arbeitsmodule im Detail

## 1. `db-042-datenbankrecht-in-agb-klauseln`

**Fokus:** Gestaltung und Prüfung datenbankrechtsrelevanter AGB-Klauseln: § 307 BGB-Inhaltskontrolle für Nutzungsverbote, Scraping-Verbote, Datenbankrechts-Zuweisung, Haftungsausschlüsse und TDM-Opt-out-Klauseln. Analysiert Wirksamkeit von Standardklauseln gegenüber Verbrauchern und B2B-Kunden sowie Schranken nach §§ 87c 44b UrhG. Erstellt AGB-Muster für Datenbankbetreiber.

# Datenbankrecht in AGB-Klauseln — Inhaltskontrolle und Gestaltung

## Mandantenfall

- Datenbankbetreiber überarbeitet seine AGB und will datenbankrechtsrelevante Klauseln (Nutzungsverbote, Scraping-Verbot, TDM-Opt-out) rechtssicher formulieren.
- Anwalt soll bestehende AGB eines SaaS-Anbieters auf unwirksame Klauseln prüfen, die alle Datenbankrechte auf den Anbieter übertragen.
- Startup hat eine Abmahnung erhalten, weil seine AGB keine ausreichenden Scraping-Verbote enthalten, und muss sie überarbeiten.

## Erste Schritte

1. AGB-Anwendungsbereich bestimmen: Handelt es sich um B2C oder B2B-Verhältnis? Unterschiedliche Prüfmaßstäbe nach §§ 307-309 BGB vs. § 310 BGB.
2. Inhaltskontrolle nach § 307 BGB: Sind die Klauseln transparent (Verständlichkeitsgebot), klar und nicht unangemessen benachteiligend?
3. Scraping-Verbot-Klausel prüfen: Hinreichend bestimmt (welche automatisierten Zugriffe sind verboten?), verhältnismäßige Rechtsfolgen (Kündigung, Schadensersatz)?
4. TDM-Opt-out in AGB bewerten: Maschinenlesbarkeit nach § 44b Abs. 3 UrhG — AGB-Text allein reicht nicht; zusätzliche technische Erklärung erforderlich.
5. Datenbankrechts-Zuweisungsklausel prüfen: Überträgt die Klausel Herstellerrecht oder Nutzungsrechte an Kundendaten auf den Betreiber — § 307 BGB-Konformität?
6. Haftungsausschlussklausel gestalten: § 309 Nr. 7 BGB — Ausschluss für Vorsatz und grobe Fahrlässigkeit unzulässig; differenzierte Haftungsbegrenzung erforderlich.

## Rechtsrahmen

- § 307 BGB: Inhaltskontrolle — Klausel unwirksam bei unangemessener Benachteiligung oder fehlender Transparenz.
- § 308 BGB: Klauselverbote mit Wertungsmöglichkeit — z. B. einseitige Änderungsvorbehalte.
- § 309 BGB: Klauselverbote ohne Wertungsmöglichkeit — Haftungsausschlüsse, Abtretungsverbote.
- § 87c UrhG: Zwingende gesetzliche Schranken — vertraglich nicht ausschließbar für rechtmäßige Nutzer.
- § 44b UrhG: TDM-Schranke — kommerzielles TDM kann durch AGB (mit technischem Opt-out) ausgeschlossen werden; wissenschaftliches nicht.
- § 87b UrhG: Verbotener Handlungsrahmen — AGB können Nutzung über das gesetzliche Verbot hinaus einschränken, müssen aber § 307 BGB standhalten.

## Prüfraster

- Sind alle datenbankrechtsrelevanten Verbote (Entnahme, Scraping, Weiterverwendung) in den AGB klar und abschließend formuliert?
- Ist das Scraping-Verbot hinreichend bestimmt — welche Arten automatisierten Zugriffs sind erfasst und welche Rechtsfolgen gelten?
- Hält die TDM-Opt-out-Klausel den Anforderungen des § 44b Abs. 3 UrhG stand (maschinenlesbar + separat technisch erklärt)?
- Sind Klauseln, die Datenbankherstellerrecht auf den Anbieter übertragen, nach § 307 BGB angemessen und transparent?
- Greifen zwingende Schranken (§ 87c UrhG) einem Verbotsumfang entgegen — Klausel insoweit unwirksam?
- Unterscheiden die Haftungsklauseln zwischen Vorsatz, grober und leichter Fahrlässigkeit — § 309 Nr. 7 BGB beachten?
- Gibt es einen wirksamen Gerichtsstand und anwendbares Recht in den AGB für grenzüberschreitende Datenbanknutzung?

## Typische Fallstricke

- Zu pauschale Scraping-Verbote, die auch zulässige Nutzungen einschließen, sind nach § 307 BGB unwirksam.
- AGB-TDM-Verbote ohne zusätzliche maschinenlesbare Opt-out-Erklärung wirken nicht als § 44b Abs. 3 UrhG-Opt-out.
- Klauseln, die dem Betreiber alle Rechte an Kundendaten zuweisen, sind in der Regel nach § 307 BGB unangemessen.
- Einseitige Leistungsänderungsvorbehalte des Betreibers (§ 308 Nr. 4 BGB) für Datenbankzugang sind begrenzt zulässig.
- Verbraucher-AGB unterliegen strengerer Kontrolle als B2B-AGB — für B2C immer zusätzlich §§ 308-309 BGB prüfen.

## Output

- AGB-Klausel-Vorlage: Scraping-Verbot (§ 307 BGB-konform)
- AGB-Klausel-Vorlage: TDM-Opt-out mit technischer Ergänzungspflicht
- AGB-Klausel-Vorlage: Datenbankrechts-Zuweisung und Nutzungsumfang
- AGB-Klausel-Vorlage: Haftungsbegrenzung (§ 309 Nr. 7 BGB-konform)
- AGB-Inhaltskontrolle-Checkliste für bestehende Datenbankbetreiber-AGB

## Quellen

- [§ 307 BGB — dejure.org](https://dejure.org/gesetze/BGB/307.html)
- [§ 309 BGB — dejure.org](https://dejure.org/gesetze/BGB/309.html)
- [§ 44b UrhG — dejure.org](https://dejure.org/gesetze/UrhG/44b.html)
- [§ 87c UrhG — dejure.org](https://dejure.org/gesetze/UrhG/87c.html)
- [§ 87b UrhG — dejure.org](https://dejure.org/gesetze/UrhG/87b.html)
- [§ 308 BGB — dejure.org](https://dejure.org/gesetze/BGB/308.html)

## 2. `db-029-auskunft-rechnungslegung-schadensschaetzung`

**Fokus:** Auskunft, Rechnungslegung und Schadensschätzung im Datenbankrecht nach §§ 97 101 UrhG: Dreigliedrige Schadensberechnung (konkreter Schaden, Herausgabe Verletzergewinn, Lizenzanalogie), Auskunftsanspruch gegen Verletzer und ISP, Rechnungslegungsvollstreckung sowie Besonderheiten bei Datenbankschutz nach §§ 87a-87e UrhG. Erstellt Schadensberechnung und Klageanträge.

# Auskunft, Rechnungslegung und Schadensschätzung im Datenbankrecht

## Mandantenfall

- Datenbankbetreiber hat eine einstweilige Verfügung erwirkt und will nun im Hauptsacheverfahren Schadensersatz geltend machen — Auskunftsanspruch und Schadensberechnung sind unklar.
- Verletzer hat Datenbankdaten für eigene kommerzielle Produkte genutzt — wie hoch ist der Schaden und welche Berechnungsmethode gilt?
- Anwalt muss den Auskunftsanspruch gegen einen unbekannten Scraper über den Internetdienstanbieter nach § 101 UrhG geltend machen.

## Erste Schritte

1. Auskunftsanspruch formulieren: § 101 UrhG gegen Verletzer — Umfang der Verletzung (Zeit, Volumen, Empfänger), Lieferkette der entnommenen Daten, Erlöse.
2. Auskunft gegen ISP prüfen: § 101 Abs. 2 UrhG gegen Internetdienstanbieter — Voraussetzung: gewerbliche Verletzung, Antrag bei Gericht erforderlich.
3. Schadensberechnungsmethode wählen: Konkreter Schaden, Herausgabe des Verletzergewinns oder Lizenzanalogie (§ 97 Abs. 2 UrhG) — welche Methode maximiert den Anspruch?
4. Lizenzanalogie berechnen: Übliche Lizenzgebühr für die entnommenen Datenbankteile ermitteln (Marktvergleich, eigene Lizenzpraxis).
5. Rechnungslegung vollstrecken: Wenn Verletzer Auskunft verweigert — Zwangsvollstreckung nach § 888 ZPO, Ordnungsgeld.
6. Verjährung prüfen: § 102 UrhG i.V.m. §§ 195-199 BGB — 3 Jahre ab Kenntnis, 10 Jahre Höchstfrist.

## Rechtsrahmen

- § 97 Abs. 1 UrhG: Unterlassung und Schadensersatz bei Datenbankrechts-Verletzung.
- § 97 Abs. 2 UrhG: Drei Berechnungsmethoden — konkreter Schaden, Verletzergewinnherausgabe, Lizenzanalogie.
- § 101 UrhG: Auskunftsanspruch gegen Verletzer und (bei gewerblicher Verletzung) gegen ISP.
- § 102 UrhG: Verjährung der Schadensersatzansprüche — 3 Jahre ab Kenntnis.
- § 888 ZPO: Erzwingung nicht vertretbarer Handlungen (Rechnungslegung) durch Ordnungsgeld.
- § 87b UrhG: Verletzungstatbestand als Grundlage aller Folgeansprüche.

## Prüfraster

- Liegt eine Verletzung nach § 87b UrhG als Grundlage des Schadensersatzes vor?
- Ist der Verletzer bekannt, oder muss der ISP-Auskunftsweg nach § 101 Abs. 2 UrhG beschritten werden?
- Welche der drei Berechnungsmethoden (§ 97 Abs. 2 UrhG) führt zu maximalem oder realistischstem Ergebnis?
- Lässt sich eine übliche Lizenzgebühr (Lizenzanalogie) aus eigenen Verträgen oder Marktvergleichen ableiten?
- Hat der Verletzer Gewinne aus der Nutzung der entnommenen Daten erzielt, die herausgegeben werden müssen?
- Ist die Verjährungsfrist nach § 102 UrhG noch offen — wann hatte der Gläubiger Kenntnis?
- Wann wurde Auskunft verlangt und noch nicht erfüllt — Rechnungslegungs-Klage und Vollstreckung planen?

## Typische Fallstricke

- Lizenzanalogie erfordert Nachweis einer „üblichen" Lizenzgebühr — ohne eigene Lizenzpraxis schwer zu begründen.
- ISP-Auskunft nach § 101 Abs. 2 UrhG setzt gewerbliche Verletzung voraus — private Nutzung scheidet aus.
- Verletzergewinnherausgabe ist oft schwer durchsetzbar, weil Verletzer keine separate Buchführung für Datenbanknutzung hat.
- Schadensberechnung ohne Sachverständigengutachten zu Datenbankwert und Lizenzüblichkeit wird von Gerichten oft gekürzt.
- Verjährung beginnt mit Kenntnis — nicht mit Entdeckung des vollen Schadensumfangs. Frühzeitige Klageerhebung oder Hemmung.

## Output

- Schadensberechnungsmatrix (alle drei Methoden nach § 97 Abs. 2 UrhG)
- Auskunftsklage-Muster gegen Verletzer (§ 101 UrhG)
- ISP-Auskunftsantrag nach § 101 Abs. 2 UrhG (gerichtlich)
- Lizenzanalogie-Berechnungsnachweis (Marktvergleich)
- Verjährungsprüfungsprotokoll mit Fristberechnung

## Quellen

- [§ 97 UrhG — dejure.org](https://dejure.org/gesetze/UrhG/97.html)
- [§ 101 UrhG — dejure.org](https://dejure.org/gesetze/UrhG/101.html)
- [§ 102 UrhG — dejure.org](https://dejure.org/gesetze/UrhG/102.html)
- [§ 87b UrhG — dejure.org](https://dejure.org/gesetze/UrhG/87b.html)
- [§ 888 ZPO — dejure.org](https://dejure.org/gesetze/ZPO/888.html)
- [§§ 195-199 BGB — dejure.org](https://dejure.org/gesetze/BGB/195.html)

## 3. `db-041-datenqualitaet-haftung-und-gewaehrleistung`

**Fokus:** Haftung und Gewährleistung für Datenbankqualität: §§ 434 437 BGB Sachmängelhaftung bei fehlerhaften Datenbankdaten, Deliktshaftung (§ 823 BGB) bei falschen Einträgen, DSGVO-Berichtigungspflichten (Art. 16 DSGVO) und vertragliche Haftungsbegrenzungen. Bewertet Schadensersatzansprüche bei Falschauskunft aus Datenbanken und Disclaimer-Klauseln.

# Datenqualität, Haftung und Gewährleistung bei Datenbankfehlern

## Mandantenfall

- Unternehmen hat auf Basis fehlerhafter Bonitätsdaten aus einer kommerziellen Datenbank einen Kredit gewährt, der ausgefallen ist — wer haftet?
- Betroffene Person verlangt die Berichtigung eines falschen Eintrags in einer Unternehmensdatenbank nach Art. 16 DSGVO und droht mit Schadensersatz.
- Datenbankbetreiber will seine Haftung für fehlerhafte Datenbankeinträge durch Disclaimer-Klauseln begrenzen — sind diese wirksam?

## Erste Schritte

1. Vertragliche Haftungsgrundlage prüfen: Liegt ein Kauf- oder Dienstleistungsvertrag für Datenbankzugang vor — gilt Sachmängelhaftung (§§ 434 ff. BGB)?
2. Deliktshaftung prüfen: § 823 Abs. 1 BGB (Verletzung absoluter Rechte) oder § 823 Abs. 2 BGB (Schutzgesetzverletzung) bei falschen Datenbankeinträgen?
3. DSGVO-Berichtigungspflicht erfüllen: Art. 16 DSGVO — Pflicht zur Berichtigung unrichtiger personenbezogener Daten; § 84 DSGVO-Schadensersatz.
4. Haftungsbegrenzung durch AGB prüfen: § 309 Nr. 7 BGB — Haftung für grobe Fahrlässigkeit und Vorsatz kann nicht ausgeschlossen werden.
5. Datenbankqualitätspflichten bestimmen: Welche Sorgfaltspflichten hat der Datenbankbetreiber bei Datenerhebung und -pflege?
6. Schadenskausalität nachweisen: Adäquanzkausalität zwischen fehlerhaftem Datenbankeintrag und eingetretenem Schaden.

## Rechtsrahmen

- §§ 434-437 BGB: Sachmangelhaftung — fehlerhafte Datenbankdaten als Sachmangel bei Datenbankverkauf oder -lizenz.
- § 823 Abs. 1 BGB: Deliktshaftung für fehlerhafte Einträge, die Eigentum, Gesundheit oder sonstige absolute Rechte verletzen.
- Art. 16 DSGVO: Berichtigungsrecht für unrichtige personenbezogene Daten — kostenlos, unverzüglich.
- Art. 82 DSGVO: Schadensersatzanspruch für materiellen oder immateriellen Schaden durch DSGVO-Verstoß.
- § 309 Nr. 7 BGB: Haftungsausschluss für Vorsatz und grobe Fahrlässigkeit in AGB unzulässig.
- § 309 Nr. 8 BGB: Einschränkungen der Mängelgewährleistung in AGB — Grenzen der wirksamen Haftungsbeschränkung.

## Prüfraster

- Liegt ein Vertrag (Kauf, Lizenz, SaaS) vor, aus dem Gewährleistungspflichten für Datenqualität entstehen?
- Ist der fehlerhafte Datenbankeintrag kausal für den eingetretenen Schaden — lässt sich die Kausalkette nachweisen?
- Hat der Datenbankbetreiber Sorgfaltspflichten bei Datenerhebung und -pflege verletzt (Fahrlässigkeit)?
- Enthält die Datenbank personenbezogene Daten — gilt die DSGVO-Berichtigungspflicht (Art. 16 DSGVO)?
- Sind Disclaimer-/Haftungsbeschrän­kungsklauseln AGB-wirksam nach §§ 307-309 BGB?
- Schreibt das Gläubiger eine Obliegenheit zur Eigenprüfung von Datenbankdaten vor — Mitverschulden (§ 254 BGB)?
- Besteht ein immaterieller Schaden wegen falscher Datenbankeinträge (z. B. Bonitätsdaten, Schwarze Liste)?

## Typische Fallstricke

- Haftungsausschluss für fehlerhafte Daten in AGB ist wirksam nur für einfache Fahrlässigkeit — grobe Fahrlässigkeit und Vorsatz können nicht ausgeschlossen werden.
- Art. 82 DSGVO-Schadensersatz ist unabhängig vom Vertragsrecht — auch ohne Vertragsverletzung kann DSGVO-Schadensersatz entstehen.
- Mitverschulden des Datenbank-Nutzers möglich, wenn er fehlerhafte Einträge nicht einer Plausibilitätsprüfung unterzogen hat.
- Bonitätsdatenbankbetreiber (SCHUFA) haben besondere gesetzliche Sorgfaltspflichten — Verletzungen können erhebliche Schadensersatzansprüche auslösen.
- Berichtigungspflicht nach Art. 16 DSGVO schließt Schadensersatzansprüche nicht aus — beides kann parallel geltend gemacht werden.

## Output

- Haftungsrisikoanalyse für Datenbankbetreiber (Vertrag + Delikt + DSGVO)
- DSGVO-Berichtigungs(Art. 16 DSGVO) für personenbezogene Datenbanken
- Haftungsbegrenzungs-AGB-Klausel (§§ 307-309 BGB-konform)
- Datenbankqualitäts-Sorgfaltspflichten-Katalog
- Schadensberechnung für Falschauskunft-Fälle (Lizenzanalogie / konkreter Schaden)

## Quellen

- [§ 434 BGB — dejure.org](https://dejure.org/gesetze/BGB/434.html)
- [§ 823 BGB — dejure.org](https://dejure.org/gesetze/BGB/823.html)
- [Art. 16 DSGVO — dejure.org](https://dejure.org/gesetze/DSGVO/16.html)
- [Art. 82 DSGVO — dejure.org](https://dejure.org/gesetze/DSGVO/82.html)
- [§ 309 BGB — dejure.org](https://dejure.org/gesetze/BGB/309.html)
- [§ 254 BGB Mitverschulden — dejure.org](https://dejure.org/gesetze/BGB/254.html)
