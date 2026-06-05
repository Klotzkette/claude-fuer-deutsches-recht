---
name: bautraeger-rueckabwicklung-insolvenz
description: "Bautraeger Rueckabwicklung Insolvenz: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Bautraeger Rueckabwicklung Insolvenz

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Bautraeger Rueckabwicklung Insolvenz** im Plugin Fachanwalt Bau- und Architektenrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `bautraeger-rueckabwicklung-bei-insolvenz` | Bautraeger-Rueckabwicklung bei Insolvenz. Skill klaert das Verfahren der Rueckabwicklung wenn der Bautraeger insolvent geht aber Eigentumsuebertragung noch nicht erfolgt ist Buergschaftsabruf Forderungsanmeldung Wohnungsuebernahme im Insolvenzverfahren. Liefert Pruefraster. |
| `bautraeger-selbstvornahme-und-vorschussklage` | Selbstvornahme und Vorschussklage gegen den Bautraeger. Skill klaert das Recht zur Selbstvornahme nach § 637 BGB die Vorschussklage zur Finanzierung der Beseitigung und die typischen Fallgruppen Erwerber will saniertes Apartment. Liefert Pruefraster. |
| `bautraeger-sonderwuensche-zusaetzliche-vereinbarungen` | Bautraeger-Sonderwuensche und zusaetzliche Vereinbarungen. Skill klaert die Behandlung von Sonderwuensche Mehrpreisen Aenderungen der Baubeschreibung Schriftform und das Verhaeltnis zur urspruenglichen Vertragsgrundlage. Liefert Klauselentwurf. |
| `bautraeger-typische-nichtigkeitsfallen-checkliste` | Bautraeger typische Nichtigkeitsfallen und Erwerber-Strategie. Skill listet die haeufigsten Nichtigkeitstatbestaende und entwickelt Strategien fuer den Erwerber wann Nichtigkeit zu seinem Vorteil genutzt werden kann (Default-Recht oft guenstiger). Liefert Risiko-Cockpit. |

## Arbeitsweg

Im Plugin Fachanwalt Bau- und Architektenrecht gilt für **Bautraeger Rueckabwicklung Insolvenz**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `bautraeger-rueckabwicklung-bei-insolvenz`

**Fokus:** Bautraeger-Rueckabwicklung bei Insolvenz. Skill klaert das Verfahren der Rueckabwicklung wenn der Bautraeger insolvent geht aber Eigentumsuebertragung noch nicht erfolgt ist Buergschaftsabruf Forderungsanmeldung Wohnungsuebernahme im Insolvenzverfahren. Liefert Pruefraster.

# Bautraeger Rueckabwicklung Bei Insolvenz

## Rueckabwicklungsschritte

### 1. Buergschaft pruefen
- Vorlegen der Originalbuergschaft.
- Bonitaet des Buergen pruefen.
- Anspruchsschreiben an den Buergen.

### 2. Insolvenzverwalter kontaktieren
- Forderungsanmeldung binnen Frist (vom IV bekanntgegeben).
- Sicherung Vormerkungsrang.

### 3. Aussonderung pruefen
- Bei Globalgrundschuld Pfandfreigabe.
- Bei Anwartschaftsrecht: insolvenzfeste Position.

### 4. Wohnungsuebernahme
- Wenn Bauwerk fertiggestellt: gegen Restzahlung uebernehmen.
- Wenn nicht fertiggestellt: Insolvenzverwalter kann Wohnung an Dritten weiterveraussern.

## Praxis

- Buergschaft greift typischerweise schnell.
- Wenn keine Buergschaft: lange Insolvenzdauer.

## Pruefraster

1. Buergschaft vorhanden?
2. Forderung angemeldet?
3. Vormerkungsrang?
4. Bauwerk fertiggestellt?

## 2. `bautraeger-selbstvornahme-und-vorschussklage`

**Fokus:** Selbstvornahme und Vorschussklage gegen den Bautraeger. Skill klaert das Recht zur Selbstvornahme nach § 637 BGB die Vorschussklage zur Finanzierung der Beseitigung und die typischen Fallgruppen Erwerber will saniertes Apartment. Liefert Pruefraster.

# Bautraeger Selbstvornahme Und Vorschussklage

## Norm

§ 637 BGB Selbstvornahme.

## Voraussetzungen

- Mangel.
- Frist gesetzt.
- Frist ist abgelaufen.
- Mangel besteht weiter.

## Selbstvornahme

- Erwerber laesst Mangel beseitigen.
- Bautraeger traegt die Kosten.

## Vorschuss

- § 637 Abs. 3 BGB: Erwerber kann einen Kostenvorschuss vom Bautraeger fordern, ohne in Vorleistung treten zu muessen.
- Vorschussklage moeglich, wenn Bautraeger nicht freiwillig zahlt.

## Praxis

- Erwerber holt Kostenvoranschlag von einem Handwerker.
- Vorschussbetrag fordern.
- Nach Beseitigung Abrechnung.

## Pruefraster

1. Frist gesetzt?
2. Kostenvoranschlag?
3. Vorschussklage erforderlich?

## 3. `bautraeger-sonderwuensche-zusaetzliche-vereinbarungen`

**Fokus:** Bautraeger-Sonderwuensche und zusaetzliche Vereinbarungen. Skill klaert die Behandlung von Sonderwuensche Mehrpreisen Aenderungen der Baubeschreibung Schriftform und das Verhaeltnis zur urspruenglichen Vertragsgrundlage. Liefert Klauselentwurf.

# Bautraeger Sonderwuensche Zusaetzliche Vereinbarungen

## Sonderwuensche

- Erwerber wuenscht Aenderung gegenueber Baubeschreibung.
- Beispiel: bessere Bodenbelaege, Sanitaer-Ausstattung.

## Form

- Schriftlich (Empfehlung).
- Beidseits unterzeichnet.
- Genaue Beschreibung und Mehrpreis.

## Mehrpreis-Klauseln

- Pauschal: oft uebersetzt.
- Auf Basis Selbstkosten-Plus: angemessener.
- Empfehlung: vorab Vergleichsangebote einholen.

## Verhaeltnis zur Baubeschreibung

- Sonderwunsch aendert Baubeschreibung punktuell.
- Restliche Vertragsregelungen gelten weiter.

## Risiken

- Bautraeger draengt zu spaeten Sonderwuensche und verlangt unangemessen.
- Verzoegerung der Bauzeit.

## Klauselentwurf Sonderwunsch

"Die Parteien vereinbaren folgende Aenderung zur Baubeschreibung vom [Datum]: [Beschreibung Sonderwunsch]. Der Mehrpreis betraegt [Betrag] EUR. Die Vertragsausfuehrung verzoegert sich um maximal [Tage] Tage. Im uebrigen bleibt der Vertrag unveraendert."

## Pruefraster

1. Schriftlich vereinbart?
2. Mehrpreis angemessen?
3. Verzug akzeptabel?

## 4. `bautraeger-typische-nichtigkeitsfallen-checkliste`

**Fokus:** Bautraeger typische Nichtigkeitsfallen und Erwerber-Strategie. Skill listet die haeufigsten Nichtigkeitstatbestaende und entwickelt Strategien fuer den Erwerber wann Nichtigkeit zu seinem Vorteil genutzt werden kann (Default-Recht oft guenstiger). Liefert Risiko-Cockpit.

# Bautraeger Typische Nichtigkeitsfallen Checkliste

## Nichtigkeitstatbestaende

### MaBV-Verstoss
- Klausel zu Vorausleistung ohne Sicherheit: unwirksam.

### Notarrechtlicher Mangel
- Aufflassung nicht beurkundet: nichtig.
- Beurkundung ohne 2-Wochen-Frist: idR wirksam, aber Belehrungspflicht verletzt.

### Sittenwidrigkeit § 138 BGB
- Bei extremem Missverhaeltnis Preis-Leistung.

### AGB-Verstoss § 307 BGB
- Einzelne Klauseln unwirksam.
- Vertrag im uebrigen wirksam.

## Erwerber-Strategie

### Wenn Default-Recht guenstiger
- Erwerber kann es bei der Unwirksamkeit belassen.
- Default = BGB-Werkvertrag oder Verbraucherbauvertrag mit besseren Rechten.

### Wenn Default-Recht ungueltiger
- Erwerber kann durch Geltendmachung der wirksamen Klauseln seine Position halten.

## Risiko-Cockpit

| Klauseltyp | Risiko Erwerber | Default-Lage |
|---|---|---|
| Abnahmefiktion | Mittel | guenstig |
| Maengelhaftungsverkuerzung | Hoch | guenstig (5 Jahre §634a) |
| Vorausleistung ohne Buergschaft | Hoch | guenstig (Rueckzahlung) |
| Einseitige Preisanpassung | Mittel | guenstig (Festpreis) |

## Pruefraster

1. Welche Klausel ist unwirksam?
2. Wer profitiert vom Default-Recht?
3. Verhaltensempfehlung?
