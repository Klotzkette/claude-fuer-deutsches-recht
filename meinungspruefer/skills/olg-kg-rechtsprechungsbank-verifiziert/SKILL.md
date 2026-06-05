---
name: olg-kg-rechtsprechungsbank-verifiziert
description: "OLG KG Rechtsprechungsbank Verifiziert: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# OLG KG Rechtsprechungsbank Verifiziert

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **OLG KG Rechtsprechungsbank Verifiziert** im Plugin Meinungsfreiheit/Persönlichkeitsrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `olg-kg-praxis-rechtsprechung` | Nutzt obergerichtliche Praxis zu Äußerungen: OLG Frankfurt, OLG München, OLG Köln, OLG Düsseldorf, KG Berlin, Social Media, Unterlassung und Sinnermittlung. |
| `rechtsprechungsbank-verifiziert` | Enthält eine verifizierte Rechtsprechungsbank zur Meinungsfreiheit und Ehrschutzprüfung mit Gericht, Datum, Aktenzeichen und freier Quelle. Keine BeckRS-, Kommentar- oder Aufsatz-Blindzitate. |

## Arbeitsweg

Im Plugin Meinungsfreiheit/Persönlichkeitsrecht gilt für **OLG KG Rechtsprechungsbank Verifiziert**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `olg-kg-praxis-rechtsprechung`

**Fokus:** Nutzt obergerichtliche Praxis zu Äußerungen: OLG Frankfurt, OLG München, OLG Köln, OLG Düsseldorf, KG Berlin, Social Media, Unterlassung und Sinnermittlung.

# OLG-/KG-Praxis zur Äußerungsprüfung

## Zweck

Dieser Skill macht aus Leitlinien der Verfassungsgerichte arbeitsfähige Instanzpraxis. Gerade in Eilverfahren, Unterlassung, Plattformfällen und Pressesachen entscheiden Details: Deutungsvarianten, Tenorweite, Verdachtsäußerung, tatsächliche Grundlage, Accountmaßnahme und Wiederholungsgefahr.

## Einsatz

- Unterlassungsantrag, Abmahnung, einstweilige Verfügung oder Gegendarstellung.
- Social-Media-Beitrag, Plattformlabel, De-Referenzierung, Kommentarspalte.
- Vorwurf innerer Tatsachen wie Absicht, Täuschung, Wissen oder "bewusst".
- Streit um Werturteil mit Tatsachenkern.
- OLG-Bezirk soll für Argumentation oder Vergleichsrisiko greifbar werden.

## Arbeitsprogramm

1. **Antrag/Tenor zuerst:** Was genau soll verboten werden? Ist die Deutungsvariante zu weit?
2. **Sinnermittlung:** Durchschnittsverständnis, Kontext, begleitende Indizien, Mehrdeutigkeit.
3. **Tatsachenkern:** Gibt es tatsächliche Anknüpfungspunkte oder nur Verdacht/Schluss?
4. **Äußerungsform:** Bericht, Gutachten, Post, Kommentar, Label, Suchtreffer, Gegendarstellung.
5. **Prozesslage:** Eilverfahren, Wiederholungsgefahr, Glaubhaftmachung, Dringlichkeit, Klarstellung.
6. **Risikoausgabe:** Was ist am wahrscheinlichsten: Verbot, Teilverbot, Abweisung, Klarstellung, Vergleich?

## Verifizierte Praxisanker

- **OLG Frankfurt am Main, Urteil vom 30.11.2023 - 16 U 206/21:** Gutachterliche Bewertung über einen Schiedsrichter; Werturteil, Sinnermittlung und Schutz fachlicher Kritik.
- **OLG München, Endurteil vom 23.05.2023 - 18 U 3399/22 Pre:** Werturteil kann unzulässig werden, wenn die tatsächliche Grundlage für schwerwiegende Schlussfolgerungen fehlt.
- **OLG München, Endurteil vom 05.03.2024 - 18 U 2827/23 Pre:** Verdachtsberichterstattung, wahre Tatsachen, Meinungsäußerung und identifizierende Berichterstattung sauber trennen.
- **OLG München, Endurteil vom 09.04.2024 - 18 U 4603/22 Pre:** Plattformlabel "Falschinformation" braucht tragfähige vertragliche Grundlage und darf Nutzerrechte nicht verfahrenslos verkürzen.
- **OLG Köln, Urteil vom 13.06.2024 - 15 U 70/23:** Bei inneren Tatsachen wie Motiv, Absicht oder Kenntnis genau zwischen beweisbarer Tatsache, Verdachtsäußerung und wertender Schlussfolgerung unterscheiden.
- **OLG Köln, Urteil vom 27.06.2024 - 15 U 221/22:** Persönlichkeitsrecht und Meinungsfreiheit im Einzelfall austarieren; EGMR-Werturteilslinie und deutsche Sinnermittlung zusammendenken.
- **OLG Düsseldorf, Beschluss vom 10.07.2006 - III-5 Ss 101/05 - 53/05 I:** Beleidigungsprüfung darf nicht aus dem Kontext gerissene Ausschnitte bewerten; Schmähkritik verlangt Gesamtwürdigung.
- **KG Berlin, Beschluss vom 11.03.2020 - 10 W 13/20:** Datenherausgabe wegen beleidigender Onlineäußerungen verlangt Prüfung, ob die Äußerung strafbar und die Herausgabe erforderlich ist.

## Output

```text
Obergerichtlicher Praxischeck
- Relevanter Bezirk/Instanz:
- Geeignete Praxisanker:
- Risiko für Antrag/Tenor:
- Schwachpunkt der Gegenseite:
- Vergleichsfenster:
- Formulierungsvorschlag für Schriftsatz:
```

## Quellenhygiene

Nur Entscheidungen verwenden, die im Skill `rechtsprechungsbank-verifiziert` oder durch freie amtliche Datenbanken nachprüfbar sind. Keine Verlagssignaturen und keine Kommentar-Fundstellen.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `rechtsprechungsbank-verifiziert`

**Fokus:** Enthält eine verifizierte Rechtsprechungsbank zur Meinungsfreiheit und Ehrschutzprüfung mit Gericht, Datum, Aktenzeichen und freier Quelle. Keine BeckRS-, Kommentar- oder Aufsatz-Blindzitate.

# Rechtsprechungsbank - verifiziert

## Quellenregel

Nutze diese Rechtsprechung als geprüfte Startbank. Zitiere sie nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und Link. Ergänze weitere Rechtsprechung nur nach Live-Verifikation über freie amtliche oder frei zugängliche Quellen.

## Leitentscheidungen

### BVerfG und deutsche Verfassungsleitlinien

| Thema | Entscheidung | Aussage für den | Freie Quelle |
|---|---|---|---|
| Normalabwägung und enge Ausnahmen | BVerfG, Beschluss vom 19.05.2020 - 1 BvR 362/18 | Auch grobe Kritik an Amtsträgern verlangt regelmäßig Abwägung; Schmähkritik, Formalbeleidigung und Menschenwürde sind eng zu begründen. | https://www.hrr-strafrecht.de/hrr/bverfg/18/1-bvr-362-18.php |
| Online-Pranger und Richterkritik | BVerfG, Beschluss vom 19.05.2020 - 1 BvR 2397/19 | Reichweite, Anprangerung und Integritätsangriffe können Ehrschutz deutlich stärken. | https://www.hrr-strafrecht.de/hrr/bverfg/19/1-bvr-2397-19.php |
| politische Machtkritik | BVerfG, Beschluss vom 19.05.2020 - 1 BvR 1094/19 | Bei Amtsträgern und Politikern ist Machtkritik besonders zu berücksichtigen; sie erlaubt aber nicht jede persönliche Beschimpfung. | https://www.hrr-strafrecht.de/hrr/bverfg/19/1-bvr-1094-19.php |
| kommunale Amtsträgerin | BVerfG, Beschluss vom 19.05.2020 - 1 BvR 2459/19 | Auch kommunale Amtskritik bleibt abwägungsgebunden; starker Ehrschutz kann bei schwachem Sachbezug überwiegen. | https://www.hrr-strafrecht.de/hrr/bverfg/19/1-bvr-2459-19.php |
| Persönlichkeitsrecht Betroffener | BVerfG, Beschluss vom 19.12.2021 - 1 BvR 1073/20 | Beleidigung setzt nicht Schmähkritik voraus; Gerichte müssen bei möglicher Beleidigung zugunsten Betroffener ebenfalls korrekt abwägen. | https://dejure.org/dienste/vernetzung/rechtsprechung?Aktenzeichen=1+BvR+1073%2F20&Datum=19.12.2021&Gericht=BVerfG |
| Kampf ums Recht | BVerfG, Beschluss vom 09.02.2022 - 1 BvR 2588/20 | In Beschwerden und Rechtsverteidigung dürfen auch starke Ausdrücke fallen; Reichweite und Anlass sind wichtig. | https://www.hrr-strafrecht.de/hrr/bverfg/20/1-bvr-2588-20.php |
| Korruptionsvorwurf im Protest | BVerfG, Beschluss vom 04.04.2024 - 1 BvR 820/24 | Bei öffentlicher Sachdebatte muss genau begründet werden, ob ein strafbarer Tatsachenvorwurf oder eine geschützte Wertung vorliegt. | https://www.hrr-strafrecht.de/hrr/bverfg/24/1-bvr-820-24.php |
| Systemkritik und Tatsachenabgrenzung | BVerfG, Beschluss vom 11.04.2024 - 1 BvR 2290/23 | Sinnermittlung ist Voraussetzung jeder rechtlichen Würdigung; Systemkritik darf nicht vorschnell als Tatsachenbehauptung verengt werden. | https://rewis.io/urteile/urteil/odx-11-04-2024-1-bvr-229023/ |
| Anwaltskritik und Mehrdeutigkeit | BVerfG, Beschluss vom 16.01.2025 - 1 BvR 1182/24 | Gerichte müssen den konkreten Aussagegehalt bestimmen, mehrdeutige Begriffe kontextgerecht verstehen und abwägen. | https://www.hrr-strafrecht.de/hrr/bverfg/24/1-bvr-1182-24.php |
| Schulkonflikt und Kontext | BVerfG, Beschluss vom 11.12.2025 - 1 BvR 986/25 | Auch harte Kritik im Schulkonflikt verlangt Sinnermittlung; Sachbezug verhindert vorschnelle Schmähkritik. | https://www.hrr-strafrecht.de/hrr/bverfg/25/1-bvr-986-25.php |

### EGMR zu Art. 10 EMRK

| Thema | Entscheidung | Aussage für den | Freie Quelle |
|---|---|---|---|
| demokratische Grundlinie | EGMR, Urteil vom 07.12.1976 - 5493/72, Handyside/Vereinigtes Königreich | Art. 10 schützt auch störende, schockierende und verletzende Äußerungen; Einschränkungen brauchen demokratische Notwendigkeit. | https://hudoc.echr.coe.int/eng?i=001-57499 |
| Politikerkritik und Werturteil | EGMR, Urteil vom 08.07.1986 - 9815/82, Lingens/Österreich | Politiker müssen weitergehende Kritik hinnehmen; Werturteile dürfen nicht wie Tatsachen bewiesen werden müssen. | https://hudoc.echr.coe.int/eng?i=001-57523 |
| grober politischer Spott | EGMR, Urteil vom 01.07.1997 - 20834/92, Oberschlick/Österreich Nr. 2 | Auch ein grober Einzelbegriff kann geschützt sein, wenn er als kontextgebundene politische Reaktion und Werturteil erscheint. | https://hudoc.echr.coe.int/eng?i=001-58044 |
| faktische Grundlage | EGMR, Urteil vom 27.02.2001 - 26958/95, Jerusalem/Österreich | Werturteile mit schwerem Vorwurf brauchen eine ausreichende Tatsachengrundlage. | https://hudoc.echr.coe.int/eng?i=001-59220 |
| Art.-8-/Art.-10-Kriterien | EGMR, Urteil vom 07.02.2012 - 39954/08, Axel Springer AG/Deutschland | Abwägung nach Beitrag zur öffentlichen Debatte, Bekanntheit, Vorverhalten, Inhalt, Form, Folgen und Sanktion. | https://hudoc.echr.coe.int/eng?i=001-109034 |
| anwaltliche Justizkritik | EGMR, Urteil vom 23.04.2015 - 29369/10, Morice/Frankreich | Anwaltliche Kritik an Justizakteuren kann geschützt sein, wenn sie auf Tatsachen beruht und öffentliche Fragen betrifft. | https://hudoc.echr.coe.int/eng?i=001-154265 |
| Hyperlinkhaftung | EGMR, Urteil vom 04.12.2018 - 11257/16, Magyar Jeti Zrt/Ungarn | Ein Link ist nicht automatisch Billigung des verlinkten Inhalts; Kontext, journalistische Sorgfalt und Kenntnis prüfen. | https://hudoc.echr.coe.int/eng?i=001-187930 |
| Drittkommentare | EGMR, Urteil vom 15.05.2023 - 45581/15, Sanchez/Frankreich | Verantwortlichkeit für Drittkommentare verlangt rollen-, kenntnis- und reaktionsbezogene Prüfung. | https://hudoc.echr.coe.int/eng?i=001-224928 |

### EuGH und Art. 11 GRCh

| Thema | Entscheidung | Aussage für den | Freie Quelle |
|---|---|---|---|
| Datenschutz und journalistische Zwecke | EuGH, Urteil vom 16.12.2008 - C-73/07, Satakunnan Markkinapörssi und Satamedia | Journalistische Zwecke sind funktional zu verstehen; Datenschutz und Informationsfreiheit müssen praktisch ausgeglichen werden. | https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:62007CJ0073 |
| Video und journalistische Zwecke | EuGH, Urteil vom 14.02.2019 - C-345/17, Buivids | Auch private Veröffentlichungen können journalistische Zwecke verfolgen; Veröffentlichung staatlicher Vorgänge braucht Datenschutzabwägung. | https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:62017CJ0345 |
| De-Referenzierung räumlich | EuGH, Urteil vom 24.09.2019 - C-507/17, Google/CNIL | Suchmaschinen-De-Referenzierung ist grundrechtlich und räumlich zu begrenzen; keine pauschale weltweite Löschung. | https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:62017CJ0507 |
| Plattform und gleichwertige Inhalte | EuGH, Urteil vom 03.10.2019 - C-18/18, Glawischnig-Piesczek/Facebook Ireland | Entfernung identischer und gleichwertiger rechtswidriger Inhalte kann angeordnet werden; allgemeine Überwachung bleibt Grenze. | https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:62018CJ0018 |
| Uploadfilter und Kommunikationsfreiheit | EuGH, Urteil vom 26.04.2022 - C-401/19, Polen/Parlament und Rat | Automatisierte Sperren brauchen wirksame Schutzvorkehrungen für rechtmäßige Kommunikation wie Zitat, Kritik und Parodie. | https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:62019CJ0401 |
| De-Referenzierung bei Unrichtigkeit | EuGH, Urteil vom 08.12.2022 - C-460/20, Google | Bei angeblich unrichtigen Suchtreffern zählen Nachweis offensichtlicher Unrichtigkeit und Grundrechtsbalance. | https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:62020CJ0460 |

### Obergerichte: OLG/KG-Praxis

| Thema | Entscheidung | Aussage für den | Freie Quelle |
|---|---|---|---|
| Kontext bei strafbarer Beleidigung | OLG Düsseldorf, Beschluss vom 10.07.2006 - III-5 Ss 101/05 - 53/05 I | Auszugsweise Wortlautwiedergabe reicht nicht; Beleidigungsprüfung braucht Einbettung und Abwägung. | https://nrwe.justiz.nrw.de/olgs/duesseldorf/j2006/III_5_Ss_101_05___53_05_Ibeschluss20060710.html |
| Gutachten und fachliche Kritik | OLG Frankfurt am Main, Urteil vom 30.11.2023 - 16 U 206/21 | Fachliche Bewertung und gutachterliche Kritik sind kontextbezogen zu prüfen; nicht jede rufschädigende Bewertung ist unzulässig. | https://ordentliche-gerichtsbarkeit.hessen.de/presse/ehemaliger-dfb-schiedsrichter-kann-nicht-unterlassen-gutachterlicher-aeusserungen-ueber-ihn |
| Verdachtsbericht oder Meinung | OLG München, Endurteil vom 05.03.2024 - 18 U 2827/23 Pre | Verdachtsberichterstattung gilt für ungeklärte Tatsachen; Rechtsauffassungen und Bewertungen unstreitig wahrer Tatsachen können Meinung sein. | https://www.gesetze-bayern.de/Content/Document/Y-300-Z-GRURRS-B-2024-N-4812 |
| Plattformlabel | OLG München, Endurteil vom 09.04.2024 - 18 U 4603/22 Pre | Falschinformationslabel auf Plattformen brauchen vertragliche Grundlage und dürfen Nutzerrechte nicht willkürlich verkürzen. | https://www.gesetze-bayern.de/Content/Document/Y-300-Z-GRURRS-B-2024-N-38301 |
| innere Tatsachen und Indizien | OLG Köln, Urteil vom 13.06.2024 - 15 U 70/23 | Kenntnis, Absicht und Motiv können beweisbare innere Tatsachen sein; Indizien, Indikativ und Verdachtskennzeichnung sind zentral. | https://nrwe.justiz.nrw.de/olgs/koeln/j2024/15_U_70_23_Urteil_20240613.html |
| scharfe Social-Media-Wertung | OLG Köln, Urteil vom 27.06.2024 - 15 U 221/22 | Wertung mit Tatsachenkern bleibt abwägungsfähig; unwahre oder nicht erweisliche Tatsachen können die Gesamtäußerung kippen. | https://nrwe.justiz.nrw.de/olgs/koeln/j2024/15_U_221_22_Urteil_20240627.html |
| Manipulationsvorwurf als Bewertung | OLG Köln, Urteil vom 20.02.2025 - 15 U 231/24 | Überschrift und Beitrag sind zusammen zu lesen; "Manipulation" kann je nach offengelegter Tatsachengrundlage Wertung sein. | https://nrwe.justiz.nrw.de/olgs/koeln/j2025/15_U_231_24_Urteil_20250220.html |

### USA-Vergleich: Supreme Court

| Thema | Entscheidung | Aussage für den | Freie Quelle |
|---|---|---|---|
| public official und actual malice | Supreme Court of the United States, 09.03.1964 - New York Times Co. v. Sullivan, 376 U.S. 254 | Amtsträger müssen bei defamation falsity und actual malice zeigen; nicht auf deutsche §§ 185 ff. StGB übertragbar. | https://cdn.loc.gov/service/ll/usrep/usrep376/usrep376254/usrep376254.pdf |
| private Kläger | Supreme Court of the United States, 25.06.1974 - Gertz v. Robert Welch, Inc., 418 U.S. 323 | Private plaintiffs genießen stärkeren Schutz; gleichwohl First-Amendment-Grenzen bei fault und damages. | https://cdn.loc.gov/service/ll/usrep/usrep418/usrep418323/usrep418323.pdf |
| Parodie und public figure | Supreme Court of the United States, 24.02.1988 - Hustler Magazine, Inc. v. Falwell, 485 U.S. 46 | Public-figure-Parodie ist stark geschützt, wenn keine vernünftig verstandene falsche Tatsachenbehauptung transportiert wird. | https://cdn.loc.gov/service/ll/usrep/usrep485/usrep485046/usrep485046.pdf |
| Meinung und beweisbare Tatsache | Supreme Court of the United States, 21.06.1990 - Milkovich v. Lorain Journal Co., 497 U.S. 1 | Das Label "opinion" schützt nicht automatisch, wenn die Äußerung eine beweisbar falsche Tatsachenbehauptung impliziert. | https://cdn.loc.gov/service/ll/usrep/usrep497/usrep497001/usrep497001.pdf |
| public concern | Supreme Court of the United States, 02.03.2011 - Snyder v. Phelps, 562 U.S. 443 | Rede zu public concern an öffentlichem Ort ist im US-Recht außerordentlich stark geschützt. | https://cdn.loc.gov/service/ll/usrep/usrep562/usrep562443/usrep562443.pdf |
| false speech | Supreme Court of the United States, 28.06.2012 - United States v. Alvarez, 567 U.S. 709 | Falsche Aussagen sind nicht allein wegen ihrer Falschheit kategorisch ungeschützt. | https://cdn.loc.gov/service/ll/usrep/usrep567/usrep567709/usrep567709.pdf |
| incitement | Supreme Court of the United States, 09.06.1969 - Brandenburg v. Ohio, 395 U.S. 444 | Incitement verlangt Ausrichtung auf und Wahrscheinlichkeit unmittelbar bevorstehender rechtswidriger Handlung. | https://cdn.loc.gov/service/ll/usrep/usrep395/usrep395444/usrep395444.pdf |
| true threats | Supreme Court of the United States, 27.06.2023 - Counterman v. Colorado, 600 U.S. 66 | True-threat-Strafbarkeit setzt mindestens recklessness hinsichtlich der bedrohlichen Bedeutung voraus. | https://www.supremecourt.gov/opinions/22pdf/22-138_43j7.pdf |

## Normquellen

- Art. 5 GG: https://www.gesetze-im-internet.de/gg/art_5.html
- StGB: https://www.gesetze-im-internet.de/stgb/BJNR001270871.html
- Art. 10 EMRK, EGMR-Guide: https://ks.echr.coe.int/documents/d/echr-ks/guide_art_10_eng-pdf
- Art. 11 GRCh: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:12016P011

## Anwendung

Nutze die Bank nicht als starre Ergebnisliste. Sie liefert Prüfmaßstäbe: Sinnermittlung, Meinung/Tatsache, enge Ausnahmen, Normalabwägung, Machtkritik, Kampf ums Recht, Reichweite, Prangerwirkung, europäische Verhältnismäßigkeit und rechtsvergleichende Einordnung.
