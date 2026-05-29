# Testakte LG Regensburg — Sieglinger gegen Burgwald Energietechnik GmbH

## ⬇️ Direkt-Download

| Testakte | Direkt-Download |
| --- | --- |
| `testakte-sachverstaendigengutachten-ki-vorwurf-lg-regensburg-sieglinger` (diese Akte) | [testakte-sachverstaendigengutachten-ki-vorwurf-lg-regensburg-sieglinger.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-sachverstaendigengutachten-ki-vorwurf-lg-regensburg-sieglinger.zip) |

Die Testakte ist **kein Teil des Plugins** und wird separat als ZIP-Datei aus dem GitHub-Release geladen. Das ZIP enthält die Originalformate (PDF, DOCX, XLSX, CSV, JPEG) für realistische Tests.


## Zweck der Testakte

Diese Akte ist eine **abstrahierte Testakte** fuer Workflows zum Umgang mit dem Vorwurf, ein gerichtliches Sachverstaendigengutachten sei ganz oder teilweise unter Einsatz von KI-Werkzeugen erstellt worden.

Sie dient dem **Plugin `vertragsrecht`** als Erprobungsfall und kann gleichzeitig folgende Skills aktivieren:

- `umgang-mit-ki-vorwurf-bei-sachverstaendigengutachten` (allgemeine Anwaltsseite)
- `pruefung-sachverstaendigengutachten-ki-deklaration` (Plugin `jveg-kostenpruefer`)
- `ki-einsatz-bei-gutachten-mandatsseite` (Plugin `grosskanzlei-corporate-ma`)

## Hinweis zur Fragmentaritaet

Die Akte ist absichtlich **fragmentarisch** aufgebaut. Manche Dokumente sind nur als Auszug enthalten (Klageerwiderung, E-Mail des Sachverstaendigen, Kostenkalkulation Privatgutachten). Manche Daten fehlen (Vergleichsgutachten). Verschiedene **Dateiformate** sind beigemischt — Markdown, JSON, CSV, EML, TXT. Das spiegelt eine reale Mandatslage wider, in der die Anwaeltin oder der Anwalt mit unvollstaendigen Informationen arbeiten muss.

## Sachverhalt — Kurz

- Klaeger: Landwirt mit Hofladen, hat Photovoltaikanlage auf Stallgebaeude errichten lassen
- Beklagte: ausfuehrendes Unternehmen
- Streit: Minderleistung, Wechselrichter-Stoerungen, Wassereintritt durch Modulhaltermangel
- Gerichtsbestellter Sachverstaendiger hat Gutachten eingereicht
- Mandant ist mit Gutachten unzufrieden — methodisch duenn, stilistisch auffaellig
- Anwaltsteam sammelt Indizien und plant gestufte Eskalation

## Vorgang in Stichworten

1. Klage erhoben am 04.06.2024
2. Klageerwiderung mit Verjaehrungseinrede
3. Beweisbeschluss vom 15.01.2025 — Sachverstaendiger Pfaffenberger bestellt
4. Gutachten Pfaffenberger eingereicht am 28.10.2025 (64 Seiten)
5. Anwaltsteam bemerkt Auffaelligkeiten:
   - mehrfach gleichfoermige Satzanfaenge
   - nicht ersetzter Platzhalter
   - vermutliche Norm-Halluzination
   - pauschale Schaetzungen
   - Stilbrueche
6. Mandantenbesprechung am 18.11.2025
7. Interne Strategieskizze (19.11.2025) — Stufenmodell
8. Quality Review durch Senior-Kollegen (20.11.2025)
9. Schriftsatzentwurf — Anhoerung und Aktenherausgabe
10. Nachfrage der Kammer beim Sachverstaendigen (E-Mail-Auszug vom 24.11.2025)

## Aktenverzeichnis

- 00_aktenuebersicht.md — Aktenuebersicht und Verfahrenslage
- 01_klage_schriftsatz.md — Klageschrift
- 02_klageerwiderung_burgwald.md — Klageerwiderung (FRAGMENT)
- 03_beweisbeschluss_15_01_2025.md — Beweisbeschluss
- 04_gutachten_pfaffenberger_auszug.txt — Gutachtenauszuege (auffaellige Stellen)
- 05_indizien_ki_einsatz.csv — Tabelle der Auffaelligkeiten
- 06_mandantenbesprechung_18_11_2025.md — Aktenvermerk Besprechung
- 07_strategieskizze_anwalt.md — Interne Strategie
- 08_schriftsatzentwurf_anhoerungsantrag.md — Schriftsatzentwurf
- 09_vergleich_andere_gutachten_pfaffenberger.json — Vergleichsrecherche (FRAGMENT)
- 10_protokoll_internes_quality_review.md — Senior-Review
- 11_kostenkalkulation_privatgutachten.csv — Kostenkalkulation (FRAGMENT)
- 12_email_sachverstaendiger_an_kammer.eml — E-Mail-Auszug
- 13_anlagenverzeichnis.md — Anlagenverzeichnis (FRAGMENT)

## Disclaimer

Alle Namen, Aktenzeichen, Adressen, Telefonnummern und technischen Daten sind erfunden. Diese Akte hat keinen Bezug zu realen Personen oder realen Verfahren. Sie dient ausschliesslich der Erprobung von Workflows in deutschen Rechtsanwaltskanzleien.

## Empfohlener Workflow

1. Aktenuebersicht lesen (00_aktenuebersicht.md)
2. Beweisbeschluss und Klageschrift kurz scannen
3. Auszug Gutachten und Indizien-CSV pruefen
4. Mit dem entsprechenden Skill arbeiten (siehe oben)
5. Schriftsatzentwurf gegen den vorhandenen Entwurf abgleichen
6. Eigene Strategie mit der internen Strategieskizze vergleichen
