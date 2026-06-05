---
name: db-open-data-geschaeftsgeheimnis
description: "Db Open Data Portal Nutzungsbedingungen / Db Datenbankrecht Geschaeftsgeheimnis / Db Datenbankrecht Datenschutz Personenbezogene Datensaet: führt durch diese fachlich verbundenen Arbeitsmodule, wählt den passenden Prüfpfad und erzeugt den nächsten belastbaren Output."
---

# Db Open Data Portal Nutzungsbedingungen / Db Datenbankrecht Geschaeftsgeheimnis / Db Datenbankrecht Datenschutz Personenbezogene Datensaet

## Arbeitsbereich

Dieser Skill bündelt **Db Open Data Portal Nutzungsbedingungen / Db Datenbankrecht Geschaeftsgeheimnis / Db Datenbankrecht Datenschutz Personenbezogene Datensaet**. Wähle zuerst das Modul, dessen Tatsachen die Akte tragen; kombiniere weitere Module nur, wenn dieselbe Frist, Zuständigkeit, Beweislast oder derselbe Output dadurch wirklich klarer wird.

## Arbeitsmodule

| Arbeitsmodul | Fokus |
| --- | --- |
| `db-010-open-data-portal-und-nutzungsbedingungen` | Rechtliche Bewertung von Open-Data-Portalen: Prüft Nutzungsbedingungen nach Open-Data-Richtlinie 2019/1024 (PSI-RL) und deren Umsetzung im IWG, Datenbankherstellerrecht öffentlicher Stellen (§ 87a UrhG), CC-Lizenz-Compliance und Weiterverwendungsrechte. Analysiert Konflikte zwischen Open-Data-Prinzip und urheberrechtlichem Datenbankschutz. |
| `db-011-datenbankrecht-und-geschaeftsgeheimnis` | Analysiert das Verhältnis zwischen Datenbankherstellerrecht (§§ 87a-87e UrhG) und Geschäftsgeheimnisschutz nach GeschGehG / EU-RL 2016/943. Prüft kumulative Schutzfähigkeit von Datenbanken als Geschäftsgeheimnisse, angemessene Schutzmaßnahmen (§ 2 Nr. 1 GeschGehG) und Handlungsoptionen bei unbefugter Offenlegung oder Nutzung. |
| `db-012-datenbankrecht-und-datenschutz-personenbezogene-datensaet` | Analysiert das Verhältnis von Datenbankherstellerrecht (§§ 87a-87e UrhG) und DSGVO bei personenbezogenen Datenbanken: Kumulative Schutzanwendung, Betroffenenrechte (Art. 15-22 DSGVO) vs. Datenbankschutz, Anonymisierungspflichten und Privacy-by-Design (Art. 25 DSGVO). Erstellt datenschutzrechtliches Compliance-Konzept für Datenbankbetreiber. |

## Arbeitsweg

Für **Db Open Data Portal Nutzungsbedingungen / Db Datenbankrecht Geschaeftsgeheimnis / Db Datenbankrecht Datenschutz Personenbezogene Datensaet** zuerst das Arbeitsmodul wählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `datenbankrecht` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; Module nur kombinieren, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Arbeitsmodule im Detail

## 1. `db-010-open-data-portal-und-nutzungsbedingungen`

**Fokus:** Rechtliche Bewertung von Open-Data-Portalen: Prüft Nutzungsbedingungen nach Open-Data-Richtlinie 2019/1024 (PSI-RL) und deren Umsetzung im IWG, Datenbankherstellerrecht öffentlicher Stellen (§ 87a UrhG), CC-Lizenz-Compliance und Weiterverwendungsrechte. Analysiert Konflikte zwischen Open-Data-Prinzip und urheberrechtlichem Datenbankschutz.

# Open-Data-Portal und Nutzungsbedingungen — Datenbankrecht öffentlicher Stellen

## Mandantenfall

- Startup möchte Daten eines behördlichen Open-Data-Portals kommerziell weiterverarbeiten und fragt, ob die angebotene Lizenz (dl-de/by-2-0) dies erlaubt.
- Behörde stellt fest, dass ein privates Unternehmen ihre Open-Data-Datenbank vollständig kopiert und kommerziell anbietet — kann sie dagegen vorgehen?
- Forschungsprojekt kombiniert Open-Data-Bestände verschiedener EU-Länder und muss Lizenz-Kompatibilität und Datenbankschutz klären.

## Erste Schritte

1. Open-Data-Lizenz identifizieren: Welche Lizenz gilt (dl-de/by-2-0, CC BY 4.0, Open Government Licence, Public Domain)? Sind Namensnennung oder Sharealike-Bedingungen vorgesehen?
2. IWG und Open-Data-RL prüfen: Gilt das Informationsweiterverwendungsgesetz (IWG)? Welche Daten sind nach Open-Data-Richtlinie 2019/1024 zur Weiterverwendung freizugeben?
3. Datenbankherstellerrecht öffentlicher Stellen bewerten: Öffentliche Stellen können Hersteller nach § 87a UrhG sein — aber Open-Data-Lizenzen können das Recht einschränken.
4. Lizenzbedingungen auf Weiterverwendungsfall anwenden: Erlaubt die Lizenz kommerzielle Nutzung, Bearbeitung, Weitergabe und Sublizenzierung?
5. Sharealike-Pflichten klären: Gilt Copyleft-Effekt für abgeleitete Datenbanken (ODbL)?
6. Behördliche Ausnahmen prüfen: Ausnahmen nach § 1 Abs. 2 IWG (Sicherheit, Datenschutz, Drittrechte).

## Rechtsrahmen

- Open-Data-Richtlinie 2019/1024 (Nachfolge PSI-RL 2003/98/EG): Weiterverwendungsrecht für Daten öffentlicher Stellen.
- IWG (Informationsweiterverwendungsgesetz): Nationale Umsetzung — Anspruch auf Weiterverwendung, Diskriminierungsverbot, Gebührenrahmen.
- § 87a UrhG: Öffentliche Stellen als mögliche Datenbankherstellerinnen.
- § 5 UrhG: Amtliche Werke (Gesetze, Verordnungen) genießen keinen Urheberrechtsschutz — aber strukturierte Zusammenstellungen können Datenbankschutz genießen.
- CC BY 4.0 / ODbL: Lizenzbedingungen für Open-Data-Veröffentlichungen — Attribution, Sharealike, Bearbeitung.
- Art. 4 Open-Data-RL: Grundsatz der Weiterverwendbarkeit; Ausnahmen bei Schutzrechten Dritter.

## Prüfraster

- Gilt für das Portal das IWG — ist die bereitstellende Stelle eine öffentliche Stelle im Sinne des § 2 IWG?
- Welche Lizenz ist auf das Portal anwendbar, und erlaubt sie die geplante Nutzungsform?
- Besteht ein eigenes Datenbankherstellerrecht der Behörde trotz Open-Data-Lizenz (z. B. für Teile mit wesentlicher Investition)?
- Sind Drittrechte (Urheberrechte einzelner Datenurheber, Persönlichkeitsrechte) in der Lizenz berücksichtigt?
- Gilt ein Copyleft-Effekt (ODbL Sharealike) für das geplante abgeleitete Produkt?
- Sind personenbezogene Daten in der Open-Data-Datenbank enthalten — welche DSGVO-Rechtsgrundlage gilt für Weiterverwendung?
- Hat die bereitstellende Behörde Ausnahmen nach § 1 Abs. 2 IWG geltend gemacht?

## Typische Fallstricke

- „Open Data" bedeutet nicht automatisch „keine Rechte" — Datenbankherstellerrecht und Urheberrecht können trotz Open-Data-Lizenz bestehen.
- Lizenzverstoß (z. B. fehlende Namensnennung bei dl-de/by) kann die Lizenz zum Erlöschen bringen und Haftung auslösen.
- ODbL-Sharealike verpflichtet zur Weitergabe abgeleiteter Datenbanken unter ODbL — wird oft unterschätzt.
- Behörden dürfen nach IWG keine exklusiven Vereinbarungen über Weiterverwendung schließen (Diskriminierungsverbot).
- Nicht alle Behördendaten fallen unter IWG — Ausnahmen für Sicherheit, Gerichte, Rundfunk und Forschungseinrichtungen.

## Output

- Lizenz-Compliance-Check für die geplante Open-Data-Nutzung
- Datenbankherstellerrecht-Prüfmatrix für öffentliche Stellen
- Nutzungsbedingungen-Vorlage für eigene Open-Data-Veröffentlichungen
- Attribution-Pflichten-Checkliste (dl-de/by / CC BY 4.0)
- DSGVO-Kurzprüfung für personenbezogene Open-Data-Bestände

## Quellen

- [Open-Data-Richtlinie 2019/1024 — EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32019L1024)
- [IWG — gesetze-im-internet.de](https://www.gesetze-im-internet.de/iwg/index.html)
- [§ 87a UrhG — dejure.org](https://dejure.org/gesetze/UrhG/87a.html)
- [§ 5 UrhG amtliche Werke — dejure.org](https://dejure.org/gesetze/UrhG/5.html)
- [RL 96/9/EG — EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A31996L0009)
- [Art. 4 Open-Data-RL 2019/1024 — EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32019L1024)

## 2. `db-011-datenbankrecht-und-geschaeftsgeheimnis`

**Fokus:** Analysiert das Verhältnis zwischen Datenbankherstellerrecht (§§ 87a-87e UrhG) und Geschäftsgeheimnisschutz nach GeschGehG / EU-RL 2016/943. Prüft kumulative Schutzfähigkeit von Datenbanken als Geschäftsgeheimnisse, angemessene Schutzmaßnahmen (§ 2 Nr. 1 GeschGehG) und Handlungsoptionen bei unbefugter Offenlegung oder Nutzung.

# Datenbankrecht und Geschäftsgeheimnisschutz — Kumulative Schutzstrategie

## Mandantenfall

- Pharmaunternehmen hat eine Wirkstoffdatenbank aufgebaut, die als Betriebsgeheimnis behandelt wird — jetzt hat ein ausgeschiedener Mitarbeiter Teile weitergegeben.
- Technologieunternehmen fragt, ob seine proprietäre Kundendatenbank als Geschäftsgeheimnis einstufbar ist und welche Schutzmaßnahmen erforderlich sind.
- Startup-Investor will vor Beteiligung prüfen, ob die Datenbank des Zielunternehmens urheberrechtlich und als Geschäftsgeheimnis ausreichend geschützt ist.

## Erste Schritte

1. Datenbankschutz nach UrhG prüfen: §§ 87a ff. (Herstellerrecht) und § 4 Abs. 2 UrhG (Datenbankwerk) — welcher Tatbestand ist erfüllt?
2. Geschäftsgeheimniseigenschaft prüfen: § 2 Nr. 1 GeschGehG — Information nicht allgemein bekannt, wirtschaftlicher Wert, angemessene Geheimhaltungsmaßnahmen.
3. Geheimhaltungsmaßnahmen dokumentieren: Zugangsbeschränkungen, NDA-Klauseln, technische Sicherung, Zugriffsprotokollierung.
4. Verletzungshandlung bestimmen: § 4 GeschGehG — rechtswidrige Erlangung, Nutzung oder Offenlegung; welche Handlung liegt vor?
5. Ansprüche kombinieren: Unterlassung, Schadensersatz, Auskunft und Vernichtung nach GeschGehG §§ 6-8 neben UrhG-Ansprüchen.
6. Beweissicherung: Digitale Forensik, Zugriffslogdaten, Kommunikationsnachweise sichern.

## Rechtsrahmen

- § 2 Nr. 1 GeschGehG: Geschäftsgeheimnis — nicht allgemein bekannt/zugänglich, wirtschaftlicher Wert, angemessene Geheimhaltungsmaßnahmen.
- § 4 GeschGehG: Verbotene Handlungen — rechtswidrige Erlangung, Nutzung oder Offenlegung.
- §§ 6-8 GeschGehG: Unterlassung, Schadensersatz, Auskunft, Vernichtung als Rechtsfolgen.
- §§ 87a-87e UrhG: Datenbankherstellerrecht — kumulativer Schutz neben Geschäftsgeheimnisrecht möglich.
- EU-RL 2016/943: Europäische Grundlage des Geschäftsgeheimnisschutzes — Trade Secrets Directive.
- § 17 UWG a.F. (heute GeschGehG): Verrat von Geschäftsgeheimnissen — Übergangsrecht beachten.

## Prüfraster

- Ist die Datenbankstruktur oder ihr Inhalt nicht allgemein bekannt und wirtschaftlich wertvoll?
- Wurden angemessene Geheimhaltungsmaßnahmen ergriffen (NDA, Zugangsbeschränkungen, Verschlüsselung)?
- Ist die Verletzungshandlung einer der Kategorien des § 4 GeschGehG zuzuordnen?
- Sind Datenbankschutz (§§ 87a ff. UrhG) und Geschäftsgeheimnisschutz (GeschGehG) kumulativ anwendbar?
- Gibt es Beweise für die Verletzungshandlung (Logs, E-Mails, exportierte Dateien)?
- Wurde das Geheimnis durch einen ehemaligen Mitarbeiter oder externen Dienstleister verletzt — welche Vertragsgrundlage besteht?
- Besteht Pflicht zur Abmahnung vor Klageerhebung oder gerichtlichem Eilantrag?

## Typische Fallstricke

- Fehlende schriftliche Geheimhaltungsmaßnahmen (keine NDA, keine Zugriffskontrollen) können den GeschGehG-Schutz vollständig entfallen lassen.
- Daten, die in einer öffentlichen Datenbank erscheinen, verlieren den Geheimnischarakter — auch wenn die eigene Datenbank weiterhin geschützt sein kann.
- GeschGehG und UrhG haben unterschiedliche Verjährungsfristen — Ansprüche dürfen nicht verwechselt werden.
- Reverse Engineering ist nach § 3 Abs. 1 Nr. 2 GeschGehG grundsätzlich erlaubt — der Datenbankschutz kann hier stärker greifen.
- Beweislastverteilung im GeschGehG-Prozess ist komplex; vorprozessuale Dokumentation der Geheimhaltungsmaßnahmen ist entscheidend.

## Output

- Geheimhaltungsmaßnahmen-Audit-Checkliste (§ 2 Nr. 1 GeschGehG)
- Kumulative Schutzrechtskarte (UrhG + GeschGehG)
- Verletzungshandlungsanalyse nach § 4 GeschGehG
- NDA-Klausel mit Datenbankbezug
- Abmahnschreiben (GeschGehG + UrhG kombiniert)

## Quellen

- [GeschGehG — gesetze-im-internet.de](https://www.gesetze-im-internet.de/geschgehg/index.html)
- [§ 87a UrhG — dejure.org](https://dejure.org/gesetze/UrhG/87a.html)
- [EU-RL 2016/943 Trade Secrets — EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32016L0943)
- [§ 4 GeschGehG — dejure.org](https://dejure.org/gesetze/GeschGehG/4.html)
- [§§ 6-8 GeschGehG — dejure.org](https://dejure.org/gesetze/GeschGehG/6.html)
- [§ 307 BGB AGB-Kontrolle — dejure.org](https://dejure.org/gesetze/BGB/307.html)

## 3. `db-012-datenbankrecht-und-datenschutz-personenbezogene-datensaet`

**Fokus:** Analysiert das Verhältnis von Datenbankherstellerrecht (§§ 87a-87e UrhG) und DSGVO bei personenbezogenen Datenbanken: Kumulative Schutzanwendung, Betroffenenrechte (Art. 15-22 DSGVO) vs. Datenbankschutz, Anonymisierungspflichten und Privacy-by-Design (Art. 25 DSGVO). Erstellt datenschutzrechtliches Compliance-Konzept für Datenbankbetreiber.

# Datenbankrecht und DSGVO — Personenbezogene Datenbanken

## Mandantenfall

- CRM-Anbieter betreibt eine personenbezogene Kundendatenbank und fragt, wie er gleichzeitig Datenbankherstellerrecht gegenüber Dritten schützt und DSGVO-Betroffenenrechte erfüllt.
- Unternehmen erhält von einem Betroffenen eine Auskunftsanfrage nach Art. 15 DSGVO für eine komplexe Datenbankstruktur und fragt, ob es dabei das Datenbankherstellerrecht verletzt.
- Startup kauft eine personenbezogene Adressdatenbank und muss prüfen, ob die Nutzung DSGVO-konform ist und welches Datenbankschutzrecht der Verkäufer übertragen hat.

## Erste Schritte

1. Datenbankschutz ermitteln: Welcher Schutztatbestand gilt für die betreffende Datenbank (§ 4 Abs. 2 UrhG / §§ 87a ff. UrhG)?
2. Personenbezug feststellen: Enthält die Datenbank personenbezogene Daten i.S.v. Art. 4 Nr. 1 DSGVO?
3. Rechtsgrundlage nach DSGVO prüfen: Welche Rechtsgrundlage (Art. 6 DSGVO) legitimiert die Verarbeitung der Daten in der Datenbank?
4. Betroffenenrechte und Datenbankschutz abwägen: Auskunft (Art. 15 DSGVO) vs. Schutz von Geschäftsgeheimnissen und Datenbankstrukturen.
5. Privacy-by-Design prüfen: Art. 25 DSGVO — ist die Datenbankstruktur so gestaltet, dass Datenschutzgrundsätze von Beginn an umgesetzt sind?
6. Auftragsverarbeitung und Datenbankrecht klären: Wer ist Verantwortlicher (Art. 4 Nr. 7 DSGVO) und wer Datenbankinhaber?

## Rechtsrahmen

- Art. 4 Nr. 1 DSGVO: Personenbezogene Daten — breites Verständnis; jede Information, die eine natürliche Person identifizierbar macht.
- Art. 6 DSGVO: Rechtsgrundlagen für Verarbeitung — Einwilligung, Vertrag, berechtigtes Interesse.
- Art. 15-22 DSGVO: Betroffenenrechte — Auskunft, Berichtigung, Löschung, Einschränkung, Datenübertragbarkeit, Widerspruch.
- Art. 25 DSGVO: Privacy-by-Design und Privacy-by-Default für Datenbankarchitektur.
- §§ 87a-87e UrhG: Datenbankherstellerrecht schützt die Investition — gilt neben DSGVO, nicht statt ihr.
- EuGH C-203/02 (BHB/William Hill): Auch personenbezogene Datenbanken können Datenbankherstellerrecht genießen.

## Prüfraster

- Sind personenbezogene Daten in der Datenbank enthalten, und auf welcher DSGVO-Rechtsgrundlage werden sie verarbeitet?
- Können Betroffenenrechte (Auskunft, Löschung) erfüllt werden, ohne die Datenbankstruktur als Geschäftsgeheimnis zu offenbaren?
- Sind technische Maßnahmen vorhanden, um Betroffenenrechte umzusetzen (Lösch-Routinen, Auskunftsschnittstellen)?
- Ist die Auftragsverarbeitung (Art. 28 DSGVO) korrekt dokumentiert, wenn ein Dienstleister die Datenbank betreibt?
- Werden bei Datenbankübertragungen (M&A, Lizenz) die DSGVO-Anforderungen für Drittlandtransfers (Art. 44 ff. DSGVO) berücksichtigt?
- Ist eine Datenschutz-Folgenabschätzung (Art. 35 DSGVO) erforderlich — z. B. bei umfangreicher systematischer Überwachung?
- Gibt es einen Interessenkonflikt zwischen Datenminimierungspflicht (Art. 5 Abs. 1 lit. c DSGVO) und dem Ziel, eine umfassende Datenbank aufzubauen?

## Typische Fallstricke

- Auskunftsanspruch nach Art. 15 DSGVO berechtigt Betroffene nicht zur Offenlegung der gesamten Datenbankstruktur — nur zu ihren eigenen Daten.
- Löschpflichten (Art. 17 DSGVO) können Datenbankintegrität stören — technische Lösung ohne Verlust des Datenbankcharakters erforderlich.
- Rechtmäßige Datenbankherstellung schützt nicht vor DSGVO-Bußgeldern bei fehlender Verarbeitungsrechtsgrundlage.
- Datenübertragungsrecht (Art. 20 DSGVO) kann faktisch zur Herausgabe wesentlicher Datenbankteile zwingen — Rechte abwägen.
- Anonymisierte Daten unterliegen nicht mehr der DSGVO, können aber weiterhin Datenbankschutz genießen.

## Output

- Doppelschutz-Karte: DSGVO-Rechtsgrundlage + UrhG-Datenbankschutz je Datenkategorie
- Betroffenenrechte-ohne Preisgabe der Datenbankstruktur
- Privacy-by-Design-Checkliste für Datenbankarchitektur
- Auftragsverarbeitungsvertrag-Klausel zum Datenbankherstellerrecht
- DSGVO-Datenschutz-Folgenabschätzungs-Vorlage für personenbezogene Datenbanken

## Quellen

- [Art. 4 DSGVO — dejure.org](https://dejure.org/gesetze/DSGVO/4.html)
- [Art. 6 DSGVO — dejure.org](https://dejure.org/gesetze/DSGVO/6.html)
- [Art. 15-22 DSGVO — dejure.org](https://dejure.org/gesetze/DSGVO/15.html)
- [Art. 25 DSGVO — dejure.org](https://dejure.org/gesetze/DSGVO/25.html)
- [§ 87a UrhG — dejure.org](https://dejure.org/gesetze/UrhG/87a.html)
- [RL 96/9/EG — EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A31996L0009)
