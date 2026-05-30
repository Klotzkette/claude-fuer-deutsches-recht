# 18 — Cybertrading-Warnliste für Mandant Windsysteme

**AZ:** MR-2026-1118
**Vertraulich — Nur für interne Verwendung Windsysteme Norderhof AG**
**Datum:** 19. Februar 2026
**Verfasser:** RA Dr. Mark Roosendaal, basierend auf IT-Security-Recherchen der Kanzlei

---

## 1. Hintergrund

Im Zuge der Due-Diligence zu Eickmann Wirtschaftspartner Pte. Ltd. erhielt die Kanzlei Schwingenstein und Partner Hinweise aus dem IT-Umfeld, dass eine Beteiligung von Eickmann — die Eickmann Trading DMCC (Dubai) — in der Vergangenheit in Cybertrading-Vorgänge involviert sein soll. Die Hinweise stammen aus zwei unabhängigen Quellen:

1. OSINT-Recherche durch die von Kanzlei beauftragte IT-Security-Firma Kronfeld Digital GmbH, Hamburg.
2. Informeller Hinweis eines früheren Eickmann-Angestellten (anonym, nur intern verwertbar).

---

## 2. Definition: Cybertrading im vorliegenden Kontext

Mit „Cybertrading" wird hier der Handel mit gestohlenen oder rechtswidrig erlangten Unternehmensdaten, Software-Lizenzen, IT-Zugangsdaten sowie das Anbieten von Hacker-as-a-Service-Leistungen auf Dark-Web-Plattformen bezeichnet.

**Abgrenzung:** Cybertrading ist kein definierter gesetzlicher Begriff. Der Vorwurf ist hier unbestätigt und beruht auf Hinweisen, nicht auf Beweisen.

---

## 3. Konkrete Hinweise

| Nr. | Hinweis | Quelle | Bewertung |
|---|---|---|---|
| H1 | Eickmann Trading DMCC soll 2023 Zugangsdaten eines deutschen Maschinenbauers angeboten haben | OSINT Kronfeld Digital | Unbestätigt; Ermittlungsansatz |
| H2 | IP-Adressblock der Eickmann Trading DMCC ist in Threat-Intelligence-Datenbank (Recorded Future) als C2-Infrastruktur gelistet (Stand: Dez. 2024) | Kronfeld Digital | Hinweis; kein Beweis; Datenbank-Einträge können veraltet sein |
| H3 | Ehemaliger Mitarbeiter berichtet von internen Diskussionen über „Datenverwertung außerhalb regulärer Kanäle" | Anonym | Nicht verwertbar; nur als Hintergrundinformation |

---

## 4. Rechtliche Würdigung

Die vorliegenden Hinweise reichen nicht aus für:
- Eine Strafanzeige gegen Eickmann (§ 202a ff. StGB, BDSG).
- Eine Kündigung des NDA oder den Abbruch der Verhandlungen ohne weitere Prüfung.

Die Hinweise rechtfertigen jedoch:
- Ein formelles IT-Security-Audit von Eickmanns IT-Infrastruktur als Bedingung für den Datenaustausch.
- Die Aufnahme einer Cybersecurity-Klausel in den JV-Hauptvertrag.
- Vorläufige Einschränkung des Informationsaustauschs auf nicht-kritische Kategorien.

---

## 5. Empfehlungen für Windsysteme

**Sofortmaßnahmen:**
- Kein Transfer von CAD-Daten (WN-7000, WN-9500) vor Abschluss des IT-Security-Audits.
- Einsatz eines Secure-Room-Verfahrens für kritische Daten (virtueller Datenraum mit Lesezugang ohne Download-Möglichkeit).
- Verpflichtung Eickmanns zur Vorlage eines aktuellen ISO-27001-Zertifikats oder vergleichbaren IT-Security-Nachweises.

**Mittelfristig:**
- IT-Security-Klausel in JV-Hauptvertrag: regelmäßige Penetrationstests, Incident-Response-Protokoll.
- Threat-Intelligence-Monitoring für Eickmann-Umfeld für Dauer der Zusammenarbeit.

---

## 6. Vertraulichkeitshinweis

Dieser Bericht ist ausschließlich für den internen Gebrauch von Windsysteme Norderhof AG und der Kanzlei Schwingenstein und Partner bestimmt. Eine Weitergabe an Eickmann oder Dritte ist nicht gestattet. Der Bericht begründet keine Ansprüche oder Handlungspflichten ohne ergänzende Beweise.
