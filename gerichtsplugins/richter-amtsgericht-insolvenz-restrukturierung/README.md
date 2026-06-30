# Insolvenz- und Restrukturierungsgericht am Amtsgericht

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Insolvenz- und Restrukturierungsgericht: Eröffnungsverfahren Sicherungsmaßnahmen Verwalterauswahl Gläubigerversammlung Prüfungstermin Schlusstermin Restschuldbefreiung Restrukturierungssache nach StaRUG mit Stabilisierungsanordnung und Planbestätigung

Dieses Plugin gehört zum Marketplace mit 232 Plugins für deutsches Recht. Es bündelt die zugehörigen Skills, Prüfraster, Vorlagen und Arbeitsroutinen in einem installierbaren Plugin-ZIP. Die zwei Markdown-Prompts sind vollwertige Ein-Datei-Starts für den Fall, dass kein Plugin-Setup genutzt werden soll: Werkstatt für den ausführlichen Arbeitsmodus, Schnellstart für den kompakten Einstieg.

Schneller Weg: Für eine erste Ergebnisrichtung den Schnellstart laden, für einen tragfähigen Arbeitsmodus die Werkstatt. Beide Prompts sollen mit einem konkreten Arbeitsprodukt beginnen, nur eng nachfragen und nicht in einer Materialinventur hängen bleiben.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`richter-amtsgericht-insolvenz-restrukturierung.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/richter-amtsgericht-insolvenz-restrukturierung.zip) |
| Großer Prompt (Werkstatt) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/gerichtsplugins/richter-amtsgericht-insolvenz-restrukturierung/richter-amtsgericht-insolvenz-restrukturierung-werkstatt.md" download><code>richter-amtsgericht-insolvenz-restrukturierung-werkstatt.md</code></a> |
| Kleiner Prompt (Schnellstart) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/gerichtsplugins/richter-amtsgericht-insolvenz-restrukturierung/richter-amtsgericht-insolvenz-restrukturierung-schnellstart.md" download><code>richter-amtsgericht-insolvenz-restrukturierung-schnellstart.md</code></a> |
| Testakte(n) als ZIP | ZIP | [Gesamt-PDF](testakte/gesamt-pdf/testakte_gesamt.pdf), [`richter-amtsgericht-insolvenz-restrukturierung-testakte.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/richter-amtsgericht-insolvenz-restrukturierung-testakte.zip), [`richter-amtsgericht-insolvenz-restrukturierung-testakte-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/richter-amtsgericht-insolvenz-restrukturierung-testakte-einzelpdfs.zip) |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 232 Plugins. Wer alle Plugins auf einmal will, nimmt `alle-plugins-megazip.zip`. Wer nur einzelne Werkstatt- oder Schnellstart-Prompts will, nimmt die Markdown-Downloads.
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du Eroeffnungsgrund und Fortbestehensprognose belastbar bestimmen und den naechsten Verfahrensschritt wählen.
> **Experimentelles Plugin im Ordner `gerichtsplugins/`** — siehe Vorspruch unten.

> **Kritisch — Hochrisiko-KI und Art. 22 DSGVO beachten.** Der Einsatz von KI in der Rechtspflege ist nach Art. 6 Abs. 2 in Verbindung mit Anhang III Nr. 8 Buchstabe a der KI-Verordnung (VO (EU) 2024/1689) grundsätzlich **Hochrisiko-KI**. Die Rückausnahme des Art. 6 Abs. 3 KI-VO greift nur bei rein vorbereitender Tätigkeit ohne Subsumtion; auch dann besteht Registrierungspflicht nach Art. 49 Abs. 2 KI-VO. Eine Entscheidung mit rechtlicher Wirkung über Menschen darf nicht einer Maschine überlassen werden (Art. 22 DSGVO) — die richterliche Letztentscheidung liegt zwingend beim Menschen. Einzelheiten unten unter „Wichtiger Hinweis vor Verwendung".

## Rolle

Insolvenzrichter oder Restrukturierungsrichter am Amtsgericht (Paragraf 2 InsO, Paragrafen 34 ff. StaRUG)

## Rechtsrahmen

InsO, StaRUG, EuInsVO 2015/848, ZPO, GVG, RPflG, GKG, InsVV

## Inhalt

- **11 Skills** (siehe `skills/`; inklusive Schnellstart-Skill)
- **Werkstatt-Prompt** (`richter-amtsgericht-insolvenz-restrukturierung-werkstatt.md`)
- **Schnellstart-Prompt** (`richter-amtsgericht-insolvenz-restrukturierung-schnellstart.md`)
- **Testakte** (`testakte/README.md`) — aus Richtersicht

## Skill-Liste

- **01-eroeffnungsantrag-prüfen-insolvenz** — Prüfung des Eröffnungsantrags Paragrafen 13-15 InsO, Zulässigkeit, Insolvenzgrund (Paragrafen 17-19 InsO), Verfahrens
- **02-sicherungsmassnahmen-vor-eroeffnung** — Sicherungsmaßnahmen Paragraf 21 InsO: vorläufiger Insolvenzverwalter (stark oder schwach), Verfügungsbeschraenkungen,
- **03-eroeffnungsbeschluss-und-verwalterbestellung** — Eröffnungsbeschluss Paragraf 27 InsO, Bestellung Insolvenzverwalter, Bestimmung Berichts-, Prüfungs- und Schlusstermin
- **04-glaeubigerversammlung-und-pruefungstermin** — Gläubigerversammlung Paragrafen 74 ff. InsO, Berichtstermin Paragraf 156, Prüfungstermin Paragraf 176, Feststellung zu
- **05-restschuldbefreiung-und-schlusstermin** — Schlusstermin Paragraf 197 InsO, Schlussverteilung, Restschuldbefreiungsverfahren Paragrafen 286 ff. InsO, Versagungsgru
- **06-eigenverwaltung-und-schutzschirm** — Eigenverwaltung Paragrafen 270 ff. InsO, Eigenverwaltungsplanung Paragraf 270a, Schutzschirmverfahren Paragraf 270d, Sac
- **07-insolvenzplan-bestätigen** — Insolvenzplanverfahren Paragrafen 217 ff. InsO: Vorprüfung Paragraf 231, Anhörung, Erläuterungs- und Abstimmungstermi
- **08-starug-restrukturierungssache-anzeigen** — Anzeige Restrukturierungssache Paragrafen 31 ff. StaRUG, Restrukturierungsbeauftragter Paragraf 73 StaRUG, Restrukturie
- **09-starug-stabilisierungsanordnung** — Stabilisierungsanordnung Paragrafen 49 ff. StaRUG (Vollstreckungs- und Verwertungssperre), Voraussetzungen, Dauer (drei
- **10-starug-planbestaetigung-und-folgen** — Planabstimmung Paragrafen 17 ff. StaRUG, gruppeninternes Mehrheitserfordernis, gruppenübergreifender Cramdown Paragraf ## Wichtiger Hinweis vor Verwendung

**Experimentelles Plugin — Vorsicht.** Dieses Plugin ist ein Funktionsexperiment für den Einsatz von KI an deutschen Gerichten. Es geht hier um die **Capability**, nicht um eine Produktivempfehlung.

### Rechtliche Einordnung der KI-Verordnung (KI-VO, VO (EU) 2024/1689)

- **Art. 6 Abs. 2 i.V.m. Anhang III Nr. 8 lit. a KI-VO**: KI-Systeme, die von einer Justizbehoerde oder in deren Auftrag bei der **Recherche und Auslegung von Sachverhalten und Rechtsvorschriften** sowie bei der **Anwendung des Rechts auf konkrete Sachverhalte** verwendet werden, sind grundsaetzlich **Hochrisiko-KI**.
- **Aber Art. 6 Abs. 3 KI-VO**: Ein KI-System gilt **nicht** als Hochrisiko-KI, wenn es nur eine **vorbereitende Aufgabe** wahrnimmt (z.B. Vorbereitung von Dokumenten, reine Recherche ohne Subsumtion).
- **Notifizierungspflicht**: Auch im Ausnahmefall des Art. 6 Abs. 3 ist der Anbieter bzw. Betreiber verpflichtet, das KI-System bei der zuständigen Aufsicht zu **registrieren** (Art. 49 Abs. 2 KI-VO).
- Die Einordnung ist im Einzelfall zu prüfen. Sobald das System konkrete Entscheidungsvorschlaege produziert, die Subsumtion vornimmt oder die richterliche Würdigung ersetzt, wird die Schwelle zur Hochrisiko-KI überschritten.

### Art. 22 DSGVO — Verbot ausschliesslich automatisierter Entscheidung

Die richterliche Letztentscheidung muss zwingend bei einem Menschen liegen. **Keine Maschine entscheidet als Richter.** Diese Skills sind ausschliesslich **Unterstuetzung** der richterlichen Arbeit, niemals deren Ersatz. Der Richter prüft, gewichtet, entscheidet — die KI bereitet vor und macht Vorschlaege.

### Aktengeheimnis und Datenschutz

- **Paragraf 353b StGB** (Verletzung von Dienstgeheimnissen) und **Paragraf 43 DRiG** (Amtsverschwiegenheit der Richter) sind strikt zu wahren.
- Akteninhalte duerfen nicht ungeprüfte an externe KI-Anbieter übermittelt werden. Vor jeder Verwendung ist zu prüfen, ob die genutzte KI-Umgebung den Datenschutz und das Aktengeheimnis gewaehrleistet.
- **Schatten-KI ist ausdrücklich abgelehnt.** Dieses Plugin soll keine Hilfe sein, KI an behoerdlichen Datenschutz- und IT-Richtlinien vorbei einzusetzen.

### Revisionssicherheit

- Saemtliche Arbeitsergebnisse müssen revisionssicher dokumentiert werden: Wer hat wann welche KI-Ausgabe genutzt, welche Änderungen wurden danach durch den Richter vorgenommen, welche Akten- und Promptbestandteile lagen zugrunde?
- Die KI-Ausgabe muss als KI-Ausgabe erkennbar bleiben (Markierung, Versionierung); die richterliche Bearbeitung dokumentiert werden.
- Aufbewahrungsfristen nach Aktenordnung der Gerichte und ggf. KI-VO-Logging-Pflichten beachten.

### Realismus-Hinweis

Viele Gerichte werden externe Cloud-Dienste auf absehbare Zeit nicht produktiv einsetzen können. Der Wert dieses Plugins liegt darin, dass **Werkstatt-Prompt und Schnellstart-Prompt portabel** sind: Sie funktionieren in einem behördlich freigegebenen Fachsystem mit ausreichendem Kontextfenster und Datei-Upload. Wer im Gericht bereits eine zugelassene Umgebung hat, kann den Werkstatt-Prompt oder Schnellstart-Prompt dort einsetzen, soweit Hausrecht und Datenschutzfreigabe das erlauben.

### Verwendung auf eigene Gefahr

Die Nutzung erfolgt **auf eigene Gefahr und eigene Verantwortung**. Es handelt sich um ein Capability-Experiment. Die Frage, ob und wie der hier abgebildete Workflow rechtssicher betrieben werden kann, ist im Einzelfall zu prüfen — und kann auch zu dem Ergebnis führen, dass es nicht geht. Wir wollen das wissen, indem wir es bauen und ausprobieren.

## Quellenhygiene

- Keine erfundenen Aktenzeichen.
- Rechtsprechung nur mit Aktenzeichen + Datum + Verfahrensbezeichnung.
- Bei Unsicherheit lieber Lueckenliste als Erfindung.
- Vor Verwendung Aktenzeichen in offiziellen Datenbanken (Bundesgerichte, juris frei, Bundesverfassungsgericht.de) live verifizieren.

## Lizenz

Dual-lizenziert MIT und Apache-2.0.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 12 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `01-eroeffnungsantrag-pruefen-insolvenz` | Prüfung des Eröffnungsantrags Paragrafen 13-15 InsO, Zulässigkeit, Insolvenzgrund (Paragrafen 17-19 InsO), Verfahrenskostendeckung, Anhörung des Schuldners |
| `02-sicherungsmassnahmen-vor-eroeffnung` | Sicherungsmaßnahmen Paragraf 21 InsO: vorläufiger Insolvenzverwalter (stark oder schwach), Verfügungsbeschraenkungen, Vollstreckungsverbote, Postsperre, Globalsicherheiten |
| `03-eroeffnungsbeschluss-und-verwalterbestellung` | Eröffnungsbeschluss Paragraf 27 InsO, Bestellung Insolvenzverwalter, Bestimmung Berichts-, Prüfungs- und Schlusstermin, Veröffentlichung, Registereintragung |
| `04-glaeubigerversammlung-und-pruefungstermin` | Gläubigerversammlung Paragrafen 74 ff. InsO, Berichtstermin Paragraf 156, Prüfungstermin Paragraf 176, Feststellung zur Tabelle Paragrafen 174 ff. |
| `05-restschuldbefreiung-und-schlusstermin` | Schlusstermin Paragraf 197 InsO, Schlussverteilung, Restschuldbefreiungsverfahren Paragrafen 286 ff. InsO, Versagungsgründe Paragraf 290, Obliegenheiten Paragraf 295 |
| `06-eigenverwaltung-und-schutzschirm` | Eigenverwaltung Paragrafen 270 ff. InsO, Eigenverwaltungsplanung Paragraf 270a, Schutzschirmverfahren Paragraf 270d, Sachwalter Paragraf 274 |
| `07-insolvenzplan-bestaetigen` | Insolvenzplanverfahren Paragrafen 217 ff. InsO: Vorprüfung Paragraf 231, Anhörung, Erlaeuterungs- und Abstimmungstermin Paragrafen 235-238, gerichtliche Bestätigung Paragraf 248, Minderheitenschutz Paragraf 251 |
| `08-starug-restrukturierungssache-anzeigen` | Anzeige Restrukturierungssache Paragrafen 31 ff. StaRUG, Restrukturierungsbeauftragter Paragraf 73 StaRUG, Restrukturierungsforum, öffentliche oder nicht-öffentliche Sache |
| `09-starug-stabilisierungsanordnung` | Stabilisierungsanordnung Paragrafen 49 ff. StaRUG (Vollstreckungs- und Verwertungssperre), Voraussetzungen, Dauer (drei Monate, Verlaengerung), Schutzbereich, Folgenanordnung |
| `10-starug-planbestaetigung-und-folgen` | Planabstimmung Paragrafen 17 ff. StaRUG, gruppeninternes Mehrheitserfordernis, gruppenübergreifender Cramdown Paragraf 26 StaRUG, gerichtliche Planbestätigung Paragrafen 60 ff., Wirkungen Paragraf 67 |
| `99-finale-entscheidung-volltext` | Erzeugt die finale entscheidung als volltext (beschluss insolvenz oder restrukturierung) als versandfertigen Volltext mit Rubrum, Tenor, Tatbestand, Entscheidungsgründen, Nebenentscheidungen und Rechtsmittelbelehrung. |
| `prozessuale-kniffe-und-rechtsprechungsanker` | Bündelt insolvenzgerichtliche Prozesskniffe zu Eröffnungsprüfung, Sicherungsmaßnahmen, Gutachten, Eigenverwaltung, Plan, Gläubigerschutz und Beschluss. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
