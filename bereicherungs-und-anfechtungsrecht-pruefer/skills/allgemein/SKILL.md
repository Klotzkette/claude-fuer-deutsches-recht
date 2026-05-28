---
name: allgemein
description: "Einstieg, Schnelltriage und Workflow-Routing im Bereicherungs Und Anfechtungsrecht Pruefer-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext startet der Skill von selbst: klassifiziert die Aktenart, routet in den passenden Spezial-Skill oder stellt eine gezielte Rueckfrage statt einer generischen Antwort."
---

# Bereicherungs- und Anfechtungsrecht-Prüfer — Allgemein

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Bereicherungs Und Anfechtungsrecht Pruefer**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Spezial-Skills aus diesem Plugin vorschlagen.

**Plugin-Fokus:** Mechanisches Durchprüfen von Bereicherungsrecht §§ 812 ff. BGB, AnfG und Insolvenzanfechtung §§ 129-147 InsO. Mit KI-Screening von Schuldnerakten, § 135 Gesellschafterdarlehen, Bargeschäft § 142 und Verteidigung des Anfechtungsgegners. Keine Rechtsberatung.

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
| `anfg-anfechtungsklage-prozessuales` | Mandant hat vollstreckbaren Titel und will angefochtene Vermögensverschiebung gerichtlich angreifen: Anfechtungsklage nach AnfG erheben. Normen: §§ 2 11 13 AnfG, §§ 195 199 BGB. Prüfraster: Titel und Fristprüfung,… |
| `anfg-einreden-und-verteidigung-anfechtungsgegner` | Mandant ist Anfechtungsgegner und will sich gegen AnfG-Anfechtungsklage verteidigen. Normen: §§ 3 4 11 AnfG, §§ 195 199 BGB, § 142 InsO analog. Prüfraster: Entreicherungseinwand, fehlende Kenntnis des… |
| `anfg-fristen-und-anfechtungszeitraum` | Anfechtungsfristen im außerinsolvenzlichen Anfechtungsrecht bestimmen: zehn Jahre Vorsatzanfechtung, vier Jahre unentgeltliche Leistung. Normen: §§ 3 4 AnfG, §§ 195 199 BGB. Prüfraster: Fristbeginn, Fristberechnung,… |
| `anfg-grundtatbestand-und-anfechtungsberechtigte` | Grundvoraussetzungen der außerinsolvenzlichen Gläubigeranfechtung klaeren: vollstreckbarer Titel, fällige Forderung, Gläubigerbenachteiligung. Normen: §§ 1 2 AnfG, §§ 195 199 BGB. Prüfraster: Anfechtungsberechtigung,… |
| `anfg-mittelbare-benachteiligung-und-kongruenz` | Kongruente und inkongruente Deckung sowie mittelbare Gläubigerbenachteiligung im AnfG-Kontext analysieren. Normen: §§ 1 3 4 AnfG. Prüfraster: unmittelbar vs. mittelbar benuenstigende Rechtshandlung, Kongruenz,… |
| `anfg-rechtsfolge-rueckgewaehr-11` | Rechtsfolge bei erfolgreicher AnfG-Anfechtung bestimmen: Duldungspflicht des Anfechtungsgegners und Wertersatz nach § 11 AnfG. Normen: § 11 AnfG, §§ 819 ff. BGB analog. Prüfraster: Duldung vs. Wertersatz,… |
| `anfg-unentgeltliche-leistung-4` | Anfechtung unentgeltlicher Leistungen außerhalb der Insolvenz prüfen: Schenkungsanfechtung in den letzten vier Jahren nach § 4 AnfG. Normen: § 4 AnfG. Prüfraster: Unentgeltlichkeitsbegriff, gemischte Schenkungen,… |
| `anfg-vorsatzanfechtung-3-i` | Vorsatzanfechtung außerhalb der Insolvenz geltend machen: Benachteiligungsvorsatz und Kenntnis des Anfechtungsgegners nach § 3 Abs. 1 AnfG. Normen: § 3 Abs. 1 AnfG. Prüfraster: Benachteiligungsvorsatz-Indizien,… |
| `ausschluss-814-bgb-kenntnis-der-nichtschuld` | Bereicherungsanspruch scheitert an § 814 BGB wegen positiver Kenntnis des Leistenden von der Nichtschuld. Normen: § 814 BGB. Prüfraster: positive Kenntnis vs. bloss Zweifel, Zeitpunkt der Kenntnis, Abgrenzung zu… |
| `ausschluss-817-bgb-gesetzes-und-sittenverstoss` | Bereicherungsanspruch gesperrt durch § 817 S. 2 BGB wegen eigenen Gesetzes- oder Sittenverstosses des Leistenden. Normen: §§ 817 134 138 BGB. Prüfraster: beiderseitiger Verstoss, Sperrwirkung, enge Rückausnahmen nach… |
| `bereicherung-eines-dritten-822-bgb` | Bereicherungsanspruch gegen Dritten bei unentgeltlicher Weitergabe des Erlangten nach § 822 BGB prüfen. Normen: § 822 BGB. Prüfraster: Unentgeltlichkeit der Weitergabe, Entreicherung des Erstempfaengers, Subsidiaritaet… |
| `condictio-indebiti-813-bgb` | Rückforderung trotz Erfuellung einer einredebehafteten Verbindlichkeit nach § 813 BGB prüfen. Normen: § 813 BGB. Prüfraster: dauernde vs. temporaere Einreden, Verjaebrungseinrede, Tatbestandsmerkmale. Output:… |
| `eingriffskondiktion-zuweisungsgehalt` | Nichtleistungskondiktion wegen Eingriffs in fremde Rechtsposition klaeren: Immaterialgueterrechte, Persoenlichkeitsrechte. Normen: § 812 Abs. 1 S. 1 Alt. 2 BGB. Prüfraster: Zuweisungsgehalt der Rechtsposition, Eingriff… |
| `falsche-wiese-warnung-bereicherung-anfechtung` | Typische Falschverortungen erkennen: Vertrag statt Bereicherung, Bereicherung statt Anfechtung, AnfG statt InsO. Normen: §§ 812 ff. BGB, AnfG, §§ 129 ff. InsO. Prüfraster: Abgrenzungsmatrix, häufige systematische… |
| `inso-bargeschaeft-142` | Bargeschäft nach § 142 InsO prüfen: unmittelbarer gleichwertiger Leistungsaustausch, Geschäftsverkehrsübung, Arbeitsentgelt-Drei-Monats-Regel, Verhältnis zu §§ 130-132 und Vorsatzanfechtung § 133 mit erkannter… |
| `inso-gesellschafterdarlehen-135` | Gesellschafterdarlehen und gleichgestellte Forderungen nach § 135 InsO prüfen: Sicherheiten zehn Jahre, Befriedigung ein Jahr, Drittdarlehen mit Gesellschaftersicherheit, Gebrauchsüberlassung, Sanierungsprivileg und… |
| `inso-grundtatbestand-129-glaeubigerbenachteiligung` | Grundvoraussetzungen der Insolvenzanfechtung nach § 129 InsO klaeren: Rechtshandlung, objektive Gläubigerbenachteiligung, Kausalität. Normen: § 129 InsO. Prüfraster: Rechtshandlungsbegriff, unmittelbare vs. mittelbare… |
| `inso-inkongruente-deckung-131` | Inkongruente Deckungsanfechtung nach § 131 InsO prüfen: Sicherung oder Befriedigung, die der Gläubiger nicht, nicht in der Art oder nicht zu der Zeit beanspruchen konnte. Fristen letzter Monat, zweiter oder dritter… |
| `inso-ki-anfechtungsansprueche-schuldnerakten` | KI-gestütztes Screening von Schuldnerakten auf mögliche Insolvenzanfechtungsansprüche nach §§ 129-147 InsO. Prüft Zahlungsdaten, Kontoauszüge, OPOS, Verträge, Sicherheiten, Gesellschafterdarlehen und Kommunikation;… |
| `inso-kongruente-deckung-130` | Kongruente Deckungsanfechtung nach § 130 InsO prüfen: geschuldete Sicherung oder Befriedigung, Drei-Monats-Zeitraum vor Insolvenzantrag oder Handlung nach Antrag, Zahlungsunfähigkeit, Kenntnis oder zwingende… |
| `inso-rechtsfolge-rueckgewaehr-143-bis-147` | Rechtsfolgen der Insolvenzanfechtung nach §§ 143-147 InsO bestimmen: Rückgewähr zur Masse, Geldschuld und Zinsen, Entreicherung bei unentgeltlicher Leistung, Gegenleistung § 144, Rechtsnachfolger § 145, Verjährung §… |
| `inso-unentgeltliche-leistung-134` | Anfechtung unentgeltlicher Leistungen in der Insolvenz nach § 134 InsO prüfen: vier Jahre vor Insolvenzantrag. Normen: § 134 InsO. Prüfraster: Unentgeltlichkeitsbegriff, Ausnahmen Anstandsschenkungen, nahestehende… |
| `inso-unmittelbar-nachteilige-rechtshandlungen-132` | Anfechtung unmittelbar nachteiliger Rechtshandlungen nach § 132 InsO prüfen: Benachteiligung in den letzten drei Monaten. Normen: §§ 132 129 InsO. Prüfraster: unmittelbare Nachteiligkeit, Kausalität, Drei-Monats-Frist,… |
| `inso-verteidigung-anfechtungsgegner` | Verteidigung des Anfechtungsgegners gegen Insolvenzanfechtung nach §§ 129-147 InsO strukturieren. Prüft fehlende Rechtshandlung oder Gläubigerbenachteiligung, Fristen, Kenntnis, § 133-Vermutungen, Bargeschäft § 142,… |
| `inso-vorsatzanfechtung-133` | Vorsatzanfechtung nach § 133 InsO prüfen: Benachteiligungsvorsatz, Kenntnis, Vermutungsregel, Deckungshandlungen mit Vier-Jahres-Frist, kongruente Deckung mit Zahlungsunfähigkeit, Zahlungserleichterungs-Vermutung,… |
| `konkurrenz-bereicherung-anfechtung-und-vindikation` | Anspruchskonkurrenzen zwischen Bereicherungsrecht §§ 812 ff. BGB, AnfG/InsO-Anfechtung und Vindikation § 985 BGB klaeren. Normen: §§ 812 985 BGB, §§ 129 ff. InsO, AnfG. Prüfraster: Verdraengungsregeln, Subsidiaritaet,… |
| `konkurrenz-bereicherung-vertraglich-deliktisch` | Verhältnis von Bereicherungsrecht zu vertraglichen Ansprüchen und Deliktsrecht §§ 823 ff. BGB klaeren. Normen: §§ 812 823 987 ff. BGB. Prüfraster: Vorrang-/Spezialitaetsfragen, bereicherungsrechtliche Lueckenfuellung.… |
| `leistungsbegriff-bewusste-zweckgerichtete-mehrung` | Leistungsbegriff im Bereicherungsrecht definieren: bewusste und zweckgerichtete Mehrung fremden Vermögens. Normen: § 812 BGB. Prüfraster: Bewusstsein, Zweckrichtung, Erkennbarkeit der Zweckbestimmung,… |
| `leistungskondiktion-grundtatbestand-812-i-1-alt-1` | Leistungskondiktion nach § 812 Abs. 1 S. 1 Alt. 1 BGB im Vier-Schritt-Schema prüfen: etwas erlangt, durch Leistung, ohne Rechtsgrund. Normen: §§ 812 813 814 817 818 819 BGB. Prüfraster: Erlangen, Leistungsbegriff,… |
| `mandatsabbruch-empfehlung-an-fachanwalt-insolvenz` | Komplexitaetsindikatoren erkennen: Wann uebersteigt der Sachverhalt dieses Prüfungstool und erfordert Fachanwalt für Insolvenzrecht. Normen: §§ 129 ff. InsO, AnfG. Prüfraster: Komplexitaetssignale, Mandatsgrenzen,… |
| `mehrpersonenverhaeltnisse-direkt-und-durchgriffskondiktion` | Bereicherungsausgleich in Mehrpersonenverhältnissen prüfen: Anweisungsfaelle, Doppelmangel, Drittleistung, Durchgriffskondiktion. Normen: § 812 BGB. Prüfraster: Leistungsbeziehungen im Dreieck, Subsidiaritaet der… |
| `nichtleistungskondiktion-grundtatbestand-812-i-1-alt-2` | Nichtleistungskondiktion nach § 812 Abs. 1 S. 1 Alt. 2 BGB prüfen: in sonstiger Weise ohne Rechtsgrund erlangt. Normen: § 812 Abs. 1 S. 1 Alt. 2 BGB. Prüfraster: kein Leistungsverhältnis, Abgrenzung zur… |
| `output-anfechtungsanzeige-insolvenzverwalter` | Anschreiben des Insolvenzverwalters an den Anfechtungsgegner erstellen: Rückgewähr nach §§ 129 ff. und § 143 InsO, Tatbestand transaktionsscharf benennen, § 142- und § 144-Hinweise, Zinsen nur bei Verzug oder § 291… |
| `output-anfechtungsklage-anfg` | Klageschrift für AnfG-Anfechtungsklage des Vollstreckungsgläubigers aufbauen: Rubrum, Duldungsantrag, Begründungsstruktur. Normen: §§ 2 11 13 AnfG. Prüfraster: Antragsformulierung, Begründungsaufbau… |
| `output-klageschrift-bereicherungsklage` | Klageschrift aus Bereicherungsrecht §§ 812 ff. BGB aufbauen: Klageantrag auf Zahlung oder Herausgabe, ODUE-Schema. Normen: §§ 812 818 BGB, §§ 253 313 ZPO. Prüfraster: Obersatz, Definition, Untersatz, Ergebnis,… |
| `output-warnhinweis-und-pruefungsdokument` | Pflicht-Header und Warnblock für alle Prüfungsdokumente generieren: kein Rechtsrat, nur mechanische Prüfung. Normen: BRAO § 3. Prüfraster: Warnhinweis, Haftungsausschluss, Hinweis auf unvollständige Sachverhalte.… |
| `parallel-und-konkurrenz-pruefung` | Bereicherungsrecht und Anfechtungsrecht gleichzeitig prüfen: Anspruchskonkurrenzen und gegenseitige Beeinflussung aller drei Regelungskreise. Normen: §§ 812 ff. BGB, AnfG, §§ 129 ff. InsO. Prüfraster: Parallelitaet,… |
| `triage-vermoegensverschiebung-erfassen` | Erster Schritt: Vermögenverschiebung strukturiert erfassen für Bereicherungs- und Anfechtungsrecht. Normen: §§ 812 ff. BGB, AnfG, §§ 129 ff. InsO. Prüfraster: Wer hat was an wen geleistet, Zeitpunkt, Belegsicherung,… |
| `umfang-der-herausgabe-818-bgb-und-entreicherung` | Umfang der Bereicherungshaftung und Entreicherungseinrede nach § 818 BGB bestimmen. Normen: §§ 818 819 BGB. Prüfraster: Erlangtes, Surrogate, Nutzungen, Wertersatz, Entreicherungseinrede, Boesglaeuigkeit. Output:… |
| `verfuegung-eines-nichtberechtigten-816-bgb` | Bereicherungsanspruch des Berechtigten nach § 816 BGB gegen verfuegenden Nichtberechtigten prüfen. Normen: § 816 BGB. Prüfraster: wirksame Verfuegung durch Gutglaubenserwerb oder Genehmigung, entgeltlich vs.… |
| `verjaehrung-bereicherung-anfechtung-fristen` | Verjährung und Anfechtungsfristen trennen: § 195 und § 199 BGB für Bereicherung, § 15 AnfG, § 146 InsO mit Verweis auf regelmäßige BGB-Verjährung. Prüft Fristbeginn, Kenntnis, grob fahrlässige Unkenntnis, Hemmung,… |
| `verschaerfte-haftung-819-bgb-bei-bosglaeubigkeit` | Verschaerfte Bereicherungshaftung nach § 819 BGB bei Boesglaeuigkeit oder Rechtshaengigkeit prüfen. Normen: §§ 819 818 Abs. 4 BGB. Prüfraster: Kenntnis des Mangels, Zeitpunkt, Umfang verschaerfte Haftung,… |
| `weichenstellung-bereicherung-oder-anfechtung` | Triage-Entscheidung: welcher Regelungskreis ist einschlaegig - Bereicherungsrecht, außerinsolvenzliche Anfechtung oder Insolvenzanfechtung. Normen: §§ 812 ff. BGB, AnfG, §§ 129 ff. InsO. Prüfraster: Rechtsgrundmangel,… |

## Worum geht es?

Dieses Plugin prueft mechanisch, welcher Regelungskreis bei Vermoegensverschie­bungen einschlaegig ist: das Bereicherungsrecht der §§ 812 ff. BGB, die ausserinsolvenzliche Glaeubigeranfechtung nach dem AnfG oder die Insolvenzanfechtung nach §§ 129 bis 147 InsO. Es unterstuetzt Anwaelte und Berater bei der Subsumtion, bei der Anspruchsformulierung und bei der Erstellung von Schriftsaetzen. Das Plugin ersetzt keine Rechtsberatung und gibt keinen Rechtsrat an Mandanten.

Die Weichenstellung zwischen den drei Regelungskreisen ist die haeufigste Fehlerquelle in der Praxis: Ein Bereicherungsanspruch setzt keinen Titel voraus und keinen Insolvenzantrag; eine AnfG-Anfechtung benoetigt einen vollstreckbaren Titel ausserhalb der Insolvenz; eine InsO-Anfechtung setzt ein eroeffnetes Insolvenzverfahren voraus. Dieses Plugin arbeitet diese Abgrenzung systematisch durch.

## Wann brauchen Sie diese Skill?

- Sie wollen pruefen, ob eine Vermoegenverschiebung bereicherungsrechtlich, ausserinsolvenzlich oder insolvenzrechtlich angegriffen werden kann.
- Sie sind Insolvenzverwalter und pruefen Anfechtungsansprueche gegen Glaeubiger oder Dritte.
- Sie sind Vollstreckungsglaeubiger und wollen eine Vermoegensverschiebung des Schuldners anfechten (AnfG).
- Sie muessen als Anfechtungsgegner Verteidigungsargumente strukturieren.
- Sie erstellen Klageschriften, Anfechtungsanzeigen oder Warnhinweise in bereicherungs- oder anfechtungsrechtlichen Mandaten.

## Fachbegriffe (kurz erklaert)

- **Leistungskondiktion** — Rueckforderungsanspruch wegen einer Leistung ohne Rechtsgrund (§ 812 Abs. 1 S. 1 Alt. 1 BGB); setzt bewusste und zweckgerichtete Vermehrung fremden Vermoegens voraus.
- **Eingriffskondiktion** — Bereicherungsanspruch bei Eingriff in eine fremde Rechtsposition mit Zuweisungsgehalt ohne Leistungsbeziehung (§ 812 Abs. 1 S. 1 Alt. 2 BGB).
- **Entreicherung** — Einrede des Bereicherten, soweit er das Erlangte nicht mehr hat (§ 818 Abs. 3 BGB); bei Boesglaeuigkeit ausgeschlossen (§ 819 BGB).
- **AnfG-Anfechtung** — Ausserinsolvenzliche Glaeubigeranfechtung durch Vollstreckungsglaeubiger mit Titel; schuetzt vor Vereitelung der Zwangsvollstreckung.
- **Kongruente Deckung** — Befriedigung oder Sicherung, die dem Glaeubiger so zustand; nach § 130 InsO anfechtbar bei Zahlungsunfaehigkeit und Kenntnis.
- **Inkongruente Deckung** — Befriedigung oder Sicherung, die so nicht oder nicht zu der Zeit beansprucht werden konnte (§ 131 InsO); erleichterte Anfechtbarkeit.
- **Bargeschäft** — unmittelbarer Austausch gleichwertiger Leistungen; schützt nach § 142 InsO, bleibt bei § 133 InsO aber nur geschützt, wenn keine erkannte Unlauterkeit des Schuldners hinzukommt.
- **Vorsatzanfechtung** — Anfechtung wegen Benachteiligungsvorsatzes des Schuldners und Kenntnis des Anfechtungsgegners (§ 133 InsO bzw. § 3 AnfG); laengste Anfechtungsfrist.

## Rechtsgrundlagen

- §§ 812 bis 822 BGB — Bereicherungsrecht (Leistungs-, Nichtleistungskondiktion, Umfang, Ausschluesse).
- §§ 1 bis 15 AnfG — Ausserinsolvenzliche Glaeubigeranfechtung.
- §§ 129 bis 147 InsO — Insolvenzanfechtung (Grundtatbestand, Deckungsanfechtung, Vorsatz, Rechtsfolgen).
- § 142 InsO — Bargeschaeftsprivileg.
- §§ 195 und 199 BGB — Regelmaessige Verjaehrung drei Jahre, Beginn mit Jahresende.
- § 15 AnfG — Verjaehrung AnfG-Anfechtungsanspruch drei Jahre.
- § 146 InsO — Verjährung des Insolvenzanfechtungsanspruchs nach den Regeln der regelmäßigen Verjährung des BGB.

## Schritt-fuer-Schritt: Einstieg ins Plugin

1. Mandantenkonstellation klaeren: Wer hat was an wen geleistet, wann, gegen welche Gegenleistung?
2. Weichenstellung treffen: Liegt ein eroeffnetes Insolvenzverfahren vor? Liegt ein vollstreckbarer Titel vor?
3. Passenden Regelungskreis auswaehlen: Skill `weichenstellung-bereicherung-oder-anfechtung` oder `triage-vermoegensverschiebung-erfassen`.
4. Fristen pruefen: Skill `verjaehrung-bereicherung-anfechtung-fristen`.
5. Anspruchsgutachten oder Schriftsatz erstellen mit dem Spezial-Skill des gewaaehlten Regelungskreises.

## Skill-Tour (was gibt es hier?)

**Triage und Weichenstellung**

- `triage-vermoegensverschiebung-erfassen` — Erster Schritt zur strukturierten Erfassung der Vermoegenverschiebung fuer alle drei Regelungskreise.
- `weichenstellung-bereicherung-oder-anfechtung` — Triage-Entscheidung: welcher Regelungskreis ist einschlaegig.
- `falsche-wiese-warnung-bereicherung-anfechtung` — Erkennt typische Falschverortungen und leitet zum richtigen Regelungskreis weiter.
- `parallel-und-konkurrenz-pruefung` — Prueft alle drei Regelungskreise gleichzeitig auf Anspruchskonkurrenzen.

**Bereicherungsrecht — Grundtatbestaende**

- `leistungskondiktion-grundtatbestand-812-i-1-alt-1` — Leistungskondiktion nach § 812 Abs. 1 S. 1 Alt. 1 BGB im Vier-Schritt-Schema.
- `nichtleistungskondiktion-grundtatbestand-812-i-1-alt-2` — Nichtleistungskondiktion nach § 812 Abs. 1 S. 1 Alt. 2 BGB.
- `leistungsbegriff-bewusste-zweckgerichtete-mehrung` — Definiert den Leistungsbegriff im Bereicherungsrecht.
- `eingriffskondiktion-zuweisungsgehalt` — Eingriffskondiktion bei Eingriff in fremde Rechtspositionen.

**Bereicherungsrecht — Spezialtatbestaende**

- `condictio-indebiti-813-bgb` — Rueckforderung trotz Erfuellung einer einredebehafteten Verbindlichkeit.
- `verfuegung-eines-nichtberechtigten-816-bgb` — Anspruch des Berechtigten nach § 816 BGB.
- `bereicherung-eines-dritten-822-bgb` — Bereicherungsanspruch gegen Dritten bei unentgeltlicher Weitergabe.
- `mehrpersonenverhaeltnisse-direkt-und-durchgriffskondiktion` — Bereicherungsausgleich in Drei- und Mehrpersonenverhaeltnissen.

**Bereicherungsrecht — Umfang und Ausschluesse**

- `umfang-der-herausgabe-818-bgb-und-entreicherung` — Umfang der Bereicherungshaftung und Entreicherungseinrede.
- `verschaerfte-haftung-819-bgb-bei-bosglaeubigkeit` — Verschaerfte Haftung bei Boesglaeuigkeit oder Rechtshaengigkeit.
- `ausschluss-814-bgb-kenntnis-der-nichtschuld` — Ausschluss bei Kenntnis der Nichtschuld.
- `ausschluss-817-bgb-gesetzes-und-sittenverstoss` — Ausschluss bei eigenem Gesetzes- oder Sittenverstoss.

**Bereicherungsrecht — Konkurrenz**

- `konkurrenz-bereicherung-vertraglich-deliktisch` — Verhaeltnis Bereicherungsrecht zu vertraglichen und deliktischen Anspruechen.
- `konkurrenz-bereicherung-anfechtung-und-vindikation` — Anspruchskonkurrenzen zwischen Bereicherungsrecht, Anfechtung und § 985 BGB.

**Ausserinsolvenzliche Anfechtung (AnfG)**

- `anfg-grundtatbestand-und-anfechtungsberechtigte` — Grundvoraussetzungen der ausserinsolvenzlichen Glaeubigeranfechtung.
- `anfg-vorsatzanfechtung-3-i` — Vorsatzanfechtung nach § 3 Abs. 1 AnfG mit Zehn-Jahres-Frist.
- `anfg-unentgeltliche-leistung-4` — Anfechtung unentgeltlicher Leistungen nach § 4 AnfG.
- `anfg-mittelbare-benachteiligung-und-kongruenz` — Kongruenz und mittelbare Glaeubigerbenachteiligung im AnfG.
- `anfg-rechtsfolge-rueckgewaehr-11` — Duldungspflicht und Wertersatz nach § 11 AnfG.
- `anfg-fristen-und-anfechtungszeitraum` — Anfechtungsfristen im AnfG: zehn Jahre Vorsatz, vier Jahre unentgeltlich.
- `anfg-einreden-und-verteidigung-anfechtungsgegner` — Verteidigung des Anfechtungsgegners gegen AnfG-Klage.
- `anfg-anfechtungsklage-prozessuales` — Prozessuales zur AnfG-Anfechtungsklage.

**Insolvenzanfechtung (§§ 129 ff. InsO)**

- `inso-grundtatbestand-129-glaeubigerbenachteiligung` — Grundtatbestand Insolvenzanfechtung: Rechtshandlung und Glaeubigerbenachteiligung.
- `inso-kongruente-deckung-130` — Kongruente Deckungsanfechtung nach § 130 InsO.
- `inso-inkongruente-deckung-131` — Inkongruente Deckungsanfechtung nach § 131 InsO.
- `inso-unmittelbar-nachteilige-rechtshandlungen-132` — Anfechtung unmittelbar nachteiliger Rechtshandlungen nach § 132 InsO.
- `inso-vorsatzanfechtung-133` — Vorsatzanfechtung nach § 133 InsO mit Zehn-Jahres-Grundfrist, Vier-Jahres-Deckungsfrist und § 133 Abs. 3.
- `inso-unentgeltliche-leistung-134` — Anfechtung unentgeltlicher Leistungen nach § 134 InsO.
- `inso-gesellschafterdarlehen-135` — Gesellschafterdarlehen, gleichgestellte Forderungen, Drittdarlehen mit Gesellschaftersicherheit.
- `inso-bargeschaeft-142` — Bargeschäft nach § 142 InsO ohne starre 30-Tage-Regel.
- `inso-rechtsfolge-rueckgewaehr-143-bis-147` — Rechtsfolgen der Insolvenzanfechtung nach §§ 143 bis 147 InsO.
- `inso-ki-anfechtungsansprueche-schuldnerakten` — KI-gestütztes Screening von Schuldnerakten auf mögliche Anfechtungsansprüche mit Beleg- und Human-Review-Matrix.
- `inso-verteidigung-anfechtungsgegner` — Verteidigung gegen Insolvenzanfechtung aus Sicht des Anfechtungsgegners.

**Verjaehrung und Fristen**

- `verjaehrung-bereicherung-anfechtung-fristen` — Verjaehrungsfristen im Ueberblick fuer alle drei Regelungskreise.

**Output-Skills**

- `output-klageschrift-bereicherungsklage` — Klageschrift aus Bereicherungsrecht §§ 812 ff. BGB aufbauen.
- `output-anfechtungsanzeige-insolvenzverwalter` — Anschreiben des Insolvenzverwalters an Anfechtungsgegner erstellen.
- `output-anfechtungsklage-anfg` — Klageschrift fuer AnfG-Anfechtungsklage des Vollstreckungsglaeubigers.
- `output-warnhinweis-und-pruefungsdokument` — Pflicht-Header und Warnblock fuer alle Pruefungsdokumente.

**Mandatssteuerung**

- `mandatsabbruch-empfehlung-an-fachanwalt-insolvenz` — Erkennt Komplexitaetsindikatoren und empfiehlt Fachanwalt.

## Worauf besonders achten

- **Weichenstellung zuerst** — Die Verwechslung von Bereicherungsrecht, AnfG und InsO-Anfechtung ist der haeufigste systematische Fehler; `weichenstellung-bereicherung-oder-anfechtung` immer zuerst aufrufen.
- **Insolvenzeroefffnung als Voraussetzung** — InsO-Anfechtung durch Insolvenzverwalter setzt eroeffnetes Verfahren voraus; ohne Eroeffnungsbeschluss ist nur AnfG einschlaegig.
- **Bargeschäft bei InsO-Anfechtung prüfen** — § 142 InsO schützt echten gleichwertigen Austausch; bei § 133 InsO zusätzlich erkannte Unlauterkeit prüfen.
- **Vorsatzanfechtung Reform 2017** — § 133 InsO wurde durch das Anfechtungsreformgesetz 2017 erheblich verändert; allgemeine Zehn-Jahres-Frist, Vier-Jahres-Frist für Deckungshandlungen und Zwei-Jahres-Regel bei § 133 Abs. 4 sauber trennen.
- **KI nur beleggebunden einsetzen** — KI darf Kandidaten und Indizien aus Schuldnerakten aufbereiten, aber § 133-Wertungen und komplexe Dreiecksverhältnisse nicht final entscheiden.
- **Entreicherungseinrede rechtzeitig pruefen** — § 818 Abs. 3 BGB wird haeufig vergessen; bei Boesglaeuigkeit (§ 819 BGB) greift sie jedoch nicht.

## Typische Fehler

- Mandant hat keinen Titel, will aber AnfG-Anfechtung betreiben — AnfG setzt vollstreckbaren Titel voraus.
- Bereicherungsanspruch wird geltend gemacht, obwohl ein vertraglicher Anspruch vorgeht und keine Subsidiaritaet ueberprueft wurde.
- Vorsatzanfechtung nach § 133 InsO wird mit der alten Rechtslage oder mit falscher Vier-Jahres-Pauschale argumentiert.
- Dreimonatsfrist des § 130 InsO wird von der Antragstellung, nicht von der Eroeffnung her berechnet.
- Warnhinweis auf fehlenden Rechtsberatungscharakter fehlt im Dokument.

## Querverweise

- `insolvenzrecht` — Fuer den uebergeordneten insolvenzrechtlichen Kontext (Eroeffnungsgruende, Antragspflicht).
- `insolvenzplan-starug-planwerkstatt` — Wenn Anfechtungsrisiken in der Plangestaltung beeinflusst werden sollen.
- `bereicherungs-und-anfechtungsrecht-pruefer` — Dieses Plugin ist bereits das spezialisierte Werkzeug.

## Quellen und Aktualitaet

- Stand: 05/2026
- BGB §§ 812 ff. in der geltenden Fassung
- InsO §§ 129 ff. in der Fassung nach dem AnfRefG 2017
- AnfG in der geltenden Fassung
