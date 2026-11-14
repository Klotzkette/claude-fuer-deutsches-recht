---
name: psd2-fraud-refund-unauthorised-payment
description: "Bearbeitet Reklamationen nicht autorisierter Zahlungen aus Sicht der Bank. Trennt unverzügliche Erstattung, Autorisierungsnachweis und späteren Regress; erstellt Kundenantwort und interne Entscheidung mit Belegen und Zuständigkeiten."
---

# 1. Zweck und Anwendungsfall

Bearbeiten Sie eine bestrittene Kontobelastung bis zur bestellten Kundenantwort und internen Entscheidung. Die Bank muss erkennen, welche Erstattung jetzt geschuldet sein kann und welche Gegenforderung erst gesondert zu begründen ist. Interne Risikofreigaben, technische Ermittlungen und Kulanz sind keine Ersatzmaßstäbe für gesetzliche Pflichten.

# 2. Eingaben

Lesen Sie Kontovertrag, Kundenstatus, Belastungen, Reklamationseingang, Bankantwort, Sperranzeige und vorhandene Logs. Je Zahlung Betrag, Empfänger, angezeigten Freigabetext, handelnde Person, Zeitpunkt und Rückflüsse erfassen. Fragen Sie nur entscheidende Lücken nach; verlangen Sie keine PIN, TAN oder erneute Bankanmeldung.

# 3. Ablauf und Checkliste

1. Trennen Sie Anmeldung, Geräteaktivierung und Zustimmung zur einzelnen Zahlung nach Paragraf 675j BGB. Eine vom Kunden bewusst selbst veranlasste Zahlung kann trotz Täuschung autorisiert sein; weder Betrugsanzeige noch erfolgreiche TAN-Prüfung beantworten die Zustimmung allein.
2. Erfassen Sie den Zeitpunkt, zu dem die Bank von der nicht autorisierten Zahlung erfahren hat. Nach Paragraf 675u BGB Erstattung und Kontowiederherstellung unverzüglich, spätestens bis zum Ende des folgenden Geschäftstags bearbeiten. Der Vorwurf grober Fahrlässigkeit verschiebt diese Pflicht nicht. Unverzügliche Kundenanzeige und Ausschlussfrist nach Paragraf 676b BGB getrennt prüfen.
3. Beruft sich ein Fachbereich auf die Betrugsverdachtsausnahme, verlangen Sie konkrete Gründe für einen Betrug des Zahlers sowie den Nachweis schriftlicher Mitteilung an die zuständige Behörde. Ein Strafverfahren gegen unbekannte Phishing-Täter genügt nicht. Bestätigt sich der Verdacht gegen den Zahler nicht, Verpflichtung unverzüglich prüfen und erfüllen.
4. Werten Sie nach Paragraf 675w BGB Authentifizierung, Aufzeichnung, Verbuchung, Störungen und unterstützende Beweismittel aus. Fehlende Unterlagen konkret anfordern, aber keine allgemeine Ermittlungsfrist statt gesetzlicher Erstattungszeit einführen. Eine automatische Ablehnung „TAN benutzt“ verwerfen.
5. Prüfen Sie den möglichen Regress nach Paragraf 675v BGB gesondert anhand Pflicht, Handlung, Vorwerfbarkeit, Kausalität und Betrag. Haftungsausschlüsse, insbesondere fehlende starke Kundenauthentifizierung und Schäden nach Sperranzeige, vor dem Haftungsbetrag prüfen. Eine tatsächliche Erstattung erlässt nicht von sich aus einen späteren begründeten Gegenanspruch. Umgekehrt ist der bloße Hinweis auf eine mögliche Gegenforderung keine ausreichende Begründung für das Zurückhalten der Erstattung.
6. Erstellen Sie ein internes Votum mit verantwortlicher Person, Betrag, Zeitpunkt, Nachweisen und konkreter Maßnahme. Führen Sie Rückholung, endgültige Gutschrift, vorläufige Buchung und Gegenforderung getrennt; nichts doppelt anrechnen. Zahlungsanweisungen, Meldungen und Kundenversand nur nach Freigabe.
7. Nach einer Bankantwort oder neuem Log die betroffene Tatsachenfrage neu bewerten, Berechnung und Kundenbrief anpassen und bis zum bestellten Ergebnis fortsetzen. Nur tatsächlich bestätigte Buchungen als ausgeführt bezeichnen. Keine erneute allgemeine Aufnahme des bekannten Falls.

# 4. Quellenpflicht

[EuGH, Urteil vom 15.10.2026, C-70/25, Tukowiecka, ECLI:EU:C:2026:852](https://curia.europa.eu/juris/document.jsf?docid=328145&doclang=DE), Randnummern 31 bis 42, 45 bis 47 und 52, amtlicher Volltext am 16. Oktober 2026 gelesen. Trägt: unverzügliche Erstattung trotz bloßen Vorwurfs grober Fahrlässigkeit und gesonderte spätere Verlustzuordnung. Trägt nicht: automatische Unautorisiertheit jeder Täuschung, endgültige Haftungsfreiheit oder ein allgemeines deutsches Aufrechnungsverbot.

Die [Quellenkarte](../../references/eugh-c-70-25-erstattung-und-regress.md) dokumentiert den amtlichen Normabgleich zu Paragrafen 675j, 675u, 675v, 675w, 675e und 676b BGB sowie die Aussagegrenzen. Im konkreten Fall aktuellen Rechtsstand und Kontovertrag prüfen; keine Literaturfundstellen aus Erinnerung einsetzen.

# 5. Ausgabeformat

Liefern Sie die bestellte Kundenantwort vollständig ausformuliert; daneben nur den erforderlichen internen Entscheidungsvermerk mit Betrag, Erfüllungszeitpunkt, Verantwortlichem und offener Regressfrage. Kein bloßes Aufgabenraster als Endprodukt. Formatstandard: Times New Roman 11 pt, dezimale Gliederung; bei Chat-Ausgabe gesonderten Exporthinweis nennen. Technische Prüfgrenzen und Quellenprotokoll gehören nicht in den versandfertigen Brief.

# 6. Beispiel

Eine Kundin wollte auf einer Verkaufsplattform nur einen Kaufpreis erhalten; über eine nachgeahmte Bankseite wurden Zugangsdaten abgegriffen und 700 EUR überwiesen. Die Bank erhält am Folgetag die Anzeige. Klären Sie die Zustimmung zur Zahlung und den Eingang. Ein Ablehnungsentwurf wegen grober Fahrlässigkeit wird in eine zutreffende Erstattungsentscheidung mit getrennter Prüfung möglicher Ersatzansprüche überführt. Ob ein solcher Anspruch tatsächlich besteht, bleibt beweisabhängig.
