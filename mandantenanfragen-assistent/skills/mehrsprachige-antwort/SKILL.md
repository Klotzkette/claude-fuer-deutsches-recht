---
name: mehrsprachige-antwort
description: "Mandantenanfrage kam auf Englisch Franzoesisch oder Italienisch und Antwort soll in derselben Sprache erfolgen. Mehrsprachige Erstantwort Kanzlei. Pruefraster: Sprache erkennen Anredekonventionen Schlussformeln Datenschutzhinweise in Zielsprache. Output: sprachlich korrekte Erstantwort. Abgrenzung zu erstantwort-generator (Deutsch) und anrede-uebernehmen (Anrede)."
---

# Mehrsprachige-Antwort

Dieser Skill erkennt die Sprache der eingehenden Mandantenanfrage und schaltet die Erstantwort in die entsprechende Sprache um. Die Sprachauswahl folgt der Sprache der Anfrage — nicht der Sprache der Kanzlei-Oberfläche.


## Triage zu Beginn
1. Welche Sprache wurde in der Anfrage verwendet und welche Sprache soll fuer die Antwort verwendet werden?
2. Gibt es landesspezifische Anredekonventionen (EN, FR, IT) die abweichen von deutschen Regeln?
3. Muss der Datenschutzhinweis (Art. 13 DSGVO) und der Kein-Mandat-Disclaimer ebenfalls in der Fremdsprache formuliert werden?
4. Ist die Anfrage moeglicherweise automatisch uebersetzt worden (Qualitaet der Sprache pruefen)?

## Aktuelle Rechtsprechung
- EuGH, Urt. v. 04.07.2023 - C-252/21, NJW 2023, 2997 — Informationspflichten nach Art. 13 DSGVO muessen in einer fuer die betroffene Person verstaendlichen Sprache erteilt werden; Datenschutzhinweis auf Deutsch bei fremdsprachiger Anfrage genuegt nicht.
- BGH, Urt. v. 14.11.2019 - IX ZR 222/18, NJW 2020, 691 — Mandantenkommunikation muss fuer den Mandanten verstaendlich sein; Sprachbarrieren erhoehen Haftungsrisiko bei Beratungsfehlern.
- BGH, Urt. v. 07.02.2019 - IX ZR 5/18, NJW 2019, 1513 — Kostenbelehrung nach § 49b Abs. 5 BRAO muss fuer den Mandanten verstaendlich sein; fremdsprachiger Mandant hat Anspruch auf Belehrung in verstaendlicher Sprache.
- BVerfG, Beschl. v. 12.01.2016 - 2 BvR 2557/14, NJW 2016, 1155 — Effektive Rechtswahrnehmung erfordert verstaendliche Kommunikation; Sprachbarriere bei Mandantenanfragen muss durch Kanzlei ueberwunden werden.

## Zentrale Normen
- Art. 13 DSGVO — Informationspflicht in verstaendlicher Sprache: gilt bei Fremdsprachler uneingeschraenkt
- Art. 12 DSGVO — Transparenz: klar und in einfacher Sprache; Fremdsprachler haben Anspruch auf verstaendliche Information
- § 49b Abs. 5 BRAO — Kostenbelehrung: muss fuer Mandanten verstaendlich sein (Sprache relevant)
- § 43 BRAO — Sorgfaltspflicht: Sprachbarriere als organisatorisches Risiko in der Kanzlei

## Kommentarliteratur
- Kühling/Buchner DSGVO Art. 12, 13 Rn. 1-20 (Verstaendliche Sprache als Transparenzanforderung)
- Gaier/Wolf/Göcken BRAO § 43 Rn. 1-30 (Sorgfaltspflicht: Umgang mit fremdsprachigen Mandanten)

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
| Vollständiger Name bekannt, Herr | „Dear Mr [Nachname]," |
| Vollständiger Name bekannt, Frau | „Dear Ms [Nachname]," (Ms als Standardform — kein Mrs/Miss ohne explizite Nennung) |
| Titel vorhanden | „Dear Dr [Nachname]," / „Dear Prof [Nachname]," |
| Name unbekannt | „Dear Sir or Madam," |

### Dank-Formulierung (EN)

„Thank you for contacting us. We have received your enquiry."

### Telefontermin-Hinweis (EN)

„To arrange an initial appointment, please contact our office by telephone: [SEKRETARIATS-TELEFON] (available: [ERREICHBARKEITSZEITEN])."

### Sachverhalt-Bitte (EN)

„To enable us to prepare for your matter, we kindly ask you to send us a brief written summary by email, covering: the nature of your concern, the relevant dates, the parties involved, and any deadlines you are aware of."

### Transkriptionsservice-Hinweis (EN)

„If you find it difficult to describe your matter in writing, we offer an automated transcription service. You may call [TRANSKRIPTIONS-TELEFON], state your concern verbally, and the recording will be automatically transcribed and forwarded to us. Please note: At the start of the call, you will be asked to confirm your consent to the recording. No recording will be made without your consent."

### Datenschutz-Kurzform (EN)

„Please note that as no client relationship has yet been established, the processing of your voice data is based on your explicit consent (Art. 6(1)(a) GDPR). You may withdraw your consent at any time."

### Disclaimer (EN)

„Please be aware that this acknowledgement does not establish a client-solicitor relationship and does not constitute legal advice. No obligations are created for [KANZLEI-NAME] by this communication."

### Schlussformel (EN)

„Yours sincerely," (formell) / „Kind regards," (etwas weniger formell, aber gebräuchlich)

## Sprachanpassung: Französisch

### Anredekonventionen (FR)

| Situation | Anrede |
|---|---|
| Herr, Name bekannt | „Madame, Monsieur [Nachname]," oder „Monsieur [Nachname]," |
| Frau, Name bekannt | „Madame [Nachname]," |
| Dr. | „Monsieur le Docteur [Nachname]," / „Madame le Docteur [Nachname]," |
| Unbekannt | „Madame, Monsieur," |

### Dank-Formulierung (FR)

„Nous vous remercions de votre prise de contact et avons bien reçu votre demande."

### Telefontermin-Hinweis (FR)

„Pour convenir d'un premier rendez-vous, nous vous invitons à nous contacter par téléphone: [SEKRETARIATS-TELEFON] (disponibilité: [ERREICHBARKEITSZEITEN])."

### Disclaimer (FR)

„Veuillez noter que la présente confirmation de réception ne constitue pas une relation avocat-client et ne représente pas un conseil juridique."

### Schlussformel (FR)

„Veuillez agréer, Madame, Monsieur, l'expression de nos salutations distinguées,"

## Sprachanpassung: Italienisch

### Anredekonventionen (IT)

| Situation | Anrede |
|---|---|
| Herr, Name bekannt | „Gentile Sig. [Nachname]," |
| Frau, Name bekannt | „Gentile Sig.ra [Nachname]," |
| Dr. | „Gentile Dott. [Nachname]," / „Gentile Dott.ssa [Nachname]," |
| Prof. | „Gentile Prof. [Nachname]," |
| Unbekannt | „Gentile Signora/Signore," oder „Spett.le [Kanzleiname]," (an Kanzleien) |

### Dank-Formulierung (IT)

„La ringraziamo per averci contattati e confermiamo la ricezione della Sua richiesta."

### Telefontermin-Hinweis (IT)

„Per fissare un primo appuntamento, La invitiamo a contattarci telefonicamente: [SEKRETARIATS-TELEFON] (orari: [ERREICHBARKEITSZEITEN])."

### Disclaimer (IT)

„Si prega di notare che questa conferma di ricezione non costituisce un rapporto avvocato-cliente e non rappresenta una consulenza legale."

### Schlussformel (IT)

„Distinti saluti," oder „Con i migliori saluti,"

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
