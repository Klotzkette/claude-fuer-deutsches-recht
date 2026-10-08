# Lizenzvertrag über urheberrechtlich geschützte Trainingsdaten für KI-Systeme

---

Kurz-Hinweis: Diese Vorlage ist unverbindlich, ein experimenteller Text und keine Rechtsberatung. Nutzung nur auf eigene Gewähr, eigene Gefahr und ohne Gewähr. Die ausführlichen Hinweise zu § 43a Abs. 2 BRAO, § 203 StGB, DSGVO sowie Apache-2.0 OR MIT stehen in der README dieser Vorlage.

---

## Vorlage

[WARNHINWEIS — nicht Vertragsbestandteil, nicht mit unterzeichnen]

Diese Vorlage ersetzt nicht die anwaltliche Eigenleistung. Sie liefert das Gerüst, nicht den Fall. Der Anwender bringt den Sachverhalt, die Beweismittel, die taktische Entscheidung und die Verantwortung; die Vorlage bringt Struktur, Sprache und die unbedingt zu prüfenden Stellen. Wer nur Platzhalter füllt, ohne den eigenen Sachverhalt zu durchdenken, hat noch keinen Vertrag, sondern einen Entwurf.

Weitere Hinweise und ausführliche Praxis-Erläuterungen in der README dieser Vorlage.

### Lizenzvertrag über urheberrechtlich geschützte Trainingsdaten für KI-Systeme

zwischen

**[Name/Firma des Rechteinhabers]**, [Rechtsform], [Anschrift], vertreten durch [vertretungsberechtigte Person]
— im Folgenden: „Lizenzgeber" —

und

**[Name/Firma des KI-Anbieters oder Forschenden]**, [Rechtsform], [Anschrift], vertreten durch [vertretungsberechtigte Person]
— im Folgenden: „Lizenznehmer" —

— gemeinsam: „Parteien" —

#### 1. Präambel / Gegenstand

1.1 Der Lizenzgeber verfügt nach eigener Darstellung über die in Anlage 1 bezeichneten Werke, Leistungsschutzrechte, Datenbankrechte, Metadaten und Begleitmaterialien (zusammen „Trainingskorpus"). Der Lizenznehmer entwickelt, evaluiert oder betreibt [Bezeichnung des KI-Systems, Modelltyps, Forschungs- oder Produktzwecks].

1.2 Die Parteien regeln mit diesem Vertrag die kontrollierte Bereitstellung und Nutzung des Trainingskorpus für Text und Data Mining, Modelltraining, Evaluierung, Sicherheitsprüfung und Dokumentation. Die Rechteübertragung betrifft nicht das Urheberrecht als solches, sondern nur die in diesem Vertrag eingeräumten Nutzungsrechte.

#### 2. Trainingskorpus, Rechtebestand und Ausschlüsse

2.1 Der lizenzierte Trainingskorpus besteht ausschließlich aus den in Anlage 1 einzeln oder kategorisiert aufgeführten Inhalten. Anlage 1 nennt je Inhalt oder Inhaltsgruppe [Titel oder Kennung], [Werkart], [Quelle], [Rechteinhaber], [Rechtekette], [territoriale Reichweite], [Nutzungsbeschränkungen], [Ausschlüsse] und [technische Prüfsumme oder Archivkennung].

2.2 Nicht lizenziert sind [Variante A: Inhalte Dritter, deren Rechtekette in Anlage 1 als offen markiert ist — geeignet bei gemischten Archiven; Variante B: Inhalte mit Persönlichkeits-, Bildnis-, Musik-, Marken- oder Datenbankrechten außerhalb der ausdrücklich genannten Rechte — geeignet bei audiovisuellen oder presseähnlichen Beständen; Variante C: Inhalte, für die ein maschinenlesbarer Nutzungsvorbehalt nach § 44b Abs. 3 UrhG dokumentiert ist — geeignet bei Web- oder Plattformkorpora].

2.3 Der Lizenznehmer darf keine Inhalte nutzen, die in Anlage 2 als gesperrt, widerrufen, rechtlich ungeklärt oder nur zu Prüfzwecken freigegeben bezeichnet sind. Werden solche Inhalte versehentlich bereitgestellt, löscht oder sperrt der Lizenznehmer sie unverzüglich nach Mitteilung und dokumentiert die technische Umsetzung in Anlage 4.

#### 3. Rechteeinräumung für Text und Data Mining und Training

3.1 Der Lizenzgeber räumt dem Lizenznehmer ein [einfaches / ausschließliches], [übertragbares / nicht übertragbares], [unterlizenzierbares / nicht unterlizenzierbares] Nutzungsrecht ein, den Trainingskorpus für die folgenden Zwecke zu vervielfältigen, zu normalisieren, zu indexieren, zu annotieren, in Vektorrepräsentationen zu überführen und automatisiert auszuwerten:

3.1.1 Entwicklung, Training und Feinabstimmung von [Modellbezeichnung oder Modellfamilie].

3.1.2 Evaluierung, Red-Teaming, Bias- und Sicherheitsprüfung, Qualitätsmessung und Dokumentation.

3.1.3 Erstellung technischer Zwischenkopien, soweit diese für die vorgenannten Zwecke erforderlich sind.

3.2 Die Lizenz umfasst keine öffentliche Wiedergabe, öffentliche Zugänglichmachung, Veröffentlichung, Weitergabe oder Einzelverwertung der Originalinhalte, Auszüge oder vollständigen Datensätze außerhalb der in diesem Vertrag geregelten Zwecke.

3.3 Rechte für bei Vertragsschluss unbekannte Nutzungsarten werden [nicht eingeräumt / nach Maßgabe einer gesonderten schriftlichen Vereinbarung gemäß § 31a UrhG eingeräumt]. Ist Schriftform erforderlich, genügt Textform nicht.

#### 4. Output, Modellgewichte und Schutz gegen Rekonstruktion

4.1 Der Lizenznehmer darf aus dem Training entstandene Modellgewichte, Embeddings, Evaluierungsdaten und statistische Parameter nutzen, soweit daraus keine wirtschaftlich verwertbare Rekonstruktion einzelner Werke oder substantieller Korpusbestandteile ermöglicht wird.

4.2 Der Lizenznehmer implementiert technische und organisatorische Maßnahmen gegen memorisierte Ausgaben, wörtliche Langausgaben und systematische Rekonstruktion. Dazu gehören mindestens [Output-Filter], [Memorization-Test], [Prompt-Abwehrtest], [Logging], [manuelle Stichprobenprüfung] und [Eskalationsprozess].

4.3 Gibt das System trotz Schutzmaßnahmen urheberrechtlich relevante Text-, Bild-, Audio- oder Videosequenzen aus dem Trainingskorpus aus, sperrt der Lizenznehmer die betroffene Nutzung, untersucht die Ursache und informiert den Lizenzgeber innerhalb von [Anzahl] Werktagen mit einem Maßnahmenbericht.

#### 5. Nutzungsvorbehalt, Opt-out und Löschung

5.1 Der Lizenzgeber erklärt, dass für die in Anlage 1 freigegebenen Inhalte kein wirksamer Nutzungsvorbehalt entgegensteht oder dass er zur vertraglichen Lizenzierung trotz Nutzungsvorbehalts berechtigt ist.

5.2 Wird nach Vertragsschluss ein Rechtevorbehalt, Widerruf, Rechtekettenmangel oder Betroffenenbegehren bekannt, prüfen die Parteien den betroffenen Inhalt nach Anlage 2. Der Lizenznehmer setzt eine Sperre für künftige Trainingsläufe innerhalb von [Anzahl] Werktagen um; bereits trainierte Modellzustände werden nach [Variante A: dokumentiert, aber nicht zurückgebaut, weil eine technische Entfernung unverhältnismäßig ist — geeignet bei großen Basismodellen; Variante B: aus dem nächsten Modellstand entfernt oder durch erneutes Training ohne die betroffenen Inhalte ersetzt — geeignet bei kleinen oder kontrollierten Modellen].

#### 6. Vergütung und Abrechnung

6.1 Der Lizenznehmer zahlt für die Rechteeinräumung eine Vergütung von [Betrag] EUR zuzüglich gesetzlicher Umsatzsteuer.

6.2 **Variante A:** Die Vergütung ist eine einmalige Pauschale für die in Anlage 1 bezeichnete Korpusversion — geeignet bei abgeschlossenen Archiven; Variante B: Die Vergütung besteht aus einer Grundvergütung von [Betrag] EUR und einer nutzungsabhängigen Vergütung von [Berechnungsformel] — geeignet bei laufender Aktualisierung oder kommerzieller Modellverwertung; Variante C: Die Parteien vereinbaren eine Forschungsfreigabe ohne Lizenzentgelt, jedoch mit strikter Nichtverwertungspflicht — geeignet bei nichtkommerzieller Forschung.

6.3 Gesetzlich zwingende Ansprüche auf angemessene Vergütung, Vertragsanpassung oder weitere Beteiligung bleiben unberührt, soweit sie anwendbar sind.

#### 7. Dokumentation, Audit und Nachweise

7.1 Der Lizenznehmer führt eine Trainings- und Nutzungsmatrix nach Anlage 3. Sie dokumentiert [Korpusversion], [Importdatum], [Trainingslauf], [Modellversion], [Zweck], [verantwortliche Stelle], [Sperrlistenprüfung], [Lösch- oder Sperrentscheidung] und [technische Prüfsummen].

7.2 Der Lizenzgeber darf einmal jährlich und bei konkretem Rechtekettenanlass Auskunft über die Nutzung des Trainingskorpus verlangen. Der Lizenznehmer darf Geschäftsgeheimnisse und sicherheitsrelevante Informationen schwärzen, solange die Prüfung der vertragsgemäßen Nutzung möglich bleibt.

7.3 [OPTIONAL — nur aufnehmen, wenn personenbezogene Daten im Korpus enthalten sind: Die Parteien prüfen vor Bereitstellung des Trainingskorpus die datenschutzrechtliche Rolle, Rechtsgrundlage, Informationspflichten, Löschfristen, Betroffenenrechte und eine etwaige Datenschutz-Folgenabschätzung. Soweit der Lizenznehmer personenbezogene Daten im Auftrag verarbeitet, schließen die Parteien vor Datenzugang eine Vereinbarung nach Art. 28 DSGVO.]

#### 8. Gewährleistung, Rechte Dritter und Freistellung

8.1 Der Lizenzgeber gewährleistet nicht den wirtschaftlichen Erfolg des Trainings. Er steht aber dafür ein, dass ihm die in Anlage 1 ausgewiesenen Rechte nach seiner Kenntnis zustehen und dass bekannte Beschränkungen vollständig in Anlage 1 oder Anlage 2 offengelegt sind.

8.2 Der Lizenznehmer gewährleistet, dass er den Trainingskorpus nur für die vereinbarten Zwecke nutzt, Zugriffe protokolliert, Sperrlisten beachtet und nicht autorisierte Kopien verhindert.

8.3 Jede Partei stellt die andere von berechtigten Ansprüchen Dritter frei, die aus einer schuldhaften Verletzung ihrer Zusicherungen oder Vertragspflichten entstehen. Die in Anspruch genommene Partei informiert die andere Partei unverzüglich und stimmt Verteidigung, Vergleich und öffentliche Kommunikation ab.

#### 9. Laufzeit, Beendigung und Rückgabe

9.1 Dieser Vertrag beginnt mit Unterzeichnung und läuft bis zum [Datum]. Er verlängert sich um [Zeitraum], wenn er nicht mit einer Frist von [Anzahl] Monaten zum Laufzeitende gekündigt wird.

9.2 Nach Vertragsende beendet der Lizenznehmer den Zugriff auf den Trainingskorpus, löscht nicht mehr benötigte Kopien und bestätigt die Umsetzung in Textform. Dokumentationsdaten, Auditnachweise und Modellversionen dürfen aufbewahrt werden, soweit dies zur Rechteverteidigung, Compliance oder gesetzlichen Aufbewahrung erforderlich ist.

9.3 Das Recht zur außerordentlichen Kündigung aus wichtigem Grund bleibt unberührt. Ein wichtiger Grund liegt insbesondere vor bei schwerwiegender Zwecküberschreitung, systematischer Missachtung von Sperrlisten oder unberechtigter Weitergabe des Trainingskorpus.

#### 10. Vertraulichkeit und Sicherheit

10.1 Die Parteien behandeln Trainingskorpus, Modellinformationen, Prüfberichte, Vergütung und technische Schutzmaßnahmen vertraulich. Die Pflicht gilt für [Anzahl] Jahre nach Vertragsende fort.

10.2 Der Lizenznehmer schützt den Trainingskorpus mindestens durch rollenbasierten Zugriff, Verschlüsselung bei Übertragung und Speicherung, Protokollierung, getrennte Entwicklungsumgebungen und Löschkonzept.

#### 11. Schlussbestimmungen

11.1 Abschnitt 1 und die Anlagen 1 bis 4 sind Bestandteil dieses Vertrags und haben Regelungsgehalt.

11.2 Änderungen und Ergänzungen bedürfen der Textform, soweit nicht gesetzlich Schriftform vorgeschrieben ist.

11.3 Es gilt deutsches Recht. Gerichtsstand ist, soweit zulässig, [Ort].

11.4 Sollte eine Bestimmung unwirksam sein, bleibt der Vertrag im Übrigen wirksam. An die Stelle der unwirksamen Bestimmung tritt die gesetzliche Regelung.

---

### Schluss, Unterzeichnung und Freigabe

**Unterzeichnung**

[Ort], den [Datum]

| Für den Lizenzgeber | Für den Lizenznehmer |
|---|---|
| _____________________________ | _____________________________ |
| [Name, Funktion, Vertretungsrolle] | [Name, Funktion, Vertretungsrolle] |

## Anlagen

### Anlage 1 — Trainingskorpus und Rechtekette

1. Identifikation

1.1 Korpusbezeichnung: [Name, Version, Archivkennung].

1.2 Rechteinhaber: [Name, Rolle, Rechtequelle].

1.3 Werkarten: [Text; Bild; Audio; Video; Metadaten; Datenbankbestandteile].

2. Rechte- und Nutzungsumfang

2.1 Lizenzierte Nutzungszwecke: [Training; Evaluierung; Forschung; kommerzielle Modellbereitstellung].

2.2 Ausgeschlossene Inhalte: [Liste oder Verweis].

2.3 Rechtekette: [Vertrag; Abtretung; Wahrnehmungsvertrag; eigene Herstellung; noch zu klären].

### Anlage 2 — Sperr-, Widerrufs- und Opt-out-Matrix

1. Inhalt oder Inhaltsgruppe: [Kennung].

2. Grund der Sperre: [Rechtevorbehalt; ungeklärte Rechtekette; Persönlichkeitsrecht; Datenschutz; sonstiger Grund].

3. Technische Maßnahme: [Sperrliste; Entfernung aus Trainingssatz; Nachtraining; Dokumentation].

4. Verantwortlich und Frist: [Rolle], [Datum].

### Anlage 3 — Trainings- und Nutzungsmatrix

1. Trainingslauf: [Kennung, Datum, Modellversion].

2. Eingesetzter Korpus: [Version, Prüfsumme].

3. Zweck: [Training; Feinabstimmung; Evaluation; Sicherheitstest].

4. Freigabe: [Name, Rolle, Datum].

### Anlage 4 — Sicherheits- und Löschprotokoll

1. Zugriffskontrolle: [System, Rollen, Freigabe].

2. Löschung oder Sperre: [Inhalt, Maßnahme, Datum].

3. Output-Prüfung: [Test, Ergebnis, Folge].

---

Lizenz: Apache-2.0 OR MIT.
