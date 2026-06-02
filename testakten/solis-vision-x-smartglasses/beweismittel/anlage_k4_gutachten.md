# Anlage K 4: Sachverstaendigengutachten

**Gutachter:** Dipl.-Ing. Tobias Reiff
öffentlich bestellt und vereidigt für Datenschutz-Technik
durch die Handelskammer Hamburg
Adolphsplatz 1, 20457 Hamburg

**Auftraggeber:** Datenschutzverein NORD e.V.
**Auftragsgegenstand:** Datenschutzrechtliche Beurteilung der Datenbrille Solis Vision X (Geräteseriennummer LO-SVX-2025-44712)
**Gutachten erstellt am:** 22. Februar 2026
**Gutachtenkosten:** 380 EUR (4 Stunden a 95 EUR netto, plus 19 Prozent Umsatzsteuer)

## I. Gegenstand der Begutachtung

Die zu begutachtende Brille wurde mir am 19. Februar 2026 in versiegelter Originalverpackung übergeben. Geräteseriennummer LO-SVX-2025-44712. Firmware-Version 2.4.1 (Werkszustand).

## II. Prüfumfang

1. Kameraverhalten bei Inbetriebnahme
2. Cloud-Anbindung und Datenfluss
3. Gesichtserkennung
4. Drittlandtransfers

## III. Feststellungen

### III.1 Kameraverhalten

Die Brille verfügt über zwei Frontkameras (16 Megapixel). Bei Einschalten der Brille startet ein Buffer-Modus, der die letzten 60 Sekunden Bildmaterial in einem Ringspeicher vorhält. Dies geschieht ohne aktive Nutzerhandlung und ohne sichtbares Signal an aufgenommene Personen (keine LED, kein akustisches Signal). Die Funktion ist im Werkszustand aktiv und lässt sich nur durch einen Eingriff in die Service-Konsole (Entwicklerzugang) abschalten.

Damit verstoesst die Brille gegen Artikel 6 DSGVO (Fehlen einer Rechtsgrundlage für die Verarbeitung personenbezogener Daten Dritter) und gegen das Transparenzgebot des Artikel 5 Absatz 1 a DSGVO.

### III.2 Cloud-Anbindung

Bei jedem Einschalten der Brille verbindet sich diese mit Servern unter den Domains api.solis-vision.example. Die DNS-Auflösung ergibt Server in den Regionen AWS us-east-1 (Virginia) und AWS ap-southeast-1 (Singapur). Eine Konfiguration auf EU-Server ist im Werkszustand nicht möglich.

Per Default werden technische Telemetriedaten sowie ungefragt thumbnails der zuletzt aufgenommenen Bilder übertragen. Dies stellt eine Drittlandsuebermittlung im Sinne von Artikel 44 ff DSGVO dar.

### III.3 Gesichtserkennung

Die Brille verfügt über ein Modul "SocialAR Vision", das in Echtzeit Gesichter im Sichtfeld mit öffentlichen Quellen (LinkedIn, Instagram, Facebook, X) abgleicht und Namen sowie weitere Informationen in das rechte Sichtfeld einblendet. Dies ist eine Verarbeitung besonderer Kategorien personenbezogener Daten im Sinne von Artikel 9 Absatz 1 DSGVO (biometrische Daten zur eindeutigen Identifizierung). Eine Rechtsgrundlage nach Artikel 9 Absatz 2 DSGVO ist nicht ersichtlich.

### III.4 Drittlandtransfers

Die Drittlandtransfers in die USA und nach Singapur erfolgen ohne Standardvertragsklauseln nach Artikel 46 Absatz 2 c DSGVO. Eine Pruefung des Schutzniveaus (Transfer Impact Assessment) nach Schrems II ist nicht ersichtlich.

## IV. Zusammenfassung

Die Datenbrille Solis Vision X verstoesst in ihrem Werkszustand gegen mindestens folgende Vorschriften:

| Verstoss | Norm |
|---|---|
| Heimliche Aufnahme Dritter (Bufferring) | Artikel 6 DSGVO, Paragraf 201a StGB |
| Fehlende Aufzeichnungsanzeige | Artikel 5 Absatz 1 a DSGVO Transparenzgebot |
| Echtzeit-Gesichtserkennung | Artikel 9 DSGVO |
| Drittlandtransfer ohne SCC | Artikel 44 ff DSGVO |

Eine DSGVO-konforme Nutzung der Brille in der Europäischen Union ist mit Werkseinstellungen **nicht** möglich.

Hamburg, den 22. Februar 2026
Dipl.-Ing. Tobias Reiff
