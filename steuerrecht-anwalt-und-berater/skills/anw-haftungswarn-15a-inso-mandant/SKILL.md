---
name: anw-haftungswarn-15a-inso-mandant
description: "Anwaltliche Beratung und Warnschreiben an GmbH-Geschaeftsfuehrung bei festgestellter Insolvenzreife nach §§ 17 19 InsO. Anwendungsfall GmbH-GF spricht beim Anwalt vor weil Steuerberater Krisensignale gemeldet hat. Antragspflicht § 15a InsO drei Wochen Zahlungsunfaehigkeit sechs Wochen Ueberschuldung. Strafbarkeit Insolvenzverschleppung § 15a Abs. 4 InsO. GF-Haftung § 15b InsO nach SanInsFoG. Output Beratungsdokumentation Warnschreiben mit Belehrung Eingangsbestaetigung. Abgrenzung zu stb-warnschreiben-krisensignale Steuerberater-Pflichthinweis und anw-insolvenzreife-pruefung-17-19-inso Gutachten."
---

# Haftungswarn an GmbH-Geschäftsführung bei Insolvenzreife (Anwaltliche Sicht)

## Zweck

Anwaltliche Beratung und schriftliche Dokumentation gegenüber der Geschäftsführung einer GmbH/UG, wenn die Mandantin (häufig nach Hinweis des Steuerberaters via `stb-warnschreiben-krisensignale`) bei dem Anwalt vorspricht und sich Insolvenzreife verdichtet. Anders als der Steuerberater **darf und muss** der Anwalt die rechtliche Beurteilung der Antragspflicht treffen — und sich dabei selbst absichern.

> ℹ️ **Rollenabgrenzung zu `anw-insolvenzreife-pruefung-17-19-inso`:** Dieser Skill ist **präventiv-belehrend** — erstellt das schriftliche Warn-/Belehrungsschreiben an den GF nach erfolgter Reife-Analyse. Die vorgeschaltete **analytische** Prüfung der Insolvenzreife (§§ 17, 19 InsO Subsumtion, Beweiswürdigung) leistet `anw-insolvenzreife-pruefung-17-19-inso`. Standardablauf: erst `anw-insolvenzreife-pruefung-17-19-inso` (Diagnose), dann dieser Skill (Mandantenbelehrung + Dokumentation).

> Dieses Schreiben dokumentiert die Beratungsleistung. Es ist **kein** anwaltliches Mahn-/Warnschreiben gegen den Mandanten, sondern eine schriftliche **Belehrung über die Antragspflicht und ihre Folgen** mit Bestätigung der Beratung — Pflicht aus § 11 BORA und Selbstschutz vor späteren Regressansprüchen.

## Eingaben

- Mandant (GmbH/UG, vollständige Firma, HRB, Stammkapital, GF mit Vertretungsbefugnis)
- Anlass (Steuerberater-Hinweis, eigener Anstoß, Gesellschafterbeschluss)
- Datenlage: Bilanz, BWA, Liquidität — vom Steuerberater oder GF übergeben
- Bisherige interne Krisenmaßnahmen (§ 102 StaRUG-Dokumentation)
- Rangrücktritte, Patronate, Bürgschaften bekannt?
- Mandatsumfang: nur Beratung Antragspflicht oder Vollmandat Sanierung/Antrag?
- Vergütungsvereinbarung (Stundenhonorar, Pauschale, RVG nach Wert)

## Rechtlicher Rahmen

### Primärnormen

- **§ 15a Abs. 1 Satz 1 InsO** — Insolvenzantragspflicht. Zahlungsunfähigkeit (§ 17 InsO) → drei Wochen. Überschuldung (§ 19 InsO) → sechs Wochen.
- **§ 15a Abs. 4 InsO** — Strafbarkeit Insolvenzverschleppung (Freiheitsstrafe bis 3 Jahre / Geldstrafe; bei Fahrlässigkeit bis 1 Jahr).
- **§ 15b InsO** — Zahlungsverbote nach Insolvenzreife. Geschäftsführerhaftung gegen die Gesellschaft (löste § 64 GmbHG a.F. ab; SanInsFoG, 1.1.2021).
- **§ 17 InsO** — Zahlungsunfähigkeit (BGH IX ZR 123/04 — 10-%-Schwelle, 3-Wochen-Horizont).
- **§ 19 InsO** — Überschuldung (zweistufig: rechnerisch und Fortbestehensprognose; vgl. `stb-ueberschuldungspruefung-19-inso`).
- **§ 18 InsO** — Drohende Zahlungsunfähigkeit (24-Monats-Horizont; Antragsrecht, keine Pflicht — Zugangstor StaRUG).
- **§ 102 StaRUG** — Krisenfrüherkennungspflicht GF; ergänzt § 91 Abs. 2 AktG analog auf alle haftungsbeschränkten Gesellschaften.
- **§ 64 StBerG / § 43a Abs. 5 BRAO** — bei Honorarrückständen Berücksichtigung; keine Beratung ohne Vergütungsvereinbarung in Hochrisikofällen.
- **§ 826 BGB / § 823 Abs. 2 BGB i.V.m. § 15a InsO** — Außenhaftung GF gegenüber Neugläubigern bei Insolvenzverschleppung.

### Leitentscheidungen

- BGH, Urt. v. 24.5.2005 — **IX ZR 123/04**, BGHZ 163, 134 (Grundsatz Zahlungsunfähigkeit; 10-%-Schwelle, 3-Wochen-Horizont).
- BGH, Urt. v. 19.11.2019 — **II ZR 233/18**, NJW 2020, 1809 (Fortbestehensprognose § 19 II InsO).
- BGH, Urt. v. 19.12.2017 — **II ZR 88/16**, BGHZ 217, 129 (Passiva II; Substantiierungslast bestreitender GF).
- BGH, Urt. v. 6.6.1994 — **II ZR 292/91** ("Girmes"; Außenhaftung GF gegenüber Neugläubigern).
- BGH, Urt. v. 27.3.2012 — **II ZR 171/10** (Quotenschaden Altgläubiger).
- BGH, Urt. v. 4.7.2017 — **II ZR 319/15** (Beweislast Beratungsfehler des anwaltlichen Beraters).

## Vorgehen

### Schritt 1 — Sachverhalt klären

- Zahlungsunfähigkeit (§ 17 InsO) oder nur Zahlungsstockung? Liquiditätslücke berechnen (Aktiva I + II vs. Passiva I + II, BGH-Schema). Vgl. `stb-liquiditaetsvorschau-3wochen` oder `liquiditaetsplanung`.
- Überschuldung (§ 19 InsO): zweistufige Prüfung (Fortbestehensprognose + rechnerischer Status). Vgl. `stb-ueberschuldungspruefung-19-inso`.
- Drohende Zahlungsunfähigkeit (§ 18 InsO): 24-Monats-Liquidität. Wenn ja → StaRUG-Option offen, **noch keine Pflicht**, aber Strategie-Frage.

### Schritt 2 — Frist-Trigger feststellen

| Tatbestand | Frist § 15a InsO | Trigger |
|---|---|---|
| Zahlungsunfähigkeit § 17 | 3 Wochen | objektives Eintreten — nicht subjektive Kenntnis |
| Überschuldung § 19 | 6 Wochen | objektives Eintreten — nicht subjektive Kenntnis |
| Drohende Zahlungsunfähigkeit § 18 | keine Pflicht | nur Antragsrecht; StaRUG-Zugang |

Aussagen klar dokumentieren: **wann** ist die Insolvenzreife objektiv eingetreten — nicht wann sie der GF erkannt hat. Wenn umstritten, IDW-S-11-Stichtagsanalyse beauftragen.

### Schritt 3 — Optionen mit dem Mandanten besprechen

1. **Insolvenzantrag** — Regelverfahren, Eigenverwaltung (§ 270b InsO), Schutzschirm (§ 270d InsO).
2. **StaRUG-Restrukturierungsverfahren** — nur bei drohender Zahlungsunfähigkeit (§ 18 InsO), nicht bei manifester Insolvenzreife.
3. **Außergerichtliche Sanierung** — nur möglich bei kurzfristiger Stockung (< 3 Wochen) oder gesichertem Kapital-/Liquiditätszufluss.
4. **Sanierungskonzept nach IDW S 6** als Voraussetzung positiver Fortbestehensprognose.
5. **Mandatsniederlegung** bei eklatanter Insolvenzverschleppung und Weigerung des GF.

### Schritt 4 — Schriftliche Belehrung

Pflicht aus § 11 BORA (Schriftform-Pflicht bei wichtigen Mandantenhinweisen) und § 49b Abs. 5 BRAO (Belehrung über Honorarauslösung bei Mandatsumfang).

### Schritt 5 — Eigene Aktendokumentation

- Aktennotiz: Sachverhalt, Beratungsinhalt, Empfehlung, Mandantenreaktion.
- Schriftliche Belehrung samt Eingangsbestätigung.
- Folge-Schritte (Wiedervorlage; ggf. weitere Honorarvereinbarung).
- Versendung beA an Mandanten-Anwalt (sofern vorhanden) bzw. Einschreiben.

## Muster — Anwaltliches Belehrungs-/Hinweisschreiben (verkürzt)

```
[Kanzlei-Briefkopf]                                               [Datum]

PERSÖNLICH UND VERTRAULICH

[Mandant — GmbH, z. Hd. Geschaeftsfuehrer/in Name]
[Anschrift]

vorab per beA / Einschreiben mit Rueckschein

In dem Mandat [Aktenzeichen] / Beratung zur Insolvenzantragspflicht

Sehr geehrte/r Frau / Herr [Name],

ich nehme Bezug auf unsere Besprechung am [Datum] und auf die mir
ueberlassenen Unterlagen (Bilanz zum [Stichtag], BWA, SuSa,
Liquiditaetsuebersicht der Steuerkanzlei [Name]).

Nach einer ersten Pruefung des Sachverhalts ist davon auszugehen, dass
zum Zeitpunkt [Datum] [Zahlungsunfaehigkeit gemaess § 17 InsO /
Ueberschuldung gemaess § 19 Abs. 2 InsO] vorliegt. Die Einzelheiten der
rechtlichen Wuerdigung entnehmen Sie bitte dem beigefuegten Vermerk.

Daraus folgt eine **Pflicht zur Insolvenzantragstellung** gemaess
§ 15a Abs. 1 Satz 1 InsO. Die Hoechstfrist betraegt
[drei Wochen ab Eintritt der Zahlungsunfaehigkeit /
sechs Wochen ab Eintritt der Ueberschuldung].

**Risiken bei Verstoss gegen die Antragspflicht:**

1. Strafrechtliche Verantwortung nach § 15a Abs. 4 InsO
   (Freiheitsstrafe bis zu drei Jahren oder Geldstrafe; bei
   fahrlaessiger Verschleppung bis zu einem Jahr).
2. Persoenliche zivilrechtliche Haftung gegenueber der Gesellschaft
   gemaess § 15b InsO (verbotene Zahlungen nach Insolvenzreife).
3. Persoenliche Haftung gegenueber Neuglaeubigern aus § 823 Abs. 2
   BGB i.V.m. § 15a InsO bzw. § 826 BGB (Quotenschaden Altglaeubiger,
   Vertrauensschaden Neuglaeubiger; vgl. BGH II ZR 292/91).

**Empfehlung:**

Ich empfehle Ihnen mit Nachdruck:

- saemtliche an Glaeubiger gerichteten Zahlungen unverzueglich auf
  Insolvenzkonformitaet zu pruefen (vgl. § 15b InsO);
- saemtliche an die Gesellschaft eingehenden Zahlungen auf einem
  gesonderten Konto zu sammeln;
- den Insolvenzantrag innerhalb der oben genannten Frist zu stellen,
  sofern eine Sanierungsperspektive ausserhalb des Insolvenzverfahrens
  nicht zeitnah belegt werden kann;
- alternative Verfahrenswege (Eigenverwaltung § 270b InsO,
  Schutzschirm § 270d InsO, StaRUG-Restrukturierung soweit erst
  drohende Zahlungsunfaehigkeit) gegen das Regelinsolvenzverfahren
  abzuwaegen.

Ich stehe zur Mandatsuebernahme fuer das Insolvenzantragsverfahren oder
fuer ein Sanierungsverfahren auf Grundlage einer gesonderten
Verguetungsvereinbarung zur Verfuegung.

Bitte bestaetigen Sie den Eingang dieses Schreibens und teilen Sie mir
Ihre Entscheidung binnen drei Werktagen mit. Sollte ich von Ihnen keine
Reaktion erhalten, gehe ich davon aus, dass Sie meine Beratung nicht
in Anspruch nehmen wollen, und werde das Mandat in Bezug auf die
Insolvenzantragstellung niederlegen.

Mit freundlichen Gruessen
[Unterschrift]
Rechtsanwalt/-anwaeltin
```

## Risiken und Red Flags

| Konstellation | Rot | Orange | Grün |
|---|---|---|---|
| GF kennt Insolvenzreife, verweigert Antrag | Beihilfe-/Anstiftungsrisiko? Mandat niederlegen | Aufklärung erneut, schriftlich | Antrag wird gestellt |
| Keine Schriftform der Belehrung | § 11 BORA-Pflichtverstoß, Regressrisiko | mündliche Belehrung dokumentiert | beA + Einschreiben |
| Anwalt selbst zahlt Honorar aus Mandantenkonto nach Insolvenzreife | § 15b InsO-Pflichtverstoß GF, Risiko Anwaltsregress | nach Verfahrenseröffnung | Honorar vor Insolvenzreife oder als Massevorab |
| Beratung ohne Aktenlage | Sorgfaltsverstoß; Beweislastumkehr bei Schaden | bei kurzfristigem Hinweis | nach umfassender Akteneinsicht |

## Querverweise

- `stb-warnschreiben-krisensignale` — vorgelagerte StB-Warnschreiben
- `stb-ueberschuldungspruefung-19-inso` — technische Vorprüfung
- `stb-liquiditaetsvorschau-3wochen` — Liquidität § 17 InsO
- `liquiditaetsplanung` (Power-Plugin) — gerichtsfeste insolvenzrechtliche Bilanz
- `fachanwalt-insolvenz-sanierungsrecht` — bei Vollmandat zur Sanierung/Antragstellung
- `anw-selbstanzeige-371` — wenn parallel Steuer-Hinterziehungsproblematik (Selbstanzeige kann § 15b-Schutz nicht ersetzen)

## Quellen und Updates

Stand: 05/2026. SanInsFoG (§ 15b InsO statt § 64 GmbHG a.F., 1.1.2021), SanInsKG (24-Monats-Prognose § 19 InsO bis 31.12.2026) berücksichtigt. § 11 BORA-Schriftformpflicht zentral. Bei Änderung InsO/BORA aktualisieren.
