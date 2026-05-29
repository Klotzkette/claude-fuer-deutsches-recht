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

| Skill | Zweck |
| --- | --- |
| `allgemein` | Einstieg, Triage und Workflow-Routing im Plugin. Bei stummem Upload (Dokument ohne Begleittext) reagiert der Skill eigenständig: ordnet das Material, prüft Eil- und Fristenhinweise, schlägt den passenden Spezial-Skill vor oder stellt genau eine gezielte Rückfrage. |
| `methodenlehre-anwenden` | Wende deutsche juristische Methodenlehre auf zivilrechtliche Bewertungen an. Anspruchsgrundlagen-Reihenfolge, Auslegung Wortlaut Systematik Historie Telos ohne starre Rangfolge. Pragmatische BGH-Praxis: Teleologie dominiert in Begründungen. Rechtsfortbildung als reales Werkzeug. Aus Anwaltsperspektive — was Gerichte wirklich tun, nicht was Lehrbücher fordern. |

## Verknüpfung mit anderen Plugins

- **`zitierweise-deutsches-recht`** — Jede Aussage wird nach der Hauszitierweise belegt; BGH-Zitate mit `Az.`-Marker, Pinpoint mit Rn., Hierarchie der Gerichte.
- **`bgb-at-pruefer`** — Konkrete BGB-AT-Prüfungen (Vertragsschluss, Anfechtung, Stellvertretung, Form, Verjährung) — dieses Plugin bleibt die methodische Grundierung.
- Alle Rechtsgebiet-Plugins setzen die Methodenlehre dieses Plugins voraus und greifen über relative Pfade auf [`references/methodik-buergerliches-recht.md`](references/methodik-buergerliches-recht.md) zu.

## Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.
