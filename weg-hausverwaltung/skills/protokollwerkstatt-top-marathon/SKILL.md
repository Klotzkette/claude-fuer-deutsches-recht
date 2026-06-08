---
name: protokollwerkstatt-top-marathon
description: "Erstellt und prüft Protokolle für lange Eigentümerversammlungen mit vielen Tagesordnungspunkten. Trennt Aussprache, Antrag, Beschlusswortlaut, Abstimmung, Verkündung, Anlagen und Nacharbeit. Output: protokollfähige TOP-Struktur."
---

# Protokollwerkstatt für TOP-Marathons

## Fachlicher Anker

- **Normen:** §§ 535, §§ 18, § 16 Abs. 2.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Fachkern: Protokollwerkstatt für TOP-Marathons
- **Normen-/Quellenanker:** WEG §§ 18-28, 44/45, BGB-Miet-/Werkvertragsrecht, BetrKV, HeizkostenV, GEG, DSGVO und landesrechtliche Bau-/Sicherheitsfragen.
- **Entscheidende Weiche:** Trenne Beschlusskompetenz, ordnungsmäßige Verwaltung, Kostenverteilung, Anfechtungsfrist, Verwalterpflicht, Belegprüfung und Vollzug.

Anwendungsfall: eine Eigentümerversammlung viele Tagesordnungspunkte hat und das Protokoll später anfechtungsfest, verständlich und verwaltbar sein muss.

## Pro TOP erfassen

1. TOP-Nummer und Überschrift
2. Beschlussgegenstand
3. wesentliche Aussprache nur knapp
4. finaler Beschlusswortlaut
5. Abstimmungsergebnis
6. Verkündung
7. Anlagen
8. Nacharbeit: Auftrag, Frist, Verantwortliche, Kostenrahmen

## Protokollschema

```text
TOP [...]
Gegenstand:
[...]

Aussprache:
[nur wesentliche Punkte, keine Wortprotokoll-Falle]

Beschluss:
Die Gemeinschaft beschließt [...]

Abstimmung:
Ja: [...] MEA / Nein: [...] MEA / Enthaltungen: [...] MEA
Der Beschluss wurde [verkündet/nicht verkündet].

Nacharbeit:
Verwaltung: [...]
Beirat: [...]
Frist: [...]
```

## Qualitätsgate

- Beschlusswortlaut steht im Protokoll selbst oder eindeutig in Anlage.
- Abstimmung und Verkündung sind dokumentiert.
- Keine unklaren Aufträge wie "Verwalter soll sich kümmern".
- Kostenrahmen und Finanzierung sind sichtbar.
- Bei abgelehnten Beschlüssen wird ebenfalls klar protokolliert, was abgelehnt wurde.

## Schneller Arbeitsmodus

- Starte mit Objekt, Beschlussgegenstand, Einladung/Tagesordnung, Kostenverteilung, Stimmen, Eigentümerrollen und Fristen.
- Trenne Verwaltungspraxis, Beschlusskompetenz, ordnungsmäßige Verwaltung, bauliche Veraenderung, Kostenfolge und Anfechtungsrisiko.
- Bei Protokollen: Beschlusswortlaut, Abstimmungsergebnis, Verkündung, Anlagen und abweichende Auffassungen so aufnehmen, dass ein Gericht den Vorgang nachvollziehen kann.

## Ausgabeformat

- TOP/Beschlusskern.
- Formelle Risiken.
- Materielle Risiken.
- Vollzugsschritte der Verwaltung.
- Anfechtungs- oder Heilungsoptionen.

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
