# Vollprüfung: notariat-alltag

## Zusammensetzung

Diese Vollprüfung enthält alle 20 Skills des Plugins `notariat-alltag`.

## Inhaltsverzeichnis

1. **kaltstart-triage** — Hauptworkflow für Notariatsmitarbeiter: führt Kundenunterlagen bis zur konkreten Urkunden- oder Anmeldevorlage an den No…
2. **ehevertrag-scheidungsfolgenvereinbarung** — Bereitet Eheverträge und Scheidungsfolgenvereinbarungen im Notariat vor. Verbindet Güterrecht, Unterhalt, Versorgung und…
3. **urkundenmappe-zur-freigabe** — Prüft eine vorbereitete Notariatsmappe vor Vorlage an den Notar: Fassungen, Beteiligte, Formwege, Anlagen, Kapital- und …
4. **gmbh-gruendung-gesellschafterliste** — Bereitet GmbH- und UG-Gründungen aus Gründerunterlagen vor: individuelle Satzung oder Musterprotokoll, Geschäftsanteile,…
5. **beteiligte-identitaet-vertretung** — Bereitet Personalien, Ausweisabgleich und Vertretungsnachweise für einen Notartermin vor. Hält Scan, vorgelegtes Origina…
6. **vorsorgevollmacht** — Bereitet Vorsorgevollmacht, Patientenverfügung und Betreuungswünsche für das Notariat vor. Klärt Umfang, Ersatzvertretun…
7. **vollzug-fristen-wiedervorlage** — Führt notarielle Vorgänge nach Entwurf oder Beurkundung weiter: Nachweise, Kaufpreisfälligkeit, Registereingänge, Zwisch…
8. **auslandsurkunde-apostille-vollmacht** — Bereitet ausländische Vollmachten, Genehmigungen und Vertretungsnachweise für notarielle Vorgänge auf. Trennt Echtheitsn…
9. **grundschuld-buchgrundschuld-treuhand** — Bereitet Grundschuldbestellungen aus Bankauftrag und Grundbuch vor. Trennt dingliche Sicherheit, persönliche Haftung, Vo…
10. **bautraegervertrag-mabv-familiengesellschaft** — Bereitet Grundstückskauf- und Bauträgerverträge für die notarielle Prüfung vor. Verbindet Käuferdaten, Grundbuch, Teilun…
11. **geschaeftsfuehrer-bestellung-register** — Bereitet Geschäftsführerbestellung, Abberufung und Handelsregisteranmeldung für GmbH und UG vor. Gleicht Beschlussdatum,…
12. **kostenrechnung-gnotkg** — Erstellt nachvollziehbare Entwürfe notarieller Kostenberechnungen aus Auftrag, Urkunde und Vollzug. Ordnet Kostenschuldn…
13. **kapitalerhoehung-beschluss-register** — Bereitet die GmbH-Kapitalerhöhung als zusammenhängenden Vorgang vor: Beschluss, Bar- oder Sacheinlage, Übernahmeerklärun…
14. **formweg-beurkundung-beglaubigung** — Ordnet für die Notariatsmitarbeiter jede konkrete Erklärung dem passenden Formweg zu: Beurkundung, Unterschriftsbeglaubi…
15. **urkundenentwurf-aendern-abgleichen** — Arbeitet Mandantenkorrekturen in notarielle Entwürfe ein, gleicht Urkunde und Anlagen ab und trennt Entwurfsänderung, of…
16. **gmbh-anteile-uebertragen-verpfaenden** — Bereitet Verkauf, Abtretung und Verpfändung von GmbH-Geschäftsanteilen für das Notariat vor. Ordnet Anteilsnummern, Zust…
17. **umwandlung-verschmelzung-kapitalerhoehung** — Bereitet Verschmelzung, Spaltung und Formwechsel für das Notariat vor: Rechtsträger, Vertrags- und Beschlussentwürfe, Sc…
18. **nachlassauseinandersetzung-grundbuch** — Bereitet notarielle Nachlassauseinandersetzungen, Grundstücksübertragungen und Erbnachweise vor. Gleicht Testament, Eröf…
19. **geldwaeschepruefung-immobilien** — Bereitet im Notariat die Geldwäscheprüfung von Grundstücks- und Gesellschaftsvorgängen vor. Klärt Beteiligung und wirtsc…
20. **grundbuchantrag-rangstelle-notarielle** — Bereitet Grundbuchanträge, Rangänderungen und Antworten auf Zwischenverfügungen vor. Gleicht Bewilligung, Auflassung, La…

---

## Skill: `kaltstart-triage`

_Hauptworkflow für Notariatsmitarbeiter: führt Kundenunterlagen bis zur konkreten Urkunden- oder Anmeldevorlage an den Notar. Wählt zwischen Entwurf, Änderung und Vollzug, übernimmt belegte Daten und steuert nur den benötigten Fachskill samt gezielten Rückfragen._

# 1. Hauptworkflow vom Kundenordner zur Urkundenmappe

## 1. Zweck und Anwendungsfall

Bereite für Notariatsmitarbeiter die bestellte Urkunde, Erklärung oder Registeranmeldung vor und führe sie nach Rückfragen zur konsistenten Vorlage. Die Aufgabe endet nicht bei einer Materialübersicht. Notarielle Belehrung, Identitätsfeststellung, Beurkundung, Beglaubigung und amtliche Freigabe bleiben beim Notar.

## 2. Eingaben

Lies zuerst die konkret freigegebenen Dateien: Auftrag oder letzte E-Mail, vorhandener Entwurf, Auszug und Anlagenverzeichnis. Übernimm bereits belegte Angaben. Fehlt der Zugriff, sage das und bitte einmal um die betreffenden Dateien. Suche nicht eigenständig in anderen Mandantenordnern.

## 3. Ablauf

### 3.1. Den Auftrag am nächsten Arbeitsergebnis festmachen

Bei eindeutigem Auftrag beginne den gewünschten Entwurf. Ohne Auftrag, aber mit Material, lies zuerst Auftragsschreiben und aktuelle Entwurfsfassung intern. Frage dann etwa: „Soll ich die Grundschuldbestellung vorbereiten, die Bankvorgaben klären oder eine bestehende Fassung ändern?“ Nenne nur tatsächlich passende Alternativen, keine Liste sämtlicher Ordnerinhalte. Ohne Material frage nach dem Urkundengeschäft und der vorhandenen Vorlage. Lade nur den einen fachlich passenden Arbeitsweg; weitere folgen erst bei einer konkreten Anschlussfrage. Ein fertiger, klar bestellter Vermerk darf unmittelbar geliefert werden.

| Material oder Wunsch | Arbeitsweg | Erstes Arbeitsprodukt |
| --- | --- | --- |
| Grundstückskauf, Bestandsobjekt oder Bauträger | `bautraegervertrag-mabv-familiengesellschaft` | Kaufvertragsentwurf und fehlende Objektanlagen |
| Bankauftrag, Grundbuch, Sicherung | `grundschuld-buchgrundschuld-treuhand` | Bestellungsentwurf mit getrennten Erklärungen |
| Unterschrift bestätigen oder Form klären | `formweg-beurkundung-beglaubigung` | Formblatt und Terminanschreiben |
| Personalien, Vollmacht, Namensabweichung | `beteiligte-identitaet-vertretung` | Beteiligtenblatt mit Nachweisstand |
| Neue GmbH oder UG | `gmbh-gruendung-gesellschafterliste` | Satzungs- und Anmeldeentwurf |
| Neues Stammkapital | `kapitalerhoehung-beschluss-register` | Beschluss, Übernahme und Vollzugsfolge |
| Geschäftsführer bestellen oder wechseln | `geschaeftsfuehrer-bestellung-register` | Beschluss- und Anmeldeentwurf |
| Anteile verkaufen oder als Sicherheit geben | `gmbh-anteile-uebertragen-verpfaenden` | Anteilsübersicht und Vertragsentwurf |
| Verschmelzen, spalten oder Rechtsform wechseln | `umwandlung-verschmelzung-kapitalerhoehung` | Urkunden- und Registerfolge |
| Grundbuchantrag oder Zwischenverfügung | `grundbuchantrag-rangstelle-notarielle` | Antrag oder konkrete Nachreichung |
| Änderungen an einer vorhandenen Urkunde | `urkundenentwurf-aendern-abgleichen` | Bereinigte Fassung und Änderungsvermerk |
| Auslandsnachweis oder abwesender Vertreter | `auslandsurkunde-apostille-vollmacht` | Nachweisanforderung und Vertretungsabschnitt |
| Beteiligung und Immobilienzahlung klären | `geldwaeschepruefung-immobilien` | Interne Prüfung und zulässige Nachforderung |
| Ehevertrag oder Scheidungsfolgen | `ehevertrag-scheidungsfolgenvereinbarung` | Abgestimmte Vereinbarung |
| Erbfolge und Nachlassübertragung | `nachlassauseinandersetzung-grundbuch` | Nachlassurkunde oder Grundbuchantrag |
| Vorsorge und Behandlungswünsche | `vorsorgevollmacht` | Gewünschte Vorsorgeerklärungen |
| Kosten des konkreten Vorgangs | `kostenrechnung-gnotkg` | Kostenberechnung mit Wertnachweisen |
| Neue Vollzugspost oder Aktenabschluss | `vollzug-fristen-wiedervorlage` | Nachforderung oder Abschlussmitteilung |
| Fertige Mappe prüfen | `urkundenmappe-zur-freigabe` | Vorlagevermerk an den Notar |

### 3.2. Angaben mit Herkunft übernehmen

Führe Name, Geburtsdatum, Anschrift, Registergericht, Registernummer, Grundstück und Beträge mit Quelldatei und Stand. Trenne Auftraggeber, Beteiligten, Vertreter, wirtschaftlich Berechtigten und bloßen Ansprechpartner. Ein Ausweisscan bedeutet nicht, dass der Notar das Original gesehen hat. Zwei unterschiedliche Anschriften bleiben bis zur Klärung sichtbar.

### 3.3. Nur den blockierten Teil anhalten

Fehlt der genaue Geschäftsanteil, bereite die übrigen Vertragsabschnitte vor und frage gezielt nach der aktuellen Liste. Erfinde weder Grundbuchdaten noch erteilte Vollmachten. Bei großem Ordner zuerst Kernunterlagen; weitere Dateien nur bei konkreter Belegfrage lesen. Leselücken knapp benennen, ohne einen Datenbestand auszubreiten. Nach Rückmeldung nur betroffene Stellen fortschreiben; kein erneutes Kaltstart-Interview.

### 3.4. Fachschritte mit einem gemeinsamen Stand verbinden

Führe intern Vorgangsnummer, gewünschtes Dokument, letzte Fassung, Beteiligtenrollen, entscheidende Belege und noch offene Bedingungen weiter. Beim Wechsel des Fachskills genau diesen Stand und die konkrete Anschlussfrage übergeben, nicht einen neuen Aufnahmeauftrag. Das Beteiligtenblatt wird einmal angelegt. Eine neue Bankantwort ändert die betroffene Haftungsklausel, nicht ungefragt die vereinbarten Erwerbsanteile. Eine Vollmacht als Scan und ihr späteres Original behalten getrennte Eingangsstände.

Entwurfsarbeit benötigt keine Freigabe nach jedem Absatz. Externe Mitteilung, Einreichung und Amtshandlung dagegen nie aus dem Auftrag zur Vorbereitung ableiten. Zur Schlussprüfung nur dann `urkundenmappe-zur-freigabe` verwenden, wenn eine konkrete Mappe vorliegt; kein Kreislauf aus Einstieg und Schlussprüfung. Bleibt ein Sachpunkt offen, das genaue Nachforderungsschreiben fertigstellen und nach Antwort an dieser Stelle fortsetzen.

## 4. Quellenpflicht

BeurkG Paragrafen 10, 12 und 17 sowie der konkrete materielle Formtatbestand bestimmen die Vorbereitung. BGH, Urteil vom 07.02.2013, III ZR 121/12: Der bloße Wunsch nach schnellem Termin ersetzt keinen sachlichen Grund und keinen anderweitigen Übereilungsschutz bei der erfassten Verbraucherbeurkundung. Das ist weder eine allgemeine Frist für alle Urkunden noch eine Aussage automatischer Vertragsnichtigkeit. Nutze [Mitarbeiter-Formwege](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/notariat-alltag/references/mitarbeiter-formwege.md) und [Zitierweise](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/notariat-alltag/references/zitierweise.md); lies weitere Quellen nur zur tatsächlich anstehenden Rechtsfrage.

## 5. Ausgabeformat

Liefere ein ausformuliertes Dokument, getrennt davon offene Punkte und die erforderlichen nächsten Handlungen mit ihren Abhängigkeiten. Jeder Urkunden- oder Registertext trägt den Status „Entwurf zur notariellen Prüfung“. Keine fingierte UVZ-Nummer, kein behaupteter Versand. Formatierte Dokumente verwenden Times New Roman 11 pt und dezimale Gliederung; reine Stichwortskelette sind kein Endprodukt.

## 6. Beispiel

Im Ordner liegen Bankauftrag, Kaufvertrag und zwei Ausweiskopien. Beginne den Grundschuldentwurf anhand des bezeichneten Grundstücks. Frage nicht nochmals nach dem Kaufzweck. Ist nur einer der Eigentümer Darlehensnehmer, markiere die persönliche Haftung des anderen als gesondert zu klären.

---

## Skill: `ehevertrag-scheidungsfolgenvereinbarung`

_Bereitet Eheverträge und Scheidungsfolgenvereinbarungen im Notariat vor. Verbindet Güterrecht, Unterhalt, Versorgung und Grundstücksübertragung mit konkreten Wünschen, Wertnachweisen und getrennten Formanforderungen, ohne einseitige Verzichtswünsche als Einigung auszugeben._

# 1. Ehevertrag und Scheidungsfolgen urkundlich vorbereiten

## 1. Zweck und Anwendungsfall

Erstelle aus abgestimmten Zielen und tatsächlichen Verhältnissen eine notarielle Vertragsvorlage. Die Mitarbeiterarbeit ist neutral gegenüber beiden Beteiligten; Belehrung und rechtliche Gestaltungsentscheidung bleiben beim Notar. Keine Interessenvertretung eines Ehegatten vortäuschen.

## 2. Eingaben

Bestehender Ehevertrag, Heirats- und gegebenenfalls Trennungsdaten, Regelungswünsche, Kinderbetreuung, Erwerbsverlauf, Vermögensnachweise, Versorgungsanrechte und Grundbuchunterlagen. Bei einem vollständigen anwaltlichen Entwurf nicht nochmals eine allgemeine Aufnahme durchführen. Frage bei fehlendem Ziel, ob Güterstand, konkrete Ausgleichszahlung oder sämtliche Scheidungsfolgen geregelt werden sollen.

## 3. Ablauf

### 3.1. Jeden Regelungsgegenstand abgrenzen

Güterstand und Zugewinnausgleich von Unterhalt, Versorgungsausgleich und Eigentumsübertragung trennen. Eine Hausübernahme entlässt niemanden ohne Zustimmung der Bank aus der Darlehensschuld. Für Abfindung und Gegenleistung Werte mit Stichtag und Quelle verwenden. Fehlende Bewertung nicht durch eine frei erfundene Pauschale ersetzen.

### 3.2. Form und Wirksamkeitsfragen gezielt prüfen

BGB Paragraf 1410 verlangt für den Ehevertrag gleichzeitige Anwesenheit beider Teile bei der notariellen Niederschrift; zulässige Vertretung und ihre Grenzen gesondert prüfen, keine pauschale Pflicht zum persönlichen Erscheinen beider behaupten. Versorgungsausgleich nach VersAusglG Paragrafen 6 bis 8 und nachehelichen Unterhalt nach BGB Paragraf 1585c jeweils mit eigenem Zeitpunkt und Formtatbestand prüfen. Grundstücksübertragung nach BGB Paragraf 311b Absatz 1 hinzunehmen.

Wirksamkeitskontrolle nach BGB Paragraf 138 und Ausübungskontrolle nach Paragraf 242 anhand konkreter Verhandlungs- und Lebensumstände auseinanderhalten. Schwangerschaft, einseitige Erwerbsaufgabe und wirtschaftliche Abhängigkeit sind aufzuklärende Umstände, keine automatische Unwirksamkeitsformel. Zukünftigen Kindes- oder Trennungsunterhalt nicht ungeprüft in einen Generalverzicht aufnehmen.

### 3.3. Vertrag und offene Entscheidung entwickeln

Ausgleichsbetrag, Fälligkeit, Sicherung, Vollzugsabhängigkeit und Folgen einer verweigerten Bankfreigabe ausformulieren. Bei abweichenden Wünschen nur die streitige Klausel mit verständlichen Alternativen zur notariellen Prüfung vorlegen. Medizinische, steuerliche oder versicherungsmathematische Feststellungen nicht fingieren.

### 3.4. Rückmeldung in die Vereinbarung übernehmen

Nach Bankzustimmung Schuldhaftung und Grundbuchvollzug neu abstimmen; ohne Zustimmung nur das Innenverhältnis regeln, soweit gewollt. Nach korrigierter Versorgungsauskunft den betroffenen Ausgleich, nicht sämtliche Vermögenswerte ändern. Abschließend an `urkundenmappe-zur-freigabe` übergeben; kein erneutes Interview.

### 3.5. Wirksamkeit und spätere Ausübung getrennt begründen

[BGH, Urteil vom 11.02.2004, XII ZR 265/02](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/XII_ZS/2002/XII_ZR_265-02.pdf?__blob=publicationFile&v=1), amtlicher Volltext Seiten 23 bis 26, unterscheidet die Wirksamkeitskontrolle anhand der Verhältnisse bei Vertragsschluss nach BGB Paragraf 138 von der Ausübungskontrolle bei späterer Berufung auf den Vertrag nach Paragraf 242. Betreuungsbelastung, Erwerbsverzicht, Versorgung und vereinbarte Kompensation im Gesamtzusammenhang erfassen. Weder Schwangerschaft noch Einkommensunterschied begründen für sich eine automatische Gesamtnichtigkeit; notarielle Belehrung ersetzt umgekehrt keine Inhaltskontrolle. Die damaligen Versorgungsausgleichsnormen nicht fortschreiben: heute VersAusglG Paragrafen 6 bis 8 verwenden. Nach veränderter Familienplanung die konkret betroffenen Verzichts- und Ausgleichsregelungen neu entwerfen, nicht nur eine allgemeine salvatorische Klausel ergänzen.

## 4. Quellenpflicht

[BGB Paragraf 1410](https://www.gesetze-im-internet.de/bgb/__1410.html), [Paragraf 1585c](https://www.gesetze-im-internet.de/bgb/__1585c.html), [VersAusglG](https://www.gesetze-im-internet.de/versausglg/) und [Zitierweise](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/notariat-alltag/references/zitierweise.md). Rechtsprechung zu Inhaltskontrolle nur mit konkretem Vergleich der dortigen Vertragssituation verwenden; ein bloßes Aktenzeichen ersetzt diesen Vergleich nicht.

## 5. Ausgabeformat

Vollständig ausformulierte Vereinbarung als „Entwurf zur notariellen Prüfung“ und getrennte kurze Entscheidungsfragen. Times New Roman 11 pt, dezimale Gliederung. Keine behauptete Belehrung, Zustimmung, Bankfreigabe oder Unterzeichnung.

## 6. Beispiel

Ein Ehegatte übernimmt das Haus gegen Ausgleich; die finanzierende Bank hat den anderen noch nicht entlassen. Formuliere die vereinbarte interne Lastentragung und lege den offenen Entlassungsweg vor, statt schon persönliche Haftungsfreiheit zu versprechen.

---

## Skill: `urkundenmappe-zur-freigabe`

_Prüft eine vorbereitete Notariatsmappe vor Vorlage an den Notar: Fassungen, Beteiligte, Formwege, Anlagen, Kapital- und Grundstücksdaten, Unterschriftsfelder sowie elektronische Einreichungsunterlagen. Kennzeichnet offene Freigaben statt Amtshandlungen zu fingieren._

# 1. Entwurfsmappe an den Notar übergeben

## 1. Zweck und Anwendungsfall

Führe eine abschließende Mitarbeiterkontrolle der konkreten Vorgangsmappe durch. „Vorbereitet“ bedeutet nicht „beurkundet“, „beglaubigt“, „eingereicht“ oder „eingetragen“. Die Verantwortung für Amtshandlungen bleibt beim Notar.

## 2. Eingaben

Aktueller Entwurf, Quellen, Nachträge, Anlagen, Beteiligtenblatt und vorhandene Freigaben. Lies geänderte Fassungen und abhängige Abschnitte, nicht bei jeder kleinen Änderung den gesamten Ordner neu. Ohne Dateizugriff keine technische Prüfung behaupten.

## 3. Ablauf

### 3.1. Fassung und Daten durchgängig vergleichen

Prüfe Namen, Rollen, Geburtsdaten, Register- und Grundbuchdaten, Nummern, Beträge und Termine zwischen Haupttext, Anlagen und Anmeldung. Rechne Kapital- und Anteilsbeträge. Ein PDF-Export einer älteren Word-Fassung erhält nicht den Status der neuesten Datei. Bewahre Originale unverändert.

### 3.2. Erklärungen und Nachweise abgleichen

Für jeden Unterzeichner muss erkennbar sein, welche Erklärung er in welcher Rolle abgeben soll. Trenne fehlenden Nachweis von fehlender Willensentscheidung. Prüfe Verbraucherentwurfsfrist, Vertretungsmacht, benötigte Anlagen und gesonderte Versicherungen. Kein Mitarbeitervermerk ersetzt die notarielle Identitätsfeststellung oder Belehrung.

### 3.3. Dateien und Signaturen kontrollieren

Öffnbarkeit, Seitenzahl, Lesbarkeit und vollständige Anlagenfolge tatsächlich prüfen, soweit Werkzeuge verfügbar sind. Urkundenentwürfe und rechtlich verbindliche Ausfertigungen getrennt halten. Elektronische Zeugnisse nach BeurkG Paragraf 39a, Registerübermittlung nach HGB Paragraf 12 und Grundbuchübermittlung nach den einschlägigen Landesvorgaben jeweils gesondert vorbereiten. Keine gewöhnliche PDF-Konvertierung als notarielle Beglaubigung ausgeben.

### 3.4. Entscheidung und nächste Handlung dokumentieren

Erstelle eine kurze Vorlage mit „bereit zur Prüfung“, „Rückfrage“ oder „Vollzug gesperrt“ je Teil. Sperre nur den betroffenen Schritt, nicht jede sonst mögliche Vorbereitung. Keine Unterschrift einfügen, keine Fälligkeit mitteilen, kein Registerpaket versenden und keine Bankdaten ändern ohne zuständige Freigabe. Eine technische Störung führt zu einem gesicherten Teilstand und einem überprüfbaren nächsten Versuch, nicht zu behauptetem Erfolg.

## 4. Quellenpflicht

BeurkG Paragrafen 10, 13, 17 und 39a; HGB Paragraf 12; GBO Paragraf 29 und einschlägige Verfahrensregeln. [Mitarbeiter-Formwege](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/notariat-alltag/references/mitarbeiter-formwege.md), [Zitierweise](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/notariat-alltag/references/zitierweise.md). Je nach Papier- oder elektronischem Verfahren die aktuelle Form prüfen.

## 5. Ausgabeformat

Ausformulierter Vorlagevermerk, bereinigte Entwurfsfassungen und übersichtliches Anlagenregister. Times New Roman 11 pt, dezimale Gliederung. Keine Klauselrümpfe. Dateinamen sind kurz und sprechend; sensible Personalien werden nicht unnötig darin verbreitet. Offen gebliebene Prüfungen werden ausdrücklich benannt.

## 6. Beispiel

Die Satzung nennt 35000 Euro Stammkapital, die Anmeldung noch 25000 Euro. Korrigiere den Entwurf nach belegtem Beschlusskonzept. Behaupte nicht, der Erhöhungsbeschluss sei schon beurkundet, nur weil die Zahl in der Word-Datei angepasst wurde.

---

## Skill: `gmbh-gruendung-gesellschafterliste`

_Bereitet GmbH- und UG-Gründungen aus Gründerunterlagen vor: individuelle Satzung oder Musterprotokoll, Geschäftsanteile, Geschäftsführerbestellung, Einzahlung, Gesellschafterliste und Registeranmeldung. Trennt Entwurf, Beurkundung und tatsächliche Eintragungsreife._

# 1. GmbH-Gründung und Registermappe vorbereiten

## 1. Zweck und Anwendungsfall

Führe den Gründungsauftrag bis zur prüffähigen Vorlage an den Notar. Eine Satzungsdatei ist weder eine beurkundete Gesellschaft noch eine Handelsregistereintragung. Andere Rechtsformen werden nicht unbesehen in ein GmbH-Muster gepresst.

## 2. Eingaben

Lies Gründerwünsche, Beteiligten- und Geschäftsführerangaben, Firma, Sitz, Geschäftsanschrift, Unternehmensgegenstand, Einlageplan und Bankunterlagen. Frage nach Individualregelungen nur, wenn die vorhandenen Wünsche keine Entscheidung erlauben.

## 3. Ablauf

### 3.1. Satzungsweg wählen

GmbHG Paragraf 2 Absatz 1a erlaubt das gesetzliche Musterprotokoll bei höchstens drei Gesellschaftern und einem Geschäftsführer ohne vom gesetzlichen Muster abweichende Bestimmungen. Es verlangt nicht ausschließlich natürliche Personen und nicht die Gesellschafterstellung des Geschäftsführers. Individuelle Zustimmungsrechte, abweichende Nachfolgeregeln oder zusätzliche Geschäftsführer sprechen gegen den unveränderten Musterweg. Das Musterprotokoll gilt zugleich als Gesellschafterliste. Keine angeblich stets beglaubigungspflichtige Zusatzliste erfinden.

### 3.2. Beteiligung und Gegenstand ausformulieren

Ordne jedem Anteil laufende Nummer, Nennbetrag und Übernehmer zu. Rechne Summe und Prozente gegen das Stammkapital. Beschreibe den Unternehmensgegenstand anhand des tatsächlichen Geschäfts, ohne eine erforderliche Erlaubnis zu behaupten. Sitz, Geschäftsanschrift und Gesellschafteranschrift sind verschiedene Felder.

### 3.3. Einlage und Anmeldung auseinanderhalten

Bei der Bar-GmbH verlangt Paragraf 7 Absatz 2 vor Anmeldung mindestens ein Viertel jedes Anteils und insgesamt mindestens die Hälfte des gesetzlichen Mindeststammkapitals; Sacheinlagen gesondert nach Absatz 3 und Paragraf 8 behandeln. Bei der UG gilt Paragraf 5a: vollständige Einzahlung vor Anmeldung und keine Sacheinlagen. Eine Überweisungsankündigung ist kein Bankbeleg. Erfasse Betrag, Wertstellung, Leistenden, Verwendungszweck und freie Verfügbarkeit. Keine Geschäftsführer-Versicherung ohne tatsächliche Grundlage als bereits abgegeben darstellen.

### 3.4. Registerunterlagen zusammenstellen

Entwerfe Satzung, Bestellung, Anmeldung und erforderliche Liste mit eigenem Zweck. Prüfe Geschäftsführerfähigkeit und Versicherung nach Paragrafen 6 und 8, Vertretungsregel und etwaige Befreiung von BGB Paragraf 181 anhand des Auftrags. Eine Befreiung ist kein ungefragter Standard. Anmeldung nach HGB Paragraf 12, nicht als gewöhnliche E-Mail.

### 3.5. Vorphase nicht beschönigen

Unterscheide Vorgründung, beurkundete Vorgesellschaft und eingetragene Gesellschaft. Paragraf 11 Absatz 2 betrifft die Haftung der Handelnden, nicht unterschiedslos aller Gesellschafter. Besondere Gründerhaftung bei Verlusten vor Eintragung ist davon getrennt dem Notar vorzulegen. Keine pauschalen Gebührenbeträge; Geschäftswert und GNotKG-Tatbestände gesondert prüfen.

### 3.5. Vertretung und abschließende Anmeldung prüfen

Eine Gründungsvollmacht muss nach GmbHG Paragraf 2 Absatz 2 notariell errichtet oder beglaubigt sein; BGB Paragraf 167 Absatz 2 allein genügt hier nicht. Für die Gründungsanmeldung verlangt GmbHG Paragraf 78 sämtliche Geschäftsführer. Eine Einzelvertretungsbefugnis ersetzt diese besondere Mitwirkung nicht. Ordne jeder erforderlichen Person Erklärung und Nachweis zu.

Soll eine GbR Gesellschafterin werden, verlangt GmbHG Paragraf 40 Absatz 1 vor ihrer Aufnahme in die Gesellschafterliste die Eintragung im Gesellschaftsregister. Nach Registereingang Namen, Sitz, Registergericht und Nummer sowie Vertretung abgleichen; die einzelnen GbR-Gesellschafter nicht ersatzweise als Inhaber des GmbH-Anteils eintragen. Anteilsnummern, Nennbeträge sowie einzelne und gesamte prozentuale Beteiligung nachrechnen.

## 4. Quellenpflicht

GmbHG Paragrafen 2, 3, 5, 5a, 6, 7, 8, 11 und 40; HGB Paragraf 12. [Amtliche Links](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/notariat-alltag/references/mitarbeiter-formwege.md), [Zitierweise](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/notariat-alltag/references/zitierweise.md). Gesetzliches Muster in aktueller Fassung verwenden.

## 5. Ausgabeformat

Vollständig ausformulierter Satzungs- und Anmeldeentwurf, Anteilsrechnung und getrennte offene Nachweise. Status „Entwurf zur notariellen Prüfung“, Times New Roman 11 pt, dezimale Gliederung. Keine Unterschrift, Versicherung oder Eintragung als erfolgt darstellen. Keine reinen Klauselskelette.

## 6. Beispiel

Zwei Gründer wollen 25000 Euro Stammkapital und einen nicht beteiligten Geschäftsführer. Das allein schließt das Musterprotokoll nicht aus. Ein zusätzlich gewünschter Zustimmungskatalog für Darlehen führt zur individuellen Satzungsprüfung.

---

## Skill: `beteiligte-identitaet-vertretung`

_Bereitet Personalien, Ausweisabgleich und Vertretungsnachweise für einen Notartermin vor. Hält Scan, vorgelegtes Original und notarielle Feststellung auseinander und klärt Namenswechsel, Registervertretung sowie zulässige Videovorgänge ohne unnötige Datensammlung._

# 1. Beteiligte und Ausweisnachweise für den Termin aufnehmen

## 1. Zweck und Anwendungsfall

Erstelle das Beteiligtenblatt. Der Mitarbeiter erfasst und gleicht ab; die Gewissheit über die Person nach BeurkG Paragraf 10 und die rechtliche Würdigung liegen beim Notar. Erzeuge keine Ausweisbilder, Nummern oder angeblichen Identitätsprüfungen.

## 2. Eingaben

Auftrag, Personendaten, vorhandene Ausweisunterlagen, Registerauszüge, Vollmachten und gewünschter Termin. Lies nur auftragsbezogene Dateien. Verlange keine weitere Ausweiskopie, wenn die nötigen Daten bereits belegbar vorliegen und die Originalvorlage zum Termin ausreicht.

## 3. Ablauf

### 3.1. Beteiligtenrolle und Datensatz anlegen

Erfasse vollständigen Namen, Geburtsnamen soweit relevant, Geburtsdatum, Wohnanschrift und Rolle. Staatsangehörigkeit sowie Ausweisart, ausstellende Stelle, Gültigkeit und Dokumentnummer nur zweckbezogen nach einschlägiger Pflicht und Büroverfahren aufnehmen. Trenne Kontaktadresse und Wohnanschrift. Veröffentliche solche Daten nicht in Dateinamen oder einem Verteileranschreiben.

### 3.2. Herkunft und Abweichung sichtbar halten

Nutze die Statuswerte „Eigenangabe“, „Kopie eingegangen“, „Originalvorlage vorgesehen“ und „Feststellung durch Notar dokumentiert“. Den letzten Status niemals selbst aus dem Vorhandensein einer Datei ableiten. Bei abweichendem Nachnamen gezielt nach Namensnachweis fragen; ein alter Ausweisname wird nicht stillschweigend überschrieben.

Bei Screenshots zuerst tatsächlich sichtbare Vorder- und Rückseiten unterscheiden. Zeichen aus maschineller Texterkennung gegen das Bild prüfen, insbesondere 0 und O, 1 und I sowie Umlaute. Unleserliche Stellen als unleserlich führen; fehlende Ziffern nicht aus einer Prüfsumme erraten. Fordere nur den benötigten Ausschnitt in einem freigegebenen Kanal an. Lege Bildfundstelle und übernommenes Feld intern zusammen, statt den vollständigen Ausweis in jede Vertragsanlage zu kopieren.

### 3.3. Vertreter und Unternehmen prüfen lassen

Erfasse Firma, Sitz, Registergericht, Registernummer, Auszugsdatum, Vertretungsregel und handelnde Person getrennt. Ein Gesellschafter ist nicht automatisch Geschäftsführer. Benenne bei Vollmachten Umfang, Form, Widerrufshinweise und vorliegende Ausfertigung beziehungsweise Original. Bei Auslandsbezug Übersetzung und Nachweisform dem Notar vorlegen. Keine Vertretungsmacht aus einer E-Mail-Signatur ableiten.

### 3.4. Präsenz und Video vorbereiten

Für Präsenz bitte um gültiges Original und konkrete Vertretungsnachweise. Bei Video erst zugelassenen Geschäftstyp, technisches Verfahren und Identifizierung nach BeurkG Paragraf 16c prüfen. Kein privater Videodienst ersetzt das notarielle Verfahren. Dolmetscherbedarf früh anzeigen; die Entscheidung über Urkundssprache und Hinzuziehung trifft der Notar.

Nach geklärtem Namenswechsel nur die betroffenen Bezeichnungen in Urkunde, Anmeldung und Unterschriftsfeldern fortschreiben. An den aufrufenden Fachskill mit dem Herkunfts- und Nachweisstand zurückgeben; kein neues Interview und keine vorschnelle Bestätigung einer Amtshandlung.

## 4. Quellenpflicht

BeurkG Paragrafen 10, 12, 16 und 16c, gegebenenfalls GwG Paragrafen 10 bis 12 nach Vorgang. [Mitarbeiter-Formwege](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/notariat-alltag/references/mitarbeiter-formwege.md) und [Zitierweise](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/notariat-alltag/references/zitierweise.md). Identifizierung nach Berufs- und Geldwäscherecht mit jeweiligem Zweck getrennt dokumentieren.

## 5. Ausgabeformat

Beteiligtenblatt mit Quelle und Status, daneben ein vollständig formuliertes Terminanschreiben. Kein fertiger Beglaubigungsvermerk mit behaupteter Anwesenheit. Dokumente: Times New Roman 11 pt, dezimale Gliederung, vollständige Sätze. Identitätsunterlagen bleiben separat und werden nur an berechtigte Empfänger weitergegeben.

## 6. Beispiel

Eine Genehmigung nennt Anna Brandt, der vorab übersandte Ausweis Anna Seidel. Frage nach dem Namensnachweis und kündige die Originalvorlage an. Vermerke nicht „Identität bestätigt“, nur weil Geburtsdatum und Foto plausibel erscheinen.

---

## Skill: `vorsorgevollmacht`

_Bereitet Vorsorgevollmacht, Patientenverfügung und Betreuungswünsche für das Notariat vor. Klärt Umfang, Ersatzvertretung, Immobilienbefugnis und besondere Gesundheitsmaßnahmen und erstellt abgestimmte Entwürfe ohne pauschale Vollmachts- oder Registerwirkungen._

# 1. Vorsorgewünsche in konkrete Erklärungen übertragen

## 1. Zweck und Anwendungsfall

Bereite die tatsächlich gewünschte Vorsorge vor, nicht ein ungeprüftes Paket maximaler Befugnisse. Mitarbeiter formulieren zur notariellen Prüfung; persönliche Belehrung, Feststellungen zur Geschäftsfähigkeit und Amtshandlungen bleiben beim Notar.

## 2. Eingaben

Vorhandene Vollmachten, gewünschte Vertrauensperson und Ersatzperson, Vermögensarten, bestehende Betreuung und konkrete Behandlungswünsche lesen. Ohne Unterlagen zunächst fragen, ob Vertretung im Alltag, medizinische Festlegungen oder beides gewünscht sind. Keine Diagnose aus einem Ausweis oder einer kurzen Nachricht ableiten.

## 3. Ablauf

### 3.1. Außenmacht und interne Begrenzung bestimmen

Einzelvertretung, gemeinschaftliche Vertretung, Ersatzfall, Untervollmacht, Schenkungen und Fortgeltung über den Tod hinaus einzeln klären. Befreiung von BGB Paragraf 181 ist eine bewusste Gestaltungsentscheidung, kein obligatorischer Mindestbestandteil. Eine nur im Innenverhältnis vereinbarte Beschränkung darf nicht als äußere Wirksamkeitsbedingung ausgegeben werden.

### 3.2. Form nach Befugnis prüfen

BGB Paragraf 167 Absatz 2 als Ausgangspunkt, besondere Form- und Nachweiserfordernisse gesondert prüfen. Grundstücksbezug bedeutet nicht immer zwingende Beurkundung der Vollmacht; GBO Paragraf 29 betrifft die Verwendbarkeit des Nachweises. Für die in BGB Paragraf 1820 Absatz 2 bezeichneten Gesundheits- und Freiheitsmaßnahmen schriftliche, ausdrückliche Erfassung prüfen. Gerichtliche Genehmigungserfordernisse werden durch die Vollmacht nicht beseitigt.

### 3.3. Patienten- und Betreuungswünsche unterscheiden

Patientenverfügung nach BGB Paragraf 1827 verbindet Behandlungssituation und konkrete Maßnahme. „Keine lebenserhaltenden Maßnahmen“ allein reicht nicht als universell eindeutige Festlegung. BGH, Beschluss vom 06.07.2016, XII ZB 61/16, behandelt diese Konkretisierung; die damaligen Normnummern nicht als heutige Nummern fortführen. Weder verlangt die Entscheidung ein medizinisches Lehrbuch noch eine stets unwirksame Verfügung bei jeder allgemein gehaltenen Wendung.

Betreuungswünsche nach BGB Paragraf 1816 Absatz 2 benennen gewünschte oder abgelehnte Personen; sie sind keine Vollmacht. Ärztliche Beratung bei offenen Behandlungsfragen empfehlen, ohne sie als allgemeine gesetzliche Wirksamkeitsvoraussetzung zu behaupten.

### 3.4. Nach Antwort Widersprüche auflösen

Will der Auftraggeber die Immobilienbefugnis, aber keine Schenkungen, genau diese Grenze einarbeiten. Widersprechen neue Behandlungswünsche einem alten Text, nur mit eindeutigem Änderungsauftrag bereinigen. Registrierung im Zentralen Vorsorgeregister, Aufbewahrung der Urkunde und Zugang zur Vollmacht getrennt vorbereiten. Die Registereintragung ersetzt weder Vollmacht noch Behandlungserklärung und garantiert nicht, dass niemals eine Betreuung nötig wird.

### 3.5. Besondere Gesundheitsbefugnis und eigene Behandlungserklärung ausarbeiten

BGH, Beschluss vom 06.07.2016, XII ZB 61/16, Randnummern 17 bis 20: Die Vollmacht muss die qualifizierte Gefahr des Todes oder eines schweren und länger dauernden Gesundheitsschadens hinreichend klar erfassen; bloßer Verweis auf eine Paragrafennummer reicht nicht. Heute BGB Paragraf 1820 Absatz 2 Nummer 1 mit Paragraf 1829 prüfen. Freiheitsentziehung und ärztliche Zwangsmaßnahmen nach Paragraf 1820 Absatz 2 Nummern 2 und 3 bleiben gesonderte Entscheidungen; aus Zustimmung zur Gesundheitsvertretung keine solche Befugnis ergänzen.

BGH, Beschluss vom 08.02.2017, XII ZB 604/15, Randnummern 17 bis 23: Für die Bestimmtheit der Patientenverfügung ist die schriftliche Erklärung insgesamt auszulegen; allgemeine Wendungen nicht isoliert für unwirksam erklären. Konkretisierung kann sich aus hinreichend beschriebenen Situationen und dem übrigen Text ergeben. Nach Klärung Situation, gewünschte beziehungsweise abgelehnte Maßnahmen und die zugehörige Vertretungsbefugnis in zusammenpassende vollständige Texte überführen. Eine Vertreterentscheidung und eine unmittelbar anwendbare eigene Patientenverfügung sind verschiedene Grundlagen; gerichtliche Genehmigung einschließlich der Ausnahme bei Einvernehmen nach BGB Paragraf 1829 Absatz 4 fallbezogen prüfen.

## 4. Quellenpflicht

[BGB Paragraf 1820](https://www.gesetze-im-internet.de/bgb/__1820.html), [1827](https://www.gesetze-im-internet.de/bgb/__1827.html), [1816](https://www.gesetze-im-internet.de/bgb/__1816.html). Die beiden [volltextgeprüften BGH-Entscheidungen mit Fundstellen und Anwendungsgrenzen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/notariat-alltag/references/rechtsprechung-geprueft.md) heranziehen; alte Normnummern nicht als geltendes Recht behandeln. [Zitierweise](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/notariat-alltag/references/zitierweise.md) beachten.

## 5. Ausgabeformat

Gewünschte Erklärungen vollständig ausformuliert als Entwurf zur notariellen Prüfung; konkrete medizinische Auswahlfragen getrennt. Times New Roman 11 pt, dezimale Gliederung. Keine erfundene ärztliche Beratung, Unterschrift oder starre Registergebühr.

## 6. Beispiel

Die Tochter soll Bankgeschäfte allein führen, das Grundstück aber nur gemeinsam mit dem Sohn verkaufen dürfen. Formuliere diese Befugnisse getrennt und kläre den Ausfall einer Person. Keine pauschale Generalvollmacht mit unbemerkter Einzelvertretung liefern.

---

## Skill: `vollzug-fristen-wiedervorlage`

_Führt notarielle Vorgänge nach Entwurf oder Beurkundung weiter: Nachweise, Kaufpreisfälligkeit, Registereingänge, Zwischenverfügungen und offene Vollzugsreste. Aktualisiert nur betroffene Schritte und bereitet Nachforderungen oder Abschlussmitteilungen vor._

# 1. Vollzug, Fristen und Aktenabschluss nachhalten

## 1. Zweck und Anwendungsfall

Bearbeite den nächsten offenen Vollzugsschritt anhand des wirklichen Nachweisstands. Ein fertig erstellter Vertrag ist nicht automatisch beurkundet oder vollzogen. Mitarbeiter führen Wiedervorlagen; Amtshandlungen und Freigaben bleiben beim Notar.

## 2. Eingaben

Übernimm Vorgangsnummer, aktuelle Urkundenfassung, Vollzugsauftrag, Fristen mit Quelle und zuletzt eingegangene Nachweise. Lies zunächst neue Post und die davon betroffene Bedingung, nicht erneut den gesamten Mandantenordner.

## 3. Ablauf

### 3.1. Voraussetzungen statt bloßer Aufgabenliste führen

Verknüpfe jede Handlung mit ihrer Grundlage: Vormerkung, Genehmigung, Lastenfreistellung, Kapitalzahlung, Registerversicherung oder Bedingung einer Abtretung. Notiere Belegdatum, zuständigen Bearbeiter und fehlenden Nachweis. Gesetzliche Frist, gerichtliche Frist, vertraglichen Termin und interne Wiedervorlage deutlich unterscheiden. Kein universelles Fristenmuster verwenden.

### 3.2. Neue Post gegen die konkrete Bedingung prüfen

Eine Bankeingangsbestätigung erledigt keine Lastenfreistellung. Eine Überweisungsankündigung belegt keine Einlage. Eine elektronische Empfangsbestätigung ist keine Registereintragung. Bei Teilvollzug nur nachgewiesene Teilschritte schließen. Ein abgelaufener Ablösestichtag verlangt aktualisierte Beträge, bevor daraus eine Zahlungsmitteilung vorbereitet wird.

### 3.3. Gezielt anfordern und fortsetzen

Bei ausstehender Antwort nach dem konkret fehlenden Dokument und erwarteten Eingang fragen. Eine nahe Zwischenverfügungsfrist dem Notar mit vorbereitetem Nachreichungs- oder Verlängerungsschreiben vorlegen. Verlängerung erst nach bestätigter Bewilligung als wirksam führen. Im Anschluss an Bank- oder Registerantwort die betroffenen Vertrags- und Mitteilungstexte aktualisieren; kein neues Aufnahmeinterview.

### 3.4. Abschluss nach tatsächlichem Vollzug

Eintragungsmitteilung gegen Antrag, Recht, Betrag und Rang prüfen. Noch bestehende Löschungen, Gebühren, Rückgaben, Ausfertigungen und nachlaufende Nachweise offenhalten. Amtliche Ausfertigung, beglaubigte Abschrift und einfache Lesekopie nach BeurkG Paragrafen 47 ff. unterscheiden; einen Export nicht als Ausfertigung bezeichnen. Aufbewahrung nach Dokumenttyp und geltender NotAktVV prüfen, keine einheitliche Löschfrist erfinden.

## 4. Quellenpflicht

Je nach Vorgang [GBO Paragraf 18](https://www.gesetze-im-internet.de/gbo/__18.html), BeurkG Paragraf 17 Absatz 2a, GmbHG Paragrafen 40 und 54 sowie GwG Paragraf 16a heranziehen. Quelle, Fristbeginn und Rechtsfolge müssen zusammenpassen. [Zitierweise](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/notariat-alltag/references/zitierweise.md) beachten.

## 5. Ausgabeformat

Das bestellte Nachforderungsschreiben, die Abschlussmitteilung oder der Vorlagevermerk steht vollständig ausformuliert im Vordergrund. Eine knappe interne Wiedervorlage ergänzt ihn nur bei Bedarf. Times New Roman 11 pt und dezimale Gliederung; keine fingierte Zahlung, Eintragung oder Freigabe.

## 6. Beispiel

Eine Vormerkung ist eingetragen, die Ablösebank hat aber nur den Eingang der Anfrage bestätigt. Übernimm den ersten Nachweis, fordere die konkrete Freistellung nach und lasse die davon abhängige Fälligkeitsmitteilung offen.

---

## Skill: `auslandsurkunde-apostille-vollmacht`

_Bereitet ausländische Vollmachten, Genehmigungen und Vertretungsnachweise für notarielle Vorgänge auf. Trennt Echtheitsnachweis, Übersetzung, materiellen Umfang und Registerform und erstellt eine konkrete Nachforderung statt pauschaler Anerkennungszusagen._

# 1. Auslandsnachweise für den Urkundenvorgang klären

## 1. Zweck und Anwendungsfall

Löse das konkrete Nachweisproblem eines abwesenden Beteiligten oder ausländischen Rechtsträgers. Apostille, Vollmachtsumfang und zulässige Verwendung im deutschen Register sind verschiedene Prüfungen. Mitarbeiter bereiten vor; Amtshandlungen und Freigaben bleiben beim Notar.

## 2. Eingaben

Lies vollständige Urkunde einschließlich Beglaubigungs- und Apostillenseiten, Herkunftsstaat, Aussteller, vorgesehenes Geschäft und Verwendungszweck. Bei einem Scan notiere den noch offenen Original- beziehungsweise elektronischen Nachweisstand. Frage nicht erneut nach dem Staat, wenn er aus der Urkunde hervorgeht.

## 3. Ablauf

### 3.1. Erklärungsinhalt vor Echtheitskette lesen

Welche Person darf für wen welches Geschäft abschließen? Prüfe Kauf, Belastung, Anteilstransaktion, Untervollmacht und mögliche Beschränkungen einzeln. Eine Generalüberschrift ersetzt den tatsächlichen Umfang nicht. Bei vollmachtlosem Auftreten Genehmigung und deren notwendigen Zugang vorbereiten; keine bereits erteilte Vollmacht fingieren. BGB Paragrafen 164 ff., 177, 182 und BeurkG Paragraf 12 sind die Ausgangspunkte.

### 3.2. Echtheit und Befreiung bestimmen

Prüfe zuerst eine einschlägige Befreiung, dann Apostille oder Legalisation anhand Staat, Urkundentyp und zuständiger Stelle. Die Verordnung (EU) 2016/1191 befreit bestimmte öffentliche Urkunden im geregelten Anwendungsbereich, nicht jede Handelsregistervollmacht aus einem Mitgliedstaat. Das mehrsprachige Formular ist kein allgemeines Erfordernis der Befreiung. Eine Apostille bestätigt nicht die Richtigkeit des Vertragsinhalts oder die materielle Vertretungsmacht.

### 3.3. Form und Übersetzung für den Empfänger klären

Für Grundbuchnachweise GBO Paragraf 29, für Registeranmeldungen HGB Paragraf 12 beachten. Echtheitsbestätigung allein ersetzt die Prüfung einer erforderlichen Gleichwertigkeit der ausländischen Amtshandlung nicht. EGBGB Artikel 11 nicht als pauschale Zulassung jedes ausländischen Grundstücksgeschäfts verwenden. Umfang einer Übersetzung und gegebenenfalls konkrete gerichtliche Anforderungen ermitteln; ausländische Übersetzer nicht ohne Prüfung generell ausschließen.

### 3.4. Nachforderung in verwendbare Unterlagen umsetzen

Fordere genau fehlende Seite, Nachweisform oder Übersetzung mit Vorgangsbezug an. Bei Eingang der Papierurkunde sämtliche Anlagen und Einschränkungen gegen den Scan vergleichen. Eine später eingegangene Vollmacht darf nicht rückwirkend als am früheren Termin vorgelegt beschrieben werden. Übergib nur geänderte Beteiligten- und Vertretungsangaben an `beteiligte-identitaet-vertretung`; anschließend im begonnenen Urkundenentwurf fortsetzen.

### 3.5. Genehmigungsanforderung und Rücklauf zuordnen

Bei vollmachtlos geschlossenem Vertrag Genehmigung nach BGB Paragraf 177 und deren Form nach Paragraf 182 Absatz 2 von einem für Grundbuch oder Register erforderlichen Nachweis unterscheiden. Fordert der andere Vertragsteil den Vertretenen zur Erklärung nach Paragraf 177 Absatz 2 auf, läuft die gesetzliche Zweiwochenfrist ab Empfang dieser Aufforderung; die Erklärung kann dann nur ihm gegenüber erfolgen. Ein gewöhnlicher Notariatsreminder löst diese Frist nicht automatisch aus. Absenderrolle, Zugang und Erklärungsempfänger belegen. Nach Ablauf oder Ablehnung keine Erledigung vermerken, sondern Wirksamkeit und weiteren Vertragsweg dem Notar vorlegen.

Nach Eingang der ausländischen Urkunde den bisherigen offenen Punkt nur schließen, wenn Person, konkrete Befugnis, Echtheitsnachweis und erforderliche Vorlageform zusammenpassen. Eine Apostille bestätigt keine ausreichende Vertretungsmacht.

## 4. Quellenpflicht

[EU-Verordnung 2016/1191](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32016R1191), [Haager Apostille-Übereinkommen](https://www.hcch.net/de/instruments/conventions/full-text/?cid=41), aktuelle staatenbezogene amtliche Hinweise und [Zitierweise](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/notariat-alltag/references/zitierweise.md). Ohne überprüften Länderstand keine verbindliche Anerkennungszusage.

## 5. Ausgabeformat

Vollständige Unterlagenanforderung oder Vorlage zur notariellen Prüfung, getrennt nach fehlendem Inhalt und fehlender Nachweisform. Times New Roman 11 pt, dezimale Gliederung. Die Urkunde selbst nur im beauftragten Umfang ändern; keine selbst erstellte Apostille, Beglaubigung oder Übersetzerbescheinigung.

## 6. Beispiel

Die Vollmacht aus Portugal liegt als Farbscan vor, das Papier soll unterwegs sein. Bereite den Vertretungsabschnitt vorläufig vor und benenne die fehlende verwendbare Urkunde. Eine Versandmeldung ist kein Eingang; nach Eingang den tatsächlichen Umfang und alle verbundenen Seiten prüfen.

---

## Skill: `grundschuld-buchgrundschuld-treuhand`

_Bereitet Grundschuldbestellungen aus Bankauftrag und Grundbuch vor. Trennt dingliche Sicherheit, persönliche Haftung, Vollstreckungsunterwerfung, Sicherungszweck und Treuhandauflagen und führt Rang sowie Lastenfreistellung zur notariellen Prüfung zusammen._

# 1. Grundschuld und Bankauftrag abstimmen

## 1. Zweck und Anwendungsfall

Bereite eine Grundschuldbestellungsurkunde oder eine reine Bewilligung entsprechend dem tatsächlichen Auftrag vor. Bankformular, Grundstück und Beteiligte werden abgeglichen. Notarielle Entscheidungen, Vollstreckungsklauseln und Zahlungsfreigaben bleiben beim Notar.

## 2. Eingaben

Bankauftrag mit Bedingungen, Grundbuchstand, Eigentümer, Darlehensnehmer, Vollmachten, Kaufvertrag, bestehende Grundpfandrechte und Ablöseunterlagen. Bei abweichender Anschrift nicht die Grundstücksbezeichnung aus einer privaten E-Mail übernehmen.

## 3. Ablauf

### 3.1. Betrag und gesicherte Forderung auseinanderhalten

Erfasse Grundschuldbetrag, dinglichen Zinssatz, Zinsbeginn, Nebenleistung und Gläubiger wortgetreu. Die abstrakte Grundschuld sichert nicht automatisch jede denkbare Forderung; der Umfang der Verwertung wird durch die Sicherungsabrede bestimmt. Darlehenszinsen sind nicht mit dinglichen Zinsen gleichzusetzen. Sicherungsabrede und Bankauftrag bleiben unterscheidbare Unterlagen.

### 3.2. Form und Haftung getrennt vorbereiten

Für die Grundbucheintragung sind Bewilligung und Nachweisform nach GBO Paragrafen 19 und 29 zu prüfen. Nicht jede Grundschuldbestellung verlangt allein deshalb eine beurkundete Willenserklärung. Eine Vollstreckungsunterwerfung als Titel nach ZPO Paragraf 794 Absatz 1 Nummer 5 gehört dagegen in die notarielle Urkunde. Trenne dingliche Unterwerfung, gegebenenfalls mit Wirkung nach ZPO Paragraf 800, von persönlichem Schuldanerkenntnis und persönlicher Unterwerfung. Miteigentum macht den Nichtdarlehensnehmer nicht automatisch zum persönlichen Schuldner.

### 3.3. Grundstück und Rang sichern

Gleiche Eigentümeranteile, laufende Nummern, Grundstücke und bestehende Rechte in beiden Belastungsabteilungen ab. Rang nach BGB Paragraf 879, GBO Paragraf 45 und konkreten Eintragungen bestimmen; nicht pauschal nur nach Kalendertag. Gewünschter erster Rang ist noch kein vorhandener erster Rang. Bei Löschung, Abtretung oder Rangänderung jeweilige Nachweise und Berechtigte erfassen.

### 3.4. Buch oder Brief und Treuhandbedingungen prüfen

Buchgrundschuld und Briefgrundschuld unterscheiden; bei bestehendem Briefrecht den tatsächlichen Briefverbleib dokumentieren. Keine Briefübergabe oder Kraftlosigkeit erfinden. Ordne Ablösebetrag, Gültigkeitsdatum, Tageszinsen, Zahlungsadressat und Freigabebedingung jeweils der betreffenden Bank zu. Ein Treuhandauftrag wird nicht durch bloße Ablage erfüllt.

### 3.5. Ausfertigung und Vollzug vorbereiten

Unterschrift, notarielle Freigabe, Einreichung, Eintragung und Ausfertigung haben eigene Status. Vollstreckbare Ausfertigungen nach ZPO Paragraf 797 und gegebenenfalls weitere Ausfertigungen nach Paragraf 733 nur nach zuständiger Prüfung vorbereiten. Keine automatische Titelausgabe und keine ungeprüften Fixgebühren.

### 3.5. Eine bestätigte Bankänderung vollständig übernehmen

Bestätigt die Bank, dass nur der Darlehensnehmer persönlich haften soll, entferne die persönliche Schuldübernahme und die persönliche Unterwerfung der anderen Eigentümerin aus sämtlichen Entwurfsstellen. Ihre Mitwirkung an dinglicher Bestellung und gegebenenfalls dinglicher Unterwerfung bleibt nach dem tatsächlichen Auftrag bestehen. Gleiche Erschienenenrubrum, Erklärungsträger, Beträge, Anlagen und Unterschriftsfelder ab; liefere den gesamten korrigierten Entwurf und die verbleibenden Vollzugsvoraussetzungen. Bestehende Löschungs- und Treuhandauflagen werden durch diese Antwort nicht erledigt.

Bei vorgeschlagener Verwahrung [BeurkG Paragraf 57](https://www.gesetze-im-internet.de/beurkg/__57.html) prüfen: berechtigtes Sicherungsinteresse, vollständige schriftliche Anweisungen, Vereinbarkeit der Bankauflagen und Annahme durch den Notar. Eine bevorstehende Ablösefrist ist allein keine Verwahrungsfreigabe.

## 4. Quellenpflicht

BGB Paragrafen 873, 879, 1191 und 1192; GBO Paragrafen 19, 29 und 45; ZPO Paragrafen 733, 794, 797 und 800. [Amtliche Links](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/notariat-alltag/references/mitarbeiter-formwege.md), [Zitierweise](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/notariat-alltag/references/zitierweise.md).

## 5. Ausgabeformat

Ausformulierter Entwurf zur notariellen Prüfung mit getrennten Haftungserklärungen, Bankabgleich und offenen Vollzugsbedingungen. Times New Roman 11 pt, dezimale Gliederung. Keine Klauselskelette, erfundenen Urkundennummern oder behaupteten Originalvorlagen.

## 6. Beispiel

Das Ehepaar besitzt je die Hälfte; nur der Mann ist Darlehensnehmer. Der Bankauftrag verlangt persönliche Haftung beider. Zeige die Abweichung ausdrücklich und kläre den Erklärungswillen über den Notar. Ergänze die Ehefrau nicht stillschweigend als persönliche Schuldnerin.

---

## Skill: `bautraegervertrag-mabv-familiengesellschaft`

_Bereitet Grundstückskauf- und Bauträgerverträge für die notarielle Prüfung vor. Verbindet Käuferdaten, Grundbuch, Teilung, Leistungsumfang und Finanzierung mit Verbraucherfrist, Entwurfsstand und Vollzug; unterscheidet Bestandskauf vom MaBV-Zahlungsplan._

# 1. Grundstücks- und Bauträgerkauf vorbereiten

## 1. Zweck und Anwendungsfall

Erstelle den prüffähigen Entwurf für Grundstück, Wohnung, Haus oder Teileigentum. Unterscheide den Kauf eines Bestandsobjekts vom Bauträgergeschäft mit Bauverpflichtung. Prüfe auch bei einer Familiengesellschaft, wer Unternehmer und wer Verbraucher ist; verwandtschaftliche Nähe ersetzt weder Form noch Schutzvorschriften. Die Mitarbeiter bereiten vor, der Notar prüft und belehrt.

## 2. Eingaben

Auftrag, Verkäufer- und Käuferdaten, Register- und Grundbuchunterlagen, Teilungserklärung, Aufteilungsplan, Baubeschreibung, Kaufpreis, Sonderwünsche, Baugenehmigung und Bankunterlagen. Fehlende Dokumente als fehlend kennzeichnen; ein Exposé ersetzt keine vollständige Baubeschreibung.

## 3. Ablauf

### 3.1. Kaufobjekt und Leistungen eindeutig zuordnen

Gleiche Grundbuchblatt, Gemarkung, Flurstück, Miteigentumsanteil, Einheit, Stellplatz und Sondernutzungsrechte ab. Wohnfläche, Bauleistung und Fertigstellungstermin mit konkreter Quellenversion erfassen. Ein geänderter Grundriss darf nicht stillschweigend als identisch behandelt werden. Bei Sonderwünschen Preis, Auftragnehmer, Fälligkeit und Zusammenhang mit dem Hauptvertrag dem Notar vorlegen.

### 3.2. Entwurf und Verbraucherfrist organisieren

BGB Paragraf 311b Absatz 1 verlangt notarielle Beurkundung. Bei Verbraucherverträgen im Anwendungsbereich von BeurkG Paragraf 17 Absatz 2a soll der beabsichtigte Text im Regelfall zwei Wochen zuvor vom beurkundenden oder einem mit ihm verbundenen Notar bereitgestellt werden. Maklerversand ist nicht automatisch gleichwertig. Dokumentiere tatsächliche Bereitstellung, Anlagen und spätere wesentliche Änderungen. Eine Fristverkürzung nicht allein aus einem Kundenwunsch genehmigen; der Notar entscheidet und dokumentiert den Grund.

### 3.3. Zahlungsplan mit Sicherungen verbinden

Beim Bestandskauf ohne Bauträgerleistung keinen MaBV-Ratenplan einsetzen. Kaufpreis, Inventar, Besitzübergang, bestehende Mietverhältnisse und Lastenfreistellung anhand der Akte regeln. Bei einem vermieteten Objekt nicht stillschweigend eine geräumte Übergabe versprechen. BGB Paragrafen 873, 883 und 925 trennen Eigentumsänderung, Vormerkung und Auflassung. Die folgenden MaBV-Schritte gelten nur für den entsprechenden Bauträgerweg.

MaBV Paragraf 3 Absatz 1 und Absatz 2 getrennt prüfen: allgemeine Sicherungsvoraussetzungen einerseits, baufortschrittsabhängige Teilbeträge andererseits. Bis zu sieben Teilbeträge, nicht sieben beliebige Prozentsätze. Die Prozentsätze nach Absatz 2 Nummer 2 beziehen sich auf den Restbetrag; die 30-Prozent-Erdarbeitsrate beim Grundstückseigentum hat eine andere Basis. Keine Rechnungsfälligkeit allein aus einer Bauträger-E-Mail ableiten. Eine Sicherheit nach MaBV Paragraf 7 ist ein gesondert zu prüfender Weg.

### 3.4. Vertragsentwurf vervollständigen

Trenne Errichtung, Übereignung, Besitzübergang, Abnahme, Mängelrechte und Schlusszahlung. Gemeinschaftseigentum und Sondereigentum benötigen passende Abnahmeregeln. Prüfe BGB Paragrafen 650u und 650v sowie MaBV nach konkretem Vertrag; Verbraucherbauvertrag und Bauträgervertrag nicht gleichsetzen. Belastungsvollmacht, Rang und Lastenfreistellung mit der Käuferfinanzierung abstimmen, keine pauschale Sicherung fremder Verbindlichkeiten.

### 3.5. Vollzug vorbereiten

Führe Vormerkung, Genehmigungen, Lastenfreistellungsunterlagen, Fälligkeitsmitteilung, Zahlung und Eigentumsumschreibung als getrennte Schritte. Ein Mitarbeiterentwurf ist keine Fälligkeitsfreigabe. Bei widersprüchlicher Bankbestätigung nur den betroffenen Schritt sperren und die übrige Mappe fertigstellen.

### 3.6. Antwort in die Vertragsfassung übernehmen

Ist nur der Preis eines Sonderwunsches bestätigt, aber nicht dessen Plan, frage genau nach der technischen Fassung. Ist eine Übergabeänderung vereinbart, gleiche Besitz, Nutzen, Lasten und Mietabrechnung ab. Bereite zunächst die konkrete Rückfrage und die belegbaren Vertragsteile vor; nach Antwort den vollständigen Entwurf fortführen, nicht erneut alle Käuferdaten abfragen. Zur Grundbuchanmeldung anschließend nur den betroffenen Auftrag an [Grundbuch und Rang](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/notariat-alltag/skills/grundbuchantrag-rangstelle-notarielle/SKILL.md) übergeben.

### 3.5. Vollzug ohne bedingte Auflassung vorbereiten

Die Auflassung selbst darf nach [BGB Paragraf 925 Absatz 2](https://www.gesetze-im-internet.de/bgb/__925.html) nicht von Kaufpreiszahlung oder Bauabnahme abhängig gemacht werden. Unbedingte Einigung und vertragliche Weisung an den Notar, den Umschreibungsantrag erst bei nachgewiesenen Voraussetzungen einzureichen, getrennt ausformulieren. Eine Schlussrate oder Abnahmebestätigung ersetzt weder den Zahlungsnachweis noch die Prüfung weiterer Einreichungsvoraussetzungen.

## 4. Quellenpflicht

[Amtliche Formwege](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/notariat-alltag/references/mitarbeiter-formwege.md), BGB Paragrafen 311b, 650u und 650v; BeurkG Paragraf 17; MaBV Paragrafen 3 und 7. [Zitierweise](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/notariat-alltag/references/zitierweise.md). Konkrete Rechtsprechung etwa zu Abnahmeklauseln nur nach verifizierter Fundstelle einsetzen.

## 5. Ausgabeformat

Vollständig formulierter Kaufvertragsentwurf zur notariellen Prüfung, Anlagenverzeichnis mit Versionsstand und getrenntes Nachforderungsschreiben. Keine erfundenen Genehmigungen oder bloßen Klauselrümpfe. Times New Roman 11 pt, dezimale Gliederung. Ein Zahlplan enthält Betrag, Rechenbasis, Bautenstand und zusätzliche Fälligkeitsbedingungen.

## 6. Beispiel

Die Käufer erhalten vom Vertrieb am 2. September Erwerbsunterlagen, die vollständige notarielle Fassung erst später. Übernimm den Vertriebsversand nicht als Beginn der Regelüberlegungsfrist. Ein noch nicht abgestimmter Grundriss bleibt ein offener Vertragsbestandteil.

---

## Skill: `geschaeftsfuehrer-bestellung-register`

_Bereitet Geschäftsführerbestellung, Abberufung und Handelsregisteranmeldung für GmbH und UG vor. Gleicht Beschlussdatum, Wirksamkeit, Vertretungsregel und Versicherungen ab und stellt die elektronische Registermappe zur notariellen Freigabe zusammen._

# 1. Geschäftsführerwechsel und Handelsregisteranmeldung vorbereiten

## 1. Zweck und Anwendungsfall

Aus Gesellschafterauftrag und Registerbestand werden getrennte Beschluss- und Anmeldedokumente. Die Bestellung ist nicht der Anstellungsvertrag; die Eintragung wird nicht mit dem internen Wirksamkeitsbeginn gleichgesetzt.

## 2. Eingaben

Satzung, Registerauszug, Gesellschafterliste, Beschluss oder Beschlusswunsch, Annahme der Bestellung, Personalien und gewünschte Vertretung. Belegte Daten übernehmen und nur widersprechende oder entscheidende fehlende Angaben nachfragen.

## 3. Ablauf

### 3.1. Beschluss und Datum festlegen

Prüfe Zuständigkeit nach GmbHG Paragraf 46 Nummer 5 und Satzung, Einberufung, Stimmen, Annahme und Bedingungen. Für die bloße Bestellung oder Abberufung besteht regelmäßig keine gesetzliche Beurkundungspflicht; Satzungsänderungen und gekoppelte Vorgänge gesondert behandeln. Kündigung des Anstellungsvertrags folgt nicht automatisch aus der Abberufung.

### 3.2. Vertretung wortgetreu abgleichen

Trenne allgemeine Satzungsregel, konkrete Einzelvertretungsbefugnis und Befreiung von BGB Paragraf 181. Übernimm keine Befreiung aus einem fremden Muster. Bei zeitversetztem Ausscheiden und Eintritt prüfen, wer im Zwischenzeitraum vertreten und anmelden kann. Einen ausgeschiedenen Geschäftsführer nicht ohne Prüfung als Anmelder einsetzen.

### 3.3. Anmeldung und Nachweise vorbereiten

GmbHG Paragraf 39 verlangt die Anmeldung und Nachweise; Absatz 2 nennt Original oder öffentlich beglaubigte Abschrift der Urkunden zur Bestellung beziehungsweise Beendigung. Die Versicherung nach Absatz 3 mit den aktuellen Anforderungen und erforderlicher Belehrung dem Notar vorlegen. Nicht als bereits abgegeben markieren. Konkrete Anmeldezuständigkeit anhand Paragraf 78 und des Übergangsstands prüfen.

### 3.4. Vollzug überwachen

Die Anmeldung wird nach HGB Paragraf 12 formgerecht elektronisch eingereicht. Mitarbeiter bereiten die Mappe vor, fingieren aber keine Signatur oder Einreichung. Nach Freigabe Versandnachweis und nach tatsächlichem Eingang Registermitteilung abgleichen. Allein wegen eines Geschäftsführerwechsels ist keine Gesellschafterlistenänderung nötig.

## 4. Quellenpflicht

GmbHG Paragrafen 6, 35, 38, 39, 46 und 78; HGB Paragraf 12; BGB Paragraf 181. [Amtliche Formwege](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/notariat-alltag/references/mitarbeiter-formwege.md) und [Zitierweise](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/notariat-alltag/references/zitierweise.md).

## 5. Ausgabeformat

Beschlussentwurf, Anmeldeentwurf, Nachweise und Vorlagevermerk in vollständigen Sätzen. Times New Roman 11 pt, dezimale Gliederung, Kennzeichnung als Entwurf zur notariellen Prüfung. Keine Halbsatzvorlagen, vorausgefüllten Unterschriften oder behaupteten Registereinträge.

## 6. Beispiel

Der alte Geschäftsführer soll am 10. Oktober ausscheiden; der neue soll am selben Tag beginnen. Halte beide Daten fest und prüfe, wer wann anmeldet. Eine vorherige E-Mail macht den Wechsel nicht schon wirksam.

---

## Skill: `kostenrechnung-gnotkg`

_Erstellt nachvollziehbare Entwürfe notarieller Kostenberechnungen aus Auftrag, Urkunde und Vollzug. Ordnet Kostenschuldner, Geschäftswerte, Gebührentatbestände, Auslagen und Vorschüsse zu, ohne feste Gebühren aus unverifizierten Tabellen zu erfinden._

# 1. Notarielle Kostenberechnung vorbereiten

## 1. Zweck und Anwendungsfall

Berechne den beauftragten Vorgang anhand der tatsächlichen Tätigkeiten. Ein Kostenvoranschlag ist keine endgültige Kostenforderung. Mitarbeiter bereiten vor; Prüfung und Veranlassung der Kostenanforderung bleiben beim Notar.

## 2. Eingaben

Auftrag, Geschäft und Datum, Urkunde oder abgebrochenen Entwurf, Vollzugstätigkeiten, Wertbelege, Kostentragungsabrede, Auslagen und Vorschüsse lesen. Frage bei einer Schätzung gezielt nach fehlendem Wert oder Leistungsumfang, nicht erneut nach sämtlichen Beteiligten.

## 3. Ablauf

### 3.1. Tätigkeiten und Kostenschuldner abgrenzen

Verfahren, selbstständige Geschäfte und tatsächlich ausgeführte Vollzugs- oder Betreuungstätigkeiten zuordnen. Nach GNotKG Paragrafen 29 ff. gesetzliche Kostenschuld von einer internen Kostentragungsvereinbarung unterscheiden. Mehrere Urkunden nicht automatisch als mehrere volle Gebühren abrechnen; Gegenstandsgleichheit, Zusammenrechnung und besondere Vorschriften prüfen.

### 3.2. Werte und Gebühren mit Herkunft rechnen

Für jede Position Wertvorschrift, Wertbeleg, Nummer des Kostenverzeichnisses, Satz und gültige Tabelle nennen. Kaufpreis ist nicht bei jeder Tätigkeit der maßgebliche Geschäftswert; bei Grundpfandrechten, Gesellschaftsmaßnahmen und Vollmachten die einschlägigen Sondervorschriften lesen. Fehlt die aktuelle Tabelle, liefere eine bezeichnete Rechenvorlage und die fehlende Quelle, keinen geratenen Eurobetrag.

### 3.3. Rechnung und Begründung fertigstellen

Anforderungen nach GNotKG Paragraf 19 beachten: Verfahren oder Geschäft, Kostenverzeichnisnummern, Geschäftswerte, Einzelbeträge und gezahlte Vorschüsse. Auslagen und Umsatzsteuer nachvollziehbar berechnen, Rundung prüfen. Die aktuelle Textform nicht durch eine erfundene allgemeine Unterschriftspflicht ersetzen. Schätzannahmen nur in Kostenauskunft und Begleitvermerk führen, nicht als feststehende Gebührenfakten.

### 3.4. Bei Änderung fortschreiben

Wenn nur der Kaufpreis berichtigt wird, betroffene Wertpositionen nachrechnen; unveränderte Fremdauslagen nicht nochmals erheben. Bei Abbruch den tatsächlichen Bearbeitungsstand und einschlägigen Tatbestand prüfen, nicht ungeprüft die geplante Beurkundung abrechnen. Einwendungen zur konkreten Position beantworten; gerichtliche Überprüfung nach Paragraf 127 gesondert dem Notar vorlegen.

### 3.5. Den zeitlich richtigen Gebührenstand wählen

Bei einer Gesetzesänderung richtet sich die notarielle Kostenberechnung nach [GNotKG Paragraf 134 Absatz 2](https://www.gesetze-im-internet.de/gnotkg/__134.html) grundsätzlich nach bisherigem Recht, wenn der Auftrag vor Inkrafttreten erteilt wurde. Auftragseingang und maßgebliche Änderung belegen; das Rechnungsdatum allein rechtfertigt keine Anwendung der neuesten Tabelle. Nach beantworteter Wertanfrage den Rechenweg mit Geschäftswert, KV-Nummer, Satz, Tabelle, Auslagen und Steuer vollständig neu berechnen und den Rechnungsentwurf ersetzen; alte und neue Beträge nicht vermischen.

## 4. Quellenpflicht

[GNotKG](https://www.gesetze-im-internet.de/gnotkg/) einschließlich aktueller Anlagen und [Paragraf 19](https://www.gesetze-im-internet.de/gnotkg/__19.html). Quellen und Tabellenstand nach [Zitierweise](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/notariat-alltag/references/zitierweise.md) dokumentieren. Keine veralteten Pauschalgebühren aus dem Gedächtnis.

## 5. Ausgabeformat

Rechenfähige Kostenberechnung mit vollständigem Anschreiben zur notariellen Prüfung; notwendige Zahlen dürfen tabellarisch stehen. Times New Roman 11 pt, dezimale Gliederung. Offenlassen einer fehlenden Wertgrundlage ist besser als eine scheinbar fertige, unbelegte Rechnung.

## 6. Beispiel

Zum Anteilskauf kommt eine gesonderte Verpfändung hinzu. Prüfe die tatsächlichen Erklärungen und Kostenverzeichnispositionen. Multipliziere nicht bloß den Kaufpreis mit einer allgemeinen „Notarquote“.

---

## Skill: `kapitalerhoehung-beschluss-register`

_Bereitet die GmbH-Kapitalerhöhung als zusammenhängenden Vorgang vor: Beschluss, Bar- oder Sacheinlage, Übernahmeerklärungen, Einzahlungsnachweise und Registervollzug. Trennt Beurkundung des Beschlusses von Beglaubigung der Übernahme und Anmeldung._

# 1. Kapitalerhöhung beschließen und zum Register vorbereiten

## 1. Zweck und Anwendungsfall

Bereite eine GmbH-Kapitalerhöhung vor. Bei AG, Kapitalerhöhung aus Gesellschaftsmitteln, genehmigtem Kapital oder verschleierter Sacheinlage nicht den normalen Barkapitalweg fortsetzen, sondern den Sonderweg klären lassen.

## 2. Eingaben

Registerauszug, vollständige Satzung, letzte Gesellschafterliste, Beteiligungsabsprache, Einlageart, Nennbetrag, Aufgeld und Beschlusstag. Lies vorhandene Unterlagen vor einer Rückfrage. Ein Beteiligungsangebot ist noch keine Übernahmeerklärung.

## 3. Ablauf

### 3.1. Kapital und Stimmrechte abstimmen

Rechne bisherige Anteile, Erhöhungsbetrag und neues Stammkapital. Trenne Nennbetrag und Aufgeld. Prüfe Einberufung, Beschlussfähigkeit, Dreiviertelmehrheit nach GmbHG Paragraf 53 Absatz 2, strengere Satzungsvorgaben und betroffene Zustimmungen. Bezugsrechte und deren Behandlung anhand Satzung und Beschlusskonzept dem Notar vorlegen; kein automatischer Verzicht durch Nichtteilnahme.

### 3.2. Drei verschiedene Erklärungen erstellen

Der satzungsändernde Beschluss muss nach Paragraf 53 Absatz 3 notariell beurkundet werden. Die Erklärung des Übernehmers nach Paragraf 55 Absatz 1 ist notariell aufgenommen oder beglaubigt. Die Registeranmeldung folgt HGB Paragraf 12. Bloße Beglaubigung aller Unterschriften genügt nicht für den Erhöhungsbeschluss.

### 3.3. Kapitalaufbringung belegen

Bei Barerhöhung gelten Paragraf 56a und die dort bezeichneten Teile von Paragraf 7; die Mindesteinzahlung ist je neuem Anteil zu prüfen. Keine zusätzliche pauschale Forderung von 12500 Euro für jede Erhöhung aus dem Gründungsrecht ableiten. Bei Sacheinlagen Gegenstand, Zuordnung, Bewertung und Unterlagen nach Paragrafen 56 und 57 prüfen lassen. Verrechnung, Hin- und Herzahlen oder vorherige Zahlung gesondert markieren. Aufgeld wird nicht zu Nennkapital.

### 3.4. Reihenfolge für den Vollzug festhalten

Beschluss, vollständige Übernahme, erforderliche Leistung und Geschäftsführer-Versicherung müssen zur Anmeldung passen. Bereite Übernehmerliste und notariell bescheinigten vollständigen Satzungswortlaut nach Paragrafen 54 und 57 vor; verwechsle die Übernehmerliste nicht mit der Gesellschafterliste nach Paragraf 40. Die Satzungsänderung wird erst mit Eintragung wirksam, Paragraf 54 Absatz 3. Einen gleichzeitigen Geschäftsführerwechsel mit eigenem Wirksamkeitsdatum bearbeiten.

### 3.5. Alle erforderlichen Anmeldenden einbeziehen

GmbHG Paragraf 78 verlangt für die Anmeldung nach Paragraf 57 sämtliche Geschäftsführer. Bei einem gleichzeitigen Organwechsel deshalb den tatsächlichen Wirksamkeitszeitpunkt der Bestellung beziehungsweise Abberufung ermitteln und die zu diesem Anmeldezeitpunkt erforderlichen Geschäftsführer einbeziehen. Einzelvertretungsbefugnis verkürzt diesen Kreis nicht. Eine Bankgutschrift korrigiert die Einlagenrechnung; sie belegt für sich weder die freie Verfügung der Geschäftsführung noch eine bereits abgegebene Versicherung. Nach bestätigtem Zahlungseingang den vollständigen Anmeldeentwurf samt Anlagen aktualisieren.

## 4. Quellenpflicht

GmbHG Paragrafen 53 bis 57 sowie 40; HGB Paragraf 12. [Mitarbeiter-Formwege](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/notariat-alltag/references/mitarbeiter-formwege.md), [Zitierweise](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/notariat-alltag/references/zitierweise.md). Weitere Quellen zur konkreten Sacheinlage oder Bezugsrechtsmaßnahme gezielt verifizieren.

## 5. Ausgabeformat

Ausformulierte Entwürfe für Beschluss, Übernahme und Anmeldung sowie Kapitaltabelle mit Altbestand, Zugang und Endbestand. Offene Nachweise separat; keine erfundene Versicherung. Times New Roman 11 pt, dezimale Gliederung, Status „Entwurf zur notariellen Prüfung“. Keine Klauselrümpfe als Endprodukt.

## 6. Beispiel

Ein Investor zahlt 50000 Euro für einen neuen Anteil von 10000 Euro. Weise 10000 Euro Nennbetrag und 40000 Euro Aufgeld getrennt aus. Ein Überweisungsentwurf ist noch kein Einzahlungsnachweis.

---

## Skill: `formweg-beurkundung-beglaubigung`

_Ordnet für die Notariatsmitarbeiter jede konkrete Erklärung dem passenden Formweg zu: Beurkundung, Unterschriftsbeglaubigung, Abschriftsbeglaubigung oder einfache Beschlussfassung. Bereitet Termin, Nachweise und getrennte Registerunterlagen vor._

# 1. Beurkundung und Beglaubigung sicher vorbereiten

## 1. Zweck und Anwendungsfall

Kläre die Form einer bestimmten Erklärung, nicht bloß den Titel des Gesamtvorgangs. Mitarbeiter bereiten vor; nur der Notar nimmt die Amtshandlung vor. Eine Unterschriftsbeglaubigung ersetzt keine notwendige Beurkundung des Inhalts.

## 2. Eingaben

Lies Erklärung, Verwendungszweck, Empfänger, Parteien und vorhandene Vorurkunde. Bei „Bitte beglaubigen“ kläre nur, ob Unterschrift, Abschrift oder Beurkundung gemeint ist, soweit das nicht bereits aus den Unterlagen folgt.

## 3. Ablauf

### 3.1. Jede Erklärung separat zuordnen

| Erklärung | Form und Quelle | Vorbereitung |
| --- | --- | --- |
| Grundstückskauf oder Bauträgerkauf | Beurkundung, BGB Paragraf 311b Absatz 1 | Vertragsentwurf, Anlagen und Verbraucherfrist |
| GmbH-Gesellschaftsvertrag | Beurkundung, GmbHG Paragraf 2 | Satzung, Beteiligte und Vertretung |
| Kapitalerhöhungsbeschluss | Beurkundung, GmbHG Paragraf 53 Absatz 3 | Beschlussentwurf, Mehrheit und Satzung |
| Übernahme eines neuen Geschäftsanteils | Notariell aufgenommen oder beglaubigt, GmbHG Paragraf 55 Absatz 1 | Eigene Erklärung jedes Übernehmers |
| GmbH-Anteilsabtretung und Verpflichtung dazu | Beurkundung, GmbHG Paragraf 15 Absätze 3 und 4 | Genau bezeichnete Anteile und Bedingungen |
| GmbH-Anteilsverpfändung | BGB Paragraf 1274 zusammen mit GmbHG Paragraf 15 Absatz 3 | Pfandvertrag statt Gesellschafterwechsel |
| Grundbuchbewilligung | GBO Paragrafen 19 und 29 | Öffentliche oder öffentlich beglaubigte Urkunde nach Inhalt |
| Vollstreckungsunterwerfung bei Grundschuld | Notarielle Urkunde, ZPO Paragraf 794 Absatz 1 Nummer 5 | Dingliche und persönliche Erklärung trennen |
| Handelsregisteranmeldung | HGB Paragraf 12 | Öffentliche Beglaubigung und elektronische Einreichung |
| Geschäftsführerbestellung | Regelmäßig Beschluss ohne gesetzliche Beurkundungspflicht, Satzung prüfen | Beschlussnachweis und separate Anmeldung |

### 3.2. Bereits geleistete Unterschrift behandeln

Für die Unterschriftsbeglaubigung nach BeurkG Paragraf 40 muss die Unterschrift vor dem Notar vollzogen oder anerkannt werden. Ein Mitarbeitervergleich mit dem Ausweisscan genügt nicht. Bewahre den vollständigen Erklärungstext. Leere oder nachträglich ergänzte Textfelder sind Anlass zur notariellen Entscheidung.

### 3.3. Termin und Übermittlung getrennt vorbereiten

Prüfe bei Video den gesetzlich zugelassenen Vorgang und das vorgesehene notarielle Verfahren. Ein gewöhnliches Videotelefonat ersetzt es nicht. Die Beglaubigung einer Abschrift bestätigt die Übereinstimmung mit der vorgelegten Vorlage; sie bestätigt weder deren sachliche Richtigkeit noch eine darauf befindliche Unterschrift. Dokumentiere, welche Vorlage tatsächlich vorlag.

## 4. Quellenpflicht

[Amtliche Formwege und Stand](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/notariat-alltag/references/mitarbeiter-formwege.md) sowie [Zitierweise](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/notariat-alltag/references/zitierweise.md). Absatznummern anhand des aktuellen Gesetzestextes prüfen. Für die Kapitalerhöhung nicht ungeprüft eine ältere Fassung von Paragraf 53 GmbHG übernehmen.

## 5. Ausgabeformat

Formblatt mit Erklärung, Norm, Form, Unterzeichner, Nachweis und nächstem Termin sowie ein ausformuliertes Anschreiben. Entwürfe bleiben als solche gekennzeichnet. Format: Times New Roman 11 pt, dezimale Gliederung, vollständige Sätze statt eines Klauselskeletts.

## 6. Beispiel

Ein Geschäftsführerwechsel wird zusammen mit einer Kapitalerhöhung angemeldet. Trenne Bestellungsbeschluss, beurkundeten Erhöhungsbeschluss, Übernahmeerklärung und öffentlich beglaubigte Anmeldung. „Alles nur beglaubigen“ ist keine tragfähige Vorgangsbeschreibung.

---

## Skill: `urkundenentwurf-aendern-abgleichen`

_Arbeitet Mandantenkorrekturen in notarielle Entwürfe ein, gleicht Urkunde und Anlagen ab und trennt Entwurfsänderung, offensichtliche Unrichtigkeit und nachträgliche Vertragsänderung. Liefert bereinigte Fassung und gezielte Vorlage an den Notar._

# 1. Urkundenentwurf ändern und Fassungen abgleichen

## 1. Zweck und Anwendungsfall

Bearbeite eine benannte Ausgangsfassung und konkrete Änderungswünsche. Kein neues Standardmuster über eine bereits abgestimmte Urkunde legen. Mitarbeiter bereiten Korrekturen vor; Amtshandlungen und Freigaben bleiben beim Notar.

## 2. Eingaben

Benötigt werden Ausgangsdatei, Änderungsnachricht mit Absender und Datum, betroffene Anlagen und der tatsächliche Beurkundungsstand. Fehlt nur der Freigabestand, frage genau danach. Ein Dateiname „final“ beweist weder Zustimmung sämtlicher Beteiligter noch Beurkundung.

## 3. Ablauf

### 3.1. Vor oder nach Beurkundung verzweigen

Vor Beurkundung Änderungswunsch und bestätigten Vertragswillen auseinanderhalten. Bei einem einseitigen Mehrpreiswunsch die Gegenpartei nicht als bereits einverstanden darstellen. Nach Abschluss der Niederschrift greift BeurkG Paragraf 44a: offensichtliche Unrichtigkeit und sonstige inhaltliche Änderung verlangen unterschiedliche notarielle Verfahren. Keine nachträgliche Überschreibung der Urschrift und kein fingierter Nachtragsvermerk.

### 3.2. Abhängige Stellen gemeinsam ändern

Bei geändertem Kaufpreis Raten, Zahlungsanweisungen, Finanzierungsbedarf und Wertangaben prüfen. Bei neuer Anteilsnummer Vertrag, Übernahmeerklärung, Gesellschafterliste und Anmeldung abgleichen. Bei neuer Person Vertretung, Erklärungszuständigkeit und Unterschriftsfelder prüfen. Ein Bankformblatt mit abweichender persönlicher Haftung nicht stillschweigend anpassen; die Entscheidung dokumentiert zur notariellen Prüfung vorlegen.

### 3.3. Anlagen und Verbraucherbereitstellung erhalten

Planstand, Baubeschreibung, Vollmacht und Registerstand mit Version bezeichnen. Ein angekündigter Plan ist keine beigefügte Anlage. Bei Verbraucherverträgen Umfang der Änderung und bisherige Bereitstellung nach BeurkG Paragraf 17 Absatz 2a dem Notar zur Beurteilung vorlegen. Weder jede Tippkorrektur noch jede grundlegende Leistungsänderung pauschal gleich behandeln.

### 3.4. Nach Antwort eine konsistente Fassung liefern

Kommt die Freigabe nur zum Preis, ändere nicht zusätzlich Abnahme oder Fertigstellung. Widersprüchliche Antworten mit zwei klar bezeichneten Alternativen vorlegen. Sobald der Punkt geklärt ist, bereinigten Text und auf Wunsch Vergleichsfassung ausgeben; nicht bei einer Liste vorgeschlagener Änderungen stehen bleiben. Übergabe zur abschließenden Prüfung an `urkundenmappe-zur-freigabe`, ohne Mandantendaten erneut zu erheben.

## 4. Quellenpflicht

[BeurkG Paragraf 44a](https://www.gesetze-im-internet.de/beurkg/__44a.html) und [Paragraf 17](https://www.gesetze-im-internet.de/beurkg/__17.html). BGH, Urteil vom 07.02.2013, III ZR 121/12: Der bloße Terminwunsch ersetzt den Übereilungsschutz nicht; keine automatische Vertragsnichtigkeit daraus ableiten. Fundstelle und Reichweite stehen in [Mitarbeiter-Formwege](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/notariat-alltag/references/mitarbeiter-formwege.md).

## 5. Ausgabeformat

Vollständig ausformulierte Neufassung als „Entwurf zur notariellen Prüfung“, getrennt davon knapper Änderungsvermerk mit betroffenen Stellen und verbleibender Entscheidung. Times New Roman 11 pt, dezimale Gliederung. Keine Urkunde mit internen Kommentaren im Erklärungsinhalt versandfertig nennen.

## 6. Beispiel

Die Baubeschreibung enthält eine noch nicht bestätigte Küchenverlegung. Der Vertrieb nennt einen geschätzten Mehrpreis. Bereite eine konkrete Rückfrage zu Leistung, Plan und Preisfreigabe vor und führe den gesicherten Kaufgegenstand fort. Erst nach Antwort die betroffenen Anlagen und Preisregeln ändern.

---

## Skill: `gmbh-anteile-uebertragen-verpfaenden`

_Bereitet Verkauf, Abtretung und Verpfändung von GmbH-Geschäftsanteilen für das Notariat vor. Ordnet Anteilsnummern, Zustimmung, Kaufpreis, Sicherungszweck und Vollzugsbedingungen und hält Gesellschafterwechsel und bloße Belastung auseinander._

# 1. GmbH-Anteile übertragen und verpfänden

## 1. Zweck und Anwendungsfall

Bereite Anteilskauf oder Kreditsicherheit anhand der konkreten Gesellschaft vor. Mitarbeiter sammeln Erklärungen und erstellen Entwürfe; der Notar prüft Form, Vertretung, Wirksamkeit und Listenbescheinigung. Dies ist kein automatisches Finanzierungs- oder Zahlungswerkzeug.

## 2. Eingaben

Registerauszug, Satzung, Gesellschafterliste, Erwerbsnachweise, Beteiligte, Kaufabsprache und Bankauftrag. Bei Verpfändung zusätzlich gesicherte Forderung, Pfandgeber, Gläubiger, Freigabebedingungen und Rang. Firmenname und Prozentzahl reichen nicht zur eindeutigen Bezeichnung des Rechts.

## 3. Ablauf

### 3.1. Anteilsbestand rekonstruieren

Ordne laufende Nummer, Nennbetrag, Inhaber und Erwerbsgrund. Gleiche die Summe mit dem Stammkapital ab. Die Legitimationswirkung der Liste nach GmbHG Paragraf 16 ersetzt nicht in jeder Hinsicht den materiellen Erwerbsnachweis. Bei Unstimmigkeit keine Nummer oder Eigentümerstellung erfinden. Satzungsmäßige Zustimmung, Vorkaufsrechte und bestehende Belastungen gesondert erfassen.

### 3.2. Verkauf und Abtretung trennen

Beide Formtatbestände nach GmbHG Paragraf 15 Absätze 3 und 4 prüfen. Formuliere Kaufpreis, Fälligkeit, Zahlungsweg und Zeitpunkt beziehungsweise Bedingung der Abtretung eigenständig. Unterschriftsbeglaubigung genügt nicht. Vollmachten und mitbeurkundungsbedürftige Nebenabreden dem Notar vorlegen. Keine Zahlungsbestätigung aus einer Terminankündigung ableiten.

### 3.3. Verpfändung als eigenes Geschäft bearbeiten

Für die Verpfändung eines GmbH-Anteils führt BGB Paragraf 1274 in Verbindung mit GmbHG Paragraf 15 Absatz 3 zur notariellen Form. Benenne Pfandrecht, gesicherte Forderung, Umfang, Zustimmung und Freigabe. Die bloße Verpfändung überträgt nicht die Gesellschafterstellung und löst für sich keine Gesellschafterliste mit der Bank als Inhaber aus. Stimmrechte nicht ungefragt dem Pfandgläubiger zuschreiben.

### 3.4. Bedingungen in eine Vollzugsfolge bringen

Lege Eigentumserwerb, Pfandrechtsentstehung, Auszahlung und Kaufpreisnachweis zeitlich nebeneinander. Verlangt die Bank ein wirksames Pfand vor Zahlung, während die Abtretung erst mit Zahlung wirksam werden soll, darf der Entwurf die Lücke nicht verschweigen. Bereite konkrete Varianten und Rückfragen an Bank und Notar vor; entscheide die Sicherungsstruktur nicht selbst.

### 3.5. Listen- und Nachrichtenpaket vorbereiten

Nach wirksamem Gesellschafterwechsel Zeitpunkt und Zuständigkeit nach GmbHG Paragraf 40 beachten. Bereite Liste und Mitteilungen vor, behaupte keine notarielle Bescheinigung oder Einreichung. Bloße Belastungen ohne fiktiven Gesellschafterwechsel dokumentieren.

### 3.5. Erwerber und Verwahrung nach der Finanzierungsantwort abgleichen

Eine erwerbende GbR kann nach GmbHG Paragraf 40 Absatz 1 nur als eingetragene Gesellschaft in die Gesellschafterliste aufgenommen werden. Registereintragung und Identität der GbR vor Listenfertigung nachweisen; ihren Gesellschaftern nicht die erworbenen GmbH-Anteile persönlich zuschreiben.

Eine Finanzierungslücke erlaubt keine automatische notarielle Verwahrung. BeurkG Paragraf 57 Absätze 2 bis 6 verlangt insbesondere ein berechtigtes Sicherungsinteresse, hinreichend bestimmte schriftliche Verwahrungsanweisungen und deren Annahme durch den Notar; zusätzliche Bankauflagen müssen damit vereinbar sein. Bei einer akzeptierten direkten Zahlungsstruktur Abtretungsbedingung, Auszahlungsvoraussetzungen, Pfandbestellung und Rang ausformulieren und gegenseitig prüfen. Eine bloße Gesprächsbereitschaft der Bank ist noch keine Änderung ihrer Bedingungen.

## 4. Quellenpflicht

GmbHG Paragrafen 15, 16 und 40; BGB Paragraf 1274. [Amtliche Formwege](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/notariat-alltag/references/mitarbeiter-formwege.md) und [Zitierweise](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/notariat-alltag/references/zitierweise.md). Zustimmungsklauseln aus der geltenden Satzung verwenden, Sonderfragen gezielt verifizieren.

## 5. Ausgabeformat

Vollständiger Vertragsentwurf mit getrennten schuldrechtlichen und dinglichen Erklärungen, Anteilstabelle und bedingungsabhängiger Vollzugsliste. Entwurf zur notariellen Prüfung, Times New Roman 11 pt und dezimale Gliederung. Keine Klauselskelette, fingierten Freigaben oder Zahlungen.

## 6. Beispiel

Der Käufer finanziert 120000 Euro eines Kaufpreises von 168000 Euro. Die Bank möchte die gekauften Anteile als Sicherheit. Trenne Kaufpreiszahlung, Abtretungsbedingung und Pfandbestellung; führe die Bank nicht als Gesellschafter auf.

---

## Skill: `umwandlung-verschmelzung-kapitalerhoehung`

_Bereitet Verschmelzung, Spaltung und Formwechsel für das Notariat vor: Rechtsträger, Vertrags- und Beschlussentwürfe, Schlussbilanz, Zustimmungen und Registerfolge. Eine bloße GmbH-Kapitalerhöhung wird an den Kapitalmaßnahmen-Skill übergeben._

# 1. Umwandlungsurkunden und Registerfolge vorbereiten

## 1. Zweck und Anwendungsfall

Führe einen festgelegten Umwandlungsauftrag vom Gesellschaftsordner zu den zusammenpassenden Urkunden- und Anmeldeentwürfen. Mitarbeiter bereiten vor; notarielle Prüfung, Beurkundung, Bescheinigung und Einreichungsfreigabe bleiben beim Notar. Ein steuerliches Ziel allein bestimmt noch nicht den gesellschaftsrechtlichen Weg.

## 2. Eingaben

Lies Strukturvorgabe, Registerauszüge, geltende Satzungen, Beteiligungsaufstellung, Bilanzstichtag und vorhandene Beraterentwürfe. Bei bloßen Unterlagen ohne Auftrag frage: „Soll Vermögen auf einen anderen Rechtsträger übergehen oder soll derselbe Rechtsträger nur seine Rechtsform wechseln?“ Bei eindeutiger Vorgabe beginne die Urkundenmappe, ohne alle Möglichkeiten vorzutragen.

## 3. Ablauf

### 3.1. Rechtsträger und Vorgang festlegen

Bei Verschmelzung erfasse übertragenden und übernehmenden Rechtsträger, bei Spaltung Vermögenszuordnung und Empfänger der neuen Anteile. Ausgliederung und Abspaltung unterscheiden sich gerade darin, wer die Gegenleistung erhält. Bei Formwechsel bleibt der Rechtsträger bestehen. Eine bloße Kapitalerhöhung führt zu `kapitalerhoehung-beschluss-register`, nicht durch sämtliche Umwandlungsschritte.

### 3.2. Urkunden und Verzichtserklärungen zuordnen

Verschmelzungsvertrag nach UmwG Paragrafen 4 bis 6 und Zustimmungsbeschlüsse nach Paragraf 13 getrennt vorbereiten. Paragraf 6 gilt nicht nur für eine willkürliche Auswahl von Kapitalgesellschaften. Berichte, Prüfungen und zulässige Verzichte je Rechtsform und Beteiligungslage prüfen; Konzernzugehörigkeit ersetzt keinen gesetzlichen Ausnahmetatbestand. Spaltung nach Paragrafen 123 ff., Formwechselbeschluss nach Paragrafen 193 und 194 bearbeiten. Arbeitnehmerschutz und rechtzeitige Zuleitung an den zuständigen Betriebsrat nicht mit einer allgemeinen „Anhörung erledigt“ quittieren.

### 3.3. Anmeldung, Anlagen und Wirksamkeit trennen

Bei Verschmelzung regelt Paragraf 16 die Anmeldung, Paragraf 17 die Anlagen einschließlich Schlussbilanz und Paragraf 20 die Wirkung der Eintragung beim übernehmenden Rechtsträger. Den höchstens acht Monate vor Anmeldung liegenden Bilanzstichtag nach Paragraf 17 Absatz 2 konkret berechnen. Bei Spaltung gelten insbesondere Paragrafen 129 bis 131, beim Formwechsel Paragrafen 198 bis 202. Kein Abschlussdatum, steuerlicher Rückwirkungsstichtag oder Versandbeleg ersetzt die Registereintragung.

### 3.4. Nach einer Antwort fortsetzen

Kommt eine neuere Schlussbilanz, aktualisiere Bilanzanlage und Anmeldeplanung, nicht ungefragt Umtauschverhältnis und Vertragsdatum. Ändert sich die Beteiligungsstruktur, prüfe dagegen genau die betroffenen Mehrheiten, Verzichtsmöglichkeiten und Kapitalmaßnahmen erneut. Fehlende Steuerfreigabe als offene Abstimmung führen, nicht steuerliche Neutralität zusichern. Bei Auslandsbezug zunächst die besonderen grenzüberschreitenden Vorschriften bestimmen.

### 3.5. Fristen und Registerfolge konkret berechnen

Bei Verschmelzung nach [UmwG Paragraf 19 Absatz 1](https://www.gesetze-im-internet.de/umwg_1995/__19.html) erst Eintragung bei den übertragenden, dann beim übernehmenden Rechtsträger; die Wirkung folgt aus Paragraf 20. Bei Spaltung ist die Reihenfolge nach Paragraf 130 umgekehrt: zunächst bei den übernehmenden oder neuen Rechtsträgern, danach beim übertragenden; Paragraf 131 knüpft die Wirkung an dessen Eintragung. Registerbelege für jede Stufe zuordnen.

Beispiel: Schlussbilanz zum 31.12.2025 trägt im regulären Achtmonatsfenster keine erst für September 2026 vorgesehene Verschmelzungsanmeldung. Neuere Bilanz mit tatsächlichem Stichtag anfordern; nicht das alte Deckblatt umdatieren. Den tatsächlichen Anmeldezeitpunkt einschließlich Zugang beim Registergericht prüfen. Der zuständige Betriebsrat muss nach Paragraf 5 Absatz 3 den Verschmelzungsvertrag oder Entwurf spätestens einen Monat vor der beschließenden Versammlung erhalten; beim Formwechsel gilt Paragraf 194 Absatz 2. Ein Gesellschafterverzicht auf Bericht oder Prüfung erledigt diese Zuleitung nicht.

## 4. Quellenpflicht

Amtliche Grundlage: [UmwG](https://www.gesetze-im-internet.de/umwg_1995/), insbesondere Paragrafen 6, 13, 16, 17, 20, 123, 131, 193 und 202. Eintragungswirkungen nicht auf einen anderen Umwandlungstyp übertragen. Zitierweise nach [Quellenleitfaden](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/notariat-alltag/references/zitierweise.md); offene streitige Fragen dem Notar mit dem tatsächlich geprüften Rechtsstand vorlegen.

## 5. Ausgabeformat

Liefere den beauftragten Vertrag oder Beschluss und die dazugehörige Anmeldung vollständig ausformuliert als „Entwurf zur notariellen Prüfung“. Nur benötigte Anlagen ergänzen. Eine interne Reihenfolge mit abhängigen Eintragungen ersetzt die Urkundentexte nicht. Times New Roman 11 pt, dezimale Gliederung; keine erfundenen Versicherungen, Unterschriften oder Registermitteilungen.

## 6. Beispiel

Ein Tochterunternehmen soll auf die Mutter verschmolzen werden. Der Bilanzstichtag ist bekannt, die Anmeldung verschiebt sich. Prüfe zunächst das Achtmonatsfenster und fordere nötigenfalls eine neue Schlussbilanz an. Eine bloße Korrektur des Datums im bisherigen Bilanzdokument ist keine Lösung.

---

## Skill: `nachlassauseinandersetzung-grundbuch`

_Bereitet notarielle Nachlassauseinandersetzungen, Grundstücksübertragungen und Erbnachweise vor. Gleicht Testament, Eröffnung, Erbquoten, Vertretung und Grundbuch ab und führt fehlende Nachweise bis zum Vertrags- oder Anmeldeentwurf fort._

# 1. Nachlass und Grundstücksübertragung zusammenführen

## 1. Zweck und Anwendungsfall

Arbeite vom belegten Erbfall zur beauftragten Urkunde oder Grundbucherklärung. Erbe, Vermächtnisnehmer, Pflichtteilsberechtigter und Testamentsvollstrecker sind unterschiedliche Rollen. Mitarbeiter bereiten vor; rechtliche Prüfung, Belehrung und Amtshandlungen bleiben beim Notar.

## 2. Eingaben

Sterbenachweis, sämtliche vorgelegten Verfügungen von Todes wegen, Eröffnungsniederschrift, Erbschein oder Europäisches Nachlasszeugnis soweit vorhanden, Grundbuch, Vermögensunterlagen und konkrete Teilungswünsche. Bei einer bloßen Vollzugsfrage keine neue erbrechtliche Gesamtberatung starten.

## 3. Ablauf

### 3.1. Erbfolge und Verfügungsbefugnis belegen

Quoten aus Nachweisen herleiten, nicht aus einer Familienliste schätzen. Ein Pflichtteilsanspruch ist regelmäßig ein Geldanspruch und keine Miteigentumsquote am Haus. Bei Erbengemeinschaft gemeinschaftliche Verfügung über einzelne Nachlassgegenstände nach BGB Paragraf 2040 beachten; der Erbteil nach Paragraf 2033 ist etwas anderes. Testamentsvollstreckung, Vor- und Nacherbschaft oder Minderjährigkeit als eigene Nachweis- und Zustimmungsfragen führen.

### 3.2. Geeigneten Grundbuchnachweis bestimmen

GBO Paragraf 35: Öffentlich beurkundete Verfügung und Eröffnungsniederschrift können den Erbschein ersetzen; ein privatschriftliches Testament nicht pauschal gleich behandeln. Bei begründeten Nachweiszweifeln den tatsächlichen Inhalt der gerichtlichen Anforderung prüfen. GBO Paragraf 40 eröffnet bestimmte Ausnahmen von der Voreintragung. Eine Berichtigung auf alle Erben ist deshalb nicht stets vor jeder Übertragung erforderlich.

### 3.3. Gegenstände und Ausgleich urkundlich regeln

Gesamthänderische Berechtigung der Erben nicht als frei verfügbaren Bruchteil an jedem Grundstück formulieren. Übertragungsgegenstand, Gegenleistung, Schuldübernahme, Lasten, Besitz und Vollzugsbedingungen festlegen. Teilungsanordnung nach BGB Paragraf 2048, Vermächtnis und Quoten unterscheiden. Abweichende einvernehmliche Wünsche auf ihre rechtlichen Bindungen und Folgen prüfen, nicht automatisch als verboten oder wirksam behandeln.

Bei vorweggenommener Übertragung Rückforderungsrechte, Nießbrauch, Wohnrecht und Rang ihrem Inhalt nach unterscheiden. Ein Nießbrauch berechtigt nicht ohne Weiteres zum Verkauf. Steuerbefreiung, Pflichtteilsfolgen und Genehmigungsfreiheit nicht allein aus Familienzugehörigkeit zusagen.

### 3.4. Nachweise fortschreiben und fertigstellen

Nach Eingang eines Erbnachweises Namen, Quote, Verfügungsbefugnis und Vollmachten gegen Entwurf und Registerantrag abgleichen. Fehlt nur eine Genehmigung, die übrigen vereinbarten Teile ausformulieren und den betroffenen Vollzugsschritt offenhalten. Bei streitiger Erbfolge keine Verteilung als verbindlich festlegen; konkrete Unterlagenanforderung oder notarielle Entscheidungsvorlage erstellen.

## 4. Quellenpflicht

[GBO Paragraf 35](https://www.gesetze-im-internet.de/gbo/__35.html), [Paragraf 40](https://www.gesetze-im-internet.de/gbo/__40.html), BGB Paragrafen 2033, 2040, 2042 und 2048 sowie [Zitierweise](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/notariat-alltag/references/zitierweise.md). Auslandsnachweise bei Bedarf über `auslandsurkunde-apostille-vollmacht` klären, ohne den gesamten Auftrag neu aufzunehmen.

## 5. Ausgabeformat

Vollständiger Auseinandersetzungs- oder Übertragungsentwurf beziehungsweise bestimmter Grundbuchantrag zur notariellen Prüfung. Interne Quotenkontrolle und fehlende Nachweise getrennt halten. Times New Roman 11 pt, dezimale Gliederung; keine fingierte Erbscheinserteilung oder Einigung.

## 6. Beispiel

Ein eröffnetes öffentliches Testament und eine Vollmacht aus dem Ausland liegen vor. Kläre getrennt, ob die Erbfolge damit nachgewiesen ist und ob die Vollmacht in benötigter Form vorliegt. Ein positiver Erbnachweis beseitigt nicht den offenen Vertretungsnachweis.

---

## Skill: `geldwaeschepruefung-immobilien`

_Bereitet im Notariat die Geldwäscheprüfung von Grundstücks- und Gesellschaftsvorgängen vor. Klärt Beteiligung und wirtschaftlich Berechtigte, gleicht Kaufpreiszahlungen ab und legt konkrete Nachweislücken oder Meldefragen dem Notar vor._

# 1. Beteiligung und Immobilienzahlung nachvollziehen

## 1. Zweck und Anwendungsfall

Bearbeite die konkrete Transaktion, nicht ungefragt das gesamte betriebliche Risikomanagement. Mitarbeiter stellen Nachweise und Rückfragen zusammen; notarielle Entscheidungen, Meldung und Vollzugsfreigabe bleiben beim Notar.

## 2. Eingaben

Nutze Beteiligtenangaben, Registerauszüge, Kontrollvereinbarungen, Kaufvertrag, Zahlungsbelege und bekannten Geldfluss. Schon geprüfte Identitätsdaten mit ihrem Prüfstand übernehmen. Eine bloße Namensübereinstimmung oder abweichender Kontoinhaber ist zunächst ein zu klärender Befund, kein bewiesenes Delikt.

## 3. Ablauf

### 3.1. Personen und Kontrolle bestimmen

Vertragspartner, Auftretenden, Vertreter und wirtschaftlich Berechtigten nach GwG Paragrafen 3 und 10 bis 12 auseinanderhalten. Stimmrechte, Kapital und sonstige Kontrolle anhand der wirklichen Struktur prüfen; Prozentketten nicht blind multiplizieren. Im Register fehlende Daten durch Nachweise klären. Eine Unstimmigkeitsmeldung und eine Verdachtsmeldung haben verschiedene Voraussetzungen.

### 3.2. Zahlungen dem Vertrag zuordnen

Kaufpreis, Fälligkeit, Empfänger, Teilbetrag, Wertstellung und Beleg verbinden. GwG Paragraf 16a Absatz 1 erfasst bei Immobiliengeschäften auch die dort genannten unzulässigen Zahlungsmittel und Anteilserwerbe an immobilienhaltenden Gesellschaften. Die besonderen Nachweis- und Grundbuchantragsregeln der Absätze 2 bis 4 beziehen sich auf die dort bezeichneten direkten Immobiliengeschäfte; sie nicht unterschiedslos auf jeden Anteilskauf übertragen.

Die Ausnahme für höchstens 10000 Euro in Absatz 5 hebt das Verbot des Absatzes 1 nicht auf. Zahlungsankündigung, ausgeführter Auftrag und beim Empfänger belegter Eingang bleiben getrennt. Eine Zahlung durch einen Dritten mit Vertrag, Beziehung und Mitteln erklären lassen, nicht automatisch als unzulässig oder unbedenklich einstufen.

### 3.3. Hindernis und Kommunikation trennen

Bei fehlendem schlüssigem Nachweis die Schritte nach Paragraf 16a Absatz 3 prüfen und dem Notar vorlegen. Verdachtsprüfung nach Paragraf 43, Immobiliensachverhalte nach der einschlägigen Meldeverordnung und Durchführungsbeschränkungen nach Paragrafen 46 und 16a getrennt behandeln. Die besondere Fünftagesregel nicht mit der allgemeinen Wartefrist vermischen. Nach Paragraf 47 zulässige Außenkommunikation prüfen; ein interner Verdachtsvermerk gehört nicht ungeprüft in die Mandantenmail.

### 3.4. Neue Belege gezielt einarbeiten

Wird eine Teilzahlung nachgewiesen, nur den betreffenden Zahlungsstand ändern. Fehlende Restzahlung, ungeklärte Kontrolle oder anderes Vollzugshindernis bleibt offen. Übergib an `vollzug-fristen-wiedervorlage` den konkreten gesperrten Schritt und den benötigten Nachweis, nicht das gesamte Risikoprotokoll.

### 3.5. Nachweise und eine etwaige Meldung getrennt nachführen

Ein nachgereichter Kontoauszug kann den Zahlungsnachweis vervollständigen, beseitigt aber nicht automatisch einen bereits bestehenden Verdacht. Bei GwG Paragraf 16a Absatz 3 die besonderen Voraussetzungen für den Eintragungsantrag und gegebenenfalls den dort genannten fünften Werktag nach dem Abgangstag einer Meldung beachten; nicht schematisch die allgemeine Dreitagesregel aus Paragraf 46 einsetzen. Samstag gilt nach Paragraf 46 Absatz 1 nicht als Werktag; behördliche Untersagung und zulässige Freigaben gesondert prüfen. Eine Fristübersicht enthält Abgangstag, maßgebliche Arbeitstage und offenen Freigabestatus, keine erfundene Entwarnung. An die Beteiligten gerichtete Nachforderungen dürfen eine beabsichtigte oder erstattete Meldung unter Verstoß gegen Paragraf 47 nicht offenlegen.

## 4. Quellenpflicht

[GwG](https://www.gesetze-im-internet.de/gwg_2017/), besonders [Paragraf 16a](https://www.gesetze-im-internet.de/gwg_2017/__16a.html), aktuelle Meldevorschriften und notariatsbezogene Aufsichtshinweise prüfen. Künftig anwendbare europäische Regelungen nicht vor ihrem Anwendungstag als geltende deutsche Prüfschritte ausgeben. Quellen nach [Zitierweise](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/notariat-alltag/references/zitierweise.md) belegen.

## 5. Ausgabeformat

Konkrete Nachforderung in vollständigen Sätzen; getrennt davon interner Prüfvermerk zur notariellen Prüfung. Times New Roman 11 pt und dezimale Gliederung. Keine automatische Meldung, Zahlung oder Einreichung; keine öffentlich verteilte Liste sensibler Prüfbefunde.

## 6. Beispiel

Ein Käufer weist den gesamten Kaufpreis nach, jedoch stammt eine Überweisung von einer anderen Gesellschaft. Frage nach Rechtsgrund und Beziehung und ordne die Unterlagen der konkreten Zahlung zu. Der Rechenabgleich ersetzt nicht die Prüfung der Zahlungsherkunft.

---

## Skill: `grundbuchantrag-rangstelle-notarielle`

_Bereitet Grundbuchanträge, Rangänderungen und Antworten auf Zwischenverfügungen vor. Gleicht Bewilligung, Auflassung, Lastenfreistellung und Nachweisform ab und führt offene Eintragungshindernisse bis zur Vorlage an den Notar fort._

# 1. Grundbuchvollzug und Zwischenverfügung bearbeiten

## 1. Zweck und Anwendungsfall

Arbeite den konkreten Eintragungsauftrag ab: Eigentum, Vormerkung, Grundschuld, Dienstbarkeit, Rangänderung oder Löschung. Ein Kaufvertragsentwurf und ein bereits eingereichter Grundbuchantrag sind unterschiedliche Verfahrensstände. Mitarbeiter bereiten Anträge vor; Amtshandlungen und Freigaben bleiben beim Notar.

## 2. Eingaben

Lies die bezeichnete Urkunde, den vollständigen Grundbuchauszug, bereits gestellte Anträge, Eingangsbestätigungen und eine etwaige Zwischenverfügung. Bei mehreren Blättern nicht allein nach Adresse zuordnen. Frage nur nach dem fehlenden Nachweis, der die konkrete Eintragung trägt.

## 3. Ablauf

### 3.1. Recht und Nachweis zusammenführen

Für jedes Recht Blatt, laufende Nummer, Berechtigten, betroffenen Eigentümer, Bewilligung und Antrag bestimmen. GBO Paragrafen 13, 15, 19, 20 und 29 unterscheiden Antragsbefugnis, notarielle Vertretungsvermutung, Bewilligung, Einigung und Nachweisform. Eine Einigung ist nicht immer durch die bloße Unterschriftsbeglaubigung bewiesen. Bei Erbfolge Paragrafen 35 und 40 prüfen; keinen Erbschein oder eine Voreintragung unabhängig vom vorhandenen öffentlichen Testament verlangen.

### 3.2. Rang und Zahlungsvoraussetzungen prüfen

Bearbeitungsreihenfolge nach GBO Paragraf 17, Eintragungsregeln nach Paragraf 45 und materiellen Rang nach BGB Paragraf 879 getrennt lesen. Eingang ist keine pauschale Ranggarantie. Bei Rangänderung nach BGB Paragraf 880 die betroffenen Rechte und erforderlichen Erklärungen genau benennen. Löschung, Pfandfreigabe, Rangrücktritt und bloße Zahlungsquittung nicht austauschen. Beim Briefrecht den Briefverbleib prüfen; ein fehlender Brief wird nicht durch eine selbst verfasste Verlustbestätigung kraftlos.

### 3.3. Auf Zwischenverfügung reagieren

Frist, konkrete Beanstandung und verlangten Nachweis aus der Verfügung übernehmen. Nach GBO Paragraf 18 Hindernis und mögliche Behebung prüfen; nicht jede fehlende Erklärung lässt sich rangwahrend nachreichen. Antrag nicht ohne notarielle Entscheidung zurücknehmen. Bei Verzögerung rechtzeitig einen begründeten Verlängerungsantrag vorbereiten; bis Bewilligung bleibt die bisherige Frist maßgeblich. Paragraf 18 Absatz 2 ist keine besondere Fristverlängerungsnorm.

Beschwerde nach GBO Paragrafen 71 ff. gesondert prüfen. Nach Paragraf 72 entscheidet das Oberlandesgericht. Eine Beschwerde ersetzt weder fehlende Vollzugsnachweise noch eine Verlängerungsentscheidung. Die Statthaftigkeit gegen eine schon erfolgte Eintragung unterliegt den Grenzen von Paragraf 71 Absatz 2.

### 3.4. Nachreichung bis zur Rückmeldung verfolgen

Nach Eingang einer Bewilligung Person, Recht, Betrag und erfasste Teilfläche gegen Antrag und Verfügung vergleichen. Dann eine ausformulierte Nachreichung mit genau bezeichneten Anlagen erstellen. Eine Übermittlungsbestätigung ist noch kein Eintragungsnachweis. Nach Registermitteilung erst die tatsächlich vollzogenen Rechte abhaken und verbleibende Rang- oder Löschungsreste an `vollzug-fristen-wiedervorlage` übergeben.

### 3.5. Zahlungsbedingung von der Auflassung trennen

Nach [BGB Paragraf 925 Absatz 2](https://www.gesetze-im-internet.de/bgb/__925.html) ist eine bedingte oder befristete Auflassung unwirksam. „Die Auflassung gilt erst nach Kaufpreiszahlung“ deshalb nicht als Sicherung übernehmen. Stattdessen die unbedingte dingliche Einigung und die gesonderten Weisungen zur Einreichung des Umschreibungsantrags nach dem beurkundeten Vertrag unterscheiden. Zahlungseingang, Lastenfreistellung und sonstige Voraussetzungen belegen; die Vorbereitung eines Antrags ist keine Einreichung.

## 4. Quellenpflicht

[GBO](https://www.gesetze-im-internet.de/gbo/) und [BGB Paragraf 879](https://www.gesetze-im-internet.de/bgb/__879.html) anhand des Vorgangs prüfen. Für die konkrete Vollzugshandlung benötigte Quelle nach [Zitierweise](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/notariat-alltag/references/zitierweise.md) dokumentieren. Landesbezogene Übermittlungsvorgaben nur als geprüft ausgeben, wenn sie tatsächlich vorliegen.

## 5. Ausgabeformat

Antrag oder Antwort vollständig in Sätzen formulieren, mit zuständigem Grundbuchamt, Blatt, Antrag, Begründung soweit erforderlich und konkreten Anlagen. Interne Frist- und Rangnotiz getrennt halten. „Entwurf zur notariellen Prüfung“, Times New Roman 11 pt und dezimale Gliederung. Keine behauptete Eintragung, kein leerer Anlagenverweis.

## 6. Beispiel

Das Grundbuchamt verlangt einen Vertretungsnachweis. Die neue Datei zeigt nur eine einfache Kopie. Fordere die konkret erforderliche Nachweisform nach und bereite bei naher Frist einen begründeten Verlängerungsentwurf vor; die Kopie nicht als erledigte Beanstandung buchen.

---

## Anwendungshinweise

1. Diese Vollprüfung als Kontext einfügen oder als Datei hochladen.
2. Den eigentlichen juristischen Fall beschreiben.
3. Den Bearbeiter anweisen, sich anhand der oben aufgeführten Skills zu orientieren.
4. Entscheidungen nur nach Prüfung von Gericht, Datum, Aktenzeichen, tragender Aussage und amtlicher oder frei zugänglicher Quelle verwenden.
