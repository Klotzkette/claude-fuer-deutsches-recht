# Rechtsgutachten (Entwurf): TDM-Opt-out nach § 44b UrhG — Windgassen ./. ImagineArt Inc.

**Von:** Dr. Antonia Kreidler-Bremer  
**An:** Akten 26-UMR-0084  
**Datum:** 20.01.2026  
**Betreff:** Prüfung Wirksamkeit des Opt-out, Schutzbereichsbestimmung, Haftung ImagineArt Inc.

---

## I. Sachverhalt (komprimiert)

Mira Windgassen ist Inhaberin der Urheberrechte an ca. 18.400 Lichtbildwerken, die über ihre Domain windgassen-photo.de öffentlich zugänglich gemacht wurden. Die Bilder wurden — nach gegenwärtiger Erkenntnis — in den Trainingsdatensatz LAION-5B aufgenommen, der u.a. als Grundlage für das Stable-Diffusion-Training und dessen Nachfolgeprodukte diente. ImagineArt Inc. (Delaware) betreibt den Dienst ImagineArt Pro, der nach Eigenangaben auf einem aus LAION-5B-Daten trainierten Modell basiert (Pressemitteilung ImagineArt Inc. vom 14.03.2025, Stand der Akte: Printout).

---

## II. Rechtsrahmen

### 1. § 44b UrhG — Text- und Data-Mining

§ 44b Abs. 1 UrhG (in Kraft seit 07.06.2021, Umsetzung Art. 3 und 4 DSM-RL 2019/790/EU) erlaubt das automatisierte Auslesen, Kopieren und Extrahieren von Werken zum Zwecke des Text- und Data-Mining. Diese Erlaubnis steht aber unter dem Vorbehalt, dass der Rechtsinhaber die Nutzung **nicht vorbehalten** hat (§ 44b Abs. 3 UrhG).

Der Vorbehalt muss:
- **maschinenlesbar** erklärt werden (z.B. robots.txt, Meta-Tags, Lizenzerklärungen in standardisiertem Format),
- **eindeutig** sein (nicht bloß allgemeine Nutzungsbeschränkungen),
- zum Zeitpunkt des Zugriffs **bereits vorliegen** (ex-ante-Anforderung).

### 2. Zeitpunkt der Nutzungshandlung

§ 44b UrhG gilt für Nutzungshandlungen, die **nach dem 07.06.2021** vorgenommen wurden. LAION-5B-Crawl-Zeiträume: Die öffentliche Dokumentation von LAION e.V. datiert den Hauptcrawl auf **April bis September 2021** — also zeitlich nach Inkrafttreten der Norm. Ob der spezifische Crawl-Durchgang, der Windgassens Bilder erfasste, vor oder nach dem 07.06.2021 stattfand, ist streitig und durch Serverlogdaten zu belegen (s.u.).

### 3. Wirksamkeit robots.txt als Vorbehalt

Die Mustergespräche mit der Mandantin (vgl. Aktstück 02) ergeben: Die robots.txt seit Juni 2019 enthielt:
```
User-agent: *
Disallow: /portfolio/
Disallow: /shop/
```

**Problem:** Diese Konfiguration blockiert alle Bots vom Zugriff auf `/portfolio/` und `/shop/`. Ob sämtliche Bildwerke unter diesen Pfaden lagen oder auch unter dem Root-Verzeichnis (`/`) abrufbar waren, ist unklar. Windgassen betreibt seit 2016 ein WordPress-basiertes Portfolio; Bilder können über direkte URLs (`/wp-content/uploads/`) abgerufen werden, ohne unter `/portfolio/` zu fallen.

**Rechtlich:** Das OLG Hamburg hat in frühen Entscheidungen zu Webcrawlern (betreffend Suchmaschinen) die robots.txt als technischen Schutzmechanismus i.S.v. § 95a UrhG anerkannt. Für den spezifischen Kontext § 44b Abs. 3 UrhG fehlt Rechtsprechung. Der Gesetzeswortlaut verlangt nur Maschinenlesbarkeit. Streitig ist, ob eine allgemeine `Disallow: /portfolio/` den Anforderungen genügt oder ob ein expliziter TDM-/KI-Vorbehalt erforderlich ist.

**Literatur:** Grünberger/Leenen, GRUR 2022, 805 ff. sprechen für weite Auslegung: Jede maschinenlesbar erklärte Sperrung eines Nutzungstyps, der das TDM einschließt, erfülle § 44b Abs. 3 UrhG. Die Gegenmeinung (Dreier/Schulze, § 44b Rn. 43) verlangt konkrete Benennung des TDM-Zwecks.

### 4. ai.txt-Datei (ab Oktober 2023)

Windgassen hat ab Oktober 2023 eine `ai.txt`-Datei eingerichtet (nach dem Devicex-ai-Standard, der sich an robots.txt anlehnt). Inhalt laut Screenshot (Anlage P-2):

```
# ai.txt — Windgassen Photo Atelier
# Stand: Oktober 2023

User-agent: GPTBot
Disallow: /

User-agent: CCBot
Disallow: /

User-agent: anthropic-ai
Disallow: /

User-agent: *
AI-Training: Disallow
```

**Bewertung:** Diese Datei ist für den LAION-Zeitraum (2021) **ohne Relevanz**, weil sie erst 2023 eingerichtet wurde. Sie ist aber für zukünftige Crawls und für eventuell laufende Fine-Tuning-Crawls durch ImagineArt-Subdienstleister relevant.

---

## III. Klärungsbedarf (offene Punkte)

| Punkt | Klärung | Verantwortlich |
|---|---|---|
| Genaues Crawl-Datum LAION-5B für windgassen-photo.de | Serverlog-Analyse; LAION-Dataset-Metadata-Abfrage | Forensik, Anlage P-1 |
| Welche URLs wurden gecrawlt? Nur `/portfolio/` oder auch `/wp-content/uploads/`? | Serverlog-Analyse | Forensik |
| robots.txt im Juni 2021 — welcher exakte Inhalt? Git-History / Hosting-Backup? | Anfrage an Hoster (Hetzner) | Kreidler-Bremer |
| ImagineArt Inc. — Welches Trainingsmodell genau? LAION-5B direkt oder Derivative? | Discovery USA / Letter of Request | Kreidler-Bremer |
| LAION e.V. als mögliche Mitbeklagte? | Rechtssitzprüfung (Hamburg) | Kreidler-Bremer |

---

## IV. Vorläufiges Ergebnis

Die Erfolgsaussichten einer Klage nach §§ 44b Abs. 3, 97 UrhG gegen ImagineArt Inc. sind **mittel bis gut**, sofern:
- der LAION-Crawl nach dem 07.06.2021 stattfand (Datum noch zu verifizieren),
- die robots.txt als wirksamer Vorbehalt i.S.v. § 44b Abs. 3 UrhG angesehen wird (strittig),
- die Bildwerke Windgassens nachweislich im Trainingsdatensatz enthalten waren.

Alternativstrategie: Schadensersatzklage nach § 97 Abs. 2 UrhG wegen urheberrechtlich relevanter Vervielfältigung beim Crawl, unabhängig vom Opt-out-Streit.

Streitwert (vorläufig): 150.000 EUR (entsprechend dem Hamburger Streitwertkanon für Lichtbildwerke im Bereich Spezialfotografie × 18.400 Bilder — zu diskutieren; ggf. auf repräsentative Auswahl beschränken).

---

*Dr. AKB, 20.01.2026*
