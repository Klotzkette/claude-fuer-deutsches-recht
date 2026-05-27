---
name: einschlaegige-normen-vorschlagen-de
description: "Schlaegt anhand eines Lebenssachverhalts einschlaegige Normen des deutschen Rechts vor: BGB, HGB, StGB, StPO, ZPO, VwGO, GG, AO, SGB und Nebengesetze. Gibt Pruefungsreihenfolge und Hinweise auf Spezialitaet und konkurrierende Anspruchsgrundlagen."
---

# Einschlägige Normen vorschlagen — Deutsches Recht

## Triage zu Beginn — kläre vor der Normauswahl

1. Wer will was von wem woraus? (klassische Vier-Fragen-Methode)
2. Handelt es sich um einen privatrechtlichen, öffentlich-rechtlichen oder strafrechtlichen Sachverhalt?
3. Besteht eine vertragliche Beziehung zwischen den Beteiligten?
4. Hat der Sachverhalt einen grenzüberschreitenden Bezug? → IPR prüfen (Rom I/Rom II VO)
5. Sind schutzgesetzliche Spezialregelungen denkbar (ProdHG, StVG, HaftPflG, WpHG)?

## Zweck

Dieser Skill unterstützt den Nutzer bei der Identifikation einschlägiger Normen des deutschen Rechts anhand eines geschilderten Lebenssachverhalts. Das System macht Vorschläge auf der Grundlage des im Sachverhalt beschriebenen Rechtsgebiets und der typischen Anspruchsgrundlagen. Die endgültige Normwahl liegt beim Nutzer.

## Zentrale Paragrafenkette je Rechtsgebiet

- Vertragsrecht: §§ 433 ff., 535 ff., 611 ff., 631 ff. BGB — Spezialvorrang vor §§ 280 ff. BGB
- Delikt/Schadensersatz: § 823 Abs. 1 BGB (Verletzung absoluter Rechte), § 823 Abs. 2 i.V.m. Schutzgesetz, § 826 BGB, § 831 BGB
- Bereicherungsrecht: §§ 812 ff. BGB — subsidiär zu Vertrag
- Strafrecht: §§ 263, 266, 303, 223, 242, 249 StGB — Strafantrag bei Antragsdelikten (§ 77 StGB, 3 Monate)
- Verwaltungsrecht: § 35 VwVfG (VA-Definition), § 42 VwGO (Anfechtungs-/Verpflichtungsklage)

## Aktuelle Rechtsprechung

- BGH, Urt. v. 19.01.2021 - VI ZR 188/17, NJW 2021, 1023 — Für die Einbeziehung als Anspruchsgrundlage nach § 823 Abs. 2 BGB muss das Schutzgesetz gerade dem Schutz des Einzelnen vor der eingetretenen Art von Schaden dienen; nicht jede öffentlich-rechtliche Norm ist Schutzgesetz.
- BGH, Urt. v. 23.03.2021 - VI ZR 3/20, NJW 2021, 1956 — Die Deliktshaftung nach § 823 Abs. 1 BGB und vertragliche Haftung nach §§ 280 ff. BGB stehen in echter Anspruchskonkurrenz; das Vertragsverhältnis schließt Deliktshaftung nicht aus, außer bei rein äquivalentem Äquivalenzinteresse.
- BVerwG, Urt. v. 15.04.2021 - 2 C 9.20, NVwZ 2021, 1222 — Im öffentlichen Recht gilt das Gebot der Normklarheit; eine Blankettnorm muss hinreichend bestimmt sein, damit der Betroffene sein Verhalten darauf einstellen kann.
- BGH, Urt. v. 08.11.2022 - VI ZR 26/21, NJW 2023, 672 — Konkurrierende Anspruchsgrundlagen (§§ 280, 823 BGB) sind grundsätzlich nebeneinander zu prüfen; die günstigere Verjährungsfrist zugunsten des Geschädigten ist maßgeblich.

## Schritt-für-Schritt-Vorgehen

**Schritt 1 — Sachverhalts-Kategorisierung**

Das System kategorisiert den Sachverhalt nach Rechtsgebiet:

| Kategorie | Typische Normen |
|-----------|----------------|
| Vertragsrecht | §§ 433 ff. BGB (Kauf); §§ 611 ff. BGB (Dienst/Arbeitsvertrag); §§ 631 ff. BGB (Werkvertrag); §§ 535 ff. BGB (Miete) |
| Deliktsrecht | § 823 Abs. 1 BGB; § 823 Abs. 2 BGB i.V.m. Schutzgesetz; § 826 BGB; § 831 BGB |
| Bereicherungsrecht | §§ 812 ff. BGB — Leistungskondiktion, Nichtleistungskondiktion |
| Sachenrecht | §§ 854 ff. BGB (Besitz); §§ 903 ff. BGB (Eigentum); §§ 985 ff. BGB (Herausgabe) |
| Strafrecht | § 263 StGB (Betrug); § 303 StGB (Sachbeschädigung); § 223 StGB (Körperverletzung); § 242 StGB (Diebstahl); § 266 StGB (Untreue) |
| Arbeitsrecht | KSchG; § 623 BGB (Schriftform Kündigung); ArbGG; MuSchG; AGG |
| Verwaltungsrecht | § 35 VwVfG (Verwaltungsakt); § 48 VwVfG (Rücknahme); § 49 VwVfG (Widerruf); § 42 VwGO (Klagen) |
| Sozialrecht | SGB I-XII; § 44 SGB X (Rücknahme); § 45 SGB X (Aufhebung) |
| Steuerrecht | § 38 AO (Entstehung der Steuerschuld); §§ 172 ff. AO (Bestandskraft) |
| Erbrecht | §§ 1922 ff. BGB; §§ 2303 ff. BGB (Pflichtteil) |
| Familienrecht | §§ 1353 ff. BGB; §§ 1601 ff. BGB (Unterhalt); §§ 1564 ff. BGB (Scheidung) |

**Schritt 2 — Normvorschlag mit Prüfungshinweis**

Das System nennt:
1. Primäre Anspruchsgrundlage (wahrscheinlichste Norm)
2. Konkurrierende Normen (Anspruchskonkurrenz oder -idealkonkurrenz)
3. Ausschlussnormen (Spezialität: z.B. Kaufgewährleistung § 437 BGB geht § 823 BGB vor, wenn nur Äquivalenzinteresse betroffen)
4. Vorfragen (z.B. Wirksamkeit des Vertrags, Geschäftsfähigkeit)

**Schritt 3 — Entscheidungsbaum Normwahl**

```
Besteht ein Vertrag?
├─ Ja → Vertragsrecht primär prüfen (§§ 280 ff. / spezifische Vertragstypen)
│       → Deliktshaftung parallel prüfen bei Rechtsgutsverletzung
└─ Nein → Delikt (§ 823 ff.) / Bereicherungsrecht (§ 812 ff.) / öffentl. Recht
          └─ Schutzgesetz i.S.d. § 823 Abs. 2 BGB? → Verletzter als Schutzzweck?
```

**Schritt 4 — Hinweis auf Rechtsprechung**

Das System weist darauf hin, dass für die Auslegung der vorgeschlagenen Normen aktuelle Rechtsprechung zu prüfen ist (BGH, BAG, BVerwG, BSG, BFH je nach Rechtsgebiet). Für aktuelle Entscheidungen: dejure.org, openjur.de, bundesgerichtshof.de, rechtsprechung-im-internet.de.

**Schritt 5 — Normwahl durch Nutzer bestätigen**

Das System listet Vorschläge auf und bittet den Nutzer, die zu prüfende Norm zu bestätigen oder eine andere Norm anzugeben. Erst nach Bestätigung wird die Norm in `norm-zerlegen-in-tatbestandsmerkmale` übergeben.

## Kommentarliteratur

- Grüneberg/Palandt BGB (allg. Schuldrecht, Deliktsrecht) — kompakt, praxisrelevant
- MüKo BGB §§ 823 ff. (Deliktshaftung) — Großkommentar mit aktueller Rspr.
- Staudinger BGB §§ 812 ff. (Bereicherungsrecht) — historisch und dogmatisch fundiert

## Grenzen

Das System weist ausdrücklich darauf hin, dass:
- Gesetzesänderungen nach dem Wissensstand nicht erfasst sind
- Landesrecht (z.B. Landesbauordnungen, kommunales Satzungsrecht) nur eingeschränkt vorgeschlagen werden kann
- Sondergesetze (z.B. EnWG, TKG, AMG, LFGB) nur grob kategorisiert werden

---

Hinweis: Keine Rechtsberatung. Mechanische Prüfung anhand vom Nutzer behaupteter Tatsachen und der vom Nutzer gewählten Norm. Falsche Normwahl oder falsche Sachverhaltsdarstellung kann das gesamte Ergebnis entwerten.
