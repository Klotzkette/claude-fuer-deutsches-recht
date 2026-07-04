# NDA-Generator und Verschwiegenheitsvereinbarungs-Checker

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`nda-verschwiegenheit-generator-checker`) | [`nda-verschwiegenheit-generator-checker.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/nda-verschwiegenheit-generator-checker.zip) |
| **Alle Skills als Markdown** | [`alle-skills-markdown.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-skills-markdown.zip) |

Dieses Plugin hat (bewusst) keine eigene Demonstrations-Akte.

<!-- END plugin-sofort-download-section (autogen) -->

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Allgemeiner NDA-Ersteller und NDA-Prüfer für deutsche und internationale Verschwiegenheitsvereinbarungen: Entwurf, Redline, GeschGehG, HinSchG, AGB, Arbeitsrecht, M&A, Forschung, Software, Datenraum und Verletzungsreaktion.

Dieses Plugin gehört zum Marketplace mit 233 Plugins für deutsches Recht. Es bündelt die zugehörigen Skills, Prüfraster, Vorlagen und Arbeitsroutinen in einem installierbaren Plugin-ZIP. Die zwei Markdown-Prompts sind vollwertige Ein-Datei-Starts für den Fall, dass kein Plugin-Setup genutzt werden soll: Werkstatt für den ausführlichen Arbeitsmodus, Schnellstart für den kompakten Einstieg.

Schneller Weg: Für eine erste Ergebnisrichtung den Schnellstart laden, für einen tragfähigen Arbeitsmodus die Werkstatt. Beide Prompts sollen mit einem konkreten Arbeitsprodukt beginnen, nur eng nachfragen und nicht in einer Materialinventur hängen bleiben.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`nda-verschwiegenheit-generator-checker.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/nda-verschwiegenheit-generator-checker.zip) |
| Großer Prompt (Werkstatt) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/nda-verschwiegenheit-generator-checker/nda-verschwiegenheit-generator-checker-werkstatt.md" download><code>nda-verschwiegenheit-generator-checker-werkstatt.md</code></a> |
| Kleiner Prompt (Schnellstart) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/nda-verschwiegenheit-generator-checker/nda-verschwiegenheit-generator-checker-schnellstart.md" download><code>nda-verschwiegenheit-generator-checker-schnellstart.md</code></a> |
| Testakte(n) als ZIP | ZIP | [`alle-testakten.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-testakten.zip) und [`alle-testakten-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-testakten-einzelpdfs.zip) (zentrale Sammlung) |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 233 Plugins. Wer alle Plugins auf einmal will, nimmt `alle-plugins-megazip.zip`. Wer nur einzelne Werkstatt- oder Schnellstart-Prompts will, nimmt die Markdown-Downloads.
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du deinen Fall strukturieren, die einschlaegigen Normen prüfen und ein verwertbares Arbeitsprodukt erhalten.
Dieses Plugin ist der allgemeine Verschwiegenheitsvereinbarungs-Generator und Checker. Es hilft beim Entwerfen, Prüfen, Verhandeln und Durchsetzen von NDAs, ohne Catch-all-Klauseln, Hinweisgeberschutz, Geschäftsgeheimnisschutz, Datenräume oder internationale Begriffe durcheinanderzuwerfen.

## Startworkflow

1. **Rolle und Ziel klären:** Wer fragt, wer entscheidet, wer trägt Risiko?
2. **Unterlagen einsammeln:** Entwurf, Satzung, Geschäftsordnung, Beschluss, Term Sheet, Vertrag, Organunterlagen, E-Mail, Datenraum, Registerauszug.
3. **Weiche wählen:** Entwerfen, prüfen, verhandeln, durchführen, protokollieren, eskalieren oder prozessfest dokumentieren.
4. **Spezialskills ziehen:** Das Plugin schlägt nach dem Kaltstart die passenden Vertiefungen vor und stoppt nicht bei einer Scheinlösung.
5. **Output liefern:** Matrix, Entwurf, Redline-Hinweise, Beschlussvorschlag, Protokollbaustein, Memo oder To-do-Liste.

## Quellenhygiene

- Aktuelle Normen aus Gesetze-im-Internet, EUR-Lex und amtlichen Registern live prüfen, wenn sie tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle zitieren.
- Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.
- **Normlogik:** Der Primäranker für Geschäftsgeheimnisse ist § 2 GeschGehG (Geheimnisqualität, wirtschaftlicher Wert, angemessene Schutzmaßnahmen). §§ 16-20 GeschGehG sind wichtig für gerichtlichen Geheimnisschutz, aber nicht die Definition. § 203 StGB nur als Sonderanker für Berufsgeheimnisträger verwenden. DSGVO Art. 28 nur anziehen, wenn tatsächlich Auftragsverarbeitung vorliegt; sonst Art. 5, 6, 26 DSGVO und ggf. BDSG/Arbeitsrecht prüfen.

## Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.


<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

## Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Die alphabetische Komplettliste bleibt darunter erhalten.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 1. Einstieg und Fallrouting | `anwaltliche-mandatsgeheimnisse`, `einseitig-gegenseitig-entwerfen-router-eu`, `entwerfen-oder-pruefen-router`, `kaltstart-routing`, `nda-intake-rollen-und-ziel` |
| 2. Unterlagen, Sachverhalt und Quellen | `beweisprotokoll-verletzung-china-nda-clause`, `datenraum-nda-datenschutz-dsgvo-deutsches`, `datenschutz-dsgvo-und-auftragsverarbeitung`, `dokumentenmatrix-und-anlagen`, `gesundheits-forschungsdaten-gesundheitswesen`, `nda-fuer-datenraum-clean-team`, `offenlegung-in-pitch-und-datenraum`, `schadensersatz-beweislast-abmahnung-cease` |
| 3. Prüfung, Anspruch und Subsumtion | `abschluss-check-vor-unterschrift`, `haftungsbegrenzung-und-carve-outs`, `risikoampel-fuer-empfaenger`, `risikoampel-fuer-offenleger`, `vertragsstrafe-hamburger-haftungsbegrenzung` |
| 4. Gestaltung, Strategie und Verhandlung | `catch-all-klausel-arbeitsvertrag`, `liquidated-damages-us-uk-vergleich`, `post-signing-compliance`, `prozessvergleich-und-mediation`, `verbundene-unternehmen-verhandlungsposition`, `verhandlungsbrief-zu-harten-klauseln`, `verhandlungsposition-und-fallbacks` |
| 5. Verfahren, Behörde und Gericht | `gerichtsstand-schiedsgericht`, `laufzeit-nachwirkungsfrist-oeffentliche-hand`, `oeffentliche-hand-und-vergabeverfahren`, `zulaessige-offenlegung-gesetz-behoerde-gericht` |
| 6. Ergebnis, Schreiben und Kommunikation | `abschlussprodukt-redline-memo`, `mandantenbrief-einfach-abschlussbericht`, `nda-abschlussbericht-playbook` |
| 7. Kontrolle, Qualität und Gegenprüfung | `agb-kontrolle-angemessene`, `nda-und-audit-rights` |
| 8. Spezialmodule und Schnittstellen | `abmahnung-und-cease-desist`, `angemessene-geheimhaltungsmassnahmen`, `arbeitsrecht-bewerber-und-recruiting`, `ausnahmen-vertraulichkeit-bank-finanzierungs`, `bank-und-finanzierungs-nda`, `berufsgeheimnisse-203-stgb`, `betriebsrat-und-personalgespraech`, `china-nda-nnn`, `clause-redline-kommentar`, `cross-border-governing-law`, `deutsches-englisches-bilinguales-nda`, `eu-trade-secrets-directive`, `executive-summary-fuer-geschaeftsfuehrung`, `familienunternehmen-nachfolge-forensik`, `forensik-und-logfiles`, `forschung-entwicklung-kooperation`, `frankreich-secret-des-affaires`, `freistellung-indemnity-geheimniskategorien`, ... plus 49 weitere |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 101 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `abmahnung-und-cease-desist` | Wenn es um Abmahnung Und Cease Desist in NDA-Generator und Verschwiegenheitsvereinbarungs-Checker geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkte... |
| `abschluss-check-vor-unterschrift` | Wenn es um Abschluss Check Vor Unterschrift in NDA-Generator und Verschwiegenheitsvereinbarungs-Checker geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüf... |
| `abschlussprodukt-redline-memo` | Wenn es um Abschlussprodukt Redline Memo in NDA-Generator und Verschwiegenheitsvereinbarungs-Checker geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründu... |
| `agb-kontrolle-angemessene` | Wenn es um Agb Kontrolle B2B Und B2C in NDA-Generator und Verschwiegenheitsvereinbarungs-Checker geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Gegenprüfung mit Fehler-, Beweis- und Fristencheck. |
| `angemessene-geheimhaltungsmassnahmen` | Wenn es um Angemessene Geheimhaltungsmassnahmen in NDA-Generator und Verschwiegenheitsvereinbarungs-Checker geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit... |
| `anwaltliche-mandatsgeheimnisse` | Wenn es um Anwaltliche Mandatsgeheimnisse in NDA-Generator und Verschwiegenheitsvereinbarungs-Checker geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpu... |
| `arbeitsrecht-bewerber-und-recruiting` | Wenn es um Arbeitsrecht Bewerber Und Recruiting in NDA-Generator und Verschwiegenheitsvereinbarungs-Checker geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit... |
| `ausnahmen-vertraulichkeit-bank-finanzierungs` | Wenn es um Ausnahmen Von Vertraulichkeit in NDA-Generator und Verschwiegenheitsvereinbarungs-Checker geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpun... |
| `bank-und-finanzierungs-nda` | Wenn es um Bank Und Finanzierungs NDA in NDA-Generator und Verschwiegenheitsvereinbarungs-Checker geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkte... |
| `berufsgeheimnisse-203-stgb` | Wenn es um Berufsgeheimnisse 203 Stgb in NDA-Generator und Verschwiegenheitsvereinbarungs-Checker geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkte... |
| `betriebsrat-und-personalgespraech` | Wenn es um Betriebsrat Und Personalgespraech in NDA-Generator und Verschwiegenheitsvereinbarungs-Checker geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prü... |
| `beweisprotokoll-verletzung-china-nda-clause` | Wenn es um Beweisprotokoll Verletzung in NDA-Generator und Verschwiegenheitsvereinbarungs-Checker geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Beweislast- und Substantiierungsmatrix. |
| `catch-all-klausel-arbeitsvertrag` | Wenn es um Catch All Klausel Arbeitsvertrag in NDA-Generator und Verschwiegenheitsvereinbarungs-Checker geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüf... |
| `china-nda-nnn` | Wenn es um China NDA Nnn in NDA-Generator und Verschwiegenheitsvereinbarungs-Checker geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken un... |
| `clause-redline-kommentar` | Wenn es um Clause Redline Kommentar in NDA-Generator und Verschwiegenheitsvereinbarungs-Checker geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten,... |
| `cross-border-governing-law` | Wenn es um Cross Border Governing Law in NDA-Generator und Verschwiegenheitsvereinbarungs-Checker geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkte... |
| `datenraum-nda-datenschutz-dsgvo-deutsches` | Wenn es um Datenraum NDA Checkliste in NDA-Generator und Verschwiegenheitsvereinbarungs-Checker geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigk... |
| `datenschutz-dsgvo-und-auftragsverarbeitung` | Wenn es um Datenschutz DSGVO Und Auftragsverarbeitung in NDA-Generator und Verschwiegenheitsvereinbarungs-Checker geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsproduk... |
| `deutsches-englisches-bilinguales-nda` | Wenn es um Deutsches Englisches Bilinguales NDA in NDA-Generator und Verschwiegenheitsvereinbarungs-Checker geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-... |
| `dokumentenmatrix-und-anlagen` | Wenn es um Dokumentenmatrix Und Anlagen in NDA-Generator und Verschwiegenheitsvereinbarungs-Checker geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Dokumentenmatrix mit Nachforderungsliste. |
| `einseitig-gegenseitig-entwerfen-router-eu` | Wenn es um Einseitig Gegenseitig Multilateral in NDA-Generator und Verschwiegenheitsvereinbarungs-Checker geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-,... |
| `entwerfen-oder-pruefen-router` | Wenn es um Entwerfen Oder Prüfen Router in NDA-Generator und Verschwiegenheitsvereinbarungs-Checker geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunk... |
| `eu-trade-secrets-directive` | Wenn es um EU Trade Secrets Directive in NDA-Generator und Verschwiegenheitsvereinbarungs-Checker geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständi... |
| `executive-summary-fuer-geschaeftsfuehrung` | Wenn es um Executive Summary Für Geschäftsführung in NDA-Generator und Verschwiegenheitsvereinbarungs-Checker geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mi... |
| `familienunternehmen-nachfolge-forensik` | Wenn es um Familienunternehmen Und Nachfolge in NDA-Generator und Verschwiegenheitsvereinbarungs-Checker geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prü... |
| `forensik-und-logfiles` | Wenn es um Forensik Und Logfiles in NDA-Generator und Verschwiegenheitsvereinbarungs-Checker geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Ri... |
| `forschung-entwicklung-kooperation` | Wenn es um Forschung Entwicklung Kooperation in NDA-Generator und Verschwiegenheitsvereinbarungs-Checker geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prü... |
| `frankreich-secret-des-affaires` | Wenn es um Frankreich Secret Des Affaires in NDA-Generator und Verschwiegenheitsvereinbarungs-Checker geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpu... |
| `freistellung-indemnity-geheimniskategorien` | Wenn es um Freistellung Und Indemnity in NDA-Generator und Verschwiegenheitsvereinbarungs-Checker geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkte... |
| `geheimniskategorien-crown-jewels` | Wenn es um Geheimniskategorien Crown Jewels in NDA-Generator und Verschwiegenheitsvereinbarungs-Checker geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüf... |
| `gerichtsstand-schiedsgericht` | Wenn es um Gerichtsstand Schiedsgericht in NDA-Generator und Verschwiegenheitsvereinbarungs-Checker geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunk... |
| `geschaeftsgeheimnis-definition-2-geschgehg` | Wenn es um Geschäftsgeheimnis Definition 2 Geschgehg in NDA-Generator und Verschwiegenheitsvereinbarungs-Checker geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt... |
| `gesundheits-forschungsdaten-gesundheitswesen` | Wenn es um Gesundheits Und Forschungsdaten in NDA-Generator und Verschwiegenheitsvereinbarungs-Checker geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfp... |
| `gesundheitswesen-klinik-pharma` | Wenn es um Gesundheitswesen Klinik Pharma in NDA-Generator und Verschwiegenheitsvereinbarungs-Checker geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpu... |
| `haftungsbegrenzung-und-carve-outs` | Wenn es um Haftungsbegrenzung Und Carve Outs in NDA-Generator und Verschwiegenheitsvereinbarungs-Checker geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prü... |
| `hinweisgeberschutz-nda-konflikt` | Wenn es um Hinweisgeberschutz NDA Konflikt in NDA-Generator und Verschwiegenheitsvereinbarungs-Checker geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfp... |
| `immobilien-und-projektentwicklung` | Wenn es um Immobilien Und Projektentwicklung in NDA-Generator und Verschwiegenheitsvereinbarungs-Checker geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prü... |
| `insiderinformationen-mar-interessenprofil` | Wenn es um Insiderinformationen Mar in NDA-Generator und Verschwiegenheitsvereinbarungs-Checker geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten,... |
| `interessenprofil-offenlegung-empfang` | Wenn es um Interessenprofil Offenlegung Empfang in NDA-Generator und Verschwiegenheitsvereinbarungs-Checker geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit... |
| `japan-business-secrets` | Wenn es um Japan Business Secrets in NDA-Generator und Verschwiegenheitsvereinbarungs-Checker geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, R... |
| `joint-venture-nda` | Wenn es um Joint Venture NDA in NDA-Generator und Verschwiegenheitsvereinbarungs-Checker geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risike... |
| `kaltstart-routing` | Wenn es um Allgemein Kaltstart in NDA-Generator und Verschwiegenheitsvereinbarungs-Checker geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kartellrecht-clean-kein-dealzwang-lizenz-ki` | Wenn es um Kartellrecht Clean Team in NDA-Generator und Verschwiegenheitsvereinbarungs-Checker geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten,... |
| `kein-dealzwang-no-obligation` | Wenn es um Kein Dealzwang No Obligation in NDA-Generator und Verschwiegenheitsvereinbarungs-Checker geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunk... |
| `kein-lizenz-und-ip-vorbehalt` | Wenn es um Kein Lizenz Und IP Vorbehalt in NDA-Generator und Verschwiegenheitsvereinbarungs-Checker geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunk... |
| `ki-tools-und-confidentiality` | Wenn es um digitale Werkzeuge Tools Und Confidentiality in NDA-Generator und Verschwiegenheitsvereinbarungs-Checker geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kol... |
| `know-how-erfahrungswissen-arbeitnehmer` | Wenn es um Know How Erfahrungswissen Arbeitnehmer in NDA-Generator und Verschwiegenheitsvereinbarungs-Checker geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mi... |
| `kurzform-vs-langform` | Wenn es um Kurzform Vs Langform in NDA-Generator und Verschwiegenheitsvereinbarungs-Checker geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Ris... |
| `laufzeit-nachwirkungsfrist-oeffentliche-hand` | Wenn es um Laufzeit Und Nachwirkungsfrist in NDA-Generator und Verschwiegenheitsvereinbarungs-Checker geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `liquidated-damages-us-uk-vergleich` | Wenn es um Liquidated Damages US Uk Vergleich in NDA-Generator und Verschwiegenheitsvereinbarungs-Checker geht: entwickelt Verhandlungsziel, Vergleichskorridor und Eskalationspfad; liefert eine Verhandlungs- oder Eskalationslinie mit Opt... |
| `ma-teaser-und-cim-nda` | Wenn es um M&A Teaser Und Cim NDA in NDA-Generator und Verschwiegenheitsvereinbarungs-Checker geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, R... |
| `mandantenbrief-einfach-abschlussbericht` | Wenn es um Mandantenbrief Einfach Erklaert in NDA-Generator und Verschwiegenheitsvereinbarungs-Checker geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begrün... |
| `nda-abschlussbericht-playbook` | Wenn es um NDA Abschlussbericht Playbook in NDA-Generator und Verschwiegenheitsvereinbarungs-Checker geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpun... |
| `nda-fuer-ai-und-modelltraining` | Wenn es um NDA Für Ai Und Modelltraining in NDA-Generator und Verschwiegenheitsvereinbarungs-Checker geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpun... |
| `nda-fuer-datenraum-clean-team` | Wenn es um NDA Für Datenraum Clean Team in NDA-Generator und Verschwiegenheitsvereinbarungs-Checker geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunk... |
| `nda-fuer-hr-und-abwerbeverbot` | Wenn es um NDA Fuer Hr Und Abwerbeverbot in NDA-Generator und Verschwiegenheitsvereinbarungs-Checker geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpun... |
| `nda-fuer-investor-pitch` | Wenn es um NDA Für Investor Pitch in NDA-Generator und Verschwiegenheitsvereinbarungs-Checker geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, R... |
| `nda-fuer-manufacturing-und-supply-chain` | Wenn es um NDA Für Manufacturing Und Supply Chain in NDA-Generator und Verschwiegenheitsvereinbarungs-Checker geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mi... |
| `nda-fuer-vorstand-und-aufsichtsrat` | Wenn es um NDA Für Vorstand Und Aufsichtsrat in NDA-Generator und Verschwiegenheitsvereinbarungs-Checker geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prü... |
| `nda-hr-abwerbeverbot-investor-pitch` | Wenn es um NDA Für Hr Und Abwerbeverbot in NDA-Generator und Verschwiegenheitsvereinbarungs-Checker geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunk... |
| `nda-intake-rollen-und-ziel` | Wenn es um NDA Intake Rollen Und Ziel in NDA-Generator und Verschwiegenheitsvereinbarungs-Checker geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkte... |
| `nda-mit-non-solicit-abgrenzung` | Wenn es um NDA Mit Non Solicit Abgrenzung in NDA-Generator und Verschwiegenheitsvereinbarungs-Checker geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpu... |
| `nda-und-audit-rights` | Wenn es um NDA Und Audit Rights in NDA-Generator und Verschwiegenheitsvereinbarungs-Checker geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Ris... |
| `nda-und-escrow` | Wenn es um NDA Und Escrow in NDA-Generator und Verschwiegenheitsvereinbarungs-Checker geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken u... |
| `nda-und-freedom-to-operate` | Wenn es um NDA Und Freedom To Operate in NDA-Generator und Verschwiegenheitsvereinbarungs-Checker geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkte... |
| `nda-und-public-disclosure` | Wenn es um NDA Und Public Disclosure in NDA-Generator und Verschwiegenheitsvereinbarungs-Checker geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten... |
| `need-to-know-empfaengerkreis` | Wenn es um Need To Know Empfaengerkreis in NDA-Generator und Verschwiegenheitsvereinbarungs-Checker geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunk... |
| `no-representation-no-warranty` | Wenn es um No Representation No Warranty in NDA-Generator und Verschwiegenheitsvereinbarungs-Checker geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpun... |
| `oeffentliche-hand-und-vergabeverfahren` | Wenn es um Oeffentliche Hand Und Vergabeverfahren in NDA-Generator und Verschwiegenheitsvereinbarungs-Checker geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mi... |
| `oesterreich-geheimhaltung-offenlegung-pitch` | Wenn es um Oesterreich Geheimhaltung in NDA-Generator und Verschwiegenheitsvereinbarungs-Checker geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten... |
| `offenlegung-in-pitch-und-datenraum` | Wenn es um Offenlegung In Pitch Und Datenraum in NDA-Generator und Verschwiegenheitsvereinbarungs-Checker geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Pr... |
| `open-source-und-secret-contamination` | Wenn es um Open Source Und Secret Contamination in NDA-Generator und Verschwiegenheitsvereinbarungs-Checker geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit... |
| `patent-erfinder-und-prior-art` | Wenn es um Patent Erfinder Und Prior Art in NDA-Generator und Verschwiegenheitsvereinbarungs-Checker geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpun... |
| `pauschalierter-schaden` | Wenn es um Pauschalierter Schaden in NDA-Generator und Verschwiegenheitsvereinbarungs-Checker geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, R... |
| `playbook-standardabweichungen-post-signing` | Wenn es um Playbook Standardabweichungen in NDA-Generator und Verschwiegenheitsvereinbarungs-Checker geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpun... |
| `post-signing-compliance` | Wenn es um Post Signing Compliance in NDA-Generator und Verschwiegenheitsvereinbarungs-Checker geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten,... |
| `prozessschutz-16-20-geschgehg` | Wenn es um Prozessschutz 16 20 Geschgehg in NDA-Generator und Verschwiegenheitsvereinbarungs-Checker geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpun... |
| `prozessvergleich-und-mediation` | Wenn es um Prozessvergleich Und Mediation in NDA-Generator und Verschwiegenheitsvereinbarungs-Checker geht: entwickelt Verhandlungsziel, Vergleichskorridor und Eskalationspfad; liefert eine Verhandlungs- oder Eskalationslinie mit Optionen. |
| `reverse-engineering-empfaenger-offenleger` | Wenn es um Reverse Engineering Und Gesetzliche Ausnahmen in NDA-Generator und Verschwiegenheitsvereinbarungs-Checker geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitspro... |
| `risikoampel-fuer-empfaenger` | Wenn es um Risikoampel Für Empfaenger in NDA-Generator und Verschwiegenheitsvereinbarungs-Checker geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `risikoampel-fuer-offenleger` | Wenn es um Risikoampel Für Offenleger in NDA-Generator und Verschwiegenheitsvereinbarungs-Checker geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `rueckgabe-loeschung-und-zertifikat` | Wenn es um Rueckgabe Loeschung Und Zertifikat in NDA-Generator und Verschwiegenheitsvereinbarungs-Checker geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Pr... |
| `sanktions-und-exportkontrollinformationen` | Wenn es um Sanktions Und Exportkontrollinformationen in NDA-Generator und Verschwiegenheitsvereinbarungs-Checker geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt... |
| `schadensersatz-beweislast-abmahnung-cease` | Wenn es um Schadensersatz Und Beweislast in NDA-Generator und Verschwiegenheitsvereinbarungs-Checker geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Beweislast- und Substantiierungsmatrix. |
| `schweiz-geheimhaltung-signatur-vollmacht` | Wenn es um Schweiz Geheimhaltung in NDA-Generator und Verschwiegenheitsvereinbarungs-Checker geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Ri... |
| `signatur-und-vollmacht` | Wenn es um Signatur Und Vollmacht in NDA-Generator und Verschwiegenheitsvereinbarungs-Checker geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, R... |
| `software-saas-und-source-code` | Wenn es um Software Saas Und Source Code in NDA-Generator und Verschwiegenheitsvereinbarungs-Checker geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpun... |
| `strafbarkeit-23-geschgehg` | Wenn es um Strafbarkeit 23 Geschgehg in NDA-Generator und Verschwiegenheitsvereinbarungs-Checker geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten... |
| `technische-organisatorische-uk` | Wenn es um Technische Organisatorische Schutzmassnahmen in NDA-Generator und Verschwiegenheitsvereinbarungs-Checker geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprod... |
| `uk-confidentiality-agreement` | Wenn es um Uk Confidentiality Agreement in NDA-Generator und Verschwiegenheitsvereinbarungs-Checker geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunk... |
| `unterlassung-eilrechtsschutz` | Wenn es um Unterlassung Eilrechtsschutz in NDA-Generator und Verschwiegenheitsvereinbarungs-Checker geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunk... |
| `us-nda-delaware-new-york` | Wenn es um US NDA Delaware New York in NDA-Generator und Verschwiegenheitsvereinbarungs-Checker geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten,... |
| `verbundene-unternehmen-verhandlungsposition` | Wenn es um Verbundene Unternehmen Berater Finanzierer in NDA-Generator und Verschwiegenheitsvereinbarungs-Checker geht: entwickelt Verhandlungsziel, Vergleichskorridor und Eskalationspfad; liefert eine Verhandlungs- oder Eskalationslinie... |
| `verhandlungsbrief-zu-harten-klauseln` | Wenn es um Verhandlungsbrief Zu Harten Klauseln in NDA-Generator und Verschwiegenheitsvereinbarungs-Checker geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, B... |
| `verhandlungsposition-und-fallbacks` | Wenn es um Verhandlungsposition Und Fallbacks in NDA-Generator und Verschwiegenheitsvereinbarungs-Checker geht: entwickelt Verhandlungsziel, Vergleichskorridor und Eskalationspfad; liefert eine Verhandlungs- oder Eskalationslinie mit Opt... |
| `verletzung-incident-response` | Wenn es um Verletzung Incident Response in NDA-Generator und Verschwiegenheitsvereinbarungs-Checker geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunk... |
| `vertragsstrafe-hamburger-haftungsbegrenzung` | Wenn es um Vertragsstrafe Hamburger Brauch in NDA-Generator und Verschwiegenheitsvereinbarungs-Checker geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfp... |
| `vertrauliche-information-definition` | Wenn es um Vertrauliche Information Definition in NDA-Generator und Verschwiegenheitsvereinbarungs-Checker geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit P... |
| `vorabinformation-protective-zulaessige` | Wenn es um Vorabinformation Und Protective Order in NDA-Generator und Verschwiegenheitsvereinbarungs-Checker geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit... |
| `zulaessige-offenlegung-gesetz-behoerde-gericht` | Wenn es um Zulaessige Offenlegung Gesetz Behörde Gericht in NDA-Generator und Verschwiegenheitsvereinbarungs-Checker geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitspro... |
| `zweckbindung-und-permitted-purpose` | Wenn es um Zweckbindung Und Permitted Purpose in NDA-Generator und Verschwiegenheitsvereinbarungs-Checker geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Pr... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
