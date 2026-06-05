---
name: verkehrsowi-haertefall-fahrverbot
description: "Haertefall Fahrverbot: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Haertefall Fahrverbot

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Haertefall Fahrverbot** im Plugin Verkehrs-OWi-Verteidigung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `verkehrsowi-haertefall-fahrverbot` | Haertefall-Argumentation gegen Fahrverbot nach § 25 StVG: Mandant ist beruflich auf Führerschein angewiesen. Normen: § 25 StVG (Fahrverbot), § 25 Abs. 2a StVG (Wirkungszeitpunkt verschiebbar), § 17 Abs. 3 OWiG (Geldbusse erhoehen als Alternative). Prüfraster: Berufsbedingte Angewiesenheit, Existenzgefaehrdung, OLG-Rspr Haertefall-Prüfung, Absehen vs. Verzoegerung Fahrverbot. Output Haertefall-Begründung, Antrag Absehen vom Fahrverbot oder Erhoehung Geldbusse. Abgrenzung: Punkte Flensburg siehe verkehrsowi-punkte-fahrverbot-flensburg; HV-Vorbereitung siehe verkehrsowi-hauptverhandlung-amtsgericht. |
| `verkehrsowi-hauptverhandlung-amtsgericht` | Hauptverhandlung in OWi-Sache am Amtsgericht vorbereiten und führen: Termin nach Einspruch gegen Bußgeldbescheid. Normen: § 71 OWiG (HV nach StPO), § 77 OWiG (Beweisanträge), § 55 OWiG (Schweigerecht), § 17 OWiG (Strafmass). Prüfraster: Beweisanträge (Sachverständiger, Zeugen), Einlassung oder Schweigen, Strafmass-Erwaegungen, Abwesenheitsmöglichkeit § 74 OWiG. Output HV-Vorbereitungs-Checkliste, Beweisantrags-Entwuerfe. Abgrenzung: Rechtsbeschwerde danach siehe verkehrsowi-rechtsbeschwerde; Haertefall vor HV siehe verkehrsowi-haertefall-fahrverbot. |
| `verkehrsowi-mandantenkommunikation` | Mandantenkommunikation im OWi-Mandat: Mandant versteht Verfahren nicht und benoetigt verstaendliche Erklärung. Normen: BRAO § 43a (Beratungspflicht), § 67 OWiG, § 25 StVG. Prüfraster: Erstgespraeche-Leitfaden, Anhoerungsbogen-Empfehlung, Fahrverbot-Erklärung, Punktestand-Abfrage, Terminvorbereitung HV. Output Mandantenbrief-Template, Erklärungsbausteine, Kommunikations-Protokoll. Abgrenzung: Inhaltliche Strategie siehe verkehrsowi-kommandocenter; Anhoerung siehe verkehrsowi-anhoerung-bußgeldbescheid. |

## Arbeitsweg

Im Plugin Verkehrs-OWi-Verteidigung gilt für **Haertefall Fahrverbot**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `verkehrsowi-haertefall-fahrverbot`

**Fokus:** Haertefall-Argumentation gegen Fahrverbot nach § 25 StVG: Mandant ist beruflich auf Führerschein angewiesen. Normen: § 25 StVG (Fahrverbot), § 25 Abs. 2a StVG (Wirkungszeitpunkt verschiebbar), § 17 Abs. 3 OWiG (Geldbusse erhoehen als Alternative). Prüfraster: Berufsbedingte Angewiesenheit, Existenzgefaehrdung, OLG-Rspr Haertefall-Prüfung, Absehen vs. Verzoegerung Fahrverbot. Output Haertefall-Begründung, Antrag Absehen vom Fahrverbot oder Erhoehung Geldbusse. Abgrenzung: Punkte Flensburg siehe verkehrsowi-punkte-fahrverbot-flensburg; HV-Vorbereitung siehe verkehrsowi-hauptverhandlung-amtsgericht.

# Haertefall-Argumentation beim Fahrverbot — § 25 StVG

## Triage zu Beginn

1. **Wie hoch ist das Fahrverbot?** — § 25 StVG: 1 bis 3 Monate; Regelfahrverbot im BKat (Bussgeldkatalog) bei bestimmten Verstaessen.
2. **Ist der Mandant beruflich auf das Fahrzeug angewiesen?** — LKW-Fahrer, Vertreter, Pflegekraft, Taxi/Uber — Haertefall-Argumentation.
3. **Existenzgefaehrdung nachweisbar?** — Drohende Kuendigung, Arbeitslosenunterstuetzung nicht ausreichend, Eigentuemer Kleinstunternehmen.
4. **Gibt es mildernde Tatumstaende?** — Dringende Notsituation, techisches Versagen, minimale Ueberschreitung.
5. **Vier-Monats-Frist nutzbar?** — § 25 Abs. 2a StVG: Betroffener kann Beginn des Fahrverbots bis zu 4 Monate nach Rechtskraft hinauszogern (vorteilhaft fuer Urlaubszeit).

## Zentrale Normen

- **§ 25 Abs. 1 StVG** — Fahrverbot im OWi-Verfahren: 1 bis 3 Monate
- **§ 25 Abs. 2a StVG** — Vier-Monats-Frist: Betroffener kann Antritt bis 4 Monate nach Rechtskraft hinausschieben
- **§ 4 Abs. 1 BKatV** — Regelfahrverbot bei bestimmten Grenzwerten; kann unterschritten werden wenn Haertefall vorliegt
- **§ 17 Abs. 3 OWiG** — Geldbusse als Alternative; Erhoehung moeglich statt Fahrverbot
- **§ 44 StGB** — Fahrverbot als strafrechtliche Nebenstrafe (andere Regelung als § 25 StVG)

## Aktuelle Rechtsprechung

- OLG Frankfurt a.M., Beschl. v. 18.3.2021 - 2 Ss OWi 148/21 (NZV 2021, 448 — Volltext über openjur.de oder offene Justizdatenbank Hessen verifizieren): Berufsbedingte Angewiesenheit ist typischerweise kein Haertefall; der Betroffene muss zusaetzlich darlegen, dass keine Alternative zum Selbstfahren besteht und Existenzgefaehrdung nachweisbar ist.
- Weitere OLG-Linien (Bayerisches Oberstes Landesgericht, OLG Hamm, OLG Düsseldorf u.a.): konkrete Aktenzeichen vor Versand in openjur.de oder offenen Landesjustiz-Datenbanken aufrufen.
- BVerfG zum Verhältnismäßigkeitsgrundsatz bei Fahrverbot: laufende Linie; Aktenzeichen vor Versand in bundesverfassungsgericht.de verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Haertefall-Argumentation — Checkliste

```
BERUFLICHE ANGEWIESENHEIT (schwache Argumentation allein):
□ Berufsbezeichnung (LKW-Fahrer, Handelsvertreter, etc.)
□ Fahrzeug notwendig fuer Berufsausuebung
□ Keine Moeglichkeit oeff. Nahverkehr zu nutzen (Nachweis?)

EXISTENZGEFAEHRDUNG (staerkere Argumentation):
□ Drohende Kuendigung durch Arbeitgeber (Bescheinigung!)
□ Arbeitnehmerarbeitgeber-Bescheinigung: "Fahrverbot = Kuendigung"
□ Selbststaendiger: Einnahmenausfall konkret beziffert (BWA)
□ Minijobber / Sozialhilfebeziehende: Existenzminimum betroffen
□ Keine Alternative vorhanden (keine Mitfahrer, kein Taxi zu vertretbaren Kosten)

MILDERNDE TATUMSTAENDE:
□ Erstverstos (kein Vorvergehen im BZR Flensburg)
□ Minimale Geschwindigkeitsueberschreitung an der Grenze zum Fahrverbot
□ Besondere Notlage zur Tatzeit (medizinischer Notfall, etc.)
□ Ueberlange Verfahrensdauer (> 2 Jahre seit Tat)

VIER-MONATS-FRIST (§ 25 Abs. 2a StVG):
□ Antrag auf Verschiebung des Fristbeginns (z.B. auf Urlaubszeit)
□ Zustimmung des Gerichts einholen
□ Zeitplanung mit Mandant abstimmen
```

## Schritt-fuer-Schritt-Workflow

1. **Mandant ueber realistische Chancen aufklaeren** — Haertefall ist selten anerkannt.
2. **Beweise sammeln:** Arbeitgeber-Bescheinigung, Einkommensnachweis, Alternativennachweis (OEPNV nicht erreichbar).
3. **Vier-Monats-Frist als Alternative:** Wenn Haertefall nicht durchsetzbar, Fristverschiebung nach § 25 Abs. 2a StVG beantragen.
4. **Absehen vom Fahrverbot beantragen:** Statt Fahrverbot erhoehte Geldbusse; § 17 Abs. 3 OWiG i.V.m. § 4 Abs. 4 BKatV.
5. **In der HV:** Haertefall-Argumente konkret und mit Belegen vortragen; pauschale Berufsnotwendigkeit genuegt nicht.

## Harte Leitplanken

- Haertefall ohne Belege wird nicht anerkannt — Bescheinigungen und Nachweise zwingend.
- Vier-Monats-Frist immer als Rueckfall-Option vorbereiten.
- Mandant realistisch informieren — Fahrverbot ist die Regel, Ausnahme ist die Ausnahme.
- Anwaltliche Endkontrolle bei Haertefall-Argumentation.

## 2. `verkehrsowi-hauptverhandlung-amtsgericht`

**Fokus:** Hauptverhandlung in OWi-Sache am Amtsgericht vorbereiten und führen: Termin nach Einspruch gegen Bußgeldbescheid. Normen: § 71 OWiG (HV nach StPO), § 77 OWiG (Beweisanträge), § 55 OWiG (Schweigerecht), § 17 OWiG (Strafmass). Prüfraster: Beweisanträge (Sachverständiger, Zeugen), Einlassung oder Schweigen, Strafmass-Erwaegungen, Abwesenheitsmöglichkeit § 74 OWiG. Output HV-Vorbereitungs-Checkliste, Beweisantrags-Entwuerfe. Abgrenzung: Rechtsbeschwerde danach siehe verkehrsowi-rechtsbeschwerde; Haertefall vor HV siehe verkehrsowi-haertefall-fahrverbot.

# Hauptverhandlung OWi am Amtsgericht

## Triage zu Beginn — Checkliste vor der HV

1. **Erscheinungspflicht?** — § 73 Abs. 1 OWiG: Betroffener kann von Erscheinungspflicht entbunden werden; auf Antrag. Verteidiger kann allein erscheinen (§ 73 Abs. 3 OWiG).
2. **Beweisantraege formuliert?** — § 77 OWiG: Beweisantraege moegen vorbereitet sein; konkretes Beweisthema + Beweismittel.
3. **Einlassung oder Schweigen?** — § 55 OWiG: Schweigen neutral; Einlassung nur wenn strategisch vorteilhaft.
4. **Verstaendigungsangebot gemacht?** — Informelle Gespraech mit Staatsanwalt oder Richter vor HV.
5. **Rechtsbeschwerde vorbereitbar?** — § 79 OWiG: Nur bei Geldbusse > 250 EUR oder Fahrverbot; Revisionsbegrenzt auf Rechtsfehler.
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Zentrale Normen

- **§ 71 OWiG** — Hauptverhandlung: gilt StPO entsprechend soweit OWiG nichts anderes regelt
- **§ 73 OWiG** — Erscheinungspflicht: Absehen, Entbindung; Verteidiger kann allein erscheinen
- **§ 74 OWiG** — Verwerfung des Einspruchs bei unentschuldigtem Ausbleiben
- **§ 77 OWiG** — Beweisantraege: Ablehnungsgruende eng; Sachverstaendigenrecht
- **§ 17 OWiG** — Geldbusse: Zubemassung nach Schwere und Einkommen
- **§ 79 OWiG** — Rechtsbeschwerde: zulaessig bei Geldbusse > 250 EUR oder Fahrverbot
- **§ 80 OWiG** — Zulassung der Rechtsbeschwerde bei grundsaetzlicher Bedeutung

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Vorbererungs-Checkliste (1 Woche vor HV)

```
□ Messakte vollstaendig ausgewertet?
□ Sachverstaendigenantrag formuliert (wenn noetig)?
□ Einlassung oder Schweigen entschieden?
□ Haertefall-Argument (Fahrverbot) vorbereitet?
□ Entbindungsantrag (§ 73 OWiG) gestellt?
□ Verstaendigung mit Gericht/StA sondiert?
□ Mandant ueber HV-Ablauf informiert?
□ Rechtsbeschwerde-Strategie vorgedacht?
```

## Ablauf-Schema HV OWi


**Vorab:** Der untenstehende ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der ist Leitfaden, nicht Pflichtprogramm.

```
1. Aufruf der Sache (§ 243 StPO i.V.m. § 71 OWiG)
2. Feststellung Erscheinen aller Beteiligten
3. Ggf. Einspruchsverwerfungsantrag der StA? → widersprechen
4. Verlesung Anklage (Tatvorwurf)
5. Belehrung Betroffener § 55 OWiG (Schweigerecht)
6. Einlassung oder Schweigen
7. Beweisaufnahme:
 a) Zeugen (Polizeibeamte)
 b) Urkundsbeweis (Messprotokoll, Eichschein)
 c) Sachverstaendiger (wenn beantragt und zugelassen)
8. Schlussvortrag Staatsanwaltschaft
9. Plaedoyer Verteidiger
10. Letztes Wort Betroffener
11. Urteil (Freispruch / Geldbusse / Fahrverbot)
```

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — OWi-Hauptverhandlung am Amtsgericht fuehren | Plaedoyer nach Schema; Template unten |
| Variante A — Mandant will Einspruch zuruecknehmen vor HV | Einspruchsruecknahme statt HV; Bussgeldbescheid wird rechtskraeftig |
| Variante B — Freispruch unrealistisch Strafmass im Fokus | Strafzumessungs-Plaedoyer; Fahrverpflichtung pruefen |
| Variante C — Rechtsbeschwerde bereits im Blick | Verteidigungsstrategie HV auf Rechtsbeschwerde ausrichten; Protokollfuehrung beachten |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.


## Schriftsatzkern Plaedoyer OWi

```
Sehr geehrtes Gericht,

[Zusammenfassung der Beweisaufnahme aus Sicht der Verteidigung]

Die Messung ist aus folgenden Gruenden anzuzweifeln:
[Konkreter Angriffspunkt 1]
[Konkreter Angriffspunkt 2]

Strafzumessung: Bei Verurteilung beantrage ich Absehen vom
Fahrverbot / Herabsetzung der Geldbusse, weil:
[Haertefall / mildernde Umstaende / Erstverstos]

Antrag: Freispruch / Einstellung / Geldbusse von [X] EUR
ohne Fahrverbot.
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Durchsetzung des Anspruchs / Vergleich / Reputationsschutz / schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestforderung / Zeitrahmen / Formerfordernis]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgesprach / Einigung vor Fristablauf]

Schlussabsatz Variante A (kooperativ):
Wir regen eine guetliche Einigung an und stehen fuer ein klaerenden Gesprach zur Verfuegung. Eine einvernehmliche Loesung erspart beiden Seiten Zeit und Kosten.

Schlussabsatz Variante B (formal-streng):
Eine aussergerichtliche Einigung kommt nur in Betracht wenn die Gegenseite innerhalb von [X] Tagen einen akzeptablen Vorschlag unterbreitet. Anderenfalls werden wir alle rechtlichen Schritte einleiten.


## Harte Leitplanken

- Sachverstaendigenantrag vor Schluss der Beweisaufnahme stellen.
- Letztes Wort des Betroffenen niemals vergessen.
- Entbindungsantrag rechtzeitig (vor HV) stellen.
- Rechtsbeschwerde nur bei Geldbusse > 250 EUR oder Fahrverbot; sonst kein Rechtsmittel.
- Anwaltliche Endkontrolle bei Plaedoyer und Antraegen.

## 3. `verkehrsowi-mandantenkommunikation`

**Fokus:** Mandantenkommunikation im OWi-Mandat: Mandant versteht Verfahren nicht und benoetigt verstaendliche Erklärung. Normen: BRAO § 43a (Beratungspflicht), § 67 OWiG, § 25 StVG. Prüfraster: Erstgespraeche-Leitfaden, Anhoerungsbogen-Empfehlung, Fahrverbot-Erklärung, Punktestand-Abfrage, Terminvorbereitung HV. Output Mandantenbrief-Template, Erklärungsbausteine, Kommunikations-Protokoll. Abgrenzung: Inhaltliche Strategie siehe verkehrsowi-kommandocenter; Anhoerung siehe verkehrsowi-anhoerung-bußgeldbescheid.

# Mandantenkommunikation im OWi-Mandat

## Triage-Erstgespraeches-Leitfaden

**Was zuerst klaeren:**

1. **Zustellungsdatum Bescheid?** — Frist sofort berechnen, Mandant informieren.
2. **Fahrzeug auf Mandanten-Namen?** — Halter = OWi-Adressat; wenn nicht Fahrzeugfuehrer: Fahreridentifikation.
3. **Aktueller Punktestand?** — Hat der Mandant eine FAER-Auskunft (§ 30 StVG)?
4. **Berufliche Folgen eines Fahrverbots?** — Existenzgefaehrdung? Arbeitgeber-Bescheinigung moeglich?
5. **Was ist das Ziel?** — Freispruch, Einstellung, Fahrverbot-Vermeidung, Tagessatz-Reduzierung?

## Kommentar-Warteraum Erstgespraeches-Sprache

- Nicht: "Die Messtoleranz wurde korrekt abgezogen" → Besser: "Von Ihrer gemessenen Geschwindigkeit wird ein Sicherheitsabzug von 3 km/h (bzw. 3%) vorgenommen — das ist gesetzlich vorgeschrieben."
- Nicht: "§ 67 OWiG-Frist" → Besser: "Sie haben ab dem Tag, an dem Sie den Bescheid bekommen haben, 2 Wochen Zeit, Einspruch einzulegen."
- Nicht: "Standardisiertes Messverfahren nach BGH" → Besser: "Das Gericht akzeptiert diese Art der Messung grundsaetzlich, aber wir pruefen trotzdem ob technische Fehler vorlagen."

## Zentrale Normen

- **§ 55 OWiG** — Schweigerecht des Betroffenen; keine Pflicht zur Aussage
- **§ 67 OWiG** — Einspruchsfrist 2 Wochen
- **§ 25 StVG** — Fahrverbot
- **§ 4 StVG** — Punkte in Flensburg

## Mandantenhinweis-Template nach Einspruchseinlegung

**Adressat:** Mandant — Tonfall: verstaendlich-erklaerend

```
Sehr geehrte/r Frau/Herr [NAME],

ich bestaedige, dass ich fristgerecht Einspruch gegen den
Bussgeldescheid vom [DATUM] eingelegt habe.

Wie es weitergeht:
Die Behörde prueft nun die Akte. Danach wird entweder:
a) das Verfahren eingestellt (kein Bussgeldbescheid mehr),
b) ein Verhandlungstermin am Amtsgericht angesetzt, oder
c) die Behörde den Bescheid bestaetigt (dann gehen wir
 weiter zum Amtsgericht).

Was Sie tun koennen:
- Bitte sprechen Sie NICHT mit Polizei oder Behörden
 ueber den Vorfall ohne mich zu kontaktieren.
- Wenn Sie neue Unterlagen erhalten, bitte sofort weiterleiten.
- Haben Sie ein Fahrtenbuch oder Notizbuch, das den Tatvorwurf
 betrifft? Bitte aufbewahren.

Kostenschaetzung: [RVG-Gebuehren]

Mit freundlichen Gruessen
[KANZLEI]
```

## Template Anhoerungsbogen-Empfehlung

**Adressat:** Mandant — Tonfall: klar und eindeutig

```
Sehr geehrte/r Frau/Herr [NAME],

Sie haben einen Anhoerungsbogen erhalten. Meine Empfehlung:

BITTE DEN BOGEN NICHT AUSFULLEN UND NICHT UNTERSCHREIBEN.

Begruendung: Sie muessen nicht antworten. Das Schweigen wird
Ihnen NICHT nachteilig ausgelegt. Unterschreiben Sie den Bogen
nur, wenn er explizit nur Ihre Personalien (Name, Adresse) abfragt
— und auch dann nur nach meiner Ruecksprache.

Falls Sie sich bereits gaeussert haben: Bitte informieren Sie
mich sofort.

Mit freundlichen Gruessen [KANZLEI]
```

## Schritt-fuer-Schritt-Mandantenbetreuung

1. **Erstgespraech:** Sachverhalt aufnehmen, Frist sofort notieren, Vollmacht einholen.
2. **Einspruch einlegen:** Mandant sofort informieren.
3. **Akteneinsicht:** Ergebnis in verstaendlicher Sprache erklaeren.
4. **Strategie besprechen:** Erfolgsaussichten realistisch einschaetzen.
5. **Vor der HV:** Mandant ueber Ablauf informieren, Erscheinungspflicht klaeren.
6. **Nach der HV / Urteil:** Ergebnis erklaeren, Rechtsmitteloptionen darlegen.

## Harte Leitplanken

- Mandant immer ueber Kosten informieren (RVG-Gebuehren schriftlich).
- Erfolgsaussichten realistisch kommunizieren — keine Garantien.
- Fristen immer in Mandantenkommunikation vermerken.
- Anwaltliche Endkontrolle bei Mandantenkorrespondenz.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
