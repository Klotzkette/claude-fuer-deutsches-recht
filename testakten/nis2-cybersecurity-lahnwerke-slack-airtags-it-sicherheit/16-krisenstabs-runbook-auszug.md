# Krisenstabs-Runbook — Auszug

## Aktivierungstrigger

Der Krisenstab wird aktiviert, sobald **eines** der folgenden Ereignisse eintritt:

- Vermuteter oder bestätigter Einbruch in produktive IT-Systeme (Produktion, Engineering, ERP, M365-Tenant).
- Eingehende Sicherheitswarnung des BSI, eines CERT, eines Versicherers oder eines Geschäftspartners mit konkretem Bezug auf Lahnwerke-Systeme.
- Ungeplanter Ausfall von M365 (Teams/Outlook/SharePoint) länger als 60 Minuten in Verbindung mit ungewöhnlichem Verhalten.
- Verlust eines mit Lahnwerke-Daten konfigurierten Endgeräts (Laptop, Smartphone, AirTag-bewehrte Werkstücke), insbesondere mit Hinweisen auf gezielten Diebstahl.
- Eingehender Hinweis über eine externe Meldestelle (Hinweisgeber, Auditor, Kunde) auf konkrete Datenschutz- oder Cybersicherheitsverletzungen.

## Besetzung

| Rolle | Hauptperson | Vertretung | Eskalationsbefugnis |
| --- | --- | --- | --- |
| Krisenstabsleitung | CEO | COO | volle |
| Informationssicherheit | CISO | Security-Engineer (Bereitschaft) | technisch |
| Rechtsabteilung | Justiziarin Dr. Wedekind | Stv. Justitiariat | rechtlich, einschl. Anzeigeerstattung |
| Datenschutz | DSB Frau Brauer (extern) | DSB-Stellvertretung interne IT | DSGVO-Meldung Art. 33 |
| HR / Personal | Personalleitung | Stv. PL | Beschäftigtenkommunikation |
| Externe Kommunikation | Kommunikationsleitung | Pressesprecher Stahlring AG (Eigentümer) | Pressemitteilungen |
| IT-Betrieb | Leitung IT-Operations | Bereitschaftsdienst | technische Sofortmaßnahmen |
| Externer Forensiker | Firma Bittner+Renz, Düsseldorf | Backup: NorthSec, Hamburg | Forensik-Image-Sicherung |

## Offene Lücken (Stand vor Vorfall)

- **Notfalltelefonliste:** Aktuell nur in SharePoint hinterlegt. Bei M365-Ausfall NICHT verfügbar. Sofortmaßnahme: Liste in verschlüsselter Offline-Kopie (Datentresor, USB) und Papierausdruck im Tresor der Geschäftsleitung; halbjährlicher Test.
- **Out-of-Band-Kommunikation:** Bisher kein Backup-Messenger. Empfehlung: Signal-Gruppe "Lahnwerke-CIRT" mit allen Krisenstabsmitgliedern, parallel SMS-Verteiler.
- **Krisenstabraum:** Bisher kein dedizierter Raum, der vom Hauptnetz abkoppelbar ist. Vorschlag: Besprechungsraum 4-A mit Stand-alone Internetzugang (LTE-Router) als Fallback-Krisenstabraum.
- **Decision-Log:** Bislang ohne strukturierte Vorgabe. Künftig pro Eskalationsstufe Pflichtprotokoll mit Zeitstempel, Beschluss, Begründung, Verantwortlichem.

## 0-30-Minuten-Checkliste

1. Alarm via Telefon an Krisenstabsleitung (CEO) und CISO; bei Nicht-Erreichbarkeit über Vertretungsliste durchrufen.
2. Erste Einschätzung CISO: betroffene Systeme, geschätzter Datenumfang, externe Sichtbarkeit.
3. Justiziarin entscheidet über sofortige NIS2-Frühwarnung (innerhalb 24 Stunden an BSI nach § 32 BSIG iVm NIS2-Umsetzung) und DSGVO-Meldung (innerhalb 72 Stunden nach Art. 33 DSGVO).
4. IT-Betrieb beginnt Isolierung betroffener Segmente, sichert Logs, hält forensisches Image vor.
5. Externer Forensiker wird informiert und in Bereitschaft gesetzt.
6. Kommunikationsleitung bereitet **Holding-Statement** vor (keine Veröffentlichung ohne Krisenstabsleitung).

## 30-Minuten-bis-4-Stunden-Checkliste

1. Krisenstab tagt physisch oder per Signal/Telefon — kein M365.
2. Decision-Log starten, Verantwortlichkeiten dokumentieren.
3. Eingehende Anfragen (Kunden, Presse, Beschäftigte) zentral kanalisieren über Kommunikationsleitung.
4. Konkrete NIS2-Frühwarnung an BSI vorbereiten; bei wesentlicher Beeinträchtigung Meldung über das BSI-Meldeportal absetzen (Konto siehe Justiziariat).
5. Bei personenbezogenen Daten: Vorabprüfung Art. 33 DSGVO durch DSB; bei "wahrscheinlich Risiko für Rechte und Freiheiten" → Meldung an Landesdatenschutzaufsicht.

## 4-bis-24-Stunden-Checkliste

1. Erste forensische Erkenntnisse: Eindringvektor, Persistenzmechanismen, betroffene Datenkategorien.
2. NIS2-**Erstmeldung** an BSI ergänzen (sofern noch nicht abgesetzt).
3. Versicherung (Cyber-Police) informieren — Frist je Police prüfen, oft 48 Stunden.
4. Bei betroffenen Geschäftspartnern: vertragliche Informationspflichten (AVV, B2B-Verträge) auswerten.
5. Beschäftigtenkommunikation: kurze, sachliche Mitteilung; Hinweis auf Mitwirkungspflichten und Pressekontakt-Verbot.

## 24-bis-72-Stunden-Checkliste

1. NIS2-**Folgenotmeldung** mit konkretem Schadensbild.
2. Art. 33 DSGVO Meldung absetzen, sofern Erkenntnisse die Risikoeinschätzung bestätigen.
3. Bei Betroffenen-Risiko nach Art. 34 DSGVO: Benachrichtigung der Betroffenen vorbereiten.
4. Externer Krisenkommunikator (auf Bereitschaft) erstellt Q&A für Presse und Vertrieb.
5. Aufsichtsrat informieren (gemäß § 90 AktG, soweit konzernrechtlich einschlägig — Stahlring AG als Eigentümerin).

## Nach Abschluss

- Vollständige Schlussmeldung an BSI gemäß NIS2-Vorgaben.
- Lessons-Learned-Workshop binnen 4 Wochen.
- Anpassung dieses Runbooks; Versionierung mit Datum und Verantwortlichem im Krisenstabsraum.
