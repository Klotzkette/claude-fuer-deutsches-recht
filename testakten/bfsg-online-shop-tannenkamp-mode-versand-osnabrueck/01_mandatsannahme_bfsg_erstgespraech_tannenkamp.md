# Aktenstück 01 — Mandatsannahme und BFSG-Erstgespräch Tannenkamp Mode-Versand

**Kanzlei:** Dr. Annerose Friedrichs — Rechtsanwältin für IT-Recht und Verbraucherschutz, Hannover
**Mandantin:** Tannenkamp Mode-Versand GmbH, Osnabrück
**Gesprächsdatum:** 17.03.2026
**Teilnehmer:** RA Dr. Annerose Friedrichs; Gerd Tannenkamp (Geschäftsführer); Marion Hüsing (kaufm. Leiterin)
**Aktenzeichen intern:** AF-IT-2026/0094
**Extern:** MüNI-BFSG-2026/0188 (Marktüberwachung); LG Hannover 18 OH 8/26 (VZ NRW)

---

## 1. Sachverhaltsaufnahme

Mandantin betreibt unter der Domain tannenkamp-mode.de einen Online-Shop für Damen- und Herrenbekleidung sowie Accessoires. Der Shop ist seit 2018 in Betrieb und wurde zuletzt 2022 auf das Shopify-Theme „Lavanda Pro" der Lavendelhaus Design GbR, Münster, umgestellt. Jahresumsatz 2025: ca. 18 Mio. EUR. Mitarbeiteranzahl: ca. 140, davon 12 im Bereich E-Commerce/IT.

Mit Schreiben vom 12.03.2026 hat die Verbraucherzentrale NRW (VZ NRW) eine förmliche Verstoßmeldung nach § 33 BFSG zugestellt und parallel eine Verbandsklage gemäß Verbandsklagerichtlinie (VRUG, Umsetzung RL EU 2020/1828) beim LG Hannover eingereicht (Az. 18 OH 8/26). Die Marktüberwachungsbehörde Niedersachsen (Landesamt für Verbraucherschutz und Lebensmittelsicherheit, intern bezeichnet als „MüNI") hat daraufhin am 15.03.2026 ein Verfahren nach § 30 BFSG eingeleitet (Az. MüNI-BFSG-2026/0188).

Bemängelt werden:

1. Fehlende Tastatur-Navigation (kein fokussiertes Steuerelement sichtbar bei Tab-Steuerung)
2. Fehlende Alt-Texte bei Produktbildern (ca. 2.300 Bilder betroffen)
3. Kontrastverhältnis Fließtext auf Shop-Hintergrund: 2,8:1 (WCAG 2.1 AA verlangt 4,5:1)
4. Kein Skip-Link zum Hauptinhalt
5. Fehlerhafte ARIA-Roles (role="button" auf `<div>`-Elementen ohne Tastaturhandler)
6. PDF-Produktkataloge Herbst/Winter 2024 und Frühjahr/Sommer 2025 nicht barrierefrei

---

## 2. Erste rechtliche Einordnung

Das BFSG ist am 28.06.2025 vollständig in Kraft getreten und setzt die Europäische Barrierefreiheitsrichtlinie EAA (RL EU 2019/882) um. Es verpflichtet Wirtschaftsakteure, die Produkte in Verkehr bringen oder Dienstleistungen erbringen, zur Einhaltung der Barrierefreiheitsanforderungen nach Anhang I der Richtlinie, konkretisiert in der BFSG-DV sowie in der harmonisierten Norm EN 301 549.

Tannenkamp Mode-Versand GmbH ist als E-Commerce-Dienst ein „Dienstleistungserbringer" im Sinne von § 1 Abs. 2 BFSG i.V.m. § 2 Nr. 17 BFSG. Umsatz und Mitarbeiterzahl überschreiten die KMU-Schwellenwerte des § 5 BFSG (< 10 MA und < 2 Mio. EUR Jahresumsatz) erheblich. Eine KMU-Ausnahme greift nicht.

Kritische Frage: Ob für den vor dem 28.06.2025 betriebenen Shop eine Übergangsregelung nach § 38 BFSG (Altdienstleistungen) greift. Dies ist unter Aktenzeichen 04 vertieft darzustellen.

---

## 3. Mandatsumfang

Dr. Friedrichs übernimmt das Mandat mit folgendem Leistungsumfang:

- Vertretung gegenüber MüNI im Verfahren Az. MüNI-BFSG-2026/0188
- Stellungnahme zur Anhörung (Frist 06.04.2026)
- Klageerwiderung LG Hannover 18 OH 8/26
- Regresskorrespondenz gegenüber Lavendelhaus Design GbR
- Beratung zur BFSG-Compliance-Roadmap
- Koordination mit IT-Dienstleister (Shopify-Experte) für Sanierung

Mandatsannahme erklärt. Vergütungsvereinbarung gemäß RVG sowie individuell vereinbarter Stundensatz (260 EUR netto) für über RVG hinausgehende Beratungsleistungen.

---

## 4. Sofortmaßnahmen (bis 25.03.2026)

| Nr. | Maßnahme | Verantwortlich | Frist |
|---|---|---|---|
| 1 | Vollständigen WCAG-Audit (automatisiert + manuell) in Auftrag geben | Tannenkamp IT | 20.03.2026 |
| 2 | Shopify-Zugangsdaten und Theme-Vertrag mit Lavendelhaus Design sicherstellen | Hüsing | 19.03.2026 |
| 3 | Sämtliche PDF-Produktkataloge mit Erstellungsdatum dokumentieren | Hüsing | 19.03.2026 |
| 4 | Entwurf Stellungnahme an MüNI vorbereiten | Dr. Friedrichs | 01.04.2026 |
| 5 | Kontraständerung (Notfall-CSS) prüfen lassen | IT-Leiter Wörmann | 22.03.2026 |

---

## 5. Aktenführung

Vollmacht liegt unterschrieben vor. Handelsregistereintrag HRB 20847 AG Osnabrück bestätigt Vertretungsbefugnis Gerd Tannenkamp (alleinvertretungsberechtigter GF).

Nächste Besprechung: 01.04.2026 (Vorbereitung Stellungnahme MüNI).

---

*Bearb.: Dr. A. Friedrichs — 17.03.2026*
