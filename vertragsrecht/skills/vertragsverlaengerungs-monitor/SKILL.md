---
name: vertragsverlaengerungs-monitor
description: "'Zeigt Verträge mit ablaufenden Kündigungsfristen an und warnt rechtzeitig, bevor Verlängerungs-/Kündigungsfenster schließen. Relevant insbesondere bei § 309 Nr. 9 BGB (automatische Verlängerung). Laden, wenn der Nutzer fragt 'welche Verträge laufen aus', 'wann muss ich kündigen', 'habe ich eine Frist verpasst', oder bei geplanter Aktualisierung des Registers.'"
---

# Verlängerungstracker

## Triage zu Beginn

1. Ist das Fristen-Register vollständig (alle aktiven Verträge mit Laufzeitende und Kündigungsfrist)?
2. Wurden Postlaufpuffer korrekt eingetragen (Schriftform: 3 Tage; elektronisch: 0 Tage)?
3. Gibt es Verträge deren Verlängerungsklausel nach § 309 Nr. 9 BGB (B2C) oder § 307 BGB (B2B) unwirksam sein könnte?
4. Welche Bundesland-Feiertage sind für die Fristberechnung relevant?

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen

- § 309 Nr. 9 BGB — Laufzeit-Klauseln B2C: Erstlaufzeit max. 2 Jahre; Verlängerung max. 1 Jahr; Kündigungsfrist max. 3 Monate
- § 307 BGB — Inhaltskontrolle B2B: unangemessen lange Bindungen
- § 130 BGB — Zugang von Willenserklärungen (Fristbeginn für Kündigung)
- § 126 BGB — Schriftform (Original-Unterschrift nötig; E-Mail reicht nicht)
- § 126b BGB — Textform (E-Mail, PDF)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Zweck

Niemand liest einen Vertrag zweimal. Das Verlängerungsdatum wird einmal beim Review entnommen und muss dann irgendwo gespeichert werden – idealerweise an einem Ort, der 45 Tage vor Ablauf der Kündigungsfrist laut warnt, nicht 45 Tage danach. Dieser Skill pflegt das Fristen-Register und zeigt, was fällig wird.

Rechtlicher Hintergrund: § 309 Nr. 9 BGB verbietet in B2C-AGB stillschweigende Verlängerungen um mehr als 1 Jahr und Kündigungsfristen über 3 Monate. Im B2B prüft § 307 BGB unangemessen lange Bindungen. Diesem Skill kommt daher auch eine präventive Prüffunktion zu: automatische Verlängerungen mit überlangen Fristen können unwirksam sein.

## Eingaben

- Register `~/.claude/plugins/config/claude-fuer-deutsches-recht/vertragsrecht/renewal-register.yaml`
- Optional: `--tage N` zur Änderung des Beobachtungsfensters (Standard: 90 Tage)
- Optional: `--verpasst` für abgelaufene Fristen ohne erfasste Kündigung

## Ablauf

### Schritt 1: Register lesen

`~/.claude/plugins/config/claude-fuer-deutsches-recht/vertragsrecht/renewal-register.yaml` lesen. Falls leer und CLM verbunden: Modus 3 (Erst-Import aus CLM) anbieten.

### Schritt 2: Standardmodus – was läuft in 90 Tagen aus?

Halboffene Intervalle (jeder Fälligkeitstag fällt in genau eine Kategorie):

| Band | Zeitraum | Bedeutung |
|---|---|---|
| 🔴 | 0–13 Tage | Sofortiger Handlungsbedarf |
| 🟠 | 14–44 Tage | Dringend – diese Woche planen |
| 🟡 | 45–89 Tage | Auf dem Schirm |

**Achtung – Absendedatum, nicht Empfangsdatum:** Wenn die Kündigung Schriftform oder Einschreiben erfordert, ist der Postweg einzurechnen. Das Register nutzt `sende_bis_effektiv` für Alerts, nicht `kündigen_bis_effektiv`.

### Schritt 3: `--verpasst`-Modus

Einträge mit `status: aktiv` anzeigen, deren `kündigen_bis_effektiv` in der Vergangenheit liegt und kein `status: gekündigt` gesetzt ist. Konsequenzen der verpassten Frist erläutern:
- Bei B2C: § 309 Nr. 9 BGB prüfen – war die Verlängerungsklausel überhaupt wirksam?
- Bei B2B: § 307 BGB prüfen
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Das Register

Gespeichert unter `~/.claude/plugins/config/claude-fuer-deutsches-recht/vertragsrecht/renewal-register.yaml`. Jeder Eintrag:

```yaml
- vertragspartner: "Acme Software GmbH"
 vertrag: "Acme Plattform-Abonnementvertrag"
 unterzeichnungsdatum: 2025-06-15
 erstlaufzeit_ende: 2026-06-15
 aktuelle_laufzeit_ende: 2026-06-15 # rollt nach jeder Verlängerung vor
 verlaengerungsmechanismus: "automatisch jährlich"
 kuendigungsfrist_tage: 90
 kuendigungsform: "schriftlich" # e-mail / schriftlich / einschreiben / portal / § X Vertrag
 postlauf_puffer_tage: 3 # 0 für elektronisch; 3 für Einschreiben; 10 für internationalen Post
 kuendigen_bis_kalender: 2026-03-17
 kuendigen_bis_effektiv: 2026-03-17 # ggf. auf letzten Werktag vorgezogen
 sende_bis_effektiv: 2026-03-14 # kündigen_bis_effektiv minus postlauf_puffer_tage
 vorzieh_hinweis: "" # z. B. "vorgezogen von Sonntag 2026-03-15; Werktags-Definition im Vertrag prüfen"
 kuendigen_bis_provenienz: "[Modellberechnung – gegen Kündigungsklausel prüfen]"
 preis_bei_verlaengerung: "jeweils aktueller Listenpreis (unbegrenzt)"
 jahreswert: 48000
 verantwortlich: "max.mustermann@firma.de"
 clm_id: "IC-12345"
 docusign_umschlag: "abc-123"
 status: "aktiv" # aktiv | gekündigt | verlängert | versäumt
 notizen: "Preis unbegrenzt – vor Verlängerung Alternativen prüfen: X, Y."
 bgb_309_9_pruefung: "B2B – § 307 BGB prüfen; nicht direkt anwendbar"
```

## Ausgabeformat

```markdown
### Verlängerungsübersicht – [Datum]

**Fenster:** nächste [N] Tage
**Einträge gesamt:** [N aktiv] | [N in Beobachtungsfenster]

---

## 🔴 Sofortiger Handlungsbedarf (0–13 Tage bis Absende-Frist)

| Vertragspartner | Vertrag | Absenden bis | Kündigen bis | Preis bei Verlängerung | Verantwortlich |
|---|---|---|---|---|---|
| [Name] | [Vertrag] | **[Datum]** | [Datum] | [Mechanismus] | [E-Mail] |

> ⚠️ Kündigungsform beachten: [schriftlich/einschreiben/e-mail] – Postlauf [N] Tage eingerechnet.

---

## 🟠 Dringend (14–44 Tage)

[gleiche Tabelle]

---

## 🟡 Auf dem Schirm (45–89 Tage)

[gleiche Tabelle]

---

## Hinweise

[Einträge mit unbegrenztem Preis, Einträge ohne Verantwortlichen, verpasste Fristen im Beobachtungsfenster]

---

## § 309 Nr. 9 BGB / § 307 BGB Hinweis

[Einträge, bei denen die Verlängerungsklausel auf Wirksamkeit zu prüfen ist]
```

## Fristenberechnung

**Beispiel:** Kündigungsfrist 90 Tage, Schriftform + Einschreiben (3 Tage Postlauf), Laufzeitende 15.06.2026:
- `kündigen_bis_kalender` = 17.03.2026
- `kündigen_bis_effektiv` = 17.03.2026 (kein Wochenende)
- `sende_bis_effektiv` = 14.03.2026

**Werktags-Regel:** Fällt `kündigen_bis` auf Samstag/Sonntag oder gesetzlichen Feiertag, auf den letzten Werktag davor vorziehen. Feiertage sind bundeslandabhängig – Bundesland des zuständigen Büros oder des Vertragsgerichtsstandsorts prüfen.

## Quellen und Zitierweise

Zitierweise nach `../references/zitierweise.md`.

Normen und Rspr.:
- § 309 Nr. 9 BGB – Laufzeit B2C; automatische Verlängerung max. 1 Jahr; Kündigungsfrist max. 3 Monate
- § 307 BGB – Inhaltskontrolle B2B; unangemessen lange Bindungen
- § 308 Nr. 3 BGB – Vorauszahlungsklauseln
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Kommentare:
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

## Risiken / typische Fehler

- **Postlauf nicht eingerechnet:** Eine Kündigung, die am letzten Fristtag abgeschickt wird, aber per Einschreiben zugestellt werden muss, kommt zu spät.
- **§ 309 Nr. 9 BGB-Unwirksamkeit nicht geprüft:** Wenn der Vertrag B2C ist und die Verlängerungsklausel gegen § 309 Nr. 9 BGB verstößt, kann die Verlängerung unwirksam sein – aber man muss es wissen.
- **Bundesland-Feiertage:** Feiertage variieren zwischen Bundesländern; pauschal "Montag bis Freitag" reicht nicht.
- **Register-Lücken:** Verträge, die vor Plugin-Einrichtung unterzeichnet wurden, sind nicht im Register – einmaliger Erst-Import erforderlich.
