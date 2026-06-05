---
name: kommentar-literatur-konkurrenzen
description: "Kommentar Literatur Konkurrenzen: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Kommentar Literatur Konkurrenzen

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Kommentar Literatur Konkurrenzen** im Plugin Subsumtions-Prüfer. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `kommentar-und-literatur-hinweis` | Quellenhinweis für vertiefte Subsumtion. Gibt keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen aus. Markiert, welche Normen vertieft in Literatur oder Datenbanken zu prüfen sind, und fordert Nutzerquellen oder lizenzierten Live-Zugriff an. |
| `konkurrenzen-anspruchsgrundlagen` | Klaert Konkurrenzfragen zwischen Anspruchsgrundlagen: Anspruchskonkurrenz, Anspruchsgrundlagenkonkurrenz, Spezialitaet, Subsidiaritaet, lex specialis/posterior/superior. Klaert Verhältnis von Vertrags- zu Deliktsrecht, nationalem zu Unionsrecht, StGB zu OWiG. |
| `norm-historie-und-aenderungen` | Prüft die Norm-Historie: geltende Fassung zum massgeblichen Zeitpunkt, Übergangsvorschriften, intertemporales Recht, aenderungsrelevante Gesetzgebungsverfahren. Warnt bei Normen, die seit dem Wissensstand des Systems geaendert worden sein koennten. |

## Arbeitsweg

Im Plugin Subsumtions-Prüfer gilt für **Kommentar Literatur Konkurrenzen**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `kommentar-und-literatur-hinweis`

**Fokus:** Quellenhinweis für vertiefte Subsumtion. Gibt keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen aus. Markiert, welche Normen vertieft in Literatur oder Datenbanken zu prüfen sind, und fordert Nutzerquellen oder lizenzierten Live-Zugriff an.

# Quellenhinweis ohne Blindzitate

## Zweck

Dieser Skill ersetzt frühere Literatur-Empfehlungslisten. Er sagt nicht "zitiere Kommentar X Rn. Y", sondern baut eine saubere Recherche- und Prüfspur. Ziel ist Quellenhygiene: nur gesicherter Gesetzestext, verifizierte Rechtsprechung und vom Nutzer bereitgestellte Literatur fließen in das Arbeitsergebnis ein.

## Quellenklassen und Umgang

### Klasse 1 — Gesetzestext (frei prüfbar, höchste Verlässlichkeit)

- **Bundesrecht:** gesetze-im-internet.de (amtlich, tagesaktuell)
- **EU-Recht:** eur-lex.europa.eu (konsolidierte Fassungen)
- **Landesrecht:** jeweilige Landesrechtsdatenbanken (z. B. landesrecht.nrw.de)
- **Nutzung:** Norm direkt zitieren mit Fassungsstand; kein "nach h. M. gilt §..." ohne eigene Prüfung

### Klasse 2 — Verifizierte Rechtsprechung (frei prüfbar bei Aktenzeichen-Angabe)

- **BGH:** bgh.de, dejure.org, openjur.de
- **BVerfG:** bverfg.de
- **BAG, BVerwG, BSG, BFH:** jeweilige Behördenwebseiten; dejure.org als Querverweisquelle
- **EuGH/EuG:** curia.europa.eu
- **Nutzung:** Gericht + Entscheidungsform + Datum + Aktenzeichen + tragender Rechtssatz; immer als Prüfpunkt markieren, wenn nicht live verifiziert

### Klasse 3 — Nutzerbereitgestellte Literatur (erlaubt mit Kennzeichnung)

- Kommentare (Palandt/Grüneberg, MüKo, Staudinger, Schönke/Schröder etc.), die der Nutzer als Text einstellt
- Aufsätze, Handbücher, Gutachten aus lizenzierter Datenbank, wenn der Nutzer den Volltext bereitstellt
- **Nutzung:** Zitierung mit Fundstelle (Autor, Werk, Auflage, Rn.); als "aus Nutzerquelle" kennzeichnen; nicht als frei verifizierbarer Nachweis behandeln

### Klasse 4 — Modellwissen (verboten für Zitate)

- BeckRS-, juris-, NJW-, NZA-, NJW-RR-Blindzitate aus dem Modellwissen
- Randnummern, die nicht live geprüft wurden
- "nach allgemeiner Ansicht" oder "h. M." ohne konkrete Quelle

## Arbeitsweise

1. Nenne die entscheidenden Normen und Tatbestandsmerkmale.
2. Nenne, welche Punkte rechtsprechungs- oder literaturbedürftig sind.
3. Verlange konkrete Nutzerquellen oder lizenzierten Live-Zugriff, bevor Literatur zitiert wird.
4. Markiere unverifizierte Fundstellen als Prüfbedarf.

## Ausgabe-Tabelle

| Punkt | Prüfbedarf | Quelle |
|---|---|---|
| Norm/TBM | Welche dogmatische Frage ist offen? | Gesetz (gesetze-im-internet.de) oder verifizierte Rechtsprechung oder Nutzerquelle |

## Recherche-Strategie für offene Fragen

Wenn Nutzer keine Literatur bereithält und eine Frage literaturbedürftig ist:

1. **Gesetzestext zuerst:** Wortlaut, systematischer Kontext, Überschriften, Legaldefinitionen
2. **Rechtsprechungsrecherche:** dejure.org (Suchfeld Norm + Stichworte); bgh.de (Volltext); curia.europa.eu (EU-Fragen)
3. **Suchstrategie-Hinweis:** Konkrete Suchbegriffe benennen (z. B. "§ 280 BGB Pflichtverletzung Unterlassen Verkehrssicherung") für kostenpflichtige Datenbanken (beck-online, juris)
4. **Offene Frage markieren:** Was ist noch zu klären, bevor der Schriftsatz finalisiert wird?

## Schneller Arbeitsmodus

- Dieses Fachmodul als Quellenhygiene-Gate: keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
- Frage nach vorhandenen lizenzierten Quellen oder frei zugänglichen Materialien. Wenn keine vorliegen, liefere nur Normen, Rechtsprechungs-Recherchefragen und Suchstrategie.
- Trenne sauber zwischen gesichertem Gesetzestext, verifizierter Rechtsprechung, Nutzerquelle und offenem Literaturbedarf.

## Ausgabeformat

- Welche Literaturfrage ist offen?
- Welche Norm/Entscheidung muss zuerst geprüft werden?
- Welche Suchbegriffe und Datenbanken sind geeignet?
- Welche Aussage darf ohne Quelle noch nicht in den Schriftsatz?

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
- Normtext live prüfen: gesetze-im-internet.de (Bund), eur-lex.europa.eu (EU), dejure.org (Querverweise).

## 2. `konkurrenzen-anspruchsgrundlagen`

**Fokus:** Klaert Konkurrenzfragen zwischen Anspruchsgrundlagen: Anspruchskonkurrenz, Anspruchsgrundlagenkonkurrenz, Spezialitaet, Subsidiaritaet, lex specialis/posterior/superior. Klaert Verhältnis von Vertrags- zu Deliktsrecht, nationalem zu Unionsrecht, StGB zu OWiG.

# Konkurrenzen und Anspruchsgrundlagen

## Triage zu Beginn — kläre vor der Konkurrenzprüfung

1. Wie viele Normen kommen für denselben Sachverhalt in Betracht?
2. Regeln diese Normen dieselbe Rechtsfolge oder unterschiedliche?
3. Enthält eine Norm einen ausdrücklichen Ausschluss der anderen (Subsidiaritätsklausel)?
4. Stammen die Normen aus unterschiedlichen Rangstufen (Verfassung, Gesetz, VO)?
5. Stammt eine Norm aus dem Unionsrecht? → Anwendungsvorrang prüfen

## Zweck

Oft sind mehrere Normen auf einen Sachverhalt anwendbar. Dieser Skill klärt das Verhältnis mehrerer Anspruchsgrundlagen zueinander und gibt die empfohlene Prüfungsreihenfolge.

## Zentrale Normen und Prinzipien

- Art. 288 AEUV — Unmittelbare Geltung von EU-Verordnungen; Anwendungsvorrang vor nationalem Recht
- § 21 OWiG — Tateinheit von Straftat und OWiG-Tatbestand (Straftat geht vor)
- §§ 280 ff. BGB i.V.m. §§ 434 ff. BGB — Kaufgewährleistung als lex specialis zu allg. Schadensersatz
- § 823 Abs. 1 BGB — Echte Konkurrenz zu § 823 Abs. 2 BGB (jede Norm selbständig prüfen)
- §§ 812 ff. BGB — Subsidiarität des Bereicherungsrechts gegenüber vertraglichen Ansprüchen

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Grundbegriffe

### Anspruchskonkurrenz (echte Konkurrenz)

Mehrere Normen sind gleichzeitig anwendbar; jede begründet selbständig den Anspruch. Der Gläubiger kann alle geltend machen, aber nur einmal Befriedigung verlangen.

**Beispiel:** § 823 Abs. 1 BGB und § 823 Abs. 2 BGB i.V.m. § 229 StGB bestehen nebeneinander.

### Spezialität (lex specialis derogat legi generali)

Die speziellere Norm verdrängt die allgemeinere im Bereich der geregelten Materie.

**Entscheidungsbaum Spezialität:**
```
Regelt Norm A dasselbe wie Norm B, aber vollständiger?
├─ Ja → Norm A (lex specialis) geht vor → Norm B nicht anwenden
└─ Nein → beide Normen in Konkurrenz → beide prüfen
```

**Beispiele:**
- Kaufgewährleistung (§§ 434 ff. BGB) ist speziell zu allgemeinem Schadensersatzrecht im Äquivalenzbereich
- DSGVO verdrängt BDSG als lex specialis des Unionsrechts
- § 21 OWiG: Straftatbestand verdrängt OWiG-Tatbestand bei Tateinheit

### Subsidiarität (lex primaria)

Eine Norm gilt nur, wenn eine andere Norm nicht eingreift.

**Beispiele:**
- § 826 BGB — subsidiär, aber eigenständig bei sittenwidrigem Schädigungsvorsatz
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Lex posterior und lex superior

- **Lex posterior:** jüngere Norm gleicher Rangstufe verdrängt ältere
- **Lex superior:** höherrangige Norm verdrängt niederrangige (Verfassung > Gesetz > VO)
- Im Unionsrecht: Primärrecht > Sekundärrecht > nationales Recht (Anwendungsvorrang)

## Verhältnis Vertrags- zu Deliktsrecht

**Grundsatz:** Anspruchskonkurrenz — beide bestehen nebeneinander.

**Ausnahme Spezialität bei reinem Äquivalenzinteresse:** Wenn der Schaden nur im Wert der mangelhaften Sache selbst besteht und kein Weiterfresserschaden vorliegt, verdrängt Kaufgewährleistung den Deliktsanspruch.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Ausgabe

Das System erstellt eine Konkurrenz-Tabelle:
- Alle einschlägigen Normen
- Verhältnis zueinander (Konkurrenz / Spezialität / Subsidiarität)
- Empfohlene Prüfungsreihenfolge
- Hinweis auf verbleibende Kumulation oder Ausschluss

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## 3. `norm-historie-und-aenderungen`

**Fokus:** Prüft die Norm-Historie: geltende Fassung zum massgeblichen Zeitpunkt, Übergangsvorschriften, intertemporales Recht, aenderungsrelevante Gesetzgebungsverfahren. Warnt bei Normen, die seit dem Wissensstand des Systems geaendert worden sein koennten.

# Norm-Historie und Änderungen

## Triage zu Beginn — kläre vor der Norm-Historienprüfung

1. Wann hat das relevante Ereignis stattgefunden? (Vertragsschluss, Tatzeitpunkt, Bescheiderlass)
2. Ist die Norm seit dem Ereignis geändert worden oder könnte sie geändert worden sein?
3. Enthält der Sachverhalt eine strafrechtliche Komponente? → § 2 StGB (lex mitior) prüfen
4. Hat der Sachverhalt EU-Bezug? → Anwendungsbeginn und Übergangszeitraum der EU-Verordnung prüfen
5. Gibt es Übergangsvorschriften, die alte Rechtslage für Altfälle erhalten?

## Zweck

Subsumtion setzt voraus, dass die richtige Normfassung angewendet wird. Für zurückliegende Sachverhalte gilt das Recht zum Zeitpunkt des relevanten Ereignisses (Tatzeit, Vertragsschluss, Bescheiderlass).

## Zentrale Normen zum intertemporalen Recht

- § 2 StGB — lex mitior: Mildestes Gesetz zwischen Tat und Urteil gilt
- Art. 103 Abs. 2 GG — Rückwirkungsverbot im Strafrecht (nulla poena sine lege)
- Art. 20 Abs. 3 GG — Rechtsstaatsprinzip: Vertrauensschutz gegen echte Rückwirkung
- Art. 49 GRCh — Rückwirkungsverbot auf Unionsebene
- Art. 99 KI-VO — gestaffeltes Inkrafttreten (August 2024 - August 2027)

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Prüfungsschritte

### Schritt 1 — Maßgeblicher Zeitpunkt

Das System fragt: Wann hat das relevante Ereignis stattgefunden?

- **Vertragsrecht:** Datum des Vertragsschlusses
- **Deliktsrecht:** Datum der schädigenden Handlung
- **Strafrecht:** Tatzeitpunkt (§ 2 StGB: mildestes Gesetz von Tatzeit bis Urteil — lex mitior)
- **Verwaltungsrecht:** Datum des Bescheiderlasses oder der Widerspruchsentscheidung
- **Steuerrecht:** Veranlagungszeitraum

### Schritt 2 — Normfassung ermitteln

**Entscheidungsbaum:**
```
Liegt das Ereignis vor einer bekannten Normänderung?
├─ Ja → alte Normfassung anwenden (intertemporales Recht)
│ → Übergangsvorschriften prüfen
└─ Nein → aktuelle Normfassung anwenden
 → gesetze-im-internet.de verifizieren
```

Bekannte wichtige Zäsuren:
- Schuldrechtsmodernisierungsgesetz 01.01.2002 (BGB-Schuldrecht)
- DSGVO-Geltungsbeginn 25.05.2018 (Datenschutz)
- KI-VO Inkrafttreten 01.08.2024; Anwendung gestaffelt bis 2027
- Telekommunikationsmodernisierungsgesetz 12.2021 (TKG)

### Schritt 3 — Übergangsvorschriften

- Stichtagsregelungen: Anwendung neuen Rechts ab einem bestimmten Datum
- Bestandsschutzklauseln: Altverträge bleiben unter altem Recht
- Rückwirkungsverbote (Art. 103 Abs. 2 GG im Strafrecht; Art. 20 Abs. 3 GG im Verwaltungsrecht)
- EU-Übergangsrecht: Geltungsbeginn von Verordnungen nach Übergangsfrist

### Schritt 4 — Intertemporales Recht

Das System unterscheidet:
- **Echte Rückwirkung** (belastend): verfassungsrechtlich grundsätzlich verboten
- **Unechte Rückwirkung** (auf laufende Sachverhalte): grundsätzlich zulässig, aber verhältnismäßig
- **Lex mitior im Strafrecht** (§ 2 Abs. 3 StGB): Bei Gesetzesänderung zwischen Tat und Urteil gilt das mildere Gesetz

### Schritt 5 — Hinweis auf Wissensgrenze

Das System gibt in jedem Fall den Hinweis: "Diese Angaben zur Normfassung entsprechen dem Wissensstand des Systems. Für Änderungen danach ist gesetze-im-internet.de oder eur-lex.europa.eu zu prüfen."

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Ausgabe

- Maßgeblicher Zeitpunkt (Nutzerangabe)
- Bekannte Normfassung zu diesem Zeitpunkt
- Wesentliche Änderungen (soweit systembekannt)
- Übergangsvorschriften (soweit einschlägig)
- Empfehlung zur Verifikation der geltenden Fassung

---

Hinweis: Keine Rechtsberatung. Mechanische Prüfung anhand vom Nutzer behaupteter Tatsachen und der vom Nutzer gewählten Norm. Falsche Normwahl oder falsche Sachverhaltsdarstellung kann das gesamte Ergebnis entwerten.

<!-- AUDIT 27.05.2026 bundle_044
 → Falsche Rechtsprechungszeile entfernt
 → kein gesicherter Ersatz für lex-temporis-actus-Aussage gefunden; Grundsatz weiterhin durch BVerfG Art. 20 Abs. 3 GG / lizenzpflichtige Literaturquelle BGB Einl. gedeckt
-->
