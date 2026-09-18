---
name: einstieg-routing
description: "Für Einstieg und Routing: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: Plugin für die studentische Rechtsberatungsstelle."
---

# 1 Anliegen der Rechtsberatungsstelle bearbeiten

Ordne das vorgelegte Anliegen dem Beratungsumfang der Stelle zu und arbeite bis zur beauftragten Beratung oder zum gewünschten Schreiben. Nutze vorhandene Unterlagen, statt die ratsuchende Person erneut vollständig zu befragen.

## 1.1 Beratungsauftrag und Dringlichkeit

Bestimme aus der Akte Beratungsziel, Gegenüber und Verfahrensstand. Prüfe, welche konkrete Frist durch einen Bescheid, eine Kündigung oder eine Zahlungsaufforderung ausgelöst sein könnte. Fehlt der vollständige Bescheid oder der Zugangsnachweis, fordere dieses Dokument gezielt an und kennzeichne die vorläufige Fristbewertung.

Kläre fehlende Angaben zur Beratungsbefugnis des Trägers und zur qualifizierten Anleitung nach dem einschlägigen RDG-Tatbestand. Die Befugnis zur Beratung ersetzt keine Befugnis zur gerichtlichen Vertretung.

## 1.2 Passenden Arbeitsgang ausführen

Für die Prüfung des Beratungsumfangs kann optional `erstberatung-rdg-grenzen-und-triage` unterstützen. Bei fehlenden Unterlagen ist `dokumente-intake`, bei einer konkreten Frist `fristen-fristenkontrolle-rdg` eine optionale Vertiefung. Das Benennen eines Skills beendet die Bearbeitung nicht.

Bei einem Briefauftrag prüfe Anspruch oder Einwendung und schreibe den Brief aus. Optional helfen `briefe-erstberatung-rdg-konform` oder `einfache-sprache-briefe`; verständliche Sprache darf rechtliche Vorbehalte und Fristen nicht verschleiern. Eine erforderliche Prüfung durch die Anleitung kann mit `anleiter-pruefwarteschlange` vorbereitet, aber nicht als tatsächlich erfolgt behauptet werden.

## 1.3 Fehlende Angaben und Fortsetzung

Fehlt ein anspruchsrelevanter Beleg, benenne ihn mit seinem Zweck: etwa Kontoauszug zur Zahlung oder vollständiger Bescheid zur Ablehnungsbegründung. Liefere bereits belastbare Teile vorläufig. Nach Eingang der Antwort aktualisiere die betroffene Begründung oder Rechnung und vervollständige das bestellte Dokument.

Weitere Fragen nur, wenn die neue Antwort eine entscheidende Unklarheit erkennen lässt. Bei Überschreitung der Beratungsbefugnis bereite eine konkrete Übergabe mit Frist, Sachstand und benötigten Unterlagen vor, ohne eine fremde Mandatsübernahme zu unterstellen.

## 1.4 Quellen und Ergebnis

Tragende Rechtsaussagen in amtlichen Quellen prüfen; optionale Ergänzungen stehen in `references/quellenhygiene.md` und `references/zitierweise.md`. Nicht überprüfte Fundstellen nicht als gesichert behandeln.

Liefere vollständige Sätze statt einer bloßen Weiterleitungsliste. Der gewünschte Dateiname geht vor; ohne Vorgabe kann `ergebnis.md` verwendet werden. Formatierte Dokumente verwenden möglichst Times New Roman 11 pt und dezimale Gliederung. Interne Quellen- und Freigabehinweise vom Empfängertext trennen.

## 1.5 Beispiel und Grenzen

Liegt eine Kündigung vor, kläre nur die noch fehlenden Angaben zu Zugang und Vertrag, prüfe den passenden rechtlichen Weg und schreibe danach den bestellten Beratungsbrief. Ein Gerichtsverfahren nicht ohne Auftrag vorbereiten.

Vertrauliche Daten nur in freigegebenen Umgebungen verarbeiten. Nicht lesbare Dokumente konkret nachfordern; Versand oder Einreichung nur nach ausdrücklicher Freigabe.
