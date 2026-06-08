---
name: barrierefreiheit-und-inklusion-robotik
description: "Prüft Barrierefreiheit, Inklusion und diskriminierungsarme Bedienung bei Robotikprodukten und Nutzerinterfaces."
---

# Barrierefreiheit und Inklusion bei Robotern

## Fachkern: Barrierefreiheit und Inklusion bei Robotern
- **Normen-/Quellenanker:** EU-Maschinenverordnung, Produkthaftungsrecht, ProdSG/GPSR, AI Act, MDR/MPDG bei Medizinrobotik, DSGVO, Cybersecurity/NIS2 und Arbeitsschutz.
- **Entscheidende Weiche:** Prüfe Rolle Hersteller/Integrator/Betreiber, bestimmungsgemäße Verwendung, CE-Konformität, Sicherheitsfunktion, Lern-/Updateverhalten, Schadenpfad und Rückrufpflicht.

## Worum geht es konkret

Service-, Pflege-, Liefer- und Empfangsroboter interagieren mit Menschen unterschiedlicher Fähigkeiten. Das BFSG (Barrierefreiheitsstärkungsgesetz, Umsetzung der EU-RL 2019/882) verlangt seit 28.06.2025 von Herstellern und Dienstleistern bestimmter Produkte und Dienstleistungen Barrierefreiheit. Ergänzt durch das AGG bei Diskriminierung in der Bedienung und durch Art. 5 KI-VO (verbotene Praktiken bei Ausnutzung von Verletzlichkeiten). Dieser Skill prüft Robotikprodukte und ihre Nutzerinterfaces (UI/UX, Sprache, Höhe, Sensorik) auf Barrierefreiheit und Diskriminierungsarmut.

## Wann dieses Modul hilft / Kaltstart-Fragen

1. **Rolle:** Hersteller eines Roboters mit Endkundenkontakt, Dienstleister mit Robotereinsatz im Publikumsverkehr, Behindertenverband, Antidiskriminierungsstelle.
2. **Produkt:** Pflege-, Service-, Empfangs-, Lieferroboter, Selbstbedienungsterminals mit Robotik-Bestandteilen, Bankautomaten mit Sprachausgabe.
3. **Zielgruppe:** Endverbraucher, Patienten, Mitarbeiter, Schüler, ältere Personen, Menschen mit Sinnes- oder kognitiven Einschränkungen.
4. **Anlass:** Markteinführung, Aufsichtsanfrage Marktüberwachungsbehörde (BMAS), Beschwerde, AGG-Mahnschreiben.
5. **Unterlagen:** Bedienkonzept, UI-Mockups, Sprachausgabe-Skripte, Sensorhöhen, Nutzerstudien.

## Rechtlicher Rahmen

- **BFSG** § 1, § 3: erfasst u. a. Selbstbedienungsterminals, Hardware-Systeme für Verbraucher mit interaktiver Funktion; Pflicht: Wahrnehmbarkeit, Bedienbarkeit, Verständlichkeit, Robustheit (BFSGV); Geltung seit 28.06.2025.
- **EU-RL 2019/882** (European Accessibility Act), national umgesetzt durch BFSG.
- **BFSGV** Anhang 1 detaillierte Anforderungen.
- **EN 301 549** harmonisierte Norm IKT-Barrierefreiheit (zuletzt überarbeitet 2024).
- **AGG** §§ 1, 2 Abs. 1 Nr. 8, 19, 20: Massengeschäfte, Diskriminierung in der Bedienung.
- **KI-VO** Art. 5 Abs. 1 lit. b: Verbot der Ausnutzung der Verletzlichkeit aufgrund Alters, Behinderung, sozialer/wirtschaftlicher Lage.
- **MaschinenVO** VO (EU) 2023/1230 Anhang III Nr. 1.1.6 Ergonomie.
- **UN-BRK** Art. 9 (Zugänglichkeit).

## Schritt für Schritt

1. **Anwendungsbereich BFSG prüfen.** Verbraucherrobotik oder gewerblich? Übergangsregelungen für Bestandsprodukte beachten.
2. **Wahrnehmbarkeit.** Mehrkanalige Ausgabe (visuell + akustisch + ggf. taktil); Kontraste mindestens WCAG AA; Schriftgrößen skalierbar; Sprachausgabe in Standardsprache.
3. **Bedienbarkeit.** Bedienelemente in Reichweite (Rollstuhl: 80-110 cm Greifhöhe); Tasten taktil unterscheidbar; keine reinen Touch-Interfaces ohne Sprach-Alternative.
4. **Verständlichkeit.** Leichte Sprache; Symbole genormt (DIN 32976, ISO 7001); Vorlesefunktion.
5. **Robustheit.** Kompatibilität mit Hilfsmitteln (Hörgeräte, Screenreader bei vorhandenen Bildschirmen).
6. **KI-VO Art. 5 Check.** Erkennt das System Schutzbedürftigkeit und beeinflusst es das Verhalten? Sprachdialoge auf manipulative Muster prüfen.
7. **Diskriminierungs-Audit.** Spracherkennung über Dialekte, Hautfarben-Erkennung in Kameras (Bias-Test), Personenerkennung im Rollstuhl.
8. **Nutzerstudien** mit Betroffenenverbänden; Iteration.
9. **Konformitätserklärung BFSG**; Marktüberwachung über die zuständigen Landesbehörden.

## Trade-off-Matrix

| Anforderung | Strenge Auslegung | Pragmatik | Empfehlung |
|---|---|---|---|
| Sprachausgabe + Display | beides immer | nur wenn Hauptkanal | beides bei Verbraucherrobotern Standard |
| Höhenverstellbare Bedienoberfläche | mechanisch | nur Software-Anpassung | mindestens Software-Skalierung; mechanisch wenn machbar |
| Leichte Sprache | überall | nur Pflichtinformationen | Pflichtinformationen + häufige Dialoge in leichter Sprache |
| Bias-Tests | breit | nur Hauptmerkmale | Test gegen Trainings-/Test-Disjunktion mit demografisch ausgewogenem Set |

## Praxistipps

- **Co-Design** mit Behindertenverbänden früh, nicht erst zum Test.
- **Falsch-Positiv-Bias** der Personenerkennung dokumentieren – sonst KI-VO/AGG-Risiko.
- **Sturzgefahr** durch Roboter im Bewegungsraum berücksichtigen (Sehbehinderung).
- **Sprachbefehle** als gleichwertige Alternative zur Touch-Bedienung.
- **Hörgerätekompatibel**: Induktionsschleife oder Bluetooth-LE-Audio.

## Mustertexte

**Auszug Konformitätserklärung BFSG:**

> Der Hersteller [Firma] erklärt, dass das Produkt [Modell, Seriennummer] die Anforderungen des BFSG und der BFSGV erfüllt. Angewandte Normen: EN 301 549:2024, DIN EN 17161. Die technische Dokumentation wird gemäß § 23 BFSG zehn Jahre vorgehalten.

**UI-Designprinzip (Auszug Spezifikation):**

> Alle sicherheitsrelevanten Bestätigungen erfolgen sowohl visuell (Kontrast 7:1) als auch akustisch (Sprachausgabe, Lautstärke vom Nutzer einstellbar). Sprachdialoge werden in deutscher Standard- und leichter Sprache angeboten. Reaktionszeit-Erwartungen werden nicht durch zeitliche Drucksetzung (Countdown) erzwungen – Nutzer mit motorischen Einschränkungen erhalten mindestens das Dreifache der Standardzeit.

## Typische Fehler

- **Reine Touch-UI** ohne haptische/sprachliche Alternative.
- **KI-Spracherkennung** nur auf Standardsprache trainiert.
- **Höhenfixierung** der Bedienoberfläche zu hoch für Rollstuhlfahrer.
- **Personenerkennung** bricht bei Rollstuhl- oder Rollator-Nutzern.
- **AGG-Risiko**: Roboter ignoriert Personen aufgrund von Größe oder Hautfarbe (Bias).

## Querverweise

- `datensatzqualitaet-und-bias-hri`
- `betriebsanleitung-sprache-und-warnhinweise`
- `biometrie-emotion-und-personenerkennung`

## Quellen Stand 06/2026

- BFSG; BFSGV.
- RL (EU) 2019/882.
- EN 301 549:2024; DIN EN 17161.
- VO (EU) 2024/1689 (KI-VO), Art. 5.
- AGG §§ 1, 19, 20.
- UN-BRK Art. 9.
- Live-Verifikation auf bmas.de, eur-lex.europa.eu, antidiskriminierungsstelle.de; lizenzierte Datenbanken (beck-online, juris) nur bei vorhandenem Zugang.
