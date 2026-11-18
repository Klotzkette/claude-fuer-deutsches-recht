# 1. Nachprüfung der Issues 546, 547, 548 und 550

Prüfdatum: 18. November 2026. Ausgangsstand: `e458e111f94ce0bcd9788e192beeb61a81d20812`. Die vollständigen Issue-Texte und Kommentarlisten wurden über den GitHub-Connector gelesen; alle vier hatten bei Abruf keine Kommentare. Die Hinweise sind Sachanregungen. Es wurden keine fremden Patches übernommen. Die Beurteilung bezieht sich auf die bezeichneten Fachmodule, nicht auf eine Vollfreigabe der vier Plugins.

## 1.1. Issue 546 – Data-Act-Verweis und Datenbankrecht

[Issue 546](https://github.com/Klotzkette/claude-fuer-deutsches-recht/issues/546). Ergebnis: Die konkret beanstandeten Fehler sind im Ausgangsstand bereits behoben. Die drei Fachinhalte `backup-export-und-vendor-lock`, `data-act-bei-backup-export` und `datenbankrecht-bei-saas-und-cloudmigration` wurden vollständig gelesen.

Cloud-Wechsel ist dort zutreffend Kapitel VI, insbesondere Artikeln 23, 25, 29 und 31, zugeordnet. Artikel 17 wird nicht als Wechselnorm verwendet. Das Entgeltverbot ab 12. Januar 2027, die vorherige Kostengrenze und die getrennte Prüfung laufender Entgelte stehen ausdrücklich im Text. Die Übergangsregel für Kapitel IV wird nicht auf Kapitel VI übertragen. Artikel 43, der Datenschutzvorrang aus Artikel 1 Absatz 5, die abgestuften Geschäftsgeheimnisregeln und der Unterschied zwischen Artikel 6 und Artikeln 8/13 sind berücksichtigt. Artikel 20 DSGVO wird als Recht natürlicher Personen mit eigenen Voraussetzungen beschrieben, nicht als allein verbraucherbezogenes oder allgemeines Unternehmensrecht.

Keine zusätzliche Änderung in `datenbankrecht/` erforderlich. Dies bedeutet nicht, dass jede dortige Vertiefung vollständig geprüft wäre.

## 1.2. Issue 547 – CRA-Meldungen

[Issue 547](https://github.com/Klotzkette/claude-fuer-deutsches-recht/issues/547). Ergebnis: Die beanstandeten Fristenfehler sind bereits behoben. Die beiden CRA-Produktmodule und der CRA-Abschnitt von `accuracy-robustness-cybersecurity-ai` unterscheiden aktiv ausgenutzte Schwachstellen und schwerwiegende Sicherheitsvorfälle. Der Abschlussbericht nach Artikel 14 Absatz 2 Buchstabe c folgt spätestens 14 Tage nach Verfügbarkeit der Maßnahme; der Bericht nach Absatz 4 Buchstabe c innerhalb eines Monats nach der Vorfallmeldung. Der Zwischenbericht nach Absatz 6 wird nicht als feste 72-Stunden-Stufe behandelt. Tatbestand, Kenntniszeitpunkt und Pflichtangaben sind im Muster abgegrenzt.

Direkt angrenzende Mängel wurden eigenständig korrigiert: Die Musterpolitik enthielt starre 30-/90-Tage-Patchfristen ohne Risikovorbehalt und die Lieferantenklausel begrenzte den Support pauschal auf fünf Jahre. Beide Produktmodule enthalten jetzt risikobezogene Bearbeitung, begründete Lieferantenfristen und eine anhand der erwarteten Nutzung bestimmte Support-Periode. Meldung, Lieferanteninformation und Abhilfe sind getrennte Arbeitsstränge. Richtlinienbezeichnungen für Produkthaftung und Funkanlagen sowie die Zuordnung wichtiger/kritischer Produkte zu den Anhängen III/IV wurden berichtigt. Die amtliche Erläuterung zur Herstellerpflicht seit 11. September 2026 und zur späteren Steward-Pflicht ist verlinkt.

Geändert:

- `robotik-recht/skills/cra-produkt-mit-digitalen-elementen/FACHINHALT.md`
- `robotik-recht/skills/cra-produkt-lager-intralogistikflotte/FACHINHALT.md`

## 1.3. Issue 548 – Fachlichkeit digitaler AGB-Module

[Issue 548](https://github.com/Klotzkette/claude-fuer-deutsches-recht/issues/548). Ergebnis: teilweise bereits erledigt, in vier Modulen noch berechtigt. Alle neun bezeichneten Module wurden gelesen. SaaS, Cloud-Hosting, Datenexport, KI-Dienste und KI-Ausgaben besitzen inzwischen konkrete eigene Prüfpfade einschließlich Data Act und KI-VO. Softwarelizenz, Abonnement, Verfügbarkeit/Wartung und Backup/Datenverlust enthielten dagegen weiterhin weitgehend austauschbare allgemeine AGB-Prüfschritte.

Diese vier Vertiefungen wurden eigenständig neu ausgearbeitet: Nutzungsmetriken und zwingende Programmbefugnisse; Laufzeit und Kündigungszugang; nachvollziehbare Verfügbarkeitsrechnung und Wartungsausnahmen; Sicherung, Rücksicherung, Kausalität und Mitverschulden. Die Data-Act-Schnittstelle setzt jeweils die tatsächliche Qualifikation des Dienstes voraus. Verbraucher- und Unternehmensregime werden getrennt. Kein Modul behauptet eine gesetzliche Universalhaftungsgrenze oder eine pauschale Klauselfreigabe.

Die gemeinsame Quellenhilfe enthält außerdem die am 6. November 2026 veröffentlichte Empfehlung (EU) 2026/2394 vom 29. Oktober 2026. Deren unverbindliche Muster sind ein Vergleichsmaßstab, keine Verordnung und kein Wirksamkeitsnachweis. Es werden keine Muster unbesehen übernommen.

Geändert:

- `agb-recht-pruefer/skills/softwarelizenz-agb/FACHINHALT.md`
- `agb-recht-pruefer/skills/subscription-abonnement/FACHINHALT.md`
- `agb-recht-pruefer/skills/verfuegbarkeit-wartungsfenster/FACHINHALT.md`
- `agb-recht-pruefer/skills/backup-datenverlust/FACHINHALT.md`
- `agb-recht-pruefer/references/digitaldienste-data-act-ki.md`

## 1.4. Issue 550 – Artikel 25 KI-VO und GPAI

[Issue 550](https://github.com/Klotzkette/claude-fuer-deutsches-recht/issues/550). Ergebnis: Die ursprünglichen Fehler sind bereits behoben. Gelesen wurden `anbieter-werden-art-25`, `bevollmaechtigter-produkthersteller-pflichten` und beide bezeichneten Einführer-Vertiefungen sowie der README-Verweis. Artikel 25 Absatz 1 hat drei Fälle; der Produktherstellerfall steht in Absatz 3. Buchstabe c setzt den Wechsel eines zuvor nicht hochriskanten Systems zum Hochrisikosystem voraus. Modell und System werden getrennt, Artikel 16 wird nicht durch den pauschalen Bereich „16 bis 42“ ersetzt. Der verlinkte Produktherstellerpfad existiert.

Zur unmittelbar verständlichen Umsetzung wurde im Rollenmodul die GPAI-Anbieterprüfung nach Artikel 3 Nummer 3 ausdrücklich ausformuliert: Entwicklung oder Entwickelnlassen, eigenes Kennzeichen und Inverkehrbringen sind zu belegen. Artikel 25 ersetzt diese Modellprüfung nicht; ein darauf aufgebautes System bleibt gesondert zu beurteilen.

Geändert: `ki-vo-ai-act-pruefer/skills/anbieter-werden-art-25/FACHINHALT.md`.

## 1.5. Gelesene Primärstellen und Abrufgrenzen

1. [Data Act, amtlicher Text](https://eur-lex.europa.eu/eli/reg/2023/2854/oj): gezielte amtliche Suchindexpassagen insbesondere zu Artikeln 29, 43 und 50; ergänzend [Bundesnetzagentur, Anbieterfragen](https://www.bundesnetzagentur.de/EN/Areas/Digitalisation/DataAct/background/3-provider/faq/faq_anbieter.html) und amtliche Erläuterungen zu Kapitel VI. Mehrere direkte EUR-Lex-Aufrufe lieferten eine JavaScript-Prüfseite. Daher wird kein vollständig direkt gelesener Normabruf behauptet. Für die bereits vorhandenen weiteren Einzelzuordnungen erfolgte eine Plausibilitätskontrolle des konkreten Textes, keine dokumentierte Volltextnachprüfung jeder Teilnorm.
2. [CRA, amtlicher Text](https://eur-lex.europa.eu/eli/reg/2024/2847/oj): amtliche Suchindexpassagen zu Artikel 13 Absatz 8, Artikel 14, Artikel 71 und Anhang I; [Kommission, CRA-Meldungen](https://digital-strategy.ec.europa.eu/en/policies/cra-reporting) direkt gelesen, einschließlich Fristen, Plattform und Staffelung. Auch hier waren mehrere direkte EUR-Lex-Volltextaufrufe technisch gesperrt. Die konkreten Meldefristen wurden durch die direkt gelesene amtliche Erläuterung gegengeprüft.
3. [Empfehlung (EU) 2026/2394, amtliches PDF](https://publications.europa.eu/resource/cellar/fea1d35a-d982-11f1-8501-01aa75ed71a1.0006.01/DOC_1): Titel, Datum, Veröffentlichung, Erwägungsgrund 9 und modulare/unverbindliche Ausgestaltung gelesen. Kein Anspruch, sämtliche 127 Seiten oder alle Klauseln vollständig geprüft zu haben.
4. [Artikel 3 KI-VO, Kommissions-Explorer](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-3) und [Artikel 25](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-25): angezeigter konsolidierter Normtext gelesen. Der Explorer bezeichnet selbst den Normstand vom 27. Juli 2026. Für die Änderung wurden Definition und Rollenwechsel geprüft, keine vollständige Verifikation aller KI-VO-Fristen behauptet.
5. Direkt gelesen auf Gesetze im Internet: [§ 69d UrhG](https://www.gesetze-im-internet.de/urhg/__69d.html), [§ 69g UrhG](https://www.gesetze-im-internet.de/urhg/__69g.html), [§ 309 BGB](https://www.gesetze-im-internet.de/bgb/__309.html), [§ 327f BGB](https://www.gesetze-im-internet.de/bgb/__327f.html), [§ 254 BGB](https://www.gesetze-im-internet.de/bgb/__254.html). [§ 310 BGB](https://www.gesetze-im-internet.de/bgb/__310.html) und [§ 312k BGB](https://www.gesetze-im-internet.de/bgb/__312k.html) wurden wegen Timeouts über amtliche Suchindexpassagen abgeglichen.

Diese Prüfung ergänzt Normen- und Workflowqualität. Sie behauptet keine neue oder vollständig überprüfte gerichtliche Entscheidung. Testakten wurden nicht verändert. Es wurden keine GitHub-Antworten versandt und keine Issues geschlossen.

## 1.6. Lokale Prüfung

`git diff --check` war erfolgreich. Geprüft wurden außerdem die sechs Abschnitte, passenden Modulnamen und vorhandenen lokalen Quellenziele der vier neu ausgearbeiteten AGB-Vertiefungen; die getrennten CRA-Abschlussfristen blieben erhalten, die starren 30-/90-Tage- und Fünfjahres-Muster wurden entfernt. Die repositoryweiten Generatoren, Quellzuordnungen und Paketprüfungen sind Aufgabe der abschließenden Integration.
