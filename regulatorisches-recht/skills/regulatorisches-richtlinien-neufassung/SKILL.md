---
name: regulatorisches-richtlinien-neufassung
description: "Richtlinien Neufassung: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Richtlinien Neufassung

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Richtlinien Neufassung** im Plugin Regulatorisches Recht (Sektoren). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `regulatorisches-recht-anpassen` | Bestehende Richtlinien oder Compliance-Dokumente an neue regulatorische Anforderungen anpassen. KWG WpHG DORA DSGVO GwG aktuelle BaFin-Vorgaben. Prüfraster: Bestandsdokument Neuregelung Delta-Analyse Anpassungsbedarf. Output: ueberarbeitetes Dokument Aenderungsprotokoll. Abgrenzung: nicht für Neuerstellung von Richtlinien (richtlinien-neufassung). |
| `regulatorisches-recht-mandat-arbeitsbereich` | Regulatorisches Mandat strukturieren und Arbeitsbereich abgrenzen. KWG WpHG DORA VAG GwG BaFin. Prüfraster: Mandatsumfang Zuständigkeiten Fristen Risikostufe beteiligte Behoerden. Output: Mandatssteckbrief Arbeitsplan Rollenverteilung. Abgrenzung: nicht für inhaltliche Regulierungsprüfung. |
| `richtlinien-neufassung` | Interne Richtlinien und Unternehmensanweisungen auf regulatorischer Basis neu verfassen. KWG WpHG DORA DSGVO GwG MaRisk. Prüfraster: regulatorische Anforderungen Inhaltsstruktur Formulierungsstandard Genehmigungsweg. Output: neue Richtlinie Implementierungshinweise. Abgrenzung: nicht für Anpassung bestehender Richtlinien (regulatorisches-recht-anpassen). |

## Arbeitsweg

Im Plugin Regulatorisches Recht (Sektoren) gilt für **Richtlinien Neufassung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `regulatorisches-recht-anpassen`

**Fokus:** Bestehende Richtlinien oder Compliance-Dokumente an neue regulatorische Anforderungen anpassen. KWG WpHG DORA DSGVO GwG aktuelle BaFin-Vorgaben. Prüfraster: Bestandsdokument Neuregelung Delta-Analyse Anpassungsbedarf. Output: ueberarbeitetes Dokument Aenderungsprotokoll. Abgrenzung: nicht für Neuerstellung von Richtlinien (richtlinien-neufassung).

# Praxisprofil anpassen

## Zweck

Dieser Skill ermöglicht die gezielte Anpassung einzelner Parameter im Praxisprofil, ohne die vollständige Ersteinrichtung zu wiederholen. Einsatz: neue Behörde hinzufügen, Materialitätsschwelle nachjustieren, Richtlinienbibliothek aktualisieren, Feed-URL korrigieren, Rollenwechsel vornehmen.

## Eingaben

- Aktives Praxisprofil (muss vorhanden sein – sonst `regulatorisches-recht-kaltstart-interview` ausführen)
- Konkrete Angabe, was geändert werden soll

## Ablauf

### 1. Profilzustand prüfen

Praxisprofil aus `~/.claude/plugins/config/claude-fuer-deutsches-recht/regulatorisches-recht/CLAUDE.md` lesen. Falls `[PLATZHALTER]`-Marker vorhanden: zum `regulatorisches-recht-kaltstart-interview` umleiten.

### 2. Änderungswunsch klären

Dem Nutzer die Hauptkategorien anbieten:

```
Was soll angepasst werden?
a) Beobachtete Behörden (hinzufügen / entfernen)
b) Richtlinienbibliothek (Speicherort, neue Richtlinien, Verantwortliche)
c) Materialitätsschwelle (Stufen neu kalibrieren)
d) Feed-Konfiguration (URLs, Prüfrhythmus)
e) Gap-Response-Prozess (Triageperson, Eigentümer, Eskalationsweg)
f) Rolle (Rollenänderung des Nutzers)
g) Mandat-Workspaces (aktivieren / deaktivieren)
h) Sonstiges
```

### 3. Änderung durchführen

Nur den betroffenen Abschnitt des Praxisprofils aktualisieren. Restliche Konfiguration unberührt lassen. Änderung mit Datum versehen:

```
[Geändert am TT.MM.JJJJ: <Beschreibung der Änderung>]
```

### 4. Bestätigung

Geänderten Abschnitt dem Nutzer zur Bestätigung vorlegen, dann speichern.

### 5. Abhängige Einstellungen prüfen

- Bei Hinzufügen einer Behörde: Feed-URL und Prüfrhythmus ebenfalls erfassen.
- Bei Änderung der Materialitätsschwelle: Hinweis, dass der `aufsichts-feed-monitor` beim nächsten Lauf die neue Schwelle anwendet.
- Bei Änderung des Richtlinienspeichers: Hinweis, dass `richtlinien-vergleich` den neuen Pfad nutzt.

## Aktuelle Rechtsprechung & Leitsätze

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen

§§ 48, 49 VwVfG (Ruecknahme, Widerruf) — §§ 313, 314 BGB (Anpassung, Kuendigung bei Aenderung der Grundlage) — Art. 288 AEUV (Richtlinien-Anpassungspflicht)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Quellen und Zitierweise

Zitierweise: `../../../references/zitierweise.md`

Keine normativen Anforderungen an das Praxisprofil selbst. Inhaltliche Anforderungen richten sich nach dem Plugin-Zweck.

## Ausgabeformat

- Kurzbestätigung der Änderung
- Aktualisierten Abschnitt des Praxisprofils anzeigen

## Beispiel

**Eingabe:** "Bitte die BNetzA als weitere beobachtete Behörde hinzufügen. Feed: https://www.bundesnetzagentur.de/DE/Presse/RSS/rss_node.html"

**Ausgabe:**

> Praxisprofil aktualisiert:
>
> **Neu hinzugefügte Behörde:**
> | Behörde | Zuständigkeit | Beobachtungsgrund | Feed-Quelle |
> |---|---|---|---|
> | Bundesnetzagentur (BNetzA) | EnWG, TKG | Telekommunikationsregulierung | RSS: bundesnetzagentur.de/RSS |
>
> Gespeichert in `~/.claude/plugins/config/claude-fuer-deutsches-recht/regulatorisches-recht/CLAUDE.md` [Geändert am 01.06.2025]
>
> Hinweis: Der `aufsichts-feed-monitor` erfasst BNetzA-Einträge ab dem nächsten Lauf.

## Risiken / typische Fehler

- **Versehentliches Überschreiben:** Dieser Skill ändert nur den angegebenen Abschnitt. Nie das gesamte Profil überschreiben.
- **Ungültige Feed-URLs:** Feed-URL vor dem Speichern testen; defekte Feeds führen zu stillen Fehlern im `aufsichts-feed-monitor`.
- **Fehlende Neuindizierung:** Nach Änderung des Richtlinienspeichers muss die Bibliothek neu indiziert werden. Hinweis geben.

## 2. `regulatorisches-recht-mandat-arbeitsbereich`

**Fokus:** Regulatorisches Mandat strukturieren und Arbeitsbereich abgrenzen. KWG WpHG DORA VAG GwG BaFin. Prüfraster: Mandatsumfang Zuständigkeiten Fristen Risikostufe beteiligte Behoerden. Output: Mandatssteckbrief Arbeitsplan Rollenverteilung. Abgrenzung: nicht für inhaltliche Regulierungsprüfung.

# Mandat-Workspace-Verwaltung

## Zweck

Dieser Skill verwaltet Mandat-Workspaces für Kanzleien mit mehreren Mandanten. Im regulatorischen Recht ist ein "Mandat" typischerweise:
- Ein bestimmter Regulierungsakt, zu dem ein Mandant beraten wird (z. B. MaRisk-Novelle-Implementierung)
- Ein offenes Konsultationsverfahren, für das eine Stellungnahme erstellt wird
- Eine BaFin-Prüfung oder eine DORA-GAP-Analyse für einen bestimmten Mandanten
- Ein Anfrageverfahren oder eine Abgrenzungsanfrage an eine Behörde

**Inhouse-Nutzer:** Dieser Skill ist nicht relevant. Das Praxisprofil gilt für das gesamte Unternehmen.

## Eingaben

- Aktives Praxisprofil mit aktivierten Mandat-Workspaces
- Mandat-Subkommando: `neu | auflisten | wechseln | schließen | keiner`
- Optional: Mandat-Name, Mandant, Rechtsgebiet, Frist

## Ablauf

### Subkommando: `neu`

Abfragen:
```
1. Mandant (intern: nur Kürzel, kein vollständiger Name in Logs)
2. Mandat-Bezeichnung / Slug (z. B. bafin-prüfung-2025-mandantA)
3. Art des Mandats:
 a) Gap-Analyse gegen Regulierungsakt
 b) Konsultationsbeitrag
 c) Richtlinienneufassung
 d) Behördenanfrage
 e) Sonstiges
4. Zuständige Behörde(n)
5. Leitfrist (falls bekannt)
```

Mandatsordner anlegen:
```
~/.claude/plugins/config/claude-fuer-deutsches-recht/regulatorisches-recht/mandate/<mandat-slug>/
├── mandat.md # Mandat-Fakten und Übersteuerungen
├── gap-tracker.yaml # Mandat-spezifische Gaps
├── comment-tracker.yaml
└── verification-log.md
```

`mandat.md` Vorlage:
```markdown
# Mandat: [Bezeichnung]
Erstellt: [TT.MM.JJJJ]
Mandant: [Kürzel]
Art: [Typ]
Behörde(n): [Liste]
Leitfrist: [TT.MM.JJJJ]
Status: aktiv

## Mandat-spezifische Fakten
[Abweichungen vom Praxisprofil; Mandant-spezifische Materialitätsschwelle usw.]

## Datenschutz-Hinweis
§ 43a Abs. 2 BRAO, § 203 StGB. Dieser Ordner enthält mandantenbezogene Daten.
Cross-Mandat-Kontext: deaktiviert (Standard).
```

### Subkommando: `auflisten`

Alle Mandate auflisten:
```
Aktive Mandate:
| Slug | Mandant | Art | Behörde | Leitfrist | Status |
|---|---|---|---|---|---|
| bafin-prüfung-2025-A | Mandant A | Gap-Analyse | BaFin | 31.12.2025 | aktiv |
```

### Subkommando: `wechseln`

```
Zu welchem Mandat wechseln?
[Liste der aktiven Mandate anzeigen]
```
Nach Auswahl: Aktives Mandat im Profil setzen. Skills lesen jetzt `mandat.md` dieses Mandats.

### Subkommando: `schließen`

```
Mandat [Slug] schließen?
Hinweis: Dateien bleiben erhalten. Status wird auf 'geschlossen' gesetzt.
Lernerkenntnisse ins Praxisprofil übertragen? (ja/nein)
```

### Subkommando: `keiner`

Aktives Mandat deaktivieren → Skills laufen wieder auf Praxisebene.

## Quellen und Zitierweise

Zitierweise: `../../../references/zitierweise.md`

Relevante Berufsrechtsnormen:
- § 43a Abs. 2 BRAO (Verschwiegenheitspflicht)
- § 203 StGB (Verletzung von Privatgeheimnissen)
- § 50 BRAO (Aktenführung)
- BORA § 2 (Unabhängigkeit), § 6 (Handakten)

## Ausgabeformat

- Bestätigung der Aktion (angelegt / gewechselt / geschlossen)
- Aktueller Workspace-Status
- Nächster empfohlener Schritt (z. B. "Mandat aktiv – starten Sie mit `/regulatorisches-recht:lücken-aufzeiger`")

## Beispiel

**Eingabe:** `/regulatorisches-recht:regulatorisches-recht-mandat-arbeitsbereich neu`

**Ausgabe:**
```
Neues Mandat anlegen.

Mandant-Kürzel (nur intern sichtbar): MandantA
Mandat-Bezeichnung: MaRisk-GAP-2025-MandantA
Art: Gap-Analyse
Zuständige Behörde: BaFin
Leitfrist: 31.12.2025

Mandat angelegt unter:
~/.../mandate/mairisk-gap-2025-mandanta/

Aktives Mandat: MaRisk-GAP-2025-MandantA

Nächster Schritt: /regulatorisches-recht:lücken-aufzeiger
```

## Risiken / typische Fehler

- **Cross-Mandat-Kontext versehentlich aktiviert:** Skills dürfen mandantsübergreifend niemals Informationen verbinden, wenn Cross-Mandat-Kontext deaktiviert ist (Standard). Explizite Anfrage erforderlich.
- **Klarnamen in Pfaden:** Mandanten-Klarnamen nicht in Dateinamen oder Logs verwenden. Nur Kürzel.
- **Nicht geschlossene Mandate:** Alte aktive Mandate ohne Leitfrist überprüfen und bei Abschluss schließen; beugt Versehen mit veralteten Kontextinformationen vor.
- **Mandantengeheimnis:** Inhalte aus `mandat.md` und den mandat-spezifischen Trackern sind vertraulich nach § 43a Abs. 2 BRAO. Nie in gemeinsame Kontexte oder Protokolle exportieren.
## Aktuelle Rechtsprechung & Leitsätze

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

**Kernnormen:** §§ 611-630 BGB (Dienstvertrag, Mandatsrecht) — §§ 48-49 VwVfG — §§ 3-7 BORA (Berufsrecht Rechtsanwaelte)

- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

## 3. `richtlinien-neufassung`

**Fokus:** Interne Richtlinien und Unternehmensanweisungen auf regulatorischer Basis neu verfassen. KWG WpHG DORA DSGVO GwG MaRisk. Prüfraster: regulatorische Anforderungen Inhaltsstruktur Formulierungsstandard Genehmigungsweg. Output: neue Richtlinie Implementierungshinweise. Abgrenzung: nicht für Anpassung bestehender Richtlinien (regulatorisches-recht-anpassen).

# Richtlinien-Neufassung

## Zweck

Dieser Skill erstellt einen Erst-Entwurf einer überarbeiteten internen Richtlinie auf Basis einer identifizierten Compliance-Lücke (aus `luecken-aufzeiger` oder `richtlinien-vergleich`). Er erzeugt keinen finalen Text – das Ergebnis ist ein Redline-Entwurf zur internen Prüfung und Freigabe, nicht die direkte Bearbeitung des Quelldokuments.

Typische Einsatzfelder:
- Anpassung von MaRisk-Richtlinien nach BaFin-Novelle
- Überarbeitung der IT-Sicherheitsrichtlinie nach neuem BAIT-Rundschreiben
- ESG-Risikorichtlinie neu erstellen nach aufsichtsrechtlicher Pflicht
- Compliance-Handbuch für Zahlungsinstitute nach ZAG-Änderung

## Eingaben

- **Gap oder Diff:** Ergebnis aus `luecken-aufzeiger` oder `richtlinien-vergleich` (oder manuelle Beschreibung der Lücke)
- **Bestandsrichtlinie:** Vollständiger Text (hochgeladen oder eingefügt)
- **Aufsichtsverlautbarung:** BaFin-Rundschreiben / Leitlinie (für Normzitate)
- Optional: Richtlinienformat-Vorlage des Unternehmens
- Optional: Übergangsfrist

## Ablauf

### 1. Ausgangslage erfassen

Aus dem Gap/Diff die zu schließende(n) Lücke(n) identifizieren:
- Welche Abschnitte der Bestandsrichtlinie müssen geändert werden?
- Welche Abschnitte sind neu hinzuzufügen?
- Gibt es Abschnitte, die gestrichen oder eingeschränkt werden müssen?

### 2. Normgrundlagen ermitteln

Für jede Änderung die maßgebliche Aufsichtsnorm zitieren:

```
Änderungsgrund: MaRisk AT 4.3.2 Novelle 2023 – Datenhaltungsfrist 10 Jahre
Maßgebliche Norm: BaFin-Rundschreiben 09/2017 (BA) i.d.F. 2023, AT 4.3.2
Verbindlichkeit: verbindliche Mindestanforderung [Modellwissen – prüfen]
Übergangsfrist: 31.12.2025
```

### 3. Redline-Entwurf erstellen

Format: Änderungen nach Redline-Konvention kennzeichnen:
- **~~Durchgestrichen~~** = zu streichender Text
- **`Fett/kursiv`** oder `[NEU:]` = neuer Text
- `[Normverweis]` = Quelle der Änderung

Beispiel:
```
§ 4 Aufbewahrungspflichten

(2) Daten des Risikomanagements sind für einen Zeitraum von
~~mindestens sieben (7) Jahren~~ **[NEU: mindestens zehn (10) Jahren]**
aufzubewahren. [MaRisk AT 4.3.2 Novelle 2023 – prüfen]

[NEU: (3) Für die Datenklassifizierung ist eine schriftliche
Dokumentation zu erstellen und jährlich zu aktualisieren.
[MaRisk AT 4.3.2 Novelle 2023 – prüfen]]
```

### 4. Neue Abschnitte vollständig entwerfen

Für neu hinzuzufügende Abschnitte vollständigen Text erstellen. Orientierung an:
- Wortlaut der Aufsichtsnorm (ggf. direktes Zitat mit Anpassung)
- Formulierungsstil der Bestandsrichtlinie
- Proportionalitätsgrundsatz (§ 25a Abs. 1 S. 3 KWG)

### 5. Metadaten der Richtlinie aktualisieren

```
Version: [alte Versionsnummer] → [neue Versionsnummer]
Stand: [TT.MM.JJJJ]
Änderungsgrund: Anpassung an [Verlautbarung]
Geprüft durch: [Freigabe durch Rechtsabteilung / Compliance / Vorstand erforderlich]
Nächste Überprüfung: [TT.MM.JJJJ – empfohlen: 12 Monate]
```

### 6. Freigabe-Checkliste

Am Ende des Entwurfs ausgeben:

```
Freigabe-Checkliste vor Inkraftsetzung:
☐ Rechtliche Prüfung abgeschlossen [prüfen]
☐ Compliance-Review durchgeführt
☐ Betroffene Fachabteilung informiert
☐ Vorstand / Geschäftsleitung hat zugestimmt (§ 25a Abs. 1 S. 2 KWG)
☐ Mitarbeiter geschult (falls neue Pflichten)
☐ Versionskontrolle aktualisiert
☐ Datum des Inkrafttretens festgelegt
```

## Aktuelle Rechtsprechung & Leitsätze

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)

Art. 288 AEUV (Richtlinien) — §§ 40-44 GGO (Verwaltungsvorschriften-Neufassung) — §§ 305-310 BGB (AGB-Neufassung) — §§ 133, 157 BGB (Auslegung)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Quellen und Zitierweise

Zitierweise: `../../../references/zitierweise.md`

Jede Änderung im Redline wird mit der maßgeblichen Norm in Kurzform zitiert:
- `[MaRisk AT 4.3.2 Novelle 2023]` – mit Modellwissens-Hinweis, wenn nicht aus Primärquelle
- `[§ 25a Abs. 1 S. 3 KWG – Proportionalität]`
- `[EBA/GL/2021/04 Rz. 45]` – für EBA-Leitlinien

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
- Quellenregel: Keine Kommentar-, Handbuch-, Aufsatz- oder Tabellenfundstellen aus Modellwissen; nur Nutzerquelle, amtliche/freie Quelle oder lizenzierte Live-Verifikation verwenden.
- Lerch, ZAG, 2. Aufl. 2020, § 27 Rn. 20 ff.
- BaFin-Rundschreiben 09/2017 (BA) – MaRisk [Primärquelle; abrufbar: bafin.de]

## Ausgabeformat

- **Redline-Entwurf:** Vollständige Richtlinie mit markierten Änderungen
- **Änderungsübersicht:** Tabelle aller Änderungen mit Normverweis
- **Freigabe-Checkliste:** Am Ende des Entwurfs
- **Prüfernotiz:** Quellen, Vollständigkeit, offene Fragen
- Reviewer-Header wie in CLAUDE.md definiert

## Beispiel

**Eingabe:** "Bitte die IKS-Richtlinie für GAP-2025-001 (MaRisk AT 4.3.2 – Datenhaltung) neu fassen. Richtlinie hochgeladen."

**Ausgabe (Auszug):**

> **⚠️ Prüfernotiz**
> - **Quellen:** MaRisk RS 09/2017 Novelle 2023 [Modellwissen – prüfen gegen bafin.de], IKS-Richtlinie [Nutzer-Input]
> - **Gelesen:** § 4 IKS-Richtlinie, AT 4.3.2 MaRisk
> - **Zu Ihrer Einschätzung:** 1 Position `[prüfen]` – Aufbewahrungsfrist; Formulierung zur Datenklassifizierung ist Erstentwurf
> - **Vor Verwendung:** Rechts- und Compliance-Freigabe erforderlich; Inkrafttreten bis 31.12.2025

---

**VERTRAULICH – ANWALTLICHES ARBEITSERGEBNIS – ERSTENTWURF ZUR INTERNEN PRÜFUNG**

**IKS-Richtlinie – Redline-Entwurf**
*Version 2.0 (Entwurf) | Stand: 01.06.2025 | Änderungsgrund: MaRisk-Novelle 2023*

---

**§ 4 Aufbewahrungspflichten**

(2) Daten des Risikomanagements sowie sämtliche für die Beurteilung der wirtschaftlichen Verhältnisse des Instituts erforderliche Unterlagen sind für einen Zeitraum von ~~mindestens sieben (7) Jahren~~ **[NEU: mindestens zehn (10) Jahren]** aufzubewahren und jederzeit innerhalb angemessener Frist abrufbar zu halten. [MaRisk AT 4.3.2 Novelle 2023 – Modellwissen, prüfen]

**[NEU: (3) Eine schriftliche Dokumentation der Datenklassifizierung ist zu erstellen. Diese ist mindestens jährlich auf Aktualität zu prüfen und bei wesentlichen Änderungen unverzüglich zu aktualisieren. [MaRisk AT 4.3.2 Novelle 2023 – Modellwissen, prüfen]]**

---

**Änderungsübersicht:**
| § | Änderungstyp | Normgrundlage | Status |
|---|---|---|---|
| § 4 Abs. 2 | Friständerung 7 → 10 Jahre | MaRisk AT 4.3.2 | `[prüfen]` |
| § 4 Abs. 3 (neu) | Neuer Absatz Datenklassifizierung | MaRisk AT 4.3.2 | `[prüfen]` |

## Risiken / typische Fehler

- **Direktes Inkraftsetzen ohne Freigabe:** Der Redline-Entwurf ist ein Arbeitsdokument. Niemals ohne rechts- und compliance-seitige Freigabe sowie (bei KWG-Instituten) Geschäftsleiterzustimmung inkraftsetzen.
- **Wörtliche Übernahme von Normtext:** Aufsichtstext ist oft Mindeststandard, nicht optimaler Richtlinientext. Formulierungen ggf. konkretisieren.
- **Fehlende Schulungsmaßnahmen:** Neue Pflichten in internen Richtlinien wirken nicht ohne Mitarbeiterschulungen. Hinweis in Checkliste.
- **Versionskontrolle:** Jede Richtlinienänderung erfordert eine neue Versionsnummer und ein Änderungsprotokoll. Ohne Versionskontrolle ist die Richtlinie in BaFin-Prüfungen nur schwer nachzuweisen.
- **Proportionalitätsgrundsatz vergessen:** Für kleine und mittelgroße Institute gelten teils erleichterte Anforderungen (§ 25a Abs. 1 S. 3 KWG); Redline ggf. anpassen.
