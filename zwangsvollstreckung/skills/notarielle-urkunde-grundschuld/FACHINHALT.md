---
name: notarielle-urkunde-grundschuld
description: "Für Vollstreckung aus notarieller Grundschuldurkunde: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt."
---

# Vollstreckung aus notarieller Grundschuldurkunde

## Arbeitsbereich

Gläubiger hat eine notarielle Grundschuldurkunde und will vollstrecken. Prüfraster: Unterwerfung nach Paragraf 794 Absatz 1 Nummer 5 ZPO, dinglicher und persönlicher Titel, Klauselumschreibung nach Paragraf 727 ZPO, Sicherungsabrede, Kündigung und Sechsmonatsfrist nach Paragraf 1193 BGB sowie ZVG oder PfÜB als Vollstreckungsweg. Output: Vollstreckungsstrategie und ausformulierter Antrag. Abgrenzung zu `zvg-antrag-glaeubiger` und `titel-klausel-zustellung`.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
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
4. **Dingliche Vollstreckung**: ZVG-Antrag → `zvg-antrag-glaeubiger`.
5. **Persönliche Vollstreckung**: zusätzlich PfÜB Bank/Lohn → `pfueb-bank` / `pfueb-arbeitsentgelt`.
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

NÄCHSTE SKILLS: zvg-antrag-glaeubiger, pfueb-bank
WIEDERVORLAGE: DD.MM.JJJJ + 6 Monate (Kündigungsfrist)
```

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht und Formatstandard.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig.
>
> **Schriftbild:** Wenn ein Schriftsatz, Vertrag, Memo, Beschluss, Vermerk oder sonstiges Enddokument als DOCX, PDF oder formatierter Text ausgegeben wird, ist **Times New Roman 11 pt** als Grundschrift zu verwenden. Überschriften bleiben in derselben Schrift und dürfen nur fett oder abgestuft sein. Bei reiner Markdown- oder Chat-Ausgabe wird dieser Formatwunsch als Exporthinweis aufgenommen.
>
> **Nummerierung:** Gliederung ausschließlich dezimal (`1`, `1.1`, `1.1.1` und so weiter). Keine römischen Ziffern, keine Buchstaben- oder Mischgliederung.
<!-- END ausformulierungspflicht (autogen) -->

## Qualitätsgates

- Niemals dingliche Vollstreckung ohne wirksame Kündigung § 1193 BGB (Sechs-Monats-Frist).
- Niemals aus Urkunde ohne Klauselumschreibung § 727 ZPO vollstrecken, wenn Forderung abgetreten.
- Niemals persönliche Vollstreckung ohne Unterwerfung in das Vermögen prüfen.
- Bei Verbraucher-Sicherungsgrundschuld AGB-Kontrolle der Unterwerfungsklausel.
