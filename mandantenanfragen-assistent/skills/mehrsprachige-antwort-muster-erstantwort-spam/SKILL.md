---
name: mehrsprachige-antwort-muster-erstantwort-spam
description: "Mehrsprachige Antwort Muster Erstantwort Spam: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Mehrsprachige Antwort Muster Erstantwort Spam

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Mehrsprachige Antwort Muster Erstantwort Spam** im Plugin Mandantenanfragen-Assistent. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `mehrsprachige-antwort` | Mandantenanfrage kam auf Englisch Franzoesisch oder Italienisch und Antwort soll in derselben Sprache erfolgen. Mehrsprachige Erstantwort Kanzlei. Prüfraster: Sprache erkennen Anredekonventionen Schlussformeln Datenschutzhinweise in Zielsprache. Output: sprachlich korrekte Erstantwort. Abgrenzung zu erstantwort-generator (Deutsch) und anrede-uebernehmen (Anrede). |
| `muster-erstantwort` | Kanzlei benoetigt fertige ausfuellbare Vorlage für die Erstantwort auf Mandantenanfragen. Template Erstantwort. Prüfraster: Platzhalter KANZLEI-NAME SEKRETARIATS-TELEFON TRANSKRIPTIONS-TELEFON UNTERZEICHNENDE-RA. Drei Varianten Standard nur Vorname Transkriptionsservice-Modus. Output: vollständiges Template-Set für Erstantwort. Abgrenzung zu erstantwort-generator (konkrete Antwort erstellen) und anfrage-eingang-parser. |
| `spam-und-massen-anfrage-filter` | Sekretariat hat Anfrage erhalten die verdaechtig ausschaut. Spam-Erkennung Kanzlei-Eingang. Prüfraster: Spam Werbung 419-Scams automatisierte Recruiter-Mails Massen-Mandantenanfragen Phishing. Output: Spam-Einschaetzung mit Empfehlung Aussortierung oder Nachfrage. Abgrenzung zu anfrage-eingang-parser (echte Anfragen) und dringlichkeitsmarker. |

## Arbeitsweg

Im Plugin Mandantenanfragen-Assistent gilt für **Mehrsprachige Antwort Muster Erstantwort Spam**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `mehrsprachige-antwort`

**Fokus:** Mandantenanfrage kam auf Englisch Franzoesisch oder Italienisch und Antwort soll in derselben Sprache erfolgen. Mehrsprachige Erstantwort Kanzlei. Prüfraster: Sprache erkennen Anredekonventionen Schlussformeln Datenschutzhinweise in Zielsprache. Output: sprachlich korrekte Erstantwort. Abgrenzung zu erstantwort-generator (Deutsch) und anrede-uebernehmen (Anrede).

# Mehrsprachige-Antwort

Dieser Skill erkennt die Sprache der eingehenden Mandantenanfrage und schaltet die Erstantwort in die entsprechende Sprache um. Die Sprachauswahl folgt der Sprache der Anfrage — nicht der Sprache der Kanzlei-Oberfläche.


## Triage zu Beginn
1. Welche Sprache wurde in der Anfrage verwendet und welche Sprache soll fuer die Antwort verwendet werden?
2. Gibt es landesspezifische Anredekonventionen (EN, FR, IT) die abweichen von deutschen Regeln?
3. Muss der Datenschutzhinweis (Art. 13 DSGVO) und der Kein-Mandat-Disclaimer ebenfalls in der Fremdsprache formuliert werden?
4. Ist die Anfrage moeglicherweise automatisch uebersetzt worden (Qualitaet der Sprache pruefen)?

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- Art. 13 DSGVO — Informationspflicht in verstaendlicher Sprache: gilt bei Fremdsprachler uneingeschraenkt
- Art. 12 DSGVO — Transparenz: klar und in einfacher Sprache; Fremdsprachler haben Anspruch auf verstaendliche Information
- § 49b Abs. 5 BRAO — Kostenbelehrung: muss fuer Mandanten verstaendlich sein (Sprache relevant)
- § 43 BRAO — Sorgfaltspflicht: Sprachbarriere als organisatorisches Risiko in der Kanzlei

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Sprach-Erkennung

| Erkannte Sprache | Antwortsprache | Fallback |
|---|---|---|
| Deutsch | Deutsch | — |
| Englisch | Englisch | — |
| Französisch | Französisch | — |
| Italienisch | Italienisch | — |
| Andere Sprache | Deutsch (Standard) + interner Hinweis | Sekretariat entscheidet |
| Gemischt (Mehrere Sprachen) | Sprache des Haupttextes | Manuelle Entscheidung |

## Sprachanpassung: Englisch

### Anredekonventionen (EN)

| Situation | Anrede |
|---|---|
| Vollständiger Name bekannt, Herr | "Dear Mr [Nachname]," |
| Vollständiger Name bekannt, Frau | "Dear Ms [Nachname]," (Ms als Standardform — kein Mrs/Miss ohne explizite Nennung) |
| Titel vorhanden | "Dear Dr [Nachname]," / "Dear Prof [Nachname]," |
| Name unbekannt | "Dear Sir or Madam," |

### Dank-Formulierung (EN)

"Thank you for contacting us. We have received your enquiry."

### Telefontermin-Hinweis (EN)

"To arrange an initial appointment, please contact our office by telephone: [SEKRETARIATS-TELEFON] (available: [ERREICHBARKEITSZEITEN])."

### Sachverhalt-Bitte (EN)

"To enable us to prepare for your matter, we kindly ask you to send us a brief written summary by email, covering: the nature of your concern, the relevant dates, the parties involved, and any deadlines you are aware of."

### Transkriptionsservice-Hinweis (EN)

"If you find it difficult to describe your matter in writing, we offer an automated transcription service. You may call [TRANSKRIPTIONS-TELEFON], state your concern verbally, and the recording will be automatically transcribed and forwarded to us. Please note: At the start of the call, you will be asked to confirm your consent to the recording. No recording will be made without your consent."

### Datenschutz-Kurzform (EN)

"Please note that as no client relationship has yet been established, the processing of your voice data is based on your explicit consent (Art. 6(1)(a) GDPR). You may withdraw your consent at any time."

### Disclaimer (EN)

"Please be aware that this acknowledgement does not establish a client-solicitor relationship and does not constitute legal advice. No obligations are created for [KANZLEI-NAME] by this communication."

### Schlussformel (EN)

"Yours sincerely," (formell) / "Kind regards," (etwas weniger formell, aber gebräuchlich)

## Sprachanpassung: Französisch

### Anredekonventionen (FR)

| Situation | Anrede |
|---|---|
| Herr, Name bekannt | "Madame, Monsieur [Nachname]," oder "Monsieur [Nachname]," |
| Frau, Name bekannt | "Madame [Nachname]," |
| Dr. | "Monsieur le Docteur [Nachname]," / "Madame le Docteur [Nachname]," |
| Unbekannt | "Madame, Monsieur," |

### Dank-Formulierung (FR)

"Nous vous remercions de votre prise de contact et avons bien reçu votre demande."

### Telefontermin-Hinweis (FR)

"Pour convenir d'un premier rendez-vous, nous vous invitons à nous contacter par téléphone: [SEKRETARIATS-TELEFON] (disponibilité: [ERREICHBARKEITSZEITEN])."

### Disclaimer (FR)

"Veuillez noter que la présente confirmation de réception ne constitue pas une relation avocat-client et ne représente pas un conseil juridique."

### Schlussformel (FR)

"Veuillez agréer, Madame, Monsieur, l'expression de nos salutations distinguées,"

## Sprachanpassung: Italienisch

### Anredekonventionen (IT)

| Situation | Anrede |
|---|---|
| Herr, Name bekannt | "Gentile Sig. [Nachname]," |
| Frau, Name bekannt | "Gentile Sig.ra [Nachname]," |
| Dr. | "Gentile Dott. [Nachname]," / "Gentile Dott.ssa [Nachname]," |
| Prof. | "Gentile Prof. [Nachname]," |
| Unbekannt | "Gentile Signora/Signore," oder "Spett.le [Kanzleiname]," (an Kanzleien) |

### Dank-Formulierung (IT)

"La ringraziamo per averci contattati e confermiamo la ricezione della Sua richiesta."

### Telefontermin-Hinweis (IT)

"Per fissare un primo appuntamento, La invitiamo a contattarci telefonicamente: [SEKRETARIATS-TELEFON] (orari: [ERREICHBARKEITSZEITEN])."

### Disclaimer (IT)

"Si prega di notare che questa conferma di ricezione non costituisce un rapporto avvocato-cliente e non rappresenta una consulenza legale."

### Schlussformel (IT)

"Distinti saluti," oder "Con i migliori saluti,"

## Interne Hinweise für das Sekretariat (bei nicht-deutscher Antwort)

```
INTERNE NOTIZ — MEHRSPRACHIGE ANFRAGE
Erkannte Sprache: [EN / FR / IT / Sonstiges]
Antwort generiert in: [Sprache]
Bitte prüfen: Haben Sie einen Anwalt mit entsprechenden Sprachkenntnissen,
der das Erstgespräch führen kann? Falls nein: Hinweis in der Mail aufnehmen.
```

## Verweise auf andere Skills

- `anfrage-eingang-parser` — erkennt die Sprache der Anfrage
- `erstantwort-generator` — erhält den Sprachmodus
- `anrede-uebernehmen` — liefert die sprachangepasste Anrede

## 2. `muster-erstantwort`

**Fokus:** Kanzlei benoetigt fertige ausfuellbare Vorlage für die Erstantwort auf Mandantenanfragen. Template Erstantwort. Prüfraster: Platzhalter KANZLEI-NAME SEKRETARIATS-TELEFON TRANSKRIPTIONS-TELEFON UNTERZEICHNENDE-RA. Drei Varianten Standard nur Vorname Transkriptionsservice-Modus. Output: vollständiges Template-Set für Erstantwort. Abgrenzung zu erstantwort-generator (konkrete Antwort erstellen) und anfrage-eingang-parser.

# Muster-Erstantwort

Dieser Skill enthält das vollständige Komplett-Musterschreiben für die Erstantwort auf Mandantenanfragen. Es ist für den direkten Copy-paste-Einsatz durch das Sekretariat konzipiert.

Alle Platzhalter in eckigen Klammern `[...]` werden durch den Skill `telefon-konfiguration` und `anrede-uebernehmen` automatisch befüllt oder sind manuell zu ersetzen.


## Triage zu Beginn
1. Welche Variante des Musterschreibens wird benoetigt: Standard, Nur-Vorname oder Transkriptionsservice-Modus?
2. Sind alle Platzhalter (Kanzleiname, Sekretariats-Telefon, Unterzeichnende-RA) in kanzlei.json konfiguriert?
3. Wurde die Anrede aus dem Skill anrede-uebernehmen bereits geliefert und kann eingesetzt werden?
4. Soll das Muster in Deutsch oder einer Fremdsprache ausgegeben werden?

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- § 49b Abs. 5 BRAO — Kostenbelehrungspflicht: im Erstantwort-Template vorzusehen
- Art. 13 DSGVO — Informationspflicht: im Erstantwort-Template vorzusehen
- § 43 BRAO — Sorgfaltspflicht: standardisierte Qualitaetssicherung durch Templates
- § 43a Abs. 2 BRAO — Verschwiegenheit: Template darf keine vertraulichen Informationen enthalten

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Platzhalter-Verzeichnis

| Platzhalter | Beschreibung | Quelle |
|---|---|---|
| `[KANZLEI-NAME]` | Vollständiger Kanzleiname | `kanzlei.json` |
| `[SEKRETARIATS-TELEFON]` | Telefonnummer des Sekretariats | `kanzlei.json` |
| `[TRANSKRIPTIONS-TELEFON]` | Telefonnummer des Transkriptionsservices | `kanzlei.json` |
| `[UNTERZEICHNENDE-RA]` | Name und Titel der unterzeichnenden Anwältin/des Anwalts | `kanzlei.json` |
| `[ANREDE]` | Formelle Anredezeile | Skill `anrede-uebernehmen` |
| `[KANZLEI-ADRESSE]` | Postanschrift | `kanzlei.json` |
| `[KANZLEI-E-MAIL]` | E-Mail-Adresse | `kanzlei.json` |
| `[ERREICHBARKEITSZEITEN]` | Bürozeiten | `kanzlei.json` |
| `[DATUM]` | Heutiges Datum | Automatisch |

---

## Variante 1: Standard (vollständige Anrede, Sachverhalt per E-Mail)

```
Betreff: Ihre Anfrage bei [KANZLEI-NAME] — Eingangsbestätigung

[ANREDE],

vielen Dank für Ihre Anfrage, die uns heute zugegangen ist.

Bitte beachten Sie, dass diese Eingangsbestätigung kein Mandatsverhältnis
begründet und keine Rechtsberatung darstellt.

Für ein erstes Beratungsgespräch vergeben wir Termine ausschließlich
telefonisch. Unser Sekretariat erreichen Sie unter:

 [SEKRETARIATS-TELEFON]
 [ERREICHBARKEITSZEITEN]

Um Ihr Anliegen bestmöglich vorzubereiten, bitten wir Sie herzlich,
uns Ihren Sachverhalt vorab kurz per E-Mail zu schildern. Folgende
Angaben helfen uns dabei:

 — Worum geht es in Ihrem Fall (in einigen Sätzen)?
 — Wann hat das zugrunde liegende Ereignis stattgefunden?
 — Gibt es Fristen, Termine oder behördliche Bescheide?
 — Wer ist die Gegenseite (Person, Unternehmen, Behörde)?

Mit freundlichen Grüßen

[UNTERZEICHNENDE-RA]
[KANZLEI-NAME]
[KANZLEI-ADRESSE]
[KANZLEI-E-MAIL]
[SEKRETARIATS-TELEFON]

---
Diese Nachricht begründet kein Mandatsverhältnis und stellt keine Rechtsberatung dar.
```

---

## Variante 2: Nur Vorname (keine Anrede, neutrale Anredeform)

```
Betreff: Ihre Anfrage bei [KANZLEI-NAME] — Eingangsbestätigung

Sehr geehrte[r] [VORNAME] [NACHNAME],

vielen Dank für Ihre Anfrage, die uns heute zugegangen ist.

[Identischer Textblock wie Variante 1 ab "Bitte beachten Sie ..."]
```

Falls Nachname nicht ermittelbar:
Anrede: "Sehr geehrte anfragende Person,"

---

## Variante 3: Transkriptionsservice-Modus (kann nicht/kaum schreiben)

```
Betreff: Ihre Anfrage bei [KANZLEI-NAME] — Eingangsbestätigung

[ANREDE],

vielen Dank für Ihre Anfrage, die uns heute zugegangen ist.

Bitte beachten Sie, dass diese Eingangsbestätigung kein Mandatsverhältnis
begründet und keine Rechtsberatung darstellt.

Für ein erstes Beratungsgespräch vergeben wir Termine ausschließlich
telefonisch. Unser Sekretariat erreichen Sie unter:

 [SEKRETARIATS-TELEFON]
 [ERREICHBARKEITSZEITEN]

Da Ihnen eine schriftliche Schilderung schwerfällt, bieten wir Ihnen
einen automatisierten Transkriptionsservice an. Sie rufen unter der
folgenden Nummer an und schildern Ihr Anliegen mündlich — es wird
automatisch verschriftlicht und uns vertraulich übermittelt:

 Transkriptionsservice: [TRANSKRIPTIONS-TELEFON]

Ablauf des Anrufs:
 1. Automatische Ansage mit Datenschutzhinweis
 2. Bestätigung Ihres Einverständnisses (Tastendruck oder "Ja")
 — Ohne Bestätigung keine Aufnahme.
 3. Freie Schilderung Ihres Anliegens
 4. Automatische Verschriftung und vertrauliche Weiterleitung an uns

Wichtiger Datenschutzhinweis: Da zwischen uns noch kein Mandatsverhältnis
besteht, erfolgt die Verarbeitung Ihrer Sprachdaten ausschließlich auf
Basis Ihrer ausdrücklichen Einwilligung nach Art. 6 Abs. 1 lit. a DSGVO.
Sie können diese Einwilligung jederzeit widerrufen. Die vollständige
Datenschutzinformation senden wir Ihnen auf Anfrage gerne zu.

Mit freundlichen Grüßen

[UNTERZEICHNENDE-RA]
[KANZLEI-NAME]
[KANZLEI-ADRESSE]
[KANZLEI-E-MAIL]
[SEKRETARIATS-TELEFON]

---
Diese Nachricht begründet kein Mandatsverhältnis und stellt keine Rechtsberatung dar.
Datenschutzhinweis gemäß Art. 13 DSGVO auf Anfrage erhältlich unter [KANZLEI-E-MAIL].
```

---

## Verwendungshinweis für das Sekretariat

1. Variante je nach Eingang auswählen.
2. Alle `[...]`-Platzhalter durch die Kanzlei-Daten ersetzen.
3. `[ANREDE]` aus dem Skill `anrede-uebernehmen` übernehmen.
4. Vor dem Versand: Korrekturlesen — insbesondere Anrede und Telefonnummern prüfen.
5. Originalmail der anfragenden Person in Kopie ablegen.
6. CRM-Eintrag aus Skill `folgekorrespondenz-vorbereiten` anlegen.

## Verweise auf andere Skills

- `anrede-uebernehmen` — Anredezeile
- `telefon-konfiguration` — alle Telefonnummern und Kanzleidaten
- `erstantwort-generator` — Hauptskill der die Variante automatisch wählt
- `einwilligung-hinweis-datenschutz` — Langform auf Anfrage
- `mandatsverhaeltnis-hinweis` — Disclaimer (Langform bei Bedarf)

## 3. `spam-und-massen-anfrage-filter`

**Fokus:** Sekretariat hat Anfrage erhalten die verdaechtig ausschaut. Spam-Erkennung Kanzlei-Eingang. Prüfraster: Spam Werbung 419-Scams automatisierte Recruiter-Mails Massen-Mandantenanfragen Phishing. Output: Spam-Einschaetzung mit Empfehlung Aussortierung oder Nachfrage. Abgrenzung zu anfrage-eingang-parser (echte Anfragen) und dringlichkeitsmarker.

# Spam-und-Massen-Anfrage-Filter

Dieser Skill erkennt und kennzeichnet eingehende E-Mails, die keine legitimen Mandantenanfragen sind. Bei positiver Spam-Erkennung wird keine Erstantwort generiert; stattdessen erhält das Sekretariat eine Aussortierungsempfehlung.


## Triage zu Beginn
1. Zeigt die Anfrage klassische Spam-Muster (419-Scam, automatisierte Masse, Phishing, Werbung)?
2. Gibt es Hinweise auf massenhafte identische Einsendung (Template-Formulierungen, ungewoehnliche Absenderadressen)?
3. Soll die Anfrage zur Aussortierung markiert oder direkt verworfen werden?
4. Gibt es Zweifelsfaelle, bei denen die Sekretariatsmitarbeiterin manuell entscheiden soll?

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- Art. 32 DSGVO — TOM: Spam-Filter als Sicherheitsmassnahme fuer Kanzleikommunikation
- § 263 StGB — Betrug: 419-Scam als strafrechtlich relevanter Betrugsversuch; Nichtbearbeitung ist pflichtgemaess
- § 43 BRAO — Sorgfaltspflicht: Ressourceneinsatz der Kanzlei darf auf legitime Anfragen beschraenkt werden
- Art. 5 Abs. 1 lit. c DSGVO — Datensparsamkeit: keine Verarbeitung von Spam-Daten

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Spam-Muster-Katalog

### Kategorie 1: Klassischer 419-Scam (Vorschussbetrug)

Kennzeichen:
- Absender aus Drittländern, die nicht zum Sachverhalt passen
- Schilderung großer Summen, die "transferiert" werden sollen
- Anfrage nach Treuhandkonto, Bankkontodaten oder Vorleistungen
- Formulierungen: "millions of dollars", "strictly confidential", "God bless you"
- Regelmäßig schlechtes Deutsch oder maschinell übersetzter Text

Aktion: `SPAM — 419-SCAM`

### Kategorie 2: Automatisierte Massen-Mandantenanfragen

Kennzeichen:
- Identischer Wortlaut in mehreren eingehenden Mails
- Merkmale automatisierter Erstellung: fehlende Personalisierung, Template-Formulierungen
- Ungewöhnliche Absenderadressen (zufällige Zeichenfolgen, zahlreiche Ziffern)
- Keine konkreten Sachverhaltsdaten

Aktion: `SPAM — MASSEN-ANFRAGE`

### Kategorie 3: Werbung und Newsletter

Kennzeichen:
- Angebotscharakter: Dienstleistungen, Produkte, Software für die Kanzlei
- Opt-out-Link vorhanden
- "Unsubscribe"- oder "Abbestellen"-Hinweis
- Absender ist erkennbar ein Unternehmen, nicht eine Privatperson

Aktion: `KEIN-SPAM — WERBUNG` (gesonderter Kanal; kein Erstantwort-Prozess)

### Kategorie 4: Automatisierte Recruiter-Mails

Kennzeichen:
- Angebot von Kandidaten für offene Stellen
- Formulierungen wie "Ich bin auf Ihr Unternehmen aufmerksam geworden"
- Anhänge mit Lebenslauf ohne Bezug zu einer Stellenausschreibung
- Häufig über LinkedIn- oder XING-Weiterleitungen

Aktion: `KEIN-SPAM — RECRUITER` (Weiterleitung an HR-Kanal)

### Kategorie 5: Phishing-Versuche

Kennzeichen:
- Links zu gefälschten Webseiten (URL-Check: Domain nicht zur angeblichen Organisation passend)
- Dringende Aufforderung, Zugangsdaten einzugeben
- Drohende Konsequenzen bei Nicht-Antwort innerhalb kurzer Frist
- Absender gibt sich als bekannte Institution aus (Finanzamt, Gericht, Strafverfolgungsbehörde)

Aktion: `SPAM — PHISHING` und: Hinweis an Kanzlei-IT

### Kategorie 6: Spamfilter-Umgehungsversuche

Kennzeichen:
- Wörter mit Ziffern statt Buchstaben: "R3cht", "An1walt"
- Unsichtbare Zeichen, übermäßige HTML-Formatierung
- Betreff-Zeile in Großbuchstaben: "DRINGEND!!!" ohne Substanz
- Mehrfache Leerzeichen oder Zeilenumbrüche zur Zeichentrennung

Aktion: `SPAM — FILTER-UMGEHUNG`

## Positive-Signal-Liste (kein Spam)

Die folgenden Merkmale sprechen gegen Spam:
- Konkreter Sachverhalt mit Datum, Personen, Ort
- Deutschsprachig oder in einer der unterstützten Sprachen (EN, FR, IT)
- Persönliche Anrede oder Selbstvorstellung
- Reale Absender-Domain (kein Wegwerf-Mail-Dienst)
- Anhang mit relevanten Dokumenten (Kündigung, Bescheid, Vertrag)

## Ausgabeformat

```
SPAM-CHECK ERGEBNIS
===================
Status: [KLAR / VERDÄCHTIG / SPAM — TYP]
Konfidenz: [HOCH / MITTEL / NIEDRIG]
Erkannte Muster: [Liste der erkannten Muster oder "keine"]
Empfehlung: [Normale Bearbeitung / Manuelle Prüfung / Aussortieren / IT-Meldung]
```

## Verhalten bei SPAM-Erkennung

1. Keine Erstantwort generieren.
2. Skeleton-Eintrag im CRM nur mit Status "SPAM" und Typ; keine vollständige Datenerfassung.
3. Sekretariat erhält Hinweis mit Aussortierungsempfehlung.
4. Bei Phishing: zusätzliche Meldung an die Kanzlei-IT.
5. Bei VERDÄCHTIG (nicht eindeutig): Empfehlung zur manuellen Prüfung durch Rechtsanwalt oder erfahrene Mitarbeitende vor Beantwortung.

## Falsch-Positiv-Schutz

Der Filter ist bewusst konservativ eingestellt. Im Zweifel lieber `VERDÄCHTIG` als `SPAM` — echte Anfragen dürfen nicht unbeantwortet aussortiert werden. Die Endentscheidung liegt immer beim Sekretariat.

## Verweise auf andere Skills

- `anfrage-eingang-parser` — liefert den geparsten Text für die Filter-Analyse
- `folgekorrespondenz-vorbereiten` — erhält den Spam-Status
- `dringlichkeitsmarker` — läuft nur bei KLAR-Status
- `erstantwort-generator` — wird nur bei KLAR-Status ausgeführt
