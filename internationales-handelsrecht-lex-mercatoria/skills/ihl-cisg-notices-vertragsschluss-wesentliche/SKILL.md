---
name: ihl-cisg-notices-vertragsschluss-wesentliche
description: "IHL CISG Notices Vertragsschluss Wesentliche: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# IHL CISG Notices Vertragsschluss Wesentliche

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **IHL CISG Notices Vertragsschluss Wesentliche** im Plugin Internationales Handelsrecht Lex Mercatoria. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `ihl-008-cisg-fristen-und-notices` | Internationales Handelsrecht: Untersuchungs- und Rügepflicht nach CISG Art. 38-39 und Art. 43. Beginn der Prüffrist, Anforderungen an die Rüge (Spezifizierungspflicht), Zwei-Jahres-Frist Art. 39 Abs. 2 und Entschuldigungsgründe Art. 44. |
| `ihl-004-cisg-vertragsschluss` | Internationales Handelsrecht: Vertragsschluss nach CISG Art. 14-24. Angebot (Bestimmtheit nach Art. 14), Annahme (Art. 18-22), Widerruflichkeit (Art. 16), Verspätung (Art. 21) und Mirror-Image-Rule vs. modifizierte Annahme (Art. 19). |
| `ihl-005-cisg-wesentliche-vertragsverletzung` | Internationales Handelsrecht: Wesentliche Vertragsverletzung nach CISG Art. 25. Vorhersehbarkeitstest, Erheblichkeit des Nachteils und Rechtsfolge (Vertragsaufhebung Art. 49/64 CISG). Abgrenzung zur unwesentlichen Verletzung und Nacherfüllungsrecht. |
| `ihl-012-schiedsklausel-icc-dis` | Internationales Handelsrecht: Schiedsklauseln nach ICC-Schiedsregeln 2021 und DIS-Schiedsregeln 2018. Musterklauseln, Sitzwahl, Anzahl Schiedsrichter, Verfahrenssprache, Schnellverfahren (Expedited Procedure) und pathologische Klauseln. |

## Arbeitsweg

Im Plugin Internationales Handelsrecht Lex Mercatoria gilt für **IHL CISG Notices Vertragsschluss Wesentliche**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `ihl-008-cisg-fristen-und-notices`

**Fokus:** Internationales Handelsrecht: Untersuchungs- und Rügepflicht nach CISG Art. 38-39 und Art. 43. Beginn der Prüffrist, Anforderungen an die Rüge (Spezifizierungspflicht), Zwei-Jahres-Frist Art. 39 Abs. 2 und Entschuldigungsgründe Art. 44.

# Fristen und Notices: Untersuchung und Rüge (CISG Art. 38-44)

## Worum es geht

Art. 38-39 CISG sind praktisch zentral: Versäumt der Käufer die Rüge, verliert er alle Mangelrechte. Die Untersuchungspflicht (Art. 38) beginnt mit Lieferung; die Rüge (Art. 39) muss spezifiziert und innerhalb angemessener Frist erfolgen. Die CISG-Praxis hat sehr unterschiedliche Fristen entwickelt (OLG: 1-3 Wochen; ICC-Schiedsgerichte oft großzügiger).

## Kernnormen / Kernquellen

- **Art. 38 CISG**: Untersuchungspflicht — so kurze Frist wie in den Umständen praktisch möglich
- **Art. 39 Abs. 1 CISG**: Rügepflicht — Art des Mangels, angemessene Frist nach Entdeckung/Entdeckbarsein
- **Art. 39 Abs. 2 CISG**: Absolute Ausschlussfrist — 2 Jahre ab tatsächlicher Übergabe
- **Art. 40 CISG**: Ausnahme — Verkäufer kannte Mangel und verheimlichte ihn
- **Art. 43 CISG**: Rügepflicht bei Rechten Dritter (Rechtsmängel)
- **Art. 44 CISG**: Entschuldigung für verspätete Rüge — vernünftiger Grund

## Schlüsselbegriffe

- Spezifizierungspflicht: Käufer muss Mangelart bezeichnen (nicht bloß "Mängel")
- Angemessene Frist: von der konkreten Branche, Ware und Mangelsymptomen abhängig
- Verborgene Mängel: Frist beginnt erst mit Entdeckbarkeit (nicht sofort bei Lieferung)
- 2-Jahres-Frist: unabhängig von Untersuchung und Rüge — hartes Limit
- Totalverlust der Mangelrechte bei verspäteter Rüge (kein § 377 HGB-Abminderungs-Kompromiss)

## Typische Streitfragen / Anwendungsfälle

1. Muss Käufer bei Weitertransport nach Lieferung Untersuchung erst am Bestimmungsort durchführen (Art. 38 Abs. 2-3)?
2. Wie spezifiziert muss die Rüge sein — "fehlt Qualitätsstandard X" oder reicht "Qualitätsmangel"?
3. Art. 44 vernünftiger Grund: Reicht schlechte Kommunikation mit Endkunden als Entschuldigung?
4. Kann Verkäufer auf Rüge verzichten (Art. 6 Ausschluss der Rügepflicht)?
5. Läuft 2-Jahres-Frist auch bei arglistig verschwiegenem Mangel (Art. 40 Interaktion)?

## Methodik

- Fristbeginn-Zeitstrahl erstellen: Lieferung → Untersuchung → Entdeckung → Rüge
- Branchenspezifische Fristübungen recherchieren (Lebensmittel kürzer als Maschinen)
- Rügeschreiben immer mit konkreter Mangelbezeichnung und Datum der Entdeckung
- Art. 40 als Gegenargument bei verstecktem Mangel mitprüfen

## Output

- Fristen-Zeitstrahl (Muster)
- Checkliste spezifizierte Rüge
- Muster-Rügeschreiben nach Art. 39

## Quellenregel

CISG Art. 38-44: uncitral.un.org. CISG-Rspr.: CISG-online.ch (Art. 38 >200 Entscheidungen). CISG Advisory Council Opinion No. 2. Schrifttum: Schwenzer in Schlechtriem/Schwenzer (2019) Art. 38-39. Unsicherheit bleibt sichtbar.

## 2. `ihl-004-cisg-vertragsschluss`

**Fokus:** Internationales Handelsrecht: Vertragsschluss nach CISG Art. 14-24. Angebot (Bestimmtheit nach Art. 14), Annahme (Art. 18-22), Widerruflichkeit (Art. 16), Verspätung (Art. 21) und Mirror-Image-Rule vs. modifizierte Annahme (Art. 19).

# CISG Vertragsschluss (Art. 14-24)

## Worum es geht

Das CISG regelt Angebot und Annahme in Art. 14-24 autonom. Ein Angebot ist ausreichend bestimmt (Art. 14 Abs. 1), wenn es Ware, Menge und Preis (oder Preisbestimmungsmethode) nennt. Die modifizierte Annahme (Art. 19) weicht vom Common-Law Mirror-Image-Prinzip ab: wesentliche Abweichungen wirken als Gegenangebot; unwesentliche werden Vertragsinhalt, sofern Anbieter nicht widerspricht.

## Kernnormen / Kernquellen

- **Art. 14 CISG**: Angebot — Bestimmtheit (Ware, Menge, Preis)
- **Art. 15-17 CISG**: Wirksamwerden, Widerruf, Erlöschen
- **Art. 16 CISG**: Widerruflichkeit vs. Bindung (Ausnahmen: Frist gesetzt, Vertrauen)
- **Art. 18 CISG**: Annahme — Erklärung oder schlüssiges Verhalten
- **Art. 19 CISG**: Modifizierte Annahme — wesentliche (Abs. 3) vs. unwesentliche Abweichung
- **Art. 21 CISG**: Verspätete Annahme (Wirksamkeit wenn Anbieter unverzüglich bestätigt)
- **Art. 23-24 CISG**: Zugang als Wirksamkeitsvoraussetzung

## Schlüsselbegriffe

- Bestimmtheit des Angebots (CISG autonom — kein BGB §145-Vergleich)
- Battle of forms unter CISG: Knock-out-Regel vs. Last-Shot (Streit)
- Wesentliche Abweichung nach Art. 19 Abs. 3 (Preis, Zahlung, Qualität, Menge, Ort, Haftung, Streitbeilegung)
- Zugang-Prinzip (Art. 24): Zugang bei mündlicher Erklärung sofort
- Schweigen als Annahme? (Grundsätzlich nein, Ausnahme: Handelsbrauch Art. 9)

## Typische Streitfragen / Anwendungsfälle

1. Ist eine Preisliste ein Angebot i.S.d. Art. 14? (Grundsatz: Einladung zur Abgabe)
2. Battle of Forms: Welche AGB gelten, wenn beide Parteien widersprechende AGB einbeziehen?
3. Wann ist eine Abweichung in der Annahmeerklärung "wesentlich" nach Art. 19 Abs. 3?
4. Kann ein Kaufvertrag durch E-Mail-Korrespondenz (ohne Unterschrift) nach CISG wirksam geschlossen werden?
5. Verspätete Annahme: Wann muss der Anbieter unverzüglich nach Art. 21 Abs. 1 reagieren?

## Methodik

- Art. 14 Bestimmtheit: Preis-Fehlen nicht automatisch fatal (Art. 55 als Lückenfüller — umstritten)
- Battle of Forms: Knock-out-Regel herrschende Meinung in Schiedsgerichtsbarkeit
- Zugang bei E-Mail: Server-Eingang als Zugang (analog Art. 24); elektronische Signatur kein CISG-Thema
- Immer prüfen ob Art. 9 Handelsbrauch eine abweichende Praxis begründet

## Output

- Vertragsschluss-Schema (Angebot → Annahme → Zugang)
- Battle-of-Forms-Matrix: welche Klauseln gelten
- Formulierungshilfe: Schiedsklausel in Angebot integrieren ohne Art. 19 zu riskieren

## Quellenregel

CISG Art. 14-24: uncitral.un.org. CISG-Rspr.: CISG-online.ch, jusmundi.com. Schrifttum: Magnus in Staudinger (2018) Art. 14-24. Unsicherheit bleibt sichtbar.

## 3. `ihl-005-cisg-wesentliche-vertragsverletzung`

**Fokus:** Internationales Handelsrecht: Wesentliche Vertragsverletzung nach CISG Art. 25. Vorhersehbarkeitstest, Erheblichkeit des Nachteils und Rechtsfolge (Vertragsaufhebung Art. 49/64 CISG). Abgrenzung zur unwesentlichen Verletzung und Nacherfüllungsrecht.

# Wesentliche Vertragsverletzung (CISG Art. 25)

## Worum es geht

Art. 25 CISG ist die Schlüsselnorm des CISG-Rechtsbehelfssystems. Nur bei wesentlicher Verletzung darf der Gläubiger den Vertrag aufheben (Art. 49 Abs. 1 lit. a, Art. 64 Abs. 1 lit. a CISG). Die Wesentlichkeit hängt vom erheblichen Nachteil und der Vorhersehbarkeit ab. Der Schuldner kann Wesentlichkeit abwenden, wenn er nachweist, dass er den Nachteil nicht vorhergesehen hat und eine vernünftige Person in seiner Lage ihn auch nicht vorhergesehen hätte.

## Kernnormen / Kernquellen

- **Art. 25 CISG**: Definition — erheblicher Nachteil + Vorhersehbarkeitstest
- **Art. 49 Abs. 1 lit. a CISG**: Aufhebungsrecht des Käufers bei wesentlicher Verletzung
- **Art. 64 Abs. 1 lit. a CISG**: Aufhebungsrecht des Verkäufers
- **Art. 46 Abs. 2 CISG**: Ersatzlieferung nur bei wesentlicher Verletzung
- **Art. 47/48 CISG**: Nachfrist (Fixierung vor Aufhebung bei unwesentlicher Verletzung)
- **Art. 51 CISG**: Teillieferung — Wesentlichkeit für gesamte oder Teillieferung

## Schlüsselbegriffe

- Erheblicher Nachteil (substantial deprivation) — nicht bagatellhafter Mangel
- Vorhersehbarkeit: objektiver Maßstab — vernünftige Person gleicher Art in gleicher Lage
- Kurierlieferung vs. Standardlieferung: Terminüberschreitung als wesentlich?
- Mangel am Kerngegenstand vs. Nebenpflichtverletzung
- Reparierbarkeit als Faktor (CISG-Advisory Council Opinion No. 5)

## Typische Streitfragen / Anwendungsfälle

1. Ist Aliud-Lieferung (falsche Ware) stets wesentlich, auch wenn Käufer sie nutzen kann?
2. Wann ist Lieferverzug wesentlich (Fixgeschäft, Jahreszeitware)?
3. Qualitätsmangel: Reicht Unterschreitung gesetzlicher Grenzwerte für Wesentlichkeit?
4. Kann Verkäufer Wesentlichkeit durch Nachbesserungsangebot (Art. 48) beseitigen?
5. Teillieferung: Wesentlichkeit für gesamten Vertrag nach Art. 51 Abs. 2?

## Methodik

- Zweistufige Prüfung: (1) erheblicher Nachteil, (2) Vorhersehbarkeit
- Wirtschaftliche Auswirkung und Vertragszweck als Maßstab für "erheblich"
- CISG Advisory Council Opinions (op. 5, 9) als nicht bindende Auslegungshilfe
- Rechtsprechungsvergleich: OLG-Rspr. via CISG-online.ch

## Output

- Wesentlichkeits-Checkliste (erheblicher Nachteil / Vorhersehbarkeitstest)
- Entscheidungsbaum: Aufhebung vs. Minderung vs. Nacherfüllung
- Muster-Aufhebungserklärung nach Art. 26 CISG

## Quellenregel

CISG Art. 25: uncitral.un.org. CISG Advisory Council Opinions: cisgac.com. Rechtsprechung: CISG-online.ch. Schrifttum: Huber/Mullis, The CISG (2007) S. 185 ff. Unsicherheit bleibt sichtbar.

## 4. `ihl-012-schiedsklausel-icc-dis`

**Fokus:** Internationales Handelsrecht: Schiedsklauseln nach ICC-Schiedsregeln 2021 und DIS-Schiedsregeln 2018. Musterklauseln, Sitzwahl, Anzahl Schiedsrichter, Verfahrenssprache, Schnellverfahren (Expedited Procedure) und pathologische Klauseln.

# Schiedsklauseln: ICC und DIS

## Worum es geht

Die Schiedsklausel ist die prozessuale Grundlage internationaler Streitbeilegung. ICC (International Chamber of Commerce, Regeln 2021) und DIS (Deutsche Institution für Schiedsgerichtsbarkeit, Regeln 2018) bieten Musterschiedsklauseln. Pathologische Klauseln (widersprüchliche Institution, fehlender Schiedsort) können zur Unzuständigkeit führen.

## Kernnormen / Kernquellen

- **ICC Schiedsregeln 2021 Art. 6**: Schiedsvereinbarung und Zuständigkeit des Gerichtshofs
- **ICC Schiedsregeln 2021 Anhang VI**: Expedited Procedure (automatisch bei < USD 3 Mio.)
- **DIS-Schiedsregeln 2018 § 1**: Schiedsvereinbarung; § 2 Schiedsort
- **New York Konvention 1958 Art. II**: Schriftform der Schiedsvereinbarung
- **UNCITRAL Model Law Art. 7**: Formvorschriften Schiedsvereinbarung (Option I/II)
- **Deutsches Recht: § 1031 ZPO**: Schiedsvereinbarung — Formvorschriften

## Schlüsselbegriffe

- Separabilität der Schiedsklausel (Competence-Competence, Art. 6 ICC Regeln)
- Schiedsort vs. Verfahrensort (Tagungsort) — Recht des Schiedsorts ist lex arbitri
- Schnellverfahren ICC: automatisch anwendbar, opt-out möglich
- Pathologische Klausel: widersprüchlicher Sitz, nicht existente Institution, ausgeschlossene Anfechtung
- Multi-Party/Multi-Contract-Schiedsgerichtsbarkeit (ICC Regeln 2021 Art. 7-10)

## Typische Streitfragen / Anwendungsfälle

1. Gilt ICC Schnellverfahren automatisch auch bei laufenden Verträgen die vor 2021 geschlossen wurden?
2. Wie wähle ich zwischen Einzelschiedsrichter (< 1 Mio. EUR) und Dreierschiedsgericht?
3. Schiedsklausel in AGB: Gilt Einbeziehungserfordernis (§ 1031 Abs. 5 ZPO) bei B2B?
4. Kann Schiedsklausel auf bestimmte Anspruchsarten beschränkt werden (carved-out disputes)?
5. Multi-Party: Wie nominieren mehrere Beklagte einen gemeinsamen Schiedsrichter?

## Methodik

- ICC-Musterklausel als Ausgangspunkt, dann anpassen (Sitz, Sprache, Richteranzahl)
- Schiedsort nach: Neutralität, Vollstreckungsfreundlichkeit, lex arbitri-Qualität
- Schnellverfahren: opt-out ausdrücklich in Klausel, wenn nicht gewünscht
- Pathologische Klauseln: Test vor Unterzeichnung — ist Institution eindeutig identifiziert?

## Output

- ICC-Musterklausel (Standard und Expedited)
- DIS-Musterklausel (Standard)
- Checkliste: Schiedsort-Auswahl nach Vollstreckungsrisiko

## Quellenregel

ICC Regeln 2021: iccwbo.org. DIS Regeln 2018: dis-arb.de. New York Konvention: newyorkconvention.org. § 1031 ZPO: gesetze-im-internet.de. Unsicherheit bleibt sichtbar.
