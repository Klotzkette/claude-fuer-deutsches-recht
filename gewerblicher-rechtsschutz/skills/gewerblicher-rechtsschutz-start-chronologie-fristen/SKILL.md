---
name: gewerblicher-rechtsschutz-start-chronologie-fristen
description: "Start Chronologie Fristen: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Start Chronologie Fristen

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Start Chronologie Fristen** im Plugin Gewerblicher Rechtsschutz. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `allgemein` | Einstieg, Schnelltriage und Fallrouting im Gewerblicher Rechtsschutz-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext reagiert der Skill eigenständig: ordnet das Material, prüft Eil- und Fristenhinweise, routet in passende Fachmodule oder stellt genau eine gezielte Rückfrage. |
| `workflow-chronologie-und-belegmatrix` | Chronologie und Belegmatrix für IP-Mandate: Sachverhalt zeitlich ordnen, Belege zu Ereignissen zuordnen, Lücken identifizieren und Beweisgrundlage für Abmahnung, EV und Klage aufbauen. Werkzeug für systematische Fallaufbereitung. |
| `workflow-fristen-und-risikoampel` | Fristenund Risikoampel für das Plugin gewerblicher-rechtsschutz: strukturierte Fristenerfassung, Risikobewertung Grün/Gelb/Rot und sofortige Handlungsempfehlung. Für alle IP-Verfahren vom Erstgespräch bis zur Vollstreckung. |

## Arbeitsweg

Im Plugin Gewerblicher Rechtsschutz gilt für **Start Chronologie Fristen**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `allgemein`

**Fokus:** Einstieg, Schnelltriage und Fallrouting im Gewerblicher Rechtsschutz-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext reagiert der Skill eigenständig: ordnet das Material, prüft Eil- und Fristenhinweise, routet in passende Fachmodule oder stellt genau eine gezielte Rückfrage.

## Konversationsstil – konzis starten, schnell zum Dokument

- **Erste Antwort kurz.** Sachverhalt einordnen, höchstens **eine** unverzichtbare Rückfrage stellen, dann arbeiten.
- **Kein Lehrbuch-Intro.** Keine Norm-Wiederholung, keine Selbstankündigung – sofort einsteigen.
- **Schnell zum Dokument.** Sobald die Mindestangaben vorliegen, liefere einen ersten Entwurf mit `[noch zu klären: …]`-Platzhaltern, statt weiter abzufragen.
- **Allgemein-Skill = Einstieg, nicht Vorlesung.** Triage, Rückfrage falls nötig, dann auf die Fachmodule dieses Plugins verweisen oder direkt den ersten Entwurf produzieren.
- **Ausführlich nur, wenn es das Arbeitsergebnis verlangt:** echte Subsumtion im Gutachtenstil, Tabellen, Chronologien, Risiko-/Beweislastanalysen, Schriftsatz- oder Memo-Text.
- **Erklärungen nur auf Nachfrage.** Wenn der Nutzer Hintergrund will, ausführlich. Sonst nicht.



# Gewerblicher Rechtsschutz — Allgemein

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


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `workflow-chronologie-und-belegmatrix`

**Fokus:** Chronologie und Belegmatrix für IP-Mandate: Sachverhalt zeitlich ordnen, Belege zu Ereignissen zuordnen, Lücken identifizieren und Beweisgrundlage für Abmahnung, EV und Klage aufbauen. Werkzeug für systematische Fallaufbereitung.

# Workflow: Chronologie und Belegmatrix

## Zweck

Dieser Skill erstellt eine **Sachverhalts-Chronologie und Belegmatrix** für IP- und Wettbewerbsrechtsmandate. Er ordnet Ereignisse zeitlich, weist Belege zu und identifiziert Lücken in der Beweiskette. Ohne strukturierte Chronologie verliert man in komplexen Fällen den Überblick.

Mandatsbezug: Mandant schildert einen komplexen Sachverhalt mit mehreren Verletzungshandlungen über längere Zeit. Anwalt muss daraus eine klare, zeitliche Abfolge mit Belegen erstellen, bevor er Abmahnung oder EV-Antrag vorbereitet.

## Chronologie-Aufbau

### Schritt 1 – Zeitachse anlegen

Folgende Ereignisse chronologisch erfassen:

| Datum | Ereignis | Beteiligte | Beleg | Status |
|---|---|---|---|---|
| [Datum] | Schutzrecht angemeldet | Mandant | Registerauszug | Gesichert |
| [Datum] | Schutzrecht eingetragen | DPMA/EUIPO | Urkunde | Gesichert |
| [Datum] | Verletzungshandlung erstmals | Verletzer | Screenshot | Gesichert |
| [Datum] | Erstkenntnis Mandant | Mandant | Eidesstattliche Versicherung | Glaubhaft |
| [Datum] | Abmahnung versandt | Mandant | Abmahnschreiben | Gesichert |
| [Datum] | Reaktion Gegenseite | Gegenseite | Antwortschreiben | Gesichert |
| [Datum] | EV beantragt | Mandant | Antragsschrift | Gesichert |
| [Datum] | EV erlassen | Gericht | EV-Beschluss | Gesichert |
| [Datum] | EV vollzogen | GV | Zustellurkunde | Gesichert |
| [Datum] | Verstoß gegen EV | Verletzer | Screenshot | Zu belegen |

### Schritt 2 – Lücken identifizieren

**Lückenkategorien:**

1. **Beleg fehlt ganz:** Ereignis ist beschrieben, aber kein Beweismittel vorhanden.
 → Mandant befragen; nachbeschaffen; eidesstattliche Versicherung?

2. **Beleg unvollständig:** Screenshot ohne Datum; Kaufbeleg ohne Produktangabe.
 → Beleg ergänzen; Screenshot mit Timestamp wiederholen.

3. **Zeitachse unklar:** Mandant weiß nicht genau, wann Erstkenntnis war.
 → Erinnerungsprotokoll; E-Mail-Suche; Browserverlauf.

4. **Beweiskette unterbrochen:** Zwischen Verletzungshandlung und Schaden fehlen Verbindungsglieder.
 → Sachverständigengutachten? Zusätzliche Zeugen?

### Schritt 3 – Belegmatrix erstellen

```
BELEGMATRIX
Mandat: [Mandant ./. Gegenseite]

Spalten: Ereignis | Datum | Beleg | Beweismittelart | Beweiswert | Status
Zeilen: Je ein Ereignis

Legende Status:
G = Gesichert (Beleg vorhanden und geprüft)
P = Plausibel (Ereignis plausibel, Beleg fehlt noch)
L = Lücke (Ereignis unbekannt oder unbelegt)
```

| # | Ereignis | Datum | Beleg | Beweismittelart | Beweiswert | Status |
|---|---|---|---|---|---|---|
| 1 | Schutzrecht eingetragen | _______ | Registerauszug | Urkunde | Hoch | G |
| 2 | Verletzungshandlung | _______ | Screenshot + URL | Augenschein | Mittel | G |
| 3 | Erstkenntnis Mandant | _______ | EV-Antrag Datum | Eidesstattliche Vers. | Mittel | P |
| 4 | Abmahnung zugestellt | _______ | Einschreiben-Rückschein | Urkunde | Hoch | G |
| 5 | EV erlassen | _______ | Beschluss | Urkunde | Hoch | G |
| 6 | EV vollzogen | _______ | Zustellurkunde | Urkunde | Hoch | G |
| 7 | Verstoß gegen EV | _______ | Screenshot nach EV | Augenschein | Mittel | L |

## Besondere Chronologie-Fragen im IP-Recht

### Dringlichkeitszeitachse (EV)

- Wann wurde Verletzung erstmals bekannt (Erstkenntnis)?
- Wie lange zwischen Erstkenntnis und EV-Antrag?
- War Zeitverzögerung begründet (Beweissammlung, Abmahnfrist)?
- Kritische Schwelle: Je nach Gericht 4–8 Wochen.

### Prioritätszeitachse (Marke)

- Wann wurde Voranmeldung eingereicht (Prioritätsdatum)?
- Wann wurde Marke veröffentlicht?
- Wann war Widerspruchsfrist?
- Wann eingetragen?

### Verletzungszeitraum (Schadensersatz)

- Wann begann die Verletzung?
- Wann endete sie (oder endet sie noch)?
- Wie häufig und in welchem Umfang?
- Diese Daten bestimmen die Höhe des Schadensersatzes.

## Lücken-Schließ-Strategie

| Lückentyp | Methode |
|---|---|
| Erstkenntnis unklar | E-Mail-Postfach durchsuchen; Browserverlauf; Zeuge |
| Verletzungsnachweis fehlt | Testkauf; erneuter Screenshot; Wayback Machine |
| Datum der Verletzungshandlung | Domain-Registrierungsdaten; Wayback Machine; Archiv |
| Schaden nicht bezifferbar | Sachverständiger; Lizenzanalogie-Recherche |
| Schutzrecht-Gültigkeit | Live-Abfrage DPMA/EUIPO; Jahresgebühren-Check |

## Output-Format Chronologie

**Kurz-Chronologie für EV-Antrag:**
```
[Datum] – Marke X eingetragen beim DPMA (Anlage 1)
[Datum] – Erstkenntnis der Verletzung durch Y (eidesstattliche Versicherung, Anlage 2)
[Datum] – Screenshot der Verletzungshandlung auf website.de (Anlage 3)
[Datum] – Abmahnung Y versandt (Anlage 4)
[Datum] – Y hat nicht reagiert / hat Abmahnung abgelehnt
[Datum] – EV-Antrag beim LG [Stadt]
```

**Detail-Belegmatrix:** Vollständige Tabelle für interne Akte und Qualitätsprüfung.

## Quellenregel

- Keine externen Rechtsquellen für diesen Prozess-Skill erforderlich.
- Belege auf Aktualität prüfen: Registerauszüge < 3 Monate; Screenshots mit Datum.
- Eidesstattliche Versicherung: Inhalt mit Chronologie abgleichen; keine Widersprüche.

## Anschluss-Skills

- `spezial-rechtsschutz-tatbestand-beweis-und-belege` – Tatbestand und Belegaufbau
- `workflow-dokumentenintake` – Dokumentenerfassung
- `gewr-einstweilige-verfuegung-eilverfahren-spezial` – EV-Antrag
- `spezial-klausel-beweislast-und-darlegungslast` – Beweislastverteilung

## 3. `workflow-fristen-und-risikoampel`

**Fokus:** Fristenund Risikoampel für das Plugin gewerblicher-rechtsschutz: strukturierte Fristenerfassung, Risikobewertung Grün/Gelb/Rot und sofortige Handlungsempfehlung. Für alle IP-Verfahren vom Erstgespräch bis zur Vollstreckung.

# Workflow: Fristen und Risikoampel

## Zweck

Dieser Skill erstellt eine **vollständige Fristenübersicht mit Risikoampel** für ein laufendes IP-Mandat. Er ist kein vollständiges Fristenbuch (s. `spezial-fristen-abschlussprodukt-und-uebergabe`), sondern das operative Werkzeug für die laufende Fristenkontrolle und Risikobewertung im Mandatsalltag.

Mandatsbezug: Wöchentlicher Fristencheck in der Kanzlei; Übergabe eines Mandats an Urlaubsvertretung; schnelle Lageeinschätzung bei einem parallelen Mandat-Portfolio.

## Risikoampel-System

### Ampelfarben und Bedeutung

| Ampel | Kriterien | Handlungspflicht |
|---|---|---|
| 🔴 ROT – Sofort | Frist in < 5 Werktagen; kritischer Tatbestand ohne Beleg | Sofortige Mandatsbearbeitung; ggf. Notfallroutine |
| 🟡 GELB – Diese Woche | Frist in 5–14 Tagen; Belege unvollständig; offene Mandantenentscheidung | Frist vorbereiten; Mandant kontaktieren |
| 🟢 GRÜN – Komfortabel | Frist > 14 Tage; alle Belege vorhanden; Mandat vorbereitet | Planmäßige Bearbeitung |
| ⚫ OFFEN | Frist nicht ermittelbar; weitere Klärung nötig | Klärung bis Ende des Tages |

## Standard-Fristencheck: Zehn Kategorien

### Kategorie 1 – EV-Vollziehungsfrist

```
Frist: § 929 Abs. 2 ZPO
Auslöser: Zustellung EV an Antragsteller
Dauer: 1 Monat
Status: _____ Tage bis Ablauf
Ampel: [ROT / GELB / GRÜN / OFFEN]
Nächster Schritt: _______________
```

### Kategorie 2 – Abmahnreaktionsfrist (gesetzt durch Abmahner)

```
Frist: Gesetzt im Abmahnschreiben
Auslöser: Datum Zustellung Abmahnung
Gesetzt auf: _______________ (Datum)
Status: _____ Tage bis Ablauf
Ampel: [ROT / GELB / GRÜN / OFFEN]
Nächster Schritt: _______________
```

### Kategorie 3 – DPMA-Widerspruchsfrist

```
Frist: § 42 Abs. 1 MarkenG
Auslöser: Veröffentlichung im Markenblatt
Dauer: 3 Monate
Veröffentlichungsdatum: _______________
Fristende: _______________
Status: _____ Tage bis Ablauf
Ampel: [ROT / GELB / GRÜN / OFFEN]
```

### Kategorie 4 – EUIPO-Widerspruchsfrist

```
Frist: Art. 46 EUTMR
Dauer: 3 Monate ab Veröffentlichung
Veröffentlichungsdatum: _______________
Fristende: _______________
Ampel: [ROT / GELB / GRÜN / OFFEN]
```

### Kategorie 5 – Patent-Einspruchsfrist

```
Frist: § 59 PatG / Art. 99 EPÜ
Dauer: 3 Monate (DPMA) / 9 Monate (EPA)
Erteilungsveröffentlichung: _______________
Fristende: _______________
Ampel: [ROT / GELB / GRÜN / OFFEN]
```

### Kategorie 6 – Berufungs-/Rechtsmittelfrist

```
Frist: § 517 ZPO (Berufung) / § 548 ZPO (Revision)
Dauer: 1 Monat
Urteilszustellung: _______________
Fristende: _______________
Ampel: [ROT / GELB / GRÜN / OFFEN]
```

### Kategorie 7 – Patent-Jahresgebühr

```
Frist: § 17 PatG
Fälligkeitsdatum: _______________
Mahngebühren-Frist (Nachzahlung): _______________
Ampel: [ROT / GELB / GRÜN / OFFEN]
```

### Kategorie 8 – Marken-Verlängerungsfrist

```
Frist: § 47 MarkenG / Art. 53 EUTMR
Ablauf Schutzperiode: _______________
Nachzahlungsfrist (6 Monate): _______________
Ampel: [ROT / GELB / GRÜN / OFFEN]
```

### Kategorie 9 – Verjährungsfrist

```
Frist: § 11 UWG / § 20 MarkenG / § 102 UrhG
Kenntnis-Datum: _______________
Fristende (3 Jahre): _______________
Ampel: [ROT / GELB / GRÜN / OFFEN]
```

### Kategorie 10 – Dringlichkeitsfrist EV

```
Frist: Gerichtspraxis (4–8 Wochen nach Erstkenntnis)
Erstkenntnis-Datum: _______________
Kritische Schwelle: _______________
Status: Dringlichkeit noch gegeben? [Ja / Grenzwertig / Nein]
Ampel: [ROT / GELB / GRÜN / OFFEN]
```

## Fristenübersicht-Vorlage (Mandatsübergabe)

```
FRISTENÜBERSICHT – [Mandat]
Stand: [Datum]
Verantwortlich: [Anwalt]

| # | Fristart | Auslöser | Fristende | Restzeit | Ampel | Nächster Schritt |
|---|---|---|---|---|---|---|
| 1 | _______ | _______ | _______ | ___ Tage | 🔴/🟡/🟢 | _______ |
| 2 | _______ | _______ | _______ | ___ Tage | 🔴/🟡/🟢 | _______ |
| 3 | _______ | _______ | _______ | ___ Tage | 🔴/🟡/🟢 | _______ |

SOFORTMASSNAHMEN (ROT):
1. _______________
2. _______________

DIESE WOCHE (GELB):
1. _______________

OFFENE KLÄRUNGSPUNKTE:
1. _______________
```

## Notfallroutine bei roter Ampel

1. Anwalt sofort informieren.
2. Mandant sofort informieren.
3. Nächste Handlung identifizieren und delegieren.
4. Prüfen: Ist Fristverlängerung möglich? (z.B. § 929 Abs. 2 Satz 2 ZPO; EUIPO-Verlängerungsantrag)
5. Dokumentation: Alle Schritte in Akte festhalten.

## Quellenregel

- Fristen nur aus aktuellen Normen; gesetze-im-internet.de und dejure.org.
- [§ 929 ZPO – dejure.org](https://dejure.org/gesetze/ZPO/929.html)
- [§ 42 MarkenG – dejure.org](https://dejure.org/gesetze/MarkenG/42.html)
- Keine Pauschalangaben; Fristberechnungen immer im konkreten Fall prüfen.

## Anschluss-Skills

- `spezial-fristen-abschlussprodukt-und-uebergabe` – Vollständige Fristenmatrix
- `spezial-schutzrechts-fristennotiz-und-naechster-schritt` – Sofort-Fristennotiz
- `workflow-dokumentenintake` – Frist-Auslöser aus Dokumenten
- `evvollzug-neu-001` – EV-Vollziehungsfrist im Detail
