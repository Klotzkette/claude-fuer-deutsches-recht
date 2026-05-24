---
name: anw-akteneinsicht-steuerakte
description: Akteneinsicht in Steuerakten — Anspruch im Einspruchsverfahren nach § 364 AO im Klageverfahren nach § 78 FGO ergaenzend Art. 15 DSGVO bei personenbezogenen Daten. Behandelt Verwaltungsakten Pruefungsakten Aktenvermerke Aussenpruefungs-Berichte. Strategie bei Schwaerzungen wegen Steuergeheimnis Dritter (§ 30 AO). Erzeugt Antragsvorlage und Auswertungsraster fuer die uebermittelte Akte.
---

# Akteneinsicht in Steuerakten

## Rechtsgrundlagen

- **§ 364 AO** Akteneinsicht im Einspruchsverfahren — wesentlicher Aspekt des rechtlichen Gehoers; Behörde teilt die Tatsachen mit auf die sie ihre Entscheidung stützen will.
- **§ 78 FGO** Akteneinsicht im Klageverfahren.
- **Art. 15 DSGVO** Auskunft über eigene personenbezogene Daten — ergänzend.
- **§ 88 AO** Untersuchungsgrundsatz im Verwaltungsverfahren.

## Antrag

### Im Einspruchsverfahren

```
An das Finanzamt XYZ
- Steuernummer ...

In dem Einspruchsverfahren über den Bescheid vom (Datum) über
(Steuerart) (Jahr) Az (...)

beantragt der Einspruchsfuehrer
Akteneinsicht in die vollständige Steuerakte gemäß § 364 AO
einschließlich
- Veranlagungsakten der Prüfungsjahre
- Außenprüfungs-Berichte und Prüfungs-Notizen
- Aktenvermerke
- Korrespondenz mit Dritten
- Daten über Kontroll- und Überwachungsprüfungen

bevorzugt durch elektronische Übersendung über **Mein ELSTER** (Nachrichtenfunktion); alternativ in Papierform oder per Telefax. Eine Übersendung über beA ist seit 6.12.2024 unzulässig (§ 87a Abs. 1 S. 2 AO n.F.).
```

### Im Klageverfahren

Antrag beim Finanzgericht auf Akteneinsicht (§ 78 FGO) zusammen mit der Beiziehung der Verwaltungsakten (§ 71 Abs. 2 FGO).

## Sonderfälle

### Steuergeheimnis Dritter (§ 30 AO)

- Akten enthalten häufig Daten Dritter (z. B. Zeugenangaben Mitteilungen von Drittstellen).
- Schwaerzung zulässig wenn Drittdatenschutz dies erfordert.
- Bei umfangreicher Schwaerzung: Antrag auf Begründung; ggf. gerichtliche Prüfung.

### Prüfungsanmerkungen und interne Vermerke

- Auch interne Prüfer-Notizen sind Aktenbestandteil — Anspruch grundsaetzlich gegeben.
- Kontrollmitteilungen aus § 93a AO Steuer-Identifikationssystem ggf. relevant.

### Internationaler Datenaustausch

- Bei Auslandssachverhalten: Hinweise auf CRS-Daten DAC-Auskuenfte FATCA — Akteneinsicht auch hierauf.

## Auswertung der eingegangenen Akte

Pro Aktenbestandteil:

- laufende Nummer
- Datum
- Verfasser
- Inhaltskurzfassung
- Entscheidungserheblichkeit (entscheidend / hilfreich / neutral / belastend / lücke)
- Pinpoint-Verweis für zukuenftigen Schriftsatz

Anschluss an Skill `anw-steuerbescheid-analyse` und Folge-Schriftsatz.

## Aktenchronik

Tabellarisch nach Datum mit:

| Datum | Aktenteil | Verfasser | Inhalt kurz | Bewertung |
|---|---|---|---|---|

## Datenschutz

- Steuerakte enthält besonders sensible Daten (Vermögen Einkommen Familie Konten).
- Verarbeitung nur in Tools mit AVV.
- Mandantenakte unter `~/.claude/plugins/config/claude-fuer-deutsches-recht/steuerrecht-anwalt-und-berater/mandate/<az>/`.

## Ausgabe

- Akteneinsichtsantrag `akteneinsichtsantrag-<az>-<datum>.docx`.
- Aktenchronik nach Eingang `aktenchronik-<az>.md`.
- Prüfer-Prüfkatalog mit `[prüferflag]`-Einträgen.
