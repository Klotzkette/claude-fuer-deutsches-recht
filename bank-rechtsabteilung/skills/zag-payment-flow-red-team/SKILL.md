---
name: zag-payment-flow-red-team
description: "ZAG-Red-Team nach BaFin-Arbeitslogik: Zahlungsfluss, Positivkatalog, Ausnahmen, E-Geld, Erlaubnis, Registrierung und Anzeigen so prüfen, dass Plattform-, Wallet-, Loyalty-, Agenten- und Embedded-Finance-Modelle nicht falsch freigegeben werden."
---

# ZAG Payment-Flow Red-Team

## Zweck

Anwendungsfall: ein Bank-, FinTech-, Plattform-, Wallet-, Karten-, Loyalty-, Merchant-, Mobility- oder Embedded-Finance-Modell nach ZAG eingeordnet werden muss. Der Skill soll nicht beruhigen, sondern die aufsichtsrechtlich gefährliche Stelle finden: Wer nimmt Geld an, wer führt eine Zahlung aus, wer kontrolliert Konten oder Zahlungsinstrumente, und wer versucht, eine Ausnahme zu weit zu ziehen?

## Start in drei Minuten

1. Zeichne den Zahlungsfluss als Tabelle: Zahler, Empfänger, Bankkonto, Treuhandkonto, Wallet, Plattformkonto, Dienstleister, Zeitpunkt der Verfügungsmacht.
2. Ordne jede Rolle zu: Bank, Zahlungsinstitut, E-Geld-Institut, Agent, technischer Dienstleister, Handelsvertreter, Händler, Plattform, TPP, Kunde.
3. Prüfe zuerst § 1 Abs. 1 Satz 2 ZAG und § 1 Abs. 2 ZAG, erst danach § 2 ZAG.
4. Markiere alle Punkte, bei denen Kundengelder, Zahlungsinstrumente, Händlerakzeptanz, API-Zugriff, Kontoinformationen oder Rücktauschversprechen auftauchen.
5. Formuliere eine Go/No-Go-These und ein stärkstes BaFin-Gegenargument.

## Tatbestandsmatrix

| Prüfpunkt | Frage | Kritische Belege |
| --- | --- | --- |
| Ein-/Auszahlung | Wird Geld auf ein Zahlungskonto gebracht oder abgehoben? | Kontoauszüge, Kassenprozess, Nutzervertrag |
| Zahlungsgeschäft | Führt jemand Zahlungsvorgänge für Nutzer aus? | Zahlungsauftrag, API-Log, SEPA-/Kartenschema |
| Zahlung mit Kredit | Wird Zahlungsausführung mit Kredit/Limit verknüpft? | Kreditlinie, Limitfreigabe, Zins-/Gebührenmodell |
| Issuing/Acquiring | Wird ein Zahlungsinstrument ausgegeben oder Händlerakzeptanz gebearbeitet? | Kartenvertrag, Merchant Agreement, Wallet Terms |
| Finanztransfer | Wird Geld ohne Zahlungskonto des Zahlers/Empfängers transferiert? | Agentenprozess, Bargeldannahme, Auszahlungskette |
| Zahlungsauslösung | Löst der Dienst aus dem Zahlungskonto des Nutzers eine Zahlung aus? | Consent, Redirect, XS2A-Protokoll, TPP-Rolle |
| Kontoinformation | Werden Kontodaten aggregiert, analysiert oder im Dashboard angezeigt? | AIS-Einwilligung, Screen, Datenmodell |
| E-Geld | Entsteht ein monetärer Wert gegen Geld, elektronisch gespeichert und bei Dritten akzeptiert? | Wallet, Voucher, Token, Rücktausch, Akzeptanznetz |

## Ausnahmeprüfung nach § 2 ZAG

Behandle Ausnahmen als Verteidigungslinie, nicht als Ausgangspunkt.

| Ausnahme | Erlaubt eher | Gefährlich |
| --- | --- | --- |
| Handelsvertreter | echte Abschluss-/Verhandlungsbefugnis nur für Zahler oder Zahlungsempfänger | Plattform verhandelt faktisch für beide Seiten oder hält Geld |
| Technischer Dienstleister | reine technische Verarbeitung ohne Besitz oder Kontrolle über Gelder | Zugang zu Zahlungskonten, Freigabelogik, Treuhandkonto |
| Limited Network | klar abgegrenzte Akzeptanzstellen und professionell kontrollierter Kreis | stetig wachsendes Partnernetz, allgemeine Einsetzbarkeit |
| Limited Range | sehr schmaler Waren-/Dienstleistungskreis | Marktplatz mit breitem Sortiment |
| Sozial/Steuer | zweckgebundenes Instrument mit öffentlichem Zweck | kommerzielle Gutschein-/Benefit-Karte ohne enge Zweckbindung |
| Konzernintern | rein interne Zahlung ohne Kundengeschäft | Dritte, Franchise, Händler oder externe Nutzer rutschen hinein |

## Erlaubnis- und Registrierungsroute

- Zahlungsinstitut: Erlaubnis nach § 10 ZAG prüfen, mit Geschäftsplan, Organisationsbeschreibung, Sicherung der Kundengelder, Eigenmitteln, Geschäftsleiterunterlagen, IT/DORA, Auslagerung und GwG.
- E-Geld-Institut: Erlaubnis nach § 11 ZAG prüfen; zusätzlich Ausgabe, Rücktausch, Akzeptanzstellen, Zinsverbot und Sicherung der entgegengenommenen Gelder.
- Nur-Kontoinformationsdienst: Registrierung nach § 34 ZAG prüfen; Datenzugriff, Haftpflicht/gleichwertige Garantie, Sicherheit und Nutzerinformation dokumentieren.
- Ausnahme mit Anzeigebezug: Bei begrenzten Netzen, begrenzter Produktpalette oder elektronischen Kommunikationsnetzen Anzeige- und Veröffentlichungspflichten prüfen.
- Zweifelsfall: BaFin-/Bundesbank-Vorabklärung mit vollständiger Vertrags- und Flow-of-Funds-Dokumentation vorbereiten.

## Red-Team-Fragen der Aufsicht

1. Warum soll dieses Modell kein Zahlungsdienst sein, wenn der Nutzer wirtschaftlich gerade eine Zahlung auslösen oder empfangen will?
2. Wer trägt das Risiko, wenn Geld im Prozess hängen bleibt?
3. Kann der Anbieter einseitig steuern, wann und an wen ausgekehrt wird?
4. Ist das Akzeptanznetz wirklich begrenzt oder praktisch offen?
5. Ist der Warenkreis wirklich eng oder nur marketingmäßig hübsch beschrieben?
6. Ist der angebliche technische Dienstleister in Wahrheit Gatekeeper der Zahlung?
7. Ist ein Token/Voucher wegen Drittakzeptanz und Rücktausch eher E-Geld?

## Output

Erzeuge:

- Flow-of-Funds-Tabelle.
- ZAG-Positivkatalog mit Treffer/kein Treffer.
- Ausnahme-Red-Team mit Ampel.
- Erlaubnis-/Registrierungs-/Anzeigeweg.
- Liste der fehlenden Unterlagen für BaFin/Bundesbank.
- Entscheidungssatz für Produktfreigabe: `Go`, `Go nur mit Auflagen`, `BaFin-Vorabklärung`, `Stop bis Erlaubnisroute geklärt`.

## Quellenanker

Nutze `references/zag-dora-inhkontrolle-crr-arbeitskern.md` und prüfe vor tragenden Aussagen die aktuelle ZAG-Fassung bei Gesetze im Internet sowie das aktuelle BaFin-Merkblatt zu ZAG und Zahlungsdiensten.
