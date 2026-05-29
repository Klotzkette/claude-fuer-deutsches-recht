# 05 DD Red Flags und Client-Fragen

Dieses Dokument ist ein **Working Draft** des DD-Index aus dem virtuellen Datenraum "comet-moth-2026". Die Partnerin Adelheid von Westarp hat Hildemar K. beauftragt, jeden Befund mit (i) DD-Findung, (ii) Risiko-Einordnung, (iii) Frage an die Mandantin und (iv) möglichem Closing-Mechanismus zu versehen. Der Datenraumindex selbst hat über 600 Einträge; die nachfolgende Liste filtert die für das Series-A-Closing relevanten Befunde.

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

Hildemar hat die für das Plugin relevanten Funde in den nachfolgenden Abschnitten zusammengefasst. Die Quelle ist immer der Datenraum, nicht externe Datenbanken.

---

## B Corporate Findings

### B.1 Gesellschafterliste vs Cap Table

| Punkt | Befund | Risiko | Maßnahme |
|---|---|---|---|
| Eingereichte Gesellschafterliste | Stand März 2024, ohne VSOP, ohne Wandeldarlehen | mittel | Pre-Closing-Liste durch Notar zum Stand nach Closing |
| CFO-Cap-Table | Stand Mai 2026, inkl. VSOP (Phantom) und Tante-Ermelind-Wandeldarlehen | hoch | Trennung Cap Table (wirtschaftlich) vs Gesellschafterliste (§ 40 GmbHG) sauber dokumentieren |
| Diskrepanz | Prozentwerte abweichend, weil Pool, Wandeldarlehen und VSOP eingerechnet | hoch | Reconciliation Sheet anlegen, Disclosure Schedule erstellen |

Client-Frage Olaf (CFO): "Ist die Gesellschafterliste falsch?" — Antwort: Nein, sie ist nicht falsch, sondern bildet nur den Status quo der formalen Geschäftsanteile ab. Cap Table ist eine wirtschaftliche Projektion.

### B.2 Wandeldarlehen Tante Ermelind Capital UG

| Punkt | Befund | Risiko |
|---|---|---|
| Form | DocuSign | gering für das schuldrechtliche Darlehen selbst |
| Wandlung | "shall convert into Series A Preferred Shares" | hoch — Wandlung bedürfte Kapitalerhöhung mit Beurkundung § 53 GmbHG i.V.m. § 55 GmbHG |
| Definitionsverweis | "customary long-form documents" | mittel — Auslegungsstreit möglich |
| Discount, Cap | 20 Prozent, EUR 10 Mio. | dokumentiert |
| Zinsen | 8 Prozent PIK p.a. | dokumentiert |
| Vorzeitige Rückzahlung | nicht geregelt | offener Punkt |

Client-Frage Walburga: "Tante Ermelind glaubt, sie sei schon Gesellschafterin." — Antwort: Nein, ein Wandeldarlehen begründet einen schuldrechtlichen Anspruch auf künftige Geschäftsanteile, keine bestehende Gesellschafterstellung.

### B.3 Beirat und Board Minutes

Der Beirat hat seit Gründung sieben Sitzungen abgehalten, aber nur drei Protokolle wurden ordentlich gefertigt. Die übrigen liegen als Slack-Threads vor. Wenn der Series-A-SHA Reserved-Matters-Zustimmungen verlangt, müssen wir eine saubere Geschäftsordnung und ein Protokollbuch einrichten.

### B.4 Powers of Attorney

Es existieren zwei generelle Vollmachten zugunsten Meinhards, beide notariell beurkundet 2023. Eine davon ist auf "Bankgeschäfte" beschränkt. Im Datenraum fehlt eine aktualisierte Generalvollmacht für Notartermine zugunsten Adelheids. Pre-Closing erforderlich.

### B.5 VSOP-Plan 2024

Phantom-Stock-Plan, virtuelle Anteile, Vesting 48 Monate mit 12-Monats-Cliff. Aktuelle Allokation: 850.000 EUR an virtuellem Wert auf 14 Mitarbeiter, davon ein Schlüsselentwickler mit 280.000 EUR. Trigger-Events: Exit. Im Datenraum kein Acceleration-Mechanismus dokumentiert.

---

## C IP Findings

### C.1 Entwicklervertrag von 2023 mit "work made for hire"

Englische Klausel: "All work product, including but not limited to source code, designs and documentation, shall be deemed work made for hire and shall vest exclusively in the Company."

Risiko: Die Rechtsfigur "work made for hire" gibt es im deutschen Urheberrecht nicht. Eine wirksame Übertragung der ausschließlichen Nutzungsrechte nach § 31 UrhG verlangt nach deutscher Rechtslage zumindest eine zweckorientierte Auslegung (Zweckübertragungslehre, § 31 Abs. 5 UrhG). Die generische "work made for hire"-Klausel ist im Zweifel unwirksam für die hier benötigten ausschließlichen Rechte.

Maßnahme: Pre-Closing Nachbesserungsvertrag mit den betroffenen Entwicklern, der die Rechteübertragung nach deutschem Recht klarstellt.

### C.2 Open-Source-Inventar

Im Datenraum eine Excel-Liste mit 47 verwendeten OSS-Komponenten. Drei davon stehen unter AGPL. Risiko: Bei Distribution der Software (z.B. SaaS-Sonderfälle) Copyleft-Effekt möglich.

Frage an die Mandantin: Wird die Software je beim Kunden installiert oder ausschließlich als SaaS betrieben? Die Antwort entscheidet, ob die AGPL-Komponenten neutralisiert werden müssen.

### C.3 Marken

Wortmarke "Comet Moth" angemeldet beim DPMA und EUIPO, aber im Datenraum ist nur die DPMA-Anmeldung in Bestätigungsphase. EUIPO-Status: "Prüfungsverfahren". Risiko: gering bis mittel.

---

## D Employment Findings

### D.1 Geschäftsführer-Anstellungsverträge

Drei Anstellungsverträge für die Gründer, alle in englischer Sprache, mit deutschem Recht (Vertragsstatut). Punkte:

- Kündigungsfrist: "six months notice". Achtung: GmbH-Geschäftsführer unterliegen nicht dem KSchG, aber besondere Schutzregelungen gelten nicht ohne weiteres analog.
- Gehalt: jeweils EUR 120.000, plus Bonus bis 30 Prozent.
- Wettbewerbsverbot post-termination: 12 Monate, Entschädigung 50 Prozent. Series-A-Term-Sheet will 24 Monate. Frage an Partnerin: Reicht eine Ergänzungsvereinbarung oder muss der Anstellungsvertrag neu gefasst werden?
- D&O-Versicherung: nicht erwähnt.

### D.2 Mitarbeiter

48 Mitarbeiter, alle in Deutschland angestellt. Keine Betriebsräte. Keine Tarifbindung.

### D.3 Whistleblowing

Hinweisgebersystem nach HinSchG existiert nicht. Die Gesellschaft hat 48 Mitarbeiter, Schwellenwert 50 ist gerade nicht erreicht. Soll bei Closing dokumentiert werden ("borderline compliance").

---

## E Commercial Findings

### E.1 Enterprise-Kunde mit Change-of-Control-Klausel

Vertrag mit Mertensbrüder & Co. KG vom 14.08.2025, Auftragsvolumen 1,4 Mio. EUR p.a. Klausel: "The customer may terminate this agreement with immediate effect upon any change of control affecting more than 50 percent of the voting rights of the supplier."

Frage: Ist die Series-A-Runde ein Change of Control? — In der Regel nicht, da die Gründer vor und nach Closing weiterhin die Stimmenmehrheit auf Stammkapitalebene halten. Aber: Wenn man die Reserved Matters und den Investor-Director-Sitz wirtschaftlich einbezieht, kann ein Gericht eine andere Sicht haben. Maßnahme: Vorab ein Waiver oder zumindest eine Notification an Mertensbrüder.

### E.2 Lieferantenverträge

Ein wesentlicher Cloud-Vertrag (Frachtkosten-Cloud GmbH) hat eine 24-monatige Restlaufzeit und keine ordentliche Kündigung. Risiko: keine.

### E.3 Partnerships

Joint-Development-Agreement mit Echolot-Beratungs-GmbH, das eine Exklusivität im DACH-Markt vorsieht. Risiko: Konflikt mit Northbridge-Wunsch nach internationaler Skalierung. Frage an Mandantin und ggf. Anpassung.

---

## F Tax Findings

### F.1 Wandeldarlehen Tante Ermelind

Steuerliche Behandlung der PIK-Zinsen aus Sicht der Gesellschaft: Aufwand. Aus Sicht Tante Ermelind: jährlich zu versteuernder Zinsertrag, ungeachtet der Fälligkeit. Im Datenraum keine Steuerbescheinigung. Frage an Tante Ermelind via Notariat: Wurden die PIK-Zinsen jährlich versteuert?

### F.2 § 8c KStG / § 8d KStG

Verlustvorträge Stand 31.12.2025: ca. EUR 4,2 Mio. Risiko: Series-A-Runde führt zu schädlichem Beteiligungserwerb gemäß § 8c Abs. 1 KStG bei Überschreitung der 50-Prozent-Schwelle. Da Northbridge plus Tante-Ermelind-Wandlung in Summe einen wesentlichen Beteiligungserwerb darstellt, ist eine Prüfung erforderlich. Optionen:

- Anwendung des fortführungsgebundenen Verlustvortrags gemäß § 8d KStG (Antrag erforderlich, strikte Voraussetzungen).
- Reorganisationsklausel gemäß § 8c Abs. 1a KStG (nicht einschlägig, da kein Sanierungsfall).
- Stille-Reserven-Klausel gemäß § 8c Abs. 1 Satz 4 ff. KStG (Prüfung).

Hildemar: "Das gehört eigentlich an die Steuer-Praxisgruppe. Ich notiere es als DD-Red-Flag und überlasse den Mechanismus den Steuerleuten."

### F.3 Umsatzsteuer

Keine Auffälligkeiten.

---

## G Litigation Findings

Eine arbeitsgerichtliche Klage einer ehemaligen Praktikantin (Streitwert EUR 8.400) anhängig vor dem ArbG Frankfurt am Main. Risiko: gering. Disclosure nötig.

---

## H Data Protection Findings

DSGVO-Verzeichnis von Verarbeitungstätigkeiten existiert, ist aber zwölf Monate alt. Datenschutzbeauftragter intern bestellt (CFO Olaf), was bei 48 Mitarbeitern grundsätzlich zulässig ist, aber der Lead Investor wird wahrscheinlich einen externen DSB verlangen.

---

## I Insurance Findings

D&O-Versicherung existiert (Deckung EUR 3 Mio.), aber Selbstbehalt 25.000 EUR und ausdrücklicher Ausschluss "Anspruche von Gesellschaftern gegen Geschäftsführer im Zusammenhang mit Kapitalmaßnahmen". Risiko: hoch bei künftigen Investor-Director-Sitzen. Maßnahme: Side-A-Erweiterung oder neue Police vor Closing.

---

## J Fragenkatalog an die Mandantin Kunigunde

1. Heißt fully diluted, dass ich sofort weniger Anteile habe?
2. Ist Liquidation Preference nur relevant, wenn die GmbH pleitegeht?
3. Können wir ein englisches Investment Agreement unter deutschem Recht unterschreiben?
4. Bedeutet Bad Leaver, dass mir alles weggenommen werden kann?
5. Ist Investor Director dasselbe wie ein Beiratsmitglied?
6. Warum ist der Cap Table nicht einfach die Gesellschafterliste?
7. Was muss der Notar sehen?
8. Bedeutet "covenant", dass wir etwas versprechen — und wenn ja, wem genau?
9. Was passiert mit unseren Verlustvorträgen?
10. Wenn Mertensbrüder kündigt, ist das ein "MAC"?
11. Tante Ermelind ist beleidigt, weil wir sie nicht beurkundet zur Gesellschafterin gemacht haben. Was sage ich ihr?
12. Wenn der Investor Director gegen den Budget-Beschluss stimmt, kann ich ihn dann überstimmen?

---

## K Hildemars Bewertung (intern, nicht für den Datenraum)

Hauptrisiken in absteigender Reihenfolge für das Deal-Closing:

1. IP-Rechteübertragung "work made for hire" (kann gefixt werden, aber kostet Zeit).
2. § 8c KStG Verlustvortrag (kostet Geld, falls keine Sicherung).
3. Mertensbrüder-Change-of-Control-Klausel (Waiver erforderlich).
4. Beurkundungsbedarf der Wandlung Tante Ermelind (logistisch handhabbar, aber Notar-Slots eng).
5. Vinkulierungs-/Drag-Mehrheiten-Konflikt zwischen Satzung und Term Sheet.
6. D&O-Ausschluss "Kapitalmaßnahmen" (Versicherer ansprechen).
7. AGPL-Komponenten.
8. Vesting-Reset und Cliff-Diskussion.

Empfehlung: Disclosure Schedule mit allen acht Punkten an Brackenmuir übergeben, bevor das erste Markup zurückkommt. Adelheid muss vor jeder Mandantenkommunikation gegenzeichnen.
