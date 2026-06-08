---
name: anschluss-routing
description: "Anschluss-Routing für Forderungsmanagement Klagewerkstatt: wählt den nächsten Spezial-Skill nach Engpass (Mahnbescheid-Widerspruch 2 Wochen, Mahnung, Mahnbescheid, Vollstreckungsbescheid), dokumentiert Router-Entscheidung mit Begründung."
---

# Anschluss-Routing

Dieser Skill folgt der Kaltstart-Triage oder einem abgeschlossenen Bearbeitungsschritt. Er liefert nicht das ganze Universum sondern genau zwei oder drei Folgeoptionen.

## Routing-Matrix

| Zustand der Akte | Empfohlener Folgeskill | Alternative |
|---|---|---|
| Akte neu Schuldner privater Verbraucher Forderung dokumentiert | mahnung-aussergerichtlich-stufenmodell | mahnbescheid-online wenn Verjährung droht |
| Mahnung verstrichen Schuldner schweigt | mahnbescheid-online | zahlungsklage-erstellen wenn Streit erwartbar |
| Mahnbescheid eingelegt Widerspruch | zahlungsklage-erstellen | inkasso-risikoampel zur Aussichtspruefung |
| Vollstreckungsbescheid rechtskraeftig | vollstreckungsbescheid-folgen | zwangsvollstreckung-ueberblick |
| Urteil rechtskraeftig | zwangsvollstreckung-ueberblick | forderung-im-ausland-vollstrecken bei Auslandsbezug |
| Schuldner zahlungsunfaehig Insolvenzantrag bekannt | forderung-gegen-insolventen-schuldner | InsO-Anmeldung 174 |
| Forderung aus Urkunde Vertrag oder Scheck | urkundenprozess-pruefen | zahlungsklage-erstellen |
| Werkvertragsforderung Bau | forderung-werkvertrag-bau | mahnverfahren-bauleiter |
| Anwaltshonorar Streit ueber RVG-Rechnung | forderung-anwaltshonorar-rvg | klagefreigabe-belegte-forderung |
| Arzthonorar GOAE-Streit | forderung-arzthonorar-goae | klagefreigabe-belegte-forderung |
| Mietrueckstand | forderung-mietrueckstand-zahlungsklage | mahnbescheid-online bei reinem Zahlungsanspruch |
| Forderung gegen GmbH Geschaeftsfuehrer | forderung-gegen-gmbh-gesellschafter | zahlungsklage-erstellen |
| Auslandsbezug Schuldner im EU-Ausland | forderung-im-ausland-vollstrecken | EuMVVO oder EuGFVO via forderung-internationaler-bezug |

## Stop-Bedingungen

| Stop wenn | Begruendung |
|---|---|
| Forderung verjaehrt nach Pruefung in verjaehrung-pruefen | Klage waere unbegruendet wenn Einrede erhoben wird |
| Schuldner verstorben Erben unklar | erst Erbenermittlung dann gesonderter Skill |
| Mandant ohne Klagewunsch trotz Aussicht | Aktenvermerk nach belegte-compliance-aktenvermerk dann Wiedervorlage |

## Norm-Pinpoints

- ZPO 688 Mahnverfahren
- ZPO 794 Vollstreckungstitel-Katalog
- ZPO 808 Sachpfaendung
- InsO 174 Forderungsanmeldung
- BGB 195 Verjährung

## Quellen

- [ZPO 794](https://www.gesetze-im-internet.de/zpo/__794.html)
- [InsO 174](https://www.gesetze-im-internet.de/inso/__174.html)

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 3a RVG
- § 71 GVG
- § 19 GmbHG
- § 8 RVG
- § 4 RDGEG
- § 41 GKG
- § 13 GmbHG
- § 31 GmbHG
- § 9 RVG
- § 23a GVG
- § 23 RVG
- § 215 VVG

### Leitentscheidungen

- BGH II ZR 256/02
- BGH VII ZR 162/00
- EuGH C-377/17
- BGH VIII ZR 261/06
- BGH XI ZR 564/15

