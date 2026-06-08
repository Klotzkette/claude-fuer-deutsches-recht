---
name: start-chronologie-fristen
description: "Einstieg, Schnelltriage und Fallrouting im Gewerblicher Rechtsschutz-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext reagiert der Skill eigenständig: ordnet das Material, prüft Eil- und Fristenhinweise, routet in passende Fachmodule oder stellt genau eine gezielte Rückfrage im Gewerblicher Rechtsschutz."
---

# Gewerblicher Rechtsschutz — Allgemein

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Gewerblicher Rechtsschutz**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Fachmodule aus diesem Plugin vorschlagen.

**Plugin-Fokus:** Gewerblicher Rechtsschutz – DPMA/EUIPO-Markenrecherche und -anmeldung, Freedom-to-Operate, Patentscreening, UWG- und Urheberrechts-Abmahnung (Versand und Reaktion), Open-Source-Compliance, IP-Klausel-Review, Schutzrechts-Fristen.

### 0. Stummer Upload — Material ohne Begleittext

Wenn der Nutzer nur ein Dokument, einen Screenshot, eine Tabelle, ein ZIP oder ein Aktenkonvolut hochlädt und keinen Auftrag dazuschreibt, behandle den Upload als Arbeitsauftrag. Warte nicht auf einen Prompt. Arbeite als aufmerksamer juristischer Co-Pilot: erst sichern, was eilt, dann das Material einordnen, dann den besten nächsten Arbeitsschritt anbieten.

**Pflicht-Reihenfolge bei stummem Upload:**

1. **Eil- und Fristenscan:** Prüfe sofort sichtbare Zustellungen, Rechtsbehelfsbelehrungen, Fristen, Termine, Vollziehungsrisiken, Zahlungsziele, Verjährungs- oder Ausschlussfristen. Wenn etwas eilt, beginne die Antwort mit `Frist zuerst: ...`.
2. **Material-Klassifikation:** Benenne in einem Satz, was vorliegt: Bescheid, Klageschrift, Vertrag, Mandantenmail, Gerichtsentscheidung, Schriftsatz, Tabellenwerk, Registerauszug, Rechnung, beA-/EGVP-Nachricht, Screenshot, Foto, Chatverlauf oder Aktenkonvolut.
3. **Kontextanker:** Notiere Absender, Adressat, Aktenzeichen, Gericht/Behörde/Gegenseite, Datum und erkennbaren Lebenssachverhalt. Wenn der Text unleserlich ist, sage genau, welcher Teil fehlt.
4. **Rechts- und Arbeitsthema:** Ordne das Material knapp einem Rechtsgebiet, einer Normengruppe oder einem Arbeitsmodus zu. Zitiere nur, was im Material oder im Plugin-Kontext wirklich trägt.
5. **Routing:** Schlage zuerst einen passenden Fachmodul aus diesem Plugin vor. Wenn der Treffer eindeutig ist, arbeite direkt in dessen Richtung weiter. Wenn mehrere Wege sinnvoll sind, nenne einen bevorzugten Primärpfad und höchstens zwei Alternativen mit Nutzen.
6. **Nur eine Rückfrage:** Frage nur dann nach, wenn ohne die Antwort ein falscher nächster Schritt droht. Die Rückfrage muss konkret sein und an das erkannte Material anknüpfen.

**Was du bei stummem Upload nicht machst:**

- Keine generische Upload-Bestätigung.
- Keine vollständige Intake-Liste aus Abschnitt 1.
- Keine erfundenen Dokumentdetails, Fristen, Anlagen oder Fundstellen.
- Keine unnötige Begrenzungsrhetorik; mache klar, wie das Material jetzt praktisch weiterverarbeitet werden kann.

**Antwortformat bei stummem Upload:**

- **Erkannt:** [Materialart, Absender/Aktenzeichen falls sichtbar]
- **Frist zuerst:** [konkretes Datum/Risiko oder `keine Frist erkennbar`]
- **Einordnung:** [Rechtsgebiet/Normengruppe/Arbeitsmodus]
- **Primärer Pfad:** `skill-name` — [warum dieser Arbeitsgang hilft]
- **Alternativen:** `...`, `...`
- **Nächster Schritt:** [direkte Bearbeitung oder genau eine konkrete Rückfrage]

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
4. **Fachmodule vorschlagen:** Zwei bis fünf passende Skills aus diesem Plugin nennen, jeweils mit einem kurzen Grund.
5. **Nächsten Schritt anbieten:** Wenn ein Skill eindeutig passt, mit diesem Skill weiterarbeiten; wenn mehrere passen, eine knappe Auswahl anbieten.
6. **Qualitätsgate:** Am Ende prüfen: Quellen, Fristen, Annahmen, offene Tatsachen, nächste Handlung.

### 3. Routing-Regeln

- Schlage **immer zuerst Skills aus diesem Plugin** vor. Andere Plugins nur als Schnittstelle nennen, wenn das Thema sichtbar auswandert.
- Nenne nie nur einen Skillnamen. Immer auch sagen: **wofür**, **wann**, **welcher Input fehlt** und **was als Output kommt**.
- Wenn die Akte groß oder unordentlich ist, zuerst einen Akten-, Tabellen- oder Triage-Skill vorschlagen, bevor materiell geprüft wird.
- Wenn ein Schriftsatz, Vertrag oder Register-/Behördenoutput gewünscht ist, zuerst die Prüfung strukturieren und danach den passenden Output-Skill nehmen.
- Wenn Rechtslage, Rechtsprechung oder Behördenpraxis aktuell sein kann, ausdrücklich Quellen-/Aktualitätsprüfung einplanen.
- Wenn der Nutzer nur schnell arbeiten will, mit einem **Minimalpfad** starten: Frist sichern, Sachverhalt ordnen, nächster Fachmodul.

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

### 5. Fachmodule in diesem Plugin

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
| `schutzschrift-eilverfuegung` | Mandant hat Abmahnung oder Verletzungsschreiben erhalten und befürchtet einstweilige Verfuegung ohne Anhörung. § 945a ZPO Schutzschrift ZSER. Prüfraster: Hinterlegung zentrales elektronisches Schutzschriftenregister… |
| `streitwert-igr-berechnen` | Anwalt muss Streitwert für IP-Verletzungsklage oder einstweilige Verfuegung im gewerblichen Rechtsschutz festlegen. Streitwertbemessung MarkenG PatG UWG UrhG. Prüfraster: Senatspraxis OLG Hamburg LG Frankfurt LG… |
| `takedown-anweisung` | Rechteinhaber findet urheberrechtsverletzende Inhalte online oder erhielt selbst eine Meldung als Hostprovider. Notice-and-Take-Down §§ 7 ff. TMG/DDG DSA Art. 16. Prüfraster: Meldung an Hostprovider Stoererhaftung DSA… |
| `unterlassungsverlangen` | Schutzrechtsinhaber will Verletzung abmahnen oder hat selbst Abmahnung erhalten. Abmahnung Unterlassung MarkenG PatG UrhG UWG. Prüfraster: Abmahnungsentwurf modifizierte Unterlassungserklärung Streitwert Kostenansatz… |
| `verletzungs-triage` | Mandant sieht IP-Verletzung oder hat Verletzungsschreiben erhalten und fragt: Was ist zu tun? Verletzungs-Triage gewerblicher Rechtsschutz. Prüfraster: Marke § 14 MarkenG Patent § 9 PatG Urheber § 97 UrhG Wettbewerb §… |

## Worum geht es?

Der gewerbliche Rechtsschutz umfasst die Gesamtheit der Schutzrechte für gewerblich verwertbare Immaterialgueter: Marken (MarkenG, EUTMR), Patente (PatG, EPUe), Gebrauchsmuster (GebrMG), Designs (DesignG), Urheberrechte (UrhG), Wettbewerbsrecht (UWG) sowie deren Durchsetzung und Abwehr. Das Plugin unterstuetzt Kanzleien und IP-Abteilungen beim gesamten Mandatsablauf — von der Markenrecherche ueber die Freedom-to-Operate-Analyse und Anmeldung bis hin zu Abmahnung, Schutzschrift und Verletzungsklage.

Dieses Plugin richtet sich an auf IP-Recht spezialisierte Kanzleien und an Unternehmensjuristen, die Schutzrechte anmelden, verwalten und durchsetzen.

## Wann brauchen Sie diese Skill?

- Ein Mandant plant eine neue Marke oder ein neues Produkt und fragt, ob er fremde Schutzrechte verletzt.
- Eine Abmahnung wegen Marken-, Patent-, Urheber- oder UWG-Verletzung ist eingegangen und erfordert sofortige Reaktion.
- Ein Mitarbeiter meldet eine betriebliche Erfindung und es ist zu klaeren, ob das Unternehmen sie in Anspruch nehmen soll.
- Ein Open-Source-Anteil in der Software soll auf Copyleft-Pflichten geprueft werden.
- Das IP-Portfolio muss auf anstehende Fristen (Jahresgebuehren, Benutzungsnachweis, Verlaengerung) ueberprueft werden.

## Fachbegriffe (kurz erklaert)

- **Freedom-to-Operate (FTO)** — Pruefung, ob ein geplantes Produkt oder Verfahren fremde Patentrechte verletzt.
- **Nizza-Klassifikation** — internationales System zur Einteilung von Waren und Dienstleistungen für Markeneintragungen (45 Klassen).
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

## Schritt-für-Schritt: Einstieg ins Plugin

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
- `open-source-pruefung` — Copyleft-Pflichten und Lizenzkompatibilitaet für Softwareprojekte pruefen.
- `ip-klausel-pruefung` — Vertragliche IP-Klauseln (Uebertragung, Lizenz, Freistellung) auf Risiken pruefen.
- `unterlassungsverlangen` — Abmahnungsschreiben oder Optionsmemo bei erhaltener Abmahnung erstellen.
- `abmahnung-urheberrecht` — Urheberrechtliche Abmahnung versenden oder auf erhaltene Abmahnung reagieren.
- `schutzschrift-eilverfuegung` — Praeventive Schutzschrift im ZSSR hinterlegen (§ 945a ZPO).
- `schutzrechts-portfolio` — IP-Portfolio verwalten: Fristen, Jahresgebuehren, Benutzungsnachweise im Ueberblick.
- `streitwert-igr-berechnen` — Streitwert für IP-Verletzungsklage und einstweilige Verfuegung berechnen.
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
- Schutzschrift vergessen: Ohne hinterlegte Schutzschrift ergeht eine einstweilige Verfuegung ohne Anhörung; Rechtsverlust ist praktisch nicht mehr heilbar.
- Vorbenutzungsrecht nach § 12 PatG nicht geprueft: Wer eine Technologie schon vor dem Anmeldetag des Patents benutzt hat, kann eine Freilizenz genessen — dieser Einwand wird oft ueversehen.
- Notice-and-Takedown an falschen Adressaten gerichtet: DSA Art. 16 richtet sich an Hostprovider, nicht an den unmittelbaren Verletzer; Verwechslung verzoegert den Takedown.

## Quellen und Aktualitaet

- Stand: 05/2026
- MarkenG, PatG, UrhG, UWG, DesignG, GebrMG in geltender Fassung
- VO (EU) 2017/1001 (EUTMR) in geltender Fassung
- ArbnErfG in geltender Fassung
- DDG (Digitale-Dienste-Gesetz) und DSA (VO (EU) 2022/2065) in geltender Fassung

