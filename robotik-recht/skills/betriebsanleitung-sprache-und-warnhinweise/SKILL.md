---
name: betriebsanleitung-sprache-und-warnhinweise
description: "Prüft Betriebsanleitung, Sicherheitsinformationen, digitale Anleitung, Sprache, Restgefahren und Verständlichkeit für Zielgruppen."
---

# Betriebsanleitung, Sprache und Warnhinweise

## Fachkern: Betriebsanleitung, Sprache und Warnhinweise
- **Normen-/Quellenanker:** EU-Maschinenverordnung, Produkthaftungsrecht, ProdSG/GPSR, AI Act, MDR/MPDG bei Medizinrobotik, DSGVO, Cybersecurity/NIS2 und Arbeitsschutz.
- **Entscheidende Weiche:** Prüfe Rolle Hersteller/Integrator/Betreiber, bestimmungsgemäße Verwendung, CE-Konformität, Sicherheitsfunktion, Lern-/Updateverhalten, Schadenpfad und Rückrufpflicht.

## Worum geht es konkret

Die Betriebsanleitung ist ein Sicherheitsbauteil im juristischen Sinn: Fehler in Sprache, Verständlichkeit, Vollständigkeit oder Warnhinweisen lösen Konstruktions- oder Instruktionsfehler nach § 1 ProdHaftG, § 823 BGB und neuer Produkthaftungs-RL (EU) 2024/2853 aus. Die MaschinenVO VO (EU) 2023/1230 erlaubt erstmals **digitale** Anleitungen unter Bedingungen (Art. 10 Abs. 7 sowie Anhang III Nr. 1.7.4) – ein Paradigmenwechsel. Bei KI-Funktionen verlangt Art. 13 KI-VO eine Gebrauchsanweisung mit besonderem Inhalt. Dieser Skill prüft Anleitung und Warnhinweise auf Compliance und Haftungsrobustheit.

## Wann dieses Modul hilft / Kaltstart-Fragen

1. **Rolle:** Hersteller, Importeur, technischer Redakteur, Marktüberwachung, Anwalt im Haftungsstreit.
2. **Produkt:** Industrieroboter, Cobot, Service-Roboter, Verbraucher-Robotik (z. B. Saugroboter).
3. **Zielgruppe:** Fachkraft, Endverbraucher, Pflegekraft, Patient, behindertengerecht?
4. **Sprache:** Welche Amtssprachen des Inverkehrbringens?
5. **Format:** Papier, PDF, Online, AR-/VR-Anleitung; Anleitung auf dem Roboter selbst?

## Rechtlicher Rahmen

- **MaschinenVO** VO (EU) 2023/1230 Anhang III Nr. 1.7 Information und Warnhinweise; Art. 10 Abs. 7 zur digitalen Form; Geltung ab 20.01.2027.
- **Maschinen-RL 2006/42/EG** (Übergang bis 19.01.2027) verlangt Anleitung in Amtssprachen des Mitgliedstaats des Inverkehrbringens.
- **ProdSG / GPSR** VO (EU) 2023/988: Information für Verbraucher.
- **ProdHaftG / VO (EU) 2024/2853 (neu)**: Instruktionsfehler als Produktfehler.
- **§ 823 BGB**: ständige Rspr. des BGH zu Instruktionspflichten (Hersteller muss vor Gefahren in vernünftigerweise vorhersehbarer Verwendung warnen).
- **KI-VO** Art. 13 Transparenz; Art. 26 Abs. 1 Pflichten der Betreiber, Anleitung zu beachten; Art. 50 Transparenz bei interaktiven KI-Systemen.
- **GS-Zeichen / TÜV** ProdSG § 21 als ergänzendes Qualitätssignal.
- **Sprachenregime**: Amtssprache des Mitgliedstaats; in Deutschland deutsch (zumindest für Sicherheits- und Warninhalte).

## Schritt für Schritt

1. **Zielgruppenanalyse.** Fachkraft oder Endverbraucher? Sprachniveau, Vorbildung, Sinneseinschränkungen.
2. **Inhalt nach Anhang III Nr. 1.7 MaschinenVO**: Identifikation, Beschreibung, bestimmungsgemäße Verwendung, Restrisiken, Aufstellung/Anschluss, Bedienung, Wartung, Außerbetriebnahme, Schaltpläne, Lärm-/Vibrationsemissionen.
3. **KI-spezifischer Inhalt** Art. 13 Abs. 3 KI-VO: Identität Anbieter, Zweck, Leistungsmerkmale, Genauigkeit/Robustheit/Sicherheit-Grenzen, Human-Oversight-Maßnahmen, Lebensdauer, Wartung.
4. **Restrisiken explizit benennen.** Risikobeurteilung als Anhang oder zusammengefasst.
5. **Warnhinweise** nach ANSI Z535 / ISO 3864 / ISO 7010: Signalwort (GEFAHR/WARNUNG/VORSICHT/HINWEIS) + Pictogramm + Folge + Vermeidung.
6. **Digitale Anleitung** Anhang III Nr. 1.7.4 MaschinenVO: Verfügbarkeit per QR/URL, Auffindbarkeit für 10 Jahre, papierne Sicherheitsinformationen "free of charge upon request" mind. zwei Jahre nach Inverkehrbringen.
7. **Sprache** der einschlägigen Amtssprache des MS des Inverkehrbringens; Sicherheitsinhalte vor allem.
8. **Verständlichkeitstest** mit Probanden der Zielgruppe; bei Verbraucherprodukten Lesetest auf Schulniveau 8.
9. **Versionierung** und Archivierung; Anleitung ist Teil der technischen Dokumentation 10 Jahre (Art. 11 MaschinenVO; Art. 18 KI-VO).

## Trade-off-Matrix

| Frage | Konservativ | Modern | Empfehlung |
|---|---|---|---|
| Papier-Anleitung | immer | nur digital | bei MaschinenVO-Geltung digital + Sicherheits-Auszug Papier |
| Sprachen | nur Amtssprache | nur Englisch | nur Amtssprache; English ergänzend |
| Warnsymbole | viele | wenige Schlüsselbilder | nach Risiko priorisieren |
| Online-Updates | jährlich | rolling | Versionsstand sichtbar; alte Versionen auffindbar |

## Praxistipps

- **Quick-Start-Card** in jeder Sprache der Hauptmärkte; Sicherheitskern in einer Seite.
- **AR-Overlay** für Wartung – aber Papier-Notfallseite immer.
- **Übersetzung** durch Fachübersetzer mit Sicherheitskenntnis – nicht maschinell ohne Review.
- **Symbol-Glossar** als Pull-Out.
- **Akustische Warnung** bei interaktiver Robotik – Sprache zusätzlich zu Display.

## Mustertexte

**Warnhinweis (ANSI Z535/ISO 3864 Format):**

> WARNUNG. Quetschgefahr durch Cobot-Arm. Nicht in den Bewegungsraum greifen, solange die LED grün leuchtet. Bei Wartung Schlüsselschalter auf "Service"; nur autorisiertes Personal.

**Auszug digitale Anleitung – Hinweis auf Papier-Auszug:**

> Diese Anleitung ist digital unter https://[…]/manuals/[Seriennummer] in der jeweils gültigen Fassung verfügbar. Sicherheitsinformationen sind in gedruckter Form Bestandteil der Lieferung. Auf schriftliche Anforderung an [Adresse] senden wir Ihnen innerhalb von zwei Jahren nach Inverkehrbringen eine vollständige Papierfassung kostenfrei zu (Art. 10 Abs. 7 MaschinenVO).

**KI-Transparenz (Art. 13 Abs. 3 KI-VO, Auszug):**

> Das im Roboter integrierte KI-System "VisionCobot 3" dient der Hinderniserkennung im Cobot-Arbeitsraum. Trainingsdatenbasis: 2,8 Mio. annotierte Frames in den in Anlage B genannten Kontexten. Bekannte Genauigkeitsgrenzen: bei Gegenlicht über 80.000 Lux Recall-Reduktion um bis zu 12 %. Menschliche Kontrolle: jederzeitiges Not-Halt per Schlüssel; Override via Operator-Konsole. Lebensdauer-Garantie: 5 Jahre.

## Typische Fehler

- **Unverständliche Sprache** durch wörtliche Maschinenübersetzung.
- **Risikobeurteilung als alleinige Informationsquelle**; Anleitung nicht abgeleitet.
- **Pauschale Warnungen** ("Vorsicht! Achtung!") ohne konkrete Folge/Vermeidung.
- **Sprachversion fehlt** in einem Mitgliedstaat.
- **Digitale Anleitung** ohne Auffindbarkeit nach 10 Jahren – Hersteller-Pflichtverletzung.

## Querverweise

- `ce-zeichen-fehlgebrauch-und-abmahnung`
- `betreiber-mitverschulden-und-fehlbedienung`
- `barrierefreiheit-und-inklusion-robotik`

## Quellen Stand 06/2026

- VO (EU) 2023/1230 (MaschinenVO), Art. 10, 11, Anhang III Nr. 1.7.
- RL 2006/42/EG (bis 19.01.2027).
- VO (EU) 2023/988 (GPSR).
- VO (EU) 2024/1689 (KI-VO), Art. 13, 18, 26, 50.
- VO (EU) 2024/2853 (neue ProdHaftRL).
- ProdHaftG; § 823 BGB.
- ISO 3864; ISO 7010; ANSI Z535.
- Live-Verifikation auf eur-lex.europa.eu, baua.de, bsi.bund.de; lizenzierte Datenbanken (beck-online, juris) nur bei vorhandenem Zugang.
