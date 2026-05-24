---
name: stb-warnschreiben-krisensignale
description: Schreibvorlage Steuerberater an Mandanten-Geschaeftsfuehrung bei Krisensignalen aus Bilanz BWA SuSa Liquiditaet. Pflichthinweis nach BGH IX ZR 285/14 und IX ZR 64/12 (Steuerberater-Hinweispflicht bei erkennbarer Krise) zur eigenen Haftungsvermeidung. Klare Bezugnahme auf § 15a InsO Antragspflicht (3 Wochen Zahlungsunfaehigkeit 6 Wochen Ueberschuldung) und § 102 StaRUG Krisenfrueherkennung. Empfehlung anwaltlicher Beratung. Keine eigene Rechtsberatung (§ 5 RDG). Eingangsbestaetigung dokumentiert.
---

# Warnschreiben Steuerberater an Mandant bei Krisensignalen

## Zweck

Dieser Skill erstellt das **schriftliche Warnschreiben** des Steuerberaters an die Geschäftsführung einer GmbH/UG, wenn aus der laufenden Buchhaltungsbetreuung Krisensignale erkennbar werden — typisch im Anschluss an `stb-bwa-sus-bilanz-pruefung`, `stb-ueberschuldungspruefung-19-inso` oder `stb-liquiditaetsvorschau-3wochen` mit gelber oder roter Ampel.

> Der Hinweis ist **keine Rechtsberatung** (§ 5 RDG). Er erfüllt die **Sorgfaltspflicht des Steuerberaters** nach BGH IX ZR 285/14 und IX ZR 64/12 — wer Krisensignale erkennt und nicht hinweist, haftet für die Verschleppungsschäden.

## Eingaben

- Mandant (Firma, HRB, Vertretungsverhältnisse)
- Ermittlungsstichtag (typisch: Stichtag der ausgewerteten BWA/Bilanz/SuSa)
- Identifizierte Krisensignale aus vorgelagertem Skill (mit Belegen)
- Vorherige Hinweise dokumentiert? (Wenn ja: dieser ist ein nachgehender Hinweis)
- Mandantenkommunikationskanal (Brief mit Einschreiben/Rückschein, beA an Mandantenvertretung, persönliche Übergabe)
- Datum der Versendung und gewählter Zustellweg

## Rechtlicher Rahmen

### Primärnormen

- **§ 1 Abs. 2 i.V.m. § 33 StBerG** — Steuerberater hat im Rahmen seines Auftrags umfassend zu beraten und vor Schäden zu warnen.
- **§ 5 RDG** — Nebenleistungspflicht: rechtliche Hinweise sind zulässig, soweit sie zur Erfüllung der steuerberatenden Hauptleistung gehören. **Keine eigene Rechtsberatung** zur Insolvenzantragspflicht — Empfehlung anwaltlicher Beratung ist Pflichtbestandteil.
- **§ 15a Abs. 1 InsO** — Insolvenzantragspflicht der GmbH-Geschäftsführung: bei Zahlungsunfähigkeit **drei Wochen**, bei Überschuldung **sechs Wochen** ab Eintritt.
- **§ 15b InsO** — Zahlungsverbote nach Insolvenzreife (löste § 64 GmbHG a.F. ab; SanInsFoG, 1.1.2021).
- **§ 102 StaRUG** — Krisenfrüherkennungspflicht der Geschäftsleitung haftungsbeschränkter Gesellschaften; ergänzt § 91 Abs. 2 AktG analog.
- **§ 627 BGB** — Vertrauensstellung Steuerberatungsvertrag; Hinweis-/Aufklärungspflicht als Hauptpflicht.

### Leitentscheidungen

- BGH, Urt. v. 26.1.2017 — **IX ZR 285/14** ("Steuerberater-Haftung wegen unterlassener Krisenwarnung"): Steuerberater haftet für Insolvenzverschleppungsschäden, wenn er aus der Buchhaltung Krisensignale erkennt und nicht hinweist. Maßstab: erkennbarer rechnerischer Überschuldungsstatus oder anhaltende Zahlungsstockung.
- BGH, Urt. v. 7.3.2013 — **IX ZR 64/12** (Hinweispflicht bei drohender Insolvenzreife): Bereits **drohende** Insolvenzreife begründet die Hinweispflicht — nicht erst die manifeste Antragspflicht.
- BGH, Urt. v. 6.6.2019 — **IX ZR 104/18** (Maßstab der erkennbaren Krisensignale; Substantiierungslast Steuerberater).
- BGH, Urt. v. 14.10.2010 — **IX ZR 153/09** (Steuerberater muss auf Schäden aus Geschäftsführerhaftung hinweisen).

## Vorgehen

### 1. Krisensignale benennen

Auflisten, **welche konkreten Befunde** der Steuerberater ermittelt hat. Beispiele:

- Negatives Eigenkapital seit Stichtag XX.XX.XXXX (Aktiva EUR …, Passiva EUR …, Differenz EUR …).
- Anhaltende Unterdeckung Lohnsteuer-/Sozialversicherungsbeiträge.
- Wiederholte Stundungsanträge Finanzamt / Sozialversicherung in letzten n Monaten.
- 3-Wochen-Liquidität nach BGH-Passiva-II-Schema (`stb-liquiditaetsvorschau-3wochen`): Lückenquote ≥ 10 %.
- Fortbestehensprognose `stb-ueberschuldungspruefung-19-inso`: negativ wegen fehlendem Sanierungskonzept.
- Krise nach IDW S 6 — Strategiekrise / Ertragskrise / Liquiditätskrise.

### 2. Rechtliche Einordnung — bewusst zurückhaltend

Steuerberater **nennt** § 15a InsO, § 102 StaRUG und § 15b InsO als anwendbare Normen, **beurteilt sie aber nicht eigenständig**. Die anwaltliche Beratungsempfehlung ist Pflichtbestandteil.

### 3. Empfehlung mit Frist

- **Anwaltliche Beratung** (Fachanwalt für Insolvenz-/Sanierungsrecht oder Fachanwalt für Steuerrecht mit Sanierungserfahrung) **binnen einer Woche** terminieren.
- **Sanierungskonzept nach IDW S 6** bei anhaltender Krise erstellen lassen.
- **Liquiditätsplanung** auf rollierender 13-Wochen-Basis (`stb-liquiditaetsvorschau-3wochen` oder Power-Plugin `liquiditaetsplanung`) wöchentlich aktualisieren.
- **Eigene Dokumentation** des GF (§ 102 StaRUG verlangt nachweisbare Krisenfrüherkennung).

### 4. Eigene Haftungsabsicherung

- **Schriftlich** versenden (Einschreiben/Rückschein, beA an Mandantenanwalt oder vergleichbar nachweisbarer Zustellweg).
- **Eingangsbestätigung** anfordern und in Mandatsakte ablegen.
- **Kein ELSTER-Versand** (ELSTER ist Kommunikationskanal zur Finanzbehörde, nicht zum Mandanten).
- **Bei ausbleibender Reaktion** binnen zwei Wochen: erneutes Schreiben mit explizitem Hinweis auf eigene Berufshaftpflicht-Pflichten. Dokumentation Wiedervorlage.

### 5. Mandatskündigung als ultima ratio

Wenn der Mandant trotz mehrfacher schriftlicher Hinweise keine anwaltliche Beratung einholt und der Steuerberater die Aussichten als manifest insolvenzverschleppend einschätzt: **Mandatsniederlegung** prüfen (§ 627 BGB; gestaffelt). Dokumentation zwingend.

## Muster-Warnschreiben (verkürzt)

```
[Steuerberater-Briefkopf]                                       [Datum]

PERSÖNLICH / VERTRAULICH

[Mandant — GmbH, vertreten durch Geschäftsführer/in Name]
[Anschrift]

Vorab per Telefax / Einschreiben mit Rückschein

Hinweis zur erkennbaren Krisensituation Ihrer Gesellschaft

Sehr geehrte/r Frau / Herr [Name],

aus der von uns für Sie geführten laufenden Finanzbuchhaltung und der von
uns aufgestellten betriebswirtschaftlichen Auswertung zum Stichtag [Datum]
ergeben sich folgende Krisensignale:

1. [Konkretes Signal 1 mit Bezifferung — z. B. negatives Eigenkapital
   EUR XXX zum Stichtag XX.XX.XXXX].
2. [Konkretes Signal 2 — z. B. anhaltende Unterdeckung Lohnsteuer/SV].
3. [Konkretes Signal 3 — z. B. Liquiditaetsluecke 3-Wochen-Schema XX %].

Diese Signale begruenden den Verdacht einer Krise nach IDW S 6 und
gegebenenfalls einer Insolvenzreife im Sinne von §§ 17 oder 19 InsO. Sie
sind als Geschaeftsfuehrer/in nach § 15a Abs. 1 InsO verpflichtet, bei
Zahlungsunfaehigkeit innerhalb von drei Wochen, bei Ueberschuldung
innerhalb von sechs Wochen Insolvenzantrag zu stellen. Zudem trifft Sie
nach § 102 StaRUG die Pflicht zur Krisenfrueherkennung und zum Ergreifen
geeigneter Gegenmassnahmen.

Wir leisten Ihnen mit diesem Schreiben den uns als Steuerberater nach
staendiger Rechtsprechung des Bundesgerichtshofs obliegenden Hinweis
(zuletzt BGH, Urt. v. 26.01.2017 — IX ZR 285/14). Eine rechtliche
Beurteilung der Insolvenzantragspflicht ist uns als Steuerberater nach
§ 5 RDG nicht erlaubt.

Wir empfehlen Ihnen mit Nachdruck, **binnen einer Woche**:

- eine/n Fachanwaltin/Fachanwalt fuer Insolvenz- und Sanierungsrecht
  oder fuer Steuerrecht mit Sanierungserfahrung zu konsultieren;
- ein Sanierungskonzept nach IDW S 6 erstellen zu lassen, soweit eine
  Fortfuehrungsperspektive besteht;
- eine rollierende 13-Wochen-Liquiditaetsplanung einzurichten, sofern
  noch nicht vorhanden, und uns wochentlich uebermitteln zu lassen;
- saemtliche Krisenfrueherkennungs-Massnahmen nach § 102 StaRUG schriftlich
  zu dokumentieren.

Bitte bestaetigen Sie uns den Eingang dieses Schreibens innerhalb von
sieben Tagen schriftlich. Bei Ausbleiben der Reaktion behalten wir uns
weitere Schritte vor.

Mit freundlichen Gruessen

[Unterschrift]
[Steuerberater/in]
[Berufsbezeichnung, Kammer]
```

## Eingangsbestätigung / Wiedervorlage

| Datum | Aktion | Empfangsbeleg | Reaktion Mandant |
|---|---|---|---|
| TT.MM.JJJJ | Erstes Warnschreiben | Einschreiben/Rückschein Nr. … | … |
| TT.MM.JJJJ | Erinnerung (bei Ausbleiben) | … | … |
| TT.MM.JJJJ | Telefonat dokumentiert | … | … |
| TT.MM.JJJJ | Ggf. Mandatsniederlegung | … | — |

## Querverweise

- `stb-bwa-sus-bilanz-pruefung` — Eingangs-Auswertung
- `stb-ueberschuldungspruefung-19-inso` — Pflichtprüfung vor Warnschreiben
- `stb-liquiditaetsvorschau-3wochen` — Liquiditätsdaten als Beleg
- `liquiditaetsplanung` (separates Power-Plugin) — gerichtsfeste insolvenzrechtliche Liquiditätsbilanz
- `anw-haftungswarn-15a-inso-mandant` — anwaltliche Spiegelvariante (typisch nachgelagert, wenn Mandant anwaltlich vertreten ist)

## Quellen und Updates

Stand: 05/2026. BGH-Hinweispflichtrechtsprechung (IX ZR 285/14, IX ZR 64/12, IX ZR 104/18) zentral. SanInsFoG-Reform berücksichtigt (§ 15b InsO statt § 64 GmbHG a.F.). § 102 StaRUG seit 1.1.2021 in Kraft. Bei Änderung StBerG/RDG oder Verschärfung der Hinweispflicht aktualisieren.
