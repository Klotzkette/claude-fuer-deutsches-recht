---
name: 23-klage-egvp-bea-einreichen
description: "Gerichtsfertige Dokumentenproduktion für Klage, Replik, Antrag und sonstigen Schriftsatz. Nutze ihn bei fertig zur Einreichung, beA-ready, eBO, Schriftsatz finalisieren oder Anlagenpaket. Prüft Eigenvertretung oder Kanzlei, Einreichungsweg, einzelne PDFs, K- oder B-Nummern, ASCII-Dateinamen, ERVV, Signatur, Freigabe und Eingang. Output Versandpaket."
---

# Gerichtsprozess-Dokumentenproduktion und Übermittlungsweg

## Zweck und Anwendungsfall

Dieser Skill macht aus einem fachlich freigegebenen Schriftsatz und seinen Belegen ein gerichtsfertiges Dokumentenpaket. Er wird geladen, wenn ein Nutzer einen Schriftsatz „fertig zur Einreichung“, „beA-ready“, „eBO-fertig“, „versandfertig“ oder „mit Anlagen K 1 ff.“ verlangt. Er prüft Inhalt, Erscheinungsbild, Anlagenfolge, PDF-Arbeitskopien, Dateinamen, Signaturweg, Übermittlungsdaten und Eingangsnachweis. Vor jeder technischen Produktion entscheidet er, ob die private Konzerngesellschaft selbst handelt oder eine Kanzlei einreicht. Er versendet nicht selbst aus einem beA oder eBO.

## Bedienmodus

Arbeite für hochtrainierte Rechtsanwalts- und Notarfachangestellte, Renofas, Rechtsfachwirt:innen und Forderungsmanagement-Spezialist:innen. Sie bereiten das Paket vollständig vor und können die private Konzerngesellschaft im zulässigen Parteiprozess nach dokumentiertem Rollencheck vertreten. Ein beA darf nur über die tatsächlich verantwortende Rechtsanwältin oder den tatsächlich verantwortenden Rechtsanwalt genutzt werden. Ein eBO darf nur als tatsächlich eingerichtetes und identifiziertes Organisationspostfach verwendet werden. Schwierige Form-, Frist- oder Signaturfragen werden rot an Skill `08-eskalation-an-anwalt` übergeben.

## Eingaben

- Gericht, Gerichtsanschrift, Aktenzeichen oder Kennzeichen `Neueingang`, Parteirolle und Verfahrensgegenstand.
- Letzte freigegebene Fassung des Schriftsatzes mit eindeutiger Versions-ID oder Hash.
- Anlagenmanifest aus Skill `39-beweisangebot-anlagenplan`, bereits eingereichte Anlagen und alle neuen Originaldateien.
- Gewünschtes Erscheinungsbild: Konzernbriefkopf oder neutrale Gerichtsfassung, Schrift, Kopf-/Fußzeile, Unterschriftsblock und zulässige Schwärzungen.
- Einreichungsrolle: Eigenvertretung der Konzerngesellschaft oder beauftragte Kanzlei; bei Eigenvertretung Beschäftigtenstatus, Vollmacht und gegebenenfalls eBO-Postfachinhaber.
- Verantwortende Person, Signaturmodell, tatsächlich verfügbarer Übermittlungsweg, Frist, Vorfrist und reale Freigabeperson.
- Verfahrensart: reguläres Verfahren oder beabsichtigtes Online-Verfahren nach Paragrafen 1122 ff. ZPO mit dokumentiertem Pilotgericht und Dienstcheck.

Fehlen Kernangaben, stelle gebündelt höchstens drei Fragen: erst Gericht/Aktenzeichen/Frist, dann Eigenvertretung oder Kanzlei samt tatsächlich verfügbarem Postfach, danach fehlende Anlagen und Gestaltungsprofil. Erzeuge bis zur Antwort ein Paket mit gelber Lückenliste, aber keine fiktiven Dateien, Postfächer oder Freigaben.

## Ablauf / Checkliste

### 1. Paketkopf und Freigabe sperren

1. Paket-ID, Akten-ID, Datenstichtag, Gericht, Aktenzeichen, Parteirolle, Dokumenttyp, Frist und verantwortliche Person erfassen.
2. Rollengate vor jeder Produktion schließen:

| Einreicher | Vertretungs- und Formprüfung | Möglicher Weg |
|---|---|---|
| Private Konzerngesellschaft in zulässiger Eigenvertretung | Paragraf 79 Abs. 2 S. 2 Nr. 1 ZPO, Beschäftigtenstatus, Konzernverbund, Vollmacht und Zeichnung prüfen | tatsächlich eingerichtetes eBO nach Paragraf 130a Abs. 4 S. 1 Nr. 3 ZPO und Paragraf 10 ERVV oder eine im konkreten Verfahren zulässige schriftliche Einreichung |
| Beauftragte Rechtsanwaltskanzlei | Mandat, verantwortende anwaltliche Person und Einreichungspflicht nach Paragraf 130d ZPO prüfen | beA mit zulässigem Signaturmodell |
| Rolle, Vollmacht oder Postfach unklar | keine Formwirksamkeit unterstellen | rote Übergabe an Skill 08 oder die reale Verfahrensverantwortung |

3. Eine private GmbH fällt nicht allein wegen ihrer Rechtsform unter Paragraf 130d ZPO. Die dortige aktive Nutzungspflicht trifft Rechtsanwälte, Behörden und juristische Personen des öffentlichen Rechts. Freiwillige elektronische Eigenübermittlung über eBO und anwaltliche Pflichtübermittlung über beA dürfen nicht vermischt werden.
4. Status zunächst auf `ENTWURF - NICHT VERSENDEN/EINREICHEN` setzen.
5. Schriftsatzversion gegen Betrag, Antrag, Partei, Frist, Beweis, Anlagenstand und Datenstichtag der Freigabekarte abgleichen. Jede Abweichung hebt eine frühere Freigabe auf.
6. Nur eine benannte reale Freigabeperson darf den Status auf `FREIGEGEBEN` setzen. Das Modell darf dies weder selbst tun noch unterstellen.

### 2. Reguläres oder Online-Verfahren festlegen

1. Das Online-Verfahren nicht mit einer regulären elektronischen Einreichung verwechseln. Es ist nur bei einer reinen Zahlungsklage bis 10.000 EUR vor dem nach allgemeinen Regeln zuständigen und nach Landesrecht teilnehmenden Amtsgericht möglich; Paragrafen 1122 bis 1125 ZPO prüfen.
2. Für Berlin gilt am 09.08.2026: Das Amtsgericht Schöneberg nimmt seit 15.04.2026 nur für seinen eigenen Gerichtsbezirk teil. Eine Zuständigkeit für andere Berliner Bezirke entsteht dadurch nicht.
3. Den aktuellen amtlichen Dienst vor Produktion öffnen und prüfen, ob Anspruch, Klägerin und tatsächliches Vertretungsmodell unterstützt werden. Der veröffentlichte Dienst bildet derzeit die Eigenklage einer natürlichen Person oder die anwaltliche Einreichung ab, nicht automatisch die Eigenvertretung einer privaten GmbH durch Beschäftigte.
4. Ein Online-Verfahren wird nur eröffnet, wenn die Klage mit dem amtlichen digitalen Eingabesystem erstellt und anschließend über den für die tatsächliche Rolle zulässigen sicheren Weg eingereicht wird. Eine vorhandene Word- oder PDF-Klage darf nicht bloß als `Online-Verfahren` umbenannt werden.
5. Scheitert eines dieser Gates, reguläres Paket nach Paragraf 253 und Paragraf 130a ZPO beziehungsweise zulässigem Schriftweg erzeugen. Das Ergebnisfeld lautet dann ausdrücklich `REGULÄRES VERFAHREN`.
6. Verfahrensart, Rechtsgrund, Gericht, Landesregel, Dienst-Abrufdatum, Rolle und Übermittlungsweg in die Freigabekarte übernehmen. Die vollständige Stichtagslogik steht in `references/rechtsstand-2026-verfahren-vollstreckung.md`.

### 3. Schriftsatz fachlich und visuell finalisieren

1. Pflichtangaben nach den Paragrafen 130 und 253 ZPO prüfen: Gericht, Parteien, Vertreter, Gegenstand, Anträge, Tatsachen, Einlassung, Beweismittel und Anlagenzahl.
2. Rubrum, Anträge, Forderungsbetrag, Zinslauf, Streitwert, Anlagenzitate und Anlagenverzeichnis gegeneinander rechnen.
3. Gewünschtes Gestaltungsprofil abfragen. Ohne Vorgabe gilt `Gericht-neutral`: ruhige Typografie, klare Seitenränder, Seitenzahlen, Aktenzeichen in Kopfzeile, keine dekorativen Elemente.
4. Kommentare, Änderungsverfolgung, verborgene Felder, leere Seiten, interne Freigabevermerke und nicht freigegebene personenbezogene Daten aus der Einreichungsfassung entfernen.
5. Jede Seite visuell prüfen: vollständig, lesbar, richtig gedreht, nicht abgeschnitten, Tabellen umbrechen sauber und Unterschriftsblock ist vorhanden.

### 4. Anlagenbestand schließen

1. Anlagenmanifest aus Skill `39` übernehmen und bereits bei Gericht eingereichte Nummern unverändert lassen.
2. Klägeranlagen fortlaufend als `K 1`, `K 2` bis `K n`, Beklagtenanlagen als `B 1`, `B 2` bis `B n` führen. Bei Replik oder weiterem Schriftsatz nicht bei 1 neu beginnen.
3. Jede neue Anlage einer konkreten Tatsachenbehauptung und dem Anlagenzitat im Schriftsatz zuordnen.
4. Fehlende, doppelte, widersprüchliche oder nicht lesbare Anlage gelb oder rot markieren. Keine Leerdatei und keinen Platzhalter als Anlage einreichen.
5. Originaldatei unverändert archivieren. Nur eine abgeleitete Einreichungs-PDF erzeugen; Original- und Arbeitsdatei erhalten getrennte Hashwerte.

### 5. Einzel-PDFs erzeugen und kennzeichnen

1. Hauptschriftsatz und jede Anlage als eigene PDF-Datei ausgeben. ZIP-Dateien gehören nicht in die Gerichtsmitteilung.
2. Word, Excel, E-Mail, Foto oder Scan in eine lesbare PDF-Arbeitskopie umwandeln. Tabellen und Bilder dürfen nicht verkleinert werden, bis Inhalte unlesbar sind.
3. Auf der ersten Seite jeder abgeleiteten Anlage rechts oben `Anlage K 1` beziehungsweise `Anlage B 1` anbringen. Die Kennzeichnung darf keinen Originalinhalt verdecken; fehlt Platz, wird ein schmaler Rand ergänzt oder ein eindeutiges Anlagen-Deckblatt vorgeschaltet.
4. Bei mehrseitigen Anlagen Seitenfolge und Vollständigkeit prüfen. Optional auf Arbeitskopien `K 1 - Seite 2 von 8` ergänzen, niemals das Original überschreiben.
5. Suchtext/OCR, Druckbarkeit, Seitenausrichtung, Schriften, Formulare, Signaturen, Dateischutz und Schadcode-Risiko prüfen. Keine Passwörter, keine zusätzliche Verschlüsselung und kein ausführbarer Inhalt.

### 6. Gerichtstaugliche Dateinamen bilden

Interner Konzernstandard ist strenger als die ERVB: höchstens 80 Zeichen einschließlich `.pdf`, nur ASCII-Buchstaben, Ziffern, Unterstrich und Minus; Umlaute werden zu `ae`, `oe`, `ue`, `ss`. Wörter werden mit Unterstrich verbunden. Vor der Dateiendung steht kein weiterer Punkt.

| Reihenfolge | Beispiel | Zweck |
|---|---|---|
| 01 | `01_K_Klage_Mietrueckstand.pdf` | Hauptdokument bei Neueingang |
| 01 | `01_K_Replik_Mietrueckstand.pdf` | weiterer Kläger-Schriftsatz |
| 02 | `02_Anlage_K01_Mietvertrag_2022-05-01.pdf` | erste Klägeranlage |
| 03 | `03_Anlage_K02_Mietkonto_2026-07-10.pdf` | zweite Klägeranlage |
| 04 | `04_Anlagenverzeichnis_K01-K02.pdf` | nur falls Verzeichnis als eigene Datei verlangt wird |

Die Parteirolle steht nur im Namen des Hauptdokuments. Die sichtbare Bezeichnung `Anlage K 1` bleibt trotzdem im Anlagen-PDF und im Schriftsatz erhalten. Bedeutungslose Namen wie `Dok1.pdf`, überlange Vertragsbezeichnungen oder interne SAP-Pfade sind verboten.

### 7. ERV- und Signaturgate

1. Die aktuelle Fassung von `references/erv-dokumentenproduktion.md` vollständig anwenden.
2. PDF-Eignung nach Paragraf 130a ZPO, Paragraf 2 ERVV und aktueller ERVB prüfen. Der aktuelle Arbeitsgrenzwert lautet höchstens 1.000 Dateien und 200 MB je Nachricht; bei Überschreitung rot stoppen und den zulässigen Ersatzweg anwaltlich festlegen.
3. Eine EGVP-Nachricht betrifft genau ein Verfahren. Gericht, SAFE-Empfänger, Aktenzeichen oder `Neueingang`, Betreff und XJustiz-Daten prüfen.
4. Einreichungsweg als Entscheidungstabelle dokumentieren:

| Weg | Freigaberegel |
|---|---|
| Kanzlei über beA | qualifizierte elektronische Signatur oder einfache Signatur der verantwortenden anwaltlichen Person plus deren eigener Versand auf dem sicheren Übermittlungsweg; Paragraf 130d ZPO beachten |
| Konzerngesellschaft über eBO | Postfachinhaber, Identifizierung und Versandberechtigung nach Paragraf 10 ERVV belegen; Schriftsatz mit qualifizierter elektronischer Signatur oder einfacher Signatur der verantwortenden Person plus sicherer Übermittlung nach Paragraf 130a Abs. 3 und Abs. 4 S. 1 Nr. 3 ZPO |
| Schriftliche Eigenvertretung | nur wählen, wenn keine aktive elektronische Nutzungspflicht besteht und dieser Weg im konkreten Verfahren zulässig ist; eigenhändig unterzeichnete Fassung, Einreichungsart und Zugangsnachweis festlegen |

5. Bei einfacher Signatur darf eine Fachangestellte den anwaltlichen beA-Versender nicht ersetzen. Im eBO-Fall verantwortende natürliche Person, Vertretungsbefugnis, einfache Signatur und authentisierten Versand aus dem Organisationspostfach ausdrücklich dokumentieren; bei ungeklärter Personen- oder Postfachzuordnung rot stoppen. Anlagen brauchen nach Paragraf 130a Abs. 3 S. 2 ZPO keine eigene Signatur.
6. Bei technischer Störung zuerst unterscheiden: Greift Paragraf 130d ZPO wegen anwaltlicher Einreichung, gelten die strengen Anforderungen an Ersatzeinreichung und Glaubhaftmachung. Bei freiwilliger eBO-Nutzung einer privaten Konzerngesellschaft darf eine Störung nicht schematisch als Paragraf-130d-Fall behandelt werden; stattdessen vor Fristablauf den sonst zulässigen Einreichungsweg festlegen.
7. Im Paragraf-130d-Fall nach BGH VIII ZB 17/25 eine aus sich verständliche, geschlossene Störungskarte sichern: Beginn und Dauer, konkretes Fehlerbild oder Meldung, betroffene Komponente, letzter erfolgreicher Versand, technische Ursache soweit feststellbar, laienverständlich beschriebene Abhilfemaßnahmen, Ergebnis jedes Versuchs und Belege. `Internet-/Routerstörung` allein genügt nicht. Die vorübergehende technische Unmöglichkeit und die Glaubhaftmachung gehören grundsätzlich in die Ersatzeinreichung; eine Nachholung ist nur in enger Ausnahme unverzüglich zulässig. Sofort an die verantwortliche anwaltliche Person übergeben.

### 8. Vier-Augen-Preflight und Übergabe

1. Manifest gegen Dateisystem prüfen: Reihenfolge, Dateiname, Anlage, Seitenzahl, Dateigröße, Hash, OCR, Kennzeichnung und Datenschutzstatus.
2. Hauptschriftsatz und jede Anlage öffnen und erste sowie letzte Seite kontrollieren; bei kritischen Tabellen oder Scans jede Seite sichten.
3. Antrag, Betrag, Zinsen, Partei, Gericht, Frist, Anlagenzitate und Anlagenverzeichnis ein letztes Mal gegeneinander abgleichen.
4. Versandauftrag an die tatsächlich verantwortende Person ausgeben: Einreichungsrolle, Weg, Postfach oder schriftliche Einreichungsart, Empfänger, Aktenzeichen, Betreff, Frist, Signaturmodell, Hauptdokument, Anlagenzahl, Gesamtgröße und Freigabestatus.
5. Erst nach realer Freigabe das Paket als `FREIGEGEBEN - ZUR UEBERMITTLUNG DURCH [NAME] AUF [WEG]` kennzeichnen. Die Kennzeichnung gehört in die interne Übergabekarte, nicht in den Schriftsatz.

### 9. Eingang und Nachlauf sichern

1. Automatisierte Eingangsbestätigung speichern und auf Gericht, Zeitstempel, Dateiliste und Fehlermeldung prüfen.
2. Gesendete Nachricht, Exportprotokoll, Prüfprotokoll, Hashmanifest und Eingangsbestätigung unveränderbar zur Akte nehmen.
3. Aktenzeichen, Gerichtskostenvorschuss, Zustellung und Wiedervorlage erfassen.
4. Bei Zahlung, Aufrechnung, Einrede, Unmöglichkeit oder Wegfall des Rechtsschutzbedürfnisses vor Zustellung nicht automatisch zurücknehmen oder erledigen. Kostenpfad über Skills `11`, `37` und `38` prüfen.

## Quellenpflicht

Es gelten `references/erv-dokumentenproduktion.md`, `references/rechtsstand-2026-verfahren-vollstreckung.md`, `references/zitierweise.md` und `references/rechtsprechungsradar-mietrecht-2021-2026.md`. Tragende Regeln werden in aktueller amtlicher Quelle live verifiziert. Kernanker sind BGH, Beschluss vom 02.12.2025 - VIII ZB 17/25, BGH, Urteil vom 11.10.2024 - V ZR 261/23, BGH, Beschluss vom 07.05.2024 - VI ZB 22/23, BGH, Beschluss vom 28.02.2024 - IX ZB 30/23 und BVerfG, Beschluss vom 16.02.2023 - 1 BvR 1881/21. Keine erfundenen Aktenzeichen, keine Kanzleiveröffentlichung als Primärbeleg.

## Ausgabeformat

1. Paketkopf mit Status und Frist.
2. Gerichtsfertiger, vollständig ausformulierter Schriftsatz.
3. Einzelne, sinnvoll benannte PDF-Arbeitskopien der Anlagen.
4. Anlagenverzeichnis und technisches Manifest mit Hash, Seitenzahl und Status.
5. ERV-/Signatur-/Freigabe-Preflight mit Ampel.
6. Versandauftrag für die verantwortende Person mit belegtem Einreichungsweg.
7. Nach Einreichung: Eingangs- und Aktenvermerk mit Wiedervorlage.

Das Endprodukt wird in vollständigen Sätzen geliefert. Skelette, Halbsätze, ungeprüfte Platzhalterdateien und bloße Dateilisten sind kein fertiges Versandpaket.

## Beispiele

- Neue Zahlungsklage: `01_K_Klage_Mietrueckstand.pdf`, danach Anlagen K 1 bis K 6 als Einzel-PDFs, Anlagenverzeichnis, Manifest und Freigabekarte.
- Eigenvertretung der Konzerngesellschaft am Amtsgericht: Beschäftigtenstatus und Vollmacht sind belegt; das tatsächlich eingerichtete eBO wird mit Postfachinhaber, verantwortender Person, Signaturmodell und Eingangsbestätigung dokumentiert.
- Zahlungsklage der privaten Konzerngesellschaft im Bezirk des Amtsgerichts Schöneberg: Online-Verfahren nur nach positivem Rollencheck des aktuellen amtlichen Eingabedienstes; sonst reguläres eBO- oder Schriftpaket ohne falsche Online-Kennzeichnung.
- Replik: bereits eingereichte K 1 bis K 6 bleiben bestehen; neue Mietkontoauswertung und Zustellnachweis werden K 7 und K 8.
- Fehlender Mietvertrag: gelbe Beschaffungslücke; kein leeres `Anlage_K01.pdf`, keine Einreichungsfreigabe.
- Einfache Signatur durch Anwältin A, geplanter Versand aus dem beA von Anwalt B: rote Ampel; Signatur- und Versandidentität klären oder qualifizierte elektronische Signatur anwenden.
- Fristablauf mit vermutetem Routerfehler: keine pauschale Ersatzeinreichung; geschlossene Störungskarte und Glaubhaftmachungsentwurf sofort an die verantwortliche anwaltliche Person.
