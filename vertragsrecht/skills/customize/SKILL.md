---
name: customize
description: >
  Geführte Anpassung des Kanzleiprofils im Vertragsrecht — ändert einzelne
  Einstellungen ohne erneutes Erstgespräch. Lädt, wenn der Nutzer
  „Profil anpassen", „Playbook ändern", „Eskalation aktualisieren",
  „Klauselposition ändern" oder „konfigurieren" sagt.
language: de
triggers:
  - "Profil anpassen"
  - "Playbook ändern"
  - "Konfiguration ändern"
  - "Klauselposition"
  - "Eskalation aktualisieren"
  - "Risikoposition"
  - "Kanzleiprofil bearbeiten"
  - "Einstellung ändern"
---

# Kanzleiprofil anpassen

## Zweck

Diese Skill ermöglicht die gezielte Anpassung einzelner Einstellungen im
Kanzleiprofil, ohne das vollständige Erstgespräch erneut zu durchlaufen.
Sie eignet sich für Situationen, in denen sich eine Verhandlungsposition,
eine Eskalationsstufe, ein Klauselstandard oder eine Integrationseinstellung
geändert hat.

Lädt, wenn der Nutzer eine einzelne Änderung am bestehenden Profil vornehmen
möchte — nicht für die Ersteinrichtung (dafür: `/vertragsrecht:cold-start-interview`).

## Eingaben

- Die gewünschte Änderung in eigenen Worten: „Ändere meine Haftungsobergrenze
  auf 6 Monate", „Neuer Eskalationsansprechpartner für Verträge über 500.000 €",
  „Risikobereitschaft auf konservativ setzen"
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
  nicht unmittelbar, aber § 307 BGB weiterhin (BGH BGHZ 174, 1 Rn. 12)
- §§ 438, 634a BGB — Gesetzliche Verjährungsfristen für Gewährleistung;
  Verkürzung in AGB nur in Grenzen des § 309 Nr. 8 BGB

### Leitentscheidungen

- BGH, Urt. v. 19.11.2019 – XI ZR 9/18, NJW 2020, 461 Rn. 22 ff.
  (Zulässige Anpassung von Zinsklauseln; Transparenzgebot bei Änderungsvorbehalten)
- BGH, Urt. v. 08.03.2005 – XI ZR 154/04, BGHZ 162, 294 Rn. 26
  (Unwirksamkeit einer AGB-Klausel bei unangemessener Benachteiligung; § 307 BGB)
- BGH, Urt. v. 25.10.2016 – VI ZR 516/15, NJW 2017, 1104 Rn. 14
  (Grenzen der Haftungsbeschränkung in AGB; § 309 Nr. 7 BGB)
- BGH, Urt. v. 04.02.2009 – VIII ZR 32/08, NJW 2009, 1337 Rn. 18
  (Unwirksamkeit verkürzter Verjährungsfristen in AGB bei versteckter Klausel)

### Kommentarliteratur

- Palandt/Grüneberg, BGB, 83. Aufl. 2024, § 307 Rn. 1 ff. (Inhaltskontrolle),
  § 309 Rn. 48 ff. (Haftungsausschluss)
- MüKoBGB/Wurmnest, 9. Aufl. 2022, § 307 Rn. 45 ff. (Transparenzgebot);
  § 309 Rn. 90 ff.
- Wolf/Lindacher/Pfeiffer, AGB-Recht, 7. Aufl. 2020, § 309 Nr. 7 Rn. 30 ff.
- BeckOGK BGB/Lehmann-Richter, 70. Ed. (Stand 01.08.2024), § 307 Rn. 150 ff.

## Ablauf

### Schritt 1 — Profil lesen

Lies `~/.claude/plugins/config/klotzkette/vertragsrecht/CLAUDE.md`.
Enthält es `[PLATZHALTER]`-Werte, sage:

> Sie haben die Ersteinrichtung noch nicht abgeschlossen. Führen Sie zuerst
> `/vertragsrecht:cold-start-interview` aus — die Anpassungsfunktion setzt
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
- **Workflow** — Mandatspfade, Fristen-Tracker-Takt
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
  „`/vertragsrecht:review` kennzeichnet künftig alles über 6 Monate als
  Abweichung; bereits protokollierte Verhandlungsergebnisse bleiben unverändert."
- *Neuer Eskalationsansprechpartner:*
  „Jeder Redline-Vorschlag, der Ihre Zeichnungsbefugnis übersteigt, wird
  künftig an diesen Ansprechpartner gerichtet."
- *Risikobereitschaft ausgewogen → konservativ:*
  „Ich kennzeichne Klauseln, die zuvor als akzeptabel galten, künftig früher
  als Abweichung und verschiebe den Eskalationsschwellenwert nach unten."
- *Spürbarkeit einer Abweichung ändern:*
  „Soll jede Verlängerung der Verjährungsfrist über 2 Jahre als GELB
  (verhandelbar) oder als ROT (Eskalation) markiert werden?"

### Schritt 5 — Gemeinsames Profil (mandantenübergreifend)

Für Änderungen an Kanzleiname, Branche, Jurisdiktion oder Rechtsform:
Schreibe in das gemeinsame Profil und weise darauf hin:

> Diese Änderung betrifft das gemeinsame Kanzleiprofil und wirkt sich
> auf alle Plugins aus, die dieses Profil lesen.

### Schritt 6 — Abschluss

> Erledigt. Ihre nächste Ausgabe spiegelt die Änderung wider. Weitere
> Anpassungen? `/vertragsrecht:customize` ist jederzeit verfügbar.

## Ausgabeformat

Keine vollständige Neuschreibung des Profils — nur gezielter Diff (alter
Wert → neuer Wert) mit Bestätigung und Downstream-Hinweis. Der Nutzer sieht
genau, was sich geändert hat.

## Beispiel

**Szenario:** Der zuständige Partner als Eskalationspunkt hat gewechselt.

1. Profil zeigt aktuell: „Eskalation an RA Müller, E-Mail"
2. Nutzer sagt: „RA Müller ist ausgeschieden, bitte auf RA Meier ändern"
3. Skill zeigt: Aktuell: `RA Müller (m.mueller@kanzlei.de)` →
   Neu: `RA Meier` (bitte E-Mail-Adresse bestätigen)
4. Nach Bestätigung: Profil aktualisiert; Hinweis, dass `/vertragsrecht:review`
   und Eskalationsvorschläge künftig RA Meier adressieren.

## Risiken und typische Fehler

- **Zwingende AGB-Grenzen nicht umgehen lassen.** Wenn der Nutzer eine
  Position eintragen will, die gegen § 309 Nr. 7 BGB oder andere zwingende
  Vorschriften verstößt (z. B. vollständiger Haftungsausschluss auch für grobe
  Fahrlässigkeit in AGB), darauf hinweisen und Eintragung verweigern oder
  mit Warnung versehen.
- **Interne Widersprüche im Profil flaggen.** Wenn Risikobereitschaft auf
  „konservativ" steht, aber jede Eskalation der GC-Genehmigung bedarf, ist
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
- Eine BGH-Entscheidung zur Grenze (z. B. BGH, Urt. v. 25.10.2016 –
  VI ZR 516/15, NJW 2017, 1104)
- Einen Kommentarbeleg (z. B. Palandt/Grüneberg, BGB, 83. Aufl. 2024,
  § 309 Rn. 48)

Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall.
