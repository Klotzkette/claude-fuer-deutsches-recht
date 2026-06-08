---
name: datenschutz-vvt-tom-avv-hausverwaltung
description: "VVT nach Art. 30 DSGVO, TOM nach Art. 32 und AVV nach Art. 28 DSGVO für die typische Hausverwaltung (Stand 06/2026): Verarbeitungsverzeichnis-Muster, TOM-Mindeststandards, AVV-Pflichten gegenueber Buchhaltungssoftware und Cloud-Diensten."
---

# Datenschutz: VVT, TOM und AVV für die Hausverwaltung

## Fachlicher Anker

- **Normen:** §§ 535, §§ 18, § 16 Abs. 2.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Ziel

Hausverwaltungen sind Verantwortliche im Sinne des Art. 4 Nr. 7 DSGVO und müssen ein vollständiges Verzeichnis von Verarbeitungstätigkeiten (VVT) nach Art. 30 führen, angemessene technisch-organisatorische Maßnahmen (TOM) nach Art. 32 umsetzen und mit allen Auftragsverarbeitern schriftliche AVV nach Art. 28 schließen. Der Skill erzeugt fertige Muster-Dokumente und prüft Lücken im Datenschutz-Setup.

## Verarbeitungstätigkeiten (VVT-Tabelle)

| Verarbeitungstätigkeit | Kategorie personenbezogener Daten | Zweck | Rechtsgrundlage | Löschfrist |
|---|---|---|---|---|
| Eigentümerstammdaten | Name, Adresse, Bankverbindung | Vertragserfüllung WEG-Verwaltung | Art. 6 Abs. 1 lit. b | 10 Jahre (§ 257 HGB) |
| Beschlusssammlung | Namen abstimmender Eigentümer | Dokumentationspflicht § 24 WEG | Art. 6 Abs. 1 lit. c | Dauerhaft (Gemeinschaftseigentum) |
| Buchhaltung / Mahnwesen | Bankdaten, Zahlungsrückstände | Vertragserfüllung, berechtigtes Interesse | Art. 6 Abs. 1 lit. b/f | 10 Jahre (§ 257 HGB) |
| Versammlungsprotokolle | Namen, Wortbeiträge, Stimmverhalten | § 24 Abs. 6 WEG | Art. 6 Abs. 1 lit. c | 30 Jahre empfohlen |
| Beirats-Kommunikation | Namen, E-Mail, Telefon | Vertragserfüllung | Art. 6 Abs. 1 lit. b | 3 Jahre nach Mandatsende |
| Videoüberwachung Eingang | Bildaufnahmen | Hausrecht, Einbruchsschutz | Art. 6 Abs. 1 lit. f | Max. 72 Stunden (DSK-OH) |
| Schlüsselverwaltung | Namen, Schlüssel-Nr., Ausgabedatum | Sicherheit Gemeinschaftseigentum | Art. 6 Abs. 1 lit. f | 5 Jahre nach Rückgabe |

Norm Art. 30 DSGVO: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32016R0679

## AVV-Pflichten gegenüber Auftragsverarbeitern

AVV nach Art. 28 Abs. 3 DSGVO ist Pflicht bei: Buchhaltungssoftware (DATEV, Karthago, Sander+Doll, Casavi), Cloud-Speicher (Microsoft 365, Google Workspace), Steuerberater (wenn Zugriff auf Mandantendaten), Versammlungs-Tools (Zoom, MS Teams), Inkassobüros, externen Beiratsplattformen und IT-Dienstleistern. Prüfpunkte je AVV: Weisungsgebundenheit, Unterauftragnehmer-Liste, Löschverpflichtung nach Vertragsende, Audit-Recht des Verantwortlichen, Sicherheitsmaßnahmen (Art. 32). Fehlt eine AVV, droht Bußgeld bis 10 Mio. Euro oder 2 % des Jahresumsatzes (Art. 83 Abs. 4 DSGVO).

## TOM-Mindeststandards für Hausverwaltungen

- **Rollen-/Rechtekonzept:** Getrennte Zugänge je Mitarbeiter, kein gemeinsames Login, Protokollierung Admin-Zugriffe.
- **2-Faktor-Authentifizierung:** Pflicht für alle Cloud-Zugänge (Microsoft 365, Google Workspace, Casavi-Portal).
- **Verschlüsselte Backups:** AES-256, mindestens 3-2-1-Regel (3 Kopien, 2 Medien, 1 off-site), Wiederherstellungstest quartalsweise.
- **Festplattenverschlüsselung:** BitLocker (Windows) oder FileVault (macOS) auf jedem Verwalter-Laptop und -Tablet; Belege für Einrichtung aufbewahren.
- **Schreddervorgaben Papierakten:** DIN 66399 Sicherheitsstufe P-4 (Partikelschnitt) für Unterlagen mit personenbezogenen Daten; Schredder-Protokoll oder Zertifikat Dienstleister.
- **Schlüsseltresor:** Schlüsselausgabe nur gegen Unterschrift, Protokoll aller Entnahmen und Rückgaben, Tresor-Zugriffsprotokoll.
- **Passwortrichtlinie:** Mindestlänge 12 Zeichen, keine Wiederverwendung, Password-Manager für Team.

Norm Art. 32 DSGVO: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32016R0679

## Beschäftigtendatenschutz (wenn Verwalter Mitarbeiter hat)

§ 26 BDSG regelt Verarbeitung von Beschäftigtendaten: Bewerbungsunterlagen (Aufbewahrung max. 6 Monate nach Absage), Gehaltsunterlagen (10 Jahre), Krankheitstage (nur Zeitraum, nicht Diagnose). Betriebsrat-Vereinbarungen gehen als Erlaubnistatbestand dem Art. 6 DSGVO vor. Norm: https://www.gesetze-im-internet.de/bdsg_2018/__26.html

## Haftung nach Art. 82 DSGVO

EuGH, Urteil vom 14.12.2023, C-340/21 (Bulgarische NRA-Hack): Schon die unbefugte Offenlegung oder der unbefugte Zugang begründet Haftung, ohne dass materieller Schaden bewiesen werden muss; immaterieller Schaden (Kontrollverlust über Daten) genügt. Für Hausverwaltungen bedeutet dies: Gestohlener Laptop ohne Verschlüsselung = Schadenersatzpflicht gegenüber betroffenen Eigentümern. Urteil: https://curia.europa.eu/juris/document/document.jsf?docid=280325&doclang=DE

## Output

- VVT-Muster als tabellarisches Gerüst (Excel-Spalten: Tätigkeit, Daten, Zweck, Rechtsgrundlage, Löschfrist, Verantwortlicher, Auftragsverarbeiter)
- AVV-Vorlagen-Checkliste (Mindestinhalte Art. 28 Abs. 3 lit. a-h)
- TOM-Audit-Checkliste (20 Prüfpunkte mit Ja/Nein/Teilweise)
- Bestandsaufnahme-Bogen für neues Mandat (Datenschutz-Erstprüfung)

## Cross-Refs

- Dokumentenfreigabe und Einsichtsrechte → `datenschutz-dokumentenfreigabe`
- Betroffenenrechte (Auskunft, Löschung) → `datenschutz-betroffenenrechte-auskunft-loeschung-weg`
- Datenpannen melden → `datenschutz-datenpanne-meldung-72h`
- Verwalterpflichten allgemein → `verwalterpflichten-26-27-weg`

## Quellenpflicht

`rechtsstand-mai-2026-faktenbank` laden. DSGVO-Texte über https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32016R0679 live verifizieren. BDSG über https://www.gesetze-im-internet.de/bdsg_2018/ abrufen. DSK-Orientierungshilfen unter https://www.datenschutzkonferenz-online.de prüfen — Fassungen ändern sich.
