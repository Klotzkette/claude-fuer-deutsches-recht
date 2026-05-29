# Betreuungsrecht

Skills für **berufliche Betreuerinnen und Betreuer** nach dem Betreuungsorganisationsgesetz
(BtOG) und den §§ 1814 ff. BGB in der Fassung der Reform 2023.

> ⚠️ **Experimentell — keine Fachgutachten.** Die Skills sind generalisierte
> Beispiele. Jede Berufsbetreuerin und jeder Berufsbetreuer kalibriert die
> Skills selbst für die eigene Praxis und prüft jeden generierten Bericht
> vor Einreichung beim Betreuungsgericht.

## ⬇️ Direkt-Download (einzelnes ZIP)

| Plugin | Direkt-Download |
| --- | --- |
| Betreuungsrecht (`betreuungsrecht`, dieses Plugin) | [betreuungsrecht.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/betreuungsrecht.zip) |

Die URL ist stabil und zeigt immer auf die neueste Version. Alle weiteren Plugins sind unter [Releases · latest](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest) genauso einzeln verfügbar.

### Installation in Claude Code

1. ZIP herunterladen (Link oben).
2. Claude Code → **Customize Plugins** → **Install from .zip** → Datei wählen.
3. Fertig. Skills sind sofort verfügbar.

> **Hinweis:** Für den ZIP-Upload muss das Archiv direkt `.claude-plugin/plugin.json`, `skills/`, `assets/` und `references/` im ZIP-Root enthalten. **Nicht** das komplette Repository-ZIP aus "Code → Download ZIP" verwenden.

### Zum Ausprobieren: Beispielakte (separat)

Fiktive Mandatsakte zum sofortigen Testen — **kein Teil des Plugins**, separater Download:

[testakte-betreuung-hildegard-sauer.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-betreuung-hildegard-sauer.zip)

Fiktive Akte einer Berufsbetreuung einer 87-jährigen Mandantin (Hildegard Sauer): Bestellungsbeschluss, Vermögensverzeichnis, erster Jahresbericht, Genehmigungsanträge.

[testakte-betreuung-schmalfeld-kontodaten-vertraege.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-betreuung-schmalfeld-kontodaten-vertraege.zip)

Fiktive Akte einer Vermögenssorge-Prüfung bei Herbert Wilhelm Schmalfeld:
Kontoauszüge 2023 bis 2025, Vertragsregister, verdächtige Zahlungen,
Fernwartung, Auslandsanlage, Immobilienreservierung und Maßnahmenplan.


## Enthaltene Skills

| Skill | Gegenstand | Rechtsnorm |
|---|---|---|
| `jahresbericht-betreuungsgericht` | Strukturierter Jahresbericht ans Betreuungsgericht aus Ereignissen, E-Mails, Quittungen und Aktenvermerken | § 1863 BGB |
| `vermoegensverzeichnis-pruefung` | Erstellung und Aktualisierung des Vermögensverzeichnisses bei Übernahme der Betreuung | §§ 1835, 1839 BGB |
| `genehmigungspflicht-pruefung` | Prüfung, ob ein konkretes Rechtsgeschäft (Grundstücksverkauf, Erbausschlagung, Darlehen, Wohnungsauflösung, Heimvertrag) der Genehmigung des Betreuungsgerichts bedarf | §§ 1848–1858 BGB |
| `kontodaten-vertragsverdacht-pruefung` | Kontoauszüge und Vertragsunterlagen auf verdächtige Vermögensabflüsse, Fernwartung, Hochrisikoanlagen, Auslandszahlungen und Schutzmaßnahmen prüfen | §§ 1821, 1825, 1835, 1865 BGB |

## Adressatenkreis

- Berufsbetreuerinnen und Berufsbetreuer mit Sachkundenachweis nach § 23 BtOG
- Vereinsbetreuerinnen und Vereinsbetreuer (§ 18 BtOG)
- Mitarbeitende von Betreuungsbehörden (§§ 6 ff. BtOG)
- Ehrenamtliche Betreuer (eingeschränkt; gerichtliche Beratung empfohlen)

## Wichtige Rechtsgrundlagen

- **BGB Buch 4 Abschnitt 3 (§§ 1814–1881)** — Rechtliche Betreuung (Reform 2023)
- **BtOG** — Betreuungsorganisationsgesetz (registrierte Berufsbetreuer, Vergütung, Aufsicht)
- **VBVG** — Vormünder- und Betreuervergütungsgesetz
- **FamFG §§ 271 ff.** — Verfahren in Betreuungssachen

## Zitierhinweise

Alle Skills zitieren nach den in der deutschen Rechtspraxis üblichen Konventionen:

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
- Quellenregel: Keine Kommentar-, Handbuch-, Aufsatz- oder Tabellenfundstellen aus Modellwissen; nur Nutzerquelle, amtliche/freie Quelle oder lizenzierte Live-Verifikation verwenden.

## Datenschutz und Vertraulichkeit

Berichte an das Betreuungsgericht enthalten Gesundheits-, Vermögens- und Sozialdaten.
Beim Einsatz von KI-Tools sind insbesondere zu beachten:

- Art. 9 DSGVO (besondere Kategorien personenbezogener Daten)
- § 203 StGB (Verletzung von Privatgeheimnissen — gilt für Berufsbetreuer)
- Empfehlung: Personenbezogene Daten vor Übergabe an KI pseudonymisieren
  (siehe Skill `playbook-aus-eigenen-daten` im Plugin `kanzlei-builder-hub`)
