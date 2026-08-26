---
name: dokumententyp-korrespondenz
description: "Für Dokumententyp Korrespondenz: ordnet Akte, Belege und Lücken; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt."
---

# Dokumententyp Korrespondenz

## Rolle und Fokus
Erkennt Korrespondenz: E-Mails, Briefe, Aktenvermerke, Faxprotokolle, Telefonnotizen. Erfasst Absender, Empfaenger, Datum, Betreff, Bezug.

## Anwendungsbeispiel
E-Mail-Korrespondenz LEAG vom 19.05.2026: Drohung mit Pachtvertragskuendigung wegen verspaeteter Vorlage der BImSchG-Genehmigungsunterlagen. Thread enthaelt vier Mails, einen Anhang (Auflistung der vermissten Unterlagen), keine Empfangsbestaetigung; im Bezug steht § 12 Abs. 3 Pachtvertrag (Beibringungspflicht).

## Output-Module
- Eintrag in Reiter 2 mit Typ-Tag Schreiben oder Korrespondenz
- Thread-Mapping in Anmerkungsspalte
- Querverweis an `dokumententyp-erklaerungen` falls Korrespondenz tatsaechlich eine Erklaerung enthaelt

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht und Formatstandard.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig.
>
> **Schriftbild:** Wenn ein Schriftsatz, Vertrag, Memo, Beschluss, Vermerk oder sonstiges Enddokument als DOCX, PDF oder formatierter Text ausgegeben wird, ist **Times New Roman 11 pt** als Grundschrift zu verwenden. Überschriften bleiben in derselben Schrift und dürfen nur fett oder abgestuft sein. Bei reiner Markdown- oder Chat-Ausgabe wird dieser Formatwunsch als Exporthinweis aufgenommen.
>
> **Nummerierung:** Gliederung ausschließlich dezimal (`1`, `1.1`, `1.1.1` und so weiter). Keine römischen Ziffern, keine Buchstaben- oder Mischgliederung.
<!-- END ausformulierungspflicht (autogen) -->

