---
name: dsfa-typische-fehler-bei-erstpruefung
description: "Katalog typischer Fehler bei der DSFA-Erstpruefung und Gegenmassnahmen. Output: Fehlerkatalog mit Pruefliste für DSB und Verantwortliche samt Beispielen aus Aufsichtspraxis."
---

# Typische Fehler bei der DSFA-Erstpruefung

## Zweck

Strukturierter Katalog der typischen Fehler bei der ersten Durchfuehrung einer DSFA, einschliesslich Gegenmassnahmen, Vermeidungsstrategien und Verweis auf die jeweils einschlaegigen Skills. Ergebnis ist eine Pruefliste für DSB und Verantwortliche, die vor Freigabe einer DSFA durchgegangen wird.

## Wann dieses Modul hilft

- Vor Freigabe einer DSFA durch den Verantwortlichen
- Bei Audit einer bestehenden DSFA
- In der Schulung neuer DSB oder Datenschutz-Koordinatoren
- Bei Aufsichtsanfrage zur Plausibilisierung einer durchgefuehrten DSFA
- Bei Re-Pruefung nach Art. 35 Abs. 11 DSGVO

## Rechtlicher Rahmen

- Art. 35 DSGVO mit allen Absaetzen.
- Art. 5 Abs. 2 DSGVO Rechenschaftspflicht.
- Art. 83 Abs. 4 lit. a DSGVO Bussgeldtatbestand für Verstoesse gegen Art. 35.
- EDSA-Leitlinien WP 248 rev.01 und einschlaegige Aufsichtsbehoerdenpraxis.

## Fehlerkatalog mit Gegenmassnahmen

### 1. Triage-Phase

- Trigger-Pruefung ohne dokumentierten Vermerk; nur muendlich. Gegenmassnahme: Triage-Vermerk gemaess Skill dsfa-art-35-dsgvo-trigger-und-anwendungsbereich.
- Nur Art. 35 Abs. 3 DSGVO geprueft, Generalklausel Abs. 1 uebersehen. Gegenmassnahme: Doppelblick auf Generalklausel und Regelbeispiele.
- Blacklist der eigenen Landesbehoerde uebersehen. Gegenmassnahme: Skill dsfa-bfdi-und-laender-blacklist.
- EDSA-Kriterien nicht durchgepruft. Gegenmassnahme: Skill dsfa-edpb-leitlinien-9-19-anwendung.

### 2. Beschreibung der Verarbeitung

- Beschreibung floskelhaft, ohne Datenfluss. Gegenmassnahme: Datenflussdiagramm und konkrete Empfaengeraufzaehlung.
- Drittlandbezug uebersehen, weil EU-Hosting. Gegenmassnahme: Zugriffsbefugnis pruefen, Skill dsfa-für-internationale-datentransfers.
- Sub-Auftragsverarbeiter nicht gelistet. Gegenmassnahme: vollstaendige AVV-Kette.
- Aufbewahrungsfristen pauschal. Gegenmassnahme: Loeschkonzept beifuegen.

### 3. Verhaeltnismaessigkeit

- Verhaeltnismaessigkeitspruefung wird auf Rechtsgrundlage reduziert. Gegenmassnahme: Datenminimierung, Zweckbindung und Speicherbegrenzung separat pruefen.
- Mildere Mittel nicht erwogen. Gegenmassnahme: Alternativ-Optionen explizit dokumentieren und verwerfen.
- Betroffenenrechte nicht beschrieben. Gegenmassnahme: Pro Recht eine Zeile, wie es operativ umgesetzt wird.

### 4. Risikoanalyse

- Risiko nur für Vertraulichkeit untersucht. Gegenmassnahme: alle Schutzziele SDM durchgehen.
- Wahrscheinlichkeit ohne Bedrohungsmodell. Gegenmassnahme: Bedrohungsannahmen explizit machen.
- Schadenschwere aus Sicht des Verantwortlichen statt Betroffener. Gegenmassnahme: Erwaegungsgrund 75 DSGVO als Massstab.
- Risikomatrix bleibt für Massnahmen-Spalte leer. Gegenmassnahme: Pro Risiko mindestens eine Massnahme zuordnen.

### 5. Massnahmen

- TOM-Konzept fehlt oder ist generisch. Gegenmassnahme: konkrete Massnahmen mit Verantwortlichen und Fristen.
- Vertragliche Massnahmen (AVV, SCC) nicht referenziert. Gegenmassnahme: Verweis auf konkrete Vertragsversion und Datum.
- KI-Spezifika fehlen. Gegenmassnahme: Skill dsfa-für-ki-systeme-schnittstelle-art-26-kivo.
- Stand der Technik nicht begruendet. Gegenmassnahme: BSI- oder ENISA-Referenz beifuegen.

### 6. Restrisiko

- Restrisiko wird kuenstlich kleingerechnet, um Art. 36 zu vermeiden. Gegenmassnahme: Ehrliche Bewertung; bei spaeterem Vorfall verdoppelter Vorwurf.
- Restrisiko ohne Begruendung pauschal als gering bewertet. Gegenmassnahme: pro Szenario Begruendung.
- Vorab-Konsultation Art. 36 als Option statt Pflicht behandelt. Gegenmassnahme: Skill dsfa-restrisiko-und-art-36-konsultation.

### 7. Konsultation und Freigabe

- DSB-Anhörung nur muendlich oder gar nicht. Gegenmassnahme: schriftliche Stellungnahme, datiert und unterzeichnet.
- Stakeholder-Konsultation Art. 35 Abs. 9 nicht erwogen. Gegenmassnahme: Skill dsfa-stakeholder-konsultation-art-35-9.
- Freigabe ohne Datum oder durch Unbefugten. Gegenmassnahme: definierter Eskalations- und Freigabeprozess.
- Verarbeitung wird vor Antwort der Aufsicht aufgenommen. Gegenmassnahme: Projektplan an Frist 8 Wochen ankoppeln.

### 8. Dokumentation und Update

- DSFA wird einmal erstellt und nie aktualisiert. Gegenmassnahme: Skill dsfa-update-bei-aenderungen-und-revision.
- Versionen werden ueberschrieben. Gegenmassnahme: Versionshistorie als Pflichtfeld.
- Aktenzeichen oder Aufbewahrungsfrist fehlt. Gegenmassnahme: Skill dsfa-dokumentation-und-rechenschaftspflicht-art-5-ii.
- Verweis im Verarbeitungsverzeichnis Art. 30 fehlt. Gegenmassnahme: Doppelnachweis VV plus DSFA.

## Pruefliste vor Freigabe

```
DSFA-FREIGABE-PRUEFLISTE [DATUM]

Verarbeitung: [BEZEICHNUNG]
Pruefer: [NAME, ROLLE]

A. Triage
[ ] Triage-Vermerk schriftlich vorhanden
[ ] Blacklist-Abgleich dokumentiert
[ ] WP-248-Kriterien gepruet

B. Beschreibung
[ ] Datenfluss konkret beschrieben
[ ] Drittlandbezug geprueft
[ ] Sub-AV-Kette vollstaendig
[ ] Aufbewahrungsfristen konkret

C. Verhaeltnismaessigkeit
[ ] Datenminimierung
[ ] Zweckbindung
[ ] Speicherbegrenzung
[ ] Mildere Mittel erwogen
[ ] Betroffenenrechte operativ

D. Risikoanalyse
[ ] Alle Schutzziele gepruet
[ ] Wahrscheinlichkeit begruendet
[ ] Schadenschwere aus Sicht Betroffener
[ ] Risikomatrix vor und nach Massnahmen

E. Massnahmen
[ ] TOM konkret mit Eigentuemer und Frist
[ ] Vertragliche Massnahmen referenziert
[ ] KI-Spezifika beruecksichtigt

F. Restrisiko
[ ] Bewertung begruendet
[ ] Art. 36 gepruet

G. Konsultation
[ ] DSB schriftlich angehoert
[ ] Stakeholder-Konsultation Art. 35 Abs. 9 erwogen
[ ] Freigabe durch befugte Person

H. Dokumentation
[ ] Aktenzeichen vergeben
[ ] Versionshistorie gefuehrt
[ ] Verweis im VV Art. 30

Freigabeempfehlung: ja / nachzubessern / nein
Unterschrift Pruefer: ____________________
```

## Querverweise

- `datenschutzrecht/skills/dsfa-art-35-dsgvo-trigger-und-anwendungsbereich/SKILL.md`
- `datenschutzrecht/skills/dsfa-edpb-leitlinien-9-19-anwendung/SKILL.md`
- `datenschutzrecht/skills/dsfa-template-deutsch-vollvorlage/SKILL.md`
- `datenschutzrecht/skills/dsfa-restrisiko-und-art-36-konsultation/SKILL.md`
- `datenschutzrecht/skills/dsfa-update-bei-aenderungen-und-revision/SKILL.md`
- `datenschutzrecht/skills/dsfa-dokumentation-und-rechenschaftspflicht-art-5-ii/SKILL.md`
- `references/zitierweise.md` — Zitierweise

## Quellen Stand 06/2026

- Art. 35, 36, 5 Abs. 2, 83 Abs. 4 lit. a DSGVO
- EDSA-Leitlinien WP 248 rev.01
- BfDI- und Landesbehoerden-Pruefberichte (live abzurufen)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe verifizieren
- Literatur: Kommentar- und Aufsatzfundstellen nur bei eigener Quelle
