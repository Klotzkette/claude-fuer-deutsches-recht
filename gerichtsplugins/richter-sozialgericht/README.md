# Sozialgericht

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Sozialgericht: Klagearten Anfechtungs- und Leistungsklage einstweiliger Rechtsschutz Paragraf 86b SGG Amtsermittlung sozialrechtliche Prüfungsschemata Krankenversicherung Rente Unfall Bürgergeld Schwerbehinderung Urteilsentwurf mit Tenorvorschlag

Dieses Plugin gehört zum Marketplace mit 232 Plugins für deutsches Recht. Es bündelt die zugehörigen Skills, Prüfraster, Vorlagen und Arbeitsroutinen in einem installierbaren Plugin-ZIP. Die zwei Markdown-Prompts sind vollwertige Ein-Datei-Starts für den Fall, dass kein Plugin-Setup genutzt werden soll: Werkstatt für den ausführlichen Arbeitsmodus, Schnellstart für den kompakten Einstieg.

Schneller Weg: Für eine erste Ergebnisrichtung den Schnellstart laden, für einen tragfähigen Arbeitsmodus die Werkstatt. Beide Prompts sollen mit einem konkreten Arbeitsprodukt beginnen, nur eng nachfragen und nicht in einer Materialinventur hängen bleiben.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`richter-sozialgericht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/richter-sozialgericht.zip) |
| Großer Prompt (Werkstatt) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/gerichtsplugins/richter-sozialgericht/richter-sozialgericht-werkstatt.md" download><code>richter-sozialgericht-werkstatt.md</code></a> |
| Kleiner Prompt (Schnellstart) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/gerichtsplugins/richter-sozialgericht/richter-sozialgericht-schnellstart.md" download><code>richter-sozialgericht-schnellstart.md</code></a> |
| Testakte(n) als ZIP | ZIP | Hilfsmittelstreit Elektrorollstuhl Heinz Körner gegen Weser-Ems Gesundheitskasse: [Gesamt-PDF](../../testakten/sozialrecht-elektrorollstuhl-koerner-oldenburg/gesamt-pdf/sozialrecht-elektrorollstuhl-koerner-oldenburg_gesamt.pdf), [`testakte-sozialrecht-elektrorollstuhl-koerner-oldenburg.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-sozialrecht-elektrorollstuhl-koerner-oldenburg.zip), [`testakte-sozialrecht-elektrorollstuhl-koerner-oldenburg-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-sozialrecht-elektrorollstuhl-koerner-oldenburg-einzelpdfs.zip); Pluginlokale Akte: [Gesamt-PDF](testakte/gesamt-pdf/testakte_gesamt.pdf), [`richter-sozialgericht-testakte.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/richter-sozialgericht-testakte.zip), [`richter-sozialgericht-testakte-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/richter-sozialgericht-testakte-einzelpdfs.zip) |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 232 Plugins. Wer alle Plugins auf einmal will, nimmt `alle-plugins-megazip.zip`. Wer nur einzelne Werkstatt- oder Schnellstart-Prompts will, nimmt die Markdown-Downloads.
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du einen Sozialleistungsbescheid angreifen und den Anspruch durchsetzen.
> **Experimentelles Plugin im Ordner `gerichtsplugins/`** — siehe Vorspruch unten.

> **Kritisch — Hochrisiko-KI und Art. 22 DSGVO beachten.** Der Einsatz von KI in der Rechtspflege ist nach Art. 6 Abs. 2 in Verbindung mit Anhang III Nr. 8 Buchstabe a der KI-Verordnung (VO (EU) 2024/1689) grundsätzlich **Hochrisiko-KI**. Die Rückausnahme des Art. 6 Abs. 3 KI-VO greift nur bei rein vorbereitender Tätigkeit ohne Subsumtion; auch dann besteht Registrierungspflicht nach Art. 49 Abs. 2 KI-VO. Eine Entscheidung mit rechtlicher Wirkung über Menschen darf nicht einer Maschine überlassen werden (Art. 22 DSGVO) — die richterliche Letztentscheidung liegt zwingend beim Menschen. Einzelheiten unten unter „Wichtiger Hinweis vor Verwendung".

## Rolle

Sozialrichter als Einzelrichter oder Kammer (Paragrafen 12, 31 SGG); mit ehrenamtlichen Richtern in muendlicher Verhandlung

## Rechtsrahmen

SGG, SGB I-XIV, BVG, AsylbLG, GKG-Sozial, RVG

## Inhalt

- **11 Skills** (siehe `skills/`; inklusive Schnellstart-Skill)
- **Werkstatt-Prompt** (`richter-sozialgericht-werkstatt.md`)
- **Schnellstart-Prompt** (`richter-sozialgericht-schnellstart.md`)
- **Testakte** (`testakte/README.md`) — aus Richtersicht

## Skill-Liste

- **01-zulässigkeit-sozialklage** — Zulässigkeit Paragrafen 51 ff. SGG: Rechtsweg, Klagearten (Anfechtung Leistung Untaetigkeit Feststellung), Vorverfahren
- **02-amtsermittlung-sozialgericht** — Amtsermittlungsgrundsatz Paragraf 103 SGG: Beweisaufnahme von Amts wegen, Sachverständigengutachten Paragraf 109 SGG (A
- **03-eilrechtsschutz-paragraf-86b** — Einstweiliger Rechtsschutz Paragraf 86b SGG: Anordnung der aufschiebenden Wirkung Abs. 1, einstweilige Anordnung Abs. 2
- **04-krankenversicherung-pruefung** — Krankenversicherung SGB V: Versicherungspflicht Paragraf 5, Leistungsanspruch Paragraf 27 (Krankenbehandlung), Hilfsmitt
- **05-rentenversicherung-pruefung** — Gesetzliche Rentenversicherung SGB VI: Altersrente Paragrafen 35 ff., Erwerbsminderungsrente Paragraf 43, Wartezeit, Min
- **06-unfallversicherung-pruefung** — Gesetzliche Unfallversicherung SGB VII: Arbeitsunfall Paragraf 8, Berufskrankheit Paragraf 9, Versicherte Paragraf 2, He
- **07-buergergeld-und-sgb-ii** — Buergergeld SGB II: Anspruchsberechtigung Paragraf 7 SGB II, Bedarfsgemeinschaft, Regelbedarf Paragraf 20, Kosten der Un
- **08-schwerbehinderung-und-grad** — Schwerbehindertenrecht SGB IX: Grad der Behinderung Paragraf 152, Versorgungsmedizinverordnung (VersMedV), Merkzeichen,
- **09-urteil-sozialgericht** — Urteil Paragrafen 132 ff. SGG: Tenor (Aufhebung, Verurteilung zur Leistung, Bescheidung), Tatbestand, Entscheidungsgruen
- **10-entscheidungsvorschlag-sozialgericht** — Strukturierter Entscheidungsvorschlag: Tenor-Skizze, sozialrechtliche Anspruchsprüfung, medizinische Beweiswürdigung,

## Wichtiger Hinweis vor Verwendung

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

Automatisch generierte Komplett-Liste aller 13 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `01-zulaessigkeit-sozialklage` | Zulässigkeit Paragrafen 51 ff. SGG: Rechtsweg, Klagearten (Anfechtung Leistung Untaetigkeit Feststellung), Vorverfahren Paragraf 78, Klagefrist Paragraf 87, Klagebefugnis |
| `02-amtsermittlung-sozialgericht` | Amtsermittlungsgrundsatz Paragraf 103 SGG: Beweisaufnahme von Amts wegen, Sachverständigengutachten Paragraf 109 SGG (Anhörung eines bestimmten Arztes), Beiziehung medizinischer Unterlagen |
| `03-eilrechtsschutz-paragraf-86b` | Einstweiliger Rechtsschutz Paragraf 86b SGG: Anordnung der aufschiebenden Wirkung Abs. 1, einstweilige Anordnung Abs. 2 (Anordnungsanspruch und -grund), Existenzsicherung in Eilfaellen |
| `04-krankenversicherung-pruefung` | Krankenversicherung SGB V: Versicherungspflicht Paragraf 5, Leistungsanspruch Paragraf 27 (Krankenbehandlung), Hilfsmittel Paragraf 33, Krankengeld Paragraf 44, ambulante und stationaere Behandlung |
| `05-rentenversicherung-pruefung` | Gesetzliche Rentenversicherung SGB VI: Altersrente Paragrafen 35 ff., Erwerbsminderungsrente Paragraf 43, Wartezeit, Mindestbeitragszeiten, Hinterbliebenenrente |
| `06-unfallversicherung-pruefung` | Gesetzliche Unfallversicherung SGB VII: Arbeitsunfall Paragraf 8, Berufskrankheit Paragraf 9, Versicherte Paragraf 2, Heilbehandlung Paragraf 27, Verletztenrente Paragraf 56 |
| `07-buergergeld-und-sgb-ii` | Buergergeld SGB II: Anspruchsberechtigung Paragraf 7 SGB II, Bedarfsgemeinschaft, Regelbedarf Paragraf 20, Kosten der Unterkunft Paragraf 22, Sanktionen Paragraf 31 ff. (jetzt Leistungsminderungen) |
| `08-schwerbehinderung-und-grad` | Schwerbehindertenrecht SGB IX: Grad der Behinderung Paragraf 152, Versorgungsmedizinverordnung (VersMedV), Merkzeichen, Gleichstellung, Nachteilsausgleiche |
| `09-urteil-sozialgericht` | Urteil Paragrafen 132 ff. SGG: Tenor (Aufhebung, Verurteilung zur Leistung, Bescheidung), Tatbestand, Entscheidungsgründe, Nebenentscheidungen Paragrafen 193 ff. SGG (Kosten), Berufung an LSG, Revision an BSG |
| `10-entscheidungsvorschlag-sozialgericht` | Strukturierter Entscheidungsvorschlag: Tenor-Skizze, sozialrechtliche Anspruchsprüfung, medizinische Beweiswürdigung, soziale Faktoren, Risikohinweise, ausdrücklich zur richterlichen Prüfung markiert |
| `99-finale-entscheidung-volltext` | Erzeugt die finale entscheidung als volltext (urteil sozialgericht) als versandfertigen Volltext mit Rubrum, Tenor, Tatbestand, Entscheidungsgründen, Nebenentscheidungen und Rechtsmittelbelehrung. |
| `prozessuale-kniffe-und-rechtsprechungsanker` | Führt öffentlich-rechtliche Verfahrenskniffe zu Amtsermittlung, Gehör, Eilrechtsschutz, Beiladung, Präklusion, Tenor und Begründung zusammen. |
| `v392-praxisraster-richter-sozialgericht` | Praxisraster für Sozialgericht: Zuständigkeit, Verfahrensstand, Pflichtnormen, Beweisbedarf und passendes Endprodukt werden in der richtigen gerichtlichen oder staatsanwaltschaftlichen Rolle abgearbeitet. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
