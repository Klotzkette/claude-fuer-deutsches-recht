---
name: 22-zustaendigkeit-amtsgericht-pruefen
description: "Sachliche und örtliche Zuständigkeit prüfen plus Anwaltszwang nach Paragraf 78 ZPO. Wohnraummietsachen stets AG Paragraf 23 Nr. 2a GVG ohne Anwaltszwang. Gewerberaum streitwertabhängig. Output Zuständigkeitsvermerk mit Norm-Anker."
---

# Zuständigkeit Amtsgericht und Anwaltszwang

## Zweck und Anwendungsfall

Dieser Skill prüft die sachliche Zuständigkeit, die örtliche Zuständigkeit und den Anwaltszwang vor jeder Klageeinreichung. Anwendungsfall ist die Bestimmung des richtigen Gerichts und der Frage, ob die Konzerngesellschaft sich selbst vertreten lassen darf oder einen Rechtsanwalt beauftragen muss.

## Bedienmodus

Arbeite für hochtrainierte Rechtsanwalts- und Notarfachangestellte, Renofas, Rechtsfachwirte und Forderungsmanagement-Spezialisten. Sie sind keine Anwälte, aber fachlich stark. Keine abgehobene Anwaltsprosa: kurze Arbeitskarten, begründete Prüffragen, kompakte Tabellen, Ampel, Lückenliste und genau eine nächste Arbeitsaktion. Juristisch schwierige Punkte werden als Eskalation markiert, nicht versteckt.

## Eingaben

- Streitgegenstand (Mietrückstand, Räumung, Mieterhöhung, Mietminderung, Betriebskosten, Kautionsrückzahlung).
- Art des Mietverhältnisses: Wohnraum oder Geschäftsraum/Gewerberaum.
- Streitwert (vorläufig).
- Lageort der Mietsache mit vollständiger Anschrift.
- Zugang zur aktuellen amtlichen Gerichts- und Geschäftsverteilung.
- Gewünschter regulärer oder digitaler Verfahrensweg und tatsächliche Kläger-/Vertretungsrolle.

## Ablauf / Checkliste

### 1. Art des Mietverhältnisses feststellen

Wohnraum oder Gewerberaum. Maßgeblich ist der vertraglich vereinbarte Nutzungszweck. Ein einheitliches Mischmietverhältnis wird nach dem überwiegenden Vertragszweck eingeordnet. Bei unklarem Schwerpunkt keine Zuständigkeit unterstellen, sondern Vertragszweck, Flächen, Entgeltanteile und tatsächliche Nutzung ermitteln und die Ampel bis zur Klärung auf Gelb setzen.

### 2. Sachliche Zuständigkeit prüfen

#### 2.1 Wohnraummietsachen

Bei Streitigkeiten über Ansprüche aus einem Mietverhältnis über Wohnraum ist nach Paragraf 23 Nr. 2a GVG ausschließlich und streitwertunabhängig das Amtsgericht zuständig. Das gilt für Mietrückstand, Räumung, Mieterhöhung, Mietminderungsstreit, Betriebskostenabrechnung und Kautionsrückzahlung. Die allgemeine Streitwertgrenze des Paragrafen 23 Nr. 1 GVG ist hier ohne Bedeutung. Beispiel: Ein Mietrückstand von 50.000 EUR aus Wohnraum bleibt sachlich Amtsgerichtssache.

#### 2.2 Gewerberaum / Geschäftsraum

Bei Geschäftsraummiete greift Paragraf 23 Nr. 2a GVG nicht. Hier gilt die allgemeine streitwertabhängige Aufteilung:

| Mietverhältnis | Streitwert | Sachlich zuständig | Norm |
|---|---|---|---|
| Wohnraum | beliebig | Amtsgericht | Paragraf 23 Nr. 2a GVG |
| Gewerberaum | bis einschließlich 10.000 EUR | Amtsgericht | Paragraf 23 Nr. 1 GVG |
| Gewerberaum | über 10.000 EUR | Landgericht | Paragraf 71 Abs. 1 GVG |

Das Plugin bedient überwiegend Wohnraum-Forderungsmanagement. Geschäftsraumsachen mit Streitwert über 10.000 EUR werden grundsätzlich an die externe Stammkanzlei eskaliert (Skill 08), weil dann regelmäßig das Landgericht zuständig ist und Anwaltszwang besteht. Gesetzesstand, Sonderzuweisung und Übergangsrecht bleiben Einreichungsgates.

### 3. Örtliche Zuständigkeit prüfen

Nach Paragraf 29a Abs. 1 ZPO ist für Streitigkeiten über Ansprüche aus Miet- oder Pachtverhältnissen über Räume oder über deren Bestehen ausschließlich das Gericht am Lageort zuständig. Vor Anwendung ist Paragraf 29a Abs. 2 ZPO zu prüfen: Der ausschließliche Lageortgerichtsstand gilt nicht für Wohnraum nach Paragraf 549 Abs. 2 Nr. 1 bis 3 BGB, insbesondere nur vorübergehend vermieteten Wohnraum und bestimmte möblierte Räume in der Vermieterwohnung. Dann den allgemeinen oder einen anderen besonderen Gerichtsstand neu bestimmen.

### 4. Konkretes Gericht zuordnen

In Berlin und anderen Großstädten kann die genaue Gerichtszuordnung bezirks- oder geschäftsverteilungsabhängig sein. Eine aktuelle amtliche Gerichts- oder Geschäftsverteilungsquelle prüfen; keine alte Tabelle ungeprüft übernehmen. Quelle, Abrufdatum und konkretes Gericht im Vermerk festhalten.

### 5. Online-Verfahren erst nach der Zuständigkeit prüfen

Das Online-Verfahren nach Paragrafen 1122 bis 1134 ZPO ist eine alternative Verfahrensart, keine zusätzliche Zuständigkeitsnorm. Es kommt nur für eine reine Zahlungsklage bis zum Betrag des Paragrafen 23 Nr. 1 GVG vor einem tatsächlich zuständigen, durch Landesverordnung teilnehmenden Amtsgericht in Betracht. Räumungs-, Herausgabe- und Duldungsanträge sowie Verfahren nach Paragraf 23a GVG gehören nicht in diesen Sonderweg.

Für Berlin gilt am 09.08.2026: Das Amtsgericht Schöneberg nimmt seit 15.04.2026 ausschließlich für seinen eigenen Gerichtsbezirk teil. Es wird dadurch nicht für alle Berliner Zahlungsklagen zuständig. Nach der Gerichtszuordnung sind deshalb vier getrennte Felder auszugeben: `zuständiges Gericht`, `Teilnahme nach aktueller Landesverordnung`, `amtlicher Eingabedienst unterstützt Anspruch und Rolle` sowie `regulärer oder Online-Verfahrensweg`. Der aktuelle Bundesdienst bildet die Eigenvertretung einer privaten GmbH durch Beschäftigte nicht automatisch ab; ohne bestätigte Dienstabdeckung bleibt es bei der regulären Klage. Details und Primärquellen stehen in `references/rechtsstand-2026-verfahren-vollstreckung.md`.

### 6. Anwaltszwang nach Paragraf 78 ZPO prüfen

#### 6.1 Grundsatz

Der Anwaltszwang in Zivilsachen richtet sich nach Paragraf 78 ZPO und damit nach der sachlichen Zuständigkeit:

- Vor dem Amtsgericht im ersten Rechtszug besteht kein Anwaltszwang. Die Parteien können den Rechtsstreit selbst führen (Paragraf 78 Abs. 1 ZPO im Umkehrschluss; Paragraf 79 Abs. 1 ZPO).
- Vor den Landgerichten und allen höheren Gerichten müssen sich die Parteien durch einen Rechtsanwalt vertreten lassen (Paragraf 78 Abs. 1 S. 1 ZPO).
- Im Berufungs- und Revisionsverfahren besteht stets Anwaltszwang (Paragraf 78 Abs. 1 ZPO).

#### 6.2 Vertretungsregeln am Amtsgericht

Vor dem Amtsgericht können sich juristische Personen nach Paragraf 79 Abs. 2 S. 2 Nr. 1 ZPO durch Beschäftigte der Partei selbst oder eines mit ihr verbundenen Unternehmens im Sinne des Paragrafen 15 AktG vertreten lassen. Zu prüfen und zu dokumentieren sind Beschäftigtenstatus, Konzernbezug, Vollmacht und interne Freigabe; eine zusätzliche, im Gesetz nicht genannte Sachkundeanforderung darf nicht erfunden werden.

#### 6.3 RDG-Einordnung getrennt prüfen

Die Bearbeitung eigener Angelegenheiten der beschäftigenden Gesellschaft ist grundsätzlich keine Tätigkeit in einer fremden Angelegenheit nach Paragraf 2 Abs. 1 RDG. Rechtsangelegenheiten innerhalb verbundener Unternehmen gelten nach Paragraf 2 Abs. 3 Nr. 6 RDG nicht als Rechtsdienstleistung. Das ersetzt die gesonderte Prozessvertretungsprüfung nach Paragraf 79 ZPO nicht. Skill 07 prüft die Abgrenzung eigens.

#### 6.4 Konsequenz für Wohnraummietsachen

Bei Wohnraummietklagen besteht im ersten Rechtszug grundsätzlich kein Anwaltszwang, ganz gleich wie hoch der Streitwert ist. Die interne 10.000-EUR-Grenze hat damit nichts zu tun: Sie ist ausschließlich eine Bearbeitungs- und Freigabeschwelle der Abteilung Forderungsmanagement, kein gesetzlicher Anwaltszwang. Auch bei einem Mietrückstand von 25.000 EUR aus Wohnraum darf die Konzerngesellschaft sich nach Paragraf 23 Nr. 2a GVG in Verbindung mit Paragraf 79 Abs. 2 S. 2 Nr. 1 ZPO durch eine Renofa selbst vertreten lassen. Die interne Freigabe ist davon getrennt zu prüfen.

#### 6.5 Verbundene Räumungs- und Zahlungsklage

Wird die Zahlungsklage wegen Mietrückstands mit einer Räumungsklage verbunden, bleibt es bei Wohnraum bei der Zuständigkeit des Amtsgerichts nach Paragraf 23 Nr. 2a GVG. Auch hier besteht im ersten Rechtszug kein Anwaltszwang. Das gilt unabhängig von der Höhe des Streitwerts der verbundenen Klage.

### 7. Eskalationsschwellen Anwaltszwang

Sobald einer der folgenden Trigger greift, ist nach Skill 08 an die externe Stammkanzlei zu eskalieren, weil dann gesetzlicher Anwaltszwang besteht oder droht:

1. Statthafte oder zugelassene Berufung gegen ein Amtsgerichtsurteil. Nach Paragraf 511 Abs. 2 ZPO muss der Wert des Beschwerdegegenstands 1.000 EUR übersteigen oder das Erstgericht die Berufung zugelassen haben; bei einer Beschwer bis 1.000 EUR ist die Zulassungsentscheidung nach Paragraf 511 Abs. 4 ZPO im Urteil zu kontrollieren. Unabhängig davon sofort Zustellung und Notfrist von einem Monat nach Paragraf 517 ZPO sowie die zweimonatige Begründungsfrist nach Paragraf 520 Abs. 2 ZPO notieren und an die Stammkanzlei geben.
2. Revision.
3. Sache fällt in die sachliche Zuständigkeit des Landgerichts (bei allgemeinen Zivilsachen grundsätzlich über 10.000 EUR Streitwert).
4. Klage wird auf eine andere Anspruchsgrundlage als Wohnraummiete gestützt und fällt deshalb nicht unter die Sonderzuweisung; Zuständigkeit und Zusammenhang neu prüfen.
5. Verfahren wird vom AG nach Paragraf 281 ZPO an das LG verwiesen.

## Quellenpflicht

Jede juristische Aussage wird nach `references/zitierweise.md` belegt (Rechtsprechung vor Literatur, neueste zuerst). Leitentscheidungen werden über `references/leitentscheidungen-anker.md` als Sucheinstieg gewählt und vor Verwendung in einer freien amtlichen Quelle live verifiziert; keine erfundenen Aktenzeichen. Für das Online-Verfahren ist `references/rechtsstand-2026-verfahren-vollstreckung.md` mit Landes-, Rollen- und Dienstgate zwingend.

## Ausgabeformat

Zuständigkeitsvermerk in dezimaler Gliederung (1, 1.1, 1.1.1, ...) mit:

- 1. Streitgegenstand und Art des Mietverhältnisses (Wohnraum/Gewerberaum)
- 2. Streitwert (vorläufig)
- 3. Sachliche Zuständigkeit mit Norm-Anker
- 4. Örtliche Zuständigkeit mit Norm-Anker
- 5. Konkretes Gericht mit Geschäftsverteilungsstand und Abrufdatum
- 6. Verfahrensweg: regulär oder Online-Verfahren mit Landes-, Anspruchs-, Betrags-, Rollen- und Dienstgate
- 7. Anwaltszwang ja/nein mit Begründung (Paragraf 78 ZPO i. V. m. Paragraf 79 ZPO und Paragraf 23 Nr. 2a GVG)
- 8. Rubrum-Baustein

Der Vermerk wird in vollständigen Sätzen ausformuliert (Ausformulierungspflicht).

## Beispiele

- Mietobjekt Wilhelmstraße 14, 10963 Berlin-Kreuzberg, Wohnraum, Mietrückstand 4.220 EUR: sachlich Amtsgericht (Paragraf 23 Nr. 2a GVG), örtlich Amtsgericht Kreuzberg (Paragraf 29a ZPO), kein Anwaltszwang (Paragraf 78 ZPO i. V. m. Paragraf 79 Abs. 1 ZPO), Konzern-Inhouse-Vertretung nach Paragraf 79 Abs. 2 S. 2 Nr. 1 ZPO zulässig. Gerichtsbezirk vor Einreichung nochmals amtlich prüfen.
- Mietobjekt Boxhagener Straße 47, Wohnraum, kombinierte Räumungs- und Zahlungsklage mit Streitwert über 10.000 EUR: trotz Streitwert sachlich Amtsgericht (Paragraf 23 Nr. 2a GVG), kein Anwaltszwang. Die interne 10.000-EUR-Grenze ist Bearbeitungsschwelle, nicht Anwaltszwang. Interne Freigabe der Bereichsleitung wird gesondert eingeholt.
- Mietobjekt Friedrichstraße 22, Geschäftsraum (Ladenlokal), Mietrückstand 18.500 EUR: sachlich grundsätzlich Landgericht (Paragraf 71 Abs. 1 GVG), Anwaltszwang nach Paragraf 78 Abs. 1 S. 1 ZPO. Eskalation an Stammkanzlei nach Skill 08.
- Reine Zahlungsklage über 4.800 EUR im Bezirk des Amtsgerichts Schöneberg: Zuständigkeit zuerst regulär prüfen, danach Teilnahme seit 15.04.2026 und aktuelle Dienstabdeckung der wirklichen Vertretungsrolle; bei nicht unterstützter GmbH-Eigenvertretung reguläres Verfahren.
- Beklagter Mieter mit Zweitwohnsitz in Hamburg: Die örtliche Zuständigkeit bleibt am Lageort der Mietsache, nicht am Wohnsitz (Paragraf 29a ZPO).
- Möbliertes Zimmer in der von der Vermieterin selbst bewohnten Wohnung: Ausnahme nach Paragraf 29a Abs. 2 ZPO in Verbindung mit Paragraf 549 Abs. 2 Nr. 2 BGB prüfen; Lageort nicht automatisch als ausschließlichen Gerichtsstand ausgeben.
