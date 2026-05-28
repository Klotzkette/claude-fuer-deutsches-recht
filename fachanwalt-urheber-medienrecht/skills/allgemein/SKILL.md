---
name: allgemein
description: "Einstieg, Schnelltriage und Workflow-Routing im Fachanwalt Urheber Medienrecht-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext startet der Skill von selbst: klassifiziert die Aktenart, routet in den passenden Spezial-Skill oder stellt eine gezielte Rueckfrage statt einer generischen Antwort."
---

# Fachanwalt Urheber Medienrecht — Allgemein

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Fachanwalt Urheber Medienrecht**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Spezial-Skills aus diesem Plugin vorschlagen.

**Plugin-Fokus:** Plugin Fachanwalt für Urheber- und Medienrecht. UrhG UWG KUG Recht am eigenen Bild Presserecht Persoenlichkeitsrecht Medienstaatsvertrag. Schnittstellen Plugin gewerblicher-rechtsschutz verlagsredaktion kanzlei-allgemein.

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
| `erstgespraech-mandatsannahme` | Erstgespraech im Urheber- und Medienrechtsmandat strukturieren und Mandat sauber aufnehmen. §§ 1 7 UrhG Werkbegriff § 43a BRAO. Prüfraster: Sachverhaltserfassung Schutzfähigkeit Parteistellung Fristen… |
| `fachanwalt-urheber-medienrecht-abmahnung-pruefen` | Urheberrechtliche Abmahnung § 97a UrhG Voraussetzungen Inhalt Aktivlegitimation Anspruchsberechtigung Lizenzkette Belege. Vorformulierte Unterlassungserklärung prüfen Vertragsstrafe Hoehe Abgrenzung modifizierte… |
| `fachanwalt-urheber-medienrecht-filesharing-verteidigung` | Filesharing-Abmahnung verteidigen und Gegenargumente entwickeln wenn Urheberrechtsverletzung per Internetzugang vorgeworfen wird. §§ 97 97a UrhG Abmahnung §§ 85 ff. UrhG Leistungsschutzrechte. Prüfraster:… |
| `fachanwalt-urheber-medienrecht-gegendarstellung-presse` | Gegendarstellung Pressefreiheit § 11 BlnPresseG analog Landes-Presse-Gesetze. Voraussetzung Tatsachen-Behauptung Betroffener berechtigtes Interesse Frist 3 Monate. Verlangen schriftlich Form. Klage AG / LG bei… |
| `fachanwalt-urheber-medienrecht-lizenzvertrag-verhandlung` | Lizenzvertraege für Urheberrechte Leistungsschutzrechte oder Marken verhandeln und gestalten. §§ 31 ff. UrhG Nutzungsrechte §§ 87a ff. UrhG Leistungsschutz. Prüfraster: Nutzungsrechtsart ausschließlich einfach… |
| `fachanwalt-urheber-medienrecht-mod-erklaerung` | Modifizierte Unterlassungserklärung als Alternative zur strafbewehrten UE prüfen und formulieren. § 97a UrhG Abmahnung und UE § 339 BGB Vertragsstrafe. Prüfraster: Wiederholungsgefahr Strafbewehrung Vertragsstrafe… |
| `fachanwalt-urheber-medienrecht-orientierung` | Urheber- und Medienrechtsmandat einordnen und Bearbeitungsroute bestimmen. §§ 1 2 7 UrhG §§ 97 ff. UrhG §§ 22 ff. KUG. Prüfraster: Schutzgegenstand Verletzungshandlung Parteistellung Route Fristen. Output:… |
| `fachanwalt-urheber-medienrecht-presse-gegendarstellung` | Gegendarstellungsanspruch in der Presse prüfen und Gegendarstellung verfassen. §§ 10 ff. LPG Gegendarstellungsrecht Art. 5 GG Pressefreiheit. Prüfraster: Tatsachenbehauptung Erstmitteilung Frist Form Umfang… |
| `fachanwalt-urheber-medienrecht-schiedsstelle-dpma-vgg` | Schiedsstellenverfahren beim DPMA nach VGG einleiten oder verteidigen. §§ 92 ff. VGG Schiedsstelle § 128 VGG. Prüfraster: Zuständigkeit Verfahrensvoraussetzungen Antrag Fristen Verhandlung Einigungsvorschlag. Output:… |
| `fachanwalt-urheber-medienrecht-tdm-44b-urhg-ki-training-opt-out` | Text- und Data-Mining-Opt-out nach § 44b UrhG erklären wenn KI-Training mit urheberrechtlich geschützten Werken verhindert werden soll. § 44b UrhG TDM §§ 87a ff. UrhG Datenbankschutz DSA. Prüfraster: Opt-out-Erklärung… |
| `gegendarstellung-presse` | Gegendarstellungsrecht im Presserecht prüfen und Gegendarstellung ausformulieren. §§ 10 ff. LPG Art. 5 GG. Prüfraster: Tatsachenbehauptung Erstmitteilung Fristen Form Umfang Abdruck Unterlassungsanspruch. Output:… |
| `mandat-triage-urheber-medienrecht` | Urheber- und Medienrechtsmandat schnell einordnen und naechste Schritte bestimmen. §§ 1 2 97 UrhG §§ 22 23 KUG LPG. Prüfraster: Schutzgegenstand Verletzungsart Parteistellung Fristen Verfahrensart. Output: Triage-Memo… |
| `schriftsatzkern-substantiierung` | Schriftsatzkern für urheber- und medienrechtliche Klagen und Anträge substantiiert ausformulieren. §§ 97 97a 101 UrhG §§ 935 940 ZPO einstweilige Verfuegung. Prüfraster: Anspruchsgrundlage Sachverhaltssubstantiierung… |
| `urheber-abmahnung-pruefen` | Urheberrechtsabmahnung auf Berechtigung Formwirksamkeit und Reaktionsstrategie prüfen. § 97a UrhG § 97 UrhG Unterlassung Schadensersatz. Prüfraster: Schutzfähigkeit Verletzungshandlung Abmahnberechtigung UE… |
| `vergleichsverhandlung-strategie` | Vergleichsverhandlung im Urheber- und Medienrechtstreit vorbereiten und Strategie entwickeln. §§ 97 97a UrhG §§ 779 BGB Vergleich. Prüfraster: Vergleichsziele BATNA Streitwert Kosten Lizenzbereitschaft Geheimhaltung.… |

## Qualitätsversprechen

- Arbeite schnell, aber nicht hektisch.
- Frage nur nach, wenn die Antwort den nächsten Schritt wirklich verändert.
- Mache Annahmen sichtbar und halte sie knapp.
- Schlage passende Spezial-Skills aus diesem Plugin vor, bevor du in Randthemen ausweichst.
- Liefere am Ende immer einen klaren nächsten Schritt.

---

Hinweis: Keine Rechtsberatung. Dieser Skill strukturiert Workflow, Intake und Routing; fachliche Ergebnisse brauchen je nach Thema die passenden Spezial-Skills und menschliche Endprüfung.
