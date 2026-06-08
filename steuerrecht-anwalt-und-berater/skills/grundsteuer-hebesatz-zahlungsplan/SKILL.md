---
name: grundsteuer-hebesatz-zahlungsplan
description: "Kommunalen Grundsteuerbescheid prüfen: Hebesatz, Satzung, Fälligkeiten, Zahlungsplan, Stundung, Erlass, Vollstreckungsaufschub, Abgrenzung Finanzamt/Gemeinde und Kommunikation mit Hausverwaltung oder Kommune."
---

# Grundsteuer: Hebesatz, Zahlung und Gemeindeebene

## Fachlicher Anker

- **Normen:** § 6a, § 25, § 28.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Aufgabe

Prüfe den Grundsteuerbescheid der Gemeinde und organisiere Zahlung, Stundung, Erlass oder kommunale Rechtsbehelfe. Dieser Skill ist nicht für Bewertungsfehler im Grundsteuerwertbescheid gedacht.

## Prüfen

1. Messbetrag aus dem Finanzamtsbescheid übernommen?
2. Hebesatz durch kommunale Satzung gedeckt?
3. Fälligkeiten korrekt?
4. Aufteilung auf Eigentümer, WEG, Hausverwaltung oder Erbbauberechtigte zutreffend?
5. Zahlung trotz Einspruch nötig?
6. Stundung, Ratenzahlung oder Erlass wegen unbilliger Härte realistisch?

## Typische Fehler

- falscher Messbetrag übernommen,
- altes Kassenzeichen oder falsches Objekt,
- falscher Eigentümer nach Verkauf,
- Hebesatzjahr verwechselt,
- Vorauszahlungen ohne neuen Bescheid fortgeschrieben,
- Hausverwaltung legt Kosten falsch auf Mieter oder WEG-Einheiten um.

## Output

Erstelle:

- Zahlungsplan mit Fälligkeiten und Vorfristen.
- Gemeindeschreiben bei Übernahmefehler.
- Stundungs-/Ratenzahlungsantrag, wenn nötig.
- Hinweis auf parallelen Einspruch beim Finanzamt, wenn die Bewertung falsch ist.
- Betriebskosten-/WEG-Hinweis nur als Nebensatz; vertiefte Prüfung an Miet-/WEG-Plugin abgeben.

## Abgrenzung

Wenn der Wert falsch ist, nicht bei der Gemeinde "korrigieren" wollen. Dann `anw-grundsteuer-kaltstart-bescheidkette` und `anw-grundsteuer-einspruch-adv-bfh` nutzen.

## Norm-Bezug konkret

- § 25 GrStG: Hebesatzrecht der Gemeinde.
- § 28 GrStG: Fälligkeit zu je einem Viertel zum 15.02., 15.05., 15.08., 15.11.
- § 27 GrStG: Jahresbescheid, Vorauszahlungen.
- § 33 GrStG: Erlass bei wesentlicher Ertragsminderung (insb. bei bebauten Grundstücken, Kulturgut).
- § 222 AO: Stundung wegen erheblicher Härte und Sicherheitsleistung.
- § 227 AO: Billigkeitserlass im Einzelfall.

## Praktischer Tipp

- Gegen den Gemeindegrundsteuerbescheid ist regelmäßig **Widerspruch nach VwGO** (nicht Einspruch nach AO) statthaft, weil es ein landesrechtlicher Verwaltungsakt ist. Frist und Form aus der Rechtsbehelfsbelehrung lesen; in einigen Bundesländern (z. B. NRW, Niedersachsen) ist das Vorverfahren abgeschafft, dann direkt Anfechtungsklage zum Verwaltungsgericht.
- § 33 GrStG-Erlass ist ein Antrag bis zum 31.03. des Folgejahres; Versäumung schließt den Erlass für das betreffende Jahr aus. Voraussetzung: Ertragsminderung über 50 % bei normaler Bewirtschaftung, nicht selbst verschuldet.
- Bei Eigentümerwechsel zum Jahreswechsel: Käufer schuldet erst ab Folgejahr (§ 10 Abs. 1 GrStG zum Stichtag); im Kaufvertrag aber häufig wirtschaftliche Übernahme pro rata temporis vereinbart - das ist nur schuldrechtlich, nicht gegenüber der Gemeinde wirksam.

## Beispiel-Mustertext (Stundungsantrag)

> Sehr geehrte Damen und Herren, hiermit beantrage ich für die mit Bescheid vom [Datum, AZ] festgesetzte Grundsteuer von EUR [...] Stundung gemäß § 222 AO. Die sofortige Einziehung würde eine erhebliche Härte bedeuten, weil [konkrete Lebenslage / Liquiditätsengpass mit Belegen]. Ich biete Ratenzahlung in monatlichen Teilbeträgen von EUR [...] ab dem [Datum] an. Auf eine Sicherheitsleistung wird verzichtet, weil [Begründung].

## Typische Fehler

- Rechtsbehelf gegen Hebesatzbescheid wird als Angriff auf den Grundsteuerwert geführt; die Gemeinde verweist auf den Grundlagenbescheid nach § 351 Abs. 2 AO - dort muss der Einspruch laufen.
- Zahlung "unter Vorbehalt" eingestellt, ohne förmliche AdV beim Finanzamt; Folge: Mahn- und Vollstreckungsverfahren der Gemeinde.

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
