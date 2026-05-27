---
name: wesentliche-vertraege-anlage
description: "Erstellt das Verzeichnis wesentlicher Verträge (Material Contracts Schedule) aus Due-Diligence-Erkenntnissen auf Grundlage der SPA-Definition und des Anhangformats. Berücksichtigt Change-of-Control-Klauseln (BGH-Rspr.), Vendor-Disclosure-Logik und Konsistenz mit anderen Gewährleistungsanhängen. Lädt bei „Vertragsanhang erstellen\", „Disclosure Schedule\", „wesentliche Verträge\", „Anhang 3.X\" oder beim Entwurf von Offenlegungsanhängen im M&A-Kontext."
---

# Material-Vertragsverzeichnis (Disclosure Schedule)

## Triage zu Beginn

Vor der Anhangs-Erstellung klaeren:

1. **SPA-Definition vorhanden?** Ist die SPA-Definition des Begriffs "wesentlicher Vertrag" (Material Contract) aus dem Vertragstext extrahiert? Falls nicht: SPA zuerst lesen; CLAUDE.md-Schwellenwerte sind nur Fallback.
2. **Transaktionsstruktur:** Share Deal (Gesellschaft mit Vertraegen geht ueber) oder Asset Deal (§ 415 BGB: Zustimmung der Gegenpartei bei Schulduebernahme)? Bei Asset Deal: Zustimmungserfordernisse weitaus umfangreicher.
3. **Due-Diligence-Daten verfuegbar?** Vertragsbestand aus Datenraum oder Disclosure Schedule extrahiert? Falls nicht: DD-Ergebnisse zuerst importieren (Skill `dd-findings-extraktion` oder `tabellenpruefung`).
4. **Anhangformat bekannt?** Gibt es andere Anhaenge im SPA-Entwurf als Formatvorlage? Nummerierte Liste oder Tabelle?
5. **Over-Disclosure-Risiko beachten?** Der Anhang ist eine Gewaehrleistung, kein Datendump. Nur Vertraege aufnehmen, die ein SPA-Kriterium erfuellen.
6. **Regulierte Branche?** Energieversorgung, Finanzdienstleistungen, Gesundheitswesen, oeffentliche Auftraege — behoerdliche Zustimmungspflichten zusätzlich pruefen.

## Zweck

Der Unternehmenskaufvertrag (SPA/Anteilskaufvertrag) enthält eine Gewährleistung: „Anhang [X] listet alle wesentlichen Verträge der Gesellschaft." Dieser Skill erstellt diesen Anhang aus den Due-Diligence-Erkenntnissen — welche Verträge sind wesentlich im Sinne der SPA-Definition, in dem Format, das der SPA vorschreibt.

## Eingaben

- Unternehmenskaufvertrag (SPA) oder Entwurf davon — für die Definition „wesentlicher Vertrag" und das Anhangformat
- Due-Diligence-Erkenntnisse aus dem Vertragsreview (vertragsebene Daten)
- Praxisprofil (CLAUDE.md) → Wesentlichkeitsschwellen (können von der SPA-Definition abweichen — SPA-Definition hat Vorrang)
- Optional: Bestehende Anhänge im SPA als Formatvorlage

## Rechtlicher Rahmen

**Wesentlichkeit / Disclosure:**
§§ 443, 444 BGB (Garantien; Haftungsausschluss); §§ 453, 435 BGB (Sachmängelgewährleistung beim Rechtskauf, Unternehmenskauf); § 311 Abs. 2 BGB (culpa in contrahendo; Offenlegungspflichten in der Due Diligence).

**Change-of-Control-Klauseln:**
BGH, Urt. v. 29.04.2008 – KZR 2/07, NJW 2008, 3055 Rn. 18 (Auslegung einer Change-of-Control-Klausel; Kündigung bei mittelbarem Kontrollwechsel); BGH, Urt. v. 10.11.2016 – I ZR 193/15, NJW-RR 2017, 877 Rn. 14 (Vertragsübernahme ohne Zustimmung des Schuldners; Grenzen der Abtretbarkeit). Vendor Disclosure: Hat der Verkäufer in einem Vendor Due Diligence Report (VDR) auf eine Tatsache hingewiesen, kann er sich im Rahmen der Gewährleistung hierauf berufen (§ 442 BGB analog; str., vgl. BGH, Urt. v. 27.03.2009 – V ZR 30/08, NJW 2009, 2064 Rn. 25).

**Vertragsregister und Anhangpflichten:**
§ 15 GmbHG (Abtretung von Geschäftsanteilen — Auswirkung auf Vertragsabschluss); § 40 GmbHG (Gesellschafterliste); §§ 246 ff. HGB (Jahresabschluss, Vollständigkeit); Art. 6 Abs. 1 lit. c DSGVO (Datenverarbeitung in Due Diligence).

**Kommentarliteratur:**
Bayer, in: Lutter/Hommelhoff, GmbHG, 21. Aufl. 2023, § 15 Rn. 5; Westermann, in: MüKoBGB, 9. Aufl. 2022, § 453 Rn. 12 (Unternehmenskauf, Gewährleistung); Hopt, in: Baumbach/Hopt, HGB, 41. Aufl. 2024, § 25 Rn. 1 (Firmenfortführung und Vertragskontinuität).

## Ablauf

### Schritt 1: SPA-Definition ermitteln

Die Definition „wesentlicher Vertrag" aus dem SPA extrahieren — die SPA-Definition ist maßgeblich, nicht der eigene Schwellenwert aus CLAUDE.md. Bei Abweichungen: SPA-Definition verwenden und die Differenz flaggen.

Transaktionsstruktur beachten (Share Deal / Asset Deal / Verschmelzung): Bei einem Asset Deal nach §§ 433 ff. BGB sind Zustimmungserfordernisse bei Vertragsübergang nach § 415 BGB anders zu behandeln als beim Share Deal, wo die Gesellschaft mit ihren Verträgen übergeht. Regulierte Branchen (Energieversorgung, Finanzdienstleistungen, Gesundheitswesen, öffentliche Aufträge) können zusätzliche behördliche Zustimmungspflichten begründen — diese sind gesondert zu recherchieren und mit Norm zu belegen.

Typische Prüfkategorien aus SPA-Definitionen (kein Ersatz für die tatsächliche SPA-Lektüre):
- Jahres- oder Gesamtwertschwelle
- Vertragslaufzeit
- Change-of-Control- oder Abtretungsbeschränkung
- Exklusivität oder Wettbewerbsverbot
- Top-N-Kunden- oder Lieferantenverträge
- Grundstücksnutzungsverträge (Miet- und Pachtverträge)
- IP-Lizenzen (in- und outbound)
- Konzerninterneliche Verträge (Related-Party-Agreements)
- Öffentliche Aufträge / Vergabeverträge
- Außerordentliche Verträge (außerhalb des gewöhnlichen Geschäftsbetriebs)

### Schritt 2: Definition auf Due-Diligence-Erkenntnisse anwenden

Für jeden geprüften Vertrag:

| Vertrag | Erfüllte Prüfkriterien | Aufnahme |
|---|---|---|
| [Name] | [Jahreswert > X EUR; CoC-Klausel] | Ja |
| [Name] | [keines] | Nein |

**Grenzfälle zur menschlichen Entscheidung flaggen:**
- Vertrag liegt knapp unterhalb des Schwellenwerts, ist aber geschäftlich bedeutsam
- Vertrag erfüllt ein Prüfkriterium, wird aber ohnehin beendet
- Mündliche Vereinbarungen oder Side Letters, deren Zuordnung zweifelhaft ist
- Lieferantenverträge mit Exklusivitätsklauseln, die nicht ausdrücklich als „wesentlich" eingestuft wurden

### Schritt 3: Anhangdaten zusammenstellen

Für jeden aufzunehmenden Vertrag werden typischerweise benötigt:

| Feld | Quelle |
|---|---|
| Name der Vertragspartei / Gegenpartei | Vertrag |
| Vertragsbezeichnung und -typ | Vertrag |
| Datum | Vertrag |
| Laufzeit / Ablauf | Vertrag |
| Jahres- / Gesamtwert | Vertrag oder Unternehmensdaten |
| Erfülltes SPA-Prüfkriterium | Schritt-2-Analyse |
| Zustimmungserfordernis für die Transaktion | Due-Diligence-Erkenntnis |
| Datenraum-Referenz | Due-Diligence-Verzeichnis |

Aus bestehenden Due-Diligence-Extraktionen ziehen. Fehlende Felder flaggen — nicht schätzen.

### Schritt 4: Format nach SPA

Offenlegungsanhänge haben ein einheitliches Format — in der Regel eine nummerierte Liste oder Tabelle, teilweise mit Unterabschnitten nach Vertragstyp. Format der anderen Anhänge im SPA-Entwurf übernehmen.

```markdown
## Anhang [X] — Wesentliche Verträge

Die folgenden Verträge sind wesentliche Verträge im Sinne des Kaufvertrags:

### (a) Kundenverträge

1. [Vertragsbezeichnung], datiert [Datum], zwischen [Zielgesellschaft] und [Gegenpartei].
   [Kurzbeschreibung, falls das Format eine solche vorsieht.]
   [Datenraum: Pfad]

2. [...]

### (b) Lieferantenverträge

[...]

### (c) Grundstücksnutzungsverträge

[...]

### (d) IP-Lizenzverträge

[...]

[etc. — Unterabschnitte gemäß SPA-Definitionsstruktur]
```

### Schritt 5: Zustimmungs-Overlay

Separat (nicht im Anhang selbst — dies ist interne Arbeit): Verfolgen, welche Vertragsanhänge Zustimmungen erfordern.

> Das Zustimmungs-Overlay und jeder Vorentwurf des Anhangs stammen aus privilegierten Due-Diligence-Unterlagen und teilen deren Vertraulichkeitsstatus gemäß § 43a Abs. 2 BRAO. Interne Annotationen vor Übergabe des finalen Anhangs als Vertragsanlage entfernen.

| Anhang # | Gegenpartei | Zustimmung erforderlich | Status | Verantwortlich | Frist |
|---|---|---|---|---|---|
| X(a)(1) | [Name] | Ja — CoC § 12.2 | Angefragt | [Name] | [Datum] |

Dieses Overlay speist die Abschluss-Checkliste.

### Schritt 6: Gegenprüfung

Vor Übergabe:
- Jeder Vertrag, der ein Prüfkriterium erfüllt, ist im Anhang (Vollständigkeit)
- Kein Vertrag, der kein Prüfkriterium erfüllt, ist im Anhang (kein Over-Disclosure — es ist eine Gewährleistung, kein Datendump)
- Anhang ist konsistent mit anderen Gewährleistungsanhängen (ein Vertrag in Anhang [X], der ein Pfandrecht begründet, muss auch im Pfandrechtsanhang erscheinen)
- Jeder Eintrag hat eine Datenraum-Referenz, damit Käuferberater das Ursprungsdokument findet

## Ausgabeformat

- Anhang im SPA-konformen Format (Markdown, uebertragbar in Word/PDF)
- Internes Zustimmungs-Overlay als Tabelle (fuer Abschluss-Checkliste)
- Flaggenliste mit Grenzfaellen zur menschlichen Entscheidung

## Output-Template

**Adressat:** Transaktionsteam / SPA-Verhandlung — Tonfall: praezise-strukturiert, SPA-konform

```
## Anhang [X.X] — Wesentliche Vertraege (Material Contracts)

> INTERN: Dieser Anhang-Entwurf ist ein privilegiertes Arbeitsdokument.
> Interne Annotationen ([INTERN: ...]) vor Lieferung als SPA-Anlage entfernen.
> Vertraulichkeit: Mandatsgeheimnis § 43a Abs. 2 BRAO.

Die folgenden Vertraege sind wesentliche Vertraege im Sinne der Definition
in § [N] des Kaufvertrages vom [DATUM] ([KURZBEZEICHNUNG SPA]):

### (a) Kundenvertraege

1. [VERTRAGSBEZEICHNUNG], datiert [TT.MM.JJJJ], zwischen [ZIELGESELLSCHAFT GmbH]
   und [GEGENPARTEI].
   [KURZBESCHREIBUNG, falls SPA-Format eine solche vorschreibt.]
   Erfuelltes SPA-Kriterium: [JAHRESWERT > EUR / CoC-Klausel / etc.]
   [INTERN: Datenraum-Referenz: VDR/[PFAD]/[DATEINAME]]
   [INTERN: Zustimmungserfordernis: [JA / NEIN]; Status: [ANGEFRAGT / ERHALTEN / VERWEIGERT]]

2. [Weitere Eintraege analog]

### (b) Lieferantenvertraege

[Analog zu (a)]

### (c) Grundstuecksnutzungsvertraege

[Analog zu (a)]

### (d) IP-Lizenzvertraege (in- und outbound)

[Analog zu (a)]

### (e) Konzerninterneliche Vertraege (Related-Party-Agreements)

[Analog zu (a)]

[Weitere Unterkategorien gemaess SPA-Definitionsstruktur]

---

## Internes Zustimmungs-Overlay (nicht im finalen Anhang)

| Anhang-Nr. | Vertragsbezeichnung | Gegenpartei | Zustimmung erforderlich | Status | Verantwortlich | Frist |
|---|---|---|---|---|---|---|
| X.X.a.1 | [NAME] | [GEGENPARTEI] | [JA — CoC § 12.2 / NEIN] | [ANGEFRAGT / ERHALTEN] | [PERSON] | [DATUM] |

## Flaggenliste — Grenzfaelle (menschliche Entscheidung erforderlich)

1. **[VERTRAGSNAME]**: Jahreswert [BETRAG EUR] — knapp unter SPA-Schwelle, aber geschaeftlich bedeutsam.
   Empfehlung: [AUFNEHMEN / WEGLASSEN] — Entscheidung erbeten bis: [DATUM]
2. **[VERTRAGSNAME]**: Erfuellt Kriterium, wird aber beendet zum [DATUM].
   Empfehlung: [MIT HINWEIS AUF BEENDIGUNG AUFNEHMEN / WEGLASSEN]
```

## Rote Schwellen

- **SPA-Definition nicht gelesen, CLAUDE.md-Schwellenwerte verwendet** — Anhang kann unvollstaendig sein oder Over-Disclosure enthalten; SPA-Definition zwingend vorher lesen.
- **Over-Disclosure: nicht-wesentliche Vertraege im Anhang** — jeder Eintrag begruendet eine Verkaeufer-Gewaehrleistung; Fehler oder Luecken im Anhang koennen Schadenersatzansprueche ausloesen.
- **Datenraum-Referenz fehlt** — Kaeuferberater kann Ursprungsdokument nicht finden; Closing-Prozess verzoegert sich; jeder Eintrag braucht VDR-Referenz.
- **Interne Annotationen in finalem Anhang belassen** — Anwaltsarbeit wird sichtbar; vor Lieferung alle [INTERN: ...]-Kommentare entfernen.
- **Anhang-Konsistenz nicht geprueft** — ein Vertrag in Anhang [X] (wesentliche Vertraege) und in Anhang [Y] (Pfandrechte) muessen konsistent sein; Querverweisung vor Lieferung pruefen.

## Beispiel

**Szenario:** GmbH-Anteilskauf, SPA-Definition wesentlicher Vertrag: Jahreswert > 50.000 EUR ODER Change-of-Control-Klausel ODER IP-Lizenz.

Due-Diligence-Ergebnis: 127 geprüfte Verträge. 23 erfüllen mindestens ein Kriterium. Anhang [X] enthält 23 Einträge in 4 Unterabschnitten. Zustimmungs-Overlay: 8 Verträge mit CoC-Klauseln → Übergabe an Integrations-Tracker.

## Risiken und typische Fehler

- **Wesentlichkeitsdefinition aus CLAUDE.md statt SPA verwenden.** Die SPA-Definition kontrolliert — immer aus dem Vertragstext lesen.
- **Over-Disclosure.** Es ist eine Gewährleistung, keine Datenmigration. Nur Verträge aufnehmen, die mindestens ein SPA-Prüfkriterium erfüllen.
- **Datenraum-Referenzen weglassen.** Jeder Eintrag muss lokalisierbar sein — Käuferberater muss Ursprungsdokument finden können.
- **Anhang-Konsistenz nicht prüfen.** Ein Vertrag kann mehrere Anhänge berühren (z.B. Hauptkundensvertrag + Pfandrecht + verwandte Partei). Querverweisung notwendig.
- **Interne Annotationen im Lieferanhang belassen.** Vertraulichkeitsstatus und Arbeitsnotizen vor finaler Übergabe entfernen.
- **Asset-Deal-Besonderheiten ignorieren.** Bei Asset Deal: § 415 BGB (Schuldübernahme mit Gläubigerzustimmung), §§ 398 ff. BGB (Forderungsabtretung). Change-of-Control-Klauseln können auch bei Share Deals ausgelöst werden — BGH, Urt. v. 29.04.2008 – KZR 2/07.

## Quellenpflicht

Alle rechtlichen Beurteilungen in der Analyse sind mit Norm und ggf. Rechtsprechung zu belegen:
- Gesetzliche Grundlage: `§§ 443, 444 BGB`, `§ 415 BGB`
- BGH-Entscheidungen: `BGH, Urt. v. 29.04.2008 – KZR 2/07, NJW 2008, 3055 Rn. 18`
- Kommentare: `Westermann, in: MüKoBGB, 9. Aufl. 2022, § 453 Rn. 12`

Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall.
