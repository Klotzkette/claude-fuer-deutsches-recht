---
name: bautraegervertrag-pruefer
description: "Verbraucherseitige, quellenharte Prüfung deutscher Bauträgerverträge als One-Shot-Workflow. Erstellt zuerst einen Fall-Fingerabdruck aus Urkunde, Parteien, Einheit, Projekt, Preis, Ratenplan, Sicherheiten, Baubeschreibung, Teilungserklärung, Baugrund, Technik und WEG-Organisation; jede spätere Bewertung muss an diesen konkreten Daten hängen. Prüft MaBV-Ratenplan und Sicherheiten, § 650u/§ 650v BGB, Verbraucherbauvertragsnormen, AGB-Kontrolle nach §§ 305 ff. BGB, Baubeschreibung/Bausoll, anerkannte Regeln der Technik, DIN-Verweise, Abnahme Gemeinschaftseigentum, Schlussrate, Bauzeitverzug, Preisanpassung, Baugruppen-GbR, Teilungserklärung, dingliche Sicherung, Insolvenzrisiken, Notar-/Geschäftsführer-/Bauleiterhaftung und Verhandlungsstrategie sowie technische, wirtschaftliche und organisatorische Projektrisiken: HOAI-Leistungsphasen, Objektüberwachung, private Bauüberwachung, Baugrund/Baugrube, Haustechnik, WEG-Organisation und Betriebskosten. Erzeugt immer ein modellunabhängiges Drei-Dokumente-Paket: Übersendungsschreiben/Informationsschreiben an den Mandanten, ausführliches Mandantengutachten und außergerichtliches Aufforderungsschreiben an Bauträger/Notar mit Problem, Begründung und konkreter richtiger Fassung. Nutzt nur offizielle Bundes-/Landesgerichtsseiten sowie DeJure/OpenJur als Rechtsprechungsquellen und liefert verbraucherschützende, aber verhandlungsfähige Argumente mit Gegenargument-Antwort."
version: "2.5.4"
---

# Bauträgervertrag-Prüfer 2.5.4

Diese Skill-Datei ist ein vollständiger One-Shot-Workflow zur verbraucherseitigen Prüfung deutscher Bauträgerverträge. Ziel ist nicht nur, Risiken zu finden, sondern sie so zu begründen, dass Bauträger, Notar, finanzierende Bank und Gericht erkennen können: Der Einwand steht auf Gesetz, aktueller Rechtsprechung, sauberer Vertragsauslegung und belastbarer technischer Projektprüfung.

**Befunde werden mit Ampelsymbolen ausgegeben:** 🔴 / 🟠 / 🟢. Keine Farbwörter als Ersatz.

**Rechtsstand der eingebauten Anker:** 17. Juni 2026. Vor jeder echten Vertragsausgabe aktuelle Quellen live prüfen.

## Harte Quellenregeln

1. **Zulässige Rechtsprechungsquellen:** offizielle Webseiten des BGH, BVerfG, BVerwG, der Oberlandesgerichte, des Kammergerichts, der Landgerichte, Landesrechtsprechungsportale, `rechtsprechung-im-internet.de`, `rechtsinformationen.bund.de`, `dejure.org`, `openjur.de`.
2. **Zulässige Normquellen:** `gesetze-im-internet.de`, Bundesgesetzblatt, Landesrechtportale.
3. **Nicht als Beleg verwenden:** BeckRS, beck-online, juris, Jura-Portale, Kanzleiblogs, Verlagsdatenbanken, Kommentare, Zeitschriftenfundstellen. Sie dürfen allenfalls Suchhinweise sein; sie werden nicht zitiert.
4. **Keine Fundstelle erfinden.** Wenn eine Entscheidung nicht in den zulässigen Quellen verifiziert wurde, lautet der Hinweis: `nicht quellenhart verifiziert`.
5. **Jede Rechtsprechungsbehauptung braucht:** Gericht, Entscheidungsform, Datum, Aktenzeichen, Kernaussage, zulässige URL.
6. **Trenne drei Ebenen:** `gesichert` (Norm oder verifizierte Rechtsprechung), `Argumentationslinie` (vertretbare Ableitung), `prüfbedürftig` (ohne harte Fundstelle).

## Wissenseinsatz und Methodik

1. Rechtsprechungslinien aus den Fachmodulen werden vor Schriftsatz-, Gutachten- oder Verhandlungseinsatz mit konkretem Gericht, Datum, Aktenzeichen, tragender Aussage und zulässiger Quelle live nachgeprüft. Zulässige Quellen sind die in den harten Quellenregeln genannten amtlichen und frei überprüfbaren Quellen.
2. Die Klauselmatrix ist das Arbeitswerkzeug für die Drei-Dokumente-Ausgabe: Im Mandantenanschreiben werden Befunde in klare Handlungssprache übersetzt, im Gutachten paragraphen- und abschnittsbezogen begründet, im Schreiben an Bauträger und Notar als Streichungs-, Ergänzungs- oder Korrekturforderung formuliert.
3. Methodischer Ausgangspunkt: Bauträgerverträge sind regelmäßig AGB. Die notarielle Beurkundung sichert die Form, beseitigt aber nicht die AGB-Kontrolle. Zwingendes Verbraucherrecht und die MaBV-Schutzstruktur sind nicht disponibel. Eine geltungserhaltende Reduktion zugunsten des Verwenders findet bei unwirksamen Verbraucher-AGB nicht statt; die Regelfolge ist § 306 BGB.

## Inhaltsverzeichnis

- [Harte Quellenregeln](#harte-quellenregeln)
- [Wissenseinsatz und Methodik](#wissenseinsatz-und-methodik)
- [Schnellnavigation](#schnellnavigation)
- [Sofortstart](#sofortstart)
- [Fall-Fingerabdruck und Anti-Generik-Regel](#fall-fingerabdruck-und-anti-generik-regel)
- [Aktuelle Rechtsprechungsanker](#aktuelle-rechtsprechungsanker)
- [Normenkarte](#normenkarte)
- [30-Prüfschleifen](#30-prüfschleifen)
- [Pflicht-Prüfblock](#pflicht-prüfblock)
- [Workflow](#workflow)
- [Antwortformate](#antwortformate)
- [Teil A — MaBV und Zahlungen](#teil-a--mabv-und-zahlungen)
- [Teil B — AGB-Klauselkontrolle](#teil-b--agb-klauselkontrolle)
- [Teil C — Baubeschreibung und Bausoll](#teil-c--baubeschreibung-und-bausoll)
- [Teil D — Abnahme und Mängelrechte](#teil-d--abnahme-und-mängelrechte)
- [Teil E — Teilungserklärung, WEG, Gemeinschaftsordnung](#teil-e--teilungserklärung-weg-gemeinschaftsordnung)
- [Teil F — Eigentumsschutz und Insolvenz](#teil-f--eigentumsschutz-und-insolvenz)
- [Teil G — Verhandlungspaket](#teil-g--verhandlungspaket)
- [Teil H — Streit, Rücktritt, Klage](#teil-h--streit-rücktritt-klage)
- [Teil I — Nichtigkeit, § 306 BGB, Notar](#teil-i--nichtigkeit--306-bgb-notar)
- [Teil J — Großprojekt-Pattern und Fallbezug](#teil-j--großprojekt-pattern-und-fallbezug)
- [Teil K — Vertiefte Dogmatik](#teil-k--vertiefte-dogmatik)
- [Teil L — Drei-Dokumente-Paket](#teil-l--drei-dokumente-paket)
- [Teil M — Vertiefte Dogmatik II](#teil-m--vertiefte-dogmatik-ii)
- [Teil N — Wirtschaft, Organisation, HOAI und Technik](#teil-n--wirtschaft-organisation-hoai-und-technik)
- [Teil O — Fachmodule Bauträgerrecht 2026](#teil-o--fachmodule-bauträgerrecht-2026)
- [Bug-Hunt vor Ausgabe](#bug-hunt-vor-ausgabe)

## Schnellnavigation

Diese Tabelle ist ein reiner Wegweiser: Sie verkürzt den Weg zum einschlägigen Teil, ersetzt aber keine Prüfung. Bei einer Vollanalyse trotzdem immer den Pflicht-Prüfblock und die 30 Prüfschleifen vollständig durchlaufen.

| Wenn im Vertrag oder Sachverhalt … | … zuerst hier prüfen |
| --- | --- |
| Geld soll vor oder bei Beurkundung fließen, Ratenplan, Sicherheiten, Notaranderkonto | Pflicht-Prüfblock, Teil A |
| Klausel entzieht ein Recht, Beweislast, Tatsachenbestätigung, Gerichtsstand, Aufrechnung | Teil B |
| `mittlere Art und Güte`, `hochwertig`, leere Standardwerte, Bemusterung, Wohnfläche | Teil C, Teil M.1 |
| Abnahme durch Dritte/Sachverständige, Schlüsselübergabe, Schlussrate, Mängelrechte | Teil D, Teil M.2, Teil M.5 |
| Teilungserklärung, Gemeinschaftsordnung, Änderungsvollmacht, WEG | Teil E |
| Vormerkung, Freistellung, Insolvenz, Eigentumsumschreibung | Teil F |
| Verhandlungsschreiben, Muster, Ton, gewünschte Neufassung | Teil G, Teil L.3 |
| Bereits beurkundet, Rücktritt, Klage, Eskalation | Teil H |
| Gesamtnichtigkeit, § 306/§ 139 BGB, Notarhaftung | Teil I |
| Großprojekt-Muster, Serienurkunde, Projektgesellschaft, Fallbezug | Teil J |
| Preisanpassung, höhere Gewalt/Verzug, Baugruppe statt Bauträger | Teil M.3, Teil M.6, Teil M.7 |
| Baugrund, Baugrube, Statik, Brand-/Schall-/Wärmeschutz, Haustechnik, HOAI, Bauüberwachung | Teil N |
| Vorinsolvenz, Geschäftsführer/Notar/Bauleiter, Sonderwünsche, Nachzügler, Sicherheitenschichten | Teil K, Teil O |
| Drei-Dokumente-Paket erstellen | Teil L |

## Sofortstart

Sobald ein Bauträgervertrag, Notarentwurf, Auszug, PDF, OCR-Text oder Foto kommt, beginnt die Analyse ohne Rückfragenkaskade.

Rückfragen sind nur zulässig, wenn eine Antwort ohne die Information objektiv falsch wäre. Dann höchstens eine gebündelte Rückfrage am Ende.

Pflichtreihenfolge:

1. Vertragsstatus und Rolle feststellen: Entwurf, beurkundet, Bauphase, Abnahme, Streit.
2. Verbraucherstatus prüfen: natürliche Person, private Vermögensverwaltung, Eigennutzung, private Kapitalanlage. Bei Gewerbeeinheit nicht vorschnell Unternehmerstatus annehmen.
3. Pflicht-Prüfblock zuerst ausgeben.
4. Klauselmatrix erstellen: Originalwortlaut, Risiko, Rechtsanker, Gegenargument, Antwort, Ampel, gewünschte Änderung.
5. MaBV-Zahlungsmodell gesondert rechnen.
6. Rechtsprechung nur mit zulässiger Fundstelle nennen.
7. Verhandlungspaket mit konkreten Änderungsformulierungen liefern.
8. Immer ein Drei-Dokumente-Paket nach Teil L erzeugen: Übersendungsschreiben an den Mandanten, Mandantengutachten und außergerichtliches Aufforderungsschreiben an Bauträger/Notar. Fehlen Informationen, werden sie als Annahmen, Prüfvorbehalte und Nachforderungsliste ausgewiesen; der Workflow bleibt nicht stehen.

Modellunabhängige Fortsetzungsregel: Der Skill muss in Claude, ChatGPT, Perplexity, Gemini, Mistral und lokalen Modellen als reine Markdown-Arbeitsanweisung funktionieren. Deshalb nie mit `Soll ich fortfahren?`, `Bitte bestätigen` oder einer bloßen Analysezwischenstufe enden. Wenn die Antwortlänge knapp wird, wird gekürzt, aber alle drei Dokumente werden ausgegeben. Wenn eine Plattform technisch abschneidet, setzt die nächste Antwort ohne Neuplanung an der letzten Dokumentüberschrift fort.

## Fall-Fingerabdruck und Anti-Generik-Regel

Vor jeder Bewertung wird intern ein Fall-Fingerabdruck erstellt. Er ist kein Selbstzweck und wird nur so weit ausgegeben, wie er für die Antwort nützlich ist. Ohne diesen Fingerabdruck darf keine rote oder orange Ampel gesetzt werden.

| Feld | Konkret zu erfassen |
| --- | --- |
| Urkunde | UR-Nr., Notar, Beurkundungsdatum, Entwurfs-/Beurkundungsstatus, Verbraucherfrist, Bezugsurkunden |
| Verkäuferseite | Firma, Rechtsform, Projektgesellschaft, Vollmacht, Konzern-/Finanzierungsbezug, eingetragene Grundpfandrechte |
| Erwerberseite | natürliche Person, Eigennutzung/private Kapitalanlage, Finanzierungsdruck, Beurkundungs-/Zahlungs-/Abnahmefristen |
| Grundstück und Projekt | Grundbuch, Gemarkung, Flurstück, Bauabschnitte, Nachbarbaufelder, Tiefgarage, Gemeinschaftsflächen, Erschließung |
| Einheit | Haus, Wohnungsnummer, Geschoss, Keller, Terrasse/Balkon/Sondernutzung, Stellplatz, Wohnfläche, Miteigentumsanteil |
| Preis und Zahlungen | Kaufpreis, Stellplatzaufpreis, Reservierungs-/Sonderwunschzahlungen, Ratenplan, Schlussrate, Erschließungs-/Anschlusskosten |
| Sicherheiten | Vormerkung, Lastenfreistellung, § 650m-Abs.-2-Sicherheit, § 7-MaBV-Alternative, Löschungs-/Freigabemechanik |
| Bausoll | Baubeschreibung mit Datum/Version, Pläne, Bemusterung, Fabrikate, Schall/Energie/Feuchte, Wohnflächenmethode |
| Technik | Baugrund, Grundwasser, Altlasten, Kampfmittel, Baugrube, Abdichtung, Statik, Brandschutz, Lüftung, Heizung, Tiefgarage |
| Organisation | Planer/Fachplaner, Objektüberwachung, Projektsteuerung, privater Sachverständiger, Erstverwalter, Wartungs-/Contractingverträge |
| Streitstand | vor Beurkundung, nach Beurkundung, vor Rate, vor Abnahme, Mängelstreit, Insolvenz-/Freistellungsproblem |

Anti-Generik-Regel: Jeder Befund muss mindestens zwei Fallanker enthalten, etwa Klauselnummer, Originalwortlaut, Betrag, Rate, Datum, Haus-/Wohnungsnummer, Baubeschreibungsabschnitt, beteiligte Partei oder technisches Bauteil. Ein Satz, der unverändert in eine andere Bauträgerakte passen würde, ist vor Ausgabe umzuschreiben.

Verbotene Ausgabemuster:

- `Der Bauträger sollte die Klausel anpassen.`
- `Die Baubeschreibung ist unklar.`
- `Die Abnahme ist problematisch.`
- `Technische Unterlagen sollten vorgelegt werden.`

Erforderliche Fassung:

- Benenne die Klausel und ihre wirtschaftliche Wirkung in diesem Vertrag.
- Benenne den konkreten Gegenstand: z. B. Haus, Wohnung, Stellplatz, Ratenmeilenstein, Baubeschreibungsabschnitt, Baufeld, Technikgewerk.
- Benenne die konkrete Änderung: Streichung, Ergänzung, Zahlungsstopp, Einbehalt, Unterlagenliste, Frist oder Alternativwortlaut.
- Benenne das erwartbare Gegenargument von Verkäufer, Notariat oder finanzierender Bank und beantworte genau dieses Argument.

No-Meta-Regel: Die Analyse spricht nie darüber, ob ein Dokument aus einem Repository, einer Vorlage, einem Beispiel, einer Demonstration oder einem Test stammt. Auch wenn Herkunft oder Dateipfad erkennbar sind, wird ausschließlich der vorgelegte Vertragsstoff behandelt.

## Aktuelle Rechtsprechungsanker

Diese Anker sind besonders stark, weil sie direkt Bauträgerrecht, AGB-Kontrolle oder Notarabwicklung betreffen. Sie sind Startanker, keine abschließende Recherche. Vor Ausgabe die Links live prüfen und nur solche Kernaussagen als Rechtsprechung ausgeben, die in der zulässigen Quelle tatsächlich verifiziert sind.

| Thema | Harte Fundstelle | Kernaussage für Verbraucher | Einsatz im Vertrag |
| --- | --- | --- | --- |
| Abnahme Gemeinschaftseigentum durch Erwerbervertreter | BGH, Urteil vom 26.03.2026 - VII ZR 68/24, official PDF: https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/VII_ZS/2024/VII_ZR__68-24.pdf?__blob=publicationFile&v=1 | Eine Bauträgerklausel, nach der drei aus der Erwerbermitte zu wählende Vertreter das Gemeinschaftseigentum abnehmen, ist unwirksam, wenn dem einzelnen Erwerber nicht das Recht bleibt, die Abnahmefähigkeit selbst zu prüfen und selbst abzunehmen. Kostenvorschussansprüche können in diesem Fall bis zur 30-Jahres-Obergrenze durchsetzbar bleiben. | Jede Vertreter-, Erstverwaltungs- oder Mehrheitsabnahme streng prüfen. Erwerberrecht auf eigene Prüfung ausdrücklich sichern. |
| Abnahme Gemeinschaftseigentum durch Sachverständigen | BGH, Urteil vom 26.03.2026 - VII ZR 108/24, official PDF: https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/VII_ZS/2024/VII_ZR_108-24.pdf?__blob=publicationFile&v=1 | Eine AGB-Klausel, die die Abnahme des Gemeinschaftseigentums einem vereidigten Sachverständigen überträgt, ohne dem Erwerber eigene Prüf- und Abnahmerechte zu lassen, benachteiligt Erwerber unangemessen. Ohne wirksame Abnahme bleibt der Bauträger beweisbelastet; 30-Jahres-Obergrenze. | Gegen Klauseln `Sachverständiger nimmt bindend ab`, auch wenn WEG ihn wählt. |
| Schlussrate und vollständige Fertigstellung | BGH, Urteil vom 22.04.2026 - VII ZR 88/25, official PDF: https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/VII_ZS/2025/VII_ZR__88-25.pdf?__blob=publicationFile&v=1 | Die Formulierung `nach vollständiger Fertigstellung` ist im Bauträgervertrag auszulegen. Wenn der Vertrag den Bauträger verpflichtet, im Abnahmeprotokoll aufgeführte Mängel/Restarbeiten zu beseitigen, kann die Schlussrate bis dahin nicht fällig sein. Nicht bloß Zug-um-Zug-Verurteilung. | Schlussrate nicht freigeben, wenn protokollierte Mängel/Restarbeiten offen sind. |
| Änderung der Teilungserklärung/Gemeinschaftsordnung | BGH, Urteil vom 23.01.2026 - V ZR 91/25, official PDF: https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/V_ZS/2025/V_ZR__91-25.pdf?__blob=publicationFile&v=1 | AGB-Pflichten des Verbrauchers, späteren Änderungen der Teilungserklärung durch den Bauträger zuzustimmen, sind nach § 308 Nr. 4 BGB unwirksam, wenn die Klausel keine im Einzelnen benannten triftigen Gründe erkennen lässt. Aus § 242 BGB folgt dann regelmäßig keine Ersatz-Zustimmungspflicht. Private Vermögensverwaltung kann Verbraucherstatus bleiben, auch bei Gewerbeeinheit. | Weite Vollmachten und Zustimmungspflichten zu Teilungserklärung, Gemeinschaftsordnung, Untergemeinschaften, Nutzungsänderungen rot markieren. |
| Abnahme durch bauträgernahe Tochtergesellschaft | BGH, Urteil vom 09.11.2023 - VII ZR 241/22, DeJure: https://dejure.org/dienste/vernetzung/rechtsprechung?Aktenzeichen=VII+ZR+241%2F22&Datum=09.11.2023&Gericht=BGH | Abnahmeklauseln, die eine im Lager des Bauträgers stehende Person/Gesellschaft für die Abnahme des Gemeinschaftseigentums einsetzen, sind AGB-rechtlich hoch angreifbar. Die GdWE kann Mängelrechte gebündelt geltend machen; der Verwender kann sich nicht auf die Folgen seiner unwirksamen Klausel berufen. | Gegen Tochtergesellschaft, Erstverwalter, Projektsteuerer, `neutralen` Bauträgerdienstleister. |
| Notaranderkonto bei Bauträgerabwicklung | BGH, Beschluss vom 02.08.2023 - VII ZB 28/20, official PDF: https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/VII_ZS/2020/VII_ZB__28-20.pdf?__blob=publicationFile&v=1 | Notaranderkonto ist kein einfacher Ersatz für MaBV-Schutz. § 57 Abs. 2 BeurkG richtet sich an den Notar; ein fehlendes Sicherungsinteresse macht die zivilrechtliche Verwahrungsabrede nicht automatisch unwirksam. Bei Abtretung/Pfändung kann der Auszahlungsanspruch gegen den Notar miterfasst sein. | Nicht pauschal `Notaranderkonto löst alles`; Verwahrungsanweisung, MaBV, Fälligkeit und Empfangsberechtigung getrennt prüfen. |

## Normenkarte

| Norm | Harte Aussage |
| --- | --- |
| § 650u BGB | Bauträgervertrag kombiniert Errichtung/Umbau mit Eigentums- oder Erbbaurechtsübertragung. Für den Bau gelten Bauvertragsnormen, soweit § 650u Abs. 2 nichts ausschließt; für die Eigentumsübertragung Kaufrecht. |
| § 650u Abs. 2 BGB | Nicht anwendbar: §§ 648, 648a, 650b bis 650e, § 650k Abs. 1, §§ 650l und 650m Abs. 1. Nicht ausgeschlossen sind § 650j, § 650k Abs. 2/3, § 650m Abs. 2, § 650n. |
| § 650v BGB | Abschlagszahlungen kann der Bauträger nur verlangen, soweit sie nach einer Verordnung aufgrund Art. 244 EGBGB vereinbart sind. Praktisch: MaBV. |
| § 650v BGB, § 1 AbschlagsV, § 12 MaBV | Ratenplan und Sonderwunschabrechnung am gesetzlichen Sicherungssystem messen. |
| § 632a BGB | Allgemeine Abschlagsregel; beim Bauträger durch § 650v BGB und MaBV praktisch überlagert. Nicht als freie Ersatz-Ratenlogik verwenden. |
| § 650m Abs. 2 BGB | Verbraucher erhält bei erster Abschlagszahlung 5 % Sicherheit für rechtzeitige Herstellung ohne wesentliche Mängel. Bei Bauträgern nicht durch § 650u Abs. 2 ausgeschlossen. |
| § 650m Abs. 1 BGB | 90 %-Deckel für Abschläge nach § 632a; bei Bauträgervertrag durch § 650u Abs. 2 ausgeschlossen. Nicht fälschlich als Bauträger-Hauptregel nutzen. |
| § 650j BGB | Baubeschreibungspflicht nach Art. 249 EGBGB. Bei Bauträgervertrag nicht durch § 650u Abs. 2 ausgeschlossen. |
| § 650k Abs. 2/3 BGB | Unklare oder unvollständige Baubeschreibung wird unter allen Umständen ausgelegt; Zweifel gehen zulasten des Unternehmers. Fertigstellungsdatum oder Bauzeit muss verbindlich sein. |
| § 650k Abs. 1 BGB | Wird durch § 650u Abs. 2 ausgeschlossen. Nicht behaupten, die vorvertragliche Baubeschreibung werde bei Bauträgern automatisch über Abs. 1 Vertragsinhalt. Vertragsinhalt muss über Beurkundung/Einbeziehung gesichert werden. |
| § 650n BGB | Planungs- und Nachweisunterlagen vor Ausführung und spätestens mit Fertigstellung; auch bei Finanzierung/KfW/GEG-Nachweisen relevant. |
| § 650p BGB | Architekten-/Ingenieurvertrag schuldet die Leistungen, die nach Stand der Planung und Ausführung erforderlich sind, um vereinbarte Planungs- und Überwachungsziele zu erreichen. Beim Bauträger nicht automatisch Anspruch des Erwerbers gegen den Planer, aber starke Systematik für Planung, Überwachung und Dokumentation. |
| § 34 HOAI i. V. m. Anlage 10.1 HOAI | Leistungsbild Gebäude und Innenräume: neun Leistungsphasen; LPH 8 ist Objektüberwachung, Bauüberwachung und Dokumentation. HOAI ist primär Honorarrecht, liefert aber eine praxisfeste Checkliste, welche Planungs- und Überwachungsleistungen im Projekt organisatorisch abgesichert sein müssen. |
| § 309 Nr. 12 BGB | Beweislaständerungen zulasten des Kunden, insbesondere Verantwortungsbereich des Verwenders oder pauschale Tatsachenbestätigungen, sind unwirksam. Ausnahme für gesondert unterschriebene Empfangsbekenntnisse. |
| § 309 Nr. 15 BGB | Werkvertrags-AGB sind unwirksam, wenn sie wesentlich überhöhte Abschlagszahlungen erlauben oder die 5 %-Sicherheit nach § 650m Abs. 2 nicht/zu niedrig leisten lassen. |
| § 3 MaBV | Vor jeder Geldannahme: wirksamer Vertrag ohne vertragliche Rücktrittsrechte des Bauträgers, Vormerkung, Freistellung, Baugenehmigung/Bestätigung. Danach nur bis zu sieben Teilbeträge nach Bauablauf. |
| § 7 MaBV | Alternative Sicherung für alle Ansprüche auf Rückgewähr/Auszahlung; bei Eigentums-/Erbbaurechtsübertragung aufrechtzuerhalten bis § 3 Abs. 1 erfüllt ist und das Objekt vollständig fertiggestellt ist. Keine gesetzliche Formel `Vertragssumme plus 5 %`. |
| § 12 MaBV | Abweichungen zulasten des Auftraggebers von §§ 2 bis 8 MaBV sind unzulässig. |
| § 306 BGB | Regelfolge unwirksamer AGB: Klausel fällt weg, Vertrag bleibt bestehen, Gesetz tritt an die Stelle. Nicht vorschnell Gesamtnichtigkeit behaupten. |
| § 311b BGB | Grundstücks-/Bauträgervertrag braucht notarielle Beurkundung. Nicht mitbeurkundete Kernbestandteile können Formrisiken auslösen. |
| §§ 642, 643 BGB | Mitwirkungs- und Kündigungsfolgen können für Bauablaufstörungen relevant sein; beim Bauträger nur konkret anwenden, nicht als pauschale Verzugsentlastung des Bauträgers. |

## 30-Prüfschleifen

Bei jeder Vollanalyse durchlaufe diese Schleifen intern. Im Ergebnis nur die relevanten Befunde ausgeben.

1. Vertragsart: echter Bauträgervertrag oder reiner Kauf-/Werkvertrag?
2. Verbraucherstatus: Eigennutzung, private Kapitalanlage, Vermögensverwaltung, Unternehmereigenschaft?
3. Beurkundung: alle wesentlichen Anlagen mitbeurkundet?
4. Zwei-Wochen-Verbraucherschutz im Beurkundungsverfahren plausibel eingehalten?
5. § 3 Abs. 1 MaBV vor erster Zahlung vollständig erfüllt?
6. Ratenplan: sieben Teilbeträge und Prozentsätze korrekt?
7. § 7 MaBV: falls Bürgschaft, alle Rückgewähr-/Auszahlungsansprüche abgesichert; keine Vermischung mit § 3-MaBV-Modell?
8. 5 %-Sicherheit nach § 650m Abs. 2 BGB vorhanden, nicht abbedungen?
9. § 309 Nr. 12: keine Beweislastumkehr, keine pauschalen Tatsachenbestätigungen?
10. § 309 Nr. 15: keine überhöhten Abschläge, keine reduzierte Sicherheit?
11. Baubeschreibung: § 650j, § 650k Abs. 2/3, Art. 249 EGBGB, Bausoll konkret?
12. Fertigstellungstermin: verbindlich, nicht beliebig verschiebbar; bei Terminverzug bauablaufbezogene Darlegung verlangt?
13. Bauänderungen: nur triftige, konkret benannte Gründe, kein freies Leistungsänderungsrecht?
14. Teilungserklärung/Gemeinschaftsordnung: keine pauschalen Änderungsvollmachten?
15. Abnahme Sondereigentum: persönlich, Protokoll, Vorbehalte, keine Fiktion durch Schlüssel?
16. Abnahme Gemeinschaftseigentum: keine bauträgernahe Person, keine bindende Fremdabnahme ohne Eigenrecht?
17. Schlussrate: vollständige Fertigstellung, protokollierte Mängel, Zurückbehaltung?
18. Vormerkung/Lastenfreistellung: keine Löschungsdruckmittel, Rang sauber?
19. Verjährung/Mängelrechte: fünf Jahre Bauwerk, keine Ausschlussfristen?
20. Verhandlungsfähigkeit: jedes 🔴 mit gesetzlicher Grundlage, Fallanker, Gegenargument und gewünschter Neufassung?
21. HOAI-/Planungslogik: Sind LPH 1 bis 9, insbesondere Ausführungsplanung und Objektüberwachung, organisatorisch nachvollziehbar beauftragt, dokumentiert und nachweisbar?
22. Private Bauüberwachung: Darf der Erwerber eigene Sachverständige zu Bautenstand, Sonderwünschen, Abnahme und Mängeln hinzuziehen?
23. Baugrund/Baugrube: Liegen Baugrundgutachten, Grundwasser-, Altlasten-, Kampfmittel- und Baugrubenkonzepte vor; wer trägt das Restrisiko?
24. Standsicherheit/Brandschutz/Schall/Feuchte/Wärme: Sind Nachweise, Ausführungskontrollen und Herausgabeunterlagen konkret geregelt?
25. Technische Ausrüstung: Heizung, Lüftung, Trinkwasser, Elektro, PV, Aufzug, Tiefgarage, Entwässerung, Gebäudeautomation und Wartung prüfen.
26. Bauablauf/Qualitätsgates: Sind Terminplan, Bautenstandsprüfung, Mängeltracking und Schlussdokumentation prüfbar?
27. Wirtschaftliche Tragfähigkeit: Projektgesellschaft, Globalfinanzierung, Freistellung, Nachunternehmer-/Generalunternehmerrisiko, Vorinsolvenzzeichen, Reservierungs-/Sonderwunschzahlungen.
28. WEG-Organisation: Erstverwalter, Untergemeinschaften, Kostenverteilung, Wartungsverträge, Instandhaltungsrücklage, Übergang der Kontrolle auf Erwerber.
29. Betriebs- und Lebenszykluskosten: Energie, Wartung, Ersatzteile, Tiefgarage, Pumpen, Lüftung, Aufzug, Außenanlagen, Gemeinschaftseinrichtungen.
30. Gesamtbild: Ergibt die Summe aus Recht, Technik, Wirtschaft und Organisation ein beurkundungsfähiges, finanzierbares und baulich kontrollierbares Projekt?

## Pflicht-Prüfblock

Dieser Block steht in jeder Vollanalyse ganz oben.

| Pflichtpunkt | Prüfung | Harte Folge |
| --- | --- | --- |
| 5 %-Sicherheit | Enthält der Vertrag eine echte Sicherheit nach § 650m Abs. 2 BGB bei der ersten Abschlagszahlung? Wird sie nicht durch Kosten, Vorleistung oder Verzicht entwertet? | Fehlt oder reduziert: 🔴, zusätzlich § 309 Nr. 15 lit. b BGB prüfen. |
| Beweislast | Verlagert eine Klausel Verantwortungsbereich des Bauträgers auf den Erwerber? | 🔴 nach § 309 Nr. 12 lit. a BGB. |
| Tatsachenbestätigung | Bestätigt der Erwerber pauschal Erhalt, Kenntnis, Prüfung, Belehrung, Vollständigkeit oder Risikoaufklärung? | 🔴 nach § 309 Nr. 12 lit. b BGB, außer gesondertes Empfangsbekenntnis. |
| MaBV-Fälligkeit | Verlangt der Bauträger Geld vor § 3 Abs. 1 MaBV oder außerhalb § 3 Abs. 2/§ 7 MaBV? | 🔴; Zahlung verweigern, Notar/Bauträger korrigieren lassen. |
| Abnahme Gemeinschaftseigentum | Wird das Recht zur eigenen Prüfung/Abnahme entzogen oder bauträgernah gebündelt? | 🔴 nach aktueller BGH-Linie 2023/2026. |
| Schlussrate | Wird Schlussrate trotz offener protokollierter Mängel oder Restarbeiten fällig gestellt? | 🔴/🟠; BGH VII ZR 88/25 nutzen. |
| Teilungserklärung | Darf Bauträger nachträglich beliebig ändern oder Zustimmung verlangen? | 🔴, § 308 Nr. 4 BGB und BGH V ZR 91/25. |
| Bausoll | Baubeschreibung konkret, vollständig, datiert und mitbeurkundet? | Lücken: 🔴/🟠; Zweifel zulasten Unternehmer (§ 650k Abs. 2 BGB). |
| Planung/Objektüberwachung | Ist erkennbar, wer LPH 5 Ausführungsplanung, LPH 8 Objektüberwachung/Bauüberwachung und technische Fachüberwachung schuldet? | Fehlt oder nur interne Verkäuferkontrolle: 🟠/🔴; Herausgabe-/Einsichts- und Bautenstandsrechte verlangen. |
| Private Sachverständige | Verhindert der Vertrag eigene Baukontrolle, Fotos, Abnahmebegleitung oder Bautenstandsnachweis? | 🔴, wenn MaBV-/Abnahme-/Mängelprüfung praktisch leerläuft. |
| Baugrund/Technik | Werden Baugrund, Grundwasser, Altlasten, Kampfmittel, Schallschutz, Feuchteschutz, Brandschutz, GEG/KfW oder Haustechnik nur pauschal oder risikoverlagernd geregelt? | 🟠/🔴; technische Unterlagen, Nachweise und Risikoallokation verlangen. |
| Vorinsolvenz/Projektgesellschaft | Fordert der Bauträger Zahlungen vor MaBV-Fälligkeit, über Sonderwünsche, Reservierung, Schlüssel-/Besitzdruck oder ohne saubere Freistellung? | 🔴; Zahlungsstopp, Sicherheiten, Rückforderungs- und Haftungsketten prüfen. |

## Workflow

### 1 — Intake

Erfasse knapp:

| Punkt | Inhalt |
| --- | --- |
| Rolle | Wer fragt konkret: Erwerber dieser Einheit, anwaltliche Vertretung, Verbraucherzentrale, GdWE, Notar-/Bauträger-Gegenprüfung |
| Status | Entwurfsdatum oder UR-Nr.; Beurkundungstermin, bereits beurkundet, Bauphase, Rate angefordert, Abnahme, Mängelstreit, Insolvenz |
| Objekt | Haus/Einheit/Geschoss, Keller, Balkon/Terrasse/Garten, Stellplatz, Miteigentumsanteil, Wohnflächenmethode, Sondernutzungsrechte |
| Projekt | Grundstück, Bauabschnitte, Nachbarbaufelder, Tiefgarage, Erschließung, Gemeinschaftsflächen, Erstverwalter, spätere Quartiersentwicklung |
| Preis | Kaufpreis, Stellplatzaufpreis, Reservierungsentgelt, Sonderwünsche, Ratenplan, Erschließungs-/Anschlusskosten, Finanzierungs-/Förderbezug |
| Unterlagen | Vertrag, Baubeschreibung mit Version, Pläne, Teilungserklärung/Nachträge, Gemeinschaftsordnung, Freistellung, Baugenehmigung, Baugrund, Fachplaner-/Nachweisunterlagen |
| Eilbedarf | Datum der Beurkundung, Rate, Bemusterung, Zutritt, Abnahme, Besitzübergang, Schlussrate, gerichtliche Frist |

### 2 — Quellenrefresh

Vor einer finalen Ausgabe:

- Normen auf `gesetze-im-internet.de` prüfen, wenn Normzitat tragend ist.
- Rechtsprechung aus der Ankerliste öffnen oder über DeJure/OpenJur/offizielle Gerichtsseite verifizieren.
- Keine `Rn.` nennen, wenn sie nicht im geöffneten Volltext geprüft wurde.

### 3 — Vertragsart und Anwendbarkeit

Ein Bauträgervertrag liegt vor, wenn der Unternehmer Bauerrichtung/Umbau schuldet und zugleich Eigentum/Erbbaurecht übertragen muss (§ 650u Abs. 1 BGB).

Wenn kein Bauträgervertrag:

- Reiner Grundstückskauf: Kaufrecht/§ 311b BGB, nicht MaBV-Ratenplan.
- Reiner Bauvertrag auf eigenem Grundstück: Verbraucherbauvertrag/Bauvertrag, nicht Eigentumsübertragung.
- Sanierungsobjekt mit Aufteilung: Bauträgerrecht, wenn Erwerb und Herstellung/Sanierung verbunden sind.

### 4 — Pflichtbausteine

| Baustein | Soll | Ampel bei Fehlen |
| --- | --- | --- |
| Notarielle Beurkundung | Urkunde mit allen wesentlichen Leistungspflichten | 🔴 |
| Exakte Objektbezeichnung | Grundbuch, Flurstück, Wohnung/Teileigentum, Sondernutzungsrechte | 🔴 |
| Teilungserklärung/Gemeinschaftsordnung | beurkundet oder eindeutig einbezogen | 🔴/🟠 |
| Baubeschreibung | konkret, datiert, mitbeurkundet/eindeutig einbezogen | 🔴 |
| Fertigstellung | Datum oder bestimmbarer Zeitraum | 🔴 |
| Vormerkung | vor Zahlung an vereinbarter Rangstelle | 🔴 |
| Freistellung | auch für Nichtvollendung gesichert | 🔴 |
| Ratenplan/Sicherheit | § 3 oder § 7 MaBV | 🔴 |
| Abnahme | persönliche Rechte, Protokoll, Vorbehalte | 🔴/🟠 |
| Mängelrechte | gesetzlich, fünf Jahre Bauwerk | 🔴 bei Verkürzung |
| Objektüberwachung | LPH-8-/Bauüberwachungslogik, Bautenstand, Dokumentation | 🟠/🔴 bei rein interner Verkäuferbestätigung |
| Technische Nachweise | Baugrund, Statik, Brandschutz, Schall, Feuchte, Energie, Haustechnik | 🟠/🔴 bei Pauschalverweis oder Risikoverlagerung |

### 5 — Klauselmatrix

Nutze diese Spalten:

| Originalwortlaut | Decodierung | Risiko | Rechtsanker | Bauträger-/Notarargument | Antwort | Änderung | Ampel |
| --- | --- | --- | --- | --- | --- | --- | --- |

Die Antwort muss streitfest sein: Gesetz zuerst, dann aktueller BGH-Anker, dann konkrete Klauselwirkung.

### 6 — Verhandlungsfassung

Für jedes 🔴:

1. Streichung oder Neufassung formulieren.
2. Kurzbegründung in zwei bis vier Sätzen.
3. Dringlichkeit: `Muss vor Beurkundung`, `Kann nachverhandelt werden`, `Streitfallposition`.

### 7 — Ergebnisbewertung

Gesamteinschätzung:

- `beurkundungsfähig nach Korrektur einzelner Punkte`
- `nur nach wesentlicher Überarbeitung beurkundungsfähig`
- `nicht beurkunden`
- `bei bereits beurkundetem Vertrag: AGB-Unwirksamkeit/Einbehalt/Klage prüfen`

## Antwortformate

### Schnellscan

```text
Kurzbild
- Fall-Fingerabdruck:
- Vertragsart:
- Verbraucherstatus:
- Pflicht-Prüfblock: 🔴 x / 🟠 y / 🟢 z
- MaBV-Fälligkeit:
- Haupthebel:
- Sofortmaßnahme:
```

### Vollanalyse

```text
1. Fall-Fingerabdruck
2. Pflicht-Prüfblock
3. Quellenstand
4. Vertragsart und Verbraucherstatus
5. MaBV-Zahlungsprüfung
6. AGB-Klauselmatrix
7. Baubeschreibung/Bausoll
8. Abnahme, Schlussrate, Mängelrechte
9. HOAI/Objektüberwachung/technische Projektrisiken
10. Wirtschaft/Organisation/WEG-Betrieb
11. Eigentumsschutz/Insolvenz
12. Verhandlungspaket
13. Restfragen
```

### Streitstellen-Tabelle

```text
| Klausel | Risiko | Harte Grundlage | Erwartetes Gegenargument | Antwort | Gewünschte Fassung | Ampel |
```

### Regelausgabe

Die Regelausgabe ist immer das **Drei-Dokumente-Paket**. Es wird auch bei unvollständigem OCR, Fotos, Entwurfsfragmenten oder fehlenden Anlagen erstellt; Unsicherheiten werden als Annahmen, Prüfvorbehalte und Unterlagenliste kenntlich gemacht.

1. **Übersendungsschreiben / Informationsschreiben an den Mandanten** in einfacher Sprache. Es erklärt Ergebnis, Hauptrisiken, Handlungsempfehlung und verweist auf das beigefügte Gutachten.
2. **Ausführliches Mandantengutachten** mit Sachverhalt, Quellenstand, Klauselmatrix, rechtlicher und technischer Begründung, Ampelbefunden, Gegenargumenten und konkreten Änderungszielen.
3. **Außergerichtliches Aufforderungsschreiben an Bauträger/Notar** mit jeder wesentlichen Änderung: Originalproblem, kurze Begründung, warum die Klausel so nicht geht, und konkrete Formulierung oder Streichungsanweisung, wie es richtig gefasst werden muss.

Alle drei Dokumente beruhen auf denselben Befunden. Was im Gutachten 🔴 ist, muss im Schreiben an Bauträger/Notar auftauchen; was im Mandantenanschreiben als Hauptrisiko steht, muss im Gutachten belegt sein. Es gibt keine bloße Endanalyse ohne diese drei Dokumente.

## Teil A — MaBV und Zahlungen

### A.1 — § 3 Abs. 1 MaBV vor erster Zahlung

Der Bauträger darf Vermögenswerte erst entgegennehmen oder sich zu deren Verwendung ermächtigen lassen, wenn die Voraussetzungen kumulativ erfüllt sind.

| Voraussetzung | Verbrauchercheck | Befund |
| --- | --- | --- |
| Wirksamer Vertrag und Genehmigungen | Notarmitteilung vorhanden; keine vertraglichen Rücktrittsrechte des Bauträgers | Fehlt: 🔴 |
| Vormerkung | Anspruch auf Eigentum/Erbbaurecht an vereinbarter Rangstelle eingetragen; bei WEG auch Begründung des Wohnungs-/Teileigentums vollzogen | Fehlt/Nachrang: 🔴 |
| Freistellung | Nicht zu übernehmende Grundpfandrechte müssen auch bei Nichtvollendung freigestellt oder Zahlungen zurückgeführt werden | Lücke: 🔴 |
| Baugenehmigung/Bestätigung | Genehmigung oder gesetzliche/behördliche Bestätigung; bei Eigenbestätigung Monatsfrist beachten; unrichtige Bestätigung oder wesentliche Abweichung von der Genehmigung sperrt die Fälligkeit | Unklar: 🟠/🔴 |

### A.2 — § 3 Abs. 2 MaBV: bis zu sieben Teilbeträge

Nicht schreiben: `dreizehn gesetzliche Raten`. Richtig ist: Der Bauträger darf in **bis zu sieben Teilbeträgen** abrechnen. Diese Teilbeträge können aus den gesetzlichen Vomhundertsätzen zusammengesetzt werden.

| Baustein | Gesetzlicher Anteil | Kontrollwert bei Grundstückserwerb (30 % + 70 %) |
| --- | --- | --- |
| Beginn Erdarbeiten | 30 % der Vertragssumme; bei Erbbaurecht 20 % | 30,0 % |
| Rohbau einschließlich Zimmerer | 40 % der restlichen Vertragssumme | 28,0 % |
| Dachflächen/Dachrinnen | 8 % der restlichen Vertragssumme | 5,6 % |
| Rohinstallation Heizung | 3 % der restlichen Vertragssumme | 2,1 % |
| Rohinstallation Sanitär | 3 % der restlichen Vertragssumme | 2,1 % |
| Rohinstallation Elektro | 3 % der restlichen Vertragssumme | 2,1 % |
| Fenster einschließlich Verglasung | 10 % der restlichen Vertragssumme | 7,0 % |
| Innenputz ohne Beiputz | 6 % der restlichen Vertragssumme | 4,2 % |
| Estrich | 3 % der restlichen Vertragssumme | 2,1 % |
| Fliesen Sanitär | 4 % der restlichen Vertragssumme | 2,8 % |
| Bezugsfertigkeit Zug um Zug gegen Besitz | 12 % der restlichen Vertragssumme | 8,4 % |
| Fassade | 3 % der restlichen Vertragssumme | 2,1 % |
| Vollständige Fertigstellung | 5 % der restlichen Vertragssumme | 3,5 % |

Bei Erbbaurecht sind die Kontrollwerte anders, weil die erste Rate 20 % beträgt und die restliche Vertragssumme 80 % ausmacht.

### A.3 — Typische MaBV-Verstöße

| Klausel/Verhalten | Problem | Antwort |
| --- | --- | --- |
| Erste Rate bei Beurkundung | § 3 Abs. 1 MaBV noch nicht erfüllt | Zahlung verweigern, Notarbestätigung/Vormerkung/Freistellung verlangen. |
| Mehr als sieben Teilbeträge | § 3 Abs. 2 MaBV sagt bis zu sieben | Zusammenfassung verlangen. |
| Pauschal `nach Baufortschritt` | Fälligkeit nicht objektiv prüfbar | Konkrete MaBV-Baustufe verlangen. |
| Schlussrate trotz offener Protokollmängel | `vollständige Fertigstellung` fraglich | BGH VII ZR 88/25 einsetzen. |
| Sonderwünsche sofort fällig | Umgehungsrisiko, wenn bauwerksbezogen und vor Leistung | Sonderwünsche nach Leistung/Abnahme oder Sicherung regeln. |
| Raten über gesetzlichem Kontrollwert | § 650v BGB i. V. m. MaBV | Korrektur auf gesetzliche Prozentsätze. |
| Zwei Großraten, z. B. 30 % bei Erdarbeiten und 70 % bei Bezugsfertigkeit | MaBV-Bauablauf und Schlussrate werden ausgehöhlt; Schlussrate darf nicht vor vollständiger Fertigstellung laufen | Zahlungsplan vollständig neu fassen; keine geltungserhaltende Rettung über `wirtschaftlich gleichwertig`. |
| Bautenstand nur nach `Mitteilung des Verkäufers` | einseitige Fälligkeitsauslösung; Erwerber verliert reale Kontrollmöglichkeit | objektiv prüfbaren Bautenstand, angemeldete Besichtigung und eigene Sachverständige vor Rate sichern. |
| Erste Rate von 30 % trotz erkennbar niedrigem Grundstücksanteil | Überzahlung in Niedrigpreisregion möglich; Grundstückswert und Bauwert gesondert plausibilisieren | Reduzierung der ersten Rate verlangen, wenn Grundstücksanteil die 30 %-Quote nicht trägt. |
| Schlussrate ohne Außenanlagen, Pflasterung, Treppenhaus oder Restarbeiten | vollständige Fertigstellung wird künstlich verengt | Außenanlagen und Gemeinschaftseigentum ausdrücklich in die Fertigstellung einbeziehen. |
| § 650m-Sicherheit nur als `Berechtigung zum Einbehalt` formuliert | Intransparenz; Erwerber soll Schutz durch Nichtausübung verlieren | Sicherheit als zwingende Vertragsmechanik regeln: Einbehalt oder taugliche Bürgschaft bei erster Abschlagszahlung. |
| Sonderwunsch außerhalb des Ratenplans sofort zahlbar | MaBV-Umgehung, wenn der Sonderwunsch bauwerksbezogen ist | in Gesamtpreis und MaBV-Ratenlogik einbauen; Ausnahme nur bei nachträglicher, fertiggestellter Leistung oder Schlussabrechnung. |
| Wesentliche Abweichung von Baugenehmigung/Nachtrag fehlt | Allgemeine Fälligkeitsvoraussetzung kann fehlen; Risiko illegaler oder nicht genehmigter Ausführung | Nachtragsgenehmigung, Auflagenstand und Zahlungsstopp prüfen; gezahlte Beträge rückfordern, wenn Fälligkeit fehlte. |
| Bezugsfertigkeitsrate trotz nicht verkehrssicherem Zugang | Bezugsfertigkeit fehlt, wenn Wohnung nur gefährlich oder unzumutbar erreichbar ist | Besitz-/Rate erst bei sicherem Zugang; Provisorien, fehlende Geländer, offene Baugruben und Baustellenwege konkret dokumentieren. |
| § 3-MaBV-Modell wird mit § 7-MaBV-Bürgschaft vermischt | Sicherungsarchitektur unklar; § 7 Abs. 1 Satz 4 MaBV beachten | Entweder vollständiges § 3-Modell oder vollständige § 7-Sicherheit; keine halbierte Mischlösung akzeptieren. |

### A.4 — § 7 MaBV-Sicherheit

§ 7 MaBV ist keine beliebige Bankbürgschaft und kein Marketingersatz. Gesichert werden müssen alle etwaigen Ansprüche des Auftraggebers auf Rückgewähr oder Auszahlung seiner Vermögenswerte. Bei Eigentums-/Erbbaurechtsübertragung ist die Sicherheit aufrechtzuerhalten, bis § 3 Abs. 1 MaBV erfüllt ist und das Vertragsobjekt vollständig fertiggestellt ist.

| Prüfpunkt | Soll | Befund |
| --- | --- | --- |
| Sicherungszweck | alle Rückgewähr-/Auszahlungsansprüche | 🔴 wenn nur Teilbetrag |
| Dauer | bis § 3 Abs. 1 erfüllt und vollständige Fertigstellung | 🔴 wenn befristet/kündbar |
| Bürge | im Geltungsbereich befugtes Kreditinstitut/Kreditversicherer | 🟠 bei Auslands-/Konzernbürge |
| Original | vor Zahlung beim Erwerber oder sicherer Zugriff | 🟠/🔴 |
| Austausch § 3/§ 7 | klar geregelt | 🟠 wenn doppeldeutig |

Vermischungsverbot: Ein Vertrag darf nicht scheinbar nach § 3 MaBV mit Vormerkung, Freistellung und Ratenplan arbeiten und zugleich einzelne Zahlungsrisiken nur bruchstückhaft über eine § 7-Bürgschaft abfangen. Wird § 7 MaBV gewählt, muss die Sicherheit die Rückgewähr-/Auszahlungsansprüche aus den entgegenzunehmenden Vermögenswerten decken; wird § 3 MaBV gewählt, müssen die allgemeinen und besonderen Fälligkeitsvoraussetzungen vollständig eingehalten werden. § 7 Abs. 1 Satz 4 MaBV erlaubt den Austausch der Sicherungen. Bei einem Wechsel den Schutz jeder einzelnen Zahlung und den Übergabe- und Freigabezeitpunkt belegen.

### A.5 — Notaranderkonto

Ein Notaranderkonto ist kein Verbraucherschutz-Automatismus.

Nutze BGH VII ZB 28/20:

- Prüfe öffentlich-rechtliche Verwahrungsanweisung an den Notar und zivilrechtliche Verwahrungsvereinbarung getrennt.
- Fehlendes Sicherungsinteresse kann notarielle Amtspflichten betreffen, macht die zivilrechtliche Abrede aber nicht automatisch unwirksam.
- Bei Pfändung/Abtretung der Kaufpreisforderung kann auch der Auszahlungsanspruch gegen den Notar erfasst sein.
- Deshalb: Fälligkeit, MaBV, Einbehalte, Abtretungen, Pfändungen und Auszahlungsanweisung sauber auseinanderhalten.

## Teil B — AGB-Klauselkontrolle

### B.1 — Grundsätze

Notarielle Beurkundung schützt nicht vor AGB-Kontrolle. Wenn der Bauträger vorformuliert und für mehrere Erwerber verwendet, sind §§ 305 ff. BGB zentral.

Regelfolgen:

- § 305c Abs. 2 BGB: Zweifel bei Auslegung gehen zulasten des Verwenders.
- § 307 BGB: unangemessene Benachteiligung/Intransparenz.
- § 308 BGB: Klauselverbote mit Wertungsmöglichkeit, wichtig bei Änderungsvorbehalten.
- § 309 BGB: Klauselverbote ohne Wertungsmöglichkeit, wichtig Nr. 2, 3, 12, 15.
- § 306 BGB: unwirksame Klausel entfällt; Gesetz tritt ein.

### B.2 — Klauselkatalog mit Gegenargumenten

| Klauseltyp | Angriff | Erwartetes Gegenargument | Harte Antwort | Ampel |
| --- | --- | --- | --- | --- |
| Abnahme GE durch Vertreter aus Erwerberkreis | § 307 BGB; BGH VII ZR 68/24 | `Die Erwerber wählen doch selbst.` | Wahl genügt nicht, wenn der einzelne Erwerber sein eigenes Prüf- und Abnahmerecht verliert. | 🔴 |
| Abnahme GE durch Sachverständigen | § 307 BGB; BGH VII ZR 108/24 | `Neutraler Sachverständiger ist besser.` | Neutralität ersetzt nicht das Bestellerrecht auf eigene Prüfung und Erklärung. | 🔴 |
| Abnahme durch Tochter/Erstverwalter/Projektpartner | § 307 BGB; BGH VII ZR 241/22 | `Organisatorisch nötig.` | Bauträgernahes Lager und Entzug eigener Abnahmerechte sind nicht organisatorisch heilbar. | 🔴 |
| Nachzüglerklausel `Abnahme ist erfolgt` | § 307/§ 305c BGB; BGH VII ZR 68/24 | `Das Objekt war schon abgenommen.` | Erwerber kann nicht formularmäßig an eine frühere, fremde und ggf. unwirksame Abnahme gebunden werden. | 🔴 |
| Schlussrate ohne Mängeleinbehalt | § 641 Abs. 3 BGB; BGH VII ZR 88/25 | `Mängel werden Zug um Zug beseitigt.` | Bei Vertragswortlaut `vollständige Fertigstellung` und protokollierten Restmängeln kann schon Fälligkeit fehlen. | 🔴 |
| Schlüssel nur gegen vollständige Zahlung | § 307, § 641 Abs. 3 BGB | `Ohne Zahlung kein Besitz.` | Zahlungspflicht kann nicht das gesetzliche Zurückbehaltungsrecht bei Mängeln entwerten. | 🔴 |
| Vormerkungslöschung bei einseitiger Verzugsmitteilung | § 307 BGB, Eigentumssicherung | `Nur für Zahlungsverzug.` | Die Vormerkung ist Kernschutz gegen Insolvenz; einseitiger Druckmechanismus ist unverhältnismäßig. | 🔴 |
| Pauschale Änderung Teilungserklärung | § 308 Nr. 4 BGB; BGH V ZR 91/25 | `Bauprojekt braucht Flexibilität.` | Flexibilität nur mit im Einzelnen benannten triftigen Gründen; § 242 ersetzt unwirksame AGB regelmäßig nicht. | 🔴 |
| Pauschale Bauänderungen `gleichwertig` | § 308 Nr. 4, § 307 BGB | `Technische Anpassungen sind üblich.` | Nur konkret benannte technische Gründe, keine Qualitäts-/Flächen-/Nutzungsverschlechterung, Informationspflicht. | 🟠/🔴 |
| Beweislast für Mängel/Verzug beim Erwerber vor Abnahme | § 309 Nr. 12 lit. a BGB | `Der Erwerber behauptet den Mangel.` | Umstände im Verantwortungsbereich des Bauträgers dürfen nicht auf den Erwerber verlagert werden. | 🔴 |
| Bestätigung `alles erhalten/geprüft/verstanden` | § 309 Nr. 12 lit. b BGB | `Nur Dokumentation.` | Pauschale Tatsachenbestätigung ist unwirksam; nur gesondertes Empfangsbekenntnis ist privilegiert. | 🔴 |
| 5 %-Sicherheit fehlt oder ist reduziert | § 650m Abs. 2, § 309 Nr. 15 lit. b BGB | `MaBV schützt ausreichend.` | § 650u Abs. 2 schließt § 650m Abs. 2 nicht aus; § 309 Nr. 15 schützt die Sicherheit zusätzlich. | 🔴 |
| Verjährung unter fünf Jahre | § 634a Abs. 1 Nr. 2 BGB, § 307 BGB | `Üblich am Markt.` | Marktüblichkeit ersetzt nicht gesetzliche Bauwerksverjährung. | 🔴 |
| Mängelanzeigefrist als Ausschlussfrist | § 307 BGB | `Schnelle Klärung nötig.` | Obliegenheit zur Anzeige darf Mängelrechte nicht ausschließen. | 🔴 |
| Aufrechnung nur mit anerkannten/rechtskräftigen Forderungen | § 309 Nr. 3 BGB | `Standardklausel.` | Nur zulässig, wenn unbestrittene und rechtskräftige Forderungen ausgenommen sind; sonst 🔴. | 🟠/🔴 |
| Gerichtsstand am Sitz Bauträger | §§ 38, 29c ZPO, § 307 BGB | `Projektstandort ist sachnah.` | Verbrauchergerichtsstände dürfen nicht formularmäßig entzogen werden. | 🔴 |
| Abtretungsverbot für Mängelrechte | § 307 BGB, WEG/GdWE-Kontext | `Bündelung verhindern.` | Mängelrechte am Gemeinschaftseigentum müssen praktisch durchsetzbar bleiben. | 🟠/🔴 |
| Bemusterungsmehrkosten pauschal | § 307 Abs. 1 S. 2 BGB | `Verwaltungsaufwand.` | Kosten müssen kalkulierbar, transparent und sachlich begründet sein. | 🟠/🔴 |
| Zwei Großraten statt MaBV-Bauablauf | § 3 Abs. 2 MaBV, § 12 MaBV, § 134 BGB | `Die Gesamtsumme bleibt gleich.` | Die MaBV schützt nicht nur die Summe, sondern die zeitliche Koppelung an reale Bautenstände und die Schlussrate. | 🔴 |
| `Mitgeteilte` Bezugsfertigkeit/Fertigstellung | § 305c Abs. 2, § 307 BGB, MaBV | `Der Bauleiter bestätigt den Stand.` | Einseitige Mitteilung ersetzt keine prüfbare Bautenstandslage; Erwerber muss vor Zahlung kontrollieren können. | 🔴 |
| Vollständige Fertigstellung ohne Außenanlagen/Pflasterung | § 3 Abs. 2 MaBV, § 12 MaBV | `Außenanlagen sind Gemeinschaftsthema.` | Sind Außenanlagen geschuldet, gehören sie zur Fertigstellung; sonst wird die Schlussrate vorverlagert. | 🔴 |
| Besichtigung nur mit freiem Verkäuferermessen | § 307 Abs. 2 BGB, MaBV-Kontrolle | `Baustellensicherheit.` | Sicherheit rechtfertigt Organisation, nicht den Ausschluss eigener Bautenstands- und Abnahmekontrolle. | 🔴 |
| Löschung der Vormerkung durch Bauträgervollmacht bei behauptetem Rücktritt | § 309 Nr. 2 lit. a, § 309 Nr. 12 BGB, § 307 BGB | `Sonst bleibt der Bauträger blockiert.` | Die Vormerkung ist Insolvenzschutz; einseitige Behauptungen dürfen den Übereignungsanspruch nicht beseitigen. | 🔴 |
| Empfangs-/Belehrungsbestätigung als Tatsachenerklärung | § 309 Nr. 12 lit. b BGB | `Der Notar protokolliert nur.` | Pauschale Tatsachenbestätigungen ersetzen keine echte Belehrung und dürfen die Beweislast nicht kippen. | 🔴 |
| Vertragsstrafe statt Verzugsschaden ohne Anrechnungssystem | §§ 340, 341 BGB, § 307 BGB | `Die Vertragsstrafe ist abschließend.` | Bei Interessenidentität ist Anrechnung zu prüfen; weitergehender Schaden darf nicht unangemessen abgeschnitten werden. | 🟠/🔴 |
| Pflichtmahnung trotz kalendarischem Termin | § 286 Abs. 2 Nr. 1 BGB, § 307 BGB | `Wir brauchen eine Bauablauf-Nachfrist.` | Ein kalendarischer Termin löst Verzug ohne Mahnung aus; zusätzliche Hürden entwerten den Fertigstellungstermin. | 🔴 |
| Höhere-Gewalt-Vermutung für Pandemie/Lieferketten/Wetter | § 286 Abs. 4 BGB, § 307 BGB | `Das war allgemein bekannt.` | Allgemeinlagen ersetzen keine bauablaufbezogene Darlegung zum konkreten Haus, Gewerk und Zeitfenster. | 🔴 |
| Preisanpassung in den ersten vier Monaten | § 309 Nr. 1 BGB | `Materialpreise steigen schnell.` | Kurzfristige Preiserhöhung ist im Verbraucher-AGB-Regime gesperrt; Krisenrisiko bleibt beim Bauträger. | 🔴 |
| Preisanpassung ohne Saldierung | § 307 Abs. 1, 2 BGB | `Nur Mehrkosten sind relevant.` | Eine einseitige Erhöhung ohne Weitergabe gesunkener Kosten verschiebt das Äquivalenzverhältnis. | 🔴 |
| Preisanpassung ohne echtes Lösungsrecht/Sicherheit | § 307 BGB, Vormerkungslogik | `Der Käufer kann ja zurücktreten.` | Rücktritt lässt den Übereignungsschutz entfallen; erforderlich ist ein sachgerechtes Lösungs- oder Sicherungsmodell. | 🔴 |
| Bauhandwerkersicherung vom Verbraucher-Erwerber | § 650f Abs. 6 Nr. 2 BGB | `Der Bauträger braucht Sicherheit.` | Der Verbraucher-Erwerber eines Bauträgervertrags schuldet keine Bauhandwerkersicherung. | 🔴 |
| VOB/B pauschal einbezogen | §§ 305 ff., § 310 BGB | `Das ist am Bau üblich.` | Gegenüber Verbrauchern greift keine pauschale Privilegierung; jede nachteilige Klausel bleibt kontrollfähig. | 🟠/🔴 |
| § 637-Selbstvornahme ausgeschlossen | § 307 BGB | `Koordination nur durch Bauträger.` | Koordination darf Mängelbeseitigung nicht praktisch monopolisieren; konkrete Reichweite und Restrechte prüfen. | 🟠/🔴 |
| Wohnflächentoleranz über Bagatellbereich | § 307 BGB, Beschaffenheitsvereinbarung | `Messungenauigkeiten sind normal.` | Toleranzen dürfen die vereinbarte Wohnfläche nicht formularmäßig entwerten; Berechnungsmethode und Abweichungsschwelle offenlegen. | 🟠/🔴 |
| Energiestandard ohne konkrete Klasse/Nachweise | § 650k Abs. 2, § 650n BGB | `GEG genügt.` | Förder-, Finanzierungs- und Bausollrisiken verlangen konkrete Effizienzklasse, Nachweise und Übergabezeitpunkte. | 🟠/🔴 |
| Anteilige Sachverständigenkosten für bauträgerseitige Abnahmeorganisation | § 307 BGB | `Die Prüfung dient allen.` | Kosten einer vom Bauträger organisierten oder interessennahen Abnahmestruktur dürfen nicht formularmäßig auf Erwerber verlagert werden. | 🔴 |
| Unbegrenzte Belastungsvollmacht/Globalgrundschuld | § 307 BGB, Vormerkung/Freistellung | `Banktechnisch erforderlich.` | Belastungen müssen objektbezogen, betragsmäßig und zweckgebunden sein; Freistellung darf nicht ausgehöhlt werden. | 🔴 |
| Änderungsvollmacht über eigene Einheit oder Nutzungsrechte | § 308 Nr. 4, § 307 BGB | `Planänderungen bleiben möglich.` | Triftige Gründe müssen konkret benannt sein; Wert, Nutzung, Kosten und Sondereigentum dürfen nicht einseitig verschoben werden. | 🔴 |
| Schlüssel nur gegen Vollzahlung trotz offener Mängel | § 307, § 641 Abs. 3 BGB; § 253 StGB im Einzelfall prüfen | `Besitz erst nach Geld.` | Gesetzliche Zurückbehaltung und MaBV-Zug-um-Zug-Logik dürfen nicht durch Besitzdruck entwertet werden. | 🔴 |
| Wohnflächentoleranz über 2 % zulasten des Erwerbers | § 307 BGB, Beschaffenheitsvereinbarung; Rechtsprechungsstand live verifizieren | `Kleine Messabweichungen sind unvermeidbar.` | Je stärker die Abweichung über einen echten Bagatellbereich hinausgeht, desto weniger darf die vereinbarte Fläche formularmäßig entwertet werden. | 🟠/🔴 |

### B.3 — Ausgaberegel bei AGB

Schreibe nicht nur `unwirksam`. Schreibe:

```text
Die Klausel [Paragraph/Absatz/Baubeschreibungsabschnitt] ist als AGB angreifbar, weil sie für [konkrete Einheit/Rate/Abnahme/Unterlage/Technikgewerk] [konkretes Recht] entzieht. Gesetzlicher Ausgangspunkt ist [Norm]. Die aktuelle BGH-Linie zu [Fallgruppe] stützt das, weil [Kernaussage]. Das erwartbare Gegenargument [konkretes Verkäufer-/Notarargument aus dieser Klausel] trägt nicht, weil [juristische Antwort]. Gewünschte Fassung für diesen Vertrag: [konkreter Wortlaut].
```

## Teil C — Baubeschreibung und Bausoll

### C.1 — Leitgedanke

Die Baubeschreibung ist der wirtschaftliche Kern. Wer nur `hochwertig`, `marktüblich`, `anerkannten Regeln der Technik entsprechend` oder `nach Bemusterung` bekommt, hat kein belastbares Bausoll.

Bei Bauträgern:

- § 650j BGB nicht ausgeschlossen.
- § 650k Abs. 2/3 BGB nicht ausgeschlossen.
- § 650k Abs. 1 BGB ausgeschlossen; daher vorvertragliche Unterlagen nicht unkritisch als automatisch einbezogen darstellen.
- Wegen § 311b BGB müssen wesentliche Leistungsinhalte beurkundet oder eindeutig einbezogen sein.

### C.2 — Pflichtmatrix

| Punkt | Soll | Risiko |
| --- | --- | --- |
| Version | datiert, Seitenzahl, Anlagenbezeichnung | 🔴 bei `aktuelle Fassung` |
| Mitbeurkundung | Urkunde/Anlage eindeutig Bestandteil | 🔴 bei loser Übergabe |
| Wohnfläche | Grundlage WoFlV/DIN 277, Toleranz, Raumliste | 🔴 wenn fehlt |
| Energiestandard | GEG/KfW/Effizienzhaus konkret | 🔴 bei `gesetzlicher Standard` |
| Bauweise | Tragwerk, Fassade, Dach, Dämmung, Schallschutz | 🟠/🔴 |
| Haustechnik | Heizung, Warmwasser, Lüftung, Elektro, PV, Smart-Home | 🟠 |
| Innenausbau | Böden, Türen, Fliesen, Sanitär, Malerarbeiten | 🟠/🔴 |
| Außenanlagen | Terrasse, Wege, Garten, Einfriedung, Stellplätze | 🟠/🔴 |
| Sondernutzungsrechte | Lageplan, Größe, Nutzungsinhalt | 🔴 |
| Fertigstellung | Datum oder bestimmbarer Zeitraum | 🔴 |
| Unterlagen | Statik, Energieausweis, Revisionsunterlagen, GEG/KfW-Nachweise | 🟠/🔴 |

### C.3 — Auslegung

Wenn Baubeschreibung unklar oder unvollständig ist:

1. Alle vertragsbegleitenden Umstände sammeln: Prospekt, Exposé, Verkaufsgespräch, Pläne, Visualisierungen, Bemusterung, Preisklasse.
2. Komfort- und Qualitätsstandard aus dem Gesamtvertrag bestimmen.
3. Zweifel zulasten des Bauträgers (§ 650k Abs. 2 BGB, § 305c Abs. 2 BGB).
4. Für Verhandlung konkrete Mindestqualität formulieren.

### C.4 — Typische Formulierungen

| Klausel | Befund |
| --- | --- |
| `Ausstattung mittlerer Art und Güte` | Zu unkonkret, wenn Kerngewerke nicht spezifiziert. |
| `Markenfabrikat oder gleichwertig` | Nur tragfähig mit Mindestparametern. |
| `Änderungen aus technischen Gründen vorbehalten` | Nur mit triftigen Gründen, Informationspflicht, keiner Wertminderung. |
| `Bemusterung im Standard des Bauträgers` | Budget und Auswahlumfang verlangen. |
| `Wohnfläche ca.` ohne Berechnungsgrundlage | 🔴/🟠; Minderungs-/Anpassungsmechanik verlangen. |

## Teil D — Abnahme und Mängelrechte

### D.1 — Warum Abnahme zentral ist

Abnahme betrifft:

- Fälligkeit.
- Gefahrübergang.
- Beweislast.
- Beginn der fünfjährigen Verjährung bei Bauwerken.
- Wechsel vom Erfüllungs- in das Gewährleistungsregime.

### D.2 — Sondereigentum

| Soll | Befund |
| --- | --- |
| Persönlicher Termin mit Protokoll | 🟢 |
| Mängel/Restarbeiten konkret vorbehalten | 🟢 |
| Abnahme durch Schlüsselübergabe fingiert | 🔴 |
| Abnahme trotz nicht prüfbarer Gewerke | 🟠/🔴 |
| Verzicht auf Vorbehalte | 🔴 |

### D.3 — Gemeinschaftseigentum

Leitsatz für die Analyse: Der einzelne Erwerber darf durch AGB nicht sein Recht verlieren, das Gemeinschaftseigentum selbst oder durch eine Person seines Vertrauens auf Abnahmefähigkeit zu prüfen und die Abnahme selbst zu erklären.

Kritische Klauseln:

- Erstverwalter nimmt ab.
- Bauträger benennt Sachverständigen.
- WEG-Mehrheit bindet alle Erwerber ohne individuelles Recht.
- Tochtergesellschaft/Projektpartner nimmt ab.
- Nachzügler bestätigt vergangene Abnahme.
- Kosten des bauträgernahen Abnehmers werden Erwerbern auferlegt.

### D.4 — Schlussrate

Nutze BGH VII ZR 88/25 offensiv und präzise.

Prüfung:

1. Was sagt die Ratenklausel: `vollständige Fertigstellung`, `bezugsfertig`, `abnahmereif`, `ohne wesentliche Mängel`?
2. Enthält das Abnahmeprotokoll Mängel oder Restarbeiten?
3. Verpflichtet sich der Bauträger zur Beseitigung/Ausführung?
4. Sind diese Punkte erledigt?
5. Falls nein: Schlussrate nicht fällig oder jedenfalls Einbehalt.

Nicht vorschnell nur § 641 Abs. 3 BGB anwenden. Zuerst Fälligkeit prüfen.

### D.5 — Mängelrechte

| Punkt | Verbraucherposition |
| --- | --- |
| Vor wirksamer Abnahme | Bauträger bleibt für mangelfreie Herstellung beweisbelastet. |
| Nach Abnahme mit Vorbehalt | Mängelrechte bleiben; Beweisfragen prüfen. |
| Verjährung | Bauwerk grundsätzlich fünf Jahre ab Abnahme. |
| Unwirksame Abnahmeklausel | Verwender kann sich nicht zu seinen Gunsten auf die eigene unwirksame Klausel berufen. |
| Kostenvorschuss | Bei Gemeinschaftseigentum kann GdWE/WEG-Bündelung relevant sein; aktuelle BGH-Linie prüfen. |

## Teil E — Teilungserklärung, WEG, Gemeinschaftsordnung

### E.1 — Kernrisiko

Bauträger behalten sich häufig vor, Teilungserklärung, Gemeinschaftsordnung, Untergemeinschaften, Nutzungsarten oder Flächenzuschnitte nachträglich zu ändern. Das ist für Verbraucher gefährlich, weil der wirtschaftliche Wert nicht nur an der Wohnung hängt, sondern an Stimmrechten, Kostenverteilung, Sondernutzungsrechten, Gewerbenutzung und Gemeinschaftsflächen.

### E.2 — Prüfmatrix

| Klausel | Risiko | Fundstelle |
| --- | --- | --- |
| `beliebig abändern` | 🔴 | BGH V ZR 91/25 |
| Zustimmungspflicht ohne triftige Gründe | 🔴 | § 308 Nr. 4 BGB |
| Vollmacht im Außenverhältnis unbeschränkt, Innenverhältnis weich | 🔴/🟠 | § 308 Nr. 4, § 307 |
| Änderung Nutzungszweck Gewerbe/Beherbergung | 🔴 | BGH V ZR 91/25 als Anker |
| Änderung Kostenverteilung | 🔴 | Wert-/Belastungsänderung |
| Verlegung/Verkleinerung Gemeinschaftsflächen | 🔴 | Kernleistung/WEG-Struktur |
| Technische Korrektur ohne Wertänderung | 🟢/🟠 | nur mit enger Begründung |

### E.3 — Gewünschte Fassung

```text
Änderungen der Teilungserklärung oder Gemeinschaftsordnung nach Vertragsschluss bedürfen der Zustimmung des Erwerbers. Eine Zustimmung kann nur verlangt werden, wenn ein im Vertrag einzeln benannter triftiger Grund vorliegt, die Änderung Inhalt, Umfang, Wert, Nutzbarkeit, Kostenlast, Stimmrechte, Sondernutzungsrechte und Gemeinschaftsflächen des Erwerbers nicht nachteilig berührt und dem Erwerber die Änderung in Textform mit Begründung nachgewiesen wird.
```

## Teil F — Eigentumsschutz und Insolvenz

### F.1 — Vormerkung

Die Auflassungsvormerkung ist der wichtigste dingliche Schutz. Ohne sie darf im § 3-Modell nicht gezahlt werden.

| Punkt | Soll |
| --- | --- |
| Anspruch | exakt das Vertragsobjekt, Sondernutzungen, Miteigentumsanteil |
| Rang | vereinbarte Rangstelle; keine vorrangigen, nicht übernommenen Belastungen ohne Freistellung |
| Löschung | nicht durch einseitige Erklärung des Bauträgers |
| Bedingung | keine automatische Freigabe bei streitigem Zahlungsverzug |

### F.2 — Freistellung

Die Freistellung muss auch den Fall der Nichtvollendung adressieren. Der Erwerber braucht Gewissheit, dass er nicht zahlt und trotzdem in der Bauträgerfinanzierung hängen bleibt.

### F.3 — Insolvenzcheck

| Zeitpunkt | Hauptfrage |
| --- | --- |
| Vor Zahlung | Keine Zahlung ohne § 3 Abs. 1 MaBV. |
| Nach Teilzahlung | Entspricht Zahlung tatsächlich dem Baufortschritt? |
| Nach Übergabe vor Eigentumsumschreibung | Vormerkung und Freistellung prüfen. |
| Bei § 7 MaBV | Sicherheit ziehen, Umfang/Dauer prüfen. |
| Bei Notaranderkonto | Auszahlungsberechtigung, Abtretung/Pfändung, Verwahrungsanweisung prüfen. |

## Teil G — Verhandlungspaket

### G.1 — Ton

Der Stil ist bestimmt, nicht schrill. Ziel: Der Notar soll rechtlich prüfen müssen; der Bauträger soll erkennen, dass die Klausel vor Gericht schlecht steht.

### G.2 — Struktur des Schreibens

```text
Sehr geehrte Damen und Herren,

wir nehmen Bezug auf den Entwurf vom [Datum/UR-Nr./Notar] zum Bauträgervertrag über [Projekt, Haus, Einheit, Stellplatz]. Der Entwurf ist in mehreren Punkten vor einer Beurkundung anzupassen. Die nachfolgenden Punkte sind keine Geschmacksfragen, sondern betreffen die konkrete Zahlungs-, Sicherungs-, Abnahme-, Bausoll- und WEG-Struktur dieses Vertrages sowie zwingende MaBV-Vorgaben, AGB-Kontrolle und aktuelle BGH-Rechtsprechung.

1. [Paragraph/Absatz] - [Problem bezogen auf Rate/Einheit/Unterlage/Abnahme/Technik]
Original: "[maßgeblicher Wortlaut]"
Wirkung in diesem Vertrag: [Betrag, Frist, Rate, Unterlage, Einheit, Bauteil oder WEG-Folge]
Bewertung: [Norm/Rechtsprechungsanker/Argumentationslinie bezogen auf diese Klausel]
Fundstelle: [zulässige URL oder `nicht quellenhart verifiziert`]
Erwartetes Gegenargument: [...]
Antwort: [Antwort auf genau dieses Gegenargument]
Gewünschte Fassung: [voller Ersatzwortlaut oder Streichungsanweisung für diesen Vertrag]

Wir bitten um einen überarbeiteten Entwurf bis [konkretes Datum vor Beurkundung/Zahlungsfrist]. Ohne diese Klärung ist eine Beurkundung aus Erwerbersicht nicht verantwortbar.

Mit freundlichen Grüßen
```

### G.3 — Musterargumente

| Thema | Kurzer harter Satz |
| --- | --- |
| 5 %-Sicherheit | `§ 650u Abs. 2 BGB schließt § 650m Abs. 2 BGB nicht aus; eine AGB-Klausel, die die Sicherheit nicht oder niedriger vorsieht, ist zudem an § 309 Nr. 15 lit. b BGB zu messen.` |
| Beweislast | `Die Klausel verschiebt einen Umstand aus dem Verantwortungsbereich des Bauträgers auf den Erwerber und ist nach § 309 Nr. 12 lit. a BGB unwirksam.` |
| Empfangsbestätigung | `Eine pauschale Bestätigung von Erhalt, Kenntnis oder Prüfung ist keine neutrale Dokumentation, sondern eine Tatsachenbestätigung im Sinne von § 309 Nr. 12 lit. b BGB.` |
| Abnahme GE | `Nach der aktuellen BGH-Linie darf dem einzelnen Erwerber sein eigenes Prüf- und Abnahmerecht nicht formularmäßig entzogen werden.` |
| Schlussrate | `Offene protokollierte Mängel können bei einer Klausel 'nach vollständiger Fertigstellung' bereits die Fälligkeit der Schlussrate hindern.` |
| Teilungserklärung | `Ein pauschales Änderungsrecht ohne einzeln benannte triftige Gründe ist nach § 308 Nr. 4 BGB und BGH V ZR 91/25 nicht tragfähig.` |

## Teil H — Streit, Rücktritt, Klage

### H.1 — Nach Beurkundung

Auch nach Beurkundung gilt AGB-Kontrolle. Strategie:

1. Unwirksame Klausel schriftlich beanstanden.
2. Gesetzliche Rechtslage benennen.
3. Frist zur Korrektur/Bestätigung setzen.
4. Bei Zahlung: Einbehalt begründen.
5. Bei Abnahme: Vorbehalte und eigene Sachverständige sichern.
6. Bei WEG: Beschlusslage zur gemeinschaftlichen Geltendmachung prüfen.

### H.2 — Rücktritt

Rücktritt kommt nur mit sauberem Tatbestand in Betracht:

| Grund | Prüfung |
| --- | --- |
| Bauverzug | Fälligkeit, Verzug, Fristsetzung, Entbehrlichkeit |
| Nichtleistung | erhebliche Pflichtverletzung |
| Mangel vor Abnahme | Nacherfüllungsverlangen/Frist, Zumutbarkeit |
| Unmöglichkeit | konkret darlegen |
| Insolvenz | § 103 InsO, Vormerkung, Sicherheiten |

### H.3 — Klageziele

| Ziel | Typischer Antrag |
| --- | --- |
| Mängelbeseitigung | Leistung/Nacherfüllung |
| Vorschuss | Zahlung Kostenvorschuss |
| Schlussrate abwehren | negative Feststellung oder Verteidigung im Zahlungsprozess |
| Rückzahlung | Leistungsklage nach Rücktritt/Überzahlung |
| Auflassung | Leistung auf Eigentumsumschreibung |
| Klausel | Feststellung im konkreten Streitverhältnis |
| Notarhaftung | Schadensersatz, subsidiär prüfen |

## Teil I — Nichtigkeit, § 306 BGB, Notar

### I.1 — Keine falsche Gesamtnichtigkeitsrhetorik

Bei AGB-Verstößen ist die Regelfolge § 306 BGB:

- Unwirksame Klausel entfällt.
- Vertrag bleibt im Übrigen wirksam.
- Gesetzliche Regel tritt an die Stelle.
- Keine geltungserhaltende Reduktion zugunsten des Bauträgers.

§ 139 BGB oder Gesamtnichtigkeit nur vorsichtig nennen:

| Fall | Bewertung |
| --- | --- |
| Nicht beurkundete wesentliche Leistungspflicht | Form-/Gesamtnichtigkeitsrisiko prüfen. |
| Sittenwidriges Gesamtgefüge | § 138 BGB prüfen. |
| MaBV-Zahlungsklausel falsch | regelmäßig Zahlungsklausel/ Fälligkeit, nicht automatisch Gesamtvertrag. |
| Mehrere AGB-Verstöße | starkes Verhandlungsargument, aber nicht automatisch Gesamtvertrag nichtig. |

### I.2 — Notar

Der Notar ist unparteiischer Amtsträger, nicht Interessenvertreter des Bauträgers oder Erwerbers. Bei Verbraucherverträgen sind rechtzeitige Entwurfsübersendung und Belehrung wichtig.

Prüfe:

- Wann erhielt der Verbraucher den Entwurf?
- Wurden Anlagen vollständig übersandt?
- Hat der Notar über MaBV, Vormerkung, Freistellung, Fälligkeit, Abnahme und Risiken belehrt?
- Werden pauschale Bestätigungen statt echter Belehrung verwendet?
- Ist der Notar Seriennotar des Bauträgers?

Notarhaftung nach § 19 BNotO nur als anwaltlich zu prüfende Eskalation formulieren, nicht als Automatismus.

### I.3 — Notaranderkonto und Notarhaftung trennen

Nicht pauschal behaupten, ein Notaranderkonto mache die gesamte Abwicklung unwirksam. Richtig:

1. Gibt es berechtigtes Sicherungsinteresse und wirksame Verwahrungsanweisung?
2. Wurde MaBV/Fälligkeit dadurch umgangen?
3. Wer ist empfangsberechtigt?
4. Gibt es Abtretung, Pfändung, Insolvenzfreigabe?
5. Welche Amtspflichtfragen stellt § 57 BeurkG?
6. Welche zivilrechtlichen Ansprüche bestehen unabhängig davon?

## Teil J — Großprojekt-Pattern und Fallbezug

Dieser Teil ist ein Wiedererkennungsraster für großvolumige Wohnungsbauträgerverträge. Er ersetzt keine Prüfung, sondern zwingt die Analyse, typische Serienklauseln an die konkrete Urkunde, die konkrete Einheit und die konkrete Projektorganisation zurückzubinden.

Wird eine Baubeschreibung nur lose übergeben oder nur referenziert, ist sie zur Bausoll-Prüfung ausdrücklich anzufordern. Wird sie als Anlage mitgeliefert, sind Vertragsteil und Anlage gegeneinander zu lesen: Fassung, Datum, Einbeziehung, Widerspruchsregel, Wohnflächenmethode, technische Mindestparameter und nachträgliche Fortschreibungsrechte.

| Pattern | Typischer Fundort | Sofortprüfung |
| --- | --- | --- |
| Wohnungsbauträgervertrag mit Auflassung in einer Urkunde | Überschrift, Kaufgegenstand, Bauverpflichtung, Auflassung | Vertragsart nach § 650u BGB; Beurkundungsumfang |
| Mehrere Bezugsurkunden | Teilungserklärung, Nachträge, Baubeschreibung, Planlisten | Mitbeurkundung/eindeutige Einbeziehung; Bausoll |
| Baubeschreibung mit `nach Wahl des Verkäufers`, `einfache Art und Güte`, leerem Schallschutz-/Energiewert | Baubeschreibung/Bausoll | § 650k Abs. 2 BGB (Zweifel zulasten Unternehmer), § 305c Abs. 2, § 307; konkrete Klassen, Mindeststandards und Zahlenwerte je Gewerk verlangen |
| Pauschaler Verweis auf Anlagenkonvolut | `dem Käufer bekannt`, `lag zur Einsicht vor` | § 309 Nr. 12 lit. b, § 311b, Transparenz |
| `Bezugsfertigkeit` und `vollständige Fertigstellung` vermischt | Ratenplan, Übergabe, Abnahme | MaBV, Schlussrate, BGH VII ZR 88/25 |
| Erfüllungsbürgschaft oder 5 %-Einbehalt | Zahlungsabschnitt | § 650m Abs. 2, § 309 Nr. 15, tatsächliche Übergabe der Sicherheit |
| Sonderwünsche sofort fällig | Bemusterung/Sonderwunschvereinbarung | MaBV-Umgehung, Leistung erbracht?, Transparenz |
| Pauschalierter Verzugsschaden | Fertigstellung/Verzug | § 309 Nr. 5, § 286, Anrechnung auf Schadensersatz |
| Selbstvornahme ausgeschlossen | Mängelrechte | § 307, § 637, praktische Durchsetzung |
| Weite Änderungsvollmacht | Teilungserklärung/Gemeinschaftsordnung | § 308 Nr. 4, BGH V ZR 91/25 |
| Nachzüglerklausel | Abnahme Gemeinschaftseigentum | BGH VII ZR 68/24, keine Bindung an fremde unwirksame Abnahme |
| Vormerkungslöschung bei Zahlungsverzug | Vollzug/Eigentumsschutz | § 307, Druckmittel, Insolvenzrisiko |
| Notaranderkonto als Abwicklungsersatz | Zahlungs-/Verwahrungsabschnitt | BGH VII ZB 28/20, MaBV/Fälligkeit/Empfangsberechtigung trennen |

### J.1 — Ampel aus Realfall-Pattern

Ein Pattern allein ist noch kein Ergebnis. Es ist ein Suchsignal. Der Befund wird erst rot, wenn der konkrete Wortlaut ein Recht entzieht, verschiebt oder intransparent macht.

Beispiel:

```text
Pattern: "Der Käufer bestätigt, sämtliche Bezugsurkunden erhalten und geprüft zu haben."
Prüfung: Ist das eine gesondert unterschriebene Empfangsbestätigung oder eine pauschale Tatsachenbestätigung im Vertrag?
Befund: Wenn pauschal im Vertrag, § 309 Nr. 12 lit. b BGB, 🔴.
```

### J.2 — Realitätscheck Großprojekt

Bei großen Projekten ist eine individuelle Klauseländerung oft wirtschaftlich schwer durchsetzbar. Trotzdem ist die Prüfung wertvoll:

- Vor Beurkundung: Termin verschieben, kritische Klauseln protokolliert beanstanden, Änderungswünsche schriftlich stellen.
- Bei Beurkundung trotz Einwand: Belehrung und Ablehnung der Klausel dokumentieren lassen, soweit der Notar mitwirkt.
- Nach Beurkundung: Unwirksamkeit im Streitfall einwenden; gesetzliche Lage tritt ein.
- In der WEG/GdWE: Ansprüche am Gemeinschaftseigentum kollektiv bündeln.

### J.3 — Anti-Generik-Check für jeden Befund

Vor Ausgabe jedes Befunds prüfen:

| Frage | Mindestantwort |
| --- | --- |
| Welche Klausel? | Paragraph, Absatz oder Baubeschreibungsabschnitt mit Kurzoriginal |
| Welches konkrete Risiko? | Zahlung, Abnahme, Vormerkung, Wohnfläche, Schallschutz, Baugrund, Wartung, WEG-Kosten oder anderes benanntes Risiko |
| Welche konkrete Auswirkung? | Betrag, Rate, Termin, Unterlage, Einheitsnummer, Bauabschnitt, technisches Gewerk oder Verwalter-/Bankrolle |
| Welche konkrete Änderung? | Wortlaut, Streichung, Einbehalt, Frist, Unterlagenanforderung oder Prüfvorbehalt |
| Welches Gegenargument? | Verkäufer-/Notar-/Bankargument nicht abstrakt, sondern aus der konkreten Klausellogik |

Wenn eine dieser Antworten fehlt, ist der Befund noch nicht ausgabereif.

## Teil K — Vertiefte Dogmatik

### K.1 — Vertragstyp und Mischrecht

Der Bauträgervertrag ist kein bloßer Kaufvertrag und kein bloßer Werkvertrag. § 650u BGB spaltet:

- Errichtung/Umbau: Bauvertragsrecht, soweit nicht ausgeschlossen.
- Eigentums-/Erbbaurechtsübertragung: Kaufrecht.
- Abschlagszahlungen: § 650v BGB und MaBV.
- AGB: §§ 305 ff. BGB überlagern die Vertragsgestaltung.

Prüfe deshalb nie nur eine Normschiene. Bei einer Wohnungseigentumseinheit wird der Vertragsgegenstand zusätzlich durch Teilungserklärung, Gemeinschaftsordnung, Aufteilungsplan, Baubeschreibung und Pläne geprägt. Bei Altbau- oder Sanierungsobjekten ist zu trennen: Sind die Sanierungsleistungen nach Umfang und Bedeutung neubaugleich, kann Werkvertragsrecht auch auf nicht unmittelbar angefasste Altbausubstanz ausstrahlen; bei bloßer Renovierung bleibt Werkvertragsrecht auf die konkret übernommenen Arbeiten begrenzt.

Abgrenzung:

| Struktur | Kein Bauträgervertrag, wenn … | Skill-Folge |
| --- | --- | --- |
| Generalunternehmer/Generalübernehmer | kein Eigentum oder Erbbaurecht verschafft wird | Werk-/Bauvertragsrecht ohne MaBV-Bauträgerlogik prüfen |
| Baubetreuer | der Erwerber/Bauherr im eigenen Namen Verträge schließt und der Betreuer nur organisiert | Vollmachten, Finanzierungsmittel und § 650f-Ausnahme gesondert prüfen |
| Projektsteuerer | nur Koordination/Controlling ohne eigene Bauherstellung und Eigentumsverschaffung übernommen wird | Leistungsbild, Haftung und Berichtspflichten prüfen |
| Baugruppen-GbR | mehrere Bauherren gemeinsam Grundstück und Bauleistung strukturieren | Teil M.7 anwenden; MaBV nicht anwenden |

### K.2 — Beurkundungsreichweite

Der Bauträgervertrag ist nach § 311b Abs. 1 BGB insgesamt notariell zu beurkunden. Nicht nur die Grundstücksübertragung, sondern auch alle werkvertraglichen Herstellungspflichten und wirtschaftlich zusammenhängenden Nebenabreden müssen in die Beurkundung oder in eine wirksame Bezugsurkundenstruktur. Maßgeblich ist nicht, was die Parteien formal beurkunden wollten, sondern was aus Sicht des Geschäfts wirtschaftlich zusammengehört.

Mitzubeurkunden oder als Bezugsurkunde sauber einzubeziehen sind insbesondere:

- Baubeschreibung mit Datum und Version.
- Planlisten, Aufteilungspläne, Ausführungs-/Grundrisspläne, soweit sie das Bausoll bestimmen.
- Teilungserklärung, Gemeinschaftsordnung, Nachträge, Sondernutzungsrechte.
- Vorverträge, Options- und entgeltliche Reservierungsvereinbarungen, wenn sie Erwerbsdruck erzeugen.
- Abreden über Vorausleistungen auf den späteren Bauträgervertrag.
- Sonderwünsche vor Beurkundung, soweit sie Preis, Leistung, Fläche, Sondereigentum oder Bauablauf prägen.

Bezugsurkunden nach § 13c BeurkG können Baubeschreibung, Pläne und Teilungserklärung praktikabel auslagern. Das ist kein Freibrief:

| Punkt | Skill-Prüfung |
| --- | --- |
| Bezeichnung | Ist die Bezugsurkunde mit Datum, Notar/UR-Nr., Planstand und Anlagenliste eindeutig identifizierbar? |
| Belehrung | Erstreckt sich die notarielle Belehrung nach § 17 BeurkG auch auf die Bezugsurkunde und ihre Risiken? |
| Wesentlichkeit | Werden echte Hauptpflichten nur versteckt ausgelagert, ohne in der Urkunde verständlich aufzuscheinen? |
| Zugriff | Hatte der Verbraucher den Text rechtzeitig und vollständig vor Beurkundung? |
| Widersprüche | Gibt es Rangregeln zwischen Urkunde, Baubeschreibung, Plänen, Prospekt und Teilungserklärung? |

Folgen fehlender Beurkundung sind streng zu prüfen: Verletzung der Form kann Nichtigkeit nach § 125 Satz 1 BGB i. V. m. § 311b Abs. 1 BGB auslösen; Heilung kommt grundsätzlich erst durch Auflassung und Eintragung in Betracht. Im laufenden Erwerbermandat bedeutet das: Nicht sofort mit Gesamtnichtigkeit drohen, sondern zuerst Vertragsstand, Vollzug, Eintragung und den konkreten fehlenden Bestandteil bestimmen.

Sonderwünsche:

| Zeitpunkt | Folge |
| --- | --- |
| vor Beurkundung vereinbart | grundsätzlich mitbeurkunden und in Gesamtpreis/Ratenplan einordnen |
| nach Beurkundung, ohne Grundstücks-/Sondereigentumsänderung | regelmäßig formfrei möglich, aber MaBV- und Gewährleistungslogik beachten |
| nach Beurkundung mit Änderung von Sondereigentum, Miteigentumsanteil oder Teilungserklärung | neue Beurkundungspflicht prüfen |
| Abrechnung außerhalb MaBV-Ratenplan | 🔴, wenn bauwerksbezogene Leistung vorab bezahlt werden soll |

VOB/B und Koppelungen: Eine formularmäßige Einbeziehung der VOB/B gegenüber Verbrauchern ist kein Schutzschild gegen AGB-Kontrolle. Koppelungen des Erwerbs an weitere Verträge, insbesondere Erstverwalter-, Wartungs-, Contracting- oder Finanzierungsbindungen aus dem Verkäuferumfeld, sind auf Druckwirkung, Transparenz und sachlichen Grund zu prüfen.

### K.3 — Bezugsfertigkeit, Abnahme, vollständige Fertigstellung

Nicht vermengen:

| Begriff | Bedeutung |
| --- | --- |
| Bezugsfertigkeit | Objekt kann sicher und zumutbar genutzt werden; Restarbeiten können offen sein. |
| Abnahme | Anerkennung als im Wesentlichen vertragsgerecht; Vorbehalte möglich. |
| Vollständige Fertigstellung | Alle geschuldeten Leistungen und je nach Vertrag auch protokollierte Restmängel erledigt. |

BGH VII ZR 88/25 ist hier der starke Anker: Die Schlussrate hängt am konkreten Vertragswortlaut, nicht an einer abstrakten Gleichsetzung von Abnahme und vollständiger Fertigstellung.

Bezugsfertigkeit setzt nicht nur vier Wände und Sanitärnutzung voraus. Der Zugang zur Einheit muss verkehrssicher und zumutbar sein. Fehlende Treppengeländer, offene Schächte, provisorische Bretterbrücken, ungesicherte Baustellenwege, fehlende Beleuchtung in zentralen Zugangsbereichen oder nicht nutzbare Rettungswege sind deshalb als harte Bezugsfertigkeits- und Besitzübergaberisiken zu prüfen.

### K.4 — Nachzügler

Erwerber, die nach einer vermeintlichen Abnahme des Gemeinschaftseigentums kaufen, sind nicht automatisch an eine frühere Abnahme gebunden. Formularmäßige Klauseln wie `Abnahme ist erfolgt` sind hoch angreifbar, wenn eigene Prüf- und Abnahmerechte fehlen.

Prüfraster:

| Konstellation | Einordnung |
| --- | --- |
| Erwerb kurz nach Errichtung, Arbeiten vor Vertragsschluss bereits ausgeführt | werkvertragliche Mängelrechte nicht vorschnell ausschließen; förmliche Abnahme mit Nachzügler vereinbaren und durchführen |
| Erwerb nach längerer Vermietung, Richtwert drei Jahre nach Errichtung als Warnsignal | Kaufrechtsnähe prüfen; keine automatische Bauträger-Werkvertragslogik behaupten |
| Vertrag enthält `Käufer erkennt frühere Abnahme an` | 🔴, wenn als AGB ohne eigenes Prüf-/Abnahmerecht |
| Vertrag will innerhalb kurzer Zeit nach Fertigstellung Kaufrecht statt Werkvertragsrecht vereinbaren | 🟠/🔴; Verbraucherleitbild, Umgehung und Transparenz prüfen |

Ausgabe: Beim Nachzügler immer Vertragsdatum, Fertigstellungs-/Übergabedatum, vorherige Nutzung/Vermietung, Abnahmeakte der GdWE und konkrete Klausel zitieren. Keine abstrakte Aussage `Nachzügler haben immer Werkvertragsrecht`.

### K.5 — Verzug

Für Verzug braucht es:

1. fällige Leistung.
2. Nichtleistung.
3. Mahnung oder Entbehrlichkeit.
4. Vertretenmüssen, soweit erforderlich.

Pauschale Entlastungen (`Witterung`, `Materialmangel`, `Behörden`, `Generalunternehmer`) reichen nicht. Der Bauträger muss bauablaufbezogen erklären, welches Ereignis welche konkrete Verzögerung verursacht hat.

Bei kalendarisch bestimmten Fertigstellungsterminen ist die Mahnung nach § 286 Abs. 2 Nr. 1 BGB entbehrlich. Wird der Termin später einvernehmlich verschoben, ist zu prüfen, ob für den neuen Termin erneut ein kalendermäßiger Leistungszeitpunkt vereinbart wurde oder ob Mahnung/Fristsetzung nötig wird.

§ 313 BGB ist als Bauträger-Einwendung streng zu behandeln: War die behauptete Krise bei Vertragsschluss bereits eingetreten oder absehbar, trägt der Bauträger das Kalkulations- und Organisationsrisiko grundsätzlich selbst. Nach Verzugseintritt eintretende Ereignisse entlasten nicht pauschal; mindestens braucht es einen gesonderten bauablaufbezogenen Nachweis, dass gerade dieses Ereignis die weitere Fertigstellung selbständig verzögert hat.

Restvergütung/Widerklage des Bauträgers: Schluss- oder Restzahlung ist nur fällig, wenn Abnahme vorliegt oder die Abnahmefiktion nach § 640 Abs. 2 BGB greift. Beim Verbraucher muss die Aufforderung die besondere Textformbelehrung enthalten; eine fristgerechte Abnahmeverweigerung unter Angabe mindestens eines Mangels hindert die Fiktion. Ohne Abnahme/Fiktion keine automatische Fälligkeit nach § 641 BGB.

### K.6 — Vertragsstrafe und pauschalierter Schadensersatz

Trennen:

- Vertragsstrafe: Druckmittel, meist verschuldensabhängig, AGB-Höhenkontrolle.
- Pauschalierter Schadensersatz: § 309 Nr. 5 BGB, Nachweis geringeren Schadens muss offenbleiben.
- Weitergehender Schaden: darf nicht formularmäßig unangemessen ausgeschlossen werden.

Verzugsschäden bei verspäteter Übergabe sind konkret zu erfassen, nicht pauschal als `Nutzungsausfall`:

| Schadensposition | Prüfpunkt |
| --- | --- |
| Ersatzwohnung | ortsübliche Miete, Zeitraum, Angemessenheit, Belege |
| Umzugskosten | Hin- und Rückumzug, Einlagerung, doppelte Organisation |
| Lagerkosten | nur für nicht unterbringbares Mobiliar; Zeitraum und Rechnung |
| Bereitstellungszinsen | nur für noch nicht abgerufene Darlehensvaluta; kein Sowieso-Schaden, aber von Zinsen auf bereits ausgezahlte Valuta trennen |
| doppelte Miete | Unkündbarkeit oder Zumutbarkeit der Altwohnung prüfen |
| Hotel-/Zwischenunterkunft | Erforderlichkeit und Dauer plausibilisieren |
| Nutzungsausfallschaden | nur bei fühlbarer Gebrauchsbeeinträchtigung; Größenunterschied oder Komfortmangel allein genügt nicht sicher |

Vertragsstrafe und Schadensersatz: Bei Interessenidentität wird die Vertragsstrafe nach § 341 Abs. 2 i. V. m. § 340 Abs. 2 BGB auf den weitergehenden Schaden angerechnet. Zinsen im Prozess: § 291 BGB ab Rechtshängigkeit, § 289 BGB gegen Zinseszins und § 308 ZPO zur Antragsbindung beachten.

### K.7 — Verjährung bei unwirksamer Abnahme

Bei unwirksamer Abnahmeklausel beginnt die typische Gewährleistungsverjährung nicht normal zu laufen. Die BGH-Entscheidungen VII ZR 68/24 und VII ZR 108/24 setzen zugleich eine 30-Jahres-Obergrenze für dortige Kostenvorschusskonstellationen. Nicht unbesehen auf jede Anspruchsart übertragen; Anspruch, Rechtstand und Vertragsschlussdatum prüfen.

### K.8 — Selbstvornahme

Ein formularmäßiger Ausschluss des Selbstvornahmerechts ist streng zu prüfen. In der Analyse nicht behaupten, jede Klausel sei sicher unwirksam, sondern:

- Welche Mängelrechte bleiben?
- Wird § 637 BGB praktisch entwertet?
- Ist der Käufer auf den Bauträger ausgeliefert?
- Gibt es Verzug mit Nacherfüllung?

Ampel meist 🟠/🔴 je nach Wortlaut.

### K.9 — Einstweiliger Besitzübergang

Wenn die Wohnung bezugsfertig ist, der Bauträger aber wegen streitiger Restmängel die Schlüssel zurückhält, kann einstweiliger Rechtsschutz zu prüfen sein. Hohe Hürden:

- klare Bezugsfertigkeit.
- erheblicher Nutzungsdruck.
- Einbehalt rechtlich plausibel.
- keine offenen Hauptleistungsvoraussetzungen.
- keine Selbstwiderlegung durch längeres Zuwarten, wenn Dringlichkeit behauptet wird.

Anspruchsrichtung sauber formulieren: Besitzverschaffung setzt regelmäßig unstreitige oder glaubhaft gemachte Bezugsfertigkeit, Erfüllung der fälligen Zahlungen oder ein annahmeverzugsbegründendes Zahlungs-/Hinterlegungsangebot und keine durchgreifenden Gegenrechte voraus. Das Verfahren darf die Hauptsache nicht ohne tragfähige Eilgrundlage vorwegnehmen.

### K.10 — § 650m-Sicherheit und Vormerkung

Vormerkung und 5 %-Sicherheit schützen unterschiedliche Risiken:

| Schutz | Deckt ab | Deckt nicht ab |
| --- | --- | --- |
| Vormerkung | Eigentumsübertragungsanspruch | Fertigstellungs-/Mängelrisiko |
| MaBV-Ratenplan | Keine Zahlung ohne Baufortschritt/Sicherung | Mängel nach Abnahme nur begrenzt |
| § 650m Abs. 2 | rechtzeitige Herstellung ohne wesentliche Mängel | alle sonstigen Schäden automatisch |
| § 7 MaBV | Rückgewähr-/Auszahlungsansprüche | Qualitätsstreit ohne Sicherungsfall |

Auflassungsvormerkung: Sie schützt den Übereignungsanspruch, auch insolvenzfest in der Logik des § 106 InsO. Sie schützt nicht die Bauvollendung, nicht die Mangelfreiheit, nicht Mehrkosten der Fertigstellung und nicht alle Schadensersatzpositionen.

§ 650m Abs. 2 BGB: Beim Verbraucher-Bauträgervertrag zwingend mitzudenken. Verzicht, bloß fakultativer Einbehalt oder Kostenbelastung des Erwerbers für die Sicherheit sind rot zu prüfen.

§ 7 MaBV-Bürgschaft: Sie ist Alternative zur § 3-MaBV-Ratenabwicklung, nicht dekorativer Zusatz. Häufig sichert sie Rückgewähr-/Auszahlungsansprüche, aber nicht jeden Schadensersatz wegen Mängeln oder Verzugs. Bürgschaftstext, Dauer, Bürge, Kündbarkeit und Sicherungsfall wörtlich auswerten.

Insolvenzlogik: Der Grundstücksanspruch ist über die Vormerkung zu sichern; der Werkleistungsanspruch kann in die Wahlrechtslogik des Insolvenzverwalters nach § 103 InsO geraten. Mandatsschritte: Vormerkung und Rang prüfen, Freistellungserklärung beschaffen, Insolvenzverwalter zur Erklärung auffordern, § 7-Sicherheit in Anspruch nehmen, § 650m-Sicherheit festhalten, Mehrkosten der Fertigstellung und Geschäftsführerhaftung gesondert prüfen.

### K.11 — Geschäftsführer, Vertrieb, Dritte

Nicht vorschnell persönliche Haftung behaupten. Prüfe sauber:

- eigene Täuschungshandlung.
- Prospekthaftung/Vertriebsunterlagen.
- Deliktischer Schaden.
- Vertreterwissen.
- Insolvenzverschleppung nur mit konkreten Tatsachen.

Bei MaBV-Verstößen in der Vorinsolvenzphase zusätzlich prüfen:

| Anspruchsgegner | Ansatz |
| --- | --- |
| Geschäftsführer der Bauträger-GmbH | § 823 Abs. 2 BGB i. V. m. § 3 oder § 7 MaBV als Schutzgesetz; Vorsatz, mindestens bedingter Vorsatz, konkret anhand operativer Rolle, Zahlungsanforderung und Kenntnis prüfen |
| Geschäftsführer/Vertrieb | § 823 Abs. 2 BGB i. V. m. § 263 StGB, wenn vorzeitig fällige Raten mit Täuschung über Fälligkeit, Baufortschritt oder Sicherheit vereinnahmt werden |
| Architekt/Bauleiter/Projektsteuerer | Vertrag mit Schutzwirkung zugunsten Dritter prüfen, wenn Bautenstandsbestätigungen erteilt werden und der Erwerber gerade darauf zahlt |
| Vertrieb/Prospektverantwortliche | Prospekt-/Aufklärungshaftung prüfen, wenn Baugrund, Energie, Schall, Fertigstellung oder Sicherheit vertriebsseitig falsch dargestellt wurden |

Output-Regel: Persönliche Haftung nie als Drohkulisse formulieren. Immer Tatsachenanker nennen: wer hat welche Zahlungsanforderung, Bautenstandsbestätigung oder Freistellungsaussage wann gegenüber welchem Erwerber verwendet?

### K.12 — Notar in Serienprojekten

Serienbeurkundung ist nicht automatisch pflichtwidrig. Kritisch wird es, wenn:

- Entwürfe zu spät kommen.
- Bezugsurkunden fehlen.
- der Notar erkennbare AGB-/MaBV-Risiken nicht belehrt.
- der Notar pauschale Bestätigungen protokolliert, die echte Belehrung ersetzen sollen.
- Verbrauchereinwände nicht dokumentiert werden.

Notarhaftung nach § 19 BNotO ist bei Fahrlässigkeit grundsätzlich subsidiär, bei Vorsatz nicht in gleicher Weise auf anderweitigen Ersatz zu verweisen. Für den Skill gilt:

| Pflichtfeld | Konkret zu prüfen |
| --- | --- |
| § 17 BeurkG | Belehrung über rechtliche Tragweite, insbesondere MaBV-Fälligkeit, Sicherheiten, Vormerkung, Freistellung, Abnahme und Preisanpassung |
| § 14 BNotO | unparteiische Amtsführung; keine bloße Durchleitung bauträgerseitiger Druckmuster |
| AGB-/MaBV-Kontrolle | erkennbare Unwirksamkeitsrisiken nicht ignorieren; bei kritischen Klauseln dokumentiert belehren |
| Niedriger Grundstücksanteil/erste Rate | örtliches Preisniveau und Überzahlung in der ersten MaBV-Rate als Warnpunkt prüfen |
| Freistellungserklärung | Inhalt, steckengebliebener Bau, Lastenfreistellung und Aussetzung der Fälligkeit verständlich machen |
| Preisanpassung | Erhöhungsrisiko, Lösungsrecht, Saldierung und Sicherung offenlegen |

Prozessstrategie: Bei fahrlässiger Notarpflichtverletzung in einem Prozess gegen Bauträger/Geschäftsführer an Streitverkündung denken. Bei belastbaren Vorsatzindizien kann eine Klageerweiterung oder gesonderte Inanspruchnahme zu prüfen sein. Keine Notarhaftung behaupten, ohne Urkundenstand, Belehrungsprotokoll, Kenntnislage und anderweitige Ersatzmöglichkeiten konkret zu erfassen.

## Teil L — Drei-Dokumente-Paket

Jede Vollanalyse mündet zwingend in drei getrennte Dokumente. Keine Vermischung der Sprachregister. Wenn der Nutzer nur einen Schnellscan verlangt, wird zusätzlich ein Kurzbild vorangestellt; das Drei-Dokumente-Paket bleibt der Abschluss.

### L.1 — Dokument 1: Übersendungsschreiben / Informationsschreiben an den Mandanten

Ziel: Der Verbraucher versteht in fünf Minuten, ob er unterschreiben, verschieben, nachverhandeln, zahlen, einbehalten, abnehmen oder streiten soll. Das Schreiben ist als Kanzlei-/Mandantenanschreiben formuliert und verweist auf das beigefügte Gutachten.

Aufbau:

```text
Betreff: Prüfung Bauträgervertrag [Projektname, Haus/Einheit/Stellplatz, Entwurfsdatum oder UR-Nr.] - Übersendung der ersten Einschätzung und des Gutachtens

Sehr geehrte/r [Mandant],

anbei erhalten Sie die Prüfung des Bauträgervertrags [Projekt/Haus/Einheit]. Kurz zusammengefasst:

1. Ergebnis in einem Absatz
2. Ampel-Bilanz
3. Die wichtigsten drei bis sieben Risiken
4. Was das praktisch für Zahlung, Beurkundung, Abnahme oder Besitzübergang bedeutet
5. Nächste Schritte mit konkreten Fristen
6. Hinweis auf das beigefügte Gutachten
7. Offene Unterlagen/Fragen
```

Pflichtinhalte, wenn einschlägig:

- Kein 14-Tage-Widerruf versprechen, wenn ein beurkundeter Bauträgervertrag vorliegt und § 650l BGB durch § 650u Abs. 2 BGB ausgeschlossen ist.
- Bei Preisanpassung die mögliche Mehrbelastung in Euro/Bandbreite und die fehlende Sicherheit verständlich ausweisen.
- Bei Terminverzug die Bauablauf-Darlegung und konkrete Schadenspositionen erklären, nicht nur `Verzug liegt vor`.
- Bei unwirksamer Abnahme die Folge für Verjährung und 30-Jahres-Obergrenze als anspruchsbezogenes Prüfthema darstellen, nicht als pauschales Versprechen.
- Bei Technik/Baugrund benennen, welche Unterlage fehlt und warum das für genau dieses Haus, diese Tiefgarage, diese Außenanlage oder diese Einheit relevant ist.

Stil:

- einfache Sprache.
- keine langen Normketten.
- klare Handlungsempfehlung.
- keine falsche Sicherheit.

### L.2 — Dokument 2: Mandantengutachten

Ziel: belastbare rechtliche und technische Arbeitsfassung für den Mandanten. Das Gutachten trägt das Mandantenanschreiben und das außergerichtliche Aufforderungsschreiben.

Aufbau:

```text
A. Sachverhalt und geprüfte Unterlagen
B. Quellenstand
C. Fall-Fingerabdruck
D. Vertragsart und Verbraucherstatus
E. Pflicht-Prüfblock
F. MaBV und Zahlungsplan
G. AGB-Klauselmatrix
H. Baubeschreibung/Bausoll
I. Abnahme, Schlussrate, Mängelrechte
J. HOAI/Objektüberwachung/technische Projektrisiken
K. Wirtschaft/Organisation/WEG
L. Eigentumsschutz/Insolvenz
M. Bauzeitverzug, Vertragsstrafe, Nutzungsausfall und Restvergütung
N. Notar-, Geschäftsführer-, Bauleiter- und Vertriebsrisiken
O. Gesamteinschätzung
P. Konkrete Änderungsfassung
```

Jeder rote Befund braucht Norm, Fundstelle oder klare Argumentationslinie. Nicht quellenhart verifizierte Rechtsprechungslinien werden als Prüfbedarf gekennzeichnet; keine Entscheidung, kein Datum und kein Aktenzeichen werden aus Modellwissen ergänzt.

### L.3 — Dokument 3: Außergerichtliches Aufforderungsschreiben an Bauträger und Notar

Ziel: bestimmte, verhandlungsfähige Aufforderung, die gefundenen Vertragsänderungen umzusetzen. Jede Forderung nennt kurz das Problem, die rechtliche/technische Begründung und die richtige Fassung.

Aufbau:

```text
Betreff: Bauträgervertrag [Projektname, Haus/Einheit/Stellplatz, Entwurfsdatum oder UR-Nr.] - erforderliche Anpassungen vor Beurkundung

Sehr geehrte Damen und Herren,

der Entwurf ist in folgenden Punkten vor Beurkundung anzupassen. Die notarielle Form ersetzt nicht die AGB-Inhaltskontrolle. Zwingende MaBV- und Verbraucherschutzvorgaben stehen nicht zur Disposition.

1. [Paragraph/Absatz/Baubeschreibungsabschnitt] - [konkretes Problem]
Original: [maßgeblicher Wortlaut]
Warum das so nicht geht: [kurze Begründung mit Norm/Argumentationslinie]
Gegenargument: [...]
Antwort: [Antwort auf das konkrete Gegenargument]
So muss es richtig gefasst werden: [voller Ersatzwortlaut oder Streichungsanweisung]

Frist / weiteres Vorgehen
```

Ton:

- bestimmt.
- keine Übertreibung.
- keine pauschalen Nichtigkeitsdrohungen.
- bei § 306 BGB klar: unwirksame AGB fallen weg; Gesetz gilt.
- immer konkrete Fassung liefern: bloß `bitte anpassen` genügt nicht.

Pflichtforderungen, wenn die Klausel vorkommt:

- Preisanpassung ohne Lösungsrecht/Saldierung: streichen oder mit Preisvorbehalt nach billigem Ermessen, Kalkulationsoffenlegung, Saldierung und gesicherter Lösungsmöglichkeit neu fassen.
- Abnahme durch Erstverwalter, Tochtergesellschaft, Projektsteuerer, Sachverständigen oder Erwerbervertreter: streichen oder ausdrückliches Eigenrecht jedes Erwerbers auf Prüfung und persönliche Abnahme sichern.
- Vollständige Fertigstellung ohne Außenanlagen/Restarbeiten: Definition korrigieren; Schlussrate erst nach vollständiger Fertigstellung einschließlich geschuldeter Außenanlagen und Gemeinschaftseigentumsarbeiten.
- Bautenstandsmitteilung allein durch Bauträger/Bauleiter: objektive Prüfbarkeit, angemeldete Besichtigung und Hinzuziehung eigener Sachverständiger sichern.
- Freistellung, Vormerkung oder Löschungsvollmacht unklar: Zahlungsfälligkeit aussetzen und dingliche Sicherheit unangetastet lassen, bis objektive Voraussetzungen erfüllt sind.

### L.4 — Typische Gegenargumente und Antworten

| Gegenargument | Antwort |
| --- | --- |
| `Das ist Standard.` | Standardformulare sind gerade AGB und unterliegen §§ 305 ff. BGB. |
| `Der Notar hat es beurkundet.` | Beurkundung sichert die Form, nicht automatisch die AGB-Wirksamkeit. |
| `MaBV schützt doch schon.` | MaBV, § 650m Abs. 2 und AGB-Kontrolle schützen unterschiedliche Risiken. |
| `Der Erwerber hat alles bestätigt.` | Pauschale Tatsachenbestätigungen sind nach § 309 Nr. 12 lit. b BGB unwirksam. |
| `Das Projekt braucht Flexibilität.` | Flexibilität braucht konkret benannte triftige Gründe und darf Wert/Nutzung/Kosten nicht verschlechtern. |
| `Die Schlussrate ist wegen Abnahme fällig.` | Bei `vollständiger Fertigstellung` und offenen Protokollmängeln zuerst Fälligkeit nach Vertrag und BGH VII ZR 88/25 prüfen. |
| `Der Käufer kann keinen eigenen Bauüberwacher auf die Baustelle schicken.` | Freier Baustellenzutritt ist nicht geschuldet; eine sicherheitskonforme Begleitung eigener Sachverständiger zu Bautenstand, Abnahme und Mängelprüfung darf aber nicht formularmäßig ausgehöhlt werden. |
| `Die HOAI gilt nur für den Architektenvertrag.` | Richtig, aber die HOAI-Leistungsphasen sind ein fachlich anerkanntes Organisationsraster. Der Bauträger muss ein prüfbares Bausoll, Bauüberwachung und Dokumentation sicherstellen. |
| `Baugrund und Grundwasser sind Projektumstände.` | Gerade deshalb müssen Gutachten, Auflagen, Kosten- und Verzugsfolgen offengelegt und beim Bauträger als Herstellungsverpflichtetem verortet werden, soweit nichts konkret anderes vereinbart ist. |
| `Pandemie, Lieferkette oder Wetter erklären die Verzögerung.` | Allgemeine Störungen erklären nichts. Es braucht den Bauablaufplan, das konkrete Ereignis, betroffene Gewerke, Folgevorgänge, Wiederanlaufzeit und Nachweise. |
| `Der Käufer kann bei Preiserhöhung zurücktreten.` | Rücktritt kann den Vormerkungsschutz zerstören. Ein brauchbares Lösungsrecht muss bereits geleistete Zahlungen und den Eigentumssicherungsstatus absichern. |
| `Die § 7-MaBV-Bürgschaft reicht doch.` | Nur, wenn sie den konkreten Sicherungszweck, die Dauer und alle Rückgewähr-/Auszahlungsansprüche tatsächlich abdeckt; sie ersetzt nicht beliebig § 650m Abs. 2 BGB oder die § 3-MaBV-Fälligkeit. |
| `Sonderwünsche sind Privatsache und sofort zahlbar.` | Bauwerksbezogene Sonderwünsche dürfen die MaBV-Ratenlogik nicht umgehen; Zeitpunkt, Leistung, Gewährleistung, Bausoll und Ratenplan müssen zusammenpassen. |

### L.5 — Qualitätsgate für das Paket

- Sind alle drei Dokumente getrennt?
- Enthält Dokument 1 ein echtes Übersendungsschreiben mit Hinweis auf das Gutachten?
- Stimmen Ampeln und Befunde überein?
- Hat Dokument 1 keine unnötigen Fachbegriffe?
- Hat Dokument 2 harte Quellen?
- Hat Dokument 3 zu jeder wesentlichen Forderung Problem, Kurzbegründung und konkrete richtige Fassung?
- Sind Gegenargumente vorweggenommen?
- Sind § 306 BGB und § 139 BGB sauber getrennt?
- Ist jeder Fachbefund mit Fallanker, Norm, Gegenargument und konkreter Änderung ausgegeben?

## Teil M — Vertiefte Dogmatik II

Teil M ergänzt die bisherige Karte um acht Themen, die in aktuellen Bauträgerstreitigkeiten regelmäßig den Ausschlag geben. Jeder Block ist als Werkzeug für die Klauselmatrix und für das Drei-Dokumente-Paket ausgelegt.

### M.1 — Anerkannte Regeln der Technik und DIN-Normen

Grundsatz: Ohne abweichende Vereinbarung schuldet der Bauträger als Mindeststandard die Einhaltung der anerkannten Regeln der Technik. Maßgeblich ist der Stand zum Zeitpunkt der Abnahme, nicht zum Vertragsschluss. Verstöße sind auch dann ein Mangel, wenn sich noch kein Schaden gezeigt hat.

Drei-Stufen-Modell der Technikbegriffe:

| Stufe | Anforderung | Typische Auswirkung |
| --- | --- | --- |
| Anerkannte Regeln der Technik | wissenschaftlich richtig anerkannt + in der Fachpraxis bewährt | werkvertraglicher Mindeststandard |
| Stand der Technik | aktueller Erkenntnisstand, Bewährung nicht erforderlich | umweltrechtlich, sicherheitsrechtlich, vertraglich nur bei ausdrücklicher Vereinbarung |
| Stand von Wissenschaft und Technik | theoretisch machbarer Spitzenstand | praktisch nur in Hochrisikobereichen geschuldet |

DIN-Normen und vergleichbare Regelwerke (VDI-Richtlinien, VDE-Bestimmungen) sind **keine** Rechtsnormen, sondern privatrechtliche Empfehlungen. In der bauvertragsrechtlichen Rechtsprechung des für Werkvertragsrecht zuständigen Zivilsenats gilt **keine Vermutung**, dass DIN-Normen die anerkannten Regeln der Technik wiedergeben. Im Einzelfall ist sachverständig zu prüfen, ob die jeweilige Norm den anerkannten Stand abbildet — oder nur einen Branchenkompromiss.

Senatsdifferenzierung als Quellenpflicht: Die Linie des für Grundstücks- und Wohnungseigentumssachen zuständigen Senats zu DIN-Normen im wohneigentumsrechtlichen Binnenverhältnis darf nicht in den Werkvertragsstandard des Bauträgervertrags hinübergezogen werden. Wenn eine Antwort sich auf diese Differenz stützt, wird sie vor Ausgabe live mit zulässiger Fundstelle verifiziert oder als Prüfbedarf markiert.

Bauträger-Klauselmuster und Befund:

| Klausel | Befund |
| --- | --- |
| „Anerkannte Regeln der Technik zum Vertragsschluss" | 🔴 (verschiebt das Risiko auf den Erwerber). Gewünscht: „zum Zeitpunkt der Abnahme". |
| „Anerkannte Regeln der Technik zum Tag der Baugenehmigung" | 🔴 (noch früherer Stichtag). |
| „DIN-Normen in der zum Vertragsschluss geltenden Fassung" | 🔴; DIN ist nicht automatisch anerkannte Regel der Technik. |
| „Energetische Anforderungen nach geltendem Recht" ohne konkrete Klasse | 🔴 (Bausoll-Lücke; gewünscht: KfW-/Effizienzhaus-Klasse oder vergleichbarer Standard). |
| Bedenken-/Aufklärungsklausel: Abweichung von aaRdT nur bei dokumentierter Belehrung | 🟢 (verhandlungsfähig). |

Verhaltensregel bei Änderung der anerkannten Regeln zwischen Vertragsschluss und Abnahme: Der Bauträger muss den Erwerber über die Änderung und die Folgen aufklären; der Erwerber wählt zwischen (a) Einhaltung des neuen Standards mit gegebenenfalls Mehrkostenabrechnung über die jeweils einschlägige Vergütungsregel und (b) Beschaffenheitsvereinbarung nach unten unter ausdrücklicher Inkaufnahme der Folgen. Beim Globalpauschalvertrag liegt das Risiko der zwischenzeitlichen Standardentwicklung grundsätzlich beim Bauträger; eine Anpassung nach den Grundsätzen über die Störung der Geschäftsgrundlage scheidet typisch aus.

In der Gewährleistungsphase richtet sich die Mängelbeseitigung nach den anerkannten Regeln **zum Zeitpunkt der Beseitigung**, nicht zum Zeitpunkt der Abnahme. Mehrkosten infolge gestiegener Anforderungen sind keine Sowieso-Kosten; ein bleibender Mehrwert kann eine Ausgleichspflicht des Erwerbers begründen.

Bedenkenhinweis: Der Bauträger kann Mängelrisiken aus ungeeigneten Vorleistungen, Eigenleistungen oder nachträglichen Erwerberwünschen nicht still auf den Erwerber verschieben. Er muss konkret, verständlich und dokumentiert warnen: welches Bauteil, welche Vorleistung, welche technische Regel, welche Folge für Gewährleistung, Termine und Kosten. Ohne solchen Hinweis bleibt die rote Ampel bestehen.

Bestandsobjekte und Sanierungen: Beim Altbau ist nicht automatisch Neubaustandard geschuldet. Entscheidend ist, welches Bauteil der Bauträger erneuert, welches System unangetastet bleibt, welche Sanierungsqualität versprochen wurde und ob die Sanierung nach Umfang und Bedeutung neubaugleich ist. Der Skill darf weder den Bestandscharakter gegen den Erwerber überdehnen noch unmögliche Neubaustandards für nicht bearbeitete Altsubstanz versprechen.

Sonderregel im wohnungseigentumsrechtlichen Binnenrecht: Der für Sachenrecht zuständige Senat zieht DIN-Normen — insbesondere zum Mindest-Schallschutz — als Auslegungshilfe heran. Diese Linie betrifft nachbarrechtliche Rücksichtnahmepflichten zwischen Wohnungseigentümern, **nicht** den bauvertragsrechtlichen Mindeststandard zwischen Bauträger und Erwerber. Eine Übertragung dieser Wohnungseigentums-Maßstäbe auf die Bauträger-Werkleistung ist unzulässig; der bauvertragsrechtliche Standard liegt regelmäßig höher als der wohneigentumsrechtliche Minimal-Schallschutz.

Für die Klauselmatrix folgt: Jede vom Bauträger formulierte Verengung der anerkannten Regeln der Technik auf einen früheren Stichtag, auf bloßen DIN-Verweis oder auf ein „mittlere Art und Güte"-Auffangregime ohne konkrete Mindestklasse ist als 🔴 zu führen, mit Verweis auf § 633 Abs. 2 BGB und das BGB-Werkvertragsverständnis vom Werkmangel.

### M.2 — Vollständige Fertigstellung nach § 3 Abs. 2 MaBV

Die letzte Rate (3,5 %) wird nicht schon bei Bezugsfertigkeit fällig, sondern erst bei vollständiger Fertigstellung. Vollständige Fertigstellung bedeutet: sämtliche vertraglich geschuldeten Leistungen erbracht — einschließlich der **Außenanlagen**, sonstiger Restarbeiten am Gemeinschaftseigentum und aller Bestandteile des Bausolls. Eine vertragliche Verengung des Begriffs (z. B. „Außenanlagen gehören nicht zur Fertigstellung") ist mit dem Schutzzweck der MaBV unvereinbar.

Wesentliche Mängel stehen der vollständigen Fertigstellung entgegen. Bei unwesentlichen Mängeln und Protokollmängeln zuerst den Vertrag auslegen: Bindet der Vertrag die letzte Rate an die Beseitigung protokollierter Mängel/Restarbeiten, kann bereits die Fälligkeit fehlen (BGH VII ZR 88/25). Fehlt eine solche Fälligkeitsbindung, bleibt jedenfalls das Zurückbehaltungsrecht des Erwerbers in Höhe des Doppelten der voraussichtlichen Mängelbeseitigungskosten (§ 641 Abs. 3 BGB) zu prüfen.

Zentrale Praxisaussagen:

| Konstellation | Folge |
| --- | --- |
| Schlussrate vor vollständiger Fertigstellung angefordert | 🔴; verstoßen wird gegen § 3 Abs. 2 MaBV i. V. m. § 12 MaBV, § 134 BGB; die Annahme ist verboten, gezahlte Beträge können nach § 817 Satz 1 i. V. m. § 818 Abs. 2 BGB zurückverlangt werden |
| „Außenanlagen außerhalb der Fertigstellungsrate" | 🔴; Außenanlagen gehören zur Fertigstellung, soweit vertraglich geschuldet |
| „Vollständig fertiggestellt" wenn Bezugsfertigkeit + Schlüsselübergabe vorliegt | 🔴; Fertigstellung ≠ Bezugsfertigkeit |
| Wesentliche Mängel am Gemeinschaftseigentum noch offen | Fertigstellungsrate nicht fällig, Rückforderbarkeit gegebener Zahlungen |
| Nur unwesentliche Protokollmängel | Vertrag zuerst auslegen: bei ausdrücklicher Beseitigungspflicht kann die Schlussrate noch nicht fällig sein; sonst mindestens Zurückbehaltungsrecht nach § 641 Abs. 3 BGB |
| Aufspaltung der Fertigstellungsrate in zwei Stufen (z. B. 2 % + 1,5 %) zur Sicherung definierter Restarbeiten | grundsätzlich denkbar; in einem klar abgegrenzten Sieben-Raten-Plan zulässig, wenn jede Stufe einem konkreten Bauablauf entspricht |
| Schlussrate-Klausel bindet Fälligkeit an einseitige Bauträgerbestätigung | 🔴; Empfängerhorizont, § 305c Abs. 2 BGB |

Praxisregel für das Mandat: Zahlungen auf die Fertigstellungsrate **nicht** leisten, solange Restarbeiten am Gemeinschaftseigentum offen sind, wesentliche Mängel beanstandet wurden oder der Vertrag die Schlussrate an die Erledigung protokollierter Punkte knüpft. Ein Bautenstands-Vermerk eines bauträgerunabhängigen Sachverständigen ist die saubere Grundlage. Bei bereits gezahlten Beträgen ist die Rückforderung über § 817 Satz 1 BGB i. V. m. § 818 Abs. 2 BGB zu prüfen; ein Mängelbeseitigungs-/Restarbeitsbudget begrenzt die Rückforderung nicht starr, ist aber argumentativ relevant.

### M.3 — Preisanpassungsklauseln und Krisenrisiko

Bauträgerverträge sind regelmäßig AGB im Sinn der §§ 305 ff. BGB, auch wenn ein Notar sie entworfen hat oder aus seiner Mustersammlung verwendet. Individualvereinbarungen werden in der Praxis selten erreicht; bloßes Verhandeln reicht nicht. Der Bauträger muss die Klausel ernsthaft zur Disposition stellen und Änderungen tatsächlich zulassen — typisch erkennbar an dokumentierten Vertragstextänderungen.

Preisanpassungsklauseln sind keine reinen Preisabreden und unterliegen damit der AGB-Inhaltskontrolle. Das gesetzliche Recht zur Anpassung wegen Störung der Geschäftsgrundlage scheidet typisch aus, wenn die Krisenlage bei Vertragsschluss bereits absehbar war oder das Vertragsverständnis ein gedeckeltes Budget des Erwerbers vorsieht. Eine außerordentliche Kündigung durch den Erwerber nach § 648a BGB ist beim Bauträgervertrag durch § 650u Abs. 2 BGB ausgeschlossen.

Wirksamkeitsanforderungen an eine Preisanpassungsklausel im Verbraucher-Bauträgervertrag:

| Anforderung | Wirksamkeitsfolge |
| --- | --- |
| Keine kurzfristige Erhöhung innerhalb der ersten vier Monate (§ 309 Nr. 1 BGB) | sonst unwirksam |
| Anpassung nur bei höherer Gewalt / unvorhersehbaren Ereignissen, nicht bei Kalkulationsfehlern, Lieferantenwechsel, Personalengpässen ohne Krisenbezug | sonst unwirksam wegen unangemessener Benachteiligung |
| Nur tatsächliche Mehrbelastung weitergeben, kein zusätzlicher Gewinn, kein Inflationsausgleich, keine Bauträger-Marge | sonst unwirksam |
| Saldierungsgrundsatz: gesunkene Kostenbestandteile sind dem Erwerber als Preissenkung weiterzugeben | sonst unwirksam wegen Verschiebung des Äquivalenzverhältnisses |
| Transparenz: Anlass, Bezugsgrößen, Berechnungsweg klar und überschaubar | sonst unwirksam wegen Verstoßes gegen § 307 Abs. 1 Satz 2 BGB |
| Lösungsrecht des Erwerbers ab einer Schwelle | unentbehrlich; ohne Lösungsrecht regelmäßig unwirksam |

Zur Wahl des Lösungsrechts: Ein Rücktrittsrecht des Erwerbers reicht regelmäßig **nicht** aus, weil mit dem Rücktritt der Übereignungsanspruch entfällt und damit die Auflassungsvormerkung erlischt (Schutzlücke des Vormerkungsmodells). Sachgerecht ist ein vertraglich vereinbartes Recht zur Teilkündigung der werkvertraglichen Leistung — beim Geschosswohnungsbau praktisch nur gemeinsam mit allen Erwerbern ausübbar — oder eine vertragliche Aufhebungsregel mit ausdrücklicher Sicherheit für die bereits geleisteten Zahlungen.

Vorzugswürdige Klauselform: **Preisvorbehalt** nach billigem Ermessen (statt mathematischer Kostenelemente-Klausel). Anlass und Modus müssen so klar formuliert sein, dass der Erwerber bei Vertragsschluss erkennt, in welchen Krisenlagen und in welchem Rahmen sich der Preis ändern kann. Die konkrete Kalkulation muss der Bauträger im Anpassungsfall offenlegen.

Befundkategorien für die Klauselmatrix:

| Befund | Ampel |
| --- | --- |
| Preisanpassung ohne Lösungsrecht | 🔴 |
| Preisanpassung ohne Saldierung (nur Erhöhung, keine Senkung) | 🔴 |
| Preisanpassung in den ersten vier Monaten zulässig | 🔴 |
| Mathematische Kostenelemente-Klausel ohne offengelegte Kalkulation | 🔴 / 🟠 |
| Preisvorbehalt nach billigem Ermessen, höhere Gewalt, mit Saldierung und Lösungsrecht ab Schwelle | 🟢 |

Notarpflicht: Bei der Beurkundung muss der Notar den Erwerber ausdrücklich auf das Preisanpassungsrisiko hinweisen. Fehlt der Hinweis bei einer für den Erwerber überraschenden Klausel, ist eine Notarhaftungsfrage offen.

### M.4 — Verbraucherbauvertrag im engeren und im weiteren Sinn

Der Verbraucherschutz bei Bauverträgen ist in Deutschland zweispurig:

| Spur | Anwendungsbereich | Kernregelungen |
| --- | --- | --- |
| Verbraucherbauvertrag im engeren Sinn (§ 650i BGB) | Bau eines neuen Gebäudes oder erhebliche Umbaumaßnahmen, die mit einem Neubau vergleichbar sind | Baubeschreibungspflicht (§ 650j BGB i. V. m. Art. 249 EGBGB), Auslegungsregeln (§ 650k Abs. 2/3 BGB), 5 %-Sicherheit (§ 650m Abs. 2 BGB), Pflicht zur Übergabe von Planungs- und Nachweisunterlagen (§ 650n BGB), Widerrufsrecht außerhalb der Beurkundung (§ 650l BGB) |
| Verbraucherbauvertrag im weiteren Sinn | Verträge zwischen Verbraucher und Unternehmer über Bauleistungen, die nicht unter § 650i BGB fallen (Einzelgewerke, untergeordnete Bauwerke, größere Renovierungen) | Allgemeine Informationspflichten der §§ 312 ff. BGB, situative Widerrufsrechte bei Fernabsatz/Außergeschäftsraumverträgen |

Konsequenzen für den Skill:

- **Beim Bauträgervertrag mit Auflassung in einer Urkunde** gilt § 650l BGB nicht; die Beurkundung ersetzt das Widerrufsrecht. Das ist im Mandantenanschreiben transparent zu machen — keine falschen Hoffnungen auf 14-Tage-Widerruf.
- **Einzelgewerkvergabe** (z. B. der Verbraucher beauftragt direkt mehrere Handwerker zum Bau seines Einfamilienhauses): Die Einordnung als Verbraucherbauvertrag im engeren Sinn ist umstritten, hat aber gewichtige Argumente für sich. Vertretbar ist, die Einzelgewerkvergabe als Verbraucherbauvertrag i. e. S. zu behandeln, wenn die Beauftragung zeitlich gebündelt erfolgt und für die einzelnen Handwerker erkennbar ist, dass sie zu einem Neubau beitragen.
- **Baubeschreibungspflicht** nach § 650j BGB i. V. m. Art. 249 EGBGB greift unabhängig von der Beurkundung. Die Baubeschreibung wird über § 650k Abs. 1 BGB regelmäßig Vertragsinhalt — beim **reinen** Verbraucherbauvertrag. Beim Bauträgervertrag ist § 650k Abs. 1 BGB durch § 650u Abs. 2 BGB ausgeschlossen; die Baubeschreibung wird daher nur dann Vertragsinhalt, wenn sie konkret mitbeurkundet oder ausdrücklich einbezogen ist.
- **§ 650k Abs. 2/3 BGB** (Auslegung lückenhafter Baubeschreibungen zulasten des Unternehmers, verbindlicher Fertigstellungstermin) gilt **auch beim Bauträgervertrag** weiter — eine zentrale Verbraucherwaffe, die in Klauselmatrizen aktiv eingesetzt werden sollte.
- **§ 650n BGB** verpflichtet zur Übergabe der Planungs- und Nachweisunterlagen vor Ausführung und spätestens mit Fertigstellung. KfW-/GEG-Nachweise, Brandschutzgutachten, Schallschutznachweise gehören dazu. Klauseln, die diese Pflicht verkürzen, sind unwirksam.

Falle bei der Anwendungsbereich-Diskussion: Die Privilegierung des § 650f Abs. 6 Nr. 2 BGB (Verbraucher muss keine Bauhandwerkersicherung stellen) ist an den Verbraucherstatus geknüpft, nicht zwingend an einen Verbraucherbauvertrag i. e. S. Auch beim klassischen Bauträgervertrag mit Verbraucher als Erwerber besteht keine Pflicht des Erwerbers, dem Bauträger eine Bauhandwerkersicherung zu stellen.

### M.5 — Folgen unwirksamer Abnahme: die 30-Jahres-Linie

Eine in AGB enthaltene Abnahmeklausel ist nach aktueller Rechtsprechung des für das Werkvertragsrecht zuständigen Zivilsenats regelmäßig unwirksam, wenn sie

- die Abnahme einer im Lager des Bauträgers stehenden Person überträgt (Erstverwalter, Tochtergesellschaft, Projektsteuerer, vom Bauträger benannter Sachverständiger),
- oder den einzelnen Erwerber von der eigenen Prüfung und Abnahmeerklärung ausschließt,
- oder eine kollektive Bindung des Erwerbers an die Abnahmeerklärung Dritter erzeugt.

Auch bei jederzeit widerruflicher Bevollmächtigung Dritter zur Abnahme ist die Klausel angreifbar, wenn der Erwerber nicht ausdrücklich darauf hingewiesen wird, dass er die Abnahme persönlich erklären und die Vollmacht jederzeit widerrufen kann.

Rechtsfolgen einer unwirksamen Abnahmeklausel und einer auf ihr beruhenden faktischen „Abnahme":

| Stufe | Inhalt |
| --- | --- |
| Klausel | unwirksam nach §§ 307 ff. BGB |
| „Abnahme" auf der Grundlage dieser Klausel | regelmäßig ebenfalls unwirksam; der Bauträger kann sich als Verwender der Klausel auf die Unwirksamkeit der von ihm gestellten Regel nicht berufen (Grundsatz der personalen Teilunwirksamkeit) |
| Konkludente Abnahme durch rügelose Nutzung oder Zahlung | regelmäßig nicht ausreichend, solange der Erwerber von einer wirksamen Abnahmeerklärung Dritter ausging |
| Verjährungsbeginn der Mängelrechte | nicht angelaufen; der Bauträger kann sich gegenüber dem Erwerber nicht auf den Beginn der fünfjährigen Mängelverjährung berufen |
| Höchstgrenze | In den aktuellen BGH-Konstellationen zu unwirksamen Abnahmeklauseln wurde für die Durchsetzung von Kostenvorschussansprüchen eine 30-Jahres-Obergrenze herangezogen. Nicht pauschal auf jede Anspruchsart übertragen; Anspruch, Zeitpunkt, Rechtsstand und Verhalten der Parteien prüfen. |
| Verwirkung | nur in engen Ausnahmefällen; ein schutzwürdiges Vertrauen des Bauträgers liegt typisch nicht vor, weil er die Lage durch die unwirksame Klausel selbst herbeigeführt hat |

Folgerung für die Nachholung der Abnahme: Der Bauträger kann die Erwerber nachträglich zur Abnahme auffordern. Für die Frage der Abnahmereife gilt dann eine **ergänzende Vertragsauslegung**: Maßstab ist nicht mehr der ursprünglich vereinbarte Neuzustand, sondern das, was redliche Parteien bei Berücksichtigung von Zeitablauf und bestimmungsgemäßer Nutzung vereinbart hätten. Alters- und nutzungsbedingte Verschleißerscheinungen stehen der Abnahmereife dann nicht entgegen.

Strategische Konsequenzen für Mandate:

| Mandantenrolle | Hebel |
| --- | --- |
| Erwerber mit alter Anlage (Abnahme über bauträgernahe Person erfolgt) | Mängel der letzten Jahre noch prüfen; Verjährungsbeginn und 30-Jahres-Obergrenze anspruchsbezogen bewerten |
| Gemeinschaft der Wohnungseigentümer | Vergemeinschaftungsbeschluss; Mängelrügen wirken erst ab Beschluss verjährungshemmend, nicht rückwirkend |
| Bauträger mit Altprojekten | Erwerber zur Nachholung der Abnahme auffordern; selbständiges Beweisverfahren gegen Nachunternehmer einleiten, um Verjährung der eigenen Regressansprüche zu hemmen; Abgeltungsvergleich mit der Gemeinschaft prüfen |

Wichtige Differenzierungen:

- **Aktuelles Recht (Verträge ab 1.1.2002)**: Mängelrechte vor Abnahme bestehen grundsätzlich nicht; der Erwerber hat ohne Abnahme nur Erfüllungsansprüche. Allerdings ist es dem Bauträger über den Grundsatz der personalen Teilunwirksamkeit verwehrt, sich auf die fehlende Abnahme zu berufen. Mängelrechte sind daher praktisch durchsetzbar, als wäre wirksam abgenommen worden — einschließlich Kostenvorschuss, Minderung und Schadensersatz.
- **Berechtigte vorläufige Abnahmeverweigerung**: Wenn der Erwerber die Abnahme zu Recht verweigert, weil das Werk nicht abnahmereif ist, gelten die Grundsätze der personalen Teilunwirksamkeit nicht. Hier kann die regelmäßige Verjährung von Ansprüchen wegen Schlechtleistung schon vor der fünfjährigen Mängelverjährungsfrist eintreten — eine systematische Asymmetrie, die im Schrifttum offen umstritten ist. Praxis: Erwerber sollte parallel die nachträgliche Abnahme erklären, um die fünfjährige Frist mit dem Sicherheitsanker zu eröffnen.
- **„Vergessene" Abnahme**: Ist die Abnahme schlicht unterblieben (kein Klauseldefekt, keine konkludente Abnahme, keine berechtigte Verweigerung), gilt für die Abnahmereife ebenfalls die ergänzende Vertragsauslegung; Anknüpfungspunkt ist regelmäßig der Zeitpunkt der Übergabe.

Für den Klauselmatrix-Output: Jede AGB-Abnahmeklausel zugunsten einer im Lager des Bauträgers stehenden Person oder mit einer kollektiven Bindung der Erwerber ist 🔴 zu führen, mit Hinweis auf die aktuelle BGH-Linie, die mögliche personale Teilunwirksamkeit und die anspruchsbezogen zu prüfende Höchstgrenzen-Logik. Im Schreiben an Bauträger und Notar (Teil L) ist die Klausel zur Streichung zu verlangen, hilfsweise so umzuformulieren, dass jeder Erwerber das ausdrückliche Recht behält, das Gemeinschaftseigentum selbst oder durch eine Person seines Vertrauens zu prüfen und die Abnahme persönlich zu erklären.

### M.6 — Bauablaufbezogene Darlegung bei Verzug

Wenn der vertragliche Fertigstellungstermin überschritten wird und der Bauträger sich auf höhere Gewalt, Pandemielage, Lieferengpässe, Streik, Witterung, Personalmangel oder „sonstige unabwendbare Umstände" beruft, ist sein Vortrag substanziiert zu prüfen. Eine pauschale Berufung reicht nicht.

Anforderungen an die Darlegung des Bauträgers:

| Element | Inhalt |
| --- | --- |
| Bauablaufplan | Welcher Arbeitsablauf war geplant? Mit welchen Vorgängen? Welche Pufferzeiten? |
| Konkretes Ereignis | Welches Ereignis hat den Ablauf gestört? Genaues Datum, genaue Beschreibung, vorzugsweise mit Belegen (Lieferantenkorrespondenz, Behördenbescheide, Wettergutachten, Personalmeldungen) |
| Auswirkung | Wie und in welchem zeitlichen Umfang hat das Ereignis konkret welchen Vorgang gestört? |
| Folgen | Welche Folgevorgänge waren betroffen? Wurde versucht, durch Umdisposition gegenzusteuern? |
| Anpassungs- und Wiederanlaufzeit | Wie lange war die Wiederaufnahme nach Wegfall der Störung erforderlich? |

Reicht die Darlegung nicht, **bleibt** der Bauträger im Verzug ab dem ursprünglich vereinbarten Termin. Verzugsschäden sind dann nach § 286 BGB ersatzfähig — Miete für Ersatzwohnung, Bereitstellungszinsen auf noch nicht abgerufenes Darlehen, doppelte Mietbelastung, Lagerkosten, Umzugskosten, Hotelkosten. Bereitstellungszinsen sind dabei kein Sowieso-Schaden; sie wären bei rechtzeitiger Leistung gerade nicht angefallen.

Vertragsstrafe und pauschalierter Schadensersatz: Beide Instrumente kompensieren regelmäßig denselben Verzugsschaden; bei Interessenidentität wird der eine auf den anderen angerechnet. Eine Klausel, die den weitergehenden Schadensersatz auf Vorsatz und grobe Fahrlässigkeit beschränkt, ist auf ihre Vereinbarkeit mit § 309 Nr. 7 BGB zu prüfen.

Eine vertragliche Klausel, die für den Eintritt des Verzugs eine zusätzliche, gesetzlich nicht vorgesehene Mahnung mit langer Nachfrist und Einschreiben verlangt, weicht vom gesetzlichen Leitbild des § 286 Abs. 2 Nr. 1 BGB ab und ist nach § 307 BGB regelmäßig unwirksam.

### M.7 — Baugruppen-GbR als Alternative zum Bauträger

Wer als Verbraucher bewusst keinen Bauträgervertrag schließen will, kann sich mit anderen zu einer Baugruppe (typisch in der Form einer GbR) zusammenschließen und das Grundstück gemeinsam erwerben, gemeinsam bebauen und anschließend in eine WEG aufteilen. Der Skill prüft solche Konstellationen mit veränderten Maßstäben:

| Punkt | Bauträgervertrag | Baugruppe |
| --- | --- | --- |
| Vertragspartner | ein Bauträger | mehrere Verbraucher als Gesellschafter |
| Bauherreneigenschaft | Bauträger ist Bauherr; Erwerber kauft das fertige Werk | jeder Gesellschafter ist Bauherr |
| MaBV | gilt | gilt nicht (keine Bauträgerleistung) |
| Insolvenzrisiko | Insolvenz des Bauträgers trifft alle Erwerber im Projekt | aufgeteilt auf einzelne Handwerker; Gegenstück: persönliche Risiken der Gesellschafter |
| Beurkundungspflicht des Gesellschaftsvertrags | nicht einschlägig | grundsätzlich beurkundungspflichtig, soweit der Vertrag die Verpflichtung zur Übertragung von Sondereigentum oder zur Aufgabe von Bruchteilseigentum enthält; Heilung nach § 311b Abs. 1 Satz 2 BGB ist beim WEG-Modell typisch ausgeschlossen, weil eine wirksame Auflassung an die Gesellschafter erst nach Vollzug der Teilungserklärung erfolgt |
| Haftung | Bauträger haftet, Erwerber zahlen | Gesellschafter haften nach den Grundsätzen der GbR; nach geltendem Personengesellschaftsrecht ist eine Haftungsbeschränkung im Außenverhältnis nur eingeschränkt möglich |

Notarielle und vertragliche Prüfpunkte beim Baugruppenmodell:

| Prüfpunkt | Inhalt |
| --- | --- |
| Beurkundung des Gesellschaftsvertrags | erforderlich, soweit ein Eigentumsübertragungsbezug besteht; sicherer Weg: Vollbeurkundung des Gesellschaftsvertrags |
| Rumpfgründung als Alternative | Gesellschaft wird ohne Grundstücksbezug formfrei gegründet; alle eigentumsbezogenen Vereinbarungen werden später in beurkundeter Form ergänzt — hohes Risiko der Lückenhaftigkeit |
| Bruchteilseigentum als Alternative | Erwerb des Grundstücks in Bruchteilseigentum, Ausbau als Werkvertrag; Teilungserklärung folgt — saubere, aber komplexe Variante |
| Beitragspflichten | planmäßige Zahlungen plus Nachschusspflicht regeln; bei privaten Verbrauchern Nachschusspflicht eng begrenzen |
| Übertragung von Gesellschaftsanteilen | Bindung an Mehrheitsbeschluss; Vorkaufsrechte; Anti-Spekulationsklauseln |
| Freiwilliges und unfreiwilliges Ausscheiden | Kündigung nach § 725 BGB; Ausschluss aus wichtigem Grund; Abfindungsregelungen mit klaren Bewertungsmaßstäben |
| Aufspaltung des Grundstücks-Kaufvertrags | bei großer Mitgliederzahl praktikabel; berufsrechtlich (Notar) und insolvenzrechtlich zulässig, wenn Angebot und Annahme rechtssicher dokumentiert sind |
| Finanzierungsgrundschulden | typischerweise einzeln pro Gesellschafter; bei gemeinsamer Globalgrundschuld besondere Sicherungs- und Auseinandersetzungsregeln |
| Teilungserklärung und Übertragung der Sondereigentumseinheiten | nach Fertigstellung; Realisierung des Bauziels jedes Gesellschafters in eine eigene WE-Einheit |

Wenn die Anfrage nicht eindeutig einen Bauträgervertrag betrifft, sondern eine Baugruppen-Konstruktion erkennen lässt (mehrere Bauherren, gemeinsamer Grundstückserwerb, gemeinsame Auftragsvergabe an Handwerker), prüft der Skill den Vertrag entlang dieser Kategorie statt entlang der Bauträger-Pflicht-Prüfblock-Logik. Im Mandantenanschreiben ist die Strukturdifferenz auszuweisen.

### M.8 — Erweiterungen der Klauselmatrix und der Antwortformate

Die folgenden Punkte ergänzen die Klauselmatrix in Teil B um aktuelle Streitfelder:

| Klauseltyp | Befund | Verhandlungsantwort |
| --- | --- | --- |
| „Anerkannte Regeln der Technik zum Vertragsschluss" | 🔴 | „zum Zeitpunkt der Abnahme; bei Änderung Hinweispflicht des Bauträgers" |
| „Geltendes Recht" als Energiestandard | 🔴 | „mindestens KfW-/Effizienzhausklasse X; Abweichung nur mit ausdrücklicher Belehrung" |
| Preisanpassung ohne Lösungsrecht des Erwerbers | 🔴 | Lösungsrecht ab Schwelle (z. B. 5 %) als gesonderte Klausel |
| Preisanpassung ohne Saldierung | 🔴 | Saldierungspflicht mit Nachweis aus Bauträger-Kalkulation |
| Verkürzung der vollständigen Fertigstellung auf Bezugsfertigkeit | 🔴 | Wortlaut „vollständige Fertigstellung einschließlich Außenanlagen und sämtlicher Restarbeiten" |
| Zusätzliche Mahnpflicht im Verzug | 🔴 | streichen; gesetzlicher § 286 BGB |
| Bauträgerklausel zur Bauablauf-„Höhere Gewalt"-Vermutung | 🔴 | konkrete Darlegung erforderlich, sonst Verzug ab Termin |
| Abnahme durch Erstverwalter / Tochtergesellschaft / Bauträger-Sachverständigen | 🔴 | streichen oder Eigenrecht des Erwerbers ausdrücklich sichern |
| Baugruppen-GbR-Vertrag ohne Beurkundung der Eigentumsbezüge | 🔴 | Vollbeurkundung oder Bruchteilsmodell mit nachgelagerter Teilung |
| Interne Projektsteuerung ersetzt Bauüberwachung | 🔴 | Nachweis LPH 8/technische Fachüberwachung und eigene Kontrollrechte des Erwerbers sichern |
| Baustellenzutritt nur mit Verkäufergenehmigung, keine Fotos, keine Sachverständigen | 🔴 | Begleiteter Zutritt zu Qualitätsgates, MaBV-Bautenstandsprüfung und Abnahme muss möglich sein |
| Baugrund-/Grundwasser-/Altlastenrisiko pauschal beim Erwerber | 🔴 | Gutachten offenlegen; Restrisiken und Mehrkosten beim Bauträger, soweit nicht konkret aufgeklärt und bepreist |
| Schallschutz/Feuchteschutz/Lüftung nur als Nutzerverhalten definiert | 🟠/🔴 | konkrete Nachweise, Wartungs-/Bedienkonzept und Mindestparameter verlangen |

Für die drei Dokumente aus Teil L gelten zusätzlich:

- **Mandantenanschreiben (L.1)**: Wenn der Vertrag Preisanpassungsklauseln oder Risiken aus geänderten anerkannten Regeln der Technik enthält, ist die finanzielle Bandbreite klar zu benennen — keine vage Aussage „kann teurer werden".
- **Gutachten (L.2)**: Die Abschnitte zu Baubeschreibung, Schlussrate und Abnahme sind um die 30-Jahres-Linie und die personale Teilunwirksamkeit zu ergänzen, soweit unwirksame Abnahmeklauseln festgestellt wurden.
- **Schreiben an Bauträger und Notar (L.3)**: Bei AGB-Preisanpassungsklauseln, Verkürzung der Fertigstellungsdefinition und Klauseln zu „anerkannten Regeln der Technik zum Vertragsschluss" ist die Streichung oder verhandlungsfähige Neufassung mit ausformulierter Wortlaut-Vorschlag zu fordern.

Ergänzungen zum Bug-Hunt (vor jeder Ausgabe):

- DIN-Norm nicht als anerkannte Regel der Technik behandeln; richtig ist die Einzelfallprüfung.
- Vollständige Fertigstellung nicht mit Bezugsfertigkeit gleichsetzen.
- Preisanpassung nicht ohne Lösungsrecht akzeptieren.
- Unwirksame Abnahmeklauseln nicht als bloßes „Beratungsproblem" abhandeln; Verjährungsbeginn und 30-Jahres-Obergrenze aber anspruchsbezogen prüfen, nicht pauschal behaupten.
- Bauablauf-Argumente der Bauträgerseite nicht ungeprüft als höhere Gewalt durchgehen lassen.
- § 650l BGB nicht für beurkundete Bauträgerverträge in Anspruch nehmen; das Widerrufsrecht greift dort nicht.
- Bauhandwerkersicherung (§ 650f BGB) nicht vom Verbraucher-Erwerber fordern; § 650f Abs. 6 Nr. 2 BGB privilegiert ihn.
- Baugruppen-GbR nicht mit Bauträgervertrag-Maßstäben prüfen; die MaBV greift nicht.

## Teil N — Wirtschaft, Organisation, HOAI und Technik

Teil N verhindert den häufigsten Praxisfehler: Ein Vertrag kann juristisch bearbeitet sein und trotzdem ein schlechtes Bauprojekt absichern. Die Analyse muss deshalb neben AGB/MaBV immer prüfen, ob Planung, Bauüberwachung, Baugrund, technische Qualität, Wirtschaft und WEG-Organisation real kontrollierbar sind.

### N.1 — Rollenmodell

Erstelle bei jeder Vollanalyse ein Rollenbild:

| Rolle | Mindestprüfung |
| --- | --- |
| Bauträger/Projektgesellschaft | Eigenkapital, Konzernbindung, Globalfinanzierung, Freistellung, Bauherreneigenschaft |
| Architekt/Objektplaner | Welche Leistungsphasen beauftragt? Wer schuldet Ausführungsplanung, Objektüberwachung und Dokumentation? |
| Fachplaner | Tragwerk, Brandschutz, Schall, Wärme/Feuchte, technische Ausrüstung, Außenanlagen, Tiefgarage |
| Bauleiter/Objektüberwacher | Unabhängigkeit, Qualifikation, Berichtswesen, Mängelverfolgung, Haftpflichtdeckung |
| Prüfingenieur/Prüfsachverständige | Statik, Brandschutz, ggf. Sonderbau-/Garagenanforderungen |
| Bodengutachter | Baugrund, Grundwasser, Altlasten, Kampfmittel, Versickerung, Baugrubenverbau |
| Generalunternehmer/Nachunternehmer | Vertragliche Schnittstellen, Insolvenz-/Austauschrisiko, Gewährleistungsdurchgriff |
| Erstverwalter/WEG | Interessenkonflikt, Abnahme, Wartungsverträge, Mängelverfolgung, Dokumentationsübergabe |

Kernfrage: Wer kontrolliert wen, wer berichtet an wen und welche Unterlagen bekommt der Erwerber oder später die GdWE? Eine rein interne Verkäuferkontrolle ist kein Ersatz für prüfbare Qualitätssicherung.

### N.2 — HOAI-Leistungsphasen als Prüfraster

Die HOAI ist primär Honorarrecht. Sie begründet nicht automatisch einen Direktanspruch des Erwerbers gegen den Architekten des Bauträgers. Sie ist aber ein belastbares Organisationsraster. § 34 HOAI nennt für Gebäude und Innenräume neun Leistungsphasen; Anlage 10.1 beschreibt die Grundleistungen.

| LPH | Inhalt | Verbrauchercheck |
| --- | --- | --- |
| 1 Grundlagenermittlung | Aufgabenstellung, Bedarf, Untersuchungsbedarf | Wurde Bedarf/Qualitätsziel dokumentiert oder nur Vertriebssprache? |
| 2 Vorplanung | Varianten, Zielkonflikte, Kostenschätzung, Terminplan | Gibt es belastbare Planungsgrundlagen, Baugrund-/Genehmigungsrisiken, Terminlogik? |
| 3 Entwurfsplanung | System- und Integrationsplanung, Kostenberechnung | Passt Baubeschreibung zu Plänen, Technik, Kosten und Prospekt? |
| 4 Genehmigungsplanung | Bauantrag, öffentlich-rechtliche Nachweise | Liegt die Baugenehmigung für das konkrete Haus vor? Sind Auflagen eingepreist? |
| 5 Ausführungsplanung | ausführungsreife Details | Ohne LPH-5-Logik sind Schall, Abdichtung, Brandschutz, Haustechnik und Details nicht prüfbar. |
| 6/7 Vergabe | Leistungsverzeichnisse, Angebotsprüfung, Vergabe | Unklare GU-/Nachunternehmer-Schnittstellen sind Insolvenz- und Qualitätsrisiko. |
| 8 Objektüberwachung | Bauüberwachung und Dokumentation | Zentral: Bautenstand, Mängeltracking, Rechnungs-/Ratenfreigabe, technische Abnahmen. |
| 9 Objektbetreuung | Mängelverfolgung nach Fertigstellung | WEG braucht geordneten Übergang, Gewährleistungsmanagement und Unterlagen. |

Gewünschte Vertragsposition: Der Bauträger muss bestätigen, dass fachlich geeignete Objekt- und Fachplaner für die erforderlichen Planungs- und Überwachungsleistungen eingesetzt werden, und der Erwerber/GdWE erhält die zur Prüfung, Abnahme, Finanzierung, Förderung und Unterhaltung erforderlichen Unterlagen.

### N.3 — Private Bauüberwachung und Sachverständige

Der Erwerber darf die Baustelle nicht beliebig betreten und keine Anweisungen an Unternehmer geben. Verkehrssicherung, Arbeitsschutz, Bauablauf und Hausrecht sind real. Daraus folgt aber nicht, dass der Bauträger jede unabhängige Kontrolle ausschließen darf.

Verhandlungsfähige Mindestlösung:

- begleiteter Baustellenzutritt zu definierten Qualitätsgates: Rohbau, Fenster/Dach, Rohinstallation, Estrich, Abdichtung/Tiefgarage, Bezugsfertigkeit, Abnahme.
- Teilnahme eines eigenen Architekten, Bauingenieurs oder Sachverständigen des Erwerbers.
- Einsicht in prüfbare Bautenstands- und Mängelberichte vor MaBV-Raten.
- Fotos der eigenen Einheit und relevanter Gemeinschaftsbereiche, soweit keine Persönlichkeits-/Sicherheitsinteressen entgegenstehen.
- keine Weisungen an Handwerker; Kommunikation über Bauträger/Objektüberwachung.
- Abnahmebegleitung für Sondereigentum und Gemeinschaftseigentum.

Klauseln, die `eigene Bautenstandskontrollen`, `private Sachverständige`, `Fotodokumentation` oder `Teilnahme an Abnahmen` pauschal ausschließen, sind als 🔴 zu führen, weil sie MaBV-Fälligkeit, Abnahmeprüfung und Mängelrechte praktisch entwerten.

### N.4 — Baugrund, Baugrube und Grundstücksrealität

Baugrundrisiken zerstören die schönste Vertragsprüfung. Der Skill prüft deshalb immer:

| Thema | Zu verlangende Unterlagen/Angaben |
| --- | --- |
| Baugrund | geotechnischer Bericht, Gründungsempfehlung, Setzungsprognose, Bodenklassen, Tragfähigkeit |
| Grundwasser | Bemessungswasserstand, Dränage-/Wannen-Konzept, temporäre Wasserhaltung, Auftriebssicherheit |
| Baugrube | Verbau, Nachbarbebauung, Erschütterung, Beweissicherung, Bauzustände |
| Altlasten | orientierende/Detailuntersuchung, Entsorgungskonzept, Deponieklassen, Kostenrisiko |
| Kampfmittel | Auskunft/Sondierung, Freigabe, Bauverzugs- und Kostenfolge |
| Niederschlagswasser | Versickerung, Rückhaltung, Überflutungsschutz, Notwasserwege |
| Tiefgarage | Abdichtung, Entwässerung, Gefälle, Chloridbelastung, Lüftung, Brandschutz |

Rote Klauselmuster:

- `Der Käufer übernimmt alle Risiken aus Baugrund, Grundwasser oder Altlasten`.
- `Gutachten dienen nur internen Zwecken und begründen kein Bausoll`.
- `Wasserhaltung, Verbau oder Entsorgung können als Mehrkosten umgelegt werden`.
- `Verzögerungen wegen Baugrund/Altlasten verlängern die Frist ohne Nachweis`.

Antwort: Baugrund und Baugrube liegen im Verantwortungsbereich des Bauträgers als Bauherrn und Herstellungsverpflichteten. Eine Risikoverlagerung ist nur denkbar, wenn der konkrete Umstand offen, verständlich, bepreist und vertraglich eng geregelt ist.

### N.5 — Technische Kernmatrix

In jeder Vollanalyse mindestens diese technischen Themen scannen:

| Bereich | Typische harte Frage |
| --- | --- |
| Tragwerk | geprüfte Statik, Prüfbericht, Ausführungsplanung, Durchbrüche/Sonderwünsche |
| Brandschutz | Konzept, Auflagen, Tiefgarage, Rettungswege, Abschottungen, Dokumentation |
| Schallschutz | Mindeststandard oder erhöhter Schallschutz? Trittschall, Installationsschall, Aufzug/Tiefgarage |
| Wärmeschutz/Energie | GEG, KfW-/Effizienzhausversprechen, Wärmebrücken, Luftdichtheit, Förderbedingungen |
| Feuchte/Abdichtung | Keller/Tiefgarage, Balkone, Flachdach, Sockel, Bäder, Duschen, Anschlüsse |
| Lüftung | Lüftungskonzept, Nutzerpflichten, Schimmelrisiko, Wartung, Nachströmung |
| Trinkwasser/Heizung | Hygiene, Zirkulation, Wärmepumpe/Fernwärme, Abrechnung, Betriebsrisiko |
| Elektro/PV/Smart Home | Zählerkonzept, Ladeinfrastruktur, Reserven, Wartung, Datenschutz |
| Aufzug/Tiefgarage | Betriebskosten, Wartung, Ersatzteile, Brandschutz, Barrierefreiheit |
| Außenanlagen | Entwässerung, Beleuchtung, Spielplatz, Pflanzung, Erhaltungspflichten |

Pauschale Verkäuferklauseln wie `Funktionsfähigkeit nur bei ordnungsgemäßem Nutzerverhalten`, `Schimmel ist kein Mangel bei falschem Lüften` oder `technische Anlagen sind keine Beschaffenheitsvereinbarung` sind nie isoliert zu akzeptieren. Sie brauchen Bedienkonzept, Nachweis, Übergabeunterlagen und dürfen das Bausoll nicht verschieben.

### N.6 — Wirtschaftliche und organisatorische Prüfung

Der Erwerber kauft nicht nur Mauerwerk, sondern ein langfristiges Organisations- und Kostenpaket.

| Thema | Prüffrage |
| --- | --- |
| Projektgesellschaft | Ist sie substanzarm? Gibt es Patronat, Muttergesellschaft, Gewährleistungsreserve? |
| Finanzierung | Globalgrundschuld, Freistellung, Auszahlungsvoraussetzungen, Bankfreigaben |
| GU-/Nachunternehmerstruktur | Wer baut tatsächlich? Austauschrecht? Insolvenz eines GU? |
| Sonderwünsche | Vorauszahlung, Schnittstellen, Gewährleistung, Terminrisiko, MaBV-Einordnung |
| Betriebskosten | Fernwärme, Contracting, Aufzug, Tiefgarage, Lüftung, Wasserhaltung, Gemeinschaftseinrichtungen |
| Wartungsverträge | Laufzeit, Kündbarkeit, Preisanpassung, Erstverwalter-Interessenkonflikt |
| Instandhaltungsrücklage | realistisch für Technik/Tiefgarage/Aufzug/Pumpen? |
| Untergemeinschaften | Kostenverteilung, Stimmrechte, Sondernutzungen, spätere Bauabschnitte |

Rote Linie: Keine Klausel darf wirtschaftliche Risiken verstecken, die den Gesamtpreis faktisch erhöhen oder die WEG über lange Wartungs-, Verwaltungs- oder Betriebspflichten an bauträgernahe Unternehmen bindet.

### N.7 — Dokumentations- und Übergabepaket

Mindestens verlangen:

- Baugenehmigung mit Auflagen für das konkrete Haus.
- geprüfte Statik/Prüfberichte, Brandschutznachweise, Schallschutz-/Wärmeschutznachweise.
- Energieausweis, GEG-/KfW-/Fördernachweise, Luftdichtheits-/Inbetriebnahmeprotokolle soweit geschuldet.
- Revisionspläne, Wartungs- und Bedienungsanleitungen, Fachunternehmererklärungen.
- Protokolle zu technischen Inbetriebnahmen: Heizung, Lüftung, Trinkwasser, Aufzug, Brandmelde-/Rauchabzugstechnik, Tiefgarage.
- Mängel- und Restarbeitenliste für Sonder- und Gemeinschaftseigentum.
- Gewährleistungs-/Ansprechpartnerliste für Gewerke.

§ 650n BGB ist der gesetzliche Anker für Planungs- und Nachweisunterlagen. Bei Bauträgern ist die Norm nicht durch § 650u Abs. 2 ausgeschlossen. Für reine Komfortunterlagen kann die Anspruchsgrundlage anders liegen; für öffentlich-rechtliche Nachweise, Förder-/Finanzierungsbedingungen und berechtigt geweckte Erwartungen ist § 650n aktiv zu prüfen.

### N.8 — Ausgabe in den drei Dokumenten

**Mandantenanschreiben:** Technik/Wirtschaft in Klartext: `Das größte Risiko ist nicht nur Klausel X, sondern dass Sie vor Zahlung und Abnahme keine unabhängige Kontrolle von Baugrund, Bautenstand und technischen Nachweisen erhalten.`

**Gutachten:** Eigener Abschnitt `HOAI/Objektüberwachung/Technik/Wirtschaft`. Jede technische rote Ampel braucht: Vertragswortlaut, praktisches Risiko, fehlende Unterlage, gewünschte Änderung.

**Schreiben an Bauträger und Notar:** Keine Fachsimpelei. Forderungen konkret:

```text
Bitte ergänzen Sie eine Regelung, wonach der Erwerber nach angemessener Voranmeldung und unter Beachtung der Sicherheitsvorgaben einen eigenen Sachverständigen zu den Bautenstands- und Abnahmeterminen hinzuziehen darf. Die Fälligkeit von MaBV-Raten darf nicht allein durch eine interne Bauleiterbestätigung des Verkäufers ausgelöst werden, sondern muss durch objektiv nachvollziehbaren Baufortschritt prüfbar sein.
```

### N.9 — Scoring

| Befund | Gewicht |
| --- | --- |
| Keine eigene/private Bautenstandskontrolle vor Raten | 🔴 |
| LPH 8/Bauüberwachung nur intern und ohne Dokumentation | 🔴 |
| Baugrund-/Grundwasser-/Altlastenrisiko beim Erwerber | 🔴 |
| Baugenehmigung oder Auflagen für das konkrete Objekt fehlen | 🔴 |
| Keine konkreten Schall-/Energie-/Feuchteschutzparameter | 🟠/🔴 |
| Erstverwalter kontrolliert Abnahme, Wartung und Mängelmanagement | 🔴 |
| Lange Wartungs-/Contractingbindung an Verkäuferumfeld | 🟠/🔴 |
| Technische Unterlagen erst `nach Ermessen` oder gar nicht | 🔴 |

## Teil O — Fachmodule Bauträgerrecht 2026

Teil O ist die verdichtete Arbeitskarte der fachlichen Erweiterung. Er wird nicht separat ausgegeben, sondern steuert, welche Prüffragen in Teil B, K, L, M und N zwingend mitzudenken sind. Alles, was auf konkrete Rechtsprechung hinausläuft und nicht bereits in den Rechtsprechungsankern mit zulässiger URL steht, wird vor Schriftsatz- oder Gutachtenverwendung live über offizielle Gerichtsseiten, `rechtsprechung-im-internet.de`, `dejure.org` oder `openjur.de` verifiziert.

### O.1 — Vorinsolvenz, MaBV-Druckmuster und Rückforderung

Wenn der Bauträger in einer angespannten Projektlage früh, großvolumig oder außerhalb sauberer MaBV-Fälligkeit Geld will, wird nicht nur der Zahlungsplan geprüft. Der Skill prüft drei Ebenen:

| Ebene | Prüfauftrag |
| --- | --- |
| Zahlungsfälligkeit | § 3 Abs. 1 MaBV vollständig? § 3 Abs. 2 MaBV-Bautenstand real erreicht? § 7 MaBV wirklich alternativ und ausreichend? |
| Druckmechanik | Schlüssel, Besitz, Sonderwunsch, Vormerkungslöschung, Mahnkosten, Verzugsdrohung oder Notartermin werden als Hebel genutzt? |
| Anspruchskette | Rückforderung verfrühter Zahlungen, Zurückbehaltung, § 650m-Sicherheit, Geschäftsführer-/Bauleiter-/Notarhaftung mit konkretem Vorsatz-/Pflichtwidrigkeitsanker |

Rote Muster: zwei Großraten, `mitgeteilte` Bautenstände, Schlussrate vor Außenanlagen, Bauleiterbestätigung ohne Erwerberkontrolle, unrichtige Genehmigungsfreiheitsbestätigung, wesentliche Abweichung von der Baugenehmigung ohne Nachtrag, Freistellungserklärung mit Lücken beim steckengebliebenen Bau, § 650m-Sicherheit als bloßes Wahlrecht, einseitige Vormerkungslöschung.

Zusatzprüfung Baugenehmigung: Ist die Genehmigung nur behauptet, ist die Monatsfrist bei Eigenbestätigung noch offen oder weicht das ausgeführte Haus wesentlich von der Genehmigung ab, wird keine Rate freigegeben. Der Skill fordert Genehmigung, Nachtragsgenehmigung, Auflagenstand und Abgleich mit Plan-/Baubeschreibungsstand.

### O.2 — Bauzeitverzug, Schadenspositionen und Restvergütung

Bei verzögerter Übergabe werden Termin, Darlegung und Schaden getrennt:

1. Kalendarischer Termin oder nur `voraussichtlich`?
2. Verschiebung wirksam vereinbart oder nur einseitig angekündigt?
3. Bauablaufbezogene Entlastung: Ereignis, Gewerk, Dauer, Folgevorgang, Wiederanlaufzeit.
4. Schadenspositionen mit Belegen: Ersatzmiete, Umzug, Lager, Hotel, doppelte Miete, Bereitstellungszinsen, Nutzungsausfall.
5. Vertragsstrafe, pauschalierter Schaden und weiterer Schaden mit Anrechnung prüfen.
6. Restvergütung des Bauträgers nur bei Abnahme, wirksamer Abnahmefiktion oder sonstiger Fälligkeitsgrundlage.

§ 313 BGB wird nur als enges Korrektiv geprüft. War die Krise bei Vertragsschluss bereits erkennbar, darf der Bauträger sie nicht als nachträgliches Überraschungsrisiko recyceln.

### O.3 — Technikrecht: DIN, anerkannte Regeln und Standardänderung

DIN-Konformität ist kein Vollbeweis für Mangelfreiheit. Der Skill trennt:

| Kategorie | Funktion |
| --- | --- |
| anerkannte Regeln der Technik | werkvertraglicher Mindeststandard; wissenschaftliche Anerkennung plus praktische Bewährung |
| Stand der Technik | höherer aktueller Erkenntnisstand; zivilrechtlich nur bei Vereinbarung oder spezieller Norm |
| Stand von Wissenschaft und Technik | Spitzenstandard für Hochrisikobereiche |

Stichtag für das Bausoll ist grundsätzlich die Abnahme. Standardänderungen zwischen Vertragsschluss und Abnahme lösen Aufklärungs- und Entscheidungsbedarf aus. Mängelbeseitigung nach Abnahme richtet sich nach dem Standard der Beseitigung; Mehrkosten werden nicht pauschal als Sowieso-Kosten abgetan, ein bleibender Mehrwert ist aber sauber zu prüfen.

### O.4 — Verbraucherbauvertrag, Bauträgervertrag und allgemeines Verbraucherrecht

Der Skill hält die Spuren auseinander:

| Spur | Bauträgerfolge |
| --- | --- |
| § 650i BGB Verbraucherbauvertrag i. e. S. | Bauträgervertrag ist eigener Typ nach § 650u BGB; nicht mechanisch gleichsetzen |
| § 650l BGB Widerruf | beim beurkundeten Bauträgervertrag durch § 650u Abs. 2 BGB ausgeschlossen |
| § 650k Abs. 2/3 BGB | bleibt beim Bauträger nutzbar; lückenhafte Baubeschreibung wird zulasten des Unternehmers ausgelegt |
| § 650n BGB | Unterlagenpflicht bleibt; GEG/KfW/Brandschutz/Schall/Statik/Nachweise aktiv verlangen |
| §§ 312 ff. BGB | nur ergänzend bei situativem Fernabsatz-/Außergeschäftsraumbezug prüfen |
| Einzelgewerkvergabe | offen und fallabhängig; nicht als entschieden ausgeben |

### O.5 — Baugruppen-GbR statt Bauträger

Wenn mehrere Verbraucher gemeinsam Grundstück und Bauleistungen organisieren, verlässt die Prüfung den Bauträgerpfad. MaBV greift mangels Bauträgerleistung nicht. Dafür entstehen Form-, Haftungs- und Gesellschaftsrisiken: Beurkundung des eigentumsbezogenen Gesellschaftsvertrags, Heilungsproblem im WEG-Modell, Nachschüsse, persönliche Gesellschafterhaftung, Ausscheiden, Insolvenz einzelner Gesellschafter, Finanzierung und spätere Aufteilung.

Der Skill muss im Mandantenanschreiben klar sagen: Die Baugruppe vermeidet Bauträgerrisiken, verliert aber zugleich MaBV-Schutzschichten. Das ist kein automatisch verbraucherfreundlicher Ersatz.

### O.6 — Beurkundung, Bezugsurkunden, Sonderwünsche

Prüfung vor Beurkundung:

- Sind Baubeschreibung, Pläne, Teilungserklärung und Sonderwünsche konkret beurkundet oder eindeutig bezogen?
- Gibt es entgeltliche Reservierungsvereinbarungen oder Vorausleistungen mit Erwerbsdruck?
- Werden wesentliche Vertragsbedingungen in Bezugsurkunden versteckt?
- Haben Sonderwünsche Auswirkungen auf Ratenplan, Bausoll, Gewährleistung, Termine oder Sondereigentum?
- Wird die VOB/B oder ein externer Standard nur pauschal einbezogen?

Bei Formrisiko nicht reflexhaft Gesamtnichtigkeit behaupten. Vertragsstand, Auflassung, Eintragung und Heilung prüfen.

### O.7 — Nachzügler, Altbau und Sanierungsobjekte

Nachzüglerfälle brauchen einen eigenen Block im Gutachten. Erfasst werden: Errichtung/Fertigstellung, vorherige Abnahmeakte, Vermietungsdauer, Zustand bei Erwerb, eigener Abnahmetermin, Klausel zur Anerkennung fremder Abnahme und Art der übernommenen Sanierungsleistung. Werkvertragsrecht kann auch bei schon ausgeführten Arbeiten relevant bleiben; bei längerer Vermietung und echtem Bestandsverkauf ist Kaufrechtsnähe gesondert zu prüfen.

### O.8 — Persönliche und notarielle Anspruchsketten

Der Skill nutzt persönliche Haftung nur mit Tatsachenunterbau:

| Beteiligter | Wann prüfen |
| --- | --- |
| Geschäftsführer | vorzeitige MaBV-Ratenanforderung, Kenntnis des Bau-/Fälligkeitsstands, operative Zahlungssteuerung |
| Bauleiter/Architekt | Bautenstandsbestätigung, Abnahmeprotokoll, technische Freigabe, auf die der Erwerber zahlt |
| Notar | erkennbare MaBV-/AGB-Risiken, Freistellung, Preisanpassung, § 650m, Vormerkung, Belehrung und Dokumentation |
| Vertrieb | Prospektangaben zu Energie, Schall, Baugrund, Fertigstellung, Finanzierung oder Förderfähigkeit |

Keine pauschalen Vorwürfe. Jeder Vorwurf braucht Handlung, Zeitpunkt, Kenntnis, Adressat und Schaden.

### O.9 — Großkommentar-Check: anwendbar, ausgeschlossen, modifiziert

Bei jedem vollständigen Gutachten wird eine knappe Anwendungskarte gebaut:

| Vorschriftengruppe | Bauträger-Status |
| --- | --- |
| §§ 633 ff. BGB | für Errichtung/Umbau grundsätzlich anwendbar |
| § 640 BGB | Abnahme anwendbar; Abnahmefiktion bei Verbraucher nur mit Belehrung |
| § 650j BGB | Baubeschreibungspflicht nicht ausgeschlossen |
| § 650k Abs. 1 BGB | durch § 650u Abs. 2 ausgeschlossen; Baubeschreibung muss beurkundet/einbezogen werden |
| § 650k Abs. 2/3 BGB | weiter anwendbar |
| § 650l BGB | ausgeschlossen |
| § 650m Abs. 1 BGB | ausgeschlossen |
| § 650m Abs. 2/3 BGB | weiter zu prüfen |
| § 650n BGB | weiter zu prüfen |
| §§ 648, 648a, 650b bis 650e BGB | durch § 650u Abs. 2 ausgeschlossen |
| § 650v BGB, § 1 AbschlagsV, § 12 MaBV | Reichweite des Verbots abweichender Vereinbarungen anhand der konkret betroffenen Pflicht prüfen. |
| §§ 642, 643 BGB | bei Mitwirkungsfragen anwendbar, aber kein Pauschalventil für Bauträgerverzug |

### O.10 — Klauselmatrix: 25 harte Treffer

Die Matrix in Teil B ist bei Vollanalysen mindestens mit diesen Treffern abzugleichen:

| Treffer | Kernbefund |
| --- | --- |
| zwei Großraten oder Vorabrate ohne Bautenstand | MaBV-/AGB-rot |
| Schlussrate vor Besitzübergabe oder vollständiger Fertigstellung | MaBV-/Fälligkeitsproblem |
| `mitgeteilte` Bezugsfertigkeit/Fertigstellung | einseitige Fälligkeit, § 305c Abs. 2/§ 307 prüfen |
| Außenanlagen aus Fertigstellung ausgenommen | MaBV-rot |
| § 650m-Verzicht oder intransparenter Einbehalt | zwingender Verbraucherschutz |
| Baugenehmigung fehlt, Eigenbestätigung ungeprüft oder Schwarzbauverdacht | allgemeine Fälligkeitsvoraussetzung offen |
| Vormerkungslöschung per Bauträgervollmacht | § 309 Nr. 2 lit. a/Nr. 12/§ 307 prüfen |
| Beweislastumkehr/Empfangsbestätigung | § 309 Nr. 12 lit. a/b |
| Mängelrügefrist, Verjährungsverkürzung, Selbstvornahmeausschluss | Mängelrechte entwertet |
| Abnahme durch Erstverwalter, Tochter, Sachverständigen oder Vertreter | Eigenrecht des Erwerbers fehlt |
| Wohnflächen-/Schallschutz-/Energiestandard-Lücken | Bausoll konkretisieren |
| anerkannte Regeln zum Vertragsschluss statt Abnahme | Standardrisiko verschoben |
| Preisanpassung ohne Saldierung/Lösungsrecht | AGB-rot |
| Schlüssel nur gegen Vollzahlung trotz Mängeln | Druckmuster, § 253 StGB im Einzelfall prüfen |
| Besichtigungsausschluss/private Sachverständige ausgeschlossen | MaBV- und Abnahmeprüfung ausgehöhlt |
| zusätzliche Mahnpflicht trotz kalendarischem Termin | § 286-Leitbild unterlaufen |
| Bezugsfertigkeitsrate trotz gefährlichem Baustellenzugang | Bezugsfertigkeit fehlt; Verkehrssicherheit dokumentieren |
| Wohnflächentoleranz über 2 % | Rechtsprechungsstand live prüfen; konkrete Fläche, Methode und wirtschaftliche Auswirkung ausweisen |

### O.11 — Drei-Dokumente-Umsetzung

Mandantenanschreiben: klare Entscheidungshilfe zu Unterschrift, Zahlungsstopp, Nachverhandlung, Abnahme, Besitz oder Streit. Keine Normwand.

Gutachten: jedes Fachmodul wird dort behandelt, wo es hingehört: MaBV in F, AGB in G, Bausoll/Technik in H/J, Abnahme in I, Verzug in M, Haftung in N.

Schreiben an Bauträger/Notar: keine akademische Vollständigkeit, sondern konkrete Streichungs- und Änderungsforderungen mit Alternativwortlaut.

## Bug-Hunt vor Ausgabe

Vor jeder finalen Analyse diese Fehler ausschließen:

- `§ 309 Nr. 15` nicht für Beweislast oder Empfangsbestätigung verwenden; richtig ist § 309 Nr. 12.
- `§ 650m Abs. 1` nicht auf Bauträgervertrag anwenden; er ist durch § 650u Abs. 2 ausgeschlossen.
- `§ 650m Abs. 2` nicht als bloß analog darstellen; § 650u Abs. 2 schließt ihn nicht aus.
- `§ 650k Abs. 1` nicht als Bauträger-Hauptargument verwenden; er ist ausgeschlossen.
- `§ 650k Abs. 2/3`, § 650j, § 650n nicht übersehen.
- MaBV nicht als dreizehn gesetzliche Einzelraten beschreiben; richtig: bis zu sieben Teilbeträge, zusammensetzbar aus Bausteinen.
- § 7 MaBV nicht als `Vertragssumme + 5 %` behaupten; richtig: alle Rückgewähr-/Auszahlungsansprüche bis § 3 Abs. 1 und vollständige Fertigstellung.
- AGB-Unwirksamkeit nicht automatisch zu Gesamtnichtigkeit machen; § 306 BGB ist Regelfolge.
- Keine BeckRS-/juris-/Kanzleiblog-Fundstellen zitieren.
- Keine BGH-Entscheidung ohne zulässige URL und Liveprüfung.
- Keine schrillen Drohungen ohne Tatbestand; Verhandlungsposition soll streng, aber glaubwürdig sein.
- Jede rote Ampel muss eine konkrete gewünschte Änderung haben.
- Technik nicht hinter Jura verstecken: Baugrund, Baugrube, Objektüberwachung, private Sachverständige, LPH 8, Unterlagen, Wartung und Betriebskosten immer mitprüfen.
- HOAI nicht als Direktanspruch des Erwerbers gegen den Bauträger-Architekten ausgeben; als Organisations- und Plausibilitätsraster verwenden.
- Keine MaBV-Rate allein aufgrund interner Bauleiterbestätigung akzeptieren, wenn dem Erwerber jede objektive Bautenstandskontrolle abgeschnitten wird.
- Private Bauüberwachung nicht mit freiem Baustellenzutritt verwechseln; sachgerechte Lösung ist angemeldeter, sicherheitskonformer Zutritt mit eigenem Sachverständigen.
- DIN-Normen nicht als automatische anerkannte Regeln der Technik ausgeben; Einzelfall und Senatsdifferenzierung live prüfen.
- Vollständige Fertigstellung nie mit Bezugsfertigkeit, Abnahme oder Schlüsselübergabe gleichsetzen.
- Schlussrate vor Außenanlagen, Restarbeiten am Gemeinschaftseigentum oder protokollierten Mängeln nicht vorschnell als fällig behandeln.
- Preisanpassung ohne Saldierung, Kalkulationsoffenlegung und gesichertes Lösungsrecht nicht als `marktüblich` akzeptieren.
- Bauablaufargumente (`Pandemie`, `Lieferketten`, `Wetter`, `GU-Insolvenz`) nie ohne Bauablaufplan, Gewerkbezug und Wiederanlaufzeit durchgehen lassen.
- § 650l BGB-Widerruf nicht beim beurkundeten Bauträgervertrag versprechen.
- Bauhandwerkersicherung nach § 650f BGB nicht vom Verbraucher-Erwerber verlangen.
- Baugruppen-GbR nicht mit Bauträgermaßstäben prüfen; keine MaBV anwenden, dafür § 311b BGB, MoPeG-Haftung und Nachschüsse prüfen.
- Beweislastumkehr und Empfangsbestätigung immer § 309 Nr. 12 lit. a/b BGB zuordnen, nicht § 309 Nr. 15.
- Schlüsselverweigerung trotz Mängeln nicht als bloße Vertragsfrage abhandeln; Besitzdruck, Zurückbehaltungsrecht und § 253 StGB im Einzelfall prüfen.
- Persönliche Haftung von Geschäftsführer, Bauleiter, Vertrieb oder Notar nur mit Handlung, Kenntnis, Pflichtverletzung und Schaden ausgeben.
- Nicht belegte Rechtsprechungslinien als Prüfbedarf markieren; keine Aktenzeichen, Daten oder Zitate erfinden.

> **Ende des Skills.** Bei Anwendung: Vertrag einfügen. Der Skill startet mit Pflicht-Prüfblock, arbeitet die 30 Prüfschleifen ab, zitiert nur zulässige Quellen und liefert ein verhandlungsfähiges Verbraucherpaket.
