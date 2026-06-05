---
name: ai-act-aktenherausgabe-zurueckbehaltung
description: "AI ACT Aktenherausgabe Zurueckbehaltung: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# AI ACT Aktenherausgabe Zurueckbehaltung

## Arbeitsbereich

Dieser Skill bündelt 5 sachlich verwandte Arbeitsschritte rund um **AI ACT Aktenherausgabe Zurueckbehaltung** im Plugin Berufsrecht der Rechtsanwälte. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `anwaelte-ai-act-transparenz-kanzlei-chatbot` | AI-Act-Transparenz in der Kanzlei prüfen: Mandantenchatbot, Website, Marketing, Legal-Update, Schriftsatzentwurf, Art. 4 und Art. 50 KI-VO, Anbieter-/Betreiberrolle, redaktionelle Kontrolle und Kennzeichnung ab 02.08.2026. |
| `anwaelte-aktenherausgabe-und-zurueckbehaltung-kammerantwort-und` | Anwälte: aktenherausgabe und zurueckbehaltung - Kammerantwort mit Verfahrensstrategie, Tonlage und Belegplan; mit Live-Normencheck, Kammerlogik, Verhältnismäßigkeit, Belegplan und nächstem Schritt. |
| `anwaelte-aktenherausgabe-und-zurueckbehaltung-organisationspfli` | Anwälte: aktenherausgabe und zurueckbehaltung - Organisationspflichten, Prävention, Team-Anweisung und Fristenkontrolle; mit Live-Normencheck, Kammerlogik, Verhältnismäßigkeit, Belegplan und nächstem Schritt. |
| `anwaelte-anwaltliche-nebentaetigkeit-kammerantwort-und-verfahre` | Anwälte: anwaltliche nebentaetigkeit - Kammerantwort mit Verfahrensstrategie, Tonlage und Belegplan; mit Live-Normencheck, Kammerlogik, Verhältnismäßigkeit, Belegplan und nächstem Schritt. |
| `anwaelte-anwaltliche-nebentaetigkeit-organisationspflicht-und-p` | Anwälte: anwaltliche nebentaetigkeit - Organisationspflichten, Prävention, Team-Anweisung und Fristenkontrolle; mit Live-Normencheck, Kammerlogik, Verhältnismäßigkeit, Belegplan und nächstem Schritt. |

## Arbeitsweg

Im Plugin Berufsrecht der Rechtsanwälte gilt für **AI ACT Aktenherausgabe Zurueckbehaltung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `anwaelte-ai-act-transparenz-kanzlei-chatbot`

**Fokus:** AI-Act-Transparenz in der Kanzlei prüfen: Mandantenchatbot, Website, Marketing, Legal-Update, Schriftsatzentwurf, Art. 4 und Art. 50 KI-VO, Anbieter-/Betreiberrolle, redaktionelle Kontrolle und Kennzeichnung ab 02.08.2026.

# KI-VO-Transparenz bei Kanzlei-Chatbot, Website und Schriftsatz

## Fachkern: KI-VO-Transparenz bei Kanzlei-Chatbot, Website und Schriftsatz
- **Spezialgegenstand:** KI-VO-Transparenz bei Kanzlei-Chatbot, Website und Schriftsatz; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** BRAO, BORA, FAO, RVG, RDG, GwG, beA, Verschwiegenheit, Interessenkollision und Anwaltsgerichtsbarkeit.
- **Entscheidende Weiche:** Pflichtnorm, Mandatsrolle, Verschulden, Kammerverfahren, Reputationsrisiko, Rechtsbehelf und milderes Organisationsmittel trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


## Startpunkt

Prüfe zuerst die Rolle der Kanzlei: nutzt sie ein fremdes System nur intern, betreibt sie einen Mandantenchatbot, veröffentlicht sie KI-generierte Inhalte oder baut sie eine eigene Oberfläche auf einem Modell? Davon hängen Art. 4, Art. 50 und mögliche Anbieter-/Betreiberfragen ab.

## Matrix

| Use Case | Typische Rolle | Transparenzlogik |
|---|---|---|
| Interner Schriftsatzentwurf | Betreiberin eines Hilfstools | Kein KI-Hinweis allein deshalb, wenn der Schriftsatz anwaltlich geprüft und verantwortet wird; Berufs- und Haftungskontrolle bleibt zentral. |
| Mandantenchatbot auf Website | Betreiberin gegenüber Mandanten/Nutzern | Nutzer müssen erkennen, dass sie mit KI interagieren; keine Scheinkanzlei-Beratung ohne Mandatsklärung. |
| Legal Update/Newsletter | Veröffentlichte Inhalte | KI-Anteil, redaktionelle Verantwortung und menschliche Prüfung dokumentieren; Kennzeichnungspflichten ab 02.08.2026 live prüfen. |
| Marketingbild/-video/-Audio | Deepfake-/synthetischer Inhalt möglich | Art.-50-Transparenz und Irreführungsverbot mit Berufsrecht zusammendenken. |
| Eigene Kanzlei-API oder White-Label-Lösung | Rollenprüfung vertiefen | Mögliches Anbieter-/Bereitstellerprofil prüfen, besonders bei eigener Zweckbestimmung und Weitergabe an Dritte. |

## Art. 4 KI-VO

Die Kanzlei muss KI-Kompetenz bei Personen organisieren, die KI-Systeme in ihrem Auftrag nutzen. Das ist kein bloßer Schulungszettel: Es braucht rollenbezogene Unterweisung zu Quellenprüfung, Geheimnisschutz, Halluzinationen, Prompt-Injection, Diskriminierungsrisiken und Grenzen automatisierter Vorschläge.

## Art. 50 KI-VO

Für Transparenzpflichten immer das konkrete Szenario prüfen:

- Interaktion Mensch mit KI-System
- KI-generierter oder manipulierter Inhalt
- Veröffentlichung gegenüber Dritten
- redaktionelle Kontrolle durch Menschen
- gesetzliche Ausnahmen oder Sonderpflichten

## Output

Erstelle:

- Rollenvermerk zur KI-VO
- Transparenzhinweis für Website/Chatbot
- Redaktions- und Freigabevermerk
- Schulungsnotiz nach Art. 4 KI-VO

## 2. `anwaelte-aktenherausgabe-und-zurueckbehaltung-kammerantwort-und`

**Fokus:** Anwälte: aktenherausgabe und zurueckbehaltung - Kammerantwort mit Verfahrensstrategie, Tonlage und Belegplan; mit Live-Normencheck, Kammerlogik, Verhältnismäßigkeit, Belegplan und nächstem Schritt.

# Anwälte: aktenherausgabe und zurueckbehaltung - Kammerantwort mit Verfahrensstrategie, Tonlage und Belegplan

## Konkreter Berufsrechtskern: Anwälte: aktenherausgabe und zurueckbehaltung - Kammerantwort mit Verfahrensstrategie, Tonlage und Belegplan
- **Spezialgegenstand:** Anwälte: aktenherausgabe und zurueckbehaltung - Kammerantwort mit Verfahrensstrategie, Tonlage und Belegplan - prüfe genau diese Pflicht, Verteidigungslinie oder Organisationsfrage berufsrechtlich bis zum verwertbaren Arbeitsergebnis.
- **Normenanker:** BRAO, BORA, FAO, RVG, RDG, GwG, beA-Pflichten, anwaltliche Verschwiegenheit und anwaltsgerichtliches Verfahren.
- **Institutionen:** Rechtsanwaltskammer, Anwaltsgericht, AGH/BGH-Anwaltssenat und gegebenenfalls Aufsichts-/Strafbehörden.
- **Spezialspur:** Leite aus dem konkreten Slug die berufsrechtliche Pflicht, den Tatsachenbeleg, den Verfahrensgegner und das mildeste tragfähige Gegenmittel ab.
- **Falllösung:** Baue eine Pflichtverletzungs-/Entlastungsmatrix mit Norm, Tatsache, Beleg, Verschulden, Verhältnismäßigkeit, möglicher Kammerantwort und prozessualem nächsten Schritt.

## Fallweichen dieser Speziallage

1. Rolle, Ziel und Entscheidungsdruck klaeren.
2. Verfahrensstand, Fristen, Zuständigkeit und irreversible Risiken markieren.
3. Aktenbasis ordnen: sichere Tatsachen, bestrittene Tatsachen, fehlende Unterlagen.
4. Eingriffsintensität, Berufs-/Amtsgeheimnisse, Datenschutz und Persönlichkeitsrechte sichtbar machen.
5. Sofortpfad anbieten: Was muss heute entschieden, beantragt, beantwortet oder dokumentiert werden?

## Prüfprogramm

- **Normenanker:** BRAO, BORA, FAO, RVG, RDG, GwG, ZPO/StPO-Schnittstellen, Kammerhinweise und Anwaltsgerichtsbarkeit live prüfen
- **Tatsachenarbeit:** Beweisquelle, Beweiswert, Gegenbeweis, Dokumentationslücke und mögliche Fehlinterpretation trennen.
- **Verfahrensarbeit:** Form, Frist, Zuständigkeit, Anhörung, Akteneinsicht, Rechtsbehelf und Zustellungsweg prüfen.
- **Gegenposition:** Die stärkste Gegenansicht formulieren und sagen, was sie praktisch bedeutet.
- **Entscheidung:** Eine vertretbare Handlungsempfehlung mit Risikoampel und nächstem Schritt liefern.

## Spezielle Leitplanken

- Rechtsprechung ist tragend nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.
- Berufsrechtliche Risiken sind oft reputations- und existenzrelevant; Verhältnismäßigkeit sichtbar prüfen.
- Mandats-, Steuer-, Prüfungs- oder Amtsgeheimnisse vor Nutzung anonymisieren.

## Output

Erzeuge Berufsrechtsmemo, Kammerantwort, Konfliktcheck, Organisationsanweisung, Vertragsklausel, Fristenblatt oder Verteidigungslinie.

## Quellenhygiene

Keine erfundenen Fundstellen. Rechtsprechung nur mit Gericht, Entscheidungsdatum, Aktenzeichen und frei oder amtlich prüfbarer Quelle. Bei unsicherer oder neuer Rechtslage ausdrücklich sagen, was live nachzusehen ist und welche Quelle dafür zuerst aufgerufen werden soll.

## 3. `anwaelte-aktenherausgabe-und-zurueckbehaltung-organisationspfli`

**Fokus:** Anwälte: aktenherausgabe und zurueckbehaltung - Organisationspflichten, Prävention, Team-Anweisung und Fristenkontrolle; mit Live-Normencheck, Kammerlogik, Verhältnismäßigkeit, Belegplan und nächstem Schritt.

# Anwälte: aktenherausgabe und zurueckbehaltung - Organisationspflichten, Prävention, Team-Anweisung und Fristenkontrolle

## Konkreter Berufsrechtskern: Anwälte: aktenherausgabe und zurueckbehaltung - Organisationspflichten, Prävention, Team-Anweisung und Fristenkontrolle
- **Spezialgegenstand:** Anwälte: aktenherausgabe und zurueckbehaltung - Organisationspflichten, Prävention, Team-Anweisung und Fristenkontrolle - prüfe genau diese Pflicht, Verteidigungslinie oder Organisationsfrage berufsrechtlich bis zum verwertbaren Arbeitsergebnis.
- **Normenanker:** BRAO, BORA, FAO, RVG, RDG, GwG, beA-Pflichten, anwaltliche Verschwiegenheit und anwaltsgerichtliches Verfahren.
- **Institutionen:** Rechtsanwaltskammer, Anwaltsgericht, AGH/BGH-Anwaltssenat und gegebenenfalls Aufsichts-/Strafbehörden.
- **Spezialspur:** Leite aus dem konkreten Slug die berufsrechtliche Pflicht, den Tatsachenbeleg, den Verfahrensgegner und das mildeste tragfähige Gegenmittel ab.
- **Falllösung:** Baue eine Pflichtverletzungs-/Entlastungsmatrix mit Norm, Tatsache, Beleg, Verschulden, Verhältnismäßigkeit, möglicher Kammerantwort und prozessualem nächsten Schritt.

## Fallweichen dieser Speziallage

1. Rolle, Ziel und Entscheidungsdruck klaeren.
2. Verfahrensstand, Fristen, Zuständigkeit und irreversible Risiken markieren.
3. Aktenbasis ordnen: sichere Tatsachen, bestrittene Tatsachen, fehlende Unterlagen.
4. Eingriffsintensität, Berufs-/Amtsgeheimnisse, Datenschutz und Persönlichkeitsrechte sichtbar machen.
5. Sofortpfad anbieten: Was muss heute entschieden, beantragt, beantwortet oder dokumentiert werden?

## Prüfprogramm

- **Normenanker:** BRAO, BORA, FAO, RVG, RDG, GwG, ZPO/StPO-Schnittstellen, Kammerhinweise und Anwaltsgerichtsbarkeit live prüfen
- **Tatsachenarbeit:** Beweisquelle, Beweiswert, Gegenbeweis, Dokumentationslücke und mögliche Fehlinterpretation trennen.
- **Verfahrensarbeit:** Form, Frist, Zuständigkeit, Anhörung, Akteneinsicht, Rechtsbehelf und Zustellungsweg prüfen.
- **Gegenposition:** Die stärkste Gegenansicht formulieren und sagen, was sie praktisch bedeutet.
- **Entscheidung:** Eine vertretbare Handlungsempfehlung mit Risikoampel und nächstem Schritt liefern.

## Spezielle Leitplanken

- Rechtsprechung ist tragend nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.
- Berufsrechtliche Risiken sind oft reputations- und existenzrelevant; Verhältnismäßigkeit sichtbar prüfen.
- Mandats-, Steuer-, Prüfungs- oder Amtsgeheimnisse vor Nutzung anonymisieren.

## Output

Erzeuge Berufsrechtsmemo, Kammerantwort, Konfliktcheck, Organisationsanweisung, Vertragsklausel, Fristenblatt oder Verteidigungslinie.

## Quellenhygiene

Keine erfundenen Fundstellen. Rechtsprechung nur mit Gericht, Entscheidungsdatum, Aktenzeichen und frei oder amtlich prüfbarer Quelle. Bei unsicherer oder neuer Rechtslage ausdrücklich sagen, was live nachzusehen ist und welche Quelle dafür zuerst aufgerufen werden soll.

## 4. `anwaelte-anwaltliche-nebentaetigkeit-kammerantwort-und-verfahre`

**Fokus:** Anwälte: anwaltliche nebentaetigkeit - Kammerantwort mit Verfahrensstrategie, Tonlage und Belegplan; mit Live-Normencheck, Kammerlogik, Verhältnismäßigkeit, Belegplan und nächstem Schritt.

# Anwälte: anwaltliche nebentaetigkeit - Kammerantwort mit Verfahrensstrategie, Tonlage und Belegplan

## Konkreter Berufsrechtskern: Anwälte: anwaltliche nebentaetigkeit - Kammerantwort mit Verfahrensstrategie, Tonlage und Belegplan
- **Spezialgegenstand:** Anwälte: anwaltliche nebentaetigkeit - Kammerantwort mit Verfahrensstrategie, Tonlage und Belegplan - prüfe genau diese Pflicht, Verteidigungslinie oder Organisationsfrage berufsrechtlich bis zum verwertbaren Arbeitsergebnis.
- **Normenanker:** BRAO, BORA, FAO, RVG, RDG, GwG, beA-Pflichten, anwaltliche Verschwiegenheit und anwaltsgerichtliches Verfahren.
- **Institutionen:** Rechtsanwaltskammer, Anwaltsgericht, AGH/BGH-Anwaltssenat und gegebenenfalls Aufsichts-/Strafbehörden.
- **Spezialspur:** Leite aus dem konkreten Slug die berufsrechtliche Pflicht, den Tatsachenbeleg, den Verfahrensgegner und das mildeste tragfähige Gegenmittel ab.
- **Falllösung:** Baue eine Pflichtverletzungs-/Entlastungsmatrix mit Norm, Tatsache, Beleg, Verschulden, Verhältnismäßigkeit, möglicher Kammerantwort und prozessualem nächsten Schritt.

## Fallweichen dieser Speziallage

1. Rolle, Ziel und Entscheidungsdruck klaeren.
2. Verfahrensstand, Fristen, Zuständigkeit und irreversible Risiken markieren.
3. Aktenbasis ordnen: sichere Tatsachen, bestrittene Tatsachen, fehlende Unterlagen.
4. Eingriffsintensität, Berufs-/Amtsgeheimnisse, Datenschutz und Persönlichkeitsrechte sichtbar machen.
5. Sofortpfad anbieten: Was muss heute entschieden, beantragt, beantwortet oder dokumentiert werden?

## Prüfprogramm

- **Normenanker:** BRAO, BORA, FAO, RVG, RDG, GwG, ZPO/StPO-Schnittstellen, Kammerhinweise und Anwaltsgerichtsbarkeit live prüfen
- **Tatsachenarbeit:** Beweisquelle, Beweiswert, Gegenbeweis, Dokumentationslücke und mögliche Fehlinterpretation trennen.
- **Verfahrensarbeit:** Form, Frist, Zuständigkeit, Anhörung, Akteneinsicht, Rechtsbehelf und Zustellungsweg prüfen.
- **Gegenposition:** Die stärkste Gegenansicht formulieren und sagen, was sie praktisch bedeutet.
- **Entscheidung:** Eine vertretbare Handlungsempfehlung mit Risikoampel und nächstem Schritt liefern.

## Spezielle Leitplanken

- Rechtsprechung ist tragend nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.
- Berufsrechtliche Risiken sind oft reputations- und existenzrelevant; Verhältnismäßigkeit sichtbar prüfen.
- Mandats-, Steuer-, Prüfungs- oder Amtsgeheimnisse vor Nutzung anonymisieren.

## Output

Erzeuge Berufsrechtsmemo, Kammerantwort, Konfliktcheck, Organisationsanweisung, Vertragsklausel, Fristenblatt oder Verteidigungslinie.

## Quellenhygiene

Keine erfundenen Fundstellen. Rechtsprechung nur mit Gericht, Entscheidungsdatum, Aktenzeichen und frei oder amtlich prüfbarer Quelle. Bei unsicherer oder neuer Rechtslage ausdrücklich sagen, was live nachzusehen ist und welche Quelle dafür zuerst aufgerufen werden soll.

## 5. `anwaelte-anwaltliche-nebentaetigkeit-organisationspflicht-und-p`

**Fokus:** Anwälte: anwaltliche nebentaetigkeit - Organisationspflichten, Prävention, Team-Anweisung und Fristenkontrolle; mit Live-Normencheck, Kammerlogik, Verhältnismäßigkeit, Belegplan und nächstem Schritt.

# Anwälte: anwaltliche nebentaetigkeit - Organisationspflichten, Prävention, Team-Anweisung und Fristenkontrolle

## Konkreter Berufsrechtskern: Anwälte: anwaltliche nebentaetigkeit - Organisationspflichten, Prävention, Team-Anweisung und Fristenkontrolle
- **Spezialgegenstand:** Anwälte: anwaltliche nebentaetigkeit - Organisationspflichten, Prävention, Team-Anweisung und Fristenkontrolle - prüfe genau diese Pflicht, Verteidigungslinie oder Organisationsfrage berufsrechtlich bis zum verwertbaren Arbeitsergebnis.
- **Normenanker:** BRAO, BORA, FAO, RVG, RDG, GwG, beA-Pflichten, anwaltliche Verschwiegenheit und anwaltsgerichtliches Verfahren.
- **Institutionen:** Rechtsanwaltskammer, Anwaltsgericht, AGH/BGH-Anwaltssenat und gegebenenfalls Aufsichts-/Strafbehörden.
- **Spezialspur:** Leite aus dem konkreten Slug die berufsrechtliche Pflicht, den Tatsachenbeleg, den Verfahrensgegner und das mildeste tragfähige Gegenmittel ab.
- **Falllösung:** Baue eine Pflichtverletzungs-/Entlastungsmatrix mit Norm, Tatsache, Beleg, Verschulden, Verhältnismäßigkeit, möglicher Kammerantwort und prozessualem nächsten Schritt.

## Fallweichen dieser Speziallage

1. Rolle, Ziel und Entscheidungsdruck klaeren.
2. Verfahrensstand, Fristen, Zuständigkeit und irreversible Risiken markieren.
3. Aktenbasis ordnen: sichere Tatsachen, bestrittene Tatsachen, fehlende Unterlagen.
4. Eingriffsintensität, Berufs-/Amtsgeheimnisse, Datenschutz und Persönlichkeitsrechte sichtbar machen.
5. Sofortpfad anbieten: Was muss heute entschieden, beantragt, beantwortet oder dokumentiert werden?

## Prüfprogramm

- **Normenanker:** BRAO, BORA, FAO, RVG, RDG, GwG, ZPO/StPO-Schnittstellen, Kammerhinweise und Anwaltsgerichtsbarkeit live prüfen
- **Tatsachenarbeit:** Beweisquelle, Beweiswert, Gegenbeweis, Dokumentationslücke und mögliche Fehlinterpretation trennen.
- **Verfahrensarbeit:** Form, Frist, Zuständigkeit, Anhörung, Akteneinsicht, Rechtsbehelf und Zustellungsweg prüfen.
- **Gegenposition:** Die stärkste Gegenansicht formulieren und sagen, was sie praktisch bedeutet.
- **Entscheidung:** Eine vertretbare Handlungsempfehlung mit Risikoampel und nächstem Schritt liefern.

## Spezielle Leitplanken

- Rechtsprechung ist tragend nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.
- Berufsrechtliche Risiken sind oft reputations- und existenzrelevant; Verhältnismäßigkeit sichtbar prüfen.
- Mandats-, Steuer-, Prüfungs- oder Amtsgeheimnisse vor Nutzung anonymisieren.

## Output

Erzeuge Berufsrechtsmemo, Kammerantwort, Konfliktcheck, Organisationsanweisung, Vertragsklausel, Fristenblatt oder Verteidigungslinie.

## Quellenhygiene

Keine erfundenen Fundstellen. Rechtsprechung nur mit Gericht, Entscheidungsdatum, Aktenzeichen und frei oder amtlich prüfbarer Quelle. Bei unsicherer oder neuer Rechtslage ausdrücklich sagen, was live nachzusehen ist und welche Quelle dafür zuerst aufgerufen werden soll.
