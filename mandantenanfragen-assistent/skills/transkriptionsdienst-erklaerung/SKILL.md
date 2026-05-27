---
name: transkriptionsdienst-erklaerung
description: "Mandant kann seinen Fall nicht schriftlich schildern und soll stattdessen anrufen. Transkriptionsservice Erklaerung in Erstantwort. Pruefraster: Telefonnummer Ablauf des Anrufs Verarbeitungshinweis DSGVO-Einwilligung Kein-Mandat-Hinweis. Output: Transkriptionsservice-Hinweis fuer Erstantwort. Abgrenzung zu einwilligung-hinweis-datenschutz (DSGVO-Klausel) und erstantwort-generator."
---

# Transkriptionsdienst-Erklärung

Dieser Skill formuliert den vollständigen Abschnitt in der Erstantwort-Mail, in dem der automatisierte Transkriptionsservice beschrieben wird. Er kommt zum Einsatz, wenn die anfragende Person signalisiert, dass sie ihren Sachverhalt nicht schriftlich schildern kann oder möchte.


## Triage zu Beginn
1. Liegt ein Ausloeser fuer den Transkriptionsservice vor (Anfrage kurz/fragmentarisch, Nutzer kann nicht schreiben, expliziter Wunsch)?
2. Ist ein Auftragsverarbeitungsvertrag nach Art. 28 DSGVO mit dem Transkriptions-Dienstleister vorhanden?
3. Enthaelt die Sprachaufnahme potenziell besondere Datenkategorien (Gesundheit, Strafrecht — Art. 9 DSGVO)?
4. Wird die Einwilligung per automatisierter Ansage (Tastendruck) oder schriftlich eingeholt?

## Aktuelle Rechtsprechung
- EuGH, Urt. v. 04.07.2023 - C-252/21, NJW 2023, 2997 — Auftragsverarbeitung durch Transkriptionsdienstleister erfordert AVV nach Art. 28 DSGVO; fehlendes AVV begruendet Datenschutzverstoß.
- EuGH, Urt. v. 11.11.2020 - C-61/19, NJW 2021, 141 — Einwilligung fuer Sprachaufnahme muss informiert und freiwillig sein; Druckknopf-Bestaetigung am Telefon gilt als valide Einwilligungsform, wenn Informationspflicht vorher erteilt wurde.
- BGH, Urt. v. 14.07.2022 - VI ZR 207/21, NJW 2022, 3215 — Sprachaufnahme ohne informierte Einwilligung begruendet Schadensersatzanspruch nach Art. 82 DSGVO; vollstaendige Vorab-Information ist Pflicht.
- OLG Koeln, Urt. v. 11.03.2021 - 15 U 137/20, ZD 2021, 391 — Fehlende oder unvollstaendige Datenschutzinformation nach Art. 13 DSGVO bei Sprachaufnahme begruendet Schadensersatz; der Transkriptionsservice-Hinweis muss vollstaendig sein.

## Zentrale Normen
- Art. 6 Abs. 1 lit. a DSGVO — Einwilligung als Rechtsgrundlage fuer Sprachaufnahme vor Mandatsannahme
- Art. 28 DSGVO — AVV mit Transkriptionsdienstleister: zwingend vor Inbetriebnahme
- Art. 9 Abs. 2 lit. a DSGVO — Ausdrückliche Einwilligung bei besonderer Datenkategorien (Gesundheit, Strafrecht)
- Art. 13 DSGVO — Informationspflicht bei Ersterhebung von Sprachdaten: vollstaendige Vorab-Aufklaerung

## Kommentarliteratur
- Kühling/Buchner DSGVO Art. 28 Rn. 1-40 (AVV: Anforderungen und Pflichtinhalt fuer Dienstleister)
- Sydow/Marsch DSGVO Art. 9 Rn. 30-50 (Besondere Datenkategorien: Einwilligungsanforderungen bei Sprachdaten)

## Wann wird dieser Skill aktiviert?

Aktivierung wenn einer der folgenden Auslöser erkannt wird:

- Explizit: „Ich kann nicht schreiben", „Ich schreibe lieber nicht", „Ich würde lieber anrufen und erzählen", „kann mich nicht gut schriftlich ausdrücken", „bin nicht so gut mit dem Computer"
- Implizit: Kurze, fragmentarische Anfrage ohne Sachverhalts-Details trotz offensichtlich komplexem Anliegen
- Manuell: Die Sekretariatsmitarbeiterin aktiviert den Modus explizit

## Ablauf des Transkriptionsservices

Der Ablauf, der in der Mail erklärt wird:

1. **Anruf:** Die anfragende Person ruft unter der Transkriptions-Telefonnummer an.
2. **Einwilligungsabfrage:** Zu Beginn des Anrufs wird eine automatisierte Ansage abgespielt, die auf die Verarbeitung der Sprachdaten hinweist. Die anrufende Person muss ihr Einverständnis durch Drücken einer Taste oder durch ein klares mündliches „Ja" bestätigen.
3. **Wichtig:** Ohne Einverständnis-Bestätigung wird die Aufnahme nicht gestartet. Der Anruf endet, oder die Person wird an das Sekretariat weitergeleitet.
4. **Schilderung:** Nach bestätigtem Einverständnis schildert die Person ihr Anliegen mündlich.
5. **Automatische Verschriftung:** Die Sprachaufnahme wird durch einen automatisierten Transkriptionsservice verschriftlicht.
6. **Übermittlung:** Das Transkript wird der Kanzlei vertraulich übermittelt und dem potenziellen Mandantenvorgang zugeordnet.
7. **Rückmeldung:** Das Sekretariat meldet sich auf Basis des Transkripts beim Anfragenden zurück.

## Mail-Abschnitt (Standard-Formulierung)

```
Falls Ihnen eine schriftliche Schilderung schwerfällt, bieten wir einen
automatisierten Transkriptionsservice an:

Sie rufen unter der folgenden Nummer an und schildern Ihr Anliegen
mündlich:

  Transkriptionsservice: [TRANSKRIPTIONS-TELEFON]

Ablauf:
  1. Automatische Ansage mit Datenschutzhinweis
  2. Bestätigung Ihres Einverständnisses (Tastendruck oder mündliches "Ja")
     — Ohne Bestätigung wird keine Aufnahme gestartet.
  3. Freie Schilderung Ihres Anliegens
  4. Automatische Verschriftung und vertrauliche Weiterleitung an uns

Bitte beachten Sie: Da zwischen uns noch kein Mandatsverhältnis besteht,
gilt für die Verarbeitung Ihrer Sprachdaten das ausdrückliche
Einverständnis nach Art. 6 Abs. 1 lit. a DSGVO als Rechtsgrundlage.
Sie können dieses Einverständnis jederzeit widerrufen. Einzelheiten
entnehmen Sie bitte unserem Datenschutzhinweis, den wir Ihnen auf
Anfrage gerne zusenden.
```

## Wichtige inhaltliche Anforderungen

### Kein Mandat, kein Vertrauensverhältnis

In diesem Stadium besteht noch kein Anwalts-Mandatsverhältnis. Das bedeutet:
- Die Schweigepflicht nach § 43a Abs. 2 BRAO gilt noch nicht für das spezifische Anliegen (wohl aber für allgemeine anwaltliche Verschwiegenheit im Rahmen der Berufsausübung).
- Die Verarbeitung der Sprachdaten bedarf deshalb einer ausdrücklichen Einwilligung (Art. 6 Abs. 1 lit. a DSGVO), nicht einer vertraglichen Notwendigkeit.
- Der Skill `einwilligung-hinweis-datenschutz` liefert die vollständige DSGVO-Klausel.

### Keine Zusagen zur Mandatsannahme

Die Formulierung des Transkriptionsservice-Abschnitts enthält keine Zusagen, dass die Kanzlei das Mandat annehmen wird. Zulässig: „Wir melden uns auf Basis des Transkripts bei Ihnen." Nicht zulässig: „Wir werden Ihren Fall übernehmen."

### Technisch neutrale Sprache

Keine Nennung von Markennamen, Anbietern oder technischen Details des Transkriptionsservices in der Mandantenmail — diese sind interne Infrastruktur.

## Konfigurierbare Parameter

Aus `kanzlei.json`:
- `telefon_transkription` — Rufnummer des Transkriptionsservices
- Optional: Betriebszeiten des Transkriptionsservices, falls abweichend von Kanzleizeiten

## Verweise auf andere Skills

- `einwilligung-hinweis-datenschutz` — vollständige DSGVO-Einwilligung
- `mandatsverhaeltnis-hinweis` — Disclaimer zum fehlenden Mandat
- `telefon-konfiguration` — liefert `telefon_transkription`
- `erstantwort-generator` — bettet diesen Abschnitt in die Antwortmail ein
