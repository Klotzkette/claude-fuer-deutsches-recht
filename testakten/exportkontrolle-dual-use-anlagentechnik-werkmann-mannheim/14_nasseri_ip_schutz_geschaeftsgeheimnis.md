# Aktenstück 14 — IP-Schutz und Geschäftsgeheimnisse: Ex-Mitarbeiter Nasseri / GeschGehG

**Aktenzeichen:** (intern) WAT-IP-2026/01
**Erstellt:** 28. April 2026
**Bearbeitung:** RAin Dr. Boekenkamp; Ass. Pfaff
**Rechtsgrundlagen:** Gesetz zum Schutz von Geschäftsgeheimnissen (GeschGehG, BGBl. I 2019, S. 466); Arbeitsvertrag Nasseri; IT-Forensik-Bericht (Datev Recht / forensics+)

---

## 1. Person und Kenntnisstand Nasseri

Zubair Nasseri (Jg. 1989, deutsch-iranische Staatsangehörigkeit) war von März 2018 bis Januar 2025 als Senior Software Engineer in der IT-Abteilung der Werkmann Anlagentechnik AG tätig. Sein Arbeitsbereich umfasste:
- Entwicklung und Wartung der MFR-Steuerungssoftware SmartFlow (aktuell v3.7)
- Schnittstellenprogrammierung für SAP-Integration
- Zugriff auf CAD-Datenbanken (CATIA V5, Solid Edge) im Rahmen von Engineering-Support-Tätigkeiten

Nasseri verfügte bis zu seinem Ausscheiden über Zugriffsrechte auf folgende IT-Systeme:
- SmartFlow-Quellcode-Repository (GitLab, intern)
- CAD-Bibliothek (Werkmann CAD-Server, Read-Access)
- Fertigungsauftragssystem SAP PP
- Kein Zugang zu Exportkontroll-Systemen oder Kundendaten

Nasseri hat das Unternehmen zum 31. Januar 2025 verlassen (Eigenkündigung, Kündigungsschreiben vom 03. Dezember 2024). IT-Zugänge wurden am 21. Februar 2025 gesperrt (interne IT-SOP: Sperrung innerhalb von 30 Tagen nach Austritt — Frist wurde damit geringfügig überschritten; gesperrt hätte werden sollen bis 28. Februar 2025).

---

## 2. Forensische IT-Untersuchung

### 2.1 Auftrag und Methodik

Die Forensikuntersuchung wurde von der forensics+ GmbH (Frankfurt) im Zeitraum 22. März bis 15. April 2026 durchgeführt. Auftrag: Analyse aller Log-Daten (GitLab-Commit-Logs, Windows-Event-Logs, VPN-Verbindungsprotokolle) im Zeitraum Dezember 2024 bis Januar 2025.

### 2.2 Ergebnisse

**Kritischer Befund:** Am 28. Dezember 2024 um 22:47 Uhr (MEZ) erfolgte ein GitLab-Klon-Befehl des Benutzerkontos nasseri@werkmann.de auf das gesamte SmartFlow-Repository. Der Befehl `git clone --mirror git@gitlab.werkmann.intern:smartflow/main.git` spiegelt sämtliche Branches inklusive der Commit-Historie und Tags. Der Umfang des geklonten Repositories: ca. 2,3 GB. Dieser Klon-Vorgang ist im Normalbetrieb unüblich (kein Entwicklungsauftrag in diesem Zeitraum) und unmittelbar vor Nasseri-Urlaub (29.12.2024–03.01.2025) erfolgt.

**Weiterer Befund:** Am 15. Januar 2025 (zwei Wochen vor seinem letzten Arbeitstag) hat Nasseri über den Werkmann-VPN-Zugang 14 CAD-Dateien (Dateinamen: MFR-3400X_Assembly_v3.stp, MFR-3400X_Sealdraw.stp, etc.) auf eine externe Dropbox-URL heruntergeladen (erkennbar aus Firewall-Log: `DENY outbound 185.34.xxx.xxx` — der Download wurde durch den Firewall-Filter teilweise blockiert; zwei Dateien wurden trotzdem durchgelassen).

**Nicht festgestellt:** Ein Kontakt zu Institutionen in Teheran oder Iranisch-nahen Adressaten aus den IT-Systemen ist in den vorliegenden Logs nicht nachweisbar.

---

## 3. Rechtliche Würdigung

### 3.1 GeschGehG — Unterlassungs- und Schadensersatzansprüche

§ 2 GeschGehG definiert Geschäftsgeheimnis als Information, die:
(a) geheim ist (nicht allgemein bekannt oder leicht zugänglich);
(b) wirtschaftlichen Wert hat, weil sie geheim ist;
(c) angemessenen Geheimhaltungsmaßnahmen des rechtmäßigen Inhabers unterliegt.

Der SmartFlow-Quellcode und die MFR-3400X-CAD-Zeichnungen erfüllen diese Voraussetzungen (interne Vertraulichkeitskennzeichnung; Zugriffssteuerung; wirtschaftlicher Wert als Kerntechnologie).

§ 4 GeschGehG (Handlungsverbote): Die unbefugte Erlangung eines Geschäftsgeheimnisses ist verboten. Der Git-Klon am 28.12.2024 ohne dienstlichen Auftrag stellt ein unbefugtes Erlangen dar.

§ 6 GeschGehG: Derjenige, der ein Geschäftsgeheimnis unbefugt erlangt, hat dem Inhaber den daraus entstehenden Schaden zu ersetzen. Anspruchsinhalt: entgangener Gewinn (§ 252 BGB), Lizenzanalogie, Herausgabe des Verletzergewinns.

### 3.2 Strafrecht

§ 23 GeschGehG sieht eine Strafbarkeit vor (Freiheitsstrafe bis zu drei Jahren oder Geldstrafe), wenn Geschäftsgeheimnisse unbefugt erlangt werden, um sich oder einem Dritten einen Vorteil zu verschaffen. Voraussetzung ist ein Strafantrag (§ 23 Abs. 4 GeschGehG: auf Antrag).

---

## 4. Handlungsempfehlungen

1. **Strafanzeige:** Erstattung einer Strafanzeige bei der Kriminalpolizei Mannheim wegen unbefugter Erlangung von Geschäftsgeheimnissen (§ 23 GeschGehG) sowie versuchtem Verrat von Geschäftsgeheimnissen (§ 23 Abs. 1 GeschGehG). Verbunden mit Strafantrag nach § 23 Abs. 4 GeschGehG.
2. **Zivilrechtliche Klage:** Klage auf Unterlassung und Schadensersatz vor dem LG Mannheim (Sitz Werkmann; §§ 6, 7 GeschGehG). Streitwert: offen; vorläufig 500.000 EUR.
3. **Technische Maßnahmen:** Sofortiger Rollout neuer Softwareversionen (SmartFlow v3.8 mit geänderter Kernarchitektur); Änderung aller kryptografischen Schlüssel der MFR-Steuerung.
4. **Information OFAC/Hogan Lovells:** Möglicher Wissenstransfer durch Nasseri als Risikofaktor in der OFAC-Response darstellen, ohne jedoch unbewiesene Verbindungen zu behaupten.
5. **BfV-Kontakt:** Über das Landesamt für Verfassungsschutz Baden-Württemberg Kontakt zum BfV aufnehmen; Wirtschaftsspionage-Meldung.

---

*Bearbeitung: Dr. Boekenkamp / Ass. Pfaff — Stand: 30. April 2026*
