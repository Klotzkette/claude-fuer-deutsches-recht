# Claude Cowork mit einem EU-Gateway verbinden

Diese Anleitung zeigt Schritt für Schritt, wie man **Claude Cowork** so einrichtet, dass die Inferenz über einen
**EU-Gateway-Anbieter** läuft. Gemeint sind hier Anbieter mit EU-Hosting, die eine **Berufsverschwiegenheitsvereinbarung** nach § 43e Abs. 3 BRAO zur Verfügung stellen können. Das tatsächliche Backend ist je nach Anbieter und Vereinbarung in der Regel **AWS Bedrock oder Google Vertex**. Welches Backend in deinem konkreten Fall verwendet wird, ist mit dem Gateway-Anbieter zwingend vor der Nutzung abzustimmen.

Die Anleitung richtet sich an **nicht-technische Nutzerinnen und Nutzer**. Alle Schritte lassen sich ohne
Programmierkenntnisse durchführen.

---

## Hinweise

- **Claude Cowork 3P befindet sich im [Research Preview](https://claude.com/docs/cowork/3p/overview).** Funktionen, Bezeichnungen und Verhalten können
  sich jederzeit ändern – einzelne Schritte heißen bei dir eventuell anders.
- Diese Anleitung erhebt **keinen Anspruch auf Vollständigkeit oder Richtigkeit**. Sie beschreibt **nur die technische Einrichtung** und ersetzt **keine rechtliche Prüfung**. Ob der Einsatz **berufsrechts- und datenschutzkonform** ist, muss **im Einzelfall** selbst geprüft werden.
- Die folgenden Angaben beziehen sich auf **Claude Desktop unter macOS**. Unter Windows funktioniert es ebenfalls, einzelne Menüpunkte können dort aber anders heißen oder an einer anderen Stelle liegen.
- Die mitgelieferte `eu-gateway-cowork.config.json` ist ein **funktionierender Ausgangspunkt**, aber **kein fertiges
Sicherheitskonzept**. Je nach **Organisation und Einsatzzweck** sind ggf. **weitere sicherheitsrelevante
Einstellungen** sinnvoll oder erforderlich (z. B. die Egress-Freigabeliste, Telemetrie-Optionen oder
Arbeitsbereich-Einschränkungen). Den **API-Key nicht** in der Datei speichern, wenn diese weitergegeben wird. **Egress-Freigabeliste (`coworkEgressAllowedHosts`):** In der mitgelieferten Config steht sie bewusst auf `"*"` (alle Hosts erlaubt), damit agentisches Arbeiten mit Web-Zugriff uneingeschränkt funktioniert. Eine Einschränkung dieser Liste beschneidet den Web-Zugriff und damit das agentische Arbeiten und sollte daher **unbedingt vorab mit der IT abgestimmt** werden.
- **AVV-Kette nach Art. 28 DSGVO beachten:** Mandant ↔ Anwalt (Verantwortlicher) ↔ Gateway-Anbieter (Auftragsverarbeiter) ↔ Backend-Anbieter (Bedrock / Vertex als Unter-Auftragsverarbeiter). Sub-Prozessor-Zustimmung nach Art. 28 Abs. 2 und 4 DSGVO erforderlich.
- **DSFA-Erwägung nach Art. 35 DSGVO:** Bei systematischer Verarbeitung von Mandantendaten je nach Risiko erforderlich.
- **Anbieterauswahl:** Diese Anleitung ist anbieterneutral. Geeignete EU-Gateways sind solche mit EU-Hosting, die einen **AVV nach Art. 28 DSGVO** und eine **Zusatzvereinbarung nach § 43e Abs. 3 BRAO i. V. m. § 203 Abs. 4 StGB** zur Verfügung stellen können. Die konkrete Anbieterauswahl, ihre vertragliche Bewertung und die Prüfung der jeweiligen Sub-Prozessor-Kette sind nicht Gegenstand dieser Anleitung.

---

## Voraussetzungen

- **Claude Desktop** ist installiert.
- Eine **passende Claude-Lizenz** für Cowork 3P (je nach Konstellation z. B. eine Team-Lizenz; ggf. ist die Einrichtung auch mit einem Free-Account möglich – bitte im eigenen Account prüfen).
- Ein **Account beim EU-Gateway-Anbieter deiner Wahl** mit einer **Lizenz, die API-Zugang erlaubt** (häufig eine Business- oder Enterprise-Lizenz – beim Anbieter prüfen).
- Mit dem Gateway-Anbieter muss – **zusätzlich** zu den Verträgen und dem **Auftragsverarbeitungsvertrag (AVV) einschließlich Begleitdokumenten** – eine **Zusatzvereinbarung zur Wahrung der anwaltlichen Verschwiegenheitspflicht** nach **§ 43e Abs. 3 BRAO i. V. m. § 203 Abs. 4 StGB** geschlossen werden.
- Die Datei **`eu-gateway-cowork.config.json`** aus diesem Ordner. **Wichtig:** Vor Verwendung muss der Platzhalter `inferenceGatewayBaseUrl` durch die konkrete Gateway-URL des gewaehlten EU-Anbieters ersetzt werden — siehe Doku des jeweiligen Anbieters für den korrekten Pfad zu den Anthropic-Modellen in der EU.

---

## Teil 1 – Beim Gateway-Anbieter: API-Key erstellen

1. Bei deinem **Gateway-Anbieter** einloggen.
2. In den **Workspace- oder Account-Einstellungen** den Bereich für **API-Zugang** öffnen (die Bezeichnung variiert pro Anbieter – häufig „API", „API-Keys" oder „Developer").
3. Einen **neuen API-Key erzeugen** und ihn **kopieren** und **sicher aufbewahren**. Du brauchst ihn gleich in Teil 4.

---

## Teil 2 – Beim Gateway-Anbieter: Anthropic-Modelle freischalten

4. In der **Modell- oder Provider-Verwaltung** des Gateway-Anbieters den Bereich für **EU-gehostete Modelle** öffnen.
5. Die gewünschten **Anthropic-Modelle aktivieren** (Sonnet, Opus, Haiku in den jeweils benötigten Versionen).
6. Sicherstellen, dass die **Base-URL** des Anbieters und der **erwartete Pfad für Anthropic-Modelle** (siehe Doku des Anbieters) bekannt sind – beides brauchst du gleich in der Config.

---

## Teil 3 – In Claude Cowork: Entwicklermenü aktivieren

8. Claude Cowork öffnen und oben auf **„Hilfe" → „Fehlerbehebung" → „Entwicklermenü einschalten"** klicken.
9. Claude Cowork einmal **neu starten**, damit das Menü erscheint.

---

## Teil 4 – Konfiguration importieren

10. In der Menüleiste den Reiter **„Entwickler"** öffnen und auf **„Drittanbieter-Inferenz konfigurieren…"** klicken.
11. Im sich öffnenden Fenster oben rechts auf das **Konfigurations-Auswahlfeld** klicken und **„Konfiguration importieren…"** wählen.
    *Falls dieser Button in deiner App-Version nicht erscheint:* Du kannst die Werte stattdessen **von Hand in die Eingabemaske eintragen** – einfach Feld für Feld entlang der `eu-gateway-cowork.config.json`. Für nicht-technische Nutzer ist das der einfachere und sicherere Weg.
12. Die Datei **`eu-gateway-cowork.config.json`** auswählen (Die Datei befindet sich hier im Repository und muss vorher auf Deinem Laptop heruntergeladen werden).
13. In der Datei die **`inferenceGatewayBaseUrl`** auf die **Base-URL deines Gateway-Anbieters** anpassen (siehe Doku des Anbieters für den korrekten Pfad zu den Anthropic-Modellen in der EU).
14. Den **API-Key aus Teil 1** in das Feld **`inferenceGatewayApiKey`** eintragen.
15. Auf **„Verbindung testen"** klicken. Wenn alles stimmt, wird die Verbindung als erfolgreich bestätigt.
16. Auf **„Änderungen übernehmen"** klicken.

**Fertig!** Du kannst in Claude Cowork jetzt oben das gewünschte Modell auswählen und loslegen.

---

## Gut zu wissen

- **Geschwindigkeitslimit:** Gateway-Anbieter haben **eigene Token-Limits pro Minute** (typischerweise im fünf- bis sechsstelligen Bereich). Für intensives, mehrschrittiges („agentisches") Arbeiten kann das Standard-Limit zu knapp sein – dann erscheint eine Limit-Meldung. Höhere Limits sind in der Regel **nur über Enterprise-Konditionen auf Anfrage** erhältlich. Konkrete Limits bitte beim gewählten Anbieter erfragen.
- **Kosten:** Die Nutzung über die API wird **nach Verbrauch** (pro Token) abgerechnet – anders als bei den
  klassischen Anthropic-Lizenzen. Der konkrete Tarif ergibt sich aus dem Vertrag mit dem Gateway-Anbieter.
- **Telemetrie:** Die mitgelieferte Config setzt `disableEssentialTelemetry`, `disableNonessentialTelemetry`, `disableNonessentialServices` und `disableAutoUpdates` auf `true`. Damit gehen keine routinemäßigen Telemetrie- und Update-Calls an Anthropic. Konversations-Inhalte selbst laufen über den Gateway zum jeweiligen Backend (Bedrock / Vertex).
