---
name: pkv-kostenerstattung-private
description: "PKV Kostenerstattung Private: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# PKV Kostenerstattung Private

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **PKV Kostenerstattung Private** im Plugin Versicherungsrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `pkv-kostenerstattung-medizinische-notwendigkeit` | PKV-Leistungsprüfung: medizinische Notwendigkeit, Gebührenrecht, Heilbehandlung, Hilfsmittel, Psychotherapie, Arzneimittel und Kürzungsschreiben. |
| `private-krankenversicherung-beitragsanpassung-treuhaender` | Private Krankenversicherung: Beitragsanpassung, Treuhänder, Begründungsschreiben, Tarifwechsel, Auskunft und Rückforderungsrisiken prüfen. |
| `produkthaftpflicht-rueckrufkosten` | Produkthaftpflichtversicherung: Produktfehler, Personenschaden, Rückruf, Austauschkosten, Rückrufkostenversicherung und internationale Lieferketten. |

## Arbeitsweg

Im Plugin Versicherungsrecht gilt für **PKV Kostenerstattung Private**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `pkv-kostenerstattung-medizinische-notwendigkeit`

**Fokus:** PKV-Leistungsprüfung: medizinische Notwendigkeit, Gebührenrecht, Heilbehandlung, Hilfsmittel, Psychotherapie, Arzneimittel und Kürzungsschreiben.

# PKV: Kostenerstattung und medizinische Notwendigkeit

## Einsatz

Für Streit um Arztrechnungen und Heilbehandlung: nicht bloß „medizinisch sinnvoll“, sondern erstattungsfähig nach Vertrag.

## Norm- und Quellenanker

VVG §§ 192, 193, 194, 203; MB/KK; GOÄ/GOZ; BGB; ZPO medizinischer Sachverständiger.

## Arbeitsfragen

1. Welche Behandlung, Diagnose, Rechnung und Tarifklausel sind betroffen?
2. Bestreitet der Versicherer medizinische Notwendigkeit, Gebührenhöhe oder Tarifdeckung?
3. Welche Belege braucht der Arzt, welche der Versicherungsnehmer?
4. Ist eine vorherige Leistungszusage relevant?

## Output

Erstattungsmemo, Arztfragebogen, Versichererantwort und Klagebaustein.

## Red Flags

- Arztbrief ersetzt keine Notwendigkeitsbegründung
- Gebührenstreit und Deckungsstreit vermischt
- Hilfsmittel nicht tariflich geprüft
- Schweigepflichtentbindung zu weit

## Anschluss-Skills

- datenschutz-schweigepflicht-gesundheitsdaten
- krankentagegeld-berufsunfaehigkeit-abgrenzung

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren; sonst nur als Prüfpunkt formulieren.

## 2. `private-krankenversicherung-beitragsanpassung-treuhaender`

**Fokus:** Private Krankenversicherung: Beitragsanpassung, Treuhänder, Begründungsschreiben, Tarifwechsel, Auskunft und Rückforderungsrisiken prüfen.

# PKV: Beitragsanpassung und Treuhänder

## Einsatz

Der Skill prüft, ob eine PKV-Beitragserhöhung formal und materiell angreifbar ist und welche Strategie wirtschaftlich sinnvoll ist.

## Norm- und Quellenanker

VVG §§ 192–208, besonders § 203; VAG; BGB; PKV-AVB; Rechtsprechung nur live verifiziert.

## Arbeitsfragen

1. Welche Anpassungen und Schreiben liegen vor?
2. Sind Gründe ausreichend mitgeteilt?
3. Welche Tarifgeneration und Rechnungsgrundlagen sind betroffen?
4. Ist Rückforderung, Tarifwechsel oder Beschwerde der bessere Weg?

## Output

Beitragsanpassungs-Tabelle, Angriffspunkte, Auskunftsschreiben und Prozessrisiko.

## Red Flags

- nur Presseartikel statt Vertragsunterlagen
- Treuhänderfrage isoliert überschätzt
- Verjährung nicht gerechnet
- Tarifwechsel nach § 204 VVG vergessen

## Anschluss-Skills

- pkv-kostenerstattung-medizinische-notwendigkeit
- vag-bafin-aufsicht-beschwerde-missstand

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren; sonst nur als Prüfpunkt formulieren.

## 3. `produkthaftpflicht-rueckrufkosten`

**Fokus:** Produkthaftpflichtversicherung: Produktfehler, Personenschaden, Rückruf, Austauschkosten, Rückrufkostenversicherung und internationale Lieferketten.

# Produkthaftpflicht und Rückrufkosten

## Einsatz

Für Hersteller und Händler, wenn ein Produktfehler Schäden oder Rückrufaktionen auslöst.

## Norm- und Quellenanker

VVG §§ 100 ff.; ProdHaftG; BGB §§ 823, 434 ff.; Produktsicherheitsrecht; AVB.

## Arbeitsfragen

1. Ist der Schaden am Produkt selbst oder an fremden Rechtsgütern?
2. Welche Rückrufkosten sind versichert, welche nicht?
3. Welche Behörden-, Kunden- und Lieferkettenkommunikation läuft?
4. Welche Regresskette besteht?

## Output

Deckungslandkarte, Rückrufkostenmatrix, Regressplan und Kommunikationsentwurf.

## Red Flags

- Eigenschaden nicht versichert
- Rückruf ohne Deckungsabstimmung
- Serienfehler weltweit
- Produktsicherheitsmeldung vergessen

## Anschluss-Skills

- betriebshaftpflicht-versicherungsfall-serienschaden
- transportversicherung-ware-lagerung

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren; sonst nur als Prüfpunkt formulieren.
