# 14 — Organisationspflichten MaRisk BA 2024

**Rechtsgrundlage:** MaRisk BA (BaFin-Rundschreiben 05/2024 (BA) vom 29. Oktober 2024)
**Geltungsbereich:** Kreditinstitute i.S.d. § 1 Abs. 1 KWG — erfasst Thalvenia Bank AG
**Prüfungsrelevanz:** AT 4.3 (Aufgaben- und Kompetenzverteilung), AT 7.1 (IT-Strategie), BTO 3 (Handelsgeschäfte)

---

## Überblick relevanter MaRisk-Module

### AT 4.3 — Aufgaben- und Kompetenzverteilung

AT 4.3.2 MaRisk verlangt eine klare Aufgaben- und Kompetenzverteilung im Institut, mit eindeutiger Abgrenzung zwischen Front-Office-Aktivitäten und Risikocontrolling. Für die Thalvenia Bank sind folgende Abgrenzungsfragen relevant:

**Problematik Eigenhandel Token TN:**
Die Eigenhandelsaktivitäten in Token TN wurden im Oktober 2024 durch den CEO und COO initiiert, ohne vorherige Genehmigung durch den CRO oder das Risikokomitee. Das interne Regelwerk sah für Kryptowerte-Eigenhandel keine spezifische Zuständigkeit vor. Die CRO (Dr. Birkenhainer) erfuhr von den Aktivitäten erst im Dezember 2024 — nach zwei Monaten aktivem Handel.

Nach AT 4.3.2 MaRisk hätte der Eigenhandel in einem neuen Instrument (Token TN) eine vorherige Produktzulassung durch ein Neues-Produkte-Prozess (NPP) erfordert, der wiederum die Risikofreigabe durch CRO und Risikokomitee voraussetzt.

**Befund BaFin:** Fehlen eines formellen NPP für Token TN-Eigenhandel; nachträgliche Dokumentation als rückdatierter NPP-Bericht ist nicht akzeptabel.

### AT 4.3.3 — Votenpflicht

Nach AT 4.3.3 MaRisk sind für wesentliche Handelsgeschäfte zwei unabhängige Voten erforderlich (Marktseite und Marktfolgeseite). Für den Eigenhandel in Token TN gibt es keine entsprechende Zweivotensystematik. Dies ist aufsichtsrechtlich problematisch, da Kryptowerte trotz ihrer Besonderheiten als Handelsgeschäfte i.S.d. MaRisk behandelt werden.

---

### AT 7.1 — IT-Strategie

AT 7.1 MaRisk verlangt eine mit der Geschäftsstrategie konsistente IT-Strategie. Die IT-Strategie der Thalvenia aus dem Jahr 2022 erwähnt MPC-Technologie und Cold-Custody-Infrastruktur. Der Cybervorfall vom Januar 2026 zeigt jedoch, dass das zugrundeliegende VPN-Gateway seit CVE-2024-21762 (publiziert November 2024) nicht gepatcht worden war — ein Prozessversagen, das auf fehlende Konsistenz zwischen IT-Strategie und Patch-Management hindeutet.

**Befund BaFin:** IT-Strategie nicht aktuell; kein Nachweis systematischen Schwachstellenmanagements für kritische Infrastrukturkomponenten.

---

### BTO 1.4 / BTO 3 — Handelsgeschäfte

BTO 3 MaRisk (in der Fassung 2024) enthält Anforderungen an Handelsgeschäfte, die analog auf Kryptowerte-Eigenhandel anzuwenden sind. Folgende Anforderungen waren beim Eigenhandel Token TN nicht erfüllt:

| Anforderung | Status |
|---|---|
| Handelslimit für Token TN | Nicht vorhanden |
| Stop-Loss-Regelung | Nicht vorhanden |
| Bewertungsmodell für illiquide Token | Marktwert-Bewertung, aber kein Modell für Marktliquidität |
| Interday-Positionsüberwachung | Nicht täglich durch CRO |
| Dokumentation Handelsstrategien | Nur informell |

---

## Auswirkungen auf das MiCAR-Verfahren

Die MaRisk-Mängel haben unmittelbare Relevanz für das MiCAR-CASP-Verfahren. Art. 68 MiCAR stellt an CASPs governance-bezogene Anforderungen, die inhaltlich mit MaRisk übereinstimmen. Wenn die BaFin MaRisk-Verstöße als Beleg für eine unzureichende interne Governance wertet, gefährdet dies den CASP-Antrag.

---

## Remediationsmaßnahmen

Das Institut hat nach Mandatserteilung an Schwertbeck Roosendaal folgende Maßnahmen zur MaRisk-Compliance ergriffen:

1. Nachträglicher NPP-Prozess für Token TN-Eigenhandel; CRO-Freigabe und Risikokomitee-Beschluss nachgeholt (April 2026).
2. Eigenhandels-Limits für Token TN: Positionslimit EUR 10 Mio., Stop-Loss bei -15 %, Daily P&L-Reporting an CRO.
3. IT-Strategie überarbeitet: Schwachstellenmanagement-Prozess formalisiert; SLA für kritische Patches: 72 Stunden nach CVE-Veröffentlichung.
4. BTO-3-konformes Zweivoten-System für Kryptowerte-Eigenhandel implementiert.

**Quellen:** bafin.de, MaRisk BA 2024, Rundschreiben 05/2024 (BA); bundesgerichtshof.de zu Bankorganisationspflichten BGH XI ZR 372/09.
