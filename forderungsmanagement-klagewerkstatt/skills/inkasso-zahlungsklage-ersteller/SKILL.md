---
name: inkasso-zahlungsklage-ersteller
description: "Freistehender Inkasso-Zahlungsklage-Ersteller für Forderungsmanagement: Mahnvorlauf, Anspruchs-Gatekeeper, Teilzahlung/Erfüllung, Verzug, Inkassokosten, Gerichtsortfindung und Klage nur für klare, fällige und belegte Ansprüche."
---

# Inkasso-Zahlungsklage-Ersteller

## Zweck

Dieser Skill baut aus einer Forderungsakte einen sauberen Mahn- und Klageworkflow. Er ist bewusst konservativ: **Eingeklagt werden nur Ansprüche, die nach Aktenlage klar, fällig, durchsetzbar und belegt sind.** Unsichere Positionen werden nicht in eine Klage hineingezogen, sondern als Rückfrage, Vergleichsvorschlag, weiterer Belegbedarf oder Nichtklage-Empfehlung ausgegeben.

Der Skill ist freistehend. Er braucht keine anderen Plugins. Er kann mit einfachen Rechnungen, Mahnungen, Inkassoschreiben, Teilzahlungen, Mahnbescheid/Widerspruch und einer vorhandenen fehlerhaften Klage arbeiten.

## Sofortregeln

1. **Nicht alles einklagen, was im Forderungskonto steht.** Jede Position braucht Anspruchsgrundlage, Betrag, Fälligkeit, Verzug oder sonstige Erstattungsnorm, Beleg und Einwendungskontrolle.
2. **Erfüllung blockt.** Eine vor Klageeinreichung gezahlte Hauptforderung darf nicht mehr als Hauptforderung eingeklagt werden. Sie kann nur noch für Kosten- und Zinsfragen relevant sein.
3. **Kenntnis blockt härter.** Wenn der Gläubiger oder Inkassodienstleister vor Klageeinreichung von der Zahlung wusste, ist eine Klage auf die Hauptforderung rot zu markieren.
4. **Nebenforderungen sind kein Autopilot.** Mahnkosten, Verzugszinsen, Inkassokosten, Mahnverfahrenskosten und Auslagen werden einzeln geprüft.
5. **Gerichtsort vor Klage.** Sachliche und örtliche Zuständigkeit sind vor Entwurf der Anträge zu prüfen und mit Online-Quelle sowie Abrufdatum zu dokumentieren.
6. **Mahnung vor Eskalation.** Wenn noch keine ausreichende Inverzugsetzung oder kalendermäßige Fälligkeit vorliegt, wird zuerst ein Mahnschreiben vorgeschlagen.

## Pflichtablauf

### Schritt 1: Akte aufnehmen

Sammle aus Rechnungen, Bestellungen, Lieferscheinen, Zustellbelegen, Mahnungen, Inkassoschreiben, Kontoauszügen, Abtretungen, Mahnbescheid und Widerspruch mindestens diese Felder:

| Feld | Pflichtinhalt |
| --- | --- |
| Gläubiger / Zessionar | Name, Anschrift, Rechtsform, Vertretung, Abtretungskette |
| Schuldner | Name, aktuelle Anschrift, Verbraucher/Unternehmer, Umzugshinweise |
| Forderungsgrund | Vertragstyp, Datum, Leistung, Rechnungsnummer, Belege |
| Hauptforderung | Betrag, Fälligkeit, Teilzahlungen, Erfüllung |
| Mahnvorlauf | Datum, Kanal, Zugang, gesetzte Frist, Mahnkosten |
| Verzug | Verzugseintritt, Grundlage, Verschuldenseinwände |
| Nebenforderungen | Mahnkosten, Verzugszinsen, Inkassokosten, Mahnbescheidkosten |
| Prozessgeschichte | Mahnbescheid, Widerspruch, Abgabe, vorhandene Klage |
| Gerichtsort | Beklagtenanschrift, Erfüllungsort, Verbraucherschutz, Gerichtsstandsvereinbarung |

Wenn Aktenangaben fehlen, arbeite mit einer Ampel und frage gezielt nach. Keine Fantasiedaten ergänzen.

### Schritt 2: Mahnvorlauf prüfen

Erstelle eine Mahnchronologie:

- Rechnung mit Fälligkeitsdatum.
- Erste Zahlungserinnerung.
- Erste Mahnung.
- Letzte Mahnung mit Klage-/Inkassohinweis.
- Inkassoschreiben und letzte Inkassoaufforderung.
- Zahlungseingänge und Zuordnung.

Bewerte jeden Mahnschritt:

- **Grün:** Zugang und Inhalt plausibel, Frist klar, Betrag richtig.
- **Gelb:** Zugang oder Betrag unklar, aber nacharbeitbar.
- **Rot:** falscher Adressat, falscher Betrag, bereits erledigte Forderung oder rechtlich ungeeignet.

Wenn noch kein sauberer Mahnvorlauf vorliegt, liefere zuerst ein Mahnschreiben. Der Klageentwurf folgt erst nach Ablauf der gesetzten Frist.

### Schritt 3: Anspruchs-Gatekeeper

Prüfe jede Forderungsposition als eigene Zeile:

| Prüffrage | Grün nur wenn |
| --- | --- |
| Anspruchsgrundlage | Norm und Tatsachen passen zusammen |
| Betrag | rechnerisch nachvollziehbar und belegt |
| Fälligkeit | Datum aus Vertrag/Rechnung/Gesetz klar |
| Durchsetzbarkeit | keine Erfüllung, Aufrechnung, Stundung, Verjährung oder Abtretungslücke |
| Verzug | § 286 BGB oder kalendermäßige Fälligkeit tragfähig |
| Verschulden | keine durchgreifenden Entlastungsargumente offen |
| Prozessrisiko | Einwendungen wurden sichtbar gewürdigt |
| Gerichtsort | zuständiges Gericht plausibel und online gegengeprüft |

Ausgabe je Position:

- **GRÜN / klagefähig:** in den Klageantrag aufnehmen.
- **GELB / nur nach Freigabe:** Rückfrage, Belegnachforderung oder Vergleichsvorschlag.
- **ROT / nicht einklagen:** nicht in die Klage aufnehmen; begründen.

### Schritt 4: Gerichtsort finden

1. **Sachliche Zuständigkeit:** Streitwert prüfen. Nach der Plugin-Logik seit 01.01.2026 grundsätzlich Amtsgericht bis 10.000 EUR, Landgericht darüber; Sonderzuständigkeiten prüfen.
2. **Örtliche Zuständigkeit:** allgemeiner Gerichtsstand der Beklagten nach §§ 12, 13 ZPO, bei juristischen Personen § 17 ZPO. Erfüllungsort nach § 29 ZPO nur nach genauer Prüfung, bei Verbrauchern § 29c ZPO beachten. Gerichtsstandsvereinbarungen bei Verbrauchern kritisch prüfen.
3. **Mahngericht:** Für ein vorgeschaltetes Mahnverfahren das zentrale Mahngericht des Landes prüfen. Bei Bayern typischerweise AG Coburg.
4. **Online-Abgleich:** Gericht über justizadressen.nrw.de, justiz.de oder das zuständige Landesjustizportal suchen. Quelle, URL, Abrufdatum, Treffer und verbleibende Unsicherheiten dokumentieren.

Wenn die Anschrift streitig oder veraltet ist, keine Klage freigeben, bevor die ladungsfähige aktuelle Anschrift geklärt ist.

### Schritt 5: Output bauen

Der Skill liefert standardmäßig:

1. **Mahnchronologie** als Tabelle.
2. **Anspruchsmatrix** mit Ampel.
3. **Klagefreigabe**: was wird eingeklagt, was nicht, warum.
4. **Gerichtsortprüfung** mit Online-Quellenplatzhalter.
5. **Klageentwurf** nur für grüne Positionen.
6. **Beleg- und Anlagenliste** mit K-Sigeln.
7. **Kosten-/Risiko-Hinweis** zu § 93 ZPO, Teilerledigung, sofortigem Anerkenntnis und unverhältnismäßiger Nebenforderungsklage.

## ModeFuchs-Testakte

Die Beispielakte `testakten/inkasso-zahlungsklage-modefuchs/` ist der Referenzfall:

- Kauf auf Rechnung über 698,00 EUR.
- Mehrere Mahnungen.
- Abtretung an InkassoZentrale GmbH.
- Inkassokosten und Verzugsnebenforderungen.
- Zahlung der Hauptforderung vor Klageeinreichung.
- Späterer Mahnbescheid und Klage, die die bereits erfüllte Hauptforderung trotzdem enthält.

Erwartete Bewertung:

- Hauptforderung 698,00 EUR: **ROT, nicht einklagen**, weil vor Klageeinreichung bezahlt und aktenkundig.
- Mahnkosten, Verzugszinsen, Inkassokosten zusammen 99,84 EUR: **GELB**, nur nach Prüfung von Zugang, Verzug, Verschulden, Höhe und Verhältnismäßigkeit; bei geringer Quote Vergleich oder Nichtklage prüfen.
- Gerichtsort: Beklagtenwohnsitz Nürnberg prüfen; vorhandene Klage zum AG Nürnberg plausibel, aber online zu verifizieren.

## Werkzeug

Für strukturierte JSON-Fälle kann `scripts/inkasso_claim_gate.py` genutzt werden:

```bash
python scripts/inkasso_claim_gate.py \
  --input testakten/inkasso-zahlungsklage-modefuchs/08_claim_gate_input.json \
  --output testakten/inkasso-zahlungsklage-modefuchs/09_claim_gate_output.json
```

Das Werkzeug ersetzt keine Rechtsprüfung. Es ist ein formaler Gatekeeper: bezahlte Hauptforderungen, fehlende Belege und unklare Nebenforderungen werden sichtbar geblockt oder in Review gestellt.

## Ausgabe-Ton

Kurz, klar und prozessnah. Keine langen Gutachten, wenn ein Gate rot ist. Dann zuerst sagen: **Diese Position nicht einklagen** und den Grund nennen.

## Übergabe an die Zwangsvollstreckung

Nach Rechtskraft des Zahlungstitels oder Erlass des Vollstreckungsbescheids lädt das freistehende
Plugin `zwangsvollstreckung` den passenden Folge-Skill: `zv-vollstreckungsbescheid-folge` für den
Übergang aus dem Mahnverfahren, `zv-pfueb-bank` für Kontopfändung, `zv-pfueb-arbeitsentgelt` für
Lohnpfändung mit Tabelle 1.7.2025, `zv-vermoegensauskunft-gv` für die Vorfeld-Recherche.
