---
name: tia-us-fisa-702-und-eo-12333-bewertung
description: "Bewertung der US-Ueberwachungsgrundlagen FISA Section 702 und Executive Order 12333 für das TIA. Sachstand der EuGH-Kritik aus Schrems II, Reform durch EO 14086 (DPF-Grundlage), Folgen für Cloud-Provider, electronic communication service provider Status. Mit Prüfraster und Texten für Schritt 3 E..."
---

# US-Ueberwachungsgrundlagen FISA 702 und EO 12333 für das TIA

## Wann dieses Modul hilft

- TIA für US-Cloud-/SaaS-Anbieter.
- Diskussion mit Anbieter, ob er als ECSP gilt.
- Bewertung des Schutzniveaus jenseits des DPF (SCC-Faelle).
- Prüfung des Restrisikos trotz DPF-Zertifizierung.
- Schulung Compliance-Team.

## Rechtlicher Rahmen

### FISA Section 702

- 50 U.S.C. § 1881a, neu autorisiert durch verschiedene Reauthorization Acts; aktuelle Reauthorization 2024.
- Erlaubt zielgerichtete Erfassung der Kommunikation von Non-US-Personen, die sich vermutlich ausserhalb der USA befinden, mit dem Ziel der Auslandsaufklaerung.
- Zuverfuegung-Pflicht: betrifft electronic communication service provider (ECSP) im weiten Sinn (Cloud, SaaS, IaaS, Telco, Messaging, E-Mail).
- Keine individuelle gerichtliche Prüfung der einzelnen Selektoren; jaehrliche Programm-Zertifizierung durch FISA Court (FISC).

### Executive Order 12333

- Vom 04.12.1981, Praesident Reagan; mehrfach modifiziert.
- Grundlage für SIGINT, einschliesslich Erfassung von Daten in Transit ausserhalb der USA.
- Kein gerichtlicher Vorbehalt; Aufsicht über DNI/PCLOB beschraenkt.

### Executive Order 14086 vom 07.10.2022

- "Enhancing Safeguards for United States Signals Intelligence Activities".
- Fuehrt Standards "necessary" und "proportionate" ein.
- Etabliert zweistufigen Redress-Mechanismus: Civil Liberties Protection Officer (CLPO) und Data Protection Review Court (DPRC).
- Grundlage des EU-US DPF Angemessenheitsbeschlusses 2023/1795.

### EuGH Schrems II – tragende Beanstandungen

- FISA 702: keine ausreichende Verhältnismäßigkeitskontrolle, keine effektive Rechtsschutzmoeglichkeit für Betroffene aus der EU.
- EO 12333: bulk collection ohne Anlassbezug, kein Rechtsschutz.

### Bewertung post EO 14086

- Verbesserung des Rechtsschutzes durch DPRC, aber Diskussion über Unabhaengigkeit dauert an.
- Standards "necessary" und "proportionate" als US-interne Selbstbindung.
- DPF ist gueltig; eigenstaendige Klage Schrems III anhaengig (NOYB).

## Ablauf / Checkliste

1. **ECSP-Status:** Ist der Importeur ECSP iSd 50 U.S.C. § 1881(b)(4)? Faustregel: Cloud, SaaS, IaaS, E-Mail, Messaging, Telco -> Ja; reine On-Premises-Lizenz -> regelmaessig nein.
2. **EO 12333-Exposition:** Daten in Transit über US-Carrier? Glasfaserkabel? Mitbenutzung von Backbone-Infrastruktur?
3. **Transparenzbericht:** Veroeffentlicht der Importeur Zahlen zu FISA-/NSL-Anfragen?
4. **Reaktionsmoeglichkeit:** Hat der Importeur die Befugnis und Praxis, FISA-Anfragen anzufechten?
5. **EDPB-EEG-Prüfung** durchfuehren (Garantien A bis D der Empfehlung 02/2020).
6. **DPF-Prüfung:** Ist der Importeur aktiv im DPF gelistet für die konkrete Datenart (HR/Non-HR)?
7. **Restrisiko:** Auch bei DPF-Listing besteht ein Restrisiko aus FISA 702 / EO 12333; technische Maßnahmen erwaegen.
8. **Dokumentation** im TIA-Schritt 3.

## Mustertext / Template

Baustein TIA-Schritt 3 (US):

> Der Importeur ist als "electronic communication service provider" im Sinne des 50 U.S.C. § 1881(b)(4) qualifiziert (Cloud-/SaaS-Anbieter). Damit greift FISA Section 702 grundsätzlich auf seine Verarbeitungstaetigkeiten zu. Daneben besteht die Moeglichkeit der Erfassung von Daten in Transit nach Executive Order 12333.
>
> Mit Executive Order 14086 vom 07.10.2022 wurden Verhältnismäßigkeitsmassstaebe ("necessary" und "proportionate") sowie der zweistufige Rechtsschutzmechanismus (CLPO/DPRC) eingefuehrt. Der EU-US Data Privacy Framework gemäß Durchfuehrungsbeschluss (EU) 2023/1795 stuetzt sich auf diese Reformen.
>
> Im konkreten Fall ist der Importeur unter dem Namen "..." mit Listing-Datum [...] aktiv im DPF gelistet; das Listing deckt [HR-/Non-HR-]Daten ab. Soweit über das DPF hinausgehend SCCs zur Anwendung kommen (z. B. Konzernuebermittlungen ausserhalb des Listings), wird eine kumulative Prüfung vorgenommen.
>
> Die EDPB-EEG-Garantien werden wie folgt bewertet:
> - Garantie A (Klarheit der Regeln): [...]
> - Garantie B (Notwendigkeit und Verhältnismäßigkeit): [...]
> - Garantie C (unabhaengige Aufsicht): [...]
> - Garantie D (effektiver Rechtsschutz): [...]
>
> Verbleibendes Restrisiko: [...]. Ergaenzende Schutzmassnahmen siehe Schritt 4.

## Typische Fehler

- "Importeur ist nicht ECSP" pauschal angenommen, ohne die weite Definition zu prüfen.
- DPF-Listing als endgueltige Loesung betrachtet; FISA/EO 12333-Restrisiko ignoriert.
- EO 12333 vergessen, weil "wir sind ja im DPF".
- Annahme, dass Anbieter Anfragen anficht – ohne Beleg.
- Quellenangaben aus Modellwissen statt Verifikation an offiziellen Texten.
- Annahme, Schrems II sei "ueberholt" durch DPF – TIA für SCC-Faelle bleibt zwingend.

## Quellen Stand 06/2026

- EuGH C-311/18 vom 16.07.2020 (Schrems II), insb. Rn. 168 ff.
- 50 U.S.C. § 1881a (FISA Section 702); FISA Reauthorization Act 2024.
- Executive Order 12333 vom 04.12.1981.
- Executive Order 14086 vom 07.10.2022.
- Durchfuehrungsbeschluss (EU) 2023/1795 vom 10.07.2023 (EU-US DPF).
- EDPB Empfehlung 02/2020 vom 10.11.2020 (EEG).
- EDPB Information Note 1/2024 on EU-US DPF redress mechanism (Verifikation am Originaldokument).
- PCLOB-Berichte (Privacy and Civil Liberties Oversight Board) zu Section 702.
