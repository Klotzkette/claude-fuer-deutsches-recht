---
name: einstieg-routing
description: "Startet Geldwäscheprüfungen in Kanzlei, Notariat und Unternehmen aus vorhandenen Unterlagen. Wählt zwischen Verpflichtetenstatus, Kundenprüfung, Immobilienzahlung und akutem Meldefall, ohne einen allgemeinen Fragebogen vorzuschalten."
---

# 1. Geldwäschevorgang aufnehmen

## 1. Zweck und Anwendungsfall

Für einen neuen Ordner, Zahlungsalarm oder eine knappe Frage zur Prävention. Ein ausdrücklich verlangter Meldeentwurf beginnt unmittelbar im Meldeskill; dieser Einstieg ist keine Pflichtschleife.

## 2. Eingaben

Lies den Auftrag, die Zahlungsnachrichten und die für den Vorgang erforderlichen Mandats- oder Kundendaten einschließlich der belegten Eigentumskette. Übernimm bereits geklärte Angaben aus der Akte. Ist das gewünschte Ergebnis nicht erkennbar, frage nach Rolle, Geschäft und anstehender Handlung; beginne keine Meldung oder Auszahlung auf Grundlage eines vermuteten Auftrags.

## 3. Ablauf

### 3.1. Handlungsdruck erkennen

Eine heute anstehende Auszahlung, Grundbucheinreichung oder Meldung vor Organisationsarbeit behandeln. Zeitpunkt und Bearbeiter aus der Akte übernehmen. Fehlender Registerzugang bedeutet eine Nachforderung, nicht automatisch einen Verdacht.

### 3.2. Einen Fachweg wählen

| Eingang | Nächster Skill | Erstes Ergebnis |
| --- | --- | --- |
| Unklarer Verpflichteter | [Verpflichtetencheck](../geldwaesche-verpflichteten-check/SKILL.md) | Begrenzter Pflichtenumfang |
| Beratungswissen oder Fremdgeld | [Kanzleimandat](../kanzleimandat-und-berufsgeheimnis/SKILL.md) | Informations- und Rollenabgrenzung |
| Kaufpreis oder Umschreibung | [Notarielle Zahlung](../notariat-immobilienzahlung-pruefen/SKILL.md) | Nachweis und Vollzugsstand |
| Neue Geschäftsbeziehung | [KYC](../geldwaesche-kyc-onboarding/SKILL.md) | Entscheidende Nachforderung |
| Verdachtstatsachen | [FIU-Meldeprüfung](../aml-verdachtsmeldung-fiu-leitfaden/SKILL.md) | Tatsachenkern und Meldeentscheidung |
| Bereits abgegangene Meldung | [Nichtdurchführung](../geldwaesche-transaktionsstopp-freeze/SKILL.md) | Frist und andere Hindernisse |
| Vorbereitung auf 2027 | [EU-Umstellung](../eu-geldwaescherecht-umstellung-2027/SKILL.md) | Datierter Änderungsplan |

Beginne mit dem passenden Fachskill und seiner benötigten Referenz. Weitere Fachfragen desselben Vorgangs dort anschließen, ohne die Aufnahme zu wiederholen. Fehlt eine Zwischenstufe der Eigentumskette, frage gezielt nach Beteiligung, Kontrolle und dem zugehörigen Nachweis. Widersprechen sich Zahlungsbestätigung und Kontobeleg, kläre Betrag, Absender, Empfänger und Buchungsdatum. Trenne fehlende Unterlagen von tatsächlichen Widersprüchen und bewerte neue Antworten zusammen mit den bisherigen Belegen; ein nun zugängliches Dokument macht die Prüfung nicht automatisch vollständig.

### 3.3. Zum verlangten Ergebnis weiterarbeiten

Aktualisiere nach jeder entscheidenden Antwort die betroffene Kundenprüfung, Zahlungsbewertung oder Meldebegründung. Zeigt sie eine weitere erhebliche Lücke, frage dazu nach, ohne bereits Beantwortetes erneut abzufragen. Liefere währenddessen die belastbaren Teile als vorläufigen Stand und benenne, was vor der Endfassung noch geklärt werden muss. Formuliere anschließend das bestellte Prüfergebnis, Nachforderungsschreiben oder den Meldeentwurf vollständig aus; eine Analyse allein erledigt keinen Schreibauftrag. Auch ein Nachforderungsschreiben darf unbekannte Beteiligungen oder Zahlungsumstände nicht als Tatsachen darstellen. Meldung, Auszahlung oder Einreichung nicht eigenmächtig veranlassen.

## 4. Quellenpflicht

[Rechtsstand und Grenzen](../../references/rechtsstand-2026-und-eu-uebergang.md): GwG Paragraf 2, Paragraf 43 und Paragraf 46 sind unterschiedliche Weichen. Den Stichtag 10. Juli 2027 nicht vorziehen.

## 5. Ausgabeformat

Verlangtes Arbeitsprodukt in vollständigen Sätzen; ohne Formatwunsch kurzer Vermerk mit Sachverhalt, Bewertung, Empfehlung und offenen Fragen. Times New Roman 11 pt, dezimale Gliederung. Kein vorgelagertes Inhaltsverzeichnis aller Skills. Abrufstatus und technische Prüfhinweise stehen in einer gesonderten Arbeitsnotiz, nicht im Empfängerschreiben.

## 6. Beispiele

„Verkäufer bestätigt Eingang, heute einreichen?“ führt zur notariellen Zahlungsprüfung. Ein Rückzahlungswunsch auf ein fremdes Konto führt zum Zahlungsbefund und gegebenenfalls zur Meldeprüfung, nicht zur Schulungsplanung.

## 7. Technische Grenzen

Bei ausgefallenem Registerzugang einen vorhandenen Auszug mit seinem Datum auswerten und die fehlende aktuelle Abfrage kenntlich machen; erfolglose Abrufe nicht unverändert wiederholen. Ohne Export den ausformulierten Text liefern. Keine simulierte Freigabe oder erfundene goAML-Bestätigung.
