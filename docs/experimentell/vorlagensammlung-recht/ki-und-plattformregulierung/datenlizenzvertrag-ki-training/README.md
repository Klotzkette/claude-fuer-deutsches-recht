# Datenlizenzvertrag für KI-Training und Modellvalidierung

## Vorspruch und Nutzungsgrenze

Diese Vorlage ist unverbindlich, ein experimenteller Text und keine Rechtsberatung. Sie ist ein Struktur- und Formulierungsvorschlag, kein Gutachten und kein ungeprüft verwendbares Mandatsprodukt. Nutzung nur auf eigene Gewähr und eigene Gefahr; vor jedem Einsatz sind Sachverhalt, Rechtslage, Form, Fristen, Zuständigkeit, Vertretungsmacht, Datenschutz, Vollziehbarkeit und wirtschaftliche Folgen fachkundig zu prüfen, anzupassen und freizugeben.

Mandatsbezogene und personenbezogene Inhalte sind nach § 43a Abs. 2 BRAO, § 203 StGB und DSGVO zu schützen. Bei Verarbeitung in Drittsystemen sind Anonymisierung, Rechtsgrundlage, Auftragsverarbeitung und Löschkonzept zu prüfen.

Lizenz: Apache-2.0 OR MIT.

## Anwendungsbereich

Diese Vorlage passt zur Lizenzierung kuratierter Datenbestände für Training, Fine-Tuning, Evaluation, Retrieval-Augmented Generation, synthetische Datengenerierung oder Modellvalidierung. Sie ist kein bloßer Datensatzkauf; sie muss Datenherkunft, Rechtekette, Ausschluss personenbezogener Daten oder deren Rechtsgrundlage, Modellartefakte, Embeddings, Rückrufmechanik und Auditfähigkeit konkret steuern.

## Einschlägige Normen

- Verordnung (EU) 2024/1689 über künstliche Intelligenz mit gestaffelten Geltungsterminen für verbotene Praktiken, GPAI-Modelle, Hochrisiko-Systeme und Betreiberpflichten.
- Art. 5, Art. 6, Art. 9, Art. 22, Art. 25, Art. 32, Art. 35 DSGVO bei Trainingsdaten, Profiling, automatisierter Entscheidung und Datenschutz-Folgenabschätzung.
- §§ 2, 4, 6 GeschGehG für Trainingsdaten, Prompts, Modellartefakte und vertrauliche Auswertungen.
- §§ 305 ff., 307 BGB bei Richtlinien, Nutzungsbedingungen, Haftungs- und Freistellungsklauseln.
- UrhG und Datenbankrecht werden zusätzlich geprüft, wenn Trainings- oder Outputdaten geschützte Inhalte enthalten.

## Besondere Warnhinweise

Trainingsdaten können personenbezogene Daten, Geschäftsgeheimnisse, urheberrechtlich geschützte Inhalte oder Datenbankrechte enthalten. Rechtekette und Löschbarkeit müssen belegt sein.

## Download

- [⬇ Datenlizenzvertrag für KI Training und Modellvalidierung – Markdown (ZIP) herunterladen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/raw/main/docs/experimentell/vorlagensammlung-recht/ki-und-plattformregulierung/datenlizenzvertrag-ki-training/datenlizenzvertrag-ki-training.md.zip)
- [⬇ Datenlizenzvertrag für KI Training und Modellvalidierung – ODT herunterladen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/raw/main/docs/experimentell/vorlagensammlung-recht/ki-und-plattformregulierung/datenlizenzvertrag-ki-training/datenlizenzvertrag-ki-training.odt)

Vorschau im Repository: [`datenlizenzvertrag-ki-training.odt`](datenlizenzvertrag-ki-training.odt) · [`datenlizenzvertrag-ki-training.md`](datenlizenzvertrag-ki-training.md)

## Hinweise zur Verwendung

Die Datenlizenz muss zwischen Trainingsdaten, Evaluationsdaten, synthetischen Ableitungen, Embeddings, Tokenizer-Artefakten und bloßen statistischen Auswertungen unterscheiden. Rechtekette, Ausschlusslisten, Löschbarkeit, Nachtrainingsrisiko und Rückruf werden so dokumentiert, dass ein späteres Modell- oder Datensatzproblem nicht in allgemeiner Unklarheit verschwindet.

Fristen- und Nachweisarchitektur: Datenlieferung, Quarantäneprüfung, Freigabe, Trainingslauf, Evaluationsbericht, Löschfrist, Sperrlisten-Update, Rückrufauslösung und Audit werden mit Verantwortlichem und Review-Termin dokumentiert. Art. 22 DSGVO, Art. 28 DSGVO und Geschäftsgeheimnisschutz werden nicht durch eine Datenlizenz ersetzt.

Abgrenzung: Für KI-Training mit Datenlizenz `ki-und-plattformregulierung/datenlizenzvertrag-ki-training/`; für Kanzlei- oder Unternehmensnutzung `informationstechnologierecht/ki-nutzungsrichtlinie-kanzlei-unternehmen/` oder `ki-und-plattformregulierung/ki-nutzungsrichtlinie-mitarbeitende-unternehmen/`.

## Taktische Hinweise

### Vorgehensreihenfolge

Datensätze, Herkunft, Rechtekette, Personenbezug, Zweck, Qualitätsmerkmale und Ausschlusslisten werden vor Übergabe in einem Datenmanifest eingefroren. Danach sind Lizenzumfang für Training, Validierung und synthetische Ableitungen, Quarantäneprüfung, Datenschutzrolle, Modellartefakte, Audit, Sperrlisten-Update, Rückruf und Löschung mit konkreten Trainingsläufen und Modellversionen zu verknüpfen.

### Typische Einwände und Antwortlinien

- Dem Einwand fehlender Trainingsrechte ist mit einer quellenspezifischen Rechtekette und ausdrücklich erfassten Vervielfältigungs-, Bearbeitungs- und Modellnutzungen zu begegnen.
- Bei Datenschutzbedenken sind Rechtsgrundlage, Zweckkompatibilität, Datenminimierung und Betroffenenrisiken unabhängig von der urheberrechtlichen Lizenz zu prüfen.

### Häufige Fehler

- Der Vertrag lizenziert „Daten“, ohne Datensatzversion, ausgeschlossene Quellen und zulässige Modellartefakte zu bestimmen.
- Löschung wird versprochen, ohne zwischen Rohdaten, Checkpoints, Embeddings, Protokollen und bereits ausgelieferten Modellen zu unterscheiden.

## Verwandte Vorlagen

- [KI-Systeminventar für Due Diligence nach KI-Verordnung](../ki-systeminventar-due-diligence-ai-act/) — für die Zuordnung der Daten zu konkreten Modellen und Systemen.
- [Risikomanagementsystem-Dokumentation (KI-VO Art. 9)](../ki-vo-risikomanagementsystem-dokumentation/) — für Risiken aus Datenqualität und Modellverhalten.
- [KI-Nutzungsrichtlinie für Mitarbeitende](../ki-nutzungsrichtlinie-mitarbeitende-unternehmen/) — für interne Eingabe- und Freigaberegeln.
