# BFF-Beratungsprotokoll — Windgassen / KI-Training-Problematik

**Datum:** 18.10.2023 (Notiz retrograd aufgenommen; Windgassen hat Dokument erst 14.01.2026 übergeben)  
**Veranstaltung:** BFF-Seminar „KI und Fotorecht", Hamburg Harbour Front, 17.–18.10.2023  
**Referent:** RA Dr. Holger Pfeffer-Schwab, München (Urheberrecht/KI)  
**Teilnehmerin:** Mira Windgassen  

---

## Persönliche Beratungsnotiz (handschriftlich von Windgassen, transkribiert)

*Transkription durch Kanzlei Kreidler-Bremer, 14.01.2026:*

---

Nach dem Seminar habe ich kurz mit Dr. Pfeffer-Schwab gesprochen. Er meinte:

- robots.txt allein reicht **möglicherweise nicht** für den KI-Opt-out nach § 44b UrhG, weil der Gesetzgeber noch keine Standardisierung vorgeschrieben hat.
- Man sollte **ai.txt** einrichten (das Devicex-Modell), aber auch in den Bildunterschriften und in den Metadaten/IPTC-Feldern der JPEGs einen Vermerk aufnehmen: „No AI training".
- Er hat empfohlen, die **VG Bild-Kunst** zu kontaktieren, die gerade an Musterformulierungen für den Opt-out arbeite.
- Er hat auf die **LAION-Problematik** hingewiesen: Falls Bilder bereits drin sind, sei der Opt-out ex nunc — rückwirkend kein Schutz.

Ich habe das dann im Oktober 2023 umgesetzt:
- ai.txt eingerichtet (Standard nach Devicex.ai, Datum: 12.10.2023)
- IPTC-Keywords ergänzt in allen neuen Uploads: „No AI Training", „AI-Training: Disallow"
- Bei alten Bildern: nur teilweise nachgepflegt (ca. 8.000 von 18.400 Bildern)

Was ich vergessen habe: Den `User-agent: *` in der robots.txt um `AI-Training: Disallow` zu ergänzen (das bot das Gerät erst im Standard ab November 2023 an).

**Meine Sorge:** Die Bilder der Bodden-Reportage, die ich im März 2021 hochgeladen hatte, waren schon vor § 44b drin. Und ich weiß nicht genau, wann Common Crawl die gecrawlt hat.

---

## Einschätzung Kanzlei (Notiz Dr. AKB, 14.01.2026)

Dieses Dokument ist wertvoll:

1. Es belegt, dass Windgassen **aktiv und in gutem Glauben** Opt-out-Maßnahmen ergriffen hat — relevant für Verschuldensfrage.
2. Die Information über IPTC-Keywords in Bilddateien ist ein weiterer Vorbehaltsmechanismus, der neben robots.txt und ai.txt tritt.
3. Es belegt, dass der Opt-out **erst ab Oktober 2023** vollständig war — für Bilder, die vor diesem Zeitpunkt gecrawlt wurden, ist der Schutz zweifelhaft.
4. Widerspricht Windgassens frühere Aussage, wonach die robots.txt seit 2019 den Schutz geleistet habe — jetzt ergibt sich, dass sie selbst 2023 noch Optimierungsbedarf sah.

**Folge für Klagestrategie:** Im Schriftsatz § 44b-Opt-out primär auf den **August-2021-Crawl** (nach § 44b) und die damalige robots.txt stützen; IPTC-Keywords als weiteres Argument (zumindest ab Oktober 2023 für Fine-Tuning-Crawls relevant).

---

*Anlage: Original-Handschrift Windgassen (bei Akte, nicht digitalisiert)*  
*Transkription: Hartenberg, 14.01.2026*
