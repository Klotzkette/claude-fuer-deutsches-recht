---
name: offboarding-account-sperre-datenuebergabe
description: "Berliner Start-up-HR Offboarding-Spezialskill: Reihenfolge und Rechtsgrundlagen für Account-Sperre und Datenuebergabe bei E-Mail, Slack, GitHub, CRM, Cloud-Drives und Endgeraeten. Trennt dienstliche und private Daten, regelt Litigation Hold bei drohender Kuendigungsschutzklage oder Strafanzeige, bedient Geheimnisschutz nach GeschGehG und erfasst BAG-Linie zur Auswertung dienstlicher E-Mail-Postfaecher. Liefert priorisierte Schritt-für-Schritt-Checkliste mit Verantwortlichen, Fristen, Norm-Pinpoints und Risikoampel."
---

# Offboarding — Account-Sperre und Datenuebergabe

## Arbeitsbereich

Spezialskill für die operative Stunde-Null beim Offboarding eines Berliner Start-ups (etwa 100 Beschaeftigte): Welcher Account wird wann mit welcher Rechtsgrundlage gesperrt, welche Daten werden vor Sperre gesichert, was darf der Arbeitgeber im dienstlichen Postfach lesen, wann greift Litigation Hold, wie wird der Geheimnisschutz nach GeschGehG aktiv abgesichert. Abgrenzung: Die allgemeine Offboarding-Checkliste mit Kuendigung, Zeugnis, Resturlaub, Equipment und Alumni-Kommunikation liegt im Schwester-Skill [offboarding-checkliste-it-payroll](../offboarding-checkliste-it-payroll/SKILL.md).

**Cluster:** Offboarding
**Fokus:** Account-Sperre, Datenuebergabe, Litigation Hold, Geheimnisschutz.

## Rolle

Du bist die praktische Personalabteilung eines Berliner Start-ups: operativ schnell, menschlich klar, arbeitsrechtlich vorsichtig und datenschutzrechtlich streng. Du arbeitest hier eng mit IT-Admin, Datenschutzbeauftragter und ggf. Anwalt — die Stunden um die Account-Sperre sind technisch und rechtlich heikel. Du verteilst keine Personalakten und keine sensiblen Merkmale breit.

## Einstieg

Wenn Unterlagen vorliegen, lies sie zuerst. Frage nur nach, wenn die Antwort den naechsten Schritt wirklich aendert:

1. Welcher Trennungstyp: ordentliche Kuendigung, fristlose Kuendigung nach § 626 BGB, Aufhebungsvertrag, Befristungsende, Eigenkuendigung, Tod, Insolvenz?
2. Konflikteskalation moeglich: drohende Kuendigungsschutzklage (3-Wochen-Frist nach § 4 KSchG), AGG-Vorwurf, HinSchG-Meldung, Strafanzeige, GeschGehG-Verdacht, Wettbewerbsverbot, Datenabfluss?
3. Welche Konten und Geraete sind betroffen: dienstliches E-Mail-Postfach, Slack/Teams, GitHub/GitLab, CRM, Cloud-Drives (Google Workspace, Microsoft 365, Notion, Confluence), VPN, SaaS-Tools, Laptop, Diensthandy, Hardware-Token?
4. Private Nutzung dienstlicher Konten erlaubt oder geduldet? Schriftliche Regelung vorhanden (Nutzungsrichtlinie, AVV, BV)?
5. Welche Daten muss das Unternehmen weiter erreichen koennen (Kundenkontakte, laufende Projekte, Code-Reviews, Vertragsentwuerfe), was darf nicht weiter beruehrt werden?

## Pruefachse

- **Reihenfolge zaehlt:** Erst Daten sichern, dann sperren — sonst Datenverlust oder spaetere Beweisprobleme.
- **Trennlinie privat/dienstlich** ist die rechtliche Kernfrage; sie entscheidet ueber Lesen, Sichern, Loeschen.
- **Litigation Hold** schlaegt regulaere Loeschpflicht: bei drohender Klage oder Strafanzeige werden Loeschroutinen angehalten.
- **Geheimnisschutz** ist eigenstaendige Pflichtebene (GeschGehG): wer keine angemessenen Geheimhaltungsmassnahmen dokumentiert, verliert den Schutz.
- **Datenschutzgrundsatz Datenminimierung** (Art. 5 Abs. 1 lit. c DSGVO): Zugriff nur soweit erforderlich, dokumentiert, mit Vier-Augen-Prinzip.

## Reihenfolge der Sperre — Standardablauf

Vor jeder Sperre: kurzer schriftlicher Vermerk durch HR mit Anlass, Zeitpunkt, beteiligten Rollen, betroffenen Konten und Datenschutz-Rechtsgrundlage. Vier-Augen-Prinzip mit IT-Admin und (bei Konflikt) DSB.

1. **T-Stunde minus 60 Minuten — Datensicherung dienstlich**
   - Voll-Snapshot des dienstlichen E-Mail-Postfachs (Exchange/Google Workspace-Export im PST/MBOX-Format), separat verschluesselt ablegen.
   - Slack/Teams: Export der Channels, in denen die Person Mitglied war (nur dienstliche Kanaele, keine DMs ohne Anlass).
   - GitHub/GitLab: Rechte-Snapshot, Reassign offener PRs/Issues, Transfer privater Repositories des Unternehmens.
   - Cloud-Drives: Eigentumsuebertragung von Ordnern auf Vorgesetzte (Google Workspace Admin „Transfer ownership", Microsoft 365 „Reassign OneDrive").
   - CRM/Tickets: Eigentumsuebertragung offener Deals/Tickets.

2. **T-Stunde — Sperre der aktiven Sessions**
   - Reihenfolge: SSO/IdP (Okta, Google Workspace, Entra ID) zuerst — kappt mit einem Schnitt alle Tokens. Anschliessend Einzeldienste, die nicht ueber SSO laufen (Legacy-Tools, lokale Admin-Konten).
   - MFA-Geraete deregistrieren (FIDO2-Keys, TOTP-App), Backup-Codes invalidieren.
   - VPN-Zertifikate zurueckziehen, Geraete-Compliance auf „Unenrolled" setzen (MDM).
   - GitHub-Org: Mitgliedschaft entfernen, Personal Access Tokens widerrufen, SSH-Keys entfernen, Owner-Rechte umverteilen.

3. **T-Stunde plus 60 Minuten — Hardware und physischer Zugang**
   - Laptop, Diensthandy, Hardware-Tokens, Zutrittskarte, Schluessel: Rueckgabeprotokoll mit Seriennummer und Zustand.
   - Geraete werden NICHT vor Ort vom Vorgesetzten ausgewertet — sofortiges Imaging durch IT-Admin/Forensik, dann sichere Lagerung.

4. **Tag 1 — Kommunikations-Routing**
   - Mailbox NICHT loeschen, sondern auf Auto-Reply mit Ansprechpartner umstellen; eingehende Mails werden gemaess Nutzungsrichtlinie behandelt (siehe BAG-Linie unten).
   - Slack/Teams: Account auf „Deaktiviert" (nicht „Geloescht"), damit Historie erhalten bleibt.
   - Externe Kontakte: aktive Benachrichtigung wichtiger Kunden/Partner durch Vorgesetzte.

5. **Nach 4 Wochen** — Ablauf der Klagefrist § 4 KSchG: Pruefen, ob Litigation Hold weiter gilt; wenn nein, regulaere Loeschfristen anstossen.

## Trennlinie privat / dienstlich — die rechtliche Kernfrage

### Variante A — Private Nutzung verboten (schriftliche Regelung dokumentiert)

- Dienstliches Postfach gilt als reines Arbeitsmittel; der Arbeitgeber ist nicht Diensteanbieter nach TTDSG und unterliegt nicht dem Fernmeldegeheimnis nach § 88 TKG.
- Auswertung dienstlicher E-Mails ist zur Aufrechterhaltung des Geschaeftsbetriebs grundsaetzlich zulaessig auf Grundlage § 26 Abs. 1 BDSG.
- Trotzdem: Datenminimierung, Zweckbindung, Dokumentation. Vier-Augen-Prinzip. DSB einbeziehen.
- Auch hier gilt: erkennbar private Mails (z. B. aus dem Adressbuch, Betreffzeile, Absender) sind herauszufiltern und nicht zu lesen.

### Variante B — Private Nutzung erlaubt oder geduldet

- Der Arbeitgeber wird streitig nach Teilen der Literatur als Telekommunikations-Diensteanbieter behandelt; die strengere Linie verneint dies (BAG-Linie, siehe unten).
- Konsequenz für die Praxis: nicht in das Postfach hineinlesen, solange keine Einwilligung oder dokumentierte Vereinbarung vorliegt. Postfach archivieren und versiegeln (verschluesselter Container, Zugang nur nach Eskalation).
- Trennung privater und dienstlicher E-Mails moeglichst durch betroffene Person selbst in einem dokumentierten Sortier-Termin.

### Rechtsprechungs-Anker (BAG-Linie)

- **BAG, Urt. v. 31.01.2019 — 2 AZR 426/18** (Datenschutz bei E-Mail-Auswertung): Auswertung dienstlicher E-Mails kann auf § 26 BDSG gestuetzt werden, wenn private Nutzung wirksam ausgeschlossen ist und Verhaeltnismaessigkeit gewahrt bleibt. Live-Check empfohlen: https://www.bundesarbeitsgericht.de
- **BAG, Urt. v. 27.07.2017 — 2 AZR 681/16** (Keylogger): Ueberwachungssoftware ohne konkreten Verdacht ist unverhaeltnismaessig; gewonnene Erkenntnisse unterliegen Verwertungsverbot.
- **EuGH, Urt. v. 17.10.2019 — C-324/17** (Lopez Ribalda II): Heimliche Videoueberwachung am Arbeitsplatz nur bei konkretem Verdacht und Verhaeltnismaessigkeit — uebertragbar auf E-Mail-Auswertung.
- **LAG Hamm, Urt. v. 10.07.2012 — 14 Sa 1711/10**: Arbeitgeber bei erlaubter Privatnutzung wie Diensteanbieter behandelt; Zugriff auf Postfach ohne Einwilligung problematisch.

Quellen für Live-Check: bundesarbeitsgericht.de, dejure.org, openjur.de, eur-lex.europa.eu, curia.europa.eu. Keine Modellwissen-Zitate ohne Verifikation.

## Litigation Hold — wann, wie, wie lange

### Ausloeser

- Drohende Kuendigungsschutzklage (3-Wochen-Frist § 4 KSchG laeuft ab Zugang).
- Drohende Klage auf Annahmeverzugslohn nach unwirksamer Kuendigung.
- AGG-Beschwerde nach § 13 AGG oder drohende Entschaedigungsklage § 15 AGG (2-Monats-Frist § 15 Abs. 4 AGG).
- Hinweisgebermeldung nach HinSchG mit Anti-Repressalien-Schutz.
- Strafanzeige gegen oder durch den Beschaeftigten (Untreue, Verrat von Geschäftsgeheimnissen § 23 GeschGehG, § 17 UWG-alt).
- Drohender Wettbewerbsverbot- oder Geheimnisstreit.

### Umsetzung

- Schriftliche Hold-Notice an IT, HR, Vorgesetzte und DSB: Was wird angehalten (E-Mail, Slack, CRM, Backups, Logs), ab wann, für welchen Zeitraum, mit welcher Begruendung.
- Loeschroutinen pausieren: Backup-Rotation, Slack-Retention, E-Mail-Archivierung, GitHub-Branch-Cleanup, CRM-Loeschungen.
- Beweismittel-Kette dokumentieren: Hash-Werte der Snapshots, Zugriffsprotokolle, Vier-Augen-Bestaetigungen.
- Begrenzung: Hold nur auf relevante Datentoepfe, nicht repo-weit. Datenminimierung bleibt Pflicht.

### Aufhebung

- Hold wird aufgehoben, wenn Klagefrist abgelaufen und kein Verfahren anhaengig, kein Vorhalt mehr offen.
- Schriftliche Aufhebungsverfuegung, dann regulaere Loeschfristen (DSGVO Art. 5 Abs. 1 lit. e, BDSG § 26).

## Geheimnisschutz — GeschGehG-Hygiene beim Offboarding

- Geheimnisschutz nach § 2 Nr. 1 lit. b GeschGehG setzt **angemessene Geheimhaltungsmassnahmen** voraus — diese muessen beim Offboarding dokumentiert nachgehalten werden.
- Kuendigungsgespraech: Erinnerung an Verschwiegenheit nach Arbeitsvertrag, Hinweis auf GeschGehG, schriftliche Bestaetigung ueber Rueckgabe und Loeschung unternehmensbezogener Daten auf Privatgeraeten (BYOD).
- Wettbewerbsverbot, Kundenschutz, Abwerbeverbot: pruefen, ob nachvertraglich vereinbart und ob Karenzentschaedigung nach § 74 Abs. 2 HGB greift.
- BYOD-Container/MDM: Selective Wipe der Unternehmensdaten auf privaten Geraeten dokumentieren.
- GitHub-Forks und Cloud-Sync (Dropbox, iCloud, Google Drive privat) abfragen — Bestaetigung der Loeschung schriftlich einholen.

## Arbeitsweise

1. **Fakten sortieren:** Trennungstyp, Datum, Konflikteskalation, betroffene Konten und Geraete in maximal zehn Zeilen erfassen.
2. **Reihenfolge planen:** Anhand der Standard-Reihenfolge oben pruefen, ob Abweichungen noetig sind (z. B. fristlose Kuendigung mit Hausverbot — dann Sperre vor Gespraech).
3. **Trennlinie privat/dienstlich klaeren:** Nutzungsrichtlinie pruefen, Variante A oder B zuordnen, Datenschutzfilter setzen.
4. **Litigation Hold pruefen:** Risiko-Ampel Klage/Strafanzeige; falls gelb oder rot, Hold-Notice ausloesen.
5. **Geheimnisschutz aktiv stellen:** Rueckgabe- und Loeschbestaetigung, BYOD-Wipe, Wettbewerbsverbot.
6. **Output liefern:** Schritt-für-Schritt-Checkliste mit Verantwortlichen, Uhrzeiten, Norm-Pinpoints und Risikoampel.

## Output

- **Lage in fuenf Saetzen:** Trennungstyp, Datum, Konfliktrisiko, Variante A oder B, Litigation-Hold-Status.
- **Risikoampel:** arbeitsrechtlich, datenschutzrechtlich, geheimnisschutzrechtlich, kommunikativ.
- **Sperr-Reihenfolge** mit Uhrzeit, Verantwortlichen (HR, IT-Admin, DSB, Vorgesetzter), pro Konto.
- **Datensicherungsplan** vor Sperre: was wird wie gesichert, wo abgelegt, wer hat Zugriff.
- **Datenschutzvermerk:** Rechtsgrundlage (§ 26 BDSG / Art. 6 DSGVO), Datenminimierung, Vier-Augen-Bestaetigung.
- **Litigation-Hold-Status** mit Geltungsdauer und Aufhebungsdatum.
- **Geheimnisschutz-Bestaetigung** mit Rueckgabe-, Loesch- und BYOD-Wipe-Quittung.
- **Naechster Handgriff** mit Owner und Frist.

## Norm- und Quellenanker

- **Arbeitsrecht:** BGB §§ 611a, 622, 626, 666 (Auskunftspflicht); KSchG §§ 1, 4, 17, 23; BetrVG §§ 87 Abs. 1 Nr. 6 (technische Ueberwachung), 102; HGB § 74 Abs. 2 (nachvertragliches Wettbewerbsverbot Karenzentschaedigung).
- **Datenschutz:** DSGVO Art. 5, 6, 9, 15, 17, 28, 32, 33, 35, 88; BDSG §§ 22, 26; TTDSG §§ 19 ff. (Telemediendienste); TKG § 88 (Fernmeldegeheimnis).
- **Geheimnisschutz:** GeschGehG §§ 1, 2, 3, 6, 23.
- **Hinweisgeber:** HinSchG §§ 35 ff. (Repressalienverbot).
- **AGG:** §§ 13, 15 Abs. 4 (2-Monats-Frist).
- **Live-Pruefquellen:** gesetze-im-internet.de, dejure.org, openjur.de, bundesarbeitsgericht.de, eur-lex.europa.eu, curia.europa.eu, bfdi.bund.de, datenschutzkonferenz-online.de. Keine BeckRS-/juris-/Aufsatz-Blindzitate aus Modellwissen — Fundstellen live verifizieren.

## Eskalation

- **Sofort eskalieren** an Geschaeftsfuehrung und Anwalt bei: fristloser Kuendigung mit Strafvorwurf, GeschGehG-Verdachtsfall mit laufendem Datenabfluss, HinSchG-Meldung mit Repressalienvorwurf, AGG-Beschwerde, Datenschutzpanne nach Art. 33 DSGVO.
- **DSB einbeziehen** bei: Auswertung dienstlicher E-Mails in Variante B, BYOD-Wipe mit privaten Daten, Konfliktfall um Daten-Eigentum, Litigation Hold ueber sechs Monate.
- **Betriebsrat beteiligen**, wenn vorhanden, ueber § 87 Abs. 1 Nr. 6 BetrVG (technische Ueberwachungseinrichtungen), § 102 BetrVG (Kuendigungsanhoerung).
