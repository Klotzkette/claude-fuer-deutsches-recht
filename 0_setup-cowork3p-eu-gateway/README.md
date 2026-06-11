# Claude Cowork mit Langdock verbinden

Diese Anleitung zeigt Schritt für Schritt, wie man **Claude Cowork** so einrichtet, dass die Inferenz über den
**EU-Gateway von Langdock** (deutsches Unternehmen, EU-Hosting, stellt Berufsverschwiegenheitsvereinbarung zur Verfügung (§ 43e Abs. 3 BRAO)) läuft. Das tatsächliche Backend auf Langdock-Seite muss dafür je nach Modell und Vereinbarung **AWS Bedrock oder Google Vertex** sein. Das ist mit Langdock zwingend vor der Nutzung abzustimmen.

Die Anleitung richtet sich an **nicht-technische Nutzerinnen und Nutzer**. Alle Schritte lassen sich ohne
Programmierkenntnisse durchführen.

---

## Hinweise

- **Claude Cowork 3P befindet sich im [Research Preview](https://claude.com/docs/cowork/3p/overview).** Funktionen, Bezeichnungen und Verhalten können
  sich jederzeit ändern – einzelne Schritte heißen bei dir eventuell anders.
- Diese Anleitung erhebt **keinen Anspruch auf Vollständigkeit oder Richtigkeit**. Sie beschreibt **nur die technische Einrichtung** und ersetzt **keine rechtliche Prüfung**. Ob der Einsatz **berufsrechts- und datenschutzkonform** ist, muss **im Einzelfall** selbst geprüft werden.
- Die folgenden Angaben beziehen sich auf **Claude Desktop unter macOS**. Unter Windows funktioniert es ebenfalls, einzelne Menüpunkte können dort aber anders heißen oder an einer anderen Stelle liegen.
- Die mitgelieferte `langdock-cowork.config.json` ist ein **funktionierender Ausgangspunkt**, aber **kein fertiges
Sicherheitskonzept**. Je nach **Organisation und Einsatzzweck** sind ggf. **weitere sicherheitsrelevante
Einstellungen** sinnvoll oder erforderlich (z. B. die Egress-Freigabeliste, Telemetrie-Optionen oder
Arbeitsbereich-Einschränkungen). Den **API-Key nicht** in der Datei speichern, wenn diese weitergegeben wird. **Egress-Freigabeliste (`coworkEgressAllowedHosts`):** In der mitgelieferten Config steht sie bewusst auf `"*"` (alle Hosts erlaubt), damit agentisches Arbeiten mit Web-Zugriff uneingeschränkt funktioniert. Eine Einschränkung dieser Liste beschneidet den Web-Zugriff und damit das agentische Arbeiten und sollte daher **unbedingt vorab mit der IT abgestimmt** werden.
- **AVV-Kette nach Art. 28 DSGVO beachten:** Mandant ↔ Anwalt (Verantwortlicher) ↔ Langdock (Auftragsverarbeiter) ↔ Backend-Anbieter (Bedrock / Vertex als Unter-Auftragsverarbeiter). Sub-Prozessor-Zustimmung nach Art. 28 Abs. 2 und 4 DSGVO erforderlich.
- **DSFA-Erwägung nach Art. 35 DSGVO:** Bei systematischer Verarbeitung von Mandantendaten je nach Risiko erforderlich.

---

## Voraussetzungen

- **Claude Desktop** ist installiert.
- Eine **passende Claude-Lizenz** für Cowork 3P (je nach Konstellation z. B. eine Team-Lizenz; ggf. ist die Einrichtung auch mit einem Free-Account möglich – bitte im eigenen Account prüfen).
- Ein **Langdock-Account** mit **passender Lizenz** für den API-Zugang (in der Regel eine Business-Lizenz).
- Mit Langdock muss – **zusätzlich** zu den Verträgen und dem **Auftragsverarbeitungsvertrag (AVV) einschließlich Begleitdokumenten** – eine **Zusatzvereinbarung zur Wahrung der anwaltlichen Verschwiegenheitspflicht** nach **§ 43e Abs. 3 BRAO i. V. m. § 203 Abs. 4 StGB** geschlossen werden.
- Die Datei **`langdock-cowork.config.json`** aus diesem Ordner.

---

## Teil 1 – In Langdock: API-Key erstellen

1. Bei **Langdock** einloggen.
2. In der Seitenleiste oben die **Workspace Settings** (Workspace-Einstellungen) öffnen.
3. Dort (ebenfalls in der Seitenleiste) unter **„Products"** auf **„API"** klicken.
4. Auf **„Create API Key"** klicken. Den erzeugten Key **kopieren** und **sicher aufbewahren**. Du brauchst ihn gleich in Teil 4.

---

## Teil 2 – In Langdock: Modelle freischalten

5. In der Seitenleiste oben die **Workspace Settings** (Workspace-Einstellungen) öffnen.
6. Dort auf **„Workspace of Models"** gehen.
7. Unter **„Hosted in the EU"** auf den Reiter **„Anthropic"** klicken und die **Anthropic-Modelle aktivieren**.

---

## Teil 3 – In Claude Cowork: Entwicklermenü aktivieren

8. Claude Cowork öffnen und oben auf **„Hilfe" → „Fehlerbehebung" → „Entwicklermenü einschalten"** klicken.
9. Claude Cowork einmal **neu starten**, damit das Menü erscheint.

---

## Teil 4 – Konfiguration importieren

10. In der Menüleiste den Reiter **„Entwickler"** öffnen und auf **„Drittanbieter-Inferenz konfigurieren…"** klicken.
11. Im sich öffnenden Fenster oben rechts auf das **Konfigurations-Auswahlfeld** klicken und **„Konfiguration importieren…"** wählen.
    *Falls dieser Button in deiner App-Version nicht erscheint:* Du kannst die Werte stattdessen **von Hand in die Eingabemaske eintragen** – einfach Feld für Feld entlang der `langdock-cowork.config.json`. Für nicht-technische Nutzer ist das der einfachere und sicherere Weg.
12. Die Datei **`langdock-cowork.config.json`** auswählen (Die Datei befindet sich hier im Repository und muss vorher auf Deinem Laptop heruntergeladen werden).
13. Den **Langdock-API-Key** aus Teil 1 einfügen.
14. Auf **„Verbindung testen"** klicken. Wenn alles stimmt, wird die Verbindung als erfolgreich bestätigt.
15. Auf **„Änderungen übernehmen"** klicken.

**Fertig!** Du kannst in Claude Cowork jetzt oben das gewünschte Modell auswählen und loslegen.

---

## Gut zu wissen

- **Geschwindigkeitslimit:** Die Standard-API von Langdock erlaubt **60.000 Tokens pro Minute**. Für intensives,
  mehrschrittiges („agentisches") Arbeiten ist das zu wenig – dann erscheint eine Limit-Meldung. Höhere
  Limits gibt es laut Langdock nur über **Enterprise-Konditionen auf Anfrage**.
- **Kosten:** Die Nutzung über die API wird **nach Verbrauch** (pro Token) abgerechnet – anders als bei den
  klassischen Anthropic-Lizenzen.
- **Telemetrie:** Die mitgelieferte Config setzt `disableEssentialTelemetry`, `disableNonessentialTelemetry`, `disableNonessentialServices` und `disableAutoUpdates` auf `true`. Damit gehen keine routinemäßigen Telemetrie- und Update-Calls an Anthropic. Konversations-Inhalte selbst laufen über den Langdock-Gateway zum jeweiligen Backend (Bedrock / Vertex).
