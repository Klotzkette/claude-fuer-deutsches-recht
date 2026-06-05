---
name: inso-kongruente-deckung-rechtsfolge
description: "Inso Kongruente Deckung Rechtsfolge: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Inso Kongruente Deckung Rechtsfolge

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Inso Kongruente Deckung Rechtsfolge** im Plugin Bereicherungs- und Anfechtungsrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `inso-kongruente-deckung-130` | Kongruente Deckungsanfechtung nach § 130 InsO prüfen: geschuldete Sicherung oder Befriedigung, Drei-Monats-Zeitraum vor Insolvenzantrag oder Handlung nach Antrag, Zahlungsunfähigkeit, Kenntnis oder zwingende Kenntnisumstände, Margensicherheiten-Ausnahme, Abgrenzung zu § 131 und § 142 InsO. Output: beleggestützte Anspruchsmatrix. |
| `inso-rechtsfolge-rueckgewaehr-143-bis-147` | Rechtsfolgen der Insolvenzanfechtung nach §§ 143-147 InsO bestimmen: Rückgewähr zur Masse, Geldschuld und Zinsen, Entreicherung bei unentgeltlicher Leistung, Gegenleistung § 144, Rechtsnachfolger § 145, Verjährung § 146 und Rechtshandlungen nach Eröffnung § 147. Output: Anspruchsberechnung und Schreiben. |
| `inso-unentgeltliche-leistung-134` | Anfechtung unentgeltlicher Leistungen in der Insolvenz nach § 134 InsO prüfen: vier Jahre vor Insolvenzantrag. Normen: § 134 InsO. Prüfraster: Unentgeltlichkeitsbegriff, Ausnahmen Anstandsschenkungen, nahestehende Personen, Fristberechnung. Output: Prüfergebnis Anfechtbarkeit unentgeltliche Leistung. Abgrenzung: nicht § 133 InsO (Vorsatzanfechtung zehn Jahre). |
| `inso-unmittelbar-nachteilige-rechtshandlungen-132` | Anfechtung unmittelbar nachteiliger Rechtshandlungen nach § 132 InsO prüfen: Benachteiligung in den letzten drei Monaten. Normen: §§ 132 129 InsO. Prüfraster: unmittelbare Nachteiligkeit, Kausalität, Drei-Monats-Frist, Abgrenzung § 129 InsO. Output: Prüfergebnis Anfechtbarkeit unmittelbar nachteilige Rechtshandlung. Abgrenzung: Auffangnorm zu §§ 130 131 InsO. |

## Arbeitsweg

Im Plugin Bereicherungs- und Anfechtungsrecht gilt für **Inso Kongruente Deckung Rechtsfolge**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `inso-kongruente-deckung-130`

**Fokus:** Kongruente Deckungsanfechtung nach § 130 InsO prüfen: geschuldete Sicherung oder Befriedigung, Drei-Monats-Zeitraum vor Insolvenzantrag oder Handlung nach Antrag, Zahlungsunfähigkeit, Kenntnis oder zwingende Kenntnisumstände, Margensicherheiten-Ausnahme, Abgrenzung zu § 131 und § 142 InsO. Output: beleggestützte Anspruchsmatrix.

# Kongruente Deckung — § 130 InsO

## Triage — kläre vor der Prüfung

1. Konnte der Gläubiger die Sicherung oder Befriedigung **in dieser Art und zu dieser Zeit** beanspruchen?
2. Wurde die Handlung in den letzten drei Monaten vor dem Eröffnungsantrag oder nach dem Antrag vorgenommen?
3. War der Schuldner zum Zeitpunkt der Handlung zahlungsunfähig?
4. Kannte der Gläubiger die Zahlungsunfähigkeit oder den Eröffnungsantrag?
5. Kann die Kenntnis aus Umständen abgeleitet werden, die zwingend auf Zahlungsunfähigkeit oder Antrag schließen lassen?
6. Greift die Margensicherheiten-Ausnahme in § 130 Abs. 1 S. 2 InsO?
7. Ist § 142 InsO als Bargeschäftsverteidigung zu prüfen?

## Zentrale Normen

§ 130 InsO — § 129 InsO — § 131 InsO — § 138 InsO — § 140 InsO — § 142 InsO — § 143 InsO — § 17 InsO.

## Gesetzliche Struktur

§ 130 Abs. 1 InsO betrifft kongruente Deckungen: Der Gläubiger erhält eine Sicherung oder Befriedigung, die er beanspruchen konnte.

| Fall | Zeitraum | Zusatzvoraussetzung |
|---|---|---|
| § 130 Abs. 1 S. 1 Nr. 1 InsO | letzte drei Monate vor Eröffnungsantrag | Schuldner zahlungsunfähig und Gläubiger kannte Zahlungsunfähigkeit |
| § 130 Abs. 1 S. 1 Nr. 2 InsO | nach Eröffnungsantrag | Gläubiger kannte Zahlungsunfähigkeit oder Eröffnungsantrag |
| § 130 Abs. 2 InsO | Kenntnisersatz | Kenntnis zwingender Umstände genügt |
| § 130 Abs. 3 InsO | nahestehende Person | Kenntnis wird vermutet |

Alte Merksätze, nach denen im letzten Monat keine Kenntnis erforderlich sei, gehören zu § 131 InsO und dürfen nicht auf § 130 InsO übertragen werden.

## Abgrenzung

| Frage | Wenn ja | Wenn nein |
|---|---|---|
| Leistung war geschuldet und fällig? | § 130 InsO möglich | § 131 InsO prüfen |
| Sicherung war vertraglich vorab vereinbart? | eher § 130 InsO | nachträgliche Sicherheit oft § 131 InsO |
| Austausch gleichwertig und unmittelbar? | § 142 InsO prüfen | Deckungsanfechtung bleibt offen |
| längerer Zeitraum oder Vorsatzindizien? | § 133 InsO zusätzlich prüfen | bei drei Monaten bleiben §§ 130/131 Hauptpfad |

## Kenntnisprüfung

Die Kenntnis darf nicht behauptet werden. Sie braucht konkrete Belege:

- Mahnungen mit offener Zahlungsstockung.
- Rücklastschriften, Pfändungen, Vollstreckungsversuche.
- Zahlungsvereinbarungen und Stundungsbitten.
- interne Vermerke des Gläubigers über Krise oder drohenden Forderungsausfall.
- öffentliche Insolvenzantragsinformationen, soweit wirklich bekannt.

Keine automatische Kenntnis folgt aus normalem Zahlungsverzug, einzelnen Mahnungen oder bloßer Branchenkenntnis.

## Prüfschema

1. Rechtshandlung und Zeitpunkt nach § 140 InsO bestimmen.
2. Kongruenz feststellen.
3. Zeitraum: letzte drei Monate vor Antrag oder nach Antrag.
4. Zahlungsunfähigkeit zum Zeitpunkt der Handlung belegen.
5. Kenntnis oder zwingende Umstände beim Gläubiger belegen.
6. Nahestehende Person und Vermutung nach § 130 Abs. 3 InsO prüfen.
7. § 142 InsO und § 133 InsO als Gegen- oder Zusatzprüfung markieren.

## Output-Template

**Prüfung § 130 InsO — Kongruente Deckung**

| Merkmal | Ergebnis | Beleg |
|---|---|---|
| Rechtshandlung | [...] | [...] |
| Zeitpunkt nach § 140 InsO | [...] | [...] |
| Kongruente Sicherung/Befriedigung | ja/nein | [...] |
| Zeitraum | vor Antrag/nach Antrag | [...] |
| Zahlungsunfähigkeit | ja/nein/offen | [...] |
| Kenntnis oder zwingende Umstände | ja/nein/offen | [...] |
| § 142 InsO | greift/greift nicht/offen | [...] |

**Ergebnis:** § 130 InsO [naheliegend / nicht naheliegend / offen wegen Beleglücke].

---

Hinweis: Keine Rechtsberatung. § 130 InsO nie ohne Kenntnisprüfung bejahen; die Kenntnis gehört zum Tatbestand.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `inso-rechtsfolge-rueckgewaehr-143-bis-147`

**Fokus:** Rechtsfolgen der Insolvenzanfechtung nach §§ 143-147 InsO bestimmen: Rückgewähr zur Masse, Geldschuld und Zinsen, Entreicherung bei unentgeltlicher Leistung, Gegenleistung § 144, Rechtsnachfolger § 145, Verjährung § 146 und Rechtshandlungen nach Eröffnung § 147. Output: Anspruchsberechnung und Schreiben.

# Rechtsfolge Insolvenzanfechtung — §§ 143 bis 147 InsO

## Triage — kläre vor der Prüfung

1. Welcher Anfechtungstatbestand ist erfüllt?
2. Was wurde aus dem Schuldnervermögen veräußert, weggegeben oder aufgegeben?
3. Ist Rückgewähr in Natur möglich oder geht es um Geld-/Wertersatz?
4. Wurde eine Gegenleistung erbracht?
5. Ist ein Rechtsnachfolger betroffen?
6. Ist Verjährung nach § 146 InsO in Verbindung mit den BGB-Regeln zu prüfen?
7. Wurde die Handlung erst nach Verfahrenseröffnung wirksam und fällt unter § 147 InsO?

## Zentrale Normen

§ 143 InsO — § 144 InsO — § 145 InsO — § 146 InsO — § 147 InsO — §§ 195, 199, 203 ff. BGB — §§ 129-135 InsO.

## Gesetzliche Struktur

| Norm | Inhalt |
|---|---|
| § 143 Abs. 1 InsO | Rückgewähr dessen, was aus dem Schuldnervermögen veräußert, weggegeben oder aufgegeben wurde |
| § 143 Abs. 1 S. 3 InsO | Geldschuld nur bei Verzug oder nach § 291 BGB zu verzinsen; keine weitergehende Nutzungsherausgabe |
| § 143 Abs. 2 InsO | Empfänger unentgeltlicher Leistung haftet nur nach Bereicherung, außer bei Kenntnis oder Kennenmüssen der Gläubigerbenachteiligung |
| § 143 Abs. 3 InsO | besondere Erstattungspflicht bei § 135 Abs. 2 InsO |
| § 144 InsO | Forderung des Anfechtungsgegners lebt nach Rückgewähr wieder auf; Gegenleistung nur begrenzt aus der Masse |
| § 145 InsO | Anfechtung gegen Rechtsnachfolger |
| § 146 InsO | Verjährung nach den Regeln der regelmäßigen Verjährung des BGB |
| § 147 InsO | bestimmte Rechtshandlungen nach Verfahrenseröffnung können nach Anfechtungsregeln behandelt werden |

## Wichtige Korrekturen

- § 145 InsO betrifft Rechtsnachfolger, nicht § 147 InsO.
- § 146 InsO enthält keine einfache Sonderregel "zehn Jahre ab Rechtshandlung". Er verweist auf die regelmäßige Verjährung nach dem BGB. Anfechtungsfristen und Verjährung bleiben getrennt.
- Zinsen laufen nicht automatisch ab Insolvenzeröffnung oder Rechtshandlung; § 143 Abs. 1 S. 3 InsO verlangt Verzug oder § 291 BGB.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Prüfschema

1. Tatbestand und Betrag je Rechtshandlung festhalten.
2. Rückgewährgegenstand bestimmen.
3. Naturalrestitution oder Geld-/Wertersatz.
4. Zinsen nur bei Verzug oder Rechtshängigkeit.
5. Gegenleistung und Wiederaufleben der Forderung nach § 144 InsO.
6. Rechtsnachfolger nach § 145 InsO.
7. Verjährung nach § 146 InsO und BGB.
8. Nach-Eröffnungs-Konstellation nach § 147 InsO.

## Output-Template

**Prüfung §§ 143 ff. InsO — Rechtsfolge**

| Merkmal | Ergebnis | Beleg |
|---|---|---|
| Anfechtungstatbestand | [...] | [...] |
| Rückgewährgegenstand | [...] | [...] |
| Betrag oder Verkehrswert | [...] EUR | [...] |
| Zinsbeginn | Verzug/§ 291 BGB/nein | [...] |
| Gegenleistung § 144 InsO | [...] | [...] |
| Rechtsnachfolger § 145 InsO | ja/nein | [...] |
| Verjährung § 146 InsO | offen/verjährt/unklar | [...] |

**Ergebnis:** Rückgewähranspruch der Masse i.H.v. [...] EUR [durchsetzbar / offen / nicht durchsetzbar].

---

Hinweis: Keine Rechtsberatung. Rechtsfolge nie ohne Betrag, Zinsgrund und Gegenleistungsprüfung ausgeben.

## 3. `inso-unentgeltliche-leistung-134`

**Fokus:** Anfechtung unentgeltlicher Leistungen in der Insolvenz nach § 134 InsO prüfen: vier Jahre vor Insolvenzantrag. Normen: § 134 InsO. Prüfraster: Unentgeltlichkeitsbegriff, Ausnahmen Anstandsschenkungen, nahestehende Personen, Fristberechnung. Output: Prüfergebnis Anfechtbarkeit unentgeltliche Leistung. Abgrenzung: nicht § 133 InsO (Vorsatzanfechtung zehn Jahre).

# Unentgeltliche Leistung — § 134 InsO

## Triage — kläre vor der Prüfung

1. Hat der Schuldner eine Zuwendung ohne angemessene Gegenleistung erbracht (vollständig oder teilweise unentgeltlich)?
2. Liegt die Handlung innerhalb der Vier-Jahres-Frist vor dem Insolvenzantrag?
3. Handelt es sich um ein gebräuchliches Gelegenheitsgeschenk oder eine sittliche Pflicht (Ausnahme § 134 Abs. 2 InsO)?
4. Gibt es eine teilweise Gegenleistung, sodass nur der unentgeltliche Teil zu prüfen ist?
5. Kommt statt § 134 InsO ein spezieller Tatbestand in Betracht, insbesondere § 135 InsO bei Gesellschafterdarlehen?

## Zentrale Normen

§ 134 InsO (unentgeltliche Leistung, 4-Jahres-Frist) — § 135 InsO (Gesellschafterdarlehen und gleichgestellte Forderungen) — § 138 InsO (nahestehende Personen) — § 129 InsO (Grundtatbestand) — § 143 InsO (Rückgewähr) — § 516 BGB (Schenkungsvertrag) — §§ 812 ff. BGB (Bereicherungsrecht, Konkurrenz)

## Rechtsprechung

Hinweis für diesen Auditstand: § 134 InsO wird hier vorrangig aus dem aktuellen Gesetzestext geprüft. Unsichere Einzelfallzitate sind nicht erforderlich; bei konkreter Prozessverwendung sind Rechtsprechungsnachweise fallbezogen nachzuziehen.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Obersatz

Anfechtbar sind nach § 134 Abs. 1 InsO unentgeltliche Leistungen des Schuldners, es sei denn, sie sind früher als vier Jahre vor Insolvenzantrag vorgenommen worden.

## Tatbestandsmerkmale

### 1. Unentgeltliche Leistung

**Vollständige Unentgeltlichkeit:** Schenkung, unentgeltliche Sicherungsübereignung, Schulderlass ohne Gegenleistung.

**Teilweise Unentgeltlichkeit:** Gemischte Schenkung — Anfechtung nur für den unentgeltlichen Teil.

**Maßstab:** Objektiver Wertvergleich; keine oder erheblich hinter dem Wert zurückbleibende Gegenleistung.

### 2. Vier-Jahres-Frist

Die Leistung muss innerhalb von vier Jahren vor dem Insolvenzantrag vorgenommen worden sein.

### 3. Kein Verschulden erforderlich

§ 134 InsO setzt weder Benachteiligungsvorsatz noch Kenntnis des Anfechtungsgegners voraus.

## Ausnahmen § 134 Abs. 2 InsO

Nicht anfechtbar:
- Gebräuchliche Gelegenheitsgeschenke (Geburtstag, Weihnachten) von angemessenem Wert.
- Leistungen in Erfüllung einer sittlichen Pflicht.

## Typische Anwendungsfälle

- Grundstücksübertragung an Familienangehörige kurz vor Insolvenz.
- Schenkung erheblicher Barmittel an Lebenspartner.
- Verzicht auf Forderungen ohne Gegenleistung.
- Sicherheitsübereignung ohne zugrundeliegende gesicherte Forderung.

## Prüfschema

1. Unentgeltlich (ganz oder teilweise)?
2. Frist: innerhalb von vier Jahren vor Insolvenzantrag?
3. Ausnahme § 134 Abs. 2 InsO (Gelegenheitsgeschenk, sittliche Pflicht)?
4. Bei Gesellschafterdarlehen oder gleichgestellter Forderung → § 135 InsO prüfen.

## Output-Template

**Prüfung § 134 InsO — Unentgeltliche Leistung**

Sachverhalt (kurz): [...]

| Merkmal | Ergebnis |
|---|---|
| Unentgeltlichkeit (objektiv) | vollständig / teilweise / nein |
| Wert der Gegenleistung (falls vorhanden) | [...] EUR |
| Zeitraum vor Insolvenzantrag | [...] Jahre → innerhalb 4 Jahre? ja / nein |
| Ausnahme § 134 Abs. 2 InsO | nein / ja: [...] |
| Gesellschafterdarlehen oder gleichgestellte Forderung | ja → § 135 InsO prüfen |

**Ergebnis:** Anfechtung nach § 134 Abs. 1 InsO [begründet / unbegründet]. Rückgewährpflicht: [...].

---

Hinweis: Keine Rechtsberatung. Mechanische Prüfung anhand vom Nutzer behaupteter Tatsachen. Falsche Normwahl oder unvollständiger Sachverhalt kann das Ergebnis vollständig entwerten.

## 4. `inso-unmittelbar-nachteilige-rechtshandlungen-132`

**Fokus:** Anfechtung unmittelbar nachteiliger Rechtshandlungen nach § 132 InsO prüfen: Benachteiligung in den letzten drei Monaten. Normen: §§ 132 129 InsO. Prüfraster: unmittelbare Nachteiligkeit, Kausalität, Drei-Monats-Frist, Abgrenzung § 129 InsO. Output: Prüfergebnis Anfechtbarkeit unmittelbar nachteilige Rechtshandlung. Abgrenzung: Auffangnorm zu §§ 130 131 InsO.

# Unmittelbar nachteilige Rechtshandlungen — § 132 InsO

## Triage — kläre vor der Prüfung

1. Handelt es sich um eine Deckungshandlung zugunsten eines Insolvenzgläubigers (→ §§ 130, 131 InsO vorrangig), oder um eine eigenständig benachteiligende Rechtshandlung?
2. Wurde die Rechtshandlung in den letzten drei Monaten vor Insolvenzantrag vorgenommen?
3. War der Schuldner zu diesem Zeitpunkt bereits zahlungsunfähig (§ 17 InsO)?
4. Kannte der andere Teil die Zahlungsunfähigkeit oder den Eröffnungsantrag?
5. Liegt eine besonders günstige Gegenleistung vor, die § 132 InsO ausschließt (marktgerechter Preis)?

## Zentrale Normen

§ 132 InsO (unmittelbar nachteilige Rechtshandlung) — § 129 InsO (Grundtatbestand) — § 130 InsO (Kenntnisregeln entsprechend) — § 131 InsO (inkongruente Deckung) — § 133 InsO (Vorsatzanfechtung) — § 17 InsO (Zahlungsunfähigkeit) — § 143 InsO (Rückgewähr)

## Rechtsprechung

Hinweis für diesen Auditstand: § 132 InsO wird hier bewusst am Gesetzestext geführt. Unsichere Altzitate wurden nicht als tragende Arbeitsregel übernommen.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Obersatz

Anfechtbar ist nach § 132 Abs. 1 InsO ein Rechtsgeschäft des Schuldners, das die Insolvenzgläubiger unmittelbar benachteiligt, wenn es entweder in den letzten drei Monaten vor dem Eröffnungsantrag bei Zahlungsunfähigkeit und Kenntnis des anderen Teils vorgenommen wurde oder nach dem Eröffnungsantrag bei Kenntnis der Zahlungsunfähigkeit oder des Antrags.

## Abgrenzung zu §§ 130, 131 InsO

§ 132 InsO greift bei Rechtshandlungen, die keine Deckung eines Gläubigeranspruchs darstellen, sondern bei denen die Schädigung des Gläubigervermögens die unmittelbare Folge der Rechtshandlung selbst ist.

## Tatbestandsmerkmale

### 1. Unmittelbare Nachteiligkeit

Die Rechtshandlung selbst (ohne Zwischenschritte) muss das Schuldnervermögen zum Nachteil der Gläubiger vermindern.

**Beispiele:**
- Verkauf von Vermögensgegenständen unter dem Verkehrswert.
- Aufnahme eines Kredits mit überhöhten Zinsen kurz vor Insolvenz.
- Abschluss langfristiger Verträge zu unausgewogenen Bedingungen.

### 2. Zeitraum

Entweder letzte drei Monate vor Antrag oder Handlung nach Eröffnungsantrag.

### 3. Zahlungsunfähigkeit (§ 17 InsO)

Der Schuldner war zum Zeitpunkt der Handlung bereits zahlungsunfähig.

### 4. Kenntnis

§ 132 Abs. 3 InsO verweist auf § 130 Abs. 2 und 3 InsO. Kenntnis zwingender Umstände und die Vermutung bei nahestehenden Personen sind mitzudenken.

## Praktische Bedeutung

§ 132 InsO ist subsidiär gegenüber §§ 130, 131, 133, 134 InsO und wird selten eigenständig angewendet.

## Prüfschema

1. Deckungshandlung ausschließen (kein § 130/131 InsO)?
2. Unmittelbare Nachteiligkeit festgestellt?
3. Dreimonatsfrist?
4. Zahlungsunfähigkeit und Kenntnis nachgewiesen?
5. Nach Antrag: Kenntnis von Zahlungsunfähigkeit oder Antrag?

## Output-Template

**Prüfung § 132 InsO — Unmittelbar nachteilige Rechtshandlung**

Sachverhalt (kurz): [...]

| Merkmal | Ergebnis |
|---|---|
| §§ 130/131 InsO (Deckung) ausgeschlossen | ja / nein |
| Unmittelbare Nachteiligkeit | ja: [...] / nein |
| Zeitraum vor Insolvenzantrag | [...] Monate → ≤3 Monate? ja / nein |
| Zahlungsunfähigkeit § 17 InsO | ja / nein |
| Kenntnis des anderen Teils | ja / nein / offen |

**Ergebnis:** Anfechtung nach § 132 Abs. 1 Nr. [...] InsO [begründet / unbegründet].

---

Hinweis: Keine Rechtsberatung. Mechanische Prüfung anhand vom Nutzer behaupteter Tatsachen. Falsche Normwahl oder unvollständiger Sachverhalt kann das Ergebnis vollständig entwerten.
