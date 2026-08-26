---
name: dokumententyp-vertraege
description: "Für Dokumententyp Verträge erkennen: ordnet Akte, Belege und Lücken; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt."
---

# Dokumententyp Verträge erkennen

## Rolle und Fokus
Erkennt Verträge als Dokumentenklasse. Pachtvertraege, Darlehensvertraege, Konsortialvertraege, Sicherungsvertraege, Gesellschaftervereinbarungen. Ordnet nach Vertragspartei, Datum, Vertragstyp.

## Anwendungsbeispiel
LausitzStorage-Vertragslandschaft: Pachtvertrag LEAG mit 2 Nachtraegen, Senior-Darlehen NordCap, Wandeldarlehen NordCap, Konsortialvertrag Stadtwerke Cottbus, Avalrahmenvertrag ILB, Netzanschluss 50Hertz. Sieben Verträge mit teils ueberlappenden Sicherheiten und Zustimmungserfordernissen — eine Vertragslandkarte vor der Reiterpflege ist Pflicht.

## Output-Module
- Vertragslandkarte (Bezugsgraph) als Vorblatt
- Eintraege in Reiter 2 mit Typ-Tag Vertrag und Untertyp
- Querverweise auf abhaengige Beschlüsse, Vollmachten und Sicherheitenbestellungen

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht und Formatstandard.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig.
>
> **Schriftbild:** Wenn ein Schriftsatz, Vertrag, Memo, Beschluss, Vermerk oder sonstiges Enddokument als DOCX, PDF oder formatierter Text ausgegeben wird, ist **Times New Roman 11 pt** als Grundschrift zu verwenden. Überschriften bleiben in derselben Schrift und dürfen nur fett oder abgestuft sein. Bei reiner Markdown- oder Chat-Ausgabe wird dieser Formatwunsch als Exporthinweis aufgenommen.
>
> **Nummerierung:** Gliederung ausschließlich dezimal (`1`, `1.1`, `1.1.1` und so weiter). Keine römischen Ziffern, keine Buchstaben- oder Mischgliederung.
<!-- END ausformulierungspflicht (autogen) -->

