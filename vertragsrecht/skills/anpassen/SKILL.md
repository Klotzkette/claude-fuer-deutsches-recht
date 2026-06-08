---
name: anpassen
description: "Geführte Anpassung des Kanzleiprofils im Vertragsrecht — ändert einzelne Einstellungen ohne erneutes Erstgespräch. Lädt, wenn der Nutzer Profil anpassen, Playbook ändern, Eskalation aktualisieren, Klauselposition ändern oder konfigurieren sagt im Vertragsrecht."
---

# Kanzleiprofil anpassen

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: BGB §§ 305-310, AGBG (alt), EuGH zu Klauseltransparenz (z. B. C-26/13, C-186/16), VerbrG; §§ 305 ff. BGB, NDA, SaaS- — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Eingaben

- Die gewünschte Änderung in eigenen Worten: "Ändere meine Haftungsobergrenze
 auf 6 Monate", "Neuer Eskalationsansprechpartner für Verträge über 500.000 €",
 "Risikobereitschaft auf konservativ setzen"
- Optional: Abschnittsnamen aus dem Kanzleiprofil (Playbook, Eskalation,
 Kanzleistil, Integrationen etc.)

## Rechtlicher Rahmen

### Kernvorschriften

Die zulässige Anpassungsspanne von Vertragsklauseln ist durch zwingendes Recht
begrenzt. Relevante Grenzen:

- § 307 BGB — Unangemessene Benachteiligung; Transparenzgebot. Klauseln,
 die den Vertragspartner entgegen den Geboten von Treu und Glauben unangemessen
 benachteiligen, sind unwirksam — auch im B2B-Bereich.
- § 308 Nr. 1, 2 BGB — Klauselverbote mit Wertungsmöglichkeit (Fristen,
 Leistungsänderungsvorbehalte)
- § 309 Nr. 7 BGB — Klauselverbot ohne Wertungsmöglichkeit: Haftungsausschluss
 für Körperverletzungen und grobe Fahrlässigkeit ist unwirksam und nicht
 verhandelbar
- § 310 Abs. 1 BGB — Im unternehmerischen Verkehr gelten §§ 308, 309 BGB
 Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- §§ 438, 634a BGB — Gesetzliche Verjährungsfristen für Gewährleistung;
 Verkürzung in AGB nur in Grenzen des § 309 Nr. 8 BGB

### Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 (Zulässige Anpassung von Zinsklauseln; Transparenzgebot bei Änderungsvorbehalten)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 (Unwirksamkeit einer AGB-Klausel bei unangemessener Benachteiligung; § 307 BGB)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 (Unwirksamkeit verkürzter Verjährungsfristen in AGB bei versteckter Klausel)

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## Ablauf

### Schritt 1 — Profil lesen

Lies `~/.claude/plugins/config/klotzkette/vertragsrecht/CLAUDE.md`.
Enthält es `[PLATZHALTER]`-Werte, sage:

> Sie haben die Ersteinrichtung noch nicht abgeschlossen. Führen Sie zuerst
> `/vertragsrecht:vertragsrecht-kaltstart-interview` aus — die Anpassungsfunktion setzt
> ein vollständiges Profil voraus.

### Schritt 2 — Anpassbare Bereiche zeigen

Zeige dem Nutzer, was im Profil änderbar ist, mit aktuellem Ist-Wert
(eine Zeile pro Einstellung):

- **Kanzlei / Profil** — Name, Branche, Jurisdiktion, Rechtsform, Setting
 (Kanzlei/In-house), Mandatseite (Verwender/Kunden-Seite)
 *(Gemeinsames Profil — Änderungen wirken sich auf alle Plugins aus)*
- **Risikobereitschaft** — konservativ / ausgewogen / risikobereit;
 Auswirkung auf Fallback-Positionen und Eskalationsschwellen
- **Personen** — Eskalationskette, Genehmiger nach Schwellenwert und
 Klauseltyp (GC, Partner, Geschäftsführung)
- **Klauselpositionen (Playbook)** — die substanziellen Vertragspositionen:
 Haftungsbeschränkung, Gewährleistung, Datenschutz/AVV, Laufzeit/Kündigung,
 AGB-Einbeziehung, Gerichtsstand, Fallback-Positionen zu jeder Klausel
- **Spürbarkeit von Abweichungen** — ab welcher Abweichung vom Standardmuster
 wird eine Klausel als GELB oder ROT gekennzeichnet?
- **Prüfungseinstellungen** — Routing-Bestätigung, Erklärungstiefe,
 Standard-Stakeholder-Zusammenfassung
- **Kanzleistil** — Ton in Gegenentwürfen, Länge von Zusammenfassungen,
 Ablageort für Arbeitsergebnisse
- **Ablauf** — Mandatspfade, Fristen-Tracker-Takt
- **Integrationen** — Status Vertragsmanagement-System, E-Signatur, Slack,
 Dokumentenablage

### Schritt 3 — Änderung abfragen

> Was möchten Sie anpassen? Nennen Sie einen Bereich oder beschreiben Sie
> die Änderung in eigenen Worten.

### Schritt 4 — Änderung durchführen

Zeigen Sie den aktuellen Wert, fragen Sie nach dem neuen Wert, erläutern
Sie, was sich downstream ändert, bestätigen Sie und schreiben Sie in das
Kanzleiprofil.

**Beispiele:**

- *Haftungsobergrenze Fallback 12 Monate → 6 Monate:*
 "`/vertragsrecht:vertragsprüfung` kennzeichnet künftig alles über 6 Monate als
 Abweichung; bereits protokollierte Verhandlungsergebnisse bleiben unverändert."
- *Neuer Eskalationsansprechpartner:*
 "Jeder Redline-Vorschlag, der Ihre Zeichnungsbefugnis übersteigt, wird
 künftig an diesen Ansprechpartner gerichtet."
- *Risikobereitschaft ausgewogen → konservativ:*
 "Ich kennzeichne Klauseln, die zuvor als akzeptabel galten, künftig früher
 als Abweichung und verschiebe den Eskalationsschwellenwert nach unten."
- *Spürbarkeit einer Abweichung ändern:*
 "Soll jede Verlängerung der Verjährungsfrist über 2 Jahre als GELB
 (verhandelbar) oder als ROT (Eskalation) markiert werden?"

### Schritt 5 — Gemeinsames Profil (mandantenübergreifend)

Für Änderungen an Kanzleiname, Branche, Jurisdiktion oder Rechtsform:
Schreibe in das gemeinsame Profil und weise darauf hin:

> Diese Änderung betrifft das gemeinsame Kanzleiprofil und wirkt sich
> auf alle Plugins aus, die dieses Profil lesen.

### Schritt 6 — Abschluss

> Erledigt. Ihre nächste Ausgabe spiegelt die Änderung wider. Weitere
> Anpassungen? `/vertragsrecht:vertragsrecht-anpassen` ist jederzeit verfügbar.

## Beispiel

**Szenario:** Der zuständige Partner als Eskalationspunkt hat gewechselt.

1. Profil zeigt aktuell: "Eskalation an RA Müller, E-Mail"
2. Nutzer sagt: "RA Müller ist ausgeschieden, bitte auf RA Meier ändern"
3. Skill zeigt: Aktuell: `RA Müller (m.mueller@kanzlei.de)` →
 Neu: `RA Meier` (bitte E-Mail-Adresse bestätigen)
4. Nach Bestätigung: Profil aktualisiert; Hinweis, dass `/vertragsrecht:vertragsprüfung`
 und Eskalationsvorschläge künftig RA Meier adressieren.

## Risiken und typische Fehler

- **Zwingende AGB-Grenzen nicht umgehen lassen.** Wenn der Nutzer eine
 Position eintragen will, die gegen § 309 Nr. 7 BGB oder andere zwingende
 Vorschriften verstößt (z. B. vollständiger Haftungsausschluss auch für grobe
 Fahrlässigkeit in AGB), darauf hinweisen und Eintragung verweigern oder
 mit Warnung versehen.
- **Interne Widersprüche im Profil flaggen.** Wenn Risikobereitschaft auf
 "konservativ" steht, aber jede Eskalation der GC-Genehmigung bedarf, ist
 das ein Widerspruch — ansprechen, welche Einstellung gelten soll.
- **Leitplanken-Abbau erklären.** Wenn der Nutzer eine Schutzmarkierung
 deaktivieren will (z. B. `[Prüfen]`-Hinweis auf Klauseln, Quellenangaben
 entfernen), den Zweck der Leitplanke erklären und Konsequenz benennen.
 Die `[Prüfen]`-Markierung, Quellenangaben und `[Verifizieren]`-Hinweise
 sind funktionstragende Elemente und sollen nicht entfernt werden.
- **Gesamtinterview nicht auslösen.** Diese Skill ändert einzelne
 Einstellungen — sie stellt keine Fragen aus dem Erstgespräch neu.

## Quellenpflicht

Wenn eine Klauselanpassung an zwingenden gesetzlichen Grenzen scheitert
oder eine Warnung ausgelöst wird, muss die Ausgabe belegen:
- Den einschlägigen Paragraphen (z. B. § 309 Nr. 7 BGB)
- Eine BGH-Entscheidung zur Grenze
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
 § 309 Rn. 48)

Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall.

---

<!-- AUDIT 27.05.2026
Quelle: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=02.11.2016&Aktenzeichen=XII+ZR+153%2F15
Bundle: bundle_047.json
-->

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- Art. 28 DSGVO
- § 203 StGB
- § 13 UWG
- § 15 AktG
- Art. 82 DSGVO
- § 2 HRG
- § 4 HRG
- § 7 HRG
- § 15 HRG
- § 16 HRG
- § 70 VwG
- § 123 VwG

### Leitentscheidungen

- EuGH C-249/21

