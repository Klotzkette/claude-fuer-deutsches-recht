# WEG- und Hausverwaltung

Operatives Plugin für Wohnungseigentümergemeinschaften, Hausverwaltungen, Verwaltungsbeiräte und anwaltliche Begleitung. Der Schwerpunkt liegt nicht auf abstrakter Dogmatik, sondern auf den täglichen Vorgängen: Eigentümerversammlung vorbereiten, Beschlussvorlagen schreiben, Beschlüsse protokollieren, Beschlusssammlung pflegen, Wirtschaftsplan und Jahresabrechnung prüfen, Hausgeld und Sonderumlagen verfolgen, Betriebskosten/Nebenkosten kontrollieren, Handwerker beauftragen, Erhaltungsmaßnahmen steuern, Restaurant- und Hausordnungskonflikte sortieren, E-Mobilität/Steckersolar/PV beschlussreif machen und rechtliche Eskalationen rechtzeitig erkennen.

Das Plugin arbeitet paralegal-praktisch: Es erstellt keine "Rechtsberatung aus dem Nichts", sondern strukturiert Akten, formuliert Beschluss- und Anschreibenentwürfe, baut Prüfmatrizen, markiert Fristen, trennt kaufmännische Verwaltung von Rechtsfragen und schlägt bei Risiko den passenden Anwalts- oder Gerichtspfad vor.

## Direkt-Download (einzelnes ZIP)

| Plugin | Direkt-Download |
| --- | --- |
| WEG- und Hausverwaltung (`weg-hausverwaltung`, dieses Plugin) | [weg-hausverwaltung.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/weg-hausverwaltung.zip) |

Die URL ist stabil und zeigt immer auf die neueste Version. Alle weiteren Plugins sind unter [Releases · latest](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest) genauso einzeln verfügbar.

## Zum Ausprobieren: Testakte

| Testakte | Direkt-Download |
| --- | --- |
| **Hohenzollernhof WEG/Hausverwaltung** | [testakte-weg-hausverwaltung-hohenzollernhof.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-weg-hausverwaltung-hohenzollernhof.zip) |

Die Arbeitsakte enthält eine unordentliche WEG-Verwaltungsakte mit Eigentümerbeschwerden, WhatsApp- und E-Mail-Fragmenten, Handwerkerangeboten, fehleranfälliger Jahresabrechnung, Entwurf einer Eigentümerversammlung, Steckersolar-/Wallbox-/PV-Anträgen, Sonderumlage, Heizungs- und Versicherungsschäden, Restaurantkonflikt, Fahrrad-/Tauben-/Kinder-/Hof-Streit und Beiratsnotizen. Zusätzlich liegt eine konsolidierte Akten-PDF mit über 100 Seiten bei.

## Installation in Claude Code

1. ZIP herunterladen.
2. Claude Code -> **Customize Plugins** -> **Install from .zip** -> Datei wählen.
3. Fertig. Skills sind sofort verfügbar.

> Für den ZIP-Upload muss das Archiv direkt `.claude-plugin/plugin.json`, `skills/` und `references/` im ZIP-Root enthalten. Nicht das komplette Repository-ZIP aus "Code -> Download ZIP" verwenden.

## Quellen- und Rollenregel

- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
- Bei streitigen Beschlüssen, Verjährung, Anfechtung, Schadensersatz, Verwalterhaftung oder gerichtlichen Schritten immer anwaltliche Eskalation markieren.
- Verwaltungspraxis, kaufmännische Kontrolle und juristische Bewertung werden sichtbar getrennt.

## Enthaltene Skills

| Skill | Zweck |
| --- | --- |
| `allgemein` | Einstieg, Triage, Upload-Erkennung und Workflow-Routing im WEG-/Hausverwaltungsalltag. |
| `rechtsstand-mai-2026-faktenbank` | Quellen-Gate mit WEG/BGB/BetrKV-Ankern und frei verifizierten BGH-Linien. |
| `mandat-objekt-triage` | Objekt, Gemeinschaft, Rollen, Verwaltervertrag, Teilungserklärung, Fristen und Aktenlage erfassen. |
| `grossakte-konfliktlandkarte` | Große unübersichtliche Verwaltungsakten clustern, priorisieren und in passende Spezial-Skills routen. |
| `eigentuemerversammlung-vorbereiten` | Versammlung vom Themenstapel bis zur Beschlussreife planen. |
| `einladung-tagesordnung-fristen` | Einladung, Tagesordnung, Ladungsfristen und Vollmachten prüfen. |
| `beschlussvorlagen-erstellen` | Rechtssichere und verständliche Beschlussvorlagen mit Alternativen formulieren. |
| `protokollwerkstatt-top-marathon` | Lange Eigentümerversammlungen mit vielen TOPs protokollfähig strukturieren. |
| `beschlusssammlung-protokoll` | Protokoll, Beschlusssammlung, Verkündung, Anlagen und Nachversand strukturieren. |
| `beschlussanfechtung-risiko` | Anfechtungs- und Nichtigkeitsrisiken nach §§ 44 und 45 WEG erkennen. |
| `wirtschaftsplan-jahresabrechnung-28-weg` | Wirtschaftsplan, Jahresabrechnung, Vermögensbericht, Nachschüsse und Vorschüsse prüfen. |
| `abrechnung-ist-plan-mieterschnittstelle` | Ist-/Plan-Kosten, Verteilerschlüssel, Betriebskosten und vermietende Eigentümer zusammenführen. |
| `hausgeld-sonderumlage-liquiditaet` | Hausgeldrückstände, Sonderumlagen, Liquidität, Mahnung und Klagepfad ordnen. |
| `betriebskosten-nebenkostenabrechnung` | Betriebskosten/Nebenkosten nach BetrKV, Mietvertrag und WEG-Abrechnung kontrollieren. |
| `handwerker-beauftragung-vergabe` | Angebote einholen, vergleichen, beauftragen, Nachträge prüfen und Dokumentation sichern. |
| `erhaltung-modernisierung-baumaengel` | Erhaltung, Modernisierung, Mängel, Gewährleistung und Bauüberwachung verwalten. |
| `heizung-schaden-versicherung-notmassnahme` | Heizungsstörung, Wasserschaden, Versicherung, Sofortmaßnahme und Beschlussnachlauf ordnen. |
| `bauliche-veraenderungen-20-weg` | Bauliche Veränderungen nach §§ 20 und 21 WEG beschlussfähig vorbereiten. |
| `steckersolar-wallbox-barrierefreiheit` | Privilegierte Maßnahmen: Steckersolar, E-Mobilität, Einbruchsschutz, Glasfaser, Barrierefreiheit. |
| `e-mobilitaet-steckersolar-kellerstrom` | Wallbox, Ladeinfrastruktur, Dach-PV, Steckersolar und riskante Kellerstrom-Provisorien prüfen. |
| `verwalterpflichten-26-27-weg` | Bestellung, Abberufung, Vertretungsmacht, Maßnahmenkatalog, Verwaltervertrag. |
| `eigentuemerkommunikation-beschwerde` | Eigentümerkommunikation, Beschwerden, Eskalationsmails und transparente Antwortbausteine. |
| `stoerung-hausordnung-mieter-eigentuemer` | Lärm, Müll, Feuchtigkeit, Gemeinschaftsflächen, Mieter als Störer, Hausordnung. |
| `gewerbe-restaurant-geruch-laerm-hof` | Restaurant-/Gewerbekonflikte mit Geruch, Lärm, Müll, Lieferverkehr, Hofnutzung und Betreiberrollen. |
| `hausordnung-tauben-fahrrad-kinder-weihnachtsbaum` | Alltagssachen sauber sortieren: Tauben, Fahrraddiebstahl, Kinder, Weihnachtsbaum, Fluchtwege. |
| `beirat-controlling-verwalter` | Verwaltungsbeirat: Rechnungsprüfung, Angebotskontrolle, Protokollcheck, Eskalationsnotiz. |
| `datenschutz-dokumentenfreigabe` | DSGVO, Eigentümerlisten, Belegeinsicht, Schwärzungen, Cloud-Freigaben. |
| `eskalation-anwalt-amtsgericht` | Wann Anwalt, Amtsgericht, Beschlussklage, Hausgeldklage oder einstweiliger Rechtsschutz nötig wird. |

## Typische Workflows

**Eigentümerversammlung:** `grossakte-konfliktlandkarte` -> `eigentuemerversammlung-vorbereiten` -> `einladung-tagesordnung-fristen` -> `beschlussvorlagen-erstellen` -> `protokollwerkstatt-top-marathon` -> `beschlussanfechtung-risiko`.

**Jahresabrechnung:** `wirtschaftsplan-jahresabrechnung-28-weg` -> `abrechnung-ist-plan-mieterschnittstelle` -> `beirat-controlling-verwalter` -> `hausgeld-sonderumlage-liquiditaet` -> bei vermieteten Wohnungen zusätzlich `betriebskosten-nebenkostenabrechnung`.

**Handwerkermaßnahme:** `erhaltung-modernisierung-baumaengel` -> `handwerker-beauftragung-vergabe` -> `beschlussvorlagen-erstellen` -> `eigentuemerkommunikation-beschwerde` -> bei Streit `eskalation-anwalt-amtsgericht`.

**Alltagskonflikt:** `grossakte-konfliktlandkarte` -> `hausordnung-tauben-fahrrad-kinder-weihnachtsbaum` oder `gewerbe-restaurant-geruch-laerm-hof` -> `eigentuemerkommunikation-beschwerde` -> bei hartem Konflikt `eskalation-anwalt-amtsgericht`.

## Grenzen

Das Plugin ersetzt keine anwaltliche Beratung, keine WEG-Spezialkanzlei, keine Steuerberatung und keine technische Bauleitung. Es hilft, die Verwaltung so zu dokumentieren, dass Anwälte, Beiräte, Verwalter und Eigentümer sauber weiterarbeiten können.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 28 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `abrechnung-ist-plan-mieterschnittstelle` | Prüft Jahresabrechnung, Wirtschaftsplan, Ist-Kosten, Planansätze und Mieterschnittstelle. Erkennt Verteilerschlüssel, umlagefähige Betriebskosten, Gewerbeanteile, Nachzahlungen, Belegeinsicht und Vermieterkommunikation. Output: Prüfmatrix. |
| `allgemein` | Einstieg, Schnelltriage und Workflow-Routing im WEG- und Hausverwaltungs-Plugin (Stand 05/2026). Ordnet Uploads, erkennt Fristen und Risiken, fragt Rolle und Objekt ab und schlägt passende Skills für Beschlüsse, Eigentümerversammlung, Ab... |
| `bauliche-veraenderungen-20-weg` | Prüft bauliche Veränderungen nach §§ 20 und 21 WEG (Stand 05/2026): Anspruch, Gestattung, Grenzen, Kostenfolge, Gebrauch, Auflagen, Rückbau, Beschlussvorschlag und Anfechtungsrisiko, einschließlich der BGH-Linie 2024-2025 zu Klimasplitge... |
| `beirat-controlling-verwalter` | Unterstützt Verwaltungsbeiräte bei Rechnungsprüfung, Angebotskontrolle, Beschlussvorbereitung, Protokollcheck, Verwalterkommunikation und Eskalationsnotizen (Stand 05/2026); berücksichtigt BGH V ZR 34/24 (Schadensersatzweg über GdWE) und... |
| `beschlussanfechtung-risiko` | Prüft Beschlüsse auf Anfechtungs- und Nichtigkeitsrisiken nach §§ 44 und 45 WEG (Stand 05/2026): Frist, Beschlusskompetenz, Einladung, Tagesordnung, Mehrheit, Kostenfolge, Bestimmtheit, ordnungsmäßige Verwaltung sowie BGH-Linie zu Schlüs... |
| `beschlusssammlung-protokoll` | Erstellt und prüft Protokoll, Beschlussverkündung, Beschlusssammlung (§ 24 Abs. 7 WEG), Anlagenverweise, Abstimmungsergebnis, Nachversand und Dokumentationsstand (Stand 05/2026). Sorgt dafür, dass Auslegungsfragen späterer Beschlussklage... |
| `beschlussvorlagen-erstellen` | Erstellt WEG-Beschlussvorlagen mit Beschlusskompetenz, Kostenfolge, Ausführungsdetails, Alternativen, Begründung, Anlagenverweis und Anfechtungsrisiko (Stand 05/2026). Liefert Mustertexte für Abrechnungsspitzen, Sonderumlage, Schlüsselän... |
| `betriebskosten-nebenkostenabrechnung` | Kontrolliert Betriebskosten- und Nebenkostenabrechnungen im Hausverwaltungs- und Vermietungskontext (Stand 05/2026): BetrKV, HeizkostenV, Mietvertrag, WEG-Abrechnung, Umlagefähigkeit, Abrechnungsfrist § 556 Abs. 3 BGB, Verteilerschlüssel... |
| `datenschutz-dokumentenfreigabe` | Prüft Datenschutz und Dokumentenfreigaben in der Hausverwaltung (Stand 05/2026): Eigentümerlisten, Belegeinsicht, Handwerkerdaten, Mieterbeschwerden, Cloud-Ordner, Schwärzungen und Versandkreis. Schnittstelle zum Datenschutzrecht-Plugin... |
| `e-mobilitaet-steckersolar-kellerstrom` | Prüft E-Mobilität, Wallboxen, Ladeinfrastruktur, Steckersolar, Dach-PV und unzulässige Kellerstrom-Lösungen in WEG-Anlagen. Ordnet § 20 WEG, Brandschutz, Messkonzept, Kosten, Netzanschluss und Beschlussvarianten. Output: Beschluss- und R... |
| `eigentuemerkommunikation-beschwerde` | Formuliert klare, deeskalierende und dokumentationssichere Kommunikation an Eigentümer, Beirat, Mieter und Handwerker bei Beschwerden, Rückfragen, Fristen und Beschlussumsetzung (Stand 05/2026). Berücksichtigt aktuelle BGH-Linien (Abrech... |
| `eigentuemerversammlung-vorbereiten` | Plant eine Eigentümerversammlung (Stand 05/2026) von Themenstapel, Beschlussbedarf, Unterlagen, Beiratsabstimmung, Einladungszeitplan, Raum/virtueller Teilnahme bis zur Nachbereitung. Berücksichtigt § 23 Abs. 1a WEG, BGH-Linie zu Vorbefa... |
| `einladung-tagesordnung-fristen` | Prüft und erstellt Einladungen zur Eigentümerversammlung mit Tagesordnung, Ladungsfrist, Zugang, Vollmacht, Beschlussgegenständen, Anlagen und Fristenkontrolle (Stand 05/2026). Berücksichtigt § 24 Abs. 4 WEG (Ladungsfrist 3 Wochen), § 23... |
| `erhaltung-modernisierung-baumaengel` | Steuert Erhaltungsmaßnahmen, Modernisierung, Baumängel, Gewährleistungsfristen, Gutachten, Sofortmaßnahmen, Beschlussbedarf und Kommunikation mit Eigentümern (Stand 05/2026). Berücksichtigt GEG § 71 (65 % erneuerbare Energien beim Heizun... |
| `eskalation-anwalt-amtsgericht` | Erkennt, wann ein WEG-/Hausverwaltungsvorgang nicht mehr nur Verwaltung ist (Stand 05/2026): Anwalt, Beschlussklage, Hausgeldklage, einstweiliger Rechtsschutz, Beweissicherung, Verwalterhaftung über GdWE oder Vergleich; berücksichtigt Fr... |
| `gewerbe-restaurant-geruch-laerm-hof` | Bearbeitet Restaurant- und Gewerbekonflikte in WEG-Anlagen: Geruch, Lüftung, Lärm, Müll, Lieferverkehr, Fettabscheider, Sondernutzung, Brandschutz und Mieter-/Eigentümerrollen. Output: Eskalations- und Beschlussplan. |
| `grossakte-konfliktlandkarte` | Ordnet unübersichtliche WEG- und Hausverwaltungsakten mit vielen Konflikten: Heizung, Dach, Gewerbe, Geruch, Tauben, Fahrrad, Kinder, Wallbox, Steckersolar, Nebenkosten, Protokolle und Beschlüsse. Output: Konfliktlandkarte, Prioritätenpl... |
| `handwerker-beauftragung-vergabe` | Begleitet Handwerkerbeauftragung in der WEG (Stand 05/2026): Leistungsbeschreibung, Vergleichsangebote, Beschlussbedarf, Budget, Nachträge, Abnahme, Rechnungskontrolle, Gewährleistung, Dokumentation; berücksichtigt § 27 WEG (Verwalterkom... |
| `hausgeld-sonderumlage-liquiditaet` | Prüft Hausgeld, Vorschüsse, Rückstände, Sonderumlagen, Liquidität, Mahnungen, Ratenzahlung, Beschlussgrundlage und Klagepfad der GdWE (Stand 05/2026). Berücksichtigt BGH V ZR 190/24 zum Zurückbehaltungsrecht und V ZR 139/23 zur Verteilun... |
| `hausordnung-tauben-fahrrad-kinder-weihnachtsbaum` | Ordnet Alltagskonflikte in WEG-Anlagen: Tauben auf Balkonen, Fahrradkeller, Diebstahl, Kinderlärm, Spielhof, Weihnachtsbaum, Brandschutz, Hausordnung und Kommunikation. Output: Maßnahmenmatrix und deeskalierende Schreiben. |
| `heizung-schaden-versicherung-notmassnahme` | Bearbeitet Heizungsstörungen, Wasserschäden, Feuchtigkeit, Frost, Versicherung und Notmaßnahmen in WEG-Anlagen. Prüft Zuständigkeit, Sofortmaßnahmen, Beweise, Handwerker, Beschlussbedarf, Umlage und Mieterkommunikation. Output: Maßnahmen... |
| `mandat-objekt-triage` | Erfasst eine WEG-/Hausverwaltungsakte (Stand 05/2026): Objekt, Rollen, Teilungserklärung, Gemeinschaftsordnung, Verwaltervertrag, Beschlusssammlung, Abrechnungen, Vermögensbericht, Angebote, Fristen, Risiken und nächsten Workflow. Identi... |
| `protokollwerkstatt-top-marathon` | Erstellt und prüft Protokolle für lange Eigentümerversammlungen mit vielen Tagesordnungspunkten. Trennt Aussprache, Antrag, Beschlusswortlaut, Abstimmung, Verkündung, Anlagen und Nacharbeit. Output: protokollfähige TOP-Struktur. |
| `rechtsstand-mai-2026-faktenbank` | Quellen-Gate für WEG und Hausverwaltung mit Stand 05/2026. Enthält Normanker zu WEG, BGB, BetrKV, HeizkostenV, GEG und CO2KostAufG sowie frei verifizierte BGH-Rechtsprechung des V. Zivilsenats 2024 bis 2026 zu Kostenverteilung, baulichen... |
| `steckersolar-wallbox-barrierefreiheit` | Spezialworkflow für privilegierte Maßnahmen nach § 20 Abs. 2 WEG (Stand 05/2026): Steckersolargerät, Wallbox/E-Mobilität, barrierefreier Umbau, Einbruchsschutz, Glasfaseranschluss. Prüft Anspruch, technische Unterlagen, Auflagen, Beschlu... |
| `stoerung-hausordnung-mieter-eigentuemer` | Bearbeitet Störungen in der WEG (Stand 05/2026): Lärm, Müll, Feuchtigkeit, Geruch, Kamera, Gemeinschaftsflächen, Mieter als Störer, vermietender Eigentümer, Hausordnung, Abmahnung, Beweissicherung. Berücksichtigt BGH V ZR 1/24 (mittelbar... |
| `verwalterpflichten-26-27-weg` | Prüft Verwalterbestellung, Abberufung, Verwaltervertrag, Aufgaben und Befugnisse nach §§ 26 und 27 WEG (Stand 05/2026), laufende Verwaltung, Eilmaßnahmen, Vertretung der GdWE und Haftung; berücksichtigt BGH V ZR 34/24 (keine Schutzwirkun... |
| `wirtschaftsplan-jahresabrechnung-28-weg` | Prüft Wirtschaftsplan, Jahresabrechnung, Vermögensbericht, Nachschüsse, Vorschussanpassungen, Rücklagen, Verteilerschlüssel, Beleglage und Beschlussformulierung nach § 28 WEG (Stand 05/2026). Berücksichtigt BGH V ZR 102/23 (Auslegung des... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
