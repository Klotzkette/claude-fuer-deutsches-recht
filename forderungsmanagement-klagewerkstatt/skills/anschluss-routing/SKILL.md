---
name: anschluss-routing
description: "Für Anschluss-Routing: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: Forderungsmanagement — Klagewerkstatt."
---

# Anschluss-Routing

Dieser Skill folgt der Kaltstart-Triage oder einem abgeschlossenen Bearbeitungsschritt. Er liefert nicht das ganze Universum sondern genau zwei oder drei Folgeoptionen.

## Routing-Matrix

| Zustand der Akte | Empfohlener Folgeskill | Alternative |
|---|---|---|
| Akte neu oder Ordner/ZIP hochgeladen | aktenordner-erstlekture | dokumente-intake bei Belegchaos |
| Akte neu Schuldner privater Verbraucher Forderung dokumentiert | mahnung-aussergerichtlich-stufenmodell | mahnbescheid-online wenn Verjährung droht |
| Mahnung verstrichen Schuldner schweigt | mahnbescheid-online | zahlungsklage-erstellen wenn Streit erwartbar |
| Zahlung Aufrechnung oder dauernde Einrede nach Klageeinreichung | kostenfeststellungsklage-verzugsschaden-erledigung | Paragraf 91a ZPO oder Paragraf 269 Abs. 3 Satz 3 ZPO nur nach Zeitachsenprüfung |
| Mahnbescheid eingelegt Widerspruch | zahlungsklage-erstellen | inkasso-risikoampel zur Aussichtspruefung |
| Vollstreckungsbescheid rechtskraeftig | vollstreckungsbescheid-folgen | zwangsvollstreckung-überblick |
| Urteil rechtskraeftig | zwangsvollstreckung-überblick | forderung-im-ausland-vollstrecken bei Auslandsbezug |
| Schuldner zahlungsunfaehig Insolvenzantrag bekannt | forderung-gegen-insolventen-schuldner | InsO-Anmeldung 174 |
| Forderung aus Urkunde Vertrag oder Scheck | urkundenprozess-prüfen | zahlungsklage-erstellen |
| Werkvertragsforderung Bau | forderung-werkvertrag-bau | mahnverfahren-bauleiter |
| Anwaltshonorar Streit über RVG-Rechnung | forderung-anwaltshonorar-rvg | klagefreigabe-belegte-forderung |
| Arzthonorar GOAE-Streit | forderung-arzthonorar-goae | klagefreigabe-belegte-forderung |
| Mietrueckstand | forderung-mietrueckstand-zahlungsklage | mahnbescheid-online bei reinem Zahlungsanspruch |
| Forderung gegen GmbH Geschäftsführer | forderung-gegen-gmbh-gesellschafter | zahlungsklage-erstellen |
| Auslandsbezug Schuldner im EU-Ausland | forderung-im-ausland-vollstrecken | EuMVVO oder EuGFVO via forderung-internationaler-bezug |

## Stop-Bedingungen

| Stop wenn | Begruendung |
|---|---|
| Forderung verjaehrt nach Prüfung in verjaehrung-prüfen | Klage waere unbegruendet wenn Einrede erhoben wird |
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
