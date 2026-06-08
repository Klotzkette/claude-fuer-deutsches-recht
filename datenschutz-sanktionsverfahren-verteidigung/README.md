# Datenschutz-Sanktionsverfahren und Verteidigung

<!-- BEGIN plugin-sofort-download-section (autogen) -->
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

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 27 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `anhoerung-owig-art-anordnung-rechtsschutz` | Anhörung Owig ART Anordnung Rechtsschutz im Datenschutz-Sanktionsverfahren-Verteidigung: prüft konkret Anhörung nach § 55 OWiG, Art.-58-Anordnung als Verwaltungsakt, Art. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und n... |
| `arbeitnehmerdaten-betriebsrat` | Arbeitnehmerdaten Betriebsrat im Datenschutz-Sanktionsverfahren-Verteidigung: prüft konkret Beschäftigtendaten und Betriebsrat, Beschlussverfahren § 72 OWiG, Beschwerde eines Betroffenen als Auslöser, Einspruch § 67 OWiG Frist und Form.... |
| `aufsicht-regulierten-aufsichtsbehoerden` | Aufsicht Regulierten Aufsichtsbehoerden im Datenschutz-Sanktionsverfahren-Verteidigung: prüft konkret Regulierte Branchen Bank Gesundheit Energie, Antwortschreiben an Aufsichtsbehörde, Auskunftsverlangen Art, Ausländische Mutter und deut... |
| `behoerdenkommunikation-reputationsschutz` | Behördenkommunikation Reputationsschutz im Datenschutz-Sanktionsverfahren-Verteidigung: prüft konkret Behördenkommunikation mit Reputationsschutz, Kooperation oder Schweigen strategisch wählen, Behördenuntätigkeit und Beschwerdegegner, E... |
| `bescheid-anhoerung-besondere-datenkategorien` | Bescheid Anhörung Besondere Datenkategorien im Datenschutz-Sanktionsverfahren-Verteidigung: prüft konkret Behördenpost richtig lesen, Besondere Datenkategorien Art, Bestimmtheit und Ermessen Art, Beweisrecht im Datenschutz-OWiG. Liefert... |
| `bfdi-vs-datenloeschung-beweissicherung` | Bfdi VS Datenloeschung Beweissicherung im Datenschutz-Sanktionsverfahren-Verteidigung: prüft konkret BfDI oder Landesaufsicht, Datenlöschung vs, Dokumentenmatrix vor Akteneinsicht, Durchsuchung Beschlagnahme und Datenzugriff. Liefert pri... |
| `bussgeldbescheid-owig-bussgeldreduzierung` | Bussgeldbescheid Owig Bussgeldreduzierung im Datenschutz-Sanktionsverfahren-Verteidigung: prüft konkret Bußgeldbescheid § 65 OWiG analysieren, Bußgeldreduzierung Verhandlungspaket, Datenpanne vor Bußgeld Selbstmeldung taktisch nutzen, Fr... |
| `edpb-bemessungsmethodik-art-streitbeilegung` | Edpb Bemessungsmethodik ART Streitbeilegung im Datenschutz-Sanktionsverfahren-Verteidigung: prüft konkret EDPB 04/2022 Bemessungsmethodik, EDPB-Streitbeilegung Art, EDPB und DSK Praxis Livecheck, Einstellung vor Bescheid anregen. Liefert... |
| `einstweilige-anordnung-eugh-vorlage` | Einstweilige Anordnung Eugh Vorlage im Datenschutz-Sanktionsverfahren-Verteidigung: prüft konkret Einstweilige Anordnung § 123 VwGO, EuGH-Vorlagefragen entwickeln, Gerichtstermin-Sprechzettel, Finanzieller Vorteil und Gewinnabschöpfung.... |
| `fristenzentrale-zustellung-fristverlaengerung` | Fristenzentrale Zustellung Fristverlaengerung im Datenschutz-Sanktionsverfahren-Verteidigung: prüft konkret Fristenzentrale Zustellung und Wiedervorlage, Fristverlängerung gegenüber Aufsicht, GRCh-Verfahrensgrundrechte, KI-Tools im Sankt... |
| `hauptverhandlung-owig-internationale` | Hauptverhandlung Owig Internationale im Datenschutz-Sanktionsverfahren-Verteidigung: prüft konkret Hauptverhandlung § 71 OWiG, Internationale Datenpanne und Multi-Notification, Interne Untersuchung und Legal Hold, Irische DPC und deutsch... |
| `kaltstart-verfahrensstand-und-mandatsziel` | Kaltstart Verfahrensstand und Mandatsziel: Anhörung, Bußgeldbescheid, Art.-58-Anordnung, Verwaltungsstreit und Gerichtsphase in zehn Minuten trennen. Normanker: DSGVO Art. 58 und 77-84; BDSG § 41; OWiG §§ 46 und 55 und 66-72; StPO über §... |
| `kinder-schutzbeduerftige-kosten-auslagen` | Kinder Schutzbeduerftige Kosten Auslagen im Datenschutz-Sanktionsverfahren-Verteidigung: prüft konkret Kinder und vulnerable Betroffene, Kosten Auslagen und D&O-Risiko, Lieferanten und Auftragsverarbeiter Regress, Löschkonzept und Aufbew... |
| `kirchliche-datenschutzaufsicht-massnahmenplan` | Kirchliche Datenschutzaufsicht Massnahmenplan im Datenschutz-Sanktionsverfahren-Verteidigung: prüft konkret Kirchliche Datenschutzaufsicht, Maßnahmenplan als Sanktionsminderung, Öffentliche Stellen und Bußgeldfähigkeit, Schlussprodukt de... |
| `loeschungsanordnung-datenbestand-logfiles` | Loeschungsanordnung Datenbestand Logfiles im Datenschutz-Sanktionsverfahren-Verteidigung: prüft konkret Löschungsanordnung und Datenbestand, Logfiles und technische Beweise, Mandanteninterview ohne Selbstbelastung, Mandantenreport regula... |
| `mehrere-verstoesse-milderung-durch` | Mehrere Verstoesse Milderung Durch im Datenschutz-Sanktionsverfahren-Verteidigung: prüft konkret Mehrere Verstöße und Art, Milderung durch Compliance vor dem Vorfall, Milderung durch Remediation nach dem Vorfall, Geheimnisse gegenüber Da... |
| `organisationsverschulden-ersteinschaetzung` | Organisationsverschulden Ersteinschaetzung im Datenschutz-Sanktionsverfahren-Verteidigung: prüft konkret Organisationsverschulden ersteinschätzen, Privilege Mandatsgeheimnis und Vertraulichkeit, Profiling und automatisierte Entscheidunge... |
| `parallelverfahren-art-strafrecht-bdsg` | Parallelverfahren ART Strafrecht BDSG im Datenschutz-Sanktionsverfahren-Verteidigung: prüft konkret Parallelverfahren Art, Parallelverfahren § 42 BDSG und Strafrecht, Rechtsweg-Router Bußgeld Verwaltungsgericht Zivilverfahren, IT-Forensi... |
| `rechtsbeschwerde-owig-schlussmemo-lessons` | Rechtsbeschwerde Owig Schlussmemo Lessons im Datenschutz-Sanktionsverfahren-Verteidigung: prüft konkret Rechtsbeschwerde § 79 OWiG, Schlussmemo und Lessons Learned, Scope Cut Behördenfragen einhegen, Selbstbelastung und Mitwirkungspflich... |
| `red-team-vor-jeder-einreichung` | Red Team vor jeder Einreichung: Stellungnahme, Klage und Einspruchsbegründung auf Selbstwidersprüche, Blindzitate und Beweisrisiken prüfen. Normanker: DSGVO Art. 58 und 77-84; BDSG § 41; OWiG §§ 46 und 55 und 66-72; StPO über § 46 OWiG;... |
| `staatsanwaltschaft-dsgvo-tracking-cookies` | Staatsanwaltschaft DSGVO Tracking Cookies im Datenschutz-Sanktionsverfahren-Verteidigung: prüft konkret Staatsanwaltschaft im DSGVO-OWiG-Verfahren, Tracking Cookies und TDDDG-Schnittstelle, Drittland-Transferstopp Art, Umsatz und wirtsch... |
| `unternehmensgruppe-federfuehrende-untersagung` | Unternehmensgruppe Federfuehrende Untersagung im Datenschutz-Sanktionsverfahren-Verteidigung: prüft konkret Unternehmensgruppe und federführende Aufsicht, Untersagung und Verarbeitungsstopp, Verhältnismäßigkeit und Existenzgefahr, Verhäl... |
| `veroeffentlichung-bussgeldentscheidungen` | Veroeffentlichung Bussgeldentscheidungen im Datenschutz-Sanktionsverfahren-Verteidigung: prüft konkret Veröffentlichung von Bußgeldentscheidungen, Anwesenheit und Entbindung § 73 OWiG, One-Stop-Shop Art, Akteneinsicht § 49 OWiG und § 147... |
| `verteidigerrolle-dsb-verwarnung-art-vg` | Verteidigerrolle DSB Verwarnung ART VG im Datenschutz-Sanktionsverfahren-Verteidigung: prüft konkret Rollenklärung Verteidiger DSB Geschäftsleitung externe, Verwarnung Art, Anfechtungsklage nach § 20 BDSG, Eilrechtsschutz § 80 Abs. Liefe... |
| `videoueberwachung-biometrie-vorbelastungen` | Videoueberwachung Biometrie Vorbelastungen im Datenschutz-Sanktionsverfahren-Verteidigung: prüft konkret Videoüberwachung und Biometrie, Vorbelastungen und Wiederholungstäter, Vorsatz und Fahrlässigkeit des Unternehmens, Vorstands- und G... |
| `wiedereinsetzung-amtsgericht-landgericht` | Wiedereinsetzung Amtsgericht Landgericht im Datenschutz-Sanktionsverfahren-Verteidigung: prüft konkret Wiedereinsetzung nach Fristversäumnis, Zuständigkeit Amtsgericht Landgericht § 41 BDSG, Zwischenverfahren § 69 OWiG, Anordnung plus Bu... |
| `zeugeninterviews-mitarbeiter-zwangsgeld` | Zeugeninterviews Mitarbeiter Zwangsgeld im Datenschutz-Sanktionsverfahren-Verteidigung: prüft konkret Mitarbeiterinterviews im Sanktionsverfahren, Zwangsgeld und Vollstreckung der Aufsicht. Liefert priorisierten Output mit Norm-Pinpoints... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
