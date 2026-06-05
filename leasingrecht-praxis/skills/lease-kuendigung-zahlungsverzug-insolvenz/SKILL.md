---
name: lease-kuendigung-zahlungsverzug-insolvenz
description: "Lease Kuendigung Zahlungsverzug Insolvenz: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Lease Kuendigung Zahlungsverzug Insolvenz

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Lease Kuendigung Zahlungsverzug Insolvenz** im Plugin Leasingrecht Praxis. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `lease-016-kuendigung-zahlungsverzug-rueckholung-und-verwertung` | Kündigung des Leasingvertrags: Zahlungsverzug, außerordentliche Kündigung, Rückholung, Verwertung und Schadensersatzberechnung. |
| `lease-017-insolvenz-leasingnehmer-aussonderung-fortfuehrung` | Insolvenz des Leasingnehmers: §§ 108 und 109 InsO, Aussonderungsrecht, Wahlrecht des Insolvenzverwalters, offene Forderungen, Sanierungsoptionen. |
| `lease-018-insolvenz-leasinggeber-eigentum-und-refinanzierung` | Insolvenz des Leasinggebers: Nutzungsrecht des LN, Refinanzierungsstruktur, Sicherungsübereignung, § 108 InsO und Ansprüche des Refinanzierers. |

## Arbeitsweg

Im Plugin Leasingrecht Praxis gilt für **Lease Kuendigung Zahlungsverzug Insolvenz**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `lease-016-kuendigung-zahlungsverzug-rueckholung-und-verwertung`

**Fokus:** Kündigung des Leasingvertrags: Zahlungsverzug, außerordentliche Kündigung, Rückholung, Verwertung und Schadensersatzberechnung.

# Kündigung, Rückholung und Verwertung

## Zweck

Wenn der Leasingnehmer in Zahlungsverzug gerät, muss der Leasinggeber schnell handeln: Mahnung, Kündigung, Rückholung und Verwertung bilden eine Prozesskette mit engen Fristen. Dieser Skill führt durch alle Schritte und die Schadensersatzberechnung nach Kündigung.

## Voraussetzungen der außerordentlichen Kündigung

### Zahlungsverzug (§ 543 II Nr. 3 BGB analog)
Fristlose Kündigung bei:
- Verzug mit mindestens **zwei aufeinanderfolgenden Raten**
- Die rückständigen Raten betragen zusammen mindestens **einen Monatsbetrag** (bei Verbraucher)
- Bei B2B: Weniger strenge Anforderungen, aber Erheblichkeit erforderlich

### Abmahnungserfordernis
- Verbraucher: Abmahnung erforderlich (§ 543 III BGB analog)
- B2B: Abmahnung vertraglich vereinbart? Sonst nur erforderlich, wenn Treu und Glauben gebietet

### Form der Kündigung
- Keine gesetzliche Formvorschrift für Kündigung (mündlich möglich)
- Praxis: Schriftliche Kündigung empfohlen (Beweiszwecke)
- Textform (§ 126b BGB): E-Mail genügt

## Rückholung des Leasingobjekts

### Herausgabeanspruch
- Nach wirksamer Kündigung: LG hat Herausgabeanspruch aus § 985 BGB (Eigentum) und aus Leasingvertrag
- LN ist zur sofortigen Herausgabe verpflichtet

### Selbsthilfe (§ 229 BGB)
- LG darf Objekt nicht eigenmächtig wegnehmen (verbotene Eigenmacht, § 858 BGB)
- Ausnahme § 229 BGB: Selbsthilfe zur Sicherung eines gefährdeten Anspruchs
- Praxis: Gerichtlicher Herausgabetitel empfohlen, nicht Selbsthilfe

### Einstweilige Verfügung (§§ 935 ff. ZPO)
- Herausgabe im einstweiligen Rechtsschutz möglich
- Voraussetzung: Verfügungsanspruch (Herausgabe nach Kündigung) + Verfügungsgrund (Veräußerungsgefahr)
- Schnell vollziehbar: Gerichtsvollzieher vollstreckt unmittelbar

## Verwertung des Leasingobjekts

### Bestmögliche Verwertung
- LG ist zur bestmöglichen Verwertung verpflichtet (§ 254 BGB analog: Schadensminderungspflicht)
- Methoden: öffentliche Auktion, freihändiger Verkauf, Online-Plattformen
- LN hat Anspruch auf Auskunft über Verwertungserlös

### Verwertungserlös-Berechnung
- Verwertungserlös wird vom Schadensersatz abgezogen
- LN kann niedrigen Erlös anfechten, wenn LG nicht bestmöglich verwertet hat

## Schadensersatzberechnung nach Kündigung

### Grundformel
```
Schadensersatz = Ausstehende Raten (abgezinst) - Verwertungserlös - Ersparte Aufwendungen
```

### Abzinsungspflicht
- Ausstehende Raten müssen abgezinst werden (Zeitwert des Geldes)
- BGH, Urteil vom 14.03.2007 - VIII ZR 68/06: LG darf nicht den nominalen Summenwert der Raten fordern

### Ersparte Aufwendungen
- Verwaltungskosten für Weiterführung
- Restverzinsung auf Leasingforderung

### AGB-Klausel: Pauschalschadensersatz
- Zulässig als Schadenspauschalierung (§ 309 Nr. 5 BGB)
- Muss dem typischen Schaden entsprechen
- LN muss nachweisen können, dass tatsächlicher Schaden geringer ist

## Prüfprogramm

1. Zahlungsverzug: Wann, wie viele Raten, Betrag?
2. Abmahnung erteilt (bei Verbraucher zwingend)?
3. Kündigung: Schriftlich, fristlos, Begründung?
4. Herausgabe: Freiwillig oder Vollstreckung erforderlich?
5. Verwertung: Bestmöglich? Erlös dokumentiert?
6. Schadensersatz: Abzinsung, Verwertungserlös, ersparte Aufwendungen berücksichtigt?

## Typische Fallen

- Abmahnung unterlassen bei Verbraucher → Kündigung unwirksam
- Selbsthilfe-Rückholung → verbotene Eigenmacht (§ 858 BGB) → Schadensersatz an LN
- Verwertung zu niedrigem Erlös ohne Dokumentation → LN kann Abzug anfechten
- Schadensersatz ohne Abzinsungspflicht → BGH-widrig → reduzierter Anspruch

## Normen und Quellen

- § 543 BGB (Außerordentliche Kündigung): https://dejure.org/gesetze/BGB/543.html
- § 985 BGB (Herausgabeanspruch): https://dejure.org/gesetze/BGB/985.html
- § 229 BGB (Selbsthilfe): https://dejure.org/gesetze/BGB/229.html
- §§ 935 ff. ZPO: https://www.gesetze-im-internet.de/zpo/__935.html
- § 309 Nr. 5 BGB (Pauschale): https://dejure.org/gesetze/BGB/309.html
- BGH, Urteil vom 14.03.2007 - VIII ZR 68/06 (Schadensersatz nach Kündigung): https://www.bgh.de
- openjur.de Leasingkündigung: https://openjur.de

## Output-Formate

- **Mahnungs-Vorlage**: Zwei-Raten-Verzug mit Kündigungsankündigung
- **Kündigungsschreiben**: Fristlose Kündigung wegen Zahlungsverzug
- **Schadensersatz-Rechner**: Formel mit Abzinsung und Verwertungserlös
- **eV-Antrag-Muster**: Einstweilige Verfügung auf Herausgabe

## 2. `lease-017-insolvenz-leasingnehmer-aussonderung-fortfuehrung`

**Fokus:** Insolvenz des Leasingnehmers: §§ 108 und 109 InsO, Aussonderungsrecht, Wahlrecht des Insolvenzverwalters, offene Forderungen, Sanierungsoptionen.

# Insolvenz des Leasingnehmers: Aussonderung und Fortführung

## Zweck

Die Insolvenz des Leasingnehmers ist ein häufiges Praxisszenario. Der Leasinggeber muss sein Aussonderungsrecht sichern, gleichzeitig prüfen ob eine Fortführung wirtschaftlich sinnvoll ist. Dieser Skill analysiert §§ 108, 109 InsO, das Wahlrecht des Insolvenzverwalters und die Forderungsanmeldung.

## Rechtlicher Rahmen

- § 47 InsO: Aussonderung (LG als Eigentümer)
- § 108 InsO: Fortbestand bestimmter Verträge (Miet-/Leasingverträge)
- § 109 InsO: Wahlrecht des Insolvenzverwalters bei Verträgen
- §§ 38, 55 InsO: Insolvenzforderung vs. Masseverbindlichkeit
- § 21 II Nr. 5 InsO: Vorläufige Insolvenzverwaltung, Anordnung des Aussonderungsverbots

## § 108 InsO: Fortbestand des Leasingvertrags

### Grundsatz
Leasingverträge über unbewegliche Sachen (Immobilien) laufen gemäß § 108 I InsO grundsätzlich mit Wirkung für die Masse fort.

Bei **beweglichen Sachen** (Regelfall im Leasing): § 108 InsO gilt nicht direkt; § 103 InsO (Wahlrecht) gilt.

**BGH-Rspr.**: Finanzierungsleasing = Mietvertrag analog → § 108 InsO analog anwendbar nach überwiegender Ansicht, aber str.

### § 103 InsO: Wahlrecht des Insolvenzverwalters
- Verwalter kann Erfüllung wählen oder ablehnen
- Wahl der Erfüllung: Leasingvertrag läuft fort; Raten = Masseverbindlichkeit (§ 55 I Nr. 2 InsO)
- Ablehnung: LN (Masse) wird von Ratenpflicht frei; LG kann Objekt aussondern (§ 47 InsO)

## § 47 InsO: Aussonderungsrecht des Leasinggebers

LG bleibt zivilrechtlicher Eigentümer → Aussonderungsrecht: LG kann das Leasingobjekt aus der Insolvenzmas se herausverlangen.

Voraussetzungen:
- LG muss Eigentümer sein (nicht nur Sicherungsnehmer)
- Objekt muss noch identifizierbar zur Insolvenzmasse gehören (nicht verarbeitet, nicht gutgläubig erworben)

**Praxis**: LG stellt Aussonderungsantrag beim Insolvenzverwalter. Verwalter hat keine Wahl bei echtem Eigentum des LG – er muss herausgeben.

## Forderungsanmeldung

### Offene Raten vor Insolvenzeröffnung
- Sind **Insolvenzforderungen** (§ 38 InsO)
- Anmeldung beim Insolvenzverwalter erforderlich (§ 174 InsO)
- Quote: Typisch 5–30 % in Regelinsolvenz

### Raten nach Verfahrenseröffnung (wenn Verwalter fortführt)
- **Masseverbindlichkeiten** (§ 55 I Nr. 2 InsO)
- Volle Erfüllung aus der Insolvenzmasse vor anderen Gläubigern

### Schadensersatz nach Kündigung
- Wenn LG kündigt (wegen Zahlungsverzug vor Insolvenzeröffnung): Schadensersatz = Insolvenzforderung
- Wenn Verwalter ablehnt: Schadensersatz-Anspruch? Str.; h.M.: LG hat Anspruch als Insolvenzforderung

## Vorläufige Insolvenzverwaltung

- § 21 II Nr. 5 InsO: Anordnung eines Aussonderungsverbots
- Während Voröffnung: LG darf Objekt nicht herausverlangen
- Gegenleistung: Nutzungsentgelt aus Masse (§ 21 II Nr. 5 S. 2 InsO)

## Sanierungsoptionen

### Fortführung mit Insolvenzplan
- Insolvenzverwalter kann Leasingvertrag fortführen
- Leasingkonditionen können im Insolvenzplan angepasst werden (einvernehmlich mit LG)

### Übertragende Sanierung
- Sanierungsunternehmen übernimmt Betrieb → LG muss Zustimmung zur Vertragsübertragung geben (§ 415 BGB)
- Ohne Zustimmung: Vertragsübertragung unwirksam

## Prüfprogramm

1. Insolvenzantrag: Eröffnungsdatum feststellen
2. Eigentum des LG: Belege sichern (Kaufvertrag, Eigentumsnachweis)
3. § 103 InsO: Verwalter kontaktieren – Erfüllung oder Ablehnung?
4. Offene Raten: Forderungsanmeldung beim Insolvenzverwalter (§ 174 InsO)
5. Raten nach Eröffnung: Masseverbindlichkeit geltend machen (§ 55 InsO)
6. Aussonderungsantrag stellen; Voröffnungsverbot beachten (§ 21 II Nr. 5 InsO)

## Typische Fallen

- Forderungsanmeldung vergessen → Insolvenzforderung verloren
- LG tritt ohne Erlaubnis ins Objekt ein → verbotene Eigenmacht
- Raten als Masseverbindlichkeit eingeklagt, aber Verwalter hat Erfüllung abgelehnt → Schadensersatz nur als Insolvenzforderung
- Sicherungsübereignung an Refinanzierer überlappt mit Aussonderungsrecht → Prioritätsstreit

## Normen und Quellen

- § 47 InsO (Aussonderung): https://www.gesetze-im-internet.de/inso/__47.html
- § 108 InsO (Fortbestand): https://www.gesetze-im-internet.de/inso/__108.html
- § 103 InsO (Wahlrecht): https://www.gesetze-im-internet.de/inso/__103.html
- § 55 InsO (Masseverbindlichkeiten): https://www.gesetze-im-internet.de/inso/__55.html
- § 21 InsO (vorläufige Insolvenzverwaltung): https://www.gesetze-im-internet.de/inso/__21.html
- § 174 InsO (Forderungsanmeldung): https://www.gesetze-im-internet.de/inso/__174.html
- BGH-Rechtsprechung zu Sanierungsbeitrag und Anfechtungsrisiko nur nach Livecheck mit Gericht, Datum, Aktenzeichen und Quelle zitieren

## Output-Formate

- **Sofortmaßnahmen-Plan**: Checkliste für LG ab Insolvenzantrag
- **Forderungsanmeldungs-Vorlage**: § 174 InsO (Raten, Schadensersatz)
- **Aussonderungsantrag-Muster**: An Insolvenzverwalter
- **Fortführungs-Analyse**: Masseverbindlichkeit vs. Quote-Forderung

## 3. `lease-018-insolvenz-leasinggeber-eigentum-und-refinanzierung`

**Fokus:** Insolvenz des Leasinggebers: Nutzungsrecht des LN, Refinanzierungsstruktur, Sicherungsübereignung, § 108 InsO und Ansprüche des Refinanzierers.

# Insolvenz des Leasinggebers: Nutzungsrecht und Refinanzierung

## Zweck

Die Insolvenz des Leasinggebers stellt den Leasingnehmer vor ein unerwartetes Problem: Wer ist jetzt Vertragspartner? Kann der Refinanzierer das Objekt herausverlangen? Dieser Skill analysiert die InsO-Lage des LN, die Refinanzierungsstruktur und den Schutz des LN.

## Rechtlicher Rahmen

- § 108 I InsO: Miet-/Leasingvertrag über unbewegliche Sachen läuft fort
- § 103 InsO: Wahlrecht Verwalter bei beweglichen Sachen
- §§ 49 ff. InsO: Absonderungsrecht (Sicherungsübereignung des LG an Refinanzierer)
- § 566 BGB: „Kauf bricht nicht Miete" – Übergang des Leasingvertrags bei Eigentumsübergang
- §§ 398, 413 BGB: Abtretung der Leasingforderungen an Refinanzierer

## Typische Refinanzierungsstruktur

### Refinanzierung durch Forderungsabtretung
1. LG schließt Leasingvertrag mit LN
2. LG tritt Leasingforderungen (Raten) an Refinanzierer ab (§ 398 BGB)
3. LN zahlt direkt an Refinanzierer (§ 407 BGB: Schuldnerschutz)
4. Bei Insolvenz LG: Refinanzierer hält Forderungen, LN zahlt weiter an Refinanzierer

### Sicherungsübereignung des Objekts
1. LG übereignet das Leasingobjekt sicherungshalber an Refinanzierer (§§ 929, 930 BGB)
2. Bei Insolvenz LG: Refinanzierer ist wirtschaftlicher Eigentümer
3. Refinanzierer hat Absonderungsrecht (§ 51 Nr. 1 InsO) am Objekt

**Problem für LN**: Refinanzierer (neuer Eigentümer) kann das Objekt nach § 47 InsO aussondern. LN verliert Nutzungsrecht?

## § 108 InsO und § 566 BGB analog

### Analogie zu § 566 BGB
„Kauf bricht nicht Miete": Bei Eigentumsübergang an einem vermieteten Objekt tritt der Erwerber in den Mietvertrag ein.

**Analogie auf Leasing**: Wenn Refinanzierer Eigentumsübergang durch Sicherungsübereignung vollzieht: Tritt er in den Leasingvertrag ein? OLG-Rspr. bejaht Analogie; BGH noch nicht abschließend entschieden.

**Folge der Analogie**: LN behält Nutzungsrecht gegen Weiterzahlung der Raten an den Refinanzierer (neuen Vertragspartner). Kündigung durch Refinanzierer nur unter den Voraussetzungen des Leasingvertrags.

### § 108 InsO für bewegliches Leasing
H.M.: § 108 InsO gilt nur für Immobilien; bei beweglichen Sachen § 103 InsO → Wahlrecht Verwalter. Wenn Verwalter Erfüllung wählt: Vertrag läuft fort als Masseverbindlichkeit.

## Schutz des Leasingnehmers

### Gutgläubiger Erwerb des Nutzungsrechts?
- Nutzungsrecht des LN (Besitz) ist kein Recht, das gutgläubig erworben werden kann (§§ 932 ff. BGB: nur Eigentumsrecht)
- LN hat Besitzrecht kraft Leasingvertrag; dieses erlischt mit Kündigung oder bei wirksamer Aussonderung

### Praktischer Schutz: Due-Diligence vor Vertragsschluss
- LN sollte vor Leasingvertragsschluss prüfen: Ist LG solide finanziert? Hat LG Refinanzierungspartner?
- Im Vertrag: Klausel, dass LN bei Refinanziererwechsel informiert wird
- KWG § 1 II Nr. 10: Finanzierungsleasinggesellschaft braucht BaFin-Erlaubnis → Aufsichtskontrolle

## Forderungsanmeldung des LN in der Insolvenz des LG

- LN hat Ansprüche aus vorausgezahlten Raten (Bereicherungsrecht, § 812 BGB)
- Anspruch auf Rückgabe von Sicherheitsleistungen/Depots
- Schadensersatz bei schuldloser Kündigung?

## Prüfprogramm

1. Ist LG insolvent? Eröffnungsbeschluss und Verwalterbestellung prüfen
2. Refinanzierungsstruktur: Wer hält die Leasingforderungen? Wer hat Eigentum am Objekt?
3. § 108 InsO / § 566 BGB-Analogie: Gilt das Nutzungsrecht fort?
4. KWG-Erlaubnis des LG: Bestand? Widerruf durch BaFin?
5. LN: Klare Zahlungspflicht an Refinanzierer oder Verwalter?
6. Anmeldung von Gegenforderungen des LN (vorausgezahlte Raten, Kaution)

## Typische Fallen

- LN zahlt weiterhin an insolventen LG statt an Refinanzierer → Doppelzahlung möglich
- § 566 BGB-Analogie nicht beachtet → LN verliert Nutzungsrecht unnötigerweise
- KWG-Erlaubniswiderruf: Betrieb des LG eingestellt → Vertrag faktisch beendet, bevor InsO eröffnet
- Sicherheitsleistung beim insolventen LG verloren; keine Anmeldung als Forderung

## Normen und Quellen

- § 108 InsO: https://www.gesetze-im-internet.de/inso/__108.html
- § 103 InsO: https://www.gesetze-im-internet.de/inso/__103.html
- § 566 BGB (Kauf bricht nicht Miete): https://dejure.org/gesetze/BGB/566.html
- §§ 49–51 InsO (Absonderung): https://www.gesetze-im-internet.de/inso/__49.html
- KWG § 1 II Nr. 10 (Finanzierungsleasing): https://www.gesetze-im-internet.de/kredwg/__1.html
- KWG § 32 (Erlaubnispflicht): https://www.gesetze-im-internet.de/kredwg/__32.html
- BGH XII ZR 18/08: https://www.bgh.de

## Output-Formate

- **Sofortmaßnahmen-Plan**: LN bei Insolvenz des LG
- **Refinanzierungsstruktur-Diagramm**: LG, LN, Refinanzierer, Eigentum, Forderungen
- **Forderungsanmeldungs-Vorlage**: LN gegen InsO-Masse des LG
- **Checkliste**: § 566 BGB-Analogie – gilt Nutzungsrecht fort?
