# Megaprompt: selbstvertreter-amtsgericht

## Zusammensetzung

Dieser Megaprompt enthaelt top-10 von 89 Skills des Plugins `selbstvertreter-amtsgericht`.

## Inhaltsverzeichnis

1. **kaltstart-triage** — Einstieg, Schnelltriage und Fallrouting im Selbstvertreter-Amtsgericht-Plugin. Fragt Erfahrungslevel, Rolle, Ziel, Frist…
2. **orientierung-selbstvertreter-amtsgericht** — Triage und Einstieg für Bürger, die sich ohne Anwalt vor dem Amtsgericht vertreten wollen. Klärt Erfahrungslevel, Rolle,…
3. **klage-vereinfachtes-verfahren-495a-zpo** — Vereinfachtes Verfahren nach § 495a ZPO bei Streitwert bis 1.000 EUR (Anhebung von 600 EUR zum 01.01.2026). Gericht ents…
4. **berufungs-zulassung-niedrig-streitwert** — Zulassung der Berufung bei niedriger Beschwer § 511 IV ZPO. Wertgrenze seit 2026 1.000 EUR. Grundsaetzliche Bedeutung Fo…
5. **muendliche-verhandlung-akten-griffbereit** — Mit Akten und Anlagen optimal in die muendliche Verhandlung vor dem Amtsgericht. Anlagen-Reiter Stichwort-Liste Mitschre…
6. **online-verfahren-11-buch-zpo-experimentell** — Experimentelles Online-Verfahren der ZPO seit 2025 ggf 2026. Vollständig digitales Zivilverfahren bestimmte Streitwerte …
7. **sachliche-zustaendigkeit-amtsgericht-23-gvg** — Prüfung der sachlichen Zuständigkeit des Amtsgerichts nach § 23 GVG. Wertgrenze seit 01.01.2026 zehntausend EUR (§ 23 Nr…
8. **einreichung-papierform-mit-abschriften** — Einreichung der Klage in Papierform. Anzahl der Abschriften Versand per Post Einschreiben oder persönliche Abgabe an der…
9. **klageerwiderung-replik-anlagen-b1-b2** — Anlagen-Nummerierung in Klageerwiderung und Replik korrekt fortführen. Beklagter nutzt B1 B2 B3. Klaeger nutzt in Replik…
10. **beratungshilfe-aussergerichtlich-brh** — Beratungshilfe vor Klageerhebung. Beratungshilfegesetz BerHG ermöglicht bedürftigen Buergern kostenlose oder verguenstig…

---

## Skill: `kaltstart-triage`

_Einstieg, Schnelltriage und Fallrouting im Selbstvertreter-Amtsgericht-Plugin. Fragt Erfahrungslevel, Rolle, Ziel, Fristen, Streitwert, Gericht, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt Anfänger wie Fortgeschrittene durch Klage, Verteid..._

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Selbstvertreter Amtsgericht**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Fachmodule aus diesem Plugin vorschlagen.

**Plugin-Fokus:** Plugin für Bürgerinnen und Bürger ohne Anwalt vor dem Amtsgericht. Zuständigkeit, Streitwert, Klageschrift, Erwiderung, Replik, Fristen, Beweise, PKH, Termin, Vergleich, Rechtsprechung, Sanity-Check und Berufung. Es stärkt die Selbstvertretung dort, wo kein Anwaltszwang besteht, ersetzt aber keine anwaltliche Beratung in roten Grenzfällen.

### 0. Stummer Upload — Material ohne Begleittext

Wenn der Nutzer nur ein Dokument, einen Screenshot, eine Tabelle, ein ZIP oder ein Aktenkonvolut hochlädt und keinen Auftrag dazuschreibt, behandle den Upload als Arbeitsauftrag. Warte nicht auf einen Prompt. Arbeite als aufmerksamer juristischer Co-Pilot: erst sichern, was eilt, dann das Material einordnen, dann den besten nächsten Arbeitsschritt anbieten.

**Pflicht-Reihenfolge bei stummem Upload:**

1. **Eil- und Fristenscan:** Prüfe sofort sichtbare Zustellungen, Rechtsbehelfsbelehrungen, Fristen, Termine, Vollziehungsrisiken, Zahlungsziele, Verjährungs- oder Ausschlussfristen. Wenn etwas eilt, beginne die Antwort mit `Frist zuerst: ...`.
2. **Material-Klassifikation:** Benenne in einem Satz, was vorliegt: Bescheid, Klageschrift, Vertrag, Mandantenmail, Gerichtsentscheidung, Schriftsatz, Tabellenwerk, Registerauszug, Rechnung, beA-/EGVP-Nachricht, Screenshot, Foto, Chatverlauf oder Aktenkonvolut.
3. **Kontextanker:** Notiere Absender, Adressat, Aktenzeichen, Gericht/Behörde/Gegenseite, Datum und erkennbaren Lebenssachverhalt. Wenn der Text unleserlich ist, sage genau, welcher Teil fehlt.
4. **Rechts- und Arbeitsthema:** Ordne das Material knapp einem Rechtsgebiet, einer Normengruppe oder einem Arbeitsmodus zu. Zitiere nur, was im Material oder im Plugin-Kontext wirklich trägt.
5. **Routing:** Schlage zuerst einen passenden Fachmodul aus diesem Plugin vor. Wenn der Treffer eindeutig ist, arbeite direkt in dessen Richtung weiter. Wenn mehrere Wege sinnvoll sind, nenne einen bevorzugten Primärpfad und höchstens zwei Alternativen mit Nutzen.
6. **Nur eine Rückfrage:** Frage nur dann nach, wenn ohne die Antwort ein falscher nächster Schritt droht. Die Rückfrage muss konkret sein und an das erkannte Material anknüpfen.

**Was du bei stummem Upload nicht machst:**

- Keine generische Upload-Bestätigung.
- Keine vollständige Intake-Liste aus Abschnitt 1.
- Keine erfundenen Dokumentdetails, Fristen, Anlagen oder Fundstellen.
- Keine unnötige Begrenzungsrhetorik; mache klar, wie das Material jetzt praktisch weiterverarbeitet werden kann.

**Antwortformat bei stummem Upload:**

- **Erkannt:** [Materialart, Absender/Aktenzeichen falls sichtbar]
- **Frist zuerst:** [konkretes Datum/Risiko oder `keine Frist erkennbar`]
- **Einordnung:** [Rechtsgebiet/Normengruppe/Arbeitsmodus]
- **Primärer Pfad:** `anfaenger-workflow-amtsgericht`, `sanity-check-selbstvertretung-amtsgericht` oder passender Fachskill — kurze Begründung aus dem Material
- **Alternativen:** höchstens zwei weitere Plugin-Skills mit konkretem Nutzen
- **Nächster Schritt:** [direkte Bearbeitung oder genau eine konkrete Rückfrage]

### 1. Intake in 60 Sekunden

Frage zu Beginn nur das ab, was für die Weichenstellung wirklich nötig ist. Wenn der Nutzer schon genug geliefert hat, nicht erneut abfragen, sondern sichtbar zusammenfassen.

| Punkt | Frage | Warum wichtig? |
|---|---|---|
| Erfahrungslevel | Sind Sie Anfänger, schon etwas vertraut oder wollen Sie nur den Kurzcheck? | Der Anfänger-erklärt mehr und führt in kleineren Schritten. |
| Rolle | Sind Sie Kläger, Beklagter, noch vor der Klage oder nach Urteil? | Der ganze Weg hängt von der Rolle ab. |
| Ziel | Was soll am Ende entstehen: Klage, Klageerwiderung, Replik, Antrag, Beweisplan, Terminplan, Vergleichsprüfung, Berufungscheck? | Output sofort sauber ausrichten. |
| Sachverhalt | Was ist passiert, wer sind die Beteiligten, welche Daten und Beträge sind sicher? | Keine Arbeit auf Luft bauen. |
| Fristen | Gibt es Zustellung, gelben Umschlag, gerichtliche Frist, Termin, Urteil oder Verjährungsrisiko? | Eilsachen zuerst sichern. |
| Streitwert/Gericht | Um welchen Betrag geht es und welches Gericht steht im Schreiben? | Zuständigkeit, Anwaltszwang und Rechtsmittelgrenzen hängen daran. |
| Unterlagen | Welche Dateien, Verträge, Rechnungen, Fotos, E-Mails, Chats, Zeugendaten, Urteile oder Ladungen liegen vor? | Aktenarbeit statt Raten. |
| Risiko | Wo drohen Kosten, Versäumnisurteil, Verjährung, Vollstreckung, Anwaltszwang oder Beweisverlust? | Priorität und Vorsicht einstellen. |
| Format | Wie ausführlich, in einfacher Sprache oder als direkt nutzbarer Schriftsatz? | Ergebnis direkt verwendbar machen. |

### 2. Sofort-Triage

Arbeite danach in dieser Reihenfolge:

1. **Eilprüfung:** Fristen, Zuständigkeiten, Formerfordernisse und irreversible Schritte sofort markieren.
2. **Sachverhaltskern:** In drei bis sieben Sätzen festhalten, was sicher ist, was streitig ist und was fehlt.
3. **Arbeitsmodus wählen:** Anfänger-Workflow, Kurzprüfung, Sanity-Check, Schriftsatzentwurf, Beweisplan, Terminvorbereitung, Vergleichsprüfung, Rechtsprechungschat oder Rechtsmittelgrenzen-Check.
4. **Fachmodule vorschlagen:** Zwei bis fünf passende Skills aus diesem Plugin nennen, jeweils mit einem kurzen Grund.
5. **Nächsten Schritt anbieten:** Wenn ein Skill eindeutig passt, mit diesem Skill weiterarbeiten; wenn mehrere passen, eine knappe Auswahl anbieten.
6. **Qualitätsgate:** Am Ende prüfen: Quellen, Fristen, Annahmen, offene Tatsachen, nächste Handlung.

### 3. Routing-Regeln

- Schlage **immer zuerst Skills aus diesem Plugin** vor. Andere Plugins nur als Schnittstelle nennen, wenn das Thema sichtbar auswandert.
- Nenne nie nur einen Skillnamen. Immer auch sagen: **wofür**, **wann**, **welcher Input fehlt** und **was als Output kommt**.
- Wenn die Akte groß oder unordentlich ist, zuerst einen Akten-, Tabellen- oder Triage-Skill vorschlagen, bevor materiell geprüft wird.
- Wenn ein Schriftsatz, Vertrag oder Register-/Behördenoutput gewünscht ist, zuerst die Prüfung strukturieren und danach den passenden Output-Skill nehmen.
- Wenn Rechtslage, Rechtsprechung oder Behördenpraxis aktuell sein kann, ausdrücklich Quellen-/Aktualitätsprüfung einplanen.
- Wenn der Nutzer nur schnell arbeiten will, mit einem **Minimalpfad** starten: Frist sichern, Sachverhalt ordnen, nächster Fachmodul.
- Wenn der Nutzer Anfänger ist oder das Material chaotisch wirkt, zuerst `anfaenger-workflow-amtsgericht` vorschlagen.
- Vor jedem Versand an das Gericht `sanity-check-selbstvertretung-amtsgericht` anbieten.
- Bei Streitwert, Zuständigkeit, § 495a ZPO, Berufung oder Anwaltszwang `zulassungsgrenzen-check-amtsgericht` vorschlagen.
- Bei Zitaten, gegnerischer Rechtsprechung oder gerichtlichem Hinweis `rechtsprechungschat-amtsgericht` vorschlagen und keine Fundstellen erfinden.

### 4. Antwortformat für den Einstieg

Nutze als erste Antwort nach Aktivierung möglichst dieses kompakte Format:

**Kurzbild**
- Ziel: konkreter nächster Output.
- Rolle: Kläger, Beklagter, vor Klage, nach Urteil oder unklar.
- Erfahrungslevel: Anfänger, normal geführt, Kurzmodus oder nicht erkennbar.
- Eilt wegen: Zustellung, gerichtlicher Frist, Termin, Verjährung, Urteil, Vollstreckung oder keine Eile erkennbar.
- Fehlende Unterlagen: konkret benennen.

**Vorgeschlagener Workflow**
1. Frist und Gericht sichern.
2. Rolle, Streitwert und Ziel ordnen.
3. Passenden Plugin-Skill wählen und vor Versand einen Sanity-Check durchführen.

**Passende Skills aus diesem Plugin**
| Skill | Warum jetzt? | Erwarteter Output |
|---|---|---|
| `anfaenger-workflow-amtsgericht` | wenn der Nutzer geführt werden möchte | kleiner Schrittplan in einfacher Sprache |
| `sanity-check-selbstvertretung-amtsgericht` | vor Abgabe oder Termin | Ampelprüfung mit Reparaturliste |
| `zulassungsgrenzen-check-amtsgericht` | bei Zuständigkeit, Streitwert, Berufung oder Anwaltszwang | Grenz- und Rechtsmittelcheck |
| `rechtsprechungschat-amtsgericht` | bei Rechtsprechungsargumenten | verifizierbare Fundstellenlogik und Schriftsatzbaustein |

**Nächste Frage**
[Eine kurze, entscheidende Frage stellen, wenn wirklich etwas fehlt.]

### 5. Fachmodule in diesem Plugin

Spiele nicht den ganzen Katalog aus. Wähle erst einen klaren Pfad, erkläre kurz warum, und nenne dann höchstens drei bis fünf Skills, die wirklich als nächstes helfen.

**Routenkarte**

| Lage | Primärpfad | Ergänzende Skills |
|---|---|---|
| Nutzer ist Anfänger oder unsicher | `anfaenger-workflow-amtsgericht` | `orientierung-selbstvertreter-amtsgericht`, danach `sanity-check-selbstvertretung-amtsgericht` |
| Zuständigkeit, Streitwert oder Anwaltszwang unklar | `zulassungsgrenzen-check-amtsgericht` | `sachliche-zuständigkeit-amtsgericht-23-gvg`, `anwaltszwang-pruefen-78-zpo`, `wann-doch-anwalt-grenzfaelle` |
| Klage soll vorbereitet werden | `vorabklaerung-erfolgsaussichten-selbstcheck` | `anspruchsgrundlage-finden-laienhilfe`, `klage-zusammenstellen-komplettes-bundle-amtsgericht`, `klageschrift-antrag-bestimmt-formulieren` |
| Klage ist zugestellt worden | `klageerwiderung-checkliste-alle-punkte` | `einreden-aktiv-geltend-machen`, `substantiiertes-bestreiten-138-iv-zpo`, `klageerwiderung-fristen-274-zpo` |
| Beweise sind das Problem | `beweismittel-vorab-sammeln-checkliste` | `beweislast-grundregel-wer-was`, `zeugenbeweis-373-ff-zpo`, `urkundenbeweis-415-ff-zpo` |
| Gerichtstermin steht an | `terminvorbereitung-checkliste` | `verhalten-gerichtssaal-laienleitfaden`, `muendliche-verhandlung-akten-griffbereit`, `vergleich-richtervorschlag-278-ii-zpo` |
| Urteil oder Rechtsmittel liegt vor | `urteil-pruefen-313-zpo` | `berufung-amtsgericht-511-zpo`, `zulassungsgrenzen-check-amtsgericht`, `rechtsmittelfrist-517-zpo` |
| Fundstellen oder Gerichtshinweise irritieren | `rechtsprechungschat-amtsgericht` | nur verifizierte Entscheidungen verwenden, keine Aktenzeichen erfinden |

**Minimalpfad für schnelle Hilfe**

1. Frist und Zustellung sichern.
2. Rolle, Gericht, Streitwert und Ziel feststellen.
3. Einen Primärskill starten.
4. Vor Abgabe immer `sanity-check-selbstvertretung-amtsgericht` anbieten.

| Skill | Wann vorschlagen? |
|---|---|
| `anfaenger-workflow-amtsgericht` | Geführter Anfänger-für Bürgerinnen und Bürger vor dem Amtsgericht: fragt Rolle, Fristen, Streitwert, Gericht, Verfahrensstand und Unterlagen ab; erklärt jeden Schritt in einfacher Sprache und routet zu Klage, Verteidigung, Beweis, PKH, Termin, Urteil und Rechtsmittel. |
| `anlagen-formatieren-k1-k2-pdf-amtsgericht` | Anlagen K1 K2 K3 richtig formatieren für Klage Klageerwiderung Replik. Schriftart Times New Roman oder Arial 12pt. Position der Anlagen-Beschriftung oben rechts. Seitenzahlen. Stempel-Vorlage. PDF-Tipps für Buerger… |
| `anspruchsgrundlage-finden-laienhilfe` | Hilfe für Laien beim Identifizieren der richtigen Anspruchsgrundlage. Reihenfolge Vertrag c.i.c. GoA dinglich Delikt Bereicherung mit Beispielen aus dem Alltag. Erste Norm finden bevor Sie klagen. Mit häufigsten… |
| `anwaltszwang-pruefen-78-zpo` | Prüfung des Anwaltszwangs nach § 78 ZPO. Vor dem Amtsgericht im Zivilprozess besteht grundsaetzlich kein Anwaltszwang. Klaert Ausnahmen Familiensachen ZPO-Spezialverfahren und die Folge für Buerger die sich selbst… |
| `augenscheinsbeweis-371-zpo` | Augenscheinsbeweis nach § 371 ZPO. Inaugenscheinnahme von Sachen am Ort oder im Gericht Fotos Videos als Augenscheins-Objekte. Wann Augenschein sinnvoll ist Bezeichnung im Beweisantrag und Sicherung von veraenderlichen… |
| `ausnahmen-streitwertgrenze-23-nr-2-gvg` | Sonderzuständigkeiten des Amtsgerichts unabhängig vom Streitwert. Wohnraummietsachen Reisevertrag Wildschaeden Unterhaltsstreitigkeiten Familiensachen Betreuungs- und Nachlasssachen nach § 23 Nr. 2 GVG § 23a § 23b und… |
| `aussergerichtliche-mahnung-286-bgb` | Außergerichtliche Mahnung als Voraussetzung für Verzug nach § 286 BGB. Mit Mustertext-Anregungen Verzugszinsen Mahngebühren und Folgen für Schadensersatz. Klaert wann Mahnung entbehrlich ist und wie Sie eine wirksame… |
| `beratungshilfe-aussergerichtlich-brh` | Beratungshilfe vor Klageerhebung. Beratungshilfegesetz BerHG ermöglicht bedürftigen Buergern kostenlose oder verguenstigte Anwaltsberatung vor Gericht. Antrag beim Amtsgericht Berechtigungsschein Eigenanteil. Sinnvoll… |
| `berufung-amtsgericht-511-zpo` | Berufung gegen Amtsgerichts-Urteil zum Landgericht nach § 511 ZPO. Wertgrenze 1.000 EUR seit 2026 (frueher 600 EUR). Berufungs-Frist 1 Monat Berufungsbegründungs-Frist 2 Monate Anwaltszwang vor LG. Hinweis ohne Anwalt… |
| `berufungs-zulassung-niedrig-streitwert` | Zulassung der Berufung bei niedriger Beschwer § 511 IV ZPO. Wertgrenze seit 2026 1.000 EUR. Grundsaetzliche Bedeutung Fortbildung des Rechts Sicherung einheitlicher Rechtsprechung. Zulassung erfolgt ausschließlich… |
| `beweislast-grundregel-wer-was` | Grundregel der Beweislast im Zivilprozess. Wer eine Norm zu seinen Gunsten geltend macht muss ihre Voraussetzungen beweisen. Beweislast-Umkehr in Sondernormen Anscheinsbeweis Indizien-Beweis und sekundaere… |
| `beweismittel-vorab-sammeln-checkliste` | Checkliste für die Sammlung von Beweismitteln vor Klage. Vertrag E-Mail Rechnung Zahlung Lieferschein Foto Zeugen Chronologie. Wie Sie systematisch das Beweismaterial ordnen bevor Sie zur Klage greifen und was bei… |
| `dokumenten-erzeugung-pdf-laien-amtsgericht` | PDF-Erstellung für Klage Klageerwiderung Replik Anlagen am Amtsgericht. Word LibreOffice direkter PDF-Export. Scanner-App Handy. OCR für durchsuchbaren Text. Dateinamen-Konvention. Komprimieren bei MJP-Obergrenze 60… |
| `dolmetscher-185-gvg` | Dolmetscher im Zivilprozess nach § 185 GVG. Wann hat man Anspruch auf Dolmetscher Verfahrenssprache deutsch Kosten Eil-Antrag bei Sprachbarriere. Praktischer Leitfaden für Selbstvertreter mit nicht-Deutsch als… |
| `duplik-nach-replik` | Duplik als Beklagten-Antwort auf die Klaeger-Replik. Letzter Schriftsatz vor Termin neue Tatsachen Beweisangebote substantiiertes Bestreiten Reaktion auf Klaeger-Replik. Wann ist Duplik noetig wann nicht. |
| `eidesstattliche-versicherung-294-zpo` | Eidesstattliche Versicherung nach § 294 ZPO als Glaubhaftmachung. Nicht Strengbeweis nur für Glaubhaftmachung bei PKH-Antrag Wiedereinsetzung einstweiligem Rechtsschutz. Strafbarkeit der falschen eidesstattlichen… |
| `einreden-aktiv-geltend-machen` | Einreden aktiv geltend machen Verjährung Aufrechnung Zurückbehaltung Stundung im Klageerwiderungs-Schriftsatz. Mustertexte und Anwendung. Gericht prüft nicht von Amts wegen außer bei rechtsvernichtenden oder… |
| `einreichung-130a-zpo-elektronisch-buerger` | Elektronische Einreichung nach § 130a ZPO für Buerger. Sichere Übermittlungswege qualifizierte elektronische Signatur Bedeutung der Eingangsbestätigung. Abgrenzung zu Email und einfachem Scan. Wann ist elektronische… |
| `einreichung-fax-und-grenzen` | Einreichung per Fax und ihre verbleibenden Grenzen. Fax als Schriftform-Ersatz bei kurzfristiger Fristwahrung. Was Sie aufbewahren muessen Sendebericht Bestätigung und Risiken durch Verlust oder unleserliche Übertragung. |
| `einreichung-mein-justizpostfach-mjp-2024` | Einrichtung und Nutzung von Mein Justizpostfach (MJP) für Buerger seit 2024. Sichere elektronische Einreichung von Klagen und Schriftsaetzen an Gerichte. BundID-Login Postfach-Funktion Versandbestätigung und Zustellung. |
| `einreichung-papierform-mit-abschriften` | Einreichung der Klage in Papierform. Anzahl der Abschriften Versand per Post Einschreiben oder persönliche Abgabe an der Geschäftsstelle. Eingangsstempel Sendebeleg Beweis für rechtzeitige Einreichung. Vorteile und… |
| `einreichung-rechtsantragsstelle-selbst` | Hilfe über die Rechtsantragsstelle des Amtsgerichts. Buerger koennen muendlich Klage zu Protokoll geben formelle Hilfe bei Klageschrift Antrag und Vollstreckung. Was die Rechtsantragsstelle leistet und was Sie selbst… |
| `fristbeginn-zustellung-protokollieren` | Fristbeginn ab Zustellung. Wie Zustellung erfolgt gelber Umschlag Postzustellungsurkunde Empfangsbekenntnis Ersatzzustellung. Warum das genaue Datum so wichtig ist und wie Sie es dokumentieren. |
| `fristen-berechnen-187-188-bgb` | Berechnung von Prozessfristen nach §§ 187 188 BGB. Beginn am Tag nach Ereignis Ende am gleichen Wochentag der Folgewoche Frist-Ende auf Wochenende oder Feiertag verschiebt sich. Praxis-Beispiele und typische Fallen. |
| `fristen-buch-fuehren-laien` | Eigenes Fristen-System für Selbstvertreter aufbauen. Tabelle Reminder Vorfristen Doppelprüfung Aufbewahrung der Zustellungs-Belege Backup-Strategien. Wie Anwalts-Kanzleien Fristen verwalten und was Sie selbst nutzen… |
| `fristverlaengerung-antrag-225-zpo` | Antrag auf Fristverlaengerung nach § 224 II und § 225 ZPO. Welche Fristen verlaengerbar sind welche nicht (Notfristen). Begründung Frist-Antrag rechtzeitig stellen Folge bei nicht-Bewilligung Substituierende Strategie. |
| `gegnerische-vollstreckung-abwehr` | Abwehr der Vollstreckung wenn Sie verloren haben. Vollstreckungs-Gegenklage Pfaendungs-Freigrenzen Stundungs-Antrag Ratenzahlung Vollstreckungs-Schutzantrag. Was Sie tun koennen wenn der Gerichtsvollzieher vor der Tuer… |
| `gerichtskostenvorschuss-12-gkg` | Gerichtskostenvorschuss nach § 12 GKG. Klage wird erst zugestellt wenn Vorschuss eingegangen ist. Berechnung Zahlung Bedeutung für § 167 ZPO und Verjährungs-Hemmung. Was tun bei finanziellen Schwierigkeiten PKH-Antrag. |
| `kein-beweis-folgen-laienwarnung` | Warnung an Laien was passiert wenn ein Tatbestandsmerkmal nicht bewiesen werden kann. Beweislastniederlage Auswirkung auf das Urteil Gesamtkosten Strategien zur Reduktion des Beweis-Risikos vor Klage. |
| `klage-streitwert-angabe-3-zpo` | Berechnung und Angabe des Streitwerts in der Klage nach § 3 ZPO § 5 ZPO § 48 GKG. Geldforderung Herausgabe Feststellung Mietsache Sondervorschriften. Mit Beispielen und Hinweisen wann das Gericht den Streitwert… |
| `klage-vereinfachtes-verfahren-495a-zpo` | Vereinfachtes Verfahren nach § 495a ZPO bei Streitwert bis 1.000 EUR (Anhebung von 600 EUR zum 01.01.2026). Gericht entscheidet nach billigem Ermessen schriftliches Verfahren ohne muendliche Verhandlung möglich.… |
| `klage-zusammenstellen-komplettes-bundle-amtsgericht` | Klage und Anlagen als komplettes Paket für das Amtsgericht. Reihenfolge Klageschrift Anlagenverzeichnis Anlagen K1 K2 K3. Heftung Bindung Abschriften. Was muss zum Gericht was bleibt bei Ihnen. Anwendbar auch für… |
| `klageerwiderung-checkliste-alle-punkte` | Vollständige Checkliste für die Klageerwiderung. Pro Klage-Punkt eine Antwort Sachverhaltsstellung Bestreiten Einreden Beweisanbietung Antrag auf Klage-Abweisung. Strukturierte Vorgehensweise für den Beklagten ohne… |
| `klageerwiderung-fristen-274-zpo` | Fristen zur Klageerwiderung nach § 274 ZPO. Notfrist zur Verteidigungsanzeige Klageerwiderungs-Frist Folge bei Versaeumnis Versaeumnisurteil. Schriftliches Vorverfahren oder frueher erster Termin als… |
| `klageerwiderung-replik-anlagen-b1-b2-fortlaufend` | Anlagen-Nummerierung in Klageerwiderung und Replik korrekt fortführen. Beklagter nutzt B1 B2 B3. Klaeger nutzt in Replik K-Folge-Nummern ab Klage-Endnummer plus eins. Keine doppelten Nummern Querverweise zwischen… |
| `klageschrift-anlagen-bezeichnen` | Bezeichnung Sortierung und Beifuegung von Anlagen zur Klageschrift. K1 K2 K3 für Klaeger B1 B2 B3 für Beklagter. Anlagenverzeichnis Leseführung im Sachvortrag und Vorbereitung der Abschriften für Gericht und Beklagten. |
| `klageschrift-anschreiben-an-gericht-laien` | Anschreiben Anrede und Form für Klage und sonstige Schriftsaetze an das Amtsgericht. Hoeflichkeitsform Gericht-Ansprache Aktenzeichen Briefkopf und uebliche Schlussformeln aus der Perspektive eines Selbstvertreters. |
| `klageschrift-antrag-bestimmt-formulieren` | Formulierung eines bestimmten Klageantrags nach § 253 II Nr. 2 ZPO. Zahlungs- Herausgabe- Unterlassungsanträge Stufenklage Feststellungs-Antrag mit Mustertext. Klagentyp prüfen Antrag vollstreckungsfähig formulieren… |
| `klageschrift-beweisangebote-einbauen-373-zpo` | Einbau von Beweisangeboten in die Klageschrift. Urkundenbeweis Zeugenbeweis Sachverständigenbeweis Augenscheinsbeweis Parteivernehmung. Mit Mustern für Beweisanträge und Hinweisen zur Benennung ladungsfähiger… |
| `klageschrift-pflichtbestandteile-253-zpo` | Pflichtbestandteile einer Klageschrift nach § 253 ZPO. Bezeichnung der Parteien Gericht bestimmter Antrag Klagegrund Beweise Unterschrift. Mit Mustertext-Anregung für eine vollständige Klage in einfacher Sprache und… |
| `klageschrift-tatsachenvortrag-strukturieren` | Strukturierung des Tatsachenvortrags in der Klageschrift. Chronologische Schilderung pro Tatbestandsmerkmal Beweis-Junktur und rechtliche Würdigung in einfacher Sprache. Mit Mustertext Vermeidung von… |
| `kostenfestsetzung-103-104-zpo` | Kostenfestsetzung nach §§ 103 104 ZPO. Bei Erfolg im Verfahren Ihre Kosten gegen den Verlierer festsetzen lassen. Antrag bei Geschäftsstelle was erstattungsfähig was nicht. Mit Muster und Hinweis auf… |
| `kostenrisiko-streitwert-berechnen-gkg` | Berechnung des Kostenrisikos bei Klage vor Amtsgericht. Gerichtskosten nach GKG Anwaltskosten der Gegenseite nach RVG Sachverständigen-Kosten. Mit Beispielen für typische Streitwerte und Tabellen-Hinweisen zur… |
| `ladung-termin-216-zpo` | Termin-Ladung nach § 216 ZPO. Inhalt der Ladung Datum Uhrzeit Ort Sitzungssaal Aktenzeichen Bedeutung von Hinweisen wie Erscheinens-Pflicht Versaeumnis-Hinweis. Wie Sie eine Ladung prüfen und bestätigen. |
| `mahnverfahren-688-ff-zpo-vor-klage` | Mahnbescheid nach §§ 688 ff. ZPO als guenstige Alternative zur Klage. Online-Formular Mahngerichte Widerspruchs-Folgen Vollstreckungsbescheid. Wann ist Mahnverfahren sinnvoll wann nicht. Mit Hinweisen zur Hemmung der… |
| `muendliche-verhandlung-akten-griffbereit` | Mit Akten und Anlagen optimal in die muendliche Verhandlung vor dem Amtsgericht. Anlagen-Reiter Stichwort-Liste Mitschreib-Block Notizen zu Streit-Punkten. Vorbereitung der Argumente zur Replik im Termin. Praesenz oder… |
| `nachgereichter-schriftsatz-296a-zpo` | Nachgereichter Schriftsatz nach Schluss der muendlichen Verhandlung gemäß § 296a ZPO. Schriftsatznachlass durch Gericht Voraussetzung Grenzen Wirkung auf Urteil. Wann ein nachgereichter Vortrag noch berücksichtigt wird… |
| `oertliche-zuständigkeit-12-37-zpo` | Bestimmung des örtlich zuständigen Amtsgerichts nach §§ 12 ff. ZPO. Allgemeiner Gerichtsstand am Wohnsitz des Beklagten Besondere Gerichtsstaende Erfuellungsort unerlaubte Handlung Niederlassung. Wahlrecht und… |
| `online-verfahren-11-buch-zpo-experimentell` | Experimentelles Online-Verfahren der ZPO seit 2025 ggf 2026. Vollständig digitales Zivilverfahren bestimmte Streitwerte teilnehmende Amtsgerichte. Aktuelle Normen-Verortung prüfen. Vergleich Praesenz-Verfahren Vorteile… |
| `orientierung-selbstvertreter-amtsgericht` | Triage und Einstieg für Buerger die sich ohne Anwalt vor dem Amtsgericht vertreten wollen. Klaert Rolle (Klaeger oder Beklagter) Streitwert Zuständigkeit und verweist auf die für Ihre Situation passenden Skills. |
| `parteivernehmung-445-ff-zpo` | Parteivernehmung nach §§ 445 ff. ZPO. Subsidiaeres Beweismittel auf Antrag oder von Amts wegen. Bedingungen und Beweiswert. Wann lohnt sich Parteivernehmung warum gilt die eigene Aussage als schwach. |
| `pkh-bewilligung-ablehnung-folgen` | Folgen der PKH-Entscheidung Bewilligung mit oder ohne Raten Beiordnung Anwalt Ablehnung wegen fehlender Erfolgsaussicht Bedürftigkeit oder Mutwilligkeit. Beschwerde gegen ablehnenden PKH-Beschluss nach § 127 ZPO und… |
| `pkh-ratenzahlung-bewilligung` | Ratenzahlung bei PKH-Bewilligung nach § 120 ZPO. Berechnung der monatlichen Rate nach einsetzbarem Einkommen Tabelle § 115 II ZPO. Maximale Laufzeit 48 Monate Aenderung Anpassung und vorzeitige Tilgung. Wirkung auf… |
| `prozesskostenhilfe-pkh-114-zpo` | Antrag auf Prozesskostenhilfe nach § 114 ZPO. Voraussetzungen Bedürftigkeit Erfolgsaussicht keine Mutwilligkeit. Antragsformular Belege Einkommensnachweise. Wirkung Befreiung von Gerichtskosten und Anwaltskosten.… |
| `rechtsmittelfrist-517-zpo` | Rechtsmittelfrist 1 Monat nach § 517 ZPO. Beginn mit Zustellung des vollständigen Urteils Notfrist keine Verlaengerung. Berechnung mit § 187 188 BGB Praeklusion bei Versaeumnis Wiedereinsetzung in Ausnahmefaellen. |
| `replik-auf-klageerwiderung-systematik` | Replik als Klaeger-Antwort auf die Klageerwiderung. Pro Beklagten-Punkt Stellungnahme neuer Sachvortrag Beweisangebote substantiiertes Bestreiten der Beklagten-Behauptungen. Wann ist Replik notwendig wann reicht… |
| `richterlicher-hinweis-139-zpo-reaktion` | Reaktion auf einen richterlichen Hinweis nach § 139 ZPO. Hinweispflicht des Gerichts Bedeutung des Hinweises welche Reaktion zu erwarten ist. Wie Sie auf Hinweise konstruktiv reagieren ohne Verfahrensvorteile zu… |
| `rechtsprechungschat-amtsgericht` | Geführter Rechtsprechungschat für Selbstvertreter vor dem Amtsgericht: findet, erklärt und bewertet Rechtsprechung, überträgt sie auf den eigenen Sachverhalt und verhindert erfundene oder unpassende Fundstellen. |
| `sachliche-zuständigkeit-amtsgericht-23-gvg` | Prüfung der sachlichen Zuständigkeit des Amtsgerichts nach § 23 GVG. Wertgrenze seit 01.01.2026 zehntausend EUR (§ 23 Nr. 1 GVG aktuelle Fassung). Sonderzuständigkeiten § 23 Nr. 2 GVG Mietsachen Reisevertrag. Stand der… |
| `sachverstaendigenbeweis-402-zpo` | Sachverständigenbeweis nach §§ 402 ff. ZPO. Antrag Kostenvorschuss Auswahl des Sachverständigen Privatgutachten als Urkunde Gerichtsgutachten Prüfung der Glaubwürdigkeit. Wann ist Sachverständigen-Beweis sinnvoll und… |
| `sanity-check-selbstvertretung-amtsgericht` | Letzter Sanity-Check vor Klage, Klageerwiderung, Replik, Termin, Vergleich oder Rechtsmittel: prüft Fristen, Zuständigkeit, Anwaltszwang, Antrag, Beweise, Anlagen, Kosten, Versand und rote Flaggen. |
| `saeumnis-im-termin-330-zpo` | Saeumnis im Termin und Versaeumnisurteil nach §§ 330 331 ZPO. Wenn Sie nicht erscheinen oder nicht verhandeln Folgen Versaeumnisurteil Einspruch und Wiedereinsetzung bei unverschuldetem Versaeumnis. |
| `saeumnis-vermeiden-330-ff-zpo` | Versaeumnisurteil verhindern §§ 330 ff. ZPO. Folgen des Schweigens als Beklagter Verteidigungsanzeige Klageerwiderung Termin-Erscheinung Einspruch gegen Versaeumnisurteil mit 2-Wochen-Frist § 339 ZPO. |
| `substantiiertes-bestreiten-138-iv-zpo` | Substantiiertes Bestreiten nach § 138 II und § 138 IV ZPO. Wann reicht einfaches Bestreiten wann ist sekundaere Darlegungslast erforderlich. Mit Nichtwissen bestreiten bei Tatsachen außer eigener Wahrnehmung.… |
| `tatbestand-zerlegen-anspruchspruefung-laien` | Den Tatbestand einer Anspruchsnorm in einzelne Merkmale zerlegen. Sie muessen jedes Merkmal vortragen und beweisen koennen. Mit Beispielen § 433 BGB § 823 BGB § 280 BGB und einer Methode wie Laien die… |
| `terminvorbereitung-checkliste` | Checkliste für die Vorbereitung der muendlichen Verhandlung. Akten Ordner Schluesselargumente Beweisstuecke Zeugen Anträge Anträge auf Bewilligung erweiterte Anträge Klage-Konzept. Was Sie mitnehmen muessen und wie Sie… |
| `typische-laien-fehler` | Die häufigsten Fehler von Buergern in der Selbstvertretung vor dem Amtsgericht. Versaeumte Fristen pauschaler Vortrag fehlende Beweisangebote Antrag unbestimmt Notfristen unterschaetzt. Mit konkreten Gegenmassnahmen. |
| `urkundenbeweis-415-ff-zpo` | Urkundenbeweis nach §§ 415 ff. ZPO. Öffentliche und Private Urkunden Beweiswert echt unecht Vertraege Rechnungen E-Mails Chats. Wie Sie Urkunden vorlegen Authentizitaet sichern und Original-Vorlage bei Bestreiten. |
| `urteil-pruefen-313-zpo` | Prüfung des schriftlichen Urteils nach § 313 ZPO. Tenor Tatbestand Entscheidungsgründe auf Vollständigkeit Korrektheit prüfen. Tatbestandsberichtigung § 320 ZPO Urteils-Ergaenzung § 321 ZPO bei vergessenen Ansprüchen.… |
| `urteil-rechtskraft-705-zpo` | Rechtskraft des Urteils nach § 705 ZPO. Wann ist ein Urteil rechtskraeftig formelle und materielle Rechtskraft. Wirkung der Rechtskraft für Vollstreckung und gegen erneute Klage Bedeutung für Sie als Selbstvertreter. |
| `urteilsverkuendung-310-zpo` | Urteilsverkündung nach § 310 ZPO. Ende der muendlichen Verhandlung Verkündungs-Termin Zustellung schriftliches Urteil Tenor Form und Inhalt. Was Sie als Partei beim Termin und nach Verkündung erleben. |
| `verbrauchergerichtsstand-29c-zpo` | Verbrauchergerichtsstand § 29c ZPO. Bei Haustuergeschäften und Außergeschäftsraum-Vertraegen kann der Verbraucher am eigenen Wohnsitz klagen oder verklagt werden. Voraussetzungen und Beispiele aus dem Versandhandel… |
| `vergleich-richtervorschlag-278-ii-zpo` | Vergleich vor dem Amtsgericht nach § 278 II ZPO Richtervorschlag Erledigungsklausel Auswirkung auf Kosten und Streitwert. Wann ist ein Vergleich vorteilhaft wann nicht und wie wird er protokolliert. |
| `verhalten-gerichtssaal-laienleitfaden` | Verhalten im Gerichtssaal für Laien. Aufstehen Anrede Hoher Herr Vorsitzender Reihenfolge der Worterteilung Anrede Gegenseite Dokumenten-Vorlage Pausen Mobiltelefone. Praktischer Leitfaden vor und im Termin. |
| `verjaehrungsfrist-pruefen-195-bgb` | Prüfung von Verjährungsfristen vor Klage. Regelfrist drei Jahre nach § 195 BGB Beginn Jahresende § 199 BGB Hemmung Neubeginn Sonderfristen. Mit Beispielen aus Kauf Werkvertrag Schadensersatz und unverjährbaren… |
| `video-verhandlung-128a-zpo` | Video-Verhandlung nach § 128a ZPO. Teilnahme an muendlicher Verhandlung per Bild und Ton-Übertragung. Antrag technische Voraussetzungen Einverstaendnis-Pflichten. Praktischer Leitfaden für Selbstvertreter. |
| `vollstreckungsklausel-724-zpo` | Vollstreckungsklausel nach § 724 ZPO. Antrag bei der Geschäftsstelle Voraussetzungen vollstreckbarer Titel Klausel-Erteilung qualifizierte Klausel. Wie Sie als Gläubiger die Klausel beantragen und was Sie damit dann tun. |
| `vorabklaerung-erfolgsaussichten-selbstcheck` | Selbstcheck der Erfolgsaussichten einer Klage vor dem Amtsgericht. Klaert Anspruchsgrundlage Beweislage Verjährung Kostenrisiko Gegenseite und Alternative zur Klage. Vermeidet teure Klage ohne Substanz und nimmt… |
| `wann-doch-anwalt-grenzfaelle` | Grenzfaelle in denen Selbstvertretung nicht mehr sinnvoll ist und ein Anwalt eingeschaltet werden sollte. Hoher Streitwert komplexer Sachverhalt Berufung Familiensache Spezialmaterie. Kostenvergleich Selbstvertretung… |
| `widerklage-33-zpo` | Widerklage nach § 33 ZPO als Gegenangriff des Beklagten. Voraussetzungen Konnexitaet Streitgegenstand-Verbindung Zuständigkeit Kostenrisiko Vorteile gegenüber reiner Aufrechnung. Wann lohnt die Widerklage und welcher… |
| `wiedereinsetzung-frist-233-zpo` | Wiedereinsetzung in den vorigen Stand nach § 233 ZPO. Voraussetzungen unverschuldetes Versaeumnis 2-Wochen-Antragsfrist Glaubhaftmachung Nachholung der versaeumten Handlung. Mustertext typische Faelle Krankheit Unfall… |
| `zeugenbeweis-373-ff-zpo` | Zeugenbeweis nach §§ 373 ff. ZPO. Ladungsfähige Anschrift Beweisthema Zeugnis-Verweigerungsrechte Vereidigung. Wie Sie Zeugen benennen und im Verfahren einbringen. Was bei nahen Angehoerigen und Aussage-Wert zu… |
| `zulassungsgrenzen-check-amtsgericht` | Zulässigkeits-, Zuständigkeits- und Rechtsmittelgrenzen: § 23 GVG 10.000 EUR, § 495a ZPO 1.000 EUR, § 511 ZPO 1.000 EUR, Übergangsfälle, Anwaltszwang und rote Flaggen. |
| `zurechnungsproblem-versand-durch-dritte` | Risiko des Versands von Schriftsaetzen durch Dritte. BVerfG-Selbstverantwortungs-Linie und BGH zur Wiedereinsetzung. Wer den Versand einem Dritten ueberlaesst traegt das Risiko der rechtzeitigen Einreichung. Praktische… |
| `zwangsvollstreckung-querverweis-substitutionsagent` | Querverweis zum Substitutionsagenten für die Zwangsvollstreckung nach Urteil. Dieses Plugin behandelt die Vollstreckung nicht inhaltlich. Hinweis welche Schritte als naechstes anstehen und welche Tools dabei helfen… |

## Qualitätsversprechen

- Arbeite schnell, aber nicht hektisch.
- Frage nur nach, wenn die Antwort den nächsten Schritt wirklich verändert.
- Mache Annahmen sichtbar und halte sie knapp.
- Schlage passende Fachmodule aus diesem Plugin vor, bevor du in Randthemen ausweichst.
- Liefere am Ende immer einen klaren nächsten Schritt.

---

Hinweis: Dieser Skill stärkt die Selbstvertretung, indem er Workflow, Fristen, Zuständigkeit, Beweis und Routing strukturiert; die fachliche Endverantwortung bleibt beim Menschen, und rote Grenzfälle gehören zur Rechtsantragsstelle, Beratungshilfe oder anwaltlichen Prüfung.

---

## Skill: `orientierung-selbstvertreter-amtsgericht`

_Triage und Einstieg für Bürger, die sich ohne Anwalt vor dem Amtsgericht vertreten wollen. Klärt Erfahrungslevel, Rolle, Fristen, Streitwert, Zuständigkeit, Anwaltszwang und verweist auf Anfänger-Workflow, Sanity-Check, Rechtsprechungschat, Klage, Verteidigung, Termin und Rechtsmittelgrenzen._

# Orientierung: Sie wollen sich selbst vor dem Amtsgericht vertreten

## Worum geht es?

Vor dem Amtsgericht (AG) brauchen Sie als Buerger keinen Rechtsanwalt. Sie koennen also selbst klagen, sich selbst verteidigen, selbst Schriftsaetze einreichen und selbst im Termin auftreten. Das spart Anwaltskosten — kann aber teuer werden, wenn Sie Fristen verpassen oder Antraege falsch formulieren. Diese Skill ordnet Ihre Situation ein und sagt Ihnen, wohin Sie als Naechstes lesen sollten.

## Wann brauchen Sie diese Skill?

- Sie wissen noch nicht, ob Sie klagen oder sich verteidigen.
- Sie wollen verstehen, was vor dem Amtsgericht ueberhaupt passiert.
- Sie wollen wissen, ob ein Anwalt zwingend ist.
- Sie suchen eine Reihenfolge, in der Sie die Skills lesen.
- Sie wollen einen Anfänger-Modus oder einen Sanity-Check vor dem Absenden.

## Fachbegriffe (kurz erklaert)

- **Amtsgericht (AG)**: Das kleinste Gericht der ordentlichen Gerichtsbarkeit. Es entscheidet ueber zivile Streitigkeiten bis zu einer bestimmten Wertgrenze und ueber bestimmte Materien (Miete, Familie, kleine Geldforderungen).
- **Streitwert**: Der Geldwert dessen, worum Sie streiten. Bei einer Forderung von 2.000 EUR ist der Streitwert 2.000 EUR.
- **Klaeger**: Wer eine Klage erhebt.
- **Beklagter**: Wer verklagt wird.
- **Anwaltszwang**: Vorschrift, dass Sie sich nur durch einen Anwalt vertreten lassen koennen. Vor dem AG gibt es ihn **nicht** (mit wenigen Ausnahmen, siehe Skill `anwaltszwang-pruefen-78-zpo`).

## Rechtsgrundlagen

- **§ 78 ZPO** — Anwaltszwang vor Landgericht und hoeher; e contrario kein Anwaltszwang vor AG.
- **§ 23 GVG** — Sachliche Zuständigkeit des AG.
- **§ 23a, 23b, 23c GVG** — Familiensachen, Betreuungssachen, Nachlasssachen.
- **§§ 12 ff. ZPO** — Oertliche Zuständigkeit.
- **§ 495a ZPO** — Vereinfachtes Verfahren bis 1.000 EUR Streitwert (Stand 2026, vorher 600 EUR).

## Schritt-für-Schritt-Anleitung

### Schritt 1 — Klaeren Sie Ihre Rolle

Sind Sie

- **Klaeger** (Sie wollen jemand verklagen)? → Block B-E, dann F-L bei Fortschritt.
- **Beklagter** (Sie wurden verklagt)? → Block F, dann G, H, I, J, K.

Wenn Sie Anfänger sind, starten Sie zuerst mit `anfaenger-workflow-amtsgericht`. Dieser Skill erklärt die Reihenfolge in kleineren Schritten.

### Schritt 2 — Streitwert bestimmen

Schaetzen Sie, um welche Geldsumme es geht. Das ist Ihr Streitwert. Bei Sachen ohne Geldforderung (z. B. "Sie sollen die Garage raeumen") schaetzt das Gericht. Skill `klage-streitwert-angabe-3-zpo` hilft.

### Schritt 3 — Zuständigkeit pruefen

- Streitwert unterhalb der Wertgrenze § 23 Nr. 1 GVG? AG zuständig. Skill `sachliche-zuständigkeit-amtsgericht-23-gvg`.
- Mietsache, Reisevertrag, Familiensache? Immer AG, unabhaengig vom Wert. Skill `ausnahmen-streitwertgrenze-23-nr-2-gvg`.
- Welches AG raeumlich? Wohnort Beklagter ist der Hauptfall. Skill `oertliche-zuständigkeit-12-37-zpo`.

### Schritt 4 — Erfolgsaussichten ehrlich pruefen

Klagen kostet Geld, auch wenn Sie keinen Anwalt brauchen — Gerichtskosten, evtl. Sachverstaendiger, im Verlust-Fall die Kosten der Gegenseite. Skill `vorabklaerung-erfolgsaussichten-selbstcheck`.

### Schritt 5 — Verjährung pruefen (Klaeger!)

Forderungen verjaehren in der Regel in **drei Jahren** zum Jahresende. Ist Ihr Anspruch noch durchsetzbar? Skill `verjaehrungsfrist-pruefen-195-bgb`.

### Schritt 6 — Naechsten Skill auswaehlen

- Sie sind Anfänger? → `anfaenger-workflow-amtsgericht`.
- Sie wollen vor Versand prüfen? → `sanity-check-selbstvertretung-amtsgericht`.
- Sie sind unsicher wegen Wertgrenze, Berufung oder Anwaltszwang? → `zulassungsgrenzen-check-amtsgericht`.
- Sie brauchen Rechtsprechung zu einem Argument? → `rechtsprechungschat-amtsgericht`.
- Sie wollen Klage erstellen? → `klageschrift-pflichtbestandteile-253-zpo`.
- Sie haben eine Klage bekommen? → `klageerwiderung-fristen-274-zpo`.
- Sie haben einen Termin? → `terminvorbereitung-checkliste`.
- Sie haben ein Urteil und wollen sich wehren? → `berufung-amtsgericht-511-zpo`.

## Worauf Sie besonders achten muessen

- **Fristen ueberleben Versaeumnisse selten.** Wenn das Gericht eine Frist setzt, ist sie ernst. Eine versaeumte Frist kostet Sie meist den Prozess. Skill `fristen-berechnen-187-188-bgb`.
- **Versand durch Dritte ist Ihr Risiko.** Wenn Sie eine Klage durch einen Boten oder Verwandten zum Gericht schicken und die Sendung verspaetet ankommt, traegt das Risiko nach BVerfG-Linie **Sie**. Skill `zurechnungsproblem-versand-durch-dritte`.
- **Bestimmter Antrag.** Eine Klage ohne klaren Antrag ist unzulaessig. Skill `klageschrift-antrag-bestimmt-formulieren`.
- **Mein Justizpostfach (MJP) seit 2024** ermoeglicht Buergern den elektronischen Versand an Gerichte. Skill `einreichung-mein-justizpostfach-mjp-2024`.

## Typische Fehler

- "Ich schreibe nur, dass ich gewinnen will." → Sie brauchen einen **konkreten** Antrag (z. B. "Der Beklagte wird verurteilt, an mich 1.500 EUR nebst Zinsen zu zahlen.").
- "Beweise reiche ich spaeter ein." → Beweismittel muessen Sie **benennen** (mindestens). Skill `klageschrift-beweisangebote-einbauen-373-zpo`.
- "Ich warte ab, was die Gegenseite schreibt." → Beim Beklagten oft toedlich: Wer in der Frist nicht reagiert, kassiert ein Versaeumnisurteil. Skill `saeumnis-vermeiden-330-ff-zpo`.
- "Ich verklage erstmal, einigen kann ich mich spaeter." → Vorgerichtliche Mahnung und Verzug sind Voraussetzung für manche Anspruchspositionen (z. B. Verzugszinsen). Skill `aussergerichtliche-mahnung-286-bgb`.

## Quellen und Aktualitaet

Stand: 05/2026. § 23 Nr. 1 GVG: Wertgrenze 10.000 EUR seit 01.01.2026 (Anhebung von 5.000 EUR durch das Justizstandort-Staerkungsgesetz). § 495a ZPO: Wertgrenze 1.000 EUR (Anhebung von 600 EUR). § 511 II Nr. 1 ZPO: Berufungs-Beschwer 1.000 EUR (Anhebung von 600 EUR). MJP (Mein Justizpostfach) ist seit 2024 im Buerger-Betrieb.

---

## Skill: `klage-vereinfachtes-verfahren-495a-zpo`

_Vereinfachtes Verfahren nach § 495a ZPO bei Streitwert bis 1.000 EUR (Anhebung von 600 EUR zum 01.01.2026). Gericht entscheidet nach billigem Ermessen schriftliches Verfahren ohne muendliche Verhandlung möglich. Voraussetzungen Vorteile Risiken und wann sich ein Antrag auf muendliche Verhandlung..._

# Vereinfachtes Verfahren bis 1.000 EUR (§ 495a ZPO)

## Worum geht es?

Bei Streitwerten **bis 1.000 EUR** (Stand 2026) kann das Amtsgericht das Verfahren nach **billigem Ermessen** gestalten — sprich: vereinfachte Form, oft schriftlich ohne muendliche Verhandlung, geringere Foermlichkeit. Das spart Zeit und Geld. Aber: Sie verlieren ein Stueck Verfahrensgarantie. Diese Skill zeigt, wann es sinnvoll ist und wann Sie muendliche Verhandlung beantragen sollten.

**Reform-Hinweis:** Die Wertgrenze des § 495a ZPO wurde zum 01.01.2026 von 600 EUR auf 1.000 EUR angehoben. Damit fallen mehr kleinere Streitigkeiten unter das vereinfachte Verfahren.

## Wann brauchen Sie diese Skill?

- Ihr Streitwert ist niedrig (bis 1.000 EUR).
- Sie wollen wissen, wie das vereinfachte Verfahren laeuft.
- Sie wollen pruefen, ob Sie muendliche Verhandlung beantragen sollten.

## Fachbegriffe (kurz erklaert)

- **Vereinfachtes Verfahren**: Verfahrensart mit reduzierten Foermlichkeiten.
- **Billiges Ermessen**: Gericht entscheidet ueber Verfahrensgestaltung nach eigener Einschaetzung.
- **Schriftliches Verfahren**: Keine muendliche Verhandlung, Entscheidung nach Aktenlage.
- **Antrag auf muendliche Verhandlung**: Recht der Partei, eine muendliche Verhandlung zu erzwingen (§ 495a S. 2 ZPO).

## Rechtsgrundlagen

- **§ 495a ZPO (Fassung seit 01.01.2026)** — Verfahren bei Streitwerten bis **1.000 EUR**; Gericht bestimmt nach billigem Ermessen. Anhebung von 600 EUR auf 1.000 EUR durch das Justizstandort-Staerkungsgesetz.
- **§ 495a S. 2 ZPO** — Antrag auf muendliche Verhandlung muss zugelassen werden.
- **§ 4 ZPO** — Streitwert (Hauptforderung ohne Nebenforderungen).

## Schritt-für-Schritt-Anleitung

### Schritt 1 — Pruefen, ob Streitwert bis 1.000 EUR

Bezogen auf Hauptforderung ohne Nebenforderungen (§ 4 ZPO). Zinsen, Mahnkosten zaehlen nicht mit.

**Beispiele:**

- Sie klagen 800 EUR Hauptforderung + 50 EUR Zinsen → Streitwert 800 EUR → § 495a ZPO anwendbar.
- Sie klagen 1.000 EUR Hauptforderung → Streitwert 1.000 EUR → noch im Anwendungsbereich (Grenze ist eingeschlossen).
- Sie klagen 1.200 EUR → § 495a ZPO **nicht** anwendbar; normales Verfahren.

### Schritt 2 — Was bedeutet "billiges Ermessen"?

Das Gericht kann:

- Auf muendliche Verhandlung verzichten.
- Eine kurze schriftliche Stellungnahme der Gegenseite verlangen, dann entscheiden.
- Auch fristfrei verfahren.
- Beweisaufnahme nach eigenem Plan gestalten.

In der Praxis: oft entscheidet das Gericht **nach Schriftsatz-Wechsel**, ohne muendliche Verhandlung.

### Schritt 3 — Vorteile

- Schneller (kein Termin).
- Billiger (Sie sparen Reisekosten, keine Anwesenheitspflicht).
- Geringerer Aufwand.
- Bei klaren, schriftlich dokumentierten Sachverhalten meist ausreichend.

### Schritt 4 — Nachteile / Risiken

- Keine muendliche Verhandlung bedeutet: Sie koennen Ihre Sache nicht persoenlich darstellen.
- Beweisaufnahme reduziert: oft keine Zeugen-Vernehmung im vereinfachten Verfahren.
- Wenn Sie subtile Sachverhalts-Punkte haben, die im Schriftsatz schwer erklaerbar sind: muendliche Verhandlung sinnvoll.

### Schritt 5 — Antrag auf muendliche Verhandlung

Sie haben das **Recht** auf muendliche Verhandlung. Antrag genuegt (§ 495a S. 2 ZPO). Beispiel:

```
Ich beantrage die Anberaumung einer muendlichen
Verhandlung gemaess § 495a S. 2 ZPO.

Begruendung: Der Sachverhalt ist im Schriftsatz
nicht vollstaendig darstellbar, da Aussagen
von Zeugen erforderlich sind.
```

### Schritt 6 — Wann verzichten?

Verzichten Sie auf muendliche Verhandlung, wenn:

- Sachverhalt klar dokumentiert (Urkunden).
- Keine Zeugen erforderlich.
- Beklagter wird voraussichtlich nicht widersprechen oder nur formal.

Dann sparen Sie Zeit.

### Schritt 7 — Wann auf muendliche Verhandlung bestehen?

Bestehen Sie, wenn:

- Zeugen-Beweis erforderlich.
- Komplexer Sachverhalt.
- Vergleichs-Verhandlung gewuenscht (im Termin oft moeglich).
- Sie das Gericht persoenlich ueberzeugen wollen.

### Schritt 8 — Beweisaufnahme im vereinfachten Verfahren

Theoretisch moeglich, aber selten. Wenn Beweis-Notwendigkeit besteht, beantragt das Gericht meist regulaere Beweisaufnahme oder wechselt ins Normalverfahren.

## Worauf Sie besonders achten muessen

- **Wertgrenze 1.000 EUR** seit 01.01.2026 (vorher 600 EUR). Bei Altklagen, die vor dem Stichtag anhaengig wurden, ggf. Uebergangsregelung pruefen.
- **Antragsrecht auf muendliche Verhandlung** ist Garantiestueck — nutzen Sie es, wenn Sie es brauchen.
- **Vergleichschance**: Im Termin oft besser als rein schriftlich.

## Typische Fehler

- "Vereinfachtes Verfahren ist meine einzige Option." → Sie koennen muendliche Verhandlung beantragen.
- "Keine muendliche Verhandlung heisst, mein Fall wird abgewiesen." → Nein, Gericht entscheidet trotzdem in der Sache.
- "Ich brauche keine Anwesenheit." → Im vereinfachten Verfahren oft nicht erforderlich. Aber wenn Termin: pflichtschuldig erscheinen.
- "Wertgrenze ist 600 EUR." → Veraltet. Seit 01.01.2026 sind es 1.000 EUR.

## Quellen und Aktualitaet

Stand: 05/2026. § 495a ZPO aktuelle Fassung: Wertgrenze 1.000 EUR (Anhebung von 600 EUR zum 01.01.2026 durch das Justizstandort-Staerkungsgesetz).

---

## Skill: `berufungs-zulassung-niedrig-streitwert`

_Zulassung der Berufung bei niedriger Beschwer § 511 IV ZPO. Wertgrenze seit 2026 1.000 EUR. Grundsaetzliche Bedeutung Fortbildung des Rechts Sicherung einheitlicher Rechtsprechung. Zulassung erfolgt ausschließlich durch das AG im Urteil eine eigene Zulassungs-Beschwerde gibt es nicht._

# Berufungs-Zulassung bei Beschwer bis 1.000 EUR

## Worum geht es?

Wenn Ihre Beschwer **1.000 EUR oder weniger** betraegt, ist Berufung grundsaetzlich **nicht** statthaft (§ 511 II Nr. 1 ZPO, Fassung seit 01.01.2026). Eine Berufung ist in dieser Konstellation nur moeglich, wenn das **Amtsgericht selbst die Berufung in seinem Urteil ausdruecklich zugelassen hat** (§ 511 II Nr. 2 ZPO i.V.m. § 511 IV ZPO).

**Achtung Uebergangsfaelle (§ 47 EGZPO):** Fuer Verfahren, in denen die anzufechtende Entscheidung **bis einschliesslich 31.12.2025** verkuendet bzw. der Geschaeftsstelle uebergeben wurde — oder die muendliche Verhandlung bis dahin geschlossen war — gilt **weiterhin die alte Wertgrenze 600 EUR**. In solchen Faellen ist Berufung ohne Zulassung schon ab einer Beschwer von mehr als 600 EUR moeglich. Pruefen Sie zuerst, in welche Phase Ihr Verfahren faellt.

**Wichtig:** Die Zulassung erfolgt **nur durch das erstinstanzliche Gericht (AG)**. Wenn das AG nicht zugelassen hat, gibt es **keinen separaten Rechtsbehelf zum LG** — keine "Zulassungs-Beschwerde", keine "Nichtzulassungsbeschwerde" wie etwa in der Revision (§ 544 ZPO). Das AG-Urteil ist dann endgueltig.

Eine sehr enge Ausnahme bietet die **Anhörungsruege § 321a ZPO** bei Verletzung des rechtlichen Gehoers — keine Vollkontrolle, sondern Korrektur eines Verfahrensfehlers durch das AG selbst.

## Wann brauchen Sie diese Skill?

- Ihre Beschwer ist 1.000 EUR oder weniger (bzw. 600 EUR oder weniger im Uebergangsfall nach § 47 EGZPO).
- Sie meinen, Ihre Sache hat grundsaetzliche Bedeutung.
- Sie wollen wissen, ob Sie das Urteil noch angreifen koennen, wenn das AG nicht zugelassen hat.

## Fachbegriffe (kurz erklaert)

- **Beschwer**: Differenz zwischen Antrag und Urteil zu Ihren Lasten.
- **Grundsaetzliche Bedeutung**: Frage, deren Beantwortung ueber den Einzelfall hinaus klaerend wirkt.
- **Zulassung der Berufung**: Erklaerung des AG im Urteil, dass Berufung ausnahmsweise statthaft ist.
- **Anhörungsruege**: Rechtsbehelf bei Verletzung des rechtlichen Gehoers (§ 321a ZPO).

## Rechtsgrundlagen

- **§ 511 II Nr. 2 ZPO** — Berufungs-Zulassung als Voraussetzung der Berufung bei geringer Beschwer.
- **§ 511 IV ZPO** — Voraussetzungen der Zulassung. Zulassung erfolgt **durch das Gericht erster Instanz** (= AG).
- **§ 47 EGZPO** — Uebergangsvorschrift Justizstandort-Staerkungsgesetz: alte Wertgrenze 600 EUR gilt fort für Altverfahren mit Stichtag 31.12.2025.
- **§ 321a ZPO** — Anhörungsruege bei Gehoersverletzung (enge Ausnahme).
- **§ 522 ZPO** — Verwerfung unstatthafter Berufung durch LG.

## Schritt-für-Schritt-Anleitung

### Schritt 1 — Zulassungsgruende pruefen

§ 511 IV ZPO setzt voraus:

- **Grundsaetzliche Bedeutung**: Rechtsfrage hat allgemeine Klaerungs-Bedeutung.
- **Fortbildung des Rechts**: Frage ist offen und braucht Entscheidung.
- **Sicherung einheitlicher Rechtsprechung**: Divergierende Entscheidungen anderer Gerichte.

In Praxis: AG-Urteile mit niedriger Beschwer werden sehr selten zugelassen.

### Schritt 2 — Im AG-Verfahren Zulassung anregen

Schon **im AG-Verfahren** koennen Sie die Zulassung der Berufung anregen — typisch in der muendlichen Verhandlung oder im letzten Schriftsatz. Begruendung:

- Welche Rechtsfrage ist klaerungs-beduerftig?
- Gibt es divergierende Entscheidungen anderer Gerichte?
- Warum ist Klaerung wichtig?

Das AG entscheidet ueber die Zulassung **im Urteil**.

### Schritt 3 — Pruefen, ob das AG zugelassen hat

Schauen Sie im Urteil unter "Tenor" oder am Ende der Entscheidungsgruende. Dort steht typisch:

- "Die Berufung wird zugelassen." → Sie koennen Berufung einlegen. Skill `berufung-amtsgericht-511-zpo`.
- Oder: Keine Aussage zur Zulassung. Das heisst: **Zulassung erfolgt nicht** (im Zweifel hat das AG sie geprueft und stillschweigend abgelehnt).

### Schritt 4 — Wenn nicht zugelassen: keine Berufung

Wenn das AG die Berufung nicht zugelassen hat und Ihre Beschwer 1.000 EUR oder weniger betraegt, ist die Berufung **endgueltig ausgeschlossen**. Eine separate "Zulassungs-Beschwerde" zum LG sieht § 511 ZPO **nicht** vor.

Versuche, dennoch eine Berufung einzulegen, werden vom LG nach § 522 I ZPO als unzulaessig verworfen — mit Kostenfolge für Sie.

**Uebergangsfall pruefen:** Wenn Ihre Beschwer zwischen 600 und 1.000 EUR liegt, kontrollieren Sie: Wurde das AG-Urteil bis 31.12.2025 verkuendet oder die muendliche Verhandlung bis dahin geschlossen? Dann gilt nach § 47 EGZPO die alte Wertgrenze 600 EUR — Berufung ist ohne Zulassung statthaft.

### Schritt 5 — Enge Ausnahme: Anhörungsruege § 321a ZPO

Wenn das AG **Ihr rechtliches Gehoer verletzt** hat (z.B. einen entscheidungserheblichen Vortrag vollstaendig ignoriert), koennen Sie binnen 2 Wochen ab Kenntnis Anhörungsruege erheben — beim **AG selbst** (nicht beim LG). Voraussetzungen sind eng:

- Konkrete Gehoersverletzung darlegen.
- Entscheidungserheblichkeit.
- Frist 2 Wochen.

Das AG prueft seine eigene Entscheidung. Bei Erfolg fuehrt es das Verfahren fort. Skill `wiedereinsetzung-frist-233-zpo` (Wiedereinsetzung, separates Thema).

### Schritt 6 — Realistisch: meist Urteil akzeptieren

Bei niedriger Beschwer ist oft sinnvoller, das AG-Urteil zu akzeptieren — selbst wenn Sie es für falsch halten. Die Kosten eines Berufungs- oder Anhörungsruege-Versuchs uebersteigen oft den Streitwert.

### Schritt 7 — Bei Zulassung: Berufung einlegen

Wenn das AG zugelassen hat: Sie koennen Berufung normal einlegen. Frist 1 Monat ab Zustellung (§ 517 ZPO). Begruendung durch Anwalt. Skill `berufung-amtsgericht-511-zpo`.

## Worauf Sie besonders achten muessen

- **Zulassung passiert im AG-Urteil** — nicht spaeter.
- **Keine separate Zulassungs-Beschwerde** zum LG. Wer trotzdem versucht, zahlt drauf.
- **Anhörungsruege § 321a ZPO** ist die einzige Notfall-Option bei Gehoersverletzung — kein Allzweck-Rechtsmittel.
- **Wertgrenze 1.000 EUR** (Stand 2026; frueher 600 EUR).
- **Uebergangsfaelle § 47 EGZPO**: Alte 600-EUR-Grenze gilt fort, wenn Urteil bis 31.12.2025 verkuendet oder muendliche Verhandlung bis dahin geschlossen wurde.

## Typische Fehler

- "Mein Fall ist grundsaetzlich, ich bekomme Zulassung." → Praxis sehr restriktiv; ohne Anregung im AG-Verfahren so gut wie nie.
- "Wenn AG nicht zulaesst, lege ich Beschwerde beim LG ein." → Existiert nicht. Eine Zulassungs-Beschwerde gibt es in § 511 ZPO **nicht**.
- "Anhörungsruege bedeutet zweite Chance auf alles." → Falsch. Nur bei konkreter, entscheidungserheblicher Gehoersverletzung.
- "Wertgrenze ist 600 EUR." → Veraltet. Seit 01.01.2026 sind es 1.000 EUR — ausser in Uebergangsfaellen nach § 47 EGZPO.
- "Mein altes Urteil ist nicht mehr berufungsfaehig, weil ich nur 800 EUR Beschwer habe." → Falsch, wenn das Urteil bis 31.12.2025 verkuendet wurde: dort gilt noch 600 EUR (§ 47 EGZPO).

## Quellen und Aktualitaet

Stand: 05/2026. § 511 ZPO mit Anhebung Beschwer auf 1.000 EUR seit 01.01.2026 (Justizstandort-Staerkungsgesetz vom 08.12.2025, BGBl. I Nr. 318). Uebergangsregel § 47 EGZPO: Alte Wertgrenze 600 EUR gilt fort für Verfahren mit anzufechtender Entscheidung bis 31.12.2025 bzw. mit bis dahin geschlossener muendlicher Verhandlung. Zulassung erfolgt ausschliesslich durch das erstinstanzliche Gericht (AG). Eine eigenstaendige Zulassungs-Beschwerde zum LG sieht § 511 ZPO nicht vor.

---

## Skill: `muendliche-verhandlung-akten-griffbereit`

_Mit Akten und Anlagen optimal in die muendliche Verhandlung vor dem Amtsgericht. Anlagen-Reiter Stichwort-Liste Mitschreib-Block Notizen zu Streit-Punkten. Vorbereitung der Argumente zur Replik im Termin. Praesenz oder Video 128a ZPO. Was zum Tisch was in die Tasche._

# In den Termin gehen — Akten griffbereit, Notizen parat

## Worum geht es?

Sie haben eine Klage eingereicht oder eine Klageerwiderung geschrieben. Jetzt kommt der Termin im Gerichtssaal (oder per Video). Diese Skill zeigt, **wie Sie Ihre Akten so vorbereiten, dass Sie im Termin nichts suchen muessen** und auf jede Frage des Richters die richtige Anlage in der Hand haben.

## Wann brauchen Sie diese Skill?

- Sie haben eine Ladung zum Termin bekommen.
- Sie haben mehrere Anlagen und Schriftsaetze.
- Sie wollen sich nicht im Termin blamieren, weil Sie etwas suchen muessen.

## Fachbegriffe (kurz erklaert)

- **Termin**: Die muendliche Verhandlung vor dem Richter. Beim Amtsgericht typisch im Gerichtssaal.
- **Akten-Reiter**: Eine Trennlasche im Ordner, beschriftet, damit Sie Anlagen schnell finden.
- **Termin-Stichwort-Liste**: Eine selbst gemachte Liste mit den wichtigsten Themen, die Sie ansprechen wollen.
- **Mitschreib-Block**: Ein Notizblock, auf dem Sie im Termin festhalten, was der Richter sagt und was die Gegenseite sagt.

## Schritt-für-Schritt-Vorbereitung

### Schritt 1 — Akten-Ordner anlegen

Besorgen Sie einen Ordner (Schnell-Hefter oder Ringordner). Erstellen Sie Trennlaschen mit:

- **Tab 1: Klageschrift**
- **Tab 2: Anlagenverzeichnis**
- **Tab 3: Anlage K1**
- **Tab 4: Anlage K2**
- ... (so viele wie Sie Anlagen haben)
- **Tab "Klageerwiderung"**
- **Tab "Replik"**
- **Tab "Termin-Notizen"** (leerer Block)

Schreiben Sie auf die Trennlasche **gross und lesbar** den Tab-Namen.

### Schritt 2 — Stichwort-Liste erstellen

Erstellen Sie ein eigenes Blatt mit **maximal 1 Seite** mit den Punkten, die Sie unbedingt ansprechen wollen:

```
Termin-Stichwort-Liste

1. Anspruch: 1.250 EUR aus Kaufvertrag vom 12.03.2025
2. Kernpunkt: Beklagter hat die Lieferung verweigert.
3. Beweise:
 - K1 = Vertrag (S. 2 Klausel III)
 - K2 = Rechnung (saldiert 1.250 EUR)
 - K3 = E-Mail Beklagter 20.04.2025 ("kann nicht zahlen")
 - K4 = Mahnung 02.05.2025
4. Gegen-Argumente Beklagter:
 - sagt: Vertrag war nichtig wegen Wuchers
 - meine Antwort: marktueblicher Preis (siehe K5 = Vergleichs-Angebote)
5. Vergleichs-Bereitschaft: ja, ab 900 EUR
6. Zeugen vorhanden: Zeuge Mueller zu Anruf vom 18.04.2025
```

### Schritt 3 — Streit-Punkte gegenueberstellen

Auf einem weiteren Blatt machen Sie eine **Tabelle** mit den Streit-Punkten:

| Punkt aus Klageerwiderung | Meine Antwort / Replik | Beweis |
|-------------------------------------|----------------------------------|---------------|
| Vertrag war nichtig wegen Wuchers | Preis war marktueblich | K5 |
| Lieferung war mangelhaft | War zur Zeit der Uebergabe ok | K1 Klausel V |
| Mahnung kam zu spaet | Frist eingehalten — 14 Tage | K4 Datum |

Diese Tabelle hilft Ihnen, im Termin **keinen Punkt zu vergessen**.

### Schritt 4 — Termin-Notizen vorbereiten

Legen Sie einen leeren Block oder Notizblock in die letzte Trennlasche. Im Termin schreiben Sie auf:

- Was sagt der Richter?
- Was sagt die Gegenseite?
- Was wird beschlossen?
- Welche Frist setzt das Gericht?

### Schritt 5 — Was kommt auf den Tisch, was in die Tasche?

**Auf den Tisch im Termin:**
- Stichwort-Liste (1 Blatt)
- Streit-Punkte-Tabelle (1 Blatt)
- Klageschrift (gut sichtbar)
- Mitschreib-Block

**Im Ordner griffbereit:**
- Alle Anlagen K1-Kn
- Klageerwiderung der Gegenseite
- Replik (falls Sie eine geschrieben haben)

**In der Tasche als Reserve:**
- Personalausweis
- Ladungs-Schreiben
- Wasser-Flasche
- Kugelschreiber + Reserve-Stift

### Schritt 6 — Anlagen-Reiter koennen Lebensretter sein

Beschriften Sie jede Trennlasche so gross, dass Sie sie aus 30 cm Entfernung lesen koennen. So koennen Sie im Termin schnell zur richtigen Stelle blaettern, ohne lange zu suchen.

## Bei Video-Verhandlung (§ 128a ZPO)

Wenn der Termin als Video stattfindet, brauchen Sie:

- Computer/Tablet mit Webcam und Mikrofon.
- Ruhigen Raum.
- **Akten-Ordner offen neben dem Geraet** — Sie koennen waehrend des Videos kurz reinschauen.
- **Zweites Geraet (z.B. Tablet)** mit den wichtigsten PDFs offen — als Backup, wenn Sie schnell etwas zeigen sollen.
- Stabile Internet-Verbindung.
- Personalausweis für Identitaets-Pruefung griffbereit.

## Worauf Sie besonders achten muessen

- **Vor dem Termin durchblaettern**: Die Akten den Tag vor dem Termin noch einmal durchgehen. So sind Sie sicher, wo was steht.
- **Frueh erscheinen**: 30 Min. vor Termin im Gericht sein (Sicherheits-Kontrolle, Saal suchen, anmelden).
- **Hoeflicher Auftritt**: Aufstehen wenn der Richter den Saal betritt; Anrede sachlich-knapp "Herr Vorsitzender" / "Frau Vorsitzende" oder "Herr Richter" / "Frau Richterin". Veraltete Formeln wie "Hohes Gericht" oder "Hoher Herr Vorsitzender" sind nicht erforderlich. Skill `verhalten-gerichtssaal-laienleitfaden`.
- **Nichts unaufgefordert sagen**: Warten, bis der Richter Sie aufruft.
- **Klar und kurz sprechen**: Punkte aus der Stichwort-Liste der Reihe nach abarbeiten.

## Typische Fehler

- **Fehler:** Akten unsortiert in einer Plastiktuete. → **So vermeiden:** Ordner mit Trennlaschen vorbereiten.
- **Fehler:** Im Termin merken: eine Anlage zuhause vergessen. → **So vermeiden:** Vor Abfahrt Checkliste durchgehen.
- **Fehler:** Vor lauter Aufregung Stichwort-Liste vergessen. → **So vermeiden:** Stichwort-Liste GANZ OBEN auf den Stapel.
- **Fehler:** Bei Video-Verhandlung Webcam nicht getestet. → **So vermeiden:** Einen Tag vorher Probe-Verbindung machen.
- **Fehler:** Mitschreib-Block vergessen, nichts notiert. → **So vermeiden:** Block und Stift IMMER mit.

## Quellen und Aktualitaet

Stand: 05/2026. Termin-Vorbereitung ist Praxis-Konvention; die hier beschriebenen Akten-Methoden sind in der anwaltlichen Praxis Standard und auch für Selbstvertreter geeignet.

---

## Skill: `online-verfahren-11-buch-zpo-experimentell`

_Experimentelles Online-Verfahren der ZPO seit 2025 ggf 2026. Vollständig digitales Zivilverfahren bestimmte Streitwerte teilnehmende Amtsgerichte. Aktuelle Normen-Verortung prüfen. Vergleich Praesenz-Verfahren Vorteile Risiken Strukturierte Eingabe-Masken. Teilnahme._

# Online-Verfahren — das neue digitale Zivilverfahren

## Worum geht es?

Seit 2025 gibt es in Deutschland ein **experimentelles vollstaendig digitales Zivilverfahren** ("Online-Verfahren"). Es ermoeglicht, einen Zivilrechtsstreit von Anfang bis Ende ueber eine Internet-Plattform zu fuehren — ohne Papier, ohne persönliche Termine vor Ort. Das Verfahren ist in einem neuen Buch der ZPO (vermutlich 11. Buch) verankert und gilt zunaechst nur an **teilnehmenden Amtsgerichten** und für **bestimmte Streit-Typen**.

**Wichtig:** Die genaue Norm-Verortung (Paragraphennummer, Geltungsbereich, Schwellenwerte) ist im laufenden Gesetzgebungs- und Erprobungs-Verfahren. **Verifizieren Sie die aktuellen Normen in amtliche/freie Quellen oder lizenzierte Datenbanken und auf der Webseite Ihres oertlich zuständigen Amtsgerichts.**

## In einfacher Sprache

Es gibt ein neues Online-Gericht. Sie machen alles am Computer. Sie reichen die Klage ein. Sie sehen die Antwort der Gegenseite am Bildschirm. Manchmal gibt es ein Video-Treffen. Das gibt es nur bei einigen Gerichten und nur für bestimmte Streit-Themen.

## Wann brauchen Sie diese Skill?

- Sie wollen klagen und Ihr Amtsgericht bietet das Online-Verfahren an.
- Sie wurden in einem Online-Verfahren verklagt.
- Sie wollen wissen, ob das Online-Verfahren für Ihren Fall passt.

## Fachbegriffe (kurz erklaert)

- **Online-Verfahren**: Ein voll-digitales Zivilverfahren auf einer Internet-Plattform.
- **Experimentier-Klausel**: Eine Gesetzesregelung, die ein neues Verfahren erstmal in einem Test-Modus zulaesst.
- **Strukturierte Eingabe-Maske**: Ein Formular auf der Plattform, in das Sie Ihren Sachverhalt Schritt für Schritt eintippen.
- **Teilnehmende Gerichte**: Nicht jedes Amtsgericht bietet das Online-Verfahren an. Eine Liste finden Sie auf der Webseite der Justiz Ihres Bundeslandes.

## Rechtsgrundlagen (Stand 2026)

- **11. Buch ZPO (Online-Verfahren)** — neues Buch der Zivilprozessordnung, eingefuehrt mit dem Gesetz zur Förderung digitaler Justiz-Verfahren (genaues Inkrafttreten und Paragraphen verifizieren).
- **§ 128a ZPO** — Video-Verhandlung (auch im klassischen Verfahren moeglich, vgl. `video-verhandlung-128a-zpo`).
- **§ 130a ZPO** — elektronische Einreichung (gilt auch im klassischen Verfahren).

**Verifizieren Sie die aktuelle Rechtslage** in amtliche/freie Quellen oder lizenzierte Datenbanken — die Normen-Nummerierung und der Anwendungsbereich des Online-Verfahrens werden im Erprobungs-Zeitraum noch praezisiert.

## Was unterscheidet das Online-Verfahren vom normalen Verfahren?

| Merkmal | Normales Verfahren | Online-Verfahren |
|-----------------------|------------------------------------------|---------------------------------------------------------|
| Klage einreichen | Papier oder MJP oder § 130a ZPO | Strukturierte Eingabe-Maske auf der Plattform |
| Klageschrift | Freier Text in Word/PDF | Vorgegebene Felder (Antrag, Sachverhalt, Beweise) |
| Schriftverkehr | E-Mail, Post, MJP | Plattform-internes Postfach |
| Termin | Im Gerichtssaal | Video-Konferenz auf der Plattform |
| Urteil | Schriftlich per Post | Im Plattform-Postfach |
| Akteneinsicht | Geschaeftsstelle, Anwalt | Plattform jederzeit |

## Vorteile

- **Niedrigschwellig**: Strukturierte Maske hilft Laien, alles Wichtige anzugeben.
- **Kein Papier**: Alles digital.
- **Termin von zuhause**: Per Video, kein Anreise-Stress.
- **Schneller**: Erprobte Standard-Wege, weniger Wartezeit.

## Risiken und Grenzen

- **Nicht für komplexe Faelle**: Schwierige Sachverhalte (medizinische Gutachten, technische Details) lassen sich in der Eingabe-Maske nur eingeschraenkt darstellen.
- **Technik-Voraussetzungen**: Sie brauchen Computer, stabile Internet-Verbindung, Webcam, Mikrofon.
- **Identifikation**: Sie muessen sich elektronisch ausweisen (z.B. Mein Justizpostfach, eID Personalausweis).
- **Akten-Backup**: Sie sollten regelmaessig Kopien Ihrer Eingaben lokal speichern (z.B. als PDF herunterladen).
- **Nicht ueberall verfuegbar**: Nur an teilnehmenden Amtsgerichten.
- **Nicht für alle Streit-Typen**: Bestimmte Sachgebiete koennen ausgeschlossen sein.

## Schritt-für-Schritt-Anleitung

### Schritt 1 — Pruefen, ob Ihr Amtsgericht teilnimmt

Schauen Sie auf der Webseite der Justiz Ihres Bundeslandes oder direkt auf der Webseite des oertlich zuständigen Amtsgerichts nach. Beispiele:

- Justizportal Bund-Länder
- "Online-Verfahren" als Stichwort suchen.
- Bei der Geschaeftsstelle des Amtsgerichts nachfragen.

### Schritt 2 — Pruefen, ob Ihr Streit-Typ zugelassen ist

Das Online-Verfahren ist nicht für alle Streit-Typen offen. Typisch zugelassen sind z.B. Zahlungsklagen unter einem bestimmten Streitwert. Lesen Sie die Bedingungen der Plattform.

### Schritt 3 — Auf der Plattform registrieren

Identifikation typisch ueber:
- **Mein Justizpostfach (MJP)** — siehe `einreichung-mein-justizpostfach-mjp-2024`.
- **eID** mit dem Personalausweis und einem Lesegeraet/Smartphone-NFC.
- Login-Daten ueber Bund-ID-Verfahren.

### Schritt 4 — Klage in der Eingabe-Maske erfassen

Die Plattform fuehrt Sie durch:
- Antrag (was wollen Sie?)
- Beklagter (Name, Adresse)
- Sachverhalt (was ist passiert?)
- Beweise (welche Beweise haben Sie?)
- Anlagen (PDF hochladen)

Speichern Sie regelmaessig (die Plattform speichert meistens automatisch).

### Schritt 5 — Einreichen und Vorschuss zahlen

- Eingabe-Maske absenden.
- Plattform berechnet die Gerichtskosten.
- Zahlung per SEPA-Lastschrift, Ueberweisung oder Karte.
- Sobald gezahlt: Klage wird zugestellt.

### Schritt 6 — Reaktion der Gegenseite abwarten

Sie sehen im Plattform-Postfach, wenn die Gegenseite antwortet. Sie reagieren wieder ueber die Maske.

### Schritt 7 — Video-Termin

Wenn ein Termin stattfindet, bekommen Sie einen Link. Loggen Sie sich rechtzeitig ein (z.B. 15 Min. vorher). Achten Sie auf:
- Ruhiger Raum, kein Hintergrund-Laerm.
- Webcam auf Augenhoehe.
- Stabile Internet-Verbindung.
- Personalausweis griffbereit für Identitaets-Pruefung.

### Schritt 8 — Urteil im Plattform-Postfach

Das Urteil erscheint im Plattform-Postfach. Laden Sie es als PDF herunter und speichern Sie es lokal.

## Worauf Sie besonders achten muessen

- **Speichern Sie alles lokal als PDF.** Wenn die Plattform mal nicht laeuft, sind Sie nicht hilflos.
- **Pruefen Sie die Fristen.** Auch im Online-Verfahren gelten die normalen Fristen der ZPO.
- **Lassen Sie sich nicht von der Eingabe-Maske eingeengen**: Wenn Ihr Sachverhalt komplexer ist, fuegen Sie ein ergaenzendes PDF als Anlage hinzu.
- **Bei Zweifel: klassisches Verfahren waehlen.** Das Online-Verfahren ist freiwillig.

## Typische Fehler

- **Fehler:** Plattform für hochkomplexe Faelle nutzen — Eingabe-Maske ist zu eng. → **So vermeiden:** Bei komplexen Faellen klassisches Verfahren waehlen.
- **Fehler:** Plattform-Postfach nicht regelmaessig pruefen — Fristen verpasst. → **So vermeiden:** Mehrmals pro Woche einloggen oder Benachrichtigungs-E-Mail aktivieren.
- **Fehler:** Lokale Sicherungs-Kopien vergessen. → **So vermeiden:** Nach jeder Eingabe als PDF herunterladen.
- **Fehler:** Bei Video-Termin technische Probleme — kein Backup-Geraet. → **So vermeiden:** Vor dem Termin Funktion testen, Smartphone als Backup griffbereit.

## Quellen und Aktualitaet

Stand: 05/2026. Das Online-Verfahren wurde 2025 als Experimentier-Verfahren eingefuehrt; die genaue Norm-Verortung im 11. Buch ZPO und der Anwendungsbereich werden im laufenden Erprobungs-Zeitraum praezisiert. **Verifizieren Sie die aktuelle Rechtslage in amtliche/freie Quellen oder lizenzierte Datenbanken und auf der Webseite Ihres oertlich zuständigen Amtsgerichts vor Klageeinreichung.**

---

## Skill: `sachliche-zustaendigkeit-amtsgericht-23-gvg`

_Prüfung der sachlichen Zuständigkeit des Amtsgerichts nach § 23 GVG. Wertgrenze seit 01.01.2026 zehntausend EUR (§ 23 Nr. 1 GVG aktuelle Fassung). Sonderzuständigkeiten § 23 Nr. 2 GVG Mietsachen Reisevertrag. Stand der Reform und Streitwert-Berechnung erlaeutert._

# Ist das Amtsgericht für Ihren Fall sachlich zuständig?

## Worum geht es?

Sachliche Zuständigkeit heisst: Welches Gericht (Amtsgericht oder Landgericht) entscheidet ueber eine bestimmte Streitart? In Deutschland richtet sich das im Zivilrecht hauptsaechlich nach dem **Streitwert** (= Geldbetrag, um den es geht) und nach **Sondernormen** für bestimmte Streitarten. Wenn Sie das falsche Gericht anrufen, wird Ihre Klage verwiesen — das kostet Sie Zeit und Geld.

## Wann brauchen Sie diese Skill?

- Sie wollen wissen, ob Sie an das AG oder ans LG muessen.
- Sie haben einen mittleren Streitwert und sind unsicher wegen der Grenze.
- Sie haben eine Mietsache, Reisemangel oder andere Spezialmaterie.

## Fachbegriffe (kurz erklaert)

- **Sachliche Zuständigkeit**: Welches Gericht (AG vs. LG) ist nach Streitart und Wert zuständig.
- **Streitwert**: Der Geldwert dessen, worum gestritten wird. Bei Geldforderung = Forderungsbetrag.
- **Wertzuständigkeit**: Zuständigkeit nach Streitwert (im Gegensatz zur Zuständigkeit nach Streitart).

## Rechtsgrundlagen

- **§ 23 Nr. 1 GVG (Fassung seit 01.01.2026)** — Amtsgericht zuständig bis zur Wertgrenze von **10.000 EUR** (zehntausend Euro). Die Grenze wurde mit dem Justizstandort-Staerkungsgesetz zum 01.01.2026 von 5.000 EUR auf 10.000 EUR angehoben. **Verifizieren Sie bei Klagen kurz vor oder kurz nach dem Stichtag, welche Fassung für Ihren Fall gilt** (Uebergangsregelungen pruefen).
- **§ 23 Nr. 2 GVG** — Bestimmte Streitarten **immer** AG, unabhaengig vom Wert.
- **§ 23a, 23b, 23c GVG** — Familiensachen, Betreuungssachen, Nachlasssachen.
- **§ 71 GVG** — LG-Zuständigkeit als Auffangzuständigkeit ab 10.000 EUR.
- **§ 3 ZPO** — Streitwert nach freiem Ermessen.

## Schritt-für-Schritt-Anleitung

### Schritt 1 — Spezialzuständigkeit pruefen

Diese Streitarten sind **unabhaengig vom Streitwert immer** beim AG (§ 23 Nr. 2 GVG, § 23a GVG):

- Wohnraummietsachen (§ 23 Nr. 2 a GVG): Miete, Nebenkosten, Kuendigung, Raeumung, Schoenheitsreparaturen.
- Streitigkeiten ueber Reisevertrag (§ 23 Nr. 2 b GVG): Reisemaengel, Reise-Erstattung.
- Streitigkeiten ueber Wildschaeden (§ 23 Nr. 2 c GVG).
- Streitigkeiten ueber Unterhaltsansprueche zwischen Verwandten (§ 23 Nr. 2 d GVG, Familienrechtl. ergaenzt § 23a GVG).
- Familiensachen: Ehescheidung, Sorgerecht, Versorgungsausgleich — immer AG (Familiengericht).
- Betreuungssachen, Nachlasssachen — immer AG (§ 23b, 23c GVG).

### Schritt 2 — Wenn keine Spezialzuständigkeit: Streitwert berechnen

- **Geldforderung**: Streitwert = Forderungssumme. Beispiel: Sie wollen 8.000 EUR — Streitwert 8.000 EUR.
- **Mehrere Forderungen**: Werden zusammengerechnet (§ 5 ZPO).
- **Rente, wiederkehrende Leistung**: § 9 ZPO — dreieinhalbfacher Jahresbetrag.
- **Anspruch auf Herausgabe einer Sache**: Wert der Sache.
- **Feststellungsklage**: 80 % des positiven Anspruchswerts (Praxisregel).
- **Mietsachen**: Bei Raeumung der Jahresbetrag der Bruttomiete (§ 41 GKG).

### Schritt 3 — Wertgrenze pruefen (Stand 2026)

- **Streitwert bis einschliesslich 10.000 EUR**: Amtsgericht (§ 23 Nr. 1 GVG). Sie koennen sich **selbst vertreten** — kein Anwaltszwang.
- **Streitwert ueber 10.000 EUR**: Landgericht (§ 71 GVG). **Anwaltszwang** § 78 I ZPO.

**Reform-Hinweis**: Die Wertgrenze wurde zum 01.01.2026 von 5.000 EUR auf 10.000 EUR angehoben. Damit gehoeren deutlich mehr Streitigkeiten zur AG-Zuständigkeit, in der Sie sich selbst vertreten koennen. Wenn Sie einen Streitwert knapp ueber 10.000 EUR haben und Anwaltszwang vermeiden wollen, kann eine **Teilklage** (nur ueber einen Teilbetrag klagen) erwogen werden — beachten Sie aber die Auswirkungen auf Verjährung und Streitwert. Sprechen Sie das ggf. mit der Rechtsantragsstelle (Skill `einreichung-rechtsantragsstelle-selbst`).

### Schritt 4 — Bei Unsicherheit beim Streitwert

Geben Sie in der Klage einen plausiblen Streitwert an. Das Gericht setzt am Ende den Streitwert endgueltig fest (§ 63 GKG). Bei Sachstreitigkeiten ohne klaren Geldwert schaetzt das Gericht nach § 3 ZPO.

### Schritt 5 — Folge bei falscher Zuständigkeit

Falsche Zuständigkeit ist nicht das Ende. Auf Ihren Antrag verweist das Gericht nach § 281 ZPO an das zuständige Gericht. **Aber**: Sie zahlen ggf. zusaetzliche Kosten und verlieren Zeit. Wenn der Beklagte vor dem unzuständigen Gericht ruegelos zur Sache verhandelt, wird das Gericht zuständig (§ 39 ZPO, "ruegelose Einlassung") — also nicht spekulieren, sondern richtig einreichen.

## Worauf Sie besonders achten muessen

- **Stichtag 01.01.2026**: Fuer Klagen, die vorher anhaengig waren, gilt die alte Grenze von 5.000 EUR (Uebergangsregelung beachten). Fuer neue Klagen ab 01.01.2026 gilt 10.000 EUR.
- **Mietsache**: Auch eine Miet-Forderung von 50.000 EUR ist AG. Streitwert ist hier irrelevant.
- **Familiensache**: Immer AG, aber Anwaltszwang nach § 114 FamFG. Skill `anwaltszwang-pruefen-78-zpo`.
- **Streitwert wird beim Einreichen vorlaeufig angegeben**; das Gericht setzt am Ende endgueltig fest.

## Typische Fehler

- "Ich klage in jedem Fall beim AG, ist ja billiger." → Wenn LG zuständig waere (Streitwert ueber 10.000 EUR), wird verwiesen und Sie haben Kosten doppelt.
- "Eine Mietsache mit 30.000 EUR Hauptforderung gehoert ans LG." → Falsch. Mietsachen sind **immer** AG, unabhaengig vom Wert.
- "Bei Unsicherheit nehme ich den niedrigsten Streitwert an." → Falsch. Setzen Sie realistisch an; bei Untererfassung droht spaetere Streitwert-Festsetzung und Nachzahlung.
- "Familiengerichts-Sachen kann ich selbst betreiben." → Bei Ehesachen und Folgesachen Anwaltszwang § 114 FamFG.
- "Die Grenze ist 5.000 EUR." → Veraltet. Seit 01.01.2026 sind es 10.000 EUR.

## Quellen und Aktualitaet

Stand: 05/2026. § 23 Nr. 1 GVG aktuelle Fassung: AG-Wertgrenze 10.000 EUR (Anhebung von 5.000 EUR zum 01.01.2026 durch das Justizstandort-Staerkungsgesetz). Bei Klagen aus der Uebergangszeit Stichtag und Anhaengigkeit pruefen.

---

## Skill: `einreichung-papierform-mit-abschriften`

_Einreichung der Klage in Papierform. Anzahl der Abschriften Versand per Post Einschreiben oder persönliche Abgabe an der Geschäftsstelle. Eingangsstempel Sendebeleg Beweis für rechtzeitige Einreichung. Vorteile und Nachteile gegenüber elektronischer Einreichung._

# Klage in Papierform einreichen

## Worum geht es?

Buerger duerfen weiterhin in Papierform einreichen. Es gibt kein § 130d-ZPO-Pflicht für Sie. Diese Skill zeigt, wie Sie sauber Papier-Klagen aufbauen, mit der richtigen Anzahl Abschriften, dem richtigen Versandweg und mit Beweis für Fristwahrung.

## Wann brauchen Sie diese Skill?

- Sie wollen klassisch per Post einreichen.
- Sie haben kein MJP-Konto und keine Zeit, eines einzurichten.
- Sie wollen persoenlich an der Geschaeftsstelle abgeben.

## Fachbegriffe (kurz erklaert)

- **Abschrift**: Vollstaendige Kopie der Klageschrift mit Anlagen, für die Gegenseite bestimmt.
- **Eingangsstempel**: Stempel des Gerichts mit Datum und Uhrzeit der Einreichung.
- **Einschreiben**: Postversand mit Empfangsbestaetigung.

## Rechtsgrundlagen

- **§ 130 ZPO** — Anforderungen an Schriftsatz.
- **§ 130 Nr. 6 ZPO** — Unterschrift.
- **§ 133 ZPO** — Schriftsaetze mit Beilagen.
- **§ 167 ZPO** — Zustellung "demnaechst" wirkt zurueck (wichtig für Fristwahrung!).

## Schritt-für-Schritt-Anleitung

### Schritt 1 — Wie viele Saetze?

Pro Streitpartei brauchen Sie eine Abschrift, plus Original für das Gericht.

- 1 Klaeger, 1 Beklagter: 2 Saetze (1 Original Gericht, 1 Abschrift Beklagter) + 1 für Sie selbst.
- 1 Klaeger, 2 Beklagte: 3 Saetze (1 Original + 2 Abschriften) + 1 für Sie selbst.

Faustregel: 1 Original + so viele Abschriften wie Beklagte + 1 Aktenkopie für Sie.

### Schritt 2 — Saetze identisch?

Ja, jede Abschrift muss exakt identisch zum Original sein:

- Klageschrift komplett.
- Alle Anlagen K1-Kn.

### Schritt 3 — Original unterschreiben

§ 130 Nr. 6 ZPO: Original handschriftlich unterzeichnen. Abschriften muessen **nicht** unterschrieben sein — Sie koennen "gez. Vorname Nachname" schreiben.

### Schritt 4 — Verpacken

- Aktenordner oder grosser Umschlag.
- Original und Abschriften in einer Sendung an das Gericht.

### Schritt 5 — Versandweg

Optionen:

- **Einschreiben mit Rueckschein**: Best — Beweis für Zugang.
- **Einschreiben Einwurf**: Etwas guenstiger, Beweis ist Sendungs-Verlaufsmeldung.
- **Normaler Brief**: Riskant; kein Zugangs-Beweis. Vermeiden, wenn Frist laeuft.
- **Persoenlich an der Geschaeftsstelle**: Sicherster Weg. Sie bekommen Eingangsstempel.

### Schritt 6 — Persoenliche Abgabe

- Gehen Sie zur Geschaeftsstelle des Amtsgerichts (Oeffnungszeiten beachten).
- Bringen Sie Ihre **eigene Kopie** als Stempelbeleg-Vorlage mit.
- Mitarbeiter stempelt auf Ihrer Kopie das Eingangsdatum.
- Wichtig: Stempel ist Ihr Beweis. Aufbewahren!

### Schritt 7 — Eingangsbeleg per Post

Wenn Sie per Post schicken und Sie selbst senden:

- Einschreiben mit Rueckschein: Rueckschein-Karte ist Beweis.
- Einschreiben Einwurf: Sendungs-Nummer mit Statusabfrage.
- Bei normaler Post: nichts. Riskant.

Skill `zurechnungsproblem-versand-durch-dritte`.

### Schritt 8 — § 167 ZPO Rueckwirkung

Wichtig für Verjährungs-Hemmung und Frist-Einhaltung: Wenn die Zustellung an den Beklagten **alsbald** erfolgt, gilt die Zustellung als am Tag der Klageeinreichung erfolgt. Sie muessen also nicht warten, dass die Zustellung tatsaechlich raus ist — der Eingang bei Gericht zaehlt für Frist.

Voraussetzung: Sie haben Gerichtskostenvorschuss zuegig gezahlt; sonst kein "demnaechst". Skill `gerichtskostenvorschuss-12-gkg`.

## Worauf Sie besonders achten muessen

- **Original unterschrieben**: ohne Unterschrift ist Klage formunwirksam.
- **Anschriften vollstaendig**: Klaeger, Beklagter.
- **Sendebeleg aufbewahren**: bei Fristen kritisch.
- **Vorschuss zahlen** zuegig: sonst Zustellung verzoegert, § 167 ZPO greift evtl. nicht.

## Typische Fehler

- "Nur Original, keine Abschriften." → Gericht muss zustellen — ohne Abschriften nicht moeglich, Verfahren verzoegert.
- "Klage als einfacher Brief." → Bei Fristen ein Risiko.
- "Unterschrift drucke ich aufs Computer." → Kein eigenhaendiges Unterzeichnen. Original muss handschriftlich unterschrieben sein.

## Quellen und Aktualitaet

Stand: 05/2026. §§ 130, 133, 167 ZPO unveraendert.

---

## Skill: `klageerwiderung-replik-anlagen-b1-b2`

_Anlagen-Nummerierung in Klageerwiderung und Replik korrekt fortführen. Beklagter nutzt B1 B2 B3. Klaeger nutzt in Replik K-Folge-Nummern ab Klage-Endnummer plus eins. Keine doppelten Nummern Querverweise zwischen Schriftsaetzen. Anlagenverzeichnis aktualisieren._

# Anlagen in Klageerwiderung und Replik — die Nummerierung fortfuehren

## Worum geht es?

Wenn Sie auf eine Klage antworten (= Klageerwiderung) oder selbst auf eine Klageerwiderung antworten (= Replik), muessen Sie wieder Anlagen einreichen. Aber **wie nummeriert man die richtig**, ohne dass es Verwirrung gibt? Diese Skill zeigt Ihnen die Praxis-Konvention.

## In aller Kuerze

- **Klaeger** nutzt **K1, K2, K3, ...** durchgehend ueber alle Schriftsaetze hinweg.
- **Beklagter** nutzt **B1, B2, B3, ...** durchgehend ueber alle Schriftsaetze hinweg.
- Wenn Sie in der Klage bei K8 aufgehoert haben, geht die Replik mit K9 weiter.
- Wenn der Beklagte in der Klageerwiderung bei B3 aufgehoert hat, geht die Duplik mit B4 weiter.
- **Nie wieder bei 1 anfangen.** Sonst kollidieren die Nummern.

## Wann brauchen Sie diese Skill?

- Sie haben eine Klageerwiderung bekommen und schreiben eine Replik.
- Sie sind beklagt und schreiben eine Klageerwiderung.
- Sie schreiben eine Duplik (Beklagter antwortet auf die Replik).

## Fachbegriffe (kurz erklaert)

- **Klageerwiderung**: Der erste Schriftsatz des Beklagten, mit dem er auf die Klage antwortet.
- **Replik**: Die Antwort des Klaegers auf die Klageerwiderung.
- **Duplik**: Die Antwort des Beklagten auf die Replik.
- **K-Anlagen**: Anlagen des Klaegers (K = Klaeger).
- **B-Anlagen**: Anlagen des Beklagten (B = Beklagter).

## Schritt-für-Schritt — als Beklagter

### Schritt 1 — Klage durchlesen und K-Anlagen identifizieren

Lesen Sie die Klageschrift. Notieren Sie: Welche K-Anlagen liegen bei? K1, K2, K3, ...? Bei welcher hoert es auf? K8?

### Schritt 2 — Eigene B-Anlagen festlegen

Wenn Sie eigene Beweisstuecke haben, fangen Sie mit **B1** an. Die K-Nummern des Klaegers werden NICHT verwendet. Klaeger und Beklagter haben getrennte Nummerierungs-Stroenge.

### Schritt 3 — Im Text verweisen

In der Klageerwiderung schreiben Sie:

> "Der Klaeger behauptet, der Vertrag sei am 12.03.2025 geschlossen worden. **Das wird bestritten.** Tatsaechlich gab es nur ein Vor-Gespraech. Der Vertrags-Entwurf wurde dem Beklagten erst am 25.03.2025 zugeleitet (**Anlage B1** — E-Mail mit Vertrags-Entwurf)."

Und auf K-Anlagen des Klaegers verweisen Sie auch:

> "Die vom Klaeger vorgelegte Rechnung (**Anlage K2 der Klageschrift**) hat der Beklagte nicht erhalten."

So ist klar: B1 = Beklagter-Anlage, K2 = Klaeger-Anlage.

### Schritt 4 — Anlagenverzeichnis B fuehren

Am Ende der Klageerwiderung:

```
Anlagenverzeichnis (Beklagter)

Anlage B1 — E-Mail mit Vertrags-Entwurf vom 25.03.2025 (1 Seite)
Anlage B2 — Foto der gelieferten Ware mit Mangel (2 Seiten)
Anlage B3 — Gutachten Sachverstaendiger ABC vom 15.05.2025 (8 Seiten)
```

## Schritt-für-Schritt — als Klaeger in der Replik

### Schritt 1 — Letzte K-Nummer der Klage merken

Wenn Sie in der Klage K1 bis K8 verwendet haben, geht es in der Replik mit **K9** weiter.

### Schritt 2 — Klageerwiderung lesen und B-Anlagen pruefen

Schauen Sie sich an, welche B-Anlagen der Beklagte vorgelegt hat. Notieren Sie: B1, B2, B3.

### Schritt 3 — Eigene neue K-Anlagen festlegen

Wenn Sie neue Beweisstuecke brauchen, fangen Sie bei K9 an (nicht bei K1!).

### Schritt 4 — Im Text verweisen

In der Replik:

> "Der Beklagte behauptet in der Klageerwiderung (S. 3, Absatz 2), der Vertrags-Entwurf sei erst am 25.03.2025 zugegangen (**Anlage B1**). **Dem wird widersprochen.** Vielmehr wurde der Vertrag bereits am 12.03.2025 in einem Praesenz-Treffen unterzeichnet (**Anlage K9** — Vertrags-Original mit Unterschriften)."

### Schritt 5 — Anlagenverzeichnis K fortfuehren

Am Ende der Replik:

```
Anlagenverzeichnis (Klaeger) — Fortfuehrung

(Anlagen K1 bis K8 wie in der Klageschrift)

Anlage K9 — Vertrags-Original mit Unterschriften vom 12.03.2025 (3 Seiten)
Anlage K10 — Zeugen-Aussage Zeuge Mueller schriftlich (2 Seiten)
```

So sieht man auf einen Blick: K1-K8 schon bekannt, K9-K10 neu.

## Schritt-für-Schritt — als Beklagter in der Duplik

### Schritt 1 — Letzte B-Nummer merken

B1, B2, B3 in der Klageerwiderung. In der Duplik geht es mit **B4** weiter.

### Schritt 2 — Eigene neue B-Anlagen vorlegen

```
Anlage B4 — Gegenargument-Schriftstueck (...)
Anlage B5 — Foto, das das Klaeger-Foto K9 widerlegt (...)
```

## Worauf Sie besonders achten muessen

- **Keine Kollision** — niemals zweimal "Anlage K3" oder "Anlage B2".
- **Konsequenz**: Wenn Klaeger K9, dann nicht "Anlage K1 zur Replik" schreiben.
- **Querverweis** auf gegnerische Anlagen: "Anlage B1 der Klageerwiderung" — so ist klar, welche gemeint ist.
- **Anlagenverzeichnis aktualisieren** — für jede neue Anlage ein Eintrag.

## Typische Fehler

- **Fehler:** In der Replik wieder bei K1 angefangen → es gibt jetzt zwei "Anlage K1". → **So vermeiden:** Immer die K-Nummerierung aus der Klage fortfuehren.
- **Fehler:** Beklagter nutzt K1, K2 (statt B1, B2) → Verwirrung. → **So vermeiden:** Beklagter immer B-Nummerierung.
- **Fehler:** Anlagenverzeichnis vergessen, nur im Text auf Anlagen verwiesen. → **So vermeiden:** Anlagenverzeichnis ist Pflicht-Element.
- **Fehler:** Querverweis "siehe Anlage 2" — unklar ob K2 oder B2. → **So vermeiden:** Immer den Buchstaben mitschreiben.

## Quellen und Aktualitaet

Stand: 05/2026. K- bzw. B-Anlagen-Konvention ist gerichtspraxis-ueblich, nicht gesetzlich vorgeschrieben. Variante: einige Anwaelte nutzen K1, K2 für Klaeger und KE1, KE2 für Klageerwiderung — Konvention regional unterschiedlich. Die hier vorgestellte K/B-Variante ist die haeufigste.

---

## Skill: `beratungshilfe-aussergerichtlich-brh`

_Beratungshilfe vor Klageerhebung. Beratungshilfegesetz BerHG ermöglicht bedürftigen Buergern kostenlose oder verguenstigte Anwaltsberatung vor Gericht. Antrag beim Amtsgericht Berechtigungsschein Eigenanteil. Sinnvoll als Vorklaerung bevor Sie selbst klagen._

# Beratungshilfe: Anwalt vor Klage (fast) umsonst

## Worum geht es?

Bevor Sie klagen, kann ein Anwaltsgespraech viel klaeren: Habe ich Erfolgsaussichten? Wie formuliere ich den Antrag? Welche Beweise? Wenn Sie beduerftig sind, koennen Sie **Beratungshilfe** nach dem Beratungshilfegesetz (BerHG) bekommen — der Anwalt wird vom Staat bezahlt, Sie zahlen nur eine Schutzgebuehr von 15 EUR.

## Wann brauchen Sie diese Skill?

- Sie ueberlegen Klage und wollen eine Beratung vor der Entscheidung.
- Sie wurden verklagt und brauchen ersten Rat.
- Sie haben Anwaltsbedarf, kein Geld.

## Fachbegriffe (kurz erklaert)

- **Beratungshilfe**: Staatliche Förderung der aussergerichtlichen Anwaltsberatung für Beduerftige.
- **Berechtigungsschein**: Vom Amtsgericht ausgestellter Schein, der dem Anwalt die Berechnung gegenueber dem Staat ermoeglicht.
- **Schutzgebuehr**: Selbst zu tragender Anteil; pauschal 15 EUR.

## Rechtsgrundlagen

- **§ 1 BerHG** — Anwendungsbereich Beratungshilfe.
- **§ 4 BerHG** — Antrag beim Amtsgericht.
- **§ 6a BerHG** — Schutzgebuehr 15 EUR.
- **§ 7 BerHG** — Gebührenrechnung Anwalt zum Staat.
- **§ 116 ZPO** — Verweisung auf PKH bei Klage.

## Schritt-für-Schritt-Anleitung

### Schritt 1 — Voraussetzungen pruefen

- Beduerftigkeit (aehnlich PKH).
- Keine anderweitige Beratungsmoeglichkeit (z. B. nicht durch Mitgliedschaft in Mieterverein etc.).
- Rechtsangelegenheit nicht mutwillig.

### Schritt 2 — Wahl: Selbst zum AG oder zum Anwalt

Variante A: Sie gehen **zum Amtsgericht**, fuellen Antrag aus, holen Berechtigungsschein und gehen damit zum Anwalt.

Variante B: Sie gehen **direkt zum Anwalt** und beantragen den Schein nachtraeglich (binnen 4 Wochen).

Variante A ist sicherer — Anwalt weiss, dass Schein bewilligt.

### Schritt 3 — Antrag stellen

Beim Amtsgericht Ihres Wohnsitzes:

- Formular für Beratungshilfe.
- Belege für Beduerftigkeit (Lohnabrechnungen, Sozialleistungs-Bescheid).
- Kurze Schilderung der Rechtsangelegenheit.

Sie bekommen einen Berechtigungsschein, mit dem Sie zum Anwalt gehen.

### Schritt 4 — Beim Anwalt

- Schein vorlegen.
- 15 EUR Schutzgebuehr zahlen (oder Anwalt schreibt Rechnung).
- Beratung erhalten — Anwalt erklaert, formuliert, prueft.

Der Anwalt rechnet seine Gebuehr direkt mit dem Staat ab.

### Schritt 5 — Was die Beratungshilfe abdeckt

- Beratungsgespraech.
- Schriftverkehr mit Gegenseite (Mahnung, Reklamation).
- Pruefung von Vertraegen.
- Entwurf von Schriftstuecken (Kuendigung etc.).

### Schritt 6 — Was sie NICHT abdeckt

- Klageerhebung (dafür PKH).
- Vertretung im Prozess (PKH).
- Verfahren vor Verwaltungsbehoerden in mehreren Bundeslaendern ausgeschlossen (Pruefen!).

### Schritt 7 — Uebergang zu PKH

Wenn nach Beratung klar wird: Sie muessen klagen — beantragen Sie PKH (Skill `prozesskostenhilfe-pkh-114-zpo`). Beratungshilfe und PKH sind unterschiedliche Förderungen.

### Schritt 8 — Welche Anwaelte?

Jeder Anwalt darf Beratungshilfe-Mandate annehmen — er muss aber **nicht**. Manche Anwaelte lehnen wegen niedriger Gebühren ab. Suchen Sie ggf. mehrere.

## Worauf Sie besonders achten muessen

- **Beratungshilfe vor Klage**, PKH **für Klage**. Verwechseln nicht.
- **15 EUR Schutzgebuehr** ist obligatorisch (auch für Beduerftige).
- **Beratungshilfe ist EINMAL pro Angelegenheit** — nicht beliebig oft.
- **Belege vollstaendig**: Sonst Antrag-Ablehnung.

## Typische Fehler

- "Beratungshilfe deckt Klage." → Nein, für Klage PKH.
- "Ich muss zuerst einen Anwalt nehmen." → Sie koennen auch direkt zum AG für Schein.
- "Beratungshilfe ist kostenlos." → 15 EUR Schutzgebuehr.

## Quellen und Aktualitaet

Stand: 05/2026. BerHG unveraendert.

---

## Anwendungshinweise

1. Diesen Megaprompt als Kontext in den Chat einfuegen oder als Datei hochladen.
2. Den eigentlichen juristischen Fall beschreiben.
3. Den Chat-Agent bitten, sich anhand der oben aufgefuehrten Skills zu orientieren.
4. Bei Zitaten Quellenhygiene beachten: keine Modellwissens-Halluzinationen; alle Rspr. live verifizieren.

