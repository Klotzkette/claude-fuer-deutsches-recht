---
name: fachanwalt-urheber-medienrecht-tdm-44b-urhg-ki-training-opt-out
description: "Text- und Data-Mining-Opt-out nach § 44b UrhG erklären wenn KI-Training mit urheberrechtlich geschützten Werken verhindert werden soll. § 44b UrhG TDM §§ 87a ff. UrhG Datenbankschutz DSA. Prüfraster: Opt-out-Erklärung Maschinenlesbarkeit Robots.txt rechtliche Wirkung Rechteinhaber. Output: Opt-out-Erklärung technische Anleitung Prüfprotokoll. Abgrenzung: nicht für allgemeine KI-Lizenzfragen."
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
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | keine Entscheidung aus Modellwissen zitieren; vor Ausgabe offizielle oder frei zugängliche Quelle mit Gericht, Datum, Aktenzeichen und Aussage protokollieren |
| Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
| US District Court NY (Reuters vs. Ross) | US District Court, 11.02.2025 | Fair Use abgelehnt: Training eines KI-Recherchetools mit Rechtsartikeln ist keine transformative Nutzung; kommerzieller Zweck schadet |
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | keine Entscheidung aus Modellwissen zitieren; vor Ausgabe offizielle oder frei zugängliche Quelle mit Gericht, Datum, Aktenzeichen und Aussage protokollieren |

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

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
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
| Rechtsprechung live prüfen | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |

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
| Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
| Rechtsprechung live prüfen | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
| Rechtsprechung live prüfen | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| "Wir sind in den USA und US-Recht gilt" | EU-Niederlassung oder Auftragsverarbeiter in EU begründet EU-Gerichtsstand; zudem: EU-Nutzer sind betroffen → Marktortprinzip |

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

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Triage-Fragen bei TDM/KI-Training-Opt-out-Mandat

Bevor die Opt-out-Strategie und ggf. Klage eingeleitet wird, klaere:
1. War das urheberrechtlich geschuetzte Werk oeffentlich zugaenglich (§ 44b I UrhG — Erlaubnis nur bei rechtmaessigem Zugang)?
2. Wurde ein Opt-out vor dem Trainings-Zeitpunkt erklaert (maschinenlesbar: robots.txt, TDM Reserved Right)?
3. Liegen Nachweise dafuer vor, dass ein KI-Anbieter das Werk tatsaechlich verwendet hat (Modellergebnis, Trainingsdaten-Erklaerung)?
4. Ist § 60d UrhG (Wissenschaftliches TDM) als Privilegierungstatbestand einschlaegig?

## Aktuelle Rechtsprechung

> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
