# Klageandrohungsschreiben an ProcessSpark Cloud AG

**Aktenstück:** 10  
**Datum:** 12.05.2026  
**Versand:** Per Einschreiben/Rückschein und per E-Mail (legal@processspark.de)**  
**Aktenzeichen intern:** DP-2026-0506-FTM / ProcessSpark  

---

Kanzlei Drosten & Pekonkur  
Rechtsanwälte und Fachanwälte  
Schillerstraße 14  
55116 Mainz  
Telefon: +49 6131 2240-0  
Telefax: +49 6131 2240-99  
E-Mail: l.drosten@drosten-pekonkur.de

Mainz, den 12.05.2026

**Per Einschreiben mit Rückschein**

ProcessSpark Cloud AG  
— Rechtsabteilung / Vorstand —  
Leopoldstraße 88  
80802 München

---

## Schadensersatz und Vertragsstrafe aus IT-Betriebsvertrag vom 15.03.2021 (mit Nachtrag 3 vom 01.07.2024) — Ransomware-Schaden durch Verletzung der Patchpflicht CVE-2026-0712

**Unsere Mandantin:** Frischetrans Mittelrhein GmbH, Binger Straße 142, 55131 Mainz, vertreten durch GF Theresia Wallbruck

---

Sehr geehrte Damen und Herren,

wir sind anwaltliche Bevollmächtigte der Frischetrans Mittelrhein GmbH. Vollmacht liegt bei.

Wir wenden uns an Sie wegen schwerwiegender Pflichtverletzungen aus dem zwischen den Parteien bestehenden IT-Betriebsvertrag vom 15.03.2021 (Nachtrag 3 vom 01.07.2024), die zu einem erheblichen Schaden für unsere Mandantin geführt haben.

### I. Sachverhalt

Wie Ihnen bekannt ist, wurde unsere Mandantin in der Nacht vom 05. auf den 06.05.2026 Opfer eines schwerwiegenden Ransomware-Angriffs der kriminellen Gruppe „AkiraNext". Durch diesen Angriff wurden das gesamte ERP-System (SAP S/4HANA), Fileserver und Telematik-Schnittstellen vollständig verschlüsselt und ca. 2,1 TB an Unternehmensdaten — darunter Personalakten, Kundenstammdaten und Finanzdaten — exfiltriert.

Die forensische Untersuchung durch die CyberForensik RheinMain GmbH (Bericht-ID CRM-2026-FT-01, Zwischenbericht vom 09.05.2026) hat ergeben, dass der initiale Angriffseinstiegspunkt die **Sicherheitslücke CVE-2026-0712** im SAP NetWeaver Application Server ABAP war. Diese Schwachstelle war von SAP SE am **18.02.2026** als kritisch (CVSS 9.8) eingestuft und ein Patch in Form des ABAP Support Package Stack SP15 bereitgestellt worden.

Ihre Gesellschaft hat diesen Patch nach unseren Erkenntnissen erst in der **Nacht vom 28. auf den 29.04.2026** eingespielt — mithin **69 Tage** nach Veröffentlichung und Bereitstellung des Patches.

### II. Pflichtverletzungen Ihrer Gesellschaft

**1. Verletzung der Patchpflicht (§ 12 Abs. 2 Nachtrag 3)**

§ 12 Abs. 2 des Nachtrages 3 verpflichtet Ihre Gesellschaft ausdrücklich, Sicherheitspatches für Schwachstellen mit CVSS-Score ≥ 9,0 innerhalb von **14 Tagen** nach Bereitstellung durch den Hersteller einzuspielen.

Die Patchfrist für CVE-2026-0712 lief am **04.03.2026** ab. Tatsächlich wurde der Patch erst am 28./29.04.2026 eingespielt. Der Verzug beträgt damit **55 Tage**.

Diese Pflichtverletzung ist schuldhaft. Öffentliche Warnungen des BSI (BSI-2026-0312-SAP-KRITIS), von ENISA und SAP SE selbst machten die Dringlichkeit des Patches unmissverständlich deutlich. Eine schriftliche Ausnahme-Genehmigung unserer Mandantin für eine Fristverlängerung liegt nicht vor.

**2. Verletzung der Informationspflicht**

Ihre Gesellschaft hat unsere Mandantin zu keinem Zeitpunkt über die Schwachstelle CVE-2026-0712, über den Patch-Rückstand oder über mögliche Schutzmaßnahmen (Netzwerk-Segmentierung, ICM-Deaktivierung) informiert. Dies verletzt die vertragliche Schutz- und Rücksichtnahmepflicht nach § 241 Abs. 2 BGB.

Hätte unsere Mandantin von der Patchlücke gewusst, hätte sie entweder selbst Maßnahmen ergriffen oder Ihre Gesellschaft zur unverzüglichen Einspielung aufgefordert.

### III. Schaden

Der unserer Mandantin durch den Ransomware-Angriff entstandene Schaden ist kausal auf Ihre Pflichtverletzung zurückzuführen. Die Schadenshöhe beläuft sich nach derzeitigem Stand:

| Schadensposition | Betrag |
|---|---|
| IT-Wiederherstellungskosten | 198.500 EUR |
| Betriebsausfall Logistik (D+0 bis D+7) | 387.200 EUR |
| Forensikkosten (CyberForensik RheinMain GmbH) | 52.800 EUR |
| Anwaltskosten dieser Angelegenheit | 24.800 EUR (netto, bisherig) |
| DSGVO-Folgekosten (DSB, DSFA) | 18.000 EUR |
| **Vorläufige Gesamtsumme** | **681.300 EUR** |

Eine abschließende Schadensquantifizierung liegt nach Fertigstellung des forensischen Abschlussberichts vor. Wir behalten uns ausdrücklich vor, den Schadensersatzanspruch zu erhöhen.

### IV. Geltend gemachte Ansprüche

Wir machen hiermit namens und in Vollmacht unserer Mandantin folgende Ansprüche geltend:

**1. Vertragsstrafe nach § 14 Abs. 3 des Vertrages:**  
Für 7 angefangene Sieben-Tages-Perioden des Patchverzugs: 7 × 0,5 % × 14.800 EUR = **518,00 EUR**

**2. Schadensersatz nach §§ 280, 241 Abs. 2 BGB i.V.m. dem Vertrag:**  
Vorläufig **681.300,00 EUR** (vorbehaltlich der Erhöhung nach forensischem Abschlussbericht)

**3. Auskunftserteilung:**  
Vorlage sämtlicher Patch-Management-Logs, Incident-Response-Protokolle und interner Kommunikation zu CVE-2026-0712 seit dem 18.02.2026 binnen 7 Tagen (bis 19.05.2026).

**4. Ankündigung der außerordentlichen Kündigung:**  
Wir kündigen an, den IT-Betriebsvertrag vom 15.03.2021 nebst Nachtrag 3 aus wichtigem Grund (§ 626 BGB) außerordentlich und fristlos zu kündigen, sofern bis zum Ablauf der nachstehenden Frist keine Einigung erzielt wird. Ein schuldhafter Patch-Verzug von 55 Tagen bei einer CVSS-9.8-Schwachstelle, der zu einem Schaden von über 680.000 EUR führt, stellt einen wichtigen Grund dar, der eine weitere Zusammenarbeit unzumutbar macht.

### V. Frist und Konsequenzen bei Untätigkeit

Wir fordern Sie auf, die unter IV. geltend gemachten Zahlungsansprüche (Vertragsstrafe EUR 518,00 und Schadensersatz vorläufig EUR 681.300,00, gesamt **EUR 681.818,00**) bis spätestens

**Montag, den 26.05.2026**

auf das Konto unserer Mandantin (Kontoverbindung wird auf gesonderte Aufforderung mitgeteilt) zu überweisen sowie die angeforderten Unterlagen vollständig vorzulegen.

Bei fruchtlosem Fristablauf werden wir unsere Mandantin empfehlen, umgehend Klage am Landgericht Mainz zu erheben (geplantes Aktenzeichen: 3 O 88/26). Die Entscheidung über die außerordentliche Kündigung bleibt vorbehalten.

Wir weisen darauf hin, dass sich die Pönale für jeden weiteren Tag der Nichterfüllung erhöhen kann und dass Kosten eines etwaigen Rechtsstreits zu Ihren Lasten gehen.

### VI. Rechtsgrundlagen

- § 280 Abs. 1 BGB — Schadensersatz wegen Pflichtverletzung  
- § 241 Abs. 2 BGB — Schutzpflichten  
- § 254 BGB — Mitverschulden (hier: unserer Mandantin nicht anzunehmen)  
- § 626 BGB — außerordentliche Kündigung aus wichtigem Grund  
- § 339 BGB — Vertragsstrafe  
- § 340 Abs. 2 BGB — Vertragsstrafe neben Schadensersatz  
- § 12 Abs. 2 Nachtrag 3 zum Vertrag vom 15.03.2021 — Patchpflicht  
- § 14 Abs. 3 Vertrag — Pönalenregelung  

---

Mit freundlichen Grüßen

RA Lukas Drosten  
Fachanwalt für IT-Recht  
Kanzlei Drosten & Pekonkur, Mainz

*Anlage: Vollmacht der Frischetrans Mittelrhein GmbH*
