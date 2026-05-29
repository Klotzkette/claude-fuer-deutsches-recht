---
name: mahnbescheid
description: "Mahnbescheid im gerichtlichen Mahnverfahren beantragen: Voraussetzungen, Formulierung, Übergang zum Streitverfahren. Normen: §§ 688 ff. ZPO. Prüfraster: Zuständigkeit Mahngericht, bestimmte Geldforderung, Widerspruchsrecht des Schuldners. Output: Mahnbescheidsantrag-Entwurf. Abgrenzung: nicht Klageschrift § 253 ZPO."
---

# Mahnverfahren – §§ 688 ff. ZPO

## Verweis auf das freistehende Plugin `zwangsvollstreckung`

Für den operativen Mahnantrag (Barcode-Datensatz, zentrales Mahnportal, EGVP/beA-Übermittlung) und
den Übergang zum Vollstreckungsbescheid samt Klausel und Zustellung lädt das freistehende Plugin
`zwangsvollstreckung` die Skills `zv-mahnbescheid-online` und `zv-vollstreckungsbescheid-folge`.
Dieser Skill liefert die dogmatische Grundlage und Strategie; das Plugin liefert das fertige
Formularpaket.

## Zweck

Dieser Skill begleitet das gerichtliche Mahnverfahren als kostengünstiges und schnelles
Verfahren zur Titulierung unstreitiger Geldforderungen. Anwendungsfelder: Forderungseinzug
bei Zahlungsverzug (Kauf-, Werk-, Darlehensverträge), Rückforderungsansprüche, titulierter
Verzugszinsanspruch. Der Skill deckt den gesamten Ablauf ab: Mahnantrag → Widerspruch →
Abgabe ins streitige Verfahren oder Vollstreckungsbescheid → Einspruch → Vollstreckung.

## Eingaben

Das Modell benötigt:

1. **Forderungsdetails**: Hauptforderung (Betrag, Entstehungsgrund), Zinsen (Verzugszinsen
   § 288 BGB; bei Verbraucher 5 % über Basiszinssatz, bei Unternehmer 9 % über Basiszinssatz),
   Mahnkosten, Auslagen
2. **Parteien**: Name, Anschrift, Rechtsform von Antragsteller und Antragsgegner
3. **Zuständigkeit**: Wohnsitz/Sitz des Antragsgegners → zuständiges Mahngericht (§ 689 ZPO)
4. **Aktuelle Situation**: Liegt bereits ein Mahnbescheid vor? Wurde Widerspruch eingelegt?
   Ist Vollstreckungsbescheid beantragt?
5. **Verjährungsstand**: Wann ist die Forderung fällig geworden? Verjährung droht?

## Rechtlicher Rahmen

### Normen

- **§ 688 ZPO** – Zulässigkeit des Mahnverfahrens (nur Geldforderungen; keine bedingten
  Forderungen; nicht gegen unbekannte Erben)
- **§ 689 ZPO** – Zuständigkeit (zentrale Mahngerichte der Länder; in Bayern: AG Coburg)
- **§ 690 ZPO** – Inhalt des Mahnantrags (Pflichtangaben: Parteien, Forderung, Zinsen,
  Entstehungsgrund kurz bezeichnet)
- **§ 692 ZPO** – Erlass des Mahnbescheids ohne Sachprüfung
- **§ 694 ZPO** – Widerspruch gegen den Mahnbescheid (binnen 2 Wochen ab Zustellung)
- **§ 696 ZPO** – Abgabe an das Streitgericht nach Widerspruch
- **§ 699 ZPO** – Antrag auf Vollstreckungsbescheid (nach Ablauf der Widerspruchsfrist oder
  nach Nicht-Einlegung des Widerspruchs; max. 6 Monate nach Zustellung des Mahnbescheids)
- **§ 700 ZPO** – Einspruch gegen den Vollstreckungsbescheid (2 Wochen ab Zustellung;
  § 700 Abs. 1 ZPO: VB steht einem Versäumnisurteil gleich)
- **§ 701 ZPO** – Weiteres Verfahren nach Einspruch
- **§ 204 Abs. 1 Nr. 3 BGB** – Verjährungshemmung durch Mahnantrag (ab Eingang beim Gericht)

### Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
  durch Mahnbescheid; § 204 Abs. 1 Nr. 3 BGB setzt voraus, dass die Forderung im Mahnantrag
  ausreichend individualisiert ist; pauschale Sammelbezeichnungen genügen nicht und hemmen
  die Verjährung nicht.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
  anforderung im Mahnverfahren; der Entstehungsgrund muss so bezeichnet sein, dass der
  Antragsgegner die Forderung zuordnen kann; Verweis auf "Lieferscheine" ohne Nummer
  unzureichend.

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Ablauf

1. **Zulässigkeitsprüfung** (§ 688 ZPO): Ist die Forderung eine bezifferte Geldforderung?
   Keine aufschiebende Bedingung? Kein Auslandsaufenthalt des Antragsgegners (§ 688 Abs. 2 ZPO)?
2. **Verjährungsprüfung** (§§ 195, 199 BGB): Verjährungsfrist bereits abgelaufen oder kurz
   vor Ablauf? → Sofortiger Mahnantrag zur Hemmung (§ 204 Abs. 1 Nr. 3 BGB).
3. **Mahnantrag** (§ 690 ZPO) über www.online-mahnantrag.de:
   - Pflichtangaben: Antragsteller/Gegner (vollständig), Forderungsbetrag, Entstehungsgrund
     (Vertragstyp + Datum), Zinsen (Fälligkeitsdatum + Zinssatz), Gerichtsgebühr (§ 12 GKG)
   - Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
     Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
4. **Erlass und Zustellung** (§§ 692, 693 ZPO): Gericht erlässt MB ohne Sachprüfung; Zustellung
   an Antragsgegner; 2-Wochen-Frist für Widerspruch beginnt.
5. **Widerspruch** (§ 694 ZPO): Binnen 2 Wochen → Abgabe an Streitgericht (§ 696 ZPO);
   Antragsteller muss innerhalb 1 Monat Kostenvorschuss einzahlen, sonst Rücknahmefiktion.
6. **Kein Widerspruch** → Antrag auf Vollstreckungsbescheid (§ 699 ZPO) innerhalb 6 Monaten;
   VB wird zugestellt; Einspruchsfrist 2 Wochen (§ 700 ZPO).
7. **Einspruch gegen VB** (§ 700 ZPO): Verfahren wie nach Widerspruch; VB gilt als
   Versäumnisurteil (§ 700 Abs. 1 ZPO).
8. **Vollstreckung**: VB ohne Einspruch → Vollstreckungsklausel beantragen (§§ 724 ff. ZPO);
   Pfändung oder Forderungspfändung einleiten (→ Skill vollstreckung).

## Ausgabeformat

- **Checkliste** für den Mahnantrag (Pflichtangaben, Zinsen, Anlagen)
- **Mahnantragsentwurf** (kann direkt auf online-mahnantrag.de übertragen werden)
- **Rechtliches Memo** zur Verjährungshemmung und Individualisierung der Forderung
- **Widerspruchsschreiben** (falls Mandant Antragsgegner ist)

## Beispiel

**Sachverhalt**: Handwerksbetrieb H hat Malerarbeiten für Vermieter V erbracht und eine Rechnung
über EUR 4.850,00 (fällig 01.12.2024) gestellt. V zahlt nicht; ein außergerichtliches Mahnschreiben
blieb erfolglos.

**Prüfung (Urteilsstil)**:

Das Mahnverfahren ist statthaft (§ 688 Abs. 1 ZPO): Die Forderung ist auf Zahlung einer
bestimmten Geldsumme gerichtet; keine aufschiebende Bedingung; V hat Wohnsitz in Deutschland.

*Individualisierung (§ 690 Abs. 1 Nr. 3 ZPO)*: Als Entstehungsgrund ist einzutragen: "Werklohn
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
1. Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
(§ 288 Abs. 2 BGB, da V Unternehmer).

*Verjährung*: Die Forderung entstand 2024; Regelverjährung 3 Jahre (§ 195 BGB), Beginn
01.01.2025. Kein Handlungsbedarf, aber Mahnantrag hemmt Verjährung ab Eingang (§ 204 Abs. 1
Nr. 3 BGB), was vorsorglich zu nutzen ist.

## Risiken und typische Fehler

- **Unzureichende Individualisierung**: Verjährungshemmung tritt nicht ein; Vollstreckungsbescheid
  Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **Versäumte 6-Monatsfrist** für VB-Antrag: Mahnbescheid verliert Wirkung; neues Verfahren
  erforderlich; Verjährungshemmung endet (§ 204 Abs. 2 BGB).
- **Falsche Zinsen**: § 288 Abs. 1 vs. Abs. 2 BGB (Verbraucher vs. Unternehmer);
  zu hoch angesetzte Zinsen führen zu Teilvollstreckungsschutz.
- **Auslands-Antragsgegner**: § 688 Abs. 2 Nr. 2 ZPO – Mahnverfahren unzulässig →
  Klage erforderlich.
- **Berufsrecht**: Mandantendaten (Forderungsunterlagen) nur in verschlüsselter Form
  übermitteln (§ 43a Abs. 2 BRAO, § 203 StGB).

## Quellenpflicht

Jede Aussage zu Zulässigkeit, Inhalt des Mahnantrags und Verjährungswirkung ist nach
Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
Rn.). Kommentare mit Bearbeiter, Werk, Aufl., §, Rn. Keine allgemeinen Pauschalverweise.

---

<!-- AUDIT-HINWEIS 27.05.2026: Halluzinierte BGH-Zitate entfernt (NOT_FOUND oder WRONG_TOPIC gemaess dejure.org-Pruefung). Betroffene AZ siehe inline-Kommentare. Frontmatter unveraendert. -->