---
name: mahnbescheid
description: "Für Mahnverfahren – Paragrafen 688 ff. ZPO: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt."
---

# Mahnverfahren – Paragrafen 688 ff. ZPO

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Verweis auf das freistehende Plugin `zwangsvollstreckung`

Für den operativen Mahnantrag (Barcode-Datensatz, zentrales Mahnportal, EGVP/beA-Übermittlung) und
den Übergang zum Vollstreckungsbescheid samt Klausel und Zustellung lädt das freistehende Plugin
`zwangsvollstreckung` die Skills `mahnbescheid-online-mobiliar-gv` und `vollstreckungsbescheid-zv`.
Liefert die dogmatische Grundlage und Strategie; das Plugin liefert das fertige
Formularpaket.

## Eingaben

Das Modell benötigt:

1. **Forderungsdetails**: Hauptforderung (Betrag, Entstehungsgrund), Zinsen (Verzugszinsen
 Paragraf 288 BGB; bei Verbraucher 5 % über Basiszinssatz, bei Unternehmer 9 % über Basiszinssatz),
 Mahnkosten, Auslagen
2. **Parteien**: Name, Anschrift, Rechtsform von Antragsteller und Antragsgegner
3. **Zuständigkeit**: Wohnsitz/Sitz des Antragsgegners → zuständiges Mahngericht (Paragraf 689 ZPO)
4. **Aktuelle Situation**: Liegt bereits ein Mahnbescheid vor? Wurde Widerspruch eingelegt?
 Ist Vollstreckungsbescheid beantragt?
5. **Verjährungsstand**: Wann ist die Forderung fällig geworden? Verjährung droht?

## Rechtlicher Rahmen

### Normen

- **Paragraf 688 ZPO** – Zulässigkeit des Mahnverfahrens (nur Geldforderungen; keine bedingten
 Forderungen; nicht gegen unbekannte Erben)
- **Paragraf 689 ZPO** – Zuständigkeit (zentrale Mahngerichte der Länder; in Bayern: AG Coburg)
- **Paragraf 690 ZPO** – Inhalt des Mahnantrags (Pflichtangaben: Parteien, Forderung, Zinsen,
 Entstehungsgrund kurz bezeichnet)
- **Paragraf 692 ZPO** – Erlass des Mahnbescheids ohne Sachprüfung
- **Paragraf 694 ZPO** – Widerspruch gegen den Mahnbescheid (binnen 2 Wochen ab Zustellung)
- **Paragraf 696 ZPO** – Abgabe an das Streitgericht nach Widerspruch
- **Paragraf 699 ZPO** – Antrag auf Vollstreckungsbescheid (nach Ablauf der Widerspruchsfrist oder
 nach Nicht-Einlegung des Widerspruchs; max. 6 Monate nach Zustellung des Mahnbescheids)
- **Paragraf 700 ZPO** – Einspruch gegen den Vollstreckungsbescheid (2 Wochen ab Zustellung;
 Paragraf 700 Abs. 1 ZPO: VB steht einem Versäumnisurteil gleich)
- **Paragraf 701 ZPO** – Weiteres Verfahren nach Einspruch
- **Paragraf 204 Abs. 1 Nr. 3 BGB** – Verjährungshemmung durch Mahnantrag (ab Eingang beim Gericht)

### Leitentscheidungen

 durch Mahnbescheid; Paragraf 204 Abs. 1 Nr. 3 BGB setzt voraus, dass die Forderung im Mahnantrag
 ausreichend individualisiert ist; pauschale Sammelbezeichnungen genügen nicht und hemmen
 die Verjährung nicht.
 anforderung im Mahnverfahren; der Entstehungsgrund muss so bezeichnet sein, dass der
 Antragsgegner die Forderung zuordnen kann; Verweis auf "Lieferscheine" ohne Nummer
 unzureichend.

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## Ablauf

1. **Zulässigkeitsprüfung** (Paragraf 688 ZPO): Ist die Forderung eine bezifferte Geldforderung?
 Keine aufschiebende Bedingung? Kein Auslandsaufenthalt des Antragsgegners (Paragraf 688 Abs. 2 ZPO)?
2. **Verjährungsprüfung** (Paragrafen 195, 199 BGB): Verjährungsfrist bereits abgelaufen oder kurz
 vor Ablauf? → Sofortiger Mahnantrag zur Hemmung (Paragraf 204 Abs. 1 Nr. 3 BGB).
3. **Mahnantrag** (Paragraf 690 ZPO) über www.online-mahnantrag.de:
 - Pflichtangaben: Antragsteller/Gegner (vollständig), Forderungsbetrag, Entstehungsgrund
 (Vertragstyp + Datum), Zinsen (Fälligkeitsdatum + Zinssatz), Gerichtsgebühr (Paragraf 12 GKG)
 Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
4. **Erlass und Zustellung** (Paragrafen 692, 693 ZPO): Gericht erlässt MB ohne Sachprüfung; Zustellung
 an Antragsgegner; 2-Wochen-Frist für Widerspruch beginnt.
5. **Widerspruch** (Paragraf 694 ZPO): Binnen 2 Wochen → Abgabe an Streitgericht (Paragraf 696 ZPO);
 Antragsteller muss innerhalb 1 Monat Kostenvorschuss einzahlen, sonst Rücknahmefiktion.
6. **Kein Widerspruch** → Antrag auf Vollstreckungsbescheid (Paragraf 699 ZPO) innerhalb 6 Monaten;
 VB wird zugestellt; Einspruchsfrist 2 Wochen (Paragraf 700 ZPO).
7. **Einspruch gegen VB** (Paragraf 700 ZPO): Verfahren wie nach Widerspruch; VB gilt als
 Versäumnisurteil (Paragraf 700 Abs. 1 ZPO).
8. **Vollstreckung**: VB ohne Einspruch → Vollstreckungsklausel beantragen (Paragrafen 724 ff. ZPO);
 Pfändung oder Forderungspfändung einleiten (→ Skill vollstreckung).

## Beispiel

**Sachverhalt**: Handwerksbetrieb H hat Malerarbeiten für Vermieter V erbracht und eine Rechnung
über EUR 4.850,00 (fällig 01.12.2024) gestellt. V zahlt nicht; ein außergerichtliches Mahnschreiben
blieb erfolglos.

**Prüfung (Urteilsstil)**:

Das Mahnverfahren ist statthaft (Paragraf 688 Abs. 1 ZPO): Die Forderung ist auf Zahlung einer
bestimmten Geldsumme gerichtet; keine aufschiebende Bedingung; V hat Wohnsitz in Deutschland.

*Individualisierung (Paragraf 690 Abs. 1 Nr. 3 ZPO)*: Als Entstehungsgrund ist einzutragen: "Werklohn
1. Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
(Paragraf 288 Abs. 2 BGB, da V Unternehmer).

*Verjährung*: Die Forderung entstand 2024; Regelverjährung 3 Jahre (Paragraf 195 BGB), Beginn
01.01.2025. Kein Handlungsbedarf, aber Mahnantrag hemmt Verjährung ab Eingang (Paragraf 204 Abs. 1
Nr. 3 BGB), was vorsorglich zu nutzen ist.

## Risiken und typische Fehler

- **Unzureichende Individualisierung**: Verjährungshemmung tritt nicht ein; Vollstreckungsbescheid
- **Versäumte 6-Monatsfrist** für VB-Antrag: Mahnbescheid verliert Wirkung; neues Verfahren
 erforderlich; Verjährungshemmung endet (Paragraf 204 Abs. 2 BGB).
- **Falsche Zinsen**: Paragraf 288 Abs. 1 vs. Abs. 2 BGB (Verbraucher vs. Unternehmer);
 zu hoch angesetzte Zinsen führen zu Teilvollstreckungsschutz.
- **Auslands-Antragsgegner**: Paragraf 688 Abs. 2 Nr. 2 ZPO – Mahnverfahren unzulässig →
 Klage erforderlich.
- **Berufsrecht**: Mandantendaten (Forderungsunterlagen) nur in verschlüsselter Form
 übermitteln (Paragraf 43a Abs. 2 BRAO, Paragraf 203 StGB).

## Quellenpflicht

Jede Aussage zu Zulässigkeit, Inhalt des Mahnantrags und Verjährungswirkung ist nach
Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
Rn.). Kommentare mit Bearbeiter, Werk, Aufl., Paragraf, Rn. Keine allgemeinen Pauschalverweise.

---

> Quellenregel: Entscheidungen nur nach Prüfung einer amtlichen oder frei zugänglichen Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage ausgeben.
