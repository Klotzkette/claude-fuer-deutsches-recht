# Präzise Arbeitswege, Skill-Namen und Rechtsquellen

## 1. Gegenstand und Ergebnis

Prüftag: **16. November 2026**. Ausgangspunkt ist Commit `76b7d5c31f0fa286b94175696b4594d29a8ce931`. Die Überarbeitung verbindet eine bestandsweite Verbesserung der Quellenmethodik mit gezielten, am Original geprüften Fachkorrekturen. Sie ist **keine erneute juristische Vollprüfung aller Aussagen der 311 Plugins und 3.153 aktiven Skills**. Ein aktueller Abruf, ein bestandener Strukturtest und eine erfolgreiche Installation belegen jeweils unterschiedliche Dinge.

322 eigenständige Werkstatt-Markdowns, drei fachgebietseigene Gesamtprompts und ihre vorhandenen Textfassungen verlangen jetzt ausdrücklich die für den Fall geltende Normfassung, getrennte Zeitpunkte für Verkündung, Inkrafttreten und Anwendbarkeit sowie eine belastbare Verbindung zwischen Rechtssatz, Quelle, Tatsachen und Gegenargument. Die 249 bereits vorhandenen zentralen Gesamtprompts wurden abgeglichen. Die fachlichen Quellen, Beweisfragen, Varianten und Grenzen bleiben erhalten; erzeugte Gesamtprompts folgen der vorhandenen Modulauswahl des Generators. Interaktive Fallansichten und Dokumentansichten werden weiterhin nur bei vorhandener technischer Fähigkeit und fachlichem Nutzen eingesetzt; die Auswahl wird in das eigentliche Arbeitsprodukt übernommen.

Bei allen aktiven Skills wurden Titel und Aktivierungsbeschreibungen erfasst. 24 Einstiegsskills in zwölf Plugins erhielten konkrete Namen und individuelle Arbeitswege; der Datenschutz-Hauptweg wurde zusätzlich fachlich präzisiert. Die stabilen technischen Kennungen bleiben bestehen. Der [Namensbericht](skillnamen.md) bezeichnet Auswahl, Bestandszahlen, neue Titel und an den berührten Stellen korrigierte Rechtsaussagen. Die übrigen generischen Namen sind damit nicht als vollständig überarbeitet ausgewiesen.

## 2. Fachlich geprüfte Schwerpunkte

| Bereich | Konkrete Verbesserung | Quellen- und Prüfvermerk |
| --- | --- | --- |
| E-Rechnung | Technische Geschäftsregelfehler und steuerliche Pflichtangaben, Bauleistungsbeschreibung mit Anlagen, Übergangsregeln und Zahlungsanforderung für fremde Leistungen getrennt prüfen. | [BMF vom 15.10.2026, BFH XI R 4/22, § 27 Abs. 38 UStG](steuer-bav.md) |
| KI und Datenschutz | Personenbezug bei Verantwortlichem, Werkzeug und Empfänger getrennt; tatsächliche Wirkung eines Scores statt pauschaler Vertragsklauseln prüfen; nachträgliche Schwärzung heilt keinen unzulässigen Upload. | [EuGH C-413/23 P und BGH I ZR 227/25](ki-recht.md) |
| Produkt-Compliance | Herstellerrolle, aktive Ausnutzung und schwerwiegenden Sicherheitsvorfall unterscheiden; bereits geltende CRA-Meldungen mit eigener Kenntnis- und Fristenkette bearbeiten. | [CRA und Gesetzgebungsverfahren](ki-recht.md) |
| Elektronischer Rechtsverkehr | In 58 kurzen Fachprüfketten PDF-Format, Lesbarkeit, Verfahrensordnung, Signatur und Übermittlungsweg trennen. | [ERVV und ERVB 2025](erv-pruefschritte.md) |
| Commercial Courts | Ausführlicher Arbeitsweg von Sprachgrundlage über Einreichungspaket und Signatur bis Eingangsbestätigung; technische Störung und ungeeignetes Dokument getrennt behandeln. | [§§ 184a/184b GVG, BGH XII ZB 158/26 und XII ZB 311/21](erv-commercial.md) |
| Form, Verfahren, Gesellschaft und Krise | Unter anderem eigenhändiges Testament, Beglaubigung, Heilung, Revisionsgründe, Kapitalaufbringung, D&O-Selbstbehalt und Prognosezeiträume an den tatsächlich bearbeiteten Stellen berichtigt. | [Einzelne Normtexte und Umfang](skillnamen.md) |
| bAV | Vorhandene Trennung der Regelungen ab 2026 und 2027 anhand des Bundesgesetzblatts bestätigt; aus einem Sitzungsergebnis ohne Entscheidungsgründe keinen neuen Rechtssatz abgeleitet. | [Nachprüfung ohne materielle Änderung](steuer-bav.md) |

Die Berichte nennen tatsächlich gelesene Stellen, Übertragungsgrenzen und Abrufbeschränkungen. Insbesondere sind eine Verwaltungsauffassung kein Gesetz und eine Zurückverweisung keine abschließende Sachentscheidung. Für die konkret benannten EUR-Lex-Passagen war teilweise nur der amtliche Suchindex lesbar; das wird nicht als Lektüre des vollständigen Rechtsakts ausgegeben. Bei mehreren deutschen Normen wurden amtliche HTML-Dateien unmittelbar gelesen, nachdem der Webabruf nicht funktioniert hatte.

## 3. Gegenprüfung und Erhaltungsnachweis

Die E-Rechnungs-, KI-/Compliance- und Commercial-Courts-Änderungen wurden zusätzlich gegengelesen; die jüngeren Rechtsprechungsstellen wurden anhand amtlicher Volltexte geprüft. Die Gegenprüfung führte bei § 3 ERVV zu einer weiteren Präzisierung: Der Datenträger wird der formgerechten Übermittlung beigefügt und ersetzt sie nicht. Die allgemeinen Normkorrekturen und die Übertragung in die erzeugten Fassungen wurden in der Integration kontrolliert. Quellenarbeit wird nicht durch neue Hashwerte ersetzt.

Der strenge Erhaltungsnachweis bleibt aktiv. Bereits im Ausgangsstand hatte der bAV-PR-Lauf `43867629915` sechs Fehler zu drei nachträglich um den Oberflächenblock ergänzten Fachdateien gemeldet. Die Synchronisierung schreibt jetzt **ausschließlich nachgewiesene Änderungen dieses Blocks** reversibel fort. Fachänderungen oder ein nicht rekonstruierbarer Originaltext werden abgewiesen. Zwei zusätzliche Regressionstests prüfen sowohl zulässige Fortschreibung als auch die Ablehnung unerlaubter Änderungen. Bewusste Fachkorrekturen dieses Durchgangs sind getrennt mit Prüfvermerk erfasst; ursprüngliche Hashes und die Möglichkeit zur bytegenauen Rekonstruktion bleiben erhalten.

Keine Testakte, kein Originalbeleg, kein Testaktenarchiv und kein bereits veröffentlichtes Release wurden geändert. Der Downloadbestand bleibt bei 631 zentralen und insgesamt 643 ausgewiesenen Testakten. Aktualisiert wurden Texte, abgeleitete Übersichten und nachvollziehbare Prüfbindungen.

## 4. Technische Nachweise

- Marketplace-Import, YAML-Frontmatter und Pluginstruktur: erfolgreich für 311 Plugins und 3.153 aktive Skills.
- Zentraler PDF-Bestand: 631 Akten erfolgreich geprüft. Downloadhinweise: 631 Akten, 5.679 Treffer, 395 weitere Downloadgruppen und 30 HTML-Seiten erfolgreich geprüft.
- Redaktionelle und Workflow-Prüfung, Root-Übersicht, Prompt-Profilzuordnung und Synchronisierung der Werkstattführung: erfolgreich. Kein verbleibender Unterschied der erzeugten Oberflächenblöcke.
- Strenger Erhaltungsnachweis einschließlich paketinterner Links: null Fehler. Die Prüfung rekonstruiert die ursprünglichen Fachtexte; sie ist kein Rechtsgutachten.
- Regressionstests: Werkstattführung 30, Workflow-Erhaltung 43, Qualitätslabor 81, Prompt-Einstiege 7, bekannte Rechtskorrekturen 7, aktuelle Fachhinweise 3, Skill-Integration 14 und Skill-Migration 16 erfolgreich. Gesamtprompt-Generator, Prompt-/Linkhygiene und Release-Routing ebenfalls erfolgreich.
- E-Rechnung: neun Tests erfolgreich, ein optionaler Java-/Mustang-/KoSIT-Integrationstest mangels konfigurierter Laufzeit übersprungen. Compliance: acht Tests ausgeführt, davon zwei vorgesehene optionale Prüfungen übersprungen. Keine neue externe Rechnungsvalidierung oder Gerichtsübermittlung behauptet.
- **Codex-Ladeprüfung:** 311 Plugins und 3.153 Skills über den tatsächlich gestarteten App-Server geladen. Vorhandene Hinweise zu zu langen optionalen Startvorschlägen bleiben Warnungen; kein Ladefehler. Dies ist kein Nachweis erfolgreicher juristischer Modellantworten.
- **Claude:** sechs Plugins in einer getrennten lokalen Konfiguration tatsächlich installiert: E-Rechnung, Konzern-Compliance, Datenschutzrecht, Schrift-/Textform, Fortbestehensprognose und Vertragsrecht. Sämtliche Skill- und Referenzdateien der Installationen mit dem Arbeitsstand bytegleich abgeglichen. Die Konfiguration des Nutzers wurde hierfür nicht verändert.
- **Paketierung:** 16 betroffene Plugins mit den vorhandenen Paketfunktionen in einen leeren temporären Ordner gebaut; sämtliche ZIP-Mitglieder und Bytes, Manifeste, Skill-Grenzen und Erreichbarkeit der Fachinhalte geprüft. Das ist ein Pakettest, keine neue versionierte Veröffentlichung.

Die Synchronisierung der öffentlichen Werkstattdownloads erfolgt über den vorhandenen Pages-Workflow nach dem Merge. Der tatsächliche Veröffentlichungs- und Abrufstatus wird beim Abschluss des Pull Requests gesondert geprüft; ein lokaler Test ersetzt diese Kontrolle nicht.
