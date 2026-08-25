# 1. Fachmodule des Plugins

Diese Karte dient der gezielten Auswahl. Lies sie nur, wenn der Auftrag keinen eindeutigen Primärskill erkennen lässt oder eine fachliche Schnittstelle geprüft werden muss.

Das Plugin enthält 20 Skills, gegliedert in fünf Blöcke. Für eine konkrete zivilrechtliche Bewertung reicht meistens `methodenlehre-anwenden` plus ein oder zwei Vertiefungsskills aus den Auslegungs- oder Rechtsfortbildungs-Blöcken. Die Strömungs-Skills sind für Hausarbeiten, Methoden-Memos und akademische Diskussion gedacht.

**Block A — Praxis-Einstieg und Anwendung**

| Skill | Wann vorschlagen? |
|---|---|
| `methodenlehre-anwenden` | Immer dann, wenn eine zivilrechtliche Frage methodisch sauber geprüft werden soll: Anspruchsgrundlagen-Reihenfolge, Auslegung der einschlägigen Norm nach Wortlaut/System/Historie/Telos, Lückenfüllung durch Analogie oder teleologische Reduktion. |
| `methoden-mix-in-der-praxis-anwaltsschriftsatz` | Wenn ein Anwaltsschriftsatz mehrere Auslegungsmethoden bewusst kombinieren soll. Vorrangdiskussion (Larenz vs. BGH-pragmatisch). Formulierungsmuster für offene und geschlossene Rechtslagen. |

**Block B — Klassische Auslegungskanones (Savigny-Vierer)**

| Skill | Wann vorschlagen? |
|---|---|
| `savigny-vier-auslegungsmethoden` | Wenn das Gerüst der vier Auslegungsmethoden gebraucht wird. Theoretische Grundlage, Werkstand, Verhältnis zur modernen pragmatischen Auslegung. |
| `wortlaut-grammatikalische-auslegung` | Wenn der Wortlaut trägt oder als Grenze diskutiert werden muss. Legaldefinitionen, Mehrdeutigkeit, unbestimmte Rechtsbegriffe. |
| `systematische-auslegung` | Wenn Stellung der Norm, Nachbarnormen, Verweisungen oder Konkordanz mit HGB/ZPO/GG/Unionsrecht den Ausschlag geben. |
| `historische-auslegung` | Wenn Gesetzesmaterialien Argumente liefern. Bundestags-Drucksachen, Ausschussberichte, Schuldrechtsmodernisierung 2002 und neuere Reformen. über dipbt.bundestag.de. |
| `teleologische-auslegung` | Wenn Sinn und Zweck der Norm das stärkste Argument ist — in der BGH-Praxis fast immer. Schutzzwecknormen. |

**Block C — Verfassungs- und Unionsrechtskonforme Auslegung**

| Skill | Wann vorschlagen? |
|---|---|
| `verfassungs-und-unionsrechtskonforme-auslegung` | Wenn Grundrechte mittelbare Drittwirkung entfalten (BVerfGE 7, 198) oder eine Norm unionsrechtlichen Ursprung hat (Marleasing, von Colson). Grenzen contra legem. |

**Block D — Rechtsfortbildung und Argumentationsfiguren**

| Skill | Wann vorschlagen? |
|---|---|
| `analogie-und-teleologische-reduktion` | Wenn die Wortlaut-Grenze überschritten werden muss. Planwidrige Lücke, vergleichbare Interessenlage. Drittschadensliquidation, Vertrag mit Schutzwirkung Dritter, § 906 II 2 BGB analog. |
| `argumentum-figuren-e-contrario-a-maiore-a-fortiori` | Wenn ein Umkehrschluss, Erst-recht-Schluss oder a fortiori-Argument trägt oder zurückgewiesen werden muss. Verhältnis zur Analogie. |

**Block E — Methodische Strömungen und Theoriegeschichte**

| Skill | Wann vorschlagen? |
|---|---|
| `pandekten-und-begriffsjurisprudenz` | Wenn Begriffspyramide oder logisches Ableitungsmodell zu erkennen oder zu kritisieren ist. AT, Stellvertretungsrecht. |
| `interessenjurisprudenz-heck` | Wenn ratio legis als Interessenabwägung formuliert werden soll. Vorstufe zur Wertungsjurisprudenz. |
| `wertungsjurisprudenz-larenz-canaris` | Wenn objektive Wertungen und Grundrechtsdogmatik die Auslegung tragen. Hauptströmung der deutschen Privatrechtslehre seit der Nachkriegszeit. |
| `topik-viehweg-vs-systemdenken` | Wenn Problemdenken statt Systemdenken überzeugt: Generalklauseln, Vertragsauslegung, Schiedsverfahren. |
| `diskurstheorie-habermas-alexy` | Wenn Diskursregeln und Anspruch auf Richtigkeit als methodische Stufe gebraucht werden. Verhältnismäßigkeit, Abwägung. |
| `systemtheorie-luhmann-rechtssystem-autopoiese` | Wenn das Recht als operativ geschlossenes autopoietisches System beschrieben werden soll. BGH als Beobachter zweiter Ordnung. |
| `oekonomische-analyse-des-rechts-coase-posner` | Wenn Effizienzargumente diskutiert werden. Coase-Theorem, Transaktionskosten. Schadens-, Vertrags-, Nachbarrecht. |
| `legal-realism-und-critical-legal-studies` | Wenn eine kritische Außensicht auf die deutsche Wertungsjurisprudenz nötig ist. Holmes, Llewellyn, Frank, Unger, Kennedy. |
| `rechtspluralismus-und-mehrebenen-system` | Wenn parallele Rechtsordnungen, lex mercatoria, Sport-Schiedsgerichte oder die Mehrebenenordnung Deutschland/EU mitgedacht werden müssen. |

**Routing-Faustregel:**

- *Schnelle Erstbewertung einer zivilrechtlichen Frage* → `methodenlehre-anwenden` direkt aktivieren.
- *Auslegung einer konkreten Norm* → `methodenlehre-anwenden` plus den zur tragenden Methode passenden Skill aus Block B (Wortlaut, System, Historie, Telos).
- *Wortlaut zu weit oder zu eng* → zusätzlich `analogie-und-teleologische-reduktion` und ggf. `argumentum-figuren-e-contrario-a-maiore-a-fortiori`.
- *Norm hat unionsrechtlichen Ursprung* → zusätzlich `verfassungs-und-unionsrechtskonforme-auslegung`.
- *Anwaltsschriftsatz mit mehreren Argumentationslinien* → `methoden-mix-in-der-praxis-anwaltsschriftsatz`.
- *Hausarbeit, Methoden-Memo, akademische Reflexion* → passende Skills aus Block E (Strömungen).
- *BGB-AT-Detailprüfung (Vertragsschluss, Anfechtung, Stellvertretung, Form, Verjährung)* → Plugin `bgb-at-pruefer` zusätzlich hinzuladen; dieses Plugin bleibt die methodische Klammer.
- *Zitierfragen* → Plugin `zitierweise-deutsches-recht`.
- *Konkrete Rechtsgebiete* (Erbrecht, Arbeitsrecht, Familienrecht, Gesellschaftsrecht etc.) → das jeweilige Fachplugin; die Methodenlehre dieses Plugins gilt als Grundierung.
