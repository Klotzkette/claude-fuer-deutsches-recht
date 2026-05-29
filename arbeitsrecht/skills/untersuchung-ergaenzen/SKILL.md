---
name: untersuchung-ergaenzen
description: "Fügt einer laufenden internen Untersuchung neue Daten hinzu — Dokumente, Befragungsnotizen oder Beobachtungen. Verarbeitet Dokumentenpakete anhand dokumentierter Auswahlkriterien, markiert relevante Funde und protokolliert alles Gesichtete zur Deckungsverifikation. Lädt, wenn neue Beweise, Befragungsnotizen oder Dokumentenlieferungen für eine laufende Untersuchung eingehen."
---

# Untersuchungs-Datenpflege (Arbeitsrecht)

## Zweck

Fügt Daten in ein laufendes Untersuchungsprotokoll ein. Verarbeitet
Dokumentenpakete anhand dokumentierter Auswahlkriterien (§ 26 BDSG —
Verhältnismäßigkeit), markiert relevante Funde, protokolliert alle
gesichteten Unterlagen zur Deckungsverifikation.

Lädt, wenn neue Erkenntnisse, Befragungsnotizen oder Dokumentenlieferungen
für eine laufende Untersuchung zur Verarbeitung eingehen.

## Eingaben

- Bezeichnung der Untersuchungssache (oder Slug)
- Art der Daten: Befragungsnotizen / Dokumentenpaket / Anwaltsnotizen /
  Bestätigung Anhörungshinweis
- Inhalt der Daten (eingefügt oder angehängt)

## Rechtlicher Rahmen

**Kernvorschriften:**

- § 26 BDSG: Verarbeitung von Beschäftigtendaten zur Aufdeckung von
  Straftaten oder schwerwiegenden Pflichtverletzungen — Verhältnismäßigkeit
  ist Voraussetzung; Verarbeitung nur soweit zur Sachaufklärung erforderlich
- Art. 5 Abs. 1 lit. c DSGVO: Datenminimierungsgrundsatz — nur notwendige
  Daten erheben und verarbeiten
- § 87 Abs. 1 Nr. 6 BetrVG: Mitbestimmung bei technischen Überwachungseinrichtungen
  — vor Auswertung von E-Mails oder IT-Kommunikation ist Zustimmung des
  Betriebsrats oder eine einschlägige Betriebsvereinbarung erforderlich
- § 626 BGB: Außerordentliche Kündigung; Frist des § 626 Abs. 2 BGB (zwei
  Wochen ab Kenntnis) — Dokumentation des Zeitpunkts des Kenntniserwerbs ist
  untersuchungskritisch
- § 241 Abs. 2 BGB: Mitwirkungspflicht des Arbeitnehmers im Rahmen
  des Untersuchungsverfahrens; Grenzen bei Selbstbelastung

**Leitentscheidungen:**

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
  Beweisverwertungsverbot bei rechtswidrig erlangten Dokumenten — heimliche
  Videoüberwachung ohne Betriebsratsinhaber führt zum Verwertungsverbot
  auch im Kündigungsschutzprozess; Grundsatz gilt sinngemäß für
  rechtswidrig ausgewertete Kommunikation
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
  Verdachtskündigung — Anforderungen an die Dokumentation des Tatverdachts;
  objektive Schwere; inhaltliche Mindestanforderungen an die Anhörung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
  Erstattungsfähigkeit von Untersuchungskosten (Detektivkosten) — nur bei
  konkreter Verdachtslage bei Beauftragung und Verhältnismäßigkeit

- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.

- Gola/Heckmann/Schomerus, BDSG, 13. Aufl. 2022, § 26 Rn. 120 ff.:
  Zulässigkeitsvoraussetzungen der Datenverarbeitung zur Straftatenaufdeckung;
  Verhältnismäßigkeitsmaßstab; Dokumentationspflichten
- Erfurter Kommentar/Kania, 24. Aufl. 2024, § 87 BetrVG Rn. 62 ff.:
  Mitbestimmung bei IT-Auswertung und technischen Überwachungseinrichtungen
- Erfurter Kommentar/Müller-Glöge, 24. Aufl. 2024, § 626 BGB Rn. 230 ff.:
  Zwei-Wochen-Frist des § 626 Abs. 2 BGB; Beginn; Dokumentation

## Ablauf

**Schritt 1 — Kontext laden**

Lese `CLAUDE.md` im Plugin-Verzeichnis.

**Schritt 2 — Sache identifizieren**

Falls mehrere Untersuchungsordner existieren: Frage, zu welcher Sache die
Daten gehören. Bei nur einer Sache: direkt fortfahren.

**Schritt 3 — Referenz-Skill laden**

Lade die Referenz-Skill `interne-untersuchung` und führe Modus 2 (Daten
hinzufügen) aus.

**§ 87 Abs. 1 Nr. 6 BetrVG-Check vor Dokumentenverarbeitung:**
Bei E-Mail- oder IT-Auswertungen: Prüfe, ob eine einschlägige
Betriebsvereinbarung vorliegt oder der Betriebsrat zugestimmt hat.
Falls unklar — flaggen, bevor Verarbeitung beginnt.

**Schritt 4 — Nach Verarbeitung melden**

Zeige Oberflächenrate und Liste relevanter Funde:

```
Dokumentenprüfung abgeschlossen.
Geprüft: [N] Dokumente
Relevant: [N]
Geprüft / nicht relevant: [N]
Neue Beweislücken: [N]

Relevante Funde:
  - [Kurzbeschreibung] → Auswahlkriterium: [Nr.]
  - [Kurzbeschreibung] → Auswahlkriterium: [Nr.]
```

**Schritt 5 — Quellencheckliste aktualisieren**

Wenn die hinzugefügten Daten einen Checklistenpunkt abdecken: Anwalt fragen,
ob der Punkt als "erledigt" oder "in Bearbeitung" markiert werden soll.
Nicht automatisch als erledigt markieren — der Anwalt entscheidet, wann eine
Quelle ausreichend abgedeckt ist.

**§ 626 Abs. 2 BGB-Kenntnisdatum:**
Bei Befragungsnotizen oder Dokumenten, die erstmals den konkreten Tatverdacht
begründen oder wesentlich vertiefen: Datum des Kenntniserwerbs explizit im
Protokolleintrag vermerken. Die Zwei-Wochen-Frist für eine außerordentliche
Kündigung beginnt ab diesem Zeitpunkt zu laufen.

## Ausgabeformat

Zusammenfassung nach Schritt 4 (Zählbericht), dann Aufforderung zur
Aktualisierung der Quellencheckliste falls zutreffend. Bei
§ 626 Abs. 2 BGB-relevantem Kenntnisdatum: gesonderter Hinweisblock.

## Beispiel

```
/arbeitsrecht:untersuchung-ergänzen Sache-Mueller
[Befragungsnotizen aus Gespräch mit Zeugin K. — 12.02.2025]
```

```
/arbeitsrecht:untersuchung-ergänzen Sache-Mueller
[E-Mail-Export 01.01.2025–31.01.2025 — nach BR-Betriebsvereinbarung freigegeben]
```

Beispiel-Ausgabe nach Dokumentenverarbeitung:

```
Dokumentenprüfung abgeschlossen.
Geprüft: 47 Dokumente
Relevant: 5
Geprüft / nicht relevant: 42
Neue Beweislücken: 2

Relevante Funde:
  - E-Mail vom 08.01.2025 Müller an Schmitt: "das solltest du lieber nicht aufschreiben"
    → Auswahlkriterium 4 (implizite Selbstbelastung)
  - E-Mail vom 15.01.2025: widerspricht Schilderung von Zeugin K. in Eintrag #3
    → Auswahlkriterium 5 (Widerspruch zu bestehendem Protokolleintrag)
```

## Risiken und typische Fehler

- **§ 87 Abs. 1 Nr. 6 BetrVG-Versäumnis**: Rechtswidrig ausgewertete
  Kommunikation kann einem Beweisverwertungsverbot unterliegen und die
  Kündigung gefährden. Betriebsvereinbarung vor Auswertung sicherstellen.
- **Verhältnismäßigkeit nach § 26 BDSG**: Massenhafte Dokumentenauswertung
  ohne konkreten Verdacht ist unzulässig. Auswahlkriterien dokumentieren,
  um Verhältnismäßigkeit nachweisen zu können.
- **§ 626 Abs. 2 BGB-Frist**: Die Zwei-Wochen-Frist beginnt ab sicherer
  Kenntnisnahme. Unklare Dokumentation des Kenntniszeitpunkts kann zur
  Fristversäumnis führen.
- **Selektive Protokollierung**: Nur relevante Funde zu protokollieren und
  nicht-relevante Dokumente nicht zu erfassen, untergräbt die Deckungsverifikation.
  Jedes gesichtete Dokument muss protokolliert werden.
- **False Negative durch zu enge Kriterien**: Auswahlkriterien großzügig
  handhaben — ein False Positive (irrelevanter Fund protokolliert) ist
  besser als ein übersehener wesentlicher Beweis.

## Quellenpflicht

Bei Ausgaben zu Dokumentenverarbeitung zitieren:
- § 26 BDSG (Verhältnismäßigkeit, Straftatenaufdeckung)
- § 87 Abs. 1 Nr. 6 BetrVG (Mitbestimmung)
- Art. 5 Abs. 1 lit. c DSGVO (Datenminimierung)
- § 626 Abs. 2 BGB (Zwei-Wochen-Frist, Kenntnisdatum)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Gola/Heckmann/Schomerus, BDSG, 13. Aufl. 2022, § 26 Rn. 120 ff.

Detaillierte Auswahlkriterien, Protokolleintrag-Format und
Deckungsverifikationsregeln befinden sich in der Referenz-Skill
`interne-untersuchung` — diese vor inhaltlicher Arbeit laden.

Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall.

## Ergänzende Rechtsprechung (v14.2)

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Triage — vor der Dateneingabe klären

1. Handelt es sich um neue Zeugenaussagen, Dokumentenlieferung oder anwaltliche Notizen?
2. Liegt eine § 87 Abs. 1 Nr. 6 BetrVG-freigabe für E-Mail-/IT-Auswertungen vor?
3. Begründet die neue Erkenntnis erstmals einen konkreten Tatverdacht? → Dann Kenntnisdatum für § 626 Abs. 2 BGB festhalten!
