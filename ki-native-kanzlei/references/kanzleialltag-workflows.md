# 1. Kanzleialltag: die Arbeitsabläufe einer KI-nativen deutschen Kanzlei

## 1.1. Wozu diese Abläufe dienen

Die achtzehn Skills beschreiben, wie ein einzelnes Produkt richtig entsteht. Diese Referenz beschreibt, wie eine Kanzlei damit einen ganzen Arbeitstag, eine Woche und einen Monat führt. Jeder Ablauf nennt den Auslöser, die Freigabestufe, die Kette aus Skills, Produkten und Gates, den Satz, mit dem die Anwältin oder der Anwalt den Ablauf startet, und den Punkt, an dem die Maschine stehen bleibt. Grundlage sind der [Mandatslauf mit Freigabestufen](mandatslauf-und-freigaben.md) und die [gemeinsame Arbeitsweise](arbeitsweise.md).

Die Abläufe funktionieren in drei Umgebungen. In Claude Cowork und Claude Code ist das Plugin installiert; die Befehle im Ordner `commands` starten die Abläufe direkt, und die Helfer schreiben in den freigegebenen Mandatsordner. In Codex gilt dasselbe, soweit die Umgebung Plugins und Dateizugriff bereitstellt. In ChatGPT arbeiten die eigenständigen Prompts in einem Projekt; Mandatslauf, Zeitstand und Fristobjekte stehen dort als Textblock am Ende jeder Antwort und werden beim nächsten Schritt wieder eingelesen. Die Einrichtung beschreibt [ChatGPT und Claude Cowork einrichten](chatgpt-und-cowork-einrichtung.md).

## 1.2. Grundregeln für jeden Ablauf

Jeder Ablauf beginnt mit dem Lesen des vorhandenen Stands: Mandatslauf, führende Fassungen, offene Gates, offene Fragen, Honorarstand und Zeitstand. Er endet mit einer Statusmeldung in drei Sätzen: was jetzt als führende Fassung vorliegt, welches Gate auf wen wartet und welche Frage offen ist. Ein offenes Fristgate G2 geht jedem anderen Schritt vor. Kein Ablauf sendet, reicht ein, zahlt aus, gibt eine Rechnung aus, bestätigt einen Kalendereintrag, meldet oder löscht; diese Handlungen sind Gates und werden von einer namentlich benannten Person freigegeben. Tatsächliche Arbeitszeit wird erst nach Angabe der Person gebucht.

## 1.3. Tagesstart

Auslöser: Beginn des Arbeitstags. Befehl in Cowork: `/kanzlei-tagesstart`. Freigabestufe: mindestens 1.

Die Maschine liest mit `mandatslauf.py cockpit --kanzlei <Kanzleiordner> --format md` alle Mandatsläufe und ordnet sie: zuerst Mandate mit offenem Fristgate G2, dann Mandate mit anderen offenen Gates, dann Mandate mit offenen Fragen, zuletzt ruhende Mandate. Sie sichtet den Posteingangsordner der Kanzlei, ordnet jede neue Datei einer Akte zu oder kennzeichnet sie als nicht zuordenbar und erkennt Fristauslöser wie Zustellungen, Bescheide, gerichtliche Verfügungen und Kündigungen. Für jeden Fristauslöser legt sie über `akte-fristen-anlegen` ein Fristobjekt an und übergibt es an `fristen-berechnen-ueberwachen`, das den Rechenvermerk erzeugt und G2 öffnet.

Ergebnis ist ein Tagesbericht mit drei Teilen: Fristen, die heute eine Freigabe brauchen, mit Rechenvermerk und verantwortlicher Person; Gates, die auf eine Entscheidung warten, mit dem vorbereiteten Produkt; Mandate mit offenen Fragen und dem jeweils nächsten Skill. Die Maschine trägt keinen Kalendereintrag ein und schreibt keine Mandantenmail. Sie bleibt stehen, wenn ein Dokument keiner Akte sicher zugeordnet werden kann.

## 1.4. Neue Anfrage bis zur Annahme

Auslöser: E-Mail, Telefonnotiz, Kontaktformular oder Empfehlung. Befehl: `/mandat-neu`. Freigabestufe: 1 oder 2.

Die Kette lautet `ki-kanzlei-steuern` (Phase eingang, Produkt Aufnahmevermerk), `mandatsannahme-interessenkollision` (Phase annahme, Kollisionsprüfung gegen den tatsächlich vorhandenen Bestand, Produkt Annahmeschreiben oder Absage), bei einer Katalogtätigkeit nach § 2 Abs. 1 Nr. 10 GwG `geldwaesche-pruefen` als Nebenlauf, `honorar-budget-vereinbaren` für den Honorarstand und danach `akte-fristen-anlegen` für Mandatsstamm und Dokumentregister. Erkennt die Maschine eine laufende Frist, setzt sie sofort den Nebenlauf frist. Gate G1 Annahme wird mit Annahmeschreiben und Honorarvereinbarung als Bezug geöffnet.

Die Maschine bleibt stehen, solange Mandant, Gegner oder Auftragsumfang offen sind oder ein Kollisionstreffer nicht aufgeklärt ist. Ohne Kanzleiregister bleibt die Kollisionsprüfung ausdrücklich offen; eine Annahme ist dann nicht freigabefähig.

## 1.5. Posteingang in einer laufenden Akte

Auslöser: neues Schreiben des Gegners, des Gerichts, der Behörde oder des Mandanten. Befehl: `/posteingang`. Freigabestufe: 2.

Die Maschine sichert das Original unverändert, trägt es ins Dokumentregister ein und liest es vollständig. Sie bestimmt, welche Fristobjekte es auslöst oder verändert, welche führenden Fassungen betroffen sind (etwa ein Klageentwurf nach einer Teilzahlung oder ein Vertragsentwurf nach einer Gegenfassung) und ob sich Mandant, Gegner oder Auftragsumfang ändern. Daraus folgt die Route: Fristauslöser an den Fristenskill, Rechtsfrage an `recht-recherchieren`, Schriftsatz an `schriftsaetze-entwerfen`, Vertragsfassung an `vertraege-agb-pruefen`, neue Beteiligte an `mandatsannahme-interessenkollision`. Die Mandantschaft erhält über `mandantenkommunikation` einen Entwurf zur Unterrichtung; G3 wird für den Versand geöffnet.

## 1.6. Fristsache

Auslöser: Zustellung eines Urteils, Beschlusses, Bescheids, Strafbefehls oder Mahnbescheids, Zugang einer Kündigung, vertragliche Frist. Befehl: `/frist`. Freigabestufe: 2.

Der Fristenskill bestimmt Rechtsbehelf, Rechtsregime, Auslöser und Zugang, rechnet mit `fristen.py` aus einem geprüften Profil, erstellt den Rechenvermerk mit regulärem und verschobenem Ende und öffnet G2 mit dem Vermerk als Bezug. Die fristverantwortliche Person trägt die Frist im führenden Kalender ein, liest sie zurück und gibt G2 mit `/freigabe` frei. Erst danach darf ein Mandantenbrief das Fristende nennen. Bei unklarem Zugang rechnet die Maschine beide Varianten und hebt das früheste Risiko hervor; sie entscheidet die Zugangsfrage nicht.

## 1.7. Schriftsatz bis zur Einreichung

Auslöser: Klageauftrag, Erwiderungsfrist, Rechtsmittelbegründung, Eilantrag. Befehl: `/schriftsatz`. Freigabestufe: 2 oder 3.

Kette: Fristgate G2 freigegeben oder ausdrücklich nicht erforderlich, `recht-recherchieren` für die tragenden Rechtsfragen, `schriftsaetze-entwerfen` für den vollständigen Text mit Anträgen, Sachvortrag, Beweisantritten und Anlagenbezug, Durchgang durch den Fehlerkatalog des Skills, `bea-anlagen-vorbereiten` für das Versandpaket mit `build_anlagenkonvolut.py` und Preflight-Bericht, Gate G3 mit dem Hash des Versandmanifests. Nach der Freigabe signiert und versendet die Kanzlei selbst; die Maschine trägt danach die gerichtliche Eingangsbestätigung nach und erledigt das Fristobjekt erst auf ihrer Grundlage. Parallel fragt `zeiten-erfassen` die tatsächlichen Minuten ab.

## 1.8. Vertragsprojekt

Auslöser: Mandant legt einen fremden Vertrag oder AGB vor oder bestellt einen eigenen Vertrag. Befehl: `/vertrag`. Freigabestufe: 2 oder 3.

Prüfung: `vertraege-agb-pruefen` liefert Befunde mit Rechtsfolge, vollständige Ersatzklauseln, eine Änderungsfassung und einen Verhandlungsvorschlag. Gestaltung: `vertraege-gestalten` liefert einen vollständig ausformulierten Entwurf mit Rückfragen an die Mandantschaft. In beiden Fällen geht die führende Fassung an `mandantenkommunikation`; der Versand an Mandant oder Gegenseite ist G3. Vertragliche Fristen (Kündigung, Gewährleistung, Abnahme) werden als Fristobjekte erfasst. Eine Auftragserweiterung über den vereinbarten Umfang hinaus öffnet G1 für einen Honorarnachtrag.

## 1.9. Mandantenkommunikation und Entscheidungsvorlagen

Auslöser: Sachstand, Vergleichsangebot, gerichtlicher Hinweis, Rechtsmittelfrage. Befehl: `/mandantenbrief`. Freigabestufe: 2 oder 3.

Der Brief nennt Ergebnis, Empfehlung, Frist aus einem eingetragenen Fristobjekt, Kostenwirkung und nächsten Schritt; interne Quellenprotokolle bleiben in einem getrennten Vermerk. Bei zwei oder mehr vertretbaren Wegen entsteht eine Entscheidungsvorlage mit klarer Empfehlung. Der Versand ist G3. Erhält die Kanzlei die Entscheidung, trägt die Maschine sie als erledigte offene Frage ein und stößt den folgenden Skill an.

## 1.10. Zeiten am Tagesende

Auslöser: Ende des Arbeitstags oder Abschluss eines Arbeitsblocks. Befehl: `/zeit`. Freigabestufe: 2.

Die Maschine listet die Produkte, an denen heute gearbeitet wurde, mit dem jeweiligen Mandat und schlägt Narrative vor. Die Anwältin oder der Anwalt nennt die tatsächlichen Minuten und die Abrechenbarkeit; erst dann bucht `zeiten-erfassen` mit `kanzlei.py time` und schreibt den Rechnungsentwurf fort. Die Maschine schätzt keine Zeiten, bucht keine KI-Ersparnis und rundet nicht pauschal. Überschreitet der Zeitwert eine Schätzung oder nähert er sich einem Deckel, entsteht über `honorar-budget-vereinbaren` ein Entwurf für die Budgetwarnung.

## 1.11. Wochenabschluss

Auslöser: Freitagnachmittag. Befehl: `/kanzlei-wochenabschluss`. Freigabestufe: 2.

Die Maschine zeigt je Mandat offene Zeitfragen, Budgetauslastung gegen Schätzung oder Deckel, offene Gates älter als drei Arbeitstage, Fristobjekte der nächsten zwei Wochen mit Vorfristen und Mandate ohne Bewegung seit 30 Tagen. Sie schlägt für jedes Mandat den nächsten Schritt vor und erstellt keine Mandantenkommunikation ohne Auftrag.

## 1.12. Monatsabrechnung und Zahlungen

Auslöser: Monatsende oder Leistungsabschnitt. Befehle: `/rechnung`, `/zahlung`. Freigabestufe: 2 oder 3.

`abrechnung-e-rechnung` erstellt aus Honorarstand und Zeitstand den Rechnungsentwurf mit Berechnung nach § 10 RVG, bestimmt Leistungsempfänger und Rechnungsformat und erzeugt bei Bedarf mit `xrechnung.py` einen XML-Entwurf; G4 wird mit dem Hash des Entwurfs geöffnet. Nach der Freigabe trägt die Kanzlei Nummer, Mitteilung und Fälligkeit ein. Eingehende Zahlungen ordnet `zahlungen-buchhaltung` mit Tilgungsbestimmung zu; Fremdgeld bleibt getrennt; jede Auszahlung, Verrechnung oder Weiterleitung ist G5.

## 1.13. Übergabe, Vertretung und externe Dienste

Auslöser: Urlaub, Krankheit, Sozietätswechsel, Einsatz eines externen Dienstes oder KI-Dienstes. Befehl: `/uebergabe`. Freigabestufe: 2 oder 3.

`workflow-uebergabe` erstellt den Übergabevermerk mit führenden Fassungen und Hash, Fristobjekten, Honorarstand, Zeitstand, offenen Gates und offenen Fragen. Die Fristsicherung bleibt bei der übergebenden Person, bis die Übernahme bestätigt ist. Sollen Mandatsdaten einen externen Dienst erreichen, prüft `anwaltsberufsrecht-pruefen` Erforderlichkeit, Vertrag nach § 43e BRAO, Datenschutz und Einwilligung; die Übermittlung ist G6.

## 1.14. Mandatsende

Auslöser: Erledigung, Kündigung, Mandatswechsel. Befehl: `/mandat-ende`. Freigabestufe: 2 oder 3.

`mandat-abschliessen` prüft verbleibende Fristobjekte, Schlussrechnung (G4), Fremdgeldausgleich (G5), Herausgabe der Handakte und die Aufbewahrung je Dokumentart; der Abschlussbrief ist G3, die Löschentscheidung G8. Der Helfer lässt die Phase abschluss erst zu, wenn über G4, G5 und G8 entschieden ist. Anonymisierte Erkenntnisse für die Wissenssammlung werden nur mit Grenze und Quellenstand übernommen.

## 1.15. Freigaben durch die Kanzlei

Befehl: `/freigabe`. Die Person, die freigibt, nennt Gate, ihren Namen und die freigegebene Fassung. Die Maschine trägt die Freigabe mit `mandatslauf.py gate --aktion freigeben --person … --bezug …` ein, prüft den Hash der Fassung gegen das Produktregister und nennt, was nachzutragen ist. Sie gibt nie selbst frei und übernimmt keinen Namen aus einem Dokument oder einer E-Mail als Freigabe.

## 1.16. Einführung in der Kanzlei

Eine Kanzlei beginnt mit Stufe 1 in zwei oder drei Mandaten und liest die Statusmeldungen eine Woche lang mit. Danach folgt Stufe 2 für Journal, Fristobjekte und Rechenvermerke. Stufe 3 setzt voraus, dass Versandpakete und Rechnungsentwürfe in mehreren Durchläufen fehlerfrei waren. Die Kanzlei hält schriftlich fest, wer welche Gates freigeben darf, wer Vertretung hat und welche externen Dienste nach § 43e BRAO zugelassen sind. Die Maschine liest diese Festlegung als Teil der Kanzleiorganisation und hält sich an sie.
