---
name: mandat-triage-verkehrsrecht
description: Strukturierte Eingangs-Abfrage fuer verkehrsrechtliche Mandate. Klaert Verfahrensart (Zivilrecht Schadensregulierung OWi-Bussgeldverfahren Strafrecht Verkehrsstraftaten Fahrerlaubnis MPU Versicherungsstreit) Unfallart (Personenschaden Sachschaden beidseitige Betriebsgefahr) Fristen-Sofort-Check (Einspruch Bussgeldbescheid zwei Wochen § 67 OWiG Verjaehrung drei Jahre § 195 BGB) Versicherungslage (Haftpflicht Kasko Rechtsschutz) und Eilbeduerftigkeit (vorlaeufige Entziehung Fahrerlaubnis § 111a StPO Fahrtenbuch-Auflage Strafanzeige). Routing zu unfall-haftungsquote-berechnen oder zu Bussgeld-Skill.
---

# Mandat-Triage Verkehrsrecht

## Zweck

Verkehrsrechtliche Mandate sind heterogen — vom Auffahrunfall (Zivilrecht) über Geschwindigkeit (OWi) bis zur Verkehrsunfallflucht (Strafrecht). Strukturierte Triage stellt richtige Spur sicher.

## Ablauf — sieben Fragen

### Frage 1 — Wer ruft und für wen?

- Selbst Unfallbeteiligter
- Angehöriger
- Versicherer (Verteidigungsmandat)
- Anderer Anwalt (Vertretung)

### Frage 2 — Verfahrensart?

- **Zivilrechtlich** Schadensregulierung
- **Owi** Bußgeldbescheid wegen Geschwindigkeit Rotlicht Abstand Handy am Steuer Trunkenheit
- **Strafrechtlich** Verkehrsstraftat (§ 315c StGB Gefährdung § 315d Raserfälle § 142 Unfallflucht § 316 § 315a Trunkenheit § 229 fahrlässige Körperverletzung § 222 fahrlässige Tötung)
- **Fahrerlaubnisrecht** vorläufige Entziehung Wiedererteilung MPU
- **Versicherungsrecht** Deckungsablehnung Kasko Haftpflicht
- **Fahrerlaubnisrecht-Punkte** Fahreignungsregister (FAER) Tilgung

### Frage 3 — Akute Eilbedürftigkeit?

- Vorläufige Entziehung Fahrerlaubnis § 111a StPO — sofort Beschwerde § 304 StPO
- Berufstätigkeit auf Führerschein angewiesen — Härtefall-Argumentation
- Fahrtenbuch-Auflage drohend
- Hauptverhandlung Strafrecht binnen Tagen

### Frage 4 — Unfall: Personen- oder Sachschaden?

- Sachschaden — Standard-Regulierung
- Personenschaden — zusätzliche Quoten Schmerzensgeld Vorhaltekosten Heilbehandlungskosten Renten-Anspruch
- Bei Personenschaden sofort SV-Träger informieren (Krankenkasse BG)

### Frage 5 — Versicherungslage?

- Eigene Haftpflicht (Vollkasko)
- Verkehrsrechtsschutz (Deckungszusage einholen)
- Insassenunfallversicherung
- Gegnerische Versicherung bekannt?

### Frage 6 — Frist?

- **Einspruch Bußgeldbescheid** zwei Wochen § 67 OWiG
- **Anhörung im Bußgeldverfahren** keine zwingende Frist aber Bedeutung der Aussage
- **Verjährung zivilrechtlicher Anspruch** drei Jahre § 195 BGB
- **Verjährung Personenschaden** dreißig Jahre § 199 Abs. 2 BGB
- **Punkte-Tilgung** Fahreignungsregister
- **Wiedererteilung Fahrerlaubnis** Sperrfrist § 69a StGB

### Frage 7 — Hauptaktenstand?

- Polizeiprotokoll vorhanden?
- Schadensgutachten vorhanden?
- Anhörungsbogen StA / Bußgeldstelle?
- Bisheriger Schriftwechsel mit Versicherung?

## Routing-Matrix

| Verfahrensart | Folge-Skill | Frist-Sofort-Check |
|---|---|---|
| Schadensregulierung Sachschaden | `unfall-haftungsquote-berechnen` | Verjährung drei Jahre |
| Schadensregulierung Personenschaden | `unfall-haftungsquote-berechnen` plus medizinische Begutachtung | drei oder dreißig Jahre |
| Bußgeldbescheid | (Skill bußgeld-prüfen — perspektivisch) | zwei Wochen § 67 OWiG |
| Vorläufige Entziehung FE | sofort Beschwerde § 304 StPO | binnen Stunden |
| Verkehrsstraftaten | Skill aus `fachanwalt-strafrecht` `mandat-triage-strafrecht` | je nach Verfahrensstadium |
| MPU | (Skill mpu-vorbereitung — perspektivisch) | sechs Monate vor Frist Beginn |
| Punkte | (Skill faer-prüfen — perspektivisch) | Tilgungsfristen |
| Versicherungs-Deckungsstreit | Skill aus `fachanwalt-versicherungsrecht` | nach VVG |

## Eilmodus vorläufige Entziehung

Bei Fahrerlaubnis-vorläufig-entzogen § 111a StPO:

- **Beschwerde § 304 StPO** statthaft
- Hilfsweise Antrag auf Aufhebung beim selben Gericht
- Eilbedürftigkeit Beruf häufig führt zu Beschluss in der Sache
- Bei Hauptverhandlung Plädoyer auf Aussetzung § 69a StGB Sperrfrist nicht erforderlich

## Mandatsannahme

- **Konflikt-Check** — kein anderer Mandant in derselben Sache (Unfallgegner Versicherer Mitfahrer)
- **Streitwert** ab EUR 10000 LG; darunter AG (Streitwertgrenze zehntausend Euro seit 01.01.2026 Justizreform)
- **Komplexität** Personenschaden Eigentums-Streit über Halterstellung Auslandsbezug Lkw-Frachtrecht

## Eskalation

- **Telefon-Sofort** vorläufige FE-Entziehung
- **Binnen einer Stunde** Verkehrsunfallflucht-Anhörung
- **Heute** Versicherungs-Reaktion auf Deckungsablehnung Akteneinsicht Bußgeld
- **Diese Woche** Klageeinreichung Schadensregulierung Einspruch Bußgeld

## Ausgabe

- `triage-protokoll-verkehrsrecht.md`
- Aktenanlage Az-Vorschlag
- Frist im Fristenbuch
- Rechtsschutz-Deckungsanfrage als Entwurf
- Mandatsvereinbarung Vorlage
- Empfehlung Folge-Skill

## Quellen

- StVG StVO StPO §§ 111a 304
- StGB §§ 142 222 229 315a 315c 315d 316 69 69a
- OWiG § 67 (Einspruch)
- VVG §§ 28 86 115
- BGH VI. Zivilsenat 4. Strafsenat
