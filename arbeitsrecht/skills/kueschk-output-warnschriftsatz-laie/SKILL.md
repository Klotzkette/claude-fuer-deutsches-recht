---
name: kueschk-output-warnschriftsatz-laie
description: "Ausgabe vollständige Klageschrift mit Pflicht-Disclaimer-Kopf für Laien; Zusammenführung aller Bausteine zu einem druckfertigen Schriftsatz; Ausfuellanleitung; Einreichungshinweise für Arbeitsgericht."
---

# Ausgabe: Vollständige Klageschrift mit Pflicht-Disclaimer (Laie)

## Zweck

Dieser Skill führt alle Bausteine des KüSchK-Laien-Workflows zu einem vollständigen, druckfertigen Klageschrift-Entwurf zusammen — inklusive Pflicht-Disclaimer-Kopf.

## Vollständige Klageschrift (Laie)

---

**⚠ WICHTIGE WARNUNG — VOR EINREICHUNG LESEN ⚠**

Dieses Dokument ist ein Entwurf, der mit Hilfe eines KI-gestützten Rechtshilfesystems erstellt wurde. Es begründet kein Mandatsverhältnis. Das System übernimmt keine rechtliche Verantwortung und haftet nicht.

**Du könntest auf der falschen Wiese unterwegs sein.** Prüfe zwingend:
- Bist du länger als sechs Monate beschäftigt? (§ 1 Abs. 1 KSchG)
- Hat dein Betrieb mehr als zehn Arbeitnehmer? (§ 23 KSchG)
- Gilt die Drei-Wochen-Frist nach § 4 KSchG? — Sie läuft ab Zugang der Kündigung.

**Dringende Empfehlung:** Suche sofort einen Rechtsanwalt oder eine Rechtsanwältin auf.

---

**KLAGESCHRIFT**

An das

Arbeitsgericht [GERICHT — z.B. Arbeitsgericht Köln]

Klage des/der

[VOLLSTÄNDIGER NAME]
[STRASSE UND HAUSNUMMER]
[PLZ ORT]
(Telefon: [NUMMER] / E-Mail: [E-MAIL])

— Kläger/Klägerin —

gegen

[VOLLSTÄNDIGE FIRMA / NAME DES ARBEITGEBERS]
[STRASSE UND HAUSNUMMER]
[PLZ ORT]
[ggf.: vertreten durch Geschäftsführer/in: NAME]

— Beklagte/r —

**Streitwert:** vorläufig [3 × MONATSLOHN] EUR (§ 42 Abs. 2 GKG)

---

**KLAGEANTRÄGE**

Ich beantrage:

1. Es wird festgestellt, dass das Arbeitsverhältnis der Parteien durch die Kündigung der Beklagten vom [DATUM DES KÜNDIGUNGSSCHREIBENS], zugegangen am [ZUGANGSDATUM], nicht aufgelöst worden ist.

2. Es wird festgestellt, dass das Arbeitsverhältnis der Parteien auch nicht durch andere Beendigungsgründe aufgelöst worden ist, sondern über den [GEPLANTES BEENDIGUNGSDATUM LAUT KÜNDIGUNG] hinaus fortbesteht.

---

**BEGRÜNDUNG**

**I. Das Arbeitsverhältnis**

Ich bin seit dem [ARBEITSBEGINN-DATUM] bei der Beklagten beschäftigt als [BERUFSBEZEICHNUNG / TÄTIGKEITSBESCHREIBUNG]. Mein monatliches Bruttogehalt beträgt [BETRAG] EUR. Im Betrieb der Beklagten sind regelmäßig mehr als zehn Arbeitnehmer beschäftigt.

**II. Die Kündigung**

Am [ZUGANGSDATUM] habe ich das Kündigungsschreiben der Beklagten erhalten (Anlage K 1). Die Kündigung ist zum [BEENDIGUNGSDATUM] ausgesprochen worden.

**III. Die Kündigung ist unwirksam**

[HIER BEGRÜNDUNG NACH TATSÄCHLICHEM GRUND EINTRAGEN:]

**Option A — Keine Sozialauswahl (betriebsbedingt):**
Eine ordnungsgemäße Sozialauswahl gemäß § 1 Abs. 3 KSchG wurde nicht durchgeführt. Der Kollege/die Kollegin [NAME, falls bekannt] weist geringere Sozialdaten auf als ich, wurde aber weiterbeschäftigt.

**Option B — Keine Abmahnung (verhaltensbedingt):**
Eine Abmahnung als notwendige Voraussetzung wurde nicht ausgesprochen. Die Kündigung ist daher unverhältnismäßig.

**Option C — Formfehler:**
[FORMFEHLER KONKRET BENENNEN]

**Option D — Sonderkündigungsschutz:**
Ich genieße Sonderkündigungsschutz wegen [GRUND — z.B.: Schwangerschaft / Elternzeit / Schwerbehinderung]. Die erforderliche behördliche Zustimmung wurde nicht eingeholt.

**IV. Beweisangebote**

- Anlage K 1: Kündigungsschreiben vom [DATUM]
- Anlage K 2: Arbeitsvertrag vom [DATUM]
- Zeuge: [NAME UND ANSCHRIFT] zum Beweis des Zugangsdatums

---

[ORT], den [DATUM]

____________________________
[UNTERSCHRIFT]
[NAME in Druckschrift]

---

## Triage zu Beginn — kläre vor Ausgabe der vollständigen Klageschrift

1. Wurden alle vorgelagerten Prüfschritte abgearbeitet?
   - KSchG-Anwendbarkeit (§ 23 KSchG, § 1 Abs. 1 KSchG) ✓/✗
   - Frist und Zugang (§ 4 KSchG) ✓/✗
   - Formfehler (§§ 623, 174 BGB) ✓/✗
   - Sonderkündigungsschutz ✓/✗
2. Liegt der Kündigungsgrund (betriebsbedingt/verhaltensbedingt/personenbedingt) fest?
3. Wurde der Laien-Disclaimer-Kopf (`kueschk-grundwarnung-falsche-wiese-und-haftung`) bereits ausgegeben?
4. Sind alle Platzhalter [NAME], [DATUM], [BETRAG] durch echte Angaben des Nutzers befüllt?

**Schrittfolge Klageschrift-Ausgabe:**
```
Step 1: Disclaimer-Kopf ausgeben (immer)
Step 2: Rubrum (Gericht, Kläger, Beklagter) ausfüllen
Step 3: Streitwert berechnen (3 × Bruttomonatsgehalt)
Step 4: Anträge formulieren (allgemeiner + besonderer Feststellungsantrag)
Step 5: Begründung nach Sachverhalt (Option A/B/C/D)
Step 6: Beweisangebote einsetzen
Step 7: Einreichungshinweise ausgeben
```

## Zentrale Normen

- **§ 4 KSchG** — Klagefrist drei Wochen (absolute Ausschlussfrist)
- **§ 256 ZPO** — Feststellungsklage, Feststellungsinteresse
- **§ 42 Abs. 2 GKG** — Streitwert drei Bruttomonatsgehalt bei Kündigungsschutz
- **§ 46 Abs. 2 ArbGG i.V.m. §§ 495, 495a ZPO** — Verfahrensvorschriften Arbeitsgericht
- **§ 11 Abs. 1 ArbGG** — Kein Anwaltszwang erste Instanz
- **§ 46 Abs. 2 ArbGG i.V.m. § 496 ZPO** — Klage kann zu Protokoll der Geschäftsstelle erklärt werden

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Einreichungshinweise

1. **Frist:** Die Klageschrift muss innerhalb von **drei Wochen** nach Zugang der Kündigung beim Arbeitsgericht eingehen.
2. **Wo einreichen:** Arbeitsgericht am Ort des Betriebs oder am Wohnort des Arbeitnehmers.
3. **Wie einreichen:** Persönlich zu Protokoll der Geschäftsstelle erklären (kostenlos, kein Schreiben nötig) oder schriftlich einreichen.
4. **Kopien:** Mindestens drei Exemplare (Gericht, Gegner, eigene Akte) + Anlagen.
5. **Empfangsbestätigung:** Immer einen Eingangsstempel des Gerichts verlangen.

---

Hinweis: Keine Rechtsberatung. Mechanische Prüfung anhand vom Nutzer behaupteter Tatsachen. Falsche Sachverhaltsangabe oder falsche Anspruchsgrundlage entwertet das Ergebnis. Dringende Empfehlung anwaltlicher Beratung, insbesondere wegen der Drei-Wochen-Fristen.

Du könntest auf der falschen Wiese unterwegs sein. Dieses System kann das nicht prüfen.
