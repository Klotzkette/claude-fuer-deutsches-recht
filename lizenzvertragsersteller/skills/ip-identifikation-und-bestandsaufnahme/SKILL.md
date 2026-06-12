---
name: ip-identifikation-und-bestandsaufnahme
description: "IP-Identifikation und Bestandsaufnahme fuer Lizenzvertraege: Schutzrechtsregister-Auszug, Klassifikation nach Typ (Urheber Patent Marke Design Gebrauchsmuster Geschäftsgeheimnis), Belastungen, Erfindervergutung, Lizenzhistorie, IP-Inventar als Anlage A."
---

# IP-Identifikation und Bestandsaufnahme

## Zweck

Ohne saubere IP-Identifikation kein guter Lizenzvertrag. Dieser Skill liefert die IP-Inventur für die Anlage A des Vertrags.

## IP-Typen — pro Typ ein Register

| IP-Typ | Register / Quelle | Prüfen |
| --- | --- | --- |
| Urheberrecht (klassische Werke) | nicht registriert; Werk-Nachweis | Schoepfungsdatum, Werkkategorie, Schoepfer/Miturheber, ggf. Verwertungsgesellschaft |
| Software | nicht registriert; Repository-Historie | Repository-Standort (GitHub etc.), Mitarbeiter-Code-Anteile $ 69b UrhG, Open-Source-Komponenten |
| Patent | DPMA (deutsch), EPA (europaeisch), USPTO/WIPO | Anmeldedatum, Erteilungsdatum, Schutzdauer, Erfinder, Gemeinschaft, Arbeitnehmererfindergesetz |
| Marke | DPMA, EUIPO, WIPO | Reg.-Nr., Wort/Bild, Klassen, Schutzgebiete, Verlaengerung, Benutzungspflicht |
| Geschmacksmuster (Design) | DPMA, EUIPO | Reg.-Nr., Anmeldedatum, Schutzdauer (max 25 J.) |
| Gebrauchsmuster | DPMA | Reg.-Nr., Anmeldedatum, Schutzdauer 10 J., kein Prüfverfahren |
| Geschäftsgeheimnis/Know-how | nicht registriert; Schutzmassnahmen | Schutzmassnahmen nach $ 2 GeschGehG (NDAs, Zugriffsbeschraenkung, Branch-Protection) |
| Domains | Whois / united-domains | Inhaber, Provider, Verlaengerung |

## Inventar-Schema (Anlage A des Vertrags)

```
| Asset-Nr. | Bezeichnung | IP-Typ | Reg.-Nr. | Schutzgebiet | Anmelder/Inhaber | Klassen | Status | Belastungen |
```

Pro Zeile: ein Schutzrecht. Belastungen = Lizenzen Dritter, Pfandrechte, Sicherungsabtretungen, Veroeffentlichungen die Patentschutz gefaehrden.

## Prüfroutine

1. **Bestand:** Sind alle Schutzrechte tatsaechlich auf den Lizenzgeber registriert?
2. **Lebensdauer:** Restschutzdauer, Verlaengerungspflichten, Gebuehren faellig?
3. **Belastungen:** Lizenzen Dritter, Verpfaendungen, Sicherungsabtretungen?
4. **Erfindervergutung:** Bei Patenten - Arbeitnehmererfindergesetz $ 9 ArbnErfG; Vergütung an Erfinder schon abgeloest?
5. **Drittstaaten:** Schutz in den Lizenzgebieten wirklich vorhanden? (insb. US/CN/JP)
6. **Mitinhaber:** Bei Miturheberschaft oder Patentgemeinschaft: alle erfasst?
7. **OSS-Compliance:** Bei Software - Open-Source-Komponenten erfasst, Lizenzkompatibilitaet $ 69c UrhG?

## Hinweis bei Software

- $ 69a UrhG schuetzt Computerprogramme als Werke.
- $ 69b UrhG: Arbeitsergebnis des AN gehoert kraft Gesetzes dem AG (ausschliessliche Nutzungsrechte).
- Prüfen: Welche Repositories? Welche Branches? Wer ist Owner? Welche Open-Source-Lizenzen sind im Stack?

## Anschluss

- Pro IP-Typ vertiefen: `lizenz-urheberrecht-und-software-urhg`, `lizenz-patent-patg`, `lizenz-marke-markeng`, `lizenz-geschmacksmuster-design-designg`, `lizenz-gebrauchsmuster-gebrmg`, `lizenz-geschaeftsgeheimnis-knowhow-geschgehg`.
