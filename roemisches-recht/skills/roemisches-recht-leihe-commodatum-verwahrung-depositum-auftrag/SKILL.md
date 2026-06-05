---
name: roemisches-recht-leihe-commodatum-verwahrung-depositum-auftrag
description: "Leihe Commodatum Verwahrung Depositum Auftrag: bündelt 8 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Leihe Commodatum Verwahrung Depositum Auftrag

## Arbeitsbereich

Dieser Skill bündelt 8 sachlich verwandte Arbeitsschritte rund um **Leihe Commodatum Verwahrung Depositum Auftrag** im Plugin Römisches Recht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `rom-024-leihe-commodatum` | Römisches Recht: Commodatum (Leihe) als Realkontrakt nach D. 13.6 und Gaius Inst. 3.196 - unentgeltliche Gebrauchsüberlassung, actio commodati (directa/contraria), Haftungsmaßstab (custodia oder culpa). |
| `rom-025-verwahrung-depositum` | Römisches Recht: Depositum (Verwahrung) nach D. 16.3 und Gaius Inst. 3.196 - unentgeltliche Aufbewahrung fremder Sache, actio depositi directa/contraria, dolus-Haftung, depositum miserabile. |
| `rom-026-auftrag-mandatum` | Römisches Recht: Mandatum (Auftrag) als Konsensualkontrakt nach D. 17.1 und Gaius Inst. 3.155-162 - Unentgeltlichkeit, actio mandati directa/contraria, mandatum post mortem und Widerruf. |
| `rom-027-gesellschaft-societas` | Römisches Recht: Societas (Gesellschaft) als Konsensualkontrakt nach D. 17.2 und Gaius Inst. 3.148-154 - societas omnium bonorum, quaestus, Haftung (diligentia quam in suis), actio pro socio. |
| `rom-028-buergschaft-und-sicherheiten` | Römisches Recht: Bürgschaft und persönliche Sicherheiten - sponsio, fidepromissio, fideiussio nach Gaius Inst. 3.115-127, D. 46.1 (Ulpian) und SC Velleianum (Haftungsausschluss für Frauen). |
| `rom-029-realvertraege-system` | Römisches Recht: Realkontrakte nach Gaius Inst. 3.90 - mutuum, commodatum, depositum, pignus als durch Hingabe der Sache (re) entstehende Verträge und ihre systematische Stellung im Obligationenrecht. |
| `rom-030-konsensualvertraege-system` | Römisches Recht: Konsensualkontrakte (consensu contrahitur) nach Gaius Inst. 3.135 - emptio venditio, locatio conductio, mandatum, societas und die Bedeutung des bloßen Konsenses für die obligatio. |
| `rom-031-innominatkontrakte` | Römisches Recht: Innominatkontrakte (contractus innominati) nach D. 19.5 und D. 2.14 - Vier-Typen-Schema (do ut des etc.), actio praescriptis verbis und Abgrenzung zu Nominalkontrakten. |

## Arbeitsweg

Im Plugin Römisches Recht gilt für **Leihe Commodatum Verwahrung Depositum Auftrag**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `rom-024-leihe-commodatum`

**Fokus:** Römisches Recht: Commodatum (Leihe) als Realkontrakt nach D. 13.6 und Gaius Inst. 3.196 - unentgeltliche Gebrauchsüberlassung, actio commodati (directa/contraria), Haftungsmaßstab (custodia oder culpa).

# Leihe (commodatum)

## Worum es geht

Das commodatum ist die unentgeltliche Gebrauchsüberlassung einer nicht-vertretbaren Sache: der Verleiher (commodans) gibt eine Sache dem Entleiher (commodatarius) zum Gebrauch ohne Übereignung; dieser schuldet Rückgabe der Sache selbst. Zweiseitig unvollkommen: actio commodati directa des Verleihers auf Rückgabe; actio commodati contraria des Entleihers auf Aufwendungsersatz. Haftungsmaßstab ist umstritten.

## Kernquellen

- **D. 13.6.1 pr. (Ulpian)**: Commodatum - Definition und actio commodati
- **D. 13.6.5.2 (Ulpian)**: Haftungsmaßstab: culpa levis in abstracto
- **Gaius Inst. 3.196**: Commodatum als Realkontrakt
- **D. 13.6.17.3 (Scaevola)**: Haftung des Entleihers für Diebstahl durch Dritte (custodia)
- **Iust. Inst. 3.14.2**: Commodatum
- **D. 13.6.18 pr. (Paulus)**: Grenze des vereinbarten Gebrauchs

## Schlüsselbegriffe

- commodans: Verleiher (bleibt Eigentümer und Besitzer)
- commodatarius: Entleiher (erhält nur Gebrauchsrecht)
- actio commodati directa: Klage des Verleihers auf Rückgabe
- actio commodati contraria: Klage des Entleihers auf Aufwandersatz
- furtum usus: Gebrauch über Abrede hinaus als Diebstahl
- custodia-Haftung: erhöhte Haftung für fremde Sachen

## Typische Streitfragen / Forschungsfragen

1. Haftungsmaßstab: culpa levis oder custodia beim commodatarius?
2. Entgeltlichkeit als Abgrenzung zu locatio conductio
3. Furtum usus: Gebrauchsdiebstahl beim Entleiher möglich?
4. Commodatum an Hauskinder: obligatio naturalis?
5. Vergleich: commodatum vs. BGB §§ 598ff. (Leihe)

## Methodik

- D. 13.6 (De commodato) als Haupttitel
- Gaius Inst. 3.196; Iust. Inst. 3.14.2
- Kaser RP I §§ 223-226; Zimmermann Law of Obligations Kap. 7

## Output

- Schema: commodatum - Pflichten beider Parteien
- Haftungsübersicht nach Verschuldensmaßstab
- Abgrenzung: commodatum vs. mutuum vs. locatio rei
- Vergleich röm. commodatum vs. BGB Leihe

## Quellenregel

D. 13.6 (Mommsen-Krüger). Gaius Inst. 3. Iust. Inst. 3.14. Kaser RP I. Zimmermann Law of Obligations.

## 2. `rom-025-verwahrung-depositum`

**Fokus:** Römisches Recht: Depositum (Verwahrung) nach D. 16.3 und Gaius Inst. 3.196 - unentgeltliche Aufbewahrung fremder Sache, actio depositi directa/contraria, dolus-Haftung, depositum miserabile.

# Verwahrung (depositum)

## Worum es geht

Das depositum ist die unentgeltliche Verwahrung einer fremden Sache. Der Hinterleger (deponens) übergibt die Sache dem Verwahrer (depositarius) ohne Übereignung; dieser schuldet Rückgabe auf Verlangen. Haftung des Verwahrers nur für dolus (Vorsatz), nicht für culpa (D. 16.3.1.6, Ulpian). Ausnahme: depositum miserabile (Notverwahrung in Gefahrensituation: höhere Haftung, D. 16.3.1.1).

## Kernquellen

- **D. 16.3.1 pr. (Ulpian)**: Depositum - Definition und Klage
- **D. 16.3.1.6 (Ulpian)**: Haftung nur für dolus
- **D. 16.3.1.1 (Ulpian)**: Depositum miserabile - Notverwahrung
- **Gaius Inst. 3.196**: Depositum als Realkontrakt
- **D. 16.3.11 (Africanus)**: actio depositi bei Konkurs
- **Iust. Inst. 3.14.3**: Depositum systematisch

## Schlüsselbegriffe

- deponens: Hinterleger (bleibt Eigentümer)
- depositarius: Verwahrer (kein Gebrauchsrecht)
- actio depositi directa: Klage auf Rückgabe
- actio depositi contraria: Gegenklage auf Aufwendungsersatz
- depositum irregulare: Verwahrung von Geld mit Vermischung
- depositum miserabile: Notverwahrung (erhöhte Haftung in duplum)

## Typische Streitfragen / Forschungsfragen

1. Dolus-Haftung: warum so mild beim Verwahrer?
2. Depositum irregulare und Geldverwahrung: Eigentumsübergang?
3. Depositum miserabile: Rechtsfolge in duplum
4. Haftung für Dritte, die Zugang zum Depot haben
5. Vergleich: depositum vs. BGB §§ 688ff. (Verwahrungsvertrag)

## Methodik

- D. 16.3 (Depositi vel contra) als Haupttitel
- Gaius Inst. 3.196; Iust. Inst. 3.14.3
- Kaser RP I §§ 226-228; Zimmermann Law of Obligations Kap. 8

## Output

- Schema: depositum - Parteien und Pflichten
- Haftungsübersicht: dolus vs. culpa vs. Notverwahrung
- Abgrenzung depositum - mutuum (bei Geld)
- Vergleich röm. depositum vs. BGB Verwahrung

## Quellenregel

D. 16.3 (Mommsen-Krüger). Gaius Inst. 3. Iust. Inst. 3.14.3. Kaser RP I. Zimmermann Law of Obligations.

## 3. `rom-026-auftrag-mandatum`

**Fokus:** Römisches Recht: Mandatum (Auftrag) als Konsensualkontrakt nach D. 17.1 und Gaius Inst. 3.155-162 - Unentgeltlichkeit, actio mandati directa/contraria, mandatum post mortem und Widerruf.

# Auftrag (mandatum)

## Worum es geht

Das mandatum ist der unentgeltliche Auftrag eines Mandanten (mandans) an einen Beauftragten (mandatarius). Entgeltlichkeit schließt das mandatum aus und begründet locatio conductio operarum (Gaius Inst. 3.162). Der Mandatar haftet für culpa (D. 17.1.8, Ulpian). Actio mandati directa: Klage des Mandanten; contraria: Klage des Mandatars auf Aufwandersatz. Mandatum endet bei Tod einer Partei oder Widerruf.

## Kernquellen

- **Gaius Inst. 3.155**: Mandatum - vier Untertypen
- **Gaius Inst. 3.162**: Entgeltlichkeit als Abgrenzung zur locatio conductio
- **D. 17.1.1 pr. (Paulus)**: Mandatum-Definition
- **D. 17.1.8.9 (Ulpian)**: Haftungsmaßstab culpa levis
- **D. 17.1.27.3 (Ulpian)**: Mandatum post mortem (Ungültigkeit)
- **D. 17.1.15 (Paulus)**: Mandatum tua tantum gratia (einseitig nützlich)

## Schlüsselbegriffe

- mandans: Auftraggeber
- mandatarius: Beauftragter
- actio mandati directa: Klage des Mandanten auf Rechenschaft/Herausgabe
- actio mandati contraria: Gegenklage auf Aufwendungsersatz
- mandatum post mortem: Auftrag über Tod hinaus (klassisch ungültig)
- procurator omnium bonorum: allgemeiner Vertreter (häufigste Praxis)

## Typische Streitfragen / Forschungsfragen

1. Mandatum vs. procuratio: Vollmacht oder Auftrag?
2. Mandatum tua tantum gratia: rechtlich unverbindlich (D. 17.1.2 pr.)?
3. Tod des Mandanten: Erlöschen oder Weitergeltung für dringende Geschäfte?
4. Haftung für Dritte, die Mandatar einschaltet
5. Vergleich: mandatum vs. BGB §§ 662ff. (Auftrag) und §§ 164ff. (Vollmacht)

## Methodik

- D. 17.1 (Mandati vel contra) als Haupttitel
- Gaius Inst. 3.155-162
- Iust. Inst. 3.26
- Kaser RP I §§ 226-230; Zimmermann Law of Obligations Kap. 15

## Output

- Schema: mandatum - vier Untertypen nach Gaius
- Pflichten- und Haftungsübersicht
- Memo: mandatum und Stellvertretung
- Vergleich röm. mandatum vs. BGB Auftrag

## Quellenregel

D. 17.1 (Mommsen-Krüger). Gaius Inst. 3.155-162. Iust. Inst. 3.26. Kaser RP I. Zimmermann Law of Obligations.

## 4. `rom-027-gesellschaft-societas`

**Fokus:** Römisches Recht: Societas (Gesellschaft) als Konsensualkontrakt nach D. 17.2 und Gaius Inst. 3.148-154 - societas omnium bonorum, quaestus, Haftung (diligentia quam in suis), actio pro socio.

# Gesellschaft (societas)

## Worum es geht

Die societas ist der Konsensualkontrakt zur Verfolgung eines gemeinsamen Zwecks durch Einlagenbeiträge. Gaius Inst. 3.148 nennt vier Untertypen: societas omnium bonorum (Gesamtgesellschaft), quaestus (Handelsgesellschaft), unius rei (Einzelgeschäft) und alicuius negotiationis (Branchengesellschaft). Haftungsmaßstab ist diligentia quam in suis rebus (D. 17.2.72, Celsus). Die societas endet mit Tod, Konkurs, Kündigung.

## Kernquellen

- **Gaius Inst. 3.148**: Vier Gesellschaftstypen
- **D. 17.2.1 pr. (Ulpian)**: Societas-Definition und Zweck
- **D. 17.2.63 (Paulus)**: Gemeinsame Haftung für Gesellschaftsverbindlichkeiten
- **D. 17.2.72 (Celsus)**: Haftungsmaßstab: diligentia quam in suis
- **D. 17.2.65 pr. (Paulus)**: Auflösungsgründe der societas
- **Iust. Inst. 3.25**: Societas systematisch

## Schlüsselbegriffe

- socii: Gesellschafter
- affectio societatis: Gesellschaftswille als Konstitutivum
- actio pro socio: Klage auf Rechnungslegung und Auseinandersetzung
- beneficium competentiae: Schutz vor Existenzvernichtung bei der actio
- societas omnium bonorum: Einbringung des gesamten Vermögens
- litis consortium: Gesamtschuldnerschaft der Gesellschafter

## Typische Streitfragen / Forschungsfragen

1. Juristische Person: Hatte die societas eigene Rechtspersönlichkeit?
2. Außenverhältnis: Haftung der socii gegenüber Dritten
3. Societas mit Gesellschafter ohne Einlage: rechtlich möglich (D. 17.2.29)?
4. Auflösung durch renuntiatio: formlos möglich?
5. Vergleich: röm. societas vs. GbR (§§ 705ff. BGB) und OHG

## Methodik

- D. 17.2 (Pro socio) als Haupttitel
- Gaius Inst. 3.148-154; Iust. Inst. 3.25
- Kaser RP I §§ 230-235; Zimmermann Law of Obligations Kap. 16

## Output

- Übersicht: vier Gesellschaftstypen nach Gaius
- Haftungsschema intern/extern
- Memo zur affectio societatis
- Vergleich röm. societas vs. GbR/OHG

## Quellenregel

D. 17.2 (Mommsen-Krüger). Gaius Inst. 3.148-154. Iust. Inst. 3.25. Kaser RP I. Zimmermann Law of Obligations.

## 5. `rom-028-buergschaft-und-sicherheiten`

**Fokus:** Römisches Recht: Bürgschaft und persönliche Sicherheiten - sponsio, fidepromissio, fideiussio nach Gaius Inst. 3.115-127, D. 46.1 (Ulpian) und SC Velleianum (Haftungsausschluss für Frauen).

# Bürgschaft und persönliche Sicherheiten

## Worum es geht

Das römische Recht kennt drei Bürgschaftsformen: sponsio (nur für Bürger, akzessorisch), fidepromissio (auch für Peregrine, Gaius Inst. 3.116) und fideiussio (klassische allgemeine Form, D. 46.1). Fideiussio ist akzessorisch und subsidiär; der Bürge kann beneficium excussionis (Einrede der Vorausklage) und beneficium divisionis geltend machen. SC Velleianum (46 n.Chr.) untersagt Frauen die Interzession.

## Kernquellen

- **Gaius Inst. 3.115**: Sponsio nur für Bürger
- **Gaius Inst. 3.116**: Fidepromissio auch für Peregrine
- **Gaius Inst. 3.119**: Fideiussio als allgemeine Bürgschaftsform
- **D. 46.1.1 pr. (Ulpian)**: Fideiussio - Definition und Akzessorietät
- **D. 16.1.2 pr. (Ulpian)**: SC Velleianum
- **D. 46.1.26 (Ulpian)**: Beneficium divisionis

## Schlüsselbegriffe

- sponsio: älteste Form (spondes?/spondeo - nur cives Romani)
- fidepromissio: für Peregrine, akzessorisch
- fideiussio: allgemeine klassische Bürgschaft
- beneficium excussionis: Einrede der Vorausklage (Justinian, Nov. 4)
- beneficium divisionis: Teilung der Bürgschaft unter Mitbürgen
- SC Velleianum (46 n.Chr.): Interzessionsverbot für Frauen

## Typische Streitfragen / Forschungsfragen

1. Akzessorietät der Bürgschaft: vollständig oder nur teilweise?
2. SC Velleianum: praxisnahe Anwendung und Ausnahmen
3. Verhältnis Bürge - Hauptschuldner: Rückgriffsrecht?
4. Einheitliche Haftung oder Gesamtschuldverhältnis?
5. Vergleich: röm. fideiussio vs. BGB §§ 765ff. (Bürgschaft)

## Methodik

- Gaius Inst. 3.115-127 für die drei Bürgschaftstypen
- D. 46.1 (De fideiussoribus) als Haupttitel
- D. 16.1 (SC Velleianum)
- Kaser RP I §§ 240-245; Zimmermann Law of Obligations Kap. 5

## Output

- Vergleichstabelle: sponsio, fidepromissio, fideiussio
- Haftungsschema mit beneficia
- Memo zum SC Velleianum
- Vergleich röm. Bürgschaft vs. BGB

## Quellenregel

Gaius Inst. 3.115-127; D. 46.1; D. 16.1 (Mommsen-Krüger). Kaser RP I. Zimmermann Law of Obligations.

## 6. `rom-029-realvertraege-system`

**Fokus:** Römisches Recht: Realkontrakte nach Gaius Inst. 3.90 - mutuum, commodatum, depositum, pignus als durch Hingabe der Sache (re) entstehende Verträge und ihre systematische Stellung im Obligationenrecht.

# Realverträge - System

## Worum es geht

Realkontrakte entstehen durch Hingabe einer Sache (re contrahitur obligatio). Gaius Inst. 3.90 nennt das mutuum als Prototyp; die justinianischen Institutionen (3.14) fügen commodatum, depositum und pignus hinzu. Das konstituierende Merkmal ist die tatsächliche Übergabe der Sache; ohne Hingabe entsteht keine obligatio. Diese Systematik ist rechtshistorisch bedeutsam für die BGB-fachliche Einordnung (§§ 488, 598, 688ff.).

## Kernquellen

- **Gaius Inst. 3.90**: re contrahitur obligatio (mutuum)
- **Iust. Inst. 3.14 pr.**: Vier Realkontrakte
- **D. 2.14.7.1 (Ulpian)**: Vertragsklassifikation allgemein
- **D. 44.7.1 (Gaius)**: Verbis, literis, re, consensu - Obligationsquellen
- **D. 12.1.1 (Ulpian)**: Condictio als Klage aus mutuum
- **D. 13.6.1 (Ulpian)**: Commodatum als Realkontrakt

## Schlüsselbegriffe

- re contrahitur: obligatio entsteht durch Hingabe
- mutuum: Darlehen (Übereignung vertretbarer Sachen)
- commodatum: Leihe (keine Übereignung)
- depositum: Verwahrung
- pignus: Pfandvertrag
- Systemvergleich: Realkontrakte vs. Konsensualkontrakte

## Typische Streitfragen / Forschungsfragen

1. Realkontrakt-Kategorie: dogmatisch sinnvoll oder historisches Relikt?
2. Abgrenzung mutuum - commodatum: Übereignung als Merkmal
3. Ohne Konsens kein mutuum: Bedeutung des Willens beim Realkontrakt
4. Innominatkontrakt als Weiterentwicklung des Realkontrakts (do ut des)
5. BGB § 604 (Commodatum) und historischer Vergleich

## Methodik

- Gaius Inst. 3.90-96; Iust. Inst. 3.14
- D. 44.7.1; D. 12.1 (Condictio)
- Kaser RP I §§ 217-230; Zimmermann Law of Obligations
- Flume Allgemeiner Teil Bd. 2 zum Vertragsrecht

## Output

- Systemtabelle: vier Realkontrakte im Vergleich
- Entstehungsvoraussetzungen tabellarisch
- Memo zur Realvertragstheorie und BGB
- Quellenmatrix D. 44.7.1

## Quellenregel

Gaius Inst. 3; Iust. Inst. 3.14; D. 44.7; D. 12.1 (Mommsen-Krüger). Kaser RP I. Zimmermann.

## 7. `rom-030-konsensualvertraege-system`

**Fokus:** Römisches Recht: Konsensualkontrakte (consensu contrahitur) nach Gaius Inst. 3.135 - emptio venditio, locatio conductio, mandatum, societas und die Bedeutung des bloßen Konsenses für die obligatio.

# Konsensualverträge - System

## Worum es geht

Konsensualkontrakte entstehen durch bloße Einigung (consensus) ohne Formakt oder Sachhingabe. Gaius Inst. 3.135 nennt vier: emptio venditio, locatio conductio, mandatum, societas. Der Konsens genügt auch bei räumlicher Trennung (durch Brief, Bote). Sie sind gegenseitige Verträge: beide Parteien tragen Klagen aus actiones bonae fidei. Dieses Modell ist Grundlage des modernen Vertragsrechts.

## Kernquellen

- **Gaius Inst. 3.135**: consensu contrahuntur obligationes - vier Typen
- **D. 2.14.7.1 (Ulpian)**: Vertragsbegriff und Einigung
- **D. 18.1.1 pr. (Paulus)**: Kauf als Konsensualkontrakt
- **D. 19.2.1 (Ulpian)**: Locatio conductio als Konsensualkontrakt
- **D. 17.1.1 pr. (Paulus)**: Mandatum als Konsensualkontrakt
- **D. 17.2.1 (Ulpian)**: Societas als Konsensualkontrakt

## Schlüsselbegriffe

- consensus: Einigung als alleinige Entstehungsvoraussetzung
- bonae fidei iudicia: Klagen aus Konsensualverträgen nach Treu und Glauben
- do ut des-Tausch: kein Konsensualkontrakt (Realkontrakt)
- synallagmatischer Vertrag: gegenseitige Leistungspflichten
- consensus per nuntium/epistulam: Einigung auf Distanz möglich
- iusta causa: Rechtsgrundelemente im Konsensualkontrakt

## Typische Streitfragen / Forschungsfragen

1. Vertragsbegriff: Reichte consensus allein oder brauchte es noch mehr?
2. Abgrenzung Konsensual- zu Innominatkontrakten
3. Formfreiheit des Konsenses: Auswirkung auf Schriftlichkeit
4. Synallagma: gegenseitige Abhängigkeit der Leistungspflichten
5. Einfluss auf BGB § 311 Abs. 1 (Vertragsfreiheit)

## Methodik

- Gaius Inst. 3.135-162; Iust. Inst. 3.22-26
- D. 2.14 (De pactis) als Ergänzung
- Kaser RP I §§ 195-215; Zimmermann Law of Obligations
- Flume AGB II zur Vertragstheorie

## Output

- Systemschaubild: Konsensualverträge mit Klagen
- Tabelle: Gemeinsamkeiten und Unterschiede der vier Typen
- Memo zur bonae fidei iudicia
- Vergleich röm. Konsensualvertrag vs. BGB

## Quellenregel

Gaius Inst. 3.135-162; Iust. Inst. 3.22-26; D. 2.14 (Mommsen-Krüger). Kaser RP I. Zimmermann. Flume.

## 8. `rom-031-innominatkontrakte`

**Fokus:** Römisches Recht: Innominatkontrakte (contractus innominati) nach D. 19.5 und D. 2.14 - Vier-Typen-Schema (do ut des etc.), actio praescriptis verbis und Abgrenzung zu Nominalkontrakten.

# Innominatkontrakte (contractus innominati)

## Worum es geht

Innominatkontrakte sind synallagmatische Verträge, die nicht zu den nominatae actiones (emptio, locatio etc.) gehören. Ihnen liegt das Schema zugrunde: do ut des (ich gebe, damit du gibst), do ut facias, facio ut des, facio ut facias. Schutzklage ist die actio praescriptis verbis (condictio causa data causa non secuta bei Vorleistung ohne Gegenleistung). D. 19.5 ist der zentrale Titel.

## Kernquellen

- **D. 19.5.1 (Labeo/Ulpian)**: Aktionen für Innominatkontrakte
- **D. 2.14.7.2 (Ulpian)**: Vier-Typen-Schema
- **D. 19.5.5 pr. (Paulus)**: Actio praescriptis verbis
- **D. 12.6.15.1 (Paulus)**: Condictio causa data causa non secuta
- **Iust. Inst. 3.14.2 i.V.m. 3.13.2**: Quasi ex contractu für Innominatkontrakte

## Schlüsselbegriffe

- contractus innominatus: Vertrag ohne eigenen Namen (Sonderform)
- do ut des: Austausch Sache gegen Sache
- do ut facias: Sache gegen Handlung
- facio ut des: Handlung gegen Sache
- facio ut facias: Handlung gegen Handlung
- actio praescriptis verbis: Klage mit vorausgeschickter Beschreibung

## Typische Streitfragen / Forschungsfragen

1. Innominatkontrakt: eigene Vertragskategorie oder Spezialfall von condictio?
2. Rückforderung nach Vorleistung: condictio ob causam datorum oder actio praescriptis verbis?
3. Verhältnis zu den Nominalkontrakten: ergänzend oder konkurrierend?
4. Permutatio (Tausch) als Innominatkontrakt (D. 19.4)
5. Einfluss auf BGB: atypische Verträge und § 311 BGB

## Methodik

- D. 19.5 (De praescriptis verbis et in factum actionibus) als Haupttitel
- D. 2.14 (De pactis)
- D. 19.4 (De rerum permutatione)
- Kaser RP I §§ 235-240; Zimmermann Law of Obligations Kap. 17

## Output

- Schema: vier Innominatkontrakt-Typen
- Klagenübersicht: actio praescriptis verbis vs. condictio
- Beispielsfälle aus D. 19.5
- Vergleich röm. Innominatkontrakt vs. atypischer BGB-Vertrag

## Quellenregel

D. 19.5; D. 19.4; D. 2.14 (Mommsen-Krüger). Gaius Inst. 3. Kaser RP I. Zimmermann.
