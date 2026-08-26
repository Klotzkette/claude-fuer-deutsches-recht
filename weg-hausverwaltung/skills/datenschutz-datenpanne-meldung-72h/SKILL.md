---
name: datenschutz-datenpanne-meldung-72h
description: "Für Datenpanne: 72-Stunden-Meldepflicht für die Hausverwaltung: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt."
---

# Datenpanne: 72-Stunden-Meldepflicht für die Hausverwaltung

## Fachlicher Anker

- **Normen:** §§ 535, §§ 18, § 16 Abs. 2.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Ziel

Bei Datenschutzverletzungen muss die Hausverwaltung binnen 72 Stunden nach Kenntniserlangung die zuständige Aufsichtsbehörde informieren (Art. 33 DSGVO) und ggf. Betroffene benachrichtigen (Art. 34 DSGVO). Der Skill liefert Risikobewertungs-Schema, Meldewege und fertige Mustertexte für die häufigsten Pannen-Szenarien.

## Typische Datenpannen in der Hausverwaltung

| Szenario | Risikostufe | Meldung an Behörde | Meldung an Betroffene |
|---|---|---|---|
| Falscher Excel-Anhang (Eigentümerliste) an gesamte WEG | Hoch | Ja | Ja (alle Betroffenen) |
| Gestohlener Verwalter-Laptop (ohne Verschlüsselung) | Sehr hoch | Ja | Ja |
| Gestohlener Laptop mit BitLocker-Verschlüsselung | Niedrig | Nein (intern dokumentieren) | Nein |
| Ransomware-Befall Server | Sehr hoch | Ja | Ja, wenn Daten exfiltriert |
| Fehlgeleitete Mahnung (falsche Adresse) | Mittel | Prüfen | Ggf. |
| Vergessene Schwärzung im öffentlichen Protokollentwurf | Mittel | Prüfen | Ggf. |
| Zugang Dritter zu Hausverwaltungsportal durch schwaches Passwort | Hoch | Ja | Ja |

## Risikobewertung (Art. 33 Abs. 1)

Meldepflicht an Behörde besteht, wenn die Verletzung **voraussichtlich ein Risiko für Rechte und Freiheiten** natürlicher Personen zur Folge hat. Bewertungsfaktoren: Art der Daten (Bankdaten, Gesundheitsdaten = höheres Risiko), Anzahl Betroffener, Identifizierbarkeit, Folgeschäden (Identitätsdiebstahl, Diskriminierung). Betroffenenbenachrichtigung nach Art. 34 nur bei **hohem Risiko**. Dokumentationspflicht gilt für alle Vorfälle, auch nicht meldepflichtige (Art. 33 Abs. 5 DSGVO).

Normen: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32016R0679

## 72-Stunden-Frist

„Kenntnis" beginnt, wenn der Verwalter oder ein Mitarbeiter (auch Praktikant, IT-Dienstleister) den Vorfall erstmals wahrnimmt — nicht erst nach interner Aufklärung. Vorab-Meldung mit unvollständigen Angaben ist zulässig und besser als Fristversäumnis; fehlende Angaben sind mit Begründung nachzureichen (Art. 33 Abs. 4). Zuständige Behörde nach Sitz des Verwalters: LDI NRW (nrw), BayLDA (Bayern), BlnBDI (Berlin), LfDI BW (Baden-Württemberg), HmbBfDI (Hamburg). Meldung online über Behörden-Portale.

## Sofortmaßnahmen (Reihenfolge)

1. Schadensquelle identifizieren und eindämmen (Laptop sperren, Server vom Netz, Account deaktivieren).
2. Backup-Stand prüfen, Integrität sichern, keine Überschreibung.
3. Passwort-Reset aller betroffenen Konten.
4. Strafanzeige bei Behörden bei Diebstahl oder Cyberangriff (Ransomware = § 303b StGB, Datendiebstahl = § 202a StGB).
5. Risikobewertung dokumentieren, 72-h-Uhr läuft.
6. Vorab-Meldung an Aufsichtsbehörde.
7. Betroffene benachrichtigen (bei hohem Risiko).
8. Vollständige Dokumentation im internen Vorfalls-Logbuch (Art. 33 Abs. 5).

Norm § 303b StGB: https://www.gesetze-im-internet.de/stgb/__303b.html

## Cross-Refs

- TOM-Mindeststandards (Prävention) → `datenschutz-vvt-tom-avv-hausverwaltung`
- Betroffenenrechte nach Vorfall → `datenschutz-betroffenenrechte-auskunft-loeschung-weg`
- Eskalation Anwalt / Strafanzeige → `eskalation-anwalt-amtsgericht`
- Verwalterpflichten und Haftung → `verwalterpflichten-26-27-weg`

## Quellenpflicht

`rechtsstand-mai-2026-faktenbank` laden. Art. 33 und 34 DSGVO über https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32016R0679 und aktuelle Melde-Formulare der Landesaufsichtsbehörden live abrufen — Portaladressen und Formularversionen ändern sich.
