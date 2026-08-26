---
name: dokumententyp-erklaerungen
description: "Für Dokumententyp einseitige Erklärungen: ordnet Akte, Belege und Lücken; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt."
---

# Dokumententyp einseitige Erklaerungen

## Rolle und Fokus
Erkennt einseitige Willenserklaerungen: Kuendigungen, Faelligstellungen, Anfechtungen, Ruecktritte, Widerrufe, Wandlungserklaerungen. Markiert besonders zugangsbeduerftige Erklaerungen.

## Anwendungsbeispiel
Drawstop-Schreiben NordCap vom 22.05.2026: einseitige Erklaerung der Auszahlungsverweigerung gestuetzt auf 'material adverse change' und 'documentation gaps'. Versand per E-Mail an Bauernfeind; Zugangsnachweis fehlt; Vertretungsbefugnis des Unterzeichners (NordCap-Investment-Director) ist im Senior-Darlehensvertrag nicht eindeutig geregelt.

## Output-Module
- Eintrag in Reiter 2 mit Typ-Tag Erklaerung und Untertyp
- Pflicht-Querverweis an `zugang-zustellung-pruefung`
- Bei Vollmachtsfrage: Querverweis an `unterschriftspruefung`

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht und Formatstandard.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig.
>
> **Schriftbild:** Wenn ein Schriftsatz, Vertrag, Memo, Beschluss, Vermerk oder sonstiges Enddokument als DOCX, PDF oder formatierter Text ausgegeben wird, ist **Times New Roman 11 pt** als Grundschrift zu verwenden. Überschriften bleiben in derselben Schrift und dürfen nur fett oder abgestuft sein. Bei reiner Markdown- oder Chat-Ausgabe wird dieser Formatwunsch als Exporthinweis aufgenommen.
>
> **Nummerierung:** Gliederung ausschließlich dezimal (`1`, `1.1`, `1.1.1` und so weiter). Keine römischen Ziffern, keine Buchstaben- oder Mischgliederung.
<!-- END ausformulierungspflicht (autogen) -->

