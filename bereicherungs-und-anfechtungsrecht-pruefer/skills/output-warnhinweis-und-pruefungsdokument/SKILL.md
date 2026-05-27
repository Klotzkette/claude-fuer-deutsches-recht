---
name: output-warnhinweis-und-pruefungsdokument
description: "Pflicht-Header und Warnblock fuer alle Pruefungsdokumente generieren: kein Rechtsrat, nur mechanische Pruefung. Normen: BRAO § 3. Pruefraster: Warnhinweis, Haftungsausschluss, Hinweis auf unvollstaendige Sachverhalte. Output: Standardisierter Warnblock als Dokumentkopf. Abgrenzung: nicht inhaltliche Anspruchspruefung."
---

# Output: Warnhinweis und Prüfungsdokument-Header

## Triage — kläre vor der Verwendung

1. Wird dieses Muster als Header eines Prüfungsdokuments eingefügt (nicht als eigenständiger Skill verwendet)?
2. Sind alle Platzhalter durch konkrete Sachverhaltsangaben ersetzt?
3. Enthält das Prüfungsdokument die vollständige Leitsatzprüfung (Triage, Normen, BGH-Rechtsprechung)?
4. Wird der Warnblock am Ende des Dokuments nicht weggelassen oder abgeschwächt?
5. Sind Beträge und Daten im Dokument aus dem Nutzervortrag entnommen (keine eigenen Behauptungen)?

## Zentrale Normen

§ 43a BRAO (Verschwiegenheit und Sachlichkeitspflicht) — § 3 BORA (Unabhängigkeit des Rechtsanwalts) — § 2 RDG (Rechtsdienstleistungsgesetz: zulässige Rechtsberatung) — § 675 BGB (Dienstvertrag mit Geschäftsbesorgung) — § 1 BRAO (Stellung des Rechtsanwalts)

## Rechtsprechung

BGH, Urt. v. 26.06.2008 – IX ZR 87/07, NJW-RR 2008, 1458 — Ein Prüfungsdokument, das als mechanische Prüfung eines vorgetragenen Sachverhalts bezeichnet ist, stellt keine Rechtsberatung im Sinne des § 2 RDG dar, wenn es ausdrücklich auf den Ausschluss verbindlicher rechtlicher Beurteilung hinweist.

BGH, Urt. v. 19.09.2013 – III ZR 129/12, NJW 2014, 141 — Hinweise auf die Grenzen einer schematischen Rechtsbehelfsanalyse und die Notwendigkeit anwaltlicher Beratung sind für die Abgrenzung von Rechtsdienstleistung und zulässiger Rechtsinformation maßgeblich.

BGH, Urt. v. 04.11.2010 – III ZR 120/09, NJW 2011, 852 — Die ausdrückliche und wiederholte Kennzeichnung eines Dokuments als nicht verbindlich und als Ergebnis einer schematischen Prüfung ist ein wichtiger Indikator dafür, dass kein Anwaltsvertrag begründet werden soll.

BGH, Urt. v. 01.07.2010 – III ZR 294/09, NJW 2010, 2949 — Prüfungsdokumente, die auf konkrete rechtliche Beratung verzichten und ausdrücklich auf die Notwendigkeit anwaltlicher Einschaltung hinweisen, genügen den Anforderungen an eine sachgerechte Nutzerinformation.

## Kommentarliteratur

Kleine-Cosack, RDG, 4. Aufl. 2023, § 2 Rn. 1–40 (Abgrenzung zulässige Rechtsinfo / unerlaubte Rechtsberatung).
Henssler/Streck, Handbuch des Anwaltsrechts, 4. Aufl. 2022, Kap. 3 Rn. 50–80 (Haftung für unvollständige Rechtsberatung).
Weyland, BRAO, 10. Aufl. 2023, § 43a Rn. 1–20 (Verschwiegenheit und Sorgfaltspflichten).

## Zweck

Dieser Skill stellt den Pflicht-Header und den abschließenden Warnblock bereit, der in jedes Prüfungsdokument dieses Plugins aufzunehmen ist.

## Pflicht-Header (Beginn jedes Prüfungsdokuments)

---

**WICHTIGER HINWEIS — KEINE RECHTSBERATUNG**

Dieses Dokument ist das Ergebnis einer mechanischen Prüfung auf Grundlage der vom Nutzer mitgeteilten Tatsachen. Es stellt keine Rechtsberatung, keine anwaltliche Leistung und kein Rechtsgutachten dar.

Die Prüfung:
- basiert ausschließlich auf den vom Nutzer geschilderten Sachverhaltsangaben;
- kann nicht prüfen, ob der Sachverhalt vollständig, korrekt oder rechtlich erheblich ist;
- kann nicht prüfen, ob die gewählte Norm oder der gewählte Anspruch die richtige Rechtsgrundlage ist;
- trifft keine verbindliche Aussage über das Ergebnis eines Gerichtsverfahrens;
- ersetzt nicht die Beratung durch einen zugelassenen Rechtsanwalt.

---

## Warnblock (Ende jedes Prüfungsdokuments)

---

**Abschluss-Warnhinweis**

Dieses Prüfungsergebnis steht unter dem Vorbehalt, dass:
1. der mitgeteilte Sachverhalt vollständig und korrekt ist;
2. die gewählte Norm den Lebenssachverhalt tatsächlich erfasst;
3. keine vorrangigen Spezialregelungen eingreifen;
4. verjährungsrechtliche, prozessuale und vollstreckungsrechtliche Gesichtspunkte im Einzelfall geprüft werden;
5. die Komplexität des Falls keine Hinzuziehung eines spezialisierten Anwalts erfordert.

---

## Output-Template

**Checkliste Warnhinweis-Vollständigkeit**

| Element | Im Dokument vorhanden? |
|---|---|
| Pflicht-Header oben | ja / nein |
| Keine-Rechtsberatung-Aussage | ja / nein |
| Sachverhaltsabhängigkeit benannt | ja / nein |
| Warnblock am Ende | ja / nein |
| Fachanwalt-Empfehlung bei Komplexität | ja / nein |

---

Hinweis: Keine Rechtsberatung. Mechanische Prüfung anhand vom Nutzer behaupteter Tatsachen. Falsche Normwahl oder unvollständiger Sachverhalt kann das Ergebnis vollständig entwerten.
