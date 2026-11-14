---
name: vertiefung-orientierung
description: 'Vertiefte Auftraggeberprüfung für unklare oder streitige Vergaben: subsumiert Auftraggeberstatus, Auftragsart, Wert, Übergangsrecht, Verfahrenswahl, Leistungsbeschreibung, Eignung, Bestangebot, Rechtsschutz und Vertragsänderung. Liefert Entscheidungsbaum, Belegmatrix, Gegenargumente und Freigabevermerk.'
---

# Vergabestelle: vertiefte Regime- und Freigabeprüfung

<!-- BEGIN output-format-block (autogen) -->

## Output-Format (verbindlich)

Schriftart Times New Roman, Schriftgrad 11 pt. Dezimalgliederung 1, 1.1, 1.1.1, 2, 2.1 fortlaufend ohne Lücken, maximal vier Ebenen. Aufzählungen mit Spiegelstrich oder Bullet. Hervorhebung nur durch Kursivsetzung bei Gesetzes- und Aktenzeichenfundstellen, kein Fettdruck, keine Unterstreichung. Vollständige Regeln in [`references/OUTPUT-FORMAT.md`](../../references/OUTPUT-FORMAT.md). Bei abweichenden Vorgaben der Stelle (Portal, Gericht, Kammer) gilt die Stelle.

<!-- END output-format-block (autogen) -->

## Einsatzgrenze

Nutze diesen Skill, wenn Auftraggeberstatus, Regime, Ausnahme, Rechtsstand oder Rechtsfolge nicht mit einer einfachen Triage feststehen. Die Prüfung endet nicht bei einer Normenliste, sondern mit einer verteidigungsfähigen Behördenentscheidung. Tatsachen, Rechtsannahmen und Wertungen strikt trennen.

## 1. Fallkarte und Aktenfreeze

1. Rolle und gewünschte Entscheidung festlegen.
2. Vergabe-ID, Lose, Portal, Aktenversion und Bearbeitungsstichtag sichern.
3. Bekanntmachung, Unterlagen, Änderungen, Bieterkommunikation, Angebote, Aufklärungen, Wertung und Zustellbelege inventarisieren.
4. Für jedes Dokument Original, Version, Urheber, Zeitstempel, Hash soweit verfügbar und Beweisthema erfassen.
5. Unvollständige Akte sperren, wenn die fehlende Unterlage Regime, Frist, Wertung oder Zuschlag beeinflusst.

## 2. Regime als Tatbestandsprüfung

| Tatbestand | Leitfrage | Beleg | Rechtsfolge |
|---|---|---|---|
| §§ 98 bis 101 GWB | Wer beschafft in welcher Funktion? | Satzung, Beteiligung, Finanzierung, Tätigkeit | klassischer, Sektoren- oder anderer Auftraggeber |
| §§ 103 bis 105 GWB | Welche Leistung oder Konzession wird vergeben? | Leistungsbild, Risikoverteilung, Vergütungsmodell | VgV, VOB/A, SektVO, KonzVgV oder VSVgV |
| § 3 VgV | Welcher Gesamtwert war ex ante zu erwarten? | Mengen, Optionen, Laufzeit, Lose, Marktpreise | Schwellen- und Losregime |
| § 106 GWB | Welche Schwelle galt am Stichtag? | aktuelle EU-Verordnung und amtliche Normfassung | Ober- oder Unterschwelle |
| § 187 Abs. 2 GWB | Wann begann das Verfahren? | interner Start reicht nicht stets; maßgeblichen Außenakt belegen | alte oder seit 1. Juli 2026 geltende Fassung |

Bei Unterschwellenfällen Haushaltsrecht, Einführungserlass und Landeswertgrenze mit Abrufdatum belegen. Keine bundesweite Einheitsgrenze unterstellen.

## 3. Verfahrenswahl und Ausnahme

1. Regelwahl nach § 119 GWB und Spezialregime bestimmen.
2. Für Verhandlungsverfahren ohne Teilnahmewettbewerb jeden Tatbestand des § 14 Abs. 4 VgV mit Zeitpunkt, Ursache, Alternativen und Kausalität belegen.
3. Technische Alleinstellung nicht aus Herstellerangaben übernehmen; Funktionsbedarf, Marktbreite, Migration und zumutbare Alternativen dokumentieren.
4. Dringlichkeit auf Unvorhersehbarkeit, Unzurechenbarkeit, Unvereinbarkeit mit Fristen und erforderlichen Umfang begrenzen.
5. Losbildung nach der anwendbaren Fassung von § 97 Abs. 4 oder § 97a GWB mit Markt-, Schnittstellen- und Steuerungsdaten entscheiden.

Output: Tatbestandsmatrix mit stärkstem Gegenargument und gesonderter Freigabe.

## 4. Leistungsbeschreibung und Wettbewerb

- Aktuelle Fassung des § 121 GWB und § 31 VgV beziehungsweise § 7 oder § 7 EU VOB/A nicht vermischen.
- Funktions- und Leistungsanforderungen mit messbaren Abnahmebedingungen verbinden.
- Typ-, Marken-, System- oder Dateiformatbezug nur mit konkreter Notwendigkeit und erforderlicher Gleichwertigkeitsöffnung.
- Bestandsdaten aus Fachsystemen quellengetrennt übernehmen; Transformation, Einheit und Verlustfreiheit in einem Roundtrip-Test belegen.
- Eine Berichtigung muss in Unterlagen, Bekanntmachung, Plattformstand und Fristberechnung konsistent sein.

Rechtsprechungsanker: OLG Düsseldorf, Beschluss vom 10.07.2024, Verg 2/24, trägt eine konkret dokumentierte Bestandskompatibilität, keinen pauschalen Lock-in.

## 5. Eignung, Ausschluss und Angebotsprüfung

1. Eignung nach § 122 GWB und §§ 42 bis 48 VgV auf Auftragsbezug, Bekanntmachung und Verhältnismäßigkeit prüfen.
2. §§ 123 und 124 GWB tatbestandsbezogen prüfen; Ermessens- und Verhältnismäßigkeitsschritt bei § 124 offenlegen.
3. Selbstreinigung nach § 125 GWB anhand Schadensausgleich, Sachverhaltsaufklärung und konkreten Präventionsmaßnahmen bewerten; Höchstzeiträume des § 126 GWB kontrollieren.
4. Nachforderung nach § 56 VgV, Ausschluss nach § 57 VgV und Preisaufklärung nach § 60 VgV als getrennte Entscheidungen dokumentieren.
5. Wettbewerbsregisterabfrage nach § 6 WRegG behördenseitig durchführen; keinen Selbstauszug des Unternehmens als Ersatz verlangen.

BGH, Beschluss vom 31.01.2017, X ZB 10/16, nur für den konkreten Niedrigpreis- und Geheimnisschutzkontext verwenden.

## 6. Bestangebot statt Billigstautomatismus

Baue die Entscheidungsbrücke:

`Bedarf -> Kriterium -> Auftragsbezug -> Nachweis -> Gewichtung -> Methode -> Angebotsfundstelle -> Einzelwertung -> Begründung`

§ 127 GWB und § 58 VgV erlauben Qualität, Organisation, Personal, Ausführungszeit, Service, Lebenszykluskosten, Nachhaltigkeit oder Resilienz, wenn die gesetzlichen Anforderungen erfüllt sind. Eine hohe Qualitätsgewichtung ist zu begründen; ein Preis-only-Modell ebenso. EuGH, Urteil vom 18.10.2001, C-19/00, *SIAC Construction*, als Transparenz- und Objektivitätsanker verwenden, nicht als Ersatz für die konkrete Matrix.

## 7. Rechtsschutz- und Fristzweig

1. § 134 GWB: Inhalt, Adressaten, Versandweg und frühesten Zuschlag prüfen.
2. Jede Rüge nach Verstoß, Kenntnis, Erkennbarkeit, Zugang und § 160 Abs. 3 GWB getrennt behandeln.
3. Im VK-Verfahren Antragsbefugnis, Präklusion, Aktenvorlage, Geheimnisschutz, Beiladung und § 169 GWB prüfen.
4. Vor §§ 172 und 173 GWB stets § 187 Abs. 2 GWB anwenden. Neu- und Altverfahren haben unterschiedliche Zuschlags- und Beschwerdefolgen.
5. Für das OLG Zustellung, Zwei-Wochen-Frist des § 171 GWB, Anträge, gleichzeitige Begründung und gegebenenfalls § 176 GWB kontrollieren.

## 8. Vertrag und Änderung

Prüfe § 132 Abs. 1 bis 3 GWB mit ursprünglichem Vertrag, Nachträgen, kumuliertem Wert und geänderter Risikoverteilung. Bei Auftragnehmerwechsel § 132 Abs. 2 Satz 1 Nr. 4 Buchstabe b GWB vollständig subsumieren. EuGH, Urteil vom 04.06.2026, C-820/24, *Strominator Elektro*, sperrt die Änderungslogik, wenn Leistung vollständig erbracht, endgültig abgenommen und schlussgerechnet ist; eine offene Zahlung genügt nicht.

## 9. Quellen- und Gegenproben

- Gesetze und Verordnungen aus amtlicher aktueller Einzelnorm; Übergang und Inkrafttreten festhalten.
- Rechtsprechung mit Gericht, Entscheidungsart, Datum, Aktenzeichen, ECLI soweit vorhanden und tragender Aussage.
- Schlussanträge als Schlussanträge kennzeichnen; C-268/25 nicht als EuGH-Urteil ausgeben.
- Vergabekammerentscheidungen als Praxisanker, nicht als bundesweit bindende Rechtssätze behandeln.
- Gegenprobe aus Sicht eines fachkundigen Bieters: Transparenz, Gleichbehandlung, Auftragsbezug, Verhältnismäßigkeit, Dokumentation und Kausalität.

## 10. Pflichtoutput

1. Entscheidungsvorschlag und Stop-/Freigabeampel.
2. Tatbestandsmatrix `Tatsache -> Norm -> Subsumtion -> Beleg -> Gegenargument -> Rechtsfolge`.
3. Fristen- und Zuständigkeitsplan.
4. Dokumenten- und Quellenlücken mit Beschaffungsweg.
5. Vollständig formulierter Vermerk oder Schriftsatzkern.
6. Red-Team-Risiken und konkrete Heilungsmaßnahme.
7. Vier-Augen-Freigabe und nächster Portal-, DMS- oder Versandvorgang.
