# Methodenlehre bürgerliches Recht

Deutsche juristische Methodenlehre und Falllösung aus anwaltlicher Perspektive. Gutachtenstil mit Anspruchsgrundlagen-Reihenfolge. Auslegung Wortlaut Systematik Historie Telos ohne starre Rangfolge — pragmatische Gewichtung wie in der BGH-Praxis. Generalklauseln und Rechtsfortbildung als reale Werkzeuge. Anwaltliche Strategie statt richterliche Selbstbindung.

Für konkrete Prüfungen im BGB Allgemeiner Teil kann `bgb-at-pruefer` hinzugeladen werden; dieses Plugin bleibt die methodische Grundierung, der BGB-AT-Prüfer übernimmt dann Vertragsschluss, Zugang, Anfechtung, Stellvertretung, Geschäftsfähigkeit, Form, Fristen und Verjährung.

## Was dieses Plugin konkret macht

Das Plugin liefert die **methodische Klammer** für jede zivilrechtliche Bewertung im Repo — also den Rahmen, in dem alle Rechtsgebiet-Plugins (`fachanwalt-erbrecht`, `fachanwalt-arbeitsrecht`, `fachanwalt-familienrecht`, `arbeitsrecht`, `gesellschaftsrecht-legal-english`, `kanzlei-allgemein` etc.) arbeiten sollen. Konkret leistet es Folgendes:

- **Anspruchsgrundlagen-Reihenfolge** strukturiert: Vertrag → c.i.c. → GoA → dingliche Ansprüche → Delikt → Gefährdungshaftung → Bereicherung. Sammelbegriffe wie „vertragsähnlich" oder „quasivertraglich" werden vermieden, weil sie in der Lehre uneinheitlich besetzt sind.
- **Vier Auslegungskanones** pragmatisch geführt: grammatikalisch (Wortlautgrenze), systematisch, historisch, teleologisch. **Keine starre Rangfolge** — in der anwaltlichen Praxis dominiert die Teleologie, weil Gerichte über die ratio legis Einzelfallgerechtigkeit begründen. Wer im Schriftsatz nur historisch argumentiert, redet am Senat vorbei.
- **Querschnittskanones**: verfassungskonforme und unionsrechtskonforme Auslegung. Bei Normen unionsrechtlichen Ursprungs autonome Auslegung; Erwägungsgründe als Auslegungshilfe, nicht als Auslegungssubstitut; keine horizontale Direktwirkung von Richtlinien zwischen Privaten.
- **Lückenfüllung als reales Werkzeug**: Analogie (planwidrige Regelungslücke + vergleichbare Interessenlage), teleologische Reduktion, Erst-Recht-Schluss, Umkehrschluss. Mit konkreten Praxisbeispielen aus der BGH-Rechtsfortbildung (Vertrag mit Schutzwirkung zugunsten Dritter, Drittschadensliquidation, c.i.c. vor Schuldrechtsreform).
- **Generalklauseln** als Auffangargument, nicht als Hauptargument: § 138, § 242, § 826 BGB greifen erst, wenn keine speziellere Norm passt. Konkretisierung über Grundrechte und Unionsrecht, nicht über gefühlte „Wertvorstellungen der Gemeinschaft".
- **Querschnittsthemen**, die jede anwaltliche Falllösung mitprüft: Verjährung (§§ 195, 199, 196, 197, 438, 634a BGB, Hemmung §§ 203 ff. BGB), prozessuale Fristen (§ 276, § 517, § 520, § 548, § 569 ZPO, § 339 ZPO, § 4 KSchG), Beweislast (Rosenbergsche Formel, § 280 Abs. 1 S. 2 BGB, § 1 Abs. 4 ProdHaftG, Anscheinsbeweis), Sachverhaltsaufklärung (Auskunftsansprüche § 242 BGB, § 666 BGB, § 810 BGB, Art. 15 DSGVO, §§ 142, 144 ZPO, § 254 ZPO).
- **Verbotsliste — methodische Selbstdisziplin**: keine scheinbaren Auslegungsregeln als tragende Begründung („Ausnahmen sind eng auszulegen", „im Zweifel für den Schuldner"), kein „h. M." als Selbstbeleg, keine Generalklausel als Erstargument.
- **Memo-Standardstruktur**: Sachverhalt → Frage(n) → Kurzantwort → rechtliche Bewertung → Gesamtergebnis → Risiken → Quellenverzeichnis nach Hauszitierweise.
- **Selbstprüfungs-Checkliste vor jeder Ausgabe**: acht Fragen, mit denen jede zivilrechtliche Antwort durchläuft, bevor sie ausgeliefert wird.

Das Plugin verzichtet bewusst darauf, eine methodendebatten-getriebene Position zu beziehen (Rüthers-Warnung vor zu freier Teleologie, Friedrich Müller, Strukturierende Rechtslehre etc.). Es bildet ab, was Senate des BGH und Berufungsinstanzen **tatsächlich** tun, nicht was die Methodenlehre als Idealtypus fordert.

## ⬇️ Direkt-Download (einzelnes ZIP)

| Plugin | Direkt-Download |
| --- | --- |
| Methodenlehre bürgerliches Recht (`methodenlehre-buergerliches-recht`, dieses Plugin) | [methodenlehre-buergerliches-recht.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/methodenlehre-buergerliches-recht.zip) |

Die URL ist stabil und zeigt immer auf die neueste Version. Alle weiteren Plugins sind unter [Releases · latest](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest) genauso einzeln verfügbar.

## Installation in Claude Code

1. ZIP herunterladen (Link oben).
2. Claude Code → **Customize Plugins** → **Install from .zip** → Datei wählen.
3. Fertig. Skills sind sofort verfügbar.

> **Hinweis:** Für den ZIP-Upload muss das Archiv direkt `.claude-plugin/plugin.json`, `skills/`, `assets/` und `references/` im ZIP-Root enthalten. **Nicht** das komplette Repository-ZIP aus „Code → Download ZIP" verwenden.

## Enthaltene Skills

Das Plugin umfasst **20 Skills**, gegliedert in fünf Blöcke. Reihenfolge bewusst: Praxis-Einstieg zuerst, Klassiker als Werkzeug, Strömungen für die methodische Tiefe.

### Praxis-Einstieg und Anwendung

| Skill | Zweck |
| --- | --- |
| `allgemein` | Einstieg, Triage und Workflow-Routing im Plugin. Bei stummem Upload reagiert der Skill eigenständig: ordnet das Material, prüft Eil- und Fristenhinweise, schlägt den passenden Spezial-Skill vor oder stellt genau eine gezielte Rückfrage. |
| `methodenlehre-anwenden` | Wende deutsche juristische Methodenlehre auf zivilrechtliche Bewertungen an. Anspruchsgrundlagen-Reihenfolge, Auslegung Wortlaut Systematik Historie Telos ohne starre Rangfolge. Pragmatische BGH-Praxis: Teleologie dominiert. Rechtsfortbildung als reales Werkzeug. |
| `methoden-mix-in-der-praxis-anwaltsschriftsatz` | Pragmatischer Methoden-Mix im Anwaltsschriftsatz. Wie Sie Wortlaut, System, Historie, Telos, Verfassung, Unionsrecht und Argumentum-Figuren konkret kombinieren. Vorrangdiskussion Larenz vs. BGH-pragmatisch. Schriftsatz-Strukturen und Formulierungsmuster. |

### Klassische Auslegungskanones (Savigny-Vierer)

| Skill | Zweck |
| --- | --- |
| `savigny-vier-auslegungsmethoden` | Savignys klassischer Vierer-Kanon (grammatikalisch, logisch-systematisch, historisch, teleologisch). Theoretische Grundlage und Anwendung im BGB. Verhältnis zur modernen pragmatischen Auslegung. Gerüst für jede Normauslegung. |
| `wortlaut-grammatikalische-auslegung` | Grammatikalische Auslegung. Allgemeiner Sprachgebrauch vs. juristische Fachsprache. Wortlaut-Grenze als äußere Grenze jeder Auslegung (jenseits davon: Rechtsfortbildung). Legaldefinitionen, Mehrdeutigkeit, unbestimmte Rechtsbegriffe. |
| `systematische-auslegung` | Systematische Auslegung. Stellung der Norm im Gesetz. Bezug zu Nachbarnormen und Verweisungen. Konkordanz mit HGB, ZPO, GG, Unionsrecht. Konkrete Beispiele zu §§ 280, 311, 433, 823 BGB. |
| `historische-auslegung` | Historische Auslegung. Subjektive vs. objektive Theorie. Arbeit mit Gesetzesmaterialien: Bundestags-Drucksachen, Ausschussberichte, Stellungnahmen. Beispiele aus der Schuldrechtsmodernisierung 2002 und neueren Reformen. Quellen-Workflow über dipbt.bundestag.de. |
| `teleologische-auslegung` | Teleologische Auslegung. Sinn und Zweck (ratio legis). Geltungstheorie vs. Entstehungstheorie. BGB-Beispiele zu Schutzzwecknormen (§§ 433, 437, 823, 1004, 1626). Warum die Teleologie in der BGH-Praxis das stärkste Argument ist und wo ihre Grenzen liegen. |

### Verfassungs- und Unionsrechtskonforme Auslegung

| Skill | Zweck |
| --- | --- |
| `verfassungs-und-unionsrechtskonforme-auslegung` | Verfassungs- und unionsrechtskonforme Auslegung. BVerfGE 7, 198 (Lüth-Drittwirkung). EuGH Marleasing C-106/89 (richtlinienkonform); EuGH von Colson C-14/83. Keine horizontale Direktwirkung von Richtlinien (EuGH Marshall 152/84). Grenzen (Wortlaut, contra legem). Anwendung im BGB (§§ 138, 242, 305 ff., 312 ff., 651a ff.). |

### Rechtsfortbildung und Argumentationsfiguren

| Skill | Zweck |
| --- | --- |
| `analogie-und-teleologische-reduktion` | Rechtsfortbildung jenseits der Wortlaut-Grenze. Analogie (planwidrige Lücke + vergleichbare Interessenlage). Teleologische Reduktion bei zu weitem Wortlaut. Gesetzes- vs. Rechtsanalogie. BGB-Beispiele (Drittschadensliquidation, Vertrag mit Schutzwirkung Dritter, § 906 II 2 BGB analog). Verbot zulasten Privater im Strafrecht und Steuerrecht. |
| `argumentum-figuren-e-contrario-a-maiore-a-fortiori` | Argumentum-Figuren. Umkehrschluss (e contrario), Erst-recht-Schluss (a maiore ad minus, a minore ad maius), a fortiori. Voraussetzungen und Verhältnis zur Analogie. BGB-Beispiele: § 181 BGB e contrario, §§ 134, 138 BGB a maiore, §§ 119, 142 BGB a fortiori. Wann diese Figuren tragen und wo sie scheitern. |

### Methodische Strömungen und Theoriegeschichte

| Skill | Zweck |
| --- | --- |
| `pandekten-und-begriffsjurisprudenz` | Pandektenwissenschaft und Begriffsjurisprudenz im 19. Jahrhundert. Puchta, Windscheid. Begriffspyramide und logisches Ableitungsmodell. Verhältnis zum BGB (1900). Kritik durch Jhering, Heck, Larenz. Wo die Begriffsjurisprudenz heute noch trifft (AT, Stellvertretung) und wo nicht. |
| `interessenjurisprudenz-heck` | Interessenjurisprudenz nach Philipp Heck. Gegenbewegung zur Begriffsjurisprudenz. Heck, Begriffsbildung und Interessenjurisprudenz 1932. Gesetz als Interessenkonflikt-Lösung. ratio legis als Interessenabwägung. Vorläufer der Wertungsjurisprudenz. Anwendung im BGB. |
| `wertungsjurisprudenz-larenz-canaris` | Wertungsjurisprudenz nach Karl Larenz und Claus-Wilhelm Canaris. Methodische Hauptströmung der deutschen Privatrechtslehre seit der Nachkriegszeit. Larenz, Methodenlehre 1960 (6. Aufl. 1991). Canaris, Systemdenken 1969. Objektive Wertungen, Rückbindung an Grundrechte und Rechtssystem. |
| `topik-viehweg-vs-systemdenken` | Topik und Jurisprudenz nach Theodor Viehweg, Topik und Jurisprudenz 1953. Renaissance der Rhetorik. Problem-Denken statt System-Denken. Topoi als Argumentationsmuster. Anwendung bei Generalklauseln, Vertragsauslegung, Schiedsverfahren. Kritik (Canaris, Larenz) und Verteidigung. |
| `diskurstheorie-habermas-alexy` | Diskurstheorie und juristische Argumentation. Habermas, Faktizität und Geltung 1992. Alexy, Theorie der juristischen Argumentation 1978. Diskursregeln, rationaler Diskurs, Anspruch auf Richtigkeit. Anwendung im Zivilrecht: Generalklauseln, Verhältnismäßigkeit, Abwägung. Kritik durch Luhmann. |
| `systemtheorie-luhmann-rechtssystem-autopoiese` | Systemtheorie Niklas Luhmanns. Luhmann, Das Recht der Gesellschaft 1993. Recht als operativ geschlossenes autopoietisches System. Binärer Code Recht/Unrecht. Verhältnis zu Wirtschaft, Politik, Wissenschaft. BGH als Beobachter zweiter Ordnung. |
| `oekonomische-analyse-des-rechts-coase-posner` | Ökonomische Analyse des Rechts (Law and Economics). Coase, The Problem of Social Cost 1960. Posner, Economic Analysis of Law 1973. Coase-Theorem, Transaktionskosten, Effizienz als Auslegungsmaßstab. Anwendung im Schadens-, Vertrags-, Nachbarrecht. Kritik aus Wertungsjurisprudenz und Grundrechtsdogmatik. |
| `legal-realism-und-critical-legal-studies` | American Legal Realism und Critical Legal Studies. Holmes, The Path of the Law 1897. Llewellyn, Frank. CLS: Unger, Kennedy. Kritik an Neutralität, Objektivität, Systemdenken. Recht als Politik mit anderen Mitteln. Kritische Außensicht auf das deutsche Zivilrecht. |
| `rechtspluralismus-und-mehrebenen-system` | Rechtspluralismus und Mehrebenen-System. Recht entsteht nicht nur durch den staatlichen Gesetzgeber. Sally Falk Moore 1973. Mehrebenenordnung Deutschland: EU, Bund, Land, Kommunal, Selbstverwaltung. Transnationale Normen, lex mercatoria, Sport-Schiedsgerichte. Vorrang Unionsrecht, autonome Auslegung. |

## Verknüpfung mit anderen Plugins

- **`zitierweise-deutsches-recht`** — Jede Aussage wird nach der Hauszitierweise belegt; BGH-Zitate mit `Az.`-Marker, Pinpoint mit Rn., Hierarchie der Gerichte.
- **`bgb-at-pruefer`** — Konkrete BGB-AT-Prüfungen (Vertragsschluss, Anfechtung, Stellvertretung, Form, Verjährung) — dieses Plugin bleibt die methodische Grundierung.
- Alle Rechtsgebiet-Plugins setzen die Methodenlehre dieses Plugins voraus und greifen über relative Pfade auf [`references/methodik-buergerliches-recht.md`](references/methodik-buergerliches-recht.md) zu.

## Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 20 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `allgemein` | Einstieg, Schnelltriage und Workflow-Routing im Methodenlehre Buergerliches Recht-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klar... |
| `analogie-und-teleologische-reduktion` | Rechtsfortbildung im deutschen Zivilrecht jenseits der Wortlaut-Grenze. Voraussetzungen der Analogie (planwidrige Regelungsluecke, vergleichbare Interessenlage). Teleologische Reduktion bei zu weitem Wortlaut. Gesetzes- vs. Rechtsanalogi... |
| `argumentum-figuren-e-contrario-a-maiore-a-fortiori` | Argumentum-Figuren im deutschen Zivilrecht. Umkehrschluss (argumentum e contrario), Erst-recht-Schluss (argumentum a maiore ad minus, a minore ad maius), argumentum a fortiori. Voraussetzungen und Verhaeltnis zur Analogie. Praezise BGB-B... |
| `diskurstheorie-habermas-alexy` | Diskurstheorie und juristische Argumentation. Juergen Habermas, Faktizitaet und Geltung 1992. Robert Alexy, Theorie der juristischen Argumentation 1978. Diskursregeln, rationaler Diskurs, Anspruch auf Richtigkeit. Verhaeltnis allgemein-p... |
| `historische-auslegung` | Historische Auslegung im deutschen Zivilrecht. Subjektive Theorie (Wille des historischen Gesetzgebers) vs. objektive Theorie (Wille des Gesetzes selbst). Arbeit mit Gesetzesmaterialien: Bundestags-Drucksachen, Ausschussberichte, Stellun... |
| `interessenjurisprudenz-heck` | Interessenjurisprudenz nach Philipp Heck. Gegenbewegung zur Begriffsjurisprudenz im fruehen 20. Jahrhundert. Hauptwerk Heck, Begriffsbildung und Interessenjurisprudenz 1932. Gesetz als Interessenkonflikt-Loesung. Methodische Folgen: rati... |
| `legal-realism-und-critical-legal-studies` | American Legal Realism und Critical Legal Studies (CLS). Oliver Wendell Holmes, The Path of the Law 1897. Karl Llewellyn, Jerome Frank. CLS-Bewegung: Roberto Mangabeira Unger, Duncan Kennedy. Kritik an Neutralitaet, Objektivitaet und Sys... |
| `methoden-mix-in-der-praxis-anwaltsschriftsatz` | Pragmatischer Methoden-Mix im Anwaltsschriftsatz. Wie Sie Wortlaut, System, Historie, Telos, Verfassung, Unionsrecht und Argumentum-Figuren konkret kombinieren. Vorrangdiskussion (Larenz vs. BGH-pragmatisch). Welche Methode in welcher Si... |
| `methodenlehre-anwenden` | Anwalt oder Rechtsstudent wendet deutsche Methodenlehre im buergerlichen Recht an: Anspruchsgrundlagen-Reihenfolge Vertrag c.i.c. GoA dinglich Delikt Gefaehrdungshaftung Bereicherung. Auslegung §§ 133 157 BGB grammatikalisch systematisch... |
| `oekonomische-analyse-des-rechts-coase-posner` | Oekonomische Analyse des Rechts (Law and Economics). Ronald H. Coase, The Problem of Social Cost 1960. Richard A. Posner, Economic Analysis of Law 1973. Coase-Theorem, Transaktionskosten, Effizienz als Auslegungsmassstab. Anwendung im de... |
| `pandekten-und-begriffsjurisprudenz` | Pandektenwissenschaft und Begriffsjurisprudenz im 19. Jahrhundert. Georg Friedrich Puchta, Bernhard Windscheid, Hauptvertreter. Begriffspyramide und logisches Ableitungsmodell. Verhaeltnis zum BGB (1900) und zur heutigen Dogmatik. Wirkun... |
| `rechtspluralismus-und-mehrebenen-system` | Rechtspluralismus und Mehrebenen-System. Recht entsteht nicht nur durch den staatlichen Gesetzgeber. Sally Falk Moore, semi-autonomous social fields 1973. Mehrebenenordnung Deutschland: EU, Bund, Land, Kommunal, Selbstverwaltung. Transna... |
| `savigny-vier-auslegungsmethoden` | Savignys klassischer Vierer-Kanon der Auslegung (grammatikalisch, logisch-systematisch, historisch, teleologisch). Theoretische Grundlage, Werkstand, Anwendung im BGB, Verhaeltnis zur modernen pragmatischen Auslegung. Klaert, warum die B... |
| `systematische-auslegung` | Systematische Auslegung im deutschen Zivilrecht. Stellung der Norm im Gesetz (Buch, Abschnitt, Titel, Untertitel). Bezug zu Nachbarnormen und Verweisungen. Auslegung im Lichte von Ueberschriften, Definitionen und Gesetzesarchitektur. Kon... |
| `systemtheorie-luhmann-rechtssystem-autopoiese` | Systemtheorie Niklas Luhmanns und das Recht. Luhmann, Das Recht der Gesellschaft 1993. Recht als operativ geschlossenes autopoietisches System. Binaerer Code Recht/Unrecht. Verhaeltnis zu anderen gesellschaftlichen Teilsystemen (Wirtscha... |
| `teleologische-auslegung` | Teleologische Auslegung im deutschen Zivilrecht. Sinn und Zweck der Norm (ratio legis). Geltungstheorie vs. Entstehungstheorie. Konkrete BGB-Beispiele zu Schutzzwecknormen (§§ 433 437 823 1004 1626). Verhaeltnis zur historischen Auslegun... |
| `topik-viehweg-vs-systemdenken` | Topik und Jurisprudenz nach Theodor Viehweg. Viehweg, Topik und Jurisprudenz 1953. Renaissance der Rhetorik in der Methodenlehre. Problem-Denken statt System-Denken. Topoi als Argumentationsmuster. Verhaeltnis zur Begriffsjurisprudenz un... |
| `verfassungs-und-unionsrechtskonforme-auslegung` | Verfassungs- und unionsrechtskonforme Auslegung im deutschen Zivilrecht. BVerfGE 7 198 Lueth-Drittwirkung der Grundrechte. EuGH Marleasing C-106/89 richtlinienkonforme Auslegung; EuGH von Colson C-14/83. Keine horizontale Direktwirkung v... |
| `wertungsjurisprudenz-larenz-canaris` | Wertungsjurisprudenz nach Karl Larenz und Claus-Wilhelm Canaris. Methodische Hauptstroemung der deutschen Privatrechtslehre seit der Nachkriegszeit. Larenz, Methodenlehre der Rechtswissenschaft 1960 (6. Aufl. 1991). Canaris, Systemdenken... |
| `wortlaut-grammatikalische-auslegung` | Grammatikalische Auslegung im deutschen Zivilrecht. Bedeutung im allgemeinen Sprachgebrauch vs. juristischer Fachsprache. Wortlaut-Grenze als aeussere Grenze jeder Auslegung (jenseits davon: Rechtsfortbildung). Umgang mit Legaldefinition... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
