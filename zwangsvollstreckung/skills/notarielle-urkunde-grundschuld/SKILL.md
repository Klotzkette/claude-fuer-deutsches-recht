---
name: notarielle-urkunde-grundschuld
description: "Gläubiger hat notarielle Grundschuld-Urkunde und will vollstrecken. § 794 Abs. 1 Nr. 5 ZPO Zwangsvollstreckung aus notarieller Urkunde. Prüfraster: Unterwerfungsklausel dinglich und persoenlich Klauselumschreibung § 727 ZPO bei Abtretung Sicherungsabrede Kündigung § 1193 BGB 6-Monats-Frist Vollstreckung Grundstueck ZVG vs. persönliches Vermögen PfUeB. Output: Vollstreckungsstrategie und Schriftsatz-Entwurf. Abgrenzung zu zv-zvg-antrag-gläubiger (Versteigerung) und zv-titel-klausel-zustellung im Zwangsvollstreckung."
---

# Vollstreckung aus notarieller Grundschuldurkunde

## Arbeitsbereich

Gläubiger hat notarielle Grundschuld-Urkunde und will vollstrecken. § 794 Abs. 1 Nr. 5 ZPO Zwangsvollstreckung aus notarieller Urkunde. Prüfraster: Unterwerfungsklausel dinglich und persoenlich Klauselumschreibung § 727 ZPO bei Abtretung Sicherungsabrede Kündigung § 1193 BGB 6-Monats-Frist Vollstreckung Grundstueck ZVG vs. persönliches Vermögen PfUeB. Output: Vollstreckungsstrategie und Schriftsatz-Entwurf. Abgrenzung zu zv-zvg-antrag-gläubiger (Versteigerung) und zv-titel-klausel-zustellung. Arbeite entlang dieser konkreten Prüfungslinie und trenne Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: §§ 704 ff. ZPO; § 802l Kontensuche, Vermögensauskunft, Räumung; § 800 ZPO Notar; § 201 InsO, ZVG, EU-Kontenpfändung VO 655; § 765a Härtefall, Schuldnerschutz — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Startet bei

- Notarielle Urkunde mit Grundschuld vorhanden
- Unterwerfung des Eigentümers/Schuldners "in sein gesamtes Vermögen" und/oder "in den jeweiligen Grundbesitz"
- Sicherungsabrede (Zweckerklärung) liegt vor
- Forderung fällig (gekündigt, Zahlungsverzug)

## Rechtsgrundlagen

- § 794 Abs. 1 Nr. 5 ZPO – notarielle Urkunde als Titel
- § 800 ZPO – Vollstreckung gegen Rechtsnachfolger im Eigentum
- § 727 ZPO – Titelumschreibung bei Forderungsabtretung
- § 1192 Abs. 1a BGB – Einreden bei Sicherungsgrundschuld
- § 1193 BGB – Kündigung Grundschuld, sechs Monate
- § 1147 BGB – Befriedigung aus dem Grundstück
- § 750 Abs. 1 ZPO – Zustellung
- §§ 15 ff. ZVG – Anordnung der Zwangsversteigerung / Zwangsverwaltung

## Workflow

1. **Drei-Säulen-Prüfung speziell**:
 - **Titel**: notarielle Urkunde mit Unterwerfung – wurde sie als "Vollstreckungstitel" ausgestellt (in der Regel formularmäßig "der Eigentümer unterwirft sich ...").
 - Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 - **Zustellung** der vollstreckbaren Ausfertigung an den Schuldner; bei dinglicher Vollstreckung an den Eigentümer (auch Dritter) nach § 800 Abs. 2 ZPO.
2. **Kündigung Grundschuld § 1193 BGB**: sechs Monate Kündigungsfrist, abdingbar nur eingeschränkt (AGB-Kontrolle gem. § 307 BGB). Kündigungsschreiben zustellen.
3. **Sicherungsabrede prüfen**: Welche Forderungen sichert die Grundschuld? Aktuelle Höhe? Zinsen? Übersicherung? Einrede § 1192 Abs. 1a BGB bei Abtretung.
4. **Dingliche Vollstreckung**: ZVG-Antrag → `zv-zvg-antrag-glaeubiger`.
5. **Persönliche Vollstreckung**: zusätzlich PfÜB Bank/Lohn → `zv-pfueb-bank` / `zv-pfueb-arbeitsentgelt`.
6. **Insolvenz**: Bei Schuldner-Insolvenz wird der Grundschuldgläubiger Absonderungsberechtigter (§ 49 InsO) – Vollstreckung außerhalb der Insolvenztabelle weiterhin möglich, aber Verwertung über Insolvenzverwalter ggf. günstiger.

## Klauselumschreibung § 727 ZPO bei Forderungsabtretung

Wird die gesicherte Forderung an einen neuen Gläubiger abgetreten (typisch bei Forderungskäufen, Loan-Sale), muss der neue Gläubiger:

- die Abtretung im notariell beglaubigtem Wege nachweisen
- den Klauselantrag beim ausstellenden Notar (oder hilfsweise § 797 ZPO) stellen
- die Klauselzustellung an den Schuldner durchführen, bevor er aus der Urkunde vollstrecken darf.

Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Sicherungsgrundschuld – Einreden § 1192 Abs. 1a BGB

Schuldner kann gegenüber neuem Erwerber alle Einreden geltend machen, die ihm gegen den ursprünglichen Sicherungsgeber zustanden – auch wenn der neue Erwerber gutgläubig war (Einschränkung des § 1157 Satz 2 BGB).

## Leitentscheidungen

- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Ausgabeformat

```
NOTAR. URKUNDE / GRUNDSCHULD [Mandant] gegen [Schuldner], Az [Notar]

Urkunde: Notar [Name], URNr [Nr/Jahr]
Grundschuld: EUR x, Zinsen x %, GB [Ort, Bl, lfd Nr]
Unterwerfung: [dinglich / persönlich / beides]
Sicherungsabrede: [Datum, Gegenstand]
Kündigung § 1193: [erforderlich? ja, am DD.MM.JJJJ erklärt]
Klausel § 727: [nicht erforderlich / umschrieben am DD.MM.JJJJ]
Zustellung § 750: [erfolgt an DD.MM.JJJJ]
Vollstreckungswege: [ZVG / PfÜB Bank / PfÜB Lohn]

NÄCHSTE SKILLS: zv-zvg-antrag-glaeubiger, zv-pfueb-bank
WIEDERVORLAGE: DD.MM.JJJJ + 6 Monate (Kündigungsfrist)
```

## Qualitätsgates

- Niemals dingliche Vollstreckung ohne wirksame Kündigung § 1193 BGB (Sechs-Monats-Frist).
- Niemals aus Urkunde ohne Klauselumschreibung § 727 ZPO vollstrecken, wenn Forderung abgetreten.
- Niemals persönliche Vollstreckung ohne Unterwerfung in das Vermögen prüfen.
- Bei Verbraucher-Sicherungsgrundschuld AGB-Kontrolle der Unterwerfungsklausel.

