# Kanzlei-Cowork

Cowork-Assistent für die deutsche Anwaltskanzlei. Fristenbuch Timesheet Rechnungserstellung nach RVG Versand-Vor-Check (PDF beA Signatur Adressat Anlagen) beA-Versand-Prüfung Postein- und ausgang Mandantenakte Aktenbestandspflege Honorar-Mahnwesen Mandantenbrief-Vorlagen Geburtstags- und Weihnachtskarten Sekretariats-Tagesbrief.

## ⬇️ Direkt-Download (einzelnes ZIP)

| Plugin | Direkt-Download |
| --- | --- |
| Kanzlei-Cowork (`kanzlei-cowork`, dieses Plugin) | [kanzlei-cowork.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/kanzlei-cowork.zip) |

Die URL ist stabil und zeigt immer auf die neueste Version. Alle weiteren Plugins sind unter [Releases · latest](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest) genauso einzeln verfügbar.

## Installation in Claude Code

1. ZIP herunterladen (Link oben).
2. Claude Code → **Customize Plugins** → **Install from .zip** → Datei wählen.
3. Fertig. Skills sind sofort verfügbar.

> **Hinweis:** Für den ZIP-Upload muss das Archiv direkt `.claude-plugin/plugin.json`, `skills/`, `assets/` und `references/` im ZIP-Root enthalten. **Nicht** das komplette Repository-ZIP aus „Code → Download ZIP“ verwenden.

## Enthaltene Skills

| Skill | Zweck |
| --- | --- |
| `aktenbestand-pflege` | Laufende Pflege des Aktenbestands der Kanzlei — Aktualisierung Aktenstatus (laufend / ruhend / abgeschlossen) Mandatsende mit Schlussrechnung und Aktenherausgabe an Mandant Archivierung nach Aufbewahrungspflicht (§ 50… |
| `bea-versand-pruefen` | Prüft den beA-Versand nach Pflichten des § 130a ZPO § 32d StPO § 65d SGG § 55a VwGO § 52d FGO sowie § 31a BRAO. Erforderliche Beachtung sicherer Übermittlungsweg (sUW durch persönliches Versenden des beA-Inhabers) … |
| `fristenbuch-fuehren` | Zentrales Fristenbuch für die Kanzlei mit Haupt- und Vorfristen über alle Rechtsgebiete. Berechnet Fristbeginn nach den jeweiligen Verfahrensordnungen (ZPO StPO SGG FGO VwGO FamFG AO BGB) Drei-Tages-Fiktionen bei Po… |
| `geburtstage-feiertage` | Pflegt einen Mandanten- und Geschäftspartner-Geburtstagsverteiler. Reminders einige Tage vor dem Tag. Vorlagen für kurze persönliche Glückwunsch-E-Mail (formell-warm). Bei Geschäftspartnern auch Firmenjubiläen. … |
| `kanzlei-cowork-kaltstart-interview` | Kaltstart-Interview für das generische Kanzlei-Cowork-Plugin. Erfragt Kanzleiprofil (Solo / Sozietät / GmbH / Partnerschaft) Rechtsgebiete-Mix Sekretariat (vorhanden Stellen) Aktenstruktur-Konvention beA-Profil Vers… |
| `mahnwesen-honorar` | Mahnwesen für eigene Honorarforderungen der Kanzlei. Stufen erste Zahlungserinnerung (vor Verzug) erste Mahnung mit Verzugsbeginn nach § 286 BGB zweite Mahnung mit konkreter Klagedrohung dritte Mahnung als letztes vo… |
| `mandantenakte-anlegen` | Legt eine Mandantenakte nach Kanzleikonvention an. Erfasst Stammdaten Bevollmächtigte Mandatsumfang Konfliktprüfung (§ 43a Abs. 4 BRAO § 3 BORA) Datenschutzhinweis (Art. 13 DSGVO) Geldwäsche-Identifizierung (§§ 10 … |
| `mandantenbrief-vorlagen` | Standardvorlagen für den Mandantenbrief der Kanzlei. Aufbau Anrede Bezug Sachstand Empfehlung nächste Schritte Frist Kostenhinweis Unterschrift mit Berufsbezeichnung. Verschiedene Vorlagen für Mandatseröffnung Zwi… |
| `posteingang-ausgang` | Postein- und Postausgangsbuch führen. Posteingang erfasst Empfangstag (relevant für Fristbeginn nach BRAO Berufsregeln und § 188 ZPO § 122 AO § 37 SGB X) Absender Inhalt Akte Aktion (zur Akte / Antwort durch / Frist… |
| `rechnungserstellung-rvg` | Erstellt Honorarrechnungen nach RVG (Anlage 1 VV RVG Anlage 2 RVG Gebührentabelle) oder nach Honorarvereinbarung mit Stundensatz. Pflichtangaben § 10 RVG (Aktenzeichen Mandant Gegenstand der Tätigkeit Vergütungstat… |
| `sekretariats-tagesbrief` | Erzeugt morgens den Tagesbrief der Kanzlei mit allen Informationen die Anwalt und Sekretariat für den Tag brauchen — Fristen heute und in der nächsten Woche Vorfristen aus dem Fristenbuch eingegangene Post vom Vorta… |
| `timesheet-aktenzeitung` | Zeiterfassung pro Mandat (Aktenzeitung) — tägliche Erfassung mit Datum Anwalt Akte Tätigkeit Dauer in 6-Minuten-Blöcken Abrechenbarkeit (abrechenbar / pro bono / nicht abrechenbar) Honorarsatz und Notiz. Reports na… |
| `versand-vor-check` | Pflicht-Pre-Check vor jedem ausgehenden Versand — prüft Dokumentidentität (das richtige PDF? Stand vom richtigen Datum? Aktenzeichen passt?) Unterschrift (durch berechtigte Person? eigenhändig oder qualifizierte el… |
| `weihnachtskarten` | Pflegt den Weihnachtskartenversand der Kanzlei. Verteiler mit Empfänger Anschrift E-Mail Versandart (postalisch / digital) Anredeform Bezug zur Kanzlei. Texte für formell-zurückhaltend warm und persönlich. Druckli… |

## Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.

## Quellen-Disclaimer

Alle Aussagen beruhen auf der im Plugin hinterlegten Rechtsprechung und genannter Kommentarliteratur. Die Skills ersetzen keine eigene anwaltliche, steuerberatende oder berufsbetreuerische Prüfung im Einzelfall.
