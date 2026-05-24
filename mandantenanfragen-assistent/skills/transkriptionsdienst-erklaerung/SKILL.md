---
name: transkriptionsdienst-erklaerung
description: "Formuliert den Hinweis auf den automatisierten Transkriptionsservice in der Erstantwort: Telefonnummer, Ablauf des Anrufs, Verarbeitungshinweis, DSGVO-Einwilligungserfordernis und Kein-Mandat-Hinweis. Nur fuer Anfragen bei denen schriftliche Schilderung nicht moeglich oder gewuenscht ist. Laedt wenn der Nutzer 'Transkriptionsservice erklaeren', 'Sprachaufnahme anbieten', 'kann nicht schreiben', 'Diktat Sachverhalt' oder 'Transkription Erstanfrage' sagt."
---

# Transkriptionsdienst-Erklärung

Dieser Skill formuliert den vollständigen Abschnitt in der Erstantwort-Mail, in dem der automatisierte Transkriptionsservice beschrieben wird. Er kommt zum Einsatz, wenn die anfragende Person signalisiert, dass sie ihren Sachverhalt nicht schriftlich schildern kann oder möchte.

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
