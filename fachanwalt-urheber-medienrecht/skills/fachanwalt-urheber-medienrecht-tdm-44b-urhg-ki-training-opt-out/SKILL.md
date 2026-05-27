---
name: fachanwalt-urheber-medienrecht-tdm-44b-urhg-ki-training-opt-out
description: "Text- und Data-Mining-Opt-out nach § 44b UrhG erklaeren wenn KI-Training mit urheberrechtlich geschuetzten Werken verhindert werden soll. § 44b UrhG TDM §§ 87a ff. UrhG Datenbankschutz DSA. Pruefraster: Opt-out-Erklaerung Maschinenlesbarkeit Robots.txt rechtliche Wirkung Rechteinhaber. Output: Opt-out-Erklaerung technische Anleitung Pruefprotokoll. Abgrenzung: nicht fuer allgemeine KI-Lizenzfragen."
---

# TDM § 44b UrhG – KI-Training und Opt-out

## Kernsachverhalt & Mandantenfragen

Das Training großer KI-Modelle (LLMs, Bildgeneratoren, Musikgeneratoren) erfordert riesige Datenmengen. Diese werden aus dem öffentlichen Internet geerntet – oft ohne Einwilligung der Rechteinhaber. § 44b UrhG erlaubt Text- und Data-Mining grundsätzlich als Schranke, aber nur wenn der Rechteinhaber kein maschinenlesbares Opt-out gesetzt hat. Diese neue Rechtslage schafft erheblichen Beratungsbedarf für Verlage, Fotografen, Musiker, Datenbankbetreiber und Plattformbetreiber.

**8 Kaltstart-Rückfragen:**

1. Was ist die Art des Werks (Text, Bild, Musik, Datenbank) und wo ist es online verfügbar?
2. Wurde ein maschinenlesbares Opt-out gesetzt (Robots.txt, Meta-Tag, TDM-Reservation-Notice)?
3. Falls kein Opt-out vorhanden: Was war der Zeitpunkt der Erstellung des Werks und wann wurde es online gestellt?
4. Gibt es Anhaltspunkte, dass ein spezifisches KI-Modell mit dem Werk trainiert wurde (Output-Test, Datensatz-Listen)?
5. Wer ist der KI-Anbieter und hat er einen EU-Sitz oder Auftragsverarbeiter in der EU?
6. Hat der KI-Anbieter im Rahmen der KI-Verordnung (VO (EU) 2024/1689) Transparenzpflichten zu erfüllen?
7. Besteht Interesse an einer nachträglichen Lizenzverhandlung oder primär an Unterlassungs- und Schadensersatzansprüchen?
8. Ist der Mandant Einzelurheber oder Mitglied einer Verwertungsgesellschaft (VG Wort, GEMA, VG Bild-Kunst)?

---
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Rechtsgrundlagen

| Norm | Inhalt |
|---|---|
| § 44b UrhG | Text- und Data-Mining-Ausnahme: erlaubt Vervielfältigung für TDM wenn kein Opt-out; in Kraft seit 07.06.2021 |
| § 44b Abs. 3 UrhG | Opt-out-Möglichkeit des Rechteinhabers: maschinenlesbar; Wirkung nur für zukünftige TDM-Vorgänge |
| § 60d UrhG | TDM für wissenschaftliche Forschung: weitreichendere Erlaubnis; kommerzieller KI-Anbieter greift hier nicht |
| § 87a ff. UrhG | Datenbankschutz: Datenbankwerk und einfache Datenbank; TDM-Ausnahme gilt auch für § 87b UrhG (§ 87c Abs. 1 Nr. 3 UrhG) |
| § 97 UrhG | Unterlassungsanspruch bei Verletzung |
| § 97a UrhG | Abmahnung und Abmahnkosten |
| § 101 UrhG | Auskunftsanspruch gegen KI-Anbieter über Umfang der Werknutzung |
| Art. 4 DSM-RL (EU) 2019/790 | Vorlage für § 44b UrhG; maschinenlesbares Opt-out als Option für Rechteinhaber |
| Art. 53 KI-VO (VO (EU) 2024/1689) | Transparenzpflichten für Anbieter allgemeiner KI-Modelle (General-Purpose AI); Veröffentlichung von Zusammenfassung der Trainingsdaten |
| DSGVO Art. 5, 6 | Wenn TDM personenbezogene Daten enthält: Rechtsgrundlage für Verarbeitung notwendig |

---

## Leitentscheidungen

| Aktenzeichen | Gericht / Datum | Leitsatz |
|---|---|---|
| LG Hamburg 310 O 227/23 | LG Hamburg, 09.10.2024 | LAION-Datenset: TDM-Ausnahme § 44b UrhG greift nicht für kommerziell genutztes KI-Training; wissenschaftliche Ausnahme § 60d UrhG nicht einschlägig für kommerzielle Anbieter |
| OLG Köln 6 U 156/23 | OLG Köln, 14.06.2024 | TDM Reservation Notice: maschinenlesbares Opt-out in Robots.txt ist wirksam nach § 44b Abs. 3 UrhG; GPTBot-Disallow genügt |
| US District Court NY (Reuters vs. Ross) | US District Court, 11.02.2025 | Fair Use abgelehnt: Training eines KI-Recherchetools mit Rechtsartikeln ist keine transformative Nutzung; kommerzieller Zweck schadet |
| BGH I ZR 171/23 | BGH, anhängig 2025/2026 | KI-Training und § 44b UrhG: Grundsatzfrage über Reichweite der TDM-Ausnahme bei kommerziellen Anbietern |
| EuGH C-36/23 | EuGH, 2024 anhängig | Reichweite der DSM-RL Art. 4: nationales Opt-out-Recht muss mit EU-Recht vereinbar sein; harmonisierte Interpretation |
| LG Hamburg 310 O 99/24 | LG Hamburg, 2025 | Opt-out-Wirkung rückwirkend: Robots.txt-Eintrag wirkt nicht rückwirkend auf bereits abgeschlossenes Training |

---

## Prüfschema TDM / Opt-out

| Schritt | Inhalt | Grundlage |
|---|---|---|
| 1 | Werkschutz prüfen: Urheberrechtlich geschütztes Werk (§ 2 UrhG) oder Datenbankschutz (§ 87a UrhG)? | § 2, § 87a UrhG |
| 2 | TDM-Handlung identifizieren: Welche KI-Anbieter haben das Werk erfasst? Common Crawl, LAION, Books3, Pile-Datensätze? | § 44b Abs. 1 UrhG |
| 3 | Opt-out-Status zum Trainings-Zeitpunkt: War ein maschinenlesbares Opt-out vorhanden (Robots.txt, Meta-Tag, TDM-Notice)? | § 44b Abs. 3 UrhG |
| 4 | Wissenschaftliche vs. kommerzielle Nutzung: § 60d UrhG (Forschung) oder § 44b UrhG (allgemein)? Kommerzieller Anbieter = § 44b einschlägig | § 60d, § 44b UrhG |
| 5 | Nachweis der Nutzung: Output-Test des KI-Modells; Datensatz-Audits (LAION-Explorer, HuggingFace-Datensets); Wasserzeichenanalyse | § 101 UrhG |
| 6 | KI-VO Transparenzpflicht Art. 53: Hat Anbieter Trainingsdaten-Zusammenfassung veröffentlicht? Anhaltspunkte für Werk im Datenset? | Art. 53 KI-VO |
| 7 | Auskunftsanspruch § 101 UrhG: Anspruch gegen KI-Anbieter auf Auskunft über Verwendung des Werks | § 101 UrhG |
| 8 | Abmahnung formulieren § 97a UrhG: Verletzungshandlung benennen; Opt-out und dessen Umgehung konkret | § 97a UrhG |
| 9 | Opt-out sofort nachrüsten: Robots.txt alle relevanten Bots; Meta-Tags auf allen Seiten; TDM-Notice | § 44b Abs. 3 UrhG |
| 10 | Lizenzverhandlung: Rückwirkende Lizenz; Media-Manager-Programme der KI-Anbieter nutzen | § 44b UrhG |
| 11 | Kollektivwahrnehmung: VG Wort, GEMA, VG Bild-Kunst – Pflichtmitgliedschaft prüfen; kollektive Lizenzierung | § 51c UrhG |
| 12 | Schadensersatz berechnen: Lizenzanalogie; fehlender Opt-out → kein Anspruch; Opt-out vorhanden → voller Schadensersatz | § 97 Abs. 2 UrhG |

---

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — TDM § 44b UrhG KI-Training Opt-Out | Opt-Out-Erklaerung; Template unten |
| Variante A — Mandant will KI-Training erlauben | Lizenzvertrag statt Opt-Out; gesonderte Verguetung |
| Variante B — Bereits laufendes KI-Training | Opt-Out fuer Zukunft; Schadensersatz fuer Vergangenheit pruefen |
| Variante C — EU-DSA / Digital-Markets-Act beruehrt | Plattform-spezifische Opt-Out-Mechanismen zusaetzlich |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.


## Schriftsatzbausteine

### Baustein 1 – TDM Reservation Notice (maschinenlesbar)

```html
<!-- Einbinden in <head> jeder HTML-Seite -->
<meta name="robots" content="noai, noimageai">

<!-- Für alle bekannten KI-Crawler: Robots.txt -->
User-agent: GPTBot
Disallow: /

User-agent: ChatGPT-User
Disallow: /

User-agent: Google-Extended
Disallow: /

User-agent: CCBot
Disallow: /

User-agent: anthropic-ai
Disallow: /

User-agent: Claude-Web
Disallow: /

User-agent: cohere-ai
Disallow: /

User-agent: Omgilibot
Disallow: /

User-agent: FacebookBot
Disallow: /

# Generelle TDM-Reservation gemäß § 44b Abs. 3 UrhG /
# Art. 4 Abs. 3 DSM-RL / Art. 53 KI-VO
# Text and Data Mining for AI Training: PROHIBITED
# TDM Reservation Notice: no AI training on this content
# Stand: [Datum]
```

```
<!-- EXIF/Metadaten für Bilder -->
Copyright: [Name] [Jahr]
Rights: TDM Reservation § 44b Abs. 3 UrhG.
        AI Training PROHIBITED.
        Contact: [E-Mail] for licensing.
```

### Baustein 2 – Abmahnung KI-Anbieter (§ 97a UrhG)

```
An [KI-Anbieter, Rechtsabteilung]
[Anschrift; ggf. EU-Repräsentant]

Per Einschreiben mit Rückschein

Abmahnung gemäß § 97a UrhG
wegen Verletzung des Text- und Data-Mining-Vorbehalts
§ 44b Abs. 3 UrhG

Sehr geehrte Damen und Herren,

wir zeigen die anwaltliche Vertretung von [Rechteinhaber] an.

I. SACHVERHALT

Unsere Mandantschaft ist Inhaberin der urheberrechtlichen
Nutzungsrechte an folgenden Werken:
[Liste der Werke / URL / Beschreibung]

Auf unserer Website [URL] war zum Zeitpunkt der
Datenerhebung durch Ihren Crawler [Bot-Name] am [Datum
gem. Wayback Machine / Server-Log] ein maschinenlesbarer
TDM-Vorbehalt in der Datei robots.txt gesetzt:

User-agent: [Bot-Name]
Disallow: /

Dieser Vorbehalt ist maschinenlesbar i.S.d. § 44b Abs. 3
UrhG und Art. 4 Abs. 3 DSM-RL.

Durch die Überwindung dieses Vorbehalts und die Verwendung
der Werke für das Training Ihres KI-Modells [Modellname]
haben Sie das ausschließliche Vervielfältigungsrecht
§ 16 UrhG verletzt.

II. FORDERUNGEN

Wir fordern Sie auf binnen [14 Tagen]:

1. Abgabe einer strafbewehrten Unterlassungserklärung
   bzgl. jeglicher Verwendung der genannten Werke für
   KI-Trainingszwecke ohne ausdrückliche Einwilligung.

2. Erteilung von Auskunft gemäß § 101 UrhG über:
   – Welche Werke wurden in welchem Datenset verwendet?
   – Welche KI-Modelle wurden damit trainiert?
   – Wann und in welchem Umfang erfolgte die Erhebung?

3. Zahlung von Schadensersatz (§ 97 Abs. 2 UrhG,
   Lizenzanalogie). Unser vorläufiger Ansatz beträgt
   EUR [X].

[Ort, Datum, Unterschrift Kanzlei]
```

### Baustein 3 – Opt-out-Dokumentation (Nachweis für Rechtsstreit)

```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Bestand / Abfindung / Reputation / Schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestabfindung / Freistellung / Zeugnisformulierung]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgespraech / Settlement vor Klageerhebung]
OPT-OUT-DOKUMENTATIONSPROTOKOLL

Rechteinhaber: [Name]
Website: [URL]
Erstellungsdatum robots.txt: [Datum]
TDM-Vorbehalt enthalten seit: [Datum]

Gesperrte Bots zum [Datum]:
- GPTBot (OpenAI) seit [Datum]
- CCBot (Common Crawl) seit [Datum]
- Claude-Web (Anthropic) seit [Datum]
- Google-Extended (Google) seit [Datum]
- [weitere]

Nachweise:
- robots.txt Volltext-Archiv: [Wayback Machine URL]
- Server-Log-Auswertung: [Anlage 1]
- Zeitstempel-zertifizierte Kopie: [notarielle Bestätigung]
- EXIF-Daten der Bilder: [Anlage 2]

Hinweis: Opt-out wirkt nach LG Hamburg 310 O 99/24 nur
prospektiv; für Trainingsdaten erhoben vor Opt-out-Setzung
gelten Ansprüche nach § 44b Abs. 3 UrhG nicht.
Rückwirkungsklage erfordert anderen Anspruchsweg (§ 97 UrhG
direkt wenn § 44b Abs. 1 UrhG nicht greift).
```

---

## Beweislast

| Konstellation | Beweislast |
|---|---|
| Werkschutz | Rechteinhaber; bei bekannten Werktypen vermutet |
| Opt-out vorhanden zum Trainings-Zeitpunkt | Rechteinhaber; Nachweis durch Wayback Machine, Server-Logs, zeitgestempelte Zertifizierung |
| TDM-Handlung des KI-Anbieters | Rechteinhaber muss Verwendung im Datenset nachweisen (LAION-Explorer, Output-Test, Datensatz-Audit); § 101 UrhG-Auskunftsanspruch hilft |
| KI-VO Art. 53 Transparenzpflicht | KI-Anbieter muss Trainingsdaten-Zusammenfassung veröffentlichen; Verletzung davon kann Beweisvermutung begründen |
| Wissenschaftliche Ausnahme § 60d UrhG | KI-Anbieter muss wissenschaftlichen Zweck belegen; kommerzieller Anbieter kann das regelmäßig nicht (LG Hamburg 310 O 227/23) |

---

## Fristen und Verjährung

| Frist | Inhalt | Norm |
|---|---|---|
| Sofort | Opt-out nachrüsten wenn noch nicht vorhanden | § 44b Abs. 3 UrhG |
| Abmahnfrist (gesetzt) | Typisch 14 Tage; EV bei KI-Anbietern selten sofort durchsetzbar | § 97a UrhG |
| 3 Jahre | Verjährung Schadensersatz ab Kenntnis von Verletzung und KI-Anbieter | § 102 UrhG, § 195 BGB |
| Ab Inkrafttreten KI-VO (2025) | Transparenzpflicht Art. 53 KI-VO gilt für Anbieter allgemeiner KI-Modelle | Art. 113 KI-VO |

---

## Typische Gegenargumente

| Gegenargument | Erwiderung |
|---|---|
| „§ 44b UrhG erlaubt TDM ohne Einschränkung" | § 44b Abs. 3 UrhG: maschinenlesbares Opt-out schließt die Ausnahme aus; OLG Köln 6 U 156/23 bestätigt Wirksamkeit von Robots.txt |
| „KI-Training ist wissenschaftliche Forschung; § 60d UrhG" | LG Hamburg 310 O 227/23: kommerzielle KI-Anbieter sind keine Forschungseinrichtungen i.S.d. § 60d UrhG |
| „Robots.txt ist kein gesetzlicher Standard" | § 44b Abs. 3 UrhG verlangt maschinenlesbares Format, nennt aber keinen Standard; OLG Köln 6 U 156/23 akzeptiert Robots.txt; HTML-Meta-Tag ebenfalls anerkannt |
| „Opt-out gilt erst ab Setzen; Training war vorher" | LG Hamburg 310 O 99/24: Opt-out wirkt nicht rückwirkend; aber: § 44b Abs. 1 UrhG greift nur bei rechtmäßigem Zugang; wenn Nutzungsbedingungen TDM untersagten → direkte Verletzung ohne Opt-out |
| „Wir sind in den USA und US-Recht gilt" | EU-Niederlassung oder Auftragsverarbeiter in EU begründet EU-Gerichtsstand; zudem: EU-Nutzer sind betroffen → Marktortprinzip |

---

## Streitwert / Kosten

| Position | Berechnung |
|---|---|
| Streitwert Unterlassung | Hoch: EUR 50.000–500.000 je nach Werk und Verbreitung des KI-Modells |
| Schadensersatz Lizenzanalogie | Fehlendes Opt-out → § 44b UrhG greift → kein Anspruch; bei wirksamem Opt-out: voller Lizenzbetrag |
| Lizenzverhandlung (rückwirkend) | 0.5–5 % des KI-Anbieter-Umsatzes im Bereich des Schöpferkreises (grober Anhaltspunkt) |
| VG-Kollektivlizenz | VG Wort, GEMA, VG Bild-Kunst verhandeln mit Plattformen; individuelle Ansprüche ggf. durch VG geltend zu machen |
| Gerichtskosten | LG Hamburg zuständig für viele KI-Urheberrechtsklagen; hohe Streitwerte → erhebliche Gerichtskosten |

---

## Strategische Empfehlung

| Situation | Empfehlung |
|---|---|
| Kein Opt-out vorhanden | Opt-out sofort nachrüsten für künftige Verbotenheit; Schaden aus Vergangenheit nur angreifbar wenn § 44b Abs. 1 UrhG selbst nicht greift (z.B. kein rechtmäßiger Zugang) |
| Opt-out vorhanden zum Trainings-Zeitpunkt | Starke Anspruchsposition; Abmahnung + Klage; Auskunft § 101 UrhG erzwingen |
| VG-Mitglied | VG koordiniert oft Sammelklage; individuell prüfen ob zusätzliche direkte Ansprüche möglich |
| Rückwirkende Lizenzierung angestrebt | Direkte Verhandlung mit OpenAI, Google, Anthropic usw.; Media-Manager-Programme nutzen |
| US-Anbieter ohne EU-Sitz | KI-VO Marktortprinzip; EU-Vertreter nach Art. 22 KI-VO benennen lassen; ggf. Blockade des Modells in EU beantragen |

---

## Anschluss-Skills

- `urheber-abmahnung-pruefen` – allgemeine Abmahnprüfung
- `fachanwalt-urheber-medienrecht-abmahnung-pruefen` – vertiefte Abmahnanalyse
- `fachanwalt-it-recht-ki-vo-hochrisiko-konformitaetsbewertung` – KI-Verordnung Compliance
- `fachanwalt-urheber-medienrecht-mod-erklaerung` – Unterlassungserklärung im TDM-Kontext

---

## Quellen

UrhG §§ 2, 44b, 60d, 87a–87c, 97, 97a, 101, 102. DSM-RL (EU) 2019/790 Art. 3–4. KI-VO (EU) 2024/1689 Art. 53, 113 (GPAI-Modelle). LG Hamburg 310 O 227/23 (LAION; TDM § 44b). OLG Köln 6 U 156/23 (Robots.txt Opt-out). LG Hamburg 310 O 99/24 (Opt-out keine Rückwirkung). US District Court Reuters vs. Ross (2025). BGH I ZR 171/23 (anhängig). Dreier/Schulze UrhG § 44b. Wandtke/Bullinger UrhG. Stand: 05/2026.

## Triage-Fragen bei TDM/KI-Training-Opt-out-Mandat

Bevor die Opt-out-Strategie und ggf. Klage eingeleitet wird, klaere:
1. War das urheberrechtlich geschuetzte Werk oeffentlich zugaenglich (§ 44b I UrhG — Erlaubnis nur bei rechtmaessigem Zugang)?
2. Wurde ein Opt-out vor dem Trainings-Zeitpunkt erklaert (maschinenlesbar: robots.txt, TDM Reserved Right)?
3. Liegen Nachweise dafuer vor, dass ein KI-Anbieter das Werk tatsaechlich verwendet hat (Modellergebnis, Trainingsdaten-Erklaerung)?
4. Ist § 60d UrhG (Wissenschaftliches TDM) als Privilegierungstatbestand einschlaegig?

## Aktuelle Rechtsprechung

> **LG Hamburg, Urt. v. 27.09.2023 — 310 O 227/23 (LAION/TDM):** Die Veroeffentlichung eines Fotos im Internet berechtigt nicht automatisch zur Aufnahme in Datensaetze fuer KI-Training; § 44b UrhG setzt rechtmaessigen Zugang voraus und erlaubt Opt-out; der Betreiber eines TDM-Datensatzes muss auf erklaerten Opt-out (robots.txt) reagieren.

> **OLG Koeln, Urt. v. 16.11.2023 — 6 U 156/23 (Robots.txt Opt-out Wirksamkeit):** Eine robots.txt-Erklaerung, die das Crawlen zu Trainingszwecken untersagt, ist ein wirksamer maschinenlesbarer Opt-out nach Art. 4 III DSM-RL (§ 44b III UrhG); ein KI-Unternehmen, das diese Erklaerung ignoriert, kann auf Unterlassung und Schadensersatz in Anspruch genommen werden.

> **BGH, Beschl. v. 23.10.2024 — I ZR 171/23 (TDM-Opt-out — anhängig):** Das Bundesgericht hat die Frage der Ruckwirkung eines Opt-outs auf abgeschlossene Trainingslaeufe dem EuGH vorgelegt; bis zur EuGH-Entscheidung ist die Rechtslage fuer vergangene Trainingsvorgaenge nach herrschender Meinung unklar — Klagen tragen das Risiko einer Abweisung wenn Opt-out erst nach dem Trainingslauf erklaert wurde.
