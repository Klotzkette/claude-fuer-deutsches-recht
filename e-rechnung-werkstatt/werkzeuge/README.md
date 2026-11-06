# E-Rechnungen lokal erzeugen und prüfen

Der Helfer erzeugt aus einem fachlich geprüften Rechnungsstand eine XRechnung als UBL-XML und eine ZUGFeRD-Hybriddatei. Das PDF wird aus denselben Daten aufgebaut; eine eingereichte Ausgangs-PDF wird weder umetikettiert noch blind eingebettet. Die Eingabedateien werden vom Host zunächst gelesen und abgeglichen. Der Helfer ist kein autonomer OCR- oder Steuerklassifizierungsdienst.

## 1 Unterstützter Fall

Der ausführbare Weg unterstützt inländische Aussteller und Empfänger, EUR, Rechnungstyp 380, positive Positionen mit 7 oder 19 Prozent Umsatzsteuer und Überweisungscode 58 auf eine deutsche IBAN. Beide Steuersätze können in derselben Rechnung vorkommen. Die einzelnen Positionen werden kaufmännisch auf Cent gerundet; die Umsatzsteuer wird je Steuersatz auf dessen gesamte Bemessungsgrundlage gerechnet. Die ausdrücklich bestätigten Gesamtsummen müssen damit übereinstimmen.

Steuerfreie Leistungen, Kleinunternehmer, Reverse Charge, Nullsteuersatz, Auslandsfälle, kaufmännische Gutschriften, Selbstfakturierung, Rabatte, Zuschläge, Abschläge und Vorschussverrechnung werden von diesem Helfer abgewiesen. Solche Fälle werden im Werkstattablauf mit einer dafür geeigneten Faktura-Anwendung erstellt und anschließend fallbezogen geprüft. Ein unbekanntes JSON-Feld wird nicht stillschweigend weggelassen.

## 2 Laufzeit einrichten

Benötigt werden Python ab 3.10, das Python-Paket `pypdf` und Java ab 11. Werkzeuge und Standards sind auf Mustangproject 2.26.0 sowie KoSIT Validator 1.6.3 mit XRechnung-Konfiguration vom 31. August 2026 festgelegt. Der Stand der Standards ist vor einem späteren Einsatz erneut zu prüfen.

```bash
python3 -m pip install 'pypdf>=6,<7'
python3 werkzeuge/runtime_einrichten.py --out /absoluter/pfad/e-rechnung-runtime
```

Der Einrichtungsaufruf lädt ausschließlich öffentlich zugängliche Werkzeugdateien über HTTPS. Er prüft die veröffentlichten und im `runtime-lock.json` festgelegten SHA-256-Werte des Mustang-JAR und des amtlichen KoSIT-Bundles, der inneren Archive und aller extrahierten KoSIT-Dateien. Das Ziel muss neu sein. Rechnungen, Zertifikate oder Zugangsdaten werden hierbei nicht übermittelt.

Der eigentliche Rechnungslauf verwendet die lokalen Werkzeuge. Die 59 beziehungsweise 63 MB großen Fremdwerkzeuge sind nicht im Plugin-ZIP enthalten. Die Lizenzen und Herkunftsnachweise der Fremdkomponenten werden durch deren originale JAR-Dateien und das originale amtliche Paket mitgeführt. Es werden keine fremden Fonts umbenannt.

## 3 Geprüfte Eingabe

Das vollständige Eingabebeispiel steht unter `../beispiele/rechnungsdaten.json`. Dort sind jede Rechnungsposition, beide Parteien, Rechnungsausstellung, Zahlungsziel, Leistungszeitraum, das gesondert bestätigte Liefer-/Leistungsabschlussdatum, Käuferreferenz, Zahlungsdaten und bestätigte Summen ausformuliert.

`sources` enthält zu jeder Originaldatei eine eindeutige ID, einen Pfad innerhalb des freigegebenen Quellenordners und den SHA-256 der tatsächlich gelesenen Bytes. `evidence` ordnet jedes fachliche Datenfeld einem Quellenbeleg und einer präzisen Fundstelle zu. Dazu gehören insbesondere Name, Steuerkennung, IBAN, Datum, Einheit, Menge und Steuersatz. Der Helfer bestätigt damit die technische Vollständigkeit der Belegzuordnung; die tatsächliche Aussage des Belegs und die steuerliche Beurteilung bleiben fachlich zu prüfen. `reviewed=true` wird erst nach dieser Prüfung gesetzt.

Datumswerte verwenden `YYYY-MM-DD`, Dezimalwerte Zeichenketten mit Punkt. `invoice_type` ist `380`, `currency` ist `EUR`. Die Käuferreferenz wird vom Empfänger übernommen und ist nicht automatisch eine Leitweg-ID. Ein Liefer-/Leistungsabschlussdatum wird nicht aus dem Ende des Leistungszeitraums abgeleitet. Fehlende tatsächliche Angaben werden vor der Erzeugung ergänzt.

## 4 Ausführen

Vom Plugin-Verzeichnis aus:

```bash
python3 werkzeuge/erechnung.py create \
  --input beispiele/rechnungsdaten.json \
  --out /absoluter/pfad/neue-rechnungsausgabe \
  --format both \
  --mustang-jar /absoluter/pfad/e-rechnung-runtime/Mustang-CLI-2.26.0.jar \
  --kosit-home /absoluter/pfad/e-rechnung-runtime/kosit \
  --java /absoluter/pfad/zur/java-laufzeit/bin/java
```

`--format xrechnung` beziehungsweise `--format zugferd` wählt eine einzelne Ausgabe. `--source-root` setzt bei Bedarf den ausdrücklich freigegebenen Quellenordner; andernfalls gilt der Ordner der JSON-Eingabedatei. Quelldateien außerhalb dieses Ordners werden abgewiesen. Vorhandene Ausgabeordner werden nicht verändert.

## 5 Ausgabe und Prüfgrenzen

`XRechnung.xml` wird mit dem aktuellen amtlichen KoSIT-Bestand gegen Schema und Geschäftsregeln geprüft. Ein positiver Rückgabecode allein genügt nicht: Der Prüfbericht muss sämtliche Schritte als gültig und die abschließende Bewertung als Annahme ausweisen.

`factur-x.xml` verwendet das EN16931-Profil von ZUGFeRD 2.5.2 beziehungsweise Factur-X 1.09.2. `ZUGFeRD.pdf` enthält exakt diese XML-Bytes. Der positive Mustang-Bericht muss die XML-Prüfung und die tatsächliche veraPDF-Konformität für PDF/A-3 nachweisen. Ein gültiger Gesamtstatus mit PDF/A-Warnung wird abgewiesen. Das zusätzliche Mustang-Profilmerkmal BR-DE-21 weist bei einer EN16931-Rechnung lediglich auf die abweichende XRechnung-Profilkennung hin; dieser einzelne Hinweis bleibt im Originalbericht dokumentiert. Andere Warnungen oder ungeklärte Hinweise verhindern die automatische Freigabe.

Die technische Rechnungstabellenansicht verwendet eingebettete Source-Sans-Pro-Schriften aus Mustang statt der Grundschrift juristischer Schriftsätze. Dieses Rechnungshausformat gewährleistet die lokal geprüfte Schrifteinbettung; es betrifft weder Briefe noch Schriftsätze. Alle Einzelpreise behalten ihre bestätigte Genauigkeit; Steuersummen werden nach dem numerischen Steuersatz gruppiert. Hinweise des Renderers auf Überlauf, fehlende Zeichen oder ersetzte Schriften verhindern die Freigabe.

`Pruefbericht.json` verbindet den ursprünglichen Eingabehash, Generator-, Layout- und Laufzeitsperrdateihash, Quellenbestand und Ausgabeprüfsummen. Die erzeugten Dateien werden erst nach erfolgreicher Prüfung gemeinsam in das neue Zielverzeichnis verschoben. Bei einem Fehler bleibt ausschließlich ein ausdrücklich als nicht freigegeben markiertes Zwischenverzeichnis mit Diagnostik erhalten. Eine während der Erstellung veränderte Eingabe oder Werkzeugdatei verhindert die Freigabe.

Der Status `generated_and_validated_not_sent` bedeutet lokale Erzeugung und Formatprüfung. Er bestätigt weder die steuerliche Richtigkeit durch das Werkzeug noch eine Annahme durch das Empfängerportal oder einen Versand. Für eine ausdrücklich beauftragte Einreichung sind Empfängervorgaben, Übermittlungsweg und Eingangsbestätigung gesondert zu prüfen.

## 6 Regressionen

```bash
python3 scripts/test-e-rechnung-werkstatt.py
```

Dieses Repository-Kommando prüft Eingabegrenzen, Summen, Quellenzuordnung, doppelte JSON-Schlüssel, unveränderte Ausgaben und PDF/A-Warnungen. Der echte Integrationstest wird nur mit lokal eingerichteten Laufzeiten ausgeführt:

```bash
E_RECHNUNG_MUSTANG_JAR=/absolut/Mustang-CLI-2.26.0.jar \
E_RECHNUNG_KOSIT_HOME=/absolut/kosit \
E_RECHNUNG_JAVA=/absolut/bin/java \
python3 scripts/test-e-rechnung-werkstatt.py
```

Der Integrationstest erzeugt beide Formate tatsächlich und manipuliert anschließend unabhängig die XML-Zahlsumme und die PDF/A-Metadaten. Beide fehlerhaften Dateien müssen durch die echten Prüfwerkzeuge beziehungsweise den strikten Freigabeguard zurückgewiesen werden. Ein übersprungener Integrationstest ist kein bestandener Integrationstest.
