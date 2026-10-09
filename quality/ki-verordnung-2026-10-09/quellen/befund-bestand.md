# 1. Quellen- und Änderungsbefund zum vorhandenen KI-VO-Bestand

Prüfdatum: 9. Oktober 2026. Bearbeitete Komponenten: `ki-vo-ai-act-pruefer` und `ki-verordnung-transparenzpruefer`, jeweils 445.35.0. Der große Prüfer behält seine 123 Skills, der Transparenzprüfer seine acht Skills. Es wurden 78 beziehungsweise acht bestehende Skills geändert; Identitäten und vorhandene Testakten bleiben erhalten. Beide Komponenten haben nun Werkstatt-, Schnellstart- und eigenständigen Hauptproblem-Prompt, jeweils mit identischer TXT-Fassung.

## 1.1. Was tatsächlich geprüft wurde

Die Screenshots waren Anlass zur fachlichen Kontrolle, keine normative Autorität. Begriffe wie Risikomanagement, FRIA, Governance oder Zertifizierung wurden nicht pauschal entfernt, sondern auf ihren konkreten Normtatbestand und ihre Rolle zurückgeführt. Der Befund dokumentiert einen Quellen- und Textvergleich. Er behauptet weder eine technische Konformitätsprüfung noch eine erfolgreiche Benutzung in Claude oder ChatGPT.

Die konsolidierte amtliche KI-VO wurde als vollständige HTML-Antwort archiviert und daraus lesbarer Text erzeugt. Gelesen wurden die für die Änderungen maßgeblichen Bestimmungen: Artikel 2, 4, 4a, 5, 6, 9 bis 15, 17 bis 19, 22 bis 27, 40, 41, 43, 47 bis 56, 71 bis 73, 79, 81, 99 bis 101, 111 und 113 sowie Anhang I, IV und V. Artikel 3 wurde in den hier benötigten Definitionen, insbesondere Marktrollen, System-/Modellbegriffen und Vorfällen, gelesen. Die erneute Schlusskontrolle umfasste zusätzlich Artikel 2, 6 und 43 sowie Anhang IV bis VII. Damit wird keine vollständige Einzellektüre aller übrigen Artikel oder aller Bestandsdateien behauptet.

Die Änderungsverordnung 2026/1744 wurde im amtlichen Volltext abgerufen und in den einschlägigen Änderungsstellen gegengelesen. Die deutsche Berichtigung vom 29. September 2026 wurde vollständig gelesen: In Artikel 6 Absatz 1b heißt es „Ungeachtet“, nicht „Unbeschadet“. Die konsolidierte Informationsfassung ersetzt nicht die veröffentlichten Rechtsakte.

Die unverbindlichen GPAI-Leitlinien von 2025 wurden insbesondere in Randnummern 9, 57 und 60 bis 71 gelesen; die Transparenzleitlinien von 2026 insbesondere in Randnummern 5, 12 bis 17, 23 bis 27, 30 bis 40, 56 bis 78, 87 bis 92, 101 bis 117, 131 bis 138 und 142 bis 155. Daraus abgeleitete Auslegungen werden als Leitlinienposition, nicht als Verordnungswortlaut oder Gerichtsentscheidung behandelt.

## 1.2. Amtliche Quellen und Archive

Alle Originalantworten haben einen SHA-256-Nachweis in [quellen.json](quellen.json). Bei `.html.gz` bezieht sich der Hash auf die dekomprimierte Originalantwort, bei PDF auf die Originaldatei. Die Textableitung erleichtert das Nachlesen, ihr Hash ersetzt nicht den Originalnachweis.

| Quelle | Amtlicher Zugang | Gelesener Zweck |
| --- | --- | --- |
| Konsolidierte KI-VO, 27.07.2026 | [EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:02024R1689-20260727) | Rollen, Tatbestände, Pflichten, Geltungszeitpunkte und Anhänge |
| Verordnung (EU) 2026/1744 | [EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32026R1744) | Verabschiedetes Änderungsrecht statt bloßer Omnibus-Vorschlag |
| Deutsche Berichtigung, 29.09.2026 | [EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32026R1744R(01)) | Vorrang der Gefährdungsprüfung in Artikel 6 Absatz 1b |
| GPAI-Leitlinien 2025 | [Kommissionsarchiv](https://ai-act-service-desk.ec.europa.eu/sites/default/files/2025-07/guidelines_on_the_scope_of_the_obligations_for_generalpurpose_ai_models_established_by_regulation_1cx2atxgq79us4n3x8jfgyy1qlm_118340-3.pdf) | Modellrolle, Änderungen und indikative Drittelgröße |
| Transparenzleitlinien 2026 | [Kommissions-PDF](https://ec.europa.eu/newsroom/dae/redirection/document/131215) | Anbieter-Markierung, Betreiber-Offenlegung, Kontrolle, konkrete Ausgabe |

## 1.3. Materielle Korrekturen

| Bereich | Festgestelltes Problem | Berichtigung und Folgeprodukt |
| --- | --- | --- |
| System, Organisation, Grundrechte | Artikel 9, 17 und 27 als austauschbare allgemeine Governance behandelt | Systemrisikoakte, Anbieter-QMS und tatbestandlich begrenzte Betreiber-FRIA getrennt; tatsächliche Belege und jeweilige Adressaten benannt |
| Hochrisiko | Falsche oder verkürzte Rückausnahmebedingungen; bloße menschliche Freigabe als Entlastung | Artikel 6 Absatz 3 Buchstaben a bis d richtig zugeordnet; erhebliches Risiko, Entscheidungsbeeinflussung und Profiling eigenständig geprüft |
| Produkt-KI | Sicherheitsbauteil, Drittprüfung und Abschnitt A/B vermischt | Artikel 6 Absätze 1a bis 1c mit Ausfallfolgen; Artikel 2 Absatz 2 für Abschnitt B; Artikel 43 Absatz 3 für Abschnitt A getrennt |
| Negative Einstufung | Registrierung teilweise als entbehrlich behandelt | Bewertungsvermerk nach Artikel 6 Absatz 4 und Anbieter-/Systemregistrierung nach Artikel 49 Absatz 2 erhalten, Pflichtbeginn separat begründet |
| Zeit | Pauschale Alttermine beziehungsweise pauschale Verschiebung sämtlicher Pflichten | Artikel 111/113 pro Pflicht; Kapitel III Abschnitte 1 bis 3 außer Artikel 6 Absatz 5: Anhang III ab 02.12.2027, Anhang I ab 02.08.2028; Artikel 43/49 nicht ohne Begründung in diese Verschiebung einbezogen |
| Kompetenz | Unbedingte Kompetenzgarantie oder gesetzlicher Einheitskurs | Artikel 4 als Unterstützung der Kompetenzentwicklung; gesonderte Qualifikation der Aufsicht nach Artikel 26 Absatz 2 |
| Vorfälle | Universelle 72-Stunden-Frist oder zwei Tage bei jeglichem Lebensrisiko | Anbieterpfad Artikel 73 mit unmittelbarer Reaktion und Höchstfristen 15/2/10 Tage; Betreiberkette Artikel 26 Absatz 5 und GPAI-Meldung getrennt |
| Händler, Einführer, Vertreter | Falsche Absatzzuordnungen, Rollenwechsel und Vertreterkündigung | Artikel 23, 24, 25 und Vertreterpflichten getrennt; konkrete Dokumentenkontrolle, Sperre, Nachforderung und Informationsfolge |
| Technische Dokumentation | Falsche Gliederung von Anhang IV | Neun tatsächliche Bereiche; Nachmarktplan unter Nummer 9, Risikoakte unter Nummer 5, Änderungen unter Nummer 6 |
| Normen und Zertifikate | ISO-Zertifizierung oder Kodex automatisch mit Konformitätsvermutung gleichgesetzt | Gesetzliche Anforderung, Amtsblattfundstelle, erfasster Teil und tatsächlicher Anwendungsnachweis; Kodex und freiwillige Standards nur in ihrer jeweiligen Nachweisfunktion |
| FLOP und GPAI | 1/3-FLOP als Systemfreistellung; missverständliche 10e25-Angabe | Leitlinienheuristik zur geänderten Modellrolle; eigenständige Systempflichten; gesetzliche Vermutung nach Artikel 51 Absatz 2 bei mehr als 10 hoch 25 FLOP |
| Veröffentlichung | Anbieter-Markierung und Betreiber-Offenlegung vermischt | Artikel 50 Absatz 2 gegenüber Absatz 4; redaktionelle Kontrolle, Verantwortlichkeit, Kanal und Veröffentlichung getrennt |
| Bestand und neue Verbote | Bloße Inbetriebnahme mit Marktbereitstellung verwechselt; künftige Verbote vorgezogen | Artikel 111 Absatz 4 nur für vor 02.08.2026 in Verkehr gebrachte Systeme und nur Artikel 50 Absatz 2; Artikel 5 ba/bb/1a/1b erst ab 02.12.2026 |
| EU-Datenbank | NANDO als Systemregister; alle öffentlichen Betreiber allein Artikel 26 Absatz 8 | Artikel 49 Absätze 1 bis 5 getrennt; Artikel 26 Absatz 8 betrifft Unionsorgane; nationale öffentliche Betreiber nach Artikel 49 Absatz 3 |
| Konformitätserklärung | Fehlende Datenschutzangabe und falsche formale Aussagen | Anhang V Nummer 5, maschinenlesbare Form, physische oder elektronische Unterzeichnung und korrekter Verfahrensweg |

## 1.4. Aktivierung und Workflow

Die Kernworkflows führen von System, Zweck, Rolle und Stichtag über Tatbestandsprüfung und fehlende Tatsachen zu einem bezeichneten Produkt: Einordnungsvermerk, Risikoakte, Betriebsanleitung, FRIA, Nachforderung, Registervermerk, Konformitätsunterlagen oder Vorfallsentwurf. Gleiche Aktivierungsbeschreibungen von 15 historisch parallel vorhandenen Skillpaaren wurden fachbezogen differenziert, ohne Identitäten zu entfernen. Bestehende eng verwandte Skills bleiben erhalten; eine Zusammenlegung wäre eine eigene Strukturentscheidung.

Der Hauptproblem-Prompt des großen Prüfers bündelt die Gesamtprüfung. Der Hauptproblem-Prompt des Transparenzprüfers endet in einer konkreten, begrenzten Veröffentlichungsentscheidung. Die Prüfpunkte zu ISO, Modelländerung, tatsächlicher Aufsicht und Pflichtbeginn stehen in den betroffenen Arbeitsschritten, nicht nur in einem allgemeinen Warnanhang.

## 1.5. Aktive Vorlagen und bearbeitbare Fassungen

Elf Vorlagen wurden einschließlich README, ODT und Markdown-ZIP aktualisiert: KI-Anforderungsliste, Systeminventar, Artikel-5-Prüfung, Artikel-6-Einstufung, Konformitäts-/Register-Due-Diligence, EU-Konformitätserklärung, Anbieter-/Betreibercheckliste, Systemrisikomanagement, Unternehmens-KI-Richtlinie, Betriebsvereinbarung und Kanzlei-/Unternehmens-KI-Richtlinie.

Die Risikomatrix ist ausdrücklich eine interne Orientierung, keine gesetzliche RPZ-Schwelle. Ein ISO-42001- oder ISO-27001-Beispiel wird nicht mehr ohne Amtsblattnachweis als harmonisierte Norm angeboten. Schulungsintervalle sind als interne beziehungsweise vereinbarte Organisationsregeln erkennbar. Die bislang pauschale dreijährige Protokollaufbewahrung wird durch einen zweck- und rechtsbezogenen Einzelfallnachweis ersetzt.

Die bestehenden Generatoren `md-to-odt.py` und `build-md-zips.py` wurden nur auf diese elf Vorlagen angewandt. Die ODT-Struktur-/Layoutprüfungen des Generators und der bytegenaue Markdown-ZIP-Vergleich liefen durch. Das ist kein behaupteter visueller Seitenvergleich in LibreOffice.

## 1.6. Prüfungen und Grenzen

Der lokale Bestandscheck ergab keine Fehler bei 131 Skill-Frontmattern und Aktivierungsbeschreibungen, lokalen Markdownlinks, grundlegender Markdownstruktur, sechs MD/TXT-Paaren, Profilhashes, Komponentenfassungen und fünf Quellenarchivhashes. Die Schnellstart-Prompts haben 7.451 und 7.495 UTF-8-Bytes; die Hauptproblem-Prompts 4.838 und 4.969 Bytes. Die Werkstätten haben 32.472 und 24.486 Bytes. Beide Qualitätsprofile wurden mit `quality_lab.validate_profile` erfolgreich geprüft. Reproduzierbar ist der begrenzte Check mit `python3 quality/ki-verordnung-2026-10-09/quellen/pruefe-bestand.py`. Ergebnisse stehen in [pruefergebnis-bestand.json](pruefergebnis-bestand.json); pro geändertem Skill sind Umfang und SHA-256 in [bearbeitete-bestandsskills.json](bearbeitete-bestandsskills.json) dokumentiert.

Der vollständige Repository-Frontmattervalidator lief mit null Fehlern und null Warnungen. Der globale Aktivierungsaudit zeigte zunächst außerhalb dieser Komponenten eine Beschreibung über 360 Zeichen sowie zwei identische Beschreibungen im gewerblichen Rechtsschutz. Innerhalb der beiden hier bearbeiteten Komponenten bestehen nach der Korrektur keine identischen Beschreibungen mehr. Die Gesamtintegration und ihre weiteren Prüfungen werden im übergreifenden Bericht dokumentiert.

Keine vorhandene Testakte wurde in dieser Runde verändert. Kein Gerichtsanker wurde aus Modellwissen ergänzt. Vorhandene Gerichts- und nationale Rechtsquellen behalten ihren historischen Prüfstand; insbesondere C-634/21 ist dadurch nicht als am 9. Oktober erneut vollständig gelesen ausgegeben. ISO-Normen wurden nicht als vollständig eingesehene Standardtexte behauptet. Die Quellenprüfung liefert keine fertige rechtliche Freigabe für ein reales System. Aus der Abschichtung der Geltungsdaten wird weder ein allgemeines Moratorium noch eine pauschale sofortige Hochrisikopflicht für jedes System abgeleitet.
