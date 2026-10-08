# 1. Mandatslauf und Freigabestufen: die agentische Schicht der KI-nativen Kanzlei

## 1.1. Zweck

Die achtzehn Skills erzeugen Produkte. Der Mandatslauf verbindet sie zu einem durchlaufenden Vorgang, in dem jederzeit erkennbar ist, in welcher Phase ein Mandat steht, welche führende Fassung gilt, welche Freigabe noch fehlt und welcher Skill als Nächstes greift. Er ist die Voraussetzung dafür, dass eine Kanzlei das Plugin agentisch einsetzen kann: Die Maschine arbeitet selbständig innerhalb der freigegebenen Stufe weiter, und jede Handlung mit Außenwirkung bleibt an eine namentlich dokumentierte menschliche Freigabe gebunden. Der Lauf ersetzt weder die anwaltliche Verantwortung noch die fachliche Prüfung des Produkts; er macht beides nachvollziehbar.

Der optionale Helfer `../scripts/mandatslauf.py` führt den Lauf als Datei `00_Mandat/mandatslauf.json` im Mandatsordner. Ohne Dateizugriff wird derselbe Stand als Textblock im Übergabevermerk geführt. Ein Mandatslauf ohne Datei ist zulässig; ein Mandatslauf, der behauptet, eine Freigabe liege vor, obwohl niemand sie erteilt hat, ist es nicht.

## 1.2. Phasen

Ein Mandat durchläuft höchstens zehn Phasen, nicht zwingend in dieser Reihenfolge und nicht zwingend alle: `eingang`, `annahme`, `akte`, `frist`, `sacharbeit`, `kommunikation`, `versandvorbereitung`, `abrechnung`, `zahlung`, `abschluss`. Ein Zeiteintrag in einer laufenden Akte verändert die Phase nicht. Ein neuer Fristauslöser setzt die Phase `frist` neben die laufende Sacharbeit; der Lauf hält deshalb neben der Hauptphase eine Liste offener Nebenläufe. Jede Phase hat einen führenden Skill, der sie verantwortet, und ein Produkt, mit dem sie endet:

| Phase | Führender Skill | Produkt, mit dem die Phase endet |
| --- | --- | --- |
| eingang | ki-kanzlei-steuern | Zugeordneter Auftrag mit erkannter Startsituation |
| annahme | mandatsannahme-interessenkollision | Annahme, begrenzte Beauftragung oder Absage |
| akte | akte-fristen-anlegen | Mandatsstamm, Dokumentregister, erfasste Fristobjekte |
| frist | fristen-berechnen-ueberwachen | Rechenvermerk mit Status „berechnet, zur Eintragung übergeben“ |
| sacharbeit | recht-recherchieren, schriftsaetze-entwerfen, vertraege-agb-pruefen, vertraege-gestalten | Führende Fassung des bestellten Fachprodukts |
| kommunikation | mandantenkommunikation | Versandfertiger Brief oder Entscheidungsvorlage |
| versandvorbereitung | bea-anlagen-vorbereiten | Versandpaket mit Manifest, Status „vorbereitet, nicht eingereicht“ |
| abrechnung | zeiten-erfassen, honorar-budget-vereinbaren, abrechnung-e-rechnung | Rechnungsentwurf oder freigegebene Rechnung |
| zahlung | zahlungen-buchhaltung | Zahlungsklärung und Buchungsvorschlag |
| abschluss | mandat-abschliessen | Abschlussbrief, Aufbewahrungs- und Löschvermerk |

Die Querschnittsskills `anwaltsberufsrecht-pruefen`, `geldwaesche-pruefen` und `workflow-uebergabe` haben keine eigene Phase. Sie werden anlassbezogen eingeschoben und tragen ihr Ergebnis als Nebenlauf in den Mandatslauf ein.

## 1.3. Freigabestufen

Die Kanzlei legt je Mandat eine Freigabestufe fest. Sie bestimmt, was die Maschine ohne Rückfrage tun darf. Höhere Stufen schließen die niedrigeren ein. Keine Stufe erlaubt eine Handlung mit Außenwirkung ohne das zugehörige Freigabegate.

| Stufe | Bezeichnung | Erlaubt ohne Rückfrage |
| --- | --- | --- |
| 0 | Nur Entwurf | Lesen der Akte, Entwürfe als Text liefern; keine Datei im Mandatsordner schreiben |
| 1 | Interne Dateiarbeit | Arbeitsprodukte unter `01_Bearbeitung` anlegen und fortschreiben, Dokumentregister führen, Originale unverändert kopieren |
| 2 | Journal und Register | Bestätigte Zeiten, Honorarabschnitte, Auslagen und belegte Zahlungen intern erfassen; Rechnungsentwurf fortschreiben, Fristobjekte und Rechenvermerke führen, Mandatslauf aktualisieren |
| 3 | Versandvorbereitung | Ausgabefertige Versand- und Rechnungspakete einschließlich XML vorbereiten; menschliche Ausgabeentscheidung bleibt erforderlich |

Interne Übergabevermerke und das Anstoßen eines Nachbarskills sind schon auf der für dessen Arbeit ausreichenden Stufe zulässig. Die Stufen sind ein vereinbarter Arbeitsumfang, keine gesetzliche Erlaubnis und keine technische Zugriffssperre des Helfers. Stufe 3 ist die Obergrenze der internen Arbeitstiefe. Keine Stufe erteilt eine pauschale Vollmacht für Einreichung, Versand, Auszahlung, Rechnungsausgabe, Kalenderbestätigung, Meldung oder Löschung. Diese Handlungen bleiben Freigabegates. Ein zusätzlich ausdrücklich beauftragter Computerlauf kann nach konkreter menschlicher Entscheidung die zulässigen delegierbaren Schritte ausführen; erforderliche persönliche Schlussakte und die Nachweiskontrolle bleiben bestehen (Abschnitt 1.13).

## 1.4. Freigabegates

Jedes Gate hat eine Kennung, einen Auslöser, einen zuständigen Skill und eine Person, die freigibt. Eine Freigabe wird mit Name, Zeitpunkt und Bezug (etwa Dateiname und Hash der freigegebenen Fassung) dokumentiert. Die Maschine darf ein Gate öffnen und das Produkt dafür vorbereiten; sie darf es nicht selbst freigeben. Ein Gate kann als „nicht erforderlich“ geschlossen werden, wenn der Sachverhalt es nicht auslöst; auch das wird mit Grund dokumentiert.

| Gate | Auslöser | Was die Freigabe bedeutet |
| --- | --- | --- |
| G1 Annahme | Neue Anfrage, neuer Gegner, Auftragserweiterung | Mandat, Umfang und Honorargrundlage sind von einem Berufsträger bestätigt |
| G2 Fristeintrag | Rechenvermerk liegt vor | Die Frist ist im führenden Kalender eingetragen und rückgelesen; Vorfrist und Verantwortliche stehen fest |
| G3 Versand und Einreichung | Versandpaket oder Brief ist vorbereitet | Ein Berufsträger hat Fassung, Anlagen und Empfänger geprüft und den Versand angeordnet; der Eingangsbeleg wird nachgetragen |
| G4 Rechnungsausgabe | Rechnungsentwurf ist fachlich geprüft | Nummer, Mitteilung und Fälligkeit sind von der Kanzlei verantwortet |
| G5 Zahlung und Fremdgeld | Auszahlung, Verrechnung oder Weiterleitung steht an | Die Kanzlei hat die Zahlungsanweisung erteilt; Fremdgeld bleibt getrennt |
| G6 Dienstleister | Daten sollen einen externen Dienst oder KI-Dienst erreichen | Erforderlichkeit, Vertrag nach § 43e BRAO, Datenschutz sowie eine im konkreten Fall erforderliche Einwilligung sind geprüft und dokumentiert |
| G7 Meldung | Verdachtsmoment nach GwG oder Haftungsfall | Ein Berufsträger hat über Meldung oder Anzeige entschieden; keine automatische Abgabe |
| G8 Abschluss und Löschung | Mandatsende | Restfristen, Fremdgeld, Herausgabe und Aufbewahrung sind entschieden; die Löschung ist je Dokumentart angeordnet |

## 1.5. Führende Fassung und Produktregister

Jedes Produkt erhält im Mandatslauf eine Kennung, einen Pfad, den Hash der Datei, den erzeugenden Skill und einen Zustand: `entwurf`, `geprueft` oder `freigegeben`. Nur eine Fassung je Produkt ist führend. Eine neue Fassung ersetzt die alte im Register; `product_history` bewahrt die früheren Einträge. Die alten Dateien sind zusätzlich unverändert aufzubewahren. Der Helfer erzeugt keine Dateisicherung und kein manipulationssicheres Archiv. Ein Skill, der ein Produkt eines anderen Skills verändert, trägt die neue Fassung mit seinem Namen ein. Ein Übergabevermerk nennt die führenden Fassungen mit Hash; ein Rücklauf wird gegen diesen Hash geprüft.

## 1.6. Nächster Schritt

Der nächste Schritt ergibt sich aus Phase, offenen Gates und offenen Fragen, nicht aus der Reihenfolge der Skillliste. Die Regel lautet: Zuerst das offene Gate mit der frühesten Fristwirkung, dann die Phase, in der das bestellte Produkt entsteht, dann der Honorar- und Zeitanschluss. Ein offenes Gate G2 wird vorrangig bearbeitet, solange die Frist nicht gesichert ist; unabhängige interne Sacharbeit darf parallel weiterlaufen. Ein offenes Gate G1 blockiert nicht die interne Vorbereitung, aber jede Außenwirkung. Der Helfer priorisiert offene G2, danach andere Gates in Kennungsreihenfolge. Er berechnet keine zeitliche Dringlichkeit aus Kalenderdaten. Die fachliche Sortierung nach tatsächlichem Fristende erfolgt zusätzlich anhand der Fristobjekte. `next` nennt Skill, gebundenes Produkt und zuständige Person, soweit diese erfasst sind; fehlende Werte bleiben offen.

## 1.7. Aufruf des Helfers

Python 3.10 oder neuer, nur Standardbibliothek. Der Mandatslauf verwendet benannte Optionen; das Honorarjournal liest Eingaben aus UTF-8-JSON. Bei einem Werkzeugaufruf Argumentlisten verwenden; frei eingegebene Mandatsdaten niemals ungeprüft in ausführbaren Shelltext einsetzen.

```bash
python3 "<Pluginordner>/scripts/mandatslauf.py" init --akte "/Mandate/M-26-104" --matter-id "M-26-104" --stufe 2
python3 "<Pluginordner>/scripts/mandatslauf.py" phase --akte "/Mandate/M-26-104" --phase sacharbeit --grund "Klageentwurf bestellt"
python3 "<Pluginordner>/scripts/mandatslauf.py" product --akte "/Mandate/M-26-104" --id klage --pfad "01_Bearbeitung/Klage_v04.docx" --skill schriftsaetze-entwerfen --zustand entwurf
python3 "<Pluginordner>/scripts/mandatslauf.py" gate --akte "/Mandate/M-26-104" --gate G3 --aktion oeffnen --person "RAin Dr. Ahrens" --bezug klage
python3 "<Pluginordner>/scripts/mandatslauf.py" status --akte "/Mandate/M-26-104"
python3 "<Pluginordner>/scripts/mandatslauf.py" next --akte "/Mandate/M-26-104"
python3 "<Pluginordner>/scripts/mandatslauf.py" cockpit --kanzlei "/Mandate" --format md
```

`gate ... --aktion oeffnen --person` dokumentiert nur die zuständige Person, keine Freigabe. Erst wenn diese Person die konkrete Entscheidung tatsächlich erklärt hat, darf `gate --akte "<Akte>" --gate G3 --aktion freigeben --person "<bestätigter Name>" --bezug klage` diese Erklärung dokumentieren. Der Platzhalter ist keine erteilte Zustimmung. `freigeben` verlangt eine namentlich bezeichnete Person; Bezeichnungen wie „KI“, „Agent“, „System“ oder „automatisch“ werden abgewiesen. `init` verweigert das Überschreiben eines vorhandenen Laufs. Jede Änderung erhöht die Revision und wird in der Historie mit Zeitstempel festgehalten; die Datei wird atomar geschrieben. `cockpit` liest alle Mandatsläufe unterhalb eines Kanzleiordners und gruppiert sie nach offenen Gates und Fragen; das ist die Grundlage des Tagesstarts in der [Kanzleialltag-Referenz](kanzleialltag-workflows.md). Der Helfer schreibt keinen Kalender, versendet nichts und bucht nichts; er dokumentiert.

## 1.8. Was agentisch bedeutet und was nicht

Agentisch heißt: Die Maschine liest den Mandatslauf, erkennt die Phase und das nächste Produkt, erzeugt es innerhalb der Freigabestufe, trägt die führende Fassung ein, öffnet das nötige Gate und stößt den Nachbarskill an, ohne dass der Nutzer die Reihenfolge diktieren muss. Sie meldet den Stand mit Dateilinks, offenen Gates und Honorar- und Zeitstand. Nicht agentisch heißt: Sie erfindet keine Freigabe, keine Zeit, keinen Zugang, keinen Kalendereintrag und keinen Eingangsbeleg, sie bleibt bei einer offenen Entscheidung stehen, wenn ohne sie kein sinnvoller Fortschritt möglich ist, und sie wechselt nicht von selbst in ein Gerichtsverfahren, wenn nur ein Gutachten bestellt ist. Die Kanzlei erweitert die Freigabestufe erst, wenn die Protokolle der niedrigeren Stufe sie überzeugt haben.

## 1.9. Zuordnung der Skills zu Phasen und Gates

Die Tabelle benennt die einheitlichen Produktkennungen. Wird `--bezug` beim Öffnen eines Gates auf eine bereits registrierte Produktkennung gesetzt, bindet der Helfer das Gate an deren Hash und erzeugenden Skill. So führt G3 für `mandantenbrief` zur Kommunikation und für `versandpaket` zur beA-Vorbereitung. Ein freier Vorgangsbezug ohne registriertes Produkt bleibt zulässig; dann gilt die Standardzuordnung des Gates, und die Fassung muss gesondert kontrolliert werden. Eine solche freie Angabe bewirkt keine technische Hashbindung.

| Skill | Phase | Gates | Produktkennung |
| --- | --- | --- | --- |
| ki-kanzlei-steuern | eingang | G1; Zusammenführung | auftrag |
| mandatsannahme-interessenkollision | annahme | G1; G6 bei Dienstleister | annahme |
| akte-fristen-anlegen | akte | G2; G6 bei Dienstleister | mandatsstamm, dokumentregister, fristenliste |
| fristen-berechnen-ueberwachen | frist, auch Nebenlauf | G2 | rechenvermerk-<id>, fristenliste |
| anwaltsberufsrecht-pruefen | Anlassphase, Querschnitt | G1, G6; G7 bei Haftungsfall | berufsrechtsvermerk |
| geldwaesche-pruefen | annahme, Querschnitt | G1, G7 | geldwaeschevermerk |
| honorar-budget-vereinbaren | abrechnung, auch Nebenlauf | G1 bei Nachtrag | honorarstand |
| zeiten-erfassen | abrechnung, auch Nebenlauf | Zeitstand für G4 | zeitstand |
| workflow-uebergabe | Querschnitt | G6 bei externem Dienst | uebergabevermerk |
| recht-recherchieren | sacharbeit | G6 vor externem Datenzugang | rechtsvermerk |
| schriftsaetze-entwerfen | sacharbeit | G3 bei Versand; G2 prüfen | klage oder konkrete Schriftsatzart, etwa einspruch |
| vertraege-agb-pruefen | sacharbeit | G3; G1 bei Mehrumfang | vertragspruefung |
| vertraege-gestalten | sacharbeit | G3; G1 bei Mehrumfang | vertrag |
| mandantenkommunikation | kommunikation | G3 | mandantenbrief |
| bea-anlagen-vorbereiten | versandvorbereitung | G3 | versandpaket |
| abrechnung-e-rechnung | abrechnung | G4 | rechnung, rechnung-xml |
| zahlungen-buchhaltung | zahlung | G5 | zahlungsstand |
| mandat-abschliessen | abschluss vorbereiten | G3, G8; G4/G5 klären | abschlussbrief, aufbewahrungsvermerk |

## 1.10. Übergaben mit Rückgabe

Alle Empfänger übernehmen Pfad und Hash der führenden Fassung, Belegstand, offene Fragen sowie Honorar- und Zeitstand. Sie erfragen nur neue oder widersprüchliche Angaben. Die Rückgabe aktualisiert den Mandatslauf; sie überträgt keine Freigabe auf geänderte Dateien.

| Abgebender Skill | Empfangender Skill | Übergebenes Produkt und Anlass | Rückgabe |
| --- | --- | --- | --- |
| `abrechnung-e-rechnung` | `zahlungen-buchhaltung` | `rechnung, gegebenenfalls rechnung-xml`; Rechnung, Zahlungsbeleg, Zweck und Berechtigte | `zahlungsstand`; belegte Zuordnung; Auszahlung erst nach G5 und Vollzug |
| `abrechnung-e-rechnung` | `mandantenkommunikation` | `rechnung, gegebenenfalls rechnung-xml`; Empfänger, Ergebnis, Friststatus und Entscheidungsbedarf | `mandantenbrief`; Briefentwurf; Entscheidung erst nach echter Antwort |
| `abrechnung-e-rechnung` | `mandat-abschliessen` | `rechnung, gegebenenfalls rechnung-xml`; Beendigungsgrund, Restpflichten und führende Register | `abschlussbrief, aufbewahrungsvermerk`; Abschlussprodukte; Freigaben und Vollzug gesondert |
| `abrechnung-e-rechnung` | `workflow-uebergabe` | `rechnung, gegebenenfalls rechnung-xml`; Empfänger, Aufgabe, Fassung und Übernahmebedarf | `uebergabevermerk`; kontrollierte Fassung; Übernahme nur mit Bestätigung |
| `abrechnung-e-rechnung` | `honorar-budget-vereinbaren` | `rechnung, gegebenenfalls rechnung-xml`; Umfang, Vereinbarung und Kostenänderung | `honorarstand`; bestätigte Grundlage oder offener Nachtrag |
| `abrechnung-e-rechnung` | `fristen-berechnen-ueberwachen` | `rechnung, gegebenenfalls rechnung-xml`; Fristobjekt, Originalauslöser, Beleg und Rechtsregime | `rechenvermerk-<id>`; berechneter Vermerk; Eintragung und Rücklesung gesondert |
| `akte-fristen-anlegen` | `fristen-berechnen-ueberwachen` | `dokumentregister, fristenliste`; Fristobjekt, Originalauslöser, Beleg und Rechtsregime | `rechenvermerk-<id>`; berechneter Vermerk; Eintragung und Rücklesung gesondert |
| `akte-fristen-anlegen` | `mandatsannahme-interessenkollision` | `dokumentregister, fristenliste`; Beteiligte, Auftrag und Konfliktanlass | `annahme`; Annahme/Begrenzung/Absage; G1-Stand |
| `akte-fristen-anlegen` | `bea-anlagen-vorbereiten` | `dokumentregister, fristenliste`; geprüfter Schriftsatz, Anlagenzuordnung, Frist, Empfänger | `versandpaket`; Manifest/Preflight; Eingang erst nach tatsächlichem Versand |
| `akte-fristen-anlegen` | `workflow-uebergabe` | `dokumentregister, fristenliste`; Empfänger, Aufgabe, Fassung und Übernahmebedarf | `uebergabevermerk`; kontrollierte Fassung; Übernahme nur mit Bestätigung |
| `akte-fristen-anlegen` | `mandat-abschliessen` | `dokumentregister, fristenliste`; Beendigungsgrund, Restpflichten und führende Register | `abschlussbrief, aufbewahrungsvermerk`; Abschlussprodukte; Freigaben und Vollzug gesondert |
| `akte-fristen-anlegen` | `anwaltsberufsrecht-pruefen` | `dokumentregister, fristenliste`; konkrete Handlung und Befugnisfrage | `berufsrechtsvermerk`; rechtliche Bewertung; menschliche Freigabe gesondert |
| `akte-fristen-anlegen` | `ki-kanzlei-steuern` | `dokumentregister, fristenliste`; aktueller Fachstand und nächster Entscheidungsbedarf | `auftrag`; nächster Skill, Produkt und verantwortliche Person |
| `anwaltsberufsrecht-pruefen` | `mandatsannahme-interessenkollision` | `berufsrechtsvermerk`; Beteiligte, Auftrag und Konfliktanlass | `annahme`; Annahme/Begrenzung/Absage; G1-Stand |
| `anwaltsberufsrecht-pruefen` | `geldwaesche-pruefen` | `berufsrechtsvermerk`; Katalogtätigkeit, Zahlungs- oder Risikobefund | `geldwaeschevermerk`; Anwendbarkeit und Nachweise; Meldefrage geschützt |
| `anwaltsberufsrecht-pruefen` | `zahlungen-buchhaltung` | `berufsrechtsvermerk`; Rechnung, Zahlungsbeleg, Zweck und Berechtigte | `zahlungsstand`; belegte Zuordnung; Auszahlung erst nach G5 und Vollzug |
| `anwaltsberufsrecht-pruefen` | `honorar-budget-vereinbaren` | `berufsrechtsvermerk`; Umfang, Vereinbarung und Kostenänderung | `honorarstand`; bestätigte Grundlage oder offener Nachtrag |
| `anwaltsberufsrecht-pruefen` | `mandat-abschliessen` | `berufsrechtsvermerk`; Beendigungsgrund, Restpflichten und führende Register | `abschlussbrief, aufbewahrungsvermerk`; Abschlussprodukte; Freigaben und Vollzug gesondert |
| `anwaltsberufsrecht-pruefen` | `mandantenkommunikation` | `berufsrechtsvermerk`; Empfänger, Ergebnis, Friststatus und Entscheidungsbedarf | `mandantenbrief`; Briefentwurf; Entscheidung erst nach echter Antwort |
| `bea-anlagen-vorbereiten` | `schriftsaetze-entwerfen` | `versandpaket`; Prozesslage, Belege, Form und Antragsziel | `konkrete Schriftsatzart, etwa klage oder einspruch`; ausformulierter Entwurf und Anlagenmatrix |
| `bea-anlagen-vorbereiten` | `workflow-uebergabe` | `versandpaket`; Empfänger, Aufgabe, Fassung und Übernahmebedarf | `uebergabevermerk`; kontrollierte Fassung; Übernahme nur mit Bestätigung |
| `bea-anlagen-vorbereiten` | `fristen-berechnen-ueberwachen` | `versandpaket`; Fristobjekt, Originalauslöser, Beleg und Rechtsregime | `rechenvermerk-<id>`; berechneter Vermerk; Eintragung und Rücklesung gesondert |
| `bea-anlagen-vorbereiten` | `zeiten-erfassen` | `versandpaket`; tatsächliche Minuten oder offene Zeitfrage | `zeitstand`; Journal-ID, offene Minuten und Entwurfswirkung |
| `bea-anlagen-vorbereiten` | `mandantenkommunikation` | `versandpaket`; Empfänger, Ergebnis, Friststatus und Entscheidungsbedarf | `mandantenbrief`; Briefentwurf; Entscheidung erst nach echter Antwort |
| `fristen-berechnen-ueberwachen` | `akte-fristen-anlegen` | `rechenvermerk-<id>`; Stammdaten, Dokument- oder Fristobjekt | `dokumentregister, fristenliste`; Register aktualisiert; Eintrag nur mit Rücklesebeleg |
| `fristen-berechnen-ueberwachen` | `schriftsaetze-entwerfen` | `rechenvermerk-<id>`; Prozesslage, Belege, Form und Antragsziel | `konkrete Schriftsatzart, etwa klage oder einspruch`; ausformulierter Entwurf und Anlagenmatrix |
| `fristen-berechnen-ueberwachen` | `bea-anlagen-vorbereiten` | `rechenvermerk-<id>`; geprüfter Schriftsatz, Anlagenzuordnung, Frist, Empfänger | `versandpaket`; Manifest/Preflight; Eingang erst nach tatsächlichem Versand |
| `fristen-berechnen-ueberwachen` | `mandantenkommunikation` | `rechenvermerk-<id>`; Empfänger, Ergebnis, Friststatus und Entscheidungsbedarf | `mandantenbrief`; Briefentwurf; Entscheidung erst nach echter Antwort |
| `fristen-berechnen-ueberwachen` | `anwaltsberufsrecht-pruefen` | `rechenvermerk-<id>`; konkrete Handlung und Befugnisfrage | `berufsrechtsvermerk`; rechtliche Bewertung; menschliche Freigabe gesondert |
| `fristen-berechnen-ueberwachen` | `zeiten-erfassen` | `rechenvermerk-<id>`; tatsächliche Minuten oder offene Zeitfrage | `zeitstand`; Journal-ID, offene Minuten und Entwurfswirkung |
| `fristen-berechnen-ueberwachen` | `mandat-abschliessen` | `rechenvermerk-<id>`; Beendigungsgrund, Restpflichten und führende Register | `abschlussbrief, aufbewahrungsvermerk`; Abschlussprodukte; Freigaben und Vollzug gesondert |
| `geldwaesche-pruefen` | `mandatsannahme-interessenkollision` | `geldwaeschevermerk`; Beteiligte, Auftrag und Konfliktanlass | `annahme`; Annahme/Begrenzung/Absage; G1-Stand |
| `geldwaesche-pruefen` | `mandantenkommunikation` | `geldwaeschevermerk`; Empfänger, Ergebnis, Friststatus und Entscheidungsbedarf | `mandantenbrief`; Briefentwurf; Entscheidung erst nach echter Antwort |
| `geldwaesche-pruefen` | `zahlungen-buchhaltung` | `geldwaeschevermerk`; Rechnung, Zahlungsbeleg, Zweck und Berechtigte | `zahlungsstand`; belegte Zuordnung; Auszahlung erst nach G5 und Vollzug |
| `geldwaesche-pruefen` | `anwaltsberufsrecht-pruefen` | `geldwaeschevermerk`; konkrete Handlung und Befugnisfrage | `berufsrechtsvermerk`; rechtliche Bewertung; menschliche Freigabe gesondert |
| `geldwaesche-pruefen` | `zeiten-erfassen` | `geldwaeschevermerk`; tatsächliche Minuten oder offene Zeitfrage | `zeitstand`; Journal-ID, offene Minuten und Entwurfswirkung |
| `geldwaesche-pruefen` | `fristen-berechnen-ueberwachen` | `geldwaeschevermerk`; Fristobjekt, Originalauslöser, Beleg und Rechtsregime | `rechenvermerk-<id>`; berechneter Vermerk; Eintragung und Rücklesung gesondert |
| `geldwaesche-pruefen` | `mandat-abschliessen` | `geldwaeschevermerk`; Beendigungsgrund, Restpflichten und führende Register | `abschlussbrief, aufbewahrungsvermerk`; Abschlussprodukte; Freigaben und Vollzug gesondert |
| `geldwaesche-pruefen` | `ki-kanzlei-steuern` | `geldwaeschevermerk`; aktueller Fachstand und nächster Entscheidungsbedarf | `auftrag`; nächster Skill, Produkt und verantwortliche Person |
| `honorar-budget-vereinbaren` | `zeiten-erfassen` | `honorarstand`; tatsächliche Minuten oder offene Zeitfrage | `zeitstand`; Journal-ID, offene Minuten und Entwurfswirkung |
| `honorar-budget-vereinbaren` | `abrechnung-e-rechnung` | `honorarstand`; Honorarstand, Zeitstand, Auslagen, Vorschüsse und Empfänger | `rechnung, gegebenenfalls rechnung-xml`; Rechnungsentwurf und Formatentscheidung; G4 offen |
| `honorar-budget-vereinbaren` | `mandantenkommunikation` | `honorarstand`; Empfänger, Ergebnis, Friststatus und Entscheidungsbedarf | `mandantenbrief`; Briefentwurf; Entscheidung erst nach echter Antwort |
| `honorar-budget-vereinbaren` | `akte-fristen-anlegen` | `honorarstand`; Stammdaten, Dokument- oder Fristobjekt | `dokumentregister, fristenliste`; Register aktualisiert; Eintrag nur mit Rücklesebeleg |
| `honorar-budget-vereinbaren` | `anwaltsberufsrecht-pruefen` | `honorarstand`; konkrete Handlung und Befugnisfrage | `berufsrechtsvermerk`; rechtliche Bewertung; menschliche Freigabe gesondert |
| `honorar-budget-vereinbaren` | `vertraege-agb-pruefen` | `honorarstand`; Klauselfassung, Rolle und Prüfauftrag | `vertragspruefung`; Befunde, Ersatzklauseln, verbleibende Risiken |
| `honorar-budget-vereinbaren` | `mandat-abschliessen` | `honorarstand`; Beendigungsgrund, Restpflichten und führende Register | `abschlussbrief, aufbewahrungsvermerk`; Abschlussprodukte; Freigaben und Vollzug gesondert |
| `ki-kanzlei-steuern` | `fristen-berechnen-ueberwachen` | `auftrag`; Fristobjekt, Originalauslöser, Beleg und Rechtsregime | `rechenvermerk-<id>`; berechneter Vermerk; Eintragung und Rücklesung gesondert |
| `ki-kanzlei-steuern` | `honorar-budget-vereinbaren` | `auftrag`; Umfang, Vereinbarung und Kostenänderung | `honorarstand`; bestätigte Grundlage oder offener Nachtrag |
| `ki-kanzlei-steuern` | `zeiten-erfassen` | `auftrag`; tatsächliche Minuten oder offene Zeitfrage | `zeitstand`; Journal-ID, offene Minuten und Entwurfswirkung |
| `ki-kanzlei-steuern` | `schriftsaetze-entwerfen` | `auftrag`; Prozesslage, Belege, Form und Antragsziel | `konkrete Schriftsatzart, etwa klage oder einspruch`; ausformulierter Entwurf und Anlagenmatrix |
| `ki-kanzlei-steuern` | `bea-anlagen-vorbereiten` | `auftrag`; geprüfter Schriftsatz, Anlagenzuordnung, Frist, Empfänger | `versandpaket`; Manifest/Preflight; Eingang erst nach tatsächlichem Versand |
| `ki-kanzlei-steuern` | `abrechnung-e-rechnung` | `auftrag`; Honorarstand, Zeitstand, Auslagen, Vorschüsse und Empfänger | `rechnung, gegebenenfalls rechnung-xml`; Rechnungsentwurf und Formatentscheidung; G4 offen |
| `ki-kanzlei-steuern` | `mandantenkommunikation` | `auftrag`; Empfänger, Ergebnis, Friststatus und Entscheidungsbedarf | `mandantenbrief`; Briefentwurf; Entscheidung erst nach echter Antwort |
| `ki-kanzlei-steuern` | `mandat-abschliessen` | `auftrag`; Beendigungsgrund, Restpflichten und führende Register | `abschlussbrief, aufbewahrungsvermerk`; Abschlussprodukte; Freigaben und Vollzug gesondert |
| `mandantenkommunikation` | `fristen-berechnen-ueberwachen` | `mandantenbrief`; Fristobjekt, Originalauslöser, Beleg und Rechtsregime | `rechenvermerk-<id>`; berechneter Vermerk; Eintragung und Rücklesung gesondert |
| `mandantenkommunikation` | `honorar-budget-vereinbaren` | `mandantenbrief`; Umfang, Vereinbarung und Kostenänderung | `honorarstand`; bestätigte Grundlage oder offener Nachtrag |
| `mandantenkommunikation` | `recht-recherchieren` | `mandantenbrief`; Rechtsfrage, Sachverhalt und Normstand | `rechtsvermerk`; belegte Antwort mit Anwendungsgrenzen |
| `mandantenkommunikation` | `schriftsaetze-entwerfen` | `mandantenbrief`; Prozesslage, Belege, Form und Antragsziel | `konkrete Schriftsatzart, etwa klage oder einspruch`; ausformulierter Entwurf und Anlagenmatrix |
| `mandantenkommunikation` | `anwaltsberufsrecht-pruefen` | `mandantenbrief`; konkrete Handlung und Befugnisfrage | `berufsrechtsvermerk`; rechtliche Bewertung; menschliche Freigabe gesondert |
| `mandantenkommunikation` | `zeiten-erfassen` | `mandantenbrief`; tatsächliche Minuten oder offene Zeitfrage | `zeitstand`; Journal-ID, offene Minuten und Entwurfswirkung |
| `mandantenkommunikation` | `mandat-abschliessen` | `mandantenbrief`; Beendigungsgrund, Restpflichten und führende Register | `abschlussbrief, aufbewahrungsvermerk`; Abschlussprodukte; Freigaben und Vollzug gesondert |
| `mandantenkommunikation` | `workflow-uebergabe` | `mandantenbrief`; Empfänger, Aufgabe, Fassung und Übernahmebedarf | `uebergabevermerk`; kontrollierte Fassung; Übernahme nur mit Bestätigung |
| `mandat-abschliessen` | `fristen-berechnen-ueberwachen` | `abschlussbrief, aufbewahrungsvermerk`; Fristobjekt, Originalauslöser, Beleg und Rechtsregime | `rechenvermerk-<id>`; berechneter Vermerk; Eintragung und Rücklesung gesondert |
| `mandat-abschliessen` | `abrechnung-e-rechnung` | `abschlussbrief, aufbewahrungsvermerk`; Honorarstand, Zeitstand, Auslagen, Vorschüsse und Empfänger | `rechnung, gegebenenfalls rechnung-xml`; Rechnungsentwurf und Formatentscheidung; G4 offen |
| `mandat-abschliessen` | `zahlungen-buchhaltung` | `abschlussbrief, aufbewahrungsvermerk`; Rechnung, Zahlungsbeleg, Zweck und Berechtigte | `zahlungsstand`; belegte Zuordnung; Auszahlung erst nach G5 und Vollzug |
| `mandat-abschliessen` | `anwaltsberufsrecht-pruefen` | `abschlussbrief, aufbewahrungsvermerk`; konkrete Handlung und Befugnisfrage | `berufsrechtsvermerk`; rechtliche Bewertung; menschliche Freigabe gesondert |
| `mandat-abschliessen` | `mandantenkommunikation` | `abschlussbrief, aufbewahrungsvermerk`; Empfänger, Ergebnis, Friststatus und Entscheidungsbedarf | `mandantenbrief`; Briefentwurf; Entscheidung erst nach echter Antwort |
| `mandat-abschliessen` | `workflow-uebergabe` | `abschlussbrief, aufbewahrungsvermerk`; Empfänger, Aufgabe, Fassung und Übernahmebedarf | `uebergabevermerk`; kontrollierte Fassung; Übernahme nur mit Bestätigung |
| `mandat-abschliessen` | `mandatsannahme-interessenkollision` | `abschlussbrief, aufbewahrungsvermerk`; Beteiligte, Auftrag und Konfliktanlass | `annahme`; Annahme/Begrenzung/Absage; G1-Stand |
| `mandat-abschliessen` | `geldwaesche-pruefen` | `abschlussbrief, aufbewahrungsvermerk`; Katalogtätigkeit, Zahlungs- oder Risikobefund | `geldwaeschevermerk`; Anwendbarkeit und Nachweise; Meldefrage geschützt |
| `mandatsannahme-interessenkollision` | `fristen-berechnen-ueberwachen` | `annahme`; Fristobjekt, Originalauslöser, Beleg und Rechtsregime | `rechenvermerk-<id>`; berechneter Vermerk; Eintragung und Rücklesung gesondert |
| `mandatsannahme-interessenkollision` | `honorar-budget-vereinbaren` | `annahme`; Umfang, Vereinbarung und Kostenänderung | `honorarstand`; bestätigte Grundlage oder offener Nachtrag |
| `mandatsannahme-interessenkollision` | `geldwaesche-pruefen` | `annahme`; Katalogtätigkeit, Zahlungs- oder Risikobefund | `geldwaeschevermerk`; Anwendbarkeit und Nachweise; Meldefrage geschützt |
| `mandatsannahme-interessenkollision` | `anwaltsberufsrecht-pruefen` | `annahme`; konkrete Handlung und Befugnisfrage | `berufsrechtsvermerk`; rechtliche Bewertung; menschliche Freigabe gesondert |
| `mandatsannahme-interessenkollision` | `akte-fristen-anlegen` | `annahme`; Stammdaten, Dokument- oder Fristobjekt | `dokumentregister, fristenliste`; Register aktualisiert; Eintrag nur mit Rücklesebeleg |
| `mandatsannahme-interessenkollision` | `zeiten-erfassen` | `annahme`; tatsächliche Minuten oder offene Zeitfrage | `zeitstand`; Journal-ID, offene Minuten und Entwurfswirkung |
| `recht-recherchieren` | `schriftsaetze-entwerfen` | `rechtsvermerk`; Prozesslage, Belege, Form und Antragsziel | `konkrete Schriftsatzart, etwa klage oder einspruch`; ausformulierter Entwurf und Anlagenmatrix |
| `recht-recherchieren` | `mandantenkommunikation` | `rechtsvermerk`; Empfänger, Ergebnis, Friststatus und Entscheidungsbedarf | `mandantenbrief`; Briefentwurf; Entscheidung erst nach echter Antwort |
| `recht-recherchieren` | `vertraege-agb-pruefen` | `rechtsvermerk`; Klauselfassung, Rolle und Prüfauftrag | `vertragspruefung`; Befunde, Ersatzklauseln, verbleibende Risiken |
| `recht-recherchieren` | `vertraege-gestalten` | `rechtsvermerk`; Geschäftsziel, Befunde und bestätigte Entscheidungen | `vertrag`; Entwurf und dokumentierte Fassungsänderungen |
| `recht-recherchieren` | `fristen-berechnen-ueberwachen` | `rechtsvermerk`; Fristobjekt, Originalauslöser, Beleg und Rechtsregime | `rechenvermerk-<id>`; berechneter Vermerk; Eintragung und Rücklesung gesondert |
| `recht-recherchieren` | `zeiten-erfassen` | `rechtsvermerk`; tatsächliche Minuten oder offene Zeitfrage | `zeitstand`; Journal-ID, offene Minuten und Entwurfswirkung |
| `recht-recherchieren` | `workflow-uebergabe` | `rechtsvermerk`; Empfänger, Aufgabe, Fassung und Übernahmebedarf | `uebergabevermerk`; kontrollierte Fassung; Übernahme nur mit Bestätigung |
| `schriftsaetze-entwerfen` | `recht-recherchieren` | `konkrete Schriftsatzart, etwa klage oder einspruch`; Rechtsfrage, Sachverhalt und Normstand | `rechtsvermerk`; belegte Antwort mit Anwendungsgrenzen |
| `schriftsaetze-entwerfen` | `fristen-berechnen-ueberwachen` | `konkrete Schriftsatzart, etwa klage oder einspruch`; Fristobjekt, Originalauslöser, Beleg und Rechtsregime | `rechenvermerk-<id>`; berechneter Vermerk; Eintragung und Rücklesung gesondert |
| `schriftsaetze-entwerfen` | `bea-anlagen-vorbereiten` | `konkrete Schriftsatzart, etwa klage oder einspruch`; geprüfter Schriftsatz, Anlagenzuordnung, Frist, Empfänger | `versandpaket`; Manifest/Preflight; Eingang erst nach tatsächlichem Versand |
| `schriftsaetze-entwerfen` | `mandantenkommunikation` | `konkrete Schriftsatzart, etwa klage oder einspruch`; Empfänger, Ergebnis, Friststatus und Entscheidungsbedarf | `mandantenbrief`; Briefentwurf; Entscheidung erst nach echter Antwort |
| `schriftsaetze-entwerfen` | `zeiten-erfassen` | `konkrete Schriftsatzart, etwa klage oder einspruch`; tatsächliche Minuten oder offene Zeitfrage | `zeitstand`; Journal-ID, offene Minuten und Entwurfswirkung |
| `schriftsaetze-entwerfen` | `workflow-uebergabe` | `konkrete Schriftsatzart, etwa klage oder einspruch`; Empfänger, Aufgabe, Fassung und Übernahmebedarf | `uebergabevermerk`; kontrollierte Fassung; Übernahme nur mit Bestätigung |
| `schriftsaetze-entwerfen` | `anwaltsberufsrecht-pruefen` | `konkrete Schriftsatzart, etwa klage oder einspruch`; konkrete Handlung und Befugnisfrage | `berufsrechtsvermerk`; rechtliche Bewertung; menschliche Freigabe gesondert |
| `vertraege-agb-pruefen` | `mandantenkommunikation` | `vertragspruefung`; Empfänger, Ergebnis, Friststatus und Entscheidungsbedarf | `mandantenbrief`; Briefentwurf; Entscheidung erst nach echter Antwort |
| `vertraege-agb-pruefen` | `vertraege-gestalten` | `vertragspruefung`; Geschäftsziel, Befunde und bestätigte Entscheidungen | `vertrag`; Entwurf und dokumentierte Fassungsänderungen |
| `vertraege-agb-pruefen` | `recht-recherchieren` | `vertragspruefung`; Rechtsfrage, Sachverhalt und Normstand | `rechtsvermerk`; belegte Antwort mit Anwendungsgrenzen |
| `vertraege-agb-pruefen` | `schriftsaetze-entwerfen` | `vertragspruefung`; Prozesslage, Belege, Form und Antragsziel | `konkrete Schriftsatzart, etwa klage oder einspruch`; ausformulierter Entwurf und Anlagenmatrix |
| `vertraege-agb-pruefen` | `fristen-berechnen-ueberwachen` | `vertragspruefung`; Fristobjekt, Originalauslöser, Beleg und Rechtsregime | `rechenvermerk-<id>`; berechneter Vermerk; Eintragung und Rücklesung gesondert |
| `vertraege-agb-pruefen` | `zeiten-erfassen` | `vertragspruefung`; tatsächliche Minuten oder offene Zeitfrage | `zeitstand`; Journal-ID, offene Minuten und Entwurfswirkung |
| `vertraege-agb-pruefen` | `workflow-uebergabe` | `vertragspruefung`; Empfänger, Aufgabe, Fassung und Übernahmebedarf | `uebergabevermerk`; kontrollierte Fassung; Übernahme nur mit Bestätigung |
| `vertraege-gestalten` | `vertraege-agb-pruefen` | `vertrag`; Klauselfassung, Rolle und Prüfauftrag | `vertragspruefung`; Befunde, Ersatzklauseln, verbleibende Risiken |
| `vertraege-gestalten` | `recht-recherchieren` | `vertrag`; Rechtsfrage, Sachverhalt und Normstand | `rechtsvermerk`; belegte Antwort mit Anwendungsgrenzen |
| `vertraege-gestalten` | `mandantenkommunikation` | `vertrag`; Empfänger, Ergebnis, Friststatus und Entscheidungsbedarf | `mandantenbrief`; Briefentwurf; Entscheidung erst nach echter Antwort |
| `vertraege-gestalten` | `fristen-berechnen-ueberwachen` | `vertrag`; Fristobjekt, Originalauslöser, Beleg und Rechtsregime | `rechenvermerk-<id>`; berechneter Vermerk; Eintragung und Rücklesung gesondert |
| `vertraege-gestalten` | `zeiten-erfassen` | `vertrag`; tatsächliche Minuten oder offene Zeitfrage | `zeitstand`; Journal-ID, offene Minuten und Entwurfswirkung |
| `vertraege-gestalten` | `abrechnung-e-rechnung` | `vertrag`; Honorarstand, Zeitstand, Auslagen, Vorschüsse und Empfänger | `rechnung, gegebenenfalls rechnung-xml`; Rechnungsentwurf und Formatentscheidung; G4 offen |
| `vertraege-gestalten` | `schriftsaetze-entwerfen` | `vertrag`; Prozesslage, Belege, Form und Antragsziel | `konkrete Schriftsatzart, etwa klage oder einspruch`; ausformulierter Entwurf und Anlagenmatrix |
| `vertraege-gestalten` | `ki-kanzlei-steuern` | `vertrag`; aktueller Fachstand und nächster Entscheidungsbedarf | `auftrag`; nächster Skill, Produkt und verantwortliche Person |
| `vertraege-gestalten` | `workflow-uebergabe` | `vertrag`; Empfänger, Aufgabe, Fassung und Übernahmebedarf | `uebergabevermerk`; kontrollierte Fassung; Übernahme nur mit Bestätigung |
| `workflow-uebergabe` | `fristen-berechnen-ueberwachen` | `uebergabevermerk`; Fristobjekt, Originalauslöser, Beleg und Rechtsregime | `rechenvermerk-<id>`; berechneter Vermerk; Eintragung und Rücklesung gesondert |
| `workflow-uebergabe` | `anwaltsberufsrecht-pruefen` | `uebergabevermerk`; konkrete Handlung und Befugnisfrage | `berufsrechtsvermerk`; rechtliche Bewertung; menschliche Freigabe gesondert |
| `workflow-uebergabe` | `bea-anlagen-vorbereiten` | `uebergabevermerk`; geprüfter Schriftsatz, Anlagenzuordnung, Frist, Empfänger | `versandpaket`; Manifest/Preflight; Eingang erst nach tatsächlichem Versand |
| `workflow-uebergabe` | `recht-recherchieren` | `uebergabevermerk`; Rechtsfrage, Sachverhalt und Normstand | `rechtsvermerk`; belegte Antwort mit Anwendungsgrenzen |
| `workflow-uebergabe` | `schriftsaetze-entwerfen` | `uebergabevermerk`; Prozesslage, Belege, Form und Antragsziel | `konkrete Schriftsatzart, etwa klage oder einspruch`; ausformulierter Entwurf und Anlagenmatrix |
| `workflow-uebergabe` | `mandantenkommunikation` | `uebergabevermerk`; Empfänger, Ergebnis, Friststatus und Entscheidungsbedarf | `mandantenbrief`; Briefentwurf; Entscheidung erst nach echter Antwort |
| `workflow-uebergabe` | `zeiten-erfassen` | `uebergabevermerk`; tatsächliche Minuten oder offene Zeitfrage | `zeitstand`; Journal-ID, offene Minuten und Entwurfswirkung |
| `workflow-uebergabe` | `mandat-abschliessen` | `uebergabevermerk`; Beendigungsgrund, Restpflichten und führende Register | `abschlussbrief, aufbewahrungsvermerk`; Abschlussprodukte; Freigaben und Vollzug gesondert |
| `zahlungen-buchhaltung` | `fristen-berechnen-ueberwachen` | `zahlungsstand`; Fristobjekt, Originalauslöser, Beleg und Rechtsregime | `rechenvermerk-<id>`; berechneter Vermerk; Eintragung und Rücklesung gesondert |
| `zahlungen-buchhaltung` | `abrechnung-e-rechnung` | `zahlungsstand`; Honorarstand, Zeitstand, Auslagen, Vorschüsse und Empfänger | `rechnung, gegebenenfalls rechnung-xml`; Rechnungsentwurf und Formatentscheidung; G4 offen |
| `zahlungen-buchhaltung` | `honorar-budget-vereinbaren` | `zahlungsstand`; Umfang, Vereinbarung und Kostenänderung | `honorarstand`; bestätigte Grundlage oder offener Nachtrag |
| `zahlungen-buchhaltung` | `mandat-abschliessen` | `zahlungsstand`; Beendigungsgrund, Restpflichten und führende Register | `abschlussbrief, aufbewahrungsvermerk`; Abschlussprodukte; Freigaben und Vollzug gesondert |
| `zahlungen-buchhaltung` | `anwaltsberufsrecht-pruefen` | `zahlungsstand`; konkrete Handlung und Befugnisfrage | `berufsrechtsvermerk`; rechtliche Bewertung; menschliche Freigabe gesondert |
| `zahlungen-buchhaltung` | `geldwaesche-pruefen` | `zahlungsstand`; Katalogtätigkeit, Zahlungs- oder Risikobefund | `geldwaeschevermerk`; Anwendbarkeit und Nachweise; Meldefrage geschützt |
| `zahlungen-buchhaltung` | `workflow-uebergabe` | `zahlungsstand`; Empfänger, Aufgabe, Fassung und Übernahmebedarf | `uebergabevermerk`; kontrollierte Fassung; Übernahme nur mit Bestätigung |
| `zeiten-erfassen` | `honorar-budget-vereinbaren` | `zeitstand`; Umfang, Vereinbarung und Kostenänderung | `honorarstand`; bestätigte Grundlage oder offener Nachtrag |
| `zeiten-erfassen` | `abrechnung-e-rechnung` | `zeitstand`; Honorarstand, Zeitstand, Auslagen, Vorschüsse und Empfänger | `rechnung, gegebenenfalls rechnung-xml`; Rechnungsentwurf und Formatentscheidung; G4 offen |
| `zeiten-erfassen` | `mandantenkommunikation` | `zeitstand`; Empfänger, Ergebnis, Friststatus und Entscheidungsbedarf | `mandantenbrief`; Briefentwurf; Entscheidung erst nach echter Antwort |
| `zeiten-erfassen` | `anwaltsberufsrecht-pruefen` | `zeitstand`; konkrete Handlung und Befugnisfrage | `berufsrechtsvermerk`; rechtliche Bewertung; menschliche Freigabe gesondert |
| `zeiten-erfassen` | `mandat-abschliessen` | `zeitstand`; Beendigungsgrund, Restpflichten und führende Register | `abschlussbrief, aufbewahrungsvermerk`; Abschlussprodukte; Freigaben und Vollzug gesondert |

Die Tabelle erfasst alle 126 gerichteten Nachbarskill-Bezüge aus den achtzehn Übergabeabschnitten. Fachliche Prüfung, menschliche Freigabe und tatsächlicher Vollzug sind eigene Nachweise. Ein Skill liefert keine Mandantenentscheidung, Eingangsbestätigung oder Auszahlung allein dadurch, dass er einen Entwurf erzeugt.

## 1.11. Statusblock ohne Dateizugriff

Am Ende jeder Bearbeitungsantwort steht dieser fortschreibbare Stand; bei bloßer Sachauskunft genügt ein Verweis auf den unveränderten letzten Stand. Ein nicht berechneter Hash wird nicht erfunden. Eine Verknüpfung auf die tatsächlich gelieferte Fassung oder ein klar abgegrenzter Textblock tritt dann an seine Stelle.

```text
Mandat: <ID>; Stand: <Datum/Revision>; Modus: Text oder Datei; Stufe: <0–3>.
Phase: <Hauptphase>; Nebenläufe: <Liste>.
Führende Produkte: <Produktkennung, Pfad oder Textfassung, Hash oder „nicht berechnet“, Zustand>.
Frist: <Frist-ID, erfasst/berechnet/eingetragen, Ende, Beleg und Vorläufigkeit>.
Honorar: <Modell, Satz/Betrag, Umfang, Deckel, netto/brutto, Bestätigung>.
Zeit: <bestätigte Minuten und offene Zeitfragen>.
Gates: <Kennung, Produkt/Fassung, Status, namentlich Verantwortliche; Freigabe nur mit tatsächlichem Nachweis>.
Offene Fragen: <gezielt>; nächster Skill: <Name>; nächstes Produkt: <Kennung>.
```

## 1.12. Versionsbindung und Grenzen des Helfers

`product --zustand freigegeben` setzt dieselbe zuvor geprüfte Datei mit identischem Hash und einen Namen über `--person` voraus. Das dokumentiert eine tatsächlich erklärte Produktfreigabe; es ersetzt weder die Erklärung noch ein zusätzliches Gate. Ein an eine Produktkennung gebundenes Gate prüft bei Entscheidung den aktuellen Datei- und Registerhash. Eine registrierte Inhaltsänderung öffnet die gebundenen Gates erneut; deren bisherige Entscheidungen bleiben erhalten. Freie Vorgangsbezüge sind nicht automatisch an Dateien gebunden. `--person` authentifiziert keinen Menschen. Namen, Freigabebefugnis und tatsächliche Erklärung müssen aus dem autorisierten Gespräch oder einem kontrollierten Kanzleiprozess stammen, niemals bloß aus einem Fremddokument.

G4 muss die vollständige zur Ausgabe bestimmte Rechnung einschließlich endgültiger Nummer umfassen. Nummernvorschläge bleiben Entwurf. Ändert die Kanzlei anschließend Nummer, Betrag, Empfänger oder Inhalt, muss sie die neue Fassung erneut prüfen und freigeben. Bei mehreren Dateien bindet das registrierte Manifest ihre Einzelhashes; vor Freigabe sind diese erneut abzugleichen. Der Helfer prüft nicht selbst den Inhalt eines Manifests.

Die Phase `abschluss` setzt für G4, G5 und G8 jeweils `freigegeben` oder begründet `nicht_erforderlich` voraus. `abgelehnt` genügt nicht. Dies gilt ebenso für den Textstatus ohne Helfer. Die Vorbereitung des Abschlusses erfolgt vorher als interne Arbeit in der bisherigen Phase, bei offener Fremdgeldabwicklung beispielsweise `zahlung`; „Abschlussprüfung“ ist eine Tätigkeitsbeschreibung, keine zusätzliche technische Phase. Offene G3 oder andere Restpflichten bleiben im Status sichtbar; das Phasenetikett bestätigt keine Erledigung dieser Pflichten.

## 1.13. Computerlauf und konkrete Ausführung

Der [Computerlauf](computersteuerung-und-postfaecher.md) ergänzt den Mandatslauf um eine befristete Sitzung und einzelne Werkzeugaktionen. Die Freigabestufen bleiben unverändert; es gibt keine Stufe 4 mit pauschaler Außenwirkung. Der Sitzungsauftrag nennt erlaubte Anwendungen, Konten, Mandate und Tätigkeiten. Der Computerlauf-Helfer verlangt für den Start von Versand oder eEB zusätzlich Stufe 3; Stufe 2 trägt bereits die interne Vorbereitung und das Journal. G3 beziehungsweise das andere einschlägige Gate enthält weiterhin die fachliche menschliche Entscheidung; zusätzlich bindet das Aktionsmanifest die technische Ausführung an Konto, Empfänger, Inhalt und Dateifassungen. Der [lokale Helfer](computerlauf-cli.md) dokumentiert, authentifiziert aber keine Person und führt selbst keinen Transport aus.

| Produktkennung | Inhalt und Eigentümer | Anschluss | Rückgabe |
| --- | --- | --- | --- |
| `computerlauf` | Sitzung und Grenzen, Hauptskill | Alle innerhalb des Rahmens nötigen Skills | Status, noch ausführbarer Schritt, Stopgrund |
| `eingang-<id>` | Unveränderter Eingang mit Herkunft und Anlagen, beA-Skill oder Aktenanlage | Fristenskill und sachlich zuständiger Skill | Dokumentregister, Fristobjekt, nächstes Fachprodukt |
| `versandauftrag-<id>` | Konkrete Empfänger, Inhalt, Dateihashes und Freigaben, versendender Fachskill | beA-Skill oder freigegebener Mailablauf | Versuch und tatsächlicher Nachweis oder ungeklärter Ausgang |
| `bea-versuch-<id>` | Zeitpunkt, Fassung und Ergebnis eines beA-Übermittlungsversuchs, beA-Skill | Ausgangskontrolle und Abgleich | Belegter Eingang oder ungeklärter Ausgang; keine automatische Wiederholung |
| `versandnachweis-<id>` | Beleg der tatsächlichen Übermittlung, ausführender Ablauf | Aktenanlage und gegebenenfalls Fristenskill | Zuordnung und überprüfter Stand; keine bloß behauptete Erledigung |
| `eeb-<id>` | Empfangssachverhalt und separate Erklärung, beA-Skill | Zuständige natürliche Person und zulässiger Übermittlungsweg | Entscheidungs-, Übermittlungs- und Fristbezug getrennt |

Diese Kennungen ergänzen die 126 fachlichen Übergaben, ohne deren bestehende Produkte umzubenennen. `versandpaket` bleibt das Anlagenmanifest; `versandauftrag-<id>` ergänzt den konkreten Ausführungsauftrag. `mandatslauf.py` prüft nicht selbst das Computerlauf-Journal oder das tatsächliche Postfach. Die ausführende Instanz muss daher beide Stände und den tatsächlichen Beleg zusammenführen.

Der Statusblock erhält bei aktivem Computerlauf zusätzlich: Sitzungskennung, Simulation oder Echtmodus, Ablaufzeit, zugelassenes Konto, aktuelle Aktionskennung, Manifestfassung, tatsächliche Freigabe und Ausgang. Ein unklarer Versandversuch bleibt sichtbar, auch wenn G3 freigegeben ist. Bei Stopp endet jede weitere beauftragte Computeraktion; bereits erfolgte oder laufende Außenwirkungen sind dadurch nicht rückgängig gemacht. Ein neuer Host benötigt eine neue Prüfung seiner tatsächlichen Fähigkeiten und Berechtigungen.
