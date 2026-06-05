# Berufsrecht Notare

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`berufsrecht-notare`) | [`berufsrecht-notare.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/berufsrecht-notare.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Akte Waldwinkel: GmbH-Anteile, Hofgrundstück, Erbfolge und drei Registerrückfragen** (`notariat-alltag-waldwinkel-gmbh-immobilien-erbfall`) | [Gesamt-PDF lesen](../testakten/notariat-alltag-waldwinkel-gmbh-immobilien-erbfall/gesamt-pdf/notariat-alltag-waldwinkel-gmbh-immobilien-erbfall_gesamt.pdf) | [`testakte-notariat-alltag-waldwinkel-gmbh-immobilien-erbfall.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-notariat-alltag-waldwinkel-gmbh-immobilien-erbfall.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Plugin für Notarrecht: BNotO, BeurkG, DONot, Dienstaufsicht, Urkundspflichten, Neutralität, Verwahrung, Amtspflichten, Vertreter/Verwalter, Disziplinarverfahren und notarielle Berufspraxis.

## Worum es geht

Dieses Plugin ist ein experimentelles Arbeits- und Lernwerkzeug. Es soll keine echten Amts-, Mandats-, Steuer-, Prüfungs- oder Berufsgeheimnisse aufnehmen, solange die technische und rechtliche Umgebung dafür nicht ausdrücklich freigegeben ist. Es arbeitet am besten mit anonymisierten, abstrahierten oder synthetischen Fällen und mit Dokumenten, die vor der Nutzung datenschutz- und geheimnisschutzrechtlich geprüft wurden.

## Arbeitsweise

Der Allgemein-Skill startet kurz, sortiert Rolle, Verfahrensstand, Frist, Unterlagen und gewünschtes Arbeitsprodukt und routet dann in die passenden Spezial-Skills. Jeder Skill verlangt Quellenhygiene: Normen, Behördenhinweise, Formulare und Rechtsprechung werden vor tragenden Aussagen live aus amtlichen oder frei zugänglichen Quellen geprüft; keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate.

## Typische Outputs

- Kurzvermerk und Risikoampel
- Checkliste für den nächsten Arbeitstag
- Fragenliste an Behörde, Gericht, Kammer, Mandant, Partei oder Zeugen
- Entwurf für Verfügung, Vermerk, Schriftsatz, Antrag, E-Mail oder Gesprächsleitfaden
- Red-Team-Check gegen Fristenfehler, Zuständigkeitsfehler und Scheingenauigkeit

## Installation

ZIP aus dem aktuellen Release laden und in Claude Code oder Cowork über Customize Plugins installieren.

## Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 50 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `belehrungspflicht-verbraucher-beurkundung` | Notare Belehrungspflicht Und Verbraucher Rechtsprechungscheck U, Notare Beurkundung Im Ausland Bezug Rechtsprechungscheck Und Re, Notare Beurkundungsabbruch Rechtsprechungscheck Und Red Team, Notare Beurkundungsverfahren Vollmacht Rechts... |
| `berufshaftpflicht-berufspflichtverletzung` | Berufshaftpflicht, Berufspflichtverletzung, Beschwerdemanagement, Cross Border: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `berufsrecht-notare-kaltstart-routing` | Allgemeiner Kaltstart und Routing: vertiefter Berufsrechts-Skill für Notare; führt vom ersten Satz oder Dokument in den richtigen Arbeitsmodus, typische Rechtsprechungslinien nur nach Live-Verifikation, Kammerpraxis, Verteidigung und näc... |
| `berufsrecht-notare-notare-amtsenthebung-vermoegensverfall` | Notare Amtsenthebung Vermoegensverfall Kammerantwort Verfah / Notare Amtsenthebung Vermoegensverfall Organisationspflicht / Notare Anderkonto Verwahrung Organisationspflicht Praev / Notare Auszahlungsanweisung Konflikt Kammerantwort Verf... |
| `berufsrecht-notare-notare-datenschutzpanne-notariat` | Notare Datenschutzpanne Notariat Kaltstart Faktenmatrix / Notare Dienstaufsicht Beschwerde Kaltstart Faktenmatrix / Notare Disziplinarverfahren Notar Kaltstart Faktenmatrix / Notare Dolmetscher Sprachrisiko Kaltstart Faktenmatrix / 1 wei... |
| `berufsrecht-notare-notare-fernbeglaubigung-videoverfahren` | Notare Fernbeglaubigung Videoverfahren Rechtsprechungscheck / Notare Geldwaesche Sanktionslisten Rechtsprechungscheck Red / Notare Geldwaeschepruefung Immobilienkauf Rechtsprechungscheck / Notare Grundschuld Sicherungszweck Rechtsprechun... |
| `berufsrecht-notare-notare-fernbeglaubigung-videoverfahren-02` | Notare Fernbeglaubigung Videoverfahren Kammerantwort Ve / Notare Fernbeglaubigung Videoverfahren Organisationspflicht / Notare Geldwaesche Sanktionslisten Kammerantwort Verfahrens / Notare Identitaetspruefung Ausweis Kammerantwort Verfah... |
| `berufsrecht-notare-notare-urkundensammlung-verwahrung` | Notare Urkundensammlung Verwahrung Organisationspflicht / Notare Verbraucherwiderruf Beurkundung Kammerantwort Ve / Notare Verbraucherwiderruf Beurkundung Organisationspflicht / Notare Verschwiegenheit Datenraum Kammerantwort Verfahr / 1... |
| `beurkundung-ausland-beurkundungsabbruch` | Notare Beurkundung Im Ausland Bezug Kammerantwort Und Verfahren, Notare Beurkundungsabbruch Kammerantwort Und Verfahrensstrategi, Notare Beurkundungsverfahren Vollmacht Kammerantwort Und Verfah, Notare Beurkundungsverfahren Vollmacht Org... |
| `datenraum-dokumentenintake-aktenlog` | Datenraum, Dokumentenintake Und Aktenlog, Entscheidungsvorlage, Fachbezeichnung: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `datenschutzpanne-notariat-dienstaufsicht` | Notare Datenschutzpanne Notariat Kammerantwort Und Verfahrensst, Notare Dienstaufsicht Beschwerde Kammerantwort Und Verfahrensst, Notare Disziplinarverfahren Notar Kammerantwort Und Verfahrenss, Notare Disziplinarverfahren Notar Organisa... |
| `geldwaesche-kyc-homeoffice-honorar-gebuehren` | Geldwaesche Und Kyc, Homeoffice, Honorar Gebuehren Verguetung, Interessenkollision: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `geldwaesche-sanktionslisten-haftpflicht` | Notare Geldwaesche Sanktionslisten Organisationspflicht Und Pra, Notare Haftpflicht Und Schadenmeldung Kammerantwort Und Verfahr, Notare Haftpflicht Und Schadenmeldung Organisationspflicht Und, Aktenfuehrung: wählt den konkreten Prüfpfad... |
| `grundschuld-sicherungszweck-haftpflicht` | Notare Grundschuld Und Sicherungszweck Kaltstart Und Faktenmatr, Notare Haftpflicht Und Schadenmeldung Kaltstart Und Faktenmatri, Notare Handelsregisteranmeldung Fehler Kaltstart Und Faktenmatr, Notare Identitaetspruefung Ausweis Kaltsta... |
| `it-cloud-kammeraufsicht-ruege` | It Cloud Ki Und Outsourcing, Kammeraufsicht Und Ruege, Kanzleiorganisation, Kooperation Mit Anderen Berufen: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `ki-notariat-kollegialitaet-kammerantwort` | Notare Ki Im Notariat Grenzen Kammerantwort Und Verfahrensstrat, Notare Kollegialitaet Und Zustaendigkeit Kammerantwort Und Verf, Notare Kollegialitaet Und Zustaendigkeit Organisationspflicht U, Notare Notarkammer Anfrage Kammerantwort U... |
| `kostenrechnung-gnotkg-nebentaetigkeit` | Notare Kostenrechnung Gnotkg Beschwerde Rechtsprechungscheck Un, Notare Nebentaetigkeit Und Interessenkollision Rechtsprechungsc, Notare Notaranderkonto Auszahlungsreife Rechtsprechungscheck Un, Notare Notarielle Verwahrung Von Daten Rec... |
| `mandatsannahme-mandatsbeendigung-mitarbeiter` | Mandatsannahme, Mandatsbeendigung, Mitarbeiter, Nebenberuf: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `notar-gesellschafterliste-register` | Notare Gesellschafterliste Nach Auslandsinsolvenz Kammerantwort, Notare Gesellschafterliste Nach Auslandsinsolvenz Organisations, Notare Gesellschafterliste Nach Auslandsinsolvenz Rechtsprechun, Notare Grundschuld Und Sicherungszweck Kam... |
| `notaranderkonto-auszahlungsreife` | Notare Notaranderkonto Auszahlungsreife Kammerantwort Und Verfa, Notare Notaranderkonto Auszahlungsreife Organisationspflicht Un, Notare Notarielle Verwahrung Von Daten Kammerantwort Und Verfah, Notare Notarielle Verwahrung Von Daten Org... |
| `notare-amtsenthebung-vermoegensverfall` | Notare: amtsenthebung vermögensverfall - Kaltstart mit Faktenmatrix, Risikoampel und fehlenden Unterlagen; mit Live-Normencheck, Kammerlogik, Verhältnismäßigkeit, Belegplan und nächstem Schritt. |
| `notare-anderkonto-verwahrung-faktenmatrix` | Notare: anderkonto und verwahrung - Kaltstart mit Faktenmatrix, Risikoampel und fehlenden Unterlagen; mit Live-Normencheck, Kammerlogik, Verhältnismäßigkeit, Belegplan und nächstem Schritt. |
| `notare-auszahlungsanweisung-faktenmatrix` | Notare: auszahlungsanweisung konflikt - Kaltstart mit Faktenmatrix, Risikoampel und fehlenden Unterlagen; mit Live-Normencheck, Kammerlogik, Verhältnismäßigkeit, Belegplan und nächstem Schritt. |
| `notare-belehrungspflicht-verbraucher` | Notare Belehrungspflicht Und Verbraucher Kammerantwort Und Verf, Notare Belehrungspflicht Und Verbraucher Organisationspflicht U, Notare Beurkundung Im Ausland Bezug Organisationspflicht Und Pr, Notare Beurkundungsabbruch Organisationspf... |
| `notare-belehrungspflicht-verbraucher-faktenma` | Notare: belehrungspflicht und verbraucher - Kaltstart mit Faktenmatrix, Risikoampel und fehlenden Unterlagen; mit Live-Normencheck, Kammerlogik, Verhältnismäßigkeit, Belegplan und nächstem Schritt. |
| `notare-beurkundung-ausland-faktenmatrix` | Notare: beurkundung im ausland bezug - Kaltstart mit Faktenmatrix, Risikoampel und fehlenden Unterlagen; mit Live-Normencheck, Kammerlogik, Verhältnismäßigkeit, Belegplan und nächstem Schritt. |
| `notare-beurkundungsabbruch-faktenmatrix` | Notare: beurkundungsabbruch - Kaltstart mit Faktenmatrix, Risikoampel und fehlenden Unterlagen; mit Live-Normencheck, Kammerlogik, Verhältnismäßigkeit, Belegplan und nächstem Schritt. |
| `notare-beurkundungsverfahren-vollmacht` | Notare: beurkundungsverfahren vollmacht - Kaltstart mit Faktenmatrix, Risikoampel und fehlenden Unterlagen; mit Live-Normencheck, Kammerlogik, Verhältnismäßigkeit, Belegplan und nächstem Schritt. |
| `notare-datenschutzpanne-notariat` | Notare Datenschutzpanne Notariat Organisationspflicht Und Praev, Notare Dienstaufsicht Beschwerde Organisationspflicht Und Praev, Notare Dolmetscher Und Sprachrisiko Organisationspflicht Und Pr, Notare Geldwaeschepruefung Immobilienkauf... |
| `notare-dienstaufsicht-beschwerde` | Notare Dienstaufsicht Beschwerde Rechtsprechungscheck Und Red T, Notare Disziplinarverfahren Notar Rechtsprechungscheck Und Red, Notare Dolmetscher Und Sprachrisiko Rechtsprechungscheck Und Re, Notare Erbvertrag Testament Belehrung Recht... |
| `notare-fernbeglaubigung-videoverfahren` | Notare Fernbeglaubigung Und Videoverfahren Kaltstart Und Fakten, Notare Geldwaesche Sanktionslisten Kaltstart Und Faktenmatrix, Notare Geldwaeschepruefung Immobilienkauf Kaltstart Und Faktenm, Notare Gesellschafterliste Nach Auslandsinso... |
| `notare-grundschuld-sicherungszweck` | Notare Grundschuld Und Sicherungszweck Organisationspflicht Und, Notare Handelsregisteranmeldung Fehler Kammerantwort Und Verfah, Notare Handelsregisteranmeldung Fehler Organisationspflicht Und, Notare Identitaetspruefung Ausweis Organis... |
| `notare-handelsregisteranmeldung-fehler` | Notare Handelsregisteranmeldung Fehler Rechtsprechungscheck Und, Notare Identitaetspruefung Ausweis Rechtsprechungscheck Und Red, Notare Ki Im Notariat Grenzen Rechtsprechungscheck Und Red Team, Notare Kollegialitaet Und Zustaendigkeit R... |
| `notare-kollegialitaet-faktenma-kostenrechnung` | Notare Kollegialitaet Und Zustaendigkeit Kaltstart Und Faktenma, Notare Kostenrechnung Gnotkg Beschwerde Kaltstart Und Faktenmat, Notare Nebentaetigkeit Und Interessenkollision Kaltstart Und Fa, Notare Notaranderkonto Auszahlungsreife Ka... |
| `notare-kostenrechnung-gnotkg-beschwerde` | Notare Kostenrechnung Gnotkg Beschwerde Kammerantwort Und Verfa, Notare Kostenrechnung Gnotkg Beschwerde Organisationspflicht Un, Notare Nebentaetigkeit Und Interessenkollision Kammerantwort Un, Notare Nebentaetigkeit Und Interessenkolli... |
| `notare-notarvertretung-notariatsverwalter` | Notare Notarvertretung Und Notariatsverwalter Rechtsprechungsch, Notare Qualitaetsmanagement Im Notariat Rechtsprechungscheck Un, Notare Rechtsmittel Gegen Dienstaufsicht Rechtsprechungscheck U, Notare Share Deal Closing Notar Rechtsprec... |
| `notare-rechtsmittel-dienstaufsicht` | Notare Rechtsmittel Gegen Dienstaufsicht Kammerantwort Und Verf, Notare Rechtsmittel Gegen Dienstaufsicht Organisationspflicht U, Notare Share Deal Closing Notar Organisationspflicht Und Praeve, Notare Umwandlung Und Registersperre Kamme... |
| `notare-umwandlung-registersperre` | Notare Umwandlung Und Registersperre Rechtsprechungscheck Und R, Notare Unparteilichkeit Bei Familiengesellschaft Rechtsprechung, Notare Urkundenrolle Fehler Rechtsprechungscheck Und Red Team, Notare Urkundensammlung Und Verwahrung Recht... |
| `notare-urkundensammlung-verwahrung` | Notare Urkundensammlung Und Verwahrung Kaltstart Und Faktenmatr, Notare Verbraucherwiderruf Und Beurkundung Kaltstart Und Fakten, Notare Verschwiegenheit Und Datenraum Kaltstart Und Faktenmatri, Notare Verwahrungsanzeige Und Gnotkg Kalts... |
| `notare-werbung-protokoll-nachbereitung` | Notare Werbung Und Amtsbezeichnung Organisationspflicht Und Pra, Protokoll Und Nachbereitung, Rechnungseinzug, Red Team Qualitygate: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nä... |
| `notarielle-verwahrung-notarkammer-anfrage` | Notare Notarielle Verwahrung Von Daten Kaltstart Und Faktenmatr, Notare Notarkammer Anfrage Kaltstart Und Faktenmatrix, Notare Notarvertretung Und Notariatsverwalter Kaltstart Und Fak, Notare Qualitaetsmanagement Im Notariat Kaltstart Un... |
| `quellen-rechtsprechungscheck-berufsgericht` | Quellen Und Rechtsprechungscheck, Berufsgericht Und Disziplinarverfahren, Frist Und Zustaendigkeit Cockpit, Fristenkontrolle: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten... |
| `share-deal-umwandlung-registersperre` | Notare Share Deal Closing Notar Kaltstart Und Faktenmatrix, Notare Umwandlung Und Registersperre Kaltstart Und Faktenmatrix, Notare Unparteilichkeit Bei Familiengesellschaft Kaltstart Und, Notare Urkundenrolle Fehler Kaltstart Und Fakten... |
| `unparteilichkeit-familiengesellschaft` | Notare Unparteilichkeit Bei Familiengesellschaft Kammerantwort, Notare Unparteilichkeit Bei Familiengesellschaft Organisationsp, Notare Urkundenrolle Fehler Organisationspflicht Und Praeventio, Notare Urkundensammlung Und Verwahrung Kamm... |
| `urkundenrolle-fehler-werbung-amtsbezeichnung` | Notare Urkundenrolle Fehler Kammerantwort Und Verfahrensstrateg, Notare Werbung Und Amtsbezeichnung Kammerantwort Und Verfahrens, Notare Erbvertrag Testament Belehrung Kammerantwort Und Verfahr, Notare Erbvertrag Testament Belehrung Orga... |
| `vermerk-mustertext-sitzungs` | Schriftsatz Vermerk Und Mustertext, Sitzungs Und Terminvorbereitung, Syndikus Oder Inhouse, Treuhand Oder Fremdgeld: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbar... |
| `verschwiegenheit-datenraum-verwahrungsanzeige` | Notare Verschwiegenheit Und Datenraum Rechtsprechungscheck Und, Notare Verwahrungsanzeige Und Gnotkg Rechtsprechungscheck Und R, Notare Vollzugsueberwachung Grundbuch Rechtsprechungscheck Und, Notare Werbung Und Amtsbezeichnung Rechtspre... |
| `verschwiegenheit-geheimnisschutz-werbung` | Verschwiegenheit Und Geheimnisschutz, Werbung Und Aussenauftritt, Zulassung Bestellung Und Register: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `verwahrungsanzeige-gnotkg` | Notare Verwahrungsanzeige Und Gnotkg Kammerantwort Und Verfahre, Notare Verwahrungsanzeige Und Gnotkg Organisationspflicht Und P, Notare Vollzugsueberwachung Grundbuch Kammerantwort Und Verfahr, Notare Vollzugsueberwachung Grundbuch Orga... |
| `werbung-amtsbezeichnung-amtsenthebung` | Notare Werbung Und Amtsbezeichnung Kaltstart Und Faktenmatrix, Notare Amtsenthebung Vermoegensverfall Rechtsprechungscheck Und, Notare Anderkonto Und Verwahrung Rechtsprechungscheck Und Red T, Notare Auszahlungsanweisung Konflikt Rechtsp... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
