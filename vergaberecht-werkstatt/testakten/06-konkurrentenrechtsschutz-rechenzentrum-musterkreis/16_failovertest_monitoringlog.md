<!-- aktenmeta
Dokumenttyp: Beigezogener Failover-Test und Monitoringauszug
Absender: Musterkreis IT-Service - Technischer Betrieb
Empfänger: Vergabeakte RZ-2026-31 und Oberlandesgericht Düsseldorf
Datum: 28.09.2026
Aktenzeichen: RZ-2026-31 / Verg 11/26
Betreff: Testlauf der angebotenen Ausfallsicherheitskonzepte und Herkunft der Messwerte
-->
# Failover-Test, Monitoringdaten und Abweichungsprotokoll

## 1. Beiziehung und Datenherkunft

Der technische Betrieb legte am 28.09.2026 einen Export des am 05.09.2026 durchgeführten Plausibilitätstests vor. Die Vergabestelle hatte den Export zunächst in der Betriebsakte `RZ-Test-2026` und nicht in der elektronischen Vergabeakte abgelegt. Der Export wurde nun unverändert beigezogen; Erstellzeit, Benutzerkennung und Prüfsumme sind im Übergabeprotokoll dokumentiert.

Der Test simulierte den Ausfall der primären Umgebung. Er war in den Vergabeunterlagen als Plausibilisierung angekündigt. Er durfte vorhandene Angebotszusagen prüfen, aber keine bis zum Ablauf der Angebotsfrist fehlende Ressource oder Leistungszusage ergänzen.

## 2. Testaufbau

| Parameter | Festlegung |
| --- | --- |
| Testfenster | 05.09.2026, 06:00 bis 10:00 Uhr |
| Primärsystem | isolierte Referenzumgebung im Rechenzentrum Musterkreis |
| Lastprofil | 420 virtuelle Arbeitsplätze, 18 Fachverfahren, 2.4 Terabyte replizierte Testdaten |
| Messpunkt Beginn | protokollierte Freigabe der Umschaltung durch Testleitung |
| Messpunkt Ende | fachlicher Schreib-/Lesetest aller priorisierten Dienste bestanden |
| Zielwert | RTO höchstens 60 Minuten für Priorität A |
| Testleitung | Stefanie Kurth, Musterkreis IT-Service |

## 3. Ereignisprotokoll

| Zeit MESZ | CloudNord AG | Datacenter Westfalen GmbH | technische Beobachtung |
| --- | --- | --- | --- |
| 06:14:00 | Umschaltung freigegeben | Umschaltung freigegeben | identischer Start |
| 06:21:34 | VPN zum bezeichneten Standort nicht erreichbar | Replikationskanal aufgebaut | CloudNord wechselte auf temporären Labortunnel |
| 06:33:18 | Labortunnel aktiv | Datenkonsistenzprüfung abgeschlossen | Labortunnel im Angebot nicht benannt |
| 06:47:52 | erste drei Dienste gestartet | 18 Dienste gestartet | Westfalen beginnt Fachtest |
| 07:05:11 | Datenkonsistenzprüfung meldet zwei offene Volumes | Fachtest abgeschlossen | Westfalen RTO 51 Minuten 11 Sekunden |
| 07:22:40 | 16 Dienste gestartet | Abschlussprotokoll signiert | CloudNord zwei Dienste offen |
| 07:41:26 | 18 Dienste fachlich verfügbar |  | CloudNord RTO 87 Minuten 26 Sekunden |

## 4. Abweichungen in den Bewertungsunterlagen

| Aktenquelle | Aussage | Gegenbefund im Testexport |
| --- | --- | --- |
| Einzelbogen Prüfer 1 | CloudNord RTO „unter 60 Minuten nachgewiesen“ | fachlicher Endpunkt erst nach 87 Minuten 26 Sekunden |
| Konsensnotiz | Verzögerung nur durch Testumgebung des Auftraggebers | VPN-Fehler betraf den von CloudNord bezeichneten Zugang |
| Aufklärungsantwort vom 02.09.2026 | Standort Hannover betriebsbereit | regulärer VPN-Zugang am Testtag nicht nutzbar |
| Wertungsvermerk | temporärer Tunnel sei funktionsgleich | Tunnel war weder Angebotsbestandteil noch regulärer Betriebsweg |

Der Testleiter vermerkte handschriftlich, der reguläre Zugang werde „nach Carrier-Schaltung Ende September“ verfügbar. Ein Carrier-Auftrag mit Datum 24.08.2026 befindet sich in der Betriebsakte. Damit liegt ein objektives Indiz dafür vor, dass die für den regulären Umschaltweg erforderliche Verbindung bei Ablauf der Angebotsfrist am 20.08.2026 noch nicht beauftragt war.

## 5. Integritäts- und Berechtigungskontrolle

| Datei | Ursprung | SHA-256 gekürzt | Veränderung |
| --- | --- | --- | --- |
| `failover_events_05092026.csv` | Monitoring Cluster T-4 | `a91c7d08…5e42` | keine |
| `testleitung_protokoll.pdf` | Signatur Stefanie Kurth | `f4d11863…bb90` | keine |
| `vpn_gateway.log` | Gateway RG-02 | `ce66351a…a903` | Zeitzone von UTC in Lesefassung ergänzt |
| `carrier_order.pdf` | Beschaffungsakte CloudNord, vorgelegt am 02.09.2026 | `18a62f40…d3a1` | keine |

Die Lesefassung des Gateway-Logs enthält eine zusätzliche Spalte MESZ. Das UTC-Original bleibt unverändert. Der Zugang der Datacenter Westfalen GmbH zu den Unterlagen beruht ausschließlich auf der Akteneinsichtsverfügung; interne Zugangsdaten und Sicherheitsparameter sind geschwärzt.

## 6. Vergaberechtlicher Aktenbefund

Der Test beweist nicht für sich allein, dass CloudNord zum Angebotsstichtag ungeeignet war. Er konkretisiert jedoch die Frage, ob der angebotene Zweitstandort und sein regulärer Umschaltweg schon bei Fristablauf bestimmt und verfügbar waren. Die Vergabestelle muss den fristgebundenen Angebotsinhalt, den Zeitpunkt der Carrier-Bestellung, die spätere Aufklärungsantwort und die tatsächlich gemessene RTO getrennt würdigen.

Eine Neubewertung darf weder den temporären Labortunnel als angebotene Dauerlösung behandeln noch die 60-Minuten-Zusage ohne Auseinandersetzung mit dem dokumentierten Endpunkt als nachgewiesen ansehen.

Stefanie Kurth, Technischer Betrieb Musterkreis IT-Service
