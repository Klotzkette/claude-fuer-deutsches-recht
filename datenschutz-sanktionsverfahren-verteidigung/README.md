# Datenschutz-Sanktionsverfahren und Verteidigung

<!-- BEGIN plugin-sofort-download-section (autogen) -->

<!-- BEGIN megaprompt-und-vorlagen (autogen) -->
## Experimentell: dieses Plugin auch ohne Claude Code

### Megaprompt (alle Kern-Skills in einer Datei)

Das Plugin gibt es zusaetzlich als **single-file Megaprompt** — ein experimentelles Markdown, das die wichtigsten Skills in einer einzigen Datei buendelt. Drop das in einen Chat ohne Claude-Code-Integration; der Agent erhaelt damit die gebuendelten Skill-Anweisungen.

- **Direkt-Download**: [`datenschutz-sanktionsverfahren-verteidigung.md`](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/testakten/megaprompts/datenschutz-sanktionsverfahren-verteidigung.md) (63 KB)
- Im Repo: [`testakten/megaprompts/datenschutz-sanktionsverfahren-verteidigung.md`](../testakten/megaprompts/datenschutz-sanktionsverfahren-verteidigung.md)

*Keine Haftung, keine Gewaehr — Megaprompts sind eine Best-Effort-Kompression, kein vollwertiger Plugin-Ersatz.*

<!-- END megaprompt-und-vorlagen (autogen) -->

## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`datenschutz-sanktionsverfahren-verteidigung`) | [`datenschutz-sanktionsverfahren-verteidigung.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/datenschutz-sanktionsverfahren-verteidigung.zip) |

Dieses Plugin hat (bewusst) keine eigene Demonstrations-Akte.

<!-- END plugin-sofort-download-section (autogen) -->

Dieses Plugin ist die Spezialwerkstatt für Mandate, in denen Datenschutzaufsicht nicht mehr nur Beratung ist, sondern Druck macht: Anhörung, Auskunftsverlangen, Art.-58-Anordnung, Bußgeldbescheid, Einspruch, Hauptverhandlung, Rechtsbeschwerde, Verwaltungsgericht und EuGH-Frage. Es ergänzt `datenschutzrecht`, ist aber bewusst eigenständig, weil solche Verfahren prozessual anders funktionieren als AVV, DSFA oder Datenschutzerklärung.

## Wofür es gedacht ist

- Verteidigung gegen DSGVO-Geldbußen nach Art. 83 DSGVO.
- Vertretung im OWiG-Verfahren nach § 41 BDSG, einschließlich Akteneinsicht, Einspruch, Zwischenverfahren, gerichtlicher Hauptverhandlung, Beschlussverfahren und Rechtsbeschwerde.
- Abwehr oder Verhandlung von Aufsichtsmaßnahmen nach Art. 58 Abs. 2 DSGVO: Verwarnung, Anordnung, Löschung, Verarbeitungsstopp, Drittlandtransfer-Stopp, Zwangsmittel und Veröffentlichungsrisiken.
- Verwaltungsgerichtlicher Rechtsschutz nach Art. 78 DSGVO und § 20 BDSG, wenn es nicht um die Geldbuße selbst geht.
- Koordination mit Datenpanne, Art.-82-Schadensersatz, Strafrecht, Geschäftsführung, D&O, Presse und internationalem One-Stop-Shop.

## Der wichtigste erste Satz im Mandat

Nicht sofort "kooperativ" alles erzählen. Erst verstehen, welche Spur läuft. Datenschutzrechtliche Mitwirkung, OWiG-Verteidigung und verwaltungsgerichtlicher Rechtsschutz haben unterschiedliche Regeln. Das Plugin fragt deshalb zuerst:

1. Liegt nur ein Auskunftsverlangen, eine Anhörung, ein Bußgeldbescheid oder eine Art.-58-Anordnung vor?
2. Wer ist Adressat und welche Behörde ist zuständig: Landesaufsicht, BfDI, kirchliche Datenschutzaufsicht oder federführende EU-Aufsicht?
3. Welche Frist läuft und wie wurde zugestellt?
4. Geht es um Geldbuße, Maßnahme, beides oder Folgerisiken?
5. Was ist belegt und was behauptet die Behörde nur?

## Zwei Hauptspuren

| Spur | Typischer Rechtsweg | Typische Arbeit |
| --- | --- | --- |
| **Bußgeld** | Art. 83 DSGVO, § 41 BDSG, OWiG/StPO sinngemäß; Einspruch nach § 67 OWiG; Zuständigkeit nach § 68 OWiG, modifiziert durch § 41 BDSG | Anhörung, Akteneinsicht, Bußgeldbescheid, Einspruch, Zwischenverfahren, Hauptverhandlung, Beschlussverfahren, Rechtsbeschwerde |
| **Aufsichtsmaßnahme** | Art. 58/78 DSGVO, § 20 BDSG, VwGO | Anordnung prüfen, Bestimmtheit/Ermessen/Verhältnismäßigkeit, Anfechtungsklage, Eilrechtsschutz, Umsetzung/Verhandlung |

## Leitentscheidungen und Stand

Stand: Juni 2026. Besonders wichtig sind EuGH, Urteil vom 05.12.2023, C-807/21 (Deutsche Wohnen), und EuGH, Urteil vom 05.12.2023, C-683/21 (Nacionalinis visuomenės sveikatos centras). Die Linie ist: Ein Unternehmen kann unmittelbar Adressat einer DSGVO-Geldbuße sein; die Aufsicht muss nicht zuerst eine natürliche Person identifizieren. Zugleich bleibt Vorsatz oder Fahrlässigkeit erforderlich. Das Plugin behandelt diese Linie als Prüfprogramm, nicht als Freibrief für schematische Unternehmenshaftung.

## Quellenhygiene

Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate. Normen und Rechtsprechung werden vor Ausgabe mit amtlichen oder frei zugänglichen Quellen geprüft, insbesondere:

- DSGVO über EUR-Lex.
- BDSG und OWiG über gesetze-im-internet.de.
- EuGH über CURIA/EUR-Lex.
- EDPB Guidelines 04/2022 über edpb.europa.eu.
- Deutsche Gerichtsentscheidungen nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und freier/amtlicher Quelle.

## Typische Outputs

- Behördenpost-Analyse: Was ist das, was droht, welche Frist läuft?
- Akteneinsichtsantrag und fristwahrender Einspruch.
- Stellungnahme vor Bußgeldbescheid.
- Art.-83-Bemessungsgegenrechnung nach EDPB 04/2022.
- Verschuldens- und Organisationsmemo nach EuGH C-807/21/C-683/21.
- Klage-/Eilantragsgerüst gegen Art.-58-Anordnung.
- Terminsmappe für Hauptverhandlung im Bußgeldverfahren.
- Management-Briefing für Vorstand/Geschäftsführung.
- Schlussmemo mit Remediation, Wiedervorlagen und Lessons Learned.

## Gute Startbefehle

```text
/datenschutz-sanktionsverfahren-verteidigung:kaltstart-verfahrensstand-und-mandatsziel
/datenschutz-sanktionsverfahren-verteidigung:bescheid-oder-anhoerung-richtig-lesen
/datenschutz-sanktionsverfahren-verteidigung:akteneinsicht-49-owig-147-stpo
/datenschutz-sanktionsverfahren-verteidigung:zustaendigkeit-amtsgericht-landgericht-41-bdsg
/datenschutz-sanktionsverfahren-verteidigung:art-58-anordnung-verwaltungsakt
/datenschutz-sanktionsverfahren-verteidigung:edpb-04-2022-bemessungsmethodik
```

## Skill-Logik

Die 100 Skills sind nicht als lose Liste gedacht, sondern als Verteidigungsmaschine: Kaltstart, Behördenvorfeld, Bußgeld/OWiG, Art.-83-Bemessung, Verwaltungsgericht, EU-One-Stop-Shop, Beweise/Forensik und Output. Jeder Skill soll die Mandantin handlungsfähiger machen und nicht bloß Normen aufsagen.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 100 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `akteneinsicht-49-owig-147-stpo` | Akteneinsicht § 49 OWiG und § 147 StPO: Behördenakte, Beschwerden, technische Anlagen, Bemessungsunterlagen und interne Vermerke auswerten: Akteneinsicht § 49 OWiG und § 147 StPO: Behördenakte, Beschwerden, technische Anlagen, Bemessungs... |
| `anhoerung-55-owig` | Anhörung nach § 55 OWiG: Reaktion auf Anhörung vorbereiten, Aussagefreiheit wahren und Akteneinsicht anstoßen: Normanker: DSGVO Art. 58 und 77-84;... |
| `anwesenheit-73-owig-vertretung` | Anwesenheit und Entbindung § 73 OWiG: Erscheinenspflicht, Entbindung und Vertretung von Unternehmen und Organen im Termin steuern: Anwesenheit und Entbindung § 73 OWiG: Erscheinenspflicht, Entbindung und Vertretung von Unternehmen und Or... |
| `arbeitnehmerdaten-und-betriebsrat-im-sanktionsverfahren` | Beschäftigtendaten und Betriebsrat: HR-Systeme, Monitoring, Betriebsrat, § 26 BDSG und Beschäftigteneinwilligung verteidigen: Norma... |
| `art-58-anordnung-verwaltungsakt` | Art.-58-Anordnung als Verwaltungsakt: Anordnung, Verwarnung, Verbot, Löschung und Transferstopp als verwaltungsgerichtliche Streitigkeit prüfen: Art.-58-Anordnung als Verwaltungsakt: Anordnung, Verwarnung, Verbot, Löschung und Transferst... |
| `art-78-rechtsschutz-und-betroffenenbeschwerde` | Art. 78 Rechtsschutz: Effektiven Rechtsschutz gegen Aufsichtsentscheidungen und Untätigkeit aus Sicht von Verantwortlichen oder Betroffenen ordnen. Normanker: DSGVO Art. 58 und 77-84; BDSG § 41; OWiG §§ 46 und 55 und 66-72; StPO über §... |
| `art-83-abs-2-kriterien-einzeln` | Art. 83 Abs. 2 Kriterien einzeln prüfen: Alle Bußgeldkriterien einzeln mit Tatsachen, Entlastung und Gegenrechnung bearbeiten. Normanker: DSGVO Art. 58 und 77-84; BDSG § 41; OWiG §§ 46 und 55 und 66-72; StPO über § 4... |
| `aufsicht-in-regulierten-branchen` | Regulierte Branchen Bank Gesundheit Energie: Datenschutzaufsicht mit BaFin, Krankenhausaufsicht, BNetzA, BSI und Sozialdatenschutz koordinieren: Regulierte Branchen Bank Gesundheit Energie: Datenschutzaufsicht mit BaFin, Krankenhausaufsi... |
| `aufsichtliche-anordnung-plus-bussgeld-doppelspur` | Anordnung plus Bußgeld Doppelspur: Verwaltungsgerichtliche und OWiG-Verteidigung bei gleicher Tatsachengrundlage widerspruchsfrei koordinieren: Anordnung plus Bußgeld Doppelspur: Verwaltungsgerichtliche und OWiG-Verteidigung bei gleicher... |
| `aufsichtsbehoerden-antwortschreiben` | Antwortschreiben an Aufsichtsbehörde: Behördenschreiben präzise, beweisgestützt, nicht überschießend und mit klaren Vorbehalten formulieren: Antwortschreiben an Aufsichtsbehörde: Behördenschreiben präzise, beweisgestützt, nicht überschie... |
| `aufsichtsbehoerden-auskunftsverlangen-art-58-1` | Auskunftsverlangen Art: 58 Abs. 1 DSGVO beantworten: Auskunfts-, Vorlage- und Prüfverlangen beantworten, ohne spätere Bußgeldverteidigung zu beschädigen. Normanker: DSGVO Art. 58 und 77-84; BDSG § 41; OWiG §§ 46 und 55 und 66-72; StP... |
| `auslaendische-mutter-und-deutsche-tochter` | Ausländische Mutter und deutsche Tochter: Adressat, Zustellung, Verantwortlicher, Niederlassung, Konzernumsatz und wirtschaftliche Einheit in Auslandsfällen prüfen: Ausländische Mutter und deutsche Tochter: Adressat, Zustellung, Verantwo... |
| `behoerdenkommunikation-reputationsschutz` | Behördenkommunikation mit Reputationsschutz: Ton, Timing, Presse, Veröffentlichung, Kundenkommunikation und Verteidigungsrechte koordinieren: Behördenkommunikation mit Reputationsschutz: Ton, Timing, Presse, Veröffentlichung, Kundenkommu... |
| `behoerdenstrategie-kooperation-oder-schweigen` | Kooperation oder Schweigen strategisch wählen: Kooperationsnutzen, Art.-83-Milderung, Aussagefreiheit, Scope-Erweiterung und Folgeklagen abwägen: Kooperation oder Schweigen strategisch wählen: Kooperationsnutzen, Art.-83-Milderung, Aussa... |
| `behoerdenuntaetigkeit-und-beschwerdegegner` | Behördenuntätigkeit und Beschwerdegegner: Untätigkeit der Aufsicht und Rechte des Beschwerdegegners im Art.-77/78-Kontext bearbeiten: Behördenuntätigkeit und Beschwerdegegner: Untätigkeit der Aufsicht und Rechte des Beschwerdegegners im... |
| `behoerdenvergleich-erledigung-und-auflagen` | Erledigung mit der Aufsicht verhandeln: Informelle Erledigung, Verwarnung, Auflage, reduzierte Geldbuße oder Rücknahme rechtlich sauber verhandeln: Erledigung mit der Aufsicht verhandeln: Informelle Erledigung, Verwarnung, Auflage, reduz... |
| `bescheid-oder-anhoerung-richtig-lesen` | Behördenpost richtig lesen: Auskunftsverlangen, Beschwerdeweiterleitung, Anhörung, Verwarnung, Anordnung, Zwangsgeldandrohung und Bußgeldbescheid voneinander unterscheiden: Behördenpost richtig lesen: Auskunftsverlangen, Beschwerdeweiter... |
| `beschlussverfahren-72-owig` | Beschlussverfahren § 72 OWiG: Schriftliche Erledigung per Beschluss prüfen, wenn Tatsachen und Verfahrenslage dafür taugen: Normanker... |
| `beschwerde-betroffener-behoerdenverfahren` | Beschwerde eines Betroffenen als Auslöser: Art.-77-Beschwerde, Behördenprüfung, Betroffenenkommunikation und Art.-82-Folgerisiko sauber steuern: Beschwerde eines Betroffenen als Auslöser: Art.-77-Beschwerde, Behördenprüfung, Betroffenenk... |
| `besondere-datenkategorien-art-9` | Besondere Datenkategorien Art: 9: Gesundheits-, Beschäftigten-, biometrische, religiöse oder politische Daten als Schwerefaktor prüfen. Normanker: DSGVO Art. 58 und 77-84; BDSG § 41; OWiG §§ 46 und 55 und 66-72; StPO über § 46... |
| `bestimmtheit-und-ermessen-art-58` | Bestimmtheit und Ermessen Art: 58: Unklare, überschießende oder ermessensfehlerhafte Aufsichtsmaßnahmen präzise angreifen. Normanker: DSGVO Art. 58 und 77-84; BDSG § 41; OWiG §§ 46 und 55 und 66-72; StPO über § 46 OWiG; gerich... |
| `beweisrecht-stpo-im-owig-datenschutz` | Beweisrecht im Datenschutz-OWiG: Strafprozessuale Beweislogik auf DSGVO-Vorwürfe übertragen, ohne zivilrechtliche Darlegungslast zu simulieren: Beweisrecht im Datenschutz-OWiG: Strafprozessuale Beweislogik auf DSGVO-Vorwürfe übertragen,... |
| `bfdi-vs-landesaufsicht` | BfDI oder Landesaufsicht: Sachliche Zuständigkeit zwischen BfDI, Landesdatenschutzbehörden, Kirchenaufsicht und Spezialaufsicht prüfen: BfDI oder Landesaufsicht: Sachliche Zuständigkeit zwischen BfDI, Landesdatenschutzbehörden, Kirchenau... |
| `bussgeldbescheid-65-owig-analyse` | Bußgeldbescheid § 65 OWiG analysieren: Tenor, Tat, Norm, Begründung, Bemessung, Zustellung und Rechtsbehelf des Bußgeldbescheids zerlegen: Bußgeldbescheid § 65 OWiG analysieren: Tenor, Tat, Norm, Begründung, Bemessung, Zustellung und Rec... |
| `bussgeldreduzierung-verhandlungspaket` | Bußgeldreduzierung Verhandlungspaket: EDPB-Gegenrechnung, Remediation, Kooperationsnachweise, Zahlungsfähigkeit und Veröffentlichungsschutz verhandlungsfähig machen: Bußgeldreduzierung Verhandlungspaket: EDPB-Gegenrechnung, Remediation,... |
| `datenloeschung-vs-beweissicherung` | Datenlöschung vs: Beweissicherung: Löschpflicht, Aufbewahrung, Zweckwechsel, Litigation Hold und minimierte Beweissicherung austarieren. Normanker: DSGVO Art. 58 und 77-84; BDSG § 41; OWiG §§ 46 und 55 und 66-72; StPO über § 46 OWiG; ger... |
| `datenpanne-vor-bussgeld-selbstmeldung` | Datenpanne vor Bußgeld Selbstmeldung taktisch nutzen: Art.-33/34-Meldung, 72-Stunden-Timeline, Remediation und Bußgeldmilderung verbinden: Datenpanne vor Bußgeld Selbstmeldung taktisch nutzen: Art.-33/34-Meldung, 72-Stunden-Timeline, Rem... |
| `dokumentenmatrix-akteneinsicht-vorlage-und-luecken` | Dokumentenmatrix vor Akteneinsicht: VVT, DSFA, TOM, AVV, Löschkonzept, Incident-Timeline, DSB-Vermerke, Schulungen und Logs einsammeln: Dokumentenmatrix vor Akteneinsicht: VVT, DSFA, TOM, AVV, Löschkonzept, Incident-Timeline, DSB-Vermerk... |
| `durchsuchung-beschlagnahme-und-datenzugriff` | Durchsuchung Beschlagnahme und Datenzugriff: Extremfälle von Behördenzugriffen auf Server, Kommunikation, Mandatsunterlagen und Geschäftsgeheimnisse vorbereiten: Durchsuchung Beschlagnahme und Datenzugriff: Extremfälle von Behördenzugrif... |
| `edpb-04-2022-bemessungsmethodik` | EDPB 04/2022 Bemessungsmethodik: Startbetrag, Schwere, Umsatz, erschwerende/mildernde Umstände, Höchstgrenze und Verhältnismäßigkeit nachrechnen: EDPB 04/2022 Bemessungsmethodik: Startbetrag, Schwere, Umsatz, erschwerende/mildernde Umstä... |
| `edpb-art-65-streitbeilegung` | EDPB-Streitbeilegung Art: 65: Verbindliche EDPB-Entscheidung bei Behördenstreit verstehen und Mandanteninteressen vorher sichern. Normanker: DSGVO Art. 58 und 77-84; BDSG § 41; OWiG §§ 46 und 55 und 66-72; StPO über § 46 OWiG; geri... |
| `edsa-und-dsk-praxis-livecheck` | EDPB und DSK Praxis Livecheck: Aktuelle Leitlinien, Orientierungshilfen und Behördenpraxis live prüfen und nicht aus Modellwissen erfinden: EDPB und DSK Praxis Livecheck: Aktuelle Leitlinien, Orientierungshilfen und Behördenpraxis live p... |
| `einspruch-67-owig-frist-und-form` | Einspruch § 67 OWiG Frist und Form: Zweiwochenfrist sichern und fristwahrenden Einspruch ohne unnötige Begründung einlegen: Normanker... |
| `einstellung-anregen-vor-bescheid` | Einstellung vor Bescheid anregen: Tatbestand, Verschulden, Bemessung, Maßnahmenplan und Verhältnismäßigkeit für Einstellung oder Verwarnung bündeln: Einstellung vor Bescheid anregen: Tatbestand, Verschulden, Bemessung, Maßnahmenplan und... |
| `einstweilige-anordnung-123-vwgo-datenschutz` | Einstweilige Anordnung § 123 VwGO: Vorläufigen Rechtsschutz bei Untätigkeit, Duldung, Datenfreigabe oder nicht klassischer Anfechtung gestalten: Einstweilige Anordnung § 123 VwGO: Vorläufigen Rechtsschutz bei Untätigkeit, Duldung, Datenf... |
| `eugh-vorlage-art-267` | EuGH-Vorlagefragen entwickeln: Vorlagefragen zu Art: 83, Umsatzbegriff, Verfahrensgarantien, Art. 58 und Grundrechtecharta formulieren. Normanker: DSGVO Art. 58 und 77-84; BDSG § 41; OWiG §§ 46 und 55 und... |
| `fristenzentrale-zustellung-und-wiedervorlage` | Fristenzentrale Zustellung und Wiedervorlage: Zustellung, Bekanntgabe, Rechtsbehelfsbelehrung, Einspruchsfrist, Behördenfrist und gerichtliche Eilfrist absichern: Fristenzentrale Zustellung und Wiedervorlage: Zustellung, Bekanntgabe, Rec... |
| `fristverlaengerung-behoerde-ohne-nachteile` | Fristverlängerung gegenüber Aufsicht: Fristverlängerung und Teilantwort beantragen, ohne Verzögerung oder Pflichtverletzung einzuräumen: Fristverlängerung gegenüber Aufsicht: Fristverlängerung und Teilantwort beantragen, ohne Verzögerung... |
| `fruehstellungnahme-vor-bussgeldbescheid` | Frühstellungnahme vor Bußgeldbescheid: Vor Bescheid mit gesicherten Tatsachen Einstellung, Verwarnung oder milde Maßnahme erreichen: Frühstellungnahme vor Bußgeldbescheid: Vor Bescheid mit gesicherten Tatsachen Einstellung, Verwarnung od... |
| `gerichtstermin-sprechzettel` | Gerichtstermin-Sprechzettel: Hauptverhandlung oder Erörterungstermin mit Rollen, Beweisthemen, Anträgen und Sprechzetteln vorbereiten: Gerichtstermin-Sprechzettel: Hauptverhandlung oder Erörterungstermin mit Rollen, Beweisthemen, Anträge... |
| `gewinnabschoepfung-und-finanzieller-vorteil` | Finanzieller Vorteil und Gewinnabschöpfung: Vorteile, Kostenersparnis, Kausalität, Schätzung und Gegenrechnung mit Remediation-Kosten prüfen: Finanzieller Vorteil und Gewinnabschöpfung: Vorteile, Kostenersparnis, Kausalität, Schätzung un... |
| `grch-verfahrensgrundrechte` | GRCh-Verfahrensgrundrechte: Art: 47/48/50/52 GRCh für Verteidigungsrechte, Rechtsschutz und Verhältnismäßigkeit nutzen. Normanker: DSGVO Art. 58 und 77-84; BDSG § 41; OWiG §§ 46 und 55 und 66-72; StPO über § 46 OWiG; gericht... |
| `hauptverhandlung-71-owig` | Hauptverhandlung § 71 OWiG: Hauptverhandlung mit StPO-Logik, Beweisaufnahme, Zeugen, Sachverständigen und Anträgen vorbereiten: N... |
| `internationale-datenpanne-und-multi-notification` | Internationale Datenpanne und Multi-Notification: Meldungen in mehreren Jurisdiktionen ohne widersprüchliche Sachverhalte und mit Lead-Authority-Strategie planen: Internationale Datenpanne und Multi-Notification: Meldungen in mehreren Ju... |
| `interne-untersuchung-legal-hold` | Interne Untersuchung und Legal Hold: Dokumentensicherung, E-Mail, Tickets, Logs, Backups, DSB-Hinweise und Vorstandsvorlagen organisieren: Interne Untersuchung und Legal Hold: Dokumentensicherung, E-Mail, Tickets, Logs, Backups, DSB-Hinw... |
| `irische-dpc-und-deutsche-aufsicht` | Irische DPC und deutsche Aufsicht: Plattform-/SaaS-Fälle mit irischer Hauptniederlassung und deutscher Beschwerde routen: Normanker: DS... |
| `kaltstart-verfahrensstand-und-mandatsziel` | Kaltstart Verfahrensstand und Mandatsziel: Anhörung, Bußgeldbescheid, Art.-58-Anordnung, Verwaltungsstreit und Gerichtsphase in zehn Minuten trennen. Normanker: DSGVO Art. 58 und 77-84; BDSG § 41; OWiG §§ 46 und 55 und 66-72; StPO über §... |
| `ki-tools-im-sanktionsverfahren` | KI-Tools im Sanktionsverfahren: KI-Aktenauswertung mit Pseudonymisierung, Mandatsgeheimnis, Anbieterprüfung und Quellenkontrolle freigeben: KI-Tools im Sanktionsverfahren: KI-Aktenauswertung mit Pseudonymisierung, Mandatsgeheimnis, Anbie... |
| `kinder-und-schutzbeduerftige-betroffene` | Kinder und vulnerable Betroffene: Kinder, Patienten, Beschäftigte, Mieterinteressenten und andere Schutzgruppen sanktionsrechtlich einordnen: Kinder und vulnerable Betroffene: Kinder, Patienten, Beschäftigte, Mieterinteressenten und ande... |
| `kirchliche-datenschutzaufsicht-sanktionen` | Kirchliche Datenschutzaufsicht: KDG, DSG-EKD, kirchliche Aufsichten, kirchliche Gerichte und Sanktionslogik einordnen: Normanker: DSGVO Ar... |
| `kosten-auslagen-und-d-und-o-risiko` | Kosten Auslagen und D&O-Risiko: Verteidigungskosten, Bußgeld, D&O-Meldung, Organhaftung und Versicherungsdeckung abschätzen: Normank... |
| `lieferanten-und-auftragsverarbeiter-regress` | Lieferanten und Auftragsverarbeiter Regress: Regress, AVV-Haftung, Freistellung und Beweissicherung gegen Auftragsverarbeiter nach einem Bußgeldfall vorbereiten: Lieferanten und Auftragsverarbeiter Regress: Regress, AVV-Haftung, Freistel... |
| `loeschkonzept-und-aufbewahrungsfehler` | Löschkonzept und Aufbewahrungsfehler: Fehlende Löschung, überlange Speicherung, Backups und Aufbewahrungspflichten als Bußgeldthema strukturieren: Löschkonzept und Aufbewahrungsfehler: Fehlende Löschung, überlange Speicherung, Backups un... |
| `loeschungsanordnung-und-datenbestand` | Löschungsanordnung und Datenbestand: Löschungsanordnung, Aufbewahrungspflichten, Litigation Hold, Backups und technische Machbarkeit lösen: Löschungsanordnung und Datenbestand: Löschungsanordnung, Aufbewahrungspflichten, Litigation Hold,... |
| `logfiles-und-technische-beweise` | Logfiles und technische Beweise: SIEM, Access Logs, Admin-Aktivitäten, Zeitstempel, Retention und Integrität als Beweise bewerten: Logfiles und technische Beweise: SIEM, Access Logs, Admin-Aktivitäten, Zeitstempel, Retention und Integrit... |
| `mandanteninterview-ohne-selbstbelastung` | Mandanteninterview ohne Selbstbelastung: Fakten sammeln, ohne neue Eingeständnisse, überschießende Datenoffenlegung oder unkluge Wertungen zu produzieren: Mandanteninterview ohne Selbstbelastung: Fakten sammeln, ohne neue Eingeständnisse... |
| `mandantenreport-regulatorische-risikolage` | Mandantenreport regulatorische Risikolage: Aus Bußgeld- und Anordnungsrisiken einen entscheidungsfähigen Monats- oder Krisenreport bauen: Mandantenreport regulatorische Risikolage: Aus Bußgeld- und Anordnungsrisiken einen entscheidungsfä... |
| `massnahmenplan-als-sanktionsminderung` | Maßnahmenplan als Sanktionsminderung: Root Cause, Sofortmaßnahme, Owner, Budget, Wirksamkeitsmessung und Nachweise bußgeldmindernd aufbereiten: Maßnahmenplan als Sanktionsminderung: Root Cause, Sofortmaßnahme, Owner, Budget, Wirksamkeits... |
| `mehrere-verstoesse-und-art-83-3` | Mehrere Verstöße und Art: 83 Abs. 3: Mehrfachverstöße aus derselben Verarbeitung und Höchstgrenze nach Art. 83 Abs. 3 prüfen. Normanker: DSGVO Art. 58 und 77-84; BDSG § 41; OWiG §§ 46 und 55 und 66-72; StPO über § 46 OWiG; gerichtl... |
| `milderung-durch-compliance-vor-dem-vorfall` | Milderung durch Compliance vor dem Vorfall: Vorhandene Schulungen, DSFA, AVV, Audits und technische Tests als konkrete Entlastung belegen: Milderung durch Compliance vor dem Vorfall: Vorhandene Schulungen, DSFA, AVV, Audits und technisch... |
| `milderung-durch-remediation-nach-dem-vorfall` | Milderung durch Remediation nach dem Vorfall: Nachträgliche Maßnahmen, Wirksamkeitsprüfung und Betroffenenschutz für Art.-83-Milderung dokumentieren: Milderung durch Remediation nach dem Vorfall: Nachträgliche Maßnahmen, Wirksamkeitsprüf... |
| `normenkollision-geheimnisse-und-datenschutzaufsicht` | Geheimnisse gegenüber Datenschutzaufsicht: Geschäftsgeheimnis, Mandatsgeheimnis, Bankgeheimnis und Sozialgeheimnis bei Behördenvorlagen schützen: Geheimnisse gegenüber Datenschutzaufsicht: Geschäftsgeheimnis, Mandatsgeheimnis, Bankgeheim... |
| `oeffentliche-stellen-bussgeldprivilegien` | Öffentliche Stellen und Bußgeldfähigkeit: Bußgeldfähigkeit öffentlicher Stellen nach Art: 83 Abs. 7 DSGVO, BDSG und Landesrecht prüfen. Normanker: DSGVO Art. 58 und 77... |
| `one-stop-shop-art-56-60` | One-Stop-Shop Art: 56 und 60: Lead Authority, betroffene Aufsichten, Draft Decision, Einwände und grenzüberschreitende Verteidigung steuern. Normanker: DSGVO Art. 58 und 77-84; BDSG § 41; OWiG §§ 46 und 55 und 66-72; StPO über § 46 OWiG;... |
| `organisationsverschulden-ersteinschaetzung` | Organisationsverschulden ersteinschätzen: Schuldhaftes Unternehmensverhalten nach EuGH C-807/21/C-683/21 anhand Organisation, Wissen und Pflichtverstoß prüfen: Organisationsverschulden ersteinschätzen: Schuldhaftes Unternehmensverhalten... |
| `parallelverfahren-art-82-massenklagen` | Parallelverfahren Art: 82 DSGVO und Massenklagen: Bußgeldverteidigung mit Schadensersatzabwehr, Massenklagen und Anerkenntnisrisiken abstimmen. Normanker: DSGVO Art. 58 und 77-84; BDSG § 41; OWiG §§ 46 und 55 und 66-72; StPO über § 46... |
| `parallelverfahren-strafrecht-42-bdsg` | Parallelverfahren § 42 BDSG und Strafrecht: Strafrechtliche Datenschutzrisiken, Durchsuchung, Aussageverhalten und Verteidigerkoordination erkennen: Parallelverfahren § 42 BDSG und Strafrecht: Strafrechtliche Datenschutzrisiken, Durchsuc... |
| `privilege-und-mandatsgeheimnis` | Privilege Mandatsgeheimnis und Vertraulichkeit: Anwaltliche Kommunikation, Verteidigungsdokumente und vertrauliche Untersuchungsunterlagen schützen: Privilege Mandatsgeheimnis und Vertraulichkeit: Anwaltliche Kommunikation, Verteidigungs... |
| `profiling-und-automatisierte-entscheidungen` | Profiling und automatisierte Entscheidungen: Art: 22, Scoring, KI-Systeme, Transparenz, DSFA und Diskriminierungsrisiko im Bußgeldfall prüfen. Normanker: DSGVO Art. 58 und 77-84; BDSG § 41; OWiG §§ 46 und 55... |
| `public-sector-und-vergabefolgen` | Public Sector und Vergabefolgen: Folgen einer Datenschutzsanktion für öffentliche Auftraggeber, Vergaben, Zuverlässigkeit und Lieferantenstatus prüfen: Public Sector und Vergabefolgen: Folgen einer Datenschutzsanktion für öffentliche Auf... |
| `rechtsbeschwerde-79-owig` | Rechtsbeschwerde § 79 OWiG: Rechtsbeschwerde, Zulassung, Verfahrensrügen und unionsrechtliche Vorlagefragen prüfen: Normanker: DSGVO Art. 58... |
| `rechtsweg-router-bussgeld-verwaltungsgericht-zivilverfahren` | Rechtsweg-Router Bußgeld Verwaltungsgericht Zivilverfahren: Geldbuße, Art.-58-Maßnahme, Art.-82-Schadensersatz und Strafrechtsspur aus demselben Vorfall trennen: Rechtsweg-Router Bußgeld Verwaltungsgericht Zivilverfahren: Geldbuße, Art.-... |
| `red-team-vor-jeder-einreichung` | Red Team vor jeder Einreichung: Stellungnahme, Klage und Einspruchsbegründung auf Selbstwidersprüche, Blindzitate und Beweisrisiken prüfen. Normanker: DSGVO Art. 58 und 77-84; BDSG § 41; OWiG §§ 46 und 55 und 66-72; StPO über § 46 OWiG;... |
| `sachverstaendige-it-forensik-im-bussgeldverfahren` | IT-Forensik und Sachverständige: Gutachten zu Logs, TOMs, Verschlüsselung, Löschung, Zugriffen und Datenabfluss gerichtsfest vorbereiten: IT-Forensik und Sachverständige: Gutachten zu Logs, TOMs, Verschlüsselung, Löschung, Zugriffen und... |
| `sanktionsmandat-schlussprodukt-planen` | Schlussprodukt des Sanktionsmandats planen: Einstellung, Verwarnung, reduzierte Geldbuße, aufgehobene Anordnung, Vergleich, Urteil oder Rechtsbeschwerde als Zielbild definieren: Schlussprodukt des Sanktionsmandats planen: Einstellung, Ve... |
| `schlussmemo-und-lessons-learned` | Schlussmemo und Lessons Learned: Bestandskraft, Auflagen, Wiedervorlagen, Schulungen, D&O, Folgeklagen und Compliance-Nacharbeit dokumentieren: Schlussmemo und Lessons Learned: Bestandskraft, Auflagen, Wiedervorlagen, Schulungen, D&O, Fo... |
| `scope-cut-behoerdenfragen-einhegen` | Scope Cut Behördenfragen einhegen: Zu weite Behördenfragen nach Zeitraum, System, Datenart, Gesellschaft und Betroffenenkreis begrenzen: Scope Cut Behördenfragen einhegen: Zu weite Behördenfragen nach Zeitraum, System, Datenart, Gesellsc... |
| `selbstbelastungsfreiheit-und-mitwirkungspflichten` | Selbstbelastung und Mitwirkungspflichten: Auskunftspflichten gegenüber der Aufsicht und Aussagefreiheit im Bußgeldverfahren balancieren: Selbstbelastung und Mitwirkungspflichten: Auskunftspflichten gegenüber der Aufsicht und Aussagefreih... |
| `staatsanwaltschaft-im-dsgvo-owig` | Staatsanwaltschaft im DSGVO-OWiG-Verfahren: Rolle der Staatsanwaltschaft nach Akteneingang und Zustimmungserfordernis der Aufsicht bei Einstellung erklären: Staatsanwaltschaft im DSGVO-OWiG-Verfahren: Rolle der Staatsanwaltschaft nach Ak... |
| `tracking-cookies-und-ttddg-schnittstelle` | Tracking Cookies und TDDDG-Schnittstelle: Cookie-/Tracking-Sanktionen zwischen DSGVO, TDDDG, Einwilligung und Aufsichts-/Telemedienpraxis bearbeiten: Tracking Cookies und TDDDG-Schnittstelle: Cookie-/Tracking-Sanktionen zwischen DSGVO, T... |
| `transferstopp-drittland-art-58` | Drittland-Transferstopp Art: 58: DPF, SCC, TIA, Transferregister, Migrationsplan und Eilrechtsschutz bei Transferstopp verbinden. Normanker: DSGVO Art. 58 und 77-84; BDSG § 41; OWiG §§ 46 und 55 und 66-72; StPO über § 46 OWiG; g... |
| `umsatz-und-wirtschaftliche-einheit` | Umsatz und wirtschaftliche Einheit: 2-/4-Prozent-Grenze, unionsrechtliches Unternehmen, Konzernumsatz und Adressat prüfen: Normanker:... |
| `unternehmensgruppe-und-federfuehrende-aufsicht` | Unternehmensgruppe und federführende Aufsicht: Hauptniederlassung, One-Stop-Shop, gemeinsame Verantwortlichkeit und Konzernadressat prüfen: Unternehmensgruppe und federführende Aufsicht: Hauptniederlassung, One-Stop-Shop, gemeinsame Vera... |
| `untersagung-und-verarbeitungsstopp` | Untersagung und Verarbeitungsstopp: Vorläufige oder endgültige Beschränkung einer Verarbeitung mit Eilrechtsschutz und milderen Mitteln angreifen: Untersagung und Verarbeitungsstopp: Vorläufige oder endgültige Beschränkung einer Verarbei... |
| `unverhaeltnismaessigkeit-und-existenzgefahr` | Verhältnismäßigkeit und Existenzgefahr: Liquidität, Eigenkapital, Insolvenznähe, Arbeitsplätze und Ratenzahlung gegen Abschreckung abwägen: Verhältnismäßigkeit und Existenzgefahr: Liquidität, Eigenkapital, Insolvenznähe, Arbeitsplätze un... |
| `verhaeltnismaessigkeit-aufsichtsmassnahme` | Verhältnismäßigkeit der Aufsichtsmaßnahme: Datenschutzgewinn, Betriebsfolgen, Grundrechte, mildere Mittel und Angemessenheit abwägen: Verhältnismäßigkeit der Aufsichtsmaßnahme: Datenschutzgewinn, Betriebsfolgen, Grundrechte, mildere Mitt... |
| `veroeffentlichung-von-bussgeldentscheidungen` | Veröffentlichung von Bußgeldentscheidungen: Namensnennung, Behördenpublikation, Geschäftsgeheimnisse und Reputationsschutz steuern: Veröffentlichung von Bußgeldentscheidungen: Namensnennung, Behördenpublikation, Geschäftsgeheimnisse und... |
| `verteidigerrolle-dsb-gf-und-externe-berater` | Rollenklärung Verteidiger DSB Geschäftsleitung externe Berater: Datenschutzbeauftragten, Geschäftsleitung, externe Anwälte, IT-Forensik und PR-Beratung konfliktfrei koordinieren: Rollenklärung Verteidiger DSB Geschäftsleitung externe Ber... |
| `verwarnung-art-58-2-b` | Verwarnung Art: 58 Abs. 2 lit. b: Verwarnung als milde, aber vorbelastungs- und reputationsrelevante Maßnahme einordnen. Normanker: DSGVO Art. 58 und 77-84; BDSG § 41; OWiG §§ 46 und 55 und 66-72; StPO über § 46 OWiG; gerichtliche Zustän... |
| `vg-anfechtungsklage-20-bdsg` | Anfechtungsklage nach § 20 BDSG: Klage gegen Aufsichtsmaßnahmen mit Verwaltungsrechtsweg, ohne Vorverfahren und Sitz der Aufsicht als Zuständigkeitsanker vorbereiten: Anfechtungsklage nach § 20 BDSG: Klage gegen Aufsichtsmaßnahmen mit Ve... |
| `vg-eilrechtsschutz-80-5-vwgo` | Eilrechtsschutz § 80 Abs: 5 VwGO: Sofortvollzug, Interessenabwägung und Erfolgsprognose gegen belastende Datenschutzanordnungen prüfen. Normanker: DSGVO Art. 58 und 77-84; BDSG § 41; OWiG §§ 46 und 55 und 66-72; StPO über § 46 OWiG... |
| `videoueberwachung-und-biometrie` | Videoüberwachung und Biometrie: Videoüberwachung, biometrische Erkennung, Hinweisschilder, Speicherfrist und Interessenabwägung bußgeldfest prüfen: Videoüberwachung und Biometrie: Videoüberwachung, biometrische Erkennung, Hinweisschilder... |
| `vorbelastungen-und-wiederholungstaeter` | Vorbelastungen und Wiederholungstäter: Frühere Auflagen, Verwarnungen oder Vorfälle auf Identität, Bestandskraft und Vergleichbarkeit prüfen: Vorbelastungen und Wiederholungstäter: Frühere Auflagen, Verwarnungen oder Vorfälle auf Identit... |
| `vorsatz-fahrlaessigkeit-unternehmen` | Vorsatz und Fahrlässigkeit des Unternehmens: Wissen, Organisation, TOMs, DSB-Hinweise und Eskalation als Schuld- oder Entlastungsmaterial nutzen: Vorsatz und Fahrlässigkeit des Unternehmens: Wissen, Organisation, TOMs, DSB-Hinweise und E... |
| `vorstands-und-gf-briefing` | Vorstands- und Geschäftsführungsbriefing: Geschäftsleitung knapp über Fristen, Optionen, Budget, Haftung, Presse und Entscheidungsbedarf informieren: Vorstands- und Geschäftsführungsbriefing: Geschäftsleitung knapp über Fristen, Optionen... |
| `wiedereinsetzung-nach-fristversaeumnis` | Wiedereinsetzung nach Fristversäumnis: Versäumte Einspruchs- oder Rechtsmittelfristen mit Zustellungs- und Büroorganisationsprüfung retten: Wiedereinsetzung nach Fristversäumnis: Versäumte Einspruchs- oder Rechtsmittelfristen mit Zustell... |
| `zeugeninterviews-mitarbeiter` | Mitarbeiterinterviews im Sanktionsverfahren: Beschäftigteninterviews mit Belehrung, Betriebsrat, Datenschutz, Aussagefreiheit und Konfliktcheck führen: Mitarbeiterinterviews im Sanktionsverfahren: Beschäftigteninterviews mit Belehrung, B... |
| `zustaendigkeit-amtsgericht-landgericht-41-bdsg` | Zuständigkeit Amtsgericht Landgericht § 41 BDSG: Prüfen, ob wegen Geldbuße über 100.000 EUR das Landgericht statt Amtsgericht entscheidet: Zuständigkeit Amtsgericht Landgericht § 41 BDSG: Prüfen, ob wegen Geldbuße über 100.000 EUR das La... |
| `zwangsgeld-und-vollstreckung-aufsicht` | Zwangsgeld und Vollstreckung der Aufsicht: Zwangsgeldandrohung, Festsetzung, Erfüllbarkeit, Frist und Vollstreckungsabwehr bearbeiten: Zwangsgeld und Vollstreckung der Aufsicht: Zwangsgeldandrohung, Festsetzung, Erfüllbarkeit, Frist und... |
| `zwischenverfahren-69-owig` | Zwischenverfahren § 69 OWiG: Nach Einspruch Rücknahme, weitere Ermittlungen oder Vorlage über Staatsanwaltschaft an das Gericht taktisch nutzen: Zwischenverfahren § 69 OWiG: Nach Einspruch Rücknahme, weitere Ermittlungen oder Vorlage übe... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
