---
name: klage-aus-eigenem-skill
description: "Laufzeit-Variante der Klagewerkstatt. Setzt voraus, dass ein zuvor mit klagevorlage-aus-eigenen-mustern erzeugtes hauseigenes Klage-Plugin installiert ist (klagewerkstatt-kanzlei). Nimmt nur noch den Sachverhalt und die Beklagtenadresse entgegen, prüft online die sachliche und örtliche Zuständigkeit (justizadressen.nrw.de und justiz.de Gerichtssuche; §§ 12, 13, 29, 29c ZPO; §§ 23, 71 GVG), füllt die hauseigene Standardvorlage und liefert die fertige Klageschrift als DOCX und Markdown. Keine erneute Extraktion, kein erneuter Lernlauf."
---

# Klagewerkstatt — Laufzeit aus eigenem Skill

## Zweck

Dieser Skill ist die **Laufzeit-Variante**. Er setzt voraus, dass das hauseigene Klage-Plugin (`klagewerkstatt-<kanzlei>`) bereits installiert ist (erzeugt vom Schwester-Skill `klagevorlage-aus-eigenen-mustern`). Er extrahiert nichts mehr, sondern nimmt Sachverhalt und Beklagtenadresse entgegen, prüft online die Zuständigkeit, füllt die hauseigene Vorlage und liefert die Klageschrift.

## Ablauf

**Schritt 1 — Hausvorlage finden**
Prüfen, ob `klagewerkstatt-<slug>` installiert ist und `assets/vorlage/standardklage.md` sowie `references/hausregeln.json` enthält. Wenn nicht: höflich auf `klagevorlage-aus-eigenen-mustern` verweisen.

**Schritt 2 — Sachverhalt einsammeln**
Alle Felder, die der Schwester-Skill in Schritt 5 abfragt, in einer Liste stellen. Dokumenten-Drop akzeptieren und Felder daraus belegen.

**Schritt 3 — Zuständigkeit online prüfen (Pflicht)**
Identisch zum Schwester-Skill, Schritt 6: rechnerische sachliche Zuständigkeit (§§ 23, 71 GVG), rechtliche örtliche Zuständigkeit (§§ 12, 13, 29, 29c, 38 ZPO; ggf. Brüssel Ia VO), Online-Recherche unter `https://www.justizadressen.nrw.de/de/justiz/suche` (PLZ oder Ort) und bundesweit unter `https://www.justiz.de/onlinedienste/gerichtsverzeichnis_und_orga/index.php`. Quelle und Abrufdatum dokumentieren. BeA-SAFE-ID nachtragen.

**Schritt 4 — Klage erzeugen**
Vorlage `assets/vorlage/standardklage.md` mit Sachverhalt befüllen, DOCX über `office/docx` rendern. Anlagenliste aus `references/anlagenliste.md` ergänzen. Dateiname `Klage-<Beklagte>-<YYYYMMDD>.docx`.

**Schritt 5 — Memo (nur auf Anfrage)**

> Soll ich zusätzlich ein Kurz-Memo im Gutachtenstil mit Anspruchsgrundlagen, Beweislage und Prozessrisiken erstellen?

## Rechtlicher Rahmen

Identisch zum Schwester-Skill (siehe dort): § 253 ZPO, §§ 130, 130a, 130d ZPO, §§ 23, 71 GVG, §§ 12, 13, 29, 29c, 38 ZPO, Brüssel Ia VO 1215/2012, §§ 286, 288, 280 BGB, RVG VV.

## Ausgabeformat

1. **Klageschrift** als DOCX und Markdown.
2. **Anlage Zuständigkeitsprüfung** mit Online-Quellen und Abrufdatum.
3. **Memo** nur auf Anfrage.

## Übergabe

Wenn die Hausvorlage erkennbar veraltet ist (z. B. Zitierungen oder Gerichtsstand-Klauseln nicht mehr aktuell), zurück an `klagevorlage-aus-eigenen-mustern` zum aktualisierten Lernlauf.
