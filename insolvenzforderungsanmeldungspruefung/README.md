# Insolvenzforderungsanmeldungsprüfung

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`insolvenzforderungsanmeldungspruefung`) | [`insolvenzforderungsanmeldungspruefung.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/insolvenzforderungsanmeldungspruefung.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Insolvenzforderungsanmeldungsprüfung Phoenix Solar Montage GmbH** (`insolvenzforderungsanmeldungspruefung-phoenix-solar`) | [Gesamt-PDF lesen](../testakten/insolvenzforderungsanmeldungspruefung-phoenix-solar/gesamt-pdf/insolvenzforderungsanmeldungspruefung-phoenix-solar_gesamt.pdf) | [`testakte-insolvenzforderungsanmeldungspruefung-phoenix-solar.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-insolvenzforderungsanmeldungspruefung-phoenix-solar.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Freistehendes Cowork-Plugin für die Prüfung von Insolvenzforderungen vom Eingang bis zur Tabellenfeststellung. Es ist ein vollständiger Arbeitsraum für Verwalterbüro, Sachwaltung, Forderungsmanagement und Prozessnachlauf: Anmeldung erfassen, Mängel erkennen, Belege nachfordern, Grund, Betrag und Rang prüfen, Entscheidung dokumentieren, Tabelle befüllen, Prüfungstermin vorbereiten, Bestreiten oder Feststellung ausgeben und streitige Forderungen bis zur Verteilung nachhalten.

## Direkt herunterladen

- [Plugin-ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/insolvenzforderungsanmeldungspruefung.zip)
- [Testakte Phoenix Solar](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-insolvenzforderungsanmeldungspruefung-phoenix-solar.zip)
- [Vorschau lokal öffnen](./assets/vorschau/index.html)

## Wofür das Plugin gedacht ist

- Masseneingang von Forderungsanmeldungen per Post, E-Mail, Portalexport, Tabellenliste oder manuellem Upload.
- Formale Prüfung nach § 174 InsO einschließlich Grund, Betrag, Urkunden, elektronischer Anmeldung, vbuH-/Unterhalts-/Steuerstraf-Hinweis und Nachrang.
- Materielle Plausibilisierung anhand Schuldnerbuchhaltung, OPOS, Verträgen, Titeln, Lieferscheinen, Kontoauszügen und bisherigem Verfahrensstand.
- Entscheidungsvorbereitung für Feststellung, Teilbestreiten, vollständiges Bestreiten, Nachforderung, Rangkorrektur, vbuH-Widerspruch und Masse-/Insolvenzforderung-Abgrenzung.
- Tabellenarbeit nach § 175 InsO, Prüfungstermin nach § 176 InsO, nachträgliche Anmeldung nach § 177 InsO, Feststellungswirkung nach § 178 InsO und Streitnachlauf nach §§ 179 bis 181, 184 und 189 InsO.

## Leitprinzip

Das Plugin arbeitet verzeihend, aber nicht schlampig. Es akzeptiert unsaubere Gläubigeranschreiben, unvollständige Belege, widersprüchliche Rechnungsnummern und doppelte Portaleingänge. Es zieht daraus aber nie automatisch eine Feststellung. Fehlende Substanz wird als Mangel, Risiko oder Rückfrage markiert. Jede Tabellenentscheidung bleibt nachvollziehbar: Was ist angemeldet, was ist belegt, was ist bestritten, warum, durch wen und mit welchem nächsten Schritt.

## Typischer Ablauf

1. Intake öffnen: Eingangsstapel, Metadaten, Gläubiger, Frist, Kanal, Dateinamen und Dublettenverdacht erfassen.
2. § 174-Check: Grund, Betrag, Rang, Belege, vbuH-Kennzeichnung und elektronische Form prüfen.
3. Belegkette bilden: Rechnung, Titel, Vertrag, Lieferung, Zahlung, Buchhaltung, offene Restforderung und Rang verbinden.
4. Prüfentscheidung treffen: feststellen, teilweise feststellen, bestreiten, vorläufig zurückstellen oder Nachforderung schreiben.
5. Tabelle füllen: Tabellenimport, Prüfvermerk, Widerspruchsvermerk und Prüfungsterminmappe erzeugen.
6. Nachlauf steuern: Tabellenauszug, Feststellungsklage, Schuldnerwiderspruch, § 189-Verteilung und Wiedervorlagen kontrollieren.

## Enthaltene Skills

| Skill | Zweck |
| --- | --- |
| ifap-kommandocenter | Startet den gesamten Prüfpfad und entscheidet, welcher Arbeitsmodus passt. |
| ifap-intake-kanalcheck | Erfasst Post, E-Mail, Portal, Stapel, Nachzügler und Metadaten. |
| ifap-aktenanlage-batchregister | Baut Register, Prüfnummern, Gläubigerstamm und Eingangsbuch auf. |
| ifap-formalpruefung-174 | Prüft die formalen Mindestangaben nach § 174 InsO. |
| ifap-beleg-und-urkundencheck | Bildet die Belegkette und erkennt fehlende Urkunden. |
| ifap-grund-betrag-zinsen | Prüft Anspruchsgrund, Betrag, Teilzahlungen und Zinslauf. |
| ifap-rang-nachrang-absonderung | Trennt Insolvenzforderung, Nachrang, Sicherheiten und Ausfall. |
| ifap-masseverbindlichkeit-abgrenzen | Erkennt falsch angemeldete Masseforderungen und Abgrenzungsfälle. |
| ifap-vbuh-pruefung | Prüft vbuH, Unterhalt und Steuerstraftat mit Tatsachenbasis. |
| ifap-dubletten-serienforderungen | Erkennt Mehrfachanmeldungen, Serienrechnungen und Vertreterwechsel. |
| ifap-nachforderung-maengelschreiben | Erstellt präzise Beleg- und Substanznachforderungen. |
| ifap-pruefentscheidung | Erstellt Feststellungs-, Teilbestreitens- und Bestreitensvermerke. |
| ifap-tabellenimport-175 | Baut einen gerichtsfesten Tabellenimport nach § 175 InsO. |
| ifap-pruefungstermin-176 | Bereitet Prüfungstermin oder schriftliches Verfahren vor. |
| ifap-nachtraegliche-anmeldung-177 | Steuert verspätete und geänderte Anmeldungen. |
| ifap-tabellenauszug-178 | Erzeugt Tabellenauszug- und Feststellungswirkungs-Ausgaben. |
| ifap-streitige-forderung-179-180 | Führt den Feststellungsklage- und Rechtsstreit-Nachlauf. |
| ifap-schuldnerwiderspruch-184 | Behandelt Schuldnerwiderspruch und Monatsfrist bei titulierten Forderungen. |
| ifap-verteilung-bestrittene-189 | Hält § 189-Nachweise und Rückbehalte für Verteilungen nach. |
| ifap-quality-gate | Prüft Vollständigkeit, Plausibilität, Quellen, Fristen und Audit-Trail. |

## Grenzen

Das Plugin trifft keine unüberprüfte Rechtsentscheidung und ersetzt keine fachliche Prüfung. Bei streitigen Rechtsfragen, Rechtskraft-/Titelthemen, vbuH, Rangverschiebungen, Absonderungsrechten, § 189-Rückbehalten und drohenden Feststellungsklagen verlangt es ausdrücklich menschliche Freigabe.

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 54 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `allgemein` | Einstieg, Schnelltriage und Workflow-Routing im Insolvenzforderungsanmeldungspruefung-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen... |
| `iap-anmeldepruefung-bauleiter` | Bauleiter Pruefung von Insolvenzforderungsanmeldungen: Grund, Hoehe, Rang, Bestreiten. Pruefraster fuer Insolvenzverwalter. |
| `iap-aussonderung-absonderung-spezial` | Spezialfall Aussonderung und Absonderung §§ 47 sowie 49 ff. InsO: Eigentumsvorbehalt, Sicherungseigentum, Forderungsabtretung, Grundpfandrecht. Pruefraster fuer Insolvenzverwalter. |
| `iap-konzernforderungen-anfechtung-spezial` | Spezialfall Konzernforderungen und Anfechtung im Konzern: Cash-Pool, Konzernverrechnung, Bargeschaeftsausnahme, BGH-Rechtsprechung. Pruefraster fuer Konzernverwalter. |
| `iap-rangordnung-checkliste` | Checkliste Rangordnung der Insolvenzforderungen § 38 / § 39 InsO: einfach, nachrangig, Massekosten, Masseverbindlichkeiten. Pruefraster fuer Tabellenfuehrer. |
| `ifap-aktenanlage-batchregister` | Batchregister für Massenverfahren Insolvenzforderungsanmeldung anlegen: Anwendungsfall Insolvenzverwalter oder Prüfungsstelle erhaelt umfangreichen Stapel Forderungsanmeldungen nach § 174 InsO und muss strukturiertes Register aufbauen. §... |
| `ifap-beleg-und-urkundencheck` | Belege und Urkunden bei Insolvenzforderungsanmeldung prüfen: Anwendungsfall Gläubiger legt Rechnungen Verträge Titel Lieferscheine Kontoauszüge vor; Insolvenzverwalter oder Prüfungsstelle muss Belegkette aufbauen und Beweiswert einordnen... |
| `ifap-dubletten-serienforderungen` | Dubletten und Serienforderungen in Insolvenzanmeldungen erkennen: Anwendungsfall mehrere Gläubiger melden gleichartige oder identische Forderungen an; Inkassounternehmen und Originalgläubiger reichen parallel ein. § 174 InsO Forderungsan... |
| `ifap-formalpruefung-174` | Formalprüfung Forderungsanmeldung nach § 174 InsO: Anwendungsfall Insolvenzverwalter oder Prüfungsstelle prüft ob eingegangene Anmeldung Mindestangaben hat und tabellenfähig ist. § 174 InsO Pflichtinhalt, § 175 InsO Tabelle, § 176 InsO P... |
| `ifap-grund-betrag-zinsen` | Anspruchsgrund Betrag und Zinsen der Insolvenzforderung prüfen: Anwendungsfall Insolvenzverwalter prüft ob angemeldeter Betrag rechnerisch korrekt und durch Anspruchsgrundlage gedeckt ist. § 174 InsO Forderungsanmeldung, §§ 38-39 InsO In... |
| `ifap-intake-kanalcheck` | Eingehende Forderungsanmeldungen kanalübergreifend erfassen: Anwendungsfall Insolvenzverwalter-Büro erhält Anmeldungen per Post E-Mail Portal Tabellenexport oder Nachtrag und muss einheitliches Eingangsbuch führen. § 174 InsO Forderungsa... |
| `ifap-kommandocenter` | Kommandocenter Insolvenzforderungsanmeldungsprüfung: Steuerung des gesamten Prüfpfads von Eingang bis Tabelle. Anwendungsfall Insolvenzverwalter oder Kanzlei erhält neuen Forderungsstapel und muss schnell den richtigen Prüfschritt finden... |
| `ifap-masseverbindlichkeit-abgrenzen` | Masseverbindlichkeiten von Insolvenzforderungen abgrenzen: Anwendungsfall Insolvenzverwalter erkennt Forderung die nach Verfahrenseroeffnung entstanden sein koennte und muss klaeren ob es Masseverbindlichkeit oder einfache Insolvenzforde... |
| `ifap-nachforderung-maengelschreiben` | Mängel- und Nachforderungsschreiben bei unvollständigen Insolvenzanmeldungen: Anwendungsfall Forderungsanmeldung nach § 174 InsO hat Mängel und Insolvenzverwalter muss Gläubiger präzise und freundlich zur Ergänzung auffordern. § 174 InsO... |
| `ifap-nachtraegliche-anmeldung-177` | Verspätete und nachträgliche Forderungsanmeldungen nach § 177 InsO: Anwendungsfall Gläubiger meldet Forderung nach Ablauf der Anmeldefrist an oder ändert bereits angemeldete Forderung. § 177 InsO Nachtragsanmeldung, § 176 InsO Prüfungste... |
| `ifap-pruefentscheidung` | Prüfentscheidung Forderung festzustellen oder zu bestreiten: Anwendungsfall nach abgeschlossener Prüfung trifft Insolvenzverwalter Entscheidung über Feststellung Teilfeststellung Bestreiten oder Rückstellung. § 176 InsO Prüfungstermin, §... |
| `ifap-pruefungstermin-176` | Prüfungstermin nach § 176 InsO vorbereiten: Anwendungsfall Prüfungstermin beim Insolvenzgericht naht und Insolvenzverwalter muss Einzelforderungen, Widersprüche und Erörterungspunkte aufbereiten. § 176 InsO Prüfungstermin, § 178 InsO Tab... |
| `ifap-quality-gate` | Qualitätsgate vor Tabelleneintrag Prüfungstermin und Verteilung: Anwendungsfall alle Prüfschritte wurden durchgeführt und jetzt muss vor Versand oder Eintrag nochmals Vollständigkeit Plausibilitaet und Risiken geprüft werden. § 175 InsO... |
| `ifap-rang-nachrang-absonderung` | Rang Nachrang Absonderung und Aussonderung bei Insolvenzforderungen prüfen: Anwendungsfall Gläubiger behauptet Sonderrechte wie Absonderungsrecht aus Sicherungsuebereignung oder Nachrang. §§ 38-39 InsO Insolvenzforderungen und Nachrang,... |
| `ifap-schuldnerwiderspruch-184` | Schuldnerwiderspruch nach § 184 InsO prüfen und Fristen einhalten: Anwendungsfall Schuldner widerspricht Forderung und bei titulierten Forderungen laeuft Monatsfrist für Aufnahme des Rechtsstreits. § 184 InsO Schuldnerwiderspruch, § 179... |
| `ifap-streitige-forderung-179-180` | Streitige Forderungen nach §§ 179 und 180 InsO nachverfolgen: Anwendungsfall Forderung wurde beim Prüfungstermin bestritten und Gläubiger muss Feststellungsklage erheben oder laufenden Rechtsstreit aufnehmen. § 179 InsO Feststellungsklag... |
| `ifap-tabellenauszug-178` | Tabellenauszug und Feststellungswirkung nach § 178 InsO: Anwendungsfall Forderung ist festgestellt und Gläubiger fragt nach Status oder Insolvenzverwalter muss Tabellenauszug als vollstreckbaren Titel erstellen. § 178 InsO Feststellungsw... |
| `ifap-tabellenimport-175` | Tabelleneintrag und Tabellenimport nach § 175 InsO: Anwendungsfall Forderungen sind geprüft und muessen in gerichtliche Tabelle überführt werden oder CSV-Import in Verwaltungssoftware vorbereitet werden. § 175 InsO Tabelle, § 176 InsO Pr... |
| `ifap-vbuh-pruefung` | Vorsätzlich begangene unerlaubte Handlung und Steuerstraftat in Insolvenzanmeldung prüfen: Anwendungsfall Gläubiger meldet Forderung mit Kennzeichnung als vbuH vorsaetzliche unerlaubte Handlung Unterhaltspflichtverletzung oder Steuerstra... |
| `ifap-verteilung-bestrittene-189` | Verteilung bei bestrittenen Forderungen nach § 189 InsO: Anwendungsfall Insolvenzverwalter bereitet Abschlags- oder Schlussverteilung vor und muss bestrittene Forderungen korrekt zurückbehalten oder ausklammern. § 189 InsO Berücksichtigu... |
| `spezial-belege-dokumentenmatrix-und-lueckenliste` | Belege: Dokumentenmatrix, Lückenliste und Nachforderung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-bestreiten-mehrparteien-konflikt-und-interessen` | Bestreiten: Mehrparteienkonflikt und Interessenmatrix: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-betrag-behoerden-gericht-und-registerweg` | Betrag: Behörden-, Gerichts- oder Registerweg: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-feststellung-internationaler-bezug-und-schnittstellen` | Feststellung: Internationaler Bezug und Schnittstellen: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-forderungsgrund-rang-und-belegpruefung` | Forderungsgrund, Rang und Belegprüfung zur Tabelle: führt schnell durch Sachverhalt, Rechtsgrundlagen, Belege, Risiken und erzeugt einen verwertbaren nächsten Output. |
| `spezial-grund-risikoampel-und-gegenargumente` | Grund: Risikoampel, Gegenargumente und Verteidigungslinien: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-ifap-mandantenkommunikation-entscheidungsvorlage` | Ifap: Mandantenkommunikation und Entscheidungsvorlage: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-inso-fristen-form-und-zustaendigkeit` | InsO: Fristen, Form, Zuständigkeit und Rechtsweg: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-insolvenzforderungsanmeldungspruefung-erstpruefung` | Insolvenzforderungsanmeldungspruefung: Erstprüfung, Rollenklärung und Mandatsziel: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-intake-tatbestand-beweis-und-belege` | Intake: Tatbestandsmerkmale, Beweisfragen und Beleglage: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-kanalcheck-beweislast-und-darlegungslast` | Kanalcheck: Beweislast, Darlegungslast und Substantiierung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-masseverbindlichkeit-sonderfall-und-edge-case` | Masseverbindlichkeit: Sonderfall und Edge-Case-Prüfung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-nachforderungen-livequellen-und-rechtsprechungscheck` | Nachforderungen: Livequellen- und Rechtsprechungscheck: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-pruefungstermin-compliance-dokumentation-und-akte` | Pruefungstermin: Compliance-Dokumentation und Aktenvermerk: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-rang-schriftsatz-brief-und-memo-bausteine` | Rang: Schriftsatz-, Brief- und Memo-Bausteine: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-tabellenauszug-formular-portal-und-einreichung` | Tabellenauszug: Formular, Portal und Einreichungslogik: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-tabellenimport-zahlen-schwellen-und-berechnung` | Tabellenimport: Zahlen, Schwellenwerte und Berechnung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-vbuh-verhandlung-vergleich-und-eskalation` | Vbuh: Verhandlung, Vergleich und Eskalation: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-verteilung-red-team-und-qualitaetskontrolle` | Verteilung: Red-Team und Qualitätskontrolle: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `workflow-anschluss-skills-router` | Anschluss-Skills Router im Plugin insolvenzforderungsanmeldungspruefung: schlägt nach der ersten Prüfung die passenden Spezialskills aus demselben Plugin vor. |
| `workflow-chronologie-und-belegmatrix` | Chronologie und Belegmatrix im Plugin insolvenzforderungsanmeldungspruefung: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen. |
| `workflow-dokumentenintake` | Dokumentenintake im Plugin insolvenzforderungsanmeldungspruefung: liest Uploads, sortiert Dokumentarten, markiert Fristen und baut eine knappe Arbeitsakte. |
| `workflow-fristen-und-risikoampel` | Fristen- und Risikoampel im Plugin insolvenzforderungsanmeldungspruefung: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen. |
| `workflow-kaltstart-und-routing` | Kaltstart und Routing im Plugin insolvenzforderungsanmeldungspruefung: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills. |
| `workflow-mandantenkommunikation` | Mandantenkommunikation im Plugin insolvenzforderungsanmeldungspruefung: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten. |
| `workflow-output-waehlen` | Output wählen im Plugin insolvenzforderungsanmeldungspruefung: entscheidet zwischen Memo, Schriftsatz, Tabelle, Brief, Checkliste, Vermerk, Redline oder Mandantenübersetzung. |
| `workflow-rechtsquellen-livecheck` | Rechtsquellen-Livecheck im Plugin insolvenzforderungsanmeldungspruefung: zwingt vor tragenden Aussagen zum aktuellen Quellencheck bei Gesetzen, Behörden, Gerichten und Formularen. |
| `workflow-redteam-qualitygate` | Red-Team Qualitygate im Plugin insolvenzforderungsanmeldungspruefung: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton. |
| `workflow-unterlagen-lueckenliste` | Unterlagen- und Lückenliste im Plugin insolvenzforderungsanmeldungspruefung: erstellt eine präzise Nachforderungsliste statt allgemeiner Fragebögen. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
