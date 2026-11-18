# Steuerrechtliche Hinweise: Nachprüfung vom 18. November 2026

## 1. Umfang und Ergebnis

Die Issues [#536](https://github.com/Klotzkette/claude-fuer-deutsches-recht/issues/536), [#537](https://github.com/Klotzkette/claude-fuer-deutsches-recht/issues/537), [#538](https://github.com/Klotzkette/claude-fuer-deutsches-recht/issues/538) und [#613](https://github.com/Klotzkette/claude-fuer-deutsches-recht/issues/613) wurden vollständig gelesen und mit den heutigen Dateien abgeglichen. Die beanstandeten Aussagen waren in diesen Dateien bereits berichtigt. Insbesondere dokumentiert die gemeinsame Software-/Lizenzreferenz eine Bearbeitung vom 1. November 2026. Die vorliegende Nachprüfung ist deshalb keine erneute Umsetzung dieser Hinweise.

Keine fremden Texte oder Commits wurden übernommen. Keine Testakte, kein Skill und kein Prompt wurde aufgrund dieser vier bereits erledigten Punkte verändert. Dieser Vermerk dokumentiert die erneute Prüfung und deren Grenzen. Er bescheinigt keine vollständige Richtigkeit der übrigen Inhalte der drei Plugins, insbesondere nicht aller Länderprofile, Abkommenssätze oder sämtlicher anderer Betriebsausgabenregeln.

## 2. Issue #536: Lizenzschranke und Freistellungsbescheinigung

**Befund: im aktuellen Bestand bereits erledigt.** Die Lizenzschranke wird nicht mehr als allgemeine Abzugsbeschränkung für den aktuellen Veranlagungszeitraum dargestellt. Die verbliebenen Hinweise kennzeichnen § 4j EStG ausdrücklich als Altjahresprüfung bis einschließlich Veranlagungszeitraum 2024. Die Angaben zur Freistellungsbescheinigung nennen höchstens fünf Jahre und den frühestmöglichen Beginn mit dem Eingang des Antrags beim BZSt; eine feste Fünfjahresdauer wird nicht zugesagt.

Gelesene Bestandspfade unter `steuerrecht-anwalt-und-berater/`:

- `references/lizenzzahlungen-software.md`
- `skills/dba-lizenzgebuehren-art-12-bzst/FACHINHALT.md`
- `skills/dba-all-country-memo-generator/FACHINHALT.md`
- `skills/dba-quellensteuer-atlas-weltweit/FACHINHALT.md`
- `skills/dba-alle-abkommen-laendermatrix-2026/references/g-k-01.md` und `t-z-02.md`
- `skills/rechtsabteilung-transfer-pricing-bei-ip-und-softwarelizenzen/FACHINHALT.md`
- `skills/rechtsabteilung-transfer-pricing-ip/FACHINHALT.md`

Erneut gelesene Primärquellen:

- [§ 4j EStG](https://www.gesetze-im-internet.de/estg/__4j.html): weggefallen.
- [§ 52 Abs. 8c EStG](https://www.gesetze-im-internet.de/estg/__52.html): Satz 3 bestimmt die letztmalige Anwendung für den Veranlagungszeitraum 2024. Satz 2 enthält die zeitliche Zuordnung der 2023 geänderten Fassung. Diese Übergangsregel erlaubt keine pauschale Anwendung der Lizenzschranke im Jahr 2026.
- [§ 50c Abs. 2 Satz 4 EStG](https://www.gesetze-im-internet.de/estg/__50c.html): höchstens fünf Jahre; frühestens ab Antragseingang; Bedingungen und Auflagen sind möglich.

Grenze: Die historische Niedrigbesteuerungs- und Präferenzprüfung wurde nicht für einzelne ausländische Steuerregime neu durchgeführt. Die im Repository nun ausdrücklich historische Behandlung des § 4j EStG wird durch die aktuellen Anwendungsvorschriften bestätigt.

## 3. Issue #537: Softwareüberlassung nach dem Rechteinhalt beurteilen

**Befund: im aktuellen Bestand bereits erledigt.** Die betroffenen Stellen unterscheiden die bloße bestimmungsgemäße Programmnutzung von wirtschaftlichen Verwertungsrechten. Vertragsbezeichnungen wie Kauf oder Lizenz und die Unterscheidung Standard-/Individualsoftware ersetzen die Rechteprüfung nicht. Interne Nutzung, notwendige Programmkopien und vertragliche Nutzungsbeschränkungen führen nicht automatisch zu einer deutschen Quellensteuerpflicht. Der vollständige wirtschaftliche Rechteerwerb und gemischte Leistungsbündel werden gesondert behandelt.

Gelesene Bestandspfade unter `steuerrecht-anwalt-und-berater/`:

- `references/lizenzzahlungen-software.md`
- `skills/dba-lizenzgebuehren-art-12-bzst/FACHINHALT.md`
- `skills/dba-quellensteuer-atlas-weltweit/FACHINHALT.md`
- `skills/dba-alle-abkommen-laendermatrix-2026/references/g-k-02.md`, Abschnitt Israel

Erneut gelesene Primärquellen:

- [OECD-Musterabkommen 2017, Kurzfassung](https://www.oecd.org/content/dam/oecd/en/publications/reports/2017/12/model-tax-convention-on-income-and-on-capital-condensed-version-2017_g1g8769b/mtc_cond-2017-en.pdf), Kommentar zu Art. 12, Tz. 12.2–17, gedruckte Seiten 280–283: Entscheidend sind die übertragenen Rechte. Die gewöhnliche Nutzung einer Programmkopie und dafür erforderliche Kopien sind von der urheberrechtlichen Verwertung abzugrenzen. Auch Mehrplatznutzung und Vertrieb ohne Vervielfältigungsrechte sind differenziert zu behandeln; vollständige Rechteveräußerung und gemischte Verträge bedürfen eigener Einordnung.
- [Amtliches Einkommensteuer-Handbuch 2025, Hinweise zu § 49 EStG](https://ao.bundesfinanzministerium.de/esth/2025/A-Einkommensteuergesetz/VIII-Besteuerung-beschraenkt-Stpfl-49-50a/Paragraf-49/paragraf-49.html): Der Abschnitt zur grenzüberschreitenden Überlassung von Software und Datenbanken verweist weiterhin auf das BMF-Schreiben vom 27. Oktober 2017, BStBl I S. 1448.
- [§ 50c EStG](https://www.gesetze-im-internet.de/estg/__50c.html): Eine abkommensrechtliche Entlastung und das dafür vorgesehene Verfahren sind von der vorgelagerten Frage zu unterscheiden, ob nach innerstaatlichem Recht überhaupt abzugsverpflichtete Einkünfte vorliegen.

Grenzen: Das OECD-Musterabkommen ist kein unmittelbar anwendbares bilaterales DBA. Der aktuelle Text verlangt deshalb zusätzlich die Prüfung des konkreten Abkommens und gegebenenfalls ausländischen Rechts. Das amtliche Handbuch bestätigt die Fundstelle des BMF-Schreibens von 2017; sein vollständiger Originaltext sowie das im Repository ergänzend angeführte Schreiben von 2022 konnten in dieser Nachprüfung nicht erneut als amtlicher Volltext abgerufen werden. Die bereits dokumentierte frühere Prüfung dieser Schreiben wird daher nicht als heutige erneute Volltextprüfung ausgegeben. Auch der OECD-Nachtrag 2025 wird hier nicht als erneut vollständig gelesene Quelle beansprucht. Die vorstehende Rechteabgrenzung ist unabhängig davon im gelesenen OECD-Kommentar belegt.

## 4. Issue #538: Entlastungsverfahren und Schreibweise UrhG

**Befund: im aktuellen Bestand bereits erledigt.** Freistellung und Erstattung werden in § 50c Abs. 2 und 3 EStG verortet. § 50d Abs. 3 EStG wird gesondert als mögliche Entlastungsbeschränkung behandelt. Die beanstandete Schreibweise „UhG“ lautet inzwischen „UrhG“ und ist mit § 31a UrhG verlinkt.

Gelesene Bestandspfade:

- `lizenzvertragsersteller/skills/steuern-quellensteuer-und-dba-lizenz/FACHINHALT.md`
- `lizenzvertragsersteller/skills/lizenz-urheberrecht-und-software-urhg/FACHINHALT.md`

Erneut gelesene Primärquellen:

- [§ 50c Abs. 1–3 EStG](https://www.gesetze-im-internet.de/estg/__50c.html): Verhältnis von Steuerabzug, Freistellung und Erstattung.
- [§ 50d Abs. 3 EStG](https://www.gesetze-im-internet.de/estg/__50d.html): Beschränkung der Entlastungsberechtigung mit den gesetzlichen Rückausnahmen; keine verfahrensrechtliche Ersatzgrundlage für § 50c EStG.

Grenze: Die Prüfung umfasst den beanstandeten Normenverweis und die redaktionelle Korrektur. Sie ist keine neue Gesamtprüfung sämtlicher Vertragsklauseln, Urheberrechtsansprüche oder Gross-up-Vereinbarungen des Lizenzplugins.

## 5. Issue #613: Geschenke, Reisekosten und Pressereisen

**Befund: im aktuellen Bestand bereits erledigt.** Die beiden Betriebsausgaben-Vertiefungen enthalten den Jahres-/Empfängerbezug der 50-Euro-Freigrenze und ihre zeitliche Anwendung. Sie unterscheiden Entfernungspauschale und auswärtige Fahrtkosten, nennen die richtigen Verpflegungspauschalen und erläutern Dreimonatsfrist, Unterbrechung sowie Mahlzeitenkürzung. Die Influencer-Vertiefungen behandeln Arbeitgebererstattungen nach § 3 Nr. 16 EStG und verweisen für Verpflegung auf § 9 Abs. 4a EStG. Eine selbständige Influencertätigkeit wird nicht allein wegen einer Einladung wie eine steuerfreie Arbeitgebererstattung behandelt.

Gelesene Bestandspfade:

- `steuerrecht-anwalt-und-berater/skills/betriebsausgaben-werbungskosten/FACHINHALT.md`
- `steuerrecht-anwalt-und-berater/skills/betriebsausgaben-werbungskosten-pruefraster/FACHINHALT.md`
- `influencer-recht/skills/restaurant-hotel-reisekosten-pressereise/FACHINHALT.md`
- `influencer-recht/skills/reisekosten-pressereise-und-gemischte-veranlassung/FACHINHALT.md`

Erneut gelesene Primärquellen:

- [§ 4 Abs. 5 Satz 1 Nr. 1, 2 und 5 EStG](https://www.gesetze-im-internet.de/estg/__4.html): Geschenkegrenze, Bewirtung und Verpflegungsmehraufwendungen. Für Geschenke gilt eine Freigrenze, kein Freibetrag; eine Überschreitung lässt nicht lediglich den übersteigenden Teil entfallen.
- [§ 52 Abs. 6 Satz 10 EStG](https://www.gesetze-im-internet.de/estg/__52.html): Anwendung der geänderten Geschenkevorschrift erstmals für nach dem 31. Dezember 2023 beginnende Wirtschaftsjahre.
- [§ 9 Abs. 1 Satz 3 Nr. 4 und 4a sowie Abs. 4a EStG](https://www.gesetze-im-internet.de/estg/__9.html), ergänzend [§ 5 BRKG](https://www.gesetze-im-internet.de/brkg_2005/__5.html): Entfernungspauschale und Auswärtstätigkeit getrennt; inländische Verpflegung 28/14 Euro, jeweilige Abwesenheitsbedingungen, Dreimonatsfrist und mindestens vierwöchige Unterbrechung, Kürzung für gestellte Mahlzeiten um 20/40 Prozent und Anrechnung eigener Zahlungen.
- [§ 3 Nr. 16 EStG](https://www.gesetze-im-internet.de/estg/__3.html): Arbeitgebererstattungen an Arbeitnehmer außerhalb des öffentlichen Dienstes, begrenzt durch die nach § 9 abziehbaren Aufwendungen.
- [BMF vom 5. Dezember 2025, Auslandsreisekosten ab 1. Januar 2026](https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Lohnsteuer/2025-12-05-steuerliche-behandlung-reisekosten-2026.pdf?__blob=publicationFile&v=2), Seiten 1–3 und Übersicht: jahres- und ortsbezogene Auslandspauschalen; Übernachtungspauschalen nur für Arbeitgebererstattungen, beim Werbungskosten-/Betriebsausgabenabzug grundsätzlich tatsächliche Übernachtungskosten.
- [BMF vom 19. November 2025, Bewirtungsaufwendungen](https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Einkommensteuer/2025-11-19-bewirtungskosten-als-betriebsausgaben.pdf?__blob=publicationFile&v=4), Einleitung und Rn. 1 ff.: Nachweisführung einschließlich elektronischer Rechnungen; das Schreiben ersetzt für die neue Rechtslage das Schreiben von 2021, das für Bewirtungen bis Ende 2024 weiter anzuwenden ist.
- [BFH, Beschluss vom 24. August 2012 – III B 21/12](https://www.bundesfinanzhof.de/de/entscheidung/entscheidungen-online/detail/STRE201250573/): Gemischte Reisen sind anhand feststellbarer Veranlassungsbeiträge zu beurteilen; aus der Möglichkeit einer Aufteilung folgt kein allgemeiner Anspruch auf einen hälftigen Abzug.

Grenzen: Aus der Korrektur dieser Reisekosten- und Geschenkepunkte folgt keine pauschale Abziehbarkeit konkreter Reisen oder Einladungen. Dokumentation, Zusammenhang mit Einnahmen und objektive Aufteilung bleiben fallbezogen zu prüfen. Andere Einkunftsarten, Abschreibungsfragen und sonstige Aussagen der umfangreichen Module waren nicht Gegenstand dieses Issue-Abgleichs.

## 6. Umsetzung und Kontrolle

Die vier sachlichen Anliegen rechtfertigen keine nochmalige Inhaltsänderung: Die betroffenen Fehler sind im geprüften Bestand nicht mehr enthalten. Es wurde ausschließlich dieser Prüfvermerk ergänzt. Die lokalen Fachdateien, Testakten, Generatoren und Versionsangaben blieben unverändert. Ein späterer Kommentar oder Abschluss der Issues ist eine gesonderte Handlung; dieser Vermerk behauptet keinen GitHub-Abschluss.
