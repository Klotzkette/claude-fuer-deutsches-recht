---
name: ins-delisting-bernahmeangebot
description: "Ins 038 Delisting, Ins 039 Bernahmeangebot: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Ins 038 Delisting, Ins 039 Bernahmeangebot

## Arbeitsbereich

Dieser Skill bündelt **Ins 038 Delisting, Ins 039 Bernahmeangebot** zu einem konkreten Arbeitsgang. Starte mit dem Modul, das die Tatsachen der Akte trägt; weitere Module nur hinzunehmen, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output betreffen.

## Arbeitsmodule

| Arbeitsmodul | Fokus |
| --- | --- |
| `ins-038-delisting` | Prueft insiderrechtliche Pflichten beim Delisting: Ad-hoc beim Beschluss, Squeeze-out-Kopplung, letzter Handelstag und Insiderlisten-Abschluss. |
| `ins-039-bernahmeangebot` | Koordiniert MAR und WpUeG-Pflichten bei Uebernahmeangeboten: Insiderinformation des Bieters, Ad-hoc, Angebotsunterlage, Insiderlisten beider Seiten. |

## Arbeitsweg

Für **Ins 038 Delisting, Ins 039 Bernahmeangebot** zuerst das Arbeitsmodul wählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `insiderrecht-compliance` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; Module nur kombinieren, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Arbeitsmodule im Detail

## 1. `ins-038-delisting`

**Fokus:** Prueft insiderrechtliche Pflichten beim Delisting: Ad-hoc beim Beschluss, Squeeze-out-Kopplung, letzter Handelstag und Insiderlisten-Abschluss.

# Delisting – Insiderrecht und Ad-hoc-Pflicht

## Rechtlicher Rahmen

Der Beschluss des Vorstands oder des Hauptaktionärs, den Widerruf der Börsenzulassung (Delisting)
zu beantragen, ist typischerweise eine kursrelevante Insiderinformation. Art. 17 MAR löst die
Ad-hoc-Pflicht aus. Nach dem Widerruf der Börsenzulassung entfällt die MAR-Pflicht für künftige
Ereignisse; laufende Compliance-Pflichten (Insiderliste 5 Jahre) bleiben bestehen.

Rechtsgrundlagen:
- Art. 7, 17 MAR: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0596
- § 39 BörsG (Widerruf der Börsenzulassung): https://www.gesetze-im-internet.de/borsG_2007/__39.html
- §§ 327a ff. AktG (Squeeze-out): https://www.gesetze-im-internet.de/aktg/__327a.html
- BaFin-Emittentenleitfaden: https://www.bafin.de/dok/8252648

## Ziel dieses Skills

Dieser Skill steuert die insiderrechtliche Compliance beim Delisting von der Entscheidung
bis zur endgültigen Zulassungsbeendigung.

## Arbeitsprogramm

### Schritt 1 – Entstehungszeitpunkt der Insiderinformation

- Wann wurde die Delisting-Entscheidung getroffen?
 (Vorstandsbeschluss, Hauptaktionär-Entscheidung, AR-Billigung)
- Geltl/Daimler-Test: Bereits bei ernsthafter Prüfung des Delistings?
- Kursrelevanz: Delisting ist regelmäßig kursrelevant (Liquiditätsverlust, Squeeze-out-Erwartung)

### Schritt 2 – Ad-hoc-Pflicht

- Unverzügliche Veröffentlichung nach Beschluss
- Inhalt: Geplantes Datum des Delisting-Antrags, Begründung, Auswirkungen auf Aktionäre,
 ggf. Abfindungsangebot
- Bei Squeeze-out-Kopplung: Koordination der Ad-hoc mit Squeeze-out-Ankündigung

### Schritt 3 – Squeeze-out-Kopplung

- Delisting wird häufig mit Squeeze-out nach §§ 327a ff. AktG kombiniert
- Abfindungsangebot: Eigene Ad-hoc-Pflicht nach WpÜG (§ 29 WpÜG)
- Koordination: Delisting-Ad-hoc und WpÜG-Angebot simultan oder sequenziell?

### Schritt 4 – Abschluss der MAR-Pflichten

- Nach Widerruf der Börsenzulassung: Keine neuen Ad-hoc-Pflichten für die Gesellschaft
- Aber: Aufbewahrungspflichten (Insiderliste 5 Jahre, Compliance-Dossier)
- PDMRs: Directors' Dealings-Pflicht endet mit letztem Handelstag
- Insiderliste: Alle offenen Einträge schließen (Austrittsdaten eintragen)

### Schritt 5 – Aktionärskommunikation

- Frühzeitige Information der Aktionäre über Delisting-Absicht
- Abfindungsangebot und Zeitplan kommunizieren
- BaFin-Genehmigung des Widerrufsantrags abwarten

## Red-Team-Fragen

- Wurde der frühestmögliche Entstehungszeitpunkt der Insiderinformation identifiziert?
- Wurde die Ad-hoc unverzüglich nach dem Beschluss veröffentlicht?
- Wurden alle parallelen Pflichten (WpÜG, Squeeze-out) koordiniert?
- Wurden alle Compliance-Unterlagen archiviert (5-Jahres-Frist)?
- Wurden PDMRs über das Ende ihrer Meldepflichten informiert?

## Ausgabeformat

Erzeuge:
1. Delisting-Zeitstrahl (Entscheidung → Ad-hoc → Antrag → Widerruf → Ende MAR-Pflichten)
2. Ad-hoc-Entwurf Delisting
3. Insiderlisten-Abschlussprotokoll
4. Squeeze-out-Koordinationsplan (falls relevant)

Belege ausschließlich mit: eur-lex.europa.eu, gesetze-im-internet.de, bafin.de, dejure.org.

## Weitere Hinweise

Beim regulären Delisting (kein Squeeze-out) hat das Bundesverfassungsgericht in der
Frosta-Entscheidung (BVerfG 2 BvR 2103/13) klargestellt, dass kein Pflichtangebot nach
WpÜG erforderlich ist. Gleichwohl müssen Aktionäre ausreichend Zeit erhalten, ihre Aktien
zu veräußern (BörsG). Die Ad-hoc bei Delistingankündigung muss daher den geplanten Zeitrahmen
für die Einstellung des Börsenhandels klar kommunizieren.

Weitere Quellen:
- § 39 BörsG: https://www.gesetze-im-internet.de/borsG_2007/__39.html
- BaFin-Emittentenleitfaden: https://www.bafin.de/dok/8252648

## 2. `ins-039-bernahmeangebot`

**Fokus:** Koordiniert MAR und WpUeG-Pflichten bei Uebernahmeangeboten: Insiderinformation des Bieters, Ad-hoc, Angebotsunterlage, Insiderlisten beider Seiten.

# Übernahmeangebot – MAR und WpÜG

## Rechtlicher Rahmen

Öffentliche Übernahmeangebote nach WpÜG unterliegen neben den WpÜG-Pflichten auch den MAR-
Vorschriften. Der Bieter erlangt regelmäßig Insiderinformationen über die Zielgesellschaft
(Due Diligence). Die Zielgesellschaft hat eigenständige MAR-Pflichten. WpÜG § 10 regelt die
Veröffentlichungspflicht des Bieters. Die BaFin koordiniert MAR-Compliance und WpÜG-Verfahren.

Rechtsgrundlagen:
- Art. 7, 17 MAR: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0596
- WpÜG §§ 10, 29, 35: https://www.gesetze-im-internet.de/wpueg/__10.html
- AktG § 53a ff. (Gleichbehandlung): https://www.gesetze-im-internet.de/aktg/__53a.html
- BaFin-Emittentenleitfaden: https://www.bafin.de/dok/8252648

## Ziel dieses Skills

Dieser Skill koordiniert die insiderrechtlichen Pflichten von Bieter und Zielgesellschaft
in einem öffentlichen Übernahmeverfahren.

## Arbeitsprogramm

### Schritt 1 – Insiderinformation des Bieters

- Bieter erlangt im Rahmen der Due Diligence Insiderinformationen über die Zielgesellschaft
- Diese Informationen begründen Handelsverbot für Bieter und seine Berater (Art. 14 MAR)
- Bieter darf nicht auf Basis dieser Informationen in Aktien der Zielgesellschaft handeln
- Ausnahme: Paketerwerb im Rahmen des Angebots ist reguläres Vorgehen; aber kein spekulativer
 Vorab-Erwerb auf Basis von DD-Insiderinformationen

### Schritt 2 – Insiderinformation der Zielgesellschaft

- Zielgesellschaft: Hat Informationen über Transaktion (kursrelevant)
- Aufschub nach Art. 17 Abs. 4 MAR möglich: Laufende Verhandlungen
- Trigger für Sofortveröffentlichung: WpÜG § 10-Veröffentlichung des Bieters

### Schritt 3 – WpÜG § 10-Veröffentlichung des Bieters

- Bieter muss Entscheidung zur Veröffentlichung eines Angebots unverzüglich gem. § 10 WpÜG
 veröffentlichen (keine MAR Ad-hoc, aber analoge Wirkung)
- Koordination: BaFin-Meldung gleichzeitig mit § 10-Veröffentlichung
- Zielgesellschaft: Unmittelbar nach § 10-Veröffentlichung eigene Stellungnahme prüfen

### Schritt 4 – Insiderlisten beider Seiten

- Bieter: Eigene Insiderliste für alle Personen mit DD-Zugang (Insiderinformation über Ziel)
- Zielgesellschaft: Insiderliste für alle Personen, die von der Transaktion wissen
- Externe Berater: Eigene Listen und Chinese Walls
- Bei Abbruch: Insiderlisten schließen, aber 5 Jahre aufbewahren

### Schritt 5 – PDMR-Eigengeschäfte und Angebotsunterlage

- PDMRs der Zielgesellschaft: Können im Rahmen des Angebots Aktien einreichen (kein MAR-Verstoß)
- Aber: Keine eigenständigen Käufe auf Basis der Übernahmeinsiderinformation vor § 10-Veröff.
- Angebotsunterlage: Enthält keine MAR-pflichtigen Informationen, aber alle wesentlichen
 Angaben nach WpÜG

## Red-Team-Fragen

- Wurden Bieter-Berater auf das Handelsverbot für DD-Insiderinformationen hingewiesen?
- Hat die Zielgesellschaft den Aufschub nach Art. 17 Abs. 4 MAR rechtmäßig aufrechterhalten?
- Wurden PDMRs beider Gesellschaften auf ihre jeweiligen Handelsverbote hingewiesen?
- Wurden Insiderlisten beider Gesellschaften zeitgerecht und vollständig geführt?

## Ausgabeformat

Erzeuge:
1. MAR/WpÜG-Pflichtentabelle (Bieter × Zielgesellschaft × Berater)
2. Zeitstrahl Insiderinformation → § 10 WpÜG → Ad-hoc Zielgesellschaft
3. Doppeltes Insiderlisten-Framework
4. PDMR-Eigengeschäfts-Sperrprotokoll (beide Gesellschaften)

Belege ausschließlich mit: eur-lex.europa.eu, gesetze-im-internet.de, bafin.de, dejure.org.

## Weitere Hinweise

Bei freiwilligen Übernahmeangeboten kann der Bieter im Vorfeld Pakete außerhalb des formellen
Angebots erwerben (Vorerwerb). Diese Transaktionen sind auf Art. 14 MAR-Verträglichkeit zu prüfen:
Hat der Bieter bei diesen Vorerwerben bereits Insiderinformationen über die Zielgesellschaft genutzt
(z. B. aus einer vertraulichen Due Diligence)? Das WpÜG-Transparenzgebot (§ 23 WpÜG) und MAR
müssen koordiniert eingehalten werden.

Weitere Quellen:
- WpÜG § 23: https://www.gesetze-im-internet.de/wpueg/__23.html
- BaFin-Emittentenleitfaden: https://www.bafin.de/dok/8252648
