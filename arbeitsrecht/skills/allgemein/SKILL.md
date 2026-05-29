---
name: allgemein
description: "Einstieg, Schnelltriage und Workflow-Routing im Arbeitsrecht-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext reagiert der Skill eigenständig: ordnet das Material, prüft Eil- und Fristenhinweise, routet in passende Spezial-Skills oder stellt genau eine gezielte Rückfrage."
---

<!-- konvers-stil-v1 -->

## Konversationsstil – konzis starten, schnell zum Dokument

- **Erste Antwort kurz.** Sachverhalt einordnen, höchstens **eine** unverzichtbare Rückfrage stellen, dann arbeiten.
- **Kein Lehrbuch-Intro.** Keine Norm-Wiederholung, keine Selbstankündigung – sofort einsteigen.
- **Schnell zum Dokument.** Sobald die Mindestangaben vorliegen, liefere einen ersten Entwurf mit `[noch zu klären: …]`-Platzhaltern, statt weiter abzufragen.
- **Allgemein-Skill = Einstieg, nicht Vorlesung.** Triage, Rückfrage falls nötig, dann auf die Spezial-Skills dieses Plugins verweisen oder direkt den ersten Entwurf produzieren.
- **Ausführlich nur, wenn es das Arbeitsergebnis verlangt:** echte Subsumtion im Gutachtenstil, Tabellen, Chronologien, Risiko-/Beweislastanalysen, Schriftsatz- oder Memo-Text.
- **Erklärungen nur auf Nachfrage.** Wenn der Nutzer Hintergrund will, ausführlich. Sonst nicht.



# Arbeitsrecht — Allgemein

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Arbeitsrecht**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Spezial-Skills aus diesem Plugin vorschlagen.

**Plugin-Fokus:** Arbeitsrecht mit aktueller BAG-Rechtsprechung 2025/2026: Equal Pay Paarvergleich AGG, kein Verzicht Mindesturlaub BUrlG, Freistellungsklausel unwirksam. Individualkündigung KSchG-Klage Drei-Wochen-Frist, Aufhebungsvertrag Sperrzeit, Abmahnung, Betriebsratsanhoerung Paragraf 102 BetrVG, TzBfG.

### 0. Stummer Upload — Material ohne Begleittext

Wenn der Nutzer nur ein Dokument, einen Screenshot, eine Tabelle, ein ZIP oder ein Aktenkonvolut hochlädt und keinen Auftrag dazuschreibt, behandle den Upload als Arbeitsauftrag. Warte nicht auf einen Prompt. Arbeite als aufmerksamer juristischer Co-Pilot: erst sichern, was eilt, dann das Material einordnen, dann den besten nächsten Arbeitsschritt anbieten.

**Pflicht-Reihenfolge bei stummem Upload:**

1. **Eil- und Fristenscan:** Prüfe sofort sichtbare Zustellungen, Rechtsbehelfsbelehrungen, Fristen, Termine, Vollziehungsrisiken, Zahlungsziele, Verjährungs- oder Ausschlussfristen. Wenn etwas eilt, beginne die Antwort mit `Frist zuerst: ...`.
2. **Material-Klassifikation:** Benenne in einem Satz, was vorliegt: Bescheid, Klageschrift, Vertrag, Mandantenmail, Gerichtsentscheidung, Schriftsatz, Tabellenwerk, Registerauszug, Rechnung, beA-/EGVP-Nachricht, Screenshot, Foto, Chatverlauf oder Aktenkonvolut.
3. **Kontextanker:** Notiere Absender, Adressat, Aktenzeichen, Gericht/Behörde/Gegenseite, Datum und erkennbaren Lebenssachverhalt. Wenn der Text unleserlich ist, sage genau, welcher Teil fehlt.
4. **Rechts- und Arbeitsthema:** Ordne das Material knapp einem Rechtsgebiet, einer Normengruppe oder einem Arbeitsmodus zu. Zitiere nur, was im Material oder im Plugin-Kontext wirklich trägt.
5. **Routing:** Schlage zuerst einen passenden Spezial-Skill aus diesem Plugin vor. Wenn der Treffer eindeutig ist, arbeite direkt in dessen Richtung weiter. Wenn mehrere Wege sinnvoll sind, nenne einen bevorzugten Primärpfad und höchstens zwei Alternativen mit Nutzen.
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
- **Primärer Pfad:** konkreter Arbeitsrecht-Skill, z.B. `kueschk-frist-und-zugang-pruefen` — [warum dieser Skill hilft]
- **Alternativen:** `...`, `...`
- **Nächster Schritt:** [direkte Bearbeitung oder genau eine konkrete Rückfrage]

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
| `abmahnung-arbeitsrecht` | Arbeitgeber will Arbeitnehmer abmahnen oder Arbeitnehmer hat Abmahnung erhalten und will sie anfechten. Prüfraster Warnfunktion Ruegefunktion Dokumentationsfunktion nach BAG-Rspr. § 314 Abs. 2 BGB § 241 Abs. 2 BGB.… |
| `agg-pruefung-bewerber-und-beschaeftigte` | AGG-Prüfung bei Bewerbung und Beschäftigung: Diskriminierungsmerkmale § 1 AGG, Benachteiligungsverbot § 7 AGG, Entschädigungs- und Schadensersatzansprüche § 15 AGG, Beweislastumkehr § 22 AGG, Geltendmachungsfrist § 15… |
| `arbeitnehmer-status` | Statusfeststellung für eine geplante Beschaeftigung - Abgrenzung Arbeitnehmer/Selbständiger nach § 611a BGB, Scheinselbständigkeit, Clearingverfahren § 7a SGB IV, AUeG-Abgrenzung (Leiharbeit vs. Werkvertrag).… |
| `arbeitsrecht-anpassen` | Gezielte Anpassung des Arbeitsrechts-Praxisprofils – Standort-Fußabdruck, Risikoeinstellung, Eskalationskontakte, Einstellungsregeln, Kündigungsregeln, Handbuchpositionen oder Untersuchungseinstellungen ändern, ohne… |
| `arbeitsrecht-kaltstart-interview` | Ersteinrichtung des Arbeitsrecht-Plugins – ermittelt Standortprofil, Tarifbindung, Betriebsratssituation und Eskalationsregeln aus Personalhandbuch und Kündigungsunterlagen. Ausführen bei Neuinstallation, wenn… |
| `arbeitsrecht-mandat-arbeitsbereich` | Mandatsakten verwalten – neu anlegen, auflisten, wechseln, schließen oder vom aktiven Mandat trennen. Verhindert, dass Kontext von einem Mandat in ein anderes übergeht. Relevant für Kanzleien mit mehreren Mandanten;… |
| `aufhebungsvertrag` | Begleitet Entwurf, Prüfung und Verhandlung eines Aufhebungsvertrags. Lädt, wenn ein Arbeitsverhältnis einvernehmlich beendet werden soll – mit Fokus auf Schriftform (§ 623 BGB), Sperrzeit nach § 159 SGB III, Abfindung,… |
| `aufhebungsvertrag-sperrzeit-prognose` | Mandant hat Aufhebungsvertrag erhalten und fragt ob er Sperrzeit beim Arbeitslosengeld riskiert. Prüfraster wichtiger Grund § 159 SGB III Selbst-Kündigungsaequivalenz. Faustformel Abfindungsschutz 0.25 bis 0.5… |
| Rechtsprechung live prüfen | Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren. |
| Rechtsprechung live prüfen | Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren. |
| Rechtsprechung live prüfen | Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren. |
| `betriebsrat-anhoerung` | Prüft und dokumentiert die ordnungsgemäße Anhörung des Betriebsrats vor Kündigungen nach § 102 BetrVG. Lädt, wenn die Wirksamkeit einer BR-Anhörung (Inhalt, Fristen, Reaktion des BR) beurteilt oder ein… |
| Rechtsprechung live prüfen | Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren. |
| `betriebsrat-ladung-und-ersatzmitglieder-pruefen` | Prüfung der ordnungsgemäßen Ladung und Besetzung einer Betriebsratssitzung nach § 29 Abs. 2 BetrVG und § 25 Abs. 2 BetrVG. Wer war geladen, wer war verhindert, wer ist nachgerückt, hat das richtige Ersatzmitglied… |
| `betriebsuebergang-613a-pruefen` | Unternehmen wird verkauft oder Betrieb geht auf neuen Inhaber über und Arbeitnehmer fragen nach Rechten oder Kündigungsschutz. Prüfraster Identitätswahrung wirtschaftliche Einheit EuGH-Suezen-Kriterien § 613a BGB.… |
| `einstellungspruefung` | Prüfung von Arbeitsvertrag und Befristung bei Neueinstellungen: TzBfG (Sachgrund, Vorbeschaeftigungsverbot), AGG (diskriminierungsfreie Ausschreibung), AUeG (Abgrenzung Arbeitnehmerüberlassung), Nachweisgesetz sowie… |
| `entfristung-elektronische-signatur-vorsicht` | Elektronische Signaturen und Befristungsabreden: Scan/einfache Signatur genügen nicht; echte QES nach § 126a BGB kann genügen. Prüft DocuSign, Adobe Sign, Zertifikate, Timing und Zugang.… |
| `entfristung-grundwarnung-drei-wochen-frist` | Grundwarnung Entfristungsklage: § 17 TzBfG drei Wochen ab vereinbartem Vertragsende; absolute Ausschlussfrist; § 17 Satz 2 TzBfG i.V.m. § 7 KSchG Fiktion Wirksamkeit der Befristung bei Fristversaeumnis;… |
| `entfristung-guetetermin-und-kammertermin-sprechzettel` | Sprechzettel für Guetetermin und Kammertermin in der Entfristungsklage: Antragsstellung; Kernargumente Schriftformmangel und Sachgrundmangel; Vergleichsstrategie; Vorbereitung Zeugenvernehmung; Verhandlungsposition;… |
| `entfristung-klageschrift-anwalt-baustein` | Anwaltliche Klageschrift Entfristungsklage mit Hauptantrag und Hilfsanträgen; Weiterbeschaeftigungsantrag; strukturierte Begründung nach § 14 Abs. 4 TzBfG und Sachgrundprüfung; Beweisangebote im BAG-Zitierstil. |
| `entfristung-klageschrift-laie-baustein` | Schritt-fuer-Schritt Klageschrift Entfristungsklage für Laien: Rubrum; Feststellungsantrag Unbefristetheit; Begründungsbausteine für Schriftformmangel und fehlenden Sachgrund; Beweisangebote; Pflicht-Disclaimer. |
| `entfristung-laie-oder-anwalt-frage` | Statusabfrage Entfristungsklage: Anwalt oder Laie; bei Laie Warnungen und Empfehlung anwaltlicher Beratung; kein Mandatsverhältnis; Hinweis auf § 17 TzBfG Drei-Wochen-Frist als kritischste Ausschlussfrist. |
| `entfristung-output-warnschriftsatz-laie` | Vollständige Klageschrift Entfristungsklage mit Pflicht-Disclaimer für Laien; Zusammenführung aller Bausteine; Ausfuellanleitung; Einreichungshinweise; Dreiwochenfrist-Warnblock prominent am Anfang. |
| `entfristung-rechtsfolge-16-tzbfg-unbefristet` | Rechtsfolge unwirksamer Befristung nach § 16 Satz 1 TzBfG: Vertrag gilt als auf unbestimmte Zeit geschlossen; Möglichkeit der fruehesten ordentlichen Kündigung zum vereinbarten Ende nach § 16 Satz 2 TzBfG; Ansprüche… |
| `entfristung-sachgrund-pruefen-14-abs-1` | Sachgrundprüfung Befristung nach § 14 Abs. 1 TzBfG: acht Sachgründe; voruebergehender Bedarf; Vertretung; Erprobung; Eigenart der Leistung; haushaltsmittelbedingte Gründe; gerichtlicher Vergleich; BAG-Rechtsprechung zu… |
| `entfristung-sachgrundlos-14-abs-2-vorbeschaeftigung` | Sachgrundlose Befristung nach § 14 Abs. 2 TzBfG: zwei Jahre Gesamtdauer; dreimal verlaengerbar; Vorbeschaeftigungsverbot; BVerfG-Entscheidung 2018; BAG-Folgerechtsprechung; Karenzzeit-Diskussion; Rechtsfolge § 16 TzBfG. |
| `entfristung-sachgrundlos-14-abs-2a-neugruendung` | Sachgrundlose Befristung bei Unternehmensneugründung nach § 14 Abs. 2a TzBfG: vier Jahre Gesamtdauer; Neugründungsprivileg; Voraussetzungen der Neugründung; Abgrenzung zu blossen Unternehmensumstrukturierungen. |
| `entfristung-sachgrundlos-14-abs-3-aelter-52` | Sachgrundlose Befristung für aeltere Arbeitnehmer nach § 14 Abs. 3 TzBfG: Befristung ab 52 Jahren; Voraussetzung Vorarbeitslosigkeit oder Massnahme aktiver Arbeitsmarktpolitik; EuGH-Entscheidung zur Vereinbarkeit mit… |
| `entfristung-schriftform-14-abs-4-erkennen` | KERNSKILL: Schriftform nach § 14 Abs. 4 TzBfG für Befristungsabreden; Papieroriginal oder echte QES; Scan/einfache Signatur genügt nicht; Rechtsfolge § 16 Satz 1 TzBfG Vertrag gilt… |
| `entfristung-triage-was-will-user` | Einstieg Entfristungsklage-Workflow: Erkennung ob Nutzer Befristungskontrollklage oder Entfristungsklage anstrebt; Abgrenzung zu Kündigungsschutzklage; Überblick Prüfprogramm TzBfG; Weiterleitung zu passenden… |
| `entfristung-vergleichsverhandlung-checkliste` | Typische Vergleichsbausteine in der Entfristungsklage: Entfristungsbestätigung oder Beendigungsdatum mit Abfindung; Weiterbeschaeftigung oder Aufhebung; Zeugnis; Freistellung; Urlaubsabgeltung; Klageerledigung;… |
| `expansion-aktualisierung` | Aktualisiert den Status eines laufenden Expansionsprojekts — ermittelt, welche Punkte nun freigegeben sind, kennzeichnet überfällige Positionen und benennt die nächsten Prioritäten. Lädt, wenn seit der letzten Sitzung… |
| `expansion-auftakt` | Startet die Planung einer Neueinstellung in einem weiteren Bundesland oder einem neuen Zielland — erhebt die relevanten Eckdaten, rahmt die Entscheidung AÜG-Modell / EOR / eigene Gesellschaft, entwirft… |
| `fehlzeit-erfassen` | Neue Abwesenheit oder neuen Urlaubseintrag im Register anlegen – mit allen für die Fristenberechnung nach BUrlG, EFZG, MuSchG und BEEG notwendigen Informationen. Startet die Überwachung von Fristen ab dem ersten Tag. |
| `fehlzeiten-register` | Überprüft offene Abwesenheiten und Fristen – Urlaubsanspruch (BUrlG), Entgeltfortzahlung (EFZG), Mutterschutz (MuSchG), Elternzeit (BEEG). Zeigt nur Abwesenheiten, bei denen eine Entscheidung oder Handlung erforderlich… |
| `handbuch-aktualisierung` | Prüft eine geplante Änderung des Personalhandbuchs auf Folgewirkungen — andere betroffene Regelungen, standortspezifische Besonderheiten nach Tarifvertrag oder Betriebsvereinbarung, Mitbestimmungsrechte des… |
| `hinschg-whistleblower-antwort` | Arbeitnehmer hat einen internen Hinweis gegeben oder Unternehmen muss internen Meldekanal einrichten oder Repressalie abwehren. Prüfraster HinSchG seit 2.7.2023 Umsetzung EU-Richtlinie 2019/1937. Pflicht interner… |
| `internationale-expansion` | Referenz-Skill: Implementierungsplanungs-Framework für internationale Einstellungen — Entscheidungsrahmen AÜG-Modell/EOR vs. eigene Gesellschaft, abteilungsübergreifende Trigger für Steuer/Finance/HR, strukturierter… |
| `interne-untersuchung` | Referenz-Skill: gemeinsames Framework für arbeitsrechtliche interne Untersuchungen vom Eingang einer Beschwerde bis zum abschließenden Memo — vertrauliches Untersuchungsprotokoll, Dokumentenverarbeitung mit… |
| `kuendigungs-pruefung` | Rechtliche Prüfung einer ordentlichen oder außerordentlichen Kündigung – KSchG (allgemeiner und besonderer Kündigungsschutz), § 102 BetrVG (Betriebsratsanhörung), §§ 622 und 626 BGB (Fristen und wichtiger Grund),… |
| `kuendigungsschutzklage` | Prüft und entwirft eine Kündigungsschutzklage nach § 4 KSchG. Lädt, wenn ein Arbeitnehmer eine ordentliche oder außerordentliche Kündigung anfechten will, die 3-Wochen-Frist droht oder ein Entwurf des Klageantrags, der… |
| `kueschk-abfindung-faustformel-und-spannweite` | Abfindung Kündigungsschutzklage: Faustformel halbes Bruttomonatsgehalt pro Beschaeftigungsjahr; Spannweite von einem Viertel bis zu einem ganzen Bruttomonatsgehalt; Einflussfaktoren; steuerliche Behandlung… |
| `kueschk-allgemeiner-und-besonderer-feststellungsantrag` | Erklärung des Unterschieds zwischen dem punktuellen Feststellungsantrag nach § 4 Satz 1 KSchG und dem allgemeinen Feststellungsantrag nach § 256 ZPO als Schleppnetz-Antrag; Formulierungsvorschlaege; warum beide Anträge… |
| `kueschk-annahmeverzug-loehne-anrechnung-zwischenverdienst` | Annahmeverzugslohn nach § 615 BGB und § 11 KSchG; Anrechnung anderweitigen Verdienstes; boeswiches Unterlassen; Berechnung Nettolohnvorteil; Schadensminderungspflicht; Auswirkung auf Vergleichsdruck; steuerliche… |
| `kueschk-anwendbarkeit-kschg-pruefen` | Prüft Anwendbarkeit des Kündigungsschutzgesetzes: Wartezeit sechs Monate nach § 1 Abs. 1 KSchG; Schwellenwert zehn Arbeitnehmer nach § 23 KSchG; Berechnung von Teilzeitkraeften und Auszubildenden; allgemeiner… |
| `kueschk-aufloesungsantrag-arbeitnehmer-9-kschg` | Aufloeungsantrag des Arbeitnehmers nach § 9 KSchG: Voraussetzung der Unzumutbarkeit der Weiterbeschaeftigung; Abfindung nach § 10 KSchG; Antrag-Formulierung; Abgrenzung zu § 12 KSchG; wann sollte man diesen Antrag… |
| `kueschk-berufung-und-revision-lag-bag` | Berufung beim Landesarbeitsgericht und Revision beim BAG: Fristen je einen Monat und zwei Monate; Zulassungsgründe Revision; Kosten ab zweiter Instanz; Divergenzrevision; typische Revisionszulassungsgründe. |
| `kueschk-erwiderung-arbeitgeber-strategien-typisch` | Typische Verteidigungsstrategien des Arbeitgebers im Kündigungsschutzprozess: Hinhaltetaktik; Stricken-Anwaelte; Nachgeben-Risiko und Rückkehrpflicht; Angriffe auf Fristen und KSchG-Geltungsbereich; Beweislast-Taktik. |
| `kueschk-formfehler-pruefen` | Formfehler-Prüfung bei Kündigungen: Schriftform § 623 BGB; Vollmachtsruege § 174 BGB bei fehlender Originalvollmacht; Anhoerung Betriebsrat § 102 BetrVG; Massenentlassung §§ 17 und 18 KSchG mit Anzeigepflicht bei… |
| `kueschk-frist-und-zugang-pruefen` | Fristprüfung Kündigungsschutzklage: § 4 KSchG drei Wochen ab Zugang; § 5 KSchG nachtraegliche Klagezulassung bei unverschuldeter Versaeumung; Zugangsbeweis-Fragen; Fristberechnung nach §§ 187 und 188 BGB. |
| `kueschk-grundwarnung-falsche-wiese-und-haftung` | Pflichtkopf für jeden Kündigungsschutzklage-Schriftsatz: Hinweis auf falsche Wiese und Haftungsausschluss; zentraler Warnblock mit Drei-Wochen-Frist nach § 4 KSchG; wird in jeden Laien-Output eingefuegt. |
| `kueschk-guetetermin-strategie-und-sprechzettel` | Guetetermin nach § 54 ArbGG: Ablauf und Funktion; was sagen und was nicht sagen; Sprechzettel-Template für den Guetetermin; Vergleichsbereitschaft signalisieren ohne Positionen aufzugeben; typische Richter-Fragen. |
| `kueschk-kammertermin-sprechzettel` | Kammertermin Hauptverhandlung im Kündigungsschutzprozess: Sprechzettel mit Anträgen und Reaktionsmustern; Beweismittel-Reihenfolge; Zeugenvernehmung; Auftreten bei Urteilsverkündung; Prozessleitung durch Vorsitzenden. |
| `kueschk-klageschrift-anwalt-baustein` | Anwaltliche Klageschrift Kündigungsschutzklage: Klageschrift mit Tenor und Hilfsanträgen; Weiterbeschaeftigungsantrag; Anlagen-Checkliste; strukturierte Begründung nach KSchG-Prüfschema; Beweisangebote; BAG-Zitierstil. |
| `kueschk-klageschrift-laie-baustein` | Bauklastenartige Klageschrift für Laien: Rubrum-Vorlage; punktueller Feststellungsantrag nach § 4 KSchG; allgemeiner Feststellungsantrag; Begründungsbausteine; Beweisangebote; Schritt-fuer-Schritt zum Selbstausfuellen… |
| `kueschk-kuendigungsgrund-personen-verhalten-betrieb` | Drei Kündigungsgründe nach § 1 Abs. 2 KSchG: betriebsbedingt mit Sozialauswahl; verhaltensbedingt mit Abmahnungserfordernis; personenbedingt mit Negativprognose; Sonderkündigungsschutz als Querverweis; strukturierte… |
| `kueschk-muendliche-verhandlung-praxistipps-laie` | Praxistipps für Laien in der muendlichen Verhandlung beim Arbeitsgericht: Auftreten; Kleidung; Anrede des Gerichts; Sitzungsverlauf; Verhalten bei Vergleichsvorschlag; Stressbewaeltigung und Dokumentation. |
| `kueschk-output-warnschriftsatz-laie` | Ausgabe vollständige Klageschrift mit Pflicht-Disclaimer-Kopf für Laien; Zusammenführung aller Bausteine zu einem druckfertigen Schriftsatz; Ausfuellanleitung; Einreichungshinweise für Arbeitsgericht. |
| `kueschk-paragraph-12-kschg-neuer-job-einseitig` | § 12 KSchG einseitige Lösung nach Aufnahme eines neuen Arbeitsverhältnisses: Erklärungsfrist eine Woche nach Rechtskraft; Rechtsfolge Annahmeverzugslohn ohne Abfindung; Abgrenzung zu § 9 KSchG; Handlungsfristen und… |
| `kueschk-replik-arbeitnehmer-baustein` | Reaktion auf die Klageerwiderung des Arbeitgebers: Bestreiten von Behauptungen; Anforderungen an die Substantiierungstiefe; Replik-Baustein mit typischen Gegenargumenten; Beweismittel-Strategie für den Kammertermin. |
| `kueschk-sonderkuendigungsschutz-checkliste` | Checkliste Sonderkündigungsschutz: Schwangerschaft § 17 MuSchG; Elternzeit § 18 BEEG; Schwerbehinderung §§ 168 ff. SGB IX; Betriebsratsmitglied § 15 KSchG; Datenschutzbeauftragter; Voraussetzungen und behoerdliche… |
| `kueschk-streitwert-kostenfolge-prozesskostenhilfe` | Streitwert nach § 42 GKG drei Bruttomonatsgehaelter; § 12a ArbGG keine Kostenerstattung erste Instanz; Ausnahme Berufung; Prozesskostenhilfe §§ 114 ff. ZPO für einkommensschwache Parteien; praktische Hinweise zu… |
| `kueschk-stricken-anwalt-risiko-und-vergleichsdruck` | KERNSKILL: Warnung vor der Stricken-Strategie des Arbeitgeberanwalts; Risiko dass Arbeitgeber spaet nachgibt wenn Arbeitnehmer neuen Job hat und Rückkehrpflicht droht; Aufloeungsantrag § 9 KSchG; § 12 KSchG einseitige… |
| `kueschk-triage-laie-oder-anwalt` | KERNEINSTIEG Kündigungsschutzklage: fragt zuerst ob Anwalt oder Verbraucher-Laie; bei Laie ständige Warnungen und dringende Empfehlung anwaltlicher Beratung; kein Mandatsverhältnis; leitet zu passenden Folge-Skills;… |
| `kueschk-vergleichsverhandlung-checkliste` | Checkliste für Kündigungsschutz-Vergleiche: Beendigungsdatum; Abfindung nach Faustformel; Freistellung und Urlaubsabgeltung; Zeugnisnote und -formulierung; Klageerledigung; Outplacement; Rücklage-Klausel; alle Punkte… |
| `kueschk-weiterbeschaeftigungsantrag-grosser-senat` | Weiterbeschaeftigungsantrag nach BAG Grosser Senat 1985: Voraussetzungen des allgemeinen Weiterbeschaeftigungsanspruchs; Vor- und Nachteile aus Arbeitnehmersicht; Vollstreckung; Unterschied zum § 102 Abs. 5 BetrVG… |
| `kueschk-zeugnisanspruch-und-vergleich` | Zeugnisanspruch nach § 109 GewO: qualifiziertes Zeugnis; BAG-Mindestnote befriedigend bei fehlender Substantiierung; Formulierungsrisiken und geheime Negativsignale; typische Vergleichsformulierungen für Zeugnisse. |
| `lohn-arbeitszeit-fragen` | Standortbezogene Lohn- und Arbeitszeitfragen – ArbZG (Höchstarbeitszeit, Pausen, Ruhezeiten, Aufzeichnungspflichten), MiLoG (Mindestlohn, Aufzeichnungspflicht), EFZG (Entgeltfortzahlung im Krankheitsfall),… |
| `lohnsteuer-sozialversicherung` | Beurteilt den sozialversicherungsrechtlichen Status (Scheinselbständigkeit, § 7a SGB IV) und lohnsteuerliche Fragen im Arbeitsverhältnis. Lädt, wenn ein Statusfeststellungsverfahren, Scheinselbständigkeit,… |
| `mandat-triage-arbeitsrecht` | Eingangs-Abfrage für arbeitsrechtliche Mandate — Mandant fragt nach Kündigung Aufhebungsvertrag Abmahnung Lohn Urlaub Befristung Betriebsuebergang Diskriminierung oder Betriebsrats-Streit. Klaert Mandantenrolle… |
| `massenentlassung-17-kschg` | Arbeitgeber plant Entlassung mehrerer Arbeitnehmer und fragt ob Massenentlassungsanzeige erforderlich ist oder Gewerkschaft und Betriebsrat anfechten. Prüfraster § 17 KSchG Schwellenwerte abhaengig von Betriebsgroesse.… |
| Rechtsprechung live prüfen | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| `richtlinien-entwurf` | Entwirft eine betriebliche Regelung (Richtlinie, Betriebsordnung, Policy) mit standortspezifischen Ergänzungen, wo das Recht oder Tarifverträge abweichende Regeln erfordern. Prüft Mitbestimmungsrechte des Betriebsrats… |
| `untersuchung-abfrage` | Beantwortet Fragen gegen ein laufendes Untersuchungsprotokoll — was Zeugen gesagt haben, wo Schilderungen im Widerspruch stehen, welche Lücken bestehen, was die stärksten Belege zu jeder Frage sind. Lädt, wenn der… |
| `untersuchung-ergaenzen` | Fügt einer laufenden internen Untersuchung neue Daten hinzu — Dokumente, Befragungsnotizen oder Beobachtungen. Verarbeitet Dokumentenpakete anhand dokumentierter Auswahlkriterien, markiert relevante Funde und… |
| `untersuchung-eroeffnen` | Eröffnet eine neue interne Untersuchungssache — führt die Sachverhaltserfassung durch, generiert die Quellencheckliste und legt das persistente Untersuchungsprotokoll an. Lädt, wenn eine Beschwerde oder ein Hinweis… |
| `untersuchungs-memo` | Entwirft den vertraulichen Untersuchungsvermerk aus dem Untersuchungsprotokoll oder aktualisiert einen bestehenden Entwurf, wenn neue Daten hinzugekommen sind. Lädt, wenn eine Untersuchung weit genug fortgeschritten… |
| `untersuchungs-zusammenfassung` | Entwirft eine zielgruppengerechte Zusammenfassung aus dem vertraulichen Untersuchungsvermerk — für HR, Geschäftsführung/Aufsichtsrat oder externe Bevollmächtigte. Lädt, wenn ein Untersuchungsvermerk für eine Zielgruppe… |

## Worum geht es?

Das Arbeitsrecht-Plugin deckt das gesamte Individual- und Kollektivarbeitsrecht fuer Arbeitgeber und Arbeitnehmer ab: Kuendigungsschutzklage (KSchG), Entfristungsklage (TzBfG), Aufhebungsvertrag, Abmahnung, Betriebsratsanhoerung (§ 102 BetrVG), Betriebsuebergang (§ 613a BGB), Massenentlassung (§ 17 KSchG), AGG-Pruefung, HinSchG-Whistleblower, Mindestlohn, Arbeitszeiterfassung sowie interne Untersuchungen und internationale Expansion. Aktuelle BAG-Rechtsprechung 2025/2026 ist eingearbeitet (Equal Pay, Mindesturlaub-Verzicht, Freistellungsklausel).

Das Plugin richtet sich an Kanzleien und Syndikusrechtsanwaelte, die sowohl Arbeitgeber- als auch Arbeitnehmer-Mandate betreuen.

## Wann brauchen Sie diese Skill?

- Ein Mandant hat eine Kuendigung erhalten oder will eine Kuendigung aussprechen und es ist sofort die Drei-Wochen-Frist des § 4 KSchG zu sichern.
- Ein befristetes Arbeitsverhaeltnis laeuft aus und die Befristung soll angegriffen werden (§ 17 TzBfG: Drei-Wochen-Frist gilt ebenso).
- Ein Aufhebungsvertrag ist vorhanden und Sperrzeit-Risiko sowie steuerliche Behandlung der Abfindung sollen geklaert werden.
- Ein Betriebsrat soll angehoert werden oder hat einen Widerspruch eingelegt (§ 102 BetrVG).
- Ein Mitarbeiter hat einen Hinweis auf Missstande gemeldet und der HinSchG-Schutz soll beurteilt werden.

## Fachbegriffe (kurz erklaert)

- **KSchG** — Kuendigungsschutzgesetz; schutzt Arbeitnehmer mit mehr als sechs Monaten Betriebszugehoerigkeit in Betrieben mit mehr als zehn Arbeitnehmern.
- **TzBfG** — Teilzeit- und Befristungsgesetz; regelt sachgrundgebundene und sachgrundlose Befristungen; Schriftformzwang nach § 14 Abs. 4 TzBfG.
- **Sozialauswahl** — Pflicht des Arbeitgebers bei betriebsbedingter Kuendigung, die schutzwuerdigsten Arbeitnehmer zu erhalten (§ 1 Abs. 3 KSchG).
- **Sperrzeit** — vorueberstgehende Verweigerung des Arbeitslosengelds nach § 159 SGB III bei Selbstkuendigung oder Aufhebungsvertrag.
- **Betriebsrat** — gewaehltes Arbeitnehmer-Gremium; bei Kuendigung ist Anhoerung nach § 102 BetrVG Wirksamkeitsvoraussetzung.
- **Betriebsuebergang** — Uebergang eines Betriebs oder Betriebsteils auf einen neuen Inhaber (§ 613a BGB); Kuendigungsverbot wegen Betriebsuebergangs.
- **AGG** — Allgemeines Gleichbehandlungsgesetz; verbietet Diskriminierung nach § 1 AGG; Entschaedigungs- und Schadensersatz nach § 15 AGG.

## Rechtsgrundlagen

- §§ 1 ff. KSchG — Kuendigungsschutz; § 4 KSchG Drei-Wochen-Frist
- §§ 14 ff. TzBfG — Befristungsrecht; § 17 TzBfG Drei-Wochen-Frist; § 14 Abs. 4 TzBfG Schriftformzwang
- § 102 BetrVG — Betriebsratsanhoerung vor Kuendigung
- § 613a BGB — Betriebsuebergang
- § 622 BGB — Kuendigungsfristen
- § 626 BGB — Ausserordentliche Kuendigung aus wichtigem Grund
- § 623 BGB — Schriftformzwang fuer Kuendigung und Aufhebungsvertrag
- §§ 1 ff. AGG — Diskriminierungsschutz
- § 1 MiLoG — Mindestlohn
- HinSchG — Hinweisgeberschutzgesetz seit 02.07.2023
- § 17 KSchG — Massenentlassung; Konsultation und Anzeige

## Schritt-fuer-Schritt: Einstieg ins Plugin

1. Mandantenkonstellation klaeren: Arbeitnehmer, Arbeitgeber, Betriebsrat, Geschaeftsfuehrer oder Syndikus?
2. Phase des Mandats bestimmen: Noch keine Kuendigung (praeventiv), Kuendigung ausgesprochen/erhalten (Fristensicherung), laufendes Verfahren oder Abschluss?
3. Passenden Skill auswaehlen (siehe Skill-Tour unten).
4. Eilfristen pruefen: § 4 KSchG drei Wochen ab Zugang der Kuendigung; § 17 TzBfG drei Wochen ab vereinbartem Vertragsende — beide absolute Ausschlussfristen.
5. Anschluss-Skill bestimmen: Nach Triage zu Kuendigungsschutzklage-Skills, Entfristungsklage-Skills oder Aufhebungsvertrag.

## Skill-Tour (was gibt es hier?)

**Einrichtung und Mandatsverwaltung**
- `arbeitsrecht-kaltstart-interview` — Ersteinrichtung: Standortprofil, Tarifbindung, Betriebsratssituation und Eskalationsregeln hinterlegen.
- `arbeitsrecht-anpassen` — Praxisprofil nachjustieren ohne vollstaendiges Erstinterview.
- `arbeitsrecht-mandat-arbeitsbereich` — Mandatsakten verwalten: anlegen, wechseln, schliessen.
- `mandat-triage-arbeitsrecht` — Eingangs-Abfrage: Kuendigung, Aufhebungsvertrag, Abmahnung, Lohn, Befristung oder Betriebsrat? Sofort-Fristen-Check.

**Kuendigungsschutzklage (kueschk-)**
- `kueschk-triage-laie-oder-anwalt` — Kerneinstieg: Anwalt oder Laie? Dringende Empfehlung und Routing.
- `kuendigungs-pruefung` — Rechtliche Pruefung einer ordentlichen oder ausserordentlichen Kuendigung.
- `kuendigungsschutzklage` — Entwurf der Kuendigungsschutzklage nach § 4 KSchG.
- `kueschk-anwendbarkeit-kschg-pruefen` — Wartezeit (sechs Monate) und Schwellenwert (zehn Arbeitnehmer) pruefen.
- `kueschk-frist-und-zugang-pruefen` — § 4 KSchG Fristberechnung und Zugangsbeweis.
- `kueschk-formfehler-pruefen` — Schriftform, Vollmachtsruege § 174 BGB, Betriebsratsanhoerung.
- `kueschk-kuendigungsgrund-personen-verhalten-betrieb` — Drei Kuendigungsgruende nach § 1 Abs. 2 KSchG pruefen.
- `kueschk-sonderkuendigungsschutz-checkliste` — Schwangerschaft, Elternzeit, Schwerbehinderung, BR-Mitglied.
- `kueschk-klageschrift-anwalt-baustein` — Anwaltliche Klageschrift mit Hilfsantraegen und Beweisangeboten.
- `kueschk-klageschrift-laie-baustein` — Klageschrift-Baustein fuer Laien mit Warnkopf.
- `kueschk-output-warnschriftsatz-laie` — Vollstaendige Laien-Klageschrift mit Pflicht-Disclaimer.
- `kueschk-grundwarnung-falsche-wiese-und-haftung` — Pflichtkopf mit Drei-Wochen-Frist-Hinweis fuer Laien-Output.
- `kueschk-allgemeiner-und-besonderer-feststellungsantrag` — Unterschied punktueller und allgemeiner Feststellungsantrag.
- `kueschk-guetetermin-strategie-und-sprechzettel` — Guetetermin nach § 54 ArbGG: Ablauf und Strategie.
- `kueschk-kammertermin-sprechzettel` — Sprechzettel fuer Hauptverhandlung im Kuendigungsschutzprozess.
- `kueschk-muendliche-verhandlung-praxistipps-laie` — Praxistipps fuer Laien in der muendlichen Verhandlung.
- `kueschk-erwiderung-arbeitgeber-strategien-typisch` — Typische Verteidigungsstrategien des Arbeitgebers.
- `kueschk-replik-arbeitnehmer-baustein` — Reaktion auf Klageerwiderung des Arbeitgebers.
- `kueschk-annahmeverzug-loehne-anrechnung-zwischenverdienst` — Annahmeverzugslohn § 615 BGB und Zwischenverdienst-Anrechnung.
- `kueschk-weiterbeschaeftigungsantrag-grosser-senat` — Weiterbeschaeftigungsantrag nach BAG Grosser Senat 1985.
- `kueschk-aufloesungsantrag-arbeitnehmer-9-kschg` — Aufloeungsantrag § 9 KSchG bei Unzumutbarkeit.
- `kueschk-paragraph-12-kschg-neuer-job-einseitig` — § 12 KSchG einseitige Loesung nach neuem Arbeitsverhaeltnis.
- `kueschk-stricken-anwalt-risiko-und-vergleichsdruck` — Warnung vor Stricken-Strategie des Arbeitgeberanwalts.
- `kueschk-abfindung-faustformel-und-spannweite` — Abfindungs-Faustformel und steuerliche Fuenftel-Regelung.
- `kueschk-vergleichsverhandlung-checkliste` — Vergleichs-Checkliste: Abfindung, Freistellung, Zeugnis, Erledigungsklausel.
- `kueschk-zeugnisanspruch-und-vergleich` — Zeugnisanspruch § 109 GewO und Vergleichsformulierungen.
- `kueschk-streitwert-kostenfolge-prozesskostenhilfe` — Streitwert § 42 GKG, § 12a ArbGG, Prozesskostenhilfe.
- `kueschk-berufung-und-revision-lag-bag` — Berufung beim LAG und Revision beim BAG.

**Entfristungsklage (entfristung-)**
- `entfristung-triage-was-will-user` — Einstieg: Befristungskontrollklage oder Entfristungsklage?
- `entfristung-laie-oder-anwalt-frage` — Statusabfrage Anwalt oder Laie fuer Entfristungsklage.
- `entfristung-schriftform-14-abs-4-erkennen` — KERNSKILL: Schriftformmangel nach § 14 Abs. 4 TzBfG als Unwirksamkeitsgrund.
- `entfristung-elektronische-signatur-vorsicht` — Scan/einfache Signatur von echter QES trennen; Rechtsfolge bei Formmangel Unbefristetheit.
- `entfristung-grundwarnung-drei-wochen-frist` — § 17 TzBfG absolute Ausschlussfrist drei Wochen.
- `entfristung-sachgrund-pruefen-14-abs-1` — Acht Sachgruende nach § 14 Abs. 1 TzBfG pruefen.
- `entfristung-sachgrundlos-14-abs-2-vorbeschaeftigung` — Sachgrundlose Befristung und Vorbeschaeftigungsverbot.
- `entfristung-sachgrundlos-14-abs-2a-neugruendung` — Neugründungsprivileg § 14 Abs. 2a TzBfG.
- `entfristung-sachgrundlos-14-abs-3-aelter-52` — Befristung aelterer Arbeitnehmer nach § 14 Abs. 3 TzBfG.
- `entfristung-rechtsfolge-16-tzbfg-unbefristet` — Rechtsfolge unwirksamer Befristung nach § 16 TzBfG.
- `entfristung-klageschrift-anwalt-baustein` — Anwaltliche Entfristungs-Klageschrift.
- `entfristung-klageschrift-laie-baustein` — Entfristungs-Klageschrift fuer Laien Schritt fuer Schritt.
- `entfristung-output-warnschriftsatz-laie` — Vollstaendige Laien-Entfristungs-Klageschrift mit Disclaimer.
- `entfristung-guetetermin-und-kammertermin-sprechzettel` — Sprechzettel fuer Guete- und Kammertermin in der Entfristungsklage.
- `entfristung-vergleichsverhandlung-checkliste` — Vergleichsbausteine in der Entfristungsklage.

**Aufhebungsvertrag und Abmahnung**
- `aufhebungsvertrag` — Entwurf, Pruefung und Verhandlung eines Aufhebungsvertrags.
- `aufhebungsvertrag-sperrzeit-prognose` — Sperrzeit-Risiko beim Aufhebungsvertrag nach § 159 SGB III.
- `abmahnung-arbeitsrecht` — Abmahnungsschreiben oder Gegendarstellung und Widerspruchsschreiben.

**Betriebsrat und kollektives Arbeitsrecht**
- `betriebsrat-anhoerung` — Betriebsratsanhoerung nach § 102 BetrVG: Inhalt, Fristen, Reaktion.
- `betriebsrat-beschluss-heilung-nachtraeglich` — Heilung unwirksamer Betriebsratsbeschluesse; BAG 25.09.2024.
- `betriebsrat-ladung-und-ersatzmitglieder-pruefen` — Ordnungsgemaesse Ladung und Nachrückreihenfolge pruefen.
- `massenentlassung-17-kschg` — Massenentlassungsanzeige und Konsultation Betriebsrat nach § 17 KSchG.

**Status, Expansion und Einstellungspruefung**
- `arbeitnehmer-status` — Statusfeststellung Arbeitnehmer vs. Selbstaendiger, § 611a BGB, Clearingverfahren.
- `einstellungspruefung` — Arbeitsvertrag, Befristung, AGG und Nachweisgesetz bei Neueinstellungen.
- `expansion-auftakt` — Planung einer Neueinstellung in neuem Bundesland oder Zielland.
- `expansion-aktualisierung` — Status eines laufenden Expansionsprojekts aktualisieren.
- `internationale-expansion` — Framework fuer internationale Einstellungen (AUeG-Modell/EOR/Gesellschaft).

**Lohn, Arbeitszeit und sonstige Themen**
- `lohn-arbeitszeit-fragen` — ArbZG, MiLoG, EFZG, Tarifvertraege: standortbezogene Lohn- und Arbeitszeitfragen.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- `lohnsteuer-sozialversicherung` — Sozialversicherungsrechtlicher Status und lohnsteuerliche Fragen.
- `fehlzeit-erfassen` — Neue Abwesenheit im Register anlegen: BUrlG, EFZG, MuSchG, BEEG.
- `fehlzeiten-register` — Offene Abwesenheiten und Fristen ueberpruefen.
- `agg-pruefung-bewerber-und-beschaeftigte` — AGG: Diskriminierungsmerkmale, Benachteiligungsverbot, Geltendmachungsfrist.
- `betriebsuebergang-613a-pruefen` — Betriebsuebergang: Identitaetswahrung, Widerspruchsrecht, Kuendigungsverbot.
- `hinschg-whistleblower-antwort` — HinSchG: interner Meldekanal, Repressalienverbot, Bussgelder.

**Handbuch, Richtlinien und Untersuchungen**
- `richtlinien-entwurf` — Betriebliche Richtlinie mit standortspezifischen Ergaenzungen entwerfen.
- `handbuch-aktualisierung` — Personalhandbuch auf Folgewirkungen und Mitbestimmungsrechte pruefen.
- `untersuchung-eroeffnen` — Neue interne Untersuchungssache eroeffnen und Protokoll anlegen.
- `untersuchung-ergaenzen` — Laufende Untersuchung mit neuen Daten und Dokumenten erganzen.
- `untersuchung-abfrage` — Fragen gegen das laufende Untersuchungsprotokoll stellen.
- `untersuchungs-memo` — Vertraulichen Untersuchungsvermerk entwerfen.
- `untersuchungs-zusammenfassung` — Zielgruppengerechte Zusammenfassung des Untersuchungsvermerks.
- `interne-untersuchung` — Referenz-Skill fuer das gesamte Untersuchungs-Framework (nicht direkt aufzurufen).

**Aktuelle BAG-Rechtsprechung 2025/2026**
- `bag-equal-pay-paarvergleich-8azr30024` — BAG 23.10.2025: Equal Pay durch Paarvergleich; ein maennlicher Kollege genuegt.
- `bag-freistellungsklausel-unwirksam-5azr10825` — BAG 25.03.2026: pauschale Freistellungsklausel nach Kuendigung unwirksam.
- `bag-mindesturlaub-kein-verzicht-9azr10424` — BAG 03.06.2025: kein Verzicht auf gesetzlichen Mindesturlaub.

## Worauf besonders achten

- **Drei-Wochen-Fristen sind absolute Ausschlussfristen**: § 4 KSchG und § 17 TzBfG dulden keine Versaeumnisse; nachtraegliche Klagezulassung nach § 5 KSchG nur bei unverschuldeter Fristversaeumung.
- **Formzwang bei Kuendigung, Aufhebung und Befristung**: § 623 BGB (Kuendigung/Aufhebungsvertrag) schliesst elektronische Form aus; § 14 Abs. 4 TzBfG verlangt Schriftform, die bei echter QES nach § 126a BGB ersetzt werden kann. Scan/einfache Signatur genügt nicht.
- **Betriebsratsanhoerung vor der Kuendigung**: Eine inhaltlich unvollstaendige Anhoerung macht die Kuendigung unwirksam; BAG-Anforderungen an Mitteilung von Kuendigungsgrund und Sozialdaten.
- **Equal Pay Paarvergleich (BAG 23.10.2025)**: Ein einziger besser bezahlter maennlicher Kollege bei gleicher Arbeit begründet bereits die Vermutung des § 22 AGG; Median-Argumente sind nicht mehr ausreichend.
- **Sperrzeit-Risiko beim Aufhebungsvertrag**: Ohne ausdruecklichen wichtigen Grund im Sinne von § 159 SGB III droht eine 12-woechige Sperrzeit; Abfindungs-Faustformel (0.25 bis 0.5 Bruttogehalt pro Jahr) als Schutz.

## Typische Fehler

- Klagefrist § 4 KSchG als Drei-Wochen-Bitte missverstanden: Die Frist laeuft ab Zugang der Kuendigung, nicht ab Erhalt eines Briefes, und ist strikt.
- Betriebsratsanhoerung nach Ausspruch der Kuendigung nachgeholt: Die Anhoerung muss vor der Kuendigung abgeschlossen sein; nachtraegliche Heilung ist ausgeschlossen.
- Aufhebungsvertrag ohne Schriftformkontrolle: § 623 BGB verlangt Schriftform und schliesst elektronische Form aus; muendlich, per E-Mail oder per QES geschlossene Aufhebungsvertraege sind nichtig.
- AGG-Fristen versaeumt: Entschaedigungsanspruch nach § 15 Abs. 4 AGG verfaellt in zwei Monaten ab Benachteiligung; Frist wird selten beachtet.
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Querverweise

- `arbeitszeugnis-analyse` — Wenn im Rahmen von Kuendigungsschutz oder Aufhebungsvertrag auch ein Zeugnis vereinbart wird.
- `prozessrecht` — Fuer allgemeine prozessrechtliche Fragen, die sich im Arbeitsgerichtsprozess ergeben.
- `krisenfrueherkennung-starug` — Wenn Massenentlassungen im Kontext einer Unternehmensrestrukturierung stattfinden.
- `schriftform-und-textform-bgb` — Fuer Schriftform-Details bei Kuendigung, Befristungsabrede und Aufhebungsvertrag.

## Quellen und Aktualitaet

- Stand: 05/2026
- KSchG, TzBfG, BetrVG, BUrlG, EFZG, MuSchG, BEEG, SGB III, AGG, HinSchG in geltender Fassung
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Mindestlohn: 12.82 EUR ab 01.01.2025; 13.90 EUR ab 01.01.2026
