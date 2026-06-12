---
name: abwaegungsgesetz-und-gewichtsformel-alexy
description: "Robert Alexys Gewichtsformel als praktisches Werkzeug fuer die Angemessenheits-Prüfung Stufe 4. Mit Triadenlogik leicht/mittel/schwer, Quotientenberechnung, Anwendung auf BVerfG-Faelle (Vorratsdaten, Klimaschutz, Bundesnotbremse) und Reflexion ueber Grenzen der Formalisierung."
---

# Abwaegungsgesetz und Gewichtsformel — Alexys Werkzeug für Stufe 4

## Zweck dieses Skills

Stufe 4 (Angemessenheit) wirkt oft wie Bauchgefuehl. Alexys Gewichtsformel formalisiert die Wertungen, ohne sie zu ersetzen. Wer die Formel beherrscht, kann eine Abwaegung strukturiert begruenden — in Klausur, Schriftsatz oder Gutachten.

## Das Abwaegungsgesetz

> **Je groesser der Grad der Nichterfuellung oder Beeintraechtigung des einen Prinzips ist, desto groesser muss die Wichtigkeit der Erfuellung des anderen sein.**
> *(Alexy, Theorie der Grundrechte, 2. Aufl. 1994)*

Das Gesetz hat drei Variable:

| Variable | Bedeutung |
|---|---|
| **I_i** | Intensitaet des Eingriffs in das Grundrecht (i = interferences) |
| **W_j** | Wichtigkeit der Erfuellung des gegenlaeufigen Prinzips (j = importance) |
| **P_ij** | Empirische Wahrscheinlichkeit, dass der Eingriff den gegenlaeufigen Zweck wirklich foerdert |

## Die Gewichtsformel

Vereinfacht:

```
                  I_i * G_i * P_i
  G_ij  =  --------------------------------
                  W_j * G_j * P_j
```

Praktischer mit triadischer Skala:

- I, W: **l** = leicht / **m** = mittel / **s** = schwer (Zahlenwerte 1, 2, 4 — geometrische Stufung)
- G_i, G_j: abstraktes Gewicht der Prinzipien (Wuerde = sehr hoch, Eigentum = mittel, allgemeine Handlungsfreiheit = niedriger)
- P_i, P_j: Wahrscheinlichkeit (sicher 1, wahrscheinlich 0.5, unsicher 0.25)

**Auswertung:**

- G_ij > 1: Eingriff ist gerechtfertigt (Gegenprinzip wiegt staerker).
- G_ij < 1: Eingriff ist nicht gerechtfertigt.
- G_ij ≈ 1: Patt — der Gesetzgeber hat Einschaetzungsspielraum.

## Anwendung auf BVerfG-Faelle

### Vorratsdatenspeicherung (BVerfGE 125, 260)

- **Eingriff (I_i):** schwer — Streubreite, anlasslos, gesamte Bevoelkerung, lange Speicherfrist.
- **Zweck (W_j):** mittel — abstrakte Gefahrenabwehr, ohne konkreten Verdacht.
- **Wahrscheinlichkeit (P_j):** mittel — Nutzen statistisch streitig.
- **Ergebnis:** G_ij < 1, Eingriff unverhaeltnismaessig. → BVerfG kassiert.

### Klimaschutz (BVerfGE 157, 30)

- **Eingriff in zukuenftige Freiheit (I_i):** schwer — irreversibel, generationenuebergreifend.
- **Zweck staatlichen Untaetigseins (W_j):** leicht — keine zwingenden Gegengruende.
- **Wahrscheinlichkeit (P_i):** sicher — IPCC-Daten.
- **Ergebnis:** Untermassverbot greift; Gesetzgeber muss nachbessern.

### Bundesnotbremse (BVerfGE 159, 223)

- **Eingriff in Art 2 II, 6 I GG (I_i):** schwer (Schulschliessungen, Kontaktbeschraenkung).
- **Zweck Lebensschutz (W_j):** sehr schwer.
- **Wahrscheinlichkeit (P_j):** mittel — dynamische Wissenslage.
- **Ergebnis:** G_ij > 1; Maßnahme haelt — Einschaetzungsspielraum bei Unsicherheit.

## Triadische Skala — Faustregeln für Eingriffsintensitaet

| Intensitaet | Indikatoren |
|---|---|
| **leicht (l = 1)** | Eingriff revidierbar, kurzer Zeitraum, geringer Personenkreis, kein Eingriff in Wuerde- oder Wesensgehaltsnaehe |
| **mittel (m = 2)** | Mittelfristige Bindung, mittlerer Personenkreis, beruflich/wirtschaftlich spuerbar |
| **schwer (s = 4)** | Irreversibel, großer Personenkreis, hohe Streubreite, Wesensgehalts-/Wuerdenaehe |

## Triadische Skala — Wichtigkeit

| Wichtigkeit | Indikatoren |
|---|---|
| **leicht** | Politisches Wunschziel ohne Verfassungsrang |
| **mittel** | Verfassungsguete (z. B. wirtschaftliches Wohl, Bildung) |
| **schwer** | Lebens-/Gesundheitsschutz, Wuerde Dritter, Demokratieprinzip |

## Wahrscheinlichkeit — Faustregeln

- **Sicher (1.0):** Mit nahezu Gewissheit foerdert die Maßnahme den Zweck (z. B. Anschnallpflicht senkt Verletzungen).
- **Wahrscheinlich (0.5):** Empirisch ueberwiegend belegt; Restzweifel bleiben.
- **Unsicher (0.25):** Spekulativ; Vorhersage ohne belastbare Datengrundlage.
- **Negativ (-0.5):** Maßnahme wirkt sogar kontraproduktiv. (Stufe 2 — Geeignetheit — scheitert dann schon.)

## Worked Example

**Frage:** Ist eine Speicherung von IP-Adressen ohne konkreten Verdacht zur Bekaempfung von Internetkriminalitaet verhaeltnismaessig?

| Variable | Stufe | Wert |
|---|---|---|
| I_i (Eingriff Datenschutz) | schwer | 4 |
| G_i (abstraktes Gewicht Art 2 I i. V. m. Art 1 I GG) | hoch | 4 |
| P_i (Eingriffssicherheit) | sicher | 1 |
| **Produkt** |  | **16** |
| W_j (Strafverfolgung) | mittel | 2 |
| G_j (abstraktes Gewicht Strafrechtspflege) | mittel | 2 |
| P_j (Aufklaerungserfolg) | mittel | 0.5 |
| **Produkt** |  | **2** |

G_ij = 2 / 16 = 0.125. Eingriff klar unverhaeltnismaessig. **Folge:** Maßnahme scheitert auf Stufe 4. Gesetzgeber muesste Zweckgewicht erhoehen (z. B. Beschraenkung auf schwere Straftaten + Richtervorbehalt + Loeschfrist).

## Grenzen der Formel

1. **Inkommensurabilitaet:** Wuerde und Eigentum lassen sich nicht auf einer Skala vergleichen. Antwort: Triadische Zuordnung macht Wertungen sichtbar, sie ersetzt sie nicht.
2. **Mathematisierung:** Die Formel verleitet zu Pseudo-Genauigkeit. Antwort: Sie ist Argumentationsgeruest, nicht Algorithmus.
3. **Wesensgehalt:** Wo Wuerde oder Wesensgehalt beruehrt sind, gibt es kein G_ij — die absolute Grenze schliesst Abwaegung aus.

## Wann benutzen, wann nicht

| Situation | Formel sinnvoll? |
|---|---|
| Klausur mit Zeitdruck | ja — strukturiert Argumentation in 3 Saetzen |
| Schriftsatz mit umfangreicher Abwaegung | ja — als methodisches Geruest für den Abwaegungsteil |
| Wuerde- oder Wesensgehalts-Beruehrung | nein — Formel ueberspringen, absolute Grenze prüfen |
| Beweisrechtliche Fragen | nein — Formel ist materiellrechtlich, nicht prozessual |

## Anschluss

- Theorielinie: `theorie-alexy-prinzipientheorie`
- Angemessenheits-Vertiefung: `angemessenheit-abwaegung`
- Klimaschutz / Untermassverbot: `untermassverbot-schutzpflicht-dimension`
- Wesensgehalt: `absolute-grenze-wesensgehalt-art-19-ii-gg`
