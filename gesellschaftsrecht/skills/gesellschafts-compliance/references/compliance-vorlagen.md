# 1. Compliance-Vorlagen

Die Vorlagen werden erst nach Bestimmung der konkreten Register-, Publizitäts- oder Organpflicht geöffnet.

## Schriftsatzbausteine

### Baustein 1: Widerspruch gegen Ordnungsgeldbescheid (Paragraf 335 HGB)

```
An das
Bundesamt für Justiz
Referat IV 4
53094 Bonn

[Mandant / Gesellschaft]
[Anschrift]

[Ort, Datum]

Az. [Ordnungsgeldaktenzeichen]

Widerspruch gegen den Ordnungsgeldbescheid vom [Datum]

Sehr geehrte Damen und Herren,

wir vertreten die [Gesellschaft], [HR-Nummer], [Anschrift], in der oben bezeichneten
Angelegenheit. Gegen den Ordnungsgeldbescheid vom [Datum], der unserer Mandantin am
[Datum] zugegangen ist, legen wir hiermit

 W i d e r s p r u c h

ein.

Begründung:

Der Jahresabschluss der [Gesellschaft] für das Geschäftsjahr [Jahr] wurde am [Datum] beim
Betreiber des Bundesanzeigers eingereicht. Der Bundesanzeiger-Veröffentlichungscode lautet:
[Code].

Die verspätete Einreichung ist auf [konkrete Begründung: Prüfungsverzögerung durch
Wirtschaftsprüfer / IT-Umstellung / externe Umstände] zurückzuführen, für die der
gesetzliche Vertreter keine Verantwortung trägt. Wir bitten, dies bei der
Ordnungsgeldbemessung zu berücksichtigen.

Wir bitten höflich, das Ordnungsgeldverfahren einzustellen und den Bescheid aufzuheben.

Mit freundlichen Grüßen
[Kanzlei / Name]
Rechtsanwalt / Rechtsanwältin

Anlage: Bundesanzeiger-Veröffentlichungsbestätigung vom [Datum]
```

### Baustein 2: Aufforderungsschreiben an Geschäftsführer zur Einreichung Gesellschafterliste

```
An den Geschäftsführer
[Name GmbH]
[Anschrift]

[Ort, Datum]

Handelsregister-Einreichung der Gesellschafterliste (Paragraf 40 GmbHG) — dringende Fristsetzung

Sehr geehrter Herr/Frau [Name],

in Ihrer Eigenschaft als Geschäftsführer der [Name GmbH] sind Sie gemäß Paragraf 40 Abs. 2
GmbHG verpflichtet, nach jeder Änderung der Beteiligungsverhältnisse eine aktualisierte
Gesellschafterliste unverzüglich zum Handelsregister einzureichen.

Die Abtretung der Geschäftsanteile des Herrn [Name] an [Erwerber] wurde am [Datum]
notariell beurkundet und ist noch nicht in der beim Handelsregister hinterlegten
Gesellschafterliste (Stand: [Datum]) eingetragen.

Wir fordern Sie auf, spätestens bis zum [Datum = 10 Tage] die aktualisierte
Gesellschafterliste beim Amtsgericht [Registergericht] zur Aufnahme in das
Handelsregister einzureichen.

Wir weisen darauf hin, dass eine nicht ordnungsgemäß eingetragene Gesellschafterliste
das Risiko eines gutgläubigen Erwerbs gemäß Paragraf 16 Abs. 3 GmbHG begründet.

Mit freundlichen Grüßen
[Kanzlei / Name]
```

--- vor Versand klären ---
1. Welches Verhandlungsziel hat der Mandant? [Durchsetzung des Anspruchs / Vergleich / Reputationsschutz / schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestforderung / Zeitrahmen / Formerfordernis]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgesprach / Einigung vor Fristablauf]

Schlussabsatz Variante A (kooperativ):
Wir regen eine guetliche Einigung an und stehen für ein klärenden Gesprach zur Verfuegung. Eine einvernehmliche Loesung erspart beiden Seiten Zeit und Kosten.

Schlussabsatz Variante B (formal-streng):
Eine aussergerichtliche Einigung kommt nur in Betracht wenn die Gegenseite innerhalb von [X] Tagen einen akzeptablen Vorschlag unterbreitet. Anderenfalls werden wir alle rechtlichen Schritte einleiten.

### Baustein 3: Gesellschafts-Compliance-Tracker YAML (vollständig)

```yaml
### Gesellschafts-Compliance-Tracker
### Erstellt: [JJJJ-MM-TT]
### Zuletzt aktualisiert: [JJJJ-MM-TT]
### HINWEIS: Fristen sind nur Referenz — beim Bundesanzeiger/HR/TR bestätigen

metadaten:
 unternehmen: "[Konzern- / Mandantenname]"
 erstellt: "[Datum]"
 zuletzt_aktualisiert: "[Datum]"
 letztes_audit: null

gesellschaften:
 - name: "Alpha GmbH"
 typ: "GmbH"
 handelsregisternummer: "HRB 12345"
 registergericht: "Amtsgericht München"
 gruendungsdatum: "2015-01-10"
 status: "aktiv"
 groessenklasse: "mittelgroß Paragraf 267 Abs. 2 HGB"
 geschaeftsjahr_ende: "12-31"
 abschlusspruefung_pflicht: "ja"
 gesellschafter_liste_aktuell: "2025-11-15"
 notizen: "Abtretung März 2026 noch nicht eingetragen"

 pflichten:
 - typ: "Jahresabschluss Paragraf 325 HGB"
 faellig: "2026-12-31"
 faelligkeits_grundlage: "GJ-Ende 31.12.2025 + 12 Monate"
 zuletzt_eingereicht: "2025-10-15"
 status: "aktuell"
 notizen: "GJ 2025 bis 31.12.2026 einzureichen"

 - typ: "Gesellschafterliste Paragraf 40 GmbHG"
 faellig: "2026-04-05"
 faelligkeits_grundlage: "Unverzüglich nach Abtretung März 2026"
 zuletzt_eingereicht: "2025-11-15"
 status: "überfällig"
 notizen: "Abtretung v. 20.03.2026 noch nicht eingetragen; GF aufgefordert"

 - typ: "Transparenzregister Paragraf 20 GwG"
 faellig: "2026-04-03"
 faelligkeits_grundlage: "Änderung wirtschaftlich Berechtigter März 2026 + 2 Wochen"
 zuletzt_eingereicht: "2025-11-15"
 status: "überfällig"
 notizen: "Neuer wirtschaftlich Berechtigter nach Abtretung"

 - typ: "Jahresabschlussprüfung Paragraf 316 HGB"
 faellig: "2026-05-31"
 faelligkeits_grundlage: "Vor Feststellung und Offenlegung GJ 2025"
 zuletzt_eingereicht: null
 status: "bald_fällig"
 notizen: "Prüfungsauftrag an KPMG erteilt 01.02.2026"
```
