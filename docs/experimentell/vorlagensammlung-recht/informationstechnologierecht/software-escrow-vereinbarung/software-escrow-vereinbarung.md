# Software-Escrow-Vereinbarung

Kurz-Hinweis: Diese Vorlage ist unverbindlich, ein experimenteller Text und keine Rechtsberatung. Nutzung nur auf eigene Gewähr, eigene Gefahr und ohne Gewähr. Die ausführlichen Hinweise zu § 43a Abs. 2 BRAO, § 203 StGB, DSGVO sowie Apache-2.0 OR MIT stehen in der README dieser Vorlage.

## Vorlage

[WARNHINWEIS — nicht Vertragsbestandteil, nicht mit unterzeichnen]

Diese Vorlage ersetzt nicht die anwaltliche Eigenleistung. Sie liefert das Gerüst, nicht den Fall. Der Anwender bringt den Sachverhalt, die Beweismittel, die taktische Entscheidung und die Verantwortung; die Vorlage bringt Struktur, Sprache und die unbedingt zu prüfenden Stellen. Wer nur Platzhalter füllt, ohne den eigenen Sachverhalt zu durchdenken, hat noch keinen Vertrag, sondern einen Entwurf.

Weitere Hinweise und ausführliche Praxis-Erläuterungen in der README dieser Vorlage.

### Vertragseingang und Bearbeitungsstand

Lizenzgeber / Softwareentwickler (Hinterleger) ist [vollständiger Name oder Firma, Rechtsform, Register, Sitz, Anschrift, Vertretung].

Lizenznehmer / Nutzungsberechtigter ist [vollständiger Name oder Firma, Rechtsform, Register, Sitz, Anschrift, Vertretung].

Treuhänder / Escrow-Agent ist [vollständiger Name oder Firma, Rechtsform, Register, Sitz, Anschrift, Vertretung].

Der Bearbeitungsstand ist [Entwurf / Verhandlung / Unterzeichnung / Vollzug], Datum: [Datum], Akte: [Az.].

---

## 1. Präambel / Gegenstand

1.1 Die Parteien schließen diese Vereinbarung, um die dauerhafte Verfügbarkeit der im Lizenzvertrag vom [Datum] bezeichneten Software für den Lizenznehmer sicherzustellen. Der Hinterleger entwickelt und pflegt die unter der Bezeichnung [Softwareprodukt, Versionstand] bekannte Software und stellt sie dem Lizenznehmer auf Grundlage des Lizenzvertrags zur Verfügung.

1.2 Zur Absicherung des Lizenznehmers für den Fall, dass der Hinterleger die Softwarewartung einstellt, insolvent wird oder die Weiterentwicklung auf Dauer aufgibt, hinterlegt der Hinterleger den vollständigen Quellcode einschließlich Entwicklungsumgebungen, Build-Skripten und technischer Dokumentation beim Treuhänder; der Treuhänder verwahrt und gibt das Hinterlegungsgut nach Maßgabe dieser Vereinbarung heraus.

---

## 2. Hinterlegungsgegenstand und Vollständigkeit

2.1 Der Hinterleger übergibt dem Treuhänder spätestens am [Datum der Ersteinlieferung] den Quellcode in der jeweils aktuellen Produktionsversion, alle Build- und Kompilierungsanweisungen, eine Beschreibung der für den Betrieb erforderlichen Systemumgebung sowie die Entwicklerdokumentation und den aktuellen Versionsstand aller eingesetzten Drittanbieter-Komponenten einschließlich ihrer Lizenzbedingungen.

2.2 Der Hinterleger stellt sicher, dass das Hinterlegungsgut vollständig und unmittelbar zur Kompilierung geeignet ist. Der Treuhänder führt nach jeder Einlieferung innerhalb von [Frist, z. B. 20 Werktagen] eine technische Integritätsprüfung durch und übermittelt das Ergebnis an beide Parteien in Textform.

2.3 Schlägt die Integritätsprüfung fehl oder fehlen wesentliche Bestandteile, setzt der Treuhänder dem Hinterleger eine Nachbesserungsfrist von [Frist, z. B. zehn Werktagen]. Wird die Frist fruchtlos verstrichen, gilt dies als wesentliche Pflichtverletzung des Hinterlegers.

---

## 3. Aktualisierungspflicht

3.1 Der Hinterleger liefert eine aktualisierte Hinterlegung innerhalb von [Frist, z. B. 30 Tagen] nach jeder wesentlichen Produktionsaktualisierung, spätestens jedoch alle sechs Monate. Als wesentlich gilt jede Änderung, die eine neue Haupt- oder Nebenversion im Sinne von Semantic Versioning ([MAJOR.MINOR.PATCH]) begründet.

3.2 Jede Aktualisierungseinlieferung ist durch den Hinterleger mit einer Release-Note zu begleiten, die die vorgenommenen Änderungen im Überblick beschreibt. Die Release-Note wird vom Treuhänder dem Lizenznehmer unverzüglich, spätestens binnen fünf Werktagen, weitergeleitet.

3.3 Der Treuhänder führt ein fortlaufendes Einlieferungsprotokoll, das Datum, Versionsnummer, Lieferumfang und Prüfergebnis für jede Einlieferung dokumentiert und auf Anfrage beiden Parteien zugänglich ist.

---

## 4. Herausgabefälle

4.1 Der Treuhänder gibt das Hinterlegungsgut an den Lizenznehmer heraus, wenn einer der folgenden Herausgabefälle eingetreten ist und der Treuhänder darüber in Textform unterrichtet wurde:

4.1.1 Der Hinterleger hat Insolvenzantrag gestellt, das Insolvenzverfahren wurde eröffnet oder mangels Masse abgewiesen.

4.1.2 Der Hinterleger hat die Einstellung der Softwarewartung oder -weiterentwicklung gegenüber dem Lizenznehmer erklärt oder den Betrieb im Bereich der betreffenden Software dauerhaft eingestellt.

4.1.3 Der Hinterleger hat seine Aktualisierungspflicht nach Abschnitt 3 für mehr als [Frist, z. B. sechs Monate] nicht erfüllt und auf eine Abmahnung des Lizenznehmers innerhalb von vier Wochen nicht reagiert.

4.2 Der Treuhänder übermittelt dem Hinterleger die Herausgabe-Ankündigung unverzüglich nach deren Eingang; dem Hinterleger steht eine Widerspruchsfrist von [Frist, z. B. zehn Werktagen] zu. Für offensichtlich begründete Herausgabeansprüche im Falle des Abschnitts 4.1.1 bedarf es keines Abwartens der Widerspruchsfrist.

4.3 Widerspricht der Hinterleger innerhalb der Frist, stellt der Treuhänder die Herausgabe zurück und unterrichtet beide Parteien; die Parteien klären die Streitfrage auf dem vereinbarten Rechtsweg.

---

## 5. Nutzungsrechte nach Herausgabe

5.1 Der Lizenznehmer erhält mit der Herausgabe das unwiderrufliche, nicht übertragbare und nicht unterlizenzierbare Recht, den Quellcode ausschließlich zum Zweck der Weiterentwicklung, Wartung und des internen Betriebs der Software zu nutzen, soweit dies für den vertragsgemäßen Einsatz erforderlich ist.

5.2 Eine Vervielfältigung, Veröffentlichung oder Weitergabe des Quellcodes an Dritte, die nicht unmittelbar für den Betrieb des Lizenznehmers tätig sind, ist ohne gesonderte Zustimmung des Hinterlegers oder eines etwaigen Insolvenzverwalters unzulässig.

5.3 Drittkomponenten im Hinterlegungsgut unterliegen den jeweiligen Open-Source- oder Drittlizenzen; der Lizenznehmer prüft deren Vereinbarkeit mit dem geplanten Einsatz eigenverantwortlich.

---

## 6. Vergütung und Kosten

6.1 Der Lizenznehmer trägt die Vergütung des Treuhänders für die Einrichtung des Escrow-Kontos, die jährliche Verwahrungsgebühr und die Integritätsprüfungen in der Höhe von [Betrag in EUR] zuzüglich der gesetzlichen Umsatzsteuer; die genaue Aufschlüsselung ist in Anlage 1 zu dieser Vereinbarung festgelegt.

6.2 Die Jahresgebühr ist jeweils zum [Zahlungstermin, z. B. 1. Januar] eines Jahres zur Zahlung fällig. Gerät der Lizenznehmer mit der Zahlung um mehr als 30 Tage in Verzug, ist der Treuhänder berechtigt, den Lizenznehmer unter Fristsetzung von 14 Tagen zu mahnen; bei weiterem Verzug ruht die Verwahrungspflicht des Treuhänders bis zur Zahlung.

6.3 Kosten für außerordentliche Herausgabeprüfungen, Streitbeilegungsverfahren und Sonderprüfungen nach Abschnitt 3.2 trägt die Partei, die sie veranlasst hat; in Streitfällen gilt § 91 ZPO entsprechend.

---

## 7. Vertraulichkeit und Datenschutz

7.1 Der Treuhänder behandelt den Quellcode und alle Bestandteile des Hinterlegungsguts als streng vertraulich und gibt sie ausschließlich nach Maßgabe dieser Vereinbarung heraus.

7.2 Der Treuhänder trifft dem Schutzbedarf des Hinterlegungsguts angemessene technische und organisatorische Sicherheitsmaßnahmen und legt sie auf Anfrage einer Partei offen.

7.3 Personenbezogene Daten, die im Rahmen der Vertragsabwicklung verarbeitet werden, werden ausschließlich auf zulässiger Rechtsgrundlage nach Art. 6 Abs. 1 DSGVO verarbeitet.

---

## 8. Laufzeit, Kündigung und Rückgabe

8.1 Diese Vereinbarung beginnt mit der Unterzeichnung aller drei Parteien und läuft unbefristet; sie endet mit dem Ende des Lizenzvertrags vom [Datum], kann jedoch von jeder Partei mit einer Frist von sechs Monaten zum Jahresende ordentlich gekündigt werden.

8.2 Das Recht zur außerordentlichen Kündigung aus wichtigem Grund bleibt unberührt; ein wichtiger Grund liegt insbesondere vor, wenn eine Partei ihre wesentlichen Pflichten nach dieser Vereinbarung dauerhaft verletzt.

8.3 Nach Beendigung dieser Vereinbarung gibt der Treuhänder das Hinterlegungsgut unverzüglich, spätestens binnen 30 Tagen, an den Hinterleger zurück, sofern kein Herausgabefall eingetreten ist; alle Kopien des Treuhänders werden unwiederbringlich gelöscht, und der Treuhänder bestätigt die Löschung schriftlich.

---

## 9. Schlussbestimmungen

9.1 Änderungen dieser Vereinbarung bedürfen der Textform und der Zustimmung aller drei Parteien.

9.2 Sollte eine Bestimmung dieser Vereinbarung ganz oder teilweise unwirksam sein oder werden, bleibt die Vereinbarung im Übrigen wirksam; die Parteien vereinbaren anstelle der unwirksamen Bestimmung eine rechtlich zulässige Regelung, die dem wirtschaftlichen Zweck der unwirksamen Bestimmung möglichst nahekommt.

9.3 Ausschließlicher Gerichtsstand für alle Streitigkeiten aus und im Zusammenhang mit dieser Vereinbarung ist [Gerichtsstand]; es gilt deutsches Recht.

9.4 Abschnitt 1 „Präambel / Gegenstand" ist Bestandteil dieses Vertrags und hat Regelungsgehalt.

---

### Schluss, Unterzeichnung und Freigabe

**Unterzeichnung**

[Ort], den [Datum]

| Für den Hinterleger | Für den Lizenznehmer | Für den Treuhänder |
|---|---|---|
| _____________________________ | _____________________________ | _____________________________ |
| [Name, Funktion, Vertretungsrolle] | [Name, Funktion, Vertretungsrolle] | [Name, Funktion, Vertretungsrolle] |

---

## Anlagen

### Anlage 1: Vergütungsübersicht

Die Vergütung des Treuhänders für den Vertragszeitraum setzt sich wie folgt zusammen: Die einmalige Einrichtungsgebühr beträgt [Betrag in EUR] netto; die jährliche Verwahrungsgebühr beträgt [Betrag in EUR] netto; für jede außerordentliche Integritätsprüfung nach Abschnitt 3.1 berechnet der Treuhänder pauschal [Betrag in EUR] netto. Alle Beträge verstehen sich zuzüglich der jeweils geltenden gesetzlichen Umsatzsteuer und sind innerhalb von 14 Tagen nach Rechnungsstellung zahlbar.

---

Lizenz: Apache-2.0 OR MIT.
