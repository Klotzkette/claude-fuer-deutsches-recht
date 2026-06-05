---
name: ki-kunst-abgrenzung-konventionelle
description: "Kunst Abgrenzung Konventionelle: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Kunst Abgrenzung Konventionelle

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Kunst Abgrenzung Konventionelle** im Plugin KI-VO / AI Act-Prüfer. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `ki-kunst-lizenzierung-kennzeichnung` | KI-Kunst, Werbung und Design: kreative Steuerung, Prompt-Protokoll, Trainings-/Referenzrisiko, Stilnaehe, Rechtefreigabe, Art.-50-Kennzeichnung, Lizenzvertrag und Dokumentation fuer Agenturen, Verlage, Kanzleien und Unternehmen. |
| `abgrenzung-konventionelle-software-vs-ki-system` | Grenzfall-Skill zur Abgrenzung konventioneller Software, Automation, Statistik, Expertensystemen, Workflows und KI-Systemen nach Art. 3 Nr. 1 KI-VO. Problematisiert Automation, Autonomie, Inferenz, gelernte Parameter, LLM/API-Komponenten und menschliche Freigabe. Output: Einordnungsmatrix mit belastbarer Begruendung und Weiterleitung zu liegt-ki-system-vor-art-3-nr-1, GPAI oder Hochrisiko-Pruefung. |
| `algorithmische-kollusion-und-pricing-ki` | Algorithmische Kollusion und KI-Pricing: Preisalgorithmen, Signalling, Hub-and-Spoke, Plattformdaten, Monitoring, Kartellrecht, Compliance-Firewalls und Beweisindikatoren fuer Rechtsabteilung und Vertrieb. |
| `anbieter-werden-art-25` | Betreiber Einführer oder Haendler fragt: Werde ich durch mein Verhalten selbst zum Anbieter eines KI-Systems mit allen daraus folgenden Pflichten? Art. 25 KI-VO Re-Provisioning. Prüfraster: vier Fallgruppen wesentliche Aenderung des Systems Bestimmungsaenderung Inverkehrbringen unter eigenem Namen Hochrisiko-Abdeckung ohne Anbieterbenennung. Output: Entscheidungsbaum mit Ja/Nein-Ergebnis und konkreten Folgepflichten. Abgrenzung zu rolle-anbieter-prüfen-art-3-nr-3 (Grunddefinition) und betreiber-deployer-pflichten-art-26 (Betreiberpflichten). |

## Arbeitsweg

Im Plugin KI-VO / AI Act-Prüfer gilt für **Kunst Abgrenzung Konventionelle**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `ki-kunst-lizenzierung-kennzeichnung`

**Fokus:** KI-Kunst, Werbung und Design: kreative Steuerung, Prompt-Protokoll, Trainings-/Referenzrisiko, Stilnaehe, Rechtefreigabe, Art.-50-Kennzeichnung, Lizenzvertrag und Dokumentation fuer Agenturen, Verlage, Kanzleien und Unternehmen.

# KI-Kunst: Lizenzierung und Kennzeichnung

## Einsatzfälle

- Kampagnenbild aus Bildgenerator.
- Cover, Illustration, Produktbild, Social-Media-Asset.
- Stilreferenz "wie Künstler X" oder "wie Marke Y".
- KI-Musik, Jingle, Layout, Video, Avatar.

## Prüfschritte

1. Prompt- und Referenzmaterial erfassen.
2. Fremdmaterialrechte prüfen.
3. Stilnähe und Verwechslungsgefahr bewerten.
4. Menschlichen Gestaltungsanteil dokumentieren.
5. Toolbedingungen und Nutzungsrechte prüfen.
6. Kennzeichnungspflichten nach Art. 50 KI-VO und Plattform-/Werberegeln prüfen.
7. Freigabe fuer Land, Medium, Dauer, Exklusivität und Bearbeitung.

## Vertragsbausteine

- Zusicherung zur Rechtekette.
- Offenlegung genutzter Tools und Referenzen.
- Haftungs- und Freistellungsklausel.
- Nachbearbeitungs- und Austauschrecht.
- Verbot bestimmter Referenzprompts.

## Output

Ein druckbarer Freigabezettel mit Ampel:

- Grün: nutzbar.
- Gelb: nur mit Anpassung/Nachlizenzierung.
- Rot: nicht veröffentlichen.

## 2. `abgrenzung-konventionelle-software-vs-ki-system`

**Fokus:** Grenzfall-Skill zur Abgrenzung konventioneller Software, Automation, Statistik, Expertensystemen, Workflows und KI-Systemen nach Art. 3 Nr. 1 KI-VO. Problematisiert Automation, Autonomie, Inferenz, gelernte Parameter, LLM/API-Komponenten und menschliche Freigabe. Output: Einordnungsmatrix mit belastbarer Begruendung und Weiterleitung zu liegt-ki-system-vor-art-3-nr-1, GPAI oder Hochrisiko-Pruefung.

# Abgrenzung: Konventionelle Software versus KI-System

## Zweck

Dieser Skill wird verwendet, wenn der Nutzer nicht sicher ist, ob eine Anwendung nur konventionelle Software oder bereits ein KI-System ist. Er vertieft die Art.-3-Nr.-1-Prüfung und verhindert zwei typische Fehler:

- KI-VO-Pflichten werden unnötig auf rein deterministische Software gezogen.
- KI-Komponenten werden übersehen, weil sie in normale Software, Workflows oder externe APIs eingebettet sind.

## Leitgedanke

Automation ist ein starkes Warnsignal, aber kein alleiniger Test. Entscheidend ist, ob das System aus Eingaben ableitet, wie Vorhersagen, Inhalte, Empfehlungen oder Entscheidungen erzeugt werden. Autonomie muss vorhanden sein, darf aber nicht überhöht werden: Auch ein Mensch-in-der-Schleife-System kann KI sein, wenn die Ausgabe inferenzbasiert entsteht.

## Abgrenzungsmatrix

### Regelmäßig konventionelle Software

| Systemtyp | Warum regelmäßig kein KI-System |
|---|---|
| SQL-Abfrage | Suche/Filter nach festen Kriterien, keine inferenzbasierte Ausgabe |
| Makro/Skript | starrer Ablauf, keine Ableitung aus Daten |
| Fristenrechner | mathematische oder juristische Regeln vollständig vorgegeben |
| Formularvalidierung | prüft Pflichtfelder oder Format, bewertet nicht |
| Dashboard mit Summen/Mittelwerten | deskriptive Statistik ohne Vorhersage/Empfehlung |
| Hartcodierter Entscheidungsbaum | Regeln und Schwellen komplett menschlich festgelegt |

### Grenzfälle

| Systemtyp | Entscheidend |
|---|---|
| Expertensystem | Nur Wissensbasis oder zusätzlich gelernte/inferenzbasierte Bewertung? |
| Scoring-Excel | Manuelle Gewichtung oder aus Daten gelernte Parameter? |
| Workflow-Automation | Nur Routing nach Regeln oder KI-Komponente mit Bewertung? |
| Suchmaschine | Reine Volltextsuche oder lernbasiertes Ranking/Personalisierung? |
| Fraud-Detection | Feste Schwellen oder Anomalie-/Klassifikationsmodell? |
| Chatbot | Skriptbaum oder generatives/LLM-basiertes System? |
| Rechts-/HR-Assistent | Nur Textentwurf oder Bewertung natürlicher Personen/Rechtsanwendung? |

### Regelmäßig KI-System oder KI-Komponente

| Systemtyp | Typisches KI-Merkmal |
|---|---|
| LLM, Transformer, generativer Chatbot | Inhalte/Empfehlungen durch Inferenz |
| Klassifikator, Random Forest, XGBoost, SVM | gelernte Muster und Zuordnung |
| Regression mit Prognosezweck | Vorhersage aus Eingaben |
| Clustering / Embeddings | Musterbildung oder Ähnlichkeit aus Daten |
| Bild-, Sprach- oder Emotionserkennung | inferenzbasierte Erkennung/Kategorisierung |
| Recommendation Engine | Empfehlung aus Nutzungs- oder Kontextdaten |
| RAG-System mit LLM-Auswertung | Retrieval plus generative/inferenzbasierte Antwort |

## Prüffragen

1. Werden Trainingsdaten, Modellgewichte, Embeddings, gelernte Parameter oder ein externes Modell genutzt?
2. Erzeugt das System aus variablen Eingaben eigenständig eine Ausgabe?
3. Ist die Ausgabe Vorhersage, Inhalt, Empfehlung, Score, Ranking, Klassifikation oder Entscheidung?
4. Kann ein Mensch die Ausgabe nur noch prüfen, übernehmen oder verwerfen?
5. Ist die Automation bloß Ablaufsteuerung oder trägt sie die inhaltliche Bewertung?
6. Ist eine KI-API oder ein GPAI-System eingebunden, auch wenn die eigene Software drumherum konventionell ist?
7. Wird das System in sensiblen Kontexten wie Beschäftigung, Bildung, Kredit, Justiz oder Verwaltung genutzt?

## Typische Fehlannahmen

**"Es lernt nicht im Betrieb, also keine KI."**
Falsch. Adaptivität nach Deployment ist optional; ein eingefrorenes trainiertes Modell kann KI-System sein.

**"Der Mensch entscheidet am Ende, also keine KI."**
Falsch. Menschliche Freigabe beseitigt die KI-Eigenschaft nicht, wenn die inhaltliche Ausgabe inferenzbasiert generiert wird.

**"Es ist nur eine API."**
Die API kann KI-System oder Bestandteil eines KI-Systems sein. Für den Betreiber zählt der konkrete Einsatz.

**"Es ist nur ein Chatbot."**
Ein skriptbasierter FAQ-Bot kann konventionell sein. Ein LLM-basierter Chatbot ist regelmäßig KI-System; Hochrisiko hängt aber erst vom Zweck ab.

**"Es ist nur Statistik."**
Deskriptive Statistik bleibt häufig draußen. Prognose, Klassifikation, Ranking oder individuelle Bewertung sprechen deutlich für KI.

## Ergebnislogik

- **KI-System wahrscheinlich:** `liegt-ki-system-vor-art-3-nr-1` dokumentierend abschließen, danach Risikoklasse prüfen.
- **Konventionelle Software wahrscheinlich:** Negativvermerk erstellen; Re-Evaluation bei neuer KI-Komponente oder Zweckänderung.
- **KI-Komponente in konventionellem System:** Gesamtarchitektur trennen und KI-Komponente separat durch die KI-VO-Prüfung führen.
- **GPAI/Chatbot betroffen:** `gpai-vorliegen-art-3-nr-63` und `begrenztes-risiko-art-50-transparenzpflichten`.
- **Sensible Zwecknähe:** zusätzlich `hochrisiko-art-6-abs-2-anhang-iii`.

## Output-Template — Abgrenzungsmatrix

```text
ABGRENZUNG KONVENTIONELLE SOFTWARE / KI-SYSTEM
Datum: [DATUM]
System / Komponente: [NAME]

1. Technischer Befund
[Regelwerk / / Statistik / ML-Modell / LLM / API / RAG / Hybrid]

2. Automation und Autonomie
[Was läuft automatisch? Wo greift ein Mensch ein? Ist die Ausgabe menschlich vorbestimmt?]

3. Inferenz
[Keine / möglich / wahrscheinlich / bestätigt]
[Begründung: Trainingsdaten, Modell, Gewichtung, Ranking, Generierung]

4. Output
[Vorhersage / Inhalt / Empfehlung / Entscheidung / nur Datenweitergabe]

5. Ergebnis
[konventionelle Software / KI-System / KI-Komponente im Gesamtsystem / Grenzfall]

6. Folgeprüfung
[liegt-ki-system-vor-art-3-nr-1 / gpai-vorliegen-art-3-nr-63 / hochrisiko-art-6-abs-2-anhang-iii / keine KI-VO]
```

## Quellen- und Aktualitätshinweis

Stand: 05/2026. Maßgeblich sind Art. 3 Nr. 1 KI-VO, Erwägungsgrund 12 und die Kommissionsleitlinien zur Definition des KI-Systems. Keine Rechtsberatung.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 3. `algorithmische-kollusion-und-pricing-ki`

**Fokus:** Algorithmische Kollusion und KI-Pricing: Preisalgorithmen, Signalling, Hub-and-Spoke, Plattformdaten, Monitoring, Kartellrecht, Compliance-Firewalls und Beweisindikatoren fuer Rechtsabteilung und Vertrieb.

# Algorithmische Kollusion und Pricing-KI

## Einsatzfälle

- Dynamic Pricing.
- Wettbewerberpreis-Monitoring.
- Repricing-Bots auf Marktplätzen.
- gemeinsame Softwareanbieter für mehrere Wettbewerber.
- KI-gestützte Rabatt- oder Ausschreibungsstrategie.

## Norm- und Quellenanker

- Art. 101 AEUV und GWB § 1 für abgestimmtes Verhalten, Kartelle, Hub-and-Spoke und Informationsaustausch.
- GWB §§ 19, 20 und Art. 102 AEUV prüfen, wenn marktbeherrschende Plattformen, Datenzugang, Selbstbevorzugung oder Behinderung betroffen sind.
- KI-VO Art. 3 Nr. 1, Art. 6 Abs. 2 i. V. m. Anhang III nur, wenn das Pricing-System in einen Hochrisikokontext rutscht; meist liegt der Schwerpunkt kartellrechtlich.
- DMA/DSA/Plattformregeln prüfen, wenn Gatekeeper, Marktplätze oder Ranking-/Recommender-Systeme beteiligt sind.
- Behördenpraxis von Bundeskartellamt, Kommission/DA Competition, CMA/FTC/DOJ nur mit aktueller Quelle einbauen.

## Kartellrechtliche Leitfragen

1. Fließen Wettbewerberdaten in dasselbe System?
2. Gibt es einen gemeinsamen Dienstleister als Hub?
3. Werden Preise automatisch an Wettbewerberpreise angepasst?
4. Können Mitarbeitende Signale setzen oder auslesen?
5. Werden zukünftige Preise, Rabatte oder Kapazitäten geteilt?
6. Gibt es menschliche Kontrolle oder nur Algorithmus-Autopilot?
7. Sind Preisregeln vom Vertrieb vorgegeben, vom Anbieter trainiert oder durch Wettbewerberdaten emergent entstanden?
8. Wird künftiges Verhalten sichtbar gemacht: Preisfenster, Kapazität, Lieferstopp, Rabattuntergrenze?
9. Gibt es Audit-Logs, mit denen ein Unternehmen im Dawn Raid erklären kann, warum ein Preis gesetzt wurde?

## Compliance-Design

- Datenminimierung.
- Wettbewerberdaten nur aus rechtmäßigen öffentlichen Quellen.
- keine Zukunftsdaten.
- Anbieter-Firewalls.
- Logging von Preisentscheidungen.
- Kartellrechtliche Schulung für Revenue Teams.

## Output

- Pricing-AI-Freigabevermerk.
- Red-Flag-Liste für Vertrieb.
- Fragen an Softwareanbieter.
- Notfallplan bei Behördenanfrage.
- Dawn-Raid-Fragenkatalog für Pricing-, Data-Science- und Revenue-Management-Teams.

## Merksatz

Ein Algorithmus kann ein Kartell nicht entschuldigen. Er kann aber dessen Beweisbild komplizierter machen.

## 4. `anbieter-werden-art-25`

**Fokus:** Betreiber Einführer oder Haendler fragt: Werde ich durch mein Verhalten selbst zum Anbieter eines KI-Systems mit allen daraus folgenden Pflichten? Art. 25 KI-VO Re-Provisioning. Prüfraster: vier Fallgruppen wesentliche Aenderung des Systems Bestimmungsaenderung Inverkehrbringen unter eigenem Namen Hochrisiko-Abdeckung ohne Anbieterbenennung. Output: Entscheidungsbaum mit Ja/Nein-Ergebnis und konkreten Folgepflichten. Abgrenzung zu rolle-anbieter-prüfen-art-3-nr-3 (Grunddefinition) und betreiber-deployer-pflichten-art-26 (Betreiberpflichten).

# Anbieter-Werden — Art. 25 KI-VO

## Zweck

Art. 25 KI-VO ist eine zentrale Schutznorm der KI-VO: Sie verhindert, dass Akteure durch die Wahl einer bestimmten Rolle in der Lieferkette den strengen Anbieter-Pflichten ausweichen. Wer unter bestimmten Umständen ein KI-System weiterverbreitet oder verändert, wird selbst zum Anbieter — mit allen Konsequenzen.

## Vier Fallgruppen (Art. 25 Abs. 1 KI-VO)

### Fallgruppe 1 — Inverkehrbringen unter eigenem Namen oder eigener Marke

Wer ein Hochrisiko-KI-System oder GPAI-Modell unter seinem eigenen Namen oder seiner eigenen Marke in Verkehr bringt, wird Anbieter — unabhängig davon, ob er das System selbst entwickelt hat.

**Prüffragen:**
- Bringen Sie ein fremdes KI-System unter Ihrem eigenen Namen oder Ihrer Marke auf den Markt?
- Erscheint der ursprüngliche Anbieter im Vertrag, in der Dokumentation oder gegenüber dem Endkunden noch sichtbar?

**Wenn ja zum ersten, nein zum zweiten:** → Sie werden Anbieter nach Art. 25 Abs. 1 lit. a KI-VO.

**Konsequenz:** Sie müssen alle Anbieter-Pflichten nach Art. 16 bis 42 KI-VO erfüllen, einschließlich Konformitätsbewertung, CE-Kennzeichnung, EU-Konformitätserklärung und Registrierung in der EU-Datenbank.

### Fallgruppe 2 — Wesentliche Änderung nach dem Inverkehrbringen

Ein Betreiber oder Händler, der ein bereits in Verkehr gebrachtes Hochrisiko-KI-System wesentlich verändert, wird Anbieter.

**Was ist eine wesentliche Änderung?**

Nach Art. 3 Nr. 23 KI-VO ist eine wesentliche Änderung eine Änderung des KI-Systems nach seinem Inverkehrbringen, die die Konformität des Systems mit den Anforderungen beeinflussen kann oder die dazu führt, dass sich der Verwendungszweck, für den das KI-System bewertet wurde, verändert.

**Beispiele für wesentliche Änderungen:**
- Erneutes Training des Modells mit neuen Daten
- Änderung der Modellarchitektur
- Anpassung der Ausgaben des Systems in einer Weise, die neue Entscheidungen ermöglicht
- Erweiterung des Einsatzbereichs auf neue Nutzergruppen oder neue Entscheidungstypen
- Konfiguration, die zu einer Änderung der Systemfunktionalität führt

**Prüffragen:**
- Haben Sie technische Änderungen am System vorgenommen (Code, Modell, Parameter)?
- Haben Sie den Einsatzbereich oder die Zielgruppe verändert?
- Haben Sie Konfigurationen vorgenommen, die über die vom Anbieter vorgesehenen Optionen hinausgehen?

### Fallgruppe 3 — Änderung des bestimmungsgemäßen Verwendungszwecks

Wer das KI-System für einen anderen als den ursprünglich vorgesehenen Zweck einsetzt, wird Anbieter — auch ohne technische Änderung.

**Beispiele:**
- Ein Personalverwaltungs-Tool wird für die Bonitätsprüfung genutzt
- Ein Bildklassifikationssystem für die Qualitätskontrolle wird für die Gesichtserkennung genutzt
- Ein Text-Zusammenfassungstool wird für automatisierte Rechtsentscheidungen genutzt

**Prüffragen:**
- Ist der tatsächliche Einsatzzweck identisch mit dem in der Gebrauchsanweisung des Anbieters beschriebenen Zweck?
- Haben Sie das System für Entscheidungen genutzt, die der Anbieter nicht vorgesehen hat?

### Fallgruppe 4 — Produkthersteller (Art. 25 Abs. 1 lit. c KI-VO)

Ein Hersteller eines Produkts, das ein Hochrisiko-KI-System als Sicherheitsbauteil enthält, wird Anbieter des Hochrisiko-KI-Systems, wenn er das Produkt unter seinem eigenen Namen in Verkehr bringt.

→ Details: `bevollmaechtigter-und-produkthersteller-pflichten-art-22-und-25`

## Informationspflicht des ursprünglichen Anbieters (Art. 25 Abs. 2 KI-VO)

Der ursprüngliche Anbieter muss dem neuen Anbieter (nach Art. 25) alle notwendigen Informationen bereitstellen, damit dieser seine Anbieter-Pflichten erfüllen kann. Dies ist vertraglich zu regeln.

## Praktische Empfehlung

Vor jeder Anpassung oder Umwidmung eines KI-Systems sollte geprüft werden:
1. Überschreitet die Maßnahme die Schwelle zur wesentlichen Änderung?
2. Liegt eine Zweckänderung vor?
3. Wenn ja: Welche Anbieter-Pflichten müssen erfüllt werden?
4. Sind die entsprechenden Ressourcen (technische Dokumentation, Konformitätsbewertung) vorhanden?

---

Hinweis: Keine Rechtsberatung. Mechanische Prüfung anhand vom Nutzer behaupteter Tatsachen. Die KI-VO ist in Auslegung und Konkretisierung dynamisch; Leitlinien der Kommission und Durchführungsrechtsakte sind laufend zu beobachten.

## Aktuelle Rechtsprechung (v14.2)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)
- Art. 3 Nr. 3/4 KI-VO — Anbieter / Betreiber-Definition
- Art. 5 KI-VO — verbotene Praktiken (absolut ab 02.02.2025)
- Art. 6 i.V.m. Anhang III KI-VO — Hochrisiko-Klassifikation
- Art. 26 KI-VO — Betreiberpflichten
- Art. 99 KI-VO — Bussgelder bis 35 Mio. EUR / 7 % Jahresumsatz

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Triage zu Beginn
1. Welche Rolle hat das Unternehmen im KI-Lieferkette (Art. 3 KI-VO — Anbieter, Betreiber, Importeur)?
2. Liegt ein Hochrisiko-System vor (Art. 6 i.V.m. Anhang III Nr. 1-8 KI-VO)?
3. Sind verbotene Praktiken nach Art. 5 KI-VO ausgeschlossen?
4. Welche konkreten Pflichten aus dem aktuellen Skill-Kontext sind einschlaegig?
5. Ist die Massnahme fristgerecht umgesetzt (KI-VO Stufenplan bis 02.08.2026)?

## Output-Template — Pruefergebnis
**Adressat:** Pruefer / Rechtsberater — Tonfall: strukturiert-rechtlich
```
PRUEFERGEBNIS — ANBIETER WERDEN ART 25
[DATUM] — System: [SYSTEMNAME] — Mandant: [NAME MANDANT]
[AKTENZEICHEN]

Gepruefte Norm(en): [Art. 25 Rn. 5]

Ergebnis:
[ ] Anforderung erfuellt
[ ] Anforderung nicht erfuellt — Massnahmen erforderlich:
 1. [MASSNAHME — Verantwortlicher: NAME — Frist: DATUM]
[ ] Nicht einschlaegig — Begruendung: [BEGRUENDUNG]

Sanktionsrisiko: [NIEDRIG / MITTEL / HOCH — bis [BETRAG] nach Art. 99 KI-VO]
Naechster Skill: [FOLGE-SKILL]
Geprueft: [NAME], [DATUM]
```
