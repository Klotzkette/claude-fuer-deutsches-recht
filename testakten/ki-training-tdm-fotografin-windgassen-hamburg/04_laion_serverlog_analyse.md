# Technische Analyse: Serverlog-Auszug windgassen-photo.de und LAION-Crawl-Nachweis

**Erstellt:** 22.01.2026  
**Von:** IT-Forensik-Beraterin: Dipl.-Inf. Kerstin Barkhoff, Hamburg (beauftragt 18.01.2026)  
**Auftrag:** Nachweis des Crawl-Datums und -Umfangs für LAION-5B bezüglich windgassen-photo.de

---

## 1. Ausgangsmaterial

Hetzner Hosting hat auf Anfrage von Dr. Kreidler-Bremer (mit Vollmacht Windgassen) Serverlog-Dateien für den Zeitraum **01.01.2021 bis 31.12.2021** herausgegeben. Geliefert wurde:
- `access.log.2021.01.gz` bis `access.log.2021.12.gz` (komprimiert, gesamt ca. 4,8 GB)
- `error.log.2021.gz`
- robots.txt-Versionierung (Git-Backup auf dem Server, seit 15.06.2019)

---

## 2. Crawl-Ereignisse Identifizierung

Grep nach bekannten LAION/Common-Crawl-User-Agent-Strings:
```
CCBot/2.0
Mozilla/5.0 (compatible; CCBot/2.0; https://commoncrawl.org/faq/)
```

**Ergebnis (Auszug, relevante Treffer):**

```
2021-06-03 02:14:09 CCBot/2.0 GET /portfolio/bodden-reportage/ 200 —
2021-06-03 02:14:11 CCBot/2.0 GET /wp-content/uploads/2021/04/bodden_01.jpg 200 3.2MB
2021-06-03 02:14:14 CCBot/2.0 GET /wp-content/uploads/2021/04/bodden_02.jpg 200 2.9MB
...
2021-06-03 02:17:45 CCBot/2.0 GET /wp-content/uploads/2021/04/bodden_16.jpg 200 3.1MB

2021-08-17 04:51:22 CCBot/2.0 GET /portfolio/island-hvide-sande/ 200 —
2021-08-17 04:51:24 CCBot/2.0 GET /wp-content/uploads/2019/11/hvide_sande_portrait_01.jpg 200 2.7MB
[... weitere 143 Einträge ...]
```

**Kritisch:** Der Crawl vom **03.06.2021** fand **VOR** Inkrafttreten des § 44b UrhG (07.06.2021) statt.  
Der Crawl vom **17.08.2021** fand **NACH** Inkrafttreten statt.

---

## 3. robots.txt zum Crawl-Zeitpunkt

Aus dem Git-Backup des Webservers:

**Stand 03.06.2021 (relevanter erster Crawl):**
```
User-agent: *
Disallow: /portfolio/
Disallow: /shop/
```

**Befund:** Das `/portfolio/`-Verzeichnis war gesperrt. Der CCBot hat dennoch auf `/portfolio/bodden-reportage/` zugegriffen und HTTP 200 erhalten. Möglich: Konfigurationsfehler in der robots.txt-Implementierung des WordPress-Plugins oder CCBot hat robots.txt ignoriert.

**Zudem:** Die Bilder unter `/wp-content/uploads/` waren in der robots.txt **nicht** gesperrt. Dadurch sind die Bilddateien selbst (JPEGs) uneingeschränkt crawlbar, selbst wenn das zugehörige Portfolio-Verzeichnis gesperrt ist.

---

## 4. Bewertung: Vor/Nach § 44b UrhG

| Crawl-Datum | Vor/Nach § 44b UrhG (07.06.2021) | Anzahl gecrawlter Bilder (Schätzung) |
|---|---|---|
| 03.06.2021 | **VOR** | ca. 16–18 Bilder (Bodden-Strecke) |
| 17.08.2021 | **NACH** | ca. 143 Bilder (verschiedene Serien) |
| weitere Crawls 2021? | noch zu prüfen | — |

---

## 5. Kritische Feststellungen

1. **Der August-Crawl (nach § 44b) umfasst massiv mehr Bilder** als der Juni-Crawl.
2. Die robots.txt blockierte `/portfolio/`, aber nicht `/wp-content/uploads/`. CCBot hat beide gecrawlt (Juni trotz `Disallow: /portfolio/`).
3. Es gibt keine direkte Verlinkung zwischen dem LAION-5B-Datensatz und den hier identifizierten CCBot-Zugriffen. LAION nutzte primär Common Crawl-Daten — der Zusammenhang ist aber wahrscheinlich (CCBot ist der Common-Crawl-Bot).
4. **Weitere Untersuchung empfohlen:** Abgleich der gecrawlten URLs mit dem LAION-Dataset-Hash-Index (soweit noch zugänglich).

---

## 6. Beilage

Vollständiger gefiltter Serverlog-Auszug (redacted) als PDF-Anlage: `pdfs/serverlog_robots_txt_auszug_redacted.pdf`

---

*Barkhoff IT-Forensik, Hamburg — 22.01.2026*
