---
name: investigation-memo
description: >
  Entwirft den vertraulichen Untersuchungsvermerk aus dem Untersuchungsprotokoll
  oder aktualisiert einen bestehenden Entwurf, wenn neue Daten hinzugekommen
  sind. Lädt, wenn eine Untersuchung weit genug fortgeschritten ist für den
  ersten Entwurf oder wenn neue Erkenntnisse einen bestehenden Entwurf
  veraltet haben.
language: de
triggers:
  - "Untersuchungsmemo"
  - "Untersuchungsvermerk"
  - "Vermerk entwerfen"
  - "Untersuchung zusammenfassen"
  - "Abschlussvermerk"
  - "Memo aktualisieren"
  - "Untersuchungsergebnis dokumentieren"
---

# Untersuchungsvermerk (Arbeitsrecht)

## Zweck

Erstellt den ersten Entwurf des vertraulichen Untersuchungsvermerks aus dem
Untersuchungsprotokoll oder aktualisiert einen bestehenden Entwurf, wenn
seit dem letzten Stand neue Protokolleinträge hinzugekommen sind.

Lädt, wenn eine Untersuchung einen ausreichenden Erkenntnisstand für die
erste Verschriftlichung erreicht hat oder wenn neue Erkenntnisse den
vorhandenen Entwurf überarbeiten.

## Eingaben

- Bezeichnung der Untersuchungssache
- Bei Aktualisierung: Hinweise, welche Teile überarbeitet werden sollen
  (vollständige Überarbeitung oder nur betroffene Abschnitte)

## Rechtlicher Rahmen

**Kernvorschriften:**

- § 626 BGB: Außerordentliche Kündigung aus wichtigem Grund; Zwei-Wochen-Frist
  des § 626 Abs. 2 BGB — der Vermerk dokumentiert den Zeitpunkt der
  gesicherten Kenntnis als Fristbeginn
- §§ 1, 2 KSchG: Allgemeiner Kündigungsschutz — Vermerk als Grundlage für
  verhaltens- oder personenbedingte Kündigung; Sozialauswahl dokumentieren
- § 102 BetrVG: Anhörung des Betriebsrats vor jeder Kündigung — Vermerk
  liefert die Tatsachengrundlage für die BR-Anhörung
- § 26 BDSG: Beschäftigtendatenschutz; Verhältnismäßigkeit der Datenerhebung
  und -verarbeitung — Vermerk muss belegen, dass die Untersuchung verhältnismäßig
  war
- § 22 AGG: Beweislastverteilung bei Diskriminierungsvorwürfen — bei
  AGG-relevantem Sachverhalt dokumentiert der Vermerk, warum keine unzulässige
  Benachteiligung vorliegt

**Leitentscheidungen:**

- BAG, Urt. v. 20.06.2013 – 2 AZR 546/12, NZA 2014, 143 Rn. 14 ff.:
  Verdachtskündigung — dringender Tatverdacht auf Basis objektiver Umstände;
  umfassende Sachaufklärung vor der Kündigung; vorherige Anhörung des
  Arbeitnehmers als zwingend; inhaltliche Mindestanforderungen
- BAG, Urt. v. 23.08.2018 – 2 AZR 133/18, NZA 2018, 1329 Rn. 29 ff.:
  Inhaltliche Anforderungen an die Anhörung vor Verdachtskündigung; Folgen
  fehlerhafter oder unvollständiger Anhörung; Heilungsmöglichkeiten
- BAG, Urt. v. 27.11.2008 – 2 AZR 675/07, NZA 2009, 842 Rn. 20:
  Anforderungen an den Tatsachennachweis bei Tatkündigung —
  Überzeugungsmaßstab im Gegensatz zur Verdachtskündigung; Anforderungen
  an Aufklärung und Dokumentation

**Kommentarliteratur:**

- Erfurter Kommentar/Müller-Glöge, 24. Aufl. 2024, § 626 BGB Rn. 165 ff.:
  Verdachtskündigung — Voraussetzungen, Verfahren, Anhörungsinhalt;
  Tatkündigung im Vergleich
- Erfurter Kommentar/Kiel, 24. Aufl. 2024, § 102 BetrVG Rn. 50 ff.:
  Inhalt der BR-Anhörung; Substantiierungsanforderungen; Folgen
  unvollständiger Mitteilung (Theorie der subjektiven Determinierung)
- HWK/Thüsing, 11. Aufl. 2024, § 1 KSchG Rn. 200 ff.:
  Verhaltensbedingte Kündigung — Pflichtverletzung, Interessenabwägung,
  Dokumentationsstandards

## Ablauf

**Schritt 1 — Referenz-Skill laden**

Lade die Referenz-Skill `internal-investigation` und führe Modus 4
(Vermerk entwerfen oder aktualisieren) aus.

**Schritt 2 — Erstmalige Erstellung: Vorbedingungen prüfen**

Falls noch kein Vermerk existiert — Warnung ausgeben, wenn folgendes
nicht erfüllt ist:
- Mindestens ein Protokolleintrag zu jeder offenen Untersuchungsfrage
- Einträge für Beschwerdeführer/in und Beschuldigte/n vorhanden
- Hochprioritäre offene Quellenchecklisten-Punkte flaggen (nicht blockieren)
- Anhörung der beschuldigten Person dokumentiert (Pflichtvoraussetzung
  für Verdachtskündigung nach § 626 BGB)

**§ 102 BetrVG-Hinweis:** Der Vermerk stellt die Tatsachengrundlage für eine
etwaige BR-Anhörung bereit. Enthält der Vermerk keine vollständige
Sachverhaltsdarstellung, kann eine auf dieser Basis erteilte BR-Anhörung
fehlerhaft sein und die Kündigung unwirksam machen.

**Schritt 3 — Warnen bei hochprioritären offenen Punkten**

Falls hochprioritäre Quellen auf der Checkliste noch offen sind:
explizit benennen, aber nicht blockieren. Anwalt entscheidet, ob der
Entwurf trotzdem erstellt werden soll (z. B. wegen § 626 Abs. 2 BGB-Frist).

**Schritt 4 — Aktualisierung eines bestehenden Entwurfs**

Was sich seit dem letzten Entwurf geändert hat, vor der Überarbeitung melden:

```
Seit dem letzten Vermerksentwurf ([Datum]) wurden dem Protokoll hinzugefügt:

[N] neue Einträge
Neue Untersuchungsfragen: [ja/nein]
Neue Widersprüche: [ja/nein]
Geschlossene Beweislücken: [ja/nein]

Betroffene Abschnitte:
  Sachverhaltliche Feststellungen: [welche Fragen betroffen]
  Glaubwürdigkeitsbewertung: [neue glaubwürdigkeitsrelevante Einträge]
  Ergebnisse: [Befunde, die revidiert werden sollten]
  Anlage A (Chronologie): [N] neue Einträge
```

Fragen: „Soll der gesamte Vermerk überarbeitet werden oder nur die
betroffenen Abschnitte?"

Geänderte Abschnitte mit `[AKTUALISIERT: Datum]` markieren bis zur
anwaltlichen Freigabe.

**Schritt 5 — Alle Ausgaben**

Alle Ausgaben dieser Skill tragen den Kopfzeilen-Vermerk:
`VERTRAULICH — INTERNE UNTERSUCHUNG — NUR ZUR INTERNEN VERWENDUNG`

## Ausgabeformat

Vorbedingungswarnung (falls zutreffend), dann vollständiger Vermerksentwurf
(Struktur: Zusammenfassung, Hintergrund/Umfang, Methodik, Sachverhaltliche
Feststellungen, Glaubwürdigkeitsbewertung, Einschlägige Regelungen,
Ergebnisse, Empfehlungen, Anlagen A und B).

Bei Aktualisierung: Änderungsbericht zuerst, dann überarbeiteter Vermerk.

## Beispiel

```
/arbeitsrecht:investigation-memo Sache-Mueller
```

```
/arbeitsrecht:investigation-memo Sache-Mueller
(aktualisiert bestehenden Entwurf, wenn einer vorhanden ist)
```

Beispiel-Ausgabe bei erster Erstellung mit fehlendem Hochprioritäts-Punkt:

> Warnung: Quellencheckliste: Punkt 2 (Anhörung Beschuldigte/r) ist noch
> offen und als hochprioritär markiert. Bei einer Verdachtskündigung nach
> § 626 BGB ist die vorherige Anhörung der beschuldigten Person zwingende
> Wirksamkeitsvoraussetzung (BAG, Urt. v. 23.08.2018 – 2 AZR 133/18).
> Entwurf trotzdem erstellen? (Antwort: ja/nein)

## Risiken und typische Fehler

- **Anhörung fehlt**: Ohne vorherige Anhörung der beschuldigten Person vor
  Aussprechen einer Verdachtskündigung ist die Kündigung in der Regel
  unwirksam. Anhörungsdokumentation gehört zwingend in den Vermerk.
- **§ 626 Abs. 2 BGB-Frist versäumt**: Vermerk muss Kenntnisdatum klar
  dokumentieren. Spätere Unklarheit über den Fristbeginn kann zur
  Unwirksamkeit der Kündigung führen.
- **BR-Anhörung auf unvollständigem Vermerk**: Eine BR-Anhörung, die nur
  Teile des Sachverhalts wiedergibt, ist fehlerhaft (Theorie der subjektiven
  Determinierung — BAG, ständige Rspr.).
- **Glaubwürdigkeit nicht bewertet**: Wenn Ergebnis von der Frage abhängt,
  welcher Schilderung zu glauben ist, muss eine eigenständige
  Glaubwürdigkeitsbewertung im Vermerk stehen. Fehlende Bewertung schwächt
  die Entscheidungsgrundlage.
- **AGG-Benachteiligung nicht ausgeschlossen**: Bei Untersuchungen mit
  AGG-Relevanz (z. B. Kündigung eines Arbeitnehmers, der kurz zuvor eine
  Beschwerde erhoben hat) muss der Vermerk belegen, dass die Maßnahme
  nicht auf einem geschützten Merkmal beruht.

## Quellenpflicht

Jede Ausgabe zum Verdachtskündigungsverfahren zitiert:
- § 626 BGB (wichtiger Grund), § 626 Abs. 2 BGB (Frist)
- § 102 BetrVG (BR-Anhörung)
- BAG, Urt. v. 20.06.2013 – 2 AZR 546/12, NZA 2014, 143 (Verdachtskündigung)
- BAG, Urt. v. 23.08.2018 – 2 AZR 133/18, NZA 2018, 1329 (Anhörungsanforderungen)
- Erfurter Kommentar/Müller-Glöge, 24. Aufl. 2024, § 626 BGB Rn. 165 ff.

Detaillierte Vermerkstruktur, Glaubwürdigkeitsbewertungsrahmen und
Aktualisierungsregeln befinden sich in der Referenz-Skill
`internal-investigation` — diese vor inhaltlicher Arbeit laden.

Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall.
