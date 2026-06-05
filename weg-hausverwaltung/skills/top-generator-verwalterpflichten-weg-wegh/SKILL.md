---
name: top-generator-verwalterpflichten-weg-wegh
description: "TOP Generator Verwalterpflichten WEG Wegh: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# TOP Generator Verwalterpflichten WEG Wegh

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **TOP Generator Verwalterpflichten WEG Wegh** im Plugin WEG / Hausverwaltung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `top-generator-emotion-zu-beschluss` | Verwandelt ungeordnete Beschwerden, WhatsApp-Nachrichten, Eigentuemermails und Verwaltervermerke in sachliche Tagesordnungspunkte, Beschlussvorschlaege, Informations-TOPs und Protokollbausteine. |
| `verwalterpflichten-26-27-weg` | Prüft Verwalterbestellung, Abberufung, Verwaltervertrag, Aufgaben und Befugnisse nach §§ 26 und 27 WEG (Stand 05/2026), laufende Verwaltung, Eilmaßnahmen, Vertretung der GdWE und Haftung; berücksichtigt BGH V ZR 34/24 (keine Schutzwirkung des Verwaltervertrags) und V ZR 167/23 (Abrechnungsanspruch gegen GdWE). |
| `wegh-bauliche-veraenderung-beschluss-spezial` | Spezialfall bauliche Veraenderung Beschluss WEG nach Reform: privilegierte Massnahmen, Kostenverteilung. Pruefraster fuer Verwalter und Eigentuemergemeinschaft. |

## Arbeitsweg

Im Plugin WEG / Hausverwaltung gilt für **TOP Generator Verwalterpflichten WEG Wegh**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `top-generator-emotion-zu-beschluss`

**Fokus:** Verwandelt ungeordnete Beschwerden, WhatsApp-Nachrichten, Eigentuemermails und Verwaltervermerke in sachliche Tagesordnungspunkte, Beschlussvorschlaege, Informations-TOPs und Protokollbausteine.

# TOP-Generator - von Emotion zu Beschluss

## Fachlicher Kern — Miet- und WEG-Recht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `TOP-Generator - von Emotion zu Beschluss` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 535 ff., 536, 543, 546a, 548, 556, 556a, 558 ff., 573 ff.; BetrKV; HeizkostenV; WEG §§ 18, 19, 20, 23, 24, 28, 44, 45; GEG; CO2KostAufG.
- **Verifizierte Anker:** BGH, Urteil vom 20.01.2016 - VIII ZR 93/15 (formelle Betriebskostenabrechnung); BGH, Urteil vom 15.12.2021 - VIII ZR 66/20 (Belegeinsicht Originale/Kopien); BGH, Urteil vom 14.02.2025 - V ZR 128/23 (§ 16 Abs. 2 Satz 2 WEG, Rücklagen/Kostenverteilung); BGH, Urteil vom 14.02.2025 - V ZR 86/24 (§ 20 WEG, bauliche Veränderung, Vorbefassung/Beschlussersetzung).
- **Arbeitsmodus:** Immer erst Verhältnis Miete/WEG/Gewerbe/Verwaltung trennen, dann Frist, Beschlusskompetenz, Umlagefähigkeit, Belege, Gebrauchsnachteil und Kostenfolge prüfen.
- **Outputpflicht:** Abrechnungsprüftabelle, Beschlussvorschlag, Anfechtungs-/Beschlussersetzungsskizze, Mietermail, Vermieterschreiben oder Verwalter-To-do-Liste.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Fachkern: TOP-Generator - von Emotion zu Beschluss
- **Spezialgegenstand:** TOP-Generator - von Emotion zu Beschluss wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** WEG §§ 18-28, 44/45, BGB-Miet-/Werkvertragsrecht, BetrKV, HeizkostenV, GEG, DSGVO und landesrechtliche Bau-/Sicherheitsfragen.
- **Entscheidende Weiche:** Trenne Beschlusskompetenz, ordnungsmäßige Verwaltung, Kostenverteilung, Anfechtungsfrist, Verwalterpflicht, Belegprüfung und Vollzug.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Zweck

Dieser Skill nimmt Material so, wie es in der Verwaltung wirklich ankommt: wuetende E-Mails, Fotos, Chatverlaeufe, halbe Kostenvoranschlaege und unklare Beschwerden. Daraus wird eine sachliche, beschlussfaehige Tagesordnung.

## Vier Pflichtbausteine

1. Ziel klaeren: Was soll entschieden, geprueft, entworfen, verbessert oder verhandelt werden?
2. Kontext sichern: Rolle, Frist, Dokumente, Beteiligte, Vorgeschichte und Belege.
3. Grenzen setzen: keine Blindzitate, keine erfundenen Tatsachen, keine ungewollten Zugestaendnisse.
4. Ausgabeformat bestimmen: Memo, Tabelle, Schriftsatz, Brief, Beschluss, TOP, Checkliste oder Red-Team-Liste.

## Workflow

1. Material erfassen und sichtbar zwischen Tatsache, Behauptung und Bewertung trennen.
2. Eilige Punkte vorziehen.
3. Schwachstellen und Gegenargumente benennen.
4. Passende Folge-Skills aus demselben Plugin vorschlagen.
5. Einen verwendbaren Output liefern und offene Punkte mit `[noch klaeren]` markieren.

## Ausgabe

| Punkt | Befund | Risiko | Naechster Schritt |
| --- | --- | --- | --- |
| ... | ... | ... | ... |

## Qualitaetsgate

Ist die Antwort handlungsorientiert, knapp, respektvoll, belegnah und ohne erfundene Quellen? Sind Fristen und offene Tatsachen sichtbar? Ist der naechste Schritt eindeutig?


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `verwalterpflichten-26-27-weg`

**Fokus:** Prüft Verwalterbestellung, Abberufung, Verwaltervertrag, Aufgaben und Befugnisse nach §§ 26 und 27 WEG (Stand 05/2026), laufende Verwaltung, Eilmaßnahmen, Vertretung der GdWE und Haftung; berücksichtigt BGH V ZR 34/24 (keine Schutzwirkung des Verwaltervertrags) und V ZR 167/23 (Abrechnungsanspruch gegen GdWE).

# Verwalterpflichten §§ 26, 27 WEG

## Fachlicher Kern — Miet- und WEG-Recht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Verwalterpflichten §§ 26, 27 WEG` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 535 ff., 536, 543, 546a, 548, 556, 556a, 558 ff., 573 ff.; BetrKV; HeizkostenV; WEG §§ 18, 19, 20, 23, 24, 28, 44, 45; GEG; CO2KostAufG.
- **Verifizierte Anker:** BGH, Urteil vom 20.01.2016 - VIII ZR 93/15 (formelle Betriebskostenabrechnung); BGH, Urteil vom 15.12.2021 - VIII ZR 66/20 (Belegeinsicht Originale/Kopien); BGH, Urteil vom 14.02.2025 - V ZR 128/23 (§ 16 Abs. 2 Satz 2 WEG, Rücklagen/Kostenverteilung); BGH, Urteil vom 14.02.2025 - V ZR 86/24 (§ 20 WEG, bauliche Veränderung, Vorbefassung/Beschlussersetzung).
- **Arbeitsmodus:** Immer erst Verhältnis Miete/WEG/Gewerbe/Verwaltung trennen, dann Frist, Beschlusskompetenz, Umlagefähigkeit, Belege, Gebrauchsnachteil und Kostenfolge prüfen.
- **Outputpflicht:** Abrechnungsprüftabelle, Beschlussvorschlag, Anfechtungs-/Beschlussersetzungsskizze, Mietermail, Vermieterschreiben oder Verwalter-To-do-Liste.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Fachkern: Verwalterpflichten §§ 26, 27 WEG
- **Spezialgegenstand:** Verwalterpflichten §§ 26, 27 WEG wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** WEG §§ 18-28, 44/45, BGB-Miet-/Werkvertragsrecht, BetrKV, HeizkostenV, GEG, DSGVO und landesrechtliche Bau-/Sicherheitsfragen.
- **Entscheidende Weiche:** Trenne Beschlusskompetenz, ordnungsmäßige Verwaltung, Kostenverteilung, Anfechtungsfrist, Verwalterpflicht, Belegprüfung und Vollzug.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


Stand: 05/2026.

## Ziel

Verwalterhandeln rechtssicher einordnen: Was darf der Verwalter allein, was braucht Beschluss, was muss sofort passieren — und wer haftet wem gegenüber?

## Prüfpunkte

- **Bestellung / Laufzeit / Abberufung** (§ 26 WEG): jederzeitige Abberufbarkeit; Bestellung höchstens 5 Jahre (3 Jahre nach erster Bestellung).
- **Aufgaben / Befugnisse** (§ 27 WEG):
 - Maßnahmen ordnungsmäßiger Verwaltung von untergeordneter Bedeutung (Bagatellen, keine erheblichen Folgen).
 - Maßnahmen zur Wahrung einer Frist oder zur Abwendung eines Nachteils (Eilmaßnahmen).
 - Vertretung der GdWE im Außenverhältnis (§ 9b WEG).
- **Informationspflichten**: Belege, Beschlusssammlung (§ 24 Abs. 7 WEG), Vermögensbericht (§ 28 Abs. 4 WEG), Jahresabrechnung.
- **Haftungsraster** seit WEMoG:
 - Verwaltervertrag entfaltet **keine** Schutzwirkung für einzelne Eigentümer — Ansprüche aus Pflichtverletzungen laufen über die GdWE: BGH, Urteil vom 05.07.2024, V ZR 34/24 (https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=05.07.2024&Aktenzeichen=V+ZR+34/24).
 - Anspruch auf Erstellung der Jahresabrechnung richtet sich gegen die GdWE, nicht persönlich gegen den Verwalter: BGH, Urteil vom 19.04.2024, V ZR 167/23 (https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=19.04.2024&Aktenzeichen=V+ZR+167/23).
 - Einzeleigentümer kann dennoch die GdWE auf Schadensersatz in Anspruch nehmen; die GdWE nimmt anschließend Regress beim Verwalter.

## Kompetenzmatrix (Beispiele, immer einzelfallabhängig)

| Maßnahme | Allein-Befugnis Verwalter | Beschluss erforderlich | Anmerkung |
| --- | --- | --- | --- |
| Routine-Instandhaltung (Glühbirne, kleine Reparatur) | ja | nein | Bagatell-Schwelle prüfen (TE, GO, Verwaltervertrag) |
| Erhaltungsmaßnahme mittlerer Größe | ggf. ja, wenn untergeordnete Bedeutung | bei substantieller Tragweite | Vergleichsangebote dokumentieren |
| Sanierungsbeschluss > Bagatell | nein | ja | Wirtschaftsplan / Sonderumlage |
| Eilmaßnahme zur Schadensabwehr (Wasserrohrbruch) | ja | nein | Sofortige Information GdWE/Beirat |
| Bauliche Veränderung § 20 WEG | nein | ja | Auflagen und Kostenfolge im Beschluss |
| Verwalter-Abberufung | nein | ja (jederzeit, § 26 Abs. 3 WEG) | Wirksamkeit Bestellung ≠ Vertragsbeendigung |
| Klage / Eilrechtsschutz | abhängig von Beschluss / Eilkompetenz | meist ja | Abstimmung mit Beirat / Anwalt |

## Eskalationsgründe

- Pflichtverletzung mit erheblichem Schaden (Versicherung, Heizung, Wasserschaden, Verzug Abrechnung).
- Interessenkonflikt (Eigengeschäft, Provision, verbundene Unternehmen) ohne Offenlegung.
- Wiederholt verspätete Jahresabrechnung / fehlender Vermögensbericht.
- Verweigerung der Belegeinsicht.
- Nichteinhaltung des CO2KostAufG (Datenbereitstellung) oder GEG-Pflichten (z. B. Heizungstausch-Beschlussvorlage).

## Output

- Kompetenzmatrix für den konkreten Vorgang
- Beschlussbedarfsliste
- Verwalter- bzw. Beiratsnotiz mit Risikoampel
- Abberufungs- und Neubestellungsfahrplan (Termine, Vergleichsangebote, Vertragsentwurf)
- Hinweis auf Schadensersatzweg über GdWE (V ZR 34/24)

## Cross-Refs

- Beschlussvorlage / Neubestellung → `beschlussvorlagen-erstellen`
- Beiratskontrolle → `beirat-controlling-verwalter`
- Jahresabrechnung / Vermögensbericht → `wirtschaftsplan-jahresabrechnung-28-weg`
- Eskalation Gericht → `eskalation-anwalt-amtsgericht`

## Quellenpflicht

`rechtsstand-mai-2026-faktenbank` laden. § 26, § 27 WEG: https://www.gesetze-im-internet.de/woeigg/__26.html, https://www.gesetze-im-internet.de/woeigg/__27.html .


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 3. `wegh-bauliche-veraenderung-beschluss-spezial`

**Fokus:** Spezialfall bauliche Veraenderung Beschluss WEG nach Reform: privilegierte Massnahmen, Kostenverteilung. Pruefraster fuer Verwalter und Eigentuemergemeinschaft.

# WEGh: Bauliche Veraenderung WEG

## Fachlicher Kern — Miet- und WEG-Recht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `WEGh: Bauliche Veraenderung WEG` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 535 ff., 536, 543, 546a, 548, 556, 556a, 558 ff., 573 ff.; BetrKV; HeizkostenV; WEG §§ 18, 19, 20, 23, 24, 28, 44, 45; GEG; CO2KostAufG.
- **Verifizierte Anker:** BGH, Urteil vom 20.01.2016 - VIII ZR 93/15 (formelle Betriebskostenabrechnung); BGH, Urteil vom 15.12.2021 - VIII ZR 66/20 (Belegeinsicht Originale/Kopien); BGH, Urteil vom 14.02.2025 - V ZR 128/23 (§ 16 Abs. 2 Satz 2 WEG, Rücklagen/Kostenverteilung); BGH, Urteil vom 14.02.2025 - V ZR 86/24 (§ 20 WEG, bauliche Veränderung, Vorbefassung/Beschlussersetzung).
- **Arbeitsmodus:** Immer erst Verhältnis Miete/WEG/Gewerbe/Verwaltung trennen, dann Frist, Beschlusskompetenz, Umlagefähigkeit, Belege, Gebrauchsnachteil und Kostenfolge prüfen.
- **Outputpflicht:** Abrechnungsprüftabelle, Beschlussvorschlag, Anfechtungs-/Beschlussersetzungsskizze, Mietermail, Vermieterschreiben oder Verwalter-To-do-Liste.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Fachkern: WEGh: Bauliche Veraenderung WEG
- **Spezialgegenstand:** WEGh: Bauliche Veraenderung WEG wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** WEG §§ 18-28, 44/45, BGB-Miet-/Werkvertragsrecht, BetrKV, HeizkostenV, GEG, DSGVO und landesrechtliche Bau-/Sicherheitsfragen.
- **Entscheidende Weiche:** Trenne Beschlusskompetenz, ordnungsmäßige Verwaltung, Kostenverteilung, Anfechtungsfrist, Verwalterpflicht, Belegprüfung und Vollzug.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Fallweichen
Frage zu Beginn nur ab, was fuer den naechsten Schritt unverzichtbar ist. Wenn Material vorliegt, mit dem Material arbeiten und nur eine gezielte Rueckfrage stellen.

1. **Rolle und Ziel:** Wer fragt, welche Rolle, welcher gewuenschte Output (Memo, Schriftsatz, Tabelle, Checkliste)?
2. **Sachverhalt:** Welche unstreitigen Tatsachen liegen vor, was ist streitig, was fehlt noch?
3. **Fristen:** Gibt es Termine, Fristen, eilbeduerftige Schritte?
4. **Unterlagen:** Welche Dokumente, Bescheide, Vertraege, Auszuege liegen vor?
5. **Format:** Wie ausfuehrlich, fuer wen, in welcher Tonalitaet?

## Pruefraster

Der Output muss als verwertbares Arbeitsprodukt aufgebaut sein:

1. **Sachverhalt fixieren** - streitige und unstreitige Tatsachen trennen, Lueckentafel.
2. **Rechtliche Einordnung** - einschlaegige Normen, Rechtsprechung BGH/BVerfG/EuGH, Literatur.
3. **Pruefung im Gutachtenstil** - Obersatz, Definition, Subsumtion, Zwischenergebnis.
4. **Handlungsempfehlung** - konkret, mit naechstem Schritt, verantwortlicher Person, Frist.

## Plugin-Kontext
Dieses Fachmodul arbeitet den konkreten Schwerpunkt aus, prüft Aktenlage, Normen, Fristen, Belege und Gegenargumente und erzeugt einen unmittelbar nutzbaren nächsten Schritt.

## Output-Module
- Strukturierter Pruefvermerk im Gutachtenstil mit klaren Ueberschriften.
- Tabellen und Checklisten, wo das die Lesbarkeit erhoeht.
- Anschreiben-, Antrags- oder Klageschriftsatz-Geruest, wenn die Aufgabe das verlangt.
- Quellenliste mit Gericht, Datum, Aktenzeichen, frei pruefbarem Link.

## Quellenregel
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei pruefbarem Link (`dejure.org`, `openjur.de`, `bundesgerichtshof.de`, `bundesverfassungsgericht.de`, `curia.europa.eu`).
- Keine Zitate aus `anwalt24.de`. Keine `BeckRS` als alleinige Fundstelle bei tragenden Aussagen.
- Aufsaetze mit Verfasser, Zeitschrift, Jahr, Heft (falls relevant) und Seite.
- Kommentare mit Bearbeiter und Randnummer.
- Annahmen explizit als solche kennzeichnen, keine Erfindungen.

## Was dieser Arbeitsgang nicht macht
- Kein Ersatz fuer eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.
