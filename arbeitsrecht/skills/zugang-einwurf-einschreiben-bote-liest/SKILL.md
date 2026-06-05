---
name: zugang-einwurf-einschreiben-bote-liest
description: "Zugang Einwurf Einschreiben Bote Liest: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Zugang Einwurf Einschreiben Bote Liest

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Zugang Einwurf Einschreiben Bote Liest** im Plugin Arbeitsrecht (BGB §§ 611a ff., KSchG). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `zugang-neu-002-einwurf-einschreiben-auslieferungsbeleg-und-inhal` | Arbeitsrecht: Einwurf-Einschreiben Auslieferungsbeleg und Inhaltseinwand mit konkreter Fachprüfung, Quellenhygiene, Fehlerbremse und verwertbarem Arbeitsergebnis. |
| `zugang-neu-003-bote-liest-kuendigung-inhalt-umschlag-und-zeugenb` | Arbeitsrecht: Bote liest Kündigung Inhalt Umschlag und Zeugenbeweis mit konkreter Fachprüfung, Quellenhygiene, Fehlerbremse und verwertbarem Arbeitsergebnis. |
| `zugang-neu-004-persoenliche-uebergabe-empfangsverweigerung-und-z` | Arbeitsrecht: Persönliche Übergabe Empfangsverweigerung und Zeugen mit konkreter Fachprüfung, Quellenhygiene, Fehlerbremse und verwertbarem Arbeitsergebnis. |
| `zugang-neu-005-hausbriefkasten-leerungszeiten-und-zugang` | Arbeitsrecht: Hausbriefkasten Leerungszeiten und Zugang mit konkreter Fachprüfung, Quellenhygiene, Fehlerbremse und verwertbarem Arbeitsergebnis. |

## Arbeitsweg

Im Plugin Arbeitsrecht (BGB §§ 611a ff., KSchG) gilt für **Zugang Einwurf Einschreiben Bote Liest**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `zugang-neu-002-einwurf-einschreiben-auslieferungsbeleg-und-inhal`

**Fokus:** Arbeitsrecht: Einwurf-Einschreiben Auslieferungsbeleg und Inhaltseinwand mit konkreter Fachprüfung, Quellenhygiene, Fehlerbremse und verwertbarem Arbeitsergebnis.

# Zugang Einwurf Einschreiben Auslieferungsbeleg Und Inhal

## Aufgabe

Skill fuer Einwurfeinschreiben als Zustellnachweis bei Kuendigung — Beweiswert des Auslieferungsbelegs.

## Was ist Einwurfeinschreiben?

- Deutsche Post-Produkt: Sendung wird in den Briefkasten eingeworfen, Zusteller dokumentiert mit Auslieferungsbeleg (Foto + GPS).
- KEINE Unterschrift des Empfaengers.

## Beweiswert nach BAG-Linie

- BAG 2 AZR 224/18 vom 22.08.2019: Der Auslieferungsbeleg ist Anscheinsbeweis fuer den Einwurf, aber NICHT fuer den Inhalt des Umschlags.
- Anscheinsbeweis kann der Empfaenger durch substanziierte Gegendarstellung erschuettern (z. B. Briefkasten ueberfuellt, fremder Briefkasten).

## Was beweist der Auslieferungsbeleg?

- Datum und Uhrzeit des Einwurfs.
- Adresse.
- Foto/GPS.

## Was NICHT beweist:

- Inhalt des Umschlags (Kuendigungsschreiben tatsaechlich enthalten).
- Zugang als solchen (Briefkasten kann fremd, ueberfuellt, kaputt sein).

## Empfehlung Arbeitgeber

1. Einwurfeinschreiben + zweites Versand (Bote zur Empfangsbestaetigung) oder Uebergabe persoenlich.
2. Inhalt protokollieren (Zeuge sieht Umschlag-Inhalt vor Einwurf).
3. Kopie der Kuendigung mit Versand-Vermerk dokumentieren.

## Pruefraster

1. Welcher Zustellweg?
2. Auslieferungsbeleg vorhanden?
3. Inhalt nachweisbar?
4. Gegenbeweis vom Empfaenger?

## Output

- Zustell-Memo.
- Beweissicherung-Empfehlung.

## 2. `zugang-neu-003-bote-liest-kuendigung-inhalt-umschlag-und-zeugenb`

**Fokus:** Arbeitsrecht: Bote liest Kündigung Inhalt Umschlag und Zeugenbeweis mit konkreter Fachprüfung, Quellenhygiene, Fehlerbremse und verwertbarem Arbeitsergebnis.

# Zugang Bote Liest Kuendigung Inhalt Umschlag Und Zeugenb

## Aufgabe

Skill fuer Botenzustellung der Kuendigung — Beweissicherung durch Zeugen.

## Konstellation

Arbeitgeber laesst die Kuendigung durch einen **Boten** uebergeben (interner Mitarbeiter, externer Zustellservice, Notar). Bote dokumentiert Einwurf oder Uebergabe.

## Was muss der Bote tun?

1. Den Inhalt des Umschlags vor dem Einwurf/Uebergabe persoenlich sehen oder lesen.
2. Den Umschlag verschliessen.
3. Den Umschlag in den Briefkasten einwerfen oder persoenlich uebergeben.
4. Datum, Uhrzeit, Adresse dokumentieren.
5. Aussagebereitschaft als Zeuge erklaeren.

## Beweiswert

- Bote ist Zeuge im Sinne § 373 ZPO.
- Persoenliche Wahrnehmung als unmittelbarer Beweis.
- BAG-Linie: Zeugenbeweis durch Boten = staerker als Anscheinsbeweis.

## Pflichten Bote

- Sichere Aufbewahrung der Beweismittel (eigene Notiz, ggf. Foto).
- Verschwiegenheit beachten (kein Mitlesen Dritter).

## BAG-Linie

- BAG 2 AZR 369/16 zur Botenzustellung.
- BAG 2 AZR 224/18 zum Zugang.
- Az im Mandat live verifizieren.

## Pruefraster

1. Wer ist Bote?
2. Hat er den Inhalt gesehen?
3. Datum/Uhrzeit dokumentiert?
4. Zeugenaussage moeglich?

## Output

- Bote-Zustellprotokoll.
- Zeugenmemo fuer den Prozess.

## 3. `zugang-neu-004-persoenliche-uebergabe-empfangsverweigerung-und-z`

**Fokus:** Arbeitsrecht: Persönliche Übergabe Empfangsverweigerung und Zeugen mit konkreter Fachprüfung, Quellenhygiene, Fehlerbremse und verwertbarem Arbeitsergebnis.

# Zugang Persoenliche Uebergabe Empfangsverweigerung Und Z

## Aufgabe

Skill fuer persoenliche Uebergabe der Kuendigung und Behandlung der Empfangsverweigerung.

## Persoenliche Uebergabe

- Arbeitgeber (oder Vertreter) uebergibt die Kuendigung direkt an den Arbeitnehmer.
- Zugang ist mit Uebergabe gegeben (§ 130 BGB analog).

## Empfangsverweigerung

- Arbeitnehmer verweigert die Annahme oder den Umschlag.
- Folge: **Zugang gilt trotzdem als erfolgt**, wenn die Verweigerung unberechtigt ist.

## Voraussetzungen fuer Zugang trotz Verweigerung

- Der Arbeitnehmer war "in der Lage", die Kuendigung zur Kenntnis zu nehmen.
- Die Verweigerung war unberechtigt (kein wirksamer Grund).

## Beweisfuehrung

- Zeuge: Personalreferent, Vorgesetzter, externer Notar.
- Protokoll mit Datum, Uhrzeit, Ort, Beschreibung der Verweigerung.

## BAG-Linie

- BAG 2 AZR 358/04 zur Empfangsverweigerung.
- BAG 2 AZR 224/18 generell zum Zugang.
- Az verifizieren.

## Pruefraster

1. Uebergabe versucht?
2. Verweigerung dokumentiert?
3. Zeuge vorhanden?
4. Grund der Verweigerung?

## Output

- Uebergabeprotokoll.
- Zeugenmemo.

## 4. `zugang-neu-005-hausbriefkasten-leerungszeiten-und-zugang`

**Fokus:** Arbeitsrecht: Hausbriefkasten Leerungszeiten und Zugang mit konkreter Fachprüfung, Quellenhygiene, Fehlerbremse und verwertbarem Arbeitsergebnis.

# Zugang Hausbriefkasten Leerungszeiten Und Zugang

## Aufgabe

Skill fuer Hausbriefkasten als Zugangsstelle und die Bedeutung der ueblichen Leerungszeit.

## Hausbriefkasten als Machtbereich

- Der Briefkasten gehoert zum Machtbereich des Empfaengers.
- Einwurf = Zugang, sobald die Erklaerung in den Briefkasten gelangt UND mit Kenntnisnahme zu rechnen ist.

## Uebliche Leerungszeit

- Werktags 1-2 mal taeglich.
- Bei Einwurf vor der ueblichen Leerung: Zugang am selben Tag.
- Bei Einwurf nach der ueblichen Leerung: Zugang erst am naechsten Werktag.

## BAG-Linie zu Sonn-/Feiertagen

- BAG: bei Einwurf an einem Sonntag erfolgt Zugang regelmaessig erst am folgenden Werktag.
- BAG 2 AZR 224/18 zur Verkehrsuebung.
- BAG 6 AZR 687/09 zur Zugangsfiktion.

## Wichtig fuer Klagefrist

- Beispiel: Einwurf Samstag 14:00 Uhr; Zugang Montag.
- 3-Wochen-Frist § 4 KSchG laeuft ab Montag.

## Streitfaelle

- Briefkasten defekt, gross genug, ueberfuellt.
- Fremder Briefkasten (Mehrfamilienhaus mit gleichem Namen).
- Arbeitnehmer im Urlaub — Zugang trotzdem (Urlaubs-Selbstrisiko).

## Pruefraster

1. Wann wurde eingeworfen?
2. Wann war Leerung uebrlich?
3. Welcher Werktag = Zugang?
4. Werktag oder Sonntag?
5. Briefkasten ordnungsgemaess?

## Output

- Zugangstabelle mit Datum-Uhrzeit-Berechnung.
- Memo zur Klagefrist § 4 KSchG.
