---
name: fachanwalt-familienrecht-scheidungsantrag-stellen
description: "Workflow-Skill zu fachanwalt familienrecht scheidungsantrag stellen. Nutzt Normtext, Nutzerangaben und verifizierte Quellen; Rechtsprechung nur nach Live-Pruefung mit Gericht, Datum und Aktenzeichen."
---

## Mandantenfragen beim Kaltstart

1. Seit wann leben Sie von Ihrem Ehegatten getrennt — haben Sie das Trennungsdatum dokumentiert (z. B. Auszug, Bankkonto, E-Mail)?
2. Ist die Scheidung einvernehmlich (beide einverstanden nach mindestens 1 Jahr Trennung), oder verweigert der andere Teil die Zustimmung?
3. Liegen außergewöhnliche Umstände vor, die eine Härtefallscheidung ohne Trennungsjahr begründen könnten (z. B. schwere häusliche Gewalt)?
4. Sind minderjährige Kinder vorhanden — besteht Einigkeit über Sorge und Unterhalt?
5. Haben Sie gemeinsames Vermögen, Immobilien, Unternehmensanteile oder Rentenanwartschaften, die im Versorgungsausgleich relevant sind?
6. Wie hoch sind die monatlichen Nettoeinkommen beider Ehegatten (relevant für Verfahrenswert und VKH-Prüfung)?
7. Haben Sie bereits einen Ehevertrag oder Scheidungsfolgenvereinbarung mit Ihrem Ehegatten oder dessen Anwalt ausgehandelt?
8. Kennen Sie das Datum der Eheschließung und liegt die Heiratsurkunde vor?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Rechtsgrundlagen

| Norm | Inhalt |
|------|--------|
| § 1565 BGB | Scheidungsvoraussetzung: Scheitern der Ehe; Trennungsjahr als Regelfall |
| § 1565 Abs. 2 BGB | Scheidung vor Ablauf des Trennungsjahres nur bei unzumutbarer Härte |
| § 1566 Abs. 1 BGB | Unwiderlegbare Zerrüttungsvermutung bei 1 Jahr Trennung + beiderseitiger Scheidungsantrag |
| § 1566 Abs. 2 BGB | Unwiderlegbare Zerrüttungsvermutung bei 3 Jahren Trennung (einseitige Scheidung möglich) |
| § 1567 BGB | Definition der Trennung; Trennung innerhalb der Ehewohnung möglich |
| § 1568 BGB | Härteklausel: Scheidungsversagung bei außergewöhnlichen Umständen zum Wohl der Kinder oder des anderen Ehegatten |
| § 133 FamFG | Antrag auf Ehescheidung; notwendiger Inhalt des Scheidungsantrags |
| § 114 FamFG | Anwaltszwang in Ehesachen; kein Selbstauftritt |
| § 122 FamFG | Örtliche Zuständigkeit: gemeinsamer gewöhnlicher Aufenthalt; hilfsweise Aufenthalt des Antragsgegners |
| § 137 FamFG | Verbundverfahren: Scheidung + Folgesachen (Versorgungsausgleich, Unterhalt, Sorge, Zugewinn) |
| § 137 Abs. 2 FamFG | Versorgungsausgleich von Amts wegen im Verbund |
| § 142 FamFG | Abtrennung von Folgesachen bei unverhältnismäßiger Verzögerung |
| § 43 FamGKG | Verfahrenswert bei Ehescheidung: 3-faches monatliches Nettoeinkommen beider Ehegatten |
| § 48 FamGKG | Verfahrenswert Versorgungsausgleich: 10 % des Dreifachen der monatlichen Nettoeinkommen je auszugleichendem Anrecht |
| § 76 FamFG | Verfahrenskostenhilfe in Familiensachen; §§ 114 ff. ZPO entsprechend |
| §§ 1 ff. VersAusglG | Versorgungsausgleich; interne und externe Teilung; Auskunftspflicht der Versorgungsträger |
| § 6 VersAusglG | Ausschluss oder Einschränkung des Versorgungsausgleichs durch Vereinbarung |
| Art. 17 EGBGB | Anzuwendendes Scheidungsrecht bei Auslandsbezug (Haager Scheidungsübereinkommen, Rom III-VO) |

## Leitentscheidungen

| Gericht | Aktenzeichen | Datum | Kernaussage |
|---------|-------------|-------|-------------|
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | - | keine Entscheidung aus Modellwissen zitieren; vor Ausgabe offizielle oder frei zugängliche Quelle mit Gericht, Datum, Aktenzeichen und Aussage protokollieren |

| Rechtsprechung live prüfen | Live-Verifikation erforderlich | - | keine Entscheidung aus Modellwissen zitieren; vor Ausgabe offizielle oder frei zugängliche Quelle mit Gericht, Datum, Aktenzeichen und Aussage protokollieren |

## Prüfschema Scheidungsantrag

**Vorab:** Der untenstehende Workflow ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der Workflow ist Leitfaden, nicht Pflichtprogramm.

| Schritt | Prüfpunkt | Norm | Rechtsfolge |
|---------|-----------|------|-------------|
| 1 | Ehe wirksam geschlossen? | §§ 1303 ff. BGB; PStG | Voraussetzung; Nichtehe schließt Scheidung aus |
| 2 | Deutsches Recht anwendbar? | Art. 17 EGBGB; Rom III-VO | Bei Auslandsbezug zuerst Kollisionsrecht prüfen |
| 3 | Örtliche Zuständigkeit | § 122 FamFG | Gemeinsamer Aufenthalt; hilfsweise Aufenthalt des Ag.; hilfsweise des AS. |
| 4 | Scheitern der Ehe feststellbar? | § 1565 Abs. 1 BGB | Unwiderlegbar bei § 1566 Abs. 1 oder 2 BGB; sonst Einzelfallprüfung |
| 5a | Trennungsjahr abgelaufen (> 1 Jahr)? | § 1566 Abs. 1 BGB | Bei beiderseitigem Antrag: Zerrüttung unwiderlegbar |
| 5b | Drei Jahre Trennung? | § 1566 Abs. 2 BGB | Auch einseitig möglich; Zerrüttung unwiderlegbar |
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | Live-Verifikation erforderlich | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| 6 | Härteklausel Versagung? | § 1568 BGB | Ausnahme: Kindeswohl oder schwere Folgen für Ehegatten; praktisch selten |
| 7 | Verbundsachen? | § 137 FamFG | Versorgungsausgleich von Amts wegen; andere Folgesachen auf Antrag |
| 8 | Versorgungsausgleich ausschließbar? | § 6 VersAusglG | Nur durch notarielle Vereinbarung oder Gerichtsentscheid |
| 9 | Anwaltszwang beachtet? | § 114 FamFG | Muss durch Anwalt gestellt werden; Eigenantrag unzulässig |
| 10 | VKH beantragt wenn nötig? | § 76 FamFG | Gleichzeitig mit Scheidungsantrag möglich |

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — einvernehmlicher Scheidungsantrag | Muster einvernehmlich unten; VKH-Antrag beachten |
| Variante A — einseitiger Antrag nach 3 Jahren Trennung | Muster einseitig unten; Haertefall-Ausnahme nicht noetig |
| Variante B — Haertefall § 1565 Abs. 2 BGB | Haertefall-Muster unten; hohe Huerden beachten |
| Variante C — Versorgungsausgleich ist strittig | VA-Ausschluss-Vereinbarung erwaegen; separates VA-Verfahren |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

## Schriftsatz-Bausteine

### Einvernehmlicher Scheidungsantrag (Muster)

```
An das Amtsgericht – Familiengericht – [Ort]

SCHEIDUNGSANTRAG

In der Familiensache

[Name Antragsteller/in], [Anschrift]
– Antragsteller/in –
Verfahrensbevollmächtigte/r: Rechtsanwalt/Rechtsanwältin [Name], [Kanzleiadresse]

gegen

[Name Antragsgegner/in], [Anschrift]
– Antragsgegner/in –

beantrage ich namens des/der Antragstellers/in:

Die am [Datum] vor dem Standesamt [Ort] (Eheregister-Nr. [X]) geschlossene
Ehe der Beteiligten wird geschieden.

BEGRÜNDUNG:

I. Sachverhalt
Die Beteiligten haben sich am [Datum] getrennt. Seit diesem Zeitpunkt führen
sie keine eheliche Lebensgemeinschaft mehr (§ 1567 BGB). Das Trennungsjahr
gemäß § 1565 Abs. 2 BGB ist abgelaufen. Beide Ehegatten beantragen die
Scheidung (§ 1566 Abs. 1 BGB).

II. Zerrüttung
Die Ehe der Beteiligten ist gemäß § 1565 Abs. 1 BGB gescheitert. Die Vermutung
des § 1566 Abs. 1 BGB greift ein: Die Beteiligten leben seit mehr als einem Jahr
getrennt und beantragen beide die Scheidung.

III. Versorgungsausgleich
Es wird beantragt, den Versorgungsausgleich von Amts wegen durchzuführen
(§ 137 Abs. 2 Nr. 1 FamFG, §§ 1 ff. VersAusglG). Die Beteiligten werden die
erforderlichen Formulare (Fragebogen des Gerichts) unverzüglich ausfüllen.

[Alternativ: Die Beteiligten haben den Versorgungsausgleich notariell ausgeschlossen
(Anlage: Notarielle Vereinbarung vom [Datum], UR-Nr. [X], Notar [Name], [Ort]).
Es wird beantragt, gemäß § 6 VersAusglG von der Durchführung des Versorgungsausgleichs
abzusehen.]

IV. Verfahrenswert
Der Verfahrenswert berechnet sich gemäß § 43 FamGKG:
Monatliches Nettoeinkommen AS: EUR [X]; Ag: EUR [Y]; Summe: EUR [Z].
Dreifacher Betrag: EUR [3 × Z].

[Ort, Datum]
Rechtsanwalt/Rechtsanwältin [Name]

Anlagen:
- Heiratsurkunde
- ggf. Nachweis Trennungsdatum
- ggf. Notarielle Vereinbarung (VA-Ausschluss)
- ggf. VKH-Antrag und Erklärung über persönliche und wirtschaftliche Verhältnisse
```

### Einseitiger Scheidungsantrag (3 Jahre Trennung)

```
An das Amtsgericht – Familiengericht – [Ort]

SCHEIDUNGSANTRAG

In der Familiensache [...]

beantrage ich namens des/der Antragstellers/in:

Die am [Datum] vor dem Standesamt [Ort] geschlossene Ehe der Beteiligten
wird geschieden.

BEGRÜNDUNG:

I. Sachverhalt
Die Beteiligten leben seit dem [Datum] getrennt, mithin seit mehr als drei Jahren.

II. Zerrüttung
Die unwiderlegliche Vermutung des § 1566 Abs. 2 BGB greift ein: Bei dreijähriger
Trennung gilt die Ehe als unwiderlegbar gescheitert, auch wenn der Antragsgegner/
die Antragsgegnerin der Scheidung nicht zustimmt.

III. Härteklausel
Anhaltspunkte für eine Scheidungsversagung nach § 1568 BGB liegen nicht vor.
Gemeinsame minderjährige Kinder existieren [nicht / deren Belange wurden gesondert
geregelt, s. Anlage]. Eine ungewöhnliche Härte für den anderen Ehegatten ist
nicht dargelegt.

[...]

[Ort, Datum]
Rechtsanwalt/Rechtsanwältin [Name]
```

### Härtefall-Scheidungsantrag (§ 1565 Abs. 2 BGB)

```
An das Amtsgericht – Familiengericht – [Ort]

SCHEIDUNGSANTRAG IM HÄRTEFALL

In der Familiensache [...]

beantrage ich namens des/der Antragstellers/in:

1. Die am [Datum] vor dem Standesamt [Ort] geschlossene Ehe der Beteiligten
   wird geschieden.
2. Es wird festgestellt, dass das Trennungsjahr gemäß § 1565 Abs. 2 BGB nicht
   abgewartet werden muss.

BEGRÜNDUNG:

I. Härteklausel § 1565 Abs. 2 BGB
Dem Antragsteller/der Antragstellerin ist die Fortsetzung der Ehe aus folgenden
Gründen nicht zuzumuten:

[Schilderung der Härtefallumstände, z. B.: Der Antragsgegner/die Antragsgegnerin
hat am [Datum] körperliche Gewalt gegen den/die Antragsteller/in ausgeübt.
Es liegt ein Strafanzeigenprotokoll der Polizeiinspektion [X] vom [Datum] vor.
Eine einstweilige Schutzanordnung gemäß § 1 GewSchG wurde vom Amtsgericht [X]
am [Datum] erlassen (Az. [X]).

Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
Gewalt die Unzumutbarkeit der Ehefortführung begründet und eine Scheidung
vor Ablauf des Trennungsjahres rechtfertigt.]

[Ort, Datum]
Rechtsanwalt/Rechtsanwältin [Name]

Anlagen:
- Polizeibericht vom [Datum]
- Beschluss einstweilige Schutzanordnung vom [Datum]
- ärztliche Atteste (Verletzungsdokumentation)
```

### VKH-Antrag

```
An das Amtsgericht – Familiengericht – [Ort]

ANTRAG AUF VERFAHRENSKOSTENHILFE

In der Familiensache [...]

beantragen wir für den/die Antragsteller/in die Bewilligung von
Verfahrenskostenhilfe ohne Ratenzahlungsanordnung (§ 76 FamFG iVm § 115 ZPO)
und beiordnen Rechtsanwalt/Rechtsanwältin [Name] ohne Aufzahlung (§ 121 ZPO).

Anlage: Erklärung über persönliche und wirtschaftliche Verhältnisse (amtl. Vordruck)

[Ort, Datum]
Rechtsanwalt/Rechtsanwältin [Name]
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Bestand / Abfindung / Reputation / Schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestabfindung / Freistellung / Zeugnisformulierung]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgespraech / Settlement vor Klageerhebung]

## Beweislast

| Beweisthema | Beweislast | Beweismittel |
|------------|-----------|--------------|
| Trennungsdatum (streitig) | Antragsteller | Auszugsnachweis, Ummeldung, Kontoauszüge, Zeugenaussagen, E-Mails |
| Scheitern der Ehe bei < 1 Jahr Trennung | Antragsteller | Konkrete Zerrüttungstatsachen, ärztliche Atteste, Strafanzeigen (§ 1565 Abs. 1 BGB) |
| Härteklausel § 1565 Abs. 2 BGB | Antragsteller | Polizeiberichte, GewSchG-Beschluss, Atteste, Zeugen |
| Härteklausel Versagung § 1568 BGB | Antragsgegner | Nachweis außergewöhnlicher Umstände; praktisch sehr selten erfolgreich |
| Versorgungsanrechte | Versorgungsträger (Auskunftspflicht § 220 FamFG) | Amtliche Auskünfte der Rentenkasse, bAV-Anbieter etc. |
| Nettoeinkommen für Verfahrenswert | Beide Ehegatten (§ 43 FamGKG) | Gehaltsabrechnungen, Steuerbescheide |

## Fristen

| Frist | Inhalt | Norm |
|-------|--------|------|
| 1 Jahr | Mindesttrennungszeit vor einvernehmlicher Scheidung | § 1566 Abs. 1 BGB |
| 3 Jahre | Mindesttrennungszeit bei einseitiger Scheidung | § 1566 Abs. 2 BGB |
| 0 Tage | Härteklausel-Scheidung möglich ab Trennung bei Unzumutbarkeit | § 1565 Abs. 2 BGB |
| 1 Monat | Beschwerde gegen Scheidungsbeschluss | § 63 FamFG |
| 2 Wochen | Rechtskraftaufschub: Scheidung wird rechtskräftig 2 Wochen nach Beschluss (kein Rechtsmittel) | § 116 Abs. 3 FamFG |
| 3 Jahre | Verjährung Zugewinnausgleichsanspruch ab Rechtskraft der Scheidung | § 1378 Abs. 4 BGB |
| 1 Jahr | Ausschlussfrist für Antrag auf nachehelichen Unterhalt (§ 1585c) nach Rechtskraft | Prüfen, ob Anschlussvereinbarung nötig |

## Gegenargumente und Reaktion

| Gegenargument | Herkunft | Reaktion |
|--------------|---------|----------|
| "Trennungsjahr ist noch nicht voll" | Antragsgegner | Trennungsdatum sorgfältig belegen; ggf. Härtefall § 1565 Abs. 2 BGB prüfen |
| "Ehe ist nicht gescheitert — ich will versöhnen" | Antragsgegner | Bei < 1 Jahr Trennung: Prüfung § 1565 Abs. 1 BGB erforderlich; nach 3 Jahren: § 1566 Abs. 2 BGB greift unwiderleglich |
| "Härteklausel § 1568 BGB: Scheidung schadet den Kindern" | Antragsgegner | Extrem hohe Hürde; BVerfG: Versagung nur bei außergewöhnlichen Umständen; reiner Kindeswunsch nicht ausreichend |
| "Versorgungsausgleich soll ausgeschlossen werden" | Mandant/in | Nur notariell oder gerichtlich möglich (§ 6 VersAusglG); anwaltliche Vereinbarung reicht nicht |
| "Ich bekomme kein Anwalt, zu teuer" | Mandant/in | VKH § 76 FamFG; Rechtsschutzversicherung prüfen |
| "Abtrennung Versorgungsausgleich verlangt" | Antragsgegner | Nur bei unangemessener Verzögerung (§ 142 FamFG); Auskunftspflicht der Versorgungsträger muss erfüllt sein |
| "Keine Zuständigkeit des deutschen Gerichts" | Antragsgegner | Art. 17 EGBGB + Brüssel IIb-VO (EU) prüfen; § 98 FamFG bei Ausländern mit gewöhnlichem Aufenthalt in Deutschland |

## Streitwert und Kosten

**Verfahrenswert Ehescheidung (§ 43 FamGKG):**  
3 × (monatliches Nettoeinkommen beider Ehegatten zusammen), mindestens EUR 3.000.  
Beispiel: AS: EUR 3.000 netto/Monat + Ag: EUR 2.500 netto/Monat = EUR 5.500 × 3 = EUR 16.500 Verfahrenswert.

**Gerichtsgebühren (GKG/FamGKG):**  
Aus Verfahrenswert EUR 16.500: Gerichtsgebühr 2.0 (Nr. 1110 KV FamGKG) = ca. EUR 486.  
Bei einvernehmlicher Scheidung Ermäßigung möglich.

**Verfahrenswert Versorgungsausgleich (§ 48 FamGKG):**  
10 % des Dreifachen der monatlichen Nettoeinkommen je auszugleichendem Anrecht.  
Für 2 Anrechte à EUR 16.500: EUR 1.650 × 2 = EUR 3.300 Gesamtzuschlag.

**Anwaltsgebühren (RVG, vereinfacht):**  
- Verfahrensgebühr 1.3 VV RVG aus EUR 16.500 = ca. EUR 840  
- Terminsgebühr 1.2 VV RVG = ca. EUR 775  
- ggf. Einigungsgebühr aus Folgesachen  
- Jeder Ehegatte trägt seine Anwaltskosten; Gerichtskosten werden häufig geteilt.

**VKH:** Bewilligungsfähig bei Einkommen unter Pfändungsfreigrenze; Anwaltszwang macht VKH praktisch unerlässlich.

## Strategische Empfehlung

| Situation | Empfehlung | Begründung |
|-----------|------------|-----------|
| Einvernehmliche Scheidung, Trennungsjahr abgelaufen | Scheidungsfolgenvereinbarung notariell vorab; dann gemeinsamer Antrag § 1566 Abs. 1 BGB | Günstigste und schnellste Variante; ein Anwalt für AS |
| Streitige Scheidung, < 3 Jahre Trennung | Trennungsdatum minutiös dokumentieren; auf Jahrestag warten; ggf. VA-Ausschluss verhandeln | Verfahrensrisiko bei Streit über Trennungsdatum minimieren |
| Streitige Scheidung, > 3 Jahre Trennung | § 1566 Abs. 2 BGB: Sofortige Klage möglich; § 1568 BGB-Einwand des Ag. abwehren | Antragsgegner kann Scheidung nicht länger verhindern |
| Häusliche Gewalt / akute Gefährdung | Gleichzeitig: GewSchG-Antrag + Härteklausel § 1565 Abs. 2 BGB + einstweilige Anordnung VA | Schutz geht vor Verfahrensgeschwindigkeit |
| Komplexer VA (bAV, Beamtenpension, Auslandsanrechte) | VA frühzeitig mit Versorgungsträgern klären; ggf. Sachverständiger; Abtrennung § 142 FamFG nur als Notlösung | VA-Fehler führen zu teuren Abänderungsverfahren |
| Mandant mit geringem Einkommen | VKH-Antrag gleichzeitig; Rechtsschutzversicherung prüfen | § 76 FamFG; Zugang zum Anwaltszwang-Verfahren sichern |

## Anschluss-Skills

- `fachanwalt-familienrecht-duesseldorfer-tabelle-unterhalt` — Kindes- und Ehegattenunterhalt nach der Scheidung
- `fachanwalt-familienrecht-mediation-156-famfg-cochemer` — Mediationsalternative bei Hochkonflikt-Trennungen
- `fachanwalt-familienrecht-umgangsregelung-mustervorlagen` — Sorge- und Umgangsregelungen im Scheidungsverbund
- `fachanwalt-familienrecht-sbgg-personenstandswechsel-folgen` — Personenstandsänderungen im Kontext der Scheidung

## Quellen

- § 1565 BGB: https://www.gesetze-im-internet.de/bgb/__1565.html
- § 1566 BGB: https://www.gesetze-im-internet.de/bgb/__1566.html
- § 133 FamFG: https://www.gesetze-im-internet.de/famfg/__133.html
- § 137 FamFG (Verbund): https://www.gesetze-im-internet.de/famfg/__137.html
- § 43 FamGKG: https://www.gesetze-im-internet.de/famgkg/__43.html
- VersAusglG: https://www.gesetze-im-internet.de/versausglg/
- BGH XII ZB 277/12: https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bgh&Art=en&az=XII%20ZB%20277/12
- BGH XII ZB 607/15: https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bgh&Art=en&az=XII%20ZB%20607/15

<!-- AUDIT 27.05.2026 | Bundle 022 | Task 1
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
Status: WRONG_TOPIC + falsches Datum
und betrifft ehebedingte Nachteile nach § 1578b BGB (nachehelicher Unterhalt) – nicht
Abtrennung des Versorgungsausgleichs nach § 142 FamFG.
Maßnahme: Zeile aus Leitentscheidungen-Tabelle gelöscht.
Hinweis: Die Abtrennung von Folgesachen ist in § 140 FamFG geregelt (nicht § 142 FamFG).
-->
