# 1. Offline-Hilfe für Phishingfälle

Die Hilfe ordnet Zahlungsangaben, offene Nachweise, den Erstattungsweg und einen möglichen späteren Rückgriff. Sie erzeugt keine automatische Haftungsquote, Autorisierungsentscheidung oder menschliche Prozessfreigabe. Die früheren Ampelschlüssel bleiben zur technischen Lesbarkeit vorhanden; GELB bezeichnet eine offene menschliche Prüfung.

## 2. Eingabe und Verwendung

```bash
python3 phishing-vorfall-pruefer/scripts/phishing_case_gate.py --input testakten/phishing-vorfall-mayer-sparkasse-berlin/08_case_gate_input.json
```

Vorhandene Eingaben bleiben nutzbar. Ohne `authorization_status` bleibt die Zustimmung unbekannt. Zulässige Angaben sind `unknown`, `disputed`, `not_authorized` und `authorized`; sie sind Nutzerangaben, keine vom Programm verifizierten Feststellungen. Faktoren verlangen echte JSON-Wahrheitswerte. Geldbeträge müssen endlich und nichtnegativ sein. Fehlende Beträge bleiben unbekannt (`null`); bei unvollständigen Einzelbeträgen gibt es weder eine bestätigte Summe noch einen bestätigten Abgleich. Ein mitgeteilter Minutenabstand wird nur neutral übernommen. Er verlangt eine nichtnegative endliche Zahl und beweist keine rechtzeitige Anzeige.

## 3. Erstattung und späterer Rückgriff

EuGH, Urteil vom 15.10.2026, C-70/25, Rn. 31–42, 45–47 und 52, trennt unverzügliche Erstattung und spätere Verlusttragung. Das Programm setzt die Erstattungsprüfung deshalb nicht wegen einer Summe belastender Fahrlässigkeitsindikatoren auf Rot. `refund_review` ordnet die nächste Prüfung, `recourse_review` hält den möglichen Rückgriff gesondert fest. `human_release_granted` bleibt immer falsch.

Ein vorgetragener Zahlerbetrugsverdacht benötigt Gründe und Belege in `payer_fraud_suspicion`; eine behauptete Behördenmitteilung steht getrennt in `authority_notification` mit schriftlicher Form, Behörde, Datum und Beleg. Auch vollständig ausgefüllte Felder lösen nur eine rechtliche Prüfung aus. Sie beweisen weder Berechtigung noch Zuständigkeit. Ein Drittbetrug ist keine solche Ausnahme.

Die Hilfe berechnet keine Geschäftstage und keine gesetzlichen Fristen. Die alte Beispieldatei `09_case_gate_output.json` dokumentiert einen früheren Programmlauf; für einen aktuellen Arbeitsstand die Eingabe erneut ausführen. Alte Farben sind keine aktuelle Rechtseinschätzung.
