# 05 DD Red Flags und Client-Fragen

> Fiktive Lehrakte. Aehnlichkeiten zu realen Transaktionen sind nicht beabsichtigt.

Dieses Dokument ist ein **Working Draft** des DD-Index aus dem virtuellen Datenraum "comet-moth-2026". Die Partnerin Adelheid von Westarp hat Hildemar K. beauftragt, jeden Befund mit (i) DD-Findung, (ii) Risiko-Einordnung, (iii) Frage an die Mandantin und (iv) moeglichem Closing-Mechanismus zu versehen. Der Datenraumindex selbst hat ueber 600 Eintraege; die nachfolgende Liste filtert die fuer Corporate-Legal-English-Didaktik relevanten Befunde.

---

## A Datenraumstruktur (Auszug, Stand 20.05.2026)

```
01_Corporate
   01_Articles_of_Association
   02_Shareholders_List
   03_Cap_Table
   04_Shareholders_Agreement
   05_Convertible_Loans
   06_Board_Minutes
   07_Powers_of_Attorney
   08_VSOP_Plan_2024
02_Commercial
   01_Customer_Contracts
   02_Supplier_Contracts
   03_Partnership_Agreements
03_IP_and_IT
   01_Patents_and_Trademarks
   02_Open_Source_Inventory
   03_Employee_IP_Assignments
   04_Contractor_IP_Assignments
04_Employment
05_Tax
06_Real_Estate
07_Litigation
08_Insurance
09_Data_Protection
```

Hildemar hat die fuer das Plugin relevanten Funde in den nachfolgenden Abschnitten zusammengefasst. Die Quelle ist immer der Datenraum, nicht externe Datenbanken.

---

## B Corporate Findings

### B.1 Gesellschafterliste vs Cap Table

| Punkt | Befund | Risiko | Massnahme |
|---|---|---|---|
| Eingereichte Gesellschafterliste | Stand Maerz 2024, ohne VSOP, ohne Wandeldarlehen | mittel | Pre-Closing-Liste durch Notar zum Stand nach Closing |
| CFO-Cap-Table | Stand Mai 2026, inkl. VSOP (Phantom) und Tante-Ermelind-Wandeldarlehen | hoch | Trennung Cap Table (wirtschaftlich) vs Gesellschafterliste (§ 40 GmbHG) sauber dokumentieren |
| Diskrepanz | Prozentwerte abweichend, weil Pool, Wandeldarlehen und VSOP eingerechnet | hoch | Reconciliation Sheet anlegen, Disclosure Schedule erstellen |

Client-Frage Olaf (CFO): "Ist die Gesellschafterliste falsch?" — Antwort: Nein, sie ist nicht falsch, sondern bildet nur den Status quo der formalen Geschaeftsanteile ab. Cap Table ist eine wirtschaftliche Projektion.

### B.2 Wandeldarlehen Tante Ermelind Capital UG

| Punkt | Befund | Risiko |
|---|---|---|
| Form | DocuSign | gering fuer das schuldrechtliche Darlehen selbst |
| Wandlung | "shall convert into Series A Preferred Shares" | hoch — Wandlung beduerfte Kapitalerhoehung mit Beurkundung § 53 GmbHG i.V.m. § 55 GmbHG |
| Definitionsverweis | "customary long-form documents" | mittel — Auslegungsstreit moeglich |
| Discount, Cap | 20 Prozent, EUR 10 Mio. | dokumentiert |
| Zinsen | 8 Prozent PIK p.a. | dokumentiert |
| Vorzeitige Rueckzahlung | nicht geregelt | offener Punkt |

Client-Frage Walburga: "Tante Ermelind glaubt, sie sei schon Gesellschafterin." — Antwort: Nein, ein Wandeldarlehen begruendet einen schuldrechtlichen Anspruch auf kuenftige Geschaeftsanteile, keine bestehende Gesellschafterstellung.

### B.3 Beirat und Board Minutes

Der Beirat hat seit Gruendung sieben Sitzungen abgehalten, aber nur drei Protokolle wurden ordentlich gefertigt. Die uebrigen liegen als Slack-Threads vor. Wenn der Series-A-SHA Reserved-Matters-Zustimmungen verlangt, muessen wir eine saubere Geschaeftsordnung und ein Protokollbuch einrichten.

### B.4 Powers of Attorney

Es existieren zwei generelle Vollmachten zugunsten Meinhards, beide notariell beurkundet 2023. Eine davon ist auf "Bankgeschaefte" beschraenkt. Im Datenraum fehlt eine aktualisierte Generalvollmacht fuer Notartermine zugunsten Adelheids. Pre-Closing erforderlich.

### B.5 VSOP-Plan 2024

Phantom-Stock-Plan, virtuelle Anteile, Vesting 48 Monate mit 12-Monats-Cliff. Aktuelle Allokation: 850.000 EUR an virtuellem Wert auf 14 Mitarbeiter, davon ein Schluesselentwickler mit 280.000 EUR. Trigger-Events: Exit. Im Datenraum kein Acceleration-Mechanismus dokumentiert.

---

## C IP Findings

### C.1 Entwicklervertrag von 2023 mit "work made for hire"

Englische Klausel: "All work product, including but not limited to source code, designs and documentation, shall be deemed work made for hire and shall vest exclusively in the Company."

Risiko: Die Rechtsfigur "work made for hire" gibt es im deutschen Urheberrecht nicht. Eine wirksame Uebertragung der ausschliesslichen Nutzungsrechte nach § 31 UrhG verlangt nach deutscher Rechtslage zumindest eine zweckorientierte Auslegung (Zweckuebertragungslehre, § 31 Abs. 5 UrhG). Die generische "work made for hire"-Klausel ist im Zweifel unwirksam fuer die hier benoetigten ausschliesslichen Rechte.

Massnahme: Pre-Closing Nachbesserungsvertrag mit den betroffenen Entwicklern, der die Rechteuebertragung nach deutschem Recht klarstellt.

### C.2 Open-Source-Inventar

Im Datenraum eine Excel-Liste mit 47 verwendeten OSS-Komponenten. Drei davon stehen unter AGPL. Risiko: Bei Distribution der Software (z.B. SaaS-Sonderfaelle) Copyleft-Effekt moeglich.

Frage an die Mandantin: Wird die Software je beim Kunden installiert oder ausschliesslich als SaaS betrieben? Die Antwort entscheidet, ob die AGPL-Komponenten neutralisiert werden muessen.

### C.3 Marken

Wortmarke "Comet Moth" angemeldet beim DPMA und EUIPO, aber im Datenraum ist nur die DPMA-Anmeldung in Bestaetigungsphase. EUIPO-Status: "Pruefungsverfahren". Risiko: gering bis mittel.

---

## D Employment Findings

### D.1 Geschaeftsfuehrer-Anstellungsvertraege

Drei Anstellungsvertraege fuer die Gruender, alle in englischer Sprache, mit deutschem Recht (Vertragsstatut). Punkte:

- Kuendigungsfrist: "six months notice". Achtung: GmbH-Geschaeftsfuehrer unterliegen nicht dem KSchG, aber besondere Schutzregelungen gelten nicht ohne weiteres analog.
- Gehalt: jeweils EUR 120.000, plus Bonus bis 30 Prozent.
- Wettbewerbsverbot post-termination: 12 Monate, Entschaedigung 50 Prozent. Series-A-Term-Sheet will 24 Monate. Frage an Partnerin: Reicht eine Ergaenzungsvereinbarung oder muss der Anstellungsvertrag neu gefasst werden?
- D&O-Versicherung: nicht erwaehnt.

### D.2 Mitarbeiter

48 Mitarbeiter, alle in Deutschland angestellt. Keine Betriebsraete. Keine Tarifbindung.

### D.3 Whistleblowing

Hinweisgebersystem nach HinSchG existiert nicht. Die Gesellschaft hat 48 Mitarbeiter, Schwellenwert 50 ist gerade nicht erreicht. Soll bei Closing dokumentiert werden ("borderline compliance").

---

## E Commercial Findings

### E.1 Enterprise-Kunde mit Change-of-Control-Klausel

Vertrag mit Mertensbrueder & Co. KG vom 14.08.2025, Auftragsvolumen 1,4 Mio. EUR p.a. Klausel: "The customer may terminate this agreement with immediate effect upon any change of control affecting more than 50 percent of the voting rights of the supplier."

Frage: Ist die Series-A-Runde ein Change of Control? — In der Regel nicht, da die Gruender vor und nach Closing weiterhin die Stimmenmehrheit auf Stammkapitalebene halten. Aber: Wenn man die Reserved Matters und den Investor-Director-Sitz wirtschaftlich einbezieht, kann ein Gericht eine andere Sicht haben. Massnahme: Vorab ein Waiver oder zumindest eine Notification an Mertensbrueder.

### E.2 Lieferantenvertraege

Ein wesentlicher Cloud-Vertrag (Frachtkosten-Cloud GmbH) hat eine 24-monatige Restlaufzeit und keine ordentliche Kuendigung. Risiko: keine.

### E.3 Partnerships

Joint-Development-Agreement mit Echolot-Beratungs-GmbH, das eine Exklusivitaet im DACH-Markt vorsieht. Risiko: Konflikt mit Northbridge-Wunsch nach internationaler Skalierung. Frage an Mandantin und ggf. Anpassung.

---

## F Tax Findings

### F.1 Wandeldarlehen Tante Ermelind

Steuerliche Behandlung der PIK-Zinsen aus Sicht der Gesellschaft: Aufwand. Aus Sicht Tante Ermelind: jaehrlich zu versteuernder Zinsertrag, ungeachtet der Faelligkeit. Im Datenraum keine Steuerbescheinigung. Frage an Tante Ermelind via Notariat: Wurden die PIK-Zinsen jaehrlich versteuert?

### F.2 § 8c KStG / § 8d KStG

Verlustvortraege Stand 31.12.2025: ca. EUR 4,2 Mio. Risiko: Series-A-Runde fuehrt zu schaedlichem Beteiligungserwerb gemaess § 8c Abs. 1 KStG bei Ueberschreitung der 50-Prozent-Schwelle. Da Northbridge plus Tante-Ermelind-Wandlung in Summe einen wesentlichen Beteiligungserwerb darstellt, ist eine Pruefung erforderlich. Optionen:

- Anwendung des fortfuehrungsgebundenen Verlustvortrags gemaess § 8d KStG (Antrag erforderlich, strikte Voraussetzungen).
- Reorganisationsklausel gemaess § 8c Abs. 1a KStG (nicht einschlaegig, da kein Sanierungsfall).
- Stille-Reserven-Klausel gemaess § 8c Abs. 1 Satz 4 ff. KStG (Pruefung).

Hildemar: "Das gehoert eigentlich an die Steuer-Praxisgruppe. Ich notiere es als DD-Red-Flag und ueberlasse den Mechanismus den Steuerleuten."

### F.3 Umsatzsteuer

Keine Auffaelligkeiten.

---

## G Litigation Findings

Eine arbeitsgerichtliche Klage einer ehemaligen Praktikantin (Streitwert EUR 8.400) anhaengig vor dem ArbG Frankfurt am Main. Risiko: gering. Disclosure noetig.

---

## H Data Protection Findings

DSGVO-Verzeichnis von Verarbeitungstaetigkeiten existiert, ist aber zwoelf Monate alt. Datenschutzbeauftragter intern bestellt (CFO Olaf), was bei 48 Mitarbeitern grundsaetzlich zulaessig ist, aber der Lead Investor wird wahrscheinlich einen externen DSB verlangen.

---

## I Insurance Findings

D&O-Versicherung existiert (Deckung EUR 3 Mio.), aber Selbstbehalt 25.000 EUR und ausdruecklicher Ausschluss "Anspruche von Gesellschaftern gegen Geschaeftsfuehrer im Zusammenhang mit Kapitalmassnahmen". Risiko: hoch bei kuenftigen Investor-Director-Sitzen. Massnahme: Side-A-Erweiterung oder neue Police vor Closing.

---

## J Fragenkatalog an die Mandantin Kunigunde

1. Heisst fully diluted, dass ich sofort weniger Anteile habe?
2. Ist Liquidation Preference nur relevant, wenn die GmbH pleitegeht?
3. Koennen wir ein englisches Investment Agreement unter deutschem Recht unterschreiben?
4. Bedeutet Bad Leaver, dass mir alles weggenommen werden kann?
5. Ist Investor Director dasselbe wie ein Beiratsmitglied?
6. Warum ist der Cap Table nicht einfach die Gesellschafterliste?
7. Was muss der Notar sehen?
8. Bedeutet "covenant", dass wir etwas versprechen — und wenn ja, wem genau?
9. Was passiert mit unseren Verlustvortraegen?
10. Wenn Mertensbrueder kuendigt, ist das ein "MAC"?
11. Tante Ermelind ist beleidigt, weil wir sie nicht beurkundet zur Gesellschafterin gemacht haben. Was sage ich ihr?
12. Wenn der Investor Director gegen den Budget-Beschluss stimmt, kann ich ihn dann ueberstimmen?

---

## K Hildemars Bewertung (intern, nicht fuer den Datenraum)

Hauptrisiken in absteigender Reihenfolge fuer das Deal-Closing:

1. IP-Rechteuebertragung "work made for hire" (kann gefixt werden, aber kostet Zeit).
2. § 8c KStG Verlustvortrag (kostet Geld, falls keine Sicherung).
3. Mertensbrueder-Change-of-Control-Klausel (Waiver erforderlich).
4. Beurkundungsbedarf der Wandlung Tante Ermelind (logistisch handhabbar, aber Notar-Slots eng).
5. Vinkulierungs-/Drag-Mehrheiten-Konflikt zwischen Satzung und Term Sheet.
6. D&O-Ausschluss "Kapitalmassnahmen" (Versicherer ansprechen).
7. AGPL-Komponenten.
8. Vesting-Reset und Cliff-Diskussion.

Empfehlung: Disclosure Schedule mit allen acht Punkten an Brackenmuir uebergeben, bevor das erste Markup zurueckkommt. Adelheid muss vor jeder Mandantenkommunikation gegenzeichnen.
