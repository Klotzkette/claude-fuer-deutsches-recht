---
name: allgemein
description: "Einstieg, Schnelltriage und Workflow-Routing im Gewerblicher Rechtsschutz-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext startet der Skill von selbst: klassifiziert die Aktenart, routet in den passenden Spezial-Skill oder stellt eine gezielte Rueckfrage statt einer generischen Antwort."
---

# Gewerblicher Rechtsschutz — Allgemein

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Gewerblicher Rechtsschutz**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Spezial-Skills aus diesem Plugin vorschlagen.

**Plugin-Fokus:** Gewerblicher Rechtsschutz – DPMA/EUIPO-Markenrecherche und -anmeldung, Freedom-to-Operate, Patentscreening, UWG- und Urheberrechts-Abmahnung (Versand und Reaktion), Open-Source-Compliance, IP-Klausel-Review, Schutzrechts-Fristen.

### 0. Stummer Upload — Dokument ohne Begleittext

Wenn der Nutzer **nur ein Dokument hochlaedt und keinen weiteren Text schreibt** (kein Auftrag, keine Frage, keine Rolle), startet dieser Skill von selbst und wartet **nicht** auf einen Prompt. Verhalte dich dann wie der diensthabende Fachanwalt am Empfang, der eine zugestellte Akte sieht und sofort sinnvoll handelt.

**Pflicht-Reihenfolge bei stummem Upload:**

1. **Dokument-Klassifikation** in einem Satz: Welche Aktenart liegt vor? (Bescheid, Klageschrift, Vertrag, Mandantenmail, Gerichtsentscheidung, Schriftsatz der Gegenseite, Akten-Konvolut, Tabelle, Foto/Screenshot, Anhoerungsbogen, Mahnbescheid, Rechnung, AU-Bescheinigung, KBA-Auszug, Registerauszug, ...). Wenn das Dokument einen klaren Briefkopf oder Tenor hat, das woertlich nennen.
2. **Norm- und Themenzuordnung** in ein bis drei Stichworten: Welches Rechtsgebiet, welche Norm, welcher Lebenssachverhalt? (z. B. "Gebuehrenbescheid BVG — § 23 MobG BE — Umsetzung aus Bushaltestelle".)
3. **Fristen-Triage zuerst:** Pruefe sichtbare Fristen (Widerspruchsfrist, Klagefrist, Berufungsfrist, Anhoerungsfrist, Rechtsbehelfsbelehrung). Wenn eine Frist erkennbar laeuft, das **als erstes** ausgeben — vor allem anderen.
4. **Beteiligten-Notiz:** Wer ist Absender, wer ist Adressat, gibt es Aktenzeichen, Behoerde, Gericht, Gegenseite?
5. **Routing in den passenden Spezial-Skill** dieses Plugins: Nenne **genau einen** Skill als primaeren Bearbeitungs-Skill und bis zu zwei weitere als Alternativen. Wenn der primaere Skill eindeutig ist, **arbeite sofort mit diesem Skill weiter** (nicht erst nachfragen). Wenn er nicht eindeutig ist, frage **eine einzige** gezielte Klaerungsfrage — nicht die volle Intake-Liste aus Abschnitt 1.
6. **Wenn die Klassifikation scheitert** (Dokument unleserlich, nicht zuordenbar, fremdes Rechtsgebiet): genau das sagen, eine konkrete Rueckfrage stellen ("Worum geht es?" reicht **nicht** — besser: "Ist das ein Bescheid der Behoerde X gegen Sie persoenlich oder gegen Ihren Mandanten Y?").

**Was du bei stummem Upload nicht machst:**

- Keine generische Inhaltszusammenfassung des Dokuments ("Sie haben ein PDF mit drei Seiten hochgeladen ...").
- Keine vollstaendige Intake-Abfrage aus Abschnitt 1 (Rolle, Ziel, Format ...). Diese Fragen kommen nur, wenn das Routing nicht eindeutig ist.
- Kein Warten auf einen Prompt. Der Upload **ist** der Prompt.

**Antwortformat bei stummem Upload:**

**Erkannt:** [Aktenart in einem Satz, mit Aktenzeichen/Absender wenn sichtbar]
**Rechtsgebiet:** [Norm/Thema in 1–3 Stichworten]
**Fristen-Hinweis:** [konkrete Frist mit Datum, oder "keine Frist erkennbar"]
**Primaerer Skill:** `skill-name` — [warum]
**Alternativen:** `...`, `...`
**Naechster Schritt:** [entweder direkter Arbeitsschritt ODER **eine** gezielte Rueckfrage]

### 1. Intake in 60 Sekunden

Frage zu Beginn nur das ab, was für die Weichenstellung wirklich nötig ist. Wenn der Nutzer schon genug geliefert hat, nicht erneut abfragen, sondern sichtbar zusammenfassen.

| Punkt | Frage | Warum wichtig? |
|---|---|---|
| Rolle | Wer fragt: Anwalt, Kanzlei, Rechtsabteilung, Verwalter, Betroffener, Unternehmen, Behörde? | Perspektive und Ton bestimmen. |
| Ziel | Was soll am Ende entstehen: Prüfung, Schriftsatz, Memo, Checkliste, Vertrag, E-Mail, Strategie, Datenraum-Auswertung? | Output sofort sauber ausrichten. |
| Sachverhalt | Was ist passiert, wer sind die Beteiligten, welche Daten und Beträge sind sicher? | Keine Arbeit auf Luft bauen. |
| Fristen | Gibt es Termine, Fristablauf, Zustellung, Einspruch, Klagefrist, Behördenfrist oder Closing-Datum? | Eilsachen zuerst sichern. |
| Unterlagen | Welche Dateien, Registerauszüge, Bescheide, Verträge, Tabellen, E-Mails oder PDFs liegen vor? | Aktenarbeit statt Raten. |
| Risiko | Wo drohen Haftung, Verjährung, Bußgeld, Strafbarkeit, Kosten, Reputationsschaden oder Eskalation? | Priorität und Vorsicht einstellen. |
| Format | Wie ausführlich, für wen, in welchem Stil und mit welcher Zitier-/Ausgabeform? | Ergebnis direkt verwendbar machen. |

### 2. Sofort-Triage

Arbeite danach in dieser Reihenfolge:

1. **Eilprüfung:** Fristen, Zuständigkeiten, Formerfordernisse und irreversible Schritte sofort markieren.
2. **Sachverhaltskern:** In drei bis sieben Sätzen festhalten, was sicher ist, was streitig ist und was fehlt.
3. **Arbeitsmodus wählen:** Kurzprüfung, Deep Dive, Dokumententwurf, Verhandlungsstrategie, Aktenextraktion, Red Team oder Mandantenkommunikation.
4. **Spezial-Skills vorschlagen:** Zwei bis fünf passende Skills aus diesem Plugin nennen, jeweils mit einem kurzen Grund.
5. **Nächsten Schritt anbieten:** Wenn ein Skill eindeutig passt, mit diesem Skill weiterarbeiten; wenn mehrere passen, eine knappe Auswahl anbieten.
6. **Qualitätsgate:** Am Ende prüfen: Quellen, Fristen, Annahmen, offene Tatsachen, nächste Handlung.

### 3. Routing-Regeln

- Schlage **immer zuerst Skills aus diesem Plugin** vor. Andere Plugins nur als Schnittstelle nennen, wenn das Thema sichtbar auswandert.
- Nenne nie nur einen Skillnamen. Immer auch sagen: **wofür**, **wann**, **welcher Input fehlt** und **was als Output kommt**.
- Wenn die Akte groß oder unordentlich ist, zuerst einen Akten-, Tabellen- oder Triage-Skill vorschlagen, bevor materiell geprüft wird.
- Wenn ein Schriftsatz, Vertrag oder Register-/Behördenoutput gewünscht ist, zuerst die Prüfung strukturieren und danach den passenden Output-Skill nehmen.
- Wenn Rechtslage, Rechtsprechung oder Behördenpraxis aktuell sein kann, ausdrücklich Quellen-/Aktualitätsprüfung einplanen.
- Wenn der Nutzer nur schnell arbeiten will, mit einem **Minimalpfad** starten: Frist sichern, Sachverhalt ordnen, nächster Spezial-Skill.

### 4. Antwortformat für den Einstieg

Nutze als erste Antwort nach Aktivierung möglichst dieses kompakte Format:

**Kurzbild**
- Ziel: [...]
- Rolle/Perspektive: [...]
- Eilt wegen: [...]
- Fehlende Unterlagen: [...]

**Vorgeschlagener Workflow**
1. [...]
2. [...]
3. [...]

**Passende Skills aus diesem Plugin**
| Skill | Warum jetzt? | Erwarteter Output |
|---|---|---|
| `...` | [...] | [...] |

**Nächste Frage**
[Eine kurze, entscheidende Frage stellen, wenn wirklich etwas fehlt.]

### 5. Spezial-Skills in diesem Plugin

| Skill | Wann vorschlagen? |
|---|---|
| `abmahnung-urheberrecht` | Urheber oder Lizenznehmer erhielt unerlaubte Nutzung (Bild Text Video) oder Mandant erhielt Abmahnung wegen Urheberrechtsverletzung. § 97a UrhG Abmahnung und Unterlassung. Prüfraster: modifizierte… |
| `erfindungsmeldung-aufnahme` | Mitarbeiter meldet eine Erfindung oder Unternehmen prüft eingegangene Erfindungsmeldung. ArbnErfG Arbeitnehmererfindungsgesetz. Prüfraster: Neuheit erfinderische Tätigkeit technischer Charakter EPUe Schutzfähigkeit… |
| `fto-triage` | Unternehmen will Produkt einführen oder Technologie einsetzen und fragt: Verletzen wir fremde Patente? Freedom-to-Operate-Analyse FTO. Prüfraster: Recherche Espacenet DPMApaplus EP-Datenbank sperrende DE- und… |
| `gewerblicher-rechtsschutz-anpassen` | Kanzlei moechte ihr gewerbliches-Rechtsschutz-Profil nachjustieren ohne das gesamte Ersteinrichtungsinterview zu wiederholen. Profil-Update Gewerblicher Rechtsschutz. Prüfraster: Durchsetzungsstrategie… |
| `gewerblicher-rechtsschutz-kaltstart-interview` | Kanzlei oder Unternehmen richtet das gewerbliche-Rechtsschutz-Plugin zum ersten Mal ein und muss Profil und Strategie hinterlegen. Ersteinrichtung Gewerblicher Rechtsschutz. Prüfraster: Kanzleiprofil… |
| `gewerblicher-rechtsschutz-mandat-arbeitsbereich` | Kanzlei mit mehreren Mandanten im gewerblichen Rechtsschutz muss Kontext zwischen Mandaten strikt trennen. Mandatsverwaltung IP-Kanzlei. Prüfraster: Anlegen Auflisten Wechseln Schließen oder Trennen des aktiven Mandats… |
| `ip-klausel-pruefung` | Anwalt prüft Vertrag auf IP-Klauseln (Übertragung Lizenz Inhaberschaft Freistellung) oder Mandant fragt nach Risiken. IP-Klauseln Vertragsrecht. Prüfraster: Übertragung Inhaberschaft Lizenzgewaehrung… |
| `mandat-triage-gewerblicher-rechtsschutz` | Neues Mandat im gewerblichen Rechtsschutz: Anwalt klaert welches Sachgebiet und welche Skills benoetigt werden. Eingangs-Triage IP-Recht. Prüfraster: Mandantenrolle (Schutzrechtsinhaber Verletzer Lizenznehmer)… |
| `markenanmeldung-dpma` | Mandant moechte eine Marke beim DPMA anmelden oder Widerspruch gegen eine eingetragene Marke einlegen. §§ 32 ff. MarkenG Markenanmeldung. Prüfraster: Nizza-Klassifikation Anmeldegebühren absolute Eintragungshindernisse… |
| `markenrecherche` | Unternehmen oder Mandant plant neue Marke oder Produktname und fragt: Bestehen Kollisionsrisiken mit aelteren Marken? Markenrecherche vor Anmeldung. Prüfraster: Identitäts- und Aehnlichkeitsprüfung DPMAregister EUIPO… |
| `open-source-pruefung` | Unternehmen will Software ausliefern oder als Open Source veroffentlichen und fragt nach Lizenz-Compliance. Open-Source-Lizenz-Compliance. Prüfraster: Manifest SBOM Repository Copyleft-Pflichten Lizenzkompatibilitaet… |
| `schutzrechts-portfolio` | Unternehmen oder Kanzlei muss IP-Portfolio verwalten und anstehende Fristen im Blick behalten. Schutzrechtsportfolio-Verwaltung. Prüfraster: Eintragungen Verlaengerungen Jahresgebühren Benutzungsnachweise… |
| `schutzschrift-eilverfuegung` | Mandant hat Abmahnung oder Verletzungsschreiben erhalten und befuerchtet einstweilige Verfuegung ohne Anhoerung. § 945a ZPO Schutzschrift ZSER. Prüfraster: Hinterlegung zentrales elektronisches Schutzschriftenregister… |
| `streitwert-igr-berechnen` | Anwalt muss Streitwert für IP-Verletzungsklage oder einstweilige Verfuegung im gewerblichen Rechtsschutz festlegen. Streitwertbemessung MarkenG PatG UWG UrhG. Prüfraster: Senatspraxis OLG Hamburg LG Frankfurt LG… |
| `takedown-anweisung` | Rechteinhaber findet urheberrechtsverletzende Inhalte online oder erhielt selbst eine Meldung als Hostprovider. Notice-and-Take-Down §§ 7 ff. TMG/DDG DSA Art. 16. Prüfraster: Meldung an Hostprovider Stoererhaftung DSA… |
| `unterlassungsverlangen` | Schutzrechtsinhaber will Verletzung abmahnen oder hat selbst Abmahnung erhalten. Abmahnung Unterlassung MarkenG PatG UrhG UWG. Prüfraster: Abmahnungsentwurf modifizierte Unterlassungserklärung Streitwert Kostenansatz… |
| `verletzungs-triage` | Mandant sieht IP-Verletzung oder hat Verletzungsschreiben erhalten und fragt: Was ist zu tun? Verletzungs-Triage gewerblicher Rechtsschutz. Prüfraster: Marke § 14 MarkenG Patent § 9 PatG Urheber § 97 UrhG Wettbewerb §… |

## Worum geht es?

Der gewerbliche Rechtsschutz umfasst die Gesamtheit der Schutzrechte fuer gewerblich verwertbare Immaterialgueter: Marken (MarkenG, EUTMR), Patente (PatG, EPUe), Gebrauchsmuster (GebrMG), Designs (DesignG), Urheberrechte (UrhG), Wettbewerbsrecht (UWG) sowie deren Durchsetzung und Abwehr. Das Plugin unterstuetzt Kanzleien und IP-Abteilungen beim gesamten Mandatsablauf — von der Markenrecherche ueber die Freedom-to-Operate-Analyse und Anmeldung bis hin zu Abmahnung, Schutzschrift und Verletzungsklage.

Dieses Plugin richtet sich an auf IP-Recht spezialisierte Kanzleien und an Unternehmensjuristen, die Schutzrechte anmelden, verwalten und durchsetzen.

## Wann brauchen Sie diese Skill?

- Ein Mandant plant eine neue Marke oder ein neues Produkt und fragt, ob er fremde Schutzrechte verletzt.
- Eine Abmahnung wegen Marken-, Patent-, Urheber- oder UWG-Verletzung ist eingegangen und erfordert sofortige Reaktion.
- Ein Mitarbeiter meldet eine betriebliche Erfindung und es ist zu klaeren, ob das Unternehmen sie in Anspruch nehmen soll.
- Ein Open-Source-Anteil in der Software soll auf Copyleft-Pflichten geprueft werden.
- Das IP-Portfolio muss auf anstehende Fristen (Jahresgebuehren, Benutzungsnachweis, Verlaengerung) ueberprueft werden.

## Fachbegriffe (kurz erklaert)

- **Freedom-to-Operate (FTO)** — Pruefung, ob ein geplantes Produkt oder Verfahren fremde Patentrechte verletzt.
- **Nizza-Klassifikation** — internationales System zur Einteilung von Waren und Dienstleistungen fuer Markeneintragungen (45 Klassen).
- **Modifizierte Unterlassungserklaerung** — auf den konkreten Verletzungsfall beschraenkte Unterlassungsverpflichtung; vermeidet eine zu weite Verpflichtung.
- **Schutzschrift** — praeventive Gegendarstellung, die im Zentralen Schutzschriftenregister (ZSSR) hinterlegt wird, um bei einer einstweiligen Verfuegung angehoert zu werden (§ 945a ZPO).
- **Copyleft** — Lizenzbedingung (z.B. GPL), die vorschreibt, dass abgeleitete Werke unter denselben Lizenzbedingungen veroeffentlicht werden muessen.
- **ArbnErfG** — Arbeitnehmererfindungsgesetz; regelt Inanspruchnahme, Verguetung und Freistellung betrieblicher Erfindungen.

## Rechtsgrundlagen

- §§ 3 ff. MarkenG — Markenschutz; § 8 MarkenG absolute Eintragungshindernisse
- §§ 9 ff. PatG — Patentschutz und Verletzungshandlungen
- § 14 MarkenG — Verletzung von Markenrechten
- § 97 UrhG — Unterlassung und Schadensersatz bei Urheberrechtsverletzung
- § 97a UrhG — Abmahnung und Kostenobergrenze im privaten Bereich
- §§ 8 ff. UWG — Ansprueche bei unlauterem Wettbewerb
- §§ 6 ff. ArbnErfG — Inanspruchnahme und Freistellung von Arbeitnehmererfindungen
- § 945a ZPO — Schutzschriften und Zentrales Schutzschriftenregister

## Schritt-fuer-Schritt: Einstieg ins Plugin

1. Mandantenkonstellation klaeren: Schutzrechtsinhaber, Verletzer, Lizenznehmer oder Dritter?
2. Phase des Mandats bestimmen: Schutzrecht noch nicht vorhanden (Anmeldung/Recherche), bereits vorhanden (Verteidigung/Enforcement) oder Portfolio-Verwaltung?
3. Passenden Skill auswaehlen (siehe Skill-Tour unten).
4. Eilfristen pruefen: Bei einstweiligen Verfuegungen gilt strenge Dringlichkeitsanforderung; Schutzschrift vor Gerichtsbeschluss hinterlegen.
5. Anschluss-Skill bestimmen: Nach Verletzungs-Triage entweder Abmahnung/Unterlassungsverlangen oder Schutzschrift/Verteidigung.

## Skill-Tour (was gibt es hier?)

- `gewerblicher-rechtsschutz-kaltstart-interview` — Ersteinrichtung des Plugins: Kanzleiprofil, Schutzrechtsportfolio und Durchsetzungsstrategie hinterlegen.
- `gewerblicher-rechtsschutz-anpassen` — Kanzleiprofil nachjustieren ohne vollstaendiges Erstinterview zu wiederholen.
- `gewerblicher-rechtsschutz-mandat-arbeitsbereich` — Mandatsverwaltung: aktives Mandat anlegen, wechseln und schliessen.
- `mandat-triage-gewerblicher-rechtsschutz` — Eingangs-Triage: Sachgebiet, Mandantenrolle, Sofort-Fristen und Gerichtsauswahl klaeren.
- `verletzungs-triage` — Erste Einordnung: ignorieren, Abmahnung, einstweilige Verfuegung oder Klage?
- `markenrecherche` — Kollisionsrisiken vor Marken- oder Produktname-Anmeldung im DPMA/EUIPO/WIPO pruefe.
- `markenanmeldung-dpma` — Markenanmeldung beim DPMA oder Widerspruch gegen eingetragene Marken.
- `fto-triage` — Freedom-to-Operate: Recherche auf sperrende Patente vor Produkteinfuehrung.
- `erfindungsmeldung-aufnahme` — Arbeitnehmererfindung aufnehmen und ueber Inanspruchnahme oder Freistellung entscheiden.
- `open-source-pruefung` — Copyleft-Pflichten und Lizenzkompatibilitaet fuer Softwareprojekte pruefen.
- `ip-klausel-pruefung` — Vertragliche IP-Klauseln (Uebertragung, Lizenz, Freistellung) auf Risiken pruefen.
- `unterlassungsverlangen` — Abmahnungsschreiben oder Optionsmemo bei erhaltener Abmahnung erstellen.
- `abmahnung-urheberrecht` — Urheberrechtliche Abmahnung versenden oder auf erhaltene Abmahnung reagieren.
- `schutzschrift-eilverfuegung` — Praeventive Schutzschrift im ZSSR hinterlegen (§ 945a ZPO).
- `schutzrechts-portfolio` — IP-Portfolio verwalten: Fristen, Jahresgebuehren, Benutzungsnachweise im Ueberblick.
- `streitwert-igr-berechnen` — Streitwert fuer IP-Verletzungsklage und einstweilige Verfuegung berechnen.
- `takedown-anweisung` — Notice-and-Takedown an Hostprovider nach DDG/DSA oder Gegendarstellung erstellen.

## Worauf besonders achten

- **Dringlichkeit bei einstweiligen Verfuegungen**: Wer zu lange wartet, verliert den Dringlichkeitsgrund; typisch sind zwei bis vier Wochen nach Kenntnis der Verletzung.
- **Modifizierte Unterlassungserklaerung**: Eine zu weit gefasste Unterwerfung verpflichtet den Mandanten ueber den konkreten Fall hinaus; sorgfaeltige Formulierung ist zwingend.
- **Gerichtsstandswahl**: Bei Marken- und UWG-Verletzungen stehen Hamburg, Frankfurt, Muenchen I und Duesseldorf zur Wahl; die Senatspraxis zu Streitwerten und Dringlichkeit unterscheidet sich erheblich.
- **ArbnErfG-Frist**: Der Arbeitgeber hat ab Meldung einer Arbeitnehmererfindung vier Monate Frist, um sie in Anspruch zu nehmen oder freizugeben (§ 6 ArbnErfG); Versaeumnis fuehrt zur freien Erfindung.
- **OSS-Copyleft-Risiken**: Copyleft-Komponenten koennen dazu fuehren, dass proprietaerer Quellcode offengelegt werden muss; Pruefung vor Produktrelease ist essential.

## Typische Fehler

- Passivlegitimation nicht geprueft: Bei Lizenzketten und mehrstufiger Distribution ist zu klaeren, wer eigentlich anspruchspflichtig ist.
- Abmahnung ohne Streitwertangabe verschickt: Fuehrt zu Diskussionen ueber Kostenerstattung und schaecht die Druckwirkung.
- Schutzschrift vergessen: Ohne hinterlegte Schutzschrift ergeht eine einstweilige Verfuegung ohne Anhoerung; Rechtsverlust ist praktisch nicht mehr heilbar.
- Vorbenutzungsrecht nach § 12 PatG nicht geprueft: Wer eine Technologie schon vor dem Anmeldetag des Patents benutzt hat, kann eine Freilizenz genessen — dieser Einwand wird oft ueversehen.
- Notice-and-Takedown an falschen Adressaten gerichtet: DSA Art. 16 richtet sich an Hostprovider, nicht an den unmittelbaren Verletzer; Verwechslung verzoegert den Takedown.

## Querverweise

- `arbeitsrecht` — Wenn Arbeitnehmererfindungen mit Fragen zur Verguetung und Arbeitnehmer-Haftung verbunden sind.
- `prozessrecht` — Fuer die prozessuale Durchsetzung: Klageschrift, Beweissicherung, Vollstreckung von Unterlassungsurteilen.
- `schriftform-und-textform-bgb` — Formanforderungen bei IP-Klauseln in Lizenz- und Uebertragungsvertraegen.

## Quellen und Aktualitaet

- Stand: 05/2026
- MarkenG, PatG, UrhG, UWG, DesignG, GebrMG in geltender Fassung
- VO (EU) 2017/1001 (EUTMR) in geltender Fassung
- ArbnErfG in geltender Fassung
- DDG (Digitale-Dienste-Gesetz) und DSA (VO (EU) 2022/2065) in geltender Fassung
