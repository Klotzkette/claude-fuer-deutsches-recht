# 1. Sicht- und Funktionsprüfung der beiden neuen Akten

Stand: 9. Oktober 2026. Zielversion: 445.35.1.

## 1.1. Native Unterlagen

Beide Akten enthalten jeweils 20 flach abgelegte Originaldateien mit zweistelligem Präfix: sechs DOCX-Dateien, sechs zugehörige PDF-Lesefassungen, sechs EML-Dateien, eine XLSX-Datei und einen Textchat. Ein DOCX/PDF-Paar führt dieselbe Nummer. Das README ist der zusätzliche Downloadindex.

Alle zwölf Dokumente wurden mit dem Dokumentrenderer über LibreOffice einzeln gerendert. Jede der zwölf resultierenden Seiten wurde als Bild visuell geprüft. Überschriften, Absätze, Grußformeln, Seitenfuß und Seitenränder sind vollständig sichtbar. Es gibt keine Rest- oder Leerseiten und keine Überlagerungen. Der Fließtext verwendet Times New Roman in 11 Punkt. Der zweisprachige Standardhinweis steht ausschließlich im README vor der Downloadtabelle.

## 1.2. Arbeitsmappen und Mailanhänge

Alle sechs Tabellenblätter wurden gerendert und visuell geprüft. Zahlen, Beschreibungen und Hinweise sind lesbar; Eingaben und Formeln sind farblich unterschieden. Die Formeln wurden mit Basiswerten, Nullwerten, fehlenden Eingaben und geänderten Daten geprüft. Danach wurden die Ausgangswerte wiederhergestellt. Ungeprüfte Gruppen werden nicht als fehlerfreie Tests ausgewiesen. Die Planspielzeiten berechnen ausdrücklich keine gesetzlichen Fristen.

Je Akte sind sieben tatsächliche Anhänge über alle sechs E-Mails verteilt. Sämtliche dekodierten Anhänge stimmen bytegenau mit den bezeichneten nativen Dateien überein. Nach der abschließenden Formatkorrektur wurden die E-Mails neu erzeugt und erneut geprüft.

## 1.3. Reproduzierbare Befunde

Die Maschinenbefunde stehen in `standards-akten-check.json`, `standards-akten-formeln.json` und `standards-akten-render.json`. Der Dateicheck dokumentiert SHA-256-Werte aller 40 Originaldateien, die Formatanzahlen, die DOCX-/PDF-Textumfänge, die Formel-Caches und jeden Mailanhang. Der Formelbericht enthält 27 erfolgreich ausgeführte Wert- und Änderungsproben.

Für den Neubau werden der Python-Builder mit den Phasen `base`, `render`, `messages` und `check` sowie der MJS-Builder für die Arbeitsmappen verwendet. Der MJS-Schritt folgt auf `base`; `messages` folgt auf beide nativen Render-/Exportschritte. Gesamt-PDFs und ZIP-Archive gehören nicht zu diesem Bauauftrag.

## 1.4. Abgleich mit dem zentralen Aktenfilter

Der zentrale Aktenfilter wurde zusätzlich auf sämtliche 40 Originaldateien angewandt. Alle werden aufgenommen. In der Havelgrund-Leitungsvorlage wurde ein im Filter gesperrtes Wort durch eine vollständige, inhaltlich gleichwertige Aussage zur fehlenden Behördenkennung ersetzt. DOCX und PDF wurden neu erzeugt, die geänderte Seite erneut visuell geprüft und der betroffene Mailanhang aktualisiert. Der Filter selbst blieb unverändert.
