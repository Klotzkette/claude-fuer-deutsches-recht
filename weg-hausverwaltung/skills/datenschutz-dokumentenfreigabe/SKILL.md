---
name: datenschutz-dokumentenfreigabe
description: "Prüft Datenschutz und Dokumentenfreigaben in der Hausverwaltung (Stand 05/2026): Eigentümerlisten, Belegeinsicht, Handwerkerdaten, Mieterbeschwerden, Cloud-Ordner, Schwärzungen und Versandkreis. Schnittstelle zum Datenschutzrecht-Plugin bei hohem Risiko; Belegeinsicht nach § 18 Abs. 4 WEG (Verwaltungsunterlagen); § 28 Abs. 4 WEG nur für den Vermögensbericht."
---

# Datenschutz und Dokumentenfreigabe

Stand: 05/2026.

## Ziel

Transparenz in der GdWE ermöglichen, ohne personenbezogene Daten unnötig breit zu streuen. Maßstab: DSGVO (Erforderlichkeit, Zweckbindung, Datenminimierung), berechtigte Interessen der GdWE und einzelner Eigentümer.

## Prüfpunkte

- **Wer braucht welches Dokument wofür?** (Eigentümer, Beirat, Verwalter, Anwalt, Handwerker, Mieter)
- **Welche Daten?** Eigentümerdaten (Name, Adresse, Anteil), Mieterdaten, Kontodaten, Gesundheitsdaten, Beschwerdedaten, Strafdaten.
- **Schwärzung / Auszug / Einsicht** statt breitem Versand.
- **Cloud-Freigaben**: Linkablaufzeit, Berechtigungen, Protokoll, AVV mit Anbieter (Art. 28 DSGVO).
- **Schnittstelle Datenschutzrecht-Plugin** bei hohem Risiko (z. B. Datenpanne, sensible Daten, größere Eigentümerzahl betroffen).

## Typische Konstellationen

| Anliegen | Empfehlung |
| --- | --- |
| Eigentümerliste an alle versenden | nur Name + Einheit + Anteil bei berechtigtem Interesse; Telefon/E-Mail nur mit Einwilligung |
| Belegeinsicht Jahresabrechnung | Vor Ort oder über sicheres Portal; sensible Belege (Krankheits-/Gesundheitsdaten) schwärzen |
| Mieterbeschwerde an WEG-Verwalter | mit Eigentümer kommunizieren; Klartext-Daten der Mieter nur, soweit erforderlich |
| Handwerker erhält Eigentümerliste | regelmäßig **nicht**; nur Kontakt der WEG-Verwaltung oder benannte Ansprechpartner |
| Kameraüberwachung Eingang | Beschluss erforderlich; Beschilderung Art. 13 DSGVO; Speicherzeit minimieren; Schutzraum Anwohner |
| Versand via Messenger / private E-Mail | vermeiden; Verwalter-Mail / Portal nutzen |

## Belegeinsicht / Vermögensbericht

- **§ 18 Abs. 4 WEG**: Anspruch jedes Wohnungseigentümers auf Einsicht in die Verwaltungsunterlagen — das ist die Rechtsgrundlage für die Belegeinsicht (Rechnungen, Verträge, Kontoauszüge, Abrechnungsunterlagen). Anspruch besteht gegen die GdWE, in der Praxis erfüllt durch den Verwalter (https://www.gesetze-im-internet.de/woeigg/__18.html).
- **§ 28 Abs. 4 WEG**: Anspruch auf Vorlage des Vermögensberichts (Aufstellung des Gemeinschaftsvermögens, Erhaltungsrücklage, Forderungen/Verbindlichkeiten) — nicht die Anspruchsgrundlage für die Belegeinsicht, sondern eigene Informationspflicht (https://www.gesetze-im-internet.de/woeigg/__28.html).
- Praxis: Belegeinsicht auf Verlangen, Ort und Zeit billigerweise festlegen, kein Verbot der Anfertigung von Kopien/Fotos, soweit nicht durch Datenschutz Dritter (z. B. Mieter-Belege, Gehaltsabrechnungen Hauspersonal) eingeschränkt.
- Empfehlenswert: kontrollierter Einsichtstermin oder geschütztes Portal mit Audit-Log.

## Mustertext Freigabeentscheidung

> **Freigabevermerk**
> Dokument: [Bezeichnung, Stand]
> Empfänger: [Liste mit Rolle]
> Rechtsgrundlage: [berechtigtes Interesse / Einwilligung / Vertragserfüllung / gesetzliche Pflicht]
> Datenminimierung: [Schwärzungen vorgenommen / Auszug erstellt / vollständig erforderlich]
> Übermittlungsweg: [Portal / E-Mail verschlüsselt / Postversand / Vor-Ort-Einsicht]
> Speicherdauer / Linkablauf: [...]
> Risikoeinschätzung: [niedrig / mittel / hoch]; bei hoch → Eskalation an Datenschutzrecht-Plugin

## Datenpanne (Art. 33 DSGVO)

- Bewertung binnen Stunden, Risikoeinschätzung für Betroffene.
- Meldung an Aufsichtsbehörde binnen 72h, soweit Risiko für Rechte und Freiheiten.
- Information der Betroffenen, wenn hohes Risiko.
- Vorgang dokumentieren (Datum, Vorfall, Maßnahmen, Beteiligte).

## Output

- Freigabeentscheidung (mit Risikoeinstufung)
- Schwärzungsliste
- Eigentümerantwort (Begründung Ablehnung / Umfang Einsicht)
- Datenschutz-Eskalationsnotiz

## Cross-Refs

- Vermögensbericht / Belegeinsicht → `wirtschaftsplan-jahresabrechnung-28-weg`
- Beschwerde / Kamera → `stoerung-hausordnung-mieter-eigentuemer`, `eigentuemerkommunikation-beschwerde`
- Eskalation Anwalt / Aufsicht → `eskalation-anwalt-amtsgericht`, Datenschutzrecht-Plugin

## Quellenpflicht

`rechtsstand-mai-2026-faktenbank` laden. § 18 Abs. 4 WEG: https://www.gesetze-im-internet.de/woeigg/__18.html ; § 28 Abs. 4 WEG: https://www.gesetze-im-internet.de/woeigg/__28.html ; DSGVO siehe Datenschutzrecht-Plugin.
