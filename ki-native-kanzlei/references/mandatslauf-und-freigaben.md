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
| 2 | Journal und Register | Bestätigte Zeiten, Honorarabschnitte, Auslagen und Zahlungen im Journal buchen, Fristobjekte erfassen, Rechenvermerke erzeugen, Mandatslauf fortschreiben |
| 3 | Versandvorbereitung | Versandpakete, Rechnungsentwürfe mit Nummernvorschlag und XML-Entwürfe erzeugen, Übergabevermerke erstellen, Nachbarskills ohne Rückfrage anstoßen |

Stufe 3 ist die Obergrenze des Plugins. Es gibt keine Stufe, in der die Maschine selbst einreicht, versendet, auszahlt, eine Rechnung ausgibt, einen Kalendereintrag als bestätigt kennzeichnet, eine Verdachtsmeldung abgibt oder Daten löscht. Diese Handlungen bleiben Freigabegates.

## 1.4. Freigabegates

Jedes Gate hat eine Kennung, einen Auslöser, einen zuständigen Skill und eine Person, die freigibt. Eine Freigabe wird mit Name, Zeitpunkt und Bezug (etwa Dateiname und Hash der freigegebenen Fassung) dokumentiert. Die Maschine darf ein Gate öffnen und das Produkt dafür vorbereiten; sie darf es nicht selbst freigeben. Ein Gate kann als „nicht erforderlich“ geschlossen werden, wenn der Sachverhalt es nicht auslöst; auch das wird mit Grund dokumentiert.

| Gate | Auslöser | Was die Freigabe bedeutet |
| --- | --- | --- |
| G1 Annahme | Neue Anfrage, neuer Gegner, Auftragserweiterung | Mandat, Umfang und Honorargrundlage sind von einem Berufsträger bestätigt |
| G2 Fristeintrag | Rechenvermerk liegt vor | Die Frist ist im führenden Kalender eingetragen und rückgelesen; Vorfrist und Verantwortliche stehen fest |
| G3 Versand und Einreichung | Versandpaket oder Brief ist vorbereitet | Ein Berufsträger hat Fassung, Anlagen und Empfänger geprüft und den Versand angeordnet; der Eingangsbeleg wird nachgetragen |
| G4 Rechnungsausgabe | Rechnungsentwurf ist fachlich geprüft | Nummer, Mitteilung und Fälligkeit sind von der Kanzlei verantwortet |
| G5 Zahlung und Fremdgeld | Auszahlung, Verrechnung oder Weiterleitung steht an | Die Kanzlei hat die Zahlungsanweisung erteilt; Fremdgeld bleibt getrennt |
| G6 Dienstleister | Daten sollen einen externen Dienst oder KI-Dienst erreichen | Erforderlichkeit, Vertrag nach § 43e BRAO, Datenschutz und Einwilligung sind geprüft und dokumentiert |
| G7 Meldung | Verdachtsmoment nach GwG oder Haftungsfall | Ein Berufsträger hat über Meldung oder Anzeige entschieden; keine automatische Abgabe |
| G8 Abschluss und Löschung | Mandatsende | Restfristen, Fremdgeld, Herausgabe und Aufbewahrung sind entschieden; die Löschung ist je Dokumentart angeordnet |

## 1.5. Führende Fassung und Produktregister

Jedes Produkt erhält im Mandatslauf eine Kennung, einen Pfad, den Hash der Datei, den erzeugenden Skill und einen Zustand: `entwurf`, `geprueft` oder `freigegeben`. Nur eine Fassung je Produkt ist führend. Eine neue Fassung ersetzt die alte im Register, ohne sie aus der Nachweiskette zu entfernen. Ein Skill, der ein Produkt eines anderen Skills verändert, trägt die neue Fassung mit seinem Namen ein. Ein Übergabevermerk nennt die führenden Fassungen mit Hash; ein Rücklauf wird gegen diesen Hash geprüft.

## 1.6. Nächster Schritt

Der nächste Schritt ergibt sich aus Phase, offenen Gates und offenen Fragen, nicht aus der Reihenfolge der Skillliste. Die Regel lautet: Zuerst das offene Gate mit der frühesten Fristwirkung, dann die Phase, in der das bestellte Produkt entsteht, dann der Honorar- und Zeitanschluss. Ein offenes Gate G2 geht jeder Sacharbeit vor, solange die Frist nicht gesichert ist. Ein offenes Gate G1 blockiert nicht die interne Vorbereitung, aber jede Außenwirkung. Der Helfer gibt mit `next` eine Empfehlung aus; sie ist ein Vorschlag, keine Anweisung.

## 1.7. Aufruf des Helfers

Python 3.10 oder neuer, nur Standardbibliothek. Alle Angaben kommen aus einer UTF-8-JSON-Datei oder aus benannten Optionen; es werden keine Mandatsdaten in Shellbefehle interpoliert.

```bash
python3 "<Pluginordner>/scripts/mandatslauf.py" init --akte "/Mandate/M-26-104" --matter-id "M-26-104" --stufe 2
python3 "<Pluginordner>/scripts/mandatslauf.py" phase --akte "/Mandate/M-26-104" --phase sacharbeit --grund "Klageentwurf bestellt"
python3 "<Pluginordner>/scripts/mandatslauf.py" product --akte "/Mandate/M-26-104" --id klage --pfad "01_Bearbeitung/Klage_v04.docx" --skill schriftsaetze-entwerfen --zustand entwurf
python3 "<Pluginordner>/scripts/mandatslauf.py" gate --akte "/Mandate/M-26-104" --gate G3 --aktion oeffnen --bezug "Klage_v04.docx"
python3 "<Pluginordner>/scripts/mandatslauf.py" gate --akte "/Mandate/M-26-104" --gate G3 --aktion freigeben --person "RAin Dr. Ahrens" --bezug "Klage_v04.docx"
python3 "<Pluginordner>/scripts/mandatslauf.py" status --akte "/Mandate/M-26-104"
python3 "<Pluginordner>/scripts/mandatslauf.py" next --akte "/Mandate/M-26-104"
```

`freigeben` verlangt eine namentlich bezeichnete Person; Bezeichnungen wie „KI“, „Agent“, „System“ oder „automatisch“ werden abgewiesen. `init` verweigert das Überschreiben eines vorhandenen Laufs. Jede Änderung erhöht die Revision und wird in der Historie mit Zeitstempel festgehalten; die Datei wird atomar geschrieben. Der Helfer schreibt keinen Kalender, versendet nichts und bucht nichts; er dokumentiert.

## 1.8. Was agentisch bedeutet und was nicht

Agentisch heißt: Die Maschine liest den Mandatslauf, erkennt die Phase und das nächste Produkt, erzeugt es innerhalb der Freigabestufe, trägt die führende Fassung ein, öffnet das nötige Gate und stößt den Nachbarskill an, ohne dass der Nutzer die Reihenfolge diktieren muss. Sie meldet den Stand mit Dateilinks, offenen Gates und Honorar- und Zeitstand. Nicht agentisch heißt: Sie erfindet keine Freigabe, keine Zeit, keinen Zugang, keinen Kalendereintrag und keinen Eingangsbeleg, sie bleibt bei einer offenen Entscheidung stehen, wenn ohne sie kein sinnvoller Fortschritt möglich ist, und sie wechselt nicht von selbst in ein Gerichtsverfahren, wenn nur ein Gutachten bestellt ist. Die Kanzlei erweitert die Freigabestufe erst, wenn die Protokolle der niedrigeren Stufe sie überzeugt haben.

## 1.9. Zuordnung der Skills zu Phasen und Gates

Die Tabelle fasst zusammen, welche Phase jeder Skill verantwortet und welche Gates er öffnet. Sie entspricht den Unterabschnitten „Agentischer Lauf und Freigabestufe“ der einzelnen Skills. Der Helfer führt jedes Gate unter einem festen zuständigen Skill (G1 Annahme, G2 Fristen, G3 beA-Vorbereitung, G4 Abrechnung, G5 Zahlungen, G6 Übergabe, G7 Geldwäsche, G8 Abschluss); öffnet ein anderer Skill das Gate, nennt der Bezug dessen Produkt, und `next` verweist dennoch auf den zuständigen Skill.

| Skill | Phase | Gates |
| --- | --- | --- |
| ki-kanzlei-steuern | eingang | G1; führt alle Gates zusammen und trägt Nachweise nach |
| mandatsannahme-interessenkollision | annahme | G1; G6 bei Portal- oder Dienstleisterbezug |
| akte-fristen-anlegen | akte | G2 öffnen (nicht freigeben); G6 bei Scan- oder KI-Dienst |
| fristen-berechnen-ueberwachen | frist (meist Nebenlauf) | G2 |
| anwaltsberufsrecht-pruefen | Nebenlauf zur Anlassphase | G6, G7 bei Haftungsfall, G1 bei Kollision |
| geldwaesche-pruefen | Nebenlauf zu annahme | G7; G1 mit Prüfvermerk als Bezug |
| honorar-budget-vereinbaren | abrechnung (Nebenlauf) | G1 für Vereinbarung oder Nachtrag |
| zeiten-erfassen | abrechnung | kein eigenes Gate; Zeitstand für G4 |
| workflow-uebergabe | Querschnitt | G6 |
| recht-recherchieren | sacharbeit | kein eigenes Gate; Stopp vor G6 |
| schriftsaetze-entwerfen | sacharbeit | G3 erst mit Versandpaket; G2 hat Vorrang |
| vertraege-agb-pruefen | sacharbeit | G3 für Verhandlungsvorschlag an die Gegenseite |
| vertraege-gestalten | sacharbeit | G3 für Versand an Mandant oder Gegenseite |
| mandantenkommunikation | kommunikation | G3; Fristangaben nur aus eingetragenen Fristobjekten |
| bea-anlagen-vorbereiten | versandvorbereitung | G3 mit Manifest-Hash als Bezug |
| abrechnung-e-rechnung | abrechnung | G4 |
| zahlungen-buchhaltung | zahlung | G5 |
| mandat-abschliessen | abschluss | G8 und G3 für den Abschlussbrief; Phase erst nach G4, G5, G8 |
