---
name: allgemein
description: "Einstieg, Schnelltriage und Workflow-Routing im KI VO AI Act Pruefer-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext startet der Skill von selbst: klassifiziert die Aktenart, routet in den passenden Spezial-Skill oder stellt eine gezielte Rueckfrage statt einer generischen Antwort."
---

# KI-VO AI-Act-Pruefer — Allgemein

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **KI VO AI Act Pruefer**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Spezial-Skills aus diesem Plugin vorschlagen.

**Plugin-Fokus:** Vollständiger Mechanik-Workflow zur Verordnung (EU) 2024/1689 (KI-VO): KI-System-Definition, Rollen, Risikoklassen, Hochrisiko-Pflichten, GPAI-Modelle, Sanktionen. Kein Rechtsrat.

**Neuer Schwerpunkt für Art. 3 und Art. 6 Abs. 2:** Wenn es um allgemeine Chatbots, ChatGPT-ähnliche Systeme, GPAI, Mitarbeitenden-Fehlgebrauch oder Hochrisiko nach Anhang III geht, immer Zweckbestimmung und tatsächliche Nutzung trennen. Ein allgemeiner Chatbot ist nicht automatisch Hochrisiko; der konkrete Einsatz in Personal, Bildung, Kredit, Justiz, Migration, Strafverfolgung, Notfalltriage, kritischer Infrastruktur oder Biometrie kann aber Hochrisiko auslösen.

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

### 1a. KI-VO-Spezialintake

Bei KI-VO-Fragen zusätzlich sofort klären:

| Punkt | Frage | Routing |
|---|---|---|
| Systemzuschnitt | Prüfen wir Modell, API, Chatbot, Agent, Workflow, Fachmodul oder Gesamtprodukt? | `liegt-ki-system-vor-art-3-nr-1` |
| Zweckbestimmung | Was sagt Anbieter/Betreiber, wofür das System bestimmt ist? | `hochrisiko-art-6-abs-2-anhang-iii` |
| Tatsächliche Nutzung | Wie wird das Tool wirklich im Unternehmen genutzt? | `betreiber-deployer-pflichten-art-26` |
| Chatbot/GPAI | Ist es ein allgemeiner Chatbot oder GPAI-basiertes System? | `gpai-vorliegen-art-3-nr-63` |
| Anhang-III-Nähe | Berührt es Personal, Bildung, Kredit, Justiz, Migration, Strafverfolgung, Biometrie, kritische Infrastruktur oder Notfalltriage? | `hochrisiko-art-6-abs-2-anhang-iii` |
| Fehlgebrauch | Können Mitarbeitende es entgegen der Zweckbestimmung hochriskant einsetzen? | `betreiber-deployer-pflichten-art-26`, ggf. `anbieter-werden-art-25` |
| Dokumentation | Soll ein Vermerk für die Compliance-Akte entstehen? | `output-pruefdokument-ki-vo-mit-warnhinweisen` |

### 2. Sofort-Triage

Arbeite danach in dieser Reihenfolge:

1. **Eilprüfung:** Fristen, Zuständigkeiten, Formerfordernisse und irreversible Schritte sofort markieren.
2. **Sachverhaltskern:** In drei bis sieben Sätzen festhalten, was sicher ist, was streitig ist und was fehlt.
3. **Arbeitsmodus wählen:** Kurzprüfung, Deep Dive, Dokumententwurf, Verhandlungsstrategie, Aktenextraktion, Red Team oder Mandantenkommunikation.
4. **Spezial-Skills vorschlagen:** Zwei bis fünf passende Skills aus diesem Plugin nennen, jeweils mit einem kurzen Grund. Bei Chatbot/GPAI und Anhang-III-Nähe immer `liegt-ki-system-vor-art-3-nr-1`, `gpai-vorliegen-art-3-nr-63`, `hochrisiko-art-6-abs-2-anhang-iii` und `output-pruefdokument-ki-vo-mit-warnhinweisen` erwägen.
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
| `abgrenzung-konventionelle-software-vs-ki-system` | Grenzfälle zwischen Automation, Statistik, Expertensystem, Workflow und KI-System; besonders Inferenz, gelernte Parameter, LLM/API und menschliche Freigabe. |
| `anbieter-werden-art-25` | Betreiber Einführer oder Haendler fragt: Werde ich durch mein Verhalten selbst zum Anbieter eines KI-Systems mit allen daraus folgenden Pflichten? Art. 25 KI-VO Re-Provisioning. Prüfraster: vier Fallgruppen wesentliche… |
| `begrenztes-risiko-art-50-transparenzpflichten` | Unternehmen setzt Chatbot Deepfake-Tool oder KI-Textgenerator ein und fragt: Welche Hinweispflichten treffen uns gegenüber Nutzern? Art. 50 KI-VO begrenztes Risiko. Prüfraster: Chatbot-Hinweispflicht Art. 50 Abs. 1… |
| `betreiber-deployer-pflichten-art-26` | Betreiberpflichten plus Off-label-Nutzung durch Mitarbeitende, Zweckänderung, Chatbot-Governance, Art. 25-Anbieterwerden und Re-Evaluation. |
| `bevollmaechtigter-und-produkthersteller-pflichten-art-22-und-25` | Drittstaaten-Anbieter ohne EU-Niederlassung oder Produkthersteller fragt: Wer vertritt uns in der EU und wer haftet für integrierte KI-Komponenten? Art. 22 KI-VO Bevollmaechtigter Art. 25 Produkthersteller. Prüfraster:… |
| `code-of-practice-und-harmonisierte-normen` | Standards-Landkarte: Art. 40/41/56, GPAI Code of Practice, ISO/IEC 42001/23894/22989/23053 ohne falsche Vermutungswirkung. |
| `einfuehrer-importer-pflichten-art-23` | Importeur von KI-Systemen aus Drittstaaten fragt: Was muss ich prüfen bevor ich ein Hochrisiko-KI-System in der EU in Verkehr bringe? Art. 23 KI-VO Einführer-Pflichten. Prüfraster: Konformitätsbewertung durch Anbieter… |
| `entscheidungsbaum-ki-vo-gesamt-workflow` | Master-Workflow von Art. 3 über Rollen, Art. 6 Abs. 2/Anhang III, GPAI/Chatbot-Abgrenzung, Fehlgebrauch und Output-Dokumentation. |
| `eu-datenbank-registrierung-art-49-und-71` | Anbieter oder Betreiber von Hochrisiko-KI fragt: In welcher EU-Datenbank muss ich mein KI-System registrieren und wann? Art. 49 und 71 KI-VO Registrierungspflichten. Prüfraster: Anbieter vor Inverkehrbringen Pflicht… |
| `falsche-wiese-warnung-ki-vo` | Nutzer fragt eine KI-VO-Frage die eigentlich unter DSGVO Produkthaftung MDR oder Maschinenverordnung faellt. Warnt vor typischen Rechtsgebiets-Verwechslungen KI-VO versus DSGVO versus Produkthaftungsrichtlinie versus… |
| `governance-aufsichtsbehoerden-art-70` | Unternehmen oder Behoerde fragt: An wen muss ich mich in Deutschland und Europa wenden wenn ich Fragen zur KI-VO-Aufsicht habe oder eine Meldepflicht erfullen muss? Art. 70 ff. KI-VO Governance. Prüfraster: nationale… |
| `gpai-modelle-art-51-bis-55` | Entwickler oder Anbieter eines Sprachmodells oder Basismodells fragt: Fallen wir unter die GPAI-Pflichten der KI-VO und was muessen wir konkret tun? Art. 51 bis 55 KI-VO GPAI-Modelle. Prüfraster: technische… |
| `gpai-systemisches-risiko-schwelle-10e25-flop` | Anbieter eines sehr grossen Basismodells fragt: Haben wir die Schwelle für systemisches Risiko ueberschritten und welche Zusatzpflichten gelten dann? Art. 51 und 55 KI-VO GPAI systemisches Risiko. Prüfraster:… |
| `gpai-vorliegen-art-3-nr-63` | GPAI-Modell/System und allgemeiner Chatbot; erklärt, warum GPAI nicht automatisch Hochrisiko ist und wann Anhang III trotzdem greift. |
| `haendler-distributor-pflichten-art-24` | Distributeur oder Grosshaendler von KI-Systemen fragt: Welche Sorgfaltspflichten habe ich beim Weitervertrieb von Hochrisiko-KI? Art. 24 KI-VO Haendler-Pflichten. Prüfraster: Plausibilitaetsprüfung CE-Kennzeichnung… |
| `hochrisiko-art-6-abs-1-sicherheitsbauteil` | Unternehmen integriert KI-Komponente in ein reguliertes Produkt (Medizinprodukt Maschine Fahrzeug) und fragt: Wird das Gesamtprodukt dadurch zum Hochrisiko-KI-System? Art. 6 Abs. 1 KI-VO Sicherheitsbauteil Anhang I.… |
| `hochrisiko-art-6-abs-2-anhang-iii` | Vertiefter Anhang-III-Checker mit allen acht Bereichen, Untertatbeständen, Zweckbestimmung, Chatbot/GPAI und Mitarbeitenden-Fehlgebrauch. |
| `hochrisiko-aufzeichnungspflichten-logging-art-12` | Anbieter von Hochrisiko-KI fragt: Was muss unser System automatisch aufzeichnen und wie lange muessen wir die Logs aufbewahren? Art. 12 KI-VO Logging-Pflichten. Prüfraster: Mindestinhalte der Logs Zeitstempel… |
| `hochrisiko-bestaetigt-end-to-end-roadmap` | Anbieter hat Hochrisiko-Einstufung des eigenen KI-Systems bestätigt und fragt: Was sind jetzt alle noetigen Schritte bis zur CE-Kennzeichnung und Marktfreigabe? End-to-End-Roadmap Hochrisiko-KI Art. 9 bis 49 KI-VO.… |
| `hochrisiko-datenqualitaet-und-data-governance-art-10` | Anbieter von Hochrisiko-KI fragt: Welche Anforderungen gelten für unsere Trainings- Validierungs- und Testdaten und wie dokumentieren wir unsere Data Governance? Art. 10 KI-VO Datenqualitaet und Data Governance.… |
| `hochrisiko-genauigkeit-robustheit-cybersicherheit-art-15` | Anbieter von Hochrisiko-KI fragt: Welche Leistungsstandards für Genauigkeit Robustheit und Cybersicherheit muessen wir nachweisen und dokumentieren? Art. 15 KI-VO Mindeststandards. Prüfraster: Genauigkeitsmetriken und… |
| `hochrisiko-konformitaetsbewertung-art-43-bis-49` | Anbieter von Hochrisiko-KI fragt: Muessen wir eine benannte Stelle einschalten oder koennen wir die Konformitätsbewertung selbst durchführen? Art. 43 bis 49 KI-VO Konformitätsbewertung. Prüfraster: Entscheidungsbaum… |
| `hochrisiko-menschliche-aufsicht-art-14` | Anbieter oder Betreiber fragt: Wie stellen wir sicher dass Menschen das Hochrisiko-KI-System wirksam beaufsichtigen und uebersteuerung ist möglich? Art. 14 KI-VO menschliche Aufsicht. Prüfraster: Verstehen der… |
| `hochrisiko-risikomanagementsystem-art-9` | Anbieter von Hochrisiko-KI fragt: Wie setzen wir ein KI-VO-konformes Risikomanagementsystem auf und was muss es enthalten? Art. 9 KI-VO Risikomanagementsystem. Prüfraster: kontinuierlicher iterativer Prozess… |
| `hochrisiko-technische-dokumentation-art-11-und-anhang-iv` | Anbieter von Hochrisiko-KI fragt: Was muss die technische Dokumentation enthalten und wie aktuell muss sie sein? Art. 11 i.V.m. Anhang IV KI-VO. Prüfraster: vollständiger Inhaltskatalog nach Anhang IV… |
| `hochrisiko-transparenz-und-informationen-fuer-betreiber-art-13` | Anbieter von Hochrisiko-KI fragt: Welche Informationen muessen wir dem Betreiber in der Gebrauchsanweisung zur Verfuegung stellen? Art. 13 KI-VO Transparenz und Informationspflichten. Prüfraster: Gebrauchsanweisung… |
| `hochrisiko-zuordnung-art-6-und-anhang-i-iii` | Überblick zu Art. 6 Abs. 1/2, Zweckbestimmung statt Tool-Label, Rückausnahme und Pflichtenfolge. |
| `liegt-ki-system-vor-art-3-nr-1` | Art.-3-Kerncheck mit sieben Elementen: Automation, Autonomie, Adaptivität, Ziele, Inferenz, Output und Umgebungseinfluss. |
| `mandatsabbruch-empfehlung-komplexe-faelle` | Mechanik-Workflow erkennt Anzeichen von Faellen die anwaltliche Spezialkenntnisse erfordern und empfiehlt Eskalation. Indikatoren für Komplexitaet jenseits des KI-VO-Prüfers: multijurisdiktionelle Lieferketten… |
| `marktueberwachung-meldung-vorfaelle-art-72-bis-79` | Anbieter oder Betreiber hat einen schwerwiegenden Vorfall mit einem Hochrisiko-KI-System und fragt: Was muss gemeldet werden an wen und innerhalb welcher Fristen? Art. 72 bis 79 KI-VO Post-Market-Monitoring und… |
| `nicht-hochrisiko-bestaetigt-end-to-end-roadmap` | Prüfung hat ergeben: kein Hochrisiko. Unternehmen fragt: Welche KI-VO-Pflichten gelten trotzdem und wie dokumentieren wir das Negativ-Ergebnis rechtssicher? Drei Pfade Anhang I/III nicht zutreffend Rückausnahme Art. 6… |
| `output-betreiber-checkliste-und-folgenabschaetzung` | Betreiber von Hochrisiko-KI benoetigt fertige Compliance-Dokumentation für interne Zwecke oder Aufsichtsbehoerde. Art. 26 und 27 KI-VO Betreiber-Compliance-Output. Zwei Output-Dokumente: Betreiber-Compliance-Checkliste… |
| `output-konformitaetserklaerung-eu-anhang-v` | Anbieter benoetigt das fertige Musterdokument für die EU-Konformitätserklärung zum Ausfuellen und Unterzeichnen. Art. 47 i.V.m. Anhang V KI-VO EU-Konformitätserklärung. Pflichtinhalt Anhang V: eindeutige… |
| `output-pruefdokument-ki-vo-mit-warnhinweisen` | Abschlussvermerk mit Art.-3-Einordnung, Zweckbestimmung, Anhang-III-Matrix, Rückausnahme, Off-label-Governance und Re-Evaluation. |
| `persoenlicher-anwendungsbereich-rollen-art-3` | Erster Schritt der KI-VO-Prüfung: Wer ist betroffen? Unternehmen fragt welche Rolle es in der KI-VO einnimmt. Art. 3 KI-VO Rollendefinitionen. Prüfraster: Anbieter Art. 3 Nr. 3 Betreiber Art. 3 Nr. 4 Einführer Art. 3… |
| `risikoklassen-uebersicht-und-triage` | Schnelle Risikoklassen-Erstdiagnose mit Schwerpunkt Art. 6 Abs. 2/Anhang III, GPAI/Chatbot und Zweckbestimmung. |
| `rolle-anbieter-pruefen-art-3-nr-3` | Unternehmen das Software oder KI entwickelt fragt: Sind wir Anbieter im Sinne der KI-VO und welche Pflichten treffen uns deshalb? Art. 3 Nr. 3 KI-VO Anbieter-Definition. Prüfraster: Entwicklung oder Beauftragung… |
| `rolle-betreiber-pruefen-art-3-nr-4` | Unternehmen kauft oder lizenziert ein KI-System von einem Anbieter und fragt: Sind wir Betreiber im Sinne der KI-VO und was muessen wir tun? Art. 3 Nr. 4 KI-VO Betreiber-Definition. Prüfraster: Verwendung in eigener… |
| `rueckausnahme-art-6-abs-3` | Art. 6 Abs. 3: Profiling-Sperre, vier Fallgruppen, Grundrechtsrisiko und Dokumentation nach Art. 6 Abs. 4. |
| `sachlicher-ausschluss-art-2-abs-3-bis-12` | Unternehmen fragt: Faellt unser KI-System möglicherweise voellig aus dem Anwendungsbereich der KI-VO heraus? Art. 2 Abs. 3 bis 12 KI-VO sachliche Ausnahmen. Prüfraster: Militaer und nationale Sicherheit Art. 2 Abs. 3… |
| `sanktionen-art-99-bis-101` | Unternehmen moechte die Kostenrisiken einer KI-VO-Verletzung einschaetzen oder Vorstand über Bußgelddimensionen informieren. Art. 99 bis 101 KI-VO Sanktionen. Prüfraster: bis 35 Mio EUR oder 7 Prozent Konzernumsatz bei… |
| `territorialer-anwendungsbereich-art-2` | Nicht-EU-Unternehmen oder Exporteur fragt: Gilt die KI-VO auch für uns obwohl wir außerhalb der EU sind? Art. 2 KI-VO territorialer Anwendungsbereich. Prüfraster: Inverkehrbringen in der EU Nutzung in der EU durch… |
| `triage-ki-vo-vorpruefung` | Nutzer kommt mit unklarer KI-VO-Frage oder möglicherweise betroffener Software und fragt: Wie starte ich die KI-VO-Prüfung? Eingangs-Triage-Skill. Prüfraster: Erfassung ob eigene Softwareentwicklung fremder Dienst… |
| `verbotene-praktiken-art-5` | Unternehmen prüft ob ein KI-Einsatz in den Bereich der absolut verbotenen KI-Praktiken faellt. Art. 5 KI-VO Verbotskatalog. Prüfraster: alle acht verbotenen Praktiken subliminale Techniken Vulnerabilitaetsausnutzung… |
| `verhaeltnis-zu-anderen-unionsrechtsakten` | Anwalt oder Compliance-Beauftragter fragt: Gilt neben der KI-VO noch ein anderes EU-Gesetz für das gleiche System und wie interagieren die Pflichten? Art. 2 Abs. 2 KI-VO Verhältnis zu anderen Rechtsakten. Prüfraster:… |
| `zeitlicher-geltungsbereich-uebergangsfristen` | Compliance-Beauftragter oder Unternehmen fragt: Ab wann muessen welche KI-VO-Pflichten eingehalten werden und welche Systeme sind schon heute betroffen? KI-VO Übergangsfristen und Zeitplan. Prüfraster: Inkrafttreten 1.… |

## Worum geht es?

Der KI-VO-AI-Act-Pruefer fuehrt Unternehmen, Kanzleien und Compliance-Beauftragte durch die vollstaendige Pruefung nach der EU-Verordnung 2024/1689 (EU AI Act / KI-VO). Er deckt alle Pruefschritte ab: ob eine Software ueberhaupt ein KI-System ist, welche Risikoklasse zutrifft, welche Rolle das Unternehmen einnimmt (Anbieter, Betreiber, Importeur, Haendler), ob verbotene Praktiken vorliegen, wie die Hochrisiko-Einstufung gehandhabt wird und wie der Weg bis zur CE-Kennzeichnung aussieht.

Zusaetzlich behandelt das Plugin General-Purpose-AI (GPAI)-Modelle, die Ausnahmen vom Hochrisiko nach Art. 6 Abs. 3, das Verhaeltnis zu anderen EU-Rechtsakten, Sanktionen sowie die laufende Marktbeobachtung nach Inverkehrbringen.

## Wann brauchen Sie diese Skill?

- Ein Unternehmen fragt, ob die eigene Software unter die KI-VO faellt und welche Pflichten daraus folgen.
- Ein Anbieter von KI hat die Hochrisiko-Einstufung erhalten und braucht eine vollstaendige Roadmap bis zur CE-Kennzeichnung.
- Ein Betreiber kauft ein KI-System ein und muss seine Betreiberpflichten nach Art. 26 KI-VO kennen.
- Ein Anbieter von GPAI-Modellen (Sprachmodelle, Basismodelle) fragt, ob er unter die GPAI-Pflichten faellt und ob systemisches Risiko vorliegt.
- Compliance-Beauftragter will wissen, welche Sanktionen bei Verstoessen drohen und wie Verfahren ablaufen.

## Fachbegriffe (kurz erklaert)

- **KI-System** — Maschinenbasiertes System nach Art. 3 Nr. 1 KI-VO: inferenzbasiert, Ausgaben erzeugt, die Entscheidungen beeinflussen koennen.
- **Anbieter** — Entwickler oder Vermarkter eines KI-Systems, der es in den Verkehr bringt (Art. 3 Nr. 3 KI-VO).
- **Betreiber** — Unternehmen oder Behoerde, die ein KI-System unter eigener Verantwortung einsetzt (Art. 3 Nr. 4 KI-VO).
- **Hochrisiko-KI** — KI-System in sensiblen Anwendungsbereichen nach Art. 6 Abs. 2 i. V. m. Anhang III KI-VO oder als Sicherheitsbauteil eines regulierten Produkts.
- **GPAI** — General-Purpose-AI-Modell nach Art. 3 Nr. 63 KI-VO; Basismodell mit Allzweck-Faehigkeiten; eigene Pflichtenkategorie.
- **Systemisches Risiko** — Erhebliche Risiken bei GPAI-Modellen mit mehr als 10 hoch 25 FLOP Trainingsaufwand (Art. 51 KI-VO).
- **Konformitaetsbewertung** — Verfahren nach Art. 43 ff. KI-VO zur CE-Kennzeichnung von Hochrisiko-KI.
- **EU-KI-Datenbank** — Oeffentliches Register nach Art. 71 KI-VO, in dem Hochrisiko-KI-Systeme registriert werden muessen.

## Rechtsgrundlagen

- Art. 1-3 KI-VO EU 2024/1689 (Anwendungsbereich, Begriffsbestimmungen)
- Art. 5 KI-VO (Verbotene Praktiken)
- Art. 6 und Anhang I und III KI-VO (Hochrisiko-Einstufung)
- Art. 9-15 KI-VO (Pflichten Anbieter Hochrisiko: Risikomanagement, Daten, Transparenz, Aufsicht)
- Art. 22-26 KI-VO (Pflichten Bevollmaechtigter, Importeur, Haendler, Betreiber)
- Art. 43-49 KI-VO (Konformitaetsbewertung, EU-Konformitaetserklaerung, EU-Datenbank)
- Art. 51-55 KI-VO (GPAI-Pflichten, systemisches Risiko)
- Art. 70-79 KI-VO (Governance, Aufsichtsbehoerden, Marktbeobachtung)
- Art. 99-101 KI-VO (Sanktionen)

## Schritt-fuer-Schritt: Einstieg ins Plugin

1. Vorpruefung: Liegt ueberhaupt ein KI-System vor? (`liegt-ki-system-vor-art-3-nr-1`)
2. Territorialen und sachlichen Anwendungsbereich pruefen (`territorialer-anwendungsbereich-art-2`, `sachlicher-ausschluss-art-2-abs-3-bis-12`).
3. Rolle bestimmen: Anbieter, Betreiber, Importeur oder Haendler? (`persoenlicher-anwendungsbereich-rollen-art-3`)
4. Risikoklasse bestimmen: Verboten, Hochrisiko, begrenztes Risiko oder GPAI? (`risikoklassen-uebersicht-und-triage`)
5. Roadmap fuer die zutreffende Risikoklasse auswaehlen und durcharbeiten.

## Skill-Tour (was gibt es hier?)

- `triage-ki-vo-vorpruefung` — Einstieg in die KI-VO-Pruefung fuer unklare Faelle; Startpunkt des Gesamt-Workflows.
- `entscheidungsbaum-ki-vo-gesamt-workflow` — Vollstaendige KI-VO-Pruefung von Anfang bis Ende in einem strukturierten Entscheidungsbaum.
- `liegt-ki-system-vor-art-3-nr-1` — Erster Pruefschritt: Ist die eigene Software ueberhaupt ein KI-System nach Art. 3 Nr. 1 KI-VO?
- `abgrenzung-konventionelle-software-vs-ki-system` — Abgrenzung konventioneller Software vom KI-System-Begriff der KI-VO.
- `territorialer-anwendungsbereich-art-2` — Gilt die KI-VO auch fuer Nicht-EU-Unternehmen oder Exporte?
- `sachlicher-ausschluss-art-2-abs-3-bis-12` — Prueft ob das KI-System vollstaendig aus dem Anwendungsbereich faellt.
- `persoenlicher-anwendungsbereich-rollen-art-3` — Wer ist betroffen und welche Rolle nimmt das Unternehmen ein?
- `risikoklassen-uebersicht-und-triage` — Schnelle Ersteinschaetzung der Risikoklasse nach Art. 5, 6, 50, 51 KI-VO.
- `verbotene-praktiken-art-5` — Prueft ob ein KI-Einsatz in den Bereich absolut verbotener KI-Praktiken faellt.
- `falsche-wiese-warnung-ki-vo` — Warnt vor Verwechslungen mit DSGVO, Produkthaftung oder MDR bei KI-VO-Fragen.
- `rolle-anbieter-pruefen-art-3-nr-3` — Prueft ob das Unternehmen als Anbieter im Sinne der KI-VO einzustufen ist.
- `rolle-betreiber-pruefen-art-3-nr-4` — Prueft ob das Unternehmen als Betreiber im Sinne der KI-VO einzustufen ist.
- `anbieter-werden-art-25` — Prueft unter welchen Bedingungen Betreiber, Importeur oder Haendler selbst zum Anbieter werden.
- `hochrisiko-zuordnung-art-6-und-anhang-i-iii` — Gesamtuebersicht der Hochrisiko-Zuordnungsregeln vor der Detailpruefung.
- `hochrisiko-art-6-abs-1-sicherheitsbauteil` — KI als Sicherheitsbauteil eines regulierten Produkts nach Art. 6 Abs. 1 KI-VO.
- `hochrisiko-art-6-abs-2-anhang-iii` — KI in einem der acht sensiblen Anwendungsbereiche nach Anhang III KI-VO.
- `rueckausnahme-art-6-abs-3` — Ausnahmen vom Hochrisiko trotz Anhang-III-Relevanz nach Art. 6 Abs. 3 KI-VO.
- `hochrisiko-bestaetigt-end-to-end-roadmap` — Vollstaendige Roadmap nach bestaetiger Hochrisiko-Einstufung bis CE-Kennzeichnung.
- `hochrisiko-risikomanagementsystem-art-9` — KI-VO-konformes Risikomanagementsystem aufsetzen (Art. 9 KI-VO).
- `hochrisiko-datenqualitaet-und-data-governance-art-10` — Anforderungen an Trainings-, Validierungs- und Testdaten (Art. 10 KI-VO).
- `hochrisiko-technische-dokumentation-art-11-und-anhang-iv` — Inhalt und Aktualitaet der technischen Dokumentation (Art. 11 und Anhang IV KI-VO).
- `hochrisiko-aufzeichnungspflichten-logging-art-12` — Automatische Aufzeichnungspflichten und Aufbewahrungsfristen (Art. 12 KI-VO).
- `hochrisiko-transparenz-und-informationen-fuer-betreiber-art-13` — Informationen in der Gebrauchsanweisung fuer Betreiber (Art. 13 KI-VO).
- `hochrisiko-menschliche-aufsicht-art-14` — Anforderungen an wirksame menschliche Aufsicht ueber Hochrisiko-KI (Art. 14 KI-VO).
- `hochrisiko-genauigkeit-robustheit-cybersicherheit-art-15` — Leistungsstandards fuer Genauigkeit, Robustheit und Cybersicherheit (Art. 15 KI-VO).
- `hochrisiko-konformitaetsbewertung-art-43-bis-49` — Konformitaetsbewertungsverfahren und Einbindung benannter Stellen (Art. 43-49 KI-VO).
- `eu-datenbank-registrierung-art-49-und-71` — Registrierungspflicht in der EU-KI-Datenbank fuer Anbieter und Betreiber.
- `nicht-hochrisiko-bestaetigt-end-to-end-roadmap` — KI-VO-Pflichten und Dokumentation fuer nicht-hochrisiko-eingestufte Systeme.
- `begrenztes-risiko-art-50-transparenzpflichten` — Transparenzpflichten fuer Chatbots, Deepfake-Tools und KI-Textgeneratoren (Art. 50 KI-VO).
- `gpai-vorliegen-art-3-nr-63` — Prueft ob ein KI-Modell ein GPAI-Modell nach Art. 3 Nr. 63 KI-VO ist.
- `gpai-modelle-art-51-bis-55` — GPAI-Pflichten: Verhaltenskodizes, technische Dokumentation, Transparenz (Art. 51-55 KI-VO).
- `gpai-systemisches-risiko-schwelle-10e25-flop` — Prueft ob die Schwelle fuer systemisches Risiko bei GPAI-Modellen ueberschritten ist.
- `bevollmaechtigter-und-produkthersteller-pflichten-art-22-und-25` — Pflichten des EU-Bevollmaechtigten und von Produktherstellern (Art. 22 und 25 KI-VO).
- `einfuehrer-importer-pflichten-art-23` — Sorgfaltspflichten des Importeurs von KI-Systemen aus Drittstaaten (Art. 23 KI-VO).
- `haendler-distributor-pflichten-art-24` — Sorgfaltspflichten des Distributeurs beim Weitervertrieb von Hochrisiko-KI (Art. 24 KI-VO).
- `betreiber-deployer-pflichten-art-26` — Betreiberpflichten beim Einsatz eingekaufter Hochrisiko-KI-Systeme (Art. 26 KI-VO).
- `code-of-practice-und-harmonisierte-normen` — Verhaltenskodizes und technische Normen fuer die KI-VO-Konformitaet nutzen.
- `governance-aufsichtsbehoerden-art-70` — Aufsichtsbehoerden in Deutschland und Europa fuer die KI-VO (Art. 70 KI-VO).
- `marktueberwachung-meldung-vorfaelle-art-72-bis-79` — Pflichten bei schwerwiegenden Vorfaellen und Marktbeobachtung nach Inverkehrbringen (Art. 72-79 KI-VO).
- `sanktionen-art-99-bis-101` — Bussgelddimensionen und Sanktionsrahmen der KI-VO (Art. 99-101 KI-VO).
- `verhaeltnis-zu-anderen-unionsrechtsakten` — Abgrenzung und Zusammenspiel der KI-VO mit DSGVO, MDR, Maschinenverordnung und anderen EU-Rechtsakten.
- `zeitlicher-geltungsbereich-uebergangsfristen` — Uebergangsfristen und zeitlicher Geltungsbeginn je Pflichtenkategorie der KI-VO.
- `output-pruefdokument-ki-vo-mit-warnhinweisen` — Abschliessendes Pruefdokument mit allen Ergebnissen und Warnhinweisen erstellen.
- `output-konformitaetserklaerung-eu-anhang-v` — Muster der EU-Konformitaetserklaerung zum Ausfuellen und Unterzeichnen (Anhang V KI-VO).
- `output-betreiber-checkliste-und-folgenabschaetzung` — Fertige Betreiber-Compliance-Dokumentation und Folgenabschaetzung erstellen.
- `mandatsabbruch-empfehlung-komplexe-faelle` — Erkennung von Faellen, die anwaltliche Spezialkenntnisse erfordern, und Eskalationsempfehlung.

## Worauf besonders achten

- KI-VO hat gestaffelte Uebergangsfristen: Verbotene Praktiken ab 02.02.2025, GPAI ab 02.08.2025, Hochrisiko-Systeme ab 02.08.2026 — Pflichten abfragen, die zum Stichtag gelten.
- Hochrisiko-Einstufung hat zwei Wege: Sicherheitsbauteil (Art. 6 Abs. 1) und Anhang-III-Bereiche (Art. 6 Abs. 2) — beide getrennt pruefen.
- Anbieter-Werden-Risiko: Betreiber, die ein System wesentlich veraendern, werden automatisch Anbieter mit vollen Anbieter-Pflichten.
- GPAI und KI-System-Schnittstelle: Ein GPAI-Modell kann in einem Hochrisiko-System eingebettet sein — dann kumulieren Pflichten.
- EU-Datenbank-Registrierung vor Inverkehrbringen: Zustimmung der Notifizierungsbehoerde abwarten.

## Typische Fehler

- Konventionelle regelbasierte Software irrtuemlicherweise als KI-System eingestuft: Abgrenzungspruefung fehlt.
- Hochrisiko-Rueckausnahme nach Art. 6 Abs. 3 uebersehen: System faellt in Anhang III, aber Rueckausnahme greift.
- Technische Dokumentation als einmaliges Dokument behandelt: KI-VO verlangt laufende Aktualisierung bei wesentlichen Aenderungen.
- GPAI-Pflichten mit Hochrisiko-Pflichten verwechselt: Verschiedene Regelungsregimes mit unterschiedlichen Anforderungen.
- Sanktionsdimensionen unterschaetzt: Bussgelder bis zu 35 Millionen Euro oder 7 Prozent des weltweiten Jahresumsatzes moeglich.

## Querverweise

- `datenschutzrecht` — DSGVO-Anforderungen ueberschneiden sich bei KI-Systemen mit Personendaten (Art. 9 und 22 DSGVO).
- `corporate-kanzlei` — KI-Governance und Berufsrecht in der Corporate-Kanzlei; KI-Einsatz im M&A-Kontext.
- `regulatorisches-recht` — Sektorspezifische Anforderungen fuer KI in Finanz- und Energiemarkt.
- `legistik-werkstatt` — KI-VO als EU-Verordnung im Kontext der nationalen Umsetzungsgesetzgebung.

## Quellen und Aktualitaet

- Stand: 05/2026
- EU KI-VO (EU 2024/1689) in der zum Stand-Datum geltenden Fassung
- Uebergangsfristen gemaess Art. 113 KI-VO
- GPAI Code of Practice der EU-KI-Buero (erste Fassung 2025)
