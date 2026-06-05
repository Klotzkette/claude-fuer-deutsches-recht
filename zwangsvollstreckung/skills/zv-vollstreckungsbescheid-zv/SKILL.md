---
name: zv-vollstreckungsbescheid-zv
description: "ZV Vollstreckungsbescheid ZV: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# ZV Vollstreckungsbescheid ZV

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **ZV Vollstreckungsbescheid ZV** im Plugin Zwangsvollstreckung (ZPO §§ 704 ff.). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `zv-vollstreckungsbescheid-folge` | Mahnbescheid wurde erlassen und Gläubiger muss entscheiden wie es weitergeht. § 699 ZPO Vollstreckungsbescheid Online-Mahnportal. Prüfraster: Beantragung VB Reaktion auf Einspruch § 700 ZPO Übergang streitiges Verfahren Wirkung VB als Titel Klausel kraft Gesetzes § 796 Abs. 1. Output: VB-Antrag oder Strategie-Empfehlung nach Einspruch. Abgrenzung zu zv-mahnbescheid-online (Mahnbescheid-Antrag) und zv-kommandocenter. |
| `zv-vollstreckungsschutz-haertefall-765a` | Schuldner ist schwerkrank suizidgefaehrdet oder sonst besonders schutzbedürftig und will Vollstreckung stoppen. § 765a ZPO Vollstreckungsschutz sittenwidrige Haerte. Prüfraster: Antrag Einstellung oder Beschraenkung Haerteanwendungsfaelle Krankheit Suizidgefahr Obdachlosigkeit Glaubhaftmachung eidesstattliche Versicherung. Output: Schutzantrag § 765a ZPO und Glaubhaftmachungs-Vorlage. Abgrenzung zu zv-abwehr-schuldner (sonstige Abwehr) und zv-räumung-885 (Räumungsschutz). |
| `zv-zvg-antrag-glaeubiger` | Gläubiger hat Grundschuld oder Hypothek und will Immobilie des Schuldners versteigern lassen. ZVG Zwangsversteigerungsgesetz. Prüfraster: Antrag Anordnung §§ 15 ff. ZVG Beitritt § 27 ZVG geringstes Gebot Bargebot Verteilungstermin vorheriges Recht eintragen Zwangshypothek § 866 ZPO. Output: ZVG-Antrag Gläubiger und Versteigerungs-Strategie. Abgrenzung zu zv-notarielle-urkunde-grundschuld (Titelgrundlage) und zv-zvg als allgemeines Zwangsversteigerungsrecht. |

## Arbeitsweg

Im Plugin Zwangsvollstreckung (ZPO §§ 704 ff.) gilt für **ZV Vollstreckungsbescheid ZV**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `zv-vollstreckungsbescheid-folge`

**Fokus:** Mahnbescheid wurde erlassen und Gläubiger muss entscheiden wie es weitergeht. § 699 ZPO Vollstreckungsbescheid Online-Mahnportal. Prüfraster: Beantragung VB Reaktion auf Einspruch § 700 ZPO Übergang streitiges Verfahren Wirkung VB als Titel Klausel kraft Gesetzes § 796 Abs. 1. Output: VB-Antrag oder Strategie-Empfehlung nach Einspruch. Abgrenzung zu zv-mahnbescheid-online (Mahnbescheid-Antrag) und zv-kommandocenter.

# Vollstreckungsbescheid und Folgeverfahren


## Triage zu Beginn

1. Ist die Widerspruchsfrist von 2 Wochen ab Zustellung des Mahnbescheids abgelaufen?
2. Wurde der VB-Antrag rechtzeitig gestellt (innerhalb 6 Monaten nach MB-Zustellung, § 701 ZPO)?
3. Hat der Schuldner Einspruch gegen den VB erhoben — wenn ja, Übergang ins Streitverfahren?
4. Ist der Schuldner insolvent — § 89 InsO Vollstreckungsverbot prüfen?

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen

- § 699 ZPO — Antrag auf Vollstreckungsbescheid (frühestens 14 Tage nach MB-Zustellung)
- § 700 ZPO — Einspruch gegen VB (Frist 2 Wochen ab Zustellung)
- § 701 ZPO — 6-Monats-Frist für VB-Antrag ab MB-Zustellung
- § 796 Abs. 1 ZPO — VB trägt Klausel kraft Gesetzes
- § 204 Abs. 2 S. 1 BGB — Ende der Verjährungshemmung bei Verfahrenseinstellung
- § 705 ZPO — Rechtskraft des VB nach Ablauf der Einspruchsfrist

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Aufgabe

Der Vollstreckungsbescheid (VB) ist der Titel, den die meisten Mahnverfahren in Deutschland produzieren. Der Skill begleitet den Antrag, die Reaktion auf Einspruch und die Vollstreckung aus dem VB.

## Rechtsgrundlagen

- **§ 699 ZPO** – Vollstreckungsbescheid auf Antrag nach Ablauf der Widerspruchsfrist; nicht früher als 14 Tage nach Zustellung des Mahnbescheids (§ 699 Abs. 1 S. 2 ZPO).
- **§ 700 ZPO** – Einspruch innerhalb von 2 Wochen ab Zustellung des VB; Verfahren wird auf Antrag ans Streitgericht abgegeben (§ 700 Abs. 3 ZPO).
- **§ 796 Abs. 1 ZPO** – VB ist Vollstreckungstitel mit Klausel von Gesetzes wegen; gesonderte Klauselerteilung nicht erforderlich.
- **§ 700 Abs. 1 ZPO** – VB wirkt wie ein für vorläufig vollstreckbar erklärtes Versäumnisurteil; Sicherheitsleistung nicht erforderlich.
- **§ 705 ZPO** – Rechtskraft tritt ein mit Ablauf der Einspruchsfrist (§ 700 Abs. 1 i.V.m. § 705 S. 2 ZPO).

## VB beantragen

1. **Voraussetzungen prüfen**:
 - Mahnbescheid erlassen und dem Antragsgegner zugestellt
 - Frist von 14 Tagen ab Zustellung verstrichen
 - Kein Widerspruch eingelegt (oder nur Teilwiderspruch – dann VB nur über unbestrittenen Teil)
 - VB-Antrag innerhalb von 6 Monaten nach Mahnbescheid-Zustellung gestellt § 701 ZPO – sonst Verfall des Mahnbescheids
2. **Antrag stellen** über [online-mahnantrag.de](https://www.online-mahnantrag.de): Antragsart "Vollstreckungsbescheid beantragen", Aktenzeichen des Mahnbescheids angeben, Versandverlust meldet System eigenständig.
3. **Erlass und Zustellung** des VB an Antragsgegner von Amts wegen § 699 Abs. 4 ZPO.
4. **Wiedervorlage** 3 Wochen nach VB-Erlass: Einspruch erfolgt? Wenn nicht: Rechtskraft, vollstrecken.

## Vollstreckung aus dem VB

Der VB ist sofort vollstreckbar (§ 700 Abs. 1 ZPO) **ohne** Sicherheitsleistung. Er trägt die Klausel kraft Gesetzes § 796 Abs. 1 ZPO. Es genügt:

1. **Ausfertigung des VB** mit Zustellnachweis als Vollstreckungstitel.
2. **Vollstreckung beginnen**: PfÜB, Mobiliarvollstreckung, Vermögensauskunft, je nach Zielobjekt – Skill `zv-kommandocenter` einsteigen lassen.

## Reaktion auf Einspruch nach VB

- **Einspruch innerhalb der 2-Wochen-Frist § 700 Abs. 1 ZPO**: Verfahren geht auf Antrag eines Beteiligten ans Streitgericht. Eingang dort = Klagebegründungspflicht innerhalb von 2 Wochen § 697 ZPO. Gerichtsgebühren werden fällig (3,0-Verfahrensgebühr Nr. 1210 KV GKG abzüglich der 0,5 aus dem Mahnverfahren).
- **Verspäteter Einspruch**: gilt als Einspruch und ist als unzulässig zu verwerfen, wenn nicht Wiedereinsetzung in den vorigen Stand § 233 ZPO begehrt und gewährt wird.
- **Teileinspruch**: nur der bestrittene Teil geht ins Streitverfahren; der unbestrittene Teil bleibt rechtskräftig und vollstreckbar.

## Häufige Stolpersteine

- **6-Monats-Frist** § 701 ZPO – nicht der Mahnbescheid, sondern der VB-Antrag muss innerhalb dieser Frist gestellt werden. Versäumnis = Antrag erneut.
- **Zustellungsnachweis fehlt**: VB darf nicht erlassen werden, wenn Mahnbescheid nicht zugestellt wurde; bei Auslandszustellung oft Verzögerung.
- **Einspruch nicht gegen VB, sondern gegen "Anspruch" formuliert** – wird vom Gericht als Einspruch ausgelegt § 133 BGB, wenn Wille erkennbar.
- **Mahnbescheid an falsche Anschrift zugestellt**: Heilung § 189 ZPO nur bei tatsächlichem Zugang; sonst muss erneut zugestellt werden, dann läuft Frist neu.

## Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Ausgabeformat

```
VB-STATUS [Mandant] gegen [Schuldner]

Mahnbescheid:
 Zugestellt am: [DD.MM.JJJJ]
 Frist 14 Tage ablauf: [DD.MM.JJJJ]
 Widerspruch: [NEIN / JA Volltext: ...]

VB-Antrag:
 Beantragt am: [DD.MM.JJJJ]
 6-Monats-Frist § 701: [eingehalten]
 VB erlassen am: [DD.MM.JJJJ]
 VB zugestellt am: [DD.MM.JJJJ]

Einspruchsfrist: [Ende DD.MM.JJJJ]
Einspruch eingegangen: [NEIN / JA – Übergang Streitverfahren]

Status: [Rechtskraft eingetreten am DD.MM.JJJJ – VOLLSTRECKBAR]

Nächster Skill: [zv-kommandocenter / zv-pfueb-bank / ...]
```

## Qualitätsgates

- Niemals VB vollstrecken, ohne Zustellnachweis vorzulegen § 750 ZPO.
- Bei Insolvenz nach VB-Erlass: keine Einzelzwangsvollstreckung mehr § 89 InsO, Forderung zur Tabelle anmelden.

## Querverweise

- `zv-mahnbescheid-online` – Mahnantrag.
- `zv-titel-klausel-zustellung` – VB-Klausel kraft Gesetzes.
- `zv-pfueb-bank`, `zv-pfueb-arbeitsentgelt`, `zv-mobiliar-gv-auftrag` – Vollstreckungsmaßnahmen.
- `forderungsmanagement-klagewerkstatt/klagevorlage-aus-eigenen-mustern` – nach Einspruch Klagebegründung.


<!-- AUDIT 27.05.2026 bundle_055
Halluzinations-Reparatur: BGH VII ZB 34/13 (NOT_FOUND) geloescht.
Kein Ersatz: § 796 Abs. 1 ZPO regelt Klausel kraft Gesetzes direkt im Gesetz;
kein bekanntes BGH-AZ zu diesem Einzelpunkt verifizierbar auf dejure.org.
-->

## 2. `zv-vollstreckungsschutz-haertefall-765a`

**Fokus:** Schuldner ist schwerkrank suizidgefaehrdet oder sonst besonders schutzbedürftig und will Vollstreckung stoppen. § 765a ZPO Vollstreckungsschutz sittenwidrige Haerte. Prüfraster: Antrag Einstellung oder Beschraenkung Haerteanwendungsfaelle Krankheit Suizidgefahr Obdachlosigkeit Glaubhaftmachung eidesstattliche Versicherung. Output: Schutzantrag § 765a ZPO und Glaubhaftmachungs-Vorlage. Abgrenzung zu zv-abwehr-schuldner (sonstige Abwehr) und zv-räumung-885 (Räumungsschutz).

# Vollstreckungsschutz § 765a ZPO — Härtefall

## Aufgabe

Antrag des **Schuldners** auf einstweilige Einstellung, Beschränkung oder Aufhebung einer Vollstreckungsmaßnahme, wenn diese eine **mit guten Sitten nicht vereinbare Härte** darstellen würde. Die Vorschrift ist die zentrale Auffangnorm für Härtefälle, in denen die Standard-Schutzmechanismen (P-Konto § 850k ZPO, Pfändungsfreigrenzen § 850c ZPO) nicht ausreichen.

> ⚠️ **Hohe Hürde**: § 765a ZPO ist **eng auszulegen** — nicht jede wirtschaftliche oder soziale Belastung reicht. Erforderlich ist eine Härte, die der **gesamten Rechtsordnung** widerspricht (BGH-Linie). Typisch: existenzielle Gefahr für Leben, Gesundheit, menschenwürdiges Dasein.

## Startet bei

- Vollstreckungsmaßnahme angekündigt oder läuft
- Schuldner in schwerwiegender persönlicher Situation (Krankheit, drohender Suizid, Schwangerschaft / Geburt, Tod naher Angehöriger, drohende Obdachlosigkeit)
- Standard-Schutzmechanismen reichen nicht (Pfändungsfreigrenze, P-Konto unzureichend)
- Klassische Vollstreckungserinnerung § 766 ZPO greift nicht (Verfahrensfehler nicht ersichtlich)
- Vollstreckungsabwehrklage § 767 ZPO bietet keine schnelle Hilfe

## Rechtsgrundlagen

- **§ 765a Abs. 1 ZPO** — "Auf Antrag des Schuldners kann das Vollstreckungsgericht die Vollstreckung einstweilen einstellen, beschränken oder aufheben, wenn die Maßnahme unter voller Würdigung der Schutzbedürfnisse des Gläubigers wegen ganz besonderer Umstände eine Härte bedeutete, die mit den guten Sitten nicht vereinbar ist."
- **§ 765a Abs. 2 ZPO** — Anhörung der Beteiligten (Gläubiger).
- **§ 765a Abs. 3 ZPO** — Bei Räumungsvollstreckung gegen Wohnraum: Pflicht-Anhörung des zuständigen Trägers Sozialhilfe und ggf. weiterer Personen (insb. Suizidgefahr).
- **Art. 1, 2 GG** — Menschenwürde, Recht auf Leben und körperliche Unversehrtheit; verfassungsrechtlicher Maßstab.
- **§§ 766, 767, 769 ZPO** — abgrenzende Schutzwege (Erinnerung, Abwehrklage, einstweilige Einstellung bei Klage).
- **§ 850k ZPO** — P-Konto-Schutz als vorgelagerter Standard-Schutz.

## Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Typische Konstellationen

### Konstellation A — Suizidgefahr

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **Glaubhaftmachung**: substantielle, nicht nur behauptete Suizidgefahr.
- **Maßnahme**: regelmäßig einstweilige Einstellung mit Wiedervorlage; Verlängerung möglich.
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Konstellation B — Schwere Krankheit / Pflege

- Schwere chronische Erkrankung Schuldner oder Familienangehöriger
- Krankenhausaufenthalt zum Vollstreckungstermin
- Substantiierung mit Attest, ggf. ärztlichem Verlauf

### Konstellation C — Schwangerschaft / Geburt

- Hochschwangerschaft (typisch ab 7. Monat)
- Kürzlich entbunden / Wochenbett-Frist
- Maßnahme: zeitlich begrenzte Einstellung

### Konstellation D — Räumungsschutz Wohnraum (§ 765a Abs. 3 ZPO)

- Drohende Obdachlosigkeit
- Suizidgefahr im Wohnsitz
- Mitbewohner mit besonderen Schutzbedürfnissen (Säugling, Schwerstkranker)
- **Pflichtanhörung Sozialamt** durch das Gericht
- Abgrenzung zu **§ 721 ZPO** (Räumungsfrist im Urteil) und **§ 794a ZPO** (Räumungsfrist im Vergleich)

### Konstellation E — Tod / Trauerfall

- Tod naher Angehöriger kürzlich
- Beerdigung in unmittelbarer Nähe Vollstreckungstermin
- Maßnahme: kurzfristige Einstellung

### Konstellation F — Existenzielle Bedrohung Lebensgrundlage

- Werkzeug / Berufsbasis betroffen (Abgrenzung zu § 811 ZPO unpfändbar)
- Verlust der einzigen Arbeitsstelle / Ausbildungsmittel
- Substantiierung mit konkreten Folgen

## Antragsverfahren

### Schritt 1 — Eilbedürftigkeit

- Vollstreckungstermin nahe oder läuft?
- Antrag **vor** Vollstreckung, idealerweise mehrere Tage davor
- Bei laufender Maßnahme: sofortige Eilanträge nach § 769 ZPO parallel

### Schritt 2 — Zuständiges Gericht

- **Vollstreckungsgericht** (§ 764 ZPO) — typisch Amtsgericht am Ort der Maßnahme
- Bei Räumung: AG am Lage-Ort des Grundstücks
- Bei Forderungspfändung: AG am Wohnsitz Schuldner

### Schritt 3 — Antragsinhalt

- **Konkrete Maßnahme** bezeichnen (Termin, Ort, Vollstreckungsgegenstand)
- **Härtegrund** substantiiert darlegen
- **Glaubhaftmachung** (§ 294 ZPO) — eidesstattliche Versicherung + Belege (Atteste, Sozialamt-Bescheinigungen)
- **Antrag** auf einstweilige Einstellung / Beschränkung / Aufhebung
- **Befristung** akzeptieren (typisch 3–6 Monate)

### Schritt 4 — Gläubiger-Anhörung

- Gericht hört Gläubiger
- Gläubiger kann widersprechen; bei nicht ausreichender Härte Ablehnung möglich

### Schritt 5 — Beschluss

- Mit Auflage / Befristung möglich
- Verlängerung auf neuen Antrag möglich
- Rechtsbehelf: **sofortige Beschwerde** § 793 ZPO (zwei Wochen, LG)

## Schreibvorlage — Antrag § 765a ZPO (verkürzt)

```
[Anwaltskanzlei] [Datum]

An das Amtsgericht [Ort]
— Vollstreckungsgericht —
[Anschrift]

In der Zwangsvollstreckungssache
[Glaeubiger] ./. [Schuldner]
Az.: [Az. AG / Vollstreckungsauftrag]

Antrag des Schuldners gemaess § 765a ZPO auf
einstweilige Einstellung der Zwangsvollstreckung
mit Eilbeduerftigkeit

Sehr geehrte Damen und Herren,

namens und in Vollmacht des Schuldners beantrage ich,

die mit Beschluss / Pfaendungs- und Ueberweisungsbeschluss / Auftrag
des Gerichtsvollziehers vom [Datum] eingeleitete Zwangsvollstreckung
gegen den Schuldner [bis zum / einstweilen bis zur Entscheidung
ueber den Antrag] einstweilen einzustellen.

Begruendung

I. Sachverhalt
[Konkrete Vollstreckungsmaßnahme — Termin, Ort, Gegenstand]

II. Haertegrund nach § 765a Abs. 1 ZPO
[Substantiierte Darstellung — Krankheit / Suizidgefahr / Schwanger-
schaft / Obdachlosigkeit / Trauerfall; mit Atest- / Belegverweis]

III. Glaubhaftmachung (§ 294 ZPO)
- Aerztliches Attest vom [Datum], Anlage A1
- Eidesstattliche Versicherung des Schuldners, Anlage A2
- [ggf. Sozialamt-Bescheinigung, Krankenhaus-Bestaetigung etc.]

IV. Beruecksichtigung der Glaeubigerinteressen
[Abwaegung — Gewicht der Glaeubigerforderung vs. Schwere der
Schuldner-Haerte; Hinweis auf Befristung der Einstellung]

V. Antrag
1. Die Vollstreckung wird einstweilen [bis zum [Datum] / bis auf
 weiteres mit Wiedervorlage in [X] Monaten] eingestellt.
2. Hilfsweise: Die Vollstreckung wird auf [konkrete Maßnahme]
 beschraenkt.

Es wird um eilige Entscheidung gebeten; die Vollstreckung droht am
[Datum].

Mit freundlichen Gruessen
[Unterschrift]
Rechtsanwalt/-anwaeltin
```

## Risiken und Red Flags

| Konstellation | Rot | Orange | Grün |
|---|---|---|---|
| Pauschale Härtebehauptung | Ablehnung absehbar | Substantiierung fehlt | Konkrete Belege beigefügt |
| Suizidgefahr behauptet ohne Attest | Ablehnung; Vollstreckung läuft | Attest in Vorbereitung | Fachärztliches Gutachten beigebracht |
| Antrag während laufender Maßnahme | Schaden tritt ein | Eilbedürftigkeit substantiieren | Antrag vor Termin |
| Gläubiger-Interesse > Schuldner-Härte | Ablehnung wahrscheinlich | knappe Abwägung | klar überwiegende Schuldner-Härte |
| Räumung Wohnraum ohne Sozialamt | § 765a Abs. 3 ZPO-Verfahrensfehler | Vorbereitung läuft | Pflicht-Anhörung dokumentiert |

## Abgrenzung zu anderen Schutzwegen

| Norm | Wirkung | Wann statt § 765a? |
|---|---|---|
| § 766 ZPO Erinnerung | Verfahrensfehler des GV / Vollstreckungsgerichts | Wenn Maßnahme rechtswidrig (nicht nur hart) |
| § 767 ZPO Vollstreckungsabwehrklage | Materielle Einwendungen gegen den Anspruch | Wenn Anspruch erloschen / nicht durchsetzbar |
| § 769 ZPO einstweilige Einstellung bei Klage | Während Abwehrklage | Wenn Klage nach § 767 anhängig |
| § 712 ZPO Schutzantrag im Urteilsverfahren | Vor Rechtskraft | Vor Vollstreckbarkeit |
| § 850k ZPO P-Konto | Pfändungsschutz Bankkonto | Standard, vorrangig prüfen |

## Querverweise

- `zv-abwehr-schuldner` — übergeordnete Schuldnerschutz-Triage
- `zv-raeumung-885` — Räumungsvollstreckung (§ 765a Abs. 3 Pflicht)
- `zv-pfueb-bank` — P-Konto-Schutz parallel
- `zv-pfaendungstabelle-2025` — Pfändungsfreigrenzen
- `betreuungsrecht` — bei betreutem Schuldner
- `fachanwalt-medizinrecht` — bei medizinischen Attest-Fragen

## Quellen und Updates

Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## 3. `zv-zvg-antrag-glaeubiger`

**Fokus:** Gläubiger hat Grundschuld oder Hypothek und will Immobilie des Schuldners versteigern lassen. ZVG Zwangsversteigerungsgesetz. Prüfraster: Antrag Anordnung §§ 15 ff. ZVG Beitritt § 27 ZVG geringstes Gebot Bargebot Verteilungstermin vorheriges Recht eintragen Zwangshypothek § 866 ZPO. Output: ZVG-Antrag Gläubiger und Versteigerungs-Strategie. Abgrenzung zu zv-notarielle-urkunde-grundschuld (Titelgrundlage) und zv-zvg als allgemeines Zwangsversteigerungsrecht.

# ZVG-Antrag (Zwangsversteigerung / Zwangsverwaltung)

## Aufgabe

Vollstreckung in das Grundstück. Wird in der Regel parallel zur PfÜB betrieben. Dieser Skill steuert ausschließlich die Gläubigerseite; der Schwesterskill `zwangsverwaltung-zvg` betrifft die Verwalterperspektive.

## Startet bei

- Titel + Klausel + Zustellung grün
- Grundstück im Eigentum des Schuldners (oder dinglich gegen Eigentümer nach § 800 ZPO)
- Vorzugsweise eingetragene Grundschuld – sonst Zwangshypothek § 866 ZPO erforderlich

## Rechtsgrundlagen

- §§ 15-145 ZVG – Zwangsversteigerung
- §§ 146-161a ZVG – Zwangsverwaltung
- § 27 ZVG – Beitritt
- § 30a ZVG – Schuldnerschutz Einstellung
- § 765a ZPO – Vollstreckungsschutz
- § 866 ZPO – Sicherungshypothek (bei persönlichem Titel)
- § 867 ZPO – Verfahren der Eintragung
- § 49 InsO – Absonderungsrecht
- § 10 ZVG – Rangklassen
- § 28 GBO – Bestimmtheit

## Workflow

1. **Vollstreckungsgrundlage**: dinglicher Titel (Grundschuld in Verbindung mit Unterwerfungsurkunde – siehe `zv-notarielle-urkunde-grundschuld`) oder persönlicher Titel + Zwangshypothek § 866 ZPO.
2. **Grundbucheinsicht** vor jedem Antrag – aktuell, weil sich Rangverhältnisse verändert haben können.
3. **Zwangshypothek § 866 ZPO eintragen**, wenn nur persönlicher Titel: Antrag beim Grundbuchamt, Forderung mindestens 750 EUR (§ 866 Abs. 3 ZPO), nach Eintragung sechs Monate warten? Nein – Eintragung selbst genügt; die sechs Monate betreffen die Wartepflicht bei Hypothek § 1147 BGB nicht.
4. **Antrag auf Anordnung** der Zwangsversteigerung beim Vollstreckungsgericht (Amtsgericht der belegenen Sache).
5. **Beitritt § 27 ZVG**, wenn bereits Verfahren läuft – einfacher, kostengünstiger.
6. **Geringstes Gebot** und Bargebot prüfen: alle vorrangigen Rechte plus 7/10 Verkehrswert – sonst Wertgrenzen § 85a ZVG.
7. **Zwangsverwaltung** als Alternative oder Parallelverfahren: Mieten und Pachten fließen über Verwalter an Gläubiger.
8. **Schuldnerschutzanträge** des Schuldners erwarten (§ 30a ZVG, § 765a ZPO) – Stellungnahme vorbereiten.
9. **Verteilungstermin** § 105 ZVG: Erlös wird nach Rangklassen § 10 ZVG verteilt.

## Wertgrenzen § 85a ZVG

- Im ersten Termin wird kein Zuschlag erteilt, wenn das Meistgebot unter 50 % des Verkehrswerts liegt.
- Zwischen 50 % und 70 % kann auf Antrag des Berechtigten Zuschlag versagt werden.
- Ab dem zweiten Termin entfallen die Grenzen.

## Insolvenz des Schuldners

- § 49 InsO: dinglich gesicherter Gläubiger ist absonderungsberechtigt.
- Die Zwangsversteigerung kann vom Insolvenzverwalter nach § 30d ZVG eingestellt werden.
- Verwertung durch den Verwalter ist häufig wirtschaftlicher.

## Leitentscheidungen

- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Ausgabeformat

```
ZVG-ANTRAG [Mandant] gegen [Schuldner], AG [Belegenheitsgericht]

Titel: [Art, Datum]
Grundbuch: [Ort, Bl, Flurst, Lage]
Eigentümer: [Schuldner / Dritter § 800 ZPO]
Rangstelle: [Abt. III, lfd Nr / Zwangshypothek § 866 erforderlich]
Vorrangige Rechte: EUR x (Bank, Steuer, sonstige)
Verkehrswert: EUR y (Schätzung)
Geringstes Gebot: ~ EUR z
Verfahrenstyp: Versteigerung / Verwaltung / beides
Beitritt § 27 möglich? [ja, AG Az / nein]

NÄCHSTER SCHRITT: Anordnung beim AG / Beitritt
WIEDERVORLAGE: DD.MM.JJJJ
```

## Qualitätsgates

- Niemals ohne aktuelle Grundbucheinsicht antragen.
- Bei persönlichem Titel: Zwangshypothek vorher eintragen.
- Wertgrenzen § 85a ZVG beachten – im ersten Termin kann Zuschlag versagt werden.
- Bei Insolvenz § 30d ZVG mitdenken.
- Bei selbstgenutztem Wohneigentum § 765a ZPO mit Härtefall-Vortrag rechnen.

## Querverweise

- `zv-notarielle-urkunde-grundschuld`
- `zv-pfueb-bank`, `zv-pfueb-arbeitsentgelt` (parallel)
- `zwangsverwaltung-zvg` – Verwalterperspektive (anderes Plugin)
- `zv-abwehr-schuldner`
- `insolvenzforderungsanmeldungspruefung/ifap-tabellenauszug-178`
