---
name: untersuchung-eroeffnen
description: "Eröffnet eine neue interne Untersuchungssache — führt die Sachverhaltserfassung durch, generiert die Quellencheckliste und legt das persistente Untersuchungsprotokoll an. Lädt, wenn eine Beschwerde oder ein Hinweis eingeht und ein vertraulicher Untersuchungsarbeitsbereich eingerichtet werden soll."
---

# Untersuchungseröffnung (Arbeitsrecht)

## Zweck

Eröffnet eine neue interne Untersuchungssache — führt die strukturierte
Sachverhaltserfassung durch, generiert die auf den Untersuchungstyp
zugeschnittene Quellencheckliste und legt das persistente
Untersuchungsprotokoll an.

Lädt, wenn eine Beschwerde oder ein Hinweis vorliegt und ein strukturierter,
vertraulicher Untersuchungsarbeitsbereich eingerichtet werden soll.

## Eingaben

- Kurzbeschreibung des Vorwurfs oder der Besorgnis (kann nach Sachverhaltserfassung
  verfeinert werden)
- Ist die Untersuchung anwaltsgeleitet? (Beeinflusst Schutzstatus der Unterlagen)

## Rechtlicher Rahmen

**Kernvorschriften:**

- § 26 BDSG: Verarbeitung von Beschäftigtendaten zur Aufdeckung von
  Straftaten oder schwerwiegenden Pflichtverletzungen — Erforderlichkeit
  und Verhältnismäßigkeit als Voraussetzung; Protokolldaten sind
  Beschäftigtendaten
- §§ 34, 36, 37 HinSchG: Hinweisgeberschutzgesetz — Vertraulichkeit der
  Identität der hinweisgebenden Person; Verbot von Repressalien; interne
  Meldestelle; Dokumentationspflichten
- § 87 Abs. 1 Nr. 6 BetrVG: Mitbestimmung bei technischen
  Überwachungseinrichtungen — vor Kommunikationsauswertungen klären
- § 82 Abs. 2 BetrVG: Recht des Arbeitnehmers, ein Betriebsratsmitglied
  zu Besprechungen über Beschwerden hinzuzuziehen
- §§ 84, 85 BetrVG: Beschwerderecht des Arbeitnehmers; Behandlung durch
  den Betriebsrat
- § 626 Abs. 2 BGB: Zwei-Wochen-Frist — Dokumentation des ersten
  Kenntniszeitpunkts ab Eröffnung kritisch
- §§ 3 ff. AGG: Diskriminierungsverbote — bei AGG-relevantem Sachverhalt
  strukturierte Untersuchung als Enthaftungsvoraussetzung

**Leitentscheidungen:**

- BAG, Urt. v. 20.06.2013 – 2 AZR 546/12, NZA 2014, 143 Rn. 14 ff.:
  Verdachtskündigung — umfassende Sachaufklärung vor Kündigung zwingend;
  Untersuchungspflicht des Arbeitgebers; Dokumentationsanforderungen
- BAG, Urt. v. 29.06.2017 – 2 AZR 597/16, NZA 2017, 1179 Rn. 22 ff.:
  Beginn der Zwei-Wochen-Frist des § 626 Abs. 2 BGB — Fristbeginn erst
  nach ausreichender Sachaufklärung; Pflicht, Ermittlungen zügig zu führen;
  mutwillige Verzögerung kann Verwirkung begründen
- BAG, Urt. v. 23.08.2018 – 2 AZR 133/18, NZA 2018, 1329 Rn. 29 ff.:
  Inhaltliche Anforderungen an die Anhörung der beschuldigten Person vor
  Verdachtskündigung; Frage und Antwortrecht; Protokollierungspflicht

**Kommentarliteratur:**

- Gola/Heckmann/Schomerus, BDSG, 13. Aufl. 2022, § 26 Rn. 100 ff.:
  Grundvoraussetzungen der Datenzulässigkeit bei interner Untersuchung;
  Dokumentationspflichten; Betriebsvereinbarung als Rechtsgrundlage
- Erfurter Kommentar/Müller-Glöge, 24. Aufl. 2024, § 626 BGB Rn. 230 ff.:
  Zwei-Wochen-Frist; Fristbeginn; Aufklärungsobliegenheit des Arbeitgebers
- Bauer/Krieger/Günther, AGG, 5. Aufl. 2022, § 12 Rn. 30 ff.:
  Untersuchungspflicht des Arbeitgebers bei Diskriminierungsbeschwerde;
  Enthaftung bei ordnungsgemäßer Untersuchung

## Ablauf

**Schritt 1 — Kontext laden**

Lese `CLAUDE.md` im Plugin-Verzeichnis → jurisdiktioneller Fußabdruck,
Eskalationstabelle, etwaige Untersuchungsprotokolle.

**Schritt 2 — Bestehende Sache prüfen**

Falls bereits ein Untersuchungsordner mit demselben Slug existiert: Warnung
ausgeben, bevor überschrieben wird.

**Schritt 3 — Referenz-Skill laden**

Lade die Referenz-Skill `interne-untersuchung` und führe Modus 1
(Neue Untersuchung eröffnen) aus.

**Vertraulichkeits-Vorabprüfung:**

> Vor der Eröffnung: Ist diese Untersuchung anwaltsgeleitet? Wenn ja —
> erhöhter Schutz der Arbeitsergebnisse. Wenn nein — Schutzstatus und
> Weitergabe der Unterlagen vorab klären. Unterlagen mit fehlerhaftem
> Schutzstatus können in einem etwaigen Verfahren problematisch werden.

**Schritt 4 — Sachverhaltserfassung, Quellencheckliste, Protokoll**

Alle Schritte aus Modus 1 der Referenz-Skill vollständig ausführen:
Sachverhaltserfassung in einem Block, Quellencheckliste je nach Untersuchungstyp
generieren und dem Anwalt vorlegen, Protokolldateien anlegen.

**§ 82 Abs. 2 BetrVG-Hinweis:**
Wenn ein Arbeitnehmer zu Gesprächen geladen wird, die seine Beschwerde
oder seine Stellung im Untersuchungsverfahren berühren: Hinweisen, dass
er nach § 82 Abs. 2 BetrVG das Recht hat, ein Betriebsratsmitglied
hinzuzuziehen. Dies protokollieren.

**Schritt 5 — Erstes Protokolldatum sichern**

Datum und Uhrzeit der Eröffnung im Protokoll festhalten. Dies ist bei
einer eventuellen Verdachtskündigung der Ausgangszeitpunkt für die
Fristberechnung nach § 626 Abs. 2 BGB (Frist beginnt mit sicherer
Kenntnis, nicht mit bloßem Verdacht — aber Aufklärung ist zügig
zu führen, BAG, Urt. v. 29.06.2017 – 2 AZR 597/16).

## Ausgabeformat

Vertraulichkeitsprüfung, dann strukturierte Sachverhaltserfassungs-Abfrage
in einem Block, dann Quellencheckliste zur Bestätigung durch den Anwalt,
dann Bestätigung der angelegten Protokolldateien:

```
Untersuchung eröffnet — [Sachebezeichnung] — [ISO-Datum]
Protokolldatei: investigation-[slug]/log.yaml
Quellencheckliste: investigation-[slug]/quellen-checkliste.yaml
Dokumentenprotokoll: investigation-[slug]/dokumente-geprueft.yaml

Nächste Schritte:
  /arbeitsrecht:untersuchung-ergaenzen [slug] — Daten hinzufügen
  /arbeitsrecht:untersuchung-abfrage [slug] — Protokoll abfragen
  /arbeitsrecht:untersuchungs-memo [slug] — Vermerk entwerfen
```

## Beispiel

```
/arbeitsrecht:untersuchung-eroeffnen
Belästigungsbeschwerde gegen Abteilungsleiter in der Hamburger Niederlassung.
```

```
/arbeitsrecht:untersuchung-eroeffnen
(Skill fragt nach Details)
```

Beispiel-Ausgabe nach Sachverhaltserfassung (Betriebsrat-Flag):

> Hinweis: Die beschuldigte Person ist Betriebsratsmitglied. Kündigung
> erfordert Zustimmung des Betriebsrats (§ 103 BetrVG) oder gerichtliche
> Ersetzung. Dies ändert den weiteren Verfahrensablauf wesentlich —
> Protokoll anpassen und externen Arbeitsrechtler einbinden.

## Risiken und typische Fehler

- **Anwaltsleitung unklar**: Ohne klare Anwaltsleitung ist der Schutzstatus
  der Untersuchungsunterlagen fraglich. Vor Anlegen der ersten Datei klären.
- **§ 626 Abs. 2 BGB-Uhr läuft**: Die Frist beginnt bei sicherer Kenntnis.
  Mutwillige Verzögerung der Untersuchung kann dazu führen, dass die
  außerordentliche Kündigung verfristet ist (BAG, Urt. v. 29.06.2017 –
  2 AZR 597/16). Zügiges Vorgehen dokumentieren.
- **§ 82 Abs. 2 BetrVG versäumt**: Wenn dem Arbeitnehmer das Recht auf
  Hinzuziehung eines Betriebsratsmitglieds nicht mitgeteilt wird, kann
  dies das Verfahren belasten.
- **HinSchG-Vertraulichkeit**: Bei Hinweisgebersachen ist die Identität der
  hinweisgebenden Person streng vertraulich zu halten (§ 8 Abs. 1 HinSchG).
  Protokolleinträge so gestalten, dass die Identität nicht für Unbefugte
  erkennbar ist.
- **Betriebsrat-Sonderstatus**: Beschuldigte Betriebsratsmitglieder
  genießen besonderen Schutz (§ 103 BetrVG). Früh klären.

## Quellenpflicht

Bei jeder Eröffnung zitieren:
- § 26 BDSG (Datenschutz, Verhältnismäßigkeit)
- §§ 34, 36, 37 HinSchG (bei Hinweisgebersachen)
- § 82 Abs. 2, §§ 84, 85 BetrVG (Betriebsratsrechte)
- § 626 Abs. 2 BGB (Fristbeginn-Dokumentation)
- BAG, Urt. v. 20.06.2013 – 2 AZR 546/12, NZA 2014, 143 (Sachaufklärungspflicht)
- BAG, Urt. v. 29.06.2017 – 2 AZR 597/16, NZA 2017, 1179 (Fristbeginn)
- Gola/Heckmann/Schomerus, BDSG, 13. Aufl. 2022, § 26 Rn. 100 ff.

Detaillierte Sachverhaltserfassung, Quellenchecklisten-Vorlagen und
Protokolldateiformate befinden sich in der Referenz-Skill
`interne-untersuchung` — diese vor inhaltlicher Arbeit laden.

Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall.
