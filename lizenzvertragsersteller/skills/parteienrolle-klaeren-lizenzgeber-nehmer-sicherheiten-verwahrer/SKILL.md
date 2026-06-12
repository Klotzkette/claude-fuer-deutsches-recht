---
name: parteienrolle-klaeren-lizenzgeber-nehmer-sicherheiten-verwahrer
description: "Rollenmatrix fuer Lizenzvertraege: Lizenzgeber, Lizenznehmer, Sicherheitengeber, Sicherheitennehmer, Verwahrer (Source-Code-Escrow), Konzernlizenzen, Cross-License. Mit Klärungs-Checkliste pro Rolle."
---

# Parteienrollen klären

## Standardrollen

| Rolle | Funktion | Typische Klausel |
| --- | --- | --- |
| Lizenzgeber (Licensor) | inhabt das IP, gewaehrt Nutzungsrechte | Lizenzgegenstand, Garantie Inhaberschaft, Verteidigungspflicht |
| Lizenznehmer (Licensee) | nutzt das IP gegen Vergütung | Vergütung, Nutzungsumfang, Verbesserungsrechte |
| Sicherheitengeber | Lizenzgeber, der das IP zur Sicherheit verpfaendet/abtritt | Sicherungslizenz, Aufschiebende Bedingungen |
| Sicherheitennehmer | Bank/Investor, der das IP als Sicherheit haelt | Realisierungsrechte, Verwertungs-Mandat |
| Verwahrer (Escrow Agent) | hinterlegt Source Code / IP-Dokumentation | Hinterlegungsbedingungen, Release-Trigger |
| Cross-Licensor | beidseitige Lizenzgewaehrung (Patentpool, Forschungspartnerschaft) | Gegenseitige Lizenz, Schiedsklausel |
| Konzernlizenznehmer | Lizenz auch für Konzernunternehmen | Definition $ 15 AktG / $ 17 AktG, Schutzkette |

## Klärungs-Checkliste

### Lizenzgeber

- Wirklich Inhaber? (Schutzrechtsregister, Originaltitel)
- Mitinhaber? (Patentgemeinschaft $ 6 PatG, $ 8 UrhG)
- Vorbelastungen? (frueheren Lizenzen)
- Konzernrechtlich: Tochtergesellschaft als Inhaber (typisch bei IP-Holding)

### Lizenznehmer

- Wer nutzt operativ? (Stamm-AG oder Tochter?)
- Soll Konzernunternehmen als Lizenznehmer mitgelten?
- Insolvenzrisiko Lizenznehmer? (Quellensteuer-Geheimnis, AGB-Schwaeche)

### Sicherheiten-Konstellation

- Sicherungslizenz: aufschiebend bedingt + Verwertungsrecht
- Pfandrecht: Bestellung notariell? $$ 1273 ff. BGB analog
- Rangverhaeltnis bei mehreren Sicherheitennehmern

### Escrow / Verwahrer

- Wer ist Hinterlegungsstelle? (Speziallabore, Eschapac, Iron Mountain, NotarisBeglaubigung)
- Release-Trigger: Insolvenz Lizenzgeber, Vertragsverletzung, Verletzung Wartungspflicht
- Aktualisierungspflicht: wie oft wird das Repository hinterlegt?
- Kosten und Streitfall: wer traegt die Escrow-Kosten?

## Output: Rollenmatrix

| Rolle | Person/Gesellschaft | Anschrift | gesetzl. Vertreter | Vollmacht-/Notar |
| --- | --- | --- | --- | --- |
| Lizenzgeber | … | … | … | … |
| Lizenznehmer | … | … | … | … |
| Sicherheitennehmer | … | … | … | … |
| Verwahrer | … | … | … | … |

## Anschluss

- Visualisierung: `transaktionsstruktur-visualisieren-ascii`
- Insolvenzfestigkeit: `insolvenz-fortbestand-paragraf-103-inso-lizenz`
- Sicherheiten: `sicherungslizenz-pfandrecht-an-immaterialguetern`
- Escrow: `escrow-quellcode-verwahrer-vereinbarung`
