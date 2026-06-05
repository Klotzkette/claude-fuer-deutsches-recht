---
name: fachanwalt-sportrecht-sportr-athletenvertrag
description: "Sportr Athletenvertrag: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Sportr Athletenvertrag

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Sportr Athletenvertrag** im Plugin Fachanwalt Sportrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `fachanwalt-sportrecht-transferklausel` | Profi-Sportler will Verein wechseln und braucht Prüfung von Transfervertrag Ausstiegsklausel Transferperiode. FIFA/UEFA-Statuten Wechselgebühr. Normen FIFA RSTP Art. 17 18 UEFA-Transferregeln DFB-Lizenzordnung. Prüfraster Ausstiegsklausel-Hoehe Transfer-Fenster Solidaritaetsmechanismus Vertragsbruch-Risiko. Output Vertrags-Prüfungsbericht Verhandlungs-Strategie Klage-Optionen. Abgrenzung zu fachanwalt-sportrecht-spielervertrag (Arbeitsvertrag) und fachanwalt-sportrecht-cas-dis-sport-verbands-schiedsverfahren (Schiedsgericht). |
| `sportr-athletenvertrag-bauleiter` | Bauleiter Athletenvertrag: Verguetung, Image- und Vermarktungsrechte, Trainingspflichten, Wettkampfteilnahme, Dopingklausel, Beendigung. Pruefraster Verband und Vereinsperspektive. |
| `fachanwalt-sportrecht-esports-vereinsrecht-dosb-anerkennung` | eSports-Organisator oder Verein fragt ob DOSB-Anerkennung möglich und wie steuerliche Gemeinnuetzigkeit erreichbar ist. § 52 AO Gemeinnuetzigkeit § 21 BGB Vereinsrecht. Normen §§ 21 ff. BGB § 52 AO DOSB-Satzung. Prüfraster DOSB-Aufnahme-Kriterien Gemeinnuetzigkeits-Prüfung Vereinstyp-Wahl. Output Rechtsstruktur-Empfehlung Satzungs-Entwurf Finanzamt-Antrag. Abgrenzung zu fachanwalt-sportrecht-vereinsstrafrecht (Vereinsstrafe) und mandat-triage-sportrecht (Erstabfrage). |

## Arbeitsweg

Im Plugin Fachanwalt Sportrecht gilt für **Sportr Athletenvertrag**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `fachanwalt-sportrecht-transferklausel`

**Fokus:** Profi-Sportler will Verein wechseln und braucht Prüfung von Transfervertrag Ausstiegsklausel Transferperiode. FIFA/UEFA-Statuten Wechselgebühr. Normen FIFA RSTP Art. 17 18 UEFA-Transferregeln DFB-Lizenzordnung. Prüfraster Ausstiegsklausel-Hoehe Transfer-Fenster Solidaritaetsmechanismus Vertragsbruch-Risiko. Output Vertrags-Prüfungsbericht Verhandlungs-Strategie Klage-Optionen. Abgrenzung zu fachanwalt-sportrecht-spielervertrag (Arbeitsvertrag) und fachanwalt-sportrecht-cas-dis-sport-verbands-schiedsverfahren (Schiedsgericht).

# Spieler-Transfer-Klausel

## Zweck

Beratung Profi-Sportler bei Vertrag-Verhandlung / Transfer.

## 1) Eingangs-Abfrage

1. Sport / Verband (FIFA, UEFA, DFB, NBA)?
2. Aktueller Vertrag (Laufzeit, Klauseln)?
3. Wechsel-Wunsch oder Verbleib-Sicherung?
4. Transferperiode aktuell?
5. Ausstiegs-Klausel im Vertrag?

## 2) FIFA-Statuten Profis

### Transfer-Periode

- Sommer-Periode ca. Juni-August
- Winter-Periode ca. Januar
- Außerhalb: keine Transfers

### TMS — Transfer Matching System

- Pflicht-Eintragung
- ITC (International Transfer Certificate)

## 3) Vertragsklauseln

### Ausstiegs-Klausel

- Festgelegter Betrag, gegen Zahlung Spieler frei
- Liga-abhängig (Spanien Standard, DE seltener)
- Marktwert kann erheblich abweichen

### Verlängerungs-Optionen

- Einseitige Option Verein
- Reziprok-Klausel (auch Spieler kann widerrufen)

### Eigenrechte (Persönlichkeitsrechte)

- Bildrechte (Image Rights)
- Werbeauftritte
- Spielerrechte vs. Vereinsrechte

## 4) Konfliktlösung

### Schiedsgerichtsbarkeit FIFA

- TMS-Spruchkammer
- DRC (Dispute Resolution Chamber) FIFA
- CAS-Berufung

### Bei DE-Verband

- Schiedsgericht DFB
- Verbands-Gericht

## 5) Vertrags-Beendigung

### Just Cause § 14 FIFA-Statuten

- Wesentliche Vertragsverletzung
- Beispiele: nicht-Zahlung Gehalt, Mobbing, Karriere-Behinderung
- Recht zur fristlosen Kündigung Spieler

### Sporting Just Cause § 15 FIFA-Statuten

- Bei nicht-Spielzeit (etablierter Profi < 10 % Einsätze)
- Standortwechsel-Recht

## 6) Vertrags-Beratung

### Phase 1 — Vertrag

- Ausstiegs-Klausel
- Verlängerungs-Option
- Image Rights

### Phase 2 — Transfer-Sondierung

- Interessenten-Vereine
- Anwalt + Berater

### Phase 3 — Verhandlung

- Wechsel-Bedingungen
- Gehalts-Erhöhung
- Bonus-Regelungen

### Phase 4 — Abschluss

- Spielervertrag neuer Verein
- Auflosung alter Vertrag
- TMS-Eintragung

## 7) Konkrete BGH-/CAS-Linien

- CAS Webster vs. Heart of Midlothian (Art. 17 FIFA-Statuten)
- CAS Matuzalem (Auflösungs-Schadenersatz)

## 8) Spieler-Berater § 14 RegBerVO

- Lizenz-Pflicht durch FIFA bis 2015, dann frei, jetzt wieder reguliert
- Beratungs-Provision typisch 5-10 % Jahres-Gehalt

## 9) Typische Fehler

1. **Ausstiegs-Klausel ohne Inhalt**
2. **Image Rights nicht separat geregelt**
3. **Transferperiode verpasst**
4. **Just-Cause-Prüfung versäumt** bei Spieler-Beschwerde

## Anschluss

- `fachanwalt-sportrecht-orientierung` — Triage
- `fachanwalt-sportrecht-doping-cas-berufung` — bei Doping-Bezug
- `cas-berufung-vorbereiten` — bei CAS-Verfahren

## Ergaenzende Rechtsprechung Transferklausel

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- CAS 2017/A/5379 (Borussia Dortmund v. Aubameyang) — Transfer-Verguetungsanspruch: Ablosegebuebre und Weiterverkaufsbeteiligung muessen in Transfer-Agreement praezise geregelt sein; pauschal-prozentuale Klauseln sind grundsaetzlich wirksam, aber auslegungsbeduerftiger Wortlaut geht zu Lasten des Verfassers.

## 2. `sportr-athletenvertrag-bauleiter`

**Fokus:** Bauleiter Athletenvertrag: Verguetung, Image- und Vermarktungsrechte, Trainingspflichten, Wettkampfteilnahme, Dopingklausel, Beendigung. Pruefraster Verband und Vereinsperspektive.

# Sport: Athletenvertrag Bauleiter

## Spezialwissen: Sport: Athletenvertrag Bauleiter
- **Spezialgegenstand:** Sport: Athletenvertrag Bauleiter / sportr athletenvertrag bauleiter. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** einschlägige Fachnormen, Behördenhinweise, Formulare, Verfahrensrecht und frei prüfbare Rechtsprechung live prüfen.
- **Entscheidende Weiche:** Aus dem Sachverhalt sind Tatbestandsmerkmal, Zuständigkeit, Frist, Beweislast, Ermessen/Wertung und Rechtsfolge getrennt herauszuarbeiten; offene Tatsachen werden als offen markiert.
- **Arbeitsprodukt:** Erzeuge eine fallbezogene Matrix `Norm / Tatsache / Beleg / Gegenargument / Risiko / nächster Schritt` plus einen direkt verwendbaren Baustein für Vermerk, Schreiben, Antrag, Schriftsatz oder Entscheidungsvorlage.


## Fallweichen
Frage zu Beginn nur ab, was fuer den naechsten Schritt unverzichtbar ist. Wenn Material vorliegt, mit dem Material arbeiten und nur eine gezielte Rueckfrage stellen.

1. **Rolle und Ziel:** Wer fragt, welche Rolle, welcher gewuenschte Output (Memo, Schriftsatz, Tabelle, Checkliste)?
2. **Sachverhalt:** Welche unstreitigen Tatsachen liegen vor, was ist streitig, was fehlt noch?
3. **Fristen:** Gibt es Termine, Fristen, eilbeduerftige Schritte?
4. **Unterlagen:** Welche Dokumente, Bescheide, Vertraege, Auszuege liegen vor?
5. **Format:** Wie ausfuehrlich, fuer wen, in welcher Tonalitaet?

## Pruefraster

Der Output muss als verwertbares Arbeitsprodukt aufgebaut sein:

1. **Sachverhalt fixieren** - streitige und unstreitige Tatsachen trennen, Lueckentafel.
2. **Rechtliche Einordnung** - einschlaegige Normen, Rechtsprechung BGH/BVerfG/EuGH, Literatur.
3. **Pruefung im Gutachtenstil** - Obersatz, Definition, Subsumtion, Zwischenergebnis.
4. **Handlungsempfehlung** - konkret, mit naechstem Schritt, verantwortlicher Person, Frist.

## Plugin-Kontext
Dieses Fachmodul arbeitet den konkreten Schwerpunkt aus, prüft Aktenlage, Normen, Fristen, Belege und Gegenargumente und erzeugt einen unmittelbar nutzbaren nächsten Schritt.

## Output-Module
- Strukturierter Pruefvermerk im Gutachtenstil mit klaren Ueberschriften.
- Tabellen und Checklisten, wo das die Lesbarkeit erhoeht.
- Anschreiben-, Antrags- oder Klageschriftsatz-Geruest, wenn die Aufgabe das verlangt.
- Quellenliste mit Gericht, Datum, Aktenzeichen, frei pruefbarem Link.

## Quellenregel
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei pruefbarem Link (`dejure.org`, `openjur.de`, `bundesgerichtshof.de`, `bundesverfassungsgericht.de`, `curia.europa.eu`).
- Keine Zitate aus `anwalt24.de`. Keine `BeckRS` als alleinige Fundstelle bei tragenden Aussagen.
- Aufsaetze mit Verfasser, Zeitschrift, Jahr, Heft (falls relevant) und Seite.
- Kommentare mit Bearbeiter und Randnummer.
- Annahmen explizit als solche kennzeichnen, keine Erfindungen.

## Was dieser Arbeitsgang nicht macht
- Kein Ersatz fuer eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.

## 3. `fachanwalt-sportrecht-esports-vereinsrecht-dosb-anerkennung`

**Fokus:** eSports-Organisator oder Verein fragt ob DOSB-Anerkennung möglich und wie steuerliche Gemeinnuetzigkeit erreichbar ist. § 52 AO Gemeinnuetzigkeit § 21 BGB Vereinsrecht. Normen §§ 21 ff. BGB § 52 AO DOSB-Satzung. Prüfraster DOSB-Aufnahme-Kriterien Gemeinnuetzigkeits-Prüfung Vereinstyp-Wahl. Output Rechtsstruktur-Empfehlung Satzungs-Entwurf Finanzamt-Antrag. Abgrenzung zu fachanwalt-sportrecht-vereinsstrafrecht (Vereinsstrafe) und mandat-triage-sportrecht (Erstabfrage).

# eSports-Verein — Vereinsrecht und DOSB-Anerkennung

## Zweck

Spezial-Mandat: Mandant möchte eSports-Verein gründen oder einen eSports-Bereich in einen bestehenden Sportverein integrieren. Zwei zentrale Rechtsfragen: (1) Ist eSports "Sport" i.S.d. § 52 AO (gemeinnützig)? — aktuell strittig. (2) DOSB / LSB-Anerkennung als Spitzenverband: nicht erfolgt.

## Eingaben

- Bestehende Vereinsstruktur (Neugründung / bestehender Sportverein)
- eSports-Sparte (Counter-Strike, League of Legends, FIFA, Dota etc.)
- Geplante Aktivität (Liga-Teilnahme, Trainings-Bootcamps, Turniere)
- Mitgliederstruktur (Hobby, semi-professionell)
- Bisherige Finanzamt-Korrespondenz (Gemeinnützigkeits-Anerkennung)
- DOSB-/LSB-Anbindung gewünscht?

## Rechtlicher Rahmen

- **§§ 21 ff. BGB** — Verein
- **§ 25 BGB** — Vereinsregister
- **§ 52 Abs. 2 Nr. 21 AO** — "Förderung des Sports (Schach gilt als Sport)" — eSports umstritten
- **§ 51 ff. AO** — Steuerbegünstigte Zwecke; Gemeinnützigkeit
- **§ 67a AO** — Sportveranstaltungen-Befreiung
- **§ 23 EStG** — Privates Veräußerungsgeschäft bei Profi-eSports

### Gerichts-/Verwaltungsentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- FinMin NRW Erlass 2024 zu eSports-Verein-Gemeinnützigkeit (eSports nicht als Sport § 52 AO anerkannt)
- DOSB-Beschluss 2018 (eSports keine Mitgliedssportart) — bis 2026 unverändert

## Strategische Optionen

### Option A — Hauptverein mit eSports-Sparte

- Sportverein (anerkannte Sportart) mit eSports-Sparte
- Gemeinnützigkeit der Hauptsportart bleibt erhalten
- eSports-Sparte als untergeordneter Zweck
- ABER: Wenn eSports überwiegt → Aberkennung Gemeinnützigkeit

### Option B — Eigenständiger eSports-Verein

- Voll eigenständig
- Aktuell **keine Gemeinnützigkeit** möglich (FinMin-Linie)
- Status als "normaler" Verein § 21 BGB
- Spenden nicht steuerlich begünstigt

### Option C — eSports gGmbH

- Gemeinnützige GmbH mit eSports-Förderzweck
- Mehrfach versucht, von Finanzämtern abgelehnt
- Risiko: Aberkennung mit rückwirkender Versteuerung

## Neugründung

### Phase 1 — Strukturentscheidung

- Hauptverein-Sparte oder eigenständiger Verein?
- Verbindungsmöglichkeit zu DSchach / DOSB-anerkannte Sportart
- Steuerliche Modellrechnung

### Phase 2 — Satzung

- Vereinszweck: "Förderung des digitalen Sports / electronic Sports"
- Bei Hauptverein: eSports als Nebenzweck
- Anti-Doping (auch für Wettkampf-eSports)
- Jugendschutz (USK-Bezug)

### Phase 3 — Vereinsregister-Anmeldung

- Beim Amtsgericht (Registergericht)
- 7 Mitglieder Mindest-Anzahl
- Vorstand mit Vertretungsregel

### Phase 4 — Finanzamt

- Antrag auf Gemeinnützigkeit
- Bei Ablehnung: Widerspruch + ggf. Klage Finanzgericht
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Phase 5 — Verbandsanbindung

- Bei Hauptverein: Sparte beim Spitzenverband melden
- Bei Standalone: ESBD (eSport-Bund Deutschland) als alternative Mitgliedschaft

## Risiken und Red Flags

| Konstellation | Rot | Orange | Grün |
|---|---|---|---|
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | Live-Verifikation erforderlich | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| Profi-Spieler mit Gehalt aus Verein | Selbstlosigkeit § 55 AO verletzt | Klärung läuft | klare Trennung Profi-/Amateur-Bereich |
| Werbung / Sponsoring überwiegt | Wirtschaftsbetrieb statt Idealverein | Klärung läuft | Idealzweck-Schwerpunkt |
| Jugendschutz-Verstoß (USK) | Vereinsaufsicht; Imageschaden | Compliance läuft | USK-konforme Spiele |

## Querverweise

- `fachanwalt-sportrecht-orientierung` — Triage
- `fachanwalt-sportrecht-transferklausel` — bei Profi-eSports-Verträgen
- `fachanwalt-steuerrecht-...` (steuerrecht-anwalt-und-berater) — Gemeinnützigkeits-Beratung

## Quellen und Updates

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Aktuelle Rechtsprechung eSports / Vereinsrecht

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Normen eSports-Vereinsrecht

- § 21 BGB — eingetragener Verein; nicht wirtschaftlicher Verein
- § 22 BGB — wirtschaftlicher Verein (bei erwerbswirtschaftlichem Schwerpunkt-eSports)
- § 52 Abs. 2 Nr. 21 AO — Foerderung des Sports; eSports streitig
- § 51 AO — allgemeine Gemeinnuetzigkeitsvoraussetzungen
- § 67a AO — Sportveranstaltungen-Steuerbefreiung
- § 58 Nr. 7 AO — Mittelbeschaffungskoerperschaft als Ausweg
