# 1. Integrationsprüfung Krankenhaus-IT und KI

Stand: 6. Oktober 2026. Geprüft wurde das neue Plugin mit seiner Klinikakte und den dazugehörigen Routingänderungen. Kein vollständiger Neulauf sämtlicher vorhandener Plugins und Testakten.

## 1.1. Plugin und Prompts

Elf Skills; Claude-CLI 2.1.168 und zentrale Plugin-ZIP-/Hauptskillvalidierung bestanden. Drei eigenständige Prompts mit bytegleichen MD-/TXT-Fassungen. Der Mini-Prompt umfasst 7.405 UTF-8-Bytes, der Hauptproblem-Prompt 7.466. Die auf das neue Plugin begrenzten Fachrouting- und Schnellstartprüfungen sowie die Qualitätsprofil-, redaktionellen und Workflowprüfungen sind bestanden. Das Qualitätsprofil enthält acht Aufgaben mit 32 Kriterien; dies ist keine Behauptung bestandener Modellläufe.

## 1.2. Testakte und Dateien

40 Originaldateien: 17 DOCX, 14 EML, fünf PDF und vier XLSX. Die zentrale Dokumentqualitätsprüfung erfasst 36 förmliche Dokumente und 40 Exportdateien; bestanden. Beide Mailanlagen stimmen bytegenau mit ihren separaten PDF-Originalen überein. Die sieben Tabellenblätter wurden nativ mit dem gebündelten LibreOffice gerechnet; sieben Basisprüfungen und elf Eingabemutationen sind bestanden. Ein fehlender Messwert wird nicht als null interpretiert; die Tabellen erteilen keine rechtliche Freigabe.

Die beiden zentralen Einzelarchiv-Validatoren prüfen das Original-ZIP und das Einzel-PDF-ZIP auf Einträge, Integrität, Hinweisdatei und PDF-Vorgaben. Alle 40 Originale sind bytegleich enthalten. Das Gesamt-PDF hat 76 Seiten. Sämtliche Originaldarstellungen und die zusätzlichen Trenn-/Mailseiten wurden visuell geprüft; Einzelheiten und Hashwerte stehen in den gesonderten Prüfberichten. Der abschließende Komponentenbuild erhält den visuell geprüften Gesamt-PDF-Hash unverändert.

## 1.3. Downloads und Regression

Vier neue Routingtests sowie die 31 vorhandenen Fixture-, Staging-, Veröffentlichungs- und Workflowtests wurden erfolgreich ausgeführt. Ein zusätzlicher vollständiger Agentenlauf der bisherigen Suite ergab 32 bestandene Tests und einen durch den Sparse-Checkout verursachten Vollbestandsfehler (erwartet mindestens 380 Akten, lokal eine materialisiert). Die nicht materialisierten Bestandsdateien wurden nicht als geprüft ausgegeben. Ein read-only Vergleich der alten und neuen Routen bestätigt unveränderte Bestandslinks und genau drei neue Komponenten-Pins.

Die neue Veröffentlichung verwendet den festen Tag `krankenhaus-it-ki-v445.33.1` und wird nicht als Latest gesetzt. Die zwei Akten-ZIPs und das Plugin-ZIP sind ausdrücklich dorthin geroutet; die Alt-Sammelpakete bleiben unverändert und enthalten diese Ergänzung noch nicht. Kataloge, Skill- und Testaktenlisten benennen diese Abweichung. Globale Generatoren wurden auf dem Sparse-Checkout nicht ausgeführt.

## 1.4. Fachliche Grenzen

Die Rechtsquellenprüfung ist in `rechtsquellen-pruefung.md` dokumentiert. Die aktuelle amtliche ThürKHG-Gesamtkonsolidierung war technisch nicht vollständig zugänglich; diese Verifizierungslücke bleibt in Referenzen und Prompts ausdrücklich offen. Vorhandene amtliche Änderungsvorschriften und ergänzende Konsolidierung wurden abgeglichen. Die Testakte enthält keine echten Patientendaten und keine fingierten Behörden-, Ethik- oder Produktfreigaben.
