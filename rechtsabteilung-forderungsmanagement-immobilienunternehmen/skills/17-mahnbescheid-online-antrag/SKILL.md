---
name: 17-mahnbescheid-online-antrag
description: "Optionale Mahnverfahren-Abzweigung für bestimmte Euro-Geldforderung prüfen. Ausschlüsse nach Paragraf 688 ZPO, Mahngericht, späteres Streitgericht, erwarteten Widerspruch, Zustellung und Verjährungshemmung trennen. Output Entscheidungsvorlage und Antragsdaten, kein automatischer Antrag."
---

# Mahnbescheid als optionale Abzweigung

## Zweck und Anwendungsfall

Dieser Skill prüft nur, ob das gerichtliche Mahnverfahren ausnahmsweise sinnvoll ist. Der Regelpfad des Plugins bleibt die strukturierte Aktenaufbereitung und anschließende Zahlungs- oder Räumungsklage.

## Bedienmodus

Arbeite für hochtrainierte Rechtsanwalts- und Notarfachangestellte, Renofas, Rechtsfachwirt:innen und Forderungsmanagement-Spezialist:innen. Sie sind keine Anwälte, aber fachlich stark. Keine abgehobene Anwaltsprosa: kurze Arbeitskarten, begründete Prüffragen, kompakte Tabellen, Ampel, Lückenliste und genau eine nächste Arbeitsaktion. Juristisch schwierige Punkte werden als Eskalation markiert, nicht versteckt.

## Eingaben

- Forderungsaufstellung und Belegmatrix.
- Korrespondenz und etwaige Mietervereinsschreiben zur Einwendungslage.
- Aktuelle Zustellanschrift aus SAP oder Meldedaten.

## Ablauf / Checkliste

1. Voraussetzungen der Abzweigung prüfen:

| Voraussetzung | Prüfung |
|---|---|
| Bestimmte Euro-Geldforderung | Hauptforderung, Zinsen und Nebenforderungen eindeutig individualisiert |
| Kein Ausschluss nach Paragraf 688 Abs. 2 ZPO | insbesondere keine noch nicht erbrachte Gegenleistung und keine erforderliche öffentliche Zustellung |
| Widerspruchsprognose | Einwendungen machen den Weg meist unzweckmäßig, sind aber kein gesetzliches Verbot |
| Anschrift sicher | aktuelle Zustellanschrift aus SAP oder Meldedaten |
| Kein Eilbedarf Räumung | sonst direkte Klage |
| Renofa will Mahnverfahren | ausdrückliche Entscheidung nach Hinweis auf Alternativen |

2. Forderung aus Mietkonto und Belegmatrix so individualisieren, dass Forderungsgrund, Zeitraum, Vertragsbezug, Hauptforderung und Zinsbeginn weder verwechselt noch später ausgetauscht werden können.
3. Mahngericht und Streitgericht getrennt bestimmen. Das Mahngericht folgt Paragraf 689 Abs. 2 und 3 ZPO sowie der landesrechtlichen Zentralisierung; der ausschließliche Gerichtsstand der Mietsache nach Paragraf 29a ZPO wird als späteres Streitgericht im Mahnantrag bezeichnet, soweit dessen Absatz 2 nicht greift.
4. Einwendungen aus Korrespondenz und Mietervereinsschreiben identifizieren. Ein erwartbarer Widerspruch spricht regelmäßig für die direkte Klage, sperrt das Mahnverfahren aber nicht automatisch; ein Mahnbescheid kann etwa zur Verjährungshemmung erwogen werden.
5. Verjährungspfad prüfen: Die Hemmung folgt aus Zustellung des individualisierten Mahnbescheids nach Paragraf 204 Abs. 1 Nr. 3 BGB. Die Rückwirkung auf den Antragseingang nach Paragraf 167 ZPO setzt eine demnächst erfolgende Zustellung voraus; Zustellanschrift, Kostenzahlung und vom Antragsteller verursachte Verzögerungen deshalb als eigenes Gate führen.
6. Zustellrisiko, Auslandsbezug und Verbot öffentlicher Zustellung im Mahnverfahren prüfen.
7. Der Renofa die Wahl zwischen direkter Klage und Mahnverfahren mit Kosten-, Zeit-, Widerspruchs- und Verjährungsfolge stellen.
8. Nur bei ausdrücklicher Wahl eine Datenliste für den Online-Mahnantrag einschließlich Mahngericht, Streitgericht, Individualisierung, Zustellanschrift und Verjährungsnotiz vorbereiten.

## Quellenpflicht

Jede juristische Aussage wird nach `references/zitierweise.md` belegt (Rechtsprechung vor Literatur, neueste zuerst); Normanker sind insbesondere Paragrafen 688, 689, 692, 696 und 697 ZPO, Paragraf 204 Abs. 1 Nr. 3 BGB, Paragraf 167 ZPO, das GKG-Kostenverzeichnis und Paragraf 29a ZPO für das spätere Streitgericht. Leitentscheidungen werden über `references/leitentscheidungen-anker.md` gesucht und live verifiziert; keine Blindzitate.

## Ausgabeformat

Entscheidungsvorlage mit Empfehlung, Paragraf-688-Gate, Mahn-/Streitgericht, Widerspruchsprognose, Zustell- und Verjährungsrisiko, benötigten Feldern und nächstem Schritt; kein automatischer Antrag ohne ausdrückliche Nutzerentscheidung. Die Entscheidungsvorlage wird in vollständigen Sätzen ausformuliert (Ausformulierungspflicht).

## Beispiele

- Unstreitiger Rückstand, sichere Anschrift, kein Räumungsbedarf: Mahnverfahren vertretbar, Datenliste wird vorbereitet.
- Mieter hat Minderung wegen Schimmels angekündigt: Mahnverfahren nicht geeignet, Empfehlung zur direkten Klage.
