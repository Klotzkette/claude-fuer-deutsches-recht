---
name: hochrisiko-zuordnung-art-6-und-anhang-i-iii
description: "Gesamtuebersicht zur Hochrisiko-Zuordnung nach Art. 6 KI-VO: Art. 6 Abs. 1 Sicherheitsbauteil/Anhang I und Art. 6 Abs. 2/Anhang III. Erklaert Zweckbestimmung, allgemeine Chatbots/GPAI, Mitarbeitenden-Fehlgebrauch, Rueckausnahme Art. 6 Abs. 3 und Pflichtenfolge. Output: Hochrisiko-Landkarte mit Routing zu Detail-Skills."
---

# Hochrisiko-Zuordnung — Art. 6 KI-VO und Anhang I/III

## Zweck

Dieser Skill gibt die Gesamtübersicht zur Hochrisiko-Einstufung. Er entscheidet nicht endgültig, sondern leitet in die passenden Detailprüfungen.

## Zwei Hochrisiko-Pfade

### Pfad 1 — Art. 6 Abs. 1

Ein KI-System ist Hochrisiko, wenn:
1. es Sicherheitsbauteil eines Produkts ist oder selbst ein Produkt, das unter Anhang-I-Sektorrecht fällt, und
2. dieses Produkt oder Sicherheitsbauteil einer Dritt-Konformitätsbewertung unterliegt.

Detail: `hochrisiko-art-6-abs-1-sicherheitsbauteil`

### Pfad 2 — Art. 6 Abs. 2 i.V.m. Anhang III

Ein KI-System ist Hochrisiko, wenn es für einen in Anhang III genannten Zweck bestimmt ist oder entsprechend eingesetzt wird.

Die acht Bereiche:
1. Biometrie
2. Kritische Infrastruktur
3. Bildung und berufliche Ausbildung
4. Beschäftigung, Arbeitnehmermanagement und Zugang zur Selbständigkeit
5. Zugang zu wesentlichen privaten und öffentlichen Diensten und Leistungen
6. Strafverfolgung
7. Migration, Asyl und Grenzkontrolle
8. Rechtspflege und demokratische Prozesse

Detail: `hochrisiko-art-6-abs-2-anhang-iii`

## Zweckbestimmung statt Tool-Label

Ein allgemeiner Chatbot oder ein GPAI-System ist nicht automatisch Hochrisiko. Entscheidend ist:
- Wofür wird es vom Anbieter bestimmt?
- Wofür nimmt der Betreiber es in Betrieb?
- Welche Nutzung ist organisatorisch erlaubt, geduldet oder technisch nahegelegt?
- Werden natürliche Personen bewertet, gerankt, priorisiert oder in Rechten/Chancen betroffen?

Wenn Mitarbeitende ein allgemeines Tool entgegen klarer Regeln missbrauchen, ist das zunächst ein Governance- und Incident-Thema. Wenn die Nutzung aber systematisch ist, geduldet wird oder der Betreiber sie in Prozesse einbaut, kann die Hochrisiko-Prüfung neu kippen.

## Rückausnahme Art. 6 Abs. 3

Auch bei Anhang-III-Treffer ist die Rückausnahme zu prüfen:
- kein erhebliches Risiko für Gesundheit, Sicherheit oder Grundrechte
- eine der vier Fallgruppen
- keine Profiling-Sperre
- Dokumentation nach Art. 6 Abs. 4

Detail: `rueckausnahme-art-6-abs-3`

## Pflichtenfolge

Bei bestätigtem Hochrisiko:
- Anbieter: Art. 9 bis 15, Art. 17, Art. 43 bis 49, Registrierung, Marktbeobachtung
- Betreiber: Art. 26, ggf. Art. 27, bestimmungsgemäße Verwendung, menschliche Aufsicht, Logging, Informationspflichten
- Zweckänderung: Art. 25 Anbieterwerden prüfen

## Output-Template — Hochrisiko-Landkarte

```text
HOCHRISIKO-LANDKARTE ART. 6 KI-VO
System: [NAME]

Art. 6 Abs. 1: [ja/nein/unklar] — [Grund]
Art. 6 Abs. 2/Anhang III: [ja/nein/unklar] — [Bereich/Zweck]
Allgemeiner Chatbot/GPAI: [ja/nein] — [warum nicht automatisch / warum konkret relevant]
Mitarbeitenden-Fehlgebrauch: [kein Thema / vorhersehbar / geduldet / systematisch]
Art. 6 Abs. 3: [prüfen / fernliegend / greift wahrscheinlich]
Nächste Skills: [...]
```

## Quellen- und Aktualitätshinweis

Stand: 05/2026. Maßgeblich sind Art. 3 Nr. 12/13/23, Art. 6 und Anhang I/III KI-VO. Keine Rechtsberatung.
