---
name: allgemein
description: "Einstieg, Schnelltriage und Workflow-Routing im Insolvenzrecht-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext startet der Skill von selbst: klassifiziert die Aktenart, routet in den passenden Spezial-Skill oder stellt eine gezielte Rueckfrage statt einer generischen Antwort."
---

# Insolvenzrecht — Allgemein

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Insolvenzrecht**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Spezial-Skills aus diesem Plugin vorschlagen.

**Plugin-Fokus:** Insolvenzrechtliche Skills zu Zahlungsunfähigkeit, Überschuldung, Antragspflicht und Gläubigerantrag.

### 0. Stummer Upload — Dokument ohne Begleittext

Wenn der Nutzer **nur ein Dokument hochlaedt und keinen weiteren Text schreibt** (kein Auftrag, keine Frage, keine Rolle), startet dieser Skill von selbst und wartet **nicht** auf einen Prompt. Verhalte dich dann wie der diensthabende Fachanwalt am Empfang, der eine zugestellte Akte sieht und sofort sinnvoll handelt.

**Pflicht-Reihenfolge bei stummem Upload:**

1. **Dokument-Klassifikation** in einem Satz: Welche Aktenart liegt vor? (Bescheid, Klageschrift, Vertrag, Mandantenmail, Gerichtsentscheidung, Schriftsatz der Gegenseite, Akten-Konvolut, Tabelle, Foto/Screenshot, Anhoerungsbogen, Mahnbescheid, Rechnung, AU-Bescheinigung, KBA-Auszug, Registerauszug, ...). Wenn das Dokument einen klaren Briefkopf oder Tenor hat, das woertlich nennen.
2. **Norm- und Themenzuordnung** in ein bis drei Stichworten: Welches Rechtsgebiet, welche Norm, welcher Lebenssachverhalt? (z. B. "Gebuehrenbescheid BVG — § 23 MobG BE — Umsetzung aus Bushaltestelle".)
3. **Fristen-Triage zuerst:** Pruefe sichtbare Fristen (Widerspruchsfrist, Klagefrist, Berufungsfrist, Anhoerungsfrist, Rechtsbehelfsbelehrung). Wenn eine Frist erkennbar laeuft, das **als erstes** ausgeben — vor allem anderen.
4. **Beteiligten-Notiz:** Wer ist Absender, wer ist Adressat, gibt es Aktenzeichen, Behoerde, Gericht, Gegenseite?
5. **Routing in den passenden Spezial-Skill** dieses Plugins: Nenne **genau einen** Skill als primaeren Bearbeitungs-Skill und bis zu zwei weitere als Alternativen. Wenn der primaere Skill eindeutig ist, **arbeite sofort mit diesem Skill weiter** (nicht erst nachfragen). Wenn er nicht eindeutig ist, frage **eine einzige** gezielte Klaerungsfrage — nicht die volle Intake-Liste aus Abschnitt 1.
6. **Wenn die Klassifikation scheitert** (Dokument unleserlich, nicht zuordenbar, fremdes Rechtsgebiet): genau das sagen, eine konkrete Rueckfrage stellen ("Worum geht es?" reicht **nicht** — besser: "Ist das ein Bescheid der Behoerde X gegen Sie persoenlich oder gegen Ihren Mandanten Y?").

**Was du bei stummem Upload nicht machst:**

- Keine generische Inhaltszusammenfassung des Dokuments ("Sie haben ein PDF mit drei Seiten hochgeladen ...").
- Keine vollstaendige Intake-Abfrage aus Abschnitt 1 (Rolle, Ziel, Format ...). Diese Fragen kommen nur, wenn das Routing nicht eindeutig ist.
- Kein Warten auf einen Prompt. Der Upload **ist** der Prompt.

**Antwortformat bei stummem Upload:**

**Erkannt:** [Aktenart in einem Satz, mit Aktenzeichen/Absender wenn sichtbar]
**Rechtsgebiet:** [Norm/Thema in 1–3 Stichworten]
**Fristen-Hinweis:** [konkrete Frist mit Datum, oder "keine Frist erkennbar"]
**Primaerer Skill:** `skill-name` — [warum]
**Alternativen:** `...`, `...`
**Naechster Schritt:** [entweder direkter Arbeitsschritt ODER **eine** gezielte Rueckfrage]

### 1. Intake in 60 Sekunden

Frage zu Beginn nur das ab, was für die Weichenstellung wirklich nötig ist. Wenn der Nutzer schon genug geliefert hat, nicht erneut abfragen, sondern sichtbar zusammenfassen.

| Punkt | Frage | Warum wichtig? |
|---|---|---|
| Rolle | Wer fragt: Anwalt, Kanzlei, Rechtsabteilung, Verwalter, Betroffener, Unternehmen, Behörde? | Perspektive und Ton bestimmen. |
| Ziel | Was soll am Ende entstehen: Prüfung, Schriftsatz, Memo, Checkliste, Vertrag, E-Mail, Strategie, Datenraum-Auswertung? | Output sofort sauber ausrichten. |
| Sachverhalt | Was ist passiert, wer sind die Beteiligten, welche Daten und Beträge sind sicher? | Keine Arbeit auf Luft bauen. |
| Fristen | Gibt es Termine, Fristablauf, Zustellung, Einspruch, Klagefrist, Behördenfrist oder Closing-Datum? | Eilsachen zuerst sichern. |
| Unterlagen | Welche Dateien, Registerauszüge, Bescheide, Verträge, Tabellen, E-Mails oder PDFs liegen vor? | Aktenarbeit statt Raten. |
| Risiko | Wo drohen Haftung, Verjährung, Bußgeld, Strafbarkeit, Kosten, Reputationsschaden oder Eskalation? | Priorität und Vorsicht einstellen. |
| Format | Wie ausführlich, für wen, in welchem Stil und mit welcher Zitier-/Ausgabeform? | Ergebnis direkt verwendbar machen. |

### 2. Sofort-Triage

Arbeite danach in dieser Reihenfolge:

1. **Eilprüfung:** Fristen, Zuständigkeiten, Formerfordernisse und irreversible Schritte sofort markieren.
2. **Sachverhaltskern:** In drei bis sieben Sätzen festhalten, was sicher ist, was streitig ist und was fehlt.
3. **Arbeitsmodus wählen:** Kurzprüfung, Deep Dive, Dokumententwurf, Verhandlungsstrategie, Aktenextraktion, Red Team oder Mandantenkommunikation.
4. **Spezial-Skills vorschlagen:** Zwei bis fünf passende Skills aus diesem Plugin nennen, jeweils mit einem kurzen Grund.
5. **Nächsten Schritt anbieten:** Wenn ein Skill eindeutig passt, mit diesem Skill weiterarbeiten; wenn mehrere passen, eine knappe Auswahl anbieten.
6. **Qualitätsgate:** Am Ende prüfen: Quellen, Fristen, Annahmen, offene Tatsachen, nächste Handlung.

### 3. Routing-Regeln

- Schlage **immer zuerst Skills aus diesem Plugin** vor. Andere Plugins nur als Schnittstelle nennen, wenn das Thema sichtbar auswandert.
- Nenne nie nur einen Skillnamen. Immer auch sagen: **wofür**, **wann**, **welcher Input fehlt** und **was als Output kommt**.
- Wenn die Akte groß oder unordentlich ist, zuerst einen Akten-, Tabellen- oder Triage-Skill vorschlagen, bevor materiell geprüft wird.
- Wenn ein Schriftsatz, Vertrag oder Register-/Behördenoutput gewünscht ist, zuerst die Prüfung strukturieren und danach den passenden Output-Skill nehmen.
- Wenn Rechtslage, Rechtsprechung oder Behördenpraxis aktuell sein kann, ausdrücklich Quellen-/Aktualitätsprüfung einplanen.
- Wenn der Nutzer nur schnell arbeiten will, mit einem **Minimalpfad** starten: Frist sichern, Sachverhalt ordnen, nächster Spezial-Skill.

### 4. Antwortformat für den Einstieg

Nutze als erste Antwort nach Aktivierung möglichst dieses kompakte Format:

**Kurzbild**
- Ziel: [...]
- Rolle/Perspektive: [...]
- Eilt wegen: [...]
- Fehlende Unterlagen: [...]

**Vorgeschlagener Workflow**
1. [...]
2. [...]
3. [...]

**Passende Skills aus diesem Plugin**
| Skill | Warum jetzt? | Erwarteter Output |
|---|---|---|
| `...` | [...] | [...] |

**Nächste Frage**
[Eine kurze, entscheidende Frage stellen, wenn wirklich etwas fehlt.]

### 5. Spezial-Skills in diesem Plugin

| Skill | Wann vorschlagen? |
|---|---|
| `anfechtungsrechte-pruefen` | Insolvenzverwalter klagt auf Rückgewaehr einer Zahlung vor Insolvenz oder Gläubiger muss Insolvenzanfechtung abwehren. Prüfraster §§ 129 ff. InsO kongruente Deckung § 130 inkongruente Deckung § 131 vorsaetzliche… |
| `antragspflicht-15a-inso` | Analysiert die Insolvenzantragspflicht des Geschäftsleiters nach § 15a InsO, die Haftung wegen Insolvenzverschleppung (§ 823 Abs. 2 BGB iVm § 15a InsO) sowie das Zahlungsverbot nach § 15b InsO. Lädt, wenn Schlagwörter… |
| `do-versicherung-manager-haftung` | Insolvenzverwalter verklagt Geschäftsführer und D&O-Versicherung soll Deckung prüfen oder Manager fragt nach Versicherungsschutz in der Krise. Prüfraster D&O-Versicherung Claims-made-Prinzip Schadensereignis vs.… |
| `forderungsanmeldung-glaeubiger-174-177-inso` | Gläubiger meldet Forderung im Insolvenzverfahren an §§ 174-177 InsO: Fristen Form Anlagen Rang § 39 InsO Vorsatz § 174 Abs. 2 InsO nachtraegliche Anmeldung § 177 InsO Prüfungstermin § 176 Bestreiten § 178 Tabelle § 179… |
| `glaeubigerantrag-pruefung` | Prüft Zulässigkeit und Begründetheit eines Gläubigerantrags auf Eröffnung des Insolvenzverfahrens nach § 14 InsO — sowohl aus Gläubigerperspektive (Antragstellung) als auch aus Schuldnerperspektive (Abwehrstrategien).… |
| `glaeubigerausschuss-mitwirkung` | Mandant ist Mitglied des Gläubiger-ausschusses oder soll in den Ausschuss gewählt werden und fragt nach Rechten Pflichten und Haftung. Prüfraster §§ 67 ff. InsO Gläubigerausschuss vorlaeufiger Gläubigerausschuss § 22a… |
| `insolvenzgeld-165-sgb-iii` | Arbeitnehmer eines insolventen Unternehmens will Insolvenzgeld beantragen oder Insolvenzverwalter bearbeitet Insolvenzgeld-Anmeldungen. Prüfraster § 165 ff. SGB III Anspruchs-Voraussetzungen Arbeitsentgelt letzte drei… |
| `insolvenzrecht-kaltstart-interview` | Kaltstart-Interview für das Insolvenzrecht-Plugin. Befüllt das Praxisprofil unter ~/.claude/plugins/config/claude-fuer-deutsches-recht/insolvenzrecht/CLAUDE.md mit Angaben zur Rolle (Insolvenzverwalter / Sachwalter /… |
| `konzerninsolvenz-koordination` | Mehrere Gesellschaften eines Konzerns sind insolvent und Koordination der Verfahren muss geplant werden. Prüfraster Konzerninsolvenz §§ 269a-269i InsO Konzern-Gerichtsstand § 3a InsO Gruppen-Folgeverfahren § 3d InsO.… |
| `liquiditaetsvorschau-insolvenzrechtlich` | Erstellt und bewertet die rollierende Liquiditätsvorschau als strukturierte Arbeitsgrundlage für insolvenzrechtliche Tatbestände nach § 17 InsO (Zahlungsunfähigkeit) und § 19 Abs. 2 InsO (Fortbestehensprognose). Lädt,… |
| `mandat-triage-insolvenzrecht` | Eingangs-Abfrage für insolvenzrechtliche Mandate — Mandant ist Geschäftsführer mit Antragspflicht Gläubiger der Forderung anmelden will oder Arbeitnehmer der Insolvenzgeld beantragt. Klaert Mandantenrolle und Vorgang… |
| `ueberschuldung-pruefung-19-inso` | Führt die zweistufige Überschuldungsprüfung gem. § 19 Abs. 2 InsO durch: Fortbestehensprognose (Stufe 1) und insolvenzrechtlicher Überschuldungsstatus auf Liquidationswertbasis (Stufe 2). Lädt, wenn Überschuldung… |
| `uebertragende-sanierung-und-asset-deals` | Insolvenzverwalter will Geschäftsbetrieb verkaufen oder Investor kauft aus der Insolvenz und braucht Prüfung des Asset-Deals. Prüfraster uebertragende Sanierung Asset Deal im Regelverfahren Zustimmung… |
| `vorsatzanfechtung-133-inso` | Insolvenzverwalter will Zahlungen nach § 133 InsO anfechten oder Gläubiger muss Vorsatzanfechtung abwehren. Prüfraster vorsaetzliche Gläubiger-Benachteiligung Kenntnis Gläubiger des Benachteiligungsvorsatzes. BGH-Linie… |
| `zahlungsunfaehigkeit-pruefung-17-inso` | Erstellt ein strukturiertes Prüfgutachten zum Eröffnungsgrund der Zahlungsunfähigkeit nach § 17 InsO. Berechnet den Liquiditätsstatus zum Stichtag, wendet das 10-%-/3-Wochen-Schema des BGH an und würdigt Indizien der… |

## Worum geht es?

Dieses Plugin deckt die insolvenzrechtlichen Grundfragen ab, die in der taeaglichen Beratungspraxis vor und waehrend eines Insolvenzverfahrens entstehen. Im Mittelpunkt stehen die Eroeffnungsgruende (Zahlungsunfaehigkeit, drohende Zahlungsunfaehigkeit, Ueberschuldung), die Insolvenzantragspflicht des Geschaeftsleiters nach § 15a InsO, das Zahlungsverbot nach § 15b InsO, Anfechtungsrechte des Insolvenzverwalters, Forderungsanmeldung durch Glaeubiger, D-and-O-Haftungsfragen und die Koordination von Konzerninsolvenzen.

Das Plugin richtet sich an Anwaelte, Insolvenzverwalter, Sachwalter, Sanierungsberater und Unternehmensberater. Es ist ein strukturiertes Pruefwerkzeug fuer insolvenzrechtliche Triage-Situationen. Fuer vertiefte Planwerkstatt-Arbeit (Insolvenzplan, StaRUG) steht das Plugin `insolvenzplan-starug-planwerkstatt` zur Verfuegung.

## Wann brauchen Sie diese Skill?

- Geschaeftsfuehrer fragt, ob er einen Insolvenzantrag stellen muss und bis wann die Dreiwochenfrist laeuft.
- Glaeubiger moechte wissen, ob er einen Insolvenzantrag stellen kann und was dabei zu beachten ist.
- Arbeitnehmer eines insolventen Unternehmens fragt nach Insolvenzgeld.
- Insolvenzverwalter prueft Anfechtungsansprueche gegen Zahlungen vor Verfahrenseroffnung.
- Mandant ist Mitglied des Glaeubigerausschusses und fragt nach Rechten, Pflichten und Haftung.

## Fachbegriffe (kurz erklaert)

- **Zahlungsunfaehigkeit** — Schuldner kann faellige Zahlungspflichten nicht mehr erfuellen; § 17 InsO; BGH-Schema: zehn Prozent Liquiditaetslucke fuer mindestens drei Wochen.
- **Drohende Zahlungsunfaehigkeit** — Schuldner wird voraussichtlich faellige Zahlungspflichten nicht erfuellen koennen; § 18 InsO; Grundlage fuer freiwilligen Antrag und StaRUG.
- **Ueberschuldung** — Vermoegen des Schuldners deckt bestehende Verbindlichkeiten nicht, sofern keine positive Fortbestehensprognose (§ 19 InsO).
- **Antragspflicht** — Geschaeftsfuehrer und Vorstand muessen bei Zahlungsunfaehigkeit oder Ueberschuldung ohne schuldhaftes Zoegern, spaetestens drei Wochen nach Eintreten, Antrag stellen (§ 15a InsO).
- **Zahlungsverbot** — Nach Insolvenzreife sind Zahlungen nur noch zulasaig, die mit der Sorgfalt eines ordentlichen Kaufmanns vereinbar sind (§ 15b InsO).
- **Insolvenzverschleppung** — Verspaetete Antragstellung; Haftung gegenueber Neuglaeubigeern und Altglaeubigern aus § 823 Abs. 2 BGB iVm § 15a InsO.
- **Bargeschaeft** — Leistungsaustausch mit sofortiger Gegenleistung; schuetzt vor Insolvenzanfechtung nach § 142 InsO.
- **Glaeubigerausschuss** — Kontrollorgan des Insolvenzverfahrens nach §§ 67 ff. InsO; prueft und beaufsichtigt den Insolvenzverwalter.

## Rechtsgrundlagen

- § 17 InsO — Zahlungsunfaehigkeit als Eroeffnungsgrund.
- § 18 InsO — Drohende Zahlungsunfaehigkeit.
- § 19 InsO — Ueberschuldung; zweistufige Pruefung.
- § 14 InsO — Glaeubigerantrag.
- § 15a InsO — Antragspflicht des Geschaeftsleiters; Dreiwochenfrist.
- § 15b InsO — Zahlungsverbot nach Insolvenzreife.
- §§ 67 ff. InsO — Glaeubigerausschuss.
- §§ 129 ff. InsO — Insolvenzanfechtung (Grundtatbestand, Deckungsanfechtung, Vorsatzanfechtung).
- § 142 InsO — Bargeschaeftsprivileg.
- §§ 165 ff. SGB III — Insolvenzgeld fuer Arbeitnehmer.
- §§ 174 bis 179 InsO — Forderungsanmeldung, Pruefungstermin, Tabelle.
- §§ 269a bis 269i InsO — Konzerninsolvenz.

## Schritt-fuer-Schritt: Einstieg ins Plugin

1. Mandantenrolle klaeren: Geschaeftsfuehrer, Glaeubiger, Arbeitnehmer, Ausschussmitglied?
2. Triage-Interview durchfuehren: Skill `mandat-triage-insolvenzrecht`.
3. Sofort-Fristen sichern: Dreiwochenfrist § 15a InsO oder Anmeldefrist § 165 SGB III?
4. Eroeffnungsgruende pruefen: `zahlungsunfaehigkeit-pruefung-17-inso` und/oder `ueberschuldung-pruefung-19-inso`.
5. Anschluss-Skill auswaehlen nach Ergebnis der Triage.

## Skill-Tour (was gibt es hier?)

**Einstieg und Triage**

- `mandat-triage-insolvenzrecht` — Eingangsabfrage; Mandantenrolle und Sofort-Fristen klaeren.
- `insolvenzrecht-kaltstart-interview` — Kaltstart-Interview fuer Plugin-Profil und Praxiskonfiguration.

**Eroeffnungsgruende und Liquiditaet**

- `zahlungsunfaehigkeit-pruefung-17-inso` — Liquiditaetsstatus nach § 17 InsO; BGH-Schema zehn Prozent und drei Wochen.
- `ueberschuldung-pruefung-19-inso` — Zweistufige Ueberschuldungspruefung nach § 19 InsO; Fortbestehensprognose und Liquidationswerte.
- `liquiditaetsvorschau-insolvenzrechtlich` — Rollierende Liquiditaetsvorschau nach IDW S 11; 13-Wochen- und 24-Monats-Vorschau.

**Antragspflicht und Haftung**

- `antragspflicht-15a-inso` — Antragspflicht nach § 15a InsO; Dreiwochenfrist; Zahlungsverbot § 15b InsO; Insolvenzverschleppungshaftung.
- `do-versicherung-manager-haftung` — D-and-O-Versicherungsdeckung bei Insolvenzhaftung; Claims-made-Prinzip; Ausschluesse.

**Glaeubigerantrag und Glaeubigerrechte**

- `glaeubigerantrag-pruefung` — Zulaessigkeit und Begruendetheit des Glaeubigerantrags nach § 14 InsO.
- `glaeubigerausschuss-mitwirkung` — Rechte, Pflichten und Haftung des Glaeubigerausschussmitglieds.
- `forderungsanmeldung-glaeubiger-174-177-inso` — Forderungsanmeldung, Fristen, Form, Rang, Pruefungstermin.

**Anfechtung**

- `anfechtungsrechte-pruefen` — Uebersicht aller InsO-Anfechtungstatbestaende §§ 129 ff. InsO; Betrag, Verteidigungslinien.
- `vorsatzanfechtung-133-inso` — Vorsatzanfechtung nach § 133 InsO; Fassung seit 5. April 2017; Bargeschaeftsprivileg.

**Sanierung und Sondersituationen**

- `uebertragende-sanierung-und-asset-deals` — Unternehmensverkauf aus der Insolvenz; Asset-Deal, Glaeubigerausschuss-Zustimmung.
- `konzerninsolvenz-koordination` — Koordination mehrerer Konzerngesellschaften nach §§ 269a bis 269i InsO.

**Arbeitnehmer**

- `insolvenzgeld-165-sgb-iii` — Insolvenzgeld fuer Arbeitnehmer; Voraussetzungen, Antragsfrist zwei Monate, Vorfinanzierung.

## Worauf besonders achten

- **Dreiwochenfrist laeuft ab Eintritt des Eroeffnungsgrundes** — Nicht ab Kenntnis des Geschaeftsfuehrers; bei unklarem Eintrittszeitpunkt ist das Risiko gross.
- **Zahlungsverbot schon vor Antragstellung** — § 15b InsO greift mit Eintritt der Insolvenzreife, nicht erst mit Eroffnung; Einzelzahlungen muessen ab diesem Zeitpunkt geprueft werden.
- **Glaeubigerantrag: Glaubhaftmachung reicht nicht immer** — § 14 InsO verlangt Nachweis der Forderung und des Eroeffnungsgrundes; bloss drohende ZU genuegt dem Glaeubiger nicht.
- **Anfechtungsreform 2017 beachten** — § 133 InsO wurde durch das AnfRefG 2017 grundlegend geaendert; Fristen und Indizien unterscheiden sich fuer Sachverhalte vor und nach dem 5. April 2017.
- **Insolvenzgeld: Zweimonatsfrist ab Insolvenz-Ereignis** — Arbeitnehmer verlieren den Anspruch, wenn Antrag zu spaet gestellt wird.

## Typische Fehler

- Geschaeftsfuehrer errechnet Dreiwochenfrist ab dem Tag, an dem er Kenntnis erlangt, statt ab Eintritt der Insolvenzreife.
- Glaeubiger stellt Antrag nach § 14 InsO ohne vollstreckbaren Titel und laeuft in Zulaessigkeitsproblem.
- Forderungsanmeldung versaeumt, weil Anmeldefrist nicht im Blick war; nachtraegliche Anmeldung nach § 177 InsO noch moeglich, aber mit Kostenrisiko.
- D-and-O-Versicherung wird nicht informiert, bevor Insolvenzantrag gestellt wird; Claims-made-Risiko.
- Koordinationsplan fuer Konzerninsolvenz wird nicht erwaogen, obwohl mehrere Schwestergesellschaften betroffen sind.

## Querverweise

- `insolvenzplan-starug-planwerkstatt` — Fuer Insolvenzplan- und StaRUG-Plangestaltung.
- `bereicherungs-und-anfechtungsrecht-pruefer` — Fuer vertiefte Anfechtungspruefung nach §§ 129 ff. InsO und AnfG.
- `europarecht-kompass` — Bei grenzueberschreitender Insolvenz nach EuInsVO Art. 56 ff.

## Quellen und Aktualitaet

- Stand: 05/2026
- InsO in der geltenden Fassung (insb. §§ 15a und 15b InsO; §§ 129 und 133 InsO Fassung seit 5. April 2017)
- SGB III §§ 165 ff. in der geltenden Fassung
- IDW S 11 (Beurteilung des Vorliegens von Insolvenzeroefffnungsgruenden)
