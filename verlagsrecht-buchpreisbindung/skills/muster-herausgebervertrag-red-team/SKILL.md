---
name: muster-herausgebervertrag-red-team
description: "Red-Team-Prüfung eines Muster-Herausgebervertrags: Sammelwerk-Besonderheiten nach UrhG § 4, Beitragsautoren-Rechtekette, Vergütung, Haftung und Klauselanalyse."
---

# Muster-Herausgebervertrag: Red-Team-Prüfung

## Zweck dieses Skills

Analysiert systematisch einen typischen **Herausgebervertrag** auf problematische Klauseln. Der Herausgebervertrag unterscheidet sich wesentlich vom reinen Autorenvertrag: Der Herausgeber steht zwischen Verlag und den einzelnen Beitragsautoren, trägt die redaktionelle Verantwortung für das Sammelwerk und nimmt dabei eine besondere Rechtsposition ein.

Die Red-Team-Prüfung beleuchtet:
- Die rechtliche Doppelrolle des Herausgebers (Urheber des Sammelwerks nach § 4 UrhG + Vertragspartner des Verlags)
- Die Pflichten gegenüber Beitragsautoren und die damit verbundene Haftungsexposition
- Typische Klauseln, die die Rechte des Herausgebers einseitig beschränken oder ihm unzumutbare Haftungsrisiken aufbürden
- Die Vergütungsstruktur für Herausgeber vs. Beitragsautoren

## Rechtsgrundlagen

| Norm | Inhalt | Quelle (URL) |
|------|--------|-------------|
| UrhG § 4 | Sammelwerke und Datenbankwerke | https://www.gesetze-im-internet.de/urhg/__4.html |
| UrhG § 8 | Miturheber | https://www.gesetze-im-internet.de/urhg/__8.html |
| UrhG § 9 | Verbundene Werke | https://www.gesetze-im-internet.de/urhg/__9.html |
| UrhG § 31 | Nutzungsrechte | https://www.gesetze-im-internet.de/urhg/__31.html |
| UrhG § 32 | Angemessene Vergütung | https://www.gesetze-im-internet.de/urhg/__32.html |
| UrhG § 32a | Bestseller-Nachvergütung | https://www.gesetze-im-internet.de/urhg/__32a.html |
| UrhG § 32d | Auskunftsanspruch | https://www.gesetze-im-internet.de/urhg/__32d.html |
| UrhG § 14 | Entstellungsverbot | https://www.gesetze-im-internet.de/urhg/__14.html |
| VerlG § 1 | Verlagsvertrag | https://www.gesetze-im-internet.de/verlg/__1.html |
| BGB §§ 305–310 | AGB-Kontrolle | https://www.gesetze-im-internet.de/bgb/__305.html |
| BGB § 278 | Haftung für Erfüllungsgehilfen | https://www.gesetze-im-internet.de/bgb/__278.html |

## Besonderheiten des Herausgebers gegenüber dem Autor

### Rechtsstellung nach UrhG § 4

Der **Herausgeber eines Sammelwerks** ist nach § 4 UrhG Urheber der Auswahl und Anordnung der Beiträge, nicht aber der Einzelbeiträge selbst. Daraus folgen wichtige Konsequenzen:

| Aspekt | Herausgeber | Beitragsautor |
|--------|-------------|---------------|
| Schutzgegenstand | Auswahl und Anordnung (§ 4 UrhG) | Einzelbeitrag (§ 2 UrhG) |
| Nutzungsrechte | Nur am Sammelwerk als Gesamtheit | An seinem Beitrag |
| Vergütungsanspruch | Aus Herausgebervertrag | Aus eigenem Autorenvertrag oder Honorarvereinbarung |
| Rückrufrecht § 41 | Gilt für Herausgeberleistung | Gilt für Einzelbeitrag |

### Doppelrolle und Haftungsrisiko

Der Herausgeber haftet dem Verlag gegenüber für:
1. Vollständige und termingerechte Ablieferung des Manuskripts inklusive aller Beiträge
2. Einholung und Weitergabe der Nutzungsrechte der Beitragsautoren
3. Richtigkeit der inhaltlichen Angaben (Sachbuch/Wissenschaft) soweit ihm zumutbar
4. Einhaltung formaler Vorgaben (Zeichenzahl, Formatierung, Zitationsstil)

Gleichzeitig ist er den Beitragsautoren gegenüber zur fairen Behandlung verpflichtet.

## Red-Team-Analyse: Klausel für Klausel

### 1. Rechteübertragungs- und Rechteketten-Klauseln

#### Typische Formulierung (problematisch)
> „Der Herausgeber versichert, dass er berechtigt ist, dem Verlag die ausschließlichen Nutzungsrechte an sämtlichen Beiträgen einzuräumen."

#### Red-Team-Bewertung

| Problem | Rechtliche Grundlage | Empfehlung |
|---------|---------------------|------------|
| Herausgeber kann Rechte der Beitragsautoren nicht selbst einräumen | UrhG § 31: Nutzungsrechte müssen vom Rechteinhaber (= Beitragsautor) eingeräumt werden | Klausel: „Herausgeber stellt sicher, dass jeder Beitragsautor dem Verlag schriftlich die Nutzungsrechte einräumt" |
| Keine Beschreibung der erforderlichen Beitragsautoren-Verträge | Lücke bei Rechtekette | Anlage: Muster-Beitragsvereinbarung als Vertragsbestandteil |
| Haftung für Urheberrechtsverletzungen in Beiträgen | BGB § 278 (Erfüllungsgehilfe) | Haftungsbeschränkung: Nur bei Vorsatz oder grober Fahrlässigkeit des Herausgebers |

### 2. Vergütungsklauseln des Herausgebers

#### Typische Formulierung (problematisch)
> „Der Herausgeber erhält als Pauschalhonorar EUR 2.000 je Herausgeberband. Weitere Ansprüche bestehen nicht."

#### Red-Team-Bewertung

| Problem | Rechtliche Grundlage | Empfehlung |
|---------|---------------------|------------|
| „Weitere Ansprüche bestehen nicht" schließt § 32a aus | UrhG § 32a: unverzichtbar | Klausel streichen oder durch Staffelhonorar ersetzen |
| Pauschalhonorar ohne Bezug zum Werk-Erfolg | Unangemessen bei Erfolgswerk | Alternativ: Absatzhonorar 3–5 % des Ladenpreises |
| Keine Regelung der Beitragsautoren-Vergütung | Unklar, wer zahlt | Verklären: Verlag zahlt Beitragsautoren direkt, oder Herausgeber verteilt Gesamtbetrag |

### 3. Ablieferungspflichten und Beitragsausfallrisiko

#### Typische Formulierung (problematisch)
> „Bei Nichtablieferung eines oder mehrerer Beiträge haftet der Herausgeber für alle dadurch entstehenden Mehrkosten."

#### Red-Team-Bewertung

- Das Beitragsausfallrisiko liegt grundsätzlich **nicht beim Herausgeber**, wenn er alle zumutbaren Schritte zur Einwerbung der Beiträge unternommen hat.
- Empfehlung: Klausel auf **Verschulden des Herausgebers** begrenzen. Herausgeber haftet nur, wenn er Beitragsautor unzureichend gemahnt oder vertraglich nicht abgesichert hat.
- Ausfalllösung vertraglich regeln: Herausgeber darf Ersatzbeitrag einwerben oder Beitrag selbst verfassen (Aufwandsvergütung geregelt).

### 4. Inhaltliche Überarbeitungs- und Ablehnungsrechte des Verlags

#### Typische Formulierung (problematisch)
> „Der Verlag ist berechtigt, einzelne Beiträge ohne Angabe von Gründen abzulehnen."

#### Red-Team-Bewertung

- Herausgeber und Beitragsautoren haben ein **Entstellungsverbot** nach § 14 UrhG. Willkürliche Ablehnung kann dieses verletzen.
- **Urheberpersönlichkeitsrecht** des Beitragsautors kann verletzt sein, wenn sein Beitrag ohne sachlichen Grund aus dem Sammelwerk entfernt wird.
- Empfehlung: Ablehnung nur aus sachlichem Grund (inhaltliche Qualität, Umfang-Überschreitung, Redundanz); Herausgeber muss Gelegenheit zur Nachbesserung einräumen.

### 5. Namentliche Nennung und Titelrecht

#### Typische Formulierung (problematisch)
> „Das Sammelwerk erscheint unter dem Titel [X] mit dem Herausgeber auf dem Titelblatt. Der Verlag kann den Titel ändern."

#### Red-Team-Bewertung

| Problem | Empfehlung |
|---------|------------|
| Titeljänderung ohne Zustimmung des Herausgebers | Zustimmungsvorbehalt einbauen |
| Namentliche Nennung von Beitragsautoren ungeregelt | Pflicht zur Nennung aller Beitragsautoren im Inhaltsverzeichnis und auf dem Titelblatt |
| Reihenfolge der Herausgeber bei mehreren | Alphabetisch oder nach Beitrag; muss vereinbart sein |

### 6. Laufzeit und Folgeauflagen

#### Typische Formulierung (problematisch)
> „Bei Neuauflagen ist der Herausgeber zur Aktualisierung verpflichtet; eine gesonderte Vergütung erfolgt nicht."

#### Red-Team-Bewertung

- Jede **Überarbeitung für eine neue Auflage** ist eine selbständige Werkleistung und begründet einen neuen Vergütungsanspruch.
- Die Verpflichtung zur unbezahlten Aktualisierung verletzt § 32 UrhG (angemessene Vergütung).
- Empfehlung: Für jede Neuauflage separates Honorar (mindestens 50 % des Ursprungshonorars bei wesentlicher Überarbeitung).

### 7. Haftung für Inhalt der Beiträge

#### Typische Formulierung (problematisch)
> „Der Herausgeber haftet gesamtschuldnerisch mit den Beitragsautoren für alle rechtlichen Beanstandungen."

#### Red-Team-Bewertung

- Gesamtschuldnerische Haftung ist für den Herausgeber **unbillig**, wenn er inhaltlich nicht in jeden Beitrag eingewirkt hat.
- Empfehlung: Herausgeber haftet nur für eigene Beiträge und für die Auswahl und Anordnung (§ 4 UrhG-Leistung); für Einzelbeiträge haftet primär der Beitragsautor.
- Internen Ausgleich regeln: Freistellungsanspruch des Herausgebers gegenüber Beitragsautoren.

### 8. Rechte bei Auflösung des Sammelwerks

| Szenario | Problem | Empfehlung |
|----------|---------|------------|
| Verlag gibt Sammelwerk auf | Rechte der Beitragsautoren bleiben gebunden? | Rückfall-Klausel für alle Beiträge bei Einstellung der Verwertung |
| Herausgeber stirbt/scheidet aus | Wer übernimmt Herausgeberrolle? | Nachfolge-Regelung oder Rückgabe der Rechte an Verlag mit Neuherausgeber-Option |
| Beitragsautor will eigenen Beitrag separat verwerten | Sammelwerk-Recht und Einzelbeitrag | Beitragsautor behält Recht zur Separat-Verwertung nach X Jahren |

## Checkliste Beitragsautoren-Verträge (Rechtekette)

Damit die Rechtekette vom Beitragsautor über den Herausgeber zum Verlag lückenlos ist:

- [ ] Schriftliche Beitragsvereinbarung mit jedem Beitragsautor
- [ ] Nutzungsrechte: Welche Nutzungsarten? (Print, E-Book, Datenbank, Übersetzung)
- [ ] Vergütung des Beitragsautors geregelt (Belegexemplare, Honorar oder unentgeltlich für Sammelband?)
- [ ] Zustimmung zur redaktionellen Bearbeitung durch Herausgeber
- [ ] § 32d-Auskunftspflicht gegenüber Beitragsautor sichergestellt
- [ ] Beitragsautor behält Recht zur Separat-Verwertung nach Sperrfrist?
- [ ] Rückrufrecht bei Vergriffenheit des Sammelbands geregelt?

## Typische Fallen

- **Rechtekette reißt**: Herausgeber versichert Rechteinhaber zu sein, ohne Beitragsautoren-Verträge zu haben → Haftung gegenüber Verlag.
- **Unklare Herausgeberleistung**: Vertrag definiert nicht, was der Herausgeber konkret schuldet (Einleitung? Redaktion? Peer Review?) → Streit über Pflichten.
- **Vergütung nicht dynamisiert**: Pauschalhonorar ohne Inflationsanpassung oder Neublatt-Vergütung bei mehrjähriger Loseblatt-Reihe.
- **Beitragsautor-Rückfragen nicht geregelt**: Wer beantwortet Fragen der Beitragsautoren zu Abrechnungen? Herausgeber oder Verlag?
- **Gerichtsstand Verlagsort**: Für Herausgeber in anderen Städten aufwendig.

## Checkliste Red-Team-Herausgebervertrag

- [ ] § 4 UrhG-Schutzposition des Herausgebers klar definiert?
- [ ] Rechtekette Beitragsautor → Herausgeber → Verlag lückenlos?
- [ ] Beitragsausfallrisiko fair verteilt (kein unverschuldetes Herausgeber-Risiko)?
- [ ] Vergütung des Herausgebers angemessen (§ 32 UrhG)?
- [ ] § 32a-Beteiligung nicht ausgeschlossen?
- [ ] Herausgeber-Auskunftsanspruch nach § 32d UrhG gesichert?
- [ ] Haftung auf eigenes Verschulden begrenzt?
- [ ] Inhaltliche Änderungsrechte des Verlags beschränkt?
- [ ] Neuauflagen-Vergütung geregelt?
- [ ] Rückfall der Beitragsrechte bei Vergriffenheit geregelt?

## Quellenreferenzen

- UrhG § 4: https://www.gesetze-im-internet.de/urhg/__4.html
- UrhG § 8: https://www.gesetze-im-internet.de/urhg/__8.html
- UrhG § 14: https://www.gesetze-im-internet.de/urhg/__14.html
- UrhG § 32: https://www.gesetze-im-internet.de/urhg/__32.html
- UrhG § 32a: https://www.gesetze-im-internet.de/urhg/__32a.html
- UrhG § 32d: https://www.gesetze-im-internet.de/urhg/__32d.html
- BGB § 278: https://www.gesetze-im-internet.de/bgb/__278.html
- BGB § 307: https://www.gesetze-im-internet.de/bgb/__307.html
- dejure.org UrhG § 4: https://dejure.org/gesetze/UrhG/4.html

## Output-Formate

- Klausel-Kommentar-Tabelle (Originalklausel / Red-Team-Bewertung / Empfehlung)
- Muster-Beitragsvereinbarung (Rechteketten-Vorlage für Herausgeber)
- Checkliste Herausgebervertrag-Prüfung
- Haftungsmatrix Herausgeber–Beitragsautor–Verlag
- Ablaufdiagramm Rechtekette im Sammelwerk

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig. Diese Regel folgt der zentralen Vorgabe in der `CLAUDE.md` des Repos und gilt ausnahmslos.
<!-- END ausformulierungspflicht (autogen) -->

