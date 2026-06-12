# Berufsgerichtliche Verfahren Freie Berufe

<!-- BEGIN plugin-sofort-download-section (autogen) -->

<!-- BEGIN megaprompt-und-vorlagen (autogen) -->
## Experimentell: dieses Plugin auch ohne Claude Code

### Megaprompt (alle Kern-Skills in einer Datei)

Das Plugin gibt es zusaetzlich als **single-file Megaprompt** — ein experimentelles Markdown, das die wichtigsten Skills in einer einzigen Datei buendelt. Drop das in einen Chat ohne Claude-Code-Integration; der Agent erhaelt damit die gebuendelten Skill-Anweisungen.

- **Direkt-Download**: [`berufsgerichtliche-verfahren-freie-berufe.md`](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/testakten/megaprompts/berufsgerichtliche-verfahren-freie-berufe.md) (42 KB)
- Im Repo: [`testakten/megaprompts/berufsgerichtliche-verfahren-freie-berufe.md`](../testakten/megaprompts/berufsgerichtliche-verfahren-freie-berufe.md)

*Keine Haftung, keine Gewaehr — Megaprompts sind eine Best-Effort-Kompression, kein vollwertiger Plugin-Ersatz.*

<!-- END megaprompt-und-vorlagen (autogen) -->

## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`berufsgerichtliche-verfahren-freie-berufe`) | [`berufsgerichtliche-verfahren-freie-berufe.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/berufsgerichtliche-verfahren-freie-berufe.zip) |

Dieses Plugin hat (bewusst) keine eigene Demonstrations-Akte.

<!-- END plugin-sofort-download-section (autogen) -->

Plugin für anwaltsgerichtliche und berufsgerichtliche Verfahren gegen Anwälte, Patentanwälte, Steuerberater, Wirtschaftsprüfer und Notare: Kammeraufsicht, Rüge, Disziplinarverfahren, Zulassung, Vermögensverfall, beA, Werbung, Sachlichkeit und Rechtsmittel.

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

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 95 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `aktenherausgabe-zurueckbehaltungsrecht-praevention` | Aktenherausgabe und Zurückbehaltungsrecht (Präventions- und Organisationspaket): steuert Herausgabe der Handakte, digitale Akte, Zurückbehaltungsrecht, Datenschutz und Fristensicherung mit berufsrechtlicher Quellenprüfung, Verhältnismäßi... |
| `aktenherausgabe-zurueckbehaltungsrecht-verteidigung` | Aktenherausgabe und Zurückbehaltungsrecht (Verteidigungs- und Kammerantwort): steuert Herausgabe der Handakte, digitale Akte, Zurückbehaltungsrecht, Datenschutz und Fristensicherung mit berufsrechtlicher Quellenprüfung, Verhältnismäßigke... |
| `anwaltsgericht-brao-ueberblick` | Anwaltsgericht nach BRAO Überblick: prüft Rüge, anwaltsgerichtliches Verfahren, Kammer, Generalstaatsanwaltschaft, Maßnahmen und Rechtsmittel in berufsgerichtlichen Verfahren freier Berufe; mit Normencheck, Aktenlog, Verteidigungslinie,... |
| `bea-nicht-berufsgericht` | beA nicht in Betrieb (Präventions- und Organisationspaket): steuert unterlassene beA-Einrichtung, Zustellungsprobleme, Fristenversäumnis und Kammeraufsicht mit berufsrechtlicher Quellenprüfung, Verhältnismäßigkeit, Aktenlog und verwertba... |
| `bea-nicht-in-betrieb-verteidigung` | beA nicht in Betrieb (Verteidigungs- und Kammerantwort): steuert unterlassene beA-Einrichtung, Zustellungsprobleme, Fristenversäumnis und Kammeraufsicht mit berufsrechtlicher Quellenprüfung, Verhältnismäßigkeit, Aktenlog und verwertbarem... |
| `bea-nutzungspflichten-kanzleisitz` | beA und elektronische Kommunikation: prüft aktive/passive Nutzungspflichten, Fristen, Wiedereinsetzung und Kammerkommunikation in berufsgerichtlichen Verfahren freier Berufe; mit Normencheck, Aktenlog, Verteidigungslinie, Verhältnismäßig... |
| `berufsgericht-anschuldigungsschrift-praevention` | Berufsgericht Anschuldigungsschrift (Präventions- und Organisationspaket): steuert Anschuldigungsschrift, Tatvorwurf, Verfahrenshindernisse, Beweisanträge und Terminstrategie mit berufsrechtlicher Quellenprüfung, Verhältnismäßigkeit, Akt... |
| `berufsgericht-anschuldigungsschrift-verteidigung` | Berufsgericht Anschuldigungsschrift (Verteidigungs- und Kammerantwort): steuert Anschuldigungsschrift, Tatvorwurf, Verfahrenshindernisse, Beweisanträge und Terminstrategie mit berufsrechtlicher Quellenprüfung, Verhältnismäßigkeit, Aktenl... |
| `berufsgericht-beweisaufnahme` | Berufsgericht Beweisaufnahme (Präventions- und Organisationspaket): steuert Zeugen, Urkunden, Mandatsgeheimnis, Kammerakte und Beweisanträge im Berufsverfahren mit berufsrechtlicher Quellenprüfung, Verhältnismäßigkeit, Aktenlog und verwe... |
| `berufsgericht-beweisaufnahme-verteidigung` | Berufsgericht Beweisaufnahme (Verteidigungs- und Kammerantwort): steuert Zeugen, Urkunden, Mandatsgeheimnis, Kammerakte und Beweisanträge im Berufsverfahren mit berufsrechtlicher Quellenprüfung, Verhältnismäßigkeit, Aktenlog und verwertb... |
| `berufsgericht-freie-berufe-dokumente-aktenlog` | Dokumentenintake und Aktenlog: prüft ordnet Uploads, Eingangspost, Aktenbestandteile und fehlende Unterlagen in berufsgerichtlichen Verfahren freier Berufe; mit Normencheck, Aktenlog, Verteidigungslinie, Verhältnismäßigkeit und Rechtsmit... |
| `berufsgericht-freie-berufe-kaltstart-routing` | Allgemeiner Kaltstart und Routing: führt vom ersten Satz oder Dokument in den richtigen Arbeitsmodus in berufsgerichtlichen Verfahren freier Berufe; mit Normencheck, Aktenlog, Verteidigungslinie, Verhältnismäßigkeit und Rechtsmittelspur. |
| `berufsgericht-freie-berufe-quellen-rspr-fristen` | Quellen- und Rechtsprechungscheck: prüft verhindert Blindzitate und zwingt zu amtlich oder frei prüfbaren Quellen in berufsgerichtlichen Verfahren freier Berufe; mit Normencheck, Aktenlog, Verteidigungslinie, Verhältnismäßigkeit und Rech... |
| `berufsgesellschaft-compliance-praevention` | Berufsgesellschaft Compliance (Präventions- und Organisationspaket): steuert Berufsausübungsgesellschaft, Compliance-System, Organpflichten, Zulassung und Aufsicht mit berufsrechtlicher Quellenprüfung, Verhältnismäßigkeit, Aktenlog und v... |
| `berufsgesellschaft-compliance-verteidigung` | Berufsgesellschaft Compliance (Verteidigungs- und Kammerantwort): steuert Berufsausübungsgesellschaft, Compliance-System, Organpflichten, Zulassung und Aufsicht mit berufsrechtlicher Quellenprüfung, Verhältnismäßigkeit, Aktenlog und verw... |
| `berufspflicht-und-verhaeltnismaessigkeit-verteidigung` | Berufspflicht und Verhältnismäßigkeit (Verteidigungs- und Kammerantwort): steuert Pflichtverletzung, Schuld, Sanktion, Wiederholungsgefahr und mildere Mittel mit berufsrechtlicher Quellenprüfung, Verhältnismäßigkeit, Aktenlog und verwert... |
| `berufspflicht-verhaeltnismaessigkeit` | Berufspflicht und Verhältnismäßigkeit (Präventions- und Organisationspaket): steuert Pflichtverletzung, Schuld, Sanktion, Wiederholungsgefahr und mildere Mittel mit berufsrechtlicher Quellenprüfung, Verhältnismäßigkeit, Aktenlog und verw... |
| `berufsrecht-ki-nutzung-praevention` | Berufsrecht KI-Nutzung (Präventions- und Organisationspaket): steuert KI-Einsatz in Kanzlei/Praxis, Mandatsdaten, Kontrolle, Transparenz und Dokumentation mit berufsrechtlicher Quellenprüfung, Verhältnismäßigkeit, Aktenlog und verwertbar... |
| `berufsrecht-ki-nutzung-verteidigung` | Berufsrecht KI-Nutzung (Verteidigungs- und Kammerantwort): steuert KI-Einsatz in Kanzlei/Praxis, Mandatsdaten, Kontrolle, Transparenz und Dokumentation mit berufsrechtlicher Quellenprüfung, Verhältnismäßigkeit, Aktenlog und verwertbarem... |
| `berufsverbot-sofortvollzug-verteidigung` | Berufsverbot und Sofortvollzug (Präventions- und Organisationspaket): steuert vorläufige Maßnahmen, Sofortvollzug, existenzielle Folgen, Eilrechtsschutz und Kanzleifortführung mit berufsrechtlicher Quellenprüfung, Verhältnismäßigkeit, Ak... |
| `berufsverbot-und-sofortvollzug-verteidigung` | Berufsverbot und Sofortvollzug (Verteidigungs- und Kammerantwort): steuert vorläufige Maßnahmen, Sofortvollzug, existenzielle Folgen, Eilrechtsschutz und Kanzleifortführung mit berufsrechtlicher Quellenprüfung, Verhältnismäßigkeit, Akten... |
| `datenpanne-berufstraeger-praevention` | Datenpanne beim Berufsträger (Präventions- und Organisationspaket): steuert verlorener Laptop, Fehlversand, Cloud-Leak, Mandatsgeheimnis und Meldestrategie mit berufsrechtlicher Quellenprüfung, Verhältnismäßigkeit, Aktenlog und verwertba... |
| `datenpanne-berufstraeger-verteidigung` | Datenpanne beim Berufsträger (Verteidigungs- und Kammerantwort): steuert verlorener Laptop, Fehlversand, Cloud-Leak, Mandatsgeheimnis und Meldestrategie mit berufsrechtlicher Quellenprüfung, Verhältnismäßigkeit, Aktenlog und verwertbarem... |
| `dienstaufsicht-notar-beschwerde-verteidigung` | Dienstaufsicht Notar Beschwerde (Verteidigungs- und Kammerantwort): steuert Dienstaufsichtsbeschwerde, Prüfungsmaßstab, Akteneinsicht, Stellungnahme und Rechtsbehelf mit berufsrechtlicher Quellenprüfung, Verhältnismäßigkeit, Aktenlog und... |
| `entscheidungsvorlage` | Entscheidungsvorlage: prüft macht aus der Prüfung eine Entscheidung mit Optionen, Risiken und Empfehlung in berufsgerichtlichen Verfahren freier Berufe; mit Normencheck, Aktenlog, Verteidigungslinie, Verhältnismäßigkeit und Rechtsmittels... |
| `fremdgeld-anderkonto-pflicht-praevention` | Fremdgeld und Anderkonto (Präventions- und Organisationspaket): steuert Fremdgeldverwahrung, verspätete Auskehrung, Aufrechnung, Treuhandauflage und Kontenorganisation mit berufsrechtlicher Quellenprüfung, Verhältnismäßigkeit, Aktenlog u... |
| `fremdgeld-anderkonto-pflicht-verteidigung` | Fremdgeld und Anderkonto (Verteidigungs- und Kammerantwort): steuert Fremdgeldverwahrung, verspätete Auskehrung, Aufrechnung, Treuhandauflage und Kontenorganisation mit berufsrechtlicher Quellenprüfung, Verhältnismäßigkeit, Aktenlog und... |
| `frist-und-zustaendigkeit-cockpit` | Fristen- und Zuständigkeitscockpit: prüft macht Fristen, Zuständigkeiten, Rechtsbehelfe und Vorfristen sofort sichtbar in berufsgerichtlichen Verfahren freier Berufe; mit Normencheck, Aktenlog, Verteidigungslinie, Verhältnismäßigkeit und... |
| `geldwaeschepflicht-kanzlei` | Geldwäschepflichten der Kanzlei (Präventions- und Organisationspaket): steuert GwG-Pflichten bei Immobilie, Gesellschaftsrecht, Treuhand und Verdachtsmeldung mit berufsrechtlicher Quellenprüfung, Verhältnismäßigkeit, Aktenlog und verwert... |
| `geldwaeschepflicht-kanzlei-verteidigung` | Geldwäschepflichten der Kanzlei (Verteidigungs- und Kammerantwort): steuert GwG-Pflichten bei Immobilie, Gesellschaftsrecht, Treuhand und Verdachtsmeldung mit berufsrechtlicher Quellenprüfung, Verhältnismäßigkeit, Aktenlog und verwertbar... |
| `haftpflichtdeckung-berufsverfahren-praevention` | Haftpflichtdeckung im Berufsverfahren (Präventions- und Organisationspaket): steuert Berufshaftpflicht, Deckungsanzeige, Ausschluss, Selbstbehalt und Interessenkonflikt mit berufsrechtlicher Quellenprüfung, Verhältnismäßigkeit, Aktenlog... |
| `haftpflichtdeckung-berufsverfahren-verteidigung` | Haftpflichtdeckung im Berufsverfahren (Verteidigungs- und Kammerantwort): steuert Berufshaftpflicht, Deckungsanzeige, Ausschluss, Selbstbehalt und Interessenkonflikt mit berufsrechtlicher Quellenprüfung, Verhältnismäßigkeit, Aktenlog und... |
| `honorarvereinbarung-erfolgshonorar-praevention` | Honorarvereinbarung und Erfolgshonorar (Präventions- und Organisationspaket): steuert Vergütungsvereinbarung, Erfolgshonorar, Transparenz, RVG-Abweichung und Rückforderung mit berufsrechtlicher Quellenprüfung, Verhältnismäßigkeit, Aktenl... |
| `honorarvereinbarung-erfolgshonorar-verteidigung` | Honorarvereinbarung und Erfolgshonorar (Verteidigungs- und Kammerantwort): steuert Vergütungsvereinbarung, Erfolgshonorar, Transparenz, RVG-Abweichung und Rückforderung mit berufsrechtlicher Quellenprüfung, Verhältnismäßigkeit, Aktenlog... |
| `interessenkollision-mehrfachvertretung` | Interessenkollision Mehrfachvertretung (Präventions- und Organisationspaket): steuert Verbot widerstreitender Interessen, Sozietät, Vorbefassung und Mandatsniederlegung mit berufsrechtlicher Quellenprüfung, Verhältnismäßigkeit, Aktenlog... |
| `interessenkollision-mehrfachvertretung-verteidigung` | Interessenkollision Mehrfachvertretung (Verteidigungs- und Kammerantwort): steuert Verbot widerstreitender Interessen, Sozietät, Vorbefassung und Mandatsniederlegung mit berufsrechtlicher Quellenprüfung, Verhältnismäßigkeit, Aktenlog und... |
| `kammeranhoerung-fristverlaengerung` | Kammeranhörung Fristverlängerung (Präventions- und Organisationspaket): steuert erste Kammeranhörung, Fristverlängerung, Akteneinsicht, Schweige-/Mitwirkungslinie mit berufsrechtlicher Quellenprüfung, Verhältnismäßigkeit, Aktenlog und ve... |
| `kammeranhoerung-fristverlaengerung-verteidigung` | Kammeranhörung Fristverlängerung (Verteidigungs- und Kammerantwort): steuert erste Kammeranhörung, Fristverlängerung, Akteneinsicht, Schweige-/Mitwirkungslinie mit berufsrechtlicher Quellenprüfung, Verhältnismäßigkeit, Aktenlog und verwe... |
| `kanzleisitz-und-erreichbarkeit-praevention` | Kanzleisitz und Erreichbarkeit (Präventions- und Organisationspaket): steuert Kanzleisitz, Briefkasten, virtuelle Kanzlei, Zustellbarkeit und berufsrechtliche Organisation mit berufsrechtlicher Quellenprüfung, Verhältnismäßigkeit, Aktenl... |
| `kanzleisitz-und-erreichbarkeit-verteidigung` | Kanzleisitz und Erreichbarkeit (Verteidigungs- und Kammerantwort): steuert Kanzleisitz, Briefkasten, virtuelle Kanzlei, Zustellbarkeit und berufsrechtliche Organisation mit berufsrechtlicher Quellenprüfung, Verhältnismäßigkeit, Aktenlog... |
| `kanzleisitz-und-zustellbarkeit` | Kanzleisitz und Zustellbarkeit: prüft Kanzleisitz, Zustellungsbevollmächtigter, Erreichbarkeit und Registerdaten prüfen in berufsgerichtlichen Verfahren freier Berufe; mit Normencheck, Aktenlog, Verteidigungslinie, Verhältnismäßigkeit un... |
| `kollegenbeleidigung-strafbarkeit` | Kollegenbeleidigung und Strafbarkeit (Präventions- und Organisationspaket): steuert Grenze zwischen harter Interessenvertretung, Beleidigung, übler Nachrede und Berufsrechtsverstoß mit berufsrechtlicher Quellenprüfung, Verhältnismäßigkei... |
| `kollegenbeleidigung-und-strafbarkeit-verteidigung` | Kollegenbeleidigung und Strafbarkeit (Verteidigungs- und Kammerantwort): steuert Grenze zwischen harter Interessenvertretung, Beleidigung, übler Nachrede und Berufsrechtsverstoß mit berufsrechtlicher Quellenprüfung, Verhältnismäßigkeit,... |
| `kollegenbeleidigung-unsachlichkeit` | Kollegenbeleidigung und Unsachlichkeit: prüft Sachlichkeitsgebot, Meinungsfreiheit, Verhältnismäßigkeit und Verteidigungslinie in berufsgerichtlichen Verfahren freier Berufe; mit Normencheck, Aktenlog, Verteidigungslinie, Verhältnismäßig... |
| `mandanten-beteiligtenkommunikation-notar` | Beteiligtenkommunikation: prüft übersetzt das Ergebnis in klare, taktisch sichere Kommunikation in berufsgerichtlichen Verfahren freier Berufe; mit Normencheck, Aktenlog, Verteidigungslinie, Verhältnismäßigkeit und Rechtsmittelspur im Be... |
| `mandatskuendigung-zur-unzeit-praevention` | Mandatskündigung zur Unzeit (Präventions- und Organisationspaket): steuert Mandatsniederlegung, Fristen, Gerichtstermin, Vorschuss, Vertrauensverlust und Haftungsrisiko mit berufsrechtlicher Quellenprüfung, Verhältnismäßigkeit, Aktenlog... |
| `mandatskuendigung-zur-unzeit-verteidigung` | Mandatskündigung zur Unzeit (Verteidigungs- und Kammerantwort): steuert Mandatsniederlegung, Fristen, Gerichtstermin, Vorschuss, Vertrauensverlust und Haftungsrisiko mit berufsrechtlicher Quellenprüfung, Verhältnismäßigkeit, Aktenlog und... |
| `notar-anderkonto-auszahlungsreife` | Notaranderkonto Auszahlungsreife (Präventions- und Organisationspaket): steuert Treuhandauflage, Anderkonto, Auszahlungsreife, Vormerkung und Insolvenzrisiko mit berufsrechtlicher Quellenprüfung, Verhältnismäßigkeit, Aktenlog und verwert... |
| `notar-anderkonto-auszahlungsreife-verteidigung` | Notaranderkonto Auszahlungsreife (Verteidigungs- und Kammerantwort): steuert Treuhandauflage, Anderkonto, Auszahlungsreife, Vormerkung und Insolvenzrisiko mit berufsrechtlicher Quellenprüfung, Verhältnismäßigkeit, Aktenlog und verwertbar... |
| `notar-disziplinar-bnoto` | Notar Disziplinarverfahren BNotO: prüft Dienstaufsicht, Disziplinarverfahren, Amtsenthebung, Verwahrung und Urkundspflichten in berufsgerichtlichen Verfahren freier Berufe; mit Normencheck, Aktenlog, Verteidigungslinie, Verhältnismäßigke... |
| `notar-geldwaesche-immobilie-praevention` | Notar Geldwäsche Immobilie (Präventions- und Organisationspaket): steuert Immobilienkauf, Barzahlungsverbot, wirtschaftlich Berechtigter, Verdachtsmeldung und Beurkundung mit berufsrechtlicher Quellenprüfung, Verhältnismäßigkeit, Aktenlo... |
| `notar-geldwaesche-immobilie-verteidigung` | Notar Geldwäsche Immobilie (Verteidigungs- und Kammerantwort): steuert Immobilienkauf, Barzahlungsverbot, wirtschaftlich Berechtigter, Verdachtsmeldung und Beurkundung mit berufsrechtlicher Quellenprüfung, Verhältnismäßigkeit, Aktenlog u... |
| `notar-gesellschafterliste-fehler-verteidigung` | Notar Gesellschafterliste Fehler (Verteidigungs- und Kammerantwort): steuert fehlerhafte Gesellschafterliste, Registervollzug, Rechtsschein, Korrektur und Amtshaftung mit berufsrechtlicher Quellenprüfung, Verhältnismäßigkeit, Aktenlog un... |
| `notar-unparteilichkeit-familiengesellschaft-praevention` | Notar Unparteilichkeit Familiengesellschaft (Präventions- und Organisationspaket): steuert Unparteilichkeit bei Familiengesellschaft, Näheverhältnis, Belehrungspflichten und Ablehnung mit berufsrechtlicher Quellenprüfung, Verhältnismäßig... |
| `notar-unparteilichkeit-familiengesellschaft-verteidigung` | Notar Unparteilichkeit Familiengesellschaft (Verteidigungs- und Kammerantwort): steuert Unparteilichkeit bei Familiengesellschaft, Näheverhältnis, Belehrungspflichten und Ablehnung mit berufsrechtlicher Quellenprüfung, Verhältnismäßigkei... |
| `patentanwalt-berufsgericht-pao` | Patentanwalt Berufsgericht PAO: prüft PAO-Pflichten, Patentanwaltskammer, berufsgerichtliches Verfahren und Schutzrechtsmandate in berufsgerichtlichen Verfahren freier Berufe; mit Normencheck, Aktenlog, Verteidigungslinie, Verhältnismäßi... |
| `patentanwalt-erfinderkonflikt-praevention` | Patentanwalt Erfinderkonflikt (Präventions- und Organisationspaket): steuert Konflikt zwischen Erfinder, Arbeitgeber, Anmelder, Investor und mehreren Schutzrechtsinhabern mit berufsrechtlicher Quellenprüfung, Verhältnismäßigkeit, Aktenlo... |
| `patentanwalt-erfinderkonflikt-verteidigung` | Patentanwalt Erfinderkonflikt (Verteidigungs- und Kammerantwort): steuert Konflikt zwischen Erfinder, Arbeitgeber, Anmelder, Investor und mehreren Schutzrechtsinhabern mit berufsrechtlicher Quellenprüfung, Verhältnismäßigkeit, Aktenlog u... |
| `patentanwalt-fristenversaeumnis-epo-dpma-praevention` | Patentanwalt Fristenversäumnis DPMA/EPO (Präventions- und Organisationspaket): steuert Fristversäumnis, Wiedereinsetzung, Mandanteninformation und berufsrechtliche Aufarbeitung mit berufsrechtlicher Quellenprüfung, Verhältnismäßigkeit, A... |
| `patentanwalt-fristenversaeumnis-epo-dpma-verteidigung` | Patentanwalt Fristenversäumnis DPMA/EPO (Verteidigungs- und Kammerantwort): steuert Fristversäumnis, Wiedereinsetzung, Mandanteninformation und berufsrechtliche Aufarbeitung mit berufsrechtlicher Quellenprüfung, Verhältnismäßigkeit, Akte... |
| `patentanwalt-vertretungsbefugnis-grenze-praevention` | Patentanwalt Vertretungsbefugnis Grenze (Präventions- und Organisationspaket): steuert Grenzen patentanwaltlicher Beratung, Rechtsdienstleistung, Prozessvertretung und Kooperation mit Rechtsanwälten mit berufsrechtlicher Quellenprüfung,... |
| `patentanwalt-vertretungsbefugnis-grenze-verteidigung` | Patentanwalt Vertretungsbefugnis Grenze (Verteidigungs- und Kammerantwort): steuert Grenzen patentanwaltlicher Beratung, Rechtsdienstleistung, Prozessvertretung und Kooperation mit Rechtsanwälten mit berufsrechtlicher Quellenprüfung, Ver... |
| `protokoll-und-nachbereitung` | Protokoll und Nachbereitung: prüft sichert Verlauf, Zusagen, Beschlüsse, Auflagen und nächste Wiedervorlagen in berufsgerichtlichen Verfahren freier Berufe; mit Normencheck, Aktenlog, Verteidigungslinie, Verhältnismäßigkeit und Rechtsmit... |
| `rak-ruege-unsachlichkeit-verteidigung` | RAK-Rüge wegen Unsachlichkeit (Verteidigungs- und Kammerantwort): steuert berufsrechtliche Rüge wegen scharfer Schriftsatzsprache, Social-Media-Äußerung oder Kollegenkonflikt mit berufsrechtlicher Quellenprüfung, Verhältnismäßigkeit, Akt... |
| `rechtsmittel-berufsgericht-praevention` | Rechtsmittel im Berufsgericht (Präventions- und Organisationspaket): steuert Berufung, Antrag auf Zulassung, sofortige Beschwerde, Frist und Begründungsdichte mit berufsrechtlicher Quellenprüfung, Verhältnismäßigkeit, Aktenlog und verwer... |
| `rechtsmittel-berufsgericht-verteidigung` | Rechtsmittel im Berufsgericht (Verteidigungs- und Kammerantwort): steuert Berufung, Antrag auf Zulassung, sofortige Beschwerde, Frist und Begründungsdichte mit berufsrechtlicher Quellenprüfung, Verhältnismäßigkeit, Aktenlog und verwertba... |
| `red-team-qualitygate` | Red-Team-Qualitygate: prüft prüft Ergebnis auf Fristenfehler, Zuständigkeitsfehler, Scheinpräzision und Ton in berufsgerichtlichen Verfahren freier Berufe; mit Normencheck, Aktenlog, Verteidigungslinie, Verhältnismäßigkeit und Rechtsmitt... |
| `robe-werbung-vermerk-mustertext-sitzungs` | Robe, Werbung und Sachlichkeit: prüft Werberecht, Sachlichkeitsgebot, Auftritt vor Gericht und Berufsbild in berufsgerichtlichen Verfahren freier Berufe; mit Normencheck, Aktenlog, Verteidigungslinie, Verhältnismäßigkeit und Rechtsmittel... |
| `sanktionen-mandatsannahme` | Sanktionen und Mandatsannahme (Präventions- und Organisationspaket): steuert Sanktionslisten, embargobehaftete Mandate, Zahlungsannahme und Niederlegung mit berufsrechtlicher Quellenprüfung, Verhältnismäßigkeit, Aktenlog und verwertbarem... |
| `sanktionen-mandatsannahme-verteidigung` | Sanktionen und Mandatsannahme (Verteidigungs- und Kammerantwort): steuert Sanktionslisten, embargobehaftete Mandate, Zahlungsannahme und Niederlegung mit berufsrechtlicher Quellenprüfung, Verhältnismäßigkeit, Aktenlog und verwertbarem Ar... |
| `schriftsatz-vermerk-und-mustertext` | Schriftsatz, Vermerk und Mustertext: prüft liefert einen belastbaren ersten Entwurf mit offenen Punkten in berufsgerichtlichen Verfahren freier Berufe; mit Normencheck, Aktenlog, Verteidigungslinie, Verhältnismäßigkeit und Rechtsmittelsp... |
| `sitzungs-und-terminvorbereitung` | Sitzungs- und Terminvorbereitung: prüft bereitet Gerichtstermin, Behördenkontakt, Kammertermin oder Verhandlungstag vor in berufsgerichtlichen Verfahren freier Berufe; mit Normencheck, Aktenlog, Verteidigungslinie, Verhältnismäßigkeit un... |
| `social-media-berufsrecht-verteidigung` | Social Media Berufsrecht (Verteidigungs- und Kammerantwort): steuert LinkedIn, X, Kanzleivideo, Fachanwaltstitel, Mandatswerbung und öffentliche Streitkultur mit berufsrechtlicher Quellenprüfung, Verhältnismäßigkeit, Aktenlog und verwert... |
| `steuerberater-153-ao-berichtigung-praevention` | Steuerberater § 153 AO Berichtigung (Präventions- und Organisationspaket): steuert Berichtigungspflicht, Selbstanzeigegrenze, Mandantenweisung und Berufsrisiko mit berufsrechtlicher Quellenprüfung, Verhältnismäßigkeit, Aktenlog und verwe... |
| `steuerberater-153-ao-berichtigung-verteidigung` | Steuerberater § 153 AO Berichtigung (Verteidigungs- und Kammerantwort): steuert Berichtigungspflicht, Selbstanzeigegrenze, Mandantenweisung und Berufsrisiko mit berufsrechtlicher Quellenprüfung, Verhältnismäßigkeit, Aktenlog und verwertb... |
| `steuerberater-berufsgericht-stberg` | Steuerberater Berufsgericht StBerG: prüft Warnung, Verweis, Geldbuße, Berufsverbot und Ausschließung nach StBerG in berufsgerichtlichen Verfahren freier Berufe; mit Normencheck, Aktenlog, Verteidigungslinie, Verhältnismäßigkeit und Recht... |
| `steuerberater-unterlagenherausgabe-praevention` | Steuerberater Unterlagenherausgabe (Präventions- und Organisationspaket): steuert Herausgabe von Buchhaltungsdaten, DATEV-Bestand, Zurückbehaltungsrecht und Mandatswechsel mit berufsrechtlicher Quellenprüfung, Verhältnismäßigkeit, Aktenl... |
| `steuerberater-unterlagenherausgabe-verteidigung` | Steuerberater Unterlagenherausgabe (Verteidigungs- und Kammerantwort): steuert Herausgabe von Buchhaltungsdaten, DATEV-Bestand, Zurückbehaltungsrecht und Mandatswechsel mit berufsrechtlicher Quellenprüfung, Verhältnismäßigkeit, Aktenlog... |
| `steuerberater-vorbehaltsaufgabe-kammer` | Steuerberater Vorbehaltsaufgabe (Verteidigungs- und Kammerantwort): steuert Abgrenzung Steuerberatung, Rechtsdienstleistung, Lohnbuchhaltung, Förderantrag und betriebswirtschaftliche Beratung mit berufsrechtlicher Quellenprüfung, Verhält... |
| `steuerberater-vorbehaltsaufgabe-praevention` | Steuerberater Vorbehaltsaufgabe (Präventions- und Organisationspaket): steuert Abgrenzung Steuerberatung, Rechtsdienstleistung, Lohnbuchhaltung, Förderantrag und betriebswirtschaftliche Beratung mit berufsrechtlicher Quellenprüfung, Verh... |
| `vergleich-mit-kammer-praevention` | Vergleich mit Kammer oder Aufsicht (Präventions- und Organisationspaket): steuert informelle Erledigung, Auflagen, Rüge, Belehrung, Schulungsnachweis und Kosten mit berufsrechtlicher Quellenprüfung, Verhältnismäßigkeit, Aktenlog und verw... |
| `vergleich-mit-kammer-verteidigung` | Vergleich mit Kammer oder Aufsicht (Verteidigungs- und Kammerantwort): steuert informelle Erledigung, Auflagen, Rüge, Belehrung, Schulungsnachweis und Kosten mit berufsrechtlicher Quellenprüfung, Verhältnismäßigkeit, Aktenlog und verwert... |
| `vermoegensverfall-zulassungswiderruf` | Vermögensverfall und Zulassungswiderruf (Verteidigungs- und Kammerantwort): steuert Widerruf der Zulassung wegen Vermögensverfall, Gläubigerschutz, Sofortvollzug und Sanierungsnachweis mit berufsrechtlicher Quellenprüfung, Verhältnismäßi... |
| `vermoegensverfall-zulassungswiderruf-praevention` | Vermögensverfall und Zulassungswiderruf (Präventions- und Organisationspaket): steuert Widerruf der Zulassung wegen Vermögensverfall, Gläubigerschutz, Sofortvollzug und Sanierungsnachweis mit berufsrechtlicher Quellenprüfung, Verhältnism... |
| `verschwiegenheit-cloud-dienstleister-praevention` | Verschwiegenheit und Cloud-Dienstleister (Präventions- und Organisationspaket): steuert Mandatsgeheimnis, Cloud, Legal Tech, KI-Tools, Auftragsverarbeitung und Berufsgeheimnisträgerprivileg mit berufsrechtlicher Quellenprüfung, Verhältni... |
| `verschwiegenheit-cloud-dienstleister-verteidigung` | Verschwiegenheit und Cloud-Dienstleister (Verteidigungs- und Kammerantwort): steuert Mandatsgeheimnis, Cloud, Legal Tech, KI-Tools, Auftragsverarbeitung und Berufsgeheimnisträgerprivileg mit berufsrechtlicher Quellenprüfung, Verhältnismä... |
| `werbung-robe-kanzleimarketing-praevention` | Werbung, Robe und Kanzleimarketing (Präventions- und Organisationspaket): steuert Berufswerbung, Robenaufdruck, Spezialisierungswerbung, Bewertungen und Irreführung mit berufsrechtlicher Quellenprüfung, Verhältnismäßigkeit, Aktenlog und... |
| `werbung-robe-wirtschaftspruefer` | Werbung, Robe und Kanzleimarketing (Verteidigungs- und Kammerantwort): steuert Berufswerbung, Robenaufdruck, Spezialisierungswerbung, Bewertungen und Irreführung mit berufsrechtlicher Quellenprüfung, Verhältnismäßigkeit, Aktenlog und ver... |
| `wirtschaftspruefer-berufsaufsicht-wpo` | Wirtschaftsprüfer Berufsaufsicht WPO: prüft WPK, APAS, Qualitätskontrolle, berufsgerichtliche Maßnahmen und Prüfungsfehler in berufsgerichtlichen Verfahren freier Berufe: Wirtschaftsprüfer Berufsaufsicht WPO: prüft WPK, APAS, Qualitätsko... |
| `wirtschaftspruefer-qualitaetskontrolle-praevention` | Wirtschaftsprüfer Qualitätskontrolle (Präventions- und Organisationspaket): steuert Qualitätssicherung, Inspektion, Dokumentation, Prüfungsakte und Maßnahmenplan mit berufsrechtlicher Quellenprüfung, Verhältnismäßigkeit, Aktenlog und ver... |
| `wirtschaftspruefer-qualitaetskontrolle-verteidigung` | Wirtschaftsprüfer Qualitätskontrolle (Verteidigungs- und Kammerantwort): steuert Qualitätssicherung, Inspektion, Dokumentation, Prüfungsakte und Maßnahmenplan mit berufsrechtlicher Quellenprüfung, Verhältnismäßigkeit, Aktenlog und verwer... |
| `wirtschaftspruefer-testat-widerruf` | Wirtschaftsprüfer Testat Widerruf (Verteidigungs- und Kammerantwort): steuert fehlerhaftes Testat, Nachtragsprüfung, Widerruf, Marktinformation und Haftung mit berufsrechtlicher Quellenprüfung, Verhältnismäßigkeit, Aktenlog und verwertba... |
| `wirtschaftspruefer-testat-widerruf-praevention` | Wirtschaftsprüfer Testat Widerruf (Präventions- und Organisationspaket): steuert fehlerhaftes Testat, Nachtragsprüfung, Widerruf, Marktinformation und Haftung mit berufsrechtlicher Quellenprüfung, Verhältnismäßigkeit, Aktenlog und verwer... |
| `wirtschaftspruefer-unabhaengigkeit-praevention` | Wirtschaftsprüfer Unabhängigkeit (Präventions- und Organisationspaket): steuert Independence, Non-Audit-Services, Cooling-off, Netzwerk und Mandatsannahme mit berufsrechtlicher Quellenprüfung, Verhältnismäßigkeit, Aktenlog und verwertbar... |
| `wirtschaftspruefer-unabhaengigkeit-verteidigung` | Wirtschaftsprüfer Unabhängigkeit (Verteidigungs- und Kammerantwort): steuert Independence, Non-Audit-Services, Cooling-off, Netzwerk und Mandatsannahme mit berufsrechtlicher Quellenprüfung, Verhältnismäßigkeit, Aktenlog und verwertbarem... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
