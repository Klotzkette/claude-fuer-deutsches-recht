---
name: untersuchung-abfrage
description: >
  Beantwortet Fragen gegen ein laufendes Untersuchungsprotokoll — was Zeugen
  gesagt haben, wo Schilderungen im Widerspruch stehen, welche Lücken bestehen,
  was die stärksten Belege zu jeder Frage sind. Lädt, wenn der Anwalt das
  Untersuchungsprotokoll abfragen möchte, ohne jeden Eintrag einzeln
  durchlesen zu müssen.
language: de
when_to_use: |
  Trigger phrases and example requests:
  - Untersuchung abfragen
  - was hat Zeuge gesagt
  - Widersprüche in Untersuchung
  - Beweislage prüfen
  - was fehlt noch
  - stärkste Belege
  - Protokoll auswerten
---

# Untersuchungsprotokoll-Abfrage (Arbeitsrecht)

## Zweck

Beantwortet Fragen gegen das Untersuchungsprotokoll — was Zeugen gesagt haben,
wo Schilderungen im Widerspruch stehen, welche Lücken bestehen, was die
stärksten Belege zu jeder Untersuchungsfrage sind.

Lädt, wenn der Anwalt das Erkenntnisbild der Untersuchung abfragen möchte,
ohne alle Protokolleinträge einzeln lesen zu müssen.

## Eingaben

- Bezeichnung der Untersuchungssache
- Konkrete Frage gegen das Protokoll

## Rechtlicher Rahmen

**Kernvorschriften:**

- § 626 BGB: Wichtiger Grund für außerordentliche Kündigung — Abfragen
  des Protokolls helfen, den Tatverdacht zu verdichten oder zu widerlegen
- § 22 AGG: Beweislastverteilung bei Diskriminierungsvorwürfen — bei
  AGG-Sachverhalt strukturierte Protokollauswertung als Basis für
  Enthaftungsnachweis des Arbeitgebers
- § 1 Abs. 2 KSchG: Soziale Rechtfertigung der Kündigung — Abfragen der
  Stärke der Beweislage je Untersuchungsfrage hilft, Wirksamkeitsrisiken
  einer verhaltens- oder personenbedingten Kündigung zu bewerten
- § 26 BDSG: Verarbeitungszweck — Protokollabfragen dienen ausschließlich
  dem Untersuchungszweck; kein Zweckwechsel ohne neue Rechtsgrundlage

**Leitentscheidungen:**

- BAG, Urt. v. 20.06.2013 – 2 AZR 546/12, NZA 2014, 143 Rn. 14 ff.:
  Verdachtskündigung — dringender Tatverdacht erfordert objektive Schwere
  auf Basis des tatsächlich Ermittelten; Protokollauswertung bestimmt, ob
  Schwelle erreicht ist
- BAG, Urt. v. 27.11.2008 – 2 AZR 675/07, NZA 2009, 842 Rn. 20:
  Tatkündigung — Überzeugungsmaßstab des Arbeitgebers; Protokollauswertung
  zur Überprüfung, ob der volle Nachweis einer Pflichtverletzung vorliegt
- BAG, Urt. v. 22.11.2012 – 2 AZR 732/11, NZA 2013, 665 Rn. 30 ff.:
  Widersprüchliche Zeugenaussagen im Kündigungsschutzprozess — der Arbeitgeber
  trägt die Darlegungs- und Beweislast für den Kündigungsgrund; nur was
  bei der Kündigung bekannt war, zählt (Nachschieben von Gründen nur
  eingeschränkt möglich)

**Kommentarliteratur:**

- Erfurter Kommentar/Müller-Glöge, 24. Aufl. 2024, § 626 BGB Rn. 165 ff.:
  Verdachtsgrad; objektive Indizien; Abgrenzung Tatverdacht von bloßem
  Verdacht
- HWK/Thüsing, 11. Aufl. 2024, § 1 KSchG Rn. 220 ff.:
  Darlegungs- und Beweislast des Arbeitgebers; Nachschieben von
  Kündigungsgründen
- Bauer/Krieger/Günther, AGG, 5. Aufl. 2022, § 22 Rn. 15 ff.:
  Beweislastverteilung; Indizien für Benachteiligung; Enthaftungsnachweis
  des Arbeitgebers durch ordnungsgemäße Untersuchung

## Ablauf

**Schritt 1 — Referenz-Skill laden**

Lade die Referenz-Skill `interne-untersuchung` und führe Modus 3
(Protokoll abfragen) aus.

**Schritt 2 — Gesamtes Protokoll lesen**

Immer das vollständige Protokoll lesen, bevor eine Frage beantwortet wird.

**Schritt 3 — Eintrags-IDs zitieren**

In jeder Antwort Protokoll-Eintrags-IDs in Klammern angeben. Dies ermöglicht
Rückverfolgung zur Primärquelle und belegt die Erkenntnisgrundlage.

**Schritt 4 — Bei fehlenden Erkenntnissen**

Falls das Protokoll zu einem Thema nichts enthält:

> Zum Thema [Thema] liegen in diesem Untersuchungsprotokoll
> ([N] Einträge gesichtet) keine Erkenntnisse vor. Dies sollte als
> Beweislücke erfasst werden.

Anbieten, den Punkt als Beweislücke zu protokollieren.

**Schritt 5 — Abfragetypen**

**Sachverhaltsabfrage** („Was hat [Person] zu [Thema] gesagt?"):
Aus Protokolleinträgen antworten, Eintrags-IDs zitieren.

**Widerspruchsabfrage** („Wo widersprechen sich die Schilderungen?"):
Alle `widerspricht_eintrag`-Verknüpfungen zeigen. Pro Widerspruch:
Was ist der Konflikt, welche Einträge stehen in Spannung, welche
dokumentarische Evidenz bezieht sich auf den Widerspruch.

**Deckungsabfrage** („Was fehlt noch?" / „Wo haben wir Lücken?"):
`quellen-checkliste.yaml` und `beweisluecken` im log.yaml auslesen. Melden:
- Noch offene Checklistenpunkte
- Protokollierte Beweislücken
- Schilderungen, die auf noch nicht erhobene Quellen hinweisen

**Stärkeabfrage** („Was ist die stärkste Evidenz zu jeder Frage?"):
Für jede Untersuchungsfrage: höchstbewertete Protokolleinträge, dokumentarische
Bestätigungen und ungelöste Widersprüche — frageweise strukturiert.

**Reife-Abfrage** (Verdachtsgrad für Kündigung):
Für eine Verdachtskündigung nach § 626 BGB: Protokolleinträge nach
objektiver Schwere und Dringlichkeit des Verdachts auswerten. Anhörung
der beschuldigten Person dokumentiert? Falls nicht: flaggen.

## Ausgabeformat

Direkte Antwort auf die gestellte Frage, mit Eintrags-IDs in Klammern.
Bei fehlenden Erkenntnissen: expliziter Hinweis und Angebot zur
Beweislückendokumentation. Bei Widerspruchsabfragen: tabellarische
Gegenüberstellung der Einträge mit Beschreibung des Konflikts.

## Beispiel

```
/arbeitsrecht:untersuchung-abfrage Sache-Mueller
Was hat der Zeuge Bauer zum Dezember-Meeting gesagt?
```

```
/arbeitsrecht:untersuchung-abfrage Sache-Mueller
Wo widersprechen sich die Schilderungen?
```

```
/arbeitsrecht:untersuchung-abfrage Sache-Mueller
Was fehlt noch?
```

Beispiel-Antwort bei Widerspruchsabfrage:

```
Identifizierte Widersprüche:

Widerspruch 1 — Eintrag #3 vs. Eintrag #7:
  Eintrag #3 (Beschwerdeführerin Koch, 15.01.2025): "Das Gespräch fand nur
  zwischen mir und Herrn Müller statt."
  Eintrag #7 (Zeuge Bauer, 22.01.2025): "Frau Schmidt war bei dem Gespräch
  anwesend."
  Dokumentarische Evidenz: Kalender-Eintrag vom 12.11.2024 (Eintrag #5)
  zeigt drei Teilnehmer. Widerspruch zur Schilderung der Beschwerdeführerin.

Handlungsbedarf: Frau Schmidt als Zeugin befragen (Checkliste Punkt 3 — noch offen).
```

## Risiken und typische Fehler

- **Protokollabfrage ohne vollständiges Lesen**: Antworten ohne Lesen des
  Gesamtprotokolls können Widersprüche und Lücken übersehen. Immer alle
  Einträge sichten.
- **Fehlende Eintrags-IDs**: Antworten ohne Eintrags-ID-Referenzen sind
  nicht rückverfolgbar und erschweren spätere Anfechtungen.
- **Lücken nicht als Lücken benennen**: „Dazu weiß ich nichts" ist kein
  angemessenes Ergebnis — die Nicht-Existenz von Erkenntnissen im Protokoll
  muss explizit als potenzielle Beweislücke benannt werden.
- **Widersprüche glätten**: Widersprechende Schilderungen dürfen nicht
  harmonisiert werden. Sie müssen direkt benannt werden — der Anwalt
  entscheidet, welcher Version geglaubt wird.
- **Zweckbindung beachten**: Protokolldaten dürfen nur für Untersuchungs-
  zwecke genutzt werden (§ 26 BDSG). Keine Weitergabe für andere Zwecke
  ohne neue Rechtsgrundlage.

## Quellenpflicht

Bei Abfragen zur Beweislage für Kündigung zitieren:
- § 626 BGB (Tatverdacht / Wichtiger Grund)
- BAG, Urt. v. 20.06.2013 – 2 AZR 546/12, NZA 2014, 143 (Verdachtsgrad)
- BAG, Urt. v. 27.11.2008 – 2 AZR 675/07, NZA 2009, 842 (Tatkündigung)
- Bei AGG-Sachverhalt: § 22 AGG, Bauer/Krieger/Günther, AGG, 5. Aufl. 2022, § 22 Rn. 15 ff.

Detaillierter Abfrageprozess, Zitierregeln und Lückendokumentations-Templates
befinden sich in der Referenz-Skill `interne-untersuchung` — diese vor
inhaltlicher Arbeit laden.

Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall.
