---
name: allgemein
description: "Einstieg, Schnelltriage und Workflow-Routing im Fachanwalt Erbrecht-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext startet der Skill von selbst: klassifiziert die Aktenart, routet in den passenden Spezial-Skill oder stellt eine gezielte Rueckfrage statt einer generischen Antwort."
---

# Fachanwalt Erbrecht — Allgemein

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Fachanwalt Erbrecht**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Spezial-Skills aus diesem Plugin vorschlagen.

**Plugin-Fokus:** Plugin Fachanwalt für Erbrecht. BGB Erbrecht §§ 1922 ff. Pflichtteil Testament Erbschein Erbauseinandersetzung Erbschaftsteuer EU-ErbVO. Schnittstellen Plugin steuerrecht-anwalt-und-berater kanzlei-allgemein.

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
| `erstgespraech-mandatsannahme` | Erstgespraech im Erbrechtmandat strukturieren und Sachverhalt vollständig aufnehmen. §§ 1922 ff. BGB Erbfolge § 43a BRAO. Prüfraster: Erblasser Testament gesetzliche Erben Pflichtteilsberechtigte Nachlassbestand… |
| `fachanwalt-erbrecht-erbschaftsausschlagung` | Erbschaftsausschlagung erlaeutern und Erklärung formulieren wenn Erbe ueberschuldet ist oder sonstige Gründe vorliegen. §§ 1942 1944 1945 BGB Ausschlagung. Prüfraster: Ausschlagungsfrist sechs Wochen drei Monate… |
| `fachanwalt-erbrecht-erbschein-antrag` | Erbschein beantragen wenn Erbfolge nachgewiesen werden muss. §§ 2353 2356 BGB Erbschein §§ 352 353 FamFG Verfahren. Prüfraster: Erbscheinsart gesetzliche oder testamentarische Erbfolge Quoten Vorlage Nachlassgericht… |
| `fachanwalt-erbrecht-krypto-wallet-nachlass-multisig` | Krypto-Vermögenswerte und digitale Wallets im Erbfall sichern und auf Erben uebertragen. §§ 1922 1967 BGB digitale Nachlasswerte. Prüfraster: Wallet-Zugang Private Keys Multi-Sig Wertermittlung Steuer Erbschaft… |
| `fachanwalt-erbrecht-orientierung` | Erbrechtsmandat einordnen Bearbeitungsroute bestimmen und erste Prioritaeten setzen. §§ 1922 2229 2303 BGB § 43a BRAO. Prüfraster: Erbfolge Testament Pflichtteil Ausschlagung Nachlassinsolvenz Fristen. Output:… |
| `fachanwalt-erbrecht-pflichtteilsberechnung` | Pflichtteilsanspruch berechnen wenn Erblasser nahe Angehoerige vom Erbe ausgeschlossen hat. §§ 2303 2311 2314 BGB Pflichtteil. Prüfraster: Pflichtteilsberechtigter Nachlasswert Bewertung Auskunftsanspruch… |
| `fachanwalt-erbrecht-pflichtteilsergaenzung-2325` | Pflichtteilsergaenzungsanspruch nach § 2325 BGB berechnen wenn Erblasser Schenkungen gemacht hat. § 2325 BGB Pflichtteilsergaenzung § 2329 BGB. Prüfraster: Schenkung innerhalb 10 Jahre Abschmelzung Wertbestimmung… |
| `fachanwalt-erbrecht-testamentsentwurf` | Testament oder Erbvertrag entwerfen wenn Mandant Nachlassplanung vornehmen moechte. §§ 2229 2231 2247 BGB Testament §§ 2274 ff. BGB Erbvertrag. Prüfraster: Testierfähigkeit Form Erbeinsetung Vermaechtnisse… |
| `fachanwalt-erbrecht-testamentsvollstreckung` | Testamentsvollstreckung einrichten oder bei Streit über Vollstreckerbefugnisse beraten. §§ 2197 ff. BGB Testamentsvollstreckung. Prüfraster: Anordnung Befugnisse Aufgaben Haftung Verguetung Aufsicht Nachlassgericht… |
| `fachanwalt-erbrecht-verhandlung-mediation-erbengemeinschaft` | Streit in der Erbengemeinschaft durch Verhandlung oder Mediation lösen. §§ 2032 2042 2047 BGB Erbengemeinschaft. Prüfraster: Erbteile Nachlassbestand Verwaltungsmassnahmen Teilungsklage Auseinandersetzung… |
| `mandat-triage-erbrecht` | Erbrechtsmandat schnell einordnen und Sofortmassnahmen bestimmen. §§ 1922 1944 2303 BGB §§ 342 ff. FamFG. Prüfraster: Erbfolge Testament Ausschlagungsfrist Pflichtteil Nachlassinsolvenz. Output: Triage-Memo… |
| `nachlassinsolvenz-erbenhaftung-begrenzen` | Nachlassinsolvenz beantragen oder Erbenhaftung auf den Nachlass begrenzen wenn Nachlass ueberschuldet ist. §§ 1975 1980 2059 BGB Nachlassinsolvenz §§ 315 ff. InsO. Prüfraster: Nachlassueberschuldung Antragspflicht… |
| `pflichtteil-berechnen` | Pflichtteilsanspruch und Pflichtteilsergaenzungsanspruch berechnen. §§ 2303 2311 2325 BGB Pflichtteil. Prüfraster: Pflichtteilsquote Nachlasswert Bewertungsstichtag Abzuege Ergaenzungsanspruch Auskunft. Output:… |
| `schriftsatzkern-substantiierung` | Erbrechtsklage oder erbrechtlichen Antrag substantiiert formulieren. §§ 2303 2353 BGB §§ 253 286 ZPO. Prüfraster: Anspruchsgrundlage Sachverhalt Beweisangebot Antrag Streitwert Fristen. Output: Schriftsatzkern… |
| `vergleichsverhandlung-strategie` | Erbrechtlichen Streit durch Vergleich lösen und Verhandlungsstrategie entwickeln. §§ 2303 2042 BGB §§ 779 BGB Vergleich. Prüfraster: Vergleichsziele BATNA Nachlasswert Kosten Zeitperspektive Geheimhaltung. Output:… |

## Qualitätsversprechen

- Arbeite schnell, aber nicht hektisch.
- Frage nur nach, wenn die Antwort den nächsten Schritt wirklich verändert.
- Mache Annahmen sichtbar und halte sie knapp.
- Schlage passende Spezial-Skills aus diesem Plugin vor, bevor du in Randthemen ausweichst.
- Liefere am Ende immer einen klaren nächsten Schritt.

---

Hinweis: Keine Rechtsberatung. Dieser Skill strukturiert Workflow, Intake und Routing; fachliche Ergebnisse brauchen je nach Thema die passenden Spezial-Skills und menschliche Endprüfung.
