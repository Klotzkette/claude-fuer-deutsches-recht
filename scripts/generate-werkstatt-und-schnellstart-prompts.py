#!/usr/bin/env python3
"""Erzeugt autarke Werkstatt- und Schnellstart-Prompts pro Plugin.

Ausgabe je Plugin:
- {plugin}/{slug}-werkstatt.md
- {plugin}/{slug}-schnellstart.md

Die Dateien sind reine Markdown-Arbeitsmittel fuer Nutzer ohne installierte
Plugin-Umgebung. Sie enthalten keine Skill-Verweise und keine ZIP-Verweise.
"""

from __future__ import annotations

import json
import re
from functools import lru_cache
from pathlib import Path
from typing import Iterable

from themen_profile import profile_for, ThemenProfil


REPO = Path(__file__).resolve().parent.parent
MAX_FAST = 7400
MAX_WERKSTATT = 48 * 1024
WERKSTATT_TEMPO_BLOCK = [
    "### 1.1. Arbeitsmodus: schnell und belastbar",
    "",
    "Beginne mit einem Sofortbild in höchstens fünf Sätzen: Ziel, vorhandene Unterlagen, Frist, stärkster Anker, nächster Output. Wenn der Nutzer einen Ordner, Dateien oder nur diesen Prompt öffnet, ist das der Arbeitsauftrag: zuerst die vorhandenen Dokumente lesen, Belegstellen bilden und einen verwertbaren Erststand liefern. Frage nur nach, wenn Frist, Zuständigkeit, Beweis oder Rechtsfolge sonst kippt.",
    "",
    "Arbeite danach in drei Ebenen: Aktenkern, Gegenargument, Arbeitsprodukt. Keine Vorrede und keine Abfragekaskade; eine Materialübersicht gibt es nur als Beleglinie mit Datum, Dokument, Kerntatsache und Lücke. Jeder Abschnitt endet mit Satz, Tabelle, Antrag, Klausel oder Nachforderung.",
    "",
]
EILSACHE_LABEL = {
    "arbeits": "Kündigung, Befristungsende oder Massenentlassung",
    "hr": "Personalmaßnahme mit laufender Anhörungsfrist",
    "zeugnis": "Zeugnisberichtigung vor Bewerbungsschluss",
    "miet": "Räumung, Kündigung oder Mieterhöhungsfrist",
    "famil": "Gewaltschutz, Umgang oder einstweilige Anordnung",
    "straf": "Haft, Durchsuchung oder Beschlagnahme",
    "insolvenz": "Antragspflicht, Anfechtungsfrist oder Massesicherung",
    "verwaltung": "Widerspruchsfrist, sofortige Vollziehung oder Eilantrag",
    "sozial": "Bescheidzugang, Widerspruchs- oder Eilantragsfrist",
    "zivilprozess": "Klagefrist, Einspruch oder Berufungsbegründung",
    "gesellschaft": "Beschlussanfechtung, Ladung oder Handelsregisterfrist",
    "ma_finanzierung": "Angebotsfrist, Exklusivität, Signing, Freigabe oder Closing",
    "steuer": "Einspruchsfrist, Vollziehungsaussetzung oder Prüfungsanordnung",
    "bau": "Abnahme, Behinderungsanzeige oder Mängelrüge",
    "vergabe": "Rüge, Angebotsfrist oder Nachprüfungsantrag",
    "datenschutz": "Meldefrist nach Datenpanne oder Auskunftsfrist",
    "medizin": "Behandlungsfehler mit drohender Verjährung",
    "ip": "Abmahnfrist, Verfügungsverfahren oder Prioritätsfrist",
    "bgb": "Verjährung, Rücktritts- oder Anfechtungsfrist",
    "erbrecht": "Ausschlagung, Pflichtteil oder Erbscheinsfrist",
}


SOURCE_WORK_PROFILE_KEYS = {"pralr", "rechtsgeschichte", "roemisch"}
RESEARCH_WORK_PROFILE_KEYS = {
    "ausbildung",
    "foerderantrag",
    "forschungszulage",
    "methodik",
}
PRODUCTION_WORK_PROFILE_KEYS = {
    "behoerdenklartext",
    "dokumentenworkflow",
    "kanzleibetrieb",
    "presse",
    "reporting",
}
DRAFTING_WORK_PROFILE_KEYS = {
    "aktg_hv",
    "bav",
    "gesellschaft",
    "lizenz",
    "ma_finanzierung",
    "vertragsgestaltung",
}
DECISION_WORK_PROFILE_KEYS = {
    "ehrenamtliche_richter",
    "eu_prozess",
    "finanzgericht",
    "justiz_zivil",
    "strafjustiz",
    "verwaltungsgericht",
    "zivilprozess",
}


def workflow_family(profile: ThemenProfil) -> str:
    """Ordnet das Profil einer Arbeitswelt zu, ohne die Fachroute zu glätten."""

    if profile.key in SOURCE_WORK_PROFILE_KEYS:
        return "source"
    if profile.key in RESEARCH_WORK_PROFILE_KEYS:
        return "research"
    if profile.key in PRODUCTION_WORK_PROFILE_KEYS:
        return "production"
    if profile.key in DRAFTING_WORK_PROFILE_KEYS:
        return "drafting"
    if profile.key in DECISION_WORK_PROFILE_KEYS:
        return "decision"
    return "case"


def werkstatt_tempo_block(profile: ThemenProfil) -> list[str]:
    """Gibt dem gemeinsamen Tempogerüst die Sprache der konkreten Arbeitswelt."""

    family = workflow_family(profile)
    if family == "source":
        first = (
            "Beginne mit einem Quellen-Sofortbild in höchstens fünf Sätzen: Erkenntnisziel, "
            "vorliegende Textzeugen, maßgebliche Fassung, stärkster Quellenbeleg und nächste "
            "Darstellungsform. Lies vorhandene Editionen, Übersetzungen und Sekundärquellen "
            "zuerst; frage nur nach, wenn Datierung, Textstufe, Rechtsraum oder Übersetzung "
            "sonst offenbleiben."
        )
        second = (
            "Arbeite danach in drei Ebenen: Quellenbefund, konkurrierende Lesart und historische "
            "Einordnung. Keine moderne Rückprojektion und keine Abfragekaskade; jede Aussage "
            "nennt Textstelle, Fassung und Verlässlichkeitsgrad und endet mit Quellenkarte, "
            "Synopse, Epochenmemo oder Rezeptionsbefund."
        )
    elif family == "research":
        first = (
            "Beginne mit einem Arbeitsbild in höchstens fünf Sätzen: konkrete Frage, vorhandenes "
            "Material, Bewertungsmaßstab, stärkster Beleg und nächstes Teilprodukt. Werte Dateien "
            "und Quellen zuerst aus; frage nur nach, wenn Aufgabenstellung, Stichtag, Maßstab oder "
            "gewünschte Darstellungsform sonst unklar bleiben."
        )
        second = (
            "Arbeite danach in drei Ebenen: Befund, Gegenhypothese und ausformuliertes Produkt. "
            "Keine Vorrede und keine Stoffinventur; jede Station endet mit Prüfungssatz, "
            "Quellenbeleg, Rechenschritt, Textbaustein oder klar begrenzter Nachforderung."
        )
    elif family == "production":
        first = (
            "Beginne mit einem Produktionsbild in höchstens fünf Sätzen: Empfänger, vorhandene "
            "Dateien, maßgebliche Fassung, Freigabeengpass und nächstes fertiges Dokument. Lies "
            "den Ordner zuerst; frage nur nach, wenn Version, Anlagenbestand, Signatur, Termin oder "
            "Ausgabeformat sonst nicht sicher feststehen."
        )
        second = (
            "Arbeite danach in drei Ebenen: Eingangsmaterial, Qualitätskontrolle und "
            "Ausgabepaket. Keine Vorrede und keine Inventarliste ohne Folgerung; jede Station "
            "endet mit korrigierter Datei, Register, Freigabefassung, Versandpaket oder präziser "
            "Fehlteilliste."
        )
    elif family == "drafting":
        first = (
            "Beginne mit einem Transaktions- oder Entwurfsbild in höchstens fünf Sätzen: "
            "Geschäftsziel, Parteien und Rollen, maßgeblicher Dokumentstand, kritischster "
            "Vollzugspunkt und nächster Entwurf. Lies Datenraum und Fassungen zuerst; frage nur "
            "nach, wenn Risikozuweisung, Kompetenz, Termin oder wirtschaftlicher Parameter kippt."
        )
        second = (
            "Arbeite danach in drei Ebenen: Deal- oder Regelungskern, Gegenposition und "
            "vollzugsfähiger Text. Keine Vorrede und keine abstrakte Checkliste; jede Station "
            "endet mit Klausel, Redline, Beschluss, Berechnung, Closing-Schritt oder konkreter "
            "Entscheidungsvorlage."
        )
    elif family == "decision":
        first = (
            "Beginne mit einem Entscheidungsbild in höchstens fünf Sätzen: Streitgegenstand, "
            "Verfahrensstand, Frist, entscheidungstragender Aktenfund und nächste richterliche "
            "oder prozessuale Handlung. Lies die Akte zuerst; frage nur nach, wenn Antrag, "
            "Zuständigkeit, Entscheidungsreife oder Beweiserhebung sonst nicht bestimmbar sind."
        )
        second = (
            "Arbeite danach in drei Ebenen: Parteivortrag und Verfahrenslage, Beweis- und "
            "Rechtsprüfung, förmliches Entscheidungsprodukt. Keine Vorrede und keine "
            "Akteninventur; jede Station endet mit Verfügung, Hinweis, Beweisbeschluss, Tenor, "
            "Urteilsbaustein oder klarer Aufklärungsmaßnahme."
        )
    else:
        return list(WERKSTATT_TEMPO_BLOCK)
    return [
        "### 1.1. Arbeitsmodus: schnell und belastbar",
        "",
        first,
        "",
        second,
        "",
    ]


DOMAIN_DOCUMENTS = {
    "arbeits": "Arbeitsvertrag, Abmahnung, Anhörungsprotokoll, Kündigungsschreiben und Zugangsnachweis",
    "hr": "Personalakte, Zielvereinbarung, Anhörung und Betriebsvereinbarung",
    "zeugnis": "Zeugnisentwurf, Beurteilungsbogen und Tätigkeitsbeschreibung",
    "miet": "Mietvertrag, Betriebskostenabrechnung, Mängelanzeige und Kündigungsschreiben",
    "famil": "Einkommensbelege, Jugendamtsvermerk, Umgangsprotokoll und Vermögensverzeichnis",
    "straf": "Ermittlungsakte, Vernehmungsprotokoll, Durchsuchungsbeschluss und Auswertebericht",
    "insolvenz": "Gutachten, Kontoauszüge, Buchhaltung, Forderungsanmeldung und Zahlungsverzeichnis",
    "verwaltung": "Bescheid, Zustellungsnachweis, Behördenakte und Anhörungsvermerk",
    "sozial": "Bescheid, Widerspruchsbescheid, ärztliche Befunde und Versicherungsverlauf",
    "zivilprozess": "Klageschrift, Anlagenkonvolut, Protokoll und Zustellungsurkunde",
    "gesellschaft": "Gesellschaftsvertrag, Gesellschafterliste, Beschlussprotokoll und Handelsregisterauszug",
    "ma_finanzierung": "Process Letter, Datenraumindex, Q&A, Due-Diligence-Berichte, Term Sheet, SPA oder Beteiligungsvertrag, Disclosure Letter, Gremienbeschlüsse und Closing Checklist",
    "steuer": "Steuerbescheid, Prüfungsbericht, Buchführung und Einspruchsschreiben",
    "bau": "Bauvertrag, Leistungsverzeichnis, Bautagebuch, Abnahmeprotokoll und Nachtragsangebot",
    "vergabe": "Vergabeunterlagen, Angebot, Vergabevermerk und Rügeschreiben",
    "datenschutz": "Verarbeitungsverzeichnis, Auftragsverarbeitungsvertrag, Löschkonzept und Meldeformular",
    "medizin": "Behandlungsdokumentation, Aufklärungsbogen, Befunde und Sachverständigengutachten",
    "ip": "Schutzrechtsregister, Lizenzvertrag, Abmahnung und Benutzungsnachweis",
    "bgb": "Vertragsurkunde, Korrespondenz, Rechnungen und Übergabeprotokoll",
    "erbrecht": "Testament, Erbvertrag, Nachlassverzeichnis, Grundbuchauszug und Kontoauswertung",
}

DOMAIN_ATTACK = {
    "arbeits": "Fristversäumnis, fehlerhafter Anhörung oder unzureichender Sozialauswahl",
    "hr": "unwirksamer Beteiligung des Betriebsrats oder fehlender Dokumentation",
    "zeugnis": "der Tatsachengrundlage der Bewertung und der Üblichkeit der Formulierung",
    "miet": "Formfehlern der Kündigung, Abrechnungsfristen und fehlender Mangelanzeige",
    "famil": "der Einkommensermittlung, der Bedarfsberechnung und dem Kindeswohlmaßstab",
    "straf": "Beweisverwertungsverboten, Aussagekonstanz und alternativen Geschehensabläufen",
    "insolvenz": "dem Zeitpunkt der Insolvenzreife, der Kenntnis und der Bargeschäftsausnahme",
    "verwaltung": "Zuständigkeit, Anhörung, Ermessensausübung und Verhältnismäßigkeit",
    "sozial": "der medizinischen Bewertung, dem Zugangszeitpunkt und der Mitwirkungsobliegenheit",
    "zivilprozess": "Substantiierung, Beweisantritt und Präklusion",
    "gesellschaft": "Ladungs- und Beschlussmängeln sowie der Vertretungsmacht",
    "ma_finanzierung": "Datenraumlücken, unklarer Risikozuweisung, Kaufpreismechanik, Wissensqualifikation, Haftungsgrenzen und unerfüllten Vollzugsbedingungen",
    "steuer": "Schätzungsbefugnis, Mitwirkungspflicht und Festsetzungsverjährung",
    "bau": "Abnahmewirkung, Mängelrüge und Bauzeitverzug",
    "vergabe": "Rügepräklusion, Wertungsfehlern und Transparenzverstößen",
    "datenschutz": "Rechtsgrundlage, Erforderlichkeit und Meldefristen",
    "medizin": "Kausalität, Aufklärungsumfang und Befunderhebungspflicht",
    "ip": "Schutzfähigkeit, Verwechslungsgefahr und rechtserhaltender Benutzung",
    "bgb": "Zugang, Verjährung und der Auslegung der Vereinbarung",
    "erbrecht": "der Auslegung der Verfügung, der Bindungswirkung und der Bewertung",
}

DOMAIN_DEADLINE_QUESTION = {
    "arbeits": "die Dreiwochenfrist ab Zugang der Kündigung benannt?",
    "miet": "die Widerspruchs- oder Abrechnungsfrist benannt?",
    "straf": "die Frist für Einspruch, Revision oder Haftprüfung benannt?",
    "insolvenz": "die Antrags-, Anfechtungs- oder Anmeldefrist benannt?",
    "verwaltung": "die Monatsfrist ab Bekanntgabe des Bescheids benannt?",
    "sozial": "die Widerspruchs- oder Klagefrist ab Bescheidzugang benannt?",
    "zivilprozess": "die Einlassungs-, Berufungs- oder Begründungsfrist benannt?",
    "steuer": "die Einspruchsfrist und die Festsetzungsverjährung benannt?",
    "vergabe": "die Rüge- und Nachprüfungsfrist benannt?",
    "datenschutz": "die Zweiundsiebzig-Stunden-Meldefrist benannt?",
    "ip": "die Widerspruchs-, Prioritäts- oder Dringlichkeitsfrist benannt?",
    "erbrecht": "die Ausschlagungs-, Pflichtteils- oder Verjährungsfrist benannt?",
    "famil": "die Frist für Beschwerde oder einstweilige Anordnung benannt?",
    "ma_finanzierung": "Angebots-, Exklusivitäts-, Signing-, Freigabe- und Closing-Termine mit Verantwortlichem und Abhängigkeit benannt?",
}


def domain_documents(profile: ThemenProfil) -> str:
    """Nennt die Dokumenttypen, die in diesem Gebiet tatsaechlich anfallen."""
    if profile.key in DOMAIN_DOCUMENTS:
        return DOMAIN_DOCUMENTS[profile.key]
    family = workflow_family(profile)
    if family == "source":
        return "die vorgelegten Quellen, Editionen, Übersetzungen und Fundstellen"
    if family == "research":
        return "die vorgelegte Aufgabenbeschreibung, Datengrundlage, Quellen und Berechnungen"
    if family == "production":
        return "die Eingangsdateien, maßgeblichen Fassungen, Anlagen und Übergabevorgaben"
    if family == "drafting":
        return "die Entwürfe, Verhandlungsstände, Beschlüsse, Anlagen und Vollzugsunterlagen"
    if family == "decision":
        return "die Anträge, Schriftsätze, Verfügungen, Beweismittel und Zustellnachweise"
    return "die vorgelegten Urkunden, Bescheide und Korrespondenz"


def role_scope_text(profile: ThemenProfil) -> str:
    """Beschreibt die Kernarbeit ohne fachfremde Universalverben."""

    documents = domain_documents(profile)
    family = workflow_family(profile)
    if family == "source":
        work = (
            "trennt Textzeuge, Fassung, Übersetzung und Datierung, prüft Begriffssinn, "
            "institutionellen Zusammenhang und Gegenlesart und hält historischen Befund, "
            "spätere Rezeption und heutige Anschlussfrage auseinander"
        )
    elif family == "research":
        work = (
            "trennt Aufgabenfrage, Maßstab, Datengrundlage und Annahme, prüft Methode, "
            "Gegenhypothese und Belastbarkeit und führt jeden tragenden Befund auf eine "
            "nachvollziehbare Quelle oder Rechnung zurück"
        )
    elif family == "production":
        work = (
            "trennt Original, Arbeits- und Freigabefassung, prüft Vollständigkeit, Lesbarkeit, "
            "Benennung, Signaturbedarf und Ausgabeweg und macht jede Änderung bis zur "
            "Eingangsdatei rückverfolgbar"
        )
    elif family == "drafting":
        work = (
            "trennt Geschäftsziel, Rechtswirkung, Verhandlungsposition und Rückfalllösung, "
            "prüft Kompetenz, Parameter, Risikozuweisung und Vollzugsbedingungen und macht aus "
            "offenen Punkten entscheidungs- oder verhandlungsfähige Fassungen"
        )
    elif family == "decision":
        work = (
            "trennt Antrag, Parteivortrag, Aktenfund und Rechtsmaßstab, prüft Zuständigkeit, "
            "Gehör, Beweislast, Entscheidungsreife und Nebenentscheidungen und überführt den "
            "Befund in den nächsten förmlichen Verfahrensschritt"
        )
    else:
        work = (
            "trennt gesicherte Tatsachen, Behauptungen und offene Punkte, prüft Norm, "
            "Tatbestandsmerkmale, Frist, Form, Beweislast und stärkste Gegenposition und leitet "
            "daraus die konkrete Rechtsfolge und den nächsten Verfahrensschritt ab"
        )
    return (
        f"Die Rolle ist keine bloße Zusammenfassung. Sie ordnet im Bereich {profile.label} "
        f"insbesondere {documents}, {work}. Jede Station endet mit einem unmittelbar "
        "verwendbaren, auf Fundstellen gestützten Produkt."
    )


def domain_attack(profile: ThemenProfil) -> str:
    """Benennt den typischen Angriffspunkt der Gegenseite im Gebiet."""
    if profile.key in DOMAIN_ATTACK:
        return DOMAIN_ATTACK[profile.key]
    if len(profile.pruefraster) > 1:
        attack = clean(profile.pruefraster[1], 140).rstrip(".")
        # Nur das erste Wort wird zum Satzfragment; Substantive und
        # Eigennamen im Profil dürfen ihre Großschreibung nicht verlieren.
        attack = attack[:1].lower() + attack[1:] if attack else attack
        return re.sub(r"^(?:ist|sind|wird|werden|wurde|wurden)\s+", "", attack)
    return "Norm, Tatbestand, Beleg, Kausalität, Höhe oder Verfahrensweg"


def domain_deadline_question(profile: ThemenProfil) -> str:
    """Formuliert die Fristfrage des Gebiets statt einer Universalfrage."""
    if profile.key in DOMAIN_DEADLINE_QUESTION:
        return DOMAIN_DEADLINE_QUESTION[profile.key]
    family = workflow_family(profile)
    if family == "source":
        return "Textzeuge, Fassung, Datierung, Rechtsraum und Übersetzungsstatus benannt?"
    if family == "research":
        return "Aufgabenstellung, Bewertungsmaßstab, Quellenstand und Abgabetermin benannt?"
    if family == "production":
        return "Empfänger, maßgebliche Fassung, Freigabe, Ausgabeformat und Übergabetermin benannt?"
    if family == "drafting":
        return "Vertragsstand, Entscheidungskompetenz, Verhandlungstermin und Vollzugszeitpunkt benannt?"
    if family == "decision":
        return "Antrag, Verfahrensstand, Entscheidungsreife und maßgebliche Frist benannt?"
    return "die maßgebliche Frist mit Beginn, Lauf und Ende benannt?"


def work_vocabulary(profile: ThemenProfil) -> dict[str, str]:
    """Liefert fachgerechte Bezeichnungen für die wiederkehrenden Werkstattgriffe."""

    family = workflow_family(profile)
    if family == "source":
        return {
            "priority_label": "Quellenkritischer Engpass",
            "priority_output": "Quellenblatt mit Textzeuge, Fassung, Datierung und Unsicherheitsgrad",
            "proof_label": "Quellennachweis",
            "proof_output": "Textzeugen- und Übersetzungsmatrix",
            "result_label": "Historische Einordnung",
            "result_output": "Quellenkarte, Synopse oder Rezeptionsbefund",
            "audience_label": "Fachliche Darstellung",
            "audience_output": "lesbarer Quellenbefund mit Gegenlesart",
            "audience_check": "Zeitstufe, Belegwert und heutige Anschlussfrage sichtbar trennen",
        }
    if family == "research":
        return {
            "priority_label": "Methodischer Engpass",
            "priority_output": "Prüfblatt mit Frage, Maßstab, Quellenlücke und nächstem Teilprodukt",
            "proof_label": "Evidenzarbeit",
            "proof_output": "Quellen-, Argument- oder Rechenmatrix",
            "result_label": "Arbeitsergebnis",
            "result_output": "Gutachten, Lösung, Antragsteil oder Bewertungsvermerk",
            "audience_label": "Adressatenfassung",
            "audience_output": "verständliche Darstellung mit tragender Begründung",
            "audience_check": "Befund, Gegenansicht, Unsicherheit und Empfehlung getrennt ausweisen",
        }
    if family == "production":
        return {
            "priority_label": "Freigabe- oder Versandengpass",
            "priority_output": "Produktionscheck mit Termin, Verantwortlichem und Sofortkorrektur",
            "proof_label": "Datei- und Fundstellenkontrolle",
            "proof_output": "Versions-, Anlagen- und Nachweismatrix",
            "result_label": "Ausgabeseite",
            "result_output": "Freigabefassung, Exportpaket oder Versandprotokoll",
            "audience_label": "Empfängerfassung",
            "audience_output": "vollständiges, lesbares und technisch geprüftes Dokument",
            "audience_check": "Dateiname, Anlagen, Signatur, Lesbarkeit und Übergabenachweis kontrollieren",
        }
    if family == "drafting":
        return {
            "priority_label": "Zeitkritischer Entwurfs- oder Vollzugspunkt",
            "priority_output": "Termin- und Entscheidungsmatrix mit sofortigem Entwurfsgriff",
            "proof_label": "Deal- und Nachweisarbeit",
            "proof_output": "Klausel-, Risiko- und Vollzugsmatrix",
            "result_label": "Regelungsseite",
            "result_output": "Klausel, Redline, Beschluss oder Closing-Fassung",
            "audience_label": "Entscheidungsvorlage",
            "audience_output": "verhandlungsfähige Empfehlung mit Fassungsvarianten",
            "audience_check": "Wirtschaftsziel, Rechtswirkung, Risiko und Vollzug zusammenführen",
        }
    if family == "decision":
        return {
            "priority_label": "Frist- oder Entscheidungsengpass",
            "priority_output": "Verfahrensblatt mit Sofortverfügung oder Sicherungsmaßnahme",
            "proof_label": "Beweis- und Aktenarbeit",
            "proof_output": "Vortrags-, Beweis- und Entscheidungsreifematrix",
            "result_label": "Entscheidungsseite",
            "result_output": "Verfügung, Hinweis, Beweisbeschluss, Tenor oder Urteil",
            "audience_label": "Förmliche Fassung",
            "audience_output": "entscheidungsreifer Text mit vollständigem Verfahrensanschluss",
            "audience_check": "Antrag, Gehör, Beweiswürdigung, Kosten und Rechtsbehelf zusammenführen",
        }
    return {
        "priority_label": "Frist- oder Eilfall",
        "priority_output": "Fristenblatt mit Sofortmaßnahme und nächstem Handlungstag",
        "proof_label": "Beweisführung",
        "proof_output": "Beweismittelspiegel je Tatbestandsmerkmal",
        "result_label": "Rechtsfolgenseite",
        "result_output": "Antrags-, Bescheid-, Vertrags- oder Antwortfassung",
        "audience_label": "Adressatenantwort",
        "audience_output": "verständlicher Ergebnisbrief mit Optionen",
        "audience_check": "Empfehlung, Risiko, Kostenfolge und nächsten Schritt getrennt ausweisen",
    }


def stop_guard_lines(profile: ThemenProfil) -> list[str]:
    """Verhindert fachfremde Universal-Stopps in konzeptionellen Werkstätten."""

    family = workflow_family(profile)
    if family == "source":
        return [
            "Wenn Textzeuge, Fassung, Datierung, Übersetzung oder Rechtsraum offen sind, wird zuerst eine präzise Quellenlücke ausgewiesen; fehlender Text wird nicht ergänzt.",
            "Historischer Befund, konkurrierende Deutung, spätere Rezeption und heutige Anschlussfrage bleiben sichtbar getrennt.",
        ]
    if family == "research":
        return [
            "Wenn Aufgabenstellung, Bewertungsmaßstab, Quellenstand oder Abgabeformat offen sind, wird zuerst eine begrenzte Arbeitsannahme mit Klärungspunkt formuliert.",
            "Vertretbare Gegenansichten und unsichere Quellen werden ausgewiesen; ein vorläufiger Befund wird nicht als gesichertes Endergebnis ausgegeben.",
        ]
    if family == "production":
        return [
            "Wenn Empfänger, maßgebliche Fassung, Freigabe, Anlagenbestand oder Ausgabeformat offen sind, wird zuerst eine priorisierte Fehlteilliste erzeugt.",
            "Keine Datei wird als fertig bezeichnet, solange Lesbarkeit, Benennung, Signaturbedarf, Anlagenfolge und Übergabenachweis nicht geprüft sind.",
        ]
    if family == "drafting":
        return [
            "Wenn Parteirolle, Vertretungsmacht, wirtschaftlicher Parameter, Gremienfreigabe oder Dokumentstand offen sind, wird zuerst eine Entscheidungsliste mit Auswirkung auf den Entwurf erzeugt.",
            "Offene Verhandlungspunkte, Bedingungen und Vollzugsvoraussetzungen bleiben im Entwurf sichtbar; sie werden nicht stillschweigend als vereinbart behandelt.",
        ]
    if family == "decision":
        return [
            "Wenn Antrag, Parteistellung, Zuständigkeit, Fristbeginn oder Verfahrensstand nicht tragfähig bestimmbar sind, wird zuerst eine gerichtliche oder prozessuale Lückenliste erzeugt.",
            "Ein Entscheidungsentwurf markiert fehlendes Gehör, offenen Beweis und ungeklärte Zulässigkeit, statt Entscheidungsreife nur zu behaupten.",
        ]
    return [
        "Wenn Identität, Vollmacht, Fristbeginn oder Verfahrensstand nicht tragfähig bestimmbar sind, wird zuerst eine knappe Lückenliste erzeugt.",
        "Wenn das gewünschte Ergebnis eine endgültige Rechtsentscheidung verlangt, wird nur ein belastbarer Entwurf mit offen markierten Prüfpunkten ausgegeben.",
    ]


def field_work_instruction(profile: ThemenProfil, detail: str) -> str:
    family = workflow_family(profile)
    if family == "source":
        return (
            f"{detail}. Verbinde den Punkt mit Textstelle, Textzeuge, Fassung, Übersetzung, "
            "historischem Kontext, Gegenlesart und Rezeptionsspur. Output: ausformulierter "
            "Quellenbefund mit Belegwert, Unsicherheitsgrad und heutiger Anschlussfrage."
        )
    if family == "research":
        return (
            f"{detail}. Verbinde den Punkt mit Aufgabenfrage, Maßstab, Quelle oder Datengrundlage, "
            "Gegenhypothese und belastbarer Folgerung. Output: ausformulierter Teilbefund mit "
            "Fundstelle, Unsicherheit und nächstem Arbeitsschritt."
        )
    if family == "production":
        return (
            f"{detail}. Verbinde den Punkt mit Eingangsdatei, maßgeblicher Fassung, Fundstelle, "
            "Formatanforderung, Freigabe und Übergabe. Output: geprüfte Datei oder konkrete "
            "Fehlteilliste mit Verantwortlichem und Termin."
        )
    if family == "drafting":
        return (
            f"{detail}. Verbinde den Punkt mit Geschäftsziel, Dokumentstand, Rechtswirkung, "
            "Verhandlungsposition, Risiko und Vollzug. Output: ausformulierter Entwurfs- oder "
            "Beschlussbaustein mit Variante und nächstem Closing-Schritt."
        )
    if family == "decision":
        return (
            f"{detail}. Verbinde den Punkt mit Parteivortrag, Aktenfund, Rechtsmaßstab, Beweislast, "
            "Gegenposition und Entscheidungsfolge. Output: ausformulierter Verfügungs-, Hinweis-, "
            "Beweis- oder Entscheidungsbaustein."
        )
    return (
        f"{detail}. Verbinde den Punkt mit Aktenfund, Norm, Beweislast, Gegenposition und "
        "konkreter Rechtsfolge. Output: ausformulierter Ergebnisbaustein mit Belegstelle, "
        "Risiko und nächstem Schritt."
    )


def output_variant_rows(
    profile: ThemenProfil,
    norm_pool: list[str],
    fields: list[tuple[str, str]],
) -> list[str]:
    family = workflow_family(profile)
    norm_hint = join_anchors(norm_pool[:2], 120)
    field_hint = fields[0][0] if fields else profile.label
    if family == "source":
        return [
            f"| Quelle identifizieren | Quellenkarte | Textzeuge, Fassung, Datierung, Rechtsraum und Belegwert zu {field_hint} |",
            "| Text vergleichen | Synopse | Original, Übersetzung, Abweichung, Gegenlesart und Unsicherheitsgrad |",
            f"| historisch einordnen | Epochenmemo | Institution, Normfunktion, Anwendungspraxis und Anker {norm_hint} |",
            "| Rezeption verfolgen | Rezeptionslinie | Übernahme, Umdeutung, Bruch, Fortgeltung und heutige Anschlussfrage |",
            "| vermitteln | lesbare Fachdarstellung | Kernbefund, Quellenstatus, konkurrierende Deutung und Grenzen der Aussage |",
        ]
    if family == "research":
        return [
            f"| schnell prüfen | Kurzbefund | Frage, Maßstab, {norm_hint}, stärkster Beleg und offene Annahme |",
            "| vertieft untersuchen | Argument- oder Evidenzmatrix | Quelle, Aussage, Gegenhypothese, Belastbarkeit und Folgerung |",
            "| rechnen oder bewerten | nachvollziehbares Arbeitsblatt | Eingabewerte, Zwischenschritte, Maßstab und Kontrollprobe |",
            "| ausformulieren | Gutachten-, Lösungs- oder Antragsteil | roter Faden, Quellenstatus, Gegenansicht und Ergebnis |",
            "| überarbeiten | kommentierte Fassung | konkrete Schwäche, Änderung, Begründung und verbleibende Unsicherheit |",
        ]
    if family == "production":
        return [
            "| Bestand ordnen | Dokumentenregister | Datei, Fassung, Datum, Autor, Signatur, Dublette und Lesbarkeit |",
            "| Fehler finden | Abweichungs- und Fehlteilliste | Fundstelle, Auswirkung, Korrektur, Verantwortlicher und Termin |",
            "| Fassung herstellen | Freigabedokument | vollständiger Text, Anlagenbezug, Empfänger, Format und Signaturbedarf |",
            "| Paket bilden | Export- oder Versandmappe | sprechende Dateinamen, Reihenfolge, Konvertierung und Öffnungsprobe |",
            "| Übergabe sichern | Übergabevermerk | Prüfschritte, Freigabe, Übermittlungsnachweis, Restpunkt und Wiedervorlage |",
        ]
    if family == "drafting":
        return [
            f"| schnell entscheiden | Deal- oder Regelungsvermerk | Ziel, {norm_hint}, Risikozuweisung und nächster Entwurfsgriff |",
            "| verhandeln | Positionsmatrix | Ausgangsfassung, Ziel, Rückfallposition, Begründung und Tauschmasse |",
            "| formulieren | Klausel oder Redline | Tatbestand, Mechanik, Rechtsfolge, Nachweis, Frist und Rechtsbehelf |",
            "| beschließen | Gremienvorlage | Kompetenz, Informationsgrundlage, Interessenkonflikt, Beschlusstext und Auftrag |",
            "| vollziehen | Signing- oder Closing-Liste | Bedingung, Dokument, Verantwortlicher, Termin, Freigabe und Nachweis |",
        ]
    if family == "decision":
        return [
            f"| Akte steuern | richterlicher Arbeitsvermerk | Antrag, Verfahrensstand, {norm_hint}, Entscheidungsreife und nächste Verfügung |",
            "| Gehör sichern | Hinweis oder Auflage | entscheidungserheblicher Punkt, Adressat, Frist und Rechtsfolge |",
            "| Beweis erheben | Beweisbeschluss oder Beweisplan | Beweisthema, Beweismittel, Beweislast und Ladungs- oder Gutachtenauftrag |",
            "| entscheiden | Tenor und Gründe | Streitgegenstand, Feststellungen, Würdigung, Subsumtion, Kosten und Vollstreckbarkeit |",
            "| Verfahren abschließen | förmliche Endfassung | Rubrum, Anträge, Rechtsmittelbelehrung, Zustellung und Anschlussverfügung |",
        ]
    return [
        f"| schnell entscheiden | Kurzvermerk | Fallkern, {norm_hint}, Risiko und nächster Schritt |",
        "| vertieft prüfen | Tatbestandsmatrix | Norm, Merkmal, Beleg, Beweislast, Gegenargument und Rechtsfolge |",
        "| versenden | Entwurf | Antrag oder Regelungsziel, Begründung, Anlagen, Frist und Zustellungsweg |",
        f"| beraten | Adressatenbrief | Ergebnis, Optionen, Kosten- und Zeitrisiko sowie Empfehlung zu {clean(consequence_marker(profile), 110)} |",
        f"| verhandeln | Vergleichs- oder Formulierungsvorschlag | sichere Fassung, risikobewusste Fassung und offene Punkte bei {domain_attack(profile)} |",
    ]


def argumentation_title(profile: ThemenProfil) -> str:
    return {
        "source": "Quellenkritisches Argumentations- und Darstellungsgerüst",
        "research": "Prüfungs- und Darstellungsgerüst",
        "production": "Produktions- und Freigabegerüst",
        "drafting": "Regelungs-, Verhandlungs- und Vollzugsgerüst",
        "decision": "Entscheidungs- und Begründungsgerüst",
    }.get(workflow_family(profile), "Argumentations- und Entwurfsgerüst")


def argumentation_lines(
    profile: ThemenProfil,
    norm_pool: list[str],
    case_pool: list[str],
    fields: list[tuple[str, str]],
) -> list[str]:
    family = workflow_family(profile)
    norm_hint = join_anchors(norm_pool[:2], 180)
    case_hint = join_anchors(case_pool[:2], 180) if case_pool else "erst nach verifizierter Recherche einzusetzen"
    first_field = fields[0][0] if fields else profile.pruefraster[0]
    consequence = clean(consequence_marker(profile), 150)
    if family == "source":
        return [
            "10.1. Erkenntnisziel: Benenne historische Frage, Rechtsraum, Zeitraum und gewünschte Darstellungsform; eine heutige Anschlussfrage steht erst danach.",
            f"10.2. Primärquelle: Sichere den maßgeblichen Textzeugen und die genaue Stelle; erste Anker sind {norm_hint}.",
            f"10.3. Textstufe: Arbeite Original, Edition, Übersetzung, Rekonstruktion und spätere Bearbeitung auseinander; erster Fachpunkt ist {first_field}.",
            f"10.4. Fundstelle: Nenne Werk, Buch, Titel, Fragment oder Paragraf, Ausgabe, Seite und Sprache; im Bereich {profile.label} tragen regelmäßig {domain_documents(profile)} den Nachweis.",
            f"10.5. Belegwert: {evidence_marker(profile)}. Zeige, welche Aussage der Text trägt und welche nicht.",
            f"10.6. Gegenlesart: Stelle die stärkste konkurrierende Deutung samt Quelle, zeitgenössischem Kontext und methodischem Unterschied dar. Prüfe besonders: {clean(profile.pruefraster[1], 180).rstrip('.')}.",
            "10.7. Einordnung: Antworte auf die Gegenlesart mit Sprachgebrauch, Systematik, institutioneller Funktion, Parallelquelle oder Rezeptionsbeleg; Unsicherheit bleibt quantifiziert.",
            f"10.8. Arbeitsprodukt: Schließe mit {output_hint(profile, fields)}; historische Wirkung, spätere Rezeption und heutige Anschlussfrage erhalten getrennte Absätze.",
            f"10.9. Quellenstatus: Ordne jeden Anker als Primärquelle, Edition, Übersetzung, Forschungsmeinung oder Rezeptionsentscheidung ein; erste Vergleichsanker sind {case_hint}.",
        ]
    if family == "research":
        return [
            "10.1. Arbeitsfrage: Benenne Prüfgegenstand, Maßstab, Adressat und gewünschtes Teilprodukt.",
            f"10.2. Tragender Maßstab: Stelle Norm, Ausschreibungskriterium, Bewertungsmaßstab oder methodische Regel voran; erste Anker sind {norm_hint}.",
            f"10.3. Kernprüfung: Bearbeite zuerst {first_field} und formuliere die entscheidende überprüfbare Aussage.",
            f"10.4. Fundstelle: Nenne Dokument, Seite, Datensatz, Rechenschritt oder Quelle; im Bereich {profile.label} sind dies regelmäßig {domain_documents(profile)}.",
            f"10.5. Evidenz: {evidence_marker(profile)}. Trenne Befund, Annahme und Schlussfolgerung.",
            f"10.6. Gegenhypothese: Prüfe die stärkste alternative Erklärung oder Bewertung; sie setzt typischerweise bei {domain_attack(profile)} an.",
            "10.7. Belastbarkeit: Antworte mit Gegenbeleg, Kontrollrechnung, methodischem Unterschied oder begrenzter Aussage; ein bloßes Etikett genügt nicht.",
            f"10.8. Arbeitsprodukt: Schließe mit {output_hint(profile, fields)} und einem ausdrücklich benannten nächsten Prüf- oder Redaktionsschritt.",
            f"10.9. Quellenstatus: Trenne Primärquelle, Sekundärquelle, Aktenfund, Datengrundlage und offene Recherche; erste Anker sind {case_hint}.",
        ]
    if family == "production":
        return [
            "10.1. Produktionsziel: Benenne Empfänger, Dokumenttyp, maßgebliche Fassung, Freigabestatus und Ausgabeformat.",
            f"10.2. Verbindliche Vorgabe: Ordne Form, Signatur, Dateityp, Benennung oder Übermittlungsweg zu; erste Anker sind {norm_hint}.",
            f"10.3. Kritischer Arbeitspunkt: Bearbeite zuerst {first_field}; Inhalt und technische Umsetzung werden gemeinsam geprüft.",
            f"10.4. Fundstelle: Nenne Eingangsdatei, Seite, Absatz, Zelle, Nachricht oder Anlage; im Bereich {profile.label} sind dies regelmäßig {domain_documents(profile)}.",
            f"10.5. Nachweis: {evidence_marker(profile)}. Jede Änderung bleibt zur Ausgangsfassung rückführbar.",
            f"10.6. Fehlerbild: Prüfe die stärkste Übergabe- oder Freigabestörung; sie liegt typischerweise bei {domain_attack(profile)}.",
            "10.7. Korrektur: Behebe Inhalt, Format, Anlagenbezug und Benennung gemeinsam und dokumentiere, welche Eingangsdatei wie verändert wurde.",
            f"10.8. Ausgabepaket: Schließe mit {output_hint(profile, fields)}; Öffnungsprobe, Freigabe und Übergabenachweis gehören dazu.",
            f"10.9. Status: Ordne jede Datei als Eingang, Arbeitsfassung, freigegeben, exportiert oder übermittelt ein; rechtliche Vorgaben werden nur mit gesichertem Stand verwendet: {case_hint}.",
        ]
    if family == "drafting":
        return [
            f"10.1. Regelungsziel: Benenne Parteien, Geschäftsziel, gewünschte Rechtswirkung und Vollzugszustand: {consequence}.",
            f"10.2. Rechtsrahmen: Stelle zwingende Grenze und dispositiven Gestaltungsspielraum voran; erste Anker sind {norm_hint}.",
            f"10.3. Mechanik: Arbeite zuerst {first_field}; Definition, Tatbestand, Leistung, Anpassung, Haftung und Rechtsbehelf müssen ineinandergreifen.",
            f"10.4. Dokumentstand: Nenne Fassung, Datum, Klausel, Datenraumfund, Beschluss oder Q&A-Antwort; im Bereich {profile.label} tragen regelmäßig {domain_documents(profile)} den Nachweis.",
            f"10.5. Nachweis und Freigabe: {evidence_marker(profile)}. Zeige die Folge eines offenen Parameters oder fehlenden Beschlusses.",
            f"10.6. Gegenposition: Formuliere die stärkste Verhandlungsposition der anderen Seite; sie setzt typischerweise bei {domain_attack(profile)} an.",
            f"10.7. Rückfallposition: Antworte mit konkreter Alternativfassung, Preis- oder Vollzugsausgleich und zeige die Auswirkung auf {consequence}.",
            f"10.8. Entwurf und Vollzug: Schließe mit {output_hint(profile, fields)}; Verantwortlicher, Termin, Bedingung und Erfüllungsnachweis sind ausformuliert.",
            f"10.9. Quellenstatus: Rechtsprechung wird nach Tragweite und Vertragsbezug eingeordnet; erste Fallanker sind {case_hint}.",
        ]
    if family == "decision":
        return [
            f"10.1. Entscheidungsziel: Benenne Spruchkörper, Parteistellungen, Streitgegenstand, Antrag und mögliche Entscheidungsfolge: {consequence}.",
            f"10.2. Rechtsmaßstab: Stelle Zuständigkeits-, Verfahrens- und materiellen Normsatz voran; erste Anker sind {norm_hint}.",
            f"10.3. Entscheidungserheblicher Punkt: Arbeite zuerst {first_field}; trenne Zulässigkeit, Tatsachenfeststellung und rechtliche Würdigung.",
            f"10.4. Aktenfund: Nenne Schriftsatz, Datum, Seite, Anlage, Protokollstelle und Parteizuordnung; im Bereich {profile.label} tragen regelmäßig {domain_documents(profile)} den Nachweis.",
            f"10.5. Darlegung und Beweis: {evidence_marker(profile)}. Zeige ausdrücklich, ob Hinweis, Beweisaufnahme oder Entscheidung folgt.",
            f"10.6. Gegenposition: Formuliere den stärksten Gegenantrag oder die tragfähigste abweichende Würdigung; sie setzt typischerweise bei {domain_attack(profile)} an.",
            f"10.7. Würdigung: Antworte mit Aktenbeleg, Beweiswürdigung, Auslegung oder Beweislastregel und ziehe die Folge auf {consequence}.",
            f"10.8. Förmliches Produkt: Schließe mit {output_hint(profile, fields)}; Rubrum, Tenor, Gründe, Nebenentscheidungen und Anschlussverfügung müssen zusammenpassen.",
            f"10.9. Rechtsprechungsstatus: Ordne jede Entscheidung nach Bindungswirkung und Aussagekern ein; erste Fallanker sind {case_hint}.",
        ]
    return [
        f"10.1. Kernsatz: Benenne Parteirolle, Ziel und die begehrte oder abzuwehrende Rechtsfolge aus diesem Arbeitsfeld: {consequence}.",
        f"10.2. Tragende Regel: Stelle den einschlägigen Normsatz voran und ordne ihn dem konkreten Streitpunkt zu; erste Anker sind {norm_hint}.",
        f"10.3. Tatbestandsmerkmal: Arbeite zuerst den entscheidenden Fachpunkt aus, regelmäßig {first_field}.",
        f"10.4. Aktenfund: Nenne Datum, Beteiligten, Handlung, Betrag und genaue Fundstelle; im Bereich {profile.label} tragen regelmäßig {domain_documents(profile)} den Nachweis. Eine streitige Behauptung bleibt als solche bezeichnet.",
        f"10.5. Beweislast: {evidence_marker(profile)}. Zeige ausdrücklich, welche Folge ein offener Beweis hat.",
        f"10.6. Gegenposition: Formuliere den stärksten ernsthaften Angriff; hier setzt die Gegenseite typischerweise bei {domain_attack(profile)} an.",
        f"10.7. Erwiderung: Antworte mit konkretem Gegenbeleg, Auslegung oder Beweislastregel und ziehe die Folge auf {consequence}; ein bloßes Bestreiten genügt nicht.",
        f"10.8. Arbeitsprodukt: Schließe mit Antrag, Tenor, Klausel, Entscheidung oder nächstem Schritt; hier typischerweise {output_hint(profile, fields)}.",
        f"10.9. Quellenstatus: Ordne Rechtsprechung nach Tragweite ein; erste Fallanker sind {case_hint}.",
    ]


def workflow_selfcheck(profile: ThemenProfil) -> str:
    family = workflow_family(profile)
    if family == "source":
        return (
            f"Selbstcheck vor Ausgabe: Sind {domain_deadline_question(profile)} Ist jede Übersetzung "
            "als Übersetzung erkennbar? Sind historischer Befund, Gegenlesart, Rezeption und "
            "heutige Anschlussfrage getrennt? Reicht der Quellenstatus für die behauptete Aussage?"
        )
    if family == "research":
        return (
            f"Selbstcheck vor Ausgabe: Sind {domain_deadline_question(profile)} Ist jeder tragende "
            "Befund belegt oder als Annahme markiert? Wurde die stärkste Gegenhypothese geprüft? "
            "Entspricht das Produkt dem Bewertungs- und Ausgabeformat?"
        )
    if family == "production":
        return (
            f"Selbstcheck vor Ausgabe: Sind {domain_deadline_question(profile)} Stimmen Inhalt, "
            "Dateiname, Anlagenfolge, Signaturbedarf und Exportformat überein? Wurde jede Datei "
            "geöffnet und die Übergabe protokolliert?"
        )
    if family == "drafting":
        return (
            f"Selbstcheck vor Ausgabe: Sind {domain_deadline_question(profile)} Sind wirtschaftliches "
            "Ziel, Rechtswirkung, Risikozuweisung und Vollzug deckungsgleich? Sind offene Punkte, "
            "Fassungsvarianten und Gremienfreigaben sichtbar?"
        )
    if family == "decision":
        return (
            f"Selbstcheck vor Ausgabe: Sind {domain_deadline_question(profile)} Sind Anträge und "
            "Streitgegenstand vollständig erfasst? Wurden Gehör, Beweislast, Beweiswürdigung, "
            "Tenor, Kosten, Vollstreckbarkeit und Rechtsmittelanschluss geprüft?"
        )
    return (
        f"Selbstcheck vor Ausgabe: Ist {domain_deadline_question(profile)} Ist die Form geklärt? "
        f"Ist die Rechtsfolge aus einer Norm abgeleitet und auf {clean(consequence_marker(profile), 120)} "
        "bezogen? Ist das Arbeitsprodukt tatsächlich verwendbar? Sind offene Tatsachen von "
        "offenen Rechtsfragen getrennt?"
    )


def workflow_method_text(profile: ThemenProfil) -> str:
    family = workflow_family(profile)
    common_end = (
        "Erst wenn wirklich kein verwertbares Material vorliegt, werden höchstens vier "
        "gezielte Fragen gestellt. Jede Antwort wird in ganzen Sätzen formuliert; Tabellen "
        "werden nur für echte Vergleiche, Nachweise, Berechnungen oder Varianten verwendet."
    )
    if family == "source":
        start = (
            "Arbeite zuerst quellenkritisch, dann kontextbezogen und zuletzt rezeptionsbewusst. "
            "Vorhandene Editionen, Scans, Übersetzungen und Kommentare werden ohne Vorfrage "
            "gelesen und mit genauer Textstelle, Fassung und Belegwert verarbeitet."
        )
    elif family == "research":
        start = (
            "Arbeite zuerst fragennah, dann quellen- oder datennah und zuletzt produktnah. "
            "Vorhandene Unterlagen werden ohne Vorfrage gelesen; jeder tragende Befund erhält "
            "Fundstelle, Maßstab und Belastbarkeitsangabe."
        )
    elif family == "production":
        start = (
            "Arbeite zuerst versionsnah, dann fundstellennah und zuletzt ausgabenah. Vorhandene "
            "Dateien werden ohne Vorfrage geöffnet, auf Lesbarkeit und maßgebliche Fassung "
            "geprüft und mit Freigabe- sowie Übergabestatus verarbeitet."
        )
    elif family == "drafting":
        start = (
            "Arbeite zuerst geschäftszielnah, dann regelungsnah und zuletzt vollzugsnah. "
            "Vorhandene Fassungen, Datenraumunterlagen und Beschlüsse werden ohne Vorfrage "
            "gelesen und auf Risikozuweisung, Kompetenz, Parameter und Abhängigkeiten bezogen."
        )
    elif family == "decision":
        start = (
            "Arbeite zuerst aktennah, dann beweis- und normnah und zuletzt entscheidungsnah. "
            "Vorhandene Schriftsätze, Anlagen, Verfügungen und Protokolle werden ohne Vorfrage "
            "mit Fundstelle, Parteizuordnung und Bedeutung für die Entscheidungsreife verarbeitet."
        )
    else:
        start = (
            f"Arbeite zuerst aktennah, dann normnah, dann produktnah. Liegen Unterlagen vor, "
            f"werden sie ohne Vorfrage gelesen und mit Fundstelle verarbeitet; im Bereich "
            f"{profile.label} sind das vor allem {domain_documents(profile)}."
        )
    return f"{start} {common_end}"


def section_titles(profile: ThemenProfil) -> tuple[str, str, tuple[str, str, str, str], str, str]:
    """Passt die zentralen Überschriften und Matrixspalten an die Arbeitswelt an."""

    family = workflow_family(profile)
    if family == "source":
        return (
            "Quellen- und Deutungsfallkarte",
            "Quellenanker, Textstufe, Deutungslast und Wirkung",
            ("Quellenanker", "Text- und Geltungsfrage", "Beleg- und Deutungsmerker", "Historische Wirkung"),
            "Quellenstatus, Gegenlesarten und Rezeptionswirkung",
            "Primärquellen und historische Rechtsanker",
        )
    if family == "research":
        return (
            "Prüf- und Evidenzfallkarte",
            "Maßstäbe, Kernfragen, Evidenz und Folgerung",
            ("Maßstab", "Entscheidende Frage", "Evidenzmerker", "Arbeitsfolge"),
            "Quellen-, Rechtsprechungs- und Belastbarkeitsstatus",
            "Tragende Maßstäbe und Quellen",
        )
    if family == "production":
        return (
            "Produktions- und Übergabekarte",
            "Anforderungen, Qualitätsmerkmale, Nachweis und Ausgabe",
            ("Anforderung", "Qualitätsmerkmal", "Nachweis", "Ausgabe"),
            "Vorgaben, Quellenstatus und technische Folge",
            "Verbindliche Form- und Verfahrensvorgaben",
        )
    if family == "drafting":
        return (
            "Regelungs- und Vollzugsfallkarte",
            "Rechtsanker, Regelungsmechanik, Nachweis und Vollzug",
            ("Rechtsanker", "Regelungsmechanik", "Nachweis und Freigabe", "Vollzugsfolge"),
            "Rechtsprechungsanker, Quellenstatus und Risikozuweisung",
            "Pflichtnormen und Vollzugsanker",
        )
    if family == "decision":
        return (
            "Verfahrens- und Entscheidungsfallkarte",
            "Rechtsanker, Entscheidungsmerkmale, Beweislast und Tenorfolge",
            ("Rechtsanker", "Entscheidungsmerkmal", "Beweis- und Darlegungslast", "Entscheidungsfolge"),
            "Rechtsprechungsanker, Quellenstatus und Entscheidungswirkung",
            "Pflichtnormen für Verfahren und Entscheidung",
        )
    return (
        "Rechtsprechungs-Fallkarte",
        "Normenanker, Tatbestandswichtigkeiten und Beweislast",
        ("Normenanker", "Tatbestandswichtigkeit", "Beweislastmerker", "Rechtsfolge"),
        "Rechtsprechungsanker, Quellenstatus und Rechtsfolgen",
        "Pflichtnormen als Kernsätze",
    )


def additional_pruefraster_items(profile: ThemenProfil) -> tuple[str, str]:
    family = workflow_family(profile)
    if family == "source":
        return (
            "Welche Textstelle, Gegenquelle oder Kontextinformation fehlt noch für den behaupteten historischen Befund.",
            "Welche Darstellungsform trennt Quelle, Deutung, Rezeption und heutige Anschlussfrage am klarsten.",
        )
    if family == "research":
        return (
            "Welche Quelle, Datengrundlage oder Kontrollrechnung fehlt noch für den tragenden Befund.",
            "Welches konkrete Teilprodukt löst den nächsten Prüfungs-, Bewertungs- oder Redaktionsschritt.",
        )
    if family == "production":
        return (
            "Welche Datei, Anlage, Freigabe oder technische Prüfung fehlt noch für eine belastbare Ausgabe.",
            "Welches konkrete Export-, Freigabe- oder Übergabeprodukt beseitigt den nächsten Engpass.",
        )
    if family == "drafting":
        return (
            "Welcher wirtschaftliche Parameter, Beschluss, Beleg oder Verhandlungspunkt fehlt noch für die Regelung.",
            "Welche Klausel, Redline, Entscheidungsvorlage oder Vollzugshandlung löst den nächsten Deal-Engpass.",
        )
    if family == "decision":
        return (
            "Welcher Parteivortrag, Beweis, Hinweis oder Gehörsschritt fehlt noch für die Entscheidungsreife.",
            "Welche Verfügung, Auflage, Beweiserhebung oder Entscheidungsfassung ist als Nächstes zu erstellen.",
        )
    return (
        "Welche Tatsache fehlt noch, obwohl sie für die Rechtsfolge entscheidend ist.",
        "Welches konkrete Arbeitsprodukt löst den nächsten praktischen Engpass.",
    )


def missing_case_anchor_line(profile: ThemenProfil) -> str:
    family = workflow_family(profile)
    if family == "source":
        return "- Historische Gerichts- oder Verwaltungsentscheidungen nur mit überprüfter Fundstelle, Datum, Spruchkörper, Textfassung und damaliger Funktion verwenden; sonst die konkrete Quellenfrage offen markieren."
    if family == "research":
        return "- Rechtsprechung und sonstige Leitquellen nur mit gesichertem Aussagekern verwenden; eine noch offene Fundstelle wird als präziser Recherchebedarf bezeichnet."
    if family == "production":
        return "- Rechtliche oder technische Vorgaben nur mit gesichertem Geltungsstand verwenden; fehlt der Beleg, wird die betroffene Produktionsentscheidung bis zur Prüfung markiert."
    return "- Rechtsprechung nur zitieren, wenn Gericht, Datum und Aktenzeichen sicher sind; sonst als Recherche- und Prüfbedarf mit konkreter Fallfrage markieren."


def case_section_footer(profile: ThemenProfil) -> list[str]:
    family = workflow_family(profile)
    if family == "source":
        return [
            f"- Historische Wirkung zuerst als Darstellungsprodukt denken: {consequence_marker(profile)}",
            "- Quellenstatus immer sichtbar machen: Primärtext, Edition, Übersetzung, Rekonstruktion, Forschungsmeinung, Rezeptionsquelle oder offene Prüfung.",
        ]
    if family == "research":
        return [
            f"- Folgerung zuerst als prüfbares Arbeitsprodukt denken: {consequence_marker(profile)}",
            "- Quellenstatus immer sichtbar machen: Aktenfund, Primärquelle, Sekundärquelle, Datengrundlage, gesicherte Entscheidung oder offene Recherche.",
        ]
    if family == "production":
        return [
            f"- Vorgaben auf die konkrete Ausgabe beziehen: {consequence_marker(profile)}",
            "- Status immer sichtbar machen: Eingangsdatei, Arbeitsfassung, geprüfte Vorgabe, freigegeben, exportiert, übermittelt oder offen.",
        ]
    return [
        f"- Rechtsfolge zuerst als Arbeitsprodukt denken: {consequence_marker(profile)}",
        "- Quellenstatus immer sichtbar machen: Aktenfund, Normtext, Profilanker, gesicherte Rechtsprechung oder offene Prüfung.",
    ]


def missing_lead_source_line(profile: ThemenProfil) -> str:
    if workflow_family(profile) == "source":
        return "- Fehlt eine belastbare Leitquelle oder historische Entscheidung, wird keine moderne Fundstelle ergänzt; stattdessen werden Textzeuge, Suchraum, Zeitraum und gesuchte Aussage präzise benannt."
    if workflow_family(profile) == "production":
        return "- Fehlt eine gesicherte Vorgabe, wird ihr Prüfbedarf mit betroffener Datei, Ausgabeentscheidung und Freigabefolge markiert."
    return "- Rechtsprechung nur mit Datum, Gericht und Aktenzeichen verwenden, wenn sie aus Unterlagen oder belastbarer Quelle sicher belegt ist; sonst als Prüfbedarf markieren."


def quality_control_text(profile: ThemenProfil) -> str:
    focus = clean(profile.pruefraster[-1], 170).rstrip(".") if profile.pruefraster else "die Herleitung des Ergebnisses"
    family = workflow_family(profile)
    if family == "source":
        checks = "falsche Textstufe, unbelegte Übersetzung, anachronistische Rückprojektion, vermischte Geltungszeiträume und übersprungene Gegenquellen"
        actions = "Quelle sichern, Lesart abgrenzen, Kontext ergänzen, Rezeption prüfen oder Aussage begrenzen"
    elif family == "research":
        checks = "unklare Aufgabenfrage, ungeprüfte Annahmen, schwache Quellen, Rechenfehler, ausgelassene Gegenhypothesen und unpassendes Ausgabeformat"
        actions = "belegen, nachrechnen, Gegenansicht prüfen, Text verdichten oder begrenzt nachfordern"
    elif family == "production":
        checks = "falsche Version, fehlende Anlage, beschädigten Export, unlesbare Seite, unklaren Dateinamen, offenen Signaturbedarf und fehlenden Übergabenachweis"
        actions = "korrigieren, konvertieren, öffnen, freigeben, verpacken oder nachfordern"
    elif family == "drafting":
        checks = "widersprüchliche Definitionen, offene Parameter, unklare Risikozuweisung, fehlende Kompetenz, unerfüllbare Frist und lückenhaften Vollzug"
        actions = "entscheiden, redlinen, beschließen, nachfordern, vollziehen oder als offenen Punkt ausweisen"
    elif family == "decision":
        checks = "unvollständige Anträge, Gehörsfehler, falsche Zuständigkeit, offenen Beweis, widersprüchliche Feststellungen, Tenorfehler und fehlende Nebenentscheidungen"
        actions = "verfügen, hinweisen, Beweis erheben, entscheiden, zustellen oder wiedervorlegen"
    else:
        checks = "Widersprüche, fehlende Belege, falsche Zuständigkeit, unklare Fristen, unvollständige Anträge, Rechenfehler und unpassenden Ton"
        actions = "sofort erledigen, nachfordern, entscheiden, entwerfen, einreichen oder zurückstellen"
    return (
        f"Zum Abschluss wird das Ergebnis auf {checks} geprüft. Besonders zu kontrollieren ist in "
        f"diesem Gebiet: {focus}. Danach folgt eine knappe Anschlussliste: {actions}."
    )


def schnellstart_direktstart(profile: ThemenProfil) -> list[str]:
    """Erzeugt den Einstieg aus dem Pruefraster des Gebiets.

    Frueher standen hier vier fuer alle Plugins wortgleiche Saetze. Jetzt fuehrt
    der Einstieg genau die Schritte auf, die in diesem Rechtsgebiet zuerst
    getan werden: die erste Leitfrage, der gebietstypische Engpass, die
    Beweislage und das erste Arbeitsprodukt.
    """
    raster = [clean(item, 165).rstrip(".") for item in profile.pruefraster[:3]]
    leitfrage = raster[0] if raster else clean(
        profile.stationen[0] if profile.stationen else profile.label,
        165,
    ).rstrip(".")
    kernpruefung = "; ".join(raster[1:3]) or clean(
        profile.stationen[1] if len(profile.stationen) > 1 else leitfrage,
        220,
    ).rstrip(".")
    engpass = clean(
        profile.stop[0] if profile.stop else "Frist, Zuständigkeit oder tragender Beleg ist offen",
        145,
    ).rstrip(".")
    beweis = clean(evidence_marker(profile), 175).rstrip(".")
    produkt = (
        clean(profile.skelette[0]).rstrip(".")
        if profile.skelette
        else clean(profile.stationen[-1], 220).rstrip(".")
        if profile.stationen
        else "Kurzvermerk mit Ergebnisrichtung, Risiko und nächstem Schritt"
    )
    # Stationstexte beginnen haeufig selbst mit "Arbeitsprodukt:"; das Praefix
    # wuerde sich sonst doppeln.
    produkt = re.sub(r"^Arbeitsprodukt:\s*", "", produkt).strip()
    steps = [
        f"Leitfrage aus Akte und Auftrag festlegen: {leitfrage}",
        f"Kernprüfung in einem Durchgang: {kernpruefung}",
        f"Belege und Engpass zusammenführen: {beweis}; besonders kritisch ist: {engpass}",
        f"Erstes Arbeitsprodukt liefern: {produkt}",
    ]
    return [f"{idx}. {step}." for idx, step in enumerate(steps, 1)]


def schnellstart_product_label(
    profile: ThemenProfil,
    fields: list[tuple[str, str]],
) -> str:
    """Benennt das Erstprodukt, ohne einen langen Mustersatz abzuschneiden."""

    if profile.skelette:
        product = clean(profile.skelette[0])
        if ":" in product:
            label = product.split(":", 1)[0].strip()
            if 3 <= len(label) <= 72:
                return label
        first_clause = re.split(r"[.;]", product, maxsplit=1)[0].strip()
        if 3 <= len(first_clause) <= 90:
            return first_clause
    if fields:
        return clean(f"Erststand zu {fields[0][0]}", 90).rstrip(".")
    return "fachbezogener Erststand"


def schnellstart_bedienlogik(
    profile: ThemenProfil,
    fields: list[tuple[str, str]],
    stations: list[str],
) -> list[str]:
    """Baut einen fachbezogenen Einstieg für vier reale Nutzungslagen."""

    def cell(value: str, limit: int) -> str:
        return clean(value, limit).replace("|", "/").rstrip(".")

    field_names = [cell(field, 52) for field, _detail in fields[:3]]
    if not field_names:
        field_names = [cell(item, 52) for item in profile.pruefraster[:3]]
    while len(field_names) < 3:
        field_names.append(cell(eilsache_label(profile), 52))
    route = cell(
        stations[0]
        if stations
        else profile.pruefraster[0]
        if profile.pruefraster
        else profile.label,
        115,
    )
    if ":" in route:
        route = route.split(":", 1)[0].strip()
    output = schnellstart_product_label(profile, fields)
    documents = cell(domain_documents(profile), 115)
    minimum = ", ".join(dict.fromkeys(field_names[:3]))
    return [
        "## 1. Sofortstart nach Eingangslage",
        "",
        f"- Dateien oder Ordner: Zuerst {documents} lesen. Mit {route} beginnen und das Arbeitsprodukt „{output}“ liefern.",
        f"- Konkreter Auftrag: Das verlangte Arbeitsprodukt „{output}“ sofort erzeugen; kein Lagebild voranstellen. Annahmen nur am betroffenen Ergebnis markieren.",
        f"- Nur Prompt oder Skill gestartet: Aus Dateinamen und Inhalt zwischen {minimum} routen und einen Erststand liefern, nicht nach dem Auftrag fragen.",
        "- Folgewunsch: Aktenfunde, Berechnungen, Quellen und offene Punkte beibehalten; nur die verlangte Dimension ändern, nicht neu beginnen.",
        "",
        f"Ohne verwertbares Material genau eine gebündelte Frage zu {minimum} und Empfänger stellen; „offen“ ist zulässig. Bei großen Ordnern nach den ersten entscheidungserheblichen Dateien einen Teilstand liefern und ungelesene oder unlesbare Dateien benennen. Passende Fachskills intern als Teilroute nutzen.",
        "",
    ]


def eilsache_label(profile: ThemenProfil) -> str:
    """Benennt die typische Eilsache des Gebiets statt einer Universalfloskel."""
    if profile.key in EILSACHE_LABEL:
        return EILSACHE_LABEL[profile.key]
    family = workflow_family(profile)
    if family == "source":
        return "Textzeuge, Fassung, Datierung oder Übersetzung"
    if family == "research":
        return "Aufgabenfrage, Bewertungsmaßstab oder belastbare Datengrundlage"
    if family == "production":
        return "maßgebliche Fassung, Freigabe, Anlage oder Ausgabeformat"
    if family == "drafting":
        return "Dokumentstand, Verhandlungsparameter, Gremienfreigabe oder Vollzug"
    if family == "decision":
        return "Antrag, Gehör, Entscheidungsreife oder förmliche Frist"
    for item in profile.stop:
        match = re.search(r"^([^,.;]{12,70})", clean(item))
        if match:
            return match.group(1).strip().rstrip(".")
    return f"Eilsache im Bereich {profile.label}"


def werkstatt_ergonomy_text(profile: ThemenProfil) -> str:
    """Baut Ausgabeformate, Rueckfragenbremse und Mini-Gerueste fachgebietsspezifisch.

    Die Bloecke waren frueher fuer alle Plugins wortgleich. Sie werden jetzt aus
    den Profildaten (Stop-Kriterien, Stationen, Pruefraster, Skelette, Beweis-
    und Rechtsfolgemerker) abgeleitet, damit jedes Rechtsgebiet seinen eigenen
    Arbeitsablauf sieht statt einer Universalformel.
    """
    engpass = clean(profile.stop[0], 150).rstrip(".") if profile.stop else "Frist, Form oder Zuständigkeit ungeklärt"
    eilname = eilsache_label(profile)
    produkt = clean(profile.skelette[0], 190).rstrip(".") if profile.skelette else clean(
        profile.stationen[-1], 190
    ).rstrip(".") if profile.stationen else "Antragssatz plus tragende Begründung"
    einstieg = clean(profile.pruefraster[0], 150).rstrip(".") if profile.pruefraster else "Tatbestand und Rechtsfolge trennen"
    beweis = clean(evidence_marker(profile), 165).rstrip(" .")
    folge = clean(consequence_marker(profile), 165).rstrip(" .")
    norm = anchor_head(profile.normen[0], 90) if profile.normen else "der tragende Normanker"
    station_rows = [clean(item, 175).rstrip(".") for item in profile.stationen[1:3]]
    family = workflow_family(profile)
    words = work_vocabulary(profile)
    trace_requirement = {
        "source": "jede historische Aussage erhält Textstelle und Quellenstatus",
        "research": "jeder tragende Befund erhält Quelle, Maßstab oder Rechenweg",
        "production": "jede Änderung bleibt auf Eingangsdatei und Freigabe zurückführbar",
        "drafting": "jede Regelung erhält Geschäftsziel, Rechtswirkung und Vollzugsbezug",
        "decision": "jede Feststellung erhält Parteivortrag, Aktenfund oder Beweisergebnis",
    }.get(family, "jede Tatsache bekommt Beleg oder Lückenmarke")
    station_output = {
        "source": "Quellenstand mit genauer Textstelle",
        "research": "Teilbefund mit Fundstelle",
        "production": "geprüfter Zwischenstand mit Versionsbezug",
        "drafting": "Entwurfsstand mit offener Entscheidung",
        "decision": "Entscheidungsstand mit Aktenfund",
    }.get(family, "Arbeitsstand mit Belegstelle")

    rows = [
        f"| {words['priority_label']}: {eilname} | {words['priority_output']} | {engpass}; vor Fortsetzung klären |",
        f"| Tragendes Arbeitsprodukt | {produkt} | {trace_requirement} |",
        f"| Prüfeinstieg | Kurzvermerk entlang der Leitfrage | {einstieg} |",
        f"| {words['proof_label']} | {words['proof_output']} | {beweis} |",
        f"| {words['result_label']} | {words['result_output']} | {folge} |",
    ]
    for idx, station in enumerate(station_rows, 1):
        rows.append(f"| Zwischenstation {idx} | {station_output} | {station} |")
    rows.append(
        f"| {words['audience_label']} | {words['audience_output']} | {words['audience_check']} |"
    )

    evidence_intro = {
        "source": "Quellenlage vor Deutung ordnen",
        "research": "Evidenz vor Schlussfolgerung ordnen",
        "production": "Datei- und Fundstellenlage vor Freigabe ordnen",
        "drafting": "Dokumentstand und Risikozuweisung vor Formulierung ordnen",
        "decision": "Parteivortrag und Beweislage vor Entscheidung ordnen",
    }.get(family, "Beweislage vor Rechtsmeinung ordnen")
    bremse = [
        f"1. Liegen Unterlagen vor, werte sie zuerst nach der Leitfrage „{einstieg}“ aus; frage erst danach gezielt nach.",
        f"2. Der Engpass dieses Gebiets hat Vorrang: {engpass}.",
        f"3. {evidence_intro}: {beweis}.",
        "4. Bei mehreren Wegen die zwei stärksten Varianten mit Entscheidungskriterium zeigen.",
        "5. Nur die Punkte nachfragen, die das nächste Arbeitsprodukt ändern.",
    ]

    if family == "source":
        geruest = [
            f"- Quellenbefund: [Textzeuge/Fassung] belegt für [Zeit und Rechtsraum] die Aussage [Befund]. Der Belegwert ist [hoch/mittel/begrenzt], weil [Grund].",
            f"- Kernsatz des Arbeitsprodukts: {produkt}.",
            f"- Textnachweis: [Aussage] steht in [Edition, Stelle, Sprache]; [Übersetzung] ist [amtlich/eigen/veröffentlicht] und weicht bei [Begriff] ab.",
            f"- Einordnungssatz: Daraus folgt als historischer Befund {folge}; eine heutige Rechtswirkung wird gesondert geprüft.",
            "- Gegenlesart: [Quelle oder Autor] versteht [Stelle] als [Deutung]. Dafür spricht [Beleg], dagegen [Kontext oder Gegenquelle].",
            f"- Quellenlücke: Für die Leitfrage „{einstieg}“ fehlt [Textzeuge/Fassung/Übersetzung]; bis zur Klärung ist nur [begrenzte Aussage] tragfähig.",
        ]
    elif family == "research":
        geruest = [
            f"- Kurzbefund: Tragender Maßstab ist {norm}. Nach dem derzeitigen Quellen- oder Datenstand spricht [Beleg] mehr für [Ergebnis]; offen bleibt [Annahme].",
            f"- Kernsatz des Arbeitsprodukts: {produkt}.",
            f"- Evidenzsatz: [Befund] folgt aus [Quelle, Datensatz oder Rechenweg]; im Übrigen gilt: {beweis}.",
            f"- Folgerungssatz: Unter [Annahme] folgt daraus {folge}.",
            "- Gegenhypothese: [Alternative] erklärt [Befund] anders. Dafür spricht [Beleg], dagegen [Kontrollquelle oder Rechenschritt].",
            f"- Klärungspunkt: Für die Leitfrage „{einstieg}“ fehlt [Quelle, Datum oder Parameter]; bis dahin ist nur [begrenzte Folgerung] tragfähig.",
        ]
    elif family == "production":
        geruest = [
            "- Produktionsbefund: Maßgeblich ist [Datei/Fassung] vom [Datum]; [Abweichung] betrifft [Inhalt, Anlage oder Format] und muss vor Freigabe behoben werden.",
            f"- Kernsatz des Arbeitsprodukts: {produkt}.",
            f"- Fundstellensatz: [Angabe] stammt aus [Datei, Seite, Zelle oder Nachricht]; im Übrigen gilt: {beweis}.",
            f"- Ausgabesatz: Nach Korrektur und Öffnungsprobe entsteht {folge}.",
            "- Abweichung: Eingangsdatei und Zielprodukt unterscheiden sich bei [Punkt]. Die Freigabefassung übernimmt [Variante] aus [Grund].",
            f"- Fehlteil: Für die Leitfrage „{einstieg}“ fehlt [Datei/Freigabe/Anlage]; verantwortlich ist [Person], Termin [Datum].",
        ]
    elif family == "drafting":
        geruest = [
            f"- Regelungskern: Der Rechtsrahmen beginnt bei {norm}. [Partei] benötigt [Wirkung], um [Geschäftsziel] umzusetzen; offen ist [Parameter].",
            f"- Kernsatz des Arbeitsprodukts: {produkt}.",
            f"- Nachweissatz: [Voraussetzung] ist durch [Dokument/Freigabe] belegt; im Übrigen gilt: {beweis}.",
            f"- Mechaniksatz: Wenn [Tatbestand] eintritt, folgt [Leistung, Anpassung, Haftung oder Vollzug] und damit {folge}.",
            "- Gegenposition: Die andere Seite verlangt [Variante]. Zielposition, Rückfallposition und Tauschmasse werden mit ihrer jeweiligen Rechts- und Preiswirkung ausgewiesen.",
            f"- Entscheidungspunkt: Für die Leitfrage „{einstieg}“ fehlt [commercial point/Freigabe/Beleg]; ohne ihn bleibt [Klausel oder Vollzug] offen.",
        ]
    elif family == "decision":
        geruest = [
            f"- Entscheidungsstand: Der Rechtsmaßstab beginnt bei {norm}. Nach Aktenlage tragen [Parteivortrag] und [Beleg] eher [Tenor/Verfügung]; offen ist [Punkt].",
            f"- Kernsatz des Arbeitsprodukts: {produkt}.",
            f"- Feststellungssatz: [Tatsache] folgt aus [Beweismittel und Würdigung]; im Übrigen gilt: {beweis}.",
            f"- Entscheidungssatz: Aus [Norm und Subsumtion] folgt {folge}.",
            "- Gegenposition: Der stärkste Gegenantrag oder die abweichende Würdigung lautet [Position]. Sie scheitert oder greift durch, weil [Beleg, Beweislast oder Norm].",
            f"- Aufklärungspunkt: Für die Leitfrage „{einstieg}“ fehlt [Vortrag/Beweis/Gehör]; nächste Verfügung: [Text] bis [Datum].",
        ]
    else:
        geruest = [
            f"- Sofortvermerk: Der Ausgangsanker ist {norm}. Nach derzeitigem Stand spricht [Beleg] bei [Tatbestandsmerkmal] mehr für [Ergebnis]; offen bleibt [Lücke].",
            f"- Kernsatz des Arbeitsprodukts: {produkt}.",
            f"- Beweissatz: [Tatsache] ist durch [Beweismittel] belegt; im Übrigen gilt: {beweis}.",
            f"- Rechtsfolgensatz: Daraus folgt {folge}.",
            f"- Gegenposition: Die Gegenseite wird einwenden, dass [Argument]. Dagegen spricht [Beleg oder Norm]. Risiko: [niedrig/mittel/hoch].",
            f"- Nachforderung: Bitte reichen Sie [Dokument] bis [Datum] ein; ohne diesen Beleg bleibt die Leitfrage „{einstieg}“ offen.",
        ]

    return (
        "### 1.2. Ausgabeformate für schnelle Lieferung\n\n"
        "| Bedarf | Sofortausgabe | Qualitätsgriff |\n| --- | --- | --- |\n"
        + "\n".join(rows)
        + "\n\n### 1.3. Rückfragenbremse\n\n"
        + "\n".join(bremse)
        + "\n\n### 1.4. Mini-Gerüste\n\n"
        + "\n".join(geruest)
        + "\n"
    )
WERKSTATT_FINAL_CHECK_LINES = """- Erstes Ergebnis steht oben, nicht am Ende versteckt.
- Jede offene Tatsache ist als Nachforderung formuliert.
- Jede Rechtsfrage hat mindestens einen Normanker.
- Das nächste Dokument oder die nächste Handlung ist benannt.
- Der Ton passt zum Empfänger: Mandant, Gericht, Behörde, Gegner oder intern.
- Wenn zwei Wege vertretbar sind, steht die empfohlene Variante mit Grund vor der Alternative.
- Keine Nebenspur bleibt offen: erledigen, zurückstellen oder nachfordern.
"""
WERKSTATT_DEPTH_LINES = """1. Rollenwahl: Antragsteller, Antragsgegner, Behörde, Gericht, Gegner oder interner Entscheider klar festlegen.
2. Sofortausgabe: Kurzlage, stärkster Anker, schwächster Punkt, Frist und nächstes Dokument zuerst liefern.
3. Beweisarbeit: Jede tragende Tatsache einer Fundstelle, einem Beweismittel oder einer Nachforderung zuordnen.
4. Gegenposition: Das stärkste Gegenargument nicht verstecken, sondern mit Beweislast und Risiko beantworten.
5. Varianten: Bei zwei vertretbaren Wegen die schnellere, die belastbarere und die taktisch riskante Variante trennen.
6. Versandreife: Am Ende prüfen, ob Empfänger, Antrag, Tenor, Anlagen, Fristen und Zustellungsweg zusammenpassen.

| Lage | Schneller Output | Vertiefung |
| --- | --- | --- |
| Unterlagen unvollständig | Lückenliste mit Priorität | Warum die Lücke das Ergebnis ändert |
| Frist oder Form kritisch | Fristenblatt und Sofortmaßnahme | Zustellungs- und Zuständigkeitsprüfung |
| Streitiger Sachverhalt | Beweis- und Widerspruchsmatrix | Substantiierung, Beweislast, Gegenbeweis |
| Entwurf gewünscht | verwertbarer Kerntext | Anlagenlogik, Gegenargument, Risiken |
| Entscheidungsvorlage | Empfehlung mit Alternativen | Kosten, Zeit, Eskalation, Vergleich |
"""

# Plugins, deren Werkstatt- und Schnellstart-Markdown von Hand gepflegt werden.
# Der Generator ueberschreibt sie nicht; er meldet sie als uebersprungen.
PROTECTED_LIST = Path(__file__).resolve().parent / "handkuratierte-prompts.txt"


def load_protected() -> set[str]:
    if not PROTECTED_LIST.exists():
        return set()
    slugs: set[str] = set()
    for raw in PROTECTED_LIST.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        slugs.add(line)
    return slugs


BAD_WORDS = (
    "s" + "crape",
    "s" + "craping",
    "c" + "rawl",
    "c" + "rawling",
    "NOT" + "_FOUND",
    "T" + "BD",
)


PROSE_REPLACEMENTS = (
    ("Aussen", "Außen"),
    ("aussen", "außen"),
    ("Fachbehorde", "Fachbehörde"),
    ("fachbehorde", "fachbehörde"),
    ("Beweisantrage", "Beweisanträge"),
    ("beweisantrage", "beweisanträge"),
    ("Personlich", "Persönlich"),
    ("personlich", "persönlich"),
    ("Vermogens", "Vermögens"),
    ("vermogens", "vermögens"),
    ("Vorauszahlungsstaende", "Vorauszahlungsstände"),
    ("vorauszahlungsstaende", "vorauszahlungsstände"),
    ("Betaeubungsmittel", "Betäubungsmittel"),
    ("betaeubungsmittel", "betäubungsmittel"),
    ("Privatsphaere", "Privatsphäre"),
    ("privatsphaere", "privatsphäre"),
    ("Eroefffnungsverfahren", "Eröffnungsverfahren"),
    ("eroefffnungsverfahren", "eröffnungsverfahren"),
    ("Prioritaet", "Priorität"),
    ("prioritaet", "priorität"),
    ("Huetterin", "Hüterin"),
    ("huetterin", "hüterin"),
    ("abzuloesen", "abzulösen"),
    ("Genuesst", "Genießt"),
    ("genuesst", "genießt"),
    ("Wuenschenswert", "Wünschenswert"),
    ("wuenschenswert", "wünschenswert"),
    ("dreijaehr", "dreijähr"),
    ("Dreijaehr", "Dreijähr"),
    ("Aerztlich", "Ärztlich"),
    ("aerztlich", "ärztlich"),
    ("Kernstueck", "Kernstück"),
    ("kernstueck", "kernstück"),
    ("beigefuegt", "beigefügt"),
    ("Beigefuegt", "Beigefügt"),
    ("abgewaelzt", "abgewälzt"),
    ("Abgewaelzt", "Abgewälzt"),
    ("Durchblaettern", "Durchblättern"),
    ("durchblaettern", "durchblättern"),
    ("Saemtlich", "Sämtlich"),
    ("saemtlich", "sämtlich"),
    ("Grundzuege", "Grundzüge"),
    ("grundzuege", "grundzüge"),
    ("Verjaerungs", "Verjährungs"),
    ("verjaerungs", "verjährungs"),
    ("praeklud", "präklud"),
    ("Praeklud", "Präklud"),
    ("Berufsausuebung", "Berufsausübung"),
    ("berufsausuebung", "berufsausübung"),
    ("Ausruestung", "Ausrüstung"),
    ("ausruestung", "ausrüstung"),
    ("Buerokratieversteher", "Bürokratieversteher"),
    ("buerokratieversteher", "bürokratieversteher"),
    ("Entbuerokratisierer", "Entbürokratisierer"),
    ("entbuerokratisierer", "entbürokratisierer"),
    ("eingeschraenkt", "eingeschränkt"),
    ("Eingeschraenkt", "Eingeschränkt"),
    ("schlaegt", "schlägt"),
    ("Schlaegt", "Schlägt"),
    ("bestandskraeftig", "bestandskräftig"),
    ("Bestandskraeftig", "Bestandskräftig"),
    ("gefaelscht", "gefälscht"),
    ("Gefaelscht", "Gefälscht"),
    ("zusaetzlich", "zusätzlich"),
    ("Zusaetzlich", "Zusätzlich"),
    ("verstaendlich", "verständlich"),
    ("Verstaendlich", "Verständlich"),
    ("uneingeschraenkt", "uneingeschränkt"),
    ("Uneingeschraenkt", "Uneingeschränkt"),
    ("Tagesverzoegerung", "Tagesverzögerung"),
    ("tagesverzoegerung", "tagesverzögerung"),
    ("Begueneten", "Begünstigten"),
    ("begueneten", "begünstigten"),
    ("Primearquelle", "Primärquelle"),
    ("primearquelle", "primärquelle"),
    ("Funktionaer", "Funktionär"),
    ("funktionaer", "funktionär"),
    ("paritaetisch", "paritätisch"),
    ("Paritaetisch", "Paritätisch"),
    ("Kuestenlage", "Küstenlage"),
    ("kuestenlage", "küstenlage"),
    ("Thueringen", "Thüringen"),
    ("thueringen", "thüringen"),
    ("Laenge", "Länge"),
    ("laenge", "länge"),
    ("Ertuechtig", "Ertüchtig"),
    ("ertuechtig", "ertüchtig"),
    ("jaehr", "jähr"),
    ("Jaehr", "Jähr"),
    ("Betriebsraete", "Betriebsräte"),
    ("betriebsraete", "betriebsräte"),
    ("erschuetter", "erschütter"),
    ("Erschuetter", "Erschütter"),
    ("Rueckstaende", "Rückstände"),
    ("rueckstaende", "rückstände"),
    ("taeglich", "täglich"),
    ("Taeglich", "Täglich"),
    ("ueblich", "üblich"),
    ("Ueblich", "Üblich"),
    ("Einverstaendnis", "Einverständnis"),
    ("einverstaendnis", "einverständnis"),
    ("Abschwaecher", "Abschwächer"),
    ("abschwaecher", "abschwächer"),
    ("unzuverlaessig", "unzuverlässig"),
    ("Unzuverlaessig", "Unzuverlässig"),
    ("zuverlaessig", "zuverlässig"),
    ("Zuverlaessig", "Zuverlässig"),
    ("Schriftstueck", "Schriftstück"),
    ("schriftstueck", "schriftstück"),
    ("wuensch", "wünsch"),
    ("Wuensch", "Wünsch"),
    ("uebrig", "übrig"),
    ("Uebrig", "Übrig"),
    ("branchenueblich", "branchenüblich"),
    ("Branchenueblich", "Branchenüblich"),
    ("schaerf", "schärf"),
    ("Schaerf", "Schärf"),
    ("Drohgebaerde", "Drohgebärde"),
    ("drohgebaerde", "drohgebärde"),
    ("abschwaech", "abschwäch"),
    ("Abschwaech", "Abschwäch"),
    ("tuerkisch", "türkisch"),
    ("Tuerkisch", "Türkisch"),
    ("ungueltig", "ungültig"),
    ("Ungueltig", "Ungültig"),
    ("taegig", "tägig"),
    ("Taegig", "Tägig"),
    ("Haelt", "Hält"),
    ("haelt", "hält"),
    ("Sozietaet", "Sozietät"),
    ("sozietaet", "sozietät"),
    ("multidisziplinaer", "multidisziplinär"),
    ("Multidisziplinaer", "Multidisziplinär"),
    ("Steuerneutralitaet", "Steuerneutralität"),
    ("steuerneutralitaet", "steuerneutralität"),
    ("Kapazitaet", "Kapazität"),
    ("kapazitaet", "kapazität"),
    ("Exklusivitaet", "Exklusivität"),
    ("exklusivitaet", "exklusivität"),
    ("Toechter", "Töchter"),
    ("toechter", "töchter"),
    ("vorsaetzlich", "vorsätzlich"),
    ("Vorsaetzlich", "Vorsätzlich"),
    ("gefuellt", "gefüllt"),
    ("Gefuellt", "Gefüllt"),
    ("marktmaechtig", "marktmächtig"),
    ("Marktmaechtig", "Marktmächtig"),
    ("Pflichtenpruefung", "Pflichtenprüfung"),
    ("pflichtenpruefung", "pflichtenprüfung"),
    ("Frageboegen", "Fragebögen"),
    ("frageboegen", "fragebögen"),
    ("maennlich", "männlich"),
    ("Maennlich", "Männlich"),
    ("faelschlich", "fälschlich"),
    ("Faelschlich", "Fälschlich"),
    ("Waermepumpe", "Wärmepumpe"),
    ("waermepumpe", "wärmepumpe"),
    ("Ausueben", "Ausüben"),
    ("ausueben", "ausüben"),
    ("außergewoehnlich", "außergewöhnlich"),
    ("Außergewoehnlich", "Außergewöhnlich"),
    ("puenktlich", "pünktlich"),
    ("Puenktlich", "Pünktlich"),
    ("Lohnpfaendung", "Lohnpfändung"),
    ("lohnpfaendung", "lohnpfändung"),
    ("Buendel", "Bündel"),
    ("buendel", "bündel"),
    ("Eingangstuer", "Eingangstür"),
    ("eingangstuer", "eingangstür"),
    ("Eintraege", "Einträge"),
    ("eintraege", "einträge"),
    ("Goae", "GOÄ"),
    ("goae", "GOÄ"),
    ("Ueben", "Üben"),
    ("ueben", "üben"),
    ("Plausibilitaet", "Plausibilität"),
    ("plausibilitaet", "plausibilität"),
    ("Verlustvortraege", "Verlustvorträge"),
    ("verlustvortraege", "verlustvorträge"),
    ("Verstaendnis", "Verständnis"),
    ("verstaendnis", "verständnis"),
    ("aehnlich", "ähnlich"),
    ("Aehnlich", "Ähnlich"),
    ("Ablaeufe", "Abläufe"),
    ("ablaeufe", "abläufe"),
    ("Rollenentscheidungsbaeume", "Rollenentscheidungsbäume"),
    ("rollenentscheidungsbaeume", "rollenentscheidungsbäume"),
    ("regelmaeßig", "regelmäßig"),
    ("Regelmaeßig", "Regelmäßig"),
    ("Erloesbudget", "Erlösbudget"),
    ("erloesbudget", "erlösbudget"),
    ("duenn", "dünn"),
    ("Duenn", "Dünn"),
    ("durchgaengig", "durchgängig"),
    ("Durchgaengig", "Durchgängig"),
    ("kuenftig", "künftig"),
    ("Kuenftig", "Künftig"),
    ("oekologisch", "ökologisch"),
    ("Oekologisch", "Ökologisch"),
    ("duerfen", "dürfen"),
    ("Duerfen", "Dürfen"),
    ("Bauauftraege", "Bauaufträge"),
    ("bauauftraege", "bauaufträge"),
    ("aufzaehl", "aufzähl"),
    ("Aufzaehl", "Aufzähl"),
    ("Schwaeche", "Schwäche"),
    ("schwaeche", "schwäche"),
    ("Lizenzkompatibilitaet", "Lizenzkompatibilität"),
    ("lizenzkompatibilitaet", "lizenzkompatibilität"),
    ("geglaettet", "geglättet"),
    ("Geglaettet", "Geglättet"),
    ("staedtebaulich", "städtebaulich"),
    ("Staedtebaulich", "Städtebaulich"),
    ("Praktikabilitaet", "Praktikabilität"),
    ("praktikabilitaet", "praktikabilität"),
    ("Patentanwaeltin", "Patentanwältin"),
    ("patentanwaeltin", "patentanwältin"),
    ("Praejudizien", "Präjudizien"),
    ("praejudizien", "präjudizien"),
    ("Kriminalitaet", "Kriminalität"),
    ("kriminalitaet", "kriminalität"),
    ("Sicherstellungszuschlaege", "Sicherstellungszuschläge"),
    ("sicherstellungszuschlaege", "sicherstellungszuschläge"),
    ("Branchenzuschlaege", "Branchenzuschläge"),
    ("branchenzuschlaege", "branchenzuschläge"),
    ("Führungskraefte", "Führungskräfte"),
    ("führungskraefte", "führungskräfte"),
    ("Zoelle", "Zölle"),
    ("zoelle", "zölle"),
    ("Erwaegungsgrund", "Erwägungsgrund"),
    ("erwaegungsgrund", "erwägungsgrund"),
    ("Sondiergaenge", "Sondiergänge"),
    ("sondiergaenge", "sondiergänge"),
    ("zaehlen", "zählen"),
    ("Zaehlen", "Zählen"),
    ("Komplexitaetsgrad", "Komplexitätsgrad"),
    ("komplexitaetsgrad", "komplexitätsgrad"),
    ("Lückenfuellung", "Lückenfüllung"),
    ("lückenfuellung", "lückenfüllung"),
    ("schriftsaetzen", "schriftsätzen"),
    ("Schriftsaetzen", "Schriftsätzen"),
    ("Berufsgeheimnisraeger", "Berufsgeheimnisträger"),
    ("berufsgeheimnisraeger", "berufsgeheimnisträger"),
    ("Zahlungsrückstaende", "Zahlungsrückstände"),
    ("zahlungsrückstaende", "zahlungsrückstände"),
    ("Hoejesteret", "Højesteret"),
    ("Oesterreich", "Österreich"),
    ("oesterreich", "österreich"),
    ("OePNV", "ÖPNV"),
    ("Oepnv", "ÖPNV"),
    ("Epue", "EPÜ"),
    ("epue", "EPÜ"),
    ("AUeG", "AÜG"),
    ("TKUe", "TKÜ"),
    ("Pfueb", "PfÜB"),
    ("pfueb", "PfÜB"),
    ("Praeferenz", "Präferenz"),
    ("praeferenz", "präferenz"),
    ("Zueigenmachen", "Zueigenmachen"),
    ("Lohnpfaendung", "Lohnpfändung"),
    ("lohnpfaendung", "lohnpfändung"),
    ("eigenhaendig", "eigenhändig"),
    ("Eigenhaendig", "Eigenhändig"),
    ("Erloes", "Erlös"),
    ("erloes", "erlös"),
    ("Zubehoer", "Zubehör"),
    ("zubehoer", "zubehör"),
    ("verkuendet", "verkündet"),
    ("Verkuendet", "Verkündet"),
    ("nuetzlich", "nützlich"),
    ("Nuetzlich", "Nützlich"),
    ("Haustuer", "Haustür"),
    ("haustuer", "haustür"),
    ("Anwaltsgespraech", "Anwaltsgespräch"),
    ("anwaltsgespraech", "anwaltsgespräch"),
    ("Stueck", "Stück"),
    ("stueck", "stück"),
    ("Opportunitaet", "Opportunität"),
    ("opportunitaet", "opportunität"),
    ("bueruehmter", "berühmter"),
    ("Bueruehmter", "Berühmter"),
    ("gleichermassen", "gleichermaßen"),
    ("Gleichermassen", "Gleichermaßen"),
    ("Vergutung", "Vergütung"),
    ("vergutung", "vergütung"),
    ("Rückstaende", "Rückstände"),
    ("rückstaende", "rückstände"),
    ("dreijaerig", "dreijährig"),
    ("Dreijaerig", "Dreijährig"),
    ("Strafmass", "Strafmaß"),
    ("strafmass", "strafmaß"),
    ("Prüfungsmassstab", "Prüfungsmaßstab"),
    ("prüfungsmassstab", "prüfungsmaßstab"),
    ("Jud Suess", "Jud Süß"),
    ("daenisch", "dänisch"),
    ("Daenisch", "Dänisch"),
    ("foermig", "förmig"),
    ("Foermig", "Förmig"),
    ("Praerogativ", "Prärogativ"),
    ("praerogativ", "prärogativ"),
    ("Effektivitaetsgleichwertigkeit", "Effektivitätsgleichwertigkeit"),
    ("effektivitaetsgleichwertigkeit", "effektivitätsgleichwertigkeit"),
    ("religioes", "religiös"),
    ("Religioes", "Religiös"),
    ("westfaelisch", "westfälisch"),
    ("Westfaelisch", "Westfälisch"),
    ("Integritaet", "Integrität"),
    ("integritaet", "integrität"),
    ("OEPNV", "ÖPNV"),
    ("Eroerrterung", "Erörterung"),
    ("eroerrterung", "erörterung"),
    ("Erwaegung", "Erwägung"),
    ("erwaegung", "erwägung"),
    ("haendisch", "händisch"),
    ("Haendisch", "Händisch"),
    ("Knoeringer", "Knöringer"),
    ("Lehrkraefte", "Lehrkräfte"),
    ("lehrkraefte", "lehrkräfte"),
    ("KostRAeG", "KostRÄG"),
    ("Gewaesser", "Gewässer"),
    ("gewaesser", "gewässer"),
    ("Bruttoabwaelzung", "Bruttoabwälzung"),
    ("bruttoabwaelzung", "bruttoabwälzung"),
    ("Nettoabwaelzung", "Nettoabwälzung"),
    ("nettoabwaelzung", "nettoabwälzung"),
    ("Suedafrika", "Südafrika"),
    ("suedafrika", "südafrika"),
    ("Kuecuekdeveci", "Kücükdeveci"),
    ("Arbeitsverhaltnis", "Arbeitsverhältnis"),
    ("arbeitsverhaltnis", "arbeitsverhältnis"),
    ("Arbeitgeberkundigung", "Arbeitgeberkündigung"),
    ("arbeitgeberkundigung", "arbeitgeberkündigung"),
    ("massig", "mäßig"),
    ("Massig", "Mäßig"),
    ("erfullt", "erfüllt"),
    ("Erfullt", "Erfüllt"),
    ("fluchtig", "flüchtig"),
    ("Fluchtig", "Flüchtig"),
    ("liessen", "ließen"),
    ("Liessen", "Ließen"),
    ("Guetetermin", "Gütetermin"),
    ("guetetermin", "gütetermin"),
    ("Berufsausuebungsgesellschaft", "Berufsausübungsgesellschaft"),
    ("berufsausuebungsgesellschaft", "berufsausübungsgesellschaft"),
    ("Wuerfel", "Würfel"),
    ("wuerfel", "würfel"),
    ("Bafoeg", "BAföG"),
    ("bafoeg", "BAföG"),
    ("Prüfungsgespraech", "Prüfungsgespräch"),
    ("prüfungsgespraech", "prüfungsgespräch"),
    ("Unterwuerfigkeit", "Unterwürfigkeit"),
    ("unterwuerfigkeit", "unterwürfigkeit"),
    ("Parteivortraege", "Parteivorträge"),
    ("parteivortraege", "parteivorträge"),
    ("Haustürgeschaeft", "Haustürgeschäft"),
    ("haustürgeschaeft", "haustürgeschäft"),
    ("Haustuergeschaeft", "Haustürgeschäft"),
    ("haustuergeschaeft", "haustürgeschäft"),
    ("oeffnest", "öffnest"),
    ("Oeffnest", "Öffnest"),
    ("Eroeffn", "Eröffn"),
    ("eroeffn", "eröffn"),
    ("fuer", "für"),
    ("Fuer", "Für"),
    ("benoetigt", "benötigt"),
    ("Benoetigt", "Benötigt"),
    ("hoechst", "höchst"),
    ("Hoechst", "Höchst"),
    ("fuenf", "fünf"),
    ("Fuenf", "Fünf"),
    ("Geringfueg", "Geringfüg"),
    ("geringfueg", "geringfüg"),
    ("Geldbusse", "Geldbuße"),
    ("geldbusse", "geldbuße"),
    ("Gemeinnuetz", "Gemeinnütz"),
    ("gemeinnuetz", "gemeinnütz"),
    ("Beschraenk", "Beschränk"),
    ("beschraenk", "beschränk"),
    ("Fahrlaess", "Fahrläss"),
    ("fahrlaess", "fahrläss"),
    ("Begruend", "Begründ"),
    ("begruend", "begründ"),
    ("Endgueltig", "Endgültig"),
    ("endgueltig", "endgültig"),
    ("Buergerlich", "Bürgerlich"),
    ("buergerlich", "bürgerlich"),
    ("Zugaeng", "Zugäng"),
    ("zugaeng", "zugäng"),
    ("Voelkerrecht", "Völkerrecht"),
    ("voelkerrecht", "völkerrecht"),
    ("vorlaeufig", "vorläufig"),
    ("Vorlaeufig", "Vorläufig"),
    ("ueber", "über"),
    ("Ueber", "Über"),
    ("Ueberschrift", "Überschrift"),
    ("ueberschrift", "überschrift"),
    ("Pruef", "Prüf"),
    ("pruef", "prüf"),
    ("Rueck", "Rück"),
    ("rueck", "rück"),
    ("Lueck", "Lück"),
    ("lueck", "lück"),
    ("Klaer", "Klär"),
    ("klaer", "klär"),
    ("laeuft", "läuft"),
    ("Laeuft", "Läuft"),
    ("einschlaeg", "einschläg"),
    ("Einschlaeg", "Einschläg"),
    ("zustaendig", "zuständig"),
    ("Zustaendig", "Zuständig"),
    ("beduerftig", "bedürftig"),
    ("Beduerftig", "Bedürftig"),
    ("vollstaendig", "vollständig"),
    ("Vollstaendig", "Vollständig"),
    ("tatsaechlich", "tatsächlich"),
    ("Tatsaechlich", "Tatsächlich"),
    ("naechst", "nächst"),
    ("Naechst", "Nächst"),
    ("haeng", "häng"),
    ("Haeng", "Häng"),
    ("Widerspruech", "Widersprüch"),
    ("widerspruech", "widersprüch"),
    ("zurueck", "zurück"),
    ("Zurueck", "Zurück"),
    ("loest", "löst"),
    ("Loest", "Löst"),
    ("Geruest", "Gerüst"),
    ("geruest", "gerüst"),
    ("Bauchgefuehl", "Bauchgefühl"),
    ("bauchgefuehl", "bauchgefühl"),
    ("knuepf", "knüpf"),
    ("Knuepf", "Knüpf"),
    ("traegt", "trägt"),
    ("Traegt", "Trägt"),
    ("fuehrt", "führt"),
    ("Fuehrt", "Führt"),
    ("Saetze", "Sätze"),
    ("Saetzen", "Sätzen"),
    ("saetze", "sätze"),
    ("saetzen", "sätzen"),
    ("Maengel", "Mängel"),
    ("maengel", "mängel"),
    ("Kuendig", "Kündig"),
    ("kuendig", "kündig"),
    ("Beschaeftig", "Beschäftig"),
    ("beschaeftig", "beschäftig"),
    ("Faellig", "Fällig"),
    ("faellig", "fällig"),
    ("Moeglich", "Möglich"),
    ("moeglich", "möglich"),
    ("Vermoeg", "Vermög"),
    ("vermoeg", "vermög"),
    ("Einkuenft", "Einkünft"),
    ("einkuenft", "einkünft"),
    ("Gruend", "Gründ"),
    ("gruend", "gründ"),
    ("Ausser", "Außer"),
    ("ausser", "außer"),
    ("oeffentlich", "öffentlich"),
    ("Oeffentlich", "Öffentlich"),
    ("ordnungsmaessig", "ordnungsmäßig"),
    ("Ordnungsgemaess", "Ordnungsgemäß"),
    ("gemaess", "gemäß"),
    ("Gemaess", "Gemäß"),
    ("Ruege", "Rüge"),
    ("ruege", "rüge"),
    ("uebersicht", "übersicht"),
    ("Uebersicht", "Übersicht"),
    ("Ueberschrift", "Überschrift"),
    ("ueberschrift", "überschrift"),
    ("zurueck", "zurück"),
    ("Zurueck", "Zurück"),
    ("Wirtschaftspruefer", "Wirtschaftsprüfer"),
    ("Bestaetig", "Bestätig"),
    ("bestaetig", "bestätig"),
    ("Einschraenk", "Einschränk"),
    ("einschraenk", "einschränk"),
    ("sorgfaeltig", "sorgfältig"),
    ("Sorgfaeltig", "Sorgfältig"),
    ("Qualitaet", "Qualität"),
    ("qualitaet", "qualität"),
    ("Frueh", "Früh"),
    ("frueh", "früh"),
    ("unfaeh", "unfäh"),
    ("Unfaeh", "Unfäh"),
    ("faeh", "fäh"),
    ("Faeh", "Fäh"),
    ("Geschaeft", "Geschäft"),
    ("geschaeft", "geschäft"),
    ("vorlaeufig", "vorläufig"),
    ("Vorlaeufig", "Vorläufig"),
    ("Massnahme", "Maßnahme"),
    ("Massnahmen", "Maßnahmen"),
    ("massnahme", "maßnahme"),
    ("massnahmen", "maßnahmen"),
    ("regelmaessig", "regelmäßig"),
    ("Regelmaessig", "Regelmäßig"),
    ("Liquiditaet", "Liquidität"),
    ("liquiditaet", "liquidität"),
    ("Glaeubiger", "Gläubiger"),
    ("glaeubiger", "gläubiger"),
    ("waehl", "wähl"),
    ("Waehl", "Wähl"),
    ("genueg", "genüg"),
    ("Genueg", "Genüg"),
    ("schliess", "schließ"),
    ("Schliess", "Schließ"),
    ("Verstoss", "Verstoß"),
    ("verstoss", "verstoß"),
    ("muessen", "müssen"),
    ("Muessen", "Müssen"),
    ("Rechtsanwaelte", "Rechtsanwälte"),
    ("Anwaelte", "Anwälte"),
    ("Aerzte", "Ärzte"),
    ("Buerger", "Bürger"),
    ("Laender", "Länder"),
    ("laender", "länder"),
    ("Anspruech", "Ansprüch"),
    ("anspruech", "ansprüch"),
    ("Verjaehr", "Verjähr"),
    ("verjaehr", "verjähr"),
    ("Miethoehe", "Miethöhe"),
    ("Rueckstaende", "Rückstände"),
    ("rueckstaende", "rückstände"),
    ("ordnungsmaessig", "ordnungsmäßig"),
    ("streitwertunabhaengig", "streitwertunabhängig"),
    ("formularmaessig", "formularmäßig"),
    ("Mietvertraeg", "Mietverträg"),
    ("mietvertraeg", "mietverträg"),
    ("Schoenheit", "Schönheit"),
    ("schoenheit", "schönheit"),
    ("koennen", "können"),
    ("Koennen", "Können"),
    ("ueberwaelz", "überwälz"),
    ("Ueberwaelz", "Überwälz"),
    ("Bautraegervertrag", "Bauträgervertrag"),
    ("Bautraegervertraeg", "Bauträgerverträg"),
    ("bautraegervertrag", "bauträgervertrag"),
    ("dreissig", "dreißig"),
    ("Dreissig", "Dreißig"),
    ("fuenf", "fünf"),
    ("Fuenf", "Fünf"),
    ("Fuenftel", "Fünftel"),
    ("fuenftel", "fünftel"),
    ("Duesseldorf", "Düsseldorf"),
    ("duesseldorf", "düsseldorf"),
    ("Foerder", "Förder"),
    ("foerder", "förder"),
    ("HoeO", "HöfeO"),
    ("Hoeo", "HöfeO"),
    ("Paechter", "Pächter"),
    ("paechter", "pächter"),
    ("hinterlaesst", "hinterlässt"),
    ("Hinterlaesst", "Hinterlässt"),
    ("Behoerde", "Behörde"),
    ("behoerde", "behörde"),
    ("Anhoer", "Anhör"),
    ("anhoer", "anhör"),
    ("traegt", "trägt"),
    ("Traegt", "Trägt"),
    ("praeg", "präg"),
    ("Praeg", "Präg"),
    ("Roemisch", "Römisch"),
    ("roemisch", "römisch"),
    ("Zwoelf", "Zwölf"),
    ("zwoelf", "zwölf"),
    ("Europaeisch", "Europäisch"),
    ("europaeisch", "europäisch"),
    ("hoeflich", "höflich"),
    ("Hoeflich", "Höflich"),
    ("Vertraeg", "Verträg"),
    ("vertraeg", "verträg"),
    ("praevent", "prävent"),
    ("Praevent", "Prävent"),
    ("Rechtsausuebung", "Rechtsausübung"),
    ("rechtsausuebung", "rechtsausübung"),
    ("Ausfuehrung", "Ausführung"),
    ("ausfuehrung", "ausführung"),
    ("waehrend", "während"),
    ("Waehrend", "Während"),
    ("Verfueg", "Verfüg"),
    ("verfueg", "verfüg"),
    ("Persoenlich", "Persönlich"),
    ("persoenlich", "persönlich"),
    ("ueble", "üble"),
    ("Ueble", "Üble"),
    ("Abwaeg", "Abwäg"),
    ("abwaeg", "abwäg"),
    ("Unterstuetz", "Unterstütz"),
    ("unterstuetz", "unterstütz"),
    ("Aerzte", "Ärzte"),
    ("aerzte", "ärzte"),
    ("Anwaelte", "Anwälte"),
    ("anwaelte", "anwälte"),
    ("langjaehrig", "langjährig"),
    ("Langjaehrig", "Langjährig"),
    ("Bewaehr", "Bewähr"),
    ("bewaehr", "bewähr"),
    ("Sachverstaendig", "Sachverständig"),
    ("sachverstaendig", "sachverständig"),
    ("Antraeg", "Anträg"),
    ("antraeg", "anträg"),
    ("Legalitaet", "Legalität"),
    ("legalitaet", "legalität"),
    ("Umstaend", "Umständ"),
    ("umstaend", "umständ"),
    ("oeffnet", "öffnet"),
    ("Oeffnet", "Öffnet"),
    ("wuerdig", "würdig"),
    ("Wuerdig", "Würdig"),
    ("Verstaendig", "Verständig"),
    ("verstaendig", "verständig"),
    ("Leistungstraeg", "Leistungsträg"),
    ("leistungstraeg", "leistungsträg"),
    ("Kostentraeg", "Kostenträg"),
    ("kostentraeg", "kostenträg"),
    ("realitaet", "realität"),
    ("Realitaet", "Realität"),
    ("Verhältnismaessig", "Verhältnismäßig"),
    ("verhältnismaessig", "verhältnismäßig"),
    ("Kuerz", "Kürz"),
    ("kuerz", "kürz"),
    ("versaeumnis", "versäumnis"),
    ("Versaeumnis", "Versäumnis"),
    ("Mobilitaet", "Mobilität"),
    ("mobilitaet", "mobilität"),
    ("einfuehrend", "einführend"),
    ("Einfuehrend", "Einführend"),
    ("grundstuetzung", "grundstützung"),
    ("Grundstuetzung", "Grundstützung"),
    ("grossen", "großen"),
    ("Grosse", "Große"),
    ("grosse", "große"),
    ("Rueckgewaehr", "Rückgewähr"),
    ("rueckgewaehr", "rückgewähr"),
    ("foermlich", "förmlich"),
    ("Foermlich", "Förmlich"),
    ("gewuenscht", "gewünscht"),
    ("Gewuenscht", "Gewünscht"),
    ("Stoerung", "Störung"),
    ("stoerung", "störung"),
    ("Wuerttemberg", "Württemberg"),
    ("wuerttemberg", "württemberg"),
    ("Bodendenkmaeler", "Bodendenkmäler"),
    ("bodendenkmaeler", "bodendenkmäler"),
    ("Schloesser", "Schlösser"),
    ("schloesser", "schlösser"),
    ("zugaenglich", "zugänglich"),
    ("Zugaenglich", "Zugänglich"),
    ("Verhaeltnismaess", "Verhältnismäß"),
    ("verhaeltnismaess", "verhältnismäß"),
    ("Verhaeltnis", "Verhältnis"),
    ("verhaeltnis", "verhältnis"),
    ("Zugehoer", "Zugehör"),
    ("zugehoer", "zugehör"),
    ("Auslaend", "Ausländ"),
    ("auslaend", "ausländ"),
    ("Kausalitaet", "Kausalität"),
    ("kausalitaet", "kausalität"),
    ("Subsidiaritaet", "Subsidiarität"),
    ("subsidiaritaet", "subsidiarität"),
    ("Rechtmaess", "Rechtmäß"),
    ("rechtmaess", "rechtmäß"),
    ("Zulaess", "Zuläss"),
    ("zulaess", "zuläss"),
    ("Schluess", "Schlüss"),
    ("schluess", "schlüss"),
    ("Nachtraeg", "Nachträg"),
    ("nachtraeg", "nachträg"),
    ("Uebereinkommen", "Übereinkommen"),
    ("uebereinkommen", "übereinkommen"),
    ("Ueberschuld", "Überschuld"),
    ("ueberschuld", "überschuld"),
    ("Zufluesse", "Zuflüsse"),
    ("zufluesse", "zuflüsse"),
    ("Erschoepf", "Erschöpf"),
    ("erschoepf", "erschöpf"),
    ("Vervielfaeltig", "Vervielfältig"),
    ("vervielfaeltig", "vervielfältig"),
    ("Bruessel", "Brüssel"),
    ("bruessel", "brüssel"),
    ("Identitaet", "Identität"),
    ("identitaet", "identität"),
    ("Ermaechtig", "Ermächtig"),
    ("ermaechtig", "ermächtig"),
    ("Tatbestaend", "Tatbeständ"),
    ("tatbestaend", "tatbeständ"),
    ("Einraeum", "Einräum"),
    ("einraeum", "einräum"),
    ("Schoepf", "Schöpf"),
    ("schoepf", "schöpf"),
    ("endguelt", "endgült"),
    ("Endguelt", "Endgült"),
    ("grundsaetz", "grundsätz"),
    ("Grundsaetz", "Grundsätz"),
    ("Menschenwuerde", "Menschenwürde"),
    ("menschenwuerde", "menschenwürde"),
    ("Loesch", "Lösch"),
    ("loesch", "lösch"),
    ("Verguet", "Vergüt"),
    ("verguet", "vergüt"),
    ("Aender", "Änder"),
    ("aender", "änder"),
    ("geschuetz", "geschütz"),
    ("Geschuetz", "Geschütz"),
    ("Bautraeger", "Bauträger"),
    ("bautraeger", "bauträger"),
    ("Strafhoehe", "Strafhöhe"),
    ("strafhoehe", "strafhöhe"),
    ("eigenstaendig", "eigenständig"),
    ("Eigenstaendig", "Eigenständig"),
    ("Vertragsmaess", "Vertragsmäß"),
    ("vertragsmaess", "vertragsmäß"),
    ("Publizitaet", "Publizität"),
    ("publizitaet", "publizität"),
    ("Konformitaet", "Konformität"),
    ("konformitaet", "konformität"),
    ("Gleichmaess", "Gleichmäß"),
    ("gleichmaess", "gleichmäß"),
    ("Kontinuitaet", "Kontinuität"),
    ("kontinuitaet", "kontinuität"),
    ("Verfassungsmaess", "Verfassungsmäß"),
    ("verfassungsmaess", "verfassungsmäß"),
    ("Erfuell", "Erfüll"),
    ("erfuell", "erfüll"),
    ("Heranfuehr", "Heranführ"),
    ("heranfuehr", "heranführ"),
    ("Beschwerdefuehr", "Beschwerdeführ"),
    ("beschwerdefuehr", "beschwerdeführ"),
    ("Voelker", "Völker"),
    ("voelker", "völker"),
    ("enthaelt", "enthält"),
    ("Enthaelt", "Enthält"),
    ("Sanktionshuerde", "Sanktionshürde"),
    ("sanktionshuerde", "sanktionshürde"),
    ("Buergschaft", "Bürgschaft"),
    ("buergschaft", "bürgschaft"),
    ("Staatsangehoer", "Staatsangehör"),
    ("staatsangehoer", "staatsangehör"),
    ("Militaer", "Militär"),
    ("militaer", "militär"),
    ("Kuenstlich", "Künstlich"),
    ("kuenstlich", "künstlich"),
    ("Bevoelker", "Bevölker"),
    ("bevoelker", "bevölker"),
    ("Volkszaehl", "Volkszähl"),
    ("volkszaehl", "volkszähl"),
    ("Masseschmaeler", "Masseschmäler"),
    ("masseschmaeler", "masseschmäler"),
    ("Toedlich", "Tödlich"),
    ("toedlich", "tödlich"),
    ("Oekoland", "Ökoland"),
    ("oekoland", "ökoland"),
    ("Loesung", "Lösung"),
    ("loesung", "lösung"),
    ("Buchfuehr", "Buchführ"),
    ("buchfuehr", "buchführ"),
    ("Bezueg", "Bezüg"),
    ("bezueg", "bezüg"),
    ("Anfaeng", "Anfäng"),
    ("anfaeng", "anfäng"),
    ("Faell", "Fäll"),
    ("faell", "fäll"),
    ("Staerk", "Stärk"),
    ("staerk", "stärk"),
    ("Fuehr", "Führ"),
    ("fuehr", "führ"),
    ("Hoehe", "Höhe"),
    ("hoehe", "höhe"),
    ("Naehe", "Nähe"),
    ("naehe", "nähe"),
    ("Begruend", "Begründ"),
    ("begruend", "begründ"),
    ("Abschaetz", "Abschätz"),
    ("abschaetz", "abschätz"),
    ("Gruen", "Grün"),
    ("gruen", "grün"),
    ("Verspaet", "Verspät"),
    ("verspaet", "verspät"),
    ("Pfaend", "Pfänd"),
    ("pfaend", "pfänd"),
    ("Ueberhoeh", "Überhöh"),
    ("ueberhoeh", "überhöh"),
    ("Überhoeh", "Überhöh"),
    ("überhoeh", "überhöh"),
    ("Erhoeh", "Erhöh"),
    ("erhoeh", "erhöh"),
    ("Groess", "Größ"),
    ("groess", "größ"),
    ("Auskuenft", "Auskünft"),
    ("auskuenft", "auskünft"),
    ("Beiraet", "Beirät"),
    ("beiraet", "beirät"),
    ("Adhaesion", "Adhäsion"),
    ("adhaesion", "adhäsion"),
    ("Zulaes", "Zuläs"),
    ("zulaes", "zuläs"),
    ("Woert", "Wört"),
    ("woert", "wört"),
    ("Verbaend", "Verbänd"),
    ("verbaend", "verbänd"),
    ("Justitiabilitaet", "Justitiabilität"),
    ("justitiabilitaet", "justitiabilität"),
    ("Subsidiaer", "Subsidiär"),
    ("subsidiaer", "subsidiär"),
    ("Haeuser", "Häuser"),
    ("haeuser", "häuser"),
    ("Klaeger", "Kläger"),
    ("klaeger", "kläger"),
    ("Aktionaer", "Aktionär"),
    ("aktionaer", "aktionär"),
    ("Flaeche", "Fläche"),
    ("flaeche", "fläche"),
    ("Woerter", "Wörter"),
    ("woerter", "wörter"),
    ("Vorschlaeg", "Vorschläg"),
    ("vorschlaeg", "vorschläg"),
    ("Traeger", "Träger"),
    ("traeger", "träger"),
    ("Gueter", "Güter"),
    ("gueter", "güter"),
    ("Staendig", "Ständig"),
    ("staendig", "ständig"),
    ("Schoeff", "Schöff"),
    ("schoeff", "schöff"),
    ("Unverzueg", "Unverzüg"),
    ("unverzueg", "unverzüg"),
    ("Lueth", "Lüth"),
    ("Vorgaeng", "Vorgäng"),
    ("vorgaeng", "vorgäng"),
    ("Zerruett", "Zerrütt"),
    ("zerruett", "zerrütt"),
    ("Bruessel", "Brüssel"),
    ("bruessel", "brüssel"),
    ("Gehoer", "Gehör"),
    ("gehoer", "gehör"),
    ("Spruchkoerper", "Spruchkörper"),
    ("spruchkoerper", "spruchkörper"),
    ("oertlich", "örtlich"),
    ("Oertlich", "Örtlich"),
    ("rechtskraeft", "rechtskräft"),
    ("Rechtskraeft", "Rechtskräft"),
    ("Abaender", "Abänder"),
    ("abaender", "abänder"),
    ("Erlaeuter", "Erläuter"),
    ("erlaeuter", "erläuter"),
    ("Gestaend", "Geständ"),
    ("gestaend", "geständ"),
    ("Klagehaeuf", "Klagehäuf"),
    ("klagehaeuf", "klagehäuf"),
    ("Praesenz", "Präsenz"),
    ("praesenz", "präsenz"),
    ("muendlich", "mündlich"),
    ("Muendlich", "Mündlich"),
    ("subsidiaer", "subsidiär"),
    ("Subsidiaer", "Subsidiär"),
    ("minderjaehr", "minderjähr"),
    ("Minderjaehr", "Minderjähr"),
    ("ortsueblic", "ortsüblich"),
    ("Ortsueblic", "Ortsüblich"),
    ("Bautraeg", "Bauträg"),
    ("bautraeg", "bauträg"),
    ("Taeusch", "Täusch"),
    ("taeusch", "täusch"),
    ("Einbuerger", "Einbürger"),
    ("einbuerger", "einbürger"),
    ("Auszueg", "Auszüg"),
    ("auszueg", "auszüg"),
    ("Praeklusion", "Präklusion"),
    ("praeklusion", "präklusion"),
    ("Entschaedig", "Entschädig"),
    ("entschaedig", "entschädig"),
    ("Identitaet", "Identität"),
    ("identitaet", "identität"),
    ("Raeum", "Räum"),
    ("raeum", "räum"),
    ("Aeusser", "Äußer"),
    ("aeusser", "äußer"),
    ("Belaestig", "Belästig"),
    ("belaestig", "belästig"),
    ("Vergueet", "Vergüt"),
    ("vergueet", "vergüt"),
    ("Verguet", "Vergüt"),
    ("verguet", "vergüt"),
    ("Haerte", "Härte"),
    ("haerte", "härte"),
    ("Gebaeud", "Gebäud"),
    ("gebaeud", "gebäud"),
    ("Betriebsgroess", "Betriebsgröß"),
    ("betriebsgroess", "betriebsgröß"),
    ("Sekundaer", "Sekundär"),
    ("sekundaer", "sekundär"),
    ("Ergaenz", "Ergänz"),
    ("ergaenz", "ergänz"),
    ("Gebuehr", "Gebühr"),
    ("gebuehr", "gebühr"),
    ("Spezialitaet", "Spezialität"),
    ("spezialitaet", "spezialität"),
    ("Kuenstlich", "Künstlich"),
    ("kuenstlich", "künstlich"),
    ("Bevoelker", "Bevölker"),
    ("bevoelker", "bevölker"),
    ("Oekoland", "Ökoland"),
    ("oekoland", "ökoland"),
    ("Militaer", "Militär"),
    ("militaer", "militär"),
    ("Humanitaer", "Humanitär"),
    ("humanitaer", "humanitär"),
    ("Auslaender", "Ausländer"),
    ("auslaender", "ausländer"),
    ("Staatsangehoer", "Staatsangehör"),
    ("staatsangehoer", "staatsangehör"),
    ("Anwaerter", "Anwärter"),
    ("anwaerter", "anwärter"),
    ("Dienstbezueg", "Dienstbezüg"),
    ("dienstbezueg", "dienstbezüg"),
    ("erfuell", "erfüll"),
    ("Erfuell", "Erfüll"),
    ("AueG", "AÜG"),
    ("Aueg", "AÜG"),
    ("EPUe", "EPÜ"),
    ("Mueller", "Müller"),
    ("mueller", "müller"),
    ("Grundstueck", "Grundstück"),
    ("grundstueck", "grundstück"),
    ("Untertaen", "Untertän"),
    ("untertaen", "untertän"),
    ("koerper", "körper"),
    ("Koerper", "Körper"),
    ("noetig", "nötig"),
    ("Noetig", "Nötig"),
    ("Vorlaeufer", "Vorläufer"),
    ("vorlaeufer", "vorläufer"),
    ("Ausflueg", "Ausflüg"),
    ("ausflueg", "ausflüg"),
    ("Fledermaeuse", "Fledermäuse"),
    ("fledermaeuse", "fledermäuse"),
    ("woertlich", "wörtlich"),
    ("Woertlich", "Wörtlich"),
    ("Klaeger", "Kläger"),
    ("klaeger", "kläger"),
    ("Beweismass", "Beweismaß"),
    ("beweismass", "beweismaß"),
    ("entscheidungstraechtig", "entscheidungsträchtig"),
    ("Entscheidungstraechtig", "Entscheidungsträchtig"),
    ("Pfaend", "Pfänd"),
    ("pfaend", "pfänd"),
    ("Erwaehn", "Erwähn"),
    ("erwaehn", "erwähn"),
    ("Taetig", "Tätig"),
    ("taetig", "tätig"),
    ("Buerge", "Bürge"),
    ("buerge", "bürge"),
    ("Buergen", "Bürgen"),
    ("buergen", "bürgen"),
    ("regulaer", "regulär"),
    ("Regulaer", "Regulär"),
    ("Grenzbaeum", "Grenzbäum"),
    ("grenzbaeum", "grenzbäum"),
    ("Kaufmaenn", "Kaufmänn"),
    ("kaufmaenn", "kaufmänn"),
    ("Loehn", "Löhn"),
    ("loehn", "löhn"),
    ("Bussgeld", "Bußgeld"),
    ("bussgeld", "bußgeld"),
    ("Beifueg", "Beifüg"),
    ("beifueg", "beifüg"),
    ("Kooperationsgespraech", "Kooperationsgespräch"),
    ("kooperationsgespraech", "kooperationsgespräch"),
    ("Bandzaehl", "Bandzähl"),
    ("bandzaehl", "bandzähl"),
    ("Aktenstueck", "Aktenstück"),
    ("aktenstueck", "aktenstück"),
    ("Interoperabilitaet", "Interoperabilität"),
    ("interoperabilitaet", "interoperabilität"),
    ("Datenportabilitaet", "Datenportabilität"),
    ("datenportabilitaet", "datenportabilität"),
    ("Tonalitaet", "Tonalität"),
    ("tonalitaet", "tonalität"),
    ("aussergewoehnlich", "außergewöhnlich"),
    ("Aussergewoehnlich", "Außergewöhnlich"),
    ("Jaehrlich", "Jährlich"),
    ("jaehrlich", "jährlich"),
    ("Grossplattform", "Großplattform"),
    ("grossplattform", "großplattform"),
    ("Luecken-Fuelung", "Lückenfüllung"),
    ("luecken-fuelung", "lückenfüllung"),
    ("Fuer", "Für"),
    ("fuer", "für"),
    ("Heranfuehr", "Heranführ"),
    ("heranfuehr", "heranführ"),
    ("Konformitaet", "Konformität"),
    ("konformitaet", "konformität"),
    ("Folgenabschaetz", "Folgenabschätz"),
    ("folgenabschaetz", "folgenabschätz"),
    ("Geschaetz", "Geschätz"),
    ("geschaetz", "geschätz"),
    ("Pruef", "Prüf"),
    ("pruef", "prüf"),
    ("Aender", "Änder"),
    ("aender", "änder"),
    ("Laender", "Länder"),
    ("laender", "länder"),
    ("Begruend", "Begründ"),
    ("begruend", "begründ"),
    ("Verfassungsmaess", "Verfassungsmäß"),
    ("verfassungsmaess", "verfassungsmäß"),
    ("Voelker", "Völker"),
    ("voelker", "völker"),
    ("Oeffentlich", "Öffentlich"),
    ("oeffentlich", "öffentlich"),
    ("Lueck", "Lück"),
    ("lueck", "lück"),
    ("Ermaechtig", "Ermächtig"),
    ("ermaechtig", "ermächtig"),
    ("Foerder", "Förder"),
    ("foerder", "förder"),
    ("Verbaendeanhoer", "Verbändeanhör"),
    ("verbaendeanhoer", "verbändeanhör"),
    ("Staatsangehoer", "Staatsangehör"),
    ("staatsangehoer", "staatsangehör"),
    ("Entwuerf", "Entwürf"),
    ("entwuerf", "entwürf"),
    ("Zustaendig", "Zuständig"),
    ("zustaendig", "zuständig"),
    ("Erhaelt", "Erhält"),
    ("erhaelt", "erhält"),
    ("Mobilitaet", "Mobilität"),
    ("mobilitaet", "mobilität"),
    ("Praevent", "Prävent"),
    ("praevent", "prävent"),
    ("Entschliess", "Entschließ"),
    ("entschliess", "entschließ"),
    ("Guetever", "Gütever"),
    ("guetever", "gütever"),
    ("Behoerd", "Behörd"),
    ("behoerd", "behörd"),
    ("Schuetz", "Schütz"),
    ("schuetz", "schütz"),
    ("Taeter", "Täter"),
    ("taeter", "täter"),
    ("Gewaehr", "Gewähr"),
    ("gewaehr", "gewähr"),
    ("Geldwaesch", "Geldwäsch"),
    ("geldwaesch", "geldwäsch"),
    ("Uebergang", "Übergang"),
    ("uebergang", "übergang"),
    ("Praez", "Präz"),
    ("praez", "präz"),
    ("Nachzueg", "Nachzüg"),
    ("nachzueg", "nachzüg"),
    ("Lektuere", "Lektüre"),
    ("lektuere", "lektüre"),
    ("Aelter", "Älter"),
    ("aelter", "älter"),
    ("Schaetz", "Schätz"),
    ("schaetz", "schätz"),
    ("Rollenklaer", "Rollenklär"),
    ("rollenklaer", "rollenklär"),
    ("Justitiabilitaet", "Justitiabilität"),
    ("justitiabilitaet", "justitiabilität"),
    ("Fuehrerschein", "Führerschein"),
    ("fuehrerschein", "führerschein"),
    ("Waehl", "Wähl"),
    ("waehl", "wähl"),
    ("Versaeum", "Versäum"),
    ("versaeum", "versäum"),
    ("Spaet", "Spät"),
    ("spaet", "spät"),
    ("Qualitaet", "Qualität"),
    ("qualitaet", "qualität"),
    ("Moechte", "Möchte"),
    ("moechte", "möchte"),
    ("Laesst", "Lässt"),
    ("laesst", "lässt"),
    ("Federfuehr", "Federführ"),
    ("federfuehr", "federführ"),
    ("Einschlaeg", "Einschläg"),
    ("einschlaeg", "einschläg"),
    ("Plaene", "Pläne"),
    ("plaene", "pläne"),
    ("Kaeufer", "Käufer"),
    ("kaeufer", "käufer"),
    ("Haustuerg", "Haustürg"),
    ("haustuerg", "haustürg"),
    ("Eingriffsintensitaet", "Eingriffsintensität"),
    ("eingriffsintensitaet", "eingriffsintensität"),
    ("Bevollmaechtig", "Bevollmächtig"),
    ("bevollmaechtig", "bevollmächtig"),
    ("Beiraete", "Beiräte"),
    ("beiraete", "beiräte"),
    ("Abflues", "Abflüs"),
    ("abflues", "abflüs"),
    ("Waere", "Wäre"),
    ("waere", "wäre"),
    ("Verstoess", "Verstöß"),
    ("verstoess", "verstöß"),
    ("Enthaelt", "Enthält"),
    ("enthaelt", "enthält"),
    ("Beruehr", "Berühr"),
    ("beruehr", "berühr"),
    ("Aufloes", "Auflös"),
    ("aufloes", "auflös"),
    ("Verlaenger", "Verlänger"),
    ("verlaenger", "verlänger"),
    ("Verkaeufer", "Verkäufer"),
    ("verkaeufer", "verkäufer"),
    ("Schaeden", "Schäden"),
    ("schaeden", "schäden"),
    ("Praesens", "Präsens"),
    ("praesens", "präsens"),
    ("Natuer", "Natür"),
    ("natuer", "natür"),
    ("Masseunzulaeng", "Masseunzuläng"),
    ("masseunzulaeng", "masseunzuläng"),
    ("Loyalitaet", "Loyalität"),
    ("loyalitaet", "loyalität"),
    ("Haeus", "Häus"),
    ("haeus", "häus"),
    ("Geraete", "Geräte"),
    ("geraete", "geräte"),
    ("Flughaef", "Flughäf"),
    ("flughaef", "flughäf"),
    ("Drehtuer", "Drehtür"),
    ("drehtuer", "drehtür"),
    ("Bonitaet", "Bonität"),
    ("bonitaet", "bonität"),
    ("Beschaedig", "Beschädig"),
    ("beschaedig", "beschädig"),
    ("Beitraeg", "Beiträg"),
    ("beitraeg", "beiträg"),
    ("Vielfaelt", "Vielfält"),
    ("vielfaelt", "vielfält"),
    ("Stationaer", "Stationär"),
    ("stationaer", "stationär"),
    ("Schaed", "Schäd"),
    ("schaed", "schäd"),
    ("Nuechtern", "Nüchtern"),
    ("nuechtern", "nüchtern"),
    ("Kalendermaess", "Kalendermäß"),
    ("kalendermaess", "kalendermäß"),
    ("Juenger", "Jünger"),
    ("juenger", "jünger"),
    ("Haeufig", "Häufig"),
    ("haeufig", "häufig"),
    ("Gutglaeub", "Gutgläub"),
    ("gutglaeub", "gutgläub"),
    ("Ausloes", "Auslös"),
    ("ausloes", "auslös"),
    ("Ausgeueb", "Ausgeüb"),
    ("ausgeueb", "ausgeüb"),
    ("Ausfuell", "Ausfüll"),
    ("ausfuell", "ausfüll"),
    ("Aufspuer", "Aufspür"),
    ("aufspuer", "aufspür"),
    ("Wuerde", "Würde"),
    ("wuerde", "würde"),
    ("Vollstaendig", "Vollständig"),
    ("vollstaendig", "vollständig"),
    ("Versoehn", "Versöhn"),
    ("versoehn", "versöhn"),
    ("Verjaehr", "Verjähr"),
    ("verjaehr", "verjähr"),
    ("Telefongespraech", "Telefongespräch"),
    ("telefongespraech", "telefongespräch"),
    ("Zirkelschlues", "Zirkelschlüss"),
    ("zirkelschlues", "zirkelschlüss"),
    ("Zaesur", "Zäsur"),
    ("zaesur", "zäsur"),
    ("Stoerer", "Störer"),
    ("stoerer", "störer"),
    ("Sonderwuensch", "Sonderwünsch"),
    ("sonderwuensch", "sonderwünsch"),
    ("Rueckstaend", "Rückständ"),
    ("rueckstaend", "rückständ"),
    ("Rechtsfoerm", "Rechtsförm"),
    ("rechtsfoerm", "rechtsförm"),
    ("Primaer", "Primär"),
    ("primaer", "primär"),
    ("Plaedoyer", "Plädoyer"),
    ("plaedoyer", "plädoyer"),
    ("Muenchen", "München"),
    ("muenchen", "münchen"),
    ("Kollegialitaet", "Kollegialität"),
    ("kollegialitaet", "kollegialität"),
    ("Koerperschaft", "Körperschaft"),
    ("koerperschaft", "körperschaft"),
    ("Koennte", "Könnte"),
    ("koennte", "könnte"),
    ("Haendler", "Händler"),
    ("haendler", "händler"),
    ("Guenstig", "Günstig"),
    ("guenstig", "günstig"),
    ("Geschaedig", "Geschädig"),
    ("geschaedig", "geschädig"),
    ("Gegenueber", "Gegenüber"),
    ("gegenueber", "gegenüber"),
    ("Gefluegel", "Geflügel"),
    ("gefluegel", "geflügel"),
    ("Empfaeng", "Empfäng"),
    ("empfaeng", "empfäng"),
    ("Einschaetz", "Einschätz"),
    ("einschaetz", "einschätz"),
    ("Eigentuem", "Eigentüm"),
    ("eigentuem", "eigentüm"),
    ("Doppelboed", "Doppelböd"),
    ("doppelboed", "doppelböd"),
    ("Daenemark", "Dänemark"),
    ("daenemark", "dänemark"),
    ("Boesglaeub", "Bösgläub"),
    ("boesglaeub", "bösgläub"),
    ("Betraeg", "Beträg"),
    ("betraeg", "beträg"),
    ("Beeintraechtig", "Beeinträchtig"),
    ("beeintraechtig", "beeinträchtig"),
    ("Amtsaerzt", "Amtsärzt"),
    ("amtsaerzt", "amtsärzt"),
    ("Aktualitaet", "Aktualität"),
    ("aktualitaet", "aktualität"),
    ("Vorlaeuflig", "Vorläufig"),
    ("vorlaeuflig", "vorläufig"),
)


TERM_REPLACEMENTS = {
    "Agg": "AGG",
    "Apas": "APAS",
    "Bgh": "BGH",
    "Bag": "BAG",
    "Bverfg": "BVerfG",
    "Bverwg": "BVerwG",
    "Bsg": "BSG",
    "Bfh": "BFH",
    "Gdb": "GdB",
    "Bk": "BK",
    "Bg": "BG",
    "Eugh": "EuGH",
    "Starug": "StaRUG",
    "Bav": "bAV",
    "Gmbh": "GmbH",
    "Ag": "AG",
    "Kg": "KG",
    "Eu": "EU",
    "Dsgvo": "Datenschutz-Grundverordnung",
    "Hr": "HR",
    "Hoai": "HOAI",
    "Euipo": "EUIPO",
    "Jveg": "JVEG",
    "Oepp": "ÖPP",
    "Pralr": "PrALR",
    "Alr": "ALR",
    "Sgb": "SGB",
    "sgb": "SGB",
    "Sgg": "SGG",
    "sgg": "SGG",
    "Famfg": "FamFG",
    "famfg": "FamFG",
    "Gvg": "GVG",
    "gvg": "GVG",
    "Bgb": "BGB",
    "Zpo": "ZPO",
    "Stpo": "StPO",
    "Stgb": "StGB",
    "Arbgg": "ArbGG",
    "Vwgo": "VwGO",
    "Inso": "InsO",
    "Umwg": "UmwG",
    "Gmbhg": "GmbHG",
    "Aktg": "AktG",
    "Tzbfg": "TzBfG",
    "Betrvg": "BetrVG",
    "Kschg": "KSchG",
    "Versausglg": "VersAusglG",
    "Gewschg": "GewSchG",
    "Vvg": "VVG",
    "Hgb": "HGB",
    "Rpfleg": "RPflG",
    "Lwvfg": "LwVfG",
    "Grdstvg": "GrdstVG",
}


SENSITIVE_TERM_REPLACEMENTS = (
    ("Micro" + "soft 365 Copi" + "lot", "Office-Arbeitsbegleiter"),
    ("Open" + "AI", "externer Modellanbieter"),
    ("Chat" + "GPT", "externes Textsystem"),
    ("Anth" + "ropic", "externer Modellanbieter"),
    ("Clau" + "de", "externes Textsystem"),
    ("Per" + "plexity", "externer Recherchedienst"),
    ("Copi" + "lot", "Arbeitsbegleiter"),
    ("Legal-" + "A" + "I", "Legal-Tech"),
    ("A" + "I Act", "Regulierungsrahmen"),
    ("A" + "I-Code", "algorithmisch erzeugter Code"),
    ("A" + "I Generated", "automatisiert erzeugtes Material"),
    ("A" + "I Training", "Training automatisierter Systeme"),
    ("A" + "I Pair Programming", "automatisiertes Pair Programming"),
    ("A" + "I VDR Classifier", "VDR-Klassifizierung"),
    ("Word Legal " + "A" + "I", "Word Legal Tech"),
    ("K" + "I-VO", "Regulierungsrahmen"),
    ("K" + "I-Verordnung", "Regulierungsrahmen"),
    ("K" + "I-Richtlinie", "Systemrichtlinie"),
    ("Schatten-" + "K" + "I", "Schatten-Systeme"),
    ("Pricing-" + "K" + "I", "Pricing-Systeme"),
    ("K" + "I-/", "System-/"),
    ("K" + "I-", "System-"),
    ("-" + "K" + "I", "-Systeme"),
)


def build_replacement_trie(replacements: tuple[tuple[str, str], ...]) -> dict:
    root: dict = {}
    for old, new in replacements:
        node = root
        for char in old:
            node = node.setdefault(char, {})
        node[None] = new
    return root


PROSE_REPLACEMENT_TRIE = build_replacement_trie(PROSE_REPLACEMENTS)

MACHINE_TOKEN_PATTERN = re.compile(
    r"```[\s\S]*?```|~~~[\s\S]*?~~~|`[^`\n]+`|"
    r"https?://[^\s<>()]+|[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}|"
    r"(?<![\w])(?:~|\.\.?|)?/(?:[A-Za-z0-9._~%+-]+/?)+|"
    r"(?:[A-Za-z0-9._~-]+/)+[A-Za-z0-9._~-]+\.[A-Za-z0-9]{1,10}"
)


def replace_from_trie(text: str, trie: dict) -> str:
    """Ersetzt alle bekannten Schreibweisen in einem linearen Textdurchlauf."""

    out: list[str] = []
    index = 0
    while index < len(text):
        node = trie
        cursor = index
        replacement: tuple[int, str] | None = None
        while cursor < len(text) and text[cursor] in node:
            node = node[text[cursor]]
            cursor += 1
            if None in node:
                replacement = (cursor, node[None])
        if replacement is None:
            out.append(text[index])
            index += 1
        else:
            index, value = replacement
            out.append(value)
    return "".join(out)


def prose_umlauts(text: str) -> str:
    # Slugs, Links, Mailadressen und Konfigurationspfade bleiben maschinenlesbar.
    # Insbesondere darf der Repository-Konfigurationspfad nicht durch die
    # Prosanormalisierung in einen anderen Verzeichnisnamen verwandelt werden.
    protected: list[str] = []

    def hold(match: re.Match[str]) -> str:
        protected.append(match.group(0))
        return f"\x00P{len(protected) - 1}\x00"

    text = MACHINE_TOKEN_PATTERN.sub(hold, text)
    # Ein abgeschnittener Altbestand endete vereinzelt unmittelbar nach
    # "Pflichtversto". Die Korrektur muss am Wortende ansetzen: Ein einfacher
    # Teilstringersatz würde auch das bereits richtige "Pflichtverstoß" erneut
    # treffen und bei jedem Generatorlauf ein weiteres scharfes S anhängen.
    text = re.sub(r"\bPflichtversto(?=[\s,.;:)\]!?-]|$)", "Pflichtverstoß", text)
    text = re.sub(r"\bpflichtversto(?=[\s,.;:)\]!?-]|$)", "pflichtverstoß", text)
    text = re.sub(r"\bPflichtverstoßß+", "Pflichtverstoß", text)
    text = re.sub(r"\bpflichtverstoßß+", "pflichtverstoß", text)
    # Zusammengesetzte Transliteration kann sich erst nach einer ersten
    # Ersetzung zeigen, etwa "Haustuergeschaeft" -> "Haustürgeschaeft".
    # Wenige begrenzte Durchläufe normalisieren solche Komposita reproduzierbar.
    for _ in range(3):
        updated = replace_from_trie(text, PROSE_REPLACEMENT_TRIE)
        if updated == text:
            break
        text = updated
    for old, new in TERM_REPLACEMENTS.items():
        if old in text:
            text = re.sub(rf"\b{re.escape(old)}\b", new, text)
    text = re.sub(
        r"\bSGB\s+([ivx]{1,5})\b",
        lambda match: f"SGB {match.group(1).upper()}",
        text,
        flags=re.IGNORECASE,
    )
    for index, value in enumerate(protected):
        text = text.replace(f"\x00P{index}\x00", value)
    return text


DANGLING_EXCERPT_WORDS = {
    "und", "oder", "sowie", "mit", "ohne", "zum", "zur", "zu",
    "der", "die", "das", "des", "dem", "den",
    "ein", "eine", "einer", "eines", "einem", "einen",
    "bei", "nach", "für", "auf", "als", "im", "in", "an", "am",
    "von", "vom", "aus", "über", "unter", "gegen", "je", "pro",
    "statt", "ist", "sind", "wird", "werden", "dessen", "deren",
    "dieser", "diese", "dieses", "liefere", "liefert", "paragraf",
    "paragrafen", "absatz", "artikel", "nummer",
    "seit", "bis", "vor",
}

SENTENCE_BOUNDARY_PATTERN = re.compile(
    r"(?<!\bAbs\.)(?<!\bArt\.)(?<!\bNr\.)(?<!\bS\.)(?<!\bRn\.)"
    r"(?<!\bUrt\.)(?<!\bBeschl\.)(?<=[.!?])\s+"
)
CLAUSE_BOUNDARY_PATTERN = re.compile(
    r"(?<!\bAbs\.)(?<!\bArt\.)(?<!\bNr\.)(?<!\bS\.)(?<!\bRn\.)"
    r"(?<!\bUrt\.)(?<!\bBeschl\.)(?<=[.!?;])\s+"
)


def balance_inline_delimiters(text: str) -> str:
    """Entfernt abgeschnittene Klammerzusätze aus kurzen Exzerpten."""

    for opening, closing in (("(", ")"), ("[", "]")):
        stack: list[int] = []
        unmatched_closing: set[int] = set()
        for index, char in enumerate(text):
            if char == opening:
                stack.append(index)
            elif char == closing:
                if stack:
                    stack.pop()
                else:
                    unmatched_closing.add(index)
        if unmatched_closing:
            text = "".join(
                char for index, char in enumerate(text)
                if index not in unmatched_closing
            )
            stack = []
            for index, char in enumerate(text):
                if char == opening:
                    stack.append(index)
                elif char == closing and stack:
                    stack.pop()
        if stack:
            text = text[: stack[0]].rstrip(" ,.;:-")
    return text


def finish_truncated_excerpt(text: str) -> str:
    text = balance_inline_delimiters(text)
    # Eine vorhandene Satzgrenze ist ein bewusster, vollständiger Abschluss.
    # Funktionswörter wie "ist" oder "sind" dürfen dann nicht als vermeintlich
    # abgeschnittener Ausklang entfernt werden.
    if text.rstrip().endswith((".", "!", "?")):
        return text.rstrip()
    words = text.rstrip().split(" ")
    while len(words) > 1 and words[-1].lower().strip(" ,.;:") in DANGLING_EXCERPT_WORDS:
        words.pop()
    text = " ".join(words).rstrip(" ,.;:-")
    for _ in range(3):
        shortened = re.sub(
            r"\s+\b(?:und|oder|mit|ohne|für|fuer|von|zu|im|in|als|bei|nach|nächstem|naechstem)\b$",
            "",
            text,
            flags=re.IGNORECASE,
        ).rstrip(" ,.;:-")
        if shortened == text:
            break
        text = shortened
    text = re.sub(r"\beine Fristen$", "eine Fristen- und Risikoampel", text)
    return balance_inline_delimiters(text).rstrip(" ,.;:-") + "."


@lru_cache(maxsize=100_000)
def sanitize_core(text: str) -> str:
    paragraph = chr(167)
    # Der Schrägstrich bezeichnet hier eine fachliche Alternative und keinen
    # Dateipfad; die Prosanormalisierung schützt Pfade bewusst vor Umlauten.
    text = text.replace("Verspaetung/Ausfall", "Verspätung/Ausfall")
    text = text.replace(paragraph * 2, "Paragrafen")
    text = text.replace(paragraph, "Paragraf")
    text = re.sub(r"(\d),(\d)", r"\1.\2", text)
    text = text.replace("gruen/gelb/rot", "grün/gelb/rot")
    # Vergleichszeichen aus Fachtexten als Prosa erhalten; erst danach übrige
    # spitze Klammern neutralisieren, damit keine XML-artigen Fragmente bleiben.
    text = re.sub(r"(?<=\s)<\s*(?=\d)", "unter ", text)
    text = re.sub(r"(?<=\s)>\s*(?=\d)", "über ", text)
    text = text.replace("<", "[").replace(">", "]")
    for bad in BAD_WORDS:
        text = re.sub(re.escape(bad), "abrufen", text, flags=re.IGNORECASE)
    for old, new in SENSITIVE_TERM_REPLACEMENTS:
        text = text.replace(old, new)
    text = re.sub(r"\b" + re.escape("K" + "I") + r"\b", "algorithmische Systeme", text)
    text = re.sub(r"\b" + re.escape("A" + "I") + r"\b", "algorithmische Systeme", text)
    text = text.replace("DSGVO", "Datenschutz-Grundverordnung")
    text = text.replace("Aktengeheimnis", "Vertraulichkeit")
    text = text.replace("Co" + "dex, Novellen", "Kaiserkonstitutionen, Novellen")
    # Querverweise aus Skilltexten werden nicht in den eigenständigen Prompt
    # übernommen. Steht der Verweis in Klammern, muss die ganze Klammer weg;
    # andernfalls bliebe nach der Bereinigung ein Fragment wie "Wortsinn (.".
    text = re.sub(
        r"\s*\(\s*siehe Skill [^)\n]*\)",
        "",
        text,
        flags=re.IGNORECASE,
    )
    text = re.sub(r"\bsiehe Skill [^\n.]*", "", text, flags=re.IGNORECASE)
    text = re.sub(r"\b" + re.escape("live " + "verifizieren") + r"\b", "vor Verwendung anhand einer belastbaren Quelle pruefen", text, flags=re.IGNORECASE)
    text = re.sub(r"([!?])\.", r"\1", text)
    text = re.sub(r"\bKonkret zu prüfen:\s*;\s*", "", text, flags=re.IGNORECASE)
    text = re.sub(r"\b(Artikel|Paragraf)\s+-([0-9]+[a-z]?)-", r"\1 \2", text)
    return text


@lru_cache(maxsize=100_000)
def sanitize(text: str) -> str:
    return prose_umlauts(sanitize_core(text))


@lru_cache(maxsize=100_000)
def sanitize_excerpt(text: str) -> str:
    """Bereitet Auswahlmaterial leichtgewichtig vor; Endhärtung folgt im Export."""

    paragraph = chr(167)
    text = text.replace("Verspaetung/Ausfall", "Verspätung/Ausfall")
    text = text.replace(paragraph * 2, "Paragrafen")
    text = text.replace(paragraph, "Paragraf")
    text = re.sub(r"(\d),(\d)", r"\1.\2", text)
    text = text.replace("gruen/gelb/rot", "grün/gelb/rot")
    text = re.sub(r"(?<=\s)<\s*(?=\d)", "unter ", text)
    text = re.sub(r"(?<=\s)>\s*(?=\d)", "über ", text)
    return text.replace("<", "[").replace(">", "]")


@lru_cache(maxsize=100_000)
def clean(text: str, limit: int | None = None) -> str:
    # Aus Skilltext übernommene Auszüge dürfen keine offenen Blockmarken in
    # Tabellenzellen oder Fließtext tragen. Vollständige Codeblöcke werden
    # bereits bei der Exzerptbildung ausgelassen; dies fängt beschädigte oder
    # einzeilige Quellen defensiv ab.
    text = re.sub(r"(?:`{3,}|~{3,})", "", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = re.sub(r"[*_]{1,3}([^*_]+)[*_]{1,3}", r"\1", text)
    # Die Umlaute werden einmal auf der fertigen Promptfassung normalisiert.
    # Zwischenstände bleiben dadurch schnell, während der Export identisch ist.
    text = sanitize_excerpt(text)
    text = re.sub(r"\s+", " ", text).strip()
    text = re.sub(r"\.{2,}", ".", text)
    text = re.sub(r"([!?])\.", r"\1", text)
    text = re.sub(r"\bKonkret zu prüfen:\s*;\s*", "", text, flags=re.IGNORECASE)
    if limit and len(text) > limit:
        cut = text[: limit - 1]
        # Rechtsprechungs- und Normenkernsätze nicht mitten im Gedanken
        # abschneiden. Wenn im nutzbaren hinteren Teil eine Satz- oder
        # Teilsatzgrenze liegt, endet die Kurzfassung dort.
        masked_cut = re.sub(
            r"\b(?:Abs|Nr|Art|S|Rn|Urt|Beschl|Az|D|C|ca|z\.\s*B|u\.\s*a)\.(?=\s|\d)",
            lambda match: match.group(0)[:-1] + "∶",
            cut,
            flags=re.IGNORECASE,
        )
        boundaries = [
            match.start()
            for match in re.finditer(r"[.!?;](?=\s)", masked_cut)
            if match.start() >= max(45, int(limit * 0.35))
        ]
        if boundaries:
            cut = cut[: boundaries[-1] + 1].rstrip()
            if cut.endswith(";"):
                cut = cut[:-1] + "."
            return finish_truncated_excerpt(cut)
        # Nur zurueckschneiden, wenn der Schnitt mitten in einem Wort endet.
        # Endet der Schnitt genau auf einer Wortgrenze (letztes Zeichen oder
        # naechstes Zeichen im Originaltext ist ein Leerzeichen), bleibt das
        # vollstaendige Grenzwort erhalten.
        if cut and not cut[-1].isspace() and not text[len(cut)].isspace():
            if " " in cut:
                cut = cut[: cut.rfind(" ")]
        # Kein haengendes Funktionswort am Satzende ("Risiken und." o. ae.):
        # nachklappernde Konjunktionen, Praepositionen und Artikel abwerfen,
        # damit der gekuerzte Satz auf einem Inhaltswort endet.
        return finish_truncated_excerpt(cut)
    return balance_inline_delimiters(text)


def sentence_terminal(text: str) -> str:
    text = text.strip()
    if not text:
        return text
    if text.endswith((".", "!", "?")):
        return text
    return text.rstrip(" ;:") + "."


def sentence_lead(text: str) -> str:
    """Hebt übernommene Profilfragmente am Satzanfang lesbar an."""

    text = text.strip()
    return text[:1].upper() + text[1:] if text else text


def route_excerpt(text: str, limit: int) -> str:
    """Kürzt Skillmaterial zu einem vollständigen, fachlichen Routensatz."""

    text = clean(text)
    text = re.sub(r"\bi\.\s*V\.\s*m\.\s*", "in Verbindung mit ", text)
    text = re.sub(r"\bD\.\s*(?=\d)", "Digesten ", text)
    text = re.sub(r"\bC\.\s*(?=\d)", "Codex ", text)
    text = re.sub(r"\bConst\.\s*", "Constitutio ", text)
    text = re.sub(r"\bAbs\.\s*", "Absatz ", text)
    text = re.sub(r"\bNr\.\s*", "Nummer ", text)
    text = re.sub(r"\bArt\.\s*", "Artikel ", text)
    text = re.sub(r"\bff\.\s*", "und folgende ", text)
    for source, target in (
        ("Prüft", "Prüfe"),
        ("Erstellt", "Erstelle"),
        ("Analysiert", "Analysiere"),
        ("Ordnet", "Ordne"),
        ("Berechnet", "Berechne"),
        ("Rechnet", "Rechne"),
        ("Liefert", "Liefere"),
        ("Entwickelt", "Entwickle"),
        ("Formuliert", "Formuliere"),
        ("Endfertigt", "Endfertige"),
        ("Bündelt", "Bündele"),
        ("Trennt", "Trenne"),
        ("Sichert", "Sichere"),
        ("Gewichtet", "Gewichte"),
        ("Verdichtet", "Verdichte"),
    ):
        text = re.sub(rf"^{source}\b", target, text, flags=re.IGNORECASE)
        text = re.sub(
            rf"([.;]\s*){source}\b",
            lambda match: match.group(1) + target,
            text,
            flags=re.IGNORECASE,
        )
    text = re.sub(r"^Dieser Skill\b", "Dieser Arbeitsgang", text, flags=re.IGNORECASE)
    text = re.sub(
        r"\s+(?:Methodischer\s+)?Werkstatt-Assistent\b[\s\S]*$",
        "",
        text,
        flags=re.IGNORECASE,
    )
    text = re.sub(
        r"(?<!Absatz)(?<!Artikel)(?<!Paragraf)(?<!Satz)(?<!Nummer)"
        r"\s+\d+\.\s+(?=[A-ZÄÖÜ])[\s\S]*$",
        "",
        text,
    )
    text = re.sub(
        r"Versorgungsausgleich\s+(?:nach\s+)?Paragraf(?:en)?\s+1587(?:\s+bis\s+1587p)?(?:\s+BGB)?",
        "Versorgungsausgleich nach dem VersAusglG",
        text,
        flags=re.IGNORECASE,
    )
    text = re.sub(r"\s+-\s+", "; ", text)
    text = re.sub(r"[.!?]\s*;\s*", "; ", text)
    text = re.sub(r";\s*;", ";", text)
    text = re.sub(r"(?<=[,:;])\s*\d+\.\s+(?=[A-ZÄÖÜ])", " ", text)
    text = re.sub(r"\s+", " ", text).strip(" .;:—-")
    text = balance_inline_delimiters(text).rstrip(" .;:-")
    # Bei gekürzten Listen darf kein bloßer Nummerierungsanfang stehenbleiben.
    text = re.sub(
        r";\s*(?:[^.;]{0,140}:\s*)?\d+\.\s*$",
        "",
        text,
    ).rstrip(" .;:-")
    text = re.sub(
        r"(?<!Absatz)(?<!Artikel)(?<!Paragraf)(?<!Satz)(?<!Nummer)"
        r"\s+\d+\.?\s*$",
        "",
        text,
    ).rstrip(" .;:-")
    if text:
        text = text[0].upper() + text[1:]
    return clean(text, limit).rstrip(" .;:-")


def byte_len(text: str) -> int:
    return len(text.encode("utf-8"))


def clip_utf8(text: str, limit: int) -> str:
    if byte_len(text) <= limit:
        return text
    clipped = text.encode("utf-8")[: max(0, limit - 1)].decode("utf-8", errors="ignore")
    return clipped.rstrip(" \n,;:-") + "\n"


def plugin_dirs() -> list[Path]:
    dirs = []
    for plugin_json in REPO.glob("*/.claude-plugin/plugin.json"):
        dirs.append(plugin_json.parent.parent)
    for plugin_json in (REPO / "_GERICHTE_EXPERIMENTAL").glob("*/.claude-plugin/plugin.json"):
        dirs.append(plugin_json.parent.parent)
    for plugin_json in (REPO / "gerichtsplugins").glob("*/.claude-plugin/plugin.json"):
        dirs.append(plugin_json.parent.parent)
    return sorted(set(dirs), key=lambda p: p.as_posix())


def next_top_level_number(text: str) -> int:
    numbers = []
    for line in text.splitlines():
        match = re.match(r"##\s+(\d+)\.\s+", line)
        if match:
            numbers.append(int(match.group(1)))
    return max(numbers, default=0) + 1


def werkstatt_final_check_block(text: str) -> str:
    number = next_top_level_number(text)
    return f"## {number}. Schlusskontrolle für Tempo\n\n{WERKSTATT_FINAL_CHECK_LINES.rstrip()}\n"


def werkstatt_depth_block(text: str) -> str:
    number = next_top_level_number(text)
    return f"## {number}. Vertiefungsmodus für belastbare Ausgabe\n\n{WERKSTATT_DEPTH_LINES.rstrip()}\n"


def frontmatter_description(text: str) -> str:
    if not text.startswith("---"):
        return ""
    m = re.match(r"---\s*\n([\s\S]*?)\n---", text)
    if not m:
        return ""
    for line in m.group(1).splitlines():
        if line.startswith("description:"):
            return clean(line.split(":", 1)[1].strip().strip('"'), 480)
    return ""


SOURCE_NOISE_BITS = (
    "tragende normen verifizieren",
    "fundstellen über",
    "fundstellen ueber",
    "gesetze-im-internet.de",
    "dejure.org",
    "openjur",
    "keine modellwissen-zitate",
    "bgh-/bverfg-/eugh-datenbank",
    "live prüfen",
    "live pruefen",
)


CURATED_PROFILE_KEYS = {
    "agrar",
    "aktg_hv",
    "design",
    "dokumentenworkflow",
    "ehrenamtliche_richter",
    "gebrauchsmuster",
    "jveg",
    "kanzleibetrieb",
    "kirchenrecht",
    "marke",
    "patent",
    "presse",
    "phishing",
    "pralr",
    "rechtsgeschichte",
    "roemisch",
    "selbststaendige",
    "sport",
    "weg",
}

CURATED_NORM_PROFILE_KEYS = CURATED_PROFILE_KEYS | {
    "technikregulierung",
    "us_insolvency",
}
CURATED_CASE_PROFILE_KEYS = CURATED_PROFILE_KEYS | {
    "betreuung",
    "hoai",
    "technikregulierung",
    "us_insolvency",
}

PROFILE_CASE_SKIP_KEYS = {
    "gesellschaft",
    "verwaltung",
}

CASE_RESEARCH_ONLY_SLUGS = {
    "notariat-alltag",
    "rechtsberatungsstelle",
}

PLUGIN_CASE_OVERRIDES: dict[str, tuple[str, ...]] = {
    "agb-recht-pruefer": (
        "BGH, Urteil vom 29.07.2021 - III ZR 192/20: Die Inhaltskontrolle nach BGB Paragraf 307 Absatz 1 Satz 1 verlangt eine umfassende Abwägung der wechselseitigen Interessen unter Berücksichtigung von Gegenstand, Zweck und Eigenart des Vertrags.",
        "BGH, Urteil vom 07.04.2022 - I ZR 212/20: Im Unterlassungsverfahren nach UKlaG sind Klauseln getrennt nach Regelungsgehalt zu prüfen; der Senat beanstandete unter anderem Kosten-, Schadensersatz- und Haftungsausschlüsse in Paketbeförderungsbedingungen.",
        "BGH, Urteil vom 19.01.2023 - VII ZR 34/20: Weicht eine Klausel von wesentlichen Grundgedanken des dispositiven Rechts ab, spricht BGB Paragraf 307 Absatz 2 Nummer 1 für eine unangemessene Benachteiligung; Vertragszweck und Risikozuweisung bleiben konkret zu würdigen.",
    ),
}


PROFILE_FIELD_OVERRIDES: dict[str, tuple[tuple[str, str], ...]] = {
    "roemisch": (
        ("Quellenstufe und Überlieferung", "Zwölftafelrekonstruktion, Juristenfragment, Inschrift, Papyri, Gaius und justinianische Kompilation nach Textzeuge, Edition, Sprache und Unsicherheit unterscheiden"),
        ("Personenstatus und Hausverband", "status libertatis, civitatis und familiae, patria potestas, manus, peculium, tutela und cura epochenbezogen ordnen"),
        ("Aktionenrecht und Prozessform", "actio, exceptio, Formelbestandteile, Legisaktion, Formularprozess und cognitio extra ordinem als Teil der Falllösung rekonstruieren"),
        ("Besitz, Eigentum und Ersitzung", "possessio, detentio, dominium, bonitarische Position, Erwerbsakt, iusta causa, bona fides, tempus und prätorischen Schutz trennen"),
        ("Vertrag und Obligation", "Stipulation, Real- und Konsensualvertrag, Leistung, Gefahr, Haftungsmaßstab, bona fides, Klage und Einrede aus dem historischen Typ ableiten"),
        ("Delikt und Schadenszurechnung", "furtum, rapina, iniuria und lex Aquilia nach Tatbestand, actio, Pönalität, Kausalität, Bewertung und Noxalfolge einordnen"),
        ("Familie und Erbfolge", "Ehestatus, Hausgewalt, Vermögenszuordnung, testamentum, heredis institutio, Legat, Fideikommiss und bonorum possessio nach Epoche prüfen"),
        ("Handels-, See- und Sicherungsgeschäfte", "institor, magister navis, lex Rhodia, receptum, fenus nauticum, pignus, hypotheca und fideiussio mit Quellen- und Prozessbezug untersuchen"),
        ("Rezeption und Gegenwartsvergleich", "antiken Ausgangstext, justinianische Fassung, ius commune, usus modernus, Pandektistik und heutige Anschlussfrage als getrennte Stufen belegen"),
    ),
    "pralr": (
        ("Textzeuge, Stichtag und Geltung", "Ausgabe, Druck, Seitenbild, Teil, Titel, Abschnitt, Paragraf, OCR-Abweichung, Ort, Provinz, Personenstand und zeitlichen Geltungsbereich sichern"),
        ("Person, Stand und Handlungsfähigkeit", "historische Statusordnung, Alter, Geschlecht, Hausverband, Vormundschaft und öffentlich-rechtliche Bindung quellenbezogen und ohne Beschönigung darstellen"),
        ("Besitz, Eigentum und Nachbarordnung", "Gewahrsam, Besitz, Eigentum, Erwerbsart, Grundstück, Grenze, Dienstbarkeit, Kataster, Hypothekenbuch und örtliche Observanz verbinden"),
        ("Vertrag und Leistungsstörung", "Vertragstyp, Fähigkeit, Erklärung, Form, Auslegung, Leistung, Gefahr, Gewährleistung und Beendigung aus dem einschlägigen Titel ableiten"),
        ("Schaden und besondere Haftung", "verletztes Recht, Handlung, Verschulden, Kausalität, Zufall, Mitverursachung, Sonderregel und Ersatzumfang nach Originalfundstelle prüfen"),
        ("Ehe, Familie und Vormundschaft", "Eheschließung, Konfession, Vermögensordnung, Gewaltverhältnis, Unterhalt, Trennung, Vormundschaft und Behördenaufsicht stichtagsbezogen ordnen"),
        ("Erbfolge und Verfügung von Todes wegen", "gesetzliche Folge, Testament, Form, Fähigkeit, Erbeinsetzung, Vermächtnis, Pflichtteilsschutz, Verwaltung und Haftung prüfen"),
        ("Staats-, Polizei- und Strafordnung", "Obrigkeit, Zuständigkeit, historischer Polizeibegriff, Ordnungszweck, Eingriffsmittel, Sanktion und damaligen Rechtsschutz rekonstruieren"),
        ("Ablösung und Rezeption", "PrALR-Regel, spätere Änderung, Reichsrecht, Einführung des BGB, fortwirkende Figur und heutige Vergleichsnorm methodisch getrennt darstellen"),
    ),
    "presse": (
        ("Entscheidungsmeldung", "Tenor, tragende Gründe, praktische Folge, Rechtsmittelstatus und belastbare Fundstelle in eine veröffentlichungsfähige Meldung überführen"),
        ("Verdachtsberichterstattung", "Beweistatsachen, Stellungnahmeanfrage, Statussprache, öffentliches Interesse und Identifizierbarkeit vor Veröffentlichung abgleichen"),
        ("Gerichts- und Sitzungsbericht", "Anträge, Beweisaufnahme, Zitate, vorläufige Einschätzungen und nächsten Termin ohne Schuldvorwegnahme einordnen"),
        ("Bild, Name und Anonymisierung", "KUG, Privatheit, Prangerwirkung, Wiedererkennbarkeit und Informationswert in Text, Überschrift und Bild konsistent abwägen"),
        ("Interview und Stellungnahme", "konkrete Fragen, angemessene Antwortfrist, Antwortauswertung und dokumentierten Veröffentlichungsentscheid vorbereiten"),
        ("Korrektur und Nachtrag", "Unwahrheit, ausgeräumten Verdacht, Gegendarstellung, Richtigstellung, Nachtrag und Reichweitenfolge getrennt prüfen"),
    ),
    "agrar": (
        ("Landpacht", "Vertrag, Textform und Übergangsrecht, Anzeige, Pachtanpassung, Kündigung, Flächenübergabe und Landwirtschaftsgericht anhand der Vertragsakte prüfen"),
        ("Hofnachfolge", "Hofstatus, Grundsteuerwert, Hoferbenberechtigung, Abfindung, Nachabfindung und Übergangsrecht in einer Stichtagsmatrix verbinden"),
        ("Landwirtschaftlicher Grundstücksverkehr", "Genehmigungspflicht, Versagungsgrund, leistungsfähigen Landwirt, Kaufpreis und gerichtlichen Antrag belegen"),
        ("GAP und Direktzahlungen", "Förderjahr, Fläche, Konditionalität, Kontrolle, Kürzung, Rückforderung und Rechtsbehelf zeilenweise nachweisen"),
        ("Betriebsbezogene Fachaufsicht", "Tierhaltung, Düngung, Pflanzenschutz, Natur-, Immissions- und Forstrecht dem konkreten Betriebsvorgang zuordnen"),
        ("Vertrag, Antrag und Widerspruch", "Adressat, Frist, Tatbestand, Beleg, Gegenposition und vollzugsfähigen Antrag zu einem versandfertigen Produkt verdichten"),
    ),
    "sport": (
        ("Verbandsentscheidung", "Regelwerkfassung, Zustellung, internes Rechtsmittel, Gleichbehandlung, Verhältnismäßigkeit und Eilbedarf prüfen"),
        ("Dopingverfahren", "Probe, Kette des Gewahrsams, Substanz, Verschuldensgrad, Sanktion, Rechtsmittel und Wettkampfkalender verbinden"),
        ("Athleten- und Trainervertrag", "Befristung, Vergütung, Einsatz, Verletzung, Bildrechte, Freistellung und Beendigung redlinen"),
        ("Transfer und Spielberechtigung", "Registrierung, Transferfenster, Ausbildungsentschädigung, Freizügigkeit und vorläufige Teilnahme klären"),
        ("Schiedsverfahren und Eilrechtsschutz", "Schiedsklausel, interne Ausschöpfung, Frist, Panel, Öffentlichkeit, Antrag und Aufhebungskontrolle planen"),
        ("Sponsoring und Vermarktung", "Exklusivität, Moralklausel, Kennzeichnung, Verbandsrechte, Leistungsstörung und Exit-Szenario verhandeln"),
    ),
    "jveg": (
        ("Ausschlussfrist", "Heranziehung und tätigkeitsabhängigen Beginn der dreimonatigen Frist mit Eingangs- und Abschlussnachweisen bestimmen"),
        ("Zeit und Honorargruppe", "Auftrag, Beweisfragen, Tätigkeitsprotokoll, Fachkunde, Zeitansatz und gesetzliche Honorargruppe plausibilisieren"),
        ("Besondere Vergütung", "Einverständnis, gerichtliche Zustimmung und ausreichende Einzahlung nach JVEG Paragraf 13 getrennt prüfen"),
        ("Fahrt und sonstige Aufwendungen", "Erforderlichkeit, Strecke, Abwesenheit, Beleg, Pauschale, Hilfskraft, Kopie und Umsatzsteuer einzeln berechnen"),
        ("Zeugen und ehrenamtliche Richter", "Zeitversäumnis, Haushalt, Verdienstausfall, Höchstbetrag und Nachweis nach Berechtigtenrolle zuordnen"),
        ("Festsetzung und Beschwerde", "bezifferten Antrag, Zuständigkeit, Kürzungspunkt, Beschwerdewert, Zulassung und Einreichungsweg aufbauen"),
    ),
    "ehrenamtliche_richter": (
        ("Rolle und Besetzung", "Spruchkörper, Heranziehung, gleiches Stimmrecht, gesetzlichen Richter und rollenbezogene Verfahrensnormen bestimmen"),
        ("Neutralität und Selbstanzeige", "persönlichen oder sachlichen Vorbezug ohne eigene Vorentscheidung unverzüglich gegenüber dem Vorsitz offenlegen"),
        ("Beweisaufnahme und Fragerecht", "offene Tatsachenfrage, Wahrnehmungsgrundlage, Widerspruch, Dolmetscher- oder Gutachterpunkt sitzungsbezogen notieren"),
        ("Beratung und Mehrheit", "Schuld-, Rechtsfolgen- und Nebenfrage trennen, gesetzliche Mehrheit bestimmen und abweichende Sicht sachlich einbringen"),
        ("Teilnahmefähigkeit", "Müdigkeit, Hören, Sprache, Verständnis oder Unterbrechungsbedarf sofort anzeigen und verfahrensfest behandeln"),
        ("Beratungsgeheimnis und Medien", "Hauptverhandlungsöffentlichkeit, nichtöffentliche Beratung, Aktenwissen, Eigenrecherche und Medienkontakt strikt trennen"),
    ),
    "rechtsgeschichte": (
        ("Quellenkritik", "Textzeuge, Ausgabe, Fassung, Sprache, Übersetzung, Datum und Rechtsraum vor jeder Aussage sichern"),
        ("Norm und Anwendungspraxis", "historischen Tatbestand, Rechtsfolge, Institution und tatsächliche Durchsetzung aus getrennten Quellen rekonstruieren"),
        ("Privatrechtsgeschichte", "Eigentum, Vertrag, Delikt, Familie und Erbe entlang der maßgeblichen Kodifikations- und Rezeptionsstufen vergleichen"),
        ("Verfassungs- und Verwaltungsgeschichte", "Institution, Kompetenz, Herrschaftspraxis, Rechtsbruch und Kontinuität ohne heutige Rückprojektion untersuchen"),
        ("Rechtsüberleitung", "Fortgeltung, Aufhebung, intertemporales Recht und Überleitungsnorm mit Verkündung und Stichtag belegen"),
        ("Historische Fallanalyse", "zeitgenössischen Maßstab, Gegenquelle, damalige Rechtsfolge und heutige Anschlussfrage sichtbar trennen"),
    ),
    "kirchenrecht": (
        ("Zuständigkeit und Rechtsquelle", "Autorität, Gericht, universales Recht, Partikularrecht, Dekret, Statut und maßgebliche Fassung bestimmen"),
        ("Kirchliches Verwaltungsverfahren", "Antrag, Anhörung, Dekret, Zustellung, hierarchische Beschwerde, Frist und Vollzug chronologisch ordnen"),
        ("Eheverfahren", "Zuständigkeit, Klagegrund, Parteistellung, Urkunden, Zeugen, Ehebandverteidiger und Rechtsmittel erfassen"),
        ("Kirchliches Strafverfahren", "Voruntersuchung, Schutzmaßnahmen, Zuständigkeit, Verteidigung, Beweis, Dekret oder Gerichtsweg trennen"),
        ("Register und Urkunden", "Taufe, Ehe, Austritt, Korrektur, Archiv, Ausfertigung und Offenlegung nach Beweiszweck bearbeiten"),
        ("Staatliche Schnittstelle", "kirchliche Wirkung, Arbeitsrecht, Personenstand, Datenschutz und staatlichen Rechtsschutz gesondert prüfen"),
    ),
    "kanzleibetrieb": (
        ("Mandatsannahme", "Beteiligte, Gegner, Interessenkontrolle, Identität, Umfang, Vollmacht, Vergütung und Annahmebestätigung sichern"),
        ("Fristenkontrolle", "Auslöser, Bekanntgabe, Kalenderberechnung, Eintrag, Gegenkontrolle, Verantwortlicher und Vertretung dokumentieren"),
        ("Bearbeitung und Freigabe", "Arbeitsauftrag, Aktenstand, offene Entscheidung, Vieraugenkontrolle, Budget und Freigabefassung führen"),
        ("Elektronischer Versand", "Empfänger, Dateiformat, Signatur, Anlagen, Übermittlungsweg, Eingangsbestätigung und Fehlerreaktion prüfen"),
        ("Abrechnung und Fremdgeld", "Gebührentatbestand, Gegenstandswert, Vereinbarung, Vorschuss, Fremdgeld, Rechnung und Zahlungslauf abstimmen"),
        ("Mandatsabschluss", "Ergebnis, Restfristen, Vollstreckung, Rückgabe, Aufbewahrung, Schlussrechnung und Wiedervorlage festhalten"),
    ),
    "selbststaendige": (
        ("Status und Anmeldung", "Vertragswirklichkeit, Weisung, Eingliederung, Unternehmerrisiko, Statusverfahren und erforderliche Anzeigen prüfen"),
        ("Angebot und Auftrag", "Leistung, Ergebnis, Mitwirkung, Termin, Preis, Abnahme, Nutzungsrechte und Haftung verständlich vereinbaren"),
        ("Rechnung und Steuern", "Pflichtangaben, Umsatzsteuerstatus, Fälligkeit, Ausgabe, Beleg, Abgabe und Rücklage ordnen"),
        ("Zahlungsausfall", "Leistungsnachweis, Fälligkeit, Verzug, Mahnung, Einwendung, Mahn- oder Klageweg und Vollstreckbarkeit bestimmen"),
        ("Versicherung und Haftung", "Tätigkeitsrisiko, Deckung, Ausschluss, Schadenanzeige, Selbstbehalt und Haftungsbegrenzung abgleichen"),
        ("Liquidität und Krise", "offene Forderungen, Abgaben, fixe Kosten, Reserve, Fortführungsentscheidung und nächsten sicheren Schritt berechnen"),
    ),
    "dokumentenworkflow": (
        ("Inventur und Version", "Datei, Typ, Datum, Autor, Fassung, Signatur, Dublette, Lesbarkeit und maßgeblichen Stand erfassen"),
        ("Fundstellenlinie", "jede Aussage, Zahl, Klausel und Frist auf Dokument, Seite, Absatz, Zelle oder Nachricht zurückführen"),
        ("Vergleich und Redline", "Einfügung, Streichung, Widerspruch, fehlende Anlage, Rechenabweichung und materielle Auswirkung markieren"),
        ("Tabellen- und Rechenprüfung", "Formel, Einheit, Bezugszelle, Rundung, Summenprobe, Filter und Exportverlust kontrollieren"),
        ("Entwurf und Format", "Zielgruppe, Dokumenttyp, Gliederung, Form, Signatur, Anlagen und Einreichungskanal vor Ausgabe festlegen"),
        ("Übergabe und Nachweis", "Ergebnisdatei, Quellen, offene Lücke, Prüfschritt, Dateiname, Freigabestatus und nächste Handlung protokollieren"),
    ),
}


def is_source_noise(line: str) -> bool:
    lowered = line.lower()
    return any(bit in lowered for bit in SOURCE_NOISE_BITS)


def skill_body_excerpt(text: str) -> str:
    body = re.sub(r"^---\s*\n[\s\S]*?\n---\s*", "", text).strip()
    buckets: list[list[str]] = [[], [], []]
    section_priority = 1
    fence_marker: str | None = None
    for raw in body.splitlines():
        line = raw.strip()
        fence = re.match(r"^(`{3,}|~{3,})", line)
        if fence:
            marker = fence.group(1)[0]
            if fence_marker is None:
                fence_marker = marker
            elif fence_marker == marker:
                fence_marker = None
            continue
        if fence_marker is not None:
            continue
        if not line:
            continue
        if line.startswith("#"):
            heading = re.sub(r"^#+\s*", "", line).strip().lower()
            generic_heading_bits = (
                "arbeitsweg", "rolle", "zweck", "rechtsrahmen",
                "pflichtschritte", "output", "normenanker", "rechtsquellen",
                "quellen", "benachbarte skills", "powersprint", "qualität",
                "stop-kriterium", "frontmatter",
            )
            section_priority = 2 if any(
                bit in heading for bit in generic_heading_bits
            ) else 0
            continue
        if line.startswith("|") or line.startswith("<!--"):
            continue
        lowered = line.lower()
        if (
            "rolle, ziel und gewünschtes arbeitsprodukt" in lowered
            or "vor einer rechtlichen schlussfolgerung" in lowered
            or "fristen und eilrisiken zuerst markieren" in lowered
            or "nur die fristen des konkreten rechtsgebiets" in lowered
            or "frage zu beginn nur" in lowered
            or "normen-/quellenanker" in lowered
            or "stichwort für die auswahl" in lowered
            or "stichwort fuer die auswahl" in lowered
            or lowered.startswith("fokus:")
            or lowered.startswith("output:")
            or "dieser skill erklärt" in lowered
            or "dieser skill erklaert" in lowered
            or "dieser skill vertieft" in lowered
            or "im allgemeinen bundesland-skill" in lowered
            or "nur kurz angerissen" in lowered
            or is_source_noise(line)
        ):
            continue
        buckets[section_priority].append(line)
    ordered: list[str] = []
    for bucket in buckets:
        for line in bucket:
            ordered.append(line)
            if len(" ".join(ordered)) > 1100:
                return clean(" ".join(ordered), 900)
    return clean(" ".join(ordered), 900)


META_SKILL_BITS = (
    "60-sekunden",
    "abschlussmemo",
    "allgemeiner-einstieg",
    "anfaenger-modus",
    "anpassen",
    "anschluss-routing",
    "automatischer-aktualisierer",
    "automation",
    "billing-narrative",
    "copilot",
    "cowork",
    "dashboard",
    "deaktivieren",
    "design-und-ausgabe",
    "dokumente-intake",
    "einstieg-routing",
    "erstgespraech",
    "erstpruefung",
    "intake",
    "kaltstart",
    "kommandocenter",
    "livecheck",
    "look-and-feel",
    "mandat-triage",
    "mandat-arbeitsbereich",
    "mandat-aktualisierung",
    "mandat-aufnahme",
    "mandat-schliessen",
    "mandatsakte-kontexttrennung",
    "orientierung",
    "output-",
    "output-waehlen",
    "qualitygate",
    "qualitaetskontrolle",
    "qualitätskontrolle",
    "quellenkarte",
    "praxisprofil",
    "simulation",
    "staffing",
    "red-team",
    "rechtsquellen-fehlerkatalog",
    "routing",
    "first-year",
    "halluzinations",
    "laienhilfe",
    "livequellen",
    "unterlagen-luecken",
    "verzeichnis-durchsuchen",
    "verwandte-skills",
    "workflow-",
)


def skill_directory_priority(path: Path) -> tuple[int, int, str]:
    """Bevorzugt Fachskills, ohne Meta- und Routing-Skills zu verwerfen."""

    slug = path.name
    meta_hits = sum(bit in slug for bit in META_SKILL_BITS)
    legal_signal = 0 if re.search(
        r"(?:paragraf|artikel|vertrag|klage|beschwerde|bescheid|haftung|"
        r"beweis|frist|abstimmung|pacht|doping|verguetung|entschaedigung)",
        slug,
    ) else 1
    return (meta_hits, legal_signal, slug)


def collect_skill_material(plugin_dir: Path) -> list[dict[str, str]]:
    items = []
    skill_dirs = [
        sd
        for sd in (plugin_dir / "skills").glob("*")
        if sd.is_dir() and sd.name != "juristischer-argumentationskern"
    ]
    # Mehr Material lesen, damit auch umfangreiche Plugins nicht nur von den
    # alphabetisch ersten Fachthemen geprägt werden. Die spätere Auswahl
    # begrenzt Wiederholungen und verwirft Routing- oder Schablonentexte.
    for sd in sorted(skill_dirs, key=skill_directory_priority)[:80]:
        slug = sd.name
        skill_file = sd / "SKILL.md"
        desc = slug.replace("-", " ")
        body = ""
        if skill_file.exists():
            try:
                chunk_lines: list[str] = []
                with skill_file.open("r", encoding="utf-8", errors="ignore") as handle:
                    for line_no, line in enumerate(handle, 1):
                        chunk_lines.append(line)
                        if line_no >= 180:
                            break
                text = "".join(chunk_lines)
                desc = frontmatter_description(text) or desc
                body = skill_body_excerpt(text)
                heading = ""
                for raw_heading in text.splitlines():
                    if raw_heading.startswith("# "):
                        heading = clean(raw_heading[2:].strip(), 140)
                        break
            except OSError:
                text = ""
                body = ""
                heading = ""
        else:
            heading = ""
        items.append({"slug": slug, "desc": desc, "body": body, "raw": text if skill_file.exists() else "", "heading": heading})
    return items


ROUTE_TITLE_REPLACEMENTS = {
    "annahmefrist leistungsfrist 308": "Annahme- und Leistungsfristen nach Paragraf 308 BGB",
    "beweislast und zugang 309": "Beweislast, Zugang und Klauselverbote nach Paragraf 309 BGB",
    "fachanwalt miet wohnungseigentumsrecht weg anfechtungsklage 44": "Beschlussanfechtung nach Paragraf 44 WEG",
    "wohnungseigentum beschluss paragraf 23 weg": "Beschlussfassung nach Paragraf 23 WEG",
    "einführung vertragstypen mietrecht": "Wohnraum-, Gewerberaum- und Mischmiete abgrenzen",
    "betriebsrat anhörung kündigung 102": "Betriebsratsanhörung vor Kündigung nach Paragraf 102 BetrVG",
    "litigation readiness 411 und 412": "Klagevoraussetzungen nach Sections 411 und 412",
    "art 21 und art 22 vermögen trennen": "Vermögenszuordnung nach Artikel 21 und 22 Einigungsvertrag",
    "außenwirtschaft beweis rügen": "Beweisrügen im außenwirtschaftsrechtlichen Bußgeldverfahren",
    "anti dumping zoll eu grundverordnung": "Antidumpingzoll nach der EU-Grundverordnung",
    "tdm 44b urhg ki training opt out": "Text- und Data-Mining nach Paragraf 44b UrhG und Nutzungsvorbehalt",
}


def polish_route_title(title: str) -> str:
    title = prose_umlauts(title).strip()
    title = re.sub(r"^EV-Vollzug\s+\d{3}:\s*", "", title, flags=re.IGNORECASE)
    title = re.sub(r"^Verl-\d{3}\s*·\s*", "", title, flags=re.IGNORECASE)
    title = re.sub(r"^\d{3}\s+", "", title)
    title = re.sub(r"^Spezial:\s*", "", title, flags=re.IGNORECASE)
    title = re.sub(r"\bParagrafen\s+(\d+)\s+ff\.?$", r"Paragrafen \1 ff.", title, flags=re.IGNORECASE)
    title = re.sub(r"\bParagraf\s+(\d+)\s+Ff\.?$", r"Paragraf \1 ff.", title)
    title = ROUTE_TITLE_REPLACEMENTS.get(title.lower(), title)
    title = re.sub(r"\bGwb\b", "GWB", title)
    title = re.sub(r"\bOwig\b", "OWiG", title)
    title = re.sub(r"\bCisg\b", "CISG", title)
    title = re.sub(r"\bUrhg\b", "UrhG", title)
    title = re.sub(r"\bEu\b", "EU", title)
    title = re.sub(r"\bDpma\b", "DPMA", title)
    title = re.sub(r"\bEuipo\b", "EUIPO", title)
    title = re.sub(r"\bWipo\b", "WIPO", title)
    title = re.sub(r"\bTdm\b", "TDM", title)
    title = re.sub(
        r"\b(Prüfen|Bewerten|Anfechten|Erstellen)$",
        lambda match: match.group(1).lower(),
        title,
    )
    return clean(title, 90).rstrip(" .;:-")


def field_title(desc: str, slug: str, heading: str = "") -> str:
    desc = clean(desc, 240)
    if heading and len(heading) >= 6:
        title = re.sub(r"^\d+(?:\.\d+)*\.?\s+", "", heading).strip()
        if len(title) > 90:
            concise = re.split(r"[:;.]", title, maxsplit=1)[0].strip()
            title = concise if 8 <= len(concise) <= 90 else slug.replace("-", " ").title()
    elif match := re.match(
        r"Für (.+?): (?:routet Rolle|erstellt Entwurf|prüft Ergebnis|prüft Frist|ordnet Akte|rechnet Beträge|entwickelt Ziel|ordnet Norm)",
        desc,
    ):
        title = match.group(1)
    elif match := re.match(r"Wenn es um (.+?) in [^:;.]{3,90} geht:", desc):
        title = match.group(1)
    else:
        safe = desc.replace("Art. ", "Art ").replace("Abs. ", "Abs ")
        title = re.split(r"[:;.] ", safe, maxsplit=1)[0]
        title = title.replace("Art ", "Art. ").replace("Abs ", "Abs. ")
    title = title.strip(" -;:.")
    if not title or len(title) < 8:
        title = slug.replace("-", " ").title()
    title = clean(title, 90).rstrip(" .;:-")
    for particle in ("Und", "Oder", "Mit", "Nach", "Von", "Zu", "Im", "In", "Bei", "Für"):
        title = re.sub(rf"(?<!^)\b{particle}\b", particle.lower(), title)
    return polish_route_title(title)


GENERIC_FIELD_BITS = (
    "erstellt den passenden Entwurf",
    "prüft Frist, Form, Zuständigkeit",
    "ordnet Sachverhalt, Norm, Beweislast",
    "liefert eine Fristen- und Risikoampel",
    "liefert einen verwertbaren Entwurf",
    "Fristen und Eilrisiken zuerst markieren",
    "nur die Fristen des konkreten Rechtsgebiets",
    "Frage zu Beginn nur",
    "Normen-/Quellenanker",
    "Normenradar:",
    "Vor einer rechtlichen Schlussfolgerung",
    "Dieser Skill erklärt",
    "Dieser Skill erklaert",
    "Dieser Skill vertieft",
    "im allgemeinen Bundesland-Skill",
    "nur kurz angerissen",
    "Tragende Normen verifizieren",
    "Fundstellen über",
    "keine Modellwissen-Zitate",
    "live prüfen",
    "Problemfokus dieses Skills",
    "Bleibe beim konkreten Titel",
    "Tatsachen, Frist, Norm, Beweislast",
    "von der ersten Aktenordnung bis zur belastbaren Empfehlung",
    "ordnet Akteninhalt, Belege, Lücken und Nachforderungen",
    "zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast",
    "entwickelt Verhandlungsziel, Vergleichskorridor",
    "rechnet Schwellen, Beträge, Varianten",
    "direkt nutzbares Arbeitsprodukt mit Prüfpunkten",
    "Schnittstellenkarte mit Kollisions-",
    "Dokumentenmatrix mit Nachforderungsliste",
    "Einreichungsplan mit Form-, Portal- und Nachweischeck",
    "Verhandlungs- oder Eskalationslinie mit Optionen",
    "Berechnungstabelle mit Schwellen, Annahmen und Kontrollfragen",
    "Beweislast- und Substantiierungsmatrix",
    "Auswahlstichwort:",
    "routet Rolle, Frist, Unterlagen und Fachschritt",
    "erstellt Entwurf mit Antrag, Beweis und Anlagen",
    "prüft Ergebnis, Beweislast und Gegenposition",
    "prüft Frist, Form, Zuständigkeit und Eilbedarf",
    "ordnet Akte, Belege und Lücken",
    "rechnet Beträge, Schwellen und Varianten",
    "entwickelt Ziel, Vergleich und Eskalation",
    "ordnet Norm, Beweislast und Gegenargument",
    "Prüfprodukt mit Risiko und nächstem Schritt",
)


def field_detail(desc: str, body: str = "", title: str = "") -> str:
    desc = clean(desc, 260)
    desc = re.sub(
        r"^Für .+?:\s*(?=(?:routet Rolle|erstellt Entwurf|prüft Ergebnis|prüft Frist|ordnet Akte|rechnet Beträge|entwickelt Ziel|ordnet Norm))",
        "",
        desc,
    )
    desc = re.sub(r"^Wenn es um .+? geht:\s*", "", desc)
    desc = re.sub(r"\s*Stichwort für die Auswahl:.*$", "", desc)
    desc = desc.strip(" .;:")
    desc = desc.rstrip(" -")
    generic = not desc or any(bit.lower() in desc.lower() for bit in GENERIC_FIELD_BITS)
    if generic and body:
        body = clean(body, 280)
        body = re.sub(r"^Wenn es um .+? geht:\s*", "", body)
        body = re.sub(r"\s*Stichwort für die Auswahl:.*$", "", body)
        body = body.lstrip("- ").strip()
        body_lower = body.lower()
        if (
            len(body) > 45
            and "rolle, ziel und gewünschtes arbeitsprodukt" not in body_lower
            and "vor einer rechtlichen schlussfolgerung" not in body_lower
            and "fristen und eilrisiken zuerst markieren" not in body_lower
            and "nur die fristen des konkreten rechtsgebiets" not in body_lower
            and "frage zu beginn nur" not in body_lower
            and "normen-/quellenanker" not in body_lower
            and "stichwort für die auswahl" not in body_lower
            and "stichwort fuer die auswahl" not in body_lower
            and not any(bit.lower() in body_lower for bit in GENERIC_FIELD_BITS)
            and "problemfokus dieses skills" not in body_lower
            and "bleibe beim konkreten titel" not in body_lower
            and "normenradar:" not in body_lower
            and "von der ersten aktenordnung bis zur belastbaren empfehlung" not in body_lower
            and not is_source_noise(body)
        ):
            desc = body.strip(" .;:")
            generic = False
    if generic:
        basis = title or "dieses Feld"
        return f"{basis}: Tatsachen, Frist, Norm, Beweislast, stärkstes Gegenargument und nächstes Dokument in einer Arbeitslinie verbinden"
    return desc


ROUTE_FRAGMENT_END = re.compile(
    r"\b(?:Abs|Art|lit|Anh|vom|seit|dann|erzeugt|bewertet|aktive|"
    r"verwertbarer|technisch|Grundbuch|unbefristetes|Beweisangebot)\.?$",
    flags=re.IGNORECASE,
)


def tailored_skill_detail(item: dict[str, str], title: str, limit: int = 540) -> str:
    """Wählt vollständige Fachsätze statt des allgemeinen Skill-Vorspanns."""

    source = item.get("body", "")
    if not source:
        return ""
    source = source.replace(" - ", ". ")
    title_tokens = {
        token for token in re.findall(r"[a-zäöüß]{5,}", title.lower())
        if token not in {"recht", "prüfung", "praxis", "erstellen", "bearbeiten"}
    }
    ranked: list[tuple[int, int, str]] = []
    for index, raw in enumerate(SENTENCE_BOUNDARY_PATTERN.split(source)):
        candidate = clean(raw).strip(" -;:")
        candidate = re.sub(r"^\d+(?:\.\d+)*\.?\s+", "", candidate)
        candidate = re.sub(
            r"^(?:Entscheidende Weiche|Normen-/Quellenanker|Arbeitsprodukt|Kernfrage):\s*",
            "",
            candidate,
            flags=re.IGNORECASE,
        )
        if len(candidate) < 45 or len(candidate) > 500:
            continue
        lowered = candidate.lower()
        if is_source_noise(candidate) or any(
            bit.lower() in lowered for bit in GENERIC_FIELD_BITS
        ):
            continue
        if any(bit in lowered for bit in PRACTICE_ROUTE_NOISE):
            continue
        if (
            any(marker in candidate for marker in COURT_MARKERS)
            or "BVerfGE" in candidate
            or "BAGE" in candidate
            or "PBvU" in candidate
            or case_id_set(candidate)
        ):
            continue
        if lowered.startswith(
            "bestimme dealphase, fondsrolle, target-risiko, finanzierungsstruktur"
        ):
            continue
        if ROUTE_FRAGMENT_END.search(candidate):
            continue
        tokens = set(re.findall(r"[a-zäöüß]{5,}", lowered))
        score = 2 * len(tokens & title_tokens)
        score += 3 * len(re.findall(
            r"\b(?:Paragraf|Artikel|can\.|[A-ZÄÖÜ][A-Za-zÄÖÜäöüß]{1,12}G)\b",
            candidate,
        ))
        if re.match(
            r"^(?:Prüfe|Bestimme|Ordne|Trenne|Gleiche|Baue|Erfasse|Sichere|"
            r"Berechne|Formuliere|Rekonstruiere|Verdichte|Der Skill)",
            candidate,
            flags=re.IGNORECASE,
        ):
            score += 3
        if re.search(r"\b\d+(?:\.\d+)?\b", candidate):
            score += 1
        ranked.append((score, index, candidate))
    if not ranked:
        return ""
    chosen = sorted(sorted(ranked, reverse=True)[:3], key=lambda row: row[1])
    parts: list[str] = []
    size = 0
    for _score, _index, candidate in chosen:
        sentence = sentence_terminal(candidate)
        if parts and size + 1 + len(sentence) > limit:
            continue
        parts.append(sentence)
        size += len(sentence) + 1
    return " ".join(parts).rstrip(" .")


def manifest(plugin_dir: Path) -> dict:
    return json.loads((plugin_dir / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))


COURT_MARKERS = (
    "BGH", "BAG", "BVerfG", "BVerwG", "BSG", "BFH", "EuGH", "BPatG",
    "OLG", "LG ", "AG ", "LAG", "ArbG", "SG ", "LSG", "BVerfGE", "BAGE", "NJW", "NZA", "ZIP",
)

LAW_MARKERS = (
    "BGB", "ZPO", "StPO", "StGB", "GG", "InsO", "StaRUG", "VwGO", "FGO",
    "SGG", "ArbGG", "FamFG", "HGB", "GmbHG", "AktG", "UmwG", "MarkenG",
    "UrhG", "DesignG", "PatG", "VVG", "VwVfG", "SGB", "AO", "EStG",
    "UStG", "KStG", "KSchG", "TzBfG", "BetrVG", "BetrAVG", "BDSG",
    "AEUV", "EUV", "EMRK", "GRCh", "DSGVO", "VOB/B", "HOAI", "BRAO",
    "BNotO", "RVG", "RDG", "GWB", "VgV", "UVgO", "ZVG", "GVG",
    "KWG", "WpHG", "WpIG", "ZAG", "GwG", "LobbyRG", "BSIG",
    "ProdHaftG", "ProdSG", "GPSR", "DORA",
)


def relevant_lines(skill_material: list[dict[str, str]], limit: int = 450) -> list[str]:
    lines: list[str] = []
    for item in skill_material:
        raw = "\n".join([item.get("desc", ""), item.get("body", ""), item.get("raw", "")])
        for raw_line in raw.splitlines():
            line = raw_line.strip(" -\t")
            if not line or line.startswith("|") or line.startswith("#") or line.startswith("<!--"):
                continue
            if re.match(r"^(?:name|description|allowed-tools)\s*:", line):
                continue
            if is_source_noise(line):
                continue
            line = clean(line, 260)
            if len(line) < 20:
                continue
            lines.append(line)
            if len(lines) >= limit:
                return lines
    return lines


def is_generic_anchor(line: str) -> bool:
    lowered = line.lower()
    generic_bits = (
        "bverwg 6 c 12.21",
        "maßstab verwaltungsentscheidung",
        "verifizierte anker",
        "gesetze-im-internet.de",
        "dejure.org",
        "openjur",
        "nur fallbezogen",
        "nicht verifizierte",
        "vor verwendung",
        "belastbaren quelle",
        "nicht erfinden",
        "rechtsprechung nur",
        "wenn es um",
        "tragende normen verifizieren",
        "fristen und eilrisiken",
        "rot (",
        "gelb (",
        "gruen (",
        "grün (",
        "rolle, ziel",
        "live",
        "dieser skill",
        "skill zum",
        "skill für",
        "skill fuer",
        "auswahlstichwort",
        "stichwort für die auswahl",
        "stichwort fuer die auswahl",
        "vor einer rechtlichen schlussfolgerung",
        "arbeitsmodus:",
        "fokus:",
        "dieser skill erklärt",
        "dieser skill erklaert",
        "dieser skill vertieft",
        "im allgemeinen bundesland-skill",
        "nur kurz angerissen",
    )
    return any(bit in lowered for bit in generic_bits)


def extract_norm_anchors(skill_material: list[dict[str, str]], max_items: int = 7) -> list[str]:
    anchors: list[str] = []
    seen: set[str] = set()
    law_pattern = "|".join(re.escape(marker) for marker in sorted(LAW_MARKERS, key=len, reverse=True))
    for line in relevant_lines(skill_material):
        if is_generic_anchor(line):
            continue
        has_norm = re.search(r"\b(?:Paragraf(?:en)?|Artikel|Art\.)\s+\d", line)
        if not has_norm:
            continue
        if not any(marker in line for marker in LAW_MARKERS):
            continue
        if any(marker in line for marker in COURT_MARKERS) and re.search(r"\b(?:Urteil|Beschluss|Entscheidung)\b", line):
            continue
        starts_like_norm = re.match(rf"^(?:Normenradar:\s*)?(?:{law_pattern})\b", line)
        starts_with_paragraph = re.match(r"^(?:Paragraf(?:en)?|Artikel|Art\.)\s+\d", line)
        if not (starts_like_norm or starts_with_paragraph):
            continue
        if re.search(r"\b(?:Erblasser|Eigentümer|Mandant|Arbeitnehmer|Arbeitgeber|Kläger|Beklagter|Versicherter|Gläubiger|Schuldner)\b", line[:90]):
            continue
        if re.search(r"\b\d[\d.]*\s*(?:EUR|Euro|Mio|ha)\b", line[:140]):
            continue
        # Ordinalzahlen in ausgeschriebenen Datumsangaben sind keine Satzenden.
        # Ohne Maskierung wird etwa "seit 1. Juli 2026" zu "seit 1" gekürzt.
        masked_line = re.sub(
            r"\b(\d{1,2})\.\s+(?=(?:Januar|Februar|März|April|Mai|Juni|Juli|August|September|Oktober|November|Dezember)\b)",
            r"\1∶ ",
            line,
            flags=re.IGNORECASE,
        )
        candidate_source = SENTENCE_BOUNDARY_PATTERN.split(masked_line, maxsplit=1)[0]
        candidate_source = candidate_source.replace("∶", ".")
        candidate = clean(candidate_source, 185).rstrip(" .,:;")
        if not candidate:
            continue
        key = re.sub(r"\W+", "", candidate.lower())
        if key in seen:
            continue
        seen.add(key)
        anchors.append(candidate)
        if len(anchors) >= max_items:
            break
    return anchors


def extract_case_anchors(skill_material: list[dict[str, str]], max_items: int = 4) -> list[str]:
    anchors: list[str] = []
    seen: set[str] = set()
    for line in relevant_lines(skill_material):
        if is_generic_anchor(line):
            continue
        if not any(marker in line for marker in COURT_MARKERS):
            continue
        if not re.match(r"^(?:BGH|BAG|BVerfG|BVerwG|BSG|BFH|EuGH|BPatG|OLG|LG|AG|LAG|ArbG|SG|LSG)\b", line):
            continue
        if re.match(r"^[a-z0-9-]+\s+[—-]\s+", line):
            continue
        has_decision_signal = (
            re.search(r"\b(?:Urteil|Beschluss|Entscheidung)\b", line)
            or re.search(r"\b\d{2}\.\d{2}\.\d{4}\b", line)
            or re.search(r"\b(?:[IVX]+ ZR|IX ZR|XII ZB|C-\d+|BvR|AZR|StR|CN|C )", line)
        )
        if not has_decision_signal:
            continue
        candidate = clean(line, 280).rstrip(".")
        if not candidate:
            continue
        key = re.sub(r"\W+", "", candidate.lower())
        if key in seen:
            continue
        seen.add(key)
        anchors.append(candidate)
        if len(anchors) >= max_items:
            break
    return anchors


def case_identity(anchor: str) -> str:
    ids = case_id_set(anchor)
    return "|".join(sorted(ids)) if ids else re.sub(r"\W+", "", anchor.lower())[:90]


def case_id_set(anchor: str) -> set[str]:
    normalized = anchor.replace("–", "-").replace("—", "-")
    patterns = (
        r"\b(?:[IVX]+|X|IX|XII|XI|VIII|VII|VI|V|IV|III|II|I)\s+ZR\s+\d+/\d+\b",
        r"\b\d+\s+AZR\s+\d+/\d+\b",
        r"\b\d+\s+StR\s+\d+/\d+\b",
        r"\b\d+\s+BvR\s+\d+/\d+\b",
        r"\b\d+\s+BvL\s+\d+/\d+\b",
        r"\bB\s+\d+\s+[A-Z]{1,3}\s+\d+/\d+\s+R\b",
        r"\bC-\d+/\d+\b",
        r"\bKZR\s+\d+/\d+\b",
        r"\b\d{1,3}\s+[A-ZÄÖÜ][A-Za-zÄÖÜäöüß]{0,7}\s+\d+/\d+\b",
    )
    ids: list[str] = []
    for pattern in patterns:
        ids.extend(match.group(0).lower().replace(" ", "") for match in re.finditer(pattern, normalized))
    return set(ids)


def dedupe_cases(profile_cases: list[str], extracted_cases: list[str]) -> list[str]:
    seen: set[str] = set()
    for case in profile_cases:
        seen.update(case_id_set(case))
    out: list[str] = []
    for case in extracted_cases:
        ids = case_id_set(case)
        fallback = case_identity(case)
        if ids and seen.intersection(ids):
            continue
        if not ids and fallback in seen:
            continue
        seen.update(ids or {fallback})
        out.append(case)
    return out


def skill_fields(skill_material: list[dict[str, str]], max_items: int = 6) -> list[tuple[str, str]]:
    fields: list[tuple[str, str]] = []
    seen: set[str] = set()
    for item in skill_material:
        desc = item.get("desc") or item.get("body") or item.get("slug", "")
        title = field_title(desc, item.get("slug", ""), item.get("heading", ""))
        detail = route_excerpt(
            field_detail(desc, item.get("body", ""), title),
            180,
        )
        key = re.sub(r"\W+", "", title.lower())
        if not key or key in seen:
            continue
        seen.add(key)
        fields.append((title, route_excerpt(detail, 150)))
        if len(fields) >= max_items:
            break
    return fields


def profile_fields(
    profile: ThemenProfil,
    skill_material: list[dict[str, str]],
    max_items: int = 6,
) -> list[tuple[str, str]]:
    overrides = PROFILE_FIELD_OVERRIDES.get(profile.key)
    if overrides:
        return [(title, clean(detail, 180)) for title, detail in overrides[:max_items]]
    fields: list[tuple[str, str]] = []
    seen: set[str] = set()
    for station in profile.stationen:
        text = clean(station, 240).rstrip(".")
        if ":" in text:
            title, detail = text.split(":", 1)
        else:
            parts = [part.strip() for part in text.split(",") if part.strip()]
            title = ", ".join(parts[:2]) if len(parts) >= 2 else " ".join(text.split()[:6])
            detail = text
        title = clean(title, 90).rstrip(" .:-")
        detail = clean(detail, 180).rstrip(" .")
        key = re.sub(r"\W+", "", title.lower())
        if not key or key in seen:
            continue
        seen.add(key)
        if detail:
            detail = detail[0].upper() + detail[1:]
        fields.append((title, detail))
        if len(fields) >= max_items:
            return fields

    noise_bits = (
        "allgemein",
        "aktenanlage",
        "beweislast",
        "chronologie",
        "deal",
        "einstieg",
        "fehlerkatalog",
        "kaltstart",
        "luecken",
        "quality",
        "quelle",
        "red-team",
        "routing",
        "start",
        "workflow",
    )
    for title, detail in skill_fields(skill_material, max_items * 3):
        lowered = title.lower()
        detail_lowered = detail.lower()
        if any(bit in lowered for bit in noise_bits):
            continue
        if any(
            bit in detail_lowered
            for bit in (
                "beginne nicht mit einem fragenkatalog",
                "dieser arbeitsgang macht chronologie und belegmatrix",
                "dieser arbeitsgang macht fristen- und risikoampel",
                "dieser arbeitsgang macht mandantenkommunikation",
                "dieser arbeitsgang ist ein konkreter fachbaustein",
            )
        ):
            continue
        if any(
            bit in detail_lowered
            for bit in (
                "problemfokus dieses skills",
                "bleibe beim konkreten titel",
                "tatsachen, frist, norm, beweislast",
            )
        ):
            detail = quick_grip(profile, title, detail)
        if (
            re.match(r"^\d+\.\s+", detail)
            or detail.rstrip().endswith("?")
            or any(bit in detail_lowered for bit in PRACTICE_ROUTE_NOISE)
            or is_generic_route_detail(detail)
        ):
            title_tokens = set(re.findall(r"[a-zäöüß]{5,}", lowered))
            station = max(
                profile.stationen,
                key=lambda item: len(
                    title_tokens
                    & set(re.findall(r"[a-zäöüß]{5,}", item.lower()))
                ),
                default=f"{profile.label} fachlich und aktennah bearbeiten",
            )
            station_detail = station.split(":", 1)[-1].strip().rstrip(".")
            detail = clean(f"Bearbeite {title}: {station_detail}", 180)
        key = re.sub(r"\W+", "", lowered)
        if not key or key in seen:
            continue
        seen.add(key)
        if detail:
            detail = detail[0].upper() + detail[1:]
        fields.append((title, detail))
        if len(fields) >= max_items:
            break
    return fields


def workshop_fields(
    profile: ThemenProfil,
    routes: list[tuple[str, str, str, str, str]],
    max_items: int = 9,
) -> list[tuple[str, str]]:
    """Baut stabile Werkstattfelder ohne Satzfragmente aus Skill-Metadaten."""

    fields: list[tuple[str, str]] = []
    seen: set[str] = set()
    for title, detail, _depth, _anchors, _output in routes:
        title = clean(title, 90).rstrip(" .:-")
        detail = clean(detail, 180).rstrip(" .")
        key = re.sub(r"\W+", "", title.lower())
        if not key or key in seen:
            continue
        fields.append((title, detail))
        seen.add(key)
        if len(fields) >= max_items:
            return fields

    overrides = PROFILE_FIELD_OVERRIDES.get(profile.key)
    fallback = (
        [(clean(title, 90), clean(detail, 180)) for title, detail in overrides]
        if overrides
        else profile_fields(profile, [], max_items)
    )
    for title, detail in fallback:
        key = re.sub(r"\W+", "", title.lower())
        if not key or key in seen:
            continue
        fields.append((title, detail))
        seen.add(key)
        if len(fields) >= max_items:
            break
    return fields[:max_items]


def station_deliverable(profile: ThemenProfil, title: str) -> str:
    """Leitet aus Arbeitswelt und Stationsbezeichnung ein konkretes Teilprodukt ab."""

    hay = title.lower()
    family = workflow_family(profile)
    catalogs: dict[str, tuple[tuple[tuple[str, ...], str], ...]] = {
        "source": (
            (("epoche", "fallfrage", "rechtsraum"), "Epochen- und Statuskarte mit begrenzter Leitfrage"),
            (("text", "quelle", "überliefer", "edition"), "Textzeugenblatt mit Edition, Übersetzung und Unsicherheitsgrad"),
            (("begriff", "system"), "Begriffssynopse mit zeitgenössischer Funktion und Gegenlesart"),
            (("prozess", "klage", "rechtsschutz", "actio"), "Aktionen- oder Verfahrenskarte mit Rechtsfolge"),
            (("materiell", "fallanalyse", "subsum"), "historische Fallanalyse nach der belegten Zeitstufe"),
            (("rezeption", "wirkung", "anschluss"), "Rezeptionslinie mit Übernahme, Umdeutung und Bruch"),
        ),
        "research": (
            (("frage", "ziel", "problem"), "Leitfragenblatt mit Bewertungsmaßstab und Arbeitsannahme"),
            (("quelle", "stand", "evidenz", "vorarbeit"), "Quellen- und Evidenzmatrix mit Belegwert"),
            (("methode", "arbeitsprogramm", "arbeitspaket"), "Methoden- und Arbeitsplan mit Abhängigkeiten"),
            (("finanz", "budget", "ressource", "kosten"), "nachrechenbares Ressourcen- oder Finanzblatt"),
            (("risiko", "review", "begutacht", "gegen"), "Gegenhypothesen- und Risikomatrix mit Erwiderung"),
            (("einreich", "abgabe", "produkt"), "abgabefähige Fassung samt Vollständigkeitskontrolle"),
        ),
        "production": (
            (("inventar", "eingang", "bestand", "register"), "Dokumentenregister mit Fassung, Status und Lücke"),
            (("version", "fundstelle", "vergleich"), "Versions- oder Abweichungsmatrix mit Fundstellen"),
            (("qualität", "konsistenz", "prüfung", "kontrolle"), "Korrekturliste mit Auswirkung und Verantwortlichem"),
            (("anlage", "vollständig"), "Anlagen- und Fehlteilliste mit eindeutiger Zuordnung"),
            (("freigabe", "export", "versand", "übergabe", "output"), "geprüftes Ausgabe- oder Übergabepaket samt Öffnungsprobe"),
        ),
        "drafting": (
            (("struktur", "ziel", "intake", "term"), "Struktur- oder Regelungsvermerk mit Ziel- und Rückfallposition"),
            (("due diligence", "datenraum", "befund"), "Befundmatrix mit Vertrags-, Preis- und Vollzugsfolge"),
            (("vertrag", "klausel", "garantie", "haftung", "regelung"), "ausformulierte Klausel oder Redline mit Alternativfassung"),
            (("beschluss", "gremium", "board", "freigabe"), "entscheidungsreife Gremienvorlage mit Beschlusstext"),
            (("signing", "closing", "vollzug", "register"), "Vollzugsliste mit Bedingung, Verantwortlichem und Nachweis"),
            (("verhandlung", "position"), "Positionsmatrix mit Ziel, Rückfallposition und Tauschmasse"),
        ),
        "decision": (
            (("eingang", "zuständig", "zulässig", "antrag"), "Eingangsverfügung oder Zulässigkeitsvermerk mit Frist"),
            (("gehör", "hinweis", "auflage", "aufklärung"), "Hinweis- oder Auflagenverfügung mit Adressat und Folge"),
            (("beweis", "zeuge", "gutacht", "ermittlung"), "Beweisplan oder Beweisbeschluss mit Beweisthema"),
            (("relation", "vortrag", "streit"), "Relationszeile mit Schlüssigkeit, Erheblichkeit und Beweislast"),
            (("tenor", "urteil", "entscheidung", "abschluss"), "Tenor- und Begründungsbaustein samt Nebenentscheidungen"),
        ),
        "case": (
            (("frist", "zugang", "zuständig", "verfahren"), "Fristen- und Verfahrensblatt mit Sofortmaßnahme"),
            (("akte", "sachverhalt", "tatsache", "chronologie"), "Chronologie und Belegmatrix mit offenen Widersprüchen"),
            (("beweis", "nachweis", "befund", "dokument"), "Beweismittelspiegel je entscheidendem Merkmal"),
            (("anspruch", "norm", "tatbestand", "prüfung"), "Tatbestandsmatrix mit Norm, Beleg und Gegenargument"),
            (("entwurf", "produkt", "ausgabe", "rechtsschutz"), "versandfähiger Entwurf mit Anlagen- und Fristenbezug"),
            (("berechnung", "höhe", "betrag"), "nachrechenbare Berechnung mit Eingabewerten und Kontrollspur"),
        ),
    }
    for terms, product in catalogs[family]:
        if any(term in hay for term in terms):
            return product
    return {
        "source": "ausformulierter Quellenbefund mit Belegwert und Gegenlesart",
        "research": "ausformulierter Teilbefund mit Quelle, Unsicherheit und Folgeschritt",
        "production": "geprüfte Datei oder priorisierte Fehlteilliste mit Termin",
        "drafting": "ausformulierte Regelung samt Variante und Vollzugsschritt",
        "decision": "förmlicher Verfahrens- oder Entscheidungsbaustein",
        "case": "ausformulierter Ergebnisbaustein mit Beleg, Risiko und nächstem Schritt",
    }[family]


def station_instruction(profile: ThemenProfil, station: str) -> str:
    text = clean(station, 240).rstrip(" .")
    if ":" in text:
        title, detail = (part.strip() for part in text.split(":", 1))
    else:
        title, detail = "Prüfstation", text
    family = workflow_family(profile)
    deliverable = station_deliverable(profile, title)
    if family == "source":
        return (
            f"Quellengriff {title}: {detail}. Ordne jedem Punkt Textstelle, Textzeuge, "
            "Fassung, Übersetzung, Datierung, institutionellen Kontext und konkurrierende "
            f"Lesart zu. Lieferstück: {deliverable}; Rezeptions- oder Anschlussfrage bleibt "
            "davon getrennt."
        )
    if family == "research":
        return (
            f"Arbeitsgriff {title}: {detail}. Ordne jedem Punkt Aufgabenfrage, Maßstab, "
            "Quelle oder Datengrundlage, Gegenhypothese und Belastbarkeit zu. Lieferstück: "
            f"{deliverable}; offene Annahme und nächster Prüf- oder Redaktionsschritt werden "
            "benannt."
        )
    if family == "production":
        return (
            f"Produktionsgriff {title}: {detail}. Ordne jedem Punkt Eingangsdatei, "
            "maßgebliche Fassung, Fundstelle, Format, Freigabe, Verantwortlichen und "
            f"Übergabe zu. Lieferstück: {deliverable}."
        )
    if family == "drafting":
        return (
            f"Entwurfsgriff {title}: {detail}. Ordne jedem Punkt Geschäftsziel, "
            "Dokumentstand, Rechtswirkung, Verhandlungsposition, Nachweis, Risiko und "
            f"Vollzug zu. Lieferstück: {deliverable}; die Rückfallposition bleibt sichtbar."
        )
    if family == "decision":
        return (
            f"Entscheidungsgriff {title}: {detail}. Ordne jedem Punkt Parteivortrag, "
            "Aktenfund, Rechtsmaßstab, Beweislast, Gegenposition und Entscheidungsreife "
            f"zu. Lieferstück: {deliverable} mit dem nächsten förmlichen Schritt."
        )
    return (
        f"Arbeitsgriff {title}: {detail}. Ordne jedem Punkt den konkreten Aktenfund, "
        "die steuernde Norm, die Beweislast und die stärkste Gegenposition zu. Lieferstück: "
        f"{deliverable}; verbleibendes Risiko und nächster Verfahrensschritt werden "
        "ausdrücklich benannt."
    )


def station_heading(station: str) -> str:
    text = clean(station, 220).rstrip(" .")
    if ":" in text:
        return clean(text.split(":", 1)[0], 90).rstrip(" .:-")
    return clean(text, 110).rstrip(" .:-")


def detail_question(detail: str) -> str:
    detail = clean(detail, 115).lstrip("- ").rstrip(". -")
    for _ in range(3):
        shortened = re.sub(r"\s+\b(?:und|oder|mit|ohne|für|fuer|von|zu|im|in|als|bei|nach|nächstem|naechstem)\b$", "", detail, flags=re.IGNORECASE).rstrip(". -")
        if shortened == detail:
            break
        detail = shortened
    repairs = {
        "Kollisions": "Kollisionsprüfung",
        "Verhandlungs": "Verhandlungslinie",
        "Fehler": "Fehlerliste",
        "Fristen": "Fristen- und Risikoampel",
        "Paragraf": "einschlägige Paragrafen",
        "Liefere": "konkreten Sofortgriff",
    }
    for suffix, replacement in repairs.items():
        if detail.endswith(suffix):
            detail = detail[: -len(suffix)].rstrip(" -") + " " + replacement
            break
    return detail.rstrip(". -")


def quick_grip(profile: ThemenProfil, field: str, detail: str) -> str:
    hay = f"{profile.key} {field} {detail}".lower()
    if profile.key in PROFILE_FIELD_OVERRIDES and detail and re.sub(
        r"\W+", "", detail.lower()
    ) != re.sub(r"\W+", "", field.lower()) and not any(
        bit.lower() in detail.lower() for bit in GENERIC_FIELD_BITS
    ):
        return clean(detail, 180).rstrip(" .")
    if profile.key in {"aktg_hv", "phishing", "weg"} and detail and not any(
        bit.lower() in detail.lower() for bit in GENERIC_FIELD_BITS
    ) and re.sub(r"\W+", "", detail.lower()) != re.sub(r"\W+", "", field.lower()):
        return clean(detail, 180).rstrip(" .")
    if profile.key == "aktg_hv":
        if "abstimmung" in hay or "feststellung" in hay:
            return "Präsenz, Stimmverbote, Mehrheitsmaßstab, Abstimmungsfrage, Zählung, Feststellung, Widerspruch und Niederschrift der Hauptversammlung lückenlos abgleichen"
        if "anfechtung" in hay:
            return "Beschluss, Teilnahme- und Widerspruchslage, Klagebefugnis, Monatsfrist, Anfechtungsgrund, Kausalität und Bekanntmachung nach Paragrafen 243 und folgende AktG sichern"
        if "aufsichtsratsvergütung" in hay:
            return "Satzungs- oder Hauptversammlungsgrundlage, Aufgabenbild, Angemessenheit, Ausschussvergütung, Interessenkonflikt, Transparenz und Beschlussfassung prüfen"
        if "beherrschungs" in hay or "gewinnabführung" in hay:
            return "Vertragsentwurf, Bericht, Prüfung, Zustimmungsbeschlüsse, Ausgleich, Abfindung, Registeranmeldung, Wirksamkeit und Minderheitenschutz in einer Vollzugsmatrix verbinden"
        if "beweisakte" in hay:
            return "Einberufung, Nachweise, Teilnehmerverzeichnis, Vollmachten, Fragen und Antworten, Abstimmung, Widersprüche, Niederschrift und Veröffentlichungen beweisfest indexieren"
        if "freigabeverfahren" in hay:
            return "Anfechtungsklage, Freigabeantrag, vorrangiges Vollzugsinteresse, wesentliche Nachteile, Sicherheitsleistung, Glaubhaftmachung und Registerkommunikation verzahnen"
        return "Einberufung, Teilnahme, Auskunft, Abstimmung, Beschlussfeststellung, Niederschrift, Anfechtungsrisiko und Registervollzug für die konkrete Hauptversammlung ordnen"
    if profile.key == "eu_prozess":
        return "Klageart, Zuständigkeit, Frist, Verfahrenssprache, e-Curia, Anlagen, Rechtsschutzinteresse und Antragssatz zuerst sichern"
    if profile.key == "zeugnis":
        return "Zeugnisart, Tätigkeitsbild, Leistungsnote, Sozialverhalten, Auslassung, Form und konkrete Änderungsfassung in einer Matrix verbinden"
    if profile.key == "bank":
        return "Produkt, Kunde, Beratung oder Autorisierung, Aufsichtspflicht, Dokumentation, Schaden und Frist in einer Bankakte trennen"
    if profile.key == "datenbank":
        return "Schutztyp, Investition, Zugriffspfad, entnommene Datenmenge, Lizenz, Schranke und Beweissicherung als Datenbankmatrix ordnen"
    if profile.key == "marke":
        return "Zeichen, Priorität, Waren oder Dienstleistungen, Kennzeichnungskraft, Ähnlichkeit, Benutzung, Verwechslungsgefahr und Verfahrensziel verbinden"
    if profile.key == "design":
        return "Ansichten, Offenbarungstag, Formenschatz, Eigenart, Gestaltungsfreiheit, Gesamteindruck, Verletzung und Nichtigkeitsrisiko vergleichen"
    if profile.key == "patent":
        return "Anspruchsmerkmale, Priorität, Stand der Technik, Rechtsbestand, angegriffene Ausführung, Schutzbereich und Verfahrensschritt ordnen"
    if profile.key == "gebrauchsmuster":
        return "Abzweigung, Schonfrist, Schutzanspruch, Recherche, ungeprüften Rechtsbestand, Verletzung und Löschungsrisiko getrennt sichern"
    if profile.key == "gewerblicher_rechtsschutz":
        return "Schutzrecht, Inhaber, Priorität, Registerstand, Verletzung, Beweis, Eilbedarf und parallele Anspruchsgrundlagen getrennt prüfen"
    if profile.key == "lobbyregister":
        return "Adressat, Interessenvertretung, Registrierungspflicht, Ausnahme, Angaben, Aktualisierung und Sanktionsrisiko sofort prüfen"
    if profile.key == "geldwaesche":
        return "Verpflichtetenrolle, Kunde, wirtschaftlich Berechtigter, Risiko, Mittelherkunft, Verdachtsschwelle und Dokumentation trennen"
    if profile.key == "cybersicherheit":
        return "Einrichtung, Rechtsrahmen, Asset, Vorfall, Meldefrist, Nachweisordner und Aufsichtsrisiko in eine Incident-Linie bringen"
    if profile.key == "kartell":
        return "Markt, Beteiligte, Verhalten, Zweck oder Wirkung, Beleg, Rechtfertigung, Schaden und Bußgeldrisiko zusammenführen"
    if profile.key == "produkt":
        return "Produktversion, Fehlerart, Sicherheitserwartung, Warnung, Beobachtung, Rückrufbedarf und Haftungsfolge sofort abgleichen"
    if profile.key == "sozialstatus":
        return "Tätigkeit, Zeitraum, Weisung, Eingliederung, Unternehmerrisiko, Vertragswirklichkeit, Beiträge und Frist gewichten"
    if profile.key == "sozial":
        if "arbeitslosengeld" in hay:
            return "Anwartschaftszeit, Bemessungsrahmen, Bemessungsentgelt, Leistungsentgelt, Anspruchsdauer, Ruhen, Sperrzeit und taggenaue Bescheidabweichung nach SGB III berechnen"
        if "arbeitsunfall" in hay:
            return "versicherte Tätigkeit, Verrichtung, Unfallereignis, Gesundheitserstschaden, Kausalität, Durchgangsarztbericht, Zeugen und Gutachterfragen nach Paragraf 8 SGB VII ordnen"
        if "pflegegrad" in hay:
            return "Pflegeantrag, Alltagsschilderung, Befunde, MD-Gutachten und Bescheid nach den sechs Modulen und gewichteten Punkten abgleichen"
        if "gdb" in hay or "merkzeichen" in hay:
            return "Funktionsbeeinträchtigungen, Einzelbewertungen, Wechselwirkungen, Versorgungsmedizin-Maßstab und Merkzeichenvoraussetzungen mit den konkreten Befunden verbinden"
        return "Bescheid, Bekanntgabe, Leistungsträger, medizinische oder wirtschaftliche Anspruchsmerkmale, Belege, SGG-Frist und passendes Leistungsziel zusammenführen"
    if profile.key == "ma_finanzierung":
        if has_route_term(hay, "kvg", "kagb", "aifm"):
            return "Bestimme Vollerlaubnis, Registrierung oder Service-KVG-Modell anhand AuM, Leverage, Lock-up und Vertrieb; prüfe Geschäftsleiter, Eigenmittel, Organisation, Auslagerungsgrenzen, Letztverantwortung, Vertragskontrollen, BaFin-Unterlagen und realistischen Genehmigungszeitplan"
        if "beirat" in hay and "zustimmung" in hay:
            return "Zustimmungskatalog nach Geschäftstyp, Schwellenwert und Berechnungsmethode definieren, Geschäftsführungsbefugnis und Vertretungsmacht trennen und Eilfall, Umlaufbeschluss, Interessenkonflikt sowie Rechtsfolge fehlender Zustimmung regeln"
        if "beirat" in hay and "haftung" in hay:
            return "Rechtsnatur des Beirats, Bestellung, Kompetenz, tatsächliche Einflussnahme, Pflichtmaßstab, Anspruchsinhaber, Beschlusslage, Kausalität und Deckung getrennt prüfen"
        if "beirat" in hay and "vergütung" in hay:
            return "Satzungs- oder Vertragsgrundlage, zuständiges Organ, Beschluss, Leistungsbild, Umsatzsteuer, Interessenkonflikt, Fälligkeit und Offenlegung der Beiratsvergütung abstimmen"
        if "verbindliche auskunft" in hay or "sanierungsgewinn" in hay:
            return "genau bestimmten, noch nicht verwirklichten Sachverhalt, besondere steuerliche Rechtsfrage, erhebliches Interesse, Gebührenwert, Bindungsumfang und zeitliche Reihenfolge von Auskunft und Umsetzung nach Paragraf 89 AO sichern"
        if "bank" in hay and ("consent" in hay or "change-of-control" in hay):
            return "Change-of-Control-Tatbestand, betroffene Finanzierung, Zustimmungsadressat, Informationspaket, Waiver-Bedingung, Gebühr, Kündigungsfolge und Closing-Bedingung in einer Consent-Matrix verbinden"
        if "bidder" in hay or "vdr" in hay or "process letter" in hay:
            return "Process-Letter-Vorgabe, Datenraumregel, Bieterfrage, Angebotsannahme, Finanzierungsvorbehalt, Markup-Grenze, Abgabefrist und Ausschlussfolge in einer Bid-Matrix ordnen"
        if "board" in hay or "business judgment" in hay:
            return "Organ, Kompetenz, angemessene Informationsgrundlage, Bewertung, Alternativen, Interessenkonflikt, Protokollierung und konkreten Beschlusstext für die Transaktionsentscheidung sichern"
        if "monitoring" in hay or "automatisierung" in hay:
            return "Signing-, Closing- und Post-Closing-Pflicht mit Auslöser, Frist, Owner, Nachweis, Abhängigkeit, Eskalation und Erledigungsbeleg in einem Transaktionskalender führen"
        if "markup" in hay or "key issues" in hay:
            return "jede materielle Vertragsabweichung nach Klausel, wirtschaftlicher Wirkung, Haftungsverschiebung, Verhandlungsziel, Rückfallposition, Owner und Freigabestatus priorisieren"
        if has_route_term(hay, "ancillary", "tsa", "sla"):
            return "Leistungskatalog, Service Level, Laufzeit, Entgelt, Abhängigkeit, Daten- und IP-Zugriff, Haftung, Exit-Unterstützung und Übergabekriterium für Nebenverträge ausformulieren"
        return "Transaktionsstruktur, Datenraumfund, Wertwirkung, Vertragsabbildung, Gremienfreigabe, Closing-Bedingung, Owner und Termin zu einer belastbaren Deal-Entscheidung verbinden"
    if profile.key == "weg":
        return "Gemeinschaftsordnung, Beschlusskompetenz, Einladung, Mehrheit, Protokoll, Verwalterbefugnis, Anfechtungsfrist und Umsetzung anhand der Verwaltungsakte prüfen"
    if profile.key == "forderung":
        return "Vertrag, Leistung, Rechnung, Fälligkeit, Verzug, Einwendung, Beweis und Klage- oder Vollstreckungsweg klagereif ordnen"
    if profile.key == "technikregulierung":
        if "kollusion" in hay or "pricing" in hay:
            return "Pricing-Zweck, Wettbewerberdaten, Hub-Dienstleister, menschliche Kontrolle, Kartellrechtsrisiko und Technikregulierung trennen"
        if "art. 4" in hay or "kompetenz" in hay or "schulung" in hay:
            return "Adressatenkreis, Rollen, Risikoklasse, Schulungsinhalt, Nachweis, Wiederholung und Verantwortlichkeit dokumentieren"
        if "anbieter" in hay or "provider" in hay or "art. 25" in hay:
            return "Eigenname, Eigenmarke, wesentliche Änderung, Zweckänderung, Produktintegration und Pflichtenwechsel nach Art. 25 trennen"
        if "betreiber" in hay or "deployer" in hay or "art. 26" in hay:
            return "bestimmungsgemäße Nutzung, menschliche Aufsicht, Eingabedaten, Logging, FRIA und Vorfallmeldung als Betreiberpflichten ordnen"
        if "owi" in hay or "untersuchung" in hay:
            return "Vorwurf, Behörde, Frist, Logs, Interviews, Datenschutz, Legal-Privilege-Risiko und Verteidigungslinie sichern"
        if "abgrenzung" in hay or "konventionelle" in hay:
            return "Inferenz, Autonomie, Output, Zweckbestimmung, Systemgrenze und Folgeprüfung nach Art. 3 Nr. 1 festlegen"
        return "Zweckbestimmung, Rolle, Risikoklasse, Stichtag, Nachweisakte, Rechtsfolge und Behördenrisiko in einer Entscheidungszeile verbinden"
    if profile.key == "bgb":
        return "Anspruchsgrundlage, Vertragsschluss, Pflichtverletzung oder Mangel, Einwendung, Frist, Beweislast und Rechtsfolge sauber abschichten"
    if profile.key == "zivilprozess":
        return "Antrag, Streitgegenstand, Schlüssigkeit, Erheblichkeit, Beweislast, Verfügung und Tenor in eine Relation bringen"
    if profile.key == "erbrecht":
        return "Familienstamm, Verfügung, Quote, Nachlasswert, Pflichtteilsergänzung, Auskunft und Erbscheinspfad rechnerisch ordnen"
    if profile.key == "medizin":
        return "Befund, Indikation, Standard, Aufklärung, Dokumentation, Beweislast, Gutachtenfrage und Verfahren zusammenführen"
    if profile.key == "verkehr":
        return "Ereignis, Frist, Haftungsquote, Beweismittel, Schaden, Einwand und Zahlungs- oder Einspruchsziel sofort sortieren"
    if profile.key == "vollstreckung":
        return "Titel, Klausel, Zustellung, Forderungsstand, Zugriffsziel, Antrag, Schuldnerschutz und Anlagen prüfen"
    if profile.key == "immobilien":
        return "Objekt, Grundbuchstand, Rechtsgeschäft, Form, Bewilligung, Nachweis, Rang und Vollzugsschritt in einer Aktenlinie verbinden"
    if profile.key == "eu_recht":
        return "Unionsnorm, Rechtsakt, Anwendungsbereich, unmittelbare Wirkung, Vorrang, Rechtfertigung und Rechtsschutzroute trennen"
    if profile.key == "methodik":
        return "Rechtsfrage, Normmerkmal, Tatsache, Aktenfund, Subsumtion, Gegenargument und Endprodukt zeilenweise verknüpfen"
    if profile.key == "betreuung":
        return "Angelegenheit, Erforderlichkeit, Wunsch, Vertretungsmacht, Genehmigung, Beleg und Gerichtsschritt konkret bestimmen"
    if profile.key == "hoai":
        return "Vertragsjahr, Leistungsbild, Leistungsphase, geschuldeter Erfolg, Leistungsstand, Honorar, Nachtrag und Haftungsbeleg trennen"
    if profile.key == "weltraum":
        return "Mission, Weltraumgegenstand, Betreiber, Startstaat, Registerstaat, Genehmigung, Frequenz, Haftung und Telemetriebeleg verbinden"
    if profile.key == "presse":
        return "Aussagetyp, Beweistatsachen, Stellungnahme, Identifizierbarkeit, Bildrecht, Verfahrensstatus und veröffentlichungsfähige Fassung abgleichen"
    if profile.key == "agrar":
        return "Betrieb, Fläche, Pacht oder Hofstatus, Grundsteuerwert, Förderjahr, Spezialbehörde, Frist und Bewirtschaftungsbeleg verbinden"
    if profile.key == "sport":
        return "Regelwerkfassung, Entscheidung, Zustellung, interne Instanz, Schieds- oder Gerichtsweg, Eilbedarf und Wettkampfbeleg sichern"
    if profile.key == "jveg":
        return "Heranziehung, Rolle, Ausschlussfrist, Zeitansatz, Honorargruppe, Auslagen, Kürzung und Rechtsbehelf rechnerisch prüfen"
    if profile.key == "ehrenamtliche_richter":
        return "Rolle, Spruchkörper, Besetzung, Neutralität, offene Beweisfrage, Beratung, Mehrheit und Beratungsgeheimnis trennen"
    if profile.key == "rechtsgeschichte":
        return "Textzeuge, Fassung, Datum, Rechtsraum, Übersetzung, Normfunktion, Anwendungspraxis und Rezeptionsspur quellenkritisch ordnen"
    if profile.key == "kirchenrecht":
        return "zuständige Autorität, Canon, Partikularrecht, Urkunde, kirchlichen Verfahrensweg, Frist und staatliche Schnittstelle bestimmen"
    if profile.key == "kanzleibetrieb":
        if "access control" in hay or "roles" in hay:
            return "Mandatsrolle, Schutzbedarf, zulässigen Lese-, Schreib-, Freigabe- und Exportzugriff, Stellvertretung, Rezertifizierung und Entzug in einer Berechtigungsmatrix festlegen"
        if "action-item" in hay or "owner matrix" in hay:
            return "Aufgabe, Ergebnis, verantwortlichen Bearbeiter, Freigeber, Fälligkeit, Abhängigkeit, Status, Eskalation und Erledigungsnachweis in einer Owner-Matrix führen"
        if "rechtsmittel" in hay or "decision gate" in hay:
            return "Zustellung, Rechtsmittelfrist, Beschwer, Statthaftigkeit, Zulassung, Kosten, Vollstreckungswirkung, Erfolgskorridor und Mandantenfreigabe vor Fristablauf entscheiden"
        if "associate workbench" in hay:
            return "Arbeitsauftrag, Aktenfundstellen, offene Rechtsfragen, Entwurfsstand, Budget, Rückfrage, Vieraugenkontrolle und Übergabe für den bearbeitenden Anwalt bündeln"
        if "response legal" in hay:
            return "Ereignis, betroffene Mandate, Sofortschutz, Verantwortliche, Beweissicherung, Melde- und Informationsbedarf, Freigaben und Nachbereitung in einem Reaktionsprotokoll steuern"
        if "authority matrix" in hay:
            return "Entscheidungstyp, Wertgrenze, fachlich Verantwortlichen, Freigeber, Vertretung, Eskalationsstufe, Unterschriftsrecht und Nachweis in einer Kompetenzmatrix ordnen"
        if "bad news" in hay:
            return "schlechte Entwicklung, gesicherte Ursache, Auswirkung, Handlungsoptionen, Kosten, Frist, Empfehlung und Entscheidungspunkt früh und ohne Beschönigung in einem Mandantenmemo darstellen"
        if "beauty contest" in hay:
            return "Auswahlkriterien, Gewichtung, Team, Erfahrung, Interessenkonflikt, Preis, Arbeitsplan, Präsentationsbefund und Entscheidungsbegründung in einer nachvollziehbaren Wertungsmatrix führen"
        return "Mandat, Interessenkontrolle, Vollmacht, Frist, Verantwortlicher, Freigabe, Versandnachweis, Budget und Wiedervorlage sichern"
    if profile.key == "selbststaendige":
        return "Tätigkeit, Status, Vertrag, Leistung, Rechnung, Abgabe, Beleg, Zahlung und nächstes Geschäfts- oder Behördendokument ordnen"
    if profile.key == "dokumentenworkflow":
        return "maßgebliche Version, Fundstelle, Signatur, Zahl, Widerspruch, Lücke, Zielprodukt und reproduzierbare Übergabe verbinden"
    if profile.key in {"arbeits", "hr"}:
        if any(bit in hay for bit in ("kündigung", "befristung", "abmahnung", "aufheb", "betriebsrat")):
            return "Zugang, Dreiwochenfrist, Schriftform, Beteiligungsrechte, Darlegungslast und Klage- oder Vergleichsziel sofort trennen"
        if any(bit in hay for bit in ("agg", "beschwerde", "arbeitsschutz", "gefährd", "hinweis")):
            return "Meldung, Schutzpflicht, Anhörung, Vertraulichkeit, Beleg, Maßnahme und Benachteiligungsrisiko in einer Fallakte trennen"
        if any(bit in hay for bit in ("angebot", "offer", "vertrag", "onboarding", "nachweis")):
            return "Vertragstyp, Tätigkeit, Vergütung, Arbeitsort, Beginn, Befristung, Nachweis und Unterschriftsweg versandfertig ordnen"
        if any(bit in hay for bit in ("arbeitszeit", "urlaub", "fehlzeit", "krank", "payroll", "vergütung")):
            return "Zeitraum, Anspruch, Berechnung, Nachweis, Ausschlussfrist, Beteiligungsrecht und Buchungs- oder Antworttext verbinden"
        return "Arbeitsvertrag, aktuelle Maßnahme, Frist, Form, Beteiligungsrecht, Beleg und nächstes Personal- oder Prozessdokument ordnen"
    if "kündigung" in hay or "befristung" in hay or "betriebsrat" in hay or "arbeitsgericht" in hay:
        return "Zugang, Dreiwochenfrist, Schriftform, Beteiligungsrechte, Darlegungslast und Klage- oder Vergleichsziel sofort trennen"
    if "insolvenz" in hay or "starug" in hay or profile.key in {"insolvenz", "liquiditaet"}:
        if "abstimmung" in hay or "mehrheit" in hay:
            return "Gruppenbildung, Stimmrecht, Kopf- und Summenmehrheit, gruppenübergreifende Mehrheitsentscheidung, Schlechterstellungsverbot und Abstimmungsnachweis im Planvergleich prüfen"
        if "international" in hay:
            return "COMI, internationale Zuständigkeit, EuInsVO-Anerkennung, betroffene ausländische Gläubiger, Zustellung, Sprache und grenzüberschreitenden Vollzug des Plans sichern"
        if "restrukturierungsplan" in hay or "insolvenzplan" in hay:
            return "darstellenden und gestaltenden Teil, Gruppen, Planvergleich, Stimmrechte, Mehrheiten, Minderheitenschutz, Bestätigung und Vollzug in einer Planmatrix verbinden"
        return "Liquiditätsstatus, Fälligkeit, Fortbestehensprognose, Antragspflicht, Beweislast und Sanierungsoption in einer Entscheidungslinie ordnen"
    if "renten" in hay or "rente" in hay or "drv" in hay or profile.key == "renten":
        return "Versicherungsverlauf, Wartezeit, Entgeltpunkte, Rentenbeginn, Bescheidfehler und Widerspruchsfrist nach SGB VI nachrechnen"
    if profile.key == "sozial" or has_route_term(
        hay, "sozialrecht", "pflege", "pflegegrad", "hilfsmittel"
    ):
        return "Bescheid, Bekanntgabe, Leistungsträger, medizinische Belege, Wirtschaftlichkeit, SGG-Frist und Eilrechtsschutz zusammenführen"
    if "gesellschaft" in hay or "gmbh" in hay or "aktg" in hay or profile.key == "gesellschaft":
        return "Satzung, Beschlusskompetenz, Mehrheit, Vertretung, Treuepflicht, Registervollzug und Haftungsrisiko nebeneinanderlegen"
    if "agrar" in hay or "landpacht" in hay or "gap" in hay or "höfe" in hay:
        return "Pacht, Höfeordnung, GrdstVG-Genehmigung, GAP-Förderung, Bescheidfrist und Bewirtschaftungsnachweis aktennah prüfen"
    if "miet" in hay or "wohnung" in hay or profile.key == "miet":
        return "Vertrag, Rückstand, Mangelanzeige, Kündigungsgrund, Schonfrist, Zuständigkeit und Räumungsrisiko sofort sortieren"
    if profile.key == "famil" or has_route_term(hay, "familienrecht", "unterhalt"):
        return "Auskunft, Einkommen, Bedarf, Selbstbehalt, Kindeswohl, Versorgungsausgleich und Verbundfrage rechnerisch trennen"
    if "urheber" in hay or profile.key == "urheber":
        return "Werk, Rechtekette, Nutzungshandlung, Lizenz, Schranke, Beweis und Anspruchsziel verdichten"
    if profile.key in {"straf", "strafjustiz"} or has_route_term(
        hay, "strafrecht", "strafsache", "anklage"
    ):
        return "Tatkomplex, Norm, Beweismittel, Einlassung, Verwertbarkeit, Frist und Rechtsfolge zeilenweise prüfen"
    if profile.key in {"steuer", "finanzgericht"} or has_route_term(
        hay, "steuer", "steuern", "steuerrecht", "steuerliche", "besteuerung"
    ):
        return "Bescheid, Bekanntgabe, Einspruchsfrist, Besteuerungsgrundlage, Beleg, Schätzung und Aussetzungsbedarf getrennt prüfen"
    if "vergabe" in hay or profile.key == "vergabe":
        return "Rügefrist, Vergabeunterlagen, Zuschlagskriterium, Dokumentation, Bieterfrage und Nachprüfungsantrag sofort abgleichen"
    if profile.key in {"bau", "bauplanung"}:
        return "Vertragssoll, Nachtrag, Behinderung, Abnahme, Mangel, Kostenfolge, Beweis und Gutachterfrage in eine Bauakte bringen"
    if "datenschutz" in hay or "dsgvo" in hay or profile.key == "datenschutz":
        return "Rolle, Rechtsgrundlage, Betroffenenrecht, Frist, TOMs, Auftragsverarbeitung und Aufsichtsrisiko dokumentieren"
    if profile.key == "it":
        return "Leistungssoll, Abnahme, SLA, Rechtekette, Datenschutz, Haftung, Change Request und Beleglage zusammenführen"
    if "verwalt" in hay or profile.key == "verwaltung":
        return "Verwaltungsakt, Bekanntgabe, Widerspruch/Klagefrist, Ermessen, Anhörung, Akteneinsicht und Eilantrag prüfen"
    candidate = detail_question(detail)
    field_prefix = field.rstrip(" .:-").lower()
    if field_prefix and candidate.lower().startswith(field_prefix + ":"):
        candidate = candidate.split(":", 1)[1].strip()
    if candidate and len(candidate) >= 45 and re.sub(
        r"\W+", "", candidate.lower()
    ) != re.sub(r"\W+", "", field.lower()) and not any(
        bit in candidate.lower()
        for bit in (
            "tatsachen, frist, zuständigkeit",
            "tatsachen, frist, norm, beweislast",
            "problemfokus dieses skills",
            "bleibe beim konkreten titel",
        )
    ):
        return candidate
    stations = [station for station in profile.stationen if station]
    if stations:
        field_tokens = set(re.findall(r"[a-zäöüß]{5,}", field.lower()))
        station = max(
            stations,
            key=lambda item: len(
                field_tokens & set(re.findall(r"[a-zäöüß]{5,}", item.lower()))
            ),
        )
        return clean(
            f"Bearbeite {field} entlang der {profile.label}-Prüflinie: {station}",
            250,
        ).rstrip(" .")
    return clean(f"Bearbeite {field} als konkreten Vorgang im Gebiet {profile.label}", 220)


def quick_stations(profile: ThemenProfil, skill_material: list[dict[str, str]]) -> list[str]:
    if profile.key != "default" or not skill_material:
        return [clean(station, 230) for station in profile.stationen[:6]]
    out: list[str] = []
    for field, detail in profile_fields(profile, skill_material, 6):
        out.append(f"{field}: {quick_grip(profile, field, detail)}.")
    if len(out) < 4:
        out.extend(profile.stationen)
    return out[:6]


def domain_goal(mf: dict, plugin_dir: Path, profile: ThemenProfil) -> str:
    intro = clean(mf.get("description", "") or first_readme_paragraph(plugin_dir) or profile.rolle, 360)
    if not intro:
        intro = profile.rolle
    return intro.rstrip(".")


def output_hint(profile: ThemenProfil, fields: list[tuple[str, str]]) -> str:
    if profile.skelette:
        return clean("; ".join(item.rstrip(" .") for item in profile.skelette[:2]), 330).rstrip(".")
    if fields:
        names = ", ".join(name for name, _detail in fields[:4])
        return clean(f"Ausgabe entlang der Kernfelder {names}: Kurzvermerk, Prüfmatrix, Entwurf, Fristenblatt oder Fragenliste mit nächstem Schritt", 330).rstrip(".")
    return "Kurzvermerk, Prüfmatrix, Entwurf, Fristenblatt oder Fragenliste mit nächstem Schritt"


PRACTICE_ROUTE_NOISE = (
    "1. scope: was genau soll entschieden",
    "1. rolle und ziel:",
    "1. sachverhalt in einem satz",
    "rolle und ziel klären",
    "wer fragt in welcher rolle",
    "welcher output wird gebraucht",
    "bester nächster arbeitsschritt",
    "starte mit einem arbeitsprodukt",
    "dieser allgemein-skill",
    "fallbild bilden:",
    "rechtsrahmen setzen:",
    "normen-/verfahrensanker:",
    "ausformulierungspflicht und formatstandard",
    "plugin-rahmen:",
    "er führt durch formular",
    "frei nachweisbar",
    "unterlagen: welche dokumente",
    "format: wie ausführlich",
    "welche frist, zuständigkeit, behörde",
    "was soll sofort entstehen",
    "wenn unterlagen vorhanden sind",
    "wenn ein dokument vorliegt",
    "wenn material vorliegt",
    "nutze diesen skill, wenn",
    "normenanker:",
    "normen:",
    "ständige rechtsprechung",
    "dieser arbeitsgang bearbeitet",
    "dieser arbeitsgang hilft",
    "zuständige stelle bestimmen",
    "normenradar:",
    "von der ersten aktenordnung bis zur belastbaren empfehlung",
    "dieser skill bearbeitet vertiefung",
    "entwickelt verhandlungsziel, vergleichskorridor und eskalationspfad",
    "ordnet sachverhalt, norm, beweislast",
    "liefert eine fristen- und risikoampel",
    "ordnet akteninhalt, belege, lücken und nachforderungen",
    "ordnet akteninhalt, belege, luecken und nachforderungen",
    "dieser skill arbeitet",
    "dieser skill erklärt",
    "dieser skill erklaert",
    "dieser skill vertieft",
    "stichwort für die auswahl",
    "stichwort fuer die auswahl",
    "siehe skill-detail",
    "beginne nicht mit einem fragenkatalog",
    "wenn material vorliegt, lies es zuerst",
    "frage höchstens zwei punkte nach",
    "fehlt material vollständig",
    "dieser arbeitsgang macht chronologie und belegmatrix",
    "dieser arbeitsgang macht fristen- und risikoampel",
    "dieser arbeitsgang macht mandantenkommunikation",
    "dieser arbeitsgang ist ein konkreter fachbaustein",
    "kein allgemeiner chat-modus",
    "ausgangspunkt ist immer die konkrete aufgabe",
    "entscheidungspunkte bilden",
    "der output muss als verwertbares arbeitsprodukt",
    "stelle nur rückfragen, die die nächste weiche verändern",
    "problemfokus dieses skills",
    "bleibe beim konkreten titel",
    "routingfragen bleiben hilfsmittel",
    "outputpflicht:",
    "fehlerbremse:",
    "plugin-fokus:",
    "wenn der nutzer nur ein dokument",
    "pflicht-reihenfolge bei stummem upload",
    "konkretes problem:",
    "norm-/quellenanker:",
    "entscheidende weiche:",
    "arbeitsprodukt:",
    "arbeite entlang dieser konkreten prüfungslinie",
    "tatsachen, frist, norm, beweislast",
    "ordne akteninhalt, belege, lücken und nachforderungen",
    "ordne akteninhalt, belege, luecken und nachforderungen",
    "zerlege ergebnis, frist, zuständigkeit, beweislast",
    "zerlegt ergebnis, frist, zuständigkeit, beweislast",
    "entwickle verhandlungsziel, vergleichskorridor",
    "rechne schwellen, beträge, varianten",
    "direkt nutzbares arbeitsprodukt mit prüfpunkten",
    "schnittstellenkarte mit kollisions-",
    "dokumentenmatrix mit nachforderungsliste",
    "einreichungsplan mit form-, portal- und nachweischeck",
    "verhandlungs- oder eskalationslinie mit optionen",
    "berechnungstabelle mit schwellen, annahmen und kontrollfragen",
    "beweislast- und substantiierungsmatrix",
    "auswahlstichwort:",
    "arbeitet innerhalb des plugins",
    "kirchentreu, papsttreu und lehramtsorientiert",
    "ziel ist keine private deutung",
    "~/.claude/",
    "claude.md",
    "erst bremsen, dann prüfen, dann schreiben",
    "dieser hub-skill",
    "dieser arbeitsgang bleibt der prozessrechtliche überblick",
    "modus: --",
    "scope: was genau soll entschieden",
    "rolle und ziel: wer fragt",
    "wird nicht als abstraktes schema beantwortet",
    "unklare tatsachen als rückfrage oder beweispunkt markieren",
    "dokumente einsammeln: bescheid, antrag, vertrag",
    "welches schreiben oder welcher verfahrensschritt liegt vor",
    "dieser arbeitsgang arbeitet als präzises werkzeug",
    "schärft die urheberrechtsprüfung auf den konkreten teilbereich",
    "rolle klären: anspruchsteller",
    "erkannte rolle, zielrichtung und verfahrensstand",
    "anspruchsgrundlage, vertragsschluss, pflichtverletzung oder mangel",
    "normen, nutzerangaben, fristen, belege und verifizierte rechtsprechung",
    "arbeitsweise: erst sachverhalt, norm, frist, zuständigkeit und beweis",
    "rechtsfolge: anspruch, ermessen, verbot, pflicht",
    "taktik: schnellster sinnvoller weg",
    "quellenhygiene:",
    "entscheidungs-/quellenanker:",
    "prüfachse: ordne den konkreten auftrag",
    "trenne sachverhalt, zuständigkeit, zustimmung",
    "transaktionsstruktur, datenraumfund, wertwirkung",
    "auslöser, zugang, fristart, beginn",
    "arbeite zuerst die tragende rechtsfrage heraus",
    "schriftbild:",
    "konkrete normen, konkrete unterlagen, konkrete nächste handlung",
    "p092",
    "pflichtversto",
)


# Diese Formulierungen stammen aus alten Querschnitts-Skills. Sie taugen als
# allgemeine Arbeitsregeln, aber nicht als eigenständige Fachroute. Der
# Generator ersetzt sie durch einen Auftrag aus Fachprofil, Routentitel und
# Plugin-Kontext.
GENERIC_ROUTE_DETAIL_BITS = (
    "welches konkrete ziel soll erreicht oder verhindert werden",
    "wenn ein fachskill eindeutig passt",
    "streitige und unstreitige tatsachen trennen, lückentafel",
    "fristen und zuständigkeit sichern: rechtsbehelfsfrist",
    "einschlägige normen, zuständige stellen, verfahrensart",
    "nur einschlägige normen, verifizierte rechtsprechung",
    "arbeitsmodus: erst gesellschaftsform, organ, beschlussweg",
    "welche einheit ist betroffen und welches recht gilt wirklich",
    "arbeitsmodus: zuerst insolvenzgrund, frist, organpflicht",
    "verfahrensarbeit: zuständigkeit, form, frist, anhörung",
    "unsichere tatsachen als offen markieren und nicht durch modellwissen ersetzen",
    "rolle klären: antragstellende person, behörde, verband",
    "rechtsfrage, gewünschtes produkt, empfänger, frist und entscheidungsschwelle",
    "nächste handlung erzeugen: liefere bei bedarf nachreichungsschreiben",
    "hindernisse benennen: formuliere jedes hindernis konkret",
    "frage nur nach, wenn es die rechtliche weiche wirklich verändert",
    "datei, typ, datum, autor, fassung, signatur, dublette",
    "chronologie, beteiligte, dokumentfundstellen, unstreitige tatsachen",
    "arbeitsmodus: immer verwaltungsakt, frist, widerspruch",
    "welche frist, behörde, vertragspartei, kundengruppe",
    "prüfschritt: fristen, zustellung, rolle, zuständigkeit",
    "symptom: falsche zuständigkeit adressiert",
    "symptom: frist falsch berechnet oder übersehen",
    "form und zuständigkeit prüfen: trenne materielle rechtslage",
    "erstelle für entscheidungsvorlage eine entscheidungsreife fassung",
    "rechtsabteilungsfähige kurzentscheidung mit ampel",
    "fristen, zustellungen, aktenzeichen, anhörungen, mahnungen",
    "fristen, registerstand, veröffentlichungen, vertragslage",
    "beteiligte, rolle und kommunikationskanal klären",
    "bearbeite prozessuale kniffe und rechtsprechungsanker entlang",
    "er führt durch dokumentenmatrix",
    "ziel ist nicht ein abstrakter lexikontext",
    "nach parteien, regelungsziel, definitionen, leistung und gegenleistung",
    "als vollständigen melde- oder dokumentationsvorgang",
    "eine entscheidungsreife fassung mit rubrum oder adressat",
    "eine beweis- und zugriffsakte",
    "vom angegriffenen verfügungssatz oder antrag aus",
    "schriftbild: wenn ein schriftsatz",
    "arbeitsmodus: immer erst",
    "welche behörde handelt:",
    "welche behörde, welches gericht, welches register",
    "prüfachse: ordne den konkreten auftrag",
    "trenne sachverhalt, zuständigkeit, zustimmung",
    "transaktionsstruktur, datenraumfund, wertwirkung",
    "auslöser, zugang, fristart, beginn",
    "arbeite zuerst die tragende rechtsfrage heraus",
    "chronologie, beteiligte, dokumentfundstellen, unstreitige tatsachen",
    "rechtsfrage, gewünschtes produkt, empfänger, frist und entscheidungsschwelle",
)


def is_generic_route_detail(text: str) -> bool:
    # Die Quellskills enthalten teils noch ASCII-Umschriften, während die
    # gerenderten Prompts echte Umlaute verwenden. Die Erkennung muss beide
    # Fassungen gleich behandeln.
    lowered = prose_umlauts(text).lower()
    return any(bit in lowered for bit in GENERIC_ROUTE_DETAIL_BITS)

GENERIC_ROUTE_TITLES = {
    "aktenvermerk",
    "arbeitsprodukt",
    "beschwerdemanagement",
    "chronologie und belegmatrix",
    "fristen- und risikoampel",
    "fristen- und zuständigkeitscockpit",
    "mandantenkommunikation",
    "materielle prüfung",
    "rechtsschutz",
    "allgemein",
    "kaltstart",
    "workflow",
    "pralr - allgemeiner einstieg",
    "audiovisuelle leitentscheidungen sammlung",
}

GENERIC_ROUTE_TITLE_BITS = (
    "allgemeiner einstieg",
    "allgemeiner start",
    "abschlussprodukt und übergabe",
    "automation",
    "automationen",
    "billing",
    "checkliste",
    "copilot",
    "cowork",
    "dashboard",
    "design und ausgabestandard",
    "einsteiger",
    "einstieg in den skill",
    "finder",
    "hauptworkflow",
    "intake",
    "look",
    "mandantenkommunikation",
    "monitoring",
    "policy pack",
    "simulation",
    "skill-verbund",
    "staffing",
    "tooling",
    "training",
    "überblick",
    "normnavigator",
    "fristen, form und zuständigkeit",
    "fristen, form, zuständigkeit",
    "begriffskompass intake",
    "beweislast, darlegungslast und substantiierung",
    "anschauungsmaterial multi-format",
    "anfänger: verhandlung",
    "— allgemein",
    "fehlerkatalog",
    "schulungsmaterial",
    "drift-detektor",
    "schaufenster-pattern",
    "adversarial test",
    "testing",
    "compliance-dokumentation und aktenvermerk",
    "tatbestandsmerkmale, beweisfragen und beleglage",
    "verhandlung, vergleich und eskalation",
    "fristennotiz und nächster schritt",
    "internationaler bezug und schnittstellen",
    "mehrparteienkonflikt und interessenmatrix",
    "formular, portal und einreichungslogik",
    "behörden-, gerichts- oder registerweg",
    "risikoampel, gegenargumente und verteidigungslinien",
    "formulare, portale und einreichungswege",
    "schriftsatz-, brief- und memo-bausteine",
    "sonderfälle und edge cases",
    "sonderfall und edge-case-prüfung",
    "zahlen, schwellen und berechnung",
    "zahlen, schwellenwerte und berechnung",
    "quality gate",
    "einarbeitung:",
    "erstprüfung, rollenklärung und mandatsziel",
    "anfänger",
    "quality-gate",
    "dokumentenmatrix, lückenliste und nachforderung",
    "paragraf 280 inso",
    "workflow",
)

TRUNCATED_ROUTE_TITLE_END = re.compile(
    r"\b(?:Anw|Anwe|Anwen|Praktis|Praktisc|Dashbo|Szenar|Pru|Prue|Deckung F|"
    r"Risiko Ma|Sperre Be|Art|Abs|lit|Anh|vs)\.?$",
    flags=re.IGNORECASE,
)

TECHNICAL_ROUTE_TITLE = re.compile(
    r"\b(?:P\d{3,4}|Dysfunk|Strafr|Vermögensfr|Schr|Personliche|Vermogens)\b|"
    r"^Setzt\s+[A-ZÄÖÜ]{2,}\s+\d+$",
    flags=re.IGNORECASE,
)


def unsuitable_route_title(title: str) -> bool:
    normalized = prose_umlauts(title.strip())
    lowered = normalized.lower()
    return (
        lowered.startswith("/")
        or lowered in GENERIC_ROUTE_TITLES
        or any(bit in lowered for bit in GENERIC_ROUTE_TITLE_BITS)
        or bool(TRUNCATED_ROUTE_TITLE_END.search(normalized))
        or bool(TECHNICAL_ROUTE_TITLE.search(normalized))
    )


def normalized_route_key(text: str) -> str:
    """Behandelt ae/oe/ue- und Umlautfassungen als denselben Routentext."""

    return re.sub(r"\W+", "", prose_umlauts(text).lower())


def practice_route_family(slug: str) -> str:
    """Bildet einen groben Themenstamm, damit kein Einzelmotiv dominiert."""

    ignored = {
        "fachanwalt", "gk", "grosskanzlei", "praxis", "pralr", "recht",
        "rechtlich", "rom", "v392", "vertiefung",
    }
    tokens = [token for token in slug.split("-") if token and not token.isdigit()]
    for token in tokens:
        if token not in ignored and not re.fullmatch(r"\d+", token):
            return token
    return slug


def has_route_term(text: str, *terms: str) -> bool:
    """Prüft Routenschlagwörter ohne Fehltreffer in längeren Wörtern."""

    return any(
        re.search(rf"(?<![\w]){re.escape(term.lower())}(?![\w])", text.lower())
        for term in terms
    )


def practice_route_output(
    profile: ThemenProfil,
    title: str,
    detail: str,
    plugin_slug: str = "",
) -> str:
    """Leitet aus dem konkreten Fachthema ein passendes Lieferstück ab."""

    hay = title.lower()
    if plugin_slug == "gesellschaftsrecht-legal-english":
        if any(word in hay for word in ("anti-dilution", "fully diluted", "waterfall", "financial debt", "earn-out")):
            return "zweisprachige Berechnungsmatrix mit Definitionen, Eingabewerten, Zwischenschritten, Kontrollsumme, gesellschaftsrechtlicher Umsetzung und Mandantenhinweis"
        if any(word in hay for word in ("articles", "shareholders agreement", "term sheet", "reps", "transfer restrictions", "vesting")):
            return "zweisprachige Klausel- und Vollzugsmatrix mit deutschem Rechtsinstitut, englischer Fassung, Form, Beschluss, Registerschritt, Risiko und Rückfallposition"
        return "zweisprachiges Corporate-Memo mit Begriffsklärung, deutscher Rechtswirkung, Aktenfund, Rechen- oder Vollzugsschritt und entscheidungsreifer Empfehlung"
    if plugin_slug == "gesellschaftsrechtliche-treuepflicht":
        if any(word in hay for word in ("ausschluss", "anfechtung", "unterlassung", "registersperre")):
            return "prozessfähige Anspruchs- und Rechtsschutzmatrix mit Antrag, Pflichtkern, Tatsachen, Belegen, Gegenposition, Dringlichkeit und Vollstreckungsziel"
        return "Treuepflichtvotum mit Rechtsform, Mitgliedschaftsrolle, konkreter Pflicht, Interessenabwägung, Zumutbarkeit, Beweislast, Gegenposition und Rechtsfolge"
    if plugin_slug == "dsa-dma-digitalregulierung":
        return "DSA- oder DMA-Arbeitsakte mit Dienste- und Rollenklassifikation, Artikelprüfung, Systembeleg, Grundrechts- und Verhältnismäßigkeitskontrolle, Verantwortlichem, Frist und Behördenprodukt"
    if plugin_slug == "status-navigator-step-plan":
        return "aktualisierbarer Akten-Tracker mit Originalfundstelle, gesichertem Befund, offener Frage, Priorität, Verantwortlichem, Termin, Abhängigkeit und Erledigungsnachweis"
    if plugin_slug == "richter-verwaltungsgericht":
        if any(word in hay for word in ("urteil", "entscheidung", "finale")):
            return "vollständiger richterlicher Entscheidungsentwurf mit Rubrum, Tenor, Streitstoff, Beweiswürdigung, Subsumtion, Kosten, Vollstreckbarkeit und Rechtsmittelbelehrung"
        if "eil" in hay or "80 abs 5" in hay or "paragraf 123" in hay:
            return "vollständiger Eilbeschluss mit bestimmtem Antrag und Tenor, Glaubhaftmachung, Interessen- oder Folgenabwägung, Kosten, Streitwert und Anschlussverfügung"
        return "richterlicher Arbeitsvermerk mit Streitgegenstand, Zulässigkeit, entscheidungserheblichen Tatsachen, Aufklärungsbedarf, Rechtsmaßstab, Tenoroption und nächster Verfügung"
    if profile.key == "rechtsgeschichte":
        return "quellenkritische Darstellung mit Textzeuge, Fassung, Übersetzung, zeitgenössischer Funktion und heutiger Anschlussfrage"
    if profile.key == "kirchenrecht":
        return "kanonistische Arbeitsausgabe mit zuständiger Autorität, maßgeblicher Fassung, Canones, Partikularrecht, Aktenbelegen, Frist, Verfahrensschritt und staatlicher Schnittstelle"
    if profile.key == "medizin":
        if "defektur" in hay:
            return "Defekturakte mit Plausibilitätsprüfung, Herstellungsanweisung, Herstellungs- und Prüfprotokoll, Freigabe, Kennzeichnung, Mengenübersicht und Abweichungsnachweis"
        if "qualitätsmanagement" in hay or "qms" in hay:
            return "freigabefähige SOP mit Zweck, Geltungsbereich, Verantwortung, Ablauf, Kontrollpunkt, Formblatt, Abweichungsweg, Schulungs- und Versionsnachweis"
        if "medikationsanalyse" in hay or "amts" in hay:
            return "Medikationsanalyse mit Einnahmeplan, arzneimittelbezogenen Problemen, Priorität, Beleg, Rückfrage, Beratung und dokumentierter Abstimmung"
        if "apothekenerlaubnis" in hay:
            return "vollständige Erlaubnismappe mit Antragsdaten, persönlichen Nachweisen, Raum- und Betriebsunterlagen, Rückfragenregister und Entscheidungskontrolle"
        if "revision" in hay:
            return "Revisionsmappe mit Prüfpunkt, Ist-Nachweis, Abweichung, Sofortmaßnahme, Verantwortlichem, Frist und formulierter Behördenantwort"
        if "notdienst" in hay or "dienstbereitschaft" in hay:
            return "Dienstbereitschaftsakte mit Plan, Besetzung, Erreichbarkeit, Befreiung oder Anordnung, Ereignisprotokoll, Vergütung und Behördennachweis"
    if profile.key == "ma_finanzierung":
        if "fund formation" in hay or "strukturentscheidung" in hay:
            return "Fund-Formation-Memo mit AIF- und KVG-Einordnung, Vehikel- und Anlegerstruktur, Management- und Carry-Governance, Vertriebsweg, Dokumentenliste, Genehmigungsbedarf und Umsetzungsplan"
        if has_route_term(hay, "kvg", "kagb", "aifm"):
            return "BaFin-fähige Erlaubnis-, Registrierungs- und Auslagerungsmatrix mit Schwellenwerten, Geschäftsleiter- und Eigenmittelnachweisen, Funktionslandkarte, Vertragskontrollen, Antragsunterlagen und Zeitplan"
        if any(word in hay for word in ("antitrust", "gun jumping", "clean team", "fusionskontroll")):
            return "Clean-Team-Protokoll, Informationsklassenmatrix, Freigaberegeln, Vollzugsverbote und kartellrechtliche Eskalationsliste"
        if any(word in hay for word in ("board", "consent", "resolution", "gremien")):
            return "beschlussfähige Gremienvorlage mit Kompetenz, Informationsgrundlage, Interessenkonflikt, Beschlusstext und Vollzugsauftrag"
        if any(word in hay for word in ("closing", "bible", "archiv", "vollzug")):
            return "Closing-Set mit Conditions-Precedent-Status, Deliverables, Unterschriften, Zahlungsnachweisen, Registervollzug und Abschlussindex"
        if any(word in hay for word in ("vdr", "diligence", "datenraum")):
            return "Due-Diligence-Matrix mit Datenraumfundstelle, Befund, Deal-Auswirkung, Nachforderung und Vertragsabbildung"
        if any(word in hay for word in ("auction", "bid", "angebot")):
            return "priorisierte Bid- und Issues-Liste mit Vorgabe aus dem Process Letter, Abweichung, Wertwirkung, Rückfallposition und Freigabe"
        if "beirat" in hay and "zustimmung" in hay:
            return "Zustimmungskatalog mit Geschäftstyp, Schwelle, Berechnung, zuständigem Organ, Beschlussweg, Eilfall, Nachweis und Rechtsfolge eines Verstoßes"
        if "markup" in hay or "key issues" in hay:
            return "priorisierte Key-Issues-Liste und nächste Vertragsfassung mit Klausel, Änderung, Wertwirkung, Risiko, Mandantenziel, Rückfallposition und Freigabe"
        if has_route_term(hay, "ancillary", "tsa", "sla"):
            return "vollzugsfähiger Nebenvertrag mit Servicekatalog, Leistungsniveau, Preis, Laufzeit, Daten- und IP-Regel, Haftung, Exit, Übergabe und offenen Punkten"
        if "deal-fristen" in hay or "cp-kalender" in hay:
            return "Deal-Kalender mit Pflicht, Vertragsfundstelle, Auslöser, Fälligkeit, Owner, Abhängigkeit, Status, Nachweis und Eskalationsdatum"
        if "verbindliche auskunft" in hay or "sanierungsgewinn" in hay:
            return "abstimmungsfähiger Auskunftsantrag mit nicht verwirklichtem Sachverhalt, konkreter Rechtsfrage, Rechtsauffassung, erheblichem Interesse, Gebührenwert, Anlagen und Umsetzungssperre"
    if profile.key == "sozialstatus":
        if any(word in hay for word in ("beitrag", "haftung", "bescheid")):
            return "Status- und Beitragsmatrix mit Zeitraum, Verfügungssatz, Berechnungszeile, Einwand, Beleg, Vollziehungsrisiko und Widerspruchs- oder Eilantrag"
        if any(word in hay for word in ("vertrag", "rahmen", "einzelauftrag")):
            return "Vertragswirklichkeitsvergleich mit Klausel, tatsächlicher Durchführung, Statusindiz, Beleg, Änderungsbedarf und verbleibendem Beitragsrisiko"
        return "begründetes Statusvotum mit Indiziengewichtung, Gegenposition, Beitragsfolge, Beweisplan und nächstem Verfahrensschritt"
    if profile.key == "sozial":
        if "krankengeld" in hay or "folgefeststellung" in hay:
            return "taggenaue AU- und Mitgliedschaftszeitleiste, Krankengeldberechnung, Zurechnungsprüfung, Beleglückenliste und begründeter Widerspruchs- oder Klagebaustein"
        if "merkzeichen" in hay or "gdb" in hay or "mobilität" in hay:
            return "Befund- und Funktionsmatrix mit Einzelbeeinträchtigungen, Wechselwirkungen, Versorgungsmedizin-Maßstab, Merkzeichenprüfung und präzisen Gutachterfragen"
        if "meldeversäumnis" in hay or has_route_term(hay, "minderung", "leistungskürzung"):
            return "Bescheidprüfung mit Meldezweck, Zugang, Belehrung, wichtigem Grund, Härte, Minderungszeitraum, Zahlungswirkung und Eilrechtsschutz"
        if "versandmappe" in hay:
            return "einreichungsfertige Sozialgerichtsmappe mit Antrag, Bescheidkette, Fristenblatt, Befund- und Anlagenregister, Dateinamen, Signatur- und Versandkontrolle"
        if "widerspruch" in hay:
            return "fristwahrender und begründeter Widerspruch mit Verfügungssatz, Leistungsziel, Verfahrensfehlern, Befunden, Beweisanträgen, Anlagen und Nachreichungsvorbehalt"
        if "arbeitsunfall" in hay:
            return "Unfall- und Kausalitätsmatrix mit versicherter Verrichtung, Ereignis, Erstschaden, Befunden, Zeugen, Beweismaß und formulierter Gutachterfrage"
        if "pflegegrad" in hay:
            return "Modul-für-Modul-Abgleich von Pflegeantrag, MD-Gutachten und Alltagsschilderung mit Punktberechnung, Befundstellen, Widersprüchen und Beweisanträgen"
        if "arbeitslosengeld" in hay:
            return "taggenaue Anspruchs- und Berechnungstabelle mit Anwartschaft, Bemessungsrahmen, Entgelt, Ruhens- oder Sperrzeit, Bescheidabweichung und Rechtsbehelf"
    if any(word in hay for word in ("berechn", "betrag", "quote", "rente", "unterhalt", "zugewinn", "honorar")):
        return "nachrechenbare Berechnung mit Eingabewerten, Zwischenschritten, Varianten, Stichtag und Belegspalte"
    if any(word in hay for word in ("klage", "widerspruch", "beschwerde", "einspruch", "antrag", "rechtsmittel")):
        return "frist- und formgerechter Entwurf mit Antrag, tragenden Tatsachen, Beweisangeboten, Anlagen und Einreichungsweg"
    if any(word in hay for word in ("vertrag", "klausel", "vereinbarung", "nda", "spa", "apa", "lizenz")):
        return "verhandlungsfähige Fassung mit Ausgangstext, Änderung, Begründung, Rückfallposition und Vollzugscheck"
    if any(word in hay for word in ("urteil", "beschluss", "verfügung", "tenor", "relation")):
        return "entscheidungsreifer Entwurf mit Tenor oder Verfügungssatz, Streitstoff, Beweiswürdigung und Nebenentscheidungen"
    if re.search(
        r"\b(?:histor\w*|quelle\w*|digest\w*|can\.|canon\w*|alr|pralr|rezeption\w*)\b",
        hay,
    ):
        return "quellenkritische Darstellung mit Textzeuge, Fassung, Übersetzung, zeitgenössischer Funktion und heutiger Anschlussfrage"
    if any(word in hay for word in ("register", "meldung", "anzeige", "portal", "eintragung")):
        return "vollständige Einreichungs- oder Registervorlage mit Zuständigkeit, Pflichtfeldern, Nachweisen, Freigabe und Vollzugskontrolle"
    if any(word in hay for word in ("gutachten", "prüfung", "pruefung", "analyse", "check", "haftung")):
        return "gewichtete Prüfmatrix mit Tatbestandsmerkmalen, Fundstellen, Gegenposition, Beweislast, Risiko und Empfehlung"
    if any(word in hay for word in ("schreiben", "antwort", "stellungnahme", "mahnung", "aufforderung")):
        return "versandfertiges Schreiben mit Betreff, Sachverhaltskern, Rechtsgrund, konkretem Begehren, Frist und Anlagenverzeichnis"
    if any(word in hay for word in ("frist", "zugang", "zustellung", "termin")):
        return f"Fristenblatt zu {title} mit Auslöser, Beginn, Ende, Vorfrist, Beleg, Sofortmaßnahme und Verantwortlichem"
    if any(word in hay for word in ("beweis", "darlegung", "substantiierung", "zeuge", "gutachter")):
        return f"Beweismatrix zu {title} mit Tatfrage, Beweislast, Beweismittel, Fundstelle, Gegenposition und Folge eines offenen Nachweises"
    if any(word in hay for word in ("vergleich", "verhandlung", "mediation", "einigung")):
        return f"Verhandlungsblatt zu {title} mit Ziel, Mindestposition, Tauschmasse, Risiko, Regelungstext und Vollzug"
    if any(word in hay for word in ("akte", "dokument", "chronologie", "unterlagen", "datenraum")):
        return f"Akten- und Belegmatrix zu {title} mit Datum, Urheber, Fundstelle, Widerspruch, Fehlteil und nächstem Bearbeitungsschritt"
    if any(word in hay for word in ("compliance", "kontrolle", "aufsicht", "audit", "governance")):
        return f"Kontrollvermerk zu {title} mit Pflicht, Ist-Nachweis, Abweichung, Risiko, Verantwortlichem, Frist und Freigabe"
    family = workflow_family(profile)
    family_outputs = {
        "source": (
            f"Quellenbefund zu {title} mit Textzeuge, Fassung, Übersetzung, "
            "zeitgenössischer Funktion, Gegenlesart und Rezeptionsspur"
        ),
        "research": (
            f"Teilbefund zu {title} mit Leitfrage, Maßstab, belastbarer Quelle, "
            "Gegenhypothese, Unsicherheitsgrad und nächstem Arbeitsschritt"
        ),
        "production": (
            f"geprüftes Übergabepaket zu {title} mit Eingangsstand, maßgeblicher "
            "Fassung, Qualitätsnachweis, Fehlteilliste, Freigabe und Öffnungsprobe"
        ),
        "drafting": (
            f"Entwurfsbaustein zu {title} mit Geschäftsziel, Rechtswirkung, "
            "Risikozuweisung, Verhandlungsvariante, Freigabe und Vollzugsschritt"
        ),
        "decision": (
            f"Entscheidungsbaustein zu {title} mit Antrag, Aktenfund, Rechtsmaßstab, "
            "Beweisfolge, Gegenposition, Tenoroption und nächster Verfügung"
        ),
        "case": (
            f"Fachvotum zu {title} mit Tatbestandsmerkmalen, Aktenfundstellen, "
            "Beweislast, stärkster Gegenposition, Risiko und ausformulierter Rechtsfolge"
        ),
    }
    return clean(family_outputs[family], 360).rstrip(".")


def professional_route_detail(plugin_slug: str, title: str) -> str:
    """Schärft wiederkehrende Berufsrechtsthemen auf den Berufsträger zu."""

    systems = {
        "berufsrecht-anwaelte": ("BRAO, BORA und RVG", "Mandat, Interessenkollision, Handakte, Frist, Vergütung und Haftung"),
        "berufsrecht-notare": ("BNotO, BeurkG, DONot und GNotKG", "Unabhängigkeit, Beteiligtenwille, Urkundenrolle, Vollzug, Kosten und Dienstaufsicht"),
        "berufsrecht-patentanwaelte": ("PAO, BOPA und den Verfahrensregeln von DPMA, BPatG und EPA", "Schutzrechtsauftrag, Priorität, Frist, Vertretung, Vergütung und Haftung"),
        "berufsrecht-steuerberater": ("StBerG, BOStB, StBVV und AO", "Mandatsumfang, Bekanntgabe, Frist, Handakte, Gebühren, Berichtigung und Haftung"),
        "berufsrecht-wirtschaftspruefer": ("WPO, BS WP/vBP, HGB und den Vorgaben von WPK und APAS", "Unabhängigkeit, Auftragsannahme, Prüfungsakte, Bericht, Honorar und Berufsaufsicht"),
    }
    system = systems.get(plugin_slug)
    if not system:
        return ""
    norms, objects = system
    hay = title.lower()
    if "frist" in hay:
        return f"Baue aus {norms} und der konkreten Zustellung oder Verfahrenshandlung ein Fristenblatt mit Beginn, Ende, Vorfrist, Verantwortlichem, Gegenkontrolle, Ausgangsnachweis und Wiedereinsetzungsreserve; ordne dabei {objects}"
    if any(word in hay for word in ("akten", "dokument", "datenraum")):
        return f"Ordne die Unterlagen nach {norms} in Original, Bearbeitungsstand, Frist, Zugriffsrecht, Verschwiegenheit, Aufbewahrung und Herausgabe; sichere für {objects} einen prüfbaren Akten- und Übergabenachweis"
    if any(word in hay for word in ("honorar", "gebühr", "vergütung")):
        return f"Prüfe Auftrag, Vergütungsabrede, gesetzlichen Gebührenmaßstab, Vorschuss, Fälligkeit, Abrechnung, Aufklärung und Einwendungen nach {norms}; rechne {objects} mit belegten Werten nach"
    if any(word in hay for word in ("haftpflicht", "haftung")):
        return f"Bestimme Pflichtenkreis und Auftragsumfang nach {norms}, trenne Pflichtverletzung, Kausalität und Schaden, sichere Verjährung und Versicherungsanzeige und baue für {objects} eine belastbare Anspruchs- und Verteidigungsmatrix"
    if any(word in hay for word in ("berufsgericht", "disziplinar", "pflichtverletzung")):
        return f"Zerlege den Vorwurf nach {norms} in konkrete Berufspflicht, Tatsachenbasis, Verschulden, Anhörung, Akteneinsicht, mögliche Maßnahme und Rechtsbehelf; ordne {objects} den einzelnen Vorwürfen und Belegen zu"
    if "berufsausübungsgesellschaft" in hay:
        return f"Prüfe nach {norms} zulässige Gesellschafter und Geschäftsleitung, berufliche Unabhängigkeit, Mehrheit, Firma, Register, Versicherung, interne Konfliktregeln und Vollzug der Berufsausübungsgesellschaft"
    if "cross-border" in hay:
        return f"Bestimme Herkunftsberuf, Niederlassung oder vorübergehende Dienstleistung, Berufsbezeichnung, Registrierung, Kollisions- und Verschwiegenheitsregeln sowie Zuständigkeit nach {norms}; halte lokale Beratungspflichten und Haftungsdeckung getrennt fest"
    if "entscheidung" in hay:
        return f"Verdichte {objects} anhand von {norms} zu einer Entscheidungsvorlage mit gesichertem Sachverhalt, Pflichtenkreis, Handlungsalternativen, Berufsrisiko, Kosten, Freigabe und dokumentiertem nächsten Schritt"
    return f"Bearbeite {title} anhand von {norms}: ordne {objects} nach sicherer Tatsache, Berufspflicht, Nachweis, Gegenposition, Risiko und nächster Handlung"


def medical_route_detail(title: str) -> str:
    """Liefert für apothekennahe Routentitel einen wirklichen Facharbeitsgang."""

    hay = title.lower()
    routes = (
        (("defektur", "100er"), "Trenne Rezeptur, Defektur und Fertigarzneimittel; prüfe Herstellungsumfang, Vorratshaltung, Plausibilität, Herstellungsanweisung, Prüfprotokoll, Freigabe, Kennzeichnung und die mengenbezogene Defekturgrenze anhand der ApBetrO-Unterlagen"),
        (("qualitätsmanagement",), "Baue das Qualitätsmanagement aus verbindlichen SOPs für Herstellung, Prüfung, Lagerung, Abgabe, Beratung, Reklamation, Rückruf, Temperaturabweichung und Selbstinspektion; sichere Version, Freigabe, Schulung, Formblatt, Abweichung und Wirksamkeitskontrolle"),
        (("heimversorgung",), "Prüfe Heimversorgungsvertrag, behördliche Genehmigung, freie Apothekenwahl, Belieferungsablauf, Beratung, Notfallversorgung, Dokumentation, Bewohnerdaten und Abrechnung als zusammenhängenden Versorgungsvorgang"),
        (("mietvertrag", "apothekenstandort"), "Prüfe Mietzweck, Genehmigungsfähigkeit der Räume, Konkurrenzschutz, Betriebspflicht, Umbau- und Rückbaukosten, Übergabe, Laufzeit, Optionen sowie das Risiko einer versagten oder verzögerten Apothekenerlaubnis"),
        (("substitution", "aut-idem"), "Gleiche Verordnung, Aut-idem-Kennzeichnung, Wirkstoff, Wirkstärke, Darreichungsform, Packungsgröße, Rabattvertrag, Lieferfähigkeit, pharmazeutische Bedenken, Dokumentation und mögliches Retaxationsrisiko ab"),
        (("amts", "medikationsanalyse"), "Erfasse vollständige Medikation, Diagnosen, Einnahmeplan, Doppelverordnungen, Interaktionen, Kontraindikationen, Adhärenz und Beratungsnachweis; formuliere priorisierte Rückfragen an Arzt und Patient ohne eigenmächtige Therapieänderung"),
        (("apothekenerlaubnis",), "Prüfe Antragsteller, Approbation, Zuverlässigkeit, gesundheitliche Eignung, Besitz- und Leitungsverhältnisse, Betriebsräume, Mehrbetriebsgrenzen, Unterlagen, Behördenrückfragen und Nebenbestimmungen des Erlaubnisbescheids"),
        (("apothekenrevision",), "Baue aus Erlaubnis, Raumplan, Personal-, Rezeptur-, Defektur-, Betäubungsmittel-, Temperatur-, Beratungs- und Qualitätsunterlagen einen Revisionsordner; ordne jeden Befund nach Nachweis, Sofortkorrektur und Behördenantwort"),
        (("apothekenübliche waren",), "Ordne das Produkt nach Zweckbestimmung und Verkehrsauffassung ein, trenne Arzneimittel, Medizinprodukt, Lebensmittel, Kosmetikum und apothekenübliche Ware und prüfe Sortiment, Werbung, Beratung, Bezugsnachweis und aufsichtsrechtliche Reaktion"),
        (("apothekenbetrieb", "dokumentenintake"), "Ordne Erlaubnis, Betriebseröffnung, Raum- und Personalunterlagen, Verantwortlichkeiten, Qualitätsmanagement, Rezeptur und Defektur, Betäubungsmittel, Temperatur, Beratung, Notdienst und Behördenkorrespondenz in einen prüfbaren Betriebsaktenindex"),
        (("apothekenbetriebsordnung", "grundpflichten"), "Gleiche Leitung, pharmazeutisches Personal, Räume, Hygiene, Qualitätsmanagement, Herstellung, Prüfung, Lagerung, Abgabe, Information, Beratung und Dokumentation mit dem tatsächlichen Apothekenbetrieb ab und priorisiere Abweichungen"),
        (("dienstbereitschaft", "notdienst"), "Prüfe Dienstbereitschaftsplan, Befreiung oder Anordnung, Erreichbarkeit, personelle Besetzung, Zugang, Arzneimittelversorgung, Dokumentation, Vergütung und behördliche Kommunikation für jeden betroffenen Zeitraum"),
        (("rezept", "retax"), "Rekonstruiere Verordnung, Abgabe, Rahmenvertragsvorgaben, Rabattvertrag, Genehmigung, Zuzahlung, Taxierung, Datenübermittlung und Beanstandungsgrund; berechne Retaxationsbetrag, Einwendungsfrist und benötigte Belege"),
        (("beschwerdemanagement",), "Rekonstruiere Abgabe, Beratung, Produkt, Charge, Verordnung, Gesprächsverlauf und behaupteten Schaden; sichere Kassen- und Dokumentationsdaten, trenne Qualitätsabweichung von Kommunikationsfehler und formuliere eine sachliche Antwort mit Eskalationsweg"),
        (("räume", "ausstattung"), "Gleiche Raumplan, Nutzflächen, Rezeptur, Labor, Lagerung, Temperaturführung, Hygiene, Geräte, Wartungsnachweise und tatsächlichen Betriebsablauf mit den Anforderungen der ApBetrO ab und bereite Mängelbeseitigung sowie Behördennachweis vor"),
    )
    for terms, detail in routes:
        if all(term in hay for term in terms):
            return detail
    return ""


def plugin_route_detail(plugin_slug: str, title: str) -> str:
    """Schärft Fachrouten für Plugins mit eigener Terminologie und Prüflogik."""

    hay = title.lower()
    if plugin_slug == "aussenwirtschaft-zoll-sanktionen" and "zollschuldentstehung" in hay:
        return (
            "Trenne die reguläre Einfuhrzollschuld nach UZK Artikel 77 von der Zollschuld "
            "wegen Pflichtverletzung nach UZK Artikel 79. Rekonstruiere Zollanmeldung, "
            "Überlassung, besonderes Verfahren, verletzte Pflicht, Tatzeit, Warenwert, "
            "Abgabenberechnung und alle als Zollschuldner in Betracht kommenden Personen; "
            "ordne Wissen, Beteiligung, Gesamtschuld, Nacherhebung, Erlass oder Erstattung "
            "je Person den konkreten Zoll- und Beförderungsunterlagen zu"
        )
    if plugin_slug == "ordnungswidrigkeitenrecht" and all(
        bit in hay for bit in ("außenwirtschaft", "beweis")
    ):
        return (
            "Bestimme den konkreten Bußgeldtatbestand mit seiner Verweisung auf AWG, AWV "
            "oder unmittelbar geltendes Unionsrecht und sichere die am Tattag geltende "
            "Fassung. Ordne Ausfuhr, Verbringung oder sonstige Handlung, Verbots- oder "
            "Genehmigungslage, Verantwortlichkeit, Vorsatz oder Fahrlässigkeit, behördliche "
            "Datenquelle und Einlassung je Tatmerkmal zu; formuliere danach konkrete "
            "Beweisrüge, Beweisantrag oder Einstellungsargument und prüfe die Verjährung"
        )
    if plugin_slug == "insiderrecht-compliance" and any(
        bit in hay for bit in ("familienangehörige", "nahestehende personen")
    ):
        return (
            "Bestimme zuerst, ob die betroffene Person nach Artikel 3 Absatz 1 Nummer 26 MAR "
            "einem Mitglied des Leitungs- oder Aufsichtsorgans oder einer sonstigen Führungskraft "
            "nahesteht. Ordne Instrument, Emittent, Geschäft, Datum, Schwellenwert und Aggregation "
            "nach Artikel 19 MAR zu; prüfe schriftliche Belehrung und Aufbewahrung nach Artikel 19 "
            "Absatz 5 MAR sowie ein mögliches Handelsverbot oder Insiderwissen gesondert. Liefere "
            "eine belegte Meldeentscheidung, gegebenenfalls die Meldedaten und eine Konflikt- und Sperrnotiz"
        )
    if plugin_slug == "gesellschaftsgruender" and "sozialversicherungs-status" in hay:
        return (
            "Prüfe den Status des Gesellschafter-Geschäftsführers nach Paragraf 7 SGB IV anhand "
            "der rechtlich durchsetzbaren Einflussmacht: Kapitalanteil, Stimmrechte, satzungsfeste "
            "umfassende Sperrminorität, Weisungsrechte, Abberufung und tatsächliche Vertragsdurchführung. "
            "Trenne Statusfeststellung nach Paragraf 7a SGB IV, Beitragsfolgen, Säumniszuschläge und "
            "Lohnsteuer; liefere eine Unterlagenmatrix, eine belastbare Statusprognose und den passenden Antrag"
        )
    if plugin_slug == "aufsichtsrat-ag-se-praxis" and any(
        bit in hay for bit in ("mutterschutz", "elternzeit", "pflege 84")
    ):
        return (
            "Lege Ersuchen des Vorstandsmitglieds, Verhinderungsgrund, gewünschten Zeitraum, "
            "Vorstandsbesetzung, Ressortabdeckung und Dienstvertrag nebeneinander. Bereite den "
            "Aufsichtsratsbeschluss nach Paragraf 84 Absatz 3 AktG mit Beginn und Ende, gesicherter "
            "Leitungs- und Vertretungsfähigkeit, Wiederbestellung, Registermeldung, Vergütung und "
            "Kommunikation vor; trenne die organschaftliche Bestellung strikt vom Dienstvertrag"
        )
    if plugin_slug == "handelsregister-praxis" and any(
        bit in hay for bit in ("rechtspfleger", "registerrichter", "geschäftsstelle")
    ):
        return (
            "Bestimme Registerart, örtlich zuständiges Registergericht, konkrete Eintragung und "
            "funktionelle Zuständigkeit nach FamFG und RPflG. Trenne materielle Registerprüfung, "
            "richterlichen Vorbehalt, Rechtspflegergeschäft und Vollzug der Geschäftsstelle; formuliere "
            "Anmeldung, Zwischenverfügungsantwort oder Beschwerde adressatengerecht und führe Notarzeugnis, "
            "Beschlüsse, Vertretungsnachweise, Einreichungsdatei und Registerbekanntmachung in einer Vollzugsliste"
        )
    if plugin_slug == "urteilsbauer-relationsmacher" and any(
        bit in hay for bit in ("rechtspfleger", "behörden-, gerichts- oder registerweg")
    ):
        return (
            "Ordne den Vorgang nach Verfahrensgegenstand, Gerichtszweig, sachlicher und örtlicher "
            "Zuständigkeit sowie funktioneller Zuständigkeit von Richter, Rechtspfleger und Geschäftsstelle. "
            "Prüfe Antrag, Beteiligte, Rechtsschutzform, Vorlagepflichten, Anhörung, Entscheidung und Rechtsbehelf; "
            "liefere einen aktennahen Zuständigkeitsvermerk und den nächsten verfügungsreifen Text"
        )
    if plugin_slug == "arbeitsrecht":
        if "freistellungsklausel" in hay or "5azr10825" in hay:
            return (
                "Lege Arbeitsvertrag, Freistellungserklärung, Kündigung, Tätigkeitsbild und "
                "Dienstwagenabrede nebeneinander. Prüfe die formularmäßige Freistellungsbefugnis "
                "nach Paragraf 307 BGB und den konkreten Beschäftigungsanspruch; BAG, Urteil vom "
                "25.03.2026 - 5 AZR 108/25 verlangt bei einer pauschalen Freistellungsklausel eine "
                "Interessenprüfung und trägt die Freistellung nicht allein wegen irgendeiner Kündigung. "
                "Behandle Widerruf der Privatnutzung, Vergütung und Nutzungsausfall gesondert"
            )
        if "aufhebungsvertrag" in hay:
            return (
                "Entwirf oder prüfe den Aufhebungsvertrag ab Beendigungsdatum rückwärts: "
                "Schriftform nach Paragraf 623 BGB, Abfindung und Fälligkeit, Freistellung, Urlaub, "
                "variable Vergütung, Zeugnis, Rückgabe, Ausgleichsklausel, Wettbewerbsbindung, "
                "Steuer- und Sperrzeitrisiko. Rekonstruiere die Verhandlungssituation nach BAG, "
                "Urteilen vom 07.02.2019 - 6 AZR 75/18 und 24.02.2022 - 6 AZR 333/21, ohne "
                "Widerrufsrecht oder Unwirksamkeit allein aus sofortiger Annahme abzuleiten"
            )
    if plugin_slug == "nachbarschaftsstreit-pruefer" and "überhang" in hay:
        return (
            "Dokumentiere Baum oder Strauch, Grundstücksgrenze, eindringende Zweige oder Wurzeln, "
            "konkrete Nutzungsbeeinträchtigung, Fotos, Messpunkte, Eigentümer und bisherigen Zugang. "
            "Prüfe Selbsthilferecht und angemessene Beseitigungsfrist nach Paragraf 910 BGB, "
            "Beseitigungs- oder Unterlassungsanspruch nach Paragraf 1004 BGB sowie entgegenstehende "
            "naturschutz- und baumschutzrechtliche Vorgaben; liefere Aufforderung, Beweisplan und "
            "eine sichere Handlungsgrenze für den Rückschnitt"
        )
    if plugin_slug == "mietrecht" and "amtlichen" in hay:
        return (
            "Behandle den amtsgerichtlichen Mietfall anhand des konkreten Begehrens: Wohnraummiete "
            "streitwertunabhängig nach Paragraf 23 Nummer 2a GVG, Geschäftsraummiete nach allgemeiner "
            "Wertzuständigkeit. Prüfe Antrag, Vertragsart, Fälligkeit, Kündigung oder Mangel, "
            "Darlegungslast, Beweisangebot, Schonfrist- und Sozialklauselrisiko und erstelle eine "
            "klage- oder verteidigungsfähige Risikoampel mit beziffertem Antrag"
        )
    if plugin_slug == "fachanwalt-miet-wohnungseigentumsrecht" and "agg" in hay:
        return (
            "Prüfe die Benachteiligung bei Anbahnung, Abschluss oder Durchführung des Mietverhältnisses "
            "nach den Paragrafen 1, 2, 19 bis 22 AGG: geschütztes Merkmal, Massengeschäft oder "
            "Wohnraumtatbestand, Ausnahmen des Paragraf 19 Absatz 3 und 5 AGG, Rechtfertigung, "
            "Indizien, Beweislastwechsel, Frist und Rechtsfolge. Trenne Auskunft, Unterlassung, "
            "Vertragsschlussbegehren und Entschädigung und sichere Inserat, Auswahlkommunikation und Vergleichsfälle"
        )
    if plugin_slug == "aufsichtsrat-ag-se-praxis" and "geschäftsordnung vorstand" in hay:
        return (
            "Gleiche Satzung, Vorstandsbestellung, Geschäftsverteilung und Aufsichtsratsbeschlüsse ab. "
            "Regle Gesamtleitung nach Paragraf 76 AktG, Geschäftsordnung und Beschlussfassung nach "
            "Paragraf 77 AktG, Vertretung nach Paragraf 78 AktG, Berichte nach Paragraf 90 AktG und "
            "Zustimmungsvorbehalte nach Paragraf 111 Absatz 4 AktG; trenne interne Geschäftsführungsbefugnis "
            "von äußerer Vertretungsmacht und liefere beschlussfähige Fassung samt Konflikt- und Eilregel"
        )
    if plugin_slug == "vereinsrecht-vereinsmanager" and "geschäftsordnung vorstand" in hay:
        return (
            "Leite die Geschäftsordnung aus Satzung, Vorstandszuschnitt und Vereinsregister ab. "
            "Ordne Vertretung nach Paragraf 26 BGB, Bestellung und Abberufung nach Paragraf 27 BGB, "
            "Beschlusszuständigkeit der Mitgliederversammlung nach Paragraf 32 BGB und zulässige "
            "Satzungsabweichungen nach Paragraf 40 BGB; regle Ressorts, Einberufung, Mehrheiten, "
            "Interessenkonflikte, Protokoll, Ausgabenfreigaben und Außenkommunikation ohne die Satzung zu überschreiben"
        )
    if plugin_slug == "richter-bverfg-verfassungsbeschwerden" and any(
        bit in hay for bit in ("entscheidungsvorschlag", "fachgerichtliche entscheidung", "nichtannahmebeschluss")
    ):
        return (
            "Entwirf die verfassungsgerichtliche Entscheidung aus Beschwerdegegenstand, Zulässigkeit, "
            "Annahmevoraussetzungen der Paragrafen 93a und 93b BVerfGG und tragender Grundrechtsprüfung. "
            "Bei Nichtannahme keine Sachentscheidung vortäuschen; bei Stattgabe Entscheidungsform und "
            "Rechtsfolge nach Paragraf 95 BVerfGG bestimmen. Fachgerichtliche Rechtsanwendung nur am "
            "spezifischen Verfassungsrecht messen und Rubrum, Tenor, Gründe sowie Kostenfolge widerspruchsfrei halten"
        )
    if plugin_slug == "richter-arbeitsgericht":
        if "zahlungsklage" in hay:
            return (
                "Prüfe den Zahlungsantrag nach Zeitraum, Brutto- oder Nettobegehren, Fälligkeit, "
                "Ausschlussfrist, Erfüllung, Aufrechnung und Verzinsung. Ordne Arbeitsvertrag, Tarif- "
                "oder Betriebsvereinbarung, Abrechnungen und Arbeitszeitbelege den einzelnen Monatsbeträgen "
                "zu; steuere Substantiierung, Hinweis und Beweisaufnahme nach Paragraf 46 Absatz 2 ArbGG "
                "in Verbindung mit der ZPO und berücksichtige Paragraf 12a ArbGG bei der Kosteninformation"
            )
        if any(bit in hay for bit in ("beschlussverfahren", "einstweilige verfügung", "entscheidungsvorschlag", "finale entscheidung")):
            return (
                "Bestimme Urteils- oder Beschlussverfahren, Beteiligte, Anträge und Entscheidungsreife "
                "nach ArbGG, bevor ein Ausspruch formuliert wird. Im Beschlussverfahren Amtsermittlung "
                "und Beteiligtenstellung nach Paragrafen 80 und 83 ArbGG, im Eilverfahren Verfügungsanspruch "
                "und Verfügungsgrund, im Urteil Schlüssigkeit, Erheblichkeit und Beweislast trennen; "
                "Tenor, Tatbestand, Gründe, Kosten und Rechtsmittel auf die richtige Verfahrensart zuschneiden"
            )
    if plugin_slug in {"grosskanzlei-corporate-ma", "mittelstand-corporate-ma"}:
        large = plugin_slug == "grosskanzlei-corporate-ma"
        if "closing bible" in hay:
            if large:
                return (
                    "Führe jede Condition Precedent, Regulatory Clearance, Funds-Flow-Position, "
                    "Corporate Approval, Unterschrift und notarielle oder registerliche Vollzugshandlung "
                    "auf Vertragsfundstelle, Rechtsordnung, Owner, Fälligkeit und Erfüllungsbeleg zurück. "
                    "Schließe aus dem mehrspurigen Signing und Closing eine versionierte Closing Bible "
                    "mit Index, Executed Copies, Legal Opinions, Zahlungsnachweisen und offenen Post-Closing-Punkten"
                )
            return (
                "Gleiche beim mittelständischen Unternehmenskauf Kaufpreiszahlung, Bankablösungen, "
                "Gesellschafterdarlehen, notarielle Abtretung, Gesellschafterliste, Geschäftsführerwechsel, "
                "Kunden- und Lieferanten-Consents sowie Schlüsselübergaben mit SPA und Closing Checklist ab. "
                "Sichere zu jedem Punkt Originalunterschrift, Zahlungs- oder Registerbeleg und eine klare "
                "Post-Closing-Verantwortung, damit der laufende Betrieb nicht zwischen Zuständigkeiten hängen bleibt"
            )
        if any(bit in hay for bit in ("vdr", "datenraum-aufbau", "datenraum aufbau")):
            if large:
                return (
                    "Klassifiziere jedes VDR-Dokument nach Gesellschaft, Rechtsordnung, Workstream, Zeitraum, "
                    "Vertraulichkeitsstufe und Versionsstand; verknüpfe Red Flag und Datenlücke mit Q&A, "
                    "Materiality, Wertwirkung und Abbildung in SPA, Disclosure Letter, W&I-Police oder Closing Condition. "
                    "Führe privilegierte, Clean-Team- und personenbezogene Unterlagen in getrennten Zugriffswegen"
                )
            return (
                "Baue den Datenraum aus Register- und Gesellschaftsunterlagen, Jahresabschlüssen, Steuern, "
                "Banken, wesentlichen Verträgen, Personal, Immobilien, Schutzrechten und Streitigkeiten auf. "
                "Kennzeichne fehlende Originale, nicht gelebte Vertragsstände und inhaberabhängige Abreden; "
                "übersetze jeden Befund in Nachforderung, Kaufpreispunkt, Garantie, Freistellung oder Vollzugshandlung"
            )
        if large and "authority matrix" in hay:
            return (
                "Erstelle je Transaktionsschritt eine Authority Matrix aus Gesellschaft, Rechtsordnung, Organ, "
                "Satzungs- oder Vertragsgrundlage, Mehrheit, Quorum, Interessenkonflikt, Zeichnungsbefugnis, "
                "Form und Wirksamkeitszeitpunkt. Gleiche Board-, Shareholder-, Investment-Committee-, Lender- "
                "und Regulatory-Approvals mit Signing- und Closing-Reihenfolge ab"
            )
        if large and "cap table" in hay:
            return (
                "Rekonstruiere Legal Ownership und wirtschaftliche Beteiligung stichtagsbezogen aus Register, "
                "Gesellschafterliste, Anteilskauf, Optionen, Wandeldarlehen, VSOP und Treuhand. Prüfe Fully-Diluted- "
                "Nenner, Verwässerung, Verfügungsbeschränkungen, wirtschaftlich Berechtigte und die Ownership Chain "
                "bis zur obersten kontrollierenden Person; markiere jede Differenz zwischen Cap Table und Rechtsnachweis"
            )
        if large and "data protection transfer" in hay:
            return (
                "Ordne im Share- oder Asset-Deal Datenbestand, Verantwortlichenrolle, Zweck, Rechtsgrundlage, "
                "Betroffeneninformation, Auftragsverarbeitung, Drittlandtransfer, Löschpflicht und Sicherheitsmaßnahme. "
                "Trenne Due-Diligence-Zugriff, Signing, Closing und Migration; bilde Datenlücke in Clean-Team-Regel, "
                "Covenant, Garantie, Freistellung und Übergabeplan ab"
            )
        if large and "mandatsannahme" in hay:
            return (
                "Prüfe vor Öffnung des Datenraums Parteien, verbundene Unternehmen, Finanzierer, Management, "
                "Bieter und frühere Mandate auf Konflikt; sichere Scope, Rechtsordnungen, Insider- und Clean-Team-Status, "
                "Vertraulichkeit, Haftungsrahmen, Budget, Staffing, lokale Berater und Freigaben. Liefere dokumentierte "
                "Annahmeentscheidung, Engagement Letter und eine Liste der bis zur Freigabe gesperrten Arbeiten"
            )
        if "rechtsprechungsrecherche" in hay:
            if large:
                return (
                    "Formuliere aus dem konkreten Deal-Befund je Rechtsordnung und Workstream eine enge Rechtsfrage, "
                    "priorisiere Gesetz, amtliche Entscheidung und belastbaren Fachbeleg und prüfe Instanz, Datum, "
                    "Aktenzeichen, Verfahrensstand sowie tragende Passage. Liefere eine zitierfähige Quellenkarte mit "
                    "Sachverhaltsvergleich, Gegenansicht, Deal-Auswirkung und Umsetzung in SPA, Disclosure, Gremienpapier, "
                    "Legal Opinion oder Closing-Schritt; kennzeichne offene lokale Beratung ausdrücklich"
                )
            return (
                "Formuliere aus dem konkreten Unternehmenskauf eine enge deutsche Rechtsfrage, prüfe zuerst Gesetz und "
                "amtliche Entscheidung auf Gericht, Datum, Aktenzeichen, Verfahrensstand und tragende Passage und "
                "übertrage den Rechtssatz erst nach Vergleich mit Gesellschaft, Vertrag und Vollzugslage. Liefere einen "
                "knappen Entscheidungsvermerk mit belastbarer Quelle, Gegenansicht, wirtschaftlicher Auswirkung und "
                "konkreter Umsetzung in Gesellschafterbeschluss, Kaufvertrag, Offenlegung oder Closing-Liste"
            )
    if plugin_slug == "fachanwalt-sozialrecht":
        if "erwerbsminderungsrente" in hay:
            return (
                "Prüfe Versicherungsverlauf, Wartezeit und Pflichtbeitragszeiten stichtagsbezogen und übersetze jeden "
                "Befund in quantitatives Leistungsvermögen auf dem allgemeinen Arbeitsmarkt. Trenne volle, teilweise "
                "und arbeitsmarktbedingte Erwerbsminderung nach Paragraf 43 SGB VI, Berufsschutz nach Paragraf 240 "
                "SGB VI, Wegefähigkeit, Summierung ungewöhnlicher Einschränkungen und Gutachtenwidersprüche; formuliere "
                "konkrete Befundanforderungen, Beweisfragen und einen bezifferten Bescheid-, Widerspruchs- oder Klagebaustein"
            )
        if "arbeitsunfall" in hay:
            return (
                "Baue die haftungsbegründende Kausalkette nach Paragraf 8 SGB VII aus versicherter Tätigkeit, "
                "konkreter Verrichtung, Unfallereignis und Gesundheitserstschaden. Gleiche Unfallanzeige, "
                "Durchgangsarztbericht, Erstbefunde, Vorerkrankungen, Bildgebung und Zeugen ab; trenne Vollbeweis "
                "der Tatsachen vom Wahrscheinlichkeitsmaßstab der Kausalität und formuliere Gutachterfragen sowie "
                "gerichtliche Ermittlungsanträge nach Paragraf 103 SGG"
            )
        if "vergleich vor sozialgericht" in hay:
            return (
                "Grenze den Streitgegenstand und die Reichweite der behördlichen Bindung ab, bevor ein Vergleich "
                "nach Paragraf 101 SGG formuliert wird. Regle Leistungszeitraum, medizinische oder wirtschaftliche "
                "Voraussetzungen, Neubescheidung oder Zahlung, Zinsen, Kosten, Erledigung, Widerrufsvorbehalt und "
                "Vollstreckbarkeit so bestimmt, dass keine unbeabsichtigten Folgezeiträume oder Parallelansprüche erledigt werden"
            )
        if "wohngeld" in hay:
            return (
                "Prüfe zuerst, ob wirklich Wohngeld nach dem WoGG oder eine andere Sozialleistung betroffen ist. "
                "Bei Wohngeld Haushaltsmitglieder, zu berücksichtigende Miete oder Belastung, Gesamteinkommen, "
                "Ausschlusstatbestände und Bewilligungszeitraum berechnen; Rechtsbehelf und Verwaltungsrechtsweg "
                "nach VwGO aus Bescheid und Landesrecht bestimmen, nicht schematisch das SGG anwenden"
            )
        if "fristen" in hay:
            return (
                "Erfasse Bescheiddatum, tatsächlichen Zugang, Rechtsbehelfsbelehrung, Widerspruch, Abhilfe- oder "
                "Widerspruchsbescheid und Gerichtseingang. Berechne Monats- und Jahresfrist nach Paragrafen 64, 66 "
                "und 84 SGG, dokumentiere elektronischen oder postalischen Zugang und führe Vorfrist, Verantwortlichen, "
                "Vieraugenkontrolle, Wiedereinsetzungstatsachen und fristwahrenden Mindestschriftsatz in einem Fristenblatt"
            )
    if plugin_slug == "selbstvertreter-sozialgericht":
        if "arbeitsunfall" in hay:
            return (
                "Schreibe in Alltagssprache eine Zeitleiste: versicherte Arbeit, genaue Verrichtung, plötzliches "
                "Ereignis, erste Beschwerden, erste Behandlung und weiterer Verlauf. Ordne Unfallanzeige, "
                "Durchgangsarztbericht, Namen der Zeugen und Befunde zu und formuliere für Berufsgenossenschaft oder "
                "Sozialgericht klar, welche Tatsache nach Paragraf 8 SGB VII noch ermittelt und welcher Arzt befragt werden soll"
            )
        if any(bit in hay for bit in ("eilantrag", "einstweilig", "paragraf 86b")):
            return (
                "Lege Bescheid, Widerspruch und akute Notlage vor und formuliere in klarer Alltagssprache, welche "
                "Leistung bis wann benötigt wird. Trenne Anordnungsanspruch und Anordnungsgrund nach Paragraf 86b SGG, "
                "belege Kontostand, Miete, Versorgung oder Gesundheitsgefahr und liefere unterschriftsreifen Haupt- "
                "und Hilfsantrag samt Anlagenliste und Hinweis auf noch beizuziehende Verwaltungsakten"
            )
        if "anlagen zur klage" in hay:
            return (
                "Ordne Ausgangsbescheid, Widerspruch, Widerspruchsbescheid, Zugangsnachweise, Befunde und sonstige "
                "Belege nach der ersten Erwähnung in der Klage. Vergib neutrale Anlagenzeichen, erhalte jedes mehrseitige "
                "Dokument als Einheit, schwärze unnötige Fremddaten nicht im Original und gleiche Dateiname, Anlagenverzeichnis, "
                "Textverweis, Lesbarkeit und Seitenfolge vor der Einreichung vollständig ab"
            )
    if plugin_slug == "fachanwalt-verwaltungsrecht" and "vergleich" in hay:
        return (
            "Prüfe zunächst, ob Behörde und Beteiligte über den Gegenstand verfügen dürfen und ob ein öffentlich-rechtlicher "
            "Vertrag nach den Paragrafen 54 und 55 VwVfG oder ein gerichtlicher Vergleich nach Paragraf 106 VwGO gemeint ist. "
            "Regle Verwaltungsakt, Vollzug, Genehmigungen, Drittbetroffenheit, Kosten, Fristen, Rücknahme der Rechtsbehelfe, "
            "Erledigung und Vollstreckbarkeit bestimmt; sichere Zuständigkeit, Vertretungsmacht und interne Behördenfreigabe"
        )
    if plugin_slug == "fachanwalt-versicherungsrecht":
        if "do deckungsabwehr" in hay or "d&o" in hay:
            return (
                "Lege Anspruchserhebung, Police, AVB, Nachträge und Ablehnung in der zeitlich richtigen Fassung "
                "nebeneinander. Prüfe versicherte Person und Tätigkeit, Claims-made-Zeitpunkt, Rückwärtsdeckung, "
                "Nachmeldefrist, Kontinuität, Ausschluss, Abwehrkosten und Obliegenheiten; keine feste Nachmeldefrist "
                "unterstellen. Paragraf 93 Absatz 2 Satz 3 AktG verlangt den gesetzlichen Selbstbehalt für den "
                "AG-Vorstand, nicht analog für den GmbH-Geschäftsführer; dort gilt nur die belegte Vertragsgrundlage"
            )
        if "vergleichsverhandlung" in hay:
            return (
                "Beziffere Versicherungsfall, unstreitige Mindestleistung, streitige Deckungs- oder Höhenfragen, "
                "Abwehrkosten, Zinsen und Prozessrisiko aus Police und Belegen. Bei BU-Leistungen Zukunftsrente, "
                "Nachprüfung und Gesundheitsentwicklung, bei Sachschäden Wiederherstellung, Zeitwert und Regress "
                "gesondert regeln; formuliere Abgeltungsumfang, Fälligkeit, Widerruf, Kosten und Fortbestand anderer Ansprüche"
            )
        if "berufsunfähigkeits" in hay:
            return (
                "Bestimme Beruf, konkrete zuletzt in gesunden Tagen ausgeübte Einzeltätigkeiten und deren Zeitanteile "
                "und gleiche sie mit medizinisch belegten Einschränkungen ab. Grad, Prognosezeitraum, fingierte oder "
                "tatsächliche Verweisung und Nachprüfung folgen ausschließlich der Police und den maßgeblichen AVB; "
                "keine pauschale Fünfzig-Prozent- oder Sechsmonatsregel ohne Klauselbeleg. Liefere Tätigkeitsbild, "
                "medizinische Beweisfragen, Rentenberechnung und passenden Feststellungs- oder Zahlungsantrag"
            )
        if "fehlerkatalog" in hay:
            return (
                "Prüfe die Fristenkette ohne die überholte Klagefrist des Paragraf 12 VVG alter Fassung: "
                "Fälligkeit nach Paragraf 14 VVG, regelmäßige Verjährung nach den Paragrafen 195 und 199 BGB, "
                "Hemmung durch Anspruchsanmeldung nach Paragraf 15 VVG sowie Anzeige-, Obliegenheits- und "
                "Gestaltungsfristen aus Gesetz und AVB. Kontrolliere außerdem Police, Bedingungsfassung, "
                "Versicherungsfall, Beweislast, Bezifferung, Zuständigkeit und Antrag"
            )
    if plugin_slug == "anlagen-zu-schriftsaetzen" and "anlagenband" in hay:
        return (
            "Ordne jede Anlage nach ihrer ersten Bezugnahme und halte Anlagenkennzeichen, "
            "sprechenden Kurztitel, Seitenzahl, Beweisthema und Schriftsatzfundstelle "
            "deckungsgleich; bilde Konvolute nur bei erkennbarem innerem Zusammenhang. "
            "Erzeuge ein durchsuchbares, seitenrichtiges PDF, kontrolliere Lesbarkeit, "
            "Ausrichtung, Leerseiten, Dateigröße und eingebettete Schriften und gleiche "
            "Anlagenverzeichnis, Textverweise und tatsächliche Dateien vor Einreichung ab"
        )
    if plugin_slug == "fachanwalt-erbrecht" and "ehegattentestament" in hay:
        return (
            "Lege beide Verfügungen, Errichtungsform, Familienbild und Vermögenszuordnung "
            "nebeneinander; ermittle durch individuelle Auslegung die Wechselbezüglichkeit "
            "nach Paragraf 2270 BGB und die Bindung nach dem ersten Erbfall. Prüfe gesondert "
            "Widerruf, Scheidung nach Paragraf 2268 BGB, Ausschlagung nach Paragraf 2271 "
            "Absatz 2 BGB, Anfechtung und lebzeitige Schenkungen und verknüpfe jede "
            "Auslegungstatsache mit Urkunde, Zeugenangebot oder sonstigem Aktenbeleg"
        )
    if plugin_slug == "richter-amtsgericht-zivil" and "prozessuale kniffe" in hay:
        return (
            "Prüfe anhand von Klage, Erwiderung und Terminsstand, ob Klageänderung, "
            "Widerklage, objektive Klagehäufung, Verbindung, Abtrennung, Teilurteil, "
            "Urkundenprozess, Versäumnisverfahren oder richterlicher Hinweis den "
            "Streitstoff wirklich fördern. Sichere für jeden Verfahrensgriff "
            "Statthaftigkeit, rechtliches Gehör, Verzögerungswirkung, Beweisfolge, "
            "Kostenwirkung und einen vollstreckbaren Entscheidungs- oder Verfügungstext"
        )
    if (
        plugin_slug == "richter-bverfg-verfassungsbeschwerden"
        and "prozessuale kniffe" in hay
    ):
        return (
            "Trenne Beschwerdegegenstand, Beschwerdebefugnis, Rechtswegerschöpfung, "
            "materielle Subsidiarität, Monats- oder Jahresfrist, substantiierte "
            "Grundrechtsrüge und Annahmegrund. Prüfe fachgerichtliche Gehörsrüge, "
            "Nachschieben innerhalb der Begründungsfrist, Aktenbezug und einen Antrag "
            "nach Paragraf 32 BVerfGG; liefere Zulässigkeitsvotum, Annahmeprognose und "
            "gegebenenfalls eine echte Folgenabwägung statt verkappter Hauptsacheprüfung"
        )
    if plugin_slug == "richter-verwaltungsgericht":
        routes = (
            (("zulässigkeit",), "Bestimme Verwaltungsrechtsweg, statthafte Klageart, Klagebefugnis, Beteiligten- und Prozessfähigkeit, richtiges beklagtes Rechtssubjekt, Vorverfahren, Klagefrist, Rechtsschutzbedürfnis und zulässigen Antrag anhand der Verwaltungsakte"),
            (("amtsermittlung",), "Lege entscheidungserhebliche Tatsachen, vorhandene Behördenakten, bestrittene Behauptungen und erreichbare Beweismittel offen; steuere Aktenbeiziehung, Aufklärungsverfügung, Erörterung, Beweisbeschluss und Grenzen der Amtsermittlung nach Paragraf 86 VwGO"),
            (("begründetheit anfechtung",), "Prüfe Ermächtigungsgrundlage, formelle und materielle Rechtmäßigkeit des Verwaltungsakts, maßgeblichen Entscheidungszeitpunkt, Rechtsverletzung und Tenor nach Paragraf 113 Absatz 1 VwGO; behandle Teilaufhebung und Ermessensfehler gesondert"),
            (("begründetheit verpflichtung",), "Prüfe Anspruchsgrundlage, Spruchreife, gebundene Entscheidung oder Ermessen, maßgeblichen Zeitpunkt und Rechtsverletzung; trenne Vornahme- und Bescheidungstenor nach Paragraf 113 Absatz 5 VwGO"),
            (("80 abs 5",), "Bestimme Ausgangslage der aufschiebenden Wirkung, Anordnung der sofortigen Vollziehung, statthaften Antrag, Begründung nach Paragraf 80 Absatz 3 VwGO, Erfolgsaussichten, Interessenabwägung, Vollzugsfolgen und tenorierbare Wiederherstellung oder Anordnung"),
            (("paragraf 123",), "Trenne Sicherungs- und Regelungsanordnung, Anordnungsanspruch, Anordnungsgrund, Glaubhaftmachung, Verbot der Vorwegnahme, Folgenabwägung und vollstreckbaren Antrag nach Paragraf 123 VwGO"),
            (("beweisaufnahme",), "Ordne Beweisthema, Darlegung der Beteiligten, Amtsermittlung, Beweismittel, Beweisbeschluss, Ladung, Beweismaß, freie Beweiswürdigung und dokumentierte Ablehnung weiterer Aufklärung nach Paragrafen 86, 96 und 108 VwGO"),
            (("urteilsentwurf",), "Erstelle Rubrum, Tenor, Tatbestand oder zulässige Bezugnahmen, Entscheidungsgründe, Kosten, vorläufige Vollstreckbarkeit und Rechtsmittelzulassung nach Paragrafen 113, 117, 124 und 167 VwGO mit widerspruchsfreier Beweiswürdigung"),
            (("rechtsmittel",), "Prüfe Statthaftigkeit, Beschwer, Zulassung, Frist, Form, Vertretungszwang, Darlegungsanforderungen und Entscheidungskompetenz für Berufung, Beschwerde oder Revision nach den Paragrafen 124 und folgende VwGO"),
            (("entscheidungsvorschlag",), "Verdichte Streitgegenstand, Anträge, Zulässigkeit, tragende Tatsachen, Beweisergebnis, entscheidende Norm, Gegenposition, Tenor und Nebenentscheidungen zu einer beratungsreifen Vorlage für den Spruchkörper"),
            (("finale entscheidung",), "Formuliere ein vollständiges Verwaltungsgerichtsurteil mit korrektem Rubrum, bestimmten Haupt- und Nebenentscheidungen, geschlossenem Sachverhalt, nachvollziehbarer Beweiswürdigung, tragender Subsumtion, Kostenentscheidung und Rechtsmittelbelehrung"),
            (("prozessuale kniffe",), "Prüfe Klageänderung, objektive Klagehäufung, Beiladung, Fortsetzungsfeststellung, Erledigung, Ruhen, Aussetzung, Gerichtsbescheid, Entscheidung ohne mündliche Verhandlung, Präklusion und richterlichen Hinweis nur soweit der Aktenstand den jeweiligen Verfahrensgriff trägt"),
            (("praxisraster",), "Führe für jeden Verfahrensabschnitt Zuständigkeit, Beteiligte, Antrag, Frist, Zustellung, Aktenzugang, Aufklärung, Termin, Tenor, Kosten, Vollstreckbarkeit und Rechtsmittel in einer richterlichen Kontrollliste mit Anschlussverfügung"),
        )
        for terms, detail in routes:
            if all(term in hay for term in terms):
                return detail
    if plugin_slug == "gesellschaftsrecht-legal-english":
        routes = (
            (("articles of association",), "Trenne Satzung, Gesellschaftervereinbarung und bloße Geschäftsordnung; ordne Beschlusskompetenz, notarielle Form, Registerwirkung und englischen Begriff jeweils dem deutschen Rechtsinstitut zu, ohne Common-Law-Bedeutungen unbesehen zu übernehmen"),
            (("anti-dilution",), "Rechne Full-Ratchet und Broad-Based Weighted Average mit Ausgangsbeteiligung, altem und neuem Ausgabepreis sowie Fully-Diluted-Nenner; übersetze das Ergebnis in zulässige Kapitalmaßnahme, Bezugsrechtsbehandlung, Satzungs- und Beteiligungsvertragsmechanik"),
            (("cap table",), "Gleiche Cap Table, Gesellschafterliste nach Paragraf 40 GmbHG, Beteiligungsverträge, Wandlungen und Optionen stichtagsbezogen ab; kennzeichne wirtschaftliche Verwässerung getrennt von der Legitimationswirkung nach Paragraf 16 GmbHG"),
            (("drag", "tag"), "Prüfe Drag-along, Tag-along und Piggyback nach Auslöser, Schwelle, Gleichbehandlung, Kaufpreis, Garantien, Vollmacht, Mitwirkung, Verzug und notarieller Form der Anteilsübertragung; formuliere englische Klausel und deutsche Vollzugsnotiz parallel"),
            (("due diligence",), "Verdichte Datenraumfunde zu Red Flags mit Fundstelle, betroffener Gesellschaft, Rechtsfolge, Wertwirkung, Nachforderung und Abbildung in Kaufpreis, Garantie, Freistellung, Covenant oder Closing-Bedingung"),
            (("earn-out",), "Definiere Earn-out-Kennzahl, Rechnungslegungsstandard, Zeitraum, zulässige Geschäftsführung, Informations- und Prüfungsrechte, Streitentscheid, Fälligkeit und Manipulationsschutz und rechne mindestens zwei belastbare Szenarien"),
            (("financial debt",), "Baue eine Definition Bridge für Financial Debt, Cash, Debt-like Items und Normalized Working Capital; sichere Bilanzstichtag, Doppelzählungen, Leakage, Quellenbeleg und die Übersetzung in Equity-Value- oder Completion-Accounts-Mechanik"),
            (("convertible",), "Prüfe Wandeldarlehen oder SAFE nach Fälligkeit, Wandlungsereignis, Discount, Valuation Cap, Zins, Rang, Zustimmungs- und Kapitalmaßnahmen, notariellem Vollzug und Auswirkungen auf den Fully-Diluted-Cap-Table"),
            (("fully diluted",), "Rekonstruiere Fully-Diluted-Beteiligungen aus Geschäftsanteilen, Optionen, VSOP, ESOP, Wandeldarlehen und reserviertem Pool; trenne rechtliche Beteiligung, wirtschaftliche Beteiligung und Exit-Waterfall mit nachvollziehbaren Zwischenschritten"),
            (("governance",), "Ordne Board, Geschäftsführung, Beirat und Gesellschafterversammlung den deutschen Organen zu; prüfe Reserved Matters, Mehrheit, Interessenkonflikt, Geschäftsführungsbefugnis, Vertretungsmacht, Beschlussnachweis und Rechtsfolge fehlender Zustimmung"),
            (("liquidation preference",), "Rechne Non-Participating, Participating und Capped Preference im Exit-Waterfall; prüfe Rangfolge, Multiple, Conversion-Option, Catch-up, Dividenden, Verwässerung und die gesellschaftsrechtliche Umsetzung in Satzung und Beteiligungsvertrag"),
            (("reps", "warranties"), "Trenne Garantie, Beschaffenheitsvereinbarung, Freistellung, Covenant und Disclosure; ordne Knowledge Qualifier, Materiality, De-minimis, Basket, Cap, Verjährung, Rechtsfolge und Anspruchsverfahren in einer zweisprachigen Klauselmatrix"),
            (("shareholders agreement",), "Baue Shareholders Agreement und Satzung als abgestimmtes Regelwerk: Governance, Reserved Matters, Finanzierung, Informationsrechte, Transfer, Leaver, Exit, Laufzeit, Streitbeilegung, Form und registerfähige Vollzugsschritte"),
            (("share classes",), "Ordne Stamm- und Vorzugsrechte, Stimmrecht, Gewinn- und Liquidationspräferenz, Umwandlung, Bezugsrecht und Sonderbeschluss den Geschäftsanteilen und Satzungsbestimmungen zu; prüfe Kapital- und Registervollzug"),
            (("term sheet",), "Markiere jede Regelung des Term Sheets als bindend, nicht bindend oder auslegungsbedürftig; prüfe Exklusivität, Vertraulichkeit, Kosten, Bedingungen, Laufzeit, Vertretungsmacht und die Überführung in Investment Agreement und Satzung"),
            (("transfer restrictions",), "Prüfe Vinkulierung, Lock-up, Right of First Refusal, Right of First Offer und Permitted Transfers nach Auslöser, Frist, Preisfindung, Zustimmung, Umgehungsschutz und notarieller Form gemäß Paragraf 15 Absatz 4 GmbHG"),
            (("upstream security",), "Prüfe Upstream- und Cross-Stream-Sicherheiten nach Gesellschaftsinteresse, Kapitalerhaltung, Freistellung, Limitation Language, Organfreigabe, Insolvenznähe, Vollstreckungsszenario und dokumentierter wirtschaftlicher Gegenleistung"),
            (("vesting",), "Prüfe Vesting, Cliff, Good- und Bad-Leaver nach Erwerbstatbestand, Rückübertragungsoption, Preisformel, Verfall, Arbeitsverhältnis, Verhältnismäßigkeit, notarieller Form und Cap-Table-Auswirkung"),
            (("exit", "spa"), "Ordne Signing, Conditions Precedent, Long-stop Date, Closing Deliverables, Kaufpreiszahlung, Anteilsübertragung, Organbeschlüsse, Registervollzug und Post-Closing-Pflichten in einer zweisprachigen Closing Checklist"),
        )
        for terms, detail in routes:
            if all(term in hay for term in terms):
                return detail
    if plugin_slug == "gesellschaftsrechtliche-treuepflicht":
        routes = (
            (("gleichbehandlung",), "Prüfe zunächst Rechtsform, mitgliedschaftliche Vergleichsgruppe und sachlichen Differenzierungsgrund; trenne den Gleichbehandlungsgrundsatz nach Paragraf 53a AktG von der rechtsformübergreifenden Treuepflicht und bestimme Beschluss-, Unterlassungs- oder Ersatzfolge"),
            (("aktionärstreuepflicht",), "Bestimme konkrete mitgliedschaftliche Rücksichtnahmepflicht, Einflussmöglichkeit des Aktionärs, Gesellschafts- und Mitaktionärsinteresse, Zumutbarkeit, Kausalität und die Auswirkungen auf Anfechtung, Stimmrechtsausübung oder Schadensersatz"),
            (("aktionaerstreuepflicht",), "Bestimme konkrete mitgliedschaftliche Rücksichtnahmepflicht, Einflussmöglichkeit des Aktionärs, Gesellschafts- und Mitaktionärsinteresse, Zumutbarkeit, Kausalität und die Auswirkungen auf Anfechtung, Stimmrechtsausübung oder Schadensersatz"),
            (("mehrheitsmacht",), "Zerlege den Mehrheitsbeschluss in Kompetenz, Verfahrensordnung, Gesellschaftsinteresse, Sondervorteil, Minderheitsnachteil und mildere Gestaltung; formuliere die stärkste sachliche Rechtfertigung und den treuwidrigen Missbrauchseinwand"),
            (("minderheitenschutz",), "Ordne Informations-, Antrags-, Stimm-, Klage- und Sonderprüfungsrechte der Minderheit nach Rechtsform, Schwelle, Frist und Beleg; trenne gesetzliches Minderheitenrecht von einer zusätzlichen Treuepflichtkorrektur"),
            (("ausschlussklage",), "Prüfe wichtigen Grund, Ultima Ratio, Abmahnung oder milderes Mittel, Beschluss- und Klagebefugnis, Abfindung, Bewertungsstichtag, Fortbestand der Gesellschaft und einstweiligen Rechtsschutz für den Ausschluss eines Gesellschafters"),
            (("austritt",), "Prüfe wichtigen Grund, Zumutbarkeit der Fortsetzung, gesellschaftsvertragliche Kündigungs- und Austrittsregeln, Abfindung, Fälligkeit, Kapitalerhaltung, Fortsetzungsklausel und Alternativen zum sofortigen Ausscheiden"),
            (("auskunft",), "Bestimme Auskunfts- und Einsichtsrecht nach Rechtsform, Informationszweck, Erforderlichkeit, Geheimhaltungsinteresse, Missbrauchseinwand, Modalität, Frist und durchsetzbaren Antrag; rechne eine Rechnungslegungspflicht getrennt"),
            (("organpflicht",), "Trenne Organpflicht und mitgliedschaftliche Treuepflicht: Rolle, Kompetenz, Business-Judgment-Spielraum, Weisung, Interessenkonflikt, Enthaltung, Dokumentation, Anspruchsinhaber und Innen- oder Außenhaftung einzeln prüfen"),
            (("pool",), "Prüfe Pool- oder Stimmbindungsvereinbarung nach Parteien, erfassten Beschlüssen, Willensbildung, Weisung, Dauer, Kündigung, Vollmacht, Vertragsstrafe, Durchsetzung und Konflikt mit Satzung, Organpflicht oder Treuepflicht"),
            (("stimmverbot",), "Prüfe Selbstbetroffenheit, Rechtsform, Beschlussgegenstand, gesetzliches oder satzungsmäßiges Stimmverbot, Stimmbindung, Mehrheitsberechnung, Beschlussfeststellung und Kausalität des fehlerhaften Stimmenansatzes"),
            (("sanierungs",), "Prüfe Sanierungskonzept, Finanzierungsbedarf, Gleichbehandlung, Bezugs- oder Beteiligungsmöglichkeit, Verwässerung, Sondervorteil, Zumutbarkeit des Beitrags und Rechtsfolgen für zustimmende, ablehnende und ausscheidende Gesellschafter"),
            (("corporate opportunity",), "Bestimme Geschäftschance, Kenntniserlangung, Tätigkeitsbereich, konkrete Erwartung der Gesellschaft, Organ- oder Gesellschafterrolle, Nutzungshandlung, Offenlegung, Zustimmung, Herausgabe, Unterlassung und Schadensberechnung"),
            (("related party",), "Prüfe nahestehende Partei, Leistung und Gegenleistung, Zuständigkeit, Interessenkonflikt, Marktüblichkeit, Kapitalerhaltung, Zustimmung, Offenlegung und Ersatz- oder Rückgewähranspruch in einer Transaktionsmatrix"),
            (("gesellschafterdarlehen",), "Trenne Finanzierungsabrede, Treuepflicht, Gleichbehandlung, Kündigung, Rang, Krise, Rückzahlung und Insolvenzwirkung; bestimme, ob und in welchem Umfang ein Finanzierungsbeitrag wirklich geschuldet oder nur wirtschaftlich sinnvoll ist"),
            (("geheimhaltung",), "Bestimme geschützte Gesellschaftsinformation, Zugangsberechtigung, Nutzungszweck, Datenraumregel, Weitergabe, Wettbewerbsbezug, Beweis, Unterlassungsbedarf und zulässige Informationsverteidigung des Gesellschafters"),
            (("nachfolge",), "Ordne Erbfall, Nachfolgeklausel, Eintritt, Abfindung, Stimmrechtsausübung, Testamentsvollstreckung, Legitimation und Treuepflichten der Erben und Altgesellschafter bis zur Register- oder Listenberichtigung"),
            (("registersperre",), "Prüfe materiellen Anspruch, drohende Register- oder Listenwirkung, Verfügungsgrund, richtigen Antragsgegner, Bestimmtheit, Vollziehungsfrist, Schutzschrift und Hauptsacheweg; formuliere Antrag und Hilfsantrag ohne unzulässige Vorwegnahme"),
            (("schadensersatz",), "Leite Pflicht, Pflichtverletzung, Vertretenmüssen, Schaden, Kausalität, Anspruchsinhaber, Vorteilsausgleich, Mitverschulden, Verjährung und Bezifferung aus der konkreten mitgliedschaftlichen Beziehung her"),
            (("unterlassung",), "Prüfe konkrete Erst- oder Wiederholungsgefahr, Reichweite der Treuepflicht, Bestimmtheit des Verbots, Zumutbarkeit, Vollstreckungsfähigkeit, Eilbedürftigkeit und Verhältnis zu Beschlussmängel- oder Leistungsklage"),
        )
        for terms, detail in routes:
            if all(term in hay for term in terms):
                return detail
    if plugin_slug == "dsa-dma-digitalregulierung":
        routes = (
            (("pyramiden",), "Klassifiziere Vermittlungsdienst, reine Durchleitung, Caching, Hosting, Online-Plattform, Suchmaschine, VLOP oder VLOSE und ordne jeder Stufe nur die tatsächlich anwendbaren Pflichten, Ausnahmen und Behördenzuständigkeiten zu"),
            (("artikel 16",), "Prüfe Meldekanal, hinreichend genaue und begründete Meldung, Kenntniswirkung, zügige Entscheidung, Mitteilung an den Meldenden und Dokumentation nach Artikel 16 DSA; trenne Notice-and-Action von gerichtlicher oder behördlicher Anordnung"),
            (("artikel 17",), "Erstelle eine konkrete Begründung nach Artikel 17 DSA mit betroffener Information, Maßnahme, Tatsachen- und Rechtsgrund, Automatisierungseinsatz und Rechtsbehelf; gleiche die Veröffentlichungspflicht nach Artikel 24 Absatz 5 DSA ab"),
            (("artikel 20",), "Prüfe Zugang zum internen Beschwerdesystem, Sechsmonatsfrist, fachkundige und nicht rein automatisierte Entscheidung, Ergebnisbegründung und Anschluss an außergerichtliche Streitbeilegung oder Gericht"),
            (("artikel 21",), "Ordne zugelassene Streitbeilegungsstelle, Antragsgegenstand, Zulässigkeit, Gebühren, Mitwirkung nach Treu und Glauben, nicht bindende Entscheidung, Kostentragung und verbleibenden Gerichtsweg nach Artikel 21 DSA"),
            (("artikel 22",), "Prüfe Status und Fachgebiet des Trusted Flagger, priorisierte Bearbeitung, Missbrauchskontrolle, Berichtspflichten und mögliche Aussetzung oder Aberkennung; dokumentiere, warum die konkrete Meldung priorisiert wurde"),
            (("dark pattern",), "Prüfe Gestaltung, Entscheidungsarchitektur, Wiederholung, Hervorhebung, Abbruchhürden und Irreführung nach Artikel 25 DSA und trenne den DSA-Maßstab von Verbraucher-, Wettbewerbs- und Datenschutzrecht"),
            (("empfehlung",), "Dokumentiere Hauptparameter des Empfehlungssystems, Einflussmöglichkeiten des Nutzers und bei VLOP oder VLOSE mindestens eine nicht profilbasierte Option nach Artikeln 27 und 38 DSA"),
            (("minderjähr",), "Prüfe Zugänglichkeit für Minderjährige, altersgerechte Gestaltung, hohes Maß an Privatsphäre, Werbeprofilingverbot und belastbare Alters- und Risikoeinschätzung nach Artikel 28 DSA ohne unnötige Datenerhebung"),
            (("artikel 34",), "Baue die jährliche und anlassbezogene Risikobewertung für VLOP oder VLOSE nach Artikel 34 DSA aus Systemdesign, Moderation, Empfehlungslogik, Werbung, Grundrechten, gesellschaftlichen Risiken, Datenbelegen und begründeter Wesentlichkeit"),
            (("artikel 35",), "Ordne jedes festgestellte systemische Risiko einer geeigneten, verhältnismäßigen und messbaren Abhilfemaßnahme nach Artikel 35 DSA zu; bestimme Verantwortlichen, Termin, Wirksamkeitsindikator, Nebenwirkung und Nachweis"),
            (("artikel 36",), "Prüfe förmliche Krisenaktivierung durch die Kommission, betroffenen VLOP- oder VLOSE-Dienst, Krisenbezug, Eignung, Erforderlichkeit, Verhältnismäßigkeit, Befristung, Bericht und Grundrechtsfolgen nach Artikel 36 DSA"),
            (("audit",), "Bereite unabhängige Prüfung nach Artikel 37 DSA mit Prüfgegenstand, Kriterien, Datenzugang, Feststellungen, positivem oder eingeschränkt positivem Prüfungsurteil, Abhilfemaßnahmen und Umsetzungsbericht vor"),
            (("gatekeeper",), "Prüfe Benennungsvoraussetzungen, zentralen Plattformdienst, Schwellenwerte und qualitative Indizien nach DMA; ordne Pflichten aus Artikeln 5 bis 7, technische Umsetzung, Nachweis und Verfahren der Kommission getrennt"),
        )
        for terms, detail in routes:
            if all(term in hay for term in terms):
                return detail
    if plugin_slug == "status-navigator-step-plan":
        routes = (
            (("inventur",), "Erfasse jede Datei mit Originalname, Dokumenttyp, Datum, Beteiligten, Version, Lesbarkeit, Unterschrift und Fundort; trenne Duplikat, Vorfassung, Anlage und leere oder beschädigte Datei ohne fallbezogene Beispieldaten fest einzubauen"),
            (("diskrepan",), "Vergleiche Namen, Daten, Beträge, Quoten, Laufzeiten, Aktenzeichen und Vertragsverweise über alle Dokumente; führe jede Abweichung mit beiden Fundstellen, Bedeutung, Klärungsweg und Verantwortlichem"),
            (("unterschrift",), "Prüfe für jede Urkunde Unterzeichner, Vertretungsregel, Vollmacht oder Registerstand, Signaturart, Datum, Vollständigkeit und Gegenzeichnung und markiere nur den konkreten Wirksamkeits- oder Beweisbedarf"),
            (("frist",), "Leite jede Frist aus Dokument, Ereignis und Rechtsgrund ab; dokumentiere Beginn, Ende, Vorfrist, Zeitzone, Zustellungsbeleg, Verantwortlichen, Vertretung, Sofortmaßnahme und Erledigungsnachweis"),
            (("cap table",), "Gleiche Beteiligungsstände stichtagsbezogen mit Register- oder Listenstand, Kapitalmaßnahmen, Wandlungen, Optionen und Quellen ab; rechne Abweichungen nach und kennzeichne ungeklärte Versionen"),
            (("rangfolge",), "Ordne Forderungen, Sicherheiten, Rangabreden, Fälligkeit, Vollstreckungszugriff und Verwertungserlös instrumentenbezogen; trenne gesetzlichen, vertraglichen und bloß wirtschaftlichen Rang"),
            (("fehlend",), "Formuliere aus jeder materiellen Lücke eine konkrete Beschaffungsaufgabe mit Dokument, Zweck, möglichem Inhaber, Anfrageweg, Frist, Ersatzbeleg, Verantwortlichem und Folge bei Nichterhalt"),
            (("workflow",), "Übersetze jeden offenen Befund in Aufgabe, Ergebnis, Verantwortlichen, Freigeber, Termin, Abhängigkeit, Status, Eskalation und Abschlussbeleg; vermeide bloße Ampelfarbe ohne Handlungsauftrag"),
            (("hyperlink",), "Verknüpfe jede Trackerzeile mit stabiler lokaler Fundstelle oder DMS-Ziel, prüfe Zugriffsrecht und Dateibestand und kennzeichne fehlende Dokumente als Beschaffungsbedarf statt mit einem scheinbaren Link"),
            (("übergabe",), "Erstelle eine Übergabenotiz mit Mandatsziel, Aktenstand, kritischen Fristen, offenen Entscheidungen, wichtigsten Fundstellen, Ansprechpartnern, nächsten fünf Handlungen und eindeutigem Bearbeitungsbesitz"),
            (("status",), "Verdichte den Aktenstand in belegte Tatsache, offene Frage, Risiko, Entscheidung, Aufgabe und nächsten Termin; jede Statuszeile muss auf ein Dokument oder eine ausdrücklich bezeichnete Nachforderung zurückführen"),
            (("vertrag",), "Baue eine Vertragslandkarte mit Parteien, Gegenstand, Laufzeit, Kündigung, Vergütung, Sicherheiten, Zustimmungen, Abhängigkeiten, Änderungen, Unterschriftsstand und Fundstelle und leite nur daraus die Bearbeitungsreihenfolge ab"),
        )
        for terms, detail in routes:
            if all(term in hay for term in terms):
                return detail
    return ""


def supplemental_plugin_routes(plugin_slug: str) -> tuple[tuple[str, str, str], ...]:
    """Ergänzt kleine Spezialsets um eigenständige, normnahe Arbeitsstationen."""

    if plugin_slug == "arbeitsrecht":
        return (
            ("Arbeitsvertrag, Status und Nachweis", "Ordne Tätigkeit, Weisungsbindung, Eingliederung, Beginn, Arbeitsort, Vergütung, Arbeitszeit, Befristung, Nebenabreden, Tarifbezug, Vertretungsmacht und Unterzeichnung nach BGB Paragraf 611a und NachwG; trenne Vertragsinhalt, Nachweispflicht und Statusfrage.", "Vertrags- und Statusmatrix mit fehlenden Angaben, Formrisiken, Nachforderung und unmittelbar verwendbarer Vertrags- oder Korrekturfassung"),
            ("Arbeitszeit, Mindestlohn und Vergütung", "Rekonstruiere Sollzeit, Istzeit, Pausen, Bereitschaft, Schicht, Zuschlag, Ausschlussfrist, Abrechnung und Zahlung; gleiche ArbZG, MiLoG, Vertrag, Tarifwerk, Zeiterfassung und Lohnabrechnung zeitraumgenau ab.", "monatsgenaue Zeit- und Entgeltberechnung mit Belegspalte, Anspruchsgrund, Einwendung, Ausschlussfrist und beziffertem Forderungsschreiben"),
            ("Urlaub, Krankheit und Entgeltfortzahlung", "Trenne Urlaubsentstehung, Übertragung, Hinweis und Verfall, Arbeitsunfähigkeit, Anzeige, Nachweis, Einheit des Verhinderungsfalls, Fortzahlungszeitraum und betriebliches Eingliederungsmanagement; ordne jeden Zeitraum einem Beleg zu.", "Abwesenheits- und Anspruchskalender mit Resturlaub, Fortzahlung, Nachweisen, offenen Widersprüchen und passendem Antwortschreiben"),
            ("Weisung, Versetzung und Maßregelung", "Prüfe Vertragsrahmen, Direktionsrecht nach GewO Paragraf 106, billiges Ermessen, Arbeitsort, Tätigkeit, Vergütung, Betriebsratsbeteiligung und Maßregelungsverbot; entwickle rechtmäßige Umsetzung und gerichtsfeste Gegenposition.", "Weisungs- oder Versetzungsvermerk mit Interessenabwägung, Beteiligungsweg, Alternativfassung und Annahme- oder Zurückweisungsschreiben"),
            ("Abmahnung und Personalmaßnahme", "Bestimme konkreten Pflichtverstoß, Datum, Kenntnis, Beleg, Anhörung, Rüge- und Warnfunktion, Gleichbehandlung, Verhältnismäßigkeit und Personalaktenfolge; vermische Verdacht, erwiesene Tatsache und Wertung nicht.", "abgestufte Personalmaßnahme mit Tatsachenkern, Belegmatrix, Abmahnungsentwurf, milderer Alternative und Personalaktenvermerk"),
            ("Ordentliche Kündigung und Kündigungsschutzklage", "Sichere Kündigungserklärung, Original, Vertretung, Zugang, Betriebsgröße, Wartezeit, Sonderkündigungsschutz, Kündigungsgrund, Sozialauswahl, Betriebsratsanhörung und Dreiwochenfrist nach KSchG Paragrafen 1, 4 und 7 sowie BGB Paragraf 623.", "Kündigungsakte mit Fristenberechnung, Wirksamkeitsmatrix, Klageantrag, Beweisangeboten und sofortigem Einreichungs- oder Verteidigungsschritt"),
            ("Außerordentliche und Verdachtskündigung", "Prüfe wichtigen Grund, Interessenabwägung, mildere Mittel, Zweiwochenfrist, Ermittlungsstand, belastende und entlastende Umstände, Anhörung des Arbeitnehmers und Betriebsrats sowie Zugang; halte Tat- und Verdachtskündigung getrennt.", "Entscheidungsvorlage mit Ermittlungsfragen, Fristenlauf, Anhörungsentwürfen, Kündigungsvariante und Prozessrisiko"),
            ("Betriebsrat, Massenentlassung und Beteiligung", "Ordne personelle Maßnahme, Mitbestimmungs- oder Anhörungstatbestand, zuständiges Gremium, Informationsstand, Stellungnahmefrist und Reaktion; prüfe bei Entlassungswellen Konsultation und Anzeige gesondert.", "Beteiligungspaket mit vollständiger Unterrichtung, Fristenblatt, Beschluss- und Übermittlungsnachweis sowie Sperrpunkt vor Umsetzung"),
            ("Befristung und Entfristung", "Prüfe Befristungsabrede, Schrift- oder elektronische Form, Unterzeichnung vor Arbeitsaufnahme, Sachgrund, Höchstdauer, Verlängerung, Vorbeschäftigung, Zweckbefristung und Klagefrist nach TzBfG Paragrafen 14 bis 17.", "Befristungsvotum mit Vertragschronologie, Formbelegen, Sachgrundprüfung, Entfristungsantrag und Arbeitgebererwiderung"),
            ("Betriebsübergang und Vertragsfortbestand", "Bestimme wirtschaftliche Einheit, Inhaberwechsel, Identitätswahrung, Übergangszeitpunkt, betroffene Arbeitnehmer, Unterrichtung, Widerspruch, Zuordnung, Haftung und Kündigungsmotiv nach BGB Paragraf 613a.", "Übergangsmatrix mit Betriebsmitteln, Personal, Kunden, Stichtag, Unterrichtung, Widerspruchsrisiko und Zuordnungsschreiben"),
            ("Annahmeverzug und Vergütung nach Trennung", "Rekonstruiere Leistungsfähigkeit, Leistungswillen, Angebot oder Entbehrlichkeit, Arbeitgeberreaktion, Zwischenverdienst, böswillig unterlassenen Verdienst und Zeitraum nach BGB Paragraf 615 sowie KSchG Paragraf 11.", "nachrechenbare Annahmeverzugstabelle mit Monatswerten, Abzügen, Auskunftsbedarf, Beweisen und beziffertem Antrag"),
            ("Vergleich, Zeugnis und Abwicklung", "Entwirf eine vollständige Beendigungslösung mit Beendigungsdatum, Vergütung, Urlaub, Freistellung, Abfindung, Zeugnis, Rückgabe, Bonus, Altersversorgung, Ausgleichsklausel, Kosten, Widerruf und steuer- oder sozialrechtlich offenen Punkten.", "vollziehbarer Vergleich mit Varianten, Zahlungs- und Abwicklungsplan, Zeugnisregelung, Erledigungsnachweisen und Mandantenfreigabe"),
        )
    if plugin_slug == "mietrecht":
        return (
            ("Mietvertrag, Mietgegenstand und Vertragsbestand", "Bestimme Parteien, Objekt, Nutzungszweck, Beginn, Laufzeit, Miete, Betriebskosten, Kaution, Übergabe, Nachträge, Vertretung und Formularcharakter; trenne Wohnraum, Gewerberaum und Mischmiete vor jeder weiteren Prüfung.", "Mietvertragsmatrix mit wirksamen Regelungen, unwirksamen Klauseln, offenen Belegen und sofort verwendbarem Nachtrags- oder Antworttext"),
            ("Miethöhe, Mietpreisbremse und Rückforderung", "Prüfe Ausgangsmiete, Vormiete, Modernisierung, Neubauausnahme, örtliche Verordnung, Auskunft, qualifizierte Rüge, Vergleichsmiete und Rückforderungszeitraum nach BGB Paragrafen 556d bis 556g.", "Mietenberechnung mit Ausgangswerten, Ausnahmeprüfung, Rügeentwurf, Rückforderungsbetrag und Beleganforderung"),
            ("Mangel, Minderung und Instandsetzung", "Rekonstruiere Sollbeschaffenheit, Auftreten, Dauer, Anzeige, Ursache, Gebrauchsbeeinträchtigung, Verantwortungsbereich, Minderungsquote, Zurückbehaltung, Fristsetzung und Beweis nach BGB Paragrafen 535, 536 und 536c.", "Mängelchronologie mit Foto-, Zeugen- und Gutachtenbelegen, Monatsberechnung, Instandsetzungsantrag und Gegenargumenten"),
            ("Betriebskosten und Belegeinsicht", "Gleiche Abrechnungszeitraum, Zugang, Gesamtkosten, Umlageschlüssel, Vorauszahlungen, Wirtschaftlichkeit, haushaltsnahe Positionen, Belege und Einwendungsfrist nach BGB Paragraf 556 Absatz 3 ab.", "belegfähige Abrechnungskontrolle mit Positionsdifferenzen, Nachforderung oder Guthaben, Einwendungsschreiben und Einsichtstermin"),
            ("Kaution, Aufrechnung und Rückgabe", "Prüfe vereinbarte Sicherheit, Höchstgrenze, Ratenzahlung, getrennte Anlage, Zinsen, Zugriff während des Mietverhältnisses, offene Ansprüche, Abrechnungsreife und Rückzahlung nach BGB Paragraf 551.", "Kautionskonto mit Einzahlungen, Zinsen, Gegenforderungen, Belegen, zurückzuzahlendem Betrag und Abrechnungsschreiben"),
            ("Mieterhöhung und Modernisierung", "Trenne Erhöhung bis zur Vergleichsmiete, Index- oder Staffelmiete und Modernisierung; prüfe Begründungsmittel, Kappungsgrenze, Ankündigung, Härte, Kostenabzug, Zugang, Frist und neue Miete nach BGB Paragrafen 557 bis 559b.", "Erhöhungsprüfung mit Rechenblatt, formellen Mängeln, Härteeinwand, Zustimmungs- oder Zurückweisungsschreiben und Zahlungstermin"),
            ("Zahlungsverzug, Kündigung und Räumung", "Ordne jede Sollstellung und Zahlung nach Monat, Verwendungszweck, Verrechnung, Rückstand und Zugang; trenne fristlose und ordentliche Kündigung, Schonfristzahlung, Fortsetzungswiderspruch und Räumungsantrag nach BGB Paragrafen 543, 569, 573 und 574.", "Rückstandskonto mit Kündigungsvarianten, Zugangsnachweis, Räumungsklage oder Verteidigung und Vergleichskorridor"),
            ("Eigenbedarf und Härtewiderspruch", "Prüfe Bedarfsperson, Beziehung, konkrete Nutzungsabsicht, Wohnsituation, Alternativwohnung, Vorrats- oder Wegfallrisiko, Kündigungsbegründung und Härtegründe; ordne Beweis und Prognose beider Seiten getrennt.", "Eigenbedarfsakte mit Tatsachenerklärung, Widerspruchs- und Beweismatrix, Kündigungs- oder Erwiderungsentwurf und Umzugsregelung"),
            ("Schönheitsreparaturen, Schäden und Rückgabe", "Trenne vertragsgemäße Abnutzung, Beschädigung, Anfangszustand, Renovierungsklausel, Quotenabgeltung, Fristsetzung, Rückgabeprotokoll, Kostenvoranschlag, Vorteilsausgleich und Kautionsbezug.", "Rückgabe- und Schadensmatrix mit Fotos, Protokoll, Klauselkontrolle, Zeitwert, Fristsetzung und bezifferter Abrechnung"),
            ("Gewerberaummiete und Laufzeitrisiken", "Prüfe Mietzweck, Laufzeit, Optionsrecht, Kündigung, Schrift- oder Textformregime am Vertragsschluss, Nachträge, Betriebspflicht, Konkurrenzschutz, Umsatzmiete, Nebenkosten und Anpassung; halte Stichtag und Übergangsrecht fest.", "Gewerberaummemo mit Vertragschronologie, Formrisiko, Kündigungstermin, Klauselvarianten und verhandlungsfähigem Nachtrag"),
            ("Wohnungseigentum und Beschlussbezug", "Kläre, ob Mietmangel oder Anspruch von Gemeinschaftseigentum, Verwalterhandeln oder Eigentümerbeschluss abhängt; trenne Mietvertragsanspruch, Verbandszuständigkeit, Beschlusslage und erforderliche Mitwirkung.", "Schnittstellenplan mit Mietpartei, Gemeinschaft, Verwalter, Beschlussbedarf, Belegen und abgestimmten Schreiben"),
            ("Mietprozess, Beweis und Vergleich", "Baue Antrag, chronologischen Sachverhalt, Mietkonto, Mangel- oder Kündigungstatsachen, substantiiertes Bestreiten, Beweisangebote, Anlagenbezug, Kosten- und Vollstreckungsfolgen zu Klage, Erwiderung oder Vergleich.", "einreichungsfähiger Schriftsatz mit Anlagenverzeichnis, Beweisplan, Hilfsanträgen, Räumungs- oder Zahlungstenor und Vergleichsvorschlag"),
        )
    if plugin_slug == "richter-familiengericht":
        return (
            ("Eingang, Zuständigkeit und Beteiligte", "Bestimme Verfahrensart, örtliche und internationale Zuständigkeit, Anwaltszwang, Antrag, notwendige Beteiligte, Verfahrensbeistand, Jugendamt, Zustellung, Eilbedarf und nächste Verfügung.", "richterliches Eingangsblatt mit Zuständigkeitsvotum, Beteiligtenliste, Fristen und unterschriftsreifer Erstverfügung"),
            ("Kindesanhörung und rechtliches Gehör", "Plane persönliche Anhörung, altersgerechte Durchführung, Elternanhörung, Jugendamtsbeteiligung, Verfahrensbeistand, Dokumentation und Umgang mit vertraulichen Angaben nach FamFG; trenne Kindeswille und Kindeswohlbewertung.", "Anhörungs- und Terminverfügung mit Ladungen, Themen, Schutzvorkehrungen, Protokollpunkten und Anschlussentscheidung"),
            ("Einstweilige Anordnung", "Prüfe dringendes Bedürfnis, Regelungsgegenstand, Tatsachengrundlage, Glaubhaftmachung, Anhörung, mögliche Entscheidung ohne mündliche Verhandlung, Befristung und Verhältnis zur Hauptsache nach FamFG Paragraf 49.", "vollständiger Eilbeschluss mit bestimmtem Tenor, Gründen, Kosten, Befristung und Hauptsacheanschluss"),
            ("Kindeswohlgefährdung und Schutzkonzept", "Trenne gegenwärtige erhebliche Gefahr, Schadensprognose, elterliche Abwendungsfähigkeit, Hilfen, mildere Mittel, Teilentzug und Trennung des Kindes; ordne Jugendamtsakte, Befunde, Anhörungen und Sachverständigenbedarf nach BGB Paragraf 1666.", "Gefährdungs- und Maßnahmenmatrix mit Tatsachen, Schutzstufe, milderem Mittel, kontrollierbarem Tenor und Überprüfungstermin"),
            ("Elterliche Sorge und Entscheidungszuständigkeit", "Bestimme bestehenden Sorgestatus, konkrete Angelegenheit, Kooperationsfähigkeit, Kontinuität, Bindungen, Förderungsprinzip, Kindeswille und beantragten Übertragungsumfang; vermeide pauschale Gesamtübertragung ohne Tatsachenbezug.", "Beschlussentwurf mit Sorgematrix, Anhörungsbefunden, bestimmtem Übertragungsbereich, Gründen und Vollzugsanweisung"),
            ("Umgang, Ferien und Vollstreckbarkeit", "Rekonstruiere Kontakte, Alter, Bindung, Entfernung, Übergaben, Kommunikation, Krankheit, Ferien, Loyalitätskonflikt und Schutzbedarf; formuliere Zeiten, Orte, Bringen, Holen, Ausfälle und Ersatztermine kalendarisch bestimmt.", "vollstreckbare Umgangsregelung mit Ferienplan, Übergabemodalitäten, Ordnungsmittelhinweis und Überprüfungsklausel"),
            ("Kindes- und Ehegattenunterhalt", "Ordne Auskunft, Einkommen, Abzüge, Bedarf, Kindergeld, Mehrbedarf, Rang, Leistungsfähigkeit, Wohnvorteil, Rückstand, Titellage und Abänderung monatsgenau; trenne Kindes-, Trennungs- und nachehelichen Unterhalt.", "Unterhaltsrelation mit Monatsrechnung, Beleglücken, Stufen- oder Leistungsantrag, Rückstand und vollstreckbarem Tenor"),
            ("Scheidung, Verbund und Folgesachen", "Prüfe Trennung, Trennungsjahr, Scheitern, Zustellung, Verbund, rechtzeitig anhängige Folgesachen, Abtrennung, persönliche Anhörung und Entscheidungsreife nach BGB Paragraf 1565 und FamFG.", "Scheidungsbeschluss mit Verfahrenschronologie, Verbundkontrolle, Tenor, Kosten und Rechtskraftvermerk"),
            ("Versorgungsausgleich", "Bestimme Ehezeit, Versorgungsträger, gesetzliche, betriebliche, private, beamten- und ausländische Anrechte, Auskunftsstand, interne oder externe Teilung, Geringfügigkeit, Vereinbarung und Härte nach VersAusglG.", "Anrechte- und Teilungsmatrix mit Auskunftslücken, Beschlussformeln, korrespondierenden Kapitalwerten und Vollzugsadressaten"),
            ("Sachverständigengutachten und Beweisaufnahme", "Formuliere entscheidungserhebliche Anknüpfungstatsachen und neutrale Beweisfragen, sichere Qualifikation, Aktenzugang, Exploration, Beteiligtenrechte, Ergänzungsfragen, Anhörung des Sachverständigen und freie Würdigung.", "Beweisbeschluss oder Gutachtenauftrag mit Aktenpaket, Fragenkatalog, Frist, Beteiligtenrechten und Würdigungsraster"),
            ("Beschluss, Tenor und Nebenentscheidungen", "Baue Rubrum, Anträge, Feststellungen, Beweiswürdigung, Rechtsmaßstab, Subsumtion, bestimmten Tenor, Kosten, Wirksamkeit, Rechtsmittelbelehrung und Anschlussverfügung nach FamFG Paragrafen 38 und 39 widerspruchsfrei.", "versandfertiger Familiengerichtsbeschluss mit Vollstreckbarkeitskontrolle und Zustellungsverfügung"),
            ("Vollstreckung, Abänderung und Rechtsmittel", "Prüfe Vollstreckungstitel, Bestimmtheit, Zuwiderhandlung, Ordnungsmittel, unmittelbaren Zwang, Abänderungsgrund, Beschwer, Statthaftigkeit, Frist, Abhilfe und Aktenvorlage; trenne Erkenntnis- und Vollstreckungsverfahren.", "Anschlussvermerk mit Vollstreckungsmaßnahme, Abänderungs- oder Beschwerdeweg, Fristen und konkreter Verfügung"),
        )
    if plugin_slug == "staatsanwaltschaft-amtsanwaltschaft":
        return (
            ("Eingang, Zuständigkeit und Anfangsverdacht", "Ordne Anzeige, Mitteilung oder Eigenwahrnehmung nach Tat, Tatort, Tatzeit, Beschuldigtem, Verletztem, Delikt, Verjährung, Zuständigkeit und Anfangsverdacht gemäß StPO Paragraf 152 Absatz 2; trenne bloße Vermutung von zureichendem tatsächlichem Anhaltspunkt.", "Eingangsverfügung mit Aktenanlage, Delikts- und Zuständigkeitsvotum, Verjährungskontrolle und ersten Ermittlungsaufträgen"),
            ("Ermittlungsplan und entlastende Umstände", "Leite aus jedem Tatbestandsmerkmal konkrete Ermittlungsfragen ab, ordne Beweismittel, Verantwortlichen, Reihenfolge, Eilbedürftigkeit und Rücklaufkontrolle zu und erforsche nach StPO Paragraf 160 Absatz 2 belastende wie entlastende Umstände.", "terminierter Ermittlungsplan mit Tatbestandsmatrix, Beweismitteln, offenen Widersprüchen und Wiedervorlage"),
            ("Beschuldigtenvernehmung und Verteidigungsrechte", "Prüfe Beschuldigtenstellung, Ladung, Belehrung, Aussagefreiheit, Verteidigerkontakt, Dolmetscher, Vernehmungsfähigkeit, Dokumentation und Fernwirkung früherer Fehler nach StPO Paragrafen 136 und 163a.", "Vernehmungsauftrag oder Beanstandungsvermerk mit vollständiger Belehrung, Themenplan, Schutzrechten und Verwertungsprüfung"),
            ("Durchsuchung, Beschlagnahme und Sicherstellung", "Bestimme Tatverdacht, Suchziel, Räume oder Person, aufzufindende Gegenstände, Verhältnismäßigkeit, Richtervorbehalt, Gefahr im Verzug, Zufallsfund, Beschlagnahmebedürftigkeit, Siegelung und Rückgabe nach StPO Paragrafen 94 bis 98 sowie 102 bis 105.", "gerichtsfester Antrag oder Eilvermerk mit Such- und Sicherungsziel, Tatsachengrundlage, Verhältnismäßigkeit und Vollzugsanweisung"),
            ("Digitale Spuren und verdeckte Maßnahmen", "Ordne Gerät, Konto, Anschluss, Verkehrsdaten, Kommunikationsinhalt, Zeitraum, Straftatenkatalog, Subsidiarität, Richtervorbehalt, Kernbereich, Löschung, Benachrichtigung und technische Auswertung; wähle nur die tatbestandlich passende Befugnis.", "Maßnahmenmatrix mit Eingriffsgrundlage, Zielperson, Zeitraum, Suchparametern, Schutzvorkehrungen, Beschlussentwurf und Prüfdatum"),
            ("Zeugen, Verletzte und Schutzbedarf", "Prüfe Zeugenthema, Erreichbarkeit, Aussageentstehung, Erinnerungsqualität, mögliche Zeugnis- oder Auskunftsverweigerung, anwaltlichen Beistand, Schutzmaßnahmen und besondere Verletztenrechte; vermeide suggestive Vorgaben.", "Zeugen- und Verletztenplan mit Ladung, Belehrung, Fragethemen, Schutzvorkehrungen, Beistand und Belegabgleich"),
            ("Beweiswürdigung und Tatnachweis", "Führe für jedes Merkmal belastende und entlastende Belege, Herkunft, Authentizität, Verwertbarkeit, Aussagekraft, Widerspruch und erforderliche Ergänzung; trenne hinreichenden Tatverdacht von bloßer Möglichkeit.", "Tatnachweismatrix mit Beweiswürdigung, Alternativerklärung, Lücken, Nachermittlung und Abschlussvotum"),
            ("Haft, Unterbringung und sonstige Zwangsmittel", "Prüfe dringenden Tatverdacht, konkreten Haftgrund, Verhältnismäßigkeit, mildere Mittel, Beschleunigungsgebot, Haftfähigkeit, Vorführung und Fortdauer; halte Freiheitsentziehung und andere Sicherungsmaßnahmen getrennt.", "Haft- oder Freilassungsvermerk mit Tatsachen, Belegen, Alternativen, Antrag, Auflagen und Kontrolltermin"),
            ("Einstellung und Opportunitätsentscheidung", "Trenne fehlenden hinreichenden Tatverdacht nach StPO Paragraf 170 Absatz 2 von Einstellungen nach Paragrafen 153 und folgende; prüfe Zustimmung, Auflagen, öffentliches Interesse, Privatklageweg, Mitteilungen, Kosten und Wiederaufnahmebedarf.", "begründete Abschlussverfügung mit Einstellungsnorm, Verfügungspunkten, Mitteilungen, Rechtsbehelf und Asservatenentscheidung"),
            ("Strafbefehlsantrag", "Prüfe Zuständigkeit, hinreichenden Tatverdacht, geeignete Rechtsfolge, Strafmaß, Tagessatzgrundlage, Nebenfolgen, Einziehung, Fahrerlaubnis, Beweismittel und vollständigen Anklagesatz nach StPO Paragrafen 407 und folgende.", "unterschriftsreifer Strafbefehlsantrag mit konkretem Tatvorwurf, Rechtsfolgen, Beweismitteln und Verfügung"),
            ("Anklage und Eröffnungsprognose", "Formuliere Anklagesatz nach StPO Paragraf 200 mit Person, Tatzeit, Tatort, Tathandlung, Tatfolge, subjektiven Merkmalen, Konkurrenzen und Vorschriften; trenne wesentliche Ermittlungsergebnisse, Beweismittelliste und Zuständigkeitsbegründung.", "einreichungsfähige Anklageschrift mit abstraktem und konkretem Anklagesatz, Beweismitteln, Zuständigkeit und Begleitverfügung"),
            ("Sitzungsdienst, Rechtsmittel und Vollstreckungsanschluss", "Bereite Beweisaufnahme, Fragen, Beweisanträge, Schlussvortrag und Rechtsfolgenantrag aktennah vor; prüfe nach Verkündung Beschwer, Rechtsmittel, Frist, Annahme, Rechtskraft, Asservate und Vollstreckungsübergabe.", "Sitzungsmappe mit Anträgen, Fragen, Plädoyergerüst, Rechtsmittelvermerk und vollständiger Nachlaufverfügung"),
        )
    if plugin_slug == "urteilsbauer-relationsmacher":
        return (
            ("Aktenaufnahme und Streitgegenstand", "Erfasse Parteien, Prozessrollen, Anträge, Lebenssachverhalt, Anspruchsziele, Zustellungen, Fristen, Verfahrensstand, Schriftsätze und Anlagen; bilde jeden Streitgegenstand als eigene Relationsspur.", "Relationsdeckblatt mit Anträgen, Streitgegenständen, Chronologie, Fundstellen und offenen Verfahrensfragen"),
            ("Klägerstation und Schlüssigkeit", "Unterstelle den schlüssig vorgetragenen Klägervortrag als wahr, ordne jede anspruchsbegründende Tatsache einem Tatbestandsmerkmal zu und prüfe, ob daraus die begehrte Rechtsfolge folgt; Beweisfragen bleiben hier zunächst außen vor.", "Klägerstation mit Anspruchsgrundlage, Merkmalen, konkretem Vortrag, Fundstelle, Schlüssigkeitsvotum und fehlendem Vortrag"),
            ("Beklagtenstation und Erheblichkeit", "Ordne Geständnis, einfaches oder substantiiertes Bestreiten, Einwendung und Einrede; prüfe für jede Verteidigungstatsache, ob sie bei unterstellter Wahrheit das Ergebnis ganz oder teilweise verändert.", "Beklagtenstation mit Verteidigungsmittel, Vortrag, Fundstelle, Erheblichkeit, Darlegungslast und Folge"),
            ("Replik, Duplik und sekundäre Darlegungslast", "Verfolge, ob ergänzender Vortrag eine Lücke schließt, neuen Streitstoff einführt oder auf zugängliche Gegentatsachen reagiert; prüfe Substantiierung, Erklärungslast nach ZPO Paragraf 138 und nur begründet eine sekundäre Darlegungslast.", "Wechselvortragsmatrix mit Behauptung, Bestreiten, Erwiderung, Fundstellen, Präklusionsfrage und verbleibendem Streitpunkt"),
            ("Beweislast und Beweisstation", "Ordne jede streitige erhebliche Tatsache der materiellen Beweislast, Beweismaß, Beweismittel, Beweisantritt, Gegenbeweis und möglicher Beweisvereitelung zu; formuliere das Beweisthema ohne Rechtsbegriffe oder Vorwegnahme.", "Beweisstation mit Beweisthema, Beweislast, Beweismittel, Ladungs- oder Gutachtenauftrag und möglicher Entscheidungsfolge"),
            ("Beweisaufnahme und Beweiswürdigung", "Gleiche Aussage, Urkunde, Augenschein, Gutachten und Parteianhörung mit dem Beweisthema ab; würdige Wahrnehmungsgrundlage, Konstanz, Plausibilität, Widersprüche und Gesamtergebnis nach ZPO Paragraf 286.", "ausformulierter Würdigungsbaustein mit Einzelbelegen, Gegenindizien, Beweismaß, Ergebnis und Auswirkung auf die Relation"),
            ("Prozessuale Vorfragen", "Prüfe Rechtsweg, sachliche und örtliche Zuständigkeit, Parteifähigkeit, Prozessfähigkeit, ordnungsgemäße Vertretung, Rechtshängigkeit, Klageänderung, Widerklage, Streitverkündung, Erledigung und Prozesshindernisse vor der Sachentscheidung.", "Vorfragenvermerk mit Entscheidungspunkt, Hinweisbedarf, möglicher Zwischenentscheidung und Anschlussverfügung"),
            ("Richterlicher Hinweis und Prozessleitung", "Leite aus unklarem Antrag, unschlüssigem Vortrag, ungenügendem Bestreiten, überraschendem Gesichtspunkt oder fehlendem Beweisantritt einen konkreten Hinweis nach ZPO Paragraf 139 mit Adressat, Inhalt, Frist und Dokumentation ab.", "Hinweisverfügung mit entscheidungserheblichem Punkt, Ergänzungsbedarf, Frist, möglicher Folge und Wiedervorlage"),
            ("Nebenforderungen und Verjährung", "Prüfe Zinsen, Verzug, vorgerichtliche Kosten, Auskunft, Nutzungen, Aufrechnung und Verjährung getrennt vom Hauptanspruch; rechne Zeitraum, Basis, Höhe und Teilunterliegen nachvollziehbar.", "Nebenforderungstabelle mit Anspruchsgrund, Beginn, Rechenweg, Einwendung, Antrag und Tenorfolge"),
            ("Entscheidungsstation und Votum", "Führe Ergebnisse aus Kläger-, Beklagten- und Beweisstation für jeden Antrag zusammen; kennzeichne Teilobsiegen, Hilfsantrag, Zug-um-Zug-Leistung, Feststellung, Stufenfolge und noch fehlende Entscheidungsreife.", "Entscheidungsstation mit Antrag-für-Antrag-Votum, tragender Norm, Beweisergebnis, Quote und Entscheidungsart"),
            ("Tenor, Kosten und Vollstreckbarkeit", "Formuliere bestimmten Hauptsachetenor, Kostenentscheidung und vorläufige Vollstreckbarkeit passend zu Obsiegen, Teilunterliegen, Sicherheitsleistung und gegebenenfalls Zug-um-Zug- oder Abwendungsbefugnis; führe eine Vollstreckungsprobe durch.", "vollstreckungsfähiger Tenor mit Kostenquote, Sicherheitsanordnung, Streitwertbezug und Kontrollrechnung"),
            ("Urteil und Rechtsmittelkontrolle", "Baue Rubrum, Tenor, Tatbestand, Anträge, Entscheidungsgründe, Beweiswürdigung, Nebenentscheidungen und Rechtsmittelbelehrung widerspruchsfrei; prüfe ZPO Paragraf 313 und zulässige Erleichterungen nur für die konkrete Entscheidungsart.", "vollständiger Urteilsentwurf mit Fundstellenkontrolle, Rechtsmittelwert, Zustellungsverfügung und Fehlerprotokoll"),
        )
    if plugin_slug == "anlagen-zu-schriftsaetzen":
        return (
            ("Ordnerinventur und maßgebliche Fassungen", "Öffne jede Datei, erfasse Originalname, Typ, Datum, Absender, Empfänger, Version, Unterschrift, Lesbarkeit und Bezug zum Schriftsatz; trenne Dubletten, Vorfassungen, leere Dateien und technisch nicht verwertbare Stücke.", "Anlageninventar mit Originalfundort, maßgeblicher Fassung, Status, Schriftsatzbezug, Konvertierungsbedarf und Verantwortlichem"),
            ("Beweisthema und Anlagenrelevanz", "Ordne jede Anlage einer konkreten Tatsachenbehauptung, einem Tatbestandsmerkmal oder einer Einwendung zu; markiere fehlende Belege, überflüssige Dubletten und Stücke, die mehr oder anderes enthalten als im Schriftsatz behauptet.", "Belegmatrix mit Behauptung, Anlage, Seitenfundstelle, Beweisthema, Risiko und notwendiger Textkorrektur"),
            ("Konvertierung in lesbare PDF-Dateien", "Wandle Text-, Tabellen-, Bild- und Nachrichtenformate nachvollziehbar in PDF um, bewahre Inhalt, Seitenfolge, Zeitstempel und Metadatenbezug, richte Seiten lesbar aus und führe nach jeder Konvertierung eine Sicht- und Öffnungsprobe durch.", "getrennte, lesbare PDF-Anlagen mit Konvertierungsprotokoll, Seitenkontrolle und unverändert aufbewahrtem Original"),
            ("Anlagenzeichen und sichtbare Kennzeichnung", "Bestimme Partei- und Verfahrensstand, führe die vorhandene K-, B-, ASt- oder AG-Reihe fort und bringe das Anlagenzeichen auf einer freien Stelle sichtbar an, ohne Originalinhalt, Unterschrift, Stempel oder Seitenzahl zu verdecken.", "konsistent gekennzeichnete Anlagenfolge mit Vergabeprotokoll und Kollisionskontrolle"),
            ("Anlagenverzeichnis und Schriftsatzabgleich", "Gleiche jedes im Text genannte Anlagenzeichen mit Dateiname, Dokumenttitel, Datum, Seitenzahl und tatsächlicher Datei ab; finde Sprünge, Doppelvergaben, verwaiste Verweise und Anlagen ohne Textbezug.", "vollständiges Anlagenverzeichnis mit Kurzbezeichnung, Datum, Seitenumfang, Fundstelle im Schriftsatz und Prüfergebnis"),
            ("Dateinamen und Sortierreihenfolge", "Bilde kurze sprechende Dateinamen ohne Umlaute oder scharfes S, verbinde Wörter mit Unterstrichen, stelle das Anlagenzeichen voran und prüfe Länge, erlaubte Zeichen, Sortierung und Eindeutigkeit gegen die jeweils geltenden Einreichungsvorgaben.", "sortierfähiger Versandordner mit eindeutigen Dateinamen, Reihenfolge und Umbenennungsprotokoll"),
            ("E-Mails, Chats und digitale Verläufe", "Bewahre Absender, Empfänger, CC, Datum, Uhrzeit, Betreff, Antwortverlauf, Anhänge und sichtbaren Kontext; trenne einzelne Nachricht, vollständigen Thread und beigefügte Datei und dokumentiere Auslassungen oder abgeschnittene Ansichten.", "beweisgeeignete PDF-Fassung digitaler Kommunikation mit Kopfzeilen, Chronologie, Anhangsbezug und Originaldateiverweis"),
            ("Tabellen, Berechnungen und große Seiten", "Sichere Formeln oder Rechenweg, Blattname, Druckbereich, Filter, ausgeblendete Zeilen, Einheit und Stichtag; teile breite Tabellen nur kontrolliert und füge eine lesbare Legende sowie Seitenbezug hinzu.", "lesbare Tabellenanlage mit Kontrollrechnung, Druckansicht, Blatt- und Zellbezug sowie unverändertem Ausgangsformat"),
            ("Fremdsprachige Urkunden und Übersetzungen", "Halte Original, Übersetzung, Übersetzer, Sprache, Vollständigkeit, Beglaubigungsstatus und Seitenzuordnung getrennt; entscheide anhand Gericht, Verfahrensstand und Bestreiten, ob Arbeitsübersetzung oder förmlicher Nachweis benötigt wird.", "paarweise zugeordnete Original- und Übersetzungsanlage mit Statusvermerk, Seitenkonkordanz und offenem Nachweisbedarf"),
            ("Große Anlagenbestände und Paketgrenzen", "Ermittle Dateizahl und Gesamtvolumen, bilde sachlogische Einzelanlagen oder zulässige Bände, wahre Anlagenzeichen und Seitenbezug und plane Übertragungsreihenfolge, Reserve und kontrollierte Aufteilung ohne inhaltliche Vermischung.", "Paketierungsplan mit Dateiliste, Größen, Reihenfolge, Bandlogik, Übermittlungsweg und Vollständigkeitskontrolle"),
            ("Beweisangebote und genaue Fundstellen", "Verknüpfe jede Anlage im Schriftsatz mit einer konkreten Behauptung und möglichst genauer Seite; formuliere Urkundenbeweis, Augenschein oder sonstigen Beweisantritt passend und vermeide pauschale Anlagenkonvolute ohne Tatsachenbezug.", "Fundstellen- und Beweisangebotsliste mit Textstelle, Anlage, Seite, Beweisthema und Einbauvorschlag"),
            ("Versandfreigabe und Übergabe", "Prüfe Hauptdokument, Anlagenzeichen, Verzeichnis, Dateinamen, Lesbarkeit, Signaturweg, sicheren Übermittlungsweg, Frist, Empfänger, Öffnungsprobe und spätere Eingangskontrolle nach ZPO Paragrafen 130a und 130d sowie geltender ERVV.", "freigabefähiges Anlagenpaket mit Prüfprotokoll, Restpunkten, Freigabeentscheidung und dokumentierter Übergabe an den Versand"),
        )
    if plugin_slug == "tierschutzrecht":
        output = "tierschutzrechtliche Arbeitsakte mit tierbezogenem Tatsachenbefund, Normprüfung, Verantwortlichkeit, Beweis, Verhältnismäßigkeit, Frist und sofort einsetzbarem Verfahrensdokument"
        return (
            ("Haltung und Betreuung nach Paragraf 2 TierSchG", "Ordne jedes Tier oder jede homogene Tiergruppe nach Art, Alter, Kennzeichnung, Gesundheitszustand, Fütterung, Wasser, Pflege, Platz, Bewegung, Sozialkontakt und Sachkunde; verknüpfe jede behauptete Abweichung mit Kontrollzeitpunkt, Foto, Messwert, Zeuge oder tierärztlichem Befund.", output),
            ("Erlaubnis und Sachkunde nach Paragraf 11 TierSchG", "Bestimme konkrete Tätigkeit, Erlaubnispflicht, Antragsteller, verantwortliche Person, Sachkunde, Zuverlässigkeit, Räume, Betriebsablauf, Tierbestand und Nebenbestimmungen; trenne fehlende Erlaubnis, Abweichung vom Erlaubnisumfang und bloßen Dokumentationsmangel.", output),
            ("Kontrolle, Betretung und Auskunft", "Prüfe Anlass, Zuständigkeit, Kontrollzeit, betroffene Räume, Duldungs- und Auskunftspflichten, mitgeführte Personen, Proben, Fotos, Niederschrift und Grenzen einer Selbstbelastung; sichere Einwendungen gegen unrichtige Tatsachen sofort mit Gegenbelegen.", output),
            ("Anordnung nach Paragraf 16a TierSchG", "Zerlege jede Verfügung in Adressat, Tierbezug, konkreten Verstoß, Rechtsfolge, Erfüllungsfrist, Zwangsmittel und Sofortvollzug; prüfe Bestimmtheit, belastbare Tatsachengrundlage, Auswahlermessen, mildere Abhilfe und kontrollierbaren Erfüllungsnachweis.", output),
            ("Wegnahme, Unterbringung und Veräußerung", "Rekonstruiere Zustand und Versorgung jedes betroffenen Tieres, Halterfähigkeit, Wegnahmezeitpunkt, Unterbringungsort, Kosten, Frist zur Herstellung ordnungsgemäßer Haltung, Veräußerungsentscheidung und Eigentumsposition; behandle Vollzugsschritt und Grundverfügung getrennt.", output),
            ("Eilrechtsschutz für Tierhalter und Behörde", "Bestimme Bekanntgabe, Sofortvollzug, Vollzugsstand, statthaften Antrag, Erfolgsaussichten, Tierwohlrisiko, Halterinteresse und reversible Zwischenlösung; formuliere einen vollziehbaren Antrag samt Hilfsantrag und konkretem Betreuungskonzept.", output),
            ("Tiertransport und Transportfähigkeit", "Prüfe Tierart, Strecke, Dauer, Witterung, Transportfähigkeit, Platz, Versorgung, Pausen, Zulassung, Fahrer- und Betreuernachweise, Transportpapier sowie Zustand bei Abfahrt und Ankunft; ordne jeden Befund dem verantwortlichen Beteiligten und Zeitpunkt zu.", output),
            ("Tötung, Schlachtung und vernünftiger Grund", "Prüfe konkreten Zweck, vernünftigen Grund, Alternativen, Betäubung, Sachkunde, technische Durchführung, Überwachung und Dokumentation; trenne die materiell-rechtliche Rechtfertigung von Verfahrens-, Betäubungs- oder Nachweismängeln.", output),
            ("Zucht, Qualzucht und erblich bedingte Belastung", "Erfasse Zuchtziel, Linie, konkrete Merkmale, klinische Befunde, Erblichkeit, Schmerzen, Leiden, Schäden, Nachkommen, Zuchteinsatz und fachwissenschaftliche Grundlage; formuliere Beweisfragen so, dass Diagnose, Prognose und rechtliche Wertung getrennt bleiben.", output),
            ("Straftat, Ordnungswidrigkeit und Einlassung", "Ordne jede Handlung einzeln nach Tatzeit, Tier, Täterrolle, objektivem Tatbestand, Vorsatz oder Fahrlässigkeit, Dauer, Erfolg, Unterlassen, Garantenpflicht und Beweis; sichere Strafantrag, Verjährung, Einziehung, Berufsfolgen und abgestimmte Einlassungsstrategie.", output),
            ("Fundtier, Eigentum und Kostenträger", "Kläre Fundort, Besitzaufgabe oder Verlust, Kennzeichnung, Eigentümerermittlung, Ablieferung, Verwahrung, kommunale Zuständigkeit, tierheimvertragliche Grundlage und notwendige Behandlung; trenne Fundrecht, Gefahrenabwehr, Tierschutzvollzug und privatrechtliche Kosten.", output),
            ("Unterbringungs- und Vollzugskosten angreifen", "Prüfe Grundverfügung, Kostentatbestand, Zeitraum, Tierzahl, Tagessatz, Behandlung, Verwertungserlös, Kausalität, Erforderlichkeit, Auswahl des Dienstleisters und Anhörung; rechne jede Position nach und ordne sie einem belegten Vollzugsschritt zu.", output),
        )
    if plugin_slug == "strassenrecht-infrastruktur":
        output = "straßenrechtliche Projekt- oder Verfahrensakte mit Straßenstatus, Baulastträger, Normpfad, Plan- und Kostenbelegen, Beteiligtenposition, Frist und vollzugsfähigem Entwurf"
        return (
            ("Straßenklasse, Widmung und Abschnitt", "Bestimme den betroffenen Abschnitt anhand Karte, Netzknoten, Stationierung oder Flurstück; sichere Widmungsakt, Straßenklasse, Ortsdurchfahrt, Umstufung oder Einziehung und den am Stichtag zuständigen Straßenbaulastträger.", output),
            ("Straßenbaulast und Unterhaltung", "Ordne Planung, Bau, Unterhaltung, Winterdienst, Verkehrssicherung, Beleuchtung und Nebenanlagen dem gesetzlichen Baulastträger oder einer wirksamen Vereinbarung zu; trenne Pflichtenträger, ausführende Stelle und bloße Kostenbeteiligung.", output),
            ("Gemeingebrauch und Anliegergebrauch", "Prüfe Widmungszweck, Verkehrsüblichkeit, konkrete Nutzung, Grundstückszugang, Erreichbarkeit und verbleibende zumutbare Anbindung; grenze geschützte Anliegerpositionen von bloßen Lagevorteilen und erlaubnispflichtiger Sondernutzung ab.", output),
            ("Sondernutzung beantragen oder untersagen", "Beschreibe Ort, Fläche, Aufbau, Zweck, Dauer, Verkehrsauswirkung und Wiederherstellung; prüfe Erlaubnispflicht, Satzung, Gebühr, Ermessen, Gleichbehandlung, Auflagen, Widerruf und vollstreckbare Beseitigungsanordnung.", output),
            ("Zufahrt, Anbau und Bauverbotszone", "Vermesse Abstand und Straßenbezug, bestimme freie Strecke oder Ortsdurchfahrt und ordne Hochbau, Werbeanlage, Zufahrt oder Leitungsanlage dem einschlägigen Anbau- oder Zustimmungstatbestand zu; sichere Sichtdreiecke, Verkehrsprognose und Alternativen.", output),
            ("Planfeststellung und Planrechtfertigung", "Kläre Vorhabenträger, gesetzliche Bedarfs- oder Zielbindung, Varianten, Trasse, Flächen, technische Planung, Umweltprüfung, Lärmschutz und Finanzierbarkeit; trenne Planrechtfertigung, zwingendes Recht und abwägende Konfliktbewältigung.", output),
            ("Einwendung und Betroffenheit", "Formuliere Eigentums-, Betriebs-, Zugangs-, Lärm-, Erschütterungs-, Wasser- oder Naturschutzbelang mit Grundstück, Tatsachen, Prognosekritik, Beleg, gewünschter Abhilfe und Hilfsauflage; sichere Auslegung, Frist, Zugang und Vertretung.", output),
            ("Kreuzung von Straße, Schiene, Gewässer oder Leitung", "Bestimme beteiligte Verkehrswege und Anlagen, vorhandenen Kreuzungszustand, veranlassende Maßnahme, technische Änderung, Unterhaltung, Folgekosten und Vorteilsausgleich; gleiche Gesetz, Altvereinbarung und neuen Vertragsentwurf positionsweise ab.", output),
            ("Kostenlast und Kostenmasse", "Rekonstruiere Maßnahme, Veranlasser, gesetzliche Kostenteilung, kreuzungsbedingte Kostenmasse, Sowieso-Kosten, Vorteil, Fördermittel, Abschlagsplan und Schlussrechnung; führe jede Position auf Aufmaß, Rechnung und Rechtsgrund zurück.", output),
            ("Baustelle, Sperrung und Verkehrsführung", "Prüfe Bauabschnitt, Bauzeit, Umleitung, Rettungswege, ÖPNV, Fuß- und Radverkehr, Grundstückszufahrten, Gewerbeanlieferung, Anordnung, Beschilderungsplan und Kommunikation; erstelle einen abgestimmten Freigabe- und Eskalationsplan.", output),
            ("Eilrechtsschutz vor Bau- oder Sperrbeginn", "Bestimme angegriffene Entscheidung, Vollziehbarkeit, Zustellung, Baubeginn, irreversible Folgen, statthaften Antrag, Antragsbefugnis und Folgenabwägung; formuliere Haupt- und Hilfsantrag mit konkreter Zwischenregelung.", output),
            ("Straßenrechtliche Vereinbarung und Vollzug", "Erstelle oder prüfe eine Vereinbarung zu Planung, Grunderwerb, Bau, Unterhaltung, Kosten, Haftung, Verkehrssicherung, Änderungen, Abnahme, Dokumentation und Streitlösung; ordne jede Pflicht einem Termin, Verantwortlichen und Nachweis zu.", output),
        )
    if plugin_slug == "strassenverkehrsrecht-stvo":
        output = "straßenverkehrsrechtliche Entscheidungsakte mit Ortsbefund, Anordnungsakte, Tatsachengrundlage, Normtatbestand, Ermessensprüfung, Beschilderungsabgleich, Frist und versandfähigem Dokument"
        return (
            ("Verkehrsanordnung und Behördenakte", "Sichere genaue Straße, Abschnitt, Fahrtrichtung, Zeichen, Zusatzzeichen, Markierung, zeitliche Geltung, Anordnungsdatum, Zuständigkeit, Anhörungen, Plan, Begründung und Umsetzungsnachweis; behandle Anordnung und sichtbaren Vollzug als zwei Beweisebenen.", output),
            ("Ortsbefund und Sichtbarkeit", "Dokumentiere Standort, Annäherungsrichtung, Sichtweite, Verdeckung, Beleuchtung, Witterung, konkurrierende Zeichen, Fahrbahnmarkierung und Wiederholung mit datierten Fotos und Maßangaben; gleiche jeden Befund mit dem Verkehrszeichenplan ab.", output),
            ("Gefahrenlage und Paragraf 45 StVO", "Bestimme den konkreten Anordnungszweck und prüfe, ob eine besondere örtliche Gefahrenlage erforderlich ist; werte Unfallzahlen, Geschwindigkeiten, Verkehrsmenge, Konfliktpunkte und Prognosezeitraum aus und teste räumlich oder zeitlich mildere Maßnahmen.", output),
            ("Bewohnerparken und Parkraumbewirtschaftung", "Prüfe erheblichen Parkraummangel, Bewohnerstruktur, Gebietsabgrenzung, Wechselwirkungen mit Gewerbe und Besuchern, Privilegierungsumfang, Gebührenregel und Evaluation; bereite Anordnung, Zonenplan und Begründungsvermerk konsistent vor.", output),
            ("Bussonderfahrstreifen und ÖPNV-Priorisierung", "Erfasse Linien, Takt, Verspätungsdaten, Abschnitt, Betriebszeiten, zugelassene Mitbenutzer, Knotenwirkungen und Ausweichverkehr; prüfe Geeignetheit, Netzfolgen, Beschilderung, Markierung und Kontrollkonzept.", output),
            ("Fahrradstraße und Radverkehrsführung", "Prüfe Netzfunktion, vorherrschenden oder angestrebten Radverkehr, zugelassenen Kraftverkehr, Vorfahrt, Geschwindigkeit, Breite, ruhenden Verkehr, Konfliktstellen und bauliche Begleitmaßnahmen; formuliere einen widerspruchsfreien Zeichen- und Markierungsplan.", output),
            ("Schulstraße, Schulweg und Tempoanordnung", "Ordne Schulzeiten, Hol- und Bringverkehr, Geh- und Radwege, Sichtbeziehungen, Unfall- und Beinaheunfalldaten, Rettungs- und Anliegerverkehr sowie Ausnahmen; entwickle eine befristete oder dauerhafte Regelung mit Evaluation und Vollzug.", output),
            ("Haltverbot, Ladezone und mobile Beschilderung", "Bestimme Beginn und Ende, Pfeilrichtung, Aufstellzeitpunkt, Vorlauf, Anlass, betroffene Fahrzeuge, Zusatzzeichen, Protokoll und Fotos; prüfe Bestimmtheit, Sichtbarkeit, Ausnahme, Abschleppvoraussetzungen und Nachweis gegenüber dem Halter.", output),
            ("Baustellenverkehr und verkehrsrechtliche Anordnung", "Gleiche Bauzeitenplan, Verkehrsphasen, Regelplan, Restbreiten, Lichtsignalanlage, Umleitung, Fuß- und Radführung, Rettungswege, ÖPNV und Grundstückszugänge ab; dokumentiere Freigabe, tägliche Kontrolle und Mängelbeseitigung.", output),
            ("Ausnahmegenehmigung nach Paragraf 46 StVO", "Beschreibe Regelverbot, Person, Fahrzeug, Strecke, Zeitraum, atypische Härte oder öffentliches Interesse, Sicherheitsrisiko und mögliche Auflagen; begründe Ermessen und Gleichbehandlung mit belastbaren Einzelfalltatsachen.", output),
            ("Verkehrszeichen, Vollzug und Ordnungswidrigkeit", "Trenne Rechtmäßigkeit und Wirksamkeit der Verkehrsregelung, Erkennbarkeit für den Betroffenen, konkreten Verstoß, Fahreridentität, Beweis und Rechtsbehelf gegen Anordnung beziehungsweise Bußgeld; übertrage Einwände nicht ungeprüft zwischen beiden Verfahren.", output),
            ("Widerspruch, Klage und Eilverfahren", "Bestimme Bekanntgabe durch erstmalige Konfrontation, fortdauernde Beschwer, Klageart, Frist, Vollzugsdruck und statthaften Eilantrag; formuliere Antrag, Tatsachenkern, Ortsbelege, Ermessensfehler, Hilfslösung und Anlagenverzeichnis.", output),
        )
    if plugin_slug == "umweltschutzverband-verbandsklage":
        output = "verbandsklagefähige Umweltakte mit Anerkennung, Entscheidungsgegenstand, Beteiligung, Rüge, Fachbeleg, Klage- oder Eilantrag, Fehlerfolge und umsetzbarer Abhilfe"
        return (
            ("Anerkennung und satzungsmäßiger Aufgabenbereich", "Prüfe Anerkennungsbescheid, räumlichen und sachlichen Tätigkeitsbereich, Mitgliederstruktur, Vertretung, Beschluss zur Rechtsverfolgung und Satzungszweck; sichere Vollmacht und internen Freigabebeschluss vor Fristablauf.", output),
            ("Entscheidung im Anwendungsbereich des UmwRG", "Ordne Zulassungsentscheidung, Plan, Programm, Vorhaben oder behördliches Unterlassen einer konkreten Fallgruppe des Umweltrechtsbehelfsgesetzes zu; bestimme Behörde, Vorhabenträger, Bekanntmachung und maßgebliches Fachrecht.", output),
            ("Beteiligung und Aktenzugang", "Rekonstruiere Auslegung, Unterlagenbestand, Bekanntmachung, digitale Zugänglichkeit, Stellungnahmefrist, Erörterung und Nachreichungen; verlange fehlende Fachbeiträge gezielt und dokumentiere jede Zugangshürde.", output),
            ("Einwendung ohne Präklusionsfalle", "Formuliere Umweltbelang, räumlichen Bezug, betroffene Art oder Schutzgut, Tatsachen, Fachquelle, Ermittlungsdefizit, Rechtsfolge und Abhilfe so konkret wie nach Aktenstand möglich; trenne spätere Vertiefung von einem neuen Streitgegenstand.", output),
            ("UVP-Pflicht, Vorprüfung und Öffentlichkeitsbeteiligung", "Prüfe Vorhabentyp, Größenwerte, Kumulation, Standortmerkmale, Vorprüfung, Dokumentation, UVP-Bericht, Alternativen, Beteiligung und zusammenfassende Darstellung; ordne Verfahrensfehler und mögliche Heilung gesondert.", output),
            ("Artenschutz und fachliche Methodik", "Bestimme betroffene Arten, Fortpflanzungs- und Ruhestätten, Erfassungszeitraum, Kartiermethode, Wirkpfad, Vermeidungsmaßnahme, Ausnahmevoraussetzungen und Monitoring; übersetze methodische Kritik in konkrete Beweisanträge oder Auflagen.", output),
            ("Gebiets- und Habitatschutz", "Prüfe Schutzgebiet, Erhaltungsziele, Wirkraum, Summationsprojekte, Verträglichkeitsprüfung, erhebliche Beeinträchtigung, Alternativen und Kohärenzsicherung; trenne Prognoseunsicherheit, Vermeidungsmaßnahme und Ausnahmeprüfung.", output),
            ("Eilrechtsschutz vor irreversiblem Vollzug", "Sichere Rodungs-, Bau-, Fang- oder Inbetriebnahmetermin, Vollziehbarkeit, statthaften Antrag, Antragsbefugnis, Fachbelege und Folgenabwägung; beantrage eine konkrete, kontrollierbare Zwischenregelung statt pauschalen Stillstandes.", output),
            ("Umweltinformation und fehlende Fachunterlagen", "Bezeichne Datensatz, Gutachten, Messreihe, Stellungnahme oder Monitoringbericht nach Behörde, Zeitraum und Vorhaben; prüfe Anspruch, Ausnahme, Teilzugang, Drittbeteiligung, Format, Gebühr und beschleunigten Rechtsschutz.", output),
            ("Fehlerfolge, Heilung und Planergänzung", "Ordne jeden Verfahrens-, Ermittlungs-, Bewertungs- oder Abwägungsfehler seiner gesetzlichen Folge zu; prüfe Kausalität, Heilung, ergänzendes Verfahren, Planergänzung, Aufhebung und Sicherungsbedarf bis zur Nachbesserung.", output),
            ("Sachverständigenkritik und Gegenbeweis", "Gleiche Auftrag, Datengrundlage, Methode, Zeitraum, Unsicherheit, Schlussfolgerung und Nebenbestimmung jedes Gutachtens ab; formuliere konkrete Ergänzungsfragen und belege, warum der Mangel entscheidungserheblich ist.", output),
            ("Klageantrag, Abhilfe und Vergleich", "Formuliere Haupt- und Hilfsanträge, angegriffene Entscheidung, Klagegründe, Belege, Fehlerfolge und Vollzugsbegehren; entwickle daneben vollziehbare Auflagen, Monitoring, Nachsteuerung und Kostenregelung als mögliche Konfliktlösung.", output),
        )
    if plugin_slug == "informationsfreiheit-presseauskunft":
        output = "zugangs- oder auskunftsfähige Verfahrensakte mit Informationsgegenstand, Anspruchsregime, Frist, Ausschlussgrund, Drittinteresse, Teilzugang, Kosten und versandfertigem Antrag oder Rechtsbehelf"
        return (
            ("Informationsgegenstand präzise bezeichnen", "Formuliere Dokumentart, Vorgang, Zeitraum, Organisationseinheit, Aktenzeichen, Suchbegriffe und gewünschtes Format so, dass vorhandene Informationen auffindbar sind, ohne eine neue behördliche Auswertung als vermeintlichen Zugangsanspruch zu verlangen.", output),
            ("IFG, UIG, VIG oder Landesrecht auswählen", "Ordne informationspflichtige Stelle, Informationsart, Bundes- oder Landesebene und spezialgesetzlichen Zugang; dokumentiere Anspruchsberechtigung, Subsidiarität, Frist, Rechtsweg und die Folgen einer falschen Adressierung.", output),
            ("Presseauskunft mit Aktualitätsbezug", "Bezeichne Medium, journalistische Recherche, konkrete Fragen, Verantwortlichkeit der Stelle, Aktualität, Antwortformat und Veröffentlichungstermin; begründe bei Zeitdruck, warum eine spätere Auskunft ihren Nachrichtenwert verliert.", output),
            ("Schutz öffentlicher Belange", "Prüfe jeden geltend gemachten Schutzgrund passagenbezogen nach betroffenem Rechtsgut, konkreter Nachteilsprognose, zeitlicher Fortdauer, Kausalität und möglichem Teilzugang; eine bloße Wiedergabe des Gesetzes genügt nicht.", output),
            ("Behördlicher Entscheidungsprozess", "Trenne Entwurf, interne Beratung, zugrunde liegende Tatsachen, abgeschlossenen Vorgang und nachwirkenden Beratungsvertraulichkeitsschutz; bestimme, welche Informationen nach Abschluss zugänglich werden und welche Passage weiterhin geschützt ist.", output),
            ("Personenbezogene Daten und Abwägung", "Erfasse betroffene Person, Datenkategorie, Funktion, Amtsbezug, Schutzintensität, Einwilligung, öffentliches Informationsinteresse, mögliche Anonymisierung und Drittanhörung; entscheide für jede Passage statt für das Gesamtdokument.", output),
            ("Betriebs- und Geschäftsgeheimnisse", "Verlange konkrete Darlegung von Geheimnischarakter, fehlender Offenkundigkeit, Geheimhaltungswillen, wirtschaftlichem Wert und drohendem Wettbewerbsnachteil; prüfe Drittanhörung, Einwilligung, Teilzugang und zeitlichen Bedeutungsverlust.", output),
            ("Urheberrecht, Datenbank und Nutzungsformat", "Trenne Zugang zur Information von urheberrechtlicher Weiternutzung; prüfe Einsicht, Kopie, vorhandenes elektronisches Format, Metadaten, Datenbankauszug, Lizenzhinweis und technisch mögliche Teilbereitstellung.", output),
            ("Drittbeteiligung und Stellungnahme", "Bezeichne betroffene Information, mögliche Schutzposition und beabsichtigte Offenlegung so genau wie nötig; setze Frist, sichere Zustellung und würdige die Stellungnahme eigenständig, ohne dem Dritten ein Entscheidungsrecht zu übertragen.", output),
            ("Gebühr, Aufwand und Antragszuschnitt", "Prüfe Gebührenordnung, voraussichtlichen Such- und Prüfaufwand, Gebührenankündigung, Obergrenze, Billigkeit, Aufteilung und möglichen engeren Antrag; verhindere überraschende Kosten durch einen schriftlichen Kostenkorridor.", output),
            ("Widerspruch und Verpflichtungsklage", "Rekonstruiere Antrag, Eingang, Präzisierung, Frist, Bescheid, Rechtsbehelfsbelehrung und Teilzugang; greife jeden Ausschlussgrund, jede Schwärzung und die Gebühr gesondert mit bestimmtem Zugangsbegehren an.", output),
            ("Eilrechtsschutz für aktuelle Auskunft", "Belege Recherchegegenstand, Presse- oder Veranstaltungstermin, bisherige Kommunikation, Anspruch, Anordnungsgrund und erforderliche konkrete Auskunft; formuliere einen vollziehbaren Antrag, der die Hauptsache nicht unnötig überschreitet.", output),
        )
    if plugin_slug == "haushaltsrecht-bho-bund-laender":
        output = "revisionsfeste Haushaltsakte mit Ermächtigung, Titelbezug, Wirtschaftlichkeitsrechnung, Freigaben, Vollzugsbelegen, Rechtsfolge, Verantwortlichem und unterschriftsreifem Vermerk"
        return (
            ("Haushaltstitel und Verfügbarkeit", "Sichere Haushaltsebene, Haushaltsjahr, Einzelplan, Kapitel, Titel, Zweckbestimmung, Ansatz, Ausgaberest, Sperre, Deckungsfähigkeit, Bindungen und aktuellen verfügbaren Betrag; trenne kassenmäßige Liquidität von haushaltsrechtlicher Ermächtigung.", output),
            ("Verpflichtungsermächtigung und Folgejahre", "Ordne Vertragslaufzeit, Fälligkeiten und Höchstbeträge den betroffenen Haushaltsjahren zu; prüfe Verpflichtungsermächtigung, Jahresbeträge, Freigabe, Vorbelastung, Kündigungsoption und Dokumentation vor Vertragsschluss.", output),
            ("Wirtschaftlichkeitsuntersuchung nach Paragraf 7 BHO", "Definiere Ziel und Mindestanforderung, bilde realistische Handlungsalternativen einschließlich Fortführung oder Verzicht, rechne Investition, Betrieb, Personal, Risiko und Restwert über denselben Zeitraum und teste kritische Annahmen in Sensitivitäten.", output),
            ("Mittelbewirtschaftung und Freigabekette", "Bestimme Beauftragten für den Haushalt, Titelverwalter, sachlich und rechnerisch Feststellenden, Anordnungsbefugten und Kasse; ordne Reservierung, Festlegung, Auftrag, Rechnung, Feststellung, Anordnung und Zahlung zeitlich und funktional.", output),
            ("Zuwendungsbedarf und Förderart", "Prüfe erhebliches Bundes- oder Landesinteresse, fehlende Eigenfinanzierung, Projekt- oder institutionelle Förderung, Finanzierungsart, Bemessungsgrundlage, Eigenmittel, Drittmittel, Besserstellungsverbot und beihilferechtliche Schnittstelle.", output),
            ("Bewilligungsbescheid und Nebenbestimmungen", "Formuliere Zweck, Zeitraum, Höchstbetrag, Finanzierungsart, Auszahlung, Nachweis, Vergabeauflagen, Mitteilungspflichten, Prüfrechte, Widerrufsvorbehalt und Rechtsbehelf widerspruchsfrei; gleiche Bescheid und Finanzierungsplan zeilenweise ab.", output),
            ("Mittelabruf und Kassenanordnung", "Prüfe Fälligkeit, Bedarf, Abrufplan, Bankverbindung, Vier-Augen-Prinzip, sachliche und rechnerische Feststellung, Zahlungsgrund, Buchungsstelle und Auszahlungsbeleg; stoppe Dublette, falschen Empfänger oder fehlende Leistung.", output),
            ("Verwendungsnachweis und Prüfung", "Gleiche Sachbericht, zahlenmäßigen Nachweis, Belegliste, Vergabe, Inventar, Fristen, Zielerreichung und nicht verbrauchte Mittel mit dem Bescheid ab; kennzeichne Abweichung, Nachforderung, Anerkennung und offene Prüffrage positionsweise.", output),
            ("Rücknahme, Widerruf und Erstattung", "Trenne anfängliche Rechtswidrigkeit, nachträglichen Zweck- oder Auflagenverstoß, Ermessen, Vertrauensschutz, Teilwiderruf, Erstattungsbetrag, Zinsen, Anhörung und Verjährung; rechne den Rückforderungsbetrag aus belegten Zahlungsdaten.", output),
            ("Vergabe und haushaltsrechtliche Dokumentation", "Bestimme Beschaffungsgegenstand, Bedarf, Schätzwert, Vergaberegime, Wettbewerb, Losbildung, Wertung, Zuschlag und Vertrag; dokumentiere zusätzlich Mittelbindung, Wirtschaftlichkeit und Freigaben, ohne Vergabe- und Haushaltsrecht gleichzusetzen.", output),
            ("Haushaltssperre, Deckung und Umschichtung", "Prüfe Art und Reichweite der Sperre, Freigabebefugnis, echte oder unechte Deckungsfähigkeit, Verstärkungsbedarf, über- oder außerplanmäßige Ausgabe, Unvorhergesehenheit und Unabweisbarkeit sowie parlamentarische Beteiligung.", output),
            ("Rechnungsprüfung und Beanstandungsantwort", "Ordne jeden Prüfungsbefund zu Norm, Vorgang, Betrag, Verantwortlichem, Aktenfund und Auswirkung; kläre Sachverhalt, räume berechtigten Fehler mit Maßnahme aus und widersprich unbelegter Beanstandung mit dokumentierter Gegenrechnung.", output),
        )
    if plugin_slug == "kommunalrecht-laender":
        output = "kommunalrechtliche Beschluss- oder Verfahrensakte mit Landesrechtsstand, Organzuständigkeit, Sitzungsnachweis, materieller Prüfung, Haushaltsfolge, Vollzug und versand- oder bekanntmachungsfähigem Dokument"
        return (
            ("Landesrecht, Kommune und Zuständigkeit", "Bestimme Land, Gemeinde- oder Kreisstatus, aktuelle Kommunalverfassung, Hauptsatzung, Zuständigkeitsordnung und Geschäftsordnung; ordne Aufgabe, Organ, Ausschuss, Bürgermeister, Rat und mögliche Delegation mit Fundstelle zu.", output),
            ("Einladung, Tagesordnung und Öffentlichkeit", "Prüfe Einberufung, Zugang, Form, Frist, Tagesordnungspunkt, Dringlichkeit, öffentliche oder nichtöffentliche Behandlung und Bekanntmachung; formuliere einen hinreichend bestimmten Beratungs- und Beschlussgegenstand.", output),
            ("Befangenheit und Mitwirkungsverbot", "Erfasse Mandatsträger, persönliche oder wirtschaftliche Beziehung, unmittelbaren Vor- oder Nachteil, Gruppeninteresse, Arbeitgeber- oder Organbezug, Offenlegung, Ausschluss, Verlassen des Raums und Protokollierung nach dem jeweiligen Landesrecht.", output),
            ("Beschlussfähigkeit, Mehrheit und Niederschrift", "Bestimme gesetzliche Mitgliederzahl, anwesende und stimmberechtigte Mitglieder, Quorum, erforderliche Mehrheit, Abstimmungsform, Ergebnis, Sondervotum und Protokollgenehmigung; rechne Enthaltungen nur nach geltendem Landesrecht ein.", output),
            ("Satzung entwerfen und bekannt machen", "Prüfe Ermächtigungsgrundlage, Geltungsbereich, Tatbestand, Rechtsfolge, Bestimmtheit, Gleichbehandlung, Übergang, Ordnungswidrigkeit, Beschluss, Ausfertigung und Bekanntmachungsform; erstelle Normtext und Vollzugscheck gemeinsam.", output),
            ("Kommunale Gebühren und Beiträge", "Ordne Einrichtung, Satzung, Abgabentatbestand, Schuldner, Maßstab, Kalkulationszeitraum, Kosten, Über- oder Unterdeckung, Fälligkeit und Billigkeit dem jeweiligen Kommunalabgabengesetz zu; führe den Bescheidbetrag auf die Kalkulation zurück.", output),
            ("Öffentliche Einrichtung und Benutzung", "Prüfe Widmung, Benutzerkreis, Zulassung, Kapazität, Gleichbehandlung, Anschluss- oder Benutzungszwang, Hausrecht, Ausschluss und Gebühr; entwirf Zulassungs-, Auflagen- oder Ablehnungsentscheidung mit Rechtsbehelf.", output),
            ("Kommunalhaushalt und Verpflichtung", "Sichere Haushaltssatzung, Produkt oder Titel, Ansatz, Sperre, Verpflichtung, Folgekosten, Wirtschaftlichkeit, Deckung und aufsichtsrechtliche Genehmigung; verknüpfe Beschlussvorschlag mit konkretem Finanzierungspfad.", output),
            ("Kommunales Unternehmen und Beteiligung", "Bestimme öffentlichen Zweck, Subsidiarität, Rechtsform, Beteiligungsquote, Organrechte, Wirtschaftsplan, Haftung, Vergabe- und Beihilfeschnittstelle, Anzeige oder Genehmigung sowie Berichtspflichten der Kommune.", output),
            ("Beanstandung und Kommunalaufsicht", "Prüfe Aufsichtsart, Rechtsgrund, Zuständigkeit, beanstandeten Beschluss, Anhörung, Frist, Suspensiveffekt, Ersatzvornahme oder Anweisung und kommunalen Rechtsschutz; trenne Rechts- von Zweckmäßigkeitskontrolle.", output),
            ("Kommunalverfassungsstreit", "Ordne beteiligte Organe oder Organteile, organschaftliche Rechtsposition, konkrete Maßnahme, Rechtsschutzbedürfnis, statthafte Klage- oder Antragsart und Eilbedarf; formuliere einen auf die Innenrechtsposition zugeschnittenen Antrag.", output),
            ("Beschlussvollzug und Wirksamkeitskontrolle", "Erstelle nach der Sitzung eine Kette aus Niederschrift, Ausfertigung, Anzeige oder Genehmigung, Bekanntmachung, Bescheid, Vertrag, Haushaltsbuchung, Verantwortlichem und Termin; markiere jeden Wirksamkeits- und Vollzugsstopp.", output),
        )
    if plugin_slug == "schulrecht-laender":
        output = "schulrechtliche Fallakte mit anwendbarem Landesrecht, Schülerstatus, Bescheid- und Ereignischronologie, pädagogischer Tatsachengrundlage, Beteiligung, Eilbedarf und sofort nutzbarem Schreiben oder Antrag"
        return (
            ("Schulaufnahme und Schulbezirk", "Bestimme Schulart, Jahrgang, Wohnsitz, Schulbezirk, Aufnahmeantrag, Kapazität, Auswahlkriterien, Geschwister- oder Härtefall, Bescheid, Bekanntgabe und verbleibende Alternativen nach dem aktuellen Landesrecht.", output),
            ("Schulwechsel und Zuweisung", "Rekonstruiere Anlass, pädagogische Gespräche, Fördermaßnahmen, Kindes- und Elternanhörung, zuständige Schulbehörde, Zielschule, Aufnahmebereitschaft, Schulweg und sofortige Folgen; trenne freiwilligen Wechsel von belastender Zuweisung.", output),
            ("Inklusion und sonderpädagogische Förderung", "Erfasse Behinderung oder Förderbedarf, funktionale Auswirkungen, Gutachten, Förderplan, Elternwunsch, geeignete Schule, personelle und sächliche Vorkehrungen, konkrete Mehrbelastung und Entscheidungsverfahren; vermeide pauschale Ressourcenargumente.", output),
            ("Nachteilsausgleich", "Bestimme konkrete Beeinträchtigung, Prüfungs- oder Unterrichtsanforderung, fachärztlichen oder pädagogischen Beleg, beantragte Maßnahme, Wahrung des Leistungsziels, Dauer, Vertraulichkeit und Dokumentation; formuliere eine umsetzbare Entscheidung.", output),
            ("Leistungsbewertung und Zeugnis", "Sichere Bewertungsgrundlage, Aufgabenstellung, Erwartungshorizont, Einzelbewertungen, Gewichtung, Dokumentation, krankheits- oder störungsbedingte Besonderheit, Konferenzentscheidung und landesrechtlichen Überdenkungs- oder Rechtsbehelfsweg.", output),
            ("Ordnungsmaßnahme und rechtliches Gehör", "Trenne pädagogische Einwirkung von förmlicher Ordnungsmaßnahme; prüfe konkretes Verhalten, Beweise, Schüler- und Elternanhörung, Zuständigkeit, Stufenfolge, Verhältnismäßigkeit, Begründung, Bekanntgabe und Vollzug.", output),
            ("Unterrichtsausschluss und Akutmaßnahme", "Bestimme Vorfall, Gefahr, Dauer, Entscheidungsbefugnis, Sofortmaßnahme, Anhörung, Beschulung während des Ausschlusses, Rückkehrplan und Eilbedarf; sichere Video-, Nachrichten-, Zeugen- und Aufsichtsbelege rechtmäßig.", output),
            ("Mobbing, Gewalt und Schutzpflicht", "Erstelle eine ereignisgenaue Chronologie mit Beteiligten, Orten, Aufsicht, Meldungen, Reaktionen, medizinischen oder digitalen Belegen und fortbestehendem Risiko; fordere konkrete Schutzmaßnahmen, Zuständigkeit, Termin und Wirksamkeitskontrolle.", output),
            ("Schülerdaten, digitale Plattform und Akteneinsicht", "Prüfe Datenart, schulischen Zweck, Rechtsgrundlage, Empfänger, Einwilligung, Aufbewahrung, Zugriffsrechte und Protokolle; trenne Akteneinsicht, Auskunft, Berichtigung und Löschung und sichere prüfungsrelevante Unterlagen unverändert.", output),
            ("Elternrechte und volljähriger Schüler", "Ordne Sorgeberechtigung, Vertretung, Informations- und Beteiligungsrechte, Volljährigkeit, Schweigepflicht, getrennt lebende Eltern und Schülerwillen; adressiere jedes Schreiben an die tatsächlich berechtigte Person.", output),
            ("Schülerbeförderung und notwendige Kosten", "Prüfe Schulweg, Entfernung, Alter, Gefährlichkeit, zuständige Schule, Behinderung, Beförderungsart, Eigenanteil, Antrag, Nachweise und Satzung; rechne Zeitraum und Erstattungsbetrag nachvollziehbar.", output),
            ("Widerspruch, Klage und Eilrechtsschutz", "Bestimme Handlungsform, Bescheid, Bekanntgabe, Vorverfahren, Klageart, Vollzugstermin, Anordnungsanspruch und Anordnungsgrund; formuliere Haupt- und Hilfsziel so, dass Unterricht, Prüfung oder Schulbesuch praktisch gesichert werden.", output),
        )
    if plugin_slug == "verbraucherinsolvenz-schuldenbereinigung":
        output = "vollständige Verbraucherinsolvenzakte mit Gläubiger- und Vermögensabgleich, Fristen, Formularstand, Schuldenbereinigungsweg, Pfändungsschutz, Restschuldbefreiungsrisiko und einreichungsfähigem Dokument"
        return (
            ("Schuldnerstatus und Verfahrenszugang", "Prüfe natürliche Person, aktuelle oder frühere Selbständigkeit, Zahl der Gläubiger, Forderungen aus Arbeitsverhältnissen, Zahlungsunfähigkeit, Wohnsitz, internationale Bezüge und Zuständigkeit; begründe Verbraucher- oder Regelinsolvenzverfahren ausdrücklich.", output),
            ("Gläubiger- und Forderungsverzeichnis", "Gleiche Mahnungen, Titel, Vollstreckungen, Abtretungen, Zinsen, Kosten, Sicherheiten, Bürgschaften und Mitverpflichtete je Gläubiger ab; führe bestrittene, bedingte und nachrangige Positionen mit Originalbeleg und Stichtagsbetrag.", output),
            ("Vermögen, Einkommen und Pfändbarkeit", "Erfasse Konten, Bargeld, Fahrzeuge, Versicherungen, Genossenschaftsanteile, Steuererstattungen, Ansprüche, Hausrat, Einkommen, Unterhaltspflichten und Drittrechte; trenne Massezugehörigkeit, Pfändbarkeit, Freigabe und Verwertung.", output),
            ("Außergerichtlicher Einigungsversuch", "Entwickle aus bereinigtem Einkommen, verwertbarem Vermögen, Laufzeit und Vergleichsquote einen realistischen Plan; versende Forderungsabgleich und Angebot nachweisbar, dokumentiere Antworten und bewerte Annahme nur anhand klarer Zustimmung.", output),
            ("Bescheinigung des Scheiterns", "Prüfe Beratungsberechtigung, ernsthaften Einigungsversuch, vollständigen Gläubigerkreis, Planinhalt, Scheiternsdatum und Sechsmonatszeitraum; erstelle Bescheinigung erst aus belegter Kommunikation und nicht aus einer bloßen Erwartung des Scheiterns.", output),
            ("Insolvenzantrag und amtliche Formulare", "Fülle Antrag, Restschuldbefreiungsantrag, Abtretungserklärung, Vermögens-, Gläubiger- und Forderungsverzeichnisse konsistent; gleiche Namen, Anschriften, Summen, Anlagen und Unterschriften mit dem aktuellen amtlichen Formularsatz ab.", output),
            ("Gerichtlicher Schuldenbereinigungsplan", "Prüfe Ruhen des Insolvenzantrags, Planinhalt, Beteiligung aller Gläubiger, Kopf- und Summenmehrheit, Einwendungen und mögliche Zustimmungsersetzung; rechne jede Gläubigerbehandlung und Vergleichsquote nach.", output),
            ("Pfändungsschutzkonto und laufende Vollstreckung", "Sichere Kontopfändung, Eingang von Lohn, Sozialleistung, Kindergeld oder Nachzahlung, Grundfreibetrag, Bescheinigung, Unterhaltspflichten, Freigabeantrag und Monatswechsel; koordiniere Vollstreckungsschutz mit dem Insolvenzantrag.", output),
            ("Forderungsanmeldung und Bestreiten", "Prüfe Tabelle, Forderungsgrund, Deliktskennzeichnung, Titel, Betrag, Rang, Prüfungstermin und Widerspruch; trenne Bestreiten der Forderungshöhe von der Eigenschaft als vorsätzlich begangene unerlaubte Handlung.", output),
            ("Obliegenheiten und Versagungsrisiken", "Ordne Erwerbsbemühung, Auskunft, Vermögensherausgabe, Wohnsitz- und Arbeitgeberwechsel, Zahlungen an Treuhänder und Gläubigergleichbehandlung dem jeweiligen Verfahrensabschnitt zu; dokumentiere Pflicht und Nachweis kalenderfähig.", output),
            ("Verfahrenskostenstundung", "Prüfe persönlichen und wirtschaftlichen Status, Antrag, Erklärung, Vollständigkeit, Versagungsrisiko und mögliche Raten; trenne Stundung der Verfahrenskosten von Beratungshilfe, Prozesskostenhilfe und Schuldenvergleichskosten.", output),
            ("Restschuldbefreiung und Nachlauf", "Erstelle einen Zeitstrahl von Antrag, Eröffnung, Abtretungsfrist, Berichten, Verteilungen, Anhörung und Entscheidung; ordne ausgenommene Forderungen, neue Schulden, Register- oder Vollstreckungsfolgen und notwendige Berichtigungsanträge.", output),
        )
    if plugin_slug == "oeffentliches-wirtschaftsrecht":
        output = "wirtschaftsverwaltungsrechtliche Akte mit Marktrolle, Erlaubnistatbestand, Zuverlässigkeitsbefund, Verfahrensrechten, Grundrechts- und Ermessenskontrolle, Frist und vollziehbarem Behörden- oder Prozessprodukt"
        return (
            ("Marktzugang und Erlaubnispflicht", "Bestimme Tätigkeit, Geschäftsmodell, Betriebsstätte, verantwortliche Personen, Erlaubnis- oder Anzeigetatbestand, Ausnahmen, zuständige Behörde und erforderliche Nachweise; trenne berufs-, gewerbe-, produkt- und anlagenbezogene Genehmigungen.", output),
            ("Zuverlässigkeit und Prognose", "Ordne jede verwertete Tatsache nach Person, Zeitpunkt, Pflicht, Gewicht, Wiederholungsgefahr und Beleg; prüfe Tilgung, Verfahrensstand, organisatorische Abhilfe und Zukunftsprognose statt vergangenes Fehlverhalten schematisch fortzuschreiben.", output),
            ("Gewerbeuntersagung nach Paragraf 35 GewO", "Prüfe Gewerbetreibenden, Unzuverlässigkeit, betroffene Tätigkeit, mögliche Erstreckung, Anhörung, Ermessen, Schutz Dritter, sofortige Vollziehung und Wiedergestattung; formuliere den Verfügungssatz personell und sachlich bestimmt.", output),
            ("Nebenbestimmung und Auflage", "Zerlege Bedingung, Befristung, Widerrufsvorbehalt oder Auflage nach Rechtsgrundlage, Zweck, Bestimmtheit, Verhältnismäßigkeit, Vollzugsnachweis und isolierter Anfechtbarkeit; entwickle eine mildere, kontrollierbare Fassung.", output),
            ("Wirtschaftsaufsicht und Auskunftsverlangen", "Prüfe Zuständigkeit, Adressat, konkrete Auskunft, Zeitraum, Dateninhaber, Vorlageform, Geschäftsgeheimnis, Selbstbelastungsrisiko, Frist und Zwangsmittel; liefere belegte Teilauskunft und begründete Schutzposition getrennt.", output),
            ("Subvention, Zuwendung und Rückforderung", "Ordne Bewilligung, Zweck, Nebenbestimmung, Auszahlung, Verwendung, Änderung, Mitteilung, Anhörung, Rücknahme oder Widerruf, Vertrauensschutz, Ermessen, Erstattung und Zins; rechne den Betrag aus Zahlungs- und Verwendungsbelegen.", output),
            ("Öffentliches Unternehmen und wirtschaftliche Betätigung", "Prüfe Träger, Rechtsform, öffentlicher Zweck, Subsidiarität, Marktbezug, Beteiligungsverfahren, Finanzierung, Haftung, Vergabe- und Beihilfeschnittstelle sowie kommunal- oder haushaltsrechtliche Genehmigung.", output),
            ("Dienstleistungsfreiheit und Anerkennung", "Bestimme Herkunfts- und Tätigkeitsstaat, vorübergehende oder dauerhafte Tätigkeit, Berufsqualifikation, Genehmigungsanforderung, zwingenden Allgemeinbelang, Diskriminierung, Verhältnismäßigkeit und unionsrechtliches Verwaltungsverfahren.", output),
            ("Beihilfe und wirtschaftlicher Vorteil", "Prüfe Unternehmen, staatliche Mittel, Zurechenbarkeit, wirtschaftlichen Vorteil, Selektivität, Wettbewerb und Handelsbeeinträchtigung; ordne Freistellung, Anmeldung, Durchführungsverbot, Rückforderung und Vertragsvollzug getrennt.", output),
            ("Sanktion, Zwangsmittel und Sofortvollzug", "Trenne Grundverfügung, Vollziehungsanordnung, Zwangsgeld, Ersatzvornahme, unmittelbaren Zwang und Bußgeld; prüfe Zustellung, Fälligkeit, Androhung, Frist, Bestimmtheit, Verhältnismäßigkeit und jeweils statthaften Rechtsschutz.", output),
            ("Widerspruch, Klage und Akteneinsicht", "Sichere Bescheid, Bekanntgabe, Rechtsbehelfsbelehrung, Akte, Betriebsgeheimnisse, Vorverfahren, Klageart, Frist und Antrag; greife Tatbestand, Prognose, Ermessen und Nebenentscheidungen in getrennten Begründungsblöcken an.", output),
            ("Eilrechtsschutz für den laufenden Betrieb", "Belege Vollzugstermin, Umsatz- und Beschäftigungsfolgen, Dritt- und Gemeinwohlrisiken, Erfolgsaussichten und reversible Zwischenlösung; formuliere einen betrieblich umsetzbaren Antrag mit Hilfsauflagen und Berichtspflichten.", output),
        )
    if plugin_slug == "betaeubungsmittelrecht":
        output = "fachspezifischer Prüfvermerk mit Stoff, Rechtsregime, Menge, Erlaubnis- oder Verschreibungsstatus, Belegen, Rechtsfolge, Einziehung, Rechtsschutz und nächster Handlung"
        return (
            ("Stoffeinordnung nach BtMG, KCanG und MedCanG", "Bestimme Wirkstoff, Zubereitung, THC-Gehalt, Menge, Zweck und Herkunft; prüfe zuerst, ob Cannabis oder Medizinalcannabis aus dem BtMG herausgenommen ist oder ob ein Stoff beziehungsweise eine Zubereitung einer BtMG-Anlage unterfällt.", output),
            ("Nicht geringe Menge und Wirkstoffgutachten", "Sichere Nettogewicht, Wirkstoffgehalt, Probenziehung, Messmethode, Gutachten und Zuordnung zu Einzeltaten; bilde die Wirkstoffmenge rechnerisch und verwende einen Grenzwert nur mit belastbarer aktueller Rechtsprechungsquelle.", output),
            ("Erlaubnispflicht nach Paragraf 3 BtMG", "Prüfe Umgangsart, Stoff, Ausnahme, Antragsteller, Zuverlässigkeit, Sachkunde, Räume, Sicherung, Verantwortlichen, Dokumentation und Nebenbestimmungen; trenne Erlaubnis vom strafrechtlichen Vorsatz über ihr Fehlen.", output),
            ("Anbau, Besitz und Weitergabe nach KCanG", "Ordne Alter, Besitzmenge, Ort, Anbaupflanzen, Weitergabe, Konsumverbotszone und Anbauvereinigung den jeweils geltenden Vorschriften des KCanG zu; trenne erlaubtes Verhalten, Ordnungswidrigkeit und Straftat.", output),
            ("Medizinalcannabis, Verschreibung und Abgabe", "Prüfe ärztliche Verschreibung, medizinischen Zweck, Produkt, Menge, Apothekenabgabe, Importweg, Dokumentation und sozialrechtliche Kostenübernahme; behandle MedCanG, Arzneimittelrecht und Leistungsrecht getrennt.", output),
            ("Betäubungsmittelverschreibung und BtMVV", "Gleiche Patient, verschreibenden Arzt, zugelassenes Mittel, Höchstmenge, Formblatt oder elektronische Vorgabe, Kennzeichnung, Abgabe, Änderung, Aufbewahrung und Dokumentation mit BtMG und BtMVV ab.", output),
            ("Apotheke, Bestand und Nachweisführung", "Rekonstruiere Wareneingang, Bestand, Abgabe, Vernichtung, Verlust, Zugriff, Verantwortlichkeit und Nachweisbuch; gleiche jede Mengenabweichung mit Beleg, Datum, Charge und möglicher Meldepflicht ab.", output),
            ("Einfuhr, Ausfuhr und grenzüberschreitender Verkehr", "Bestimme Stoff, Herkunfts- und Zielland, Transportweg, Erlaubnisse, Ein- oder Ausfuhrgenehmigung, Begleitpapiere, beteiligte Unternehmen und Zollvorgang; stoppe den Vollzug bei ungeklärter Genehmigung.", output),
            ("Grundtatbestand, Qualifikation und Beteiligung", "Prüfe für jede Einzeltat Umgangsform, Stoff und Menge, Vorsatz, Täterschaft oder Teilnahme, Gewerbsmäßigkeit, Bande, Waffe, Minderjährigenbezug und Konkurrenz nach BtMG oder KCanG; pauschale Gesamtmengen genügen nicht.", output),
            ("Durchsuchung, Beschlagnahme und Verwertbarkeit", "Prüfe Tatverdacht, Durchsuchungsziel, Beschluss oder Gefahr im Verzug, Auffindesituation, Sicherstellung, Probenkette, Auswertung digitaler Geräte und Dokumentation nach StPO Paragrafen 94 und folgende sowie 102 und folgende.", output),
            ("Therapie, Zurückstellung und Vollstreckung", "Prüfe Abhängigkeit, Tatbezug, verhängte Strafe, Therapieplatz, Kostenzusage, Zurückstellung nach Paragraf 35 BtMG, Therapieverlauf und Anrechnung nach Paragraf 36 BtMG; erstelle Fristen- und Nachweisplan.", output),
            ("Fahrerlaubnis- und Berufsrechtsschnittstelle", "Trenne Strafverfahren, Ordnungswidrigkeit, Fahrerlaubnisrecht, ärztliche Verordnung, Eignungszweifel, Konsummuster und berufsrechtliche Folgen; übertrage weder Besitzgrenzen noch Strafwertungen automatisch in die Fahreignungsprüfung.", output),
        )
    if plugin_slug == "tabellenreview-3d":
        output = "prüffähige Tabellenarbeitsmappe mit Befund, Originalfundstelle, Auswirkung, Korrektur, Gegenprobe, Freigabestatus und Übergabenachweis"
        return (
            ("Formelherkunft und Abhängigkeitskette", "Verfolge jede entscheidende Ergebniszelle über Formeln, benannte Bereiche, Hilfsblätter, externe Verknüpfungen und Eingabewerte zurück; markiere hart codierte Werte, Zirkelbezüge und nicht erreichbare Quellen.", output),
            ("Import, Export und Formatverlust", "Vergleiche Ausgangsdatei, importierte Arbeitsmappe und Export zeilen- und zellbezogen; prüfe Datentypen, Datumswerte, Dezimaltrennzeichen, Formeln, Filter, ausgeblendete Bereiche und abgeschnittene Texte.", output),
            ("Pivot, Diagramm und Berichtsaussage", "Gleiche Datenquelle, Filter, Aggregation, Zeitraum, Einheit und Beschriftung von Pivot und Diagramm mit den Rohdaten ab; verhindere, dass leere, ausgeblendete oder doppelte Datensätze die Aussage verzerren.", output),
        )
    if plugin_slug == "richter-sozialgericht":
        return (
            ("Aktenaufnahme und Streitgegenstand", "Erfasse Bescheidkette, Verfügungssätze, Beteiligte, Beigeladene, Vorverfahren, Klageantrag, Leistungszeitraum, Verwaltungsakte, medizinische Unterlagen und Eilbedarf; trenne einzelne Streitgegenstände und Teilzeiträume.", "richterliches Eingangsblatt mit Streitgegenständen, Bescheidkette, Fristen, Aktenanforderung, Beiladungsfrage und erster Verfügung"),
            ("Zulässigkeit der Sozialgerichtsklage", "Prüfe Rechtsweg, statthafte Klageart, Klagebefugnis, Vorverfahren, Klagefrist, Beteiligtenfähigkeit, Prozessfähigkeit, richtige Beklagte und bestimmten Antrag nach SGG Paragrafen 51, 54, 70, 78, 87, 90 und 92.", "Zulässigkeitsvotum mit Antrag, Fristenberechnung, Heilungs- oder Hinweisbedarf und Entscheidungsfolge"),
            ("Amtsermittlung und richterliche Hinweise", "Lege entscheidungserhebliche Tatsachen, Ermittlungen des Leistungsträgers, substantiiertes Parteivorbringen und erreichbare Beweismittel offen; steuere Befundanforderung, Aktenbeiziehung, Auskunft, Hinweis und Erörterung nach Paragrafen 103 und 106 SGG.", "Ermittlungsplan mit Beweisthema, Quelle, konkreter Verfügung, Frist, Erledigung und verbleibender Erkenntnislücke"),
            ("Medizinischer Sachverständigenbeweis", "Formuliere funktions- und zeitraumbezogene Beweisfragen, wähle Fachgebiet und Aktenbasis, prüfe Befangenheit, Zusatzgutachten und Antrag nach Paragraf 109 SGG und trenne Diagnose, Funktion, Kausalität und rechtliche Wertung.", "Beweisanordnung mit Gutachterfragen, Befundindex, Vorschussfrage, Beteiligtenanhörung und späterem Würdigungsraster"),
            ("Eilrechtsschutz nach Paragraf 86b SGG", "Bestimme aufschiebende Wirkung oder einstweilige Anordnung, Hauptsachebezug, Anordnungsanspruch, Anordnungsgrund, Glaubhaftmachung, existenzielle Folgen, mögliche Vorwegnahme und vollziehbaren Tenor.", "vollständiger Eilbeschluss mit Antrag, Glaubhaftmachung, Folgenabwägung, Kosten, Zustellung und Anschlussverfügung"),
            ("Existenzsicherung und SGB II", "Prüfe Bedarfsgemeinschaft, gewöhnlichen Aufenthalt, Erwerbsfähigkeit, Einkommen, Vermögen, Unterkunft, Mehrbedarf, Sanktion oder Aufrechnung zeitraumbezogen; rechne streitige Monate und Verfügungssätze getrennt.", "Monats- und Anspruchsmatrix mit Berechnung, Belegen, offenen Tatsachen, Eilbedarf und tenorierbarer Differenz"),
            ("Gesetzliche Krankenversicherung", "Prüfe Versichertenstatus, Leistungstatbestand, ärztliche Verordnung, Nutzen, medizinische Notwendigkeit, Wirtschaftlichkeit, Genehmigungsfiktion nur nach geltendem Recht, MD-Gutachten und mögliche Systemversagens- oder Ausnahmefrage.", "Leistungsvotum mit medizinischer Tatsachenmatrix, Rechtsmaßstab, Gutachtenkritik, Beweisfragen und bestimmtem Sachleistungs- oder Erstattungsziel"),
            ("Gesetzliche Rentenversicherung", "Ordne Versicherungsverlauf, Wartezeit, Pflichtbeiträge, Anrechnungs- und Zurechnungszeiten, Kontenklärung, Leistungsfall, medizinische oder versicherungsrechtliche Voraussetzungen und Berechnung nach Bescheidzeilen.", "Rentenstreitmatrix mit Zeitraum, rentenrechtlicher Zeit, Beleg, Rechenwert, Streitpunkt, Beweisbedarf und Tenoroption"),
            ("Gesetzliche Unfallversicherung", "Prüfe versicherte Tätigkeit, konkrete Verrichtung, Unfallereignis, Gesundheitserstschaden, haftungsbegründende und haftungsausfüllende Kausalität, Folgen und Beweismaß; trenne Anerkennung und Leistungsfolgen.", "Unfall- und Kausalitätsvotum mit Ereignischronologie, Befunden, Zeugen, Gutachterfragen und Entscheidungssatz"),
            ("Schwerbehindertenrecht und Merkzeichen", "Ordne Funktionsbeeinträchtigungen, Einzelbewertungen, Wechselwirkungen, Gesamt-GdB und Merkzeichen den Versorgungsmedizinischen Grundsätzen und konkreten Befunden zu; addiere Einzel-GdB nicht schematisch.", "Funktions- und Bewertungsmatrix mit Befundstelle, Zeitraum, Wechselwirkung, Gutachterfrage und tenorierbarem Feststellungsziel"),
            ("Mündliche Verhandlung und Vergleich", "Bereite Sachbericht, Anträge, Hinweise, Beweisstand, Erörterungsfragen, persönliches Erscheinen, Vergleichsoption und Protokollierung vor; wahre Amtsermittlung und rechtliches Gehör trotz Vergleichsgespräch.", "Terminsmappe mit Streitpunkten, Fragen, Hinweisen, Vergleichskorridor, Protokolltext und Entscheidungsalternativen"),
            ("Urteil, Gerichtsbescheid und Nebenentscheidungen", "Wähle zulässige Entscheidungsform, würdige das Gesamtergebnis nach Paragraf 128 SGG und formuliere Rubrum, Tenor, Tatbestand, Gründe, Kosten nach Paragraf 193 SGG und Rechtsmittelangaben nach Paragraf 136 SGG widerspruchsfrei.", "absetzungsreifer Entscheidungsentwurf mit Beweiswürdigung, Leistungszeitraum, Kosten, Rechtsmittel und Zustellungsverfügung"),
        )
    if plugin_slug == "richter-finanzgericht":
        return (
            ("Aktenaufnahme und angefochtener Verwaltungsakt", "Erfasse Steuerart, Zeitraum, Bescheid, Änderungsbescheid, Einspruchsentscheidung, Bekanntgabe, Anträge, Besteuerungsgrundlagen, Steuerakte und Vollziehungsstand; trenne jeden Verfügungssatz und Verfahrensabschnitt.", "finanzgerichtliches Eingangsblatt mit Bescheidkette, Anträgen, Fristen, Aktenanforderung, Streitwert und erster Verfügung"),
            ("Zulässigkeit nach der FGO", "Prüfe Finanzrechtsweg, Klageart, Klagebefugnis, Vorverfahren, Klagefrist, Beteiligte, Prozessvertretung und bestimmten Antrag nach FGO Paragrafen 33, 40, 44, 47, 57, 62 und 65.", "Zulässigkeitsvotum mit Bekanntgaberechnung, Antrag, Heilungs- oder Hinweisbedarf und prozessualer Folge"),
            ("Aussetzung der Vollziehung", "Prüfe Antrag bei Behörde oder Gericht, Zugangsvoraussetzungen, ernstliche Zweifel, unbillige Härte, Sicherheitsleistung, Teilbeträge und rückwirkende Aufhebung der Vollziehung nach Paragraf 69 FGO.", "vollständiger AdV-Beschluss mit Streitbetrag, summarischer Prüfung, Sicherheitsfrage, Kosten und Anschlussverfügung"),
            ("Amtsermittlung und Mitwirkung", "Bestimme entscheidungserhebliche Tatsachen, Mitwirkungssphäre, Steuerakten, Buchführung, Auskunftspersonen und erreichbare Beweismittel; steuere Sachaufklärung nach Paragraf 76 FGO, ohne Feststellungslast und Mitwirkung zu vermengen.", "richterlicher Ermittlungsplan mit Beweisthema, Aktenfund, Auflage, Beweismittel, Frist und Auswirkung bei Nichterweislichkeit"),
            ("Schätzung und Besteuerungsgrundlagen", "Prüfe Schätzungsbefugnis, Schätzungsmethode, Ausgangsdaten, Unsicherheitszuschläge, inneren und äußeren Betriebsvergleich und Ergebnisrahmen nach Paragraf 162 AO; das Gericht muss eine eigene tragfähige Überzeugung bilden.", "Schätzungsvotum mit Datengrundlage, Rechenweg, Bandbreite, Einwendungen, Gegenprobe und tenorierbarem Betrag"),
            ("Beweisaufnahme und Feststellungslast", "Ordne jede streitige Tatsache dem materiellen Steuertatbestand, Beweismittel und der objektiven Feststellungslast zu; formuliere Beweisbeschluss, Zeugen- oder Sachverständigenfragen und Würdigung nach FGO Paragrafen 81 und folgende sowie 96.", "Beweismatrix und beschlussfähige Beweisanordnung mit Beweisthema, Beweismaß, Kosten und Anschlussentscheidung"),
            ("Änderungsnormen und Verböserungsgrenze", "Prüfe Bestandskraft, Vorbehalt, Vorläufigkeit, Korrekturvorschrift der AO, Änderungsrahmen des Klageverfahrens und Bindung an den angefochtenen Verwaltungsakt; trenne Fehlergrund und zulässige Rechtsfolge.", "Änderungsmatrix mit Bescheidposition, Korrekturgrund, Frist, Betrag, Gegenposition und Entscheidungsgrenze"),
            ("Beteiligte, Beiladung und Steuergeheimnis", "Prüfe notwendige oder einfache Beiladung, Prozessstandschaft, Gesamtrechtsnachfolge, Akteneinsicht, Schutz steuerlicher Daten und Umfang der Beteiligtenrechte nach FGO und AO; dokumentiere jede Offenlegung.", "Beteiligten- und Schutzverfügung mit Rechtsgrund, Umfang, Schwärzung, Zustellung und Rechtsbehelf"),
            ("Mündliche Verhandlung und Erörterung", "Bereite Sachbericht, Anträge, Hinweise, unstreitige Berechnungszeilen, Beweisthemen, Verständigungsmöglichkeiten und Protokoll vor; kläre Verzicht auf mündliche Verhandlung nur ausdrücklich und wirksam.", "Terminsmappe mit Streitpunkten, Rechenblatt, Hinweisen, Fragen, Protokollbausteinen und Entscheidungsalternativen"),
            ("Urteil und Tenor im Steuerstreit", "Formuliere Aufhebung, Änderung, Verpflichtung oder Abweisung betrags- und zeitraumgenau; stimme Tatbestand, Entscheidungsgründe, Berechnungsanlage, Kosten und vorläufige Vollstreckbarkeit mit FGO Paragrafen 95, 100, 105 und 151 ab.", "absetzungsreifes Urteil mit eindeutigem Steuerbetrag, Berechnungsgrundlage, Kosten und Zustellungsverfügung"),
            ("Revision und Nichtzulassungsbeschwerde", "Prüfe Beschwer, Zulassungsgründe, Divergenz, grundsätzliche Bedeutung, Verfahrensmangel, Frist, Form und Vertretungszwang nach FGO Paragrafen 115 und folgende; bezeichne tragende Rechtssätze präzise.", "Rechtsmittelvermerk mit Zulassungsfrage, Fristenblatt, Divergenz- oder Verfahrensrüge und Aktenvorlage"),
            ("Kosten, Streitwert und Vollzug", "Kontrolliere Kostenquote, Hinzuziehung eines Bevollmächtigten im Vorverfahren, Streitwert, Erstattungsfähigkeit, Vollziehung nach Entscheidung und erforderliche Mitteilung an Finanzbehörde oder Vollstreckungsstelle.", "Nebenentscheidungs- und Vollzugsblatt mit Berechnung, Kostentenor, Empfängern, Zustellung und Erledigungskontrolle"),
        )
    if plugin_slug == "richter-amtsgericht-straf":
        return (
            ("Eingang, Zuständigkeit und Verfahrensart", "Prüfe sachliche und örtliche Zuständigkeit, Spruchkörper, Anklage, Strafbefehl, beschleunigtes Verfahren oder Privatklage, Haftstatus, Pflichtverteidigung und anstehende Fristen; ordne die Akte der richtigen richterlichen Spur zu.", "richterliches Eingangsblatt mit Verfahrensart, Zuständigkeit, Haft- und Verteidigungsstatus, Fristen und erster Verfügung"),
            ("Zwischenverfahren und Eröffnungsentscheidung", "Prüfe wirksame Anklage, Angeschuldigtenbezeichnung, Tat im prozessualen Sinn, hinreichenden Tatverdacht, Zuständigkeit, notwendige Beweiserhebung und rechtlichen Hinweis nach StPO Paragrafen 199 und folgende.", "Eröffnungs-, Ablehnungs- oder Ergänzungsentwurf mit Tatabgrenzung, Beweislage, Zustellung und Terminfolge"),
            ("Strafbefehl und Einspruch", "Prüfe Zulässigkeit des Strafbefehls, Rechtsfolgenkompetenz, Aktenlage, Antrag, Tatbezeichnung, Zustellung, Einspruchsfrist, Beschränkung und Übergang zur Hauptverhandlung nach StPO Paragrafen 407 und folgende.", "Strafbefehls- oder Einspruchsvermerk mit Tat, Rechtsfolge, Fristen, Ladung und Entscheidungsoption"),
            ("Hauptverhandlung vorbereiten", "Erstelle Ladungs- und Beweisplan, prüfe persönliches Erscheinen, Verteidigung, Dolmetscher, Nebenklage, Zeugen- und Sachverständigenladung, Selbstleseverfahren, Verständigungsbedarf und Terminsdauer.", "vollständige Terminsverfügung mit Beteiligten, Beweismitteln, Ladungszusätzen, Vorführungsfragen und Reserveplan"),
            ("Beweisaufnahme und Aufklärungspflicht", "Ordne Einlassung, Zeugen, Urkunden, Augenschein, Sachverständige und digitale Beweise den konkreten Tatfragen zu; wahre Aufklärungspflicht, Unmittelbarkeit, Beweisantragsrecht und Verwertungsgrenzen.", "Beweisprogramm mit Tatfrage, Beweismittel, Ladungsgrund, Einwand, möglichem Beschluss und Dokumentationspunkt"),
            ("Zeugenvernehmung und Aussagewürdigung", "Trenne Wahrnehmungsfähigkeit, Entstehung, Konstanz, Detailreichtum, Belastungsmotiv, Widerspruch und externe Bestätigung; behandle Aussage-gegen-Aussage-Konstellationen anhand der konkreten Beweislage und ohne schematische Glaubwürdigkeitsformeln.", "richterlicher Fragenkatalog und Würdigungsgerüst mit Aussagekern, Widersprüchen, Bestätigungen und offenem Beweisergebnis"),
            ("Geständnis, Verständigung und Dokumentation", "Prüfe Freiwilligkeit, Belehrung, Aktenbasis und Glaubhaftigkeit des Geständnisses sowie Voraussetzungen, Inhalt, Transparenz, Protokollierung und Negativmitteilung einer Verständigung nach Paragraf 257c und Paragraf 273 StPO.", "Verständigungsvermerk oder Protokollbaustein mit zulässigem Gegenstand, Belehrungen, Erklärungen und verbleibender Beweisaufnahme"),
            ("Rechtlicher Hinweis und Tatidentität", "Prüfe, ob eine andere rechtliche Bewertung, Qualifikation, Versuch, Teilnahme oder Rechtsfolge in Betracht kommt, wahre die Tatidentität und erteile den erforderlichen Hinweis nach Paragraf 265 StPO rechtzeitig und konkret.", "Hinweisbeschluss mit Tatbezug, möglicher Bewertung, Verteidigungsmöglichkeit, Unterbrechungsfrage und Protokollierung"),
            ("Einstellung und Verfahrensabsprachen", "Prüfe Einstellung nach Paragrafen 153 und folgende StPO, Zustimmungserfordernisse, Auflagen, Abtrennung, Teileinstellung und Kosten; trenne Opportunität von fehlendem Tatnachweis nach Paragraf 170 Absatz 2 StPO.", "Einstellungsentscheidung mit Reichweite, Zustimmung, Auflage, Frist, Kosten, Mitteilungen und Wiederaufnahmefolge"),
            ("Strafzumessung und Nebenfolgen", "Bestimme Strafrahmen, minder schweren Fall, vertypte Milderung, Tat- und Täterumstände, Nachtatverhalten, Vorstrafen, Tagessatzhöhe, Bewährung, Fahrverbot, Entziehung, Einziehung und Kompensation.", "Strafzumessungstabelle mit Strafrahmen, gewichteten Umständen, Rechtsfolgenvorschlag, Bewährungsprognose und Nebenentscheidungen"),
            ("Urteilsberatung, Tenor und Gründe", "Führe Beweisergebnis, Feststellungen, rechtliche Würdigung und Strafzumessung zusammen; formuliere Tenor, angewendete Vorschriften, Kosten und Urteilsgründe nach Paragraf 267 StPO widerspruchsfrei und vollständig.", "absetzungsreifer Urteilsentwurf mit Feststellungen, Beweiswürdigung, Subsumtion, Strafzumessung und Kosten"),
            ("Rechtsmittel, Protokoll und Vollstreckungsanschluss", "Prüfe Verkündung, Rechtsmittelbelehrung, Protokollfertigstellung, Berufung oder Sprungrevision, Rechtsmittelbeschränkung, Fristen, Aktenversand und rechtskraftabhängige Vollstreckungsmitteilungen.", "Abschlussverfügung mit Belehrung, Fristenblatt, Protokollkontrolle, Rechtskraftvermerk und Vollstreckungsnachrichten"),
        )
    if plugin_slug == "prozessrecht":
        return (
            ("Klage, Streitgegenstand und bestimmter Antrag", "Bestimme Rechtsschutzziel, prozessualen Anspruch und Lebenssachverhalt; gleiche Rubrum, Antrag, Haupt- und Hilfsbegehren, Nebenforderungen und Tatsachenvortrag mit Paragrafen 253 und 260 ZPO ab.", "Klagegerüst mit bestimmtem Antrag, Streitgegenstandsvermerk, Tatsachenblöcken, Beweisangeboten, Anlagen und Zustellungsangaben"),
            ("Rechtsweg, Zuständigkeit und Verweisung", "Prüfe Rechtsweg, sachliche, örtliche, internationale und funktionelle Zuständigkeit, Gerichtsstandsvereinbarung, rügelose Einlassung und Verweisung nach GVG Paragrafen 13 und 17a sowie ZPO Paragrafen 12 und folgende.", "Zuständigkeitsvermerk mit tragenden Anknüpfungstatsachen, Gegenposition, Verweisungsoption, Antrag und Kostenfolge"),
            ("Zustellung, Verteidigungsanzeige und Fristen", "Rekonstruiere Zustellungsart, Zustellungsdatum, Heilung, Fristbeginn, Notfrist, richterliche Frist, Verlängerungsantrag, Säumnisfolge und Kalenderkontrolle nach Paragrafen 166 und folgende sowie 276 ZPO.", "taggenaues Fristenblatt mit Zustellungsbelegen, Vorfristen, Verantwortlichem, Sofortmaßnahme und Erledigungsnachweis"),
            ("Schlüssigkeit, Bestreiten und Substantiierung", "Ordne jedes Tatbestandsmerkmal einer konkreten Behauptung zu, prüfe Erklärungslast und zulässiges Bestreiten nach Paragraf 138 ZPO und trenne Schlüssigkeitslücke, Erheblichkeitslücke und erst danach Beweisbedarf.", "Anspruchs- und Vortragstabelle mit Merkmal, Klägerbehauptung, Beklagtenerklärung, Beweislast, Beweismittel und Hinweisbedarf"),
            ("Richterlicher Hinweis und Prozessleitung", "Formuliere einen rechtzeitigen, konkreten und ergebnisoffenen Hinweis nach Paragraf 139 ZPO; bestimme betroffenen Punkt, bisherige Lücke, mögliche Ergänzung, Frist, Gelegenheit zur Stellungnahme und Dokumentation im Protokoll oder in der Verfügung.", "vollständige Hinweisverfügung mit Auflagen, Fristen, Zustellung, Wiedervorlage und nächster richterlicher Entscheidung"),
            ("Beweisprogramm, Urkundenvorlage und Beweiswürdigung", "Isoliere nur streitige und erhebliche Tatsachen, ordne Beweislast und Beweismittel zu und prüfe Urkundenvorlage, Sachverständigenbedarf, Zeugenfragen, Beweismaß sowie Paragrafen 142, 284, 286 und 287 ZPO.", "Beweismatrix und ausformulierter Beweisbeschluss mit Beweisthema, Beweismittel, Vorschuss, Ladung und Anschlussverfügung"),
            ("Arrest und einstweilige Verfügung", "Trenne Arrestanspruch und Arrestgrund von Verfügungsanspruch und Verfügungsgrund; prüfe Glaubhaftmachung, Dringlichkeit, Vorwegnahme, Schutzschrift, Vollziehungsfrist und Sicherheitsleistung nach Paragrafen 916 und folgende sowie 935 und 940 ZPO.", "Eilantrag oder Erwiderung mit bestimmten Anträgen, Glaubhaftmachungsmitteln, Dringlichkeitschronologie und Vollziehungsplan"),
            ("Mahnverfahren und Übergang ins Streitverfahren", "Prüfe Geldforderung, Zulässigkeit des Mahnverfahrens, richtige Parteibezeichnung, Anspruchskennzeichnung, Zinsen, Widerspruch oder Einspruch, Abgabe, Anspruchsbegründung und Fristen nach Paragrafen 688 und folgende ZPO.", "Mahnverfahrensakte mit Antragsdaten, Forderungsrechnung, Fristen, Zustellungsstand und vorbereitetem Übergang in das Streitverfahren"),
            ("Elektronische Einreichung, Ersatzeinreichung und Wiedereinsetzung", "Prüfe Dateiformat, verantwortende Person, einfache Signatur und sicheren Übermittlungsweg nach Paragraf 130a ZPO, Nutzungspflicht und technische Unmöglichkeit nach Paragraf 130d ZPO sowie Wiedereinsetzung nach Paragrafen 233 und folgende ZPO.", "Versand- und Fristrettungspaket mit Schriftsatz, Anlagenindex, Übermittlungsnachweis, Störungsdokumentation und Glaubhaftmachung"),
            ("Erledigung, Klagerücknahme und Kosten", "Rekonstruiere das erledigende Ereignis und seinen Zeitpunkt; vergleiche übereinstimmende oder einseitige Erledigung, Klagerücknahme und Fortsetzung und prüfe Kosten nach Paragrafen 91a und 269 ZPO sowie einen möglichen materiellen Kostenerstattungsanspruch.", "Entscheidungsmatrix mit Antragsfassung, Tatsachenchronologie, Kostenprognose, Gegenposition und empfohlener Prozesserklärung"),
            ("Vergleich, Protokollierung und Vollstreckbarkeit", "Formuliere einen vollstreckbaren Vergleich nach Paragrafen 278 und 794 ZPO mit Leistung, Fälligkeit, Zug um Zug, Kosten, Widerruf, Erledigung, Auskunft, Herausgabe und eindeutiger Reichweite der Abgeltung.", "protokollierungsfähiger Vergleichstext mit Variantenrechnung, Regelung offener Nebenpunkte und Vollstreckbarkeitskontrolle"),
            ("Urteil, Rechtsmittel und vorläufige Vollstreckbarkeit", "Baue Rubrum, Tenor, Tatbestand und Entscheidungsgründe nach Paragraf 313 ZPO auf; kontrolliere Kosten, Vollstreckbarkeit, Streitwert, Beschwer und Berufungszugang nach Paragrafen 511 und folgende sowie 708 und folgende ZPO.", "urteils- oder rechtsmittelfähige Endfassung mit Tenorcheck, Nebenentscheidungen, Beschwerdewert, Fristenblatt und Zustellungsverfügung"),
        )
    if plugin_slug == "relationstechnik-zivilrecht":
        return (
            ("Aktenaufnahme und Prozesslage", "Erfasse Parteien, Anträge, Zustellungen, Schriftsatzfolge, gerichtliche Hinweise, Protokolle, Fristen und bereits erhobene Beweise; trenne sicheren Aktenstand, offene Verfahrensfrage und materiellen Streit.", "Relationsdeckblatt mit Verfahrenschronologie, Anträgen, Fristen, Aktenfundstellen und nächster Verfügung"),
            ("Streitgegenstand und Anspruchsreihenfolge", "Leite aus Antrag und Lebenssachverhalt den Streitgegenstand ab und ordne vertragliche, gesetzliche, dingliche, deliktische und bereicherungsrechtliche Anspruchsgrundlagen in einer entscheidungslogischen Reihenfolge.", "Anspruchslandkarte mit Antrag, Rechtsfolge, Tatbestandsmerkmalen, Konkurrenz und Prüfungsreihenfolge"),
            ("Klägerstation und Schlüssigkeit", "Unterstelle den Klägervortrag als wahr, ordne jedem Tatbestandsmerkmal eine konkrete Behauptung zu und kennzeichne fehlenden Vortrag als Hinweisproblem; Beweisbarkeit bleibt an dieser Station außer Betracht.", "Klägerstationsvotum mit Anspruch, Behauptung, Fundstelle, Schlüssigkeit, Lücke und Hinweisentwurf"),
            ("Beklagtenstation und Erheblichkeit", "Unterstelle den Beklagtenvortrag als wahr und trenne Bestreiten, Einwendung, Einrede, Hilfsaufrechnung und Widerklage; prüfe, welche Verteidigung die schlüssige Klage ganz oder teilweise zu Fall bringt.", "Beklagtenstationsvotum mit Verteidigungsmittel, Tatsachenkern, Erheblichkeit, Beweislast und Rechtsfolge"),
            ("Replik, Duplik und neuer Streitstoff", "Ordne Replik und Duplik nur den jeweils ausgelösten Verteidigungsmitteln zu, prüfe Geständnis, Bestreitensqualität, Verspätung und Klageänderung und halte jede Änderung des Streitstands fundstellengenau fest.", "mehrstufige Streitstandstabelle mit Vortragsebene, Reaktion, verbleibendem Streit und prozessualer Folge"),
            ("Darlegungslast und sekundäre Darlegungslast", "Bestimme die primäre Darlegungs- und Beweislast je Merkmal, prüfe nur bei Informationsgefälle eine sekundäre Darlegungslast und trenne diese strikt von Beweislastumkehr, tatsächlicher Vermutung und Anscheinsbeweis.", "Lastenmatrix mit Merkmal, primär belasteter Partei, Informationszugang, abgestuftem Vortrag und verbleibendem non liquet"),
            ("Beweisstation und Beweisbeschluss", "Nimm nur streitige, erhebliche und beweisbedürftige Tatsachen in das Beweisprogramm auf; formuliere bestimmte Beweisthemen, ordne Beweismittel und Vorschuss zu und verhindere Ausforschung.", "Beweisstationsvotum mit Beweisthema, Beweismittel, Beweislast, Beweismaß und beschlussfähigem Tenor"),
            ("Beweisergebnis und Würdigung", "Würdige jedes erhobene Beweismittel einzeln und in der Gesamtschau nach Paragraf 286 ZPO, behandle Widersprüche und Erinnerungslücken und greife erst bei verbleibendem non liquet auf die Beweislast zurück.", "ausformulierte Beweiswürdigung mit Wahrnehmungsgrundlage, Konsistenz, Gegenindizien und eindeutiger Tatsachenfeststellung"),
            ("Hinweispflicht und rechtliches Gehör", "Prüfe für jede entscheidungstragende Lücke oder abweichende Rechtsansicht einen Hinweis nach Paragraf 139 ZPO, Reaktionsfrist und erneute Verhandlung; vermeide Überraschungsentscheidung und vorweggenommene Beweiswürdigung.", "konkrete Hinweisverfügung mit Streitpunkt, Ergänzungsbedarf, Frist, Zustellung und dokumentierter Gehörskontrolle"),
            ("Vergleichsstation und Prozessökonomie", "Bewerte Obsiegenswahrscheinlichkeit, Beweisrisiko, Kosten, Dauer, Vollstreckbarkeit und Beziehungen der Parteien; entwickle einen Korridor, ohne ungeklärte Rechtsfragen als feststehend auszugeben.", "richterlicher Vergleichsvorschlag mit Rechenweg, beiderseitigem Risiko, Regelungspunkten und Protokolltext"),
            ("Entscheidungsstation und Tenor", "Führe Kläger-, Beklagten- und Beweisstation zur rechtlichen Würdigung zusammen; formuliere Hauptsache, Nebenforderungen, Kosten, vorläufige Vollstreckbarkeit und Streitwert widerspruchsfrei.", "Entscheidungsvotum mit Ergebnisbaum, tragenden Gründen, vollständigem Tenor und Nebenentscheidungen"),
            ("Urteil oder Beschluss als Volltext", "Überführe die Relation in Rubrum, Tenor, Tatbestand oder zulässige Bezugnahmen, Entscheidungsgründe und Rechtsmittelangaben; jede Feststellung muss aus Vortrag, Beweis oder unstreitigem Aktenstand hervorgehen.", "absetzungsreifer Volltext mit Fundstellenkontrolle, Beweiswürdigung, Subsumtion, Kosten und Vollstreckbarkeit"),
        )
    if plugin_slug == "produktrecht":
        return (
            ("Produkt, Wirtschaftsakteur und anwendbares Regelwerk", "Bestimme Produkt, Modell, Charge, Softwarestand, bestimmungsgemäße und vernünftigerweise vorhersehbare Verwendung sowie Hersteller, Importeur, Händler, Fulfilment-Dienstleister und Online-Marktplatz; ordne GPSR, ProdSG und sektorales Harmonisierungsrecht abgrenzend zu.", "Regelwerks- und Rollenmatrix mit Produktabgrenzung, Wirtschaftsakteur, Pflicht, Nachweis, Behörde und Freigabesperre"),
            ("Konformität, CE-Kennzeichnung und technische Unterlagen", "Prüfe, ob harmonisiertes Unionsrecht gilt, welche grundlegenden Anforderungen, Normen, Konformitätsbewertung, EU-Konformitätserklärung, technische Unterlagen, Kennzeichnung und Sprachfassungen erforderlich sind.", "vollständige Konformitätsakte mit Rechtsaktmatrix, Nachweisindex, Lücken, Verantwortlichem und Launch-Entscheidung"),
            ("Risikobeurteilung und Sicherheitskonzept", "Erfasse Gefährdung, Exposition, Eintrittswahrscheinlichkeit und Schadensschwere über alle Nutzergruppen und Fehlanwendungen; gleiche Konstruktion, Schutzmaßnahme, Warnung, Restrisiko und Feldbeobachtung in einer nachvollziehbaren Risikokette ab.", "Risikobeurteilung mit Szenario, Beleg, Risikostufe, Maßnahme, Verifikation, Restrisiko und Freigabestatus"),
            ("Gebrauchsanleitung, Warnhinweis und Sprache", "Prüfe Inhalt, Platzierung, Verständlichkeit, Zielgruppe, Sprache, Piktogramm, Montage, Wartung, Entsorgung und digitale Bereitstellung; ein Warnhinweis darf eine vermeidbare konstruktive Gefahr nicht ersetzen.", "freigabefähige Anleitungsmatrix mit Pflichtinformation, Fundstelle, Änderungsfassung, Übersetzungsbedarf und Versionsnachweis"),
            ("Software, digitale Elemente und Sicherheitsupdates", "Ordne Hardware, eingebettete Software, App, Cloud-Funktion und Updatepfad einem Produktstand zu; prüfe Sicherheitsrelevanz, Änderungsmanagement, Cyberrisiko, Supportzeitraum, Updateinformation und Auswirkungen auf Konformität und Haftung.", "Versions- und Updateakte mit Produktkonfiguration, Risikoänderung, Testnachweis, Nutzerinformation und Rollout- oder Stop-Entscheidung"),
            ("Lieferkette, Rückverfolgbarkeit und Wirtschaftsakteure", "Rekonstruiere Hersteller, Bevollmächtigten, Importeur, Händler, Logistik und Plattform bis zur Charge; kontrolliere Identifikationsangaben, Lieferantennachweise, Prüfpflichten, Aufbewahrung und Weitergabe sicherheitsrelevanter Informationen.", "Rückverfolgbarkeitsmatrix mit Produkt, Charge, Akteur, Pflicht, Beleg, Kontaktweg und Eskalationsfrist"),
            ("Marktbeobachtung, Beschwerden und Signalerkennung", "Bündele Reklamationen, Retouren, Unfälle, Near Misses, Serviceberichte, Plattformmeldungen und ausländische Vorkommnisse; trenne Einzelmangel, Serienmuster und neue Gefahr und dokumentiere Schwellenwert sowie Entscheidung.", "Feldbeobachtungsbericht mit Signalcluster, Produktpopulation, Trend, Risikobewertung, Maßnahme und Managementfreigabe"),
            ("Unfall, Behördenmeldung und Safety Business Gateway", "Sichere Ereignis, Verletzung, Produktidentität, Charge, Softwarestand, Verwendung, Beweise und Sofortmaßnahme; prüfe Meldepflicht, Adressat, Frist, Mindestinhalt, Nachbericht und Abstimmung mit betroffenen Staaten.", "fristfähiges Meldepaket mit Ereignischronologie, Risikobeurteilung, Produktdaten, Maßnahmen, Anlagen und Nachreichungsplan"),
            ("Korrekturmaßnahme, Rücknahme und Rückruf", "Vergleiche technische Korrektur, Update, Verkaufsstopp, Rücknahme und Rückruf nach Gefahrenlage, Reichweite, Identifizierbarkeit, Nutzerkontakt, Wirksamkeit und Behördenabstimmung; plane Rücklauf und Abschlusskontrolle.", "Rückrufplan mit Population, Maßnahme, Kommunikationsfassungen, Kanal, Frist, Wirksamkeitskennzahl und Abschlussbericht"),
            ("Marktüberwachung, Auskunft und Verteidigung", "Zerlege Behördenanfrage, Rechtsgrundlage, Zuständigkeit, verlangte Unterlagen, Frist und mögliche Maßnahme; liefere vollständig, aber ohne unbelegte Schuldeingeständnisse, und halte technische sowie rechtliche Position konsistent.", "Behördenantwort mit Verfahrensstand, Dokumentenindex, Sachverhaltsdarstellung, Rechtsposition, Maßnahmenstand und Vorbehalt"),
            ("Produkthaftung, Kausalität und Regress", "Prüfe Fehler, berechtigte Sicherheitserwartung, Schaden und Kausalität nach geltendem Produkthaftungsrecht; trenne Delikt, Vertrag, Regress und Versicherungsdeckung und markiere den künftigen Anwendungsbereich der Richtlinie (EU) 2024/2853 nach Umsetzungsstand.", "Anspruchs- und Verteidigungsmatrix mit Produktstand, Fehlerhypothese, Beweis, Schaden, Kausalität, Einwand, Regress und Deckungsanzeige"),
            ("Ware mit digitalen Elementen und Gewährleistung", "Prüfe vereinbarte und objektive Anforderungen, Montage, digitale Elemente, Aktualisierungspflicht, Gefahrübergang, Nacherfüllung, Rücktritt, Minderung, Schadensersatz und Beweislast nach BGB Paragrafen 434, 475b, 475c und 477.", "Gewährleistungsvermerk mit Soll-Ist-Vergleich, Updatechronologie, Beweislast, Nacherfüllungsplan und formulierter Kunden- oder Händlerantwort"),
        )
    if plugin_slug == "normenkontrollrat-nkr":
        return (
            ("Auftrag und Prüfkompetenz nach NKRG", "Bestimme Vorhaben, federführendes Ressort, Verfahrensstand und Vorlagepflicht; trenne Prüfung des Erfüllungsaufwands, methodische Beratung und Stellungnahme von politischer Zweckmäßigkeitskontrolle.", "NKR-Prüfvermerk mit Kompetenz, Prüfgegenstand, fehlenden Angaben, methodischem Befund und nächster Ressortanforderung"),
            ("Frühe Beteiligung und prüffähige Vorlage", "Lege fest, wann Ziele, Regelungsalternativen, Vollzugsdaten und Erfüllungsaufwand belastbar vorliegen müssen; verhindere, dass wesentliche Berechnungen erst nach Ressortabstimmung oder Kabinettbefassung nachgeschoben werden.", "Zeit- und Lieferplan mit Datenverantwortlichen, Prüfreife, Ressortterminen, NKR-Beteiligung und Eskalationspunkten"),
            ("Regelungsziel, Erforderlichkeit und Alternativen", "Formuliere messbares Problem und Ziel, prüfe Nichtstun, Vollzugsverbesserung, Information, Selbstregulierung, Förderung und gesetzliche Varianten und begründe, warum die gewählte Alternative erforderlich ist.", "Alternativenmatrix mit Zielbeitrag, Aufwand, Vollzugsfähigkeit, Nebenwirkung, Evidenz und begründeter Auswahl"),
            ("Erfüllungsaufwand methodisch ermitteln", "Zerlege jede Vorgabe in Fallzahl, Häufigkeit, Zeitaufwand, Sachkosten und Lohnsatz; trenne Umstellungs- und laufenden Aufwand, Preiswirkung und sonstige Kosten und dokumentiere Datenquelle sowie Unsicherheit.", "nachrechenbares Standardkostenmodell mit Vorgabe, Normadressat, Fallzahl, Zeit, Tarif, Sachkosten, Quelle und Sensitivität"),
            ("Bürger, Wirtschaft und Verwaltung getrennt bilanzieren", "Ordne jede Informations-, Handlungs-, Duldungs- und Zahlungspflicht der richtigen Normadressatengruppe zu; verhindere Doppelzählungen zwischen Bürgern, Unternehmen, Vollzugsbehörden und Sozialversicherungsträgern.", "dreigeteilte Aufwandsbilanz mit Vorgaben, Einmal- und Jahreswerten, Quellen, Doppelzählungscheck und offenen Daten"),
            ("One in, one out und Entlastungsbilanz", "Prüfe Anwendungsbereich, Belastung, anrechenbare Entlastung, Ausnahme und Buchungszeitpunkt nach geltender Methodik; trenne nationale Regelung von unionsrechtlich zwingender Umsetzung und politische Entlastung von methodischer Buchung.", "Buchungsvermerk mit Belastungsbetrag, Entlastungsmaßnahme, Zeitpunkt, Ausnahmebegründung und Bilanzwirkung"),
            ("Kleine und mittlere Unternehmen sowie EU-Umsetzung", "Prüfe unverhältnismäßige Belastung kleiner Betriebe, Schwellenwerte, Übergangsfristen, Vereinfachungen und Vollzugshilfen; kennzeichne nationale Mehrbelastungen gegenüber zwingendem Unionsrecht gesondert.", "KMU- und Umsetzungscheck mit Betroffenheit, Zusatzaufwand, Gestaltungsoption, Wettbewerbswirkung und Ressortfrage"),
            ("Digitale Vollzugstauglichkeit und Once-only", "Prüfe medienbruchfreien Prozess, bestehende Register, Identifikatoren, Datenfelder, Nachweise, Schnittstellen, Wiederverwendung vorhandener Daten, Barrierefreiheit und Betriebskosten; eine Portalidee ersetzt keinen Ende-zu-Ende-Prozess.", "Vollzugsprozesskarte mit Akteur, Dateneingang, Registerquelle, Entscheidung, Rückkanal, Medienbruch und Verbesserungsauftrag"),
            ("Praxis- und Vollzugscheck", "Spiele die Regelung mit typischen und schwierigen Fällen aus Sicht von Bürger, Unternehmen, Kommune, Fachbehörde und Gericht durch; dokumentiere unklare Tatbestände, fehlende Daten, unrealistische Fristen und personelle Engpässe.", "Praxistestprotokoll mit Fall, Bearbeitungsschritt, Hindernis, Aufwand, Rechtsfolge und konkreter Text- oder Vollzugsänderung"),
            ("Verhältnismäßigkeit und belastungsärmere Gestaltung", "Vergleiche Eignung, Erforderlichkeit und Belastungsintensität der Instrumente; entwickle Schwellenwerte, Ausnahmen, Stufenmodelle, Genehmigungsfiktionen oder Stichproben, ohne das Regelungsziel zu unterlaufen.", "Verhältnismäßigkeitsmatrix mit Ziel, Eingriff, Alternative, Restbelastung, Missbrauchsrisiko und Formulierungsvorschlag"),
            ("Evaluierung, Befristung und Datenplan", "Definiere Zielindikatoren, Ausgangswert, Datenhalter, Erhebungsrhythmus, Evaluierungszeitpunkt und Entscheidungskriterien; verbinde Befristung oder Sunset-Klausel mit rechtzeitigem Bericht und Fortgeltungsentscheidung.", "Evaluierungsplan mit Kennzahl, Baseline, Quelle, Verantwortlichem, Termin, Schwelle und möglicher Rechtsfolge"),
            ("Stellungnahme und Antwort des Ressorts", "Verdichte methodische Mängel, wesentliche Aufwandsrisiken, Alternativen und Vollzugsfragen in priorisierte Feststellungen; trenne ausgeräumte, teilweise geklärte und offene Punkte und beantworte Gegenargumente nachvollziehbar.", "veröffentlichungsfähige NKR-Stellungnahme mit Kurzvotum, nummerierten Befunden, Ressortantwort, Restpunkten und Anlagenindex"),
        )
    if plugin_slug == "strafanzeige-vorbereiter":
        return (
            ("Strafanzeige, Strafantrag und Verfolgungswille", "Trenne Mitteilung eines Sachverhalts nach Paragraf 158 StPO vom erforderlichen Strafantrag nach StGB Paragrafen 77 und folgende; sichere Berechtigten, eindeutigen Verfolgungswillen, Kenntniszeitpunkt, Dreimonatsfrist des Paragraf 77b StGB und formgerechte Einreichung.", "einreichungsfertige Anzeige mit gesondertem Strafantrag, Fristenblatt, Vollmacht, Empfangsbestätigung und Anlagenregister"),
            ("Anfangsverdacht und nüchterner Sachverhalt", "Formuliere nur konkrete Tatsachen, trenne eigene Wahrnehmung, Drittmitteilung und Schlussfolgerung und ordne jedem möglichen Tatbestandsmerkmal einen Beleg zu; die Schwelle des Paragraf 152 Absatz 2 StPO ersetzt keinen Tatnachweis.", "chronologische Sachverhaltsdarstellung mit Tatkomplexen, Beteiligten, Belegfundstellen, offenen Punkten und vorsichtigem Prüfvorbehalt"),
            ("Digitale Beweise, Chats und Sicherungskette", "Sichere Originalgerät, Exportformat, vollständigen Gesprächskontext, Absenderdaten, Zeitstempel, Metadaten, Hashwert und Übergaben; kennzeichne Screenshots ohne Kontext und vermeide Veränderungen am Originalbestand.", "Beweismittelverzeichnis mit Originalfundort, Exportweg, Hashwert, Zeuge, Relevanz, Lücke und geordneter Anlagenbezeichnung"),
            ("Betrug und Vermögensschaden", "Prüfe Täuschung, Irrtum, Vermögensverfügung, konkreten Schaden, Kausalität, Vorsatz und Bereicherungsabsicht nach Paragraf 263 StGB; trenne bloße Vertragsverletzung, schlechte Leistung und Zahlungsunfähigkeit vom nachweisbaren Eingehungsbetrug.", "Tatbestandsmatrix mit Kommunikationsbelegen, Zahlungsfluss, Schadensrechnung, Alternativerklärung und Ermittlungsansätzen"),
            ("Computerbetrug, Phishing und Datenzugriff", "Ordne Manipulation eines Datenverarbeitungsvorgangs, unbefugte Datennutzung, Ausspähen oder Abfangen von Daten und anschließende Vermögensverschiebung nach Paragrafen 202a und folgende sowie 263a StGB; sichere Konten, Header und Logdaten.", "technisch nachvollziehbare Anzeige mit Ereigniszeitleiste, Konten- und Gerätebezug, Loganforderungen, Sicherungsersuchen und Schadensübersicht"),
            ("Körperverletzung und Strafantrag", "Prüfe körperliche Misshandlung, Gesundheitsschädigung, Vorsatz, Rechtfertigung und mögliche Qualifikation nach Paragrafen 223 und 224 StGB; beachte, dass Paragraf 223 nach Paragraf 230 StGB grundsätzlich einen Strafantrag oder besonderes öffentliches Interesse verlangt.", "Anzeige- und Strafantragsentwurf mit Verletzungsbild, Behandlungsunterlagen, Zeugen, Fotos, Kausalitätsangaben und Antragfrist"),
            ("Bedrohung, Nötigung und Nachstellung", "Trenne angekündigte Straftat nach Paragraf 241 StGB, Gewalt oder empfindliches Übel nach Paragraf 240 StGB und wiederholte Nachstellung nach Paragraf 238 StGB; zitiere Wortlaut, Kontext, Häufigkeit, Reaktion und konkrete Auswirkungen.", "Tatkomplextabelle mit Einzelereignis, Wortlaut, Kanal, Zeuge, Beleg, Gefahrenlage und beantragter Schutz- oder Ermittlungsmaßnahme"),
            ("Beleidigung, üble Nachrede und Verleumdung", "Ordne Äußerung, Adressat, Empfängerkreis, Tatsachen- oder Werturteilscharakter, Wahrheitsbeweis, Vorsatz und Verbreitungsweg nach Paragrafen 185 bis 187 StGB; sichere den regelmäßig nötigen Strafantrag und die genaue Äußerung.", "äußerungsgenaue Anzeige mit Kontext, Reichweite, Screenshot- oder Zeugenbeleg, Strafantrag und Abgrenzung zulässiger Kritik"),
            ("Häusliche Gewalt, Akutgefahr und Opferschutz", "Priorisiere Sicherheit, medizinische Versorgung und polizeilichen Notruf; dokumentiere Einzelereignisse, Verletzungen, Drohungen, Kinder, Waffen, Wohnsituation und Schutzbedarf und trenne Strafanzeige von Maßnahmen nach dem Gewaltschutzgesetz.", "sofort nutzbares Schutzpaket mit Anzeige, Strafantrag, Ereignischronologie, Belegen, Kontaktverbotssachverhalt und sicherem Kommunikationsweg"),
            ("Unternehmensdelikte, Korruption und Insolvenzstraftaten", "Bestimme Organ- und Mitarbeiterrollen, Pflichtenkreis, Vermögensnachteil, Vorteil, Unrechtsvereinbarung, Krise und Buchführungsstand; prüfe Paragrafen 266, 299, 331 und folgende sowie 283 StGB und Paragraf 15a InsO nur anhand konkreter Geschäftsvorgänge.", "Ermittlungsdossier mit Verantwortungsmatrix, Zahlungs- und Kommunikationsspuren, Krisenstichtagen, entlastenden Umständen und gezielten Sicherungsanregungen"),
            ("Verletztenrechte, Akteneinsicht und Nebenklage", "Prüfe Verletzteneigenschaft, Akteneinsicht nach Paragraf 406e StPO, Nebenklagebefugnis nach Paragraf 395 StPO, Beistand nach Paragraf 397a StPO, Schutzbedarf und Adhäsionsmöglichkeit; begründe jedes berechtigte Interesse konkret.", "Verletztenrechtsvermerk mit Anträgen, Vollmacht, Schutzbedarf, Akteneinsichtsbegründung, Nebenklageoption und Fristen"),
            ("Einstellung, Beschwerde und Klageerzwingung", "Ordne Abschlussverfügung nach Paragraf 170 StPO, Opportunitätseinstellung nach Paragrafen 153 und folgende StPO, Gegenvorstellung oder Beschwerde und das Klageerzwingungsverfahren nach Paragraf 172 StPO; prüfe Verletztenstellung, Vorschaltbeschwerde, Monatsfrist und Darstellungsanforderungen.", "Reaktionsplan mit Zustellungsdatum, statthaftem Rechtsbehelf, vollständiger Sachverhaltsdarstellung, Beweismitteln, Antrag und Fristenkontrolle"),
        )
    if plugin_slug == "us-bankruptcy-code":
        return (
            ("Chapter, Rolle und Docket-Triage", "Bestimme debtor, creditor, committee, trustee, equity holder oder contract counterparty, zuständiges Gericht, Chapter, Petition Date, Docket-Stand, local rules, anstehende hearings und die nächste nicht verlängerbare Frist.", "US-Counsel-Briefing mit Rollenbild, Docket-Auszug, Fristen, Sofortfragen, deutschen Schnittstellen und nächster filing- oder hearing-Entscheidung"),
            ("Automatic Stay und Relief from Stay", "Prüfe, ob die konkrete Handlung gegen den debtor, estate property oder einen Dritten gerichtet ist, welche Wirkung Section 362 auslöst, ob eine Ausnahme greift und ob stay relief, comfort order oder sofortiger Vollzugsstopp nötig ist.", "Stay-Vermerk mit Handlung, betroffener Normvariante, Ausnahme, Sanktionsrisiko, Belegen und vorgeschlagener motion oder objection"),
            ("Proof of Claim, Bar Date und Claim Objection", "Rekonstruiere Forderungsgrund, Betrag, Währung, Fälligkeit, Sicherheit, Priorität, contingent-, unliquidated- oder disputed-Status, Belege, Schedule-Eintrag und Bar Date nach Sections 501 und 502.", "einreichungsfähiges Claim-Paket mit Berechnung, Belegindex, Sicherheit, Priorität, Reservation of Rights und Fristenblatt"),
            ("Estate Property, Turnover und Secured Status", "Prüfe Massezugehörigkeit nach Section 541, Besitz, Eigentum, Treuhand, Aufrechnung, Sicherungsrecht, perfection, valuation und möglichen turnover nach Section 542; trenne deutsche dingliche Positionen von US-Wirkungen.", "Asset- und Sicherheitenmatrix mit Rechtsinhaber, Besitz, Wert, lien, Rang, Zugriffshindernis, Beweis und Abstimmungsfrage an US-Counsel"),
            ("Cash Collateral, DIP-Finanzierung und Adequate Protection", "Bestimme collateral base, cash collateral, Wertverzehr, Budget, carve-out, replacement liens, superpriority, priming und Gläubigerzustimmung nach Sections 361, 363 und 364; gleiche motion, declaration und proposed order zeilenweise ab.", "Finanzierungs- und Einwendungsmatrix mit Liquiditätsbedarf, Sicherheitenverschiebung, Schutzpaket, Meilensteinen, Default-Folgen und hearing points"),
            ("Section-363-Verkauf und Credit Bid", "Prüfe estate property, sale process, notice, bidding procedures, stalking horse, break-up fee, free-and-clear-Grund, adequate protection, credit bid nach Section 363(k), good faith und benötigte findings.", "Sale- oder Bid-Checkliste mit Verfahrenskalender, Bieteranforderungen, Einwendungen, Kaufpreisvergleich, proposed-order-Punkten und Vollzugssperren"),
            ("Executory Contracts, Leases und IP-Lizenzen", "Bestimme executory contract oder unexpired lease, Cure, Defaults, adequate assurance, assumption, assignment oder rejection nach Section 365; prüfe bei IP-Lizenzen die Schutzentscheidung nach Section 365(n) und die deutschen Vertragsfolgen getrennt.", "Vertragsmatrix mit Status, Cure-Betrag, Entscheidungstermin, Gegenparteioption, Belegen, US-Antrag und deutscher Anschlussmaßnahme"),
            ("Preferences, Fraudulent Transfers und Defenses", "Rekonstruiere transfer, debtor interest, creditor, antecedent debt, Lookback, Insolvenzvermutung, Mehrerhalt und Verteidigung nach Sections 547 und 548; sichere ordinary course, new value, contemporaneous exchange und Solvenzunterlagen.", "Anfechtungs- oder Verteidigungsakte mit Transferzeile, Tatbestandsmerkmal, Beleg, Einwand, Schadensbetrag, Discovery-Bedarf und Vergleichskorridor"),
            ("Disclosure, Classification, Voting und Confirmation", "Gleiche disclosure statement, Klassenbildung, impairment, solicitation, ballot, acceptance, best interests, feasibility, good faith und Voraussetzungen des Section 1129(b) cramdown ab; rechne Abstimmung und Verteilung nachvollziehbar.", "Planbestätigungsmatrix mit Klasse, Anspruch, Behandlung, Stimmrecht, Abstimmung, Einwand, Wertannahme und confirmation finding"),
            ("Third-Party Releases und Planbegrenzungen", "Prüfe Opt-in oder Einwilligung, betroffene Nichtschuldner, freigestellte Ansprüche, Gegenleistung, Zuständigkeit und Planerforderlichkeit; berücksichtige Harrington v. Purdue Pharma für nicht einvernehmliche Freistellungen außerhalb des Schuldnerverhältnisses.", "Release-Vermerk mit Anspruchsinhaber, Einwilligung, Reichweite, Rechtsgrund, Gegenposition, Planfolge und alternativer Vergleichsstruktur"),
            ("Chapter 7, Chapter 13 und Subchapter V", "Bestimme Zugangsvoraussetzungen, trustee- oder debtor-in-possession-Rolle, Einkommen oder Geschäftsbetrieb, Vermögensverwertung, Planpflicht, discharge, objection und Konversionsoption; vermische Verbraucher-, Kleinunternehmer- und Großrestrukturierungsregeln nicht.", "Chapter-Vergleich mit Eligibility, Verfahrensorganen, Fristen, Vermögenswirkung, Plan- oder Verteilungsweg und Entscheidungsempfehlung"),
            ("Chapter 15 und deutsch-amerikanische Koordination", "Prüfe foreign proceeding, foreign representative, center of main interests, recognition als main oder nonmain proceeding, automatische und zusätzliche relief, cooperation, creditor protection und public-policy-Grenze nach Sections 1501 und folgende.", "Anerkennungs- und Koordinationsmemo mit Urkunden, COMI-Indizien, beantragter relief, deutschen Parallelmaßnahmen, Gläubigerschutz und US-Counsel-Fragen"),
        )
    if plugin_slug == "richter-verwaltungsgericht":
        return (
            ("Verpflichtungsklage und Bescheidung", "Prüfe Anspruchsgrundlage, Antragstellung, Spruchreife, gebundene Entscheidung oder Ermessen, maßgeblichen Zeitpunkt und Tenor nach Paragraf 113 Absatz 5 VwGO.", "entscheidungsreifer Vornahme- oder Bescheidungstenor mit tragenden Gründen, Beweislage und Nebenentscheidungen"),
            ("Eilrechtsschutz nach Paragraf 80 Absatz 5 VwGO", "Bestimme aufschiebende Wirkung, Vollziehungsanordnung, statthaften Antrag, formelle Vollziehungsbegründung, Erfolgsaussichten, Interessenabwägung und Vollzugsfolgen.", "vollständiger Eilbeschluss mit Tenor, Streitwert, Kosten, Abwägung und Anschlussverfügung"),
            ("Einstweilige Anordnung nach Paragraf 123 VwGO", "Trenne Sicherungs- und Regelungsanordnung, Anordnungsanspruch, Anordnungsgrund, Glaubhaftmachung, Vorwegnahme der Hauptsache und vollstreckbaren Antrag.", "vollständiger Beschlussentwurf mit Haupt- und Hilfsantrag, Glaubhaftmachungsmatrix, Kosten und Streitwert"),
            ("Beweisaufnahme und Aufklärungspflicht", "Lege Beweisthema, vorhandene Akte, Beweismittel, Beweismaß und verbleibenden Aufklärungsbedarf fest; formuliere Beiziehungs-, Aufklärungs- oder Beweisbeschluss nach Paragraf 86 VwGO.", "richterlicher Aufklärungsplan mit konkreten Verfügungen, Beweisbeschluss und dokumentierter Erledigung jeder Beweisfrage"),
            ("Urteil, Kosten und Vollstreckbarkeit", "Baue Rubrum, Tenor, Tatbestand, Entscheidungsgründe, Kosten, vorläufige Vollstreckbarkeit und Rechtsmittelzulassung nach Paragrafen 117 und 167 VwGO vollständig und widerspruchsfrei auf.", "versandfertiger Urteilsentwurf mit Haupt- und Nebenentscheidungen sowie passender Rechtsmittelbelehrung"),
            ("Berufung, Beschwerde und Revision", "Prüfe Statthaftigkeit, Zulassung, Beschwer, Frist, Form, Vertretungszwang und Darlegungsanforderungen der Paragrafen 124 und folgende VwGO.", "Rechtsmittelvermerk mit Zulassungsfrage, Fristenblatt, Rechtsbehelfsbelehrung und Vorlageverfügung"),
        )
    if plugin_slug == "dsa-dma-digitalregulierung":
        output = "prüffähige Regulierungsakte mit Rollenklassifikation, Artikelmatrix, Systembelegen, Grundrechts- und Verhältnismäßigkeitskontrolle, Verantwortlichem, Frist und Behördenprodukt"
        return (
            ("Dienste- und Rollenpyramide des DSA", "Klassifiziere Vermittlungsdienst, reine Durchleitung, Caching, Hosting, Online-Plattform, Online-Suchmaschine, VLOP oder VLOSE und ordne jeder Stufe nur die tatsächlich anwendbaren Pflichten, Ausnahmen und Behördenzuständigkeiten zu.", output),
            ("Meldung und Abhilfe nach Artikel 16 DSA", "Prüfe Meldekanal, hinreichend genaue und begründete Meldung, Kenntniswirkung, zügige Entscheidung, Mitteilung an den Meldenden und Dokumentation; trenne Notice-and-Action von gerichtlicher oder behördlicher Anordnung.", output),
            ("Begründung einer Beschränkung nach Artikel 17 DSA", "Erstelle eine konkrete Begründung mit betroffener Information, Maßnahme, Tatsachen- und Rechtsgrund, Automatisierungseinsatz und Rechtsbehelf; gleiche die Übermittlung an die Transparenzdatenbank nach Artikel 24 Absatz 5 DSA ab.", output),
            ("Internes Beschwerdesystem nach Artikel 20 DSA", "Prüfe Zugang, Sechsmonatsfrist, fachkundige und nicht rein automatisierte Entscheidung, Ergebnisbegründung und Anschluss an außergerichtliche Streitbeilegung oder gerichtlichen Rechtsschutz.", output),
            ("Außergerichtliche Streitbeilegung nach Artikel 21 DSA", "Ordne zertifizierte Streitbeilegungsstelle, Antragsgegenstand, Zulässigkeit, Gebühren, Mitwirkung nach Treu und Glauben, nicht bindende Entscheidung, Kostentragung und verbleibenden Gerichtsweg.", output),
            ("Trusted Flagger nach Artikel 22 DSA", "Prüfe Status, ausgewiesenes Fachgebiet, priorisierte Bearbeitung, Missbrauchskontrolle, Berichtspflichten und mögliche Aussetzung oder Aberkennung; dokumentiere, warum die konkrete Meldung priorisiert wurde.", output),
            ("Dark Patterns und Werbung nach Artikeln 25 und 26 DSA", "Prüfe Entscheidungsarchitektur, Wiederholung, Hervorhebung, Abbruchhürden, Kennzeichnung der Werbung, Auftraggeber und Parameter; trenne den DSA-Maßstab von Verbraucher-, Wettbewerbs- und Datenschutzrecht.", output),
            ("Empfehlungssysteme nach Artikeln 27 und 38 DSA", "Dokumentiere Hauptparameter und Einflussmöglichkeiten des Nutzers; prüfe für VLOP oder VLOSE eine leicht zugängliche, nicht profilbasierte Option und gleiche Oberfläche, Erklärung und technische Konfiguration ab.", output),
            ("Schutz Minderjähriger nach Artikel 28 DSA", "Prüfe Zugänglichkeit für Minderjährige, altersgerechte Gestaltung, hohes Maß an Privatsphäre, Werbeprofilingverbot und belastbare Alters- und Risikoeinschätzung ohne unnötige zusätzliche Datenerhebung.", output),
            ("Systemische Risiken und Abhilfe nach Artikeln 34 und 35 DSA", "Baue die jährliche und anlassbezogene Risikobewertung aus Systemdesign, Moderation, Empfehlung, Werbung, Grundrechten und Datenbelegen; ordne jedem Risiko eine geeignete, verhältnismäßige und messbare Abhilfemaßnahme zu.", output),
            ("Krisenreaktion und unabhängige Prüfung nach Artikeln 36 und 37 DSA", "Prüfe förmliche Krisenaktivierung, betroffenen Dienst, Eignung, Erforderlichkeit, Verhältnismäßigkeit, Befristung und Bericht; bereite daneben Prüfgegenstand, Kriterien, Datenzugang, Prüfungsurteil und Umsetzungsbericht vor.", output),
            ("Gatekeeper-Pflichten und Verfahren nach DMA", "Prüfe zentralen Plattformdienst, Benennungsvoraussetzungen und Schwellenwerte; ordne Pflichten aus Artikeln 5 bis 7 DMA, technische Umsetzung, Nachweise, Umgehungsrisiko, Bericht und Verfahren der Kommission getrennt.", output),
        )
    if plugin_slug == "status-navigator-step-plan":
        output = "aktualisierbarer Akten-Tracker mit Originalfundstelle, gesichertem Befund, offener Frage, Priorität, Verantwortlichem, Termin, Abhängigkeit und Erledigungsnachweis"
        return (
            ("Dokumenteninventur und Dateitypen", "Erfasse jede Datei mit Originalname, Dokumenttyp, Datum, Beteiligten, Version, Lesbarkeit, Unterschrift und Fundort; trenne Duplikat, Vorfassung, Anlage und leere oder beschädigte Datei.", output),
            ("Versionen und Diskrepanzen", "Vergleiche Namen, Daten, Beträge, Quoten, Laufzeiten, Aktenzeichen und Vertragsverweise über alle Dokumente; führe jede Abweichung mit beiden Fundstellen, Bedeutung, Klärungsweg und Verantwortlichem.", output),
            ("Unterschrift und Vertretungsmacht", "Prüfe für jede Urkunde Unterzeichner, Vertretungsregel, Vollmacht oder Registerstand, Signaturart, Datum, Vollständigkeit und Gegenzeichnung und markiere den konkreten Wirksamkeits- oder Beweisbedarf.", output),
            ("Zugang und Zustellung", "Ordne jede empfangsbedürftige Erklärung nach Absender, Empfänger, Übermittlungsweg, Empfangsmöglichkeit, Zugangsnachweis, Bestreiten und daraus ausgelöster Frist; trenne sicheren Befund und offene Beweisfrage.", output),
            ("Fristen- und Terminsteuerung", "Leite jede Frist aus Dokument, Ereignis und Rechtsgrund ab; dokumentiere Beginn, Ende, Vorfrist, Zeitzone, Zustellungsbeleg, Verantwortlichen, Vertretung, Sofortmaßnahme und Erledigungsnachweis.", output),
            ("Vertrags- und Verpflichtungslandkarte", "Führe Parteien, Gegenstand, Laufzeit, Kündigung, Vergütung, Sicherheiten, Zustimmungen, Abhängigkeiten, Änderungen, Unterschriftsstand und Fundstelle je Vertrag und leite daraus die Bearbeitungsreihenfolge ab.", output),
            ("Beteiligungs- und Finanzierungsstände", "Gleiche Beteiligungsstände, Kapitalmaßnahmen, Wandlungen, Optionen, Finanzierungsinstrumente, Sicherheiten und Rangabreden stichtagsbezogen mit den jeweiligen Urkunden und Registern ab.", output),
            ("Fehlende Unterlagen beschaffen", "Formuliere aus jeder materiellen Lücke eine Aufgabe mit Dokument, Zweck, möglichem Inhaber, Anfrageweg, Frist, Ersatzbeleg, Verantwortlichem und Folge bei Nichterhalt.", output),
            ("Priorität und Statusampel", "Verdichte jeden Befund in belegte Tatsache, offene Frage, Risiko, Entscheidung, Aufgabe und nächsten Termin; eine Farbe ohne Fundstelle und Handlungsauftrag genügt nicht.", output),
            ("Verantwortung und Eskalation", "Ordne jeder Aufgabe Bearbeiter, Freigeber, Stellvertretung, Fälligkeit, Abhängigkeit, Eskalationsdatum, Kommunikationsweg und Abschlussbeleg zu.", output),
            ("Fundstellen und stabile Verknüpfungen", "Verknüpfe jede Trackerzeile mit stabiler lokaler Fundstelle oder DMS-Ziel, prüfe Zugriffsrecht und Dateibestand und kennzeichne fehlende Unterlagen als Beschaffungsbedarf statt mit einem scheinbaren Link.", output),
            ("Übergabe und laufende Aktualisierung", "Erstelle eine Übergabenotiz mit Mandatsziel, Aktenstand, kritischen Fristen, offenen Entscheidungen, wichtigsten Fundstellen, Ansprechpartnern, nächsten fünf Handlungen und eindeutigem Bearbeitungsbesitz; führe danach ein Änderungsprotokoll.", output),
        )
    if plugin_slug == "roemisches-recht":
        return (
            ("Quellenstufe und Textzeuge bestimmen", "Bestimme, ob Zwölftafelüberlieferung, Juristenfragment, Gaius, Institutionen, Digesten, Codex, Novelle, Inschrift oder Papyri vorliegen; sichere Buch, Titel, Fragment, Ausgabe, Sprache, Übersetzung, Datierung und möglichen Interpolationsverdacht, bevor eine Rechtsregel formuliert wird.", "Quellenkarte mit Werk, Stelle, Textstufe, Edition, lateinischem Text, Übersetzung, Datierung, Überlieferungsstatus und begrenzter Aussage"),
            ("Falllösung aus actio und exceptio", "Beginne mit möglicher actio, passiv legitimierter Person, intentio, condemnatio und Einrede; rekonstruiere dann Tatbestand, Beweis, Prozessform und Rechtsfolge für Legisaktionen-, Formular- oder Kognitionsverfahren, ohne die Verfahrensstufen zu vermischen.", "Aktionenblatt mit Parteirollen, actio, Formelbestandteilen, exceptio, Beweisfrage, Prozessstufe und möglicher condemnatio"),
            ("Status, Hausgewalt und Familienvermögen", "Ordne status libertatis, civitatis und familiae, patria potestas, manus, peculium, tutela und cura der belegten Epoche zu; trenne Rechtsfähigkeit, Gewaltverhältnis, Vermögenszuordnung und prozessuale Handlungsfähigkeit und benenne menschenrechtlich problematische Institutionen ohne Beschönigung.", "Status- und Hausverbandsmatrix mit Person, Epoche, Gewaltverhältnis, Vermögenszuordnung, Handlungsfähigkeit, Quelle und historischer Begrenzung"),
            ("Besitz, Eigentum und Ersitzung", "Trenne possessio, detentio, dominium ex iure Quiritium, bonitarisches Eigentum und prätorischen Schutz; prüfe traditio oder mancipatio, iusta causa, bona fides, res habilis, tempus sowie rei vindicatio, actio Publiciana und Interdikte epochengerecht.", "Sachenrechtsvotum mit Besitzlage, Erwerbsakt, causa, Eigentumsstufe, Ersitzungsvoraussetzungen und passendem dinglichen oder prätorischen Schutz"),
            ("Vertragstypen und bona fides", "Qualifiziere das Geschäft als Stipulation, mutuum, commodatum, depositum, pignus, emptio venditio, locatio conductio, societas oder mandatum; leite Klage, Leistungsmaßstab, bona fides, Gefahr, Haftung und Nebenpflicht aus dem historischen Typ statt aus einem modernen Generaltatbestand ab.", "Vertragstypenmatrix mit Geschäftsform, Entstehung, Leistung, Haftungsmaßstab, Gefahr, bona-fides-Bezug, actio und Einrede"),
            ("Kauf, Gefahr, Eviktion und Sachmangel", "Rekonstruiere Konsens, merx, pretium, Gefahrübergang, custodia, Eviktion und ädilizische Rechtsbehelfe mit ihrer zeitlichen Schichtung; stelle actio empti, actio redhibitoria und actio quanti minoris nur für die belegte Konstellation und Epoche gegenüber.", "Kaufrechtliche Exegese mit merx, pretium, Gefahrzeitpunkt, Eviktion, Mangel, Klagenkonkurrenz, Rechtsfolge und Quellenstufe"),
            ("Delikt und Schadenszurechnung", "Ordne furtum, rapina, damnum iniuria datum und iniuria nach Tatbestand, Klage, Pönalität, Tätermehrheit, Noxalhaftung und Vererblichkeit; prüfe bei der lex Aquilia Sache, Handlung, iniuria, Kausalität und Bewertungszeitraum statt Paragraf 823 BGB rückzuprojizieren.", "Deliktsmatrix mit Deliktstyp, actio, Pönalität, iniuria, Kausalität, Bewertungszeitraum, Tätermehrheit und Noxalfolge"),
            ("Condictiones und Geschäftsführung", "Bestimme Leistungs- oder Eingriffslage, causa, einschlägige condictio, actio negotiorum gestorum oder Versionsklage; trenne klassische Einzelklagen, justinianische Systematisierung und moderne Bereicherungs- oder Geschäftsführungsvergleiche sichtbar voneinander.", "Condictiones- und Geschäftsführungssynopse mit Vermögensbewegung, causa, Einzelklage, Epoche, Einrede und Grenze des modernen Vergleichs"),
            ("Pfand, Hypothek und Bürgschaft", "Trenne fiducia, pignus, hypotheca, sponsio, fidepromissio und fideiussio; prüfe Akzessorietät, Besitz, Rang, Verwertung, beneficium divisionis, beneficium excussionis und Regress nach ihrer jeweiligen historischen Einführung.", "Sicherheitenkarte mit Sicherungstyp, Entstehung, Besitz, Akzessorietät, Rang, Verwertung, Einrede, Regress und zeitlicher Schichtung"),
            ("Erbfolge, Testament und prätorische Korrektur", "Ordne testamentum, heredis institutio, Substitution, Legat, Fideikommiss, Intestaterbfolge, bonorum possessio und Pflichtteilsmechanismen nach Epoche; trenne zivile hereditas, prätorische Einweisung und justinianische Vereinheitlichung.", "Erbfolgetafel mit Berufungsgrund, heredis institutio, ziviler und prätorischer Position, Legat oder Fideikommiss, Klage und Epochenstand"),
            ("Rezeption und ius commune", "Verfolge die konkrete Regel von Corpus iuris, Glosse und Kommentatoren über Reichskammergericht, usus modernus und Pandektistik; belege jeden Rezeptionsschritt und kennzeichne, ob das BGB fortführt, verändert oder bewusst bricht.", "belegte Rezeptionslinie mit antiker Stelle, Glosse, Kommentatorenposition, usus modernus, Pandektistik, BGB-Anschluss und methodischer Bruchstelle"),
            ("Romanistisches Abschlussgutachten", "Löse den Sachverhalt in der gewählten Epoche mit Parteien, Status, Gegenstand, actio, Einrede, Beweis, Rechtsfolge und Quellenbelegen; gib gesicherte, wahrscheinliche und spekulative Rekonstruktion getrennt aus und füge einen Gegenwartsvergleich erst danach an.", "vollständiges römischrechtliches Fallgutachten mit Epochenannahme, Quellenapparat, Status, actio, exceptio, Beweis, Rechtsfolge, Gegenrekonstruktion und getrenntem Gegenwartsvergleich"),
        )
    if plugin_slug == "preussisches-allgemeines-landrecht-pralr":
        return (
            ("Ausgabe, Druck und Textzeuge sichern", "Bestimme 1792er Entwurf oder Gesetzbuch von 1794, Band, Teil, Titel, Paragraf, Druck, Scan und Seitenbild; vergleiche OCR mit dem Faksimile, bewahre historische Orthografie im Zitat und dokumentiere jede stillschweigende Modernisierung.", "Textzeugenprotokoll mit Ausgabe, Druck, Band, Seitenbild, OCR-Abweichung, historischer Orthografie, eigener Normalisierung und zitierfähiger Fundstelle"),
            ("Geltungsraum und Rechtsquellenhierarchie", "Kläre Stichtag, preußisches Gebiet, Provinz, Personenstand, lokales Statut, Partikularrecht und subsidiäres gemeines Recht; behandle das PrALR weder vor seinem Inkrafttreten noch nach seiner Ablösung als automatisch anwendbar.", "Geltungsmatrix mit Ort, Provinz, Stichtag, Personenstand, Partikularrecht, subsidiärer Quelle, Vorrang und begründetem Anwendungsbefund"),
            ("Normnavigator durch Teil, Titel und Paragraf", "Lege aus der Sachfrage eine Suchroute durch Einleitung, Ersten oder Zweiten Teil und einschlägigen Titel an; lies Nachbarparagrafen, Definitionen, Ausnahmen und Verweisungen mit und liefere Fundstelle samt stabilem Link zum Digitalisat.", "Normenpfad mit Einleitung, Teil, Titel, Abschnitt, Paragraf, Nachbarvorschriften, Definitionen, Ausnahmen, Verweisungen und Digitalisatfundstelle"),
            ("Person, Stand und Handlungsfähigkeit", "Ordne natürliche und juristische Person, Stand, Geschlecht, Alter, Hausverband, Vormundschaft und öffentlich-rechtliche Bindung im damaligen System; trenne historische Rechtslage, gesellschaftliche Machtordnung und heutige verfassungsrechtliche Bewertung.", "historische Statusmatrix mit Person, Stand, Alter, Geschlecht, Hausverband, Handlungsfähigkeit, Vormundschaft, Quelle und getrenntem Gegenwartsbefund"),
            ("Besitz, Eigentum und Nachbarordnung", "Prüfe Gewahrsam, Besitz, Eigentum, Erwerbsart, Grundstücksbezug, Grenze, Nutzung, Dienstbarkeit und Abwehrrecht anhand des Ersten Teils; gleiche Kataster, Hypothekenbuch, Vertrag und örtliche Observanz ab, ohne heutiges Grundbuchrecht einzusetzen.", "Sachen- und Nachbarrechtskarte mit Grundstück, Gewahrsam, Besitz, Erwerb, Eigentum, Grenze, Dienstbarkeit, Observanz, Abwehrrecht und Urkundenbeleg"),
            ("Willenserklärung und Vertrag", "Bestimme Vertragstyp, Parteien, Fähigkeit, Erklärung, Form, Auslegung, Irrtum, Leistung, Gefahr, Gewährleistung und Beendigung aus den einschlägigen Titeln des Ersten Teils; kennzeichne, wo spätere BGB-Begriffe nur Vergleich und nicht historische Norm sind.", "historisches Vertragsvotum mit Vertragstyp, Fähigkeit, Erklärung, Form, Leistung, Gefahr, Gewährleistung, Beendigung und gekennzeichnetem BGB-Vergleich"),
            ("Schadensersatz und unerlaubte Handlung", "Rekonstruiere verletztes Recht, Handlung, Verschulden, Kausalität, Zufall, Mitverursachung und Ersatzumfang aus dem PrALR; prüfe Sonderregeln für Amt, Gewerbe, Hausverband oder Tierhaltung und vermeide eine rückwirkende BGB-Generalklausel.", "Schadensmatrix mit verletztem Recht, Handlung, Verschulden, Kausalität, Zufall, Mitverursachung, Sonderregel, Ersatzumfang und Originalfundstelle"),
            ("Ehe, Familie und Vormundschaft", "Ordne Eheschließung, Vermögensordnung, elterliche Gewalt, Unterhalt, Trennung, Vormundschaft und Behördenaufsicht der konkreten Zeit und Konfession zu; stelle diskriminierende Statusfolgen offen dar und trenne sie von heutiger Rechtslage.", "familienrechtliche Zeitstandskarte mit Konfession, Eheschließung, Vermögensordnung, Gewaltverhältnis, Unterhalt, Vormundschaft, Aufsicht und offener Gegenwartsdistanz"),
            ("Erbfolge und letztwillige Verfügung", "Prüfe gesetzliche Folge, Testament, Form, Fähigkeit, Erbeinsetzung, Vermächtnis, Pflichtteilsschutz, Nachlassverwaltung und Schuldenhaftung mit Personen- und Vermögensbelegen; berücksichtige partikulares Lehns- oder Familienrecht nur bei nachgewiesener Geltung.", "historische Erbfolgetafel mit Stamm, Berufungsgrund, Form, Fähigkeit, Erbeinsetzung, Vermächtnis, Pflichtteilsschutz, Haftung und partikularrechtlichem Vorbehalt"),
            ("Polizeirecht und gute Ordnung", "Arbeite für den Zweiten Teil, Titel 17, den historischen Polizeibegriff, zuständige Obrigkeit, Gefahr- oder Ordnungszweck, Eingriffsmittel und damaligen Rechtsschutz heraus; übertrage die Generalklausel nicht ungeprüft auf heutiges Polizei- und Ordnungsrecht.", "Polizeirechtsmemo zum damaligen Begriff mit Obrigkeit, Ordnungszweck, Tatbestand, Eingriffsmittel, zeitgenössischem Rechtsschutz und getrennter heutiger Vergleichsebene"),
            ("Aufopferung und Fortwirkung", "Sichere den Wortlaut der Einleitung Paragrafen 74 und 75, bestimme Eingriff, Gemeinwohlbezug, besonderes Opfer und Ausgleich im historischen Fall und zeichne die spätere dogmatische Fortwirkung nur mit eigenständigem heutigen Rechtsanker nach.", "Aufopferungssynopse mit Originalwortlaut, Eingriff, Gemeinwohl, besonderem Opfer, Ausgleich, historischer Anwendung und eigenständig belegter Fortwirkung"),
            ("Historisches Fallgutachten und Ablösung", "Löse den Fall stichtagsbezogen mit Geltungsrecht, Originalfundstelle, Tatbestand, Beweis, Rechtsfolge und zeitgenössischem Verfahrensweg; schließe mit einer Transformationskarte zu Reichsrecht, BGB-Einführungsgesetz oder Landesrecht, ohne Ergebnisse zu vermengen.", "vollständiges PrALR-Fallgutachten mit Stichtag, Geltung, Originalfundstelle, historischer Subsumtion, Beweis, Rechtsfolge, Verfahrensweg und getrennter Ablösungskarte"),
        )
    if plugin_slug == "fachanwalt-erbrecht":
        output = "mandatsreifes erbrechtliches Arbeitsprodukt mit Personenstands- und Erbfolgegrafik, Stichtagen, Nachlass- oder Schenkungswerten, Belegkette, Anspruch, Antrag und vollstreckbarer nächster Handlung"
        return (
            ("Erbfall, Statut und Fristen", "Sichere Sterbezeitpunkt, gewöhnlichen Aufenthalt, Staatsangehörigkeiten, Rechtswahl, letztwillige Verfügungen, Kenntnisdaten und Ausschlagungsfristen; trenne EuErbVO, deutsches Sachrecht, Nachlassverfahren und mögliche ausländische Registerwirkung.", output),
            ("Testament und Erbvertrag auslegen", "Ermittle Errichtungsform, Testierfähigkeit, Wortlaut, Systematik, Familienbild, Vermögenszuordnung, Andeutungen und spätere Veränderungen; trenne Erbeinsetzung, Vermächtnis, Teilungsanordnung, Auflage und Testamentsvollstreckung.", output),
            ("Bindung beim Ehegattentestament", "Prüfe Wechselbezüglichkeit nach Paragraf 2270 BGB, Widerruf, Scheidungsfolge nach Paragraf 2268 BGB, Bindung nach dem ersten Erbfall, Ausschlagung nach Paragraf 2271 Absatz 2 BGB, Anfechtung und beeinträchtigende Schenkung.", output),
            ("Gesetzliche Erbfolge und Quoten", "Baue eine Personenstandskette aus Urkunden, ordne Ordnungen und Repräsentation nach Paragrafen 1924 und folgende BGB, prüfe Ehegattenquote samt Güterstand und berechne jede Quote mit Gegenprobe.", output),
            ("Ausschlagung und Anfechtung", "Berechne Kenntnis, Sechswochen- oder Auslandsfrist, Form und zuständiges Nachlassgericht; prüfe Irrtum, Kausalität, Anfechtungsfrist und Folgen für nachrückende Personen, bevor eine Erklärung entworfen wird.", output),
            ("Pflichtteil und Auskunftsstufe", "Bestimme Berechtigten, hypothetische gesetzliche Quote, Nachlassbestand, Passiva, Anrechnungen, lebzeitige Zuwendungen und Stichtagswerte; formuliere Auskunft, notarielles Verzeichnis, Wertermittlung, eidesstattliche Versicherung und Zahlung als abgestufte Anspruchsstrategie.", output),
            ("Pflichtteilsergänzung und Abschmelzung", "Ordne jede Zuwendung nach Datum, Gegenleistung, Nießbrauch, Wohnrecht, Rückforderungsrechten, Ehegattenbezug und tatsächlichem Genussverlust; berechne Paragraf 2325 BGB ohne schematischen Fristbeginn und sichere Wertbelege.", output),
            ("Erbengemeinschaft und Auseinandersetzung", "Erfasse Nachlassgegenstände, Verwaltung, Nutzungen, Kosten, Ausgleichung, Teilungsanordnungen, Vorausvermächtnisse und Teilungsreife; trenne Verwaltungsmaßnahme, Verfügung, Abschichtung, Teilungsversteigerung und Zustimmungserfordernis.", output),
            ("Erbenhaftung und Nachlassinsolvenz", "Prüfe Inventar, unbekannte Schulden, Dreißig-Tage-Einrede, Aufgebot, Nachlassverwaltung, Nachlassinsolvenz, Dürftigkeit und Vermögensvermischung; liefere eine Fristen- und Haftungsentscheidung statt einer bloßen Schuldenliste.", output),
            ("Erbschein, Grundbuch und Register", "Trenne materiellen Erbennachweis, Erbscheinsantrag, Amtsermittlung, Einziehung, Europäisches Nachlasszeugnis und grundbuchrechtliche Nachweise; sichere Personenstand, Verfügung, Eröffnungsniederschrift und konkrete Zweifel an Echtheit oder Testierfähigkeit.", output),
            ("Testamentsvollstreckung", "Bestimme Amt, Aufgaben, Dauer, Verwaltungs- oder Abwicklungsvollstreckung, Nachlassverzeichnis, Verfügungsbefugnis, Vergütung, Interessenkonflikt, Entlassungsgrund und Rechnungslegung; formuliere Zeugnis-, Auskunfts- oder Entlassungsantrag mit Belegen.", output),
            ("Erbrechtlicher Schriftsatz und Vergleich", "Verdichte Anspruch, Quote, Berechnung, Stichtag, Beleg, Auskunftslücke, Einwendung, Verjährung und Vollstreckungsziel zu Klage, Erwiderung oder Vergleich; halte Nachlass-, Pflichtteils- und Steuerwerte sowie Kostenfolgen getrennt.", output),
        )
    if plugin_slug == "fachanwalt-familienrecht":
        output = "familiengerichtsfestes Arbeitsprodukt mit Verfahren, Eilbedarf, Monats- oder Stichtagsrechnung, Kindeswohl- und Beweismatrix, bestimmtem Antrag, Anlagenbezug und vollstreckbarer Anschlussmaßnahme"
        return (
            ("Verfahrensart, Verbund und Eilspur", "Bestimme Scheidungssache, Folgesache, selbständige Familienstreitsache, Kindschafts- oder Gewaltschutzsache, Anwaltszwang, örtliche und internationale Zuständigkeit, notwendige Beteiligte, Verbundwirkung und statthaften Eilantrag.", output),
            ("Scheidung und Trennungsjahr", "Rekonstruiere Trennung von Tisch und Bett, Wohnsituation, Versorgung, Versöhnungsversuche, Ablauf des Trennungsjahrs und Härtefall; gleiche Antrag, Zustellung, Anhängigkeit weiterer Folgesachen und Scheidungsvoraussetzungen ab.", output),
            ("Kindesunterhalt monatsgenau", "Berechne Alter, Betreuung, bereinigtes Einkommen, Einstufung, Tabellenbedarf, Kindergeld, Mehr- und Sonderbedarf, Leistungsfähigkeit, Mangelfall, Zahlungen und Rückstand für jeden Monat; belege jede Variable und trenne Titel, Auskunft und Abänderung.", output),
            ("Trennungs- und nachehelicher Unterhalt", "Trenne Bedarf nach ehelichen Lebensverhältnissen, Erwerbs- und sonstige Einkünfte, Abzüge, Erwerbsobliegenheit, Wohnvorteil, Vorsorge, Bedürftigkeit und Leistungsfähigkeit; prüfe Einsatzzeitpunkt, Befristung, Begrenzung und konkrete ehebedingte Nachteile.", output),
            ("Auskunft, Belege und Stufenantrag", "Bestimme Auskunftszeitraum, Einkunftsart und erforderliche Belege; formuliere geordnetes Verzeichnis, Belegvorlage, eidesstattliche Versicherung, Bezifferungsvorbehalt und Leistungsstufe ohne unbestimmte Sammelforderung.", output),
            ("Zugewinn und Vermögensstichtage", "Erfasse Anfangs-, Trennungs- und Endvermögen, indexiertes Anfangsvermögen, privilegierten Erwerb, illoyale Vermögensminderung, Schulden und Bewertungen; führe Vermögensbewegungen zwischen den Stichtagen in einer Beleg- und Auskunftsmatrix.", output),
            ("Versorgungsausgleich", "Bestimme Ehezeit nach Paragraf 3 VersAusglG, erfasse gesetzliche, betriebliche, private, beamten- und ausländische Anrechte, prüfe interne oder externe Teilung, Geringfügigkeit, Härte, Vereinbarung und fehlende Versorgungsträgerauskunft.", output),
            ("Elterliche Sorge", "Ordne gemeinsame oder alleinige Sorge, konkrete Angelegenheit, Kommunikationsfähigkeit, Kontinuität, Bindungen, Kindeswille, Förderungsprinzip und Risiken; formuliere Ermittlungsplan, Anhörungen, Verfahrensbeistand und bestimmten Übertragungsantrag.", output),
            ("Umgang und Vollstreckbarkeit", "Rekonstruiere bisherige Kontakte, Bindung, Alter, Kindeswille, Loyalitätskonflikt, Schutzbedarf, Entfernung und Übergaben; entwirf eine kalendarisch bestimmte, vollstreckbare Regelung samt Ferien, Kommunikation, Krankheit und Umgangspflegschaftsprüfung.", output),
            ("Kindeswohlgefährdung und Schutz", "Trenne gegenwärtige erhebliche Gefahr, körperliche oder seelische Folgen, elterliche Abwendungsfähigkeit, Hilfen und mildere Mittel; ordne Jugendamtsakte, Befunde, Anhörungen und Sachverständigenbedarf und formuliere nur erforderliche Maßnahmen nach Paragraf 1666 BGB.", output),
            ("Ehevertrag und Scheidungsfolgenvereinbarung", "Prüfe Abschlusskontrolle nach Inhalt, Verhandlungsparität und Kernbereich sowie getrennt Ausübungskontrolle nach späterer Entwicklung; ordne Unterhalt, Zugewinn, Versorgungsausgleich, Wohnung, Hausrat, Steuer und Vollzug in eine notarielle Regelungs- und Risikomatrix.", output),
            ("Familiengerichtlicher Schriftsatz", "Baue Rubrum, Verfahrensart, bestimmte Anträge, chronologischen Sachverhalt, Monats- oder Stichtagsrechnung, Kindeswohl- oder Vermögensbelege, Glaubhaftmachung, Gegenposition und Anlagenverzeichnis zu einer unmittelbar einreichbaren Fassung.", output),
        )
    if plugin_slug == "roemisch-katholisches-kirchenrecht":
        return (
            ("Hierarchischer Rekurs gegen Verwaltungsdekrete", "Ordne Urheber des Dekrets, Bekanntgabe, vorgeschaltete Abänderungsbitte, Nutzfrist, zuständigen Oberen, aufschiebende Wirkung, Aktenvorlage und Entscheidung nach cann. 1732 bis 1739 CIC.", "rekursfähige Eingabe mit Dekretsbezug, Fristenblatt, Antrag, Gründen, Belegen und Zuständigkeitsweg"),
            ("Ehenichtigkeitsverfahren", "Prüfe kirchliche Zuständigkeit, konkrete Nichtigkeitsgründe, Klageschrift, Streitfestlegung, Urkunden, Zeugen, Sachverständigenbedarf, Ehebandverteidiger, Urteil und Rechtsmittel nach cann. 1671 bis 1691 CIC.", "kanonistische Eheprozessakte mit Klagegrundmatrix, Beweisplan, Fragenkatalog und nächstem Verfahrensdekret"),
            ("Voruntersuchung und kirchliches Strafverfahren", "Trenne Voruntersuchung nach can. 1717 CIC, Schutzmaßnahmen, Verteidigungsrechte, Verjährung, gerichtlichen und außergerichtlichen Weg sowie mögliche Entscheidung nach cann. 1717 bis 1731 CIC.", "Verfahrensplan mit Zuständigkeit, Untersuchungsauftrag, Schutz- und Beweisfragen, Anhörung und zulässigem Abschlussweg"),
            ("Beweislast, Zeugen und Urkunden", "Ordne die Beweislast nach can. 1526 CIC sowie öffentliche und private Urkunden nach cann. 1540 bis 1543 CIC; dokumentiere Echtheit, Vorlage, Bestreiten, Zeugenbeweis und Beweiswert.", "Beweismatrix mit Behauptung, beweisbelasteter Partei, Beweismittel, Einwand, Erhebungsweg und Würdigung"),
            ("Dispens, Privileg und Gnadenerweis", "Prüfe zuständige Autorität, dispensables Gesetz, gerechten und vernünftigen Grund, Reichweite, Auslegung, Form, Vollzug und Erlöschen nach cann. 76 bis 93 CIC.", "Entwurf für Bittschrift oder Dekret mit Zuständigkeit, Sachgrund, beantragter Reichweite, Bedingungen und Registervermerk"),
            ("Kirchliches Amt, Bestellung und Amtsverlust", "Prüfe Errichtung und Inhalt des Amtes, Eignung, Übertragung, Besitzergreifung, Versetzung, Amtsenthebung, Verzicht und Rechtsbehelf nach cann. 145 bis 196 CIC.", "Status- und Verfahrensvermerk mit Amtsgrundlage, zuständiger Autorität, Wirksamkeitsdatum, Anhörung und Rechtsbehelf"),
            ("Kirchliches Vermögen und außerordentliche Verwaltung", "Ordne Eigentümer, Verwalter, Haushalts- und Aufsichtspflichten, ordentliche oder außerordentliche Verwaltung, Veräußerung, Genehmigungsschwellen und Haftung nach cann. 1254 bis 1310 CIC.", "Genehmigungs- und Vollzugsmatrix mit Vermögenswert, Bewertung, Zuständigkeit, Beschluss, Erlaubnis, Vertrag und Nachweis"),
            ("Pfarrei, Vermögensverwaltungsrat und Vertretung", "Prüfe Errichtung und Status der Pfarrei, Pfarrerzuständigkeit, gesetzliche Vertretung, Vermögensverwaltungsrat, Beteiligung des Ordinariats und Dokumentation nach cann. 515, 532 und 537 CIC.", "pfarreiliche Entscheidungsvorlage mit Kompetenz, Beratung, Beschlussweg, Vertretung, Urkunde und Vollzug"),
            ("Kirchenbücher, Berichtigung und Ausfertigung", "Prüfe Registerzuständigkeit, Eintragung, Randvermerk, Berichtigungsgrund, Nachweis, authentische Ausfertigung und Weitergabe insbesondere nach can. 535 CIC und einschlägigem Partikularrecht.", "Registerverfügung mit Antragsdaten, Belegprüfung, genauer Eintragung, Randvermerk, Ausfertigung und Benachrichtigung"),
            ("Archiv, Aktenzugang und Beichtgeheimnis", "Trenne kuriales Archiv nach cann. 482 bis 491 CIC, sakramentales Siegel nach cann. 983 und 984 CIC und sonstiges Seelsorgewissen; bestimme Zugangsrecht und zulässige Reaktion ohne Inhaltsweitergabe.", "Zugangs- oder Ablehnungsvermerk mit Aktenart, Berechtigung, Schutzgrund, zulässigem Umfang und dokumentierter Entscheidung"),
            ("Mehrsprachige kanonische Kommunikation", "Sichere den maßgeblichen Canon in verlässlicher Fassung, trenne verbindlichen Rechtsgehalt von pastoraler Erklärung und halte Begriffe, Namen, Fristen und Rechtsbehelf in allen Sprachfassungen deckungsgleich.", "parallele Sprachfassungen mit kanonischem Kernsatz, verständlicher Erläuterung, Handlungsauftrag und kontrollierter Terminologie"),
            ("Kirchliche und staatliche Rechtsfolgen trennen", "Bestimme eigenständig kirchliche Status- oder Verfahrenswirkung und gesondert mögliche Folgen im Arbeits-, Personenstands-, Vereins-, Datenschutz- oder staatlichen Prozessrecht; übertrage keine Rechtsfolge ungeprüft.", "Schnittstellenmemo mit zwei getrennten Rechtswegen, Zuständigkeiten, Fristen, Belegen und widerspruchsfreier Handlungsempfehlung"),
        )
    return ()


def closest_profile_line(lines: tuple[str, ...], title: str) -> str:
    """Findet nur bei echter Wortnähe eine fachlich passende Profillinie."""

    ignored = {
        "arbeiten", "bearbeiten", "erstellen", "fachanwalt", "praxis", "prüfen",
        "pruefen", "recht", "rechtlich", "skill", "spezial", "und", "oder",
    }
    title_tokens = {
        token
        for token in re.findall(r"[a-zäöüß]{4,}", title.lower())
        if token not in ignored
    }
    if not title_tokens:
        return ""
    ranked = sorted(
        (
            (
                len(
                    title_tokens
                    & {
                        token
                        for token in re.findall(r"[a-zäöüß]{4,}", line.lower())
                        if token not in ignored
                    }
                ),
                line,
            )
            for line in lines
        ),
        reverse=True,
    )
    return ranked[0][1] if ranked and ranked[0][0] else ""


def enriched_route_fallback(
    profile: ThemenProfil,
    title: str,
    focus: str,
) -> str:
    """Verbindet Routentitel, Fachprofil und konkreten Arbeitsgriff."""

    core = quick_grip(profile, title, title).rstrip(" .")
    if is_generic_route_detail(core):
        if profile.key == "ma_finanzierung":
            core = (
                f"Verankere {title} in Dealphase, Parteien, Datenraumfund, "
                "Wertwirkung, Vertragsabbildung, Freigabe, Vollzug und verantwortlichem Owner"
            )
        else:
            core = f"Bearbeite {title} als eigenständige Fachroute für {profile.label}"
    elif normalized_route_key(title) not in normalized_route_key(core):
        core = f"Bearbeite {title}: {core[:1].lower()}{core[1:]}"
    station = closest_profile_line(profile.stationen, title)
    norm = closest_profile_line(profile.normen, title)
    parts = [core, focus.rstrip(" .")]
    if (
        station
        and not is_generic_route_detail(station)
        and normalized_route_key(station) not in normalized_route_key(core)
    ):
        parts.append(f"Fachstation: {station.rstrip(' .')}")
    if norm:
        parts.append(f"Normenanker: {norm.rstrip(' .')}")
    return clean(". ".join(part for part in parts if part) + ".", 550).rstrip(" .")


def practice_route_fallback(profile: ThemenProfil, title: str, plugin_slug: str = "") -> str:
    """Formuliert aus Titel und Fachprofil einen belastbaren Spezialauftrag."""

    hay = title.lower()
    if profile.key == "berufsrecht":
        tailored = professional_route_detail(plugin_slug, title)
        if tailored:
            return tailored
    if profile.key == "medizin":
        tailored = medical_route_detail(title)
        if tailored:
            return tailored
    if profile.key == "sozial" and "pflegegrad" in hay:
        return "Ordne Pflegeantrag, MD-Gutachten und Bescheid nach den sechs Begutachtungsmodulen, prüfe Selbstständigkeit statt Diagnosen, bilde gewichtete Punkte und formuliere Beweisanträge sowie Widerspruchsziel"
    if profile.key == "sozial" and ("gdb" in hay or "merkzeichen" in hay):
        return "Ordne Funktionsbeeinträchtigungen, Einzelbewertungen, Wechselwirkungen und Merkzeichenvoraussetzungen dem Befundmaterial zu und formuliere einen medizinisch konkreten Ermittlungs- und Beweisplan"
    if profile.key == "sozial" and "arbeitslosengeld" in hay:
        return "Prüfe Anwartschaftszeit, Bemessungsrahmen, Bemessungsentgelt, Leistungsentgelt, Anspruchsdauer, Ruhen oder Sperrzeit und rechne den Bescheid mit taggenauen Versicherungs- und Entgeltdaten nach"
    if profile.key == "sozial" and "eilantrag" in hay:
        return "Bestimme statthaften Eilrechtsschutz, Anordnungsanspruch oder Vollzugsfolgen, Anordnungsgrund, Glaubhaftmachungsmittel, drohende Nachteile und formuliere Antrag sowie Hilfsantrag nach Paragraf 86b SGG"
    if profile.key == "sozial" and "widerspruch" in hay:
        return "Sichere Bekanntgabe und Monatsfrist, bezeichne den angegriffenen Verfügungssatz, trenne Verfahrens- und Leistungsfehler, fordere die Verwaltungsakte an und formuliere Abhilfeziel, Beweisanträge und Nachreichungsvorbehalt"
    if profile.key == "sozial" and "arbeitsunfall" in hay:
        return "Ordne versicherte Tätigkeit, Verrichtung, Unfallereignis, Gesundheitserstschaden und haftungsbegründende Kausalität; gleiche Durchgangsarztbericht, Unfallanzeige und Zeugen ab und formuliere die Beweisfragen nach Paragraf 8 SGB VII"
    if profile.key == "sozial" and "long covid" in hay:
        return "Prüfe versicherte Tätigkeit, Infektionsgefahr, BK-Nummer 3101, Exposition, Infektionsnachweis, Primärerkrankung und Folgen; baue aus Arbeitsplatzdaten und Befunden eine medizinisch-berufskundliche Kausalitätskette"
    if profile.key == "sozial" and "bescheidanalyse" in hay:
        return "Zerlege Verfügungssatz, Begründung, Rechtsgrundlage, Anhörung, Amtsermittlung, Ermessensausübung, Berechnung, Rechtsbehelfsbelehrung und Zustellung und liefere Fehler-, Beleg- und Angriffszeile"
    if profile.key == "sozialstatus":
        if "beitragsnachforderung" in hay or "haftung" in hay:
            return "Bestimme Beschäftigten, Einzugsstelle, Zeitraum und Beitragstatbestand, trenne Gesamtsozialversicherungsbeitrag, Säumniszuschlag und Haftungsadressat und prüfe Verjährung, Vorsatz, Vertrauensschutz sowie Vollziehung anhand des Prüfbescheids"
        if "bescheidanalyse" in hay:
            return "Zerlege Verfügungssätze zu Status und Beiträgen, Zuordnungszeitraum, Tatsachenwürdigung, Anhörung, Berechnung, Säumniszuschlag und Rechtsbehelf und markiere jede Abweichung zwischen Vertrag, gelebter Tätigkeit und Bescheid"
        if "dienst-/werkvertrag" in hay or "dienstvertrag" in hay or "werkvertrag" in hay:
            return "Trenne geschuldeten Erfolg von laufender Tätigkeit, Einzelauftrag von Rahmenvertrag und Vertragswortlaut von tatsächlicher Durchführung; ordne Weisungen, Eingliederung, Abnahme, Gewährleistung und Unternehmerrisiko nach Paragraf 7 SGB IV"
        if "honorarvertrag" in hay:
            return "Lege Honorarregel, Zeit- oder Erfolgsschuld, Ausfallrisiko, Betriebsmittel, Vertretungsrecht, Kundenakquise und tatsächliche Abrechnung nebeneinander und formuliere Vertragsänderungen nur dort, wo sie gelebte Selbständigkeit belastbar abbilden"
        if "kurzfristige beschäftigung" in hay:
            return "Prüfe Beschäftigungstage, Befristung, Zeitgrenzen, Berufsmäßigkeit, Vorbeschäftigungen und Entgelt anhand Kalender und Abrechnungen und bestimme Versicherungsfreiheit oder Beitragspflicht für jeden Teilzeitraum"
        if "paragraf 7 sgb iv" in hay or "grundabgrenzung" in hay:
            return "Gewichte Weisungsgebundenheit, Eingliederung, Unternehmerrisiko, eigene Marktpräsenz und tatsächliche Durchführung in einer Indizienmatrix; behandle Vertragsbezeichnungen nur als Ausgangspunkt und formuliere das Statusvotum mit Gegenindizien"
        if "rahmenvertrag" in hay or "einzelauftrag" in hay:
            return "Ordne jeden Einzelauftrag nach Inhalt, Abruf, Ablehnungsfreiheit, Einsatzplanung, Vergütung und Abnahme und prüfe, ob der Rahmenvertrag faktisch eine dauerhafte Eingliederung oder echte unternehmerische Disposition ermöglicht"
        if "selbständige lehrer" in hay or "selbstständige lehrer" in hay:
            return "Prüfe neben dem Beschäftigungsstatus die eigenständige Versicherungspflicht nach Paragraf 2 Satz 1 Nummer 1 SGB VI, Auftraggeberstruktur, versicherungspflichtige Arbeitnehmer, Beginn, Meldung und Beitragsfolgen"
        return "Ordne Tätigkeit, Zeitraum, Vertragsregel und gelebte Durchführung den Indizien des Paragraf 7 SGB IV zu und liefere Statusvotum, Beitragszeitraum, Beweisplan und passenden Rechtsbehelf"
    if profile.key == "rechtsgeschichte" and "normnavigator" in hay:
        return "Bestimme Teil, Titel und Paragraf des PrALR, sichere Wortlaut und Ausgabe, erläutere historischen Tatbestand und Rechtsfolge, gleiche zeitgenössische Anwendung sowie spätere Ablösung ab und kennzeichne jede moderne Anschlussfrage getrennt"
    if profile.key == "kirchenrecht":
        if "beistand" in hay and "straf" in hay:
            return "Bestimme Beschuldigungsakt, zuständige Autorität, Voruntersuchung, Schutzmaßnahme, Akteneinsicht, Verteidigungsrechte, Beweisangebot, Verjährung und zulässigen Abschluss durch Dekret oder gerichtliches Verfahren"
        if "aktenaufnahme" in hay:
            return "Erfasse Antragsteller, betroffene Person, Pfarrei, Ordinariat oder Offizialat, Zuständigkeit, Ziel, Urkunden, Registerstand, Vollmacht, Frist und erste kanonische Verfügung in einem Aktenblatt"
        if "beweis" in hay or "urkunden" in hay:
            return "Ordne Behauptung und Beweislast nach can. 1526 CIC, unterscheide öffentliche und private Urkunden nach cann. 1540 bis 1543 CIC und dokumentiere Echtheit, Vorlage, Bestreiten und Beweiswert"
        if "frist" in hay or "zeitrechnung" in hay or "verjährung" in hay:
            return "Bestimme fristauslösenden Akt, Zustellung, zusammenhängende oder Nutzfrist, Anfangs- und Endtag nach cann. 200 bis 203 CIC sowie eine besondere Verjährungs- oder Rechtsmittelfrist"
        if "arabisch" in hay or "pastoral" in hay:
            return "Kläre kirchenrechtliche Frage, Adressat, Sprachvariante und pastoralen Kontext, sichere den maßgeblichen Canon im Original und formuliere eine verständliche arabische Antwort mit getrenntem Rechts- und Seelsorgehinweis"
        if "archiv" in hay or "register" in hay:
            return "Bestimme Aktenart, Register- oder Personenstandsbezug, zuständiges Archiv, Inventarnachweis, Zugangsberechtigung, authentische Abschrift, Entnahmeverbot und Partikularrecht nach cann. 482 bis 491 CIC"
        if "auslegung" in hay or "aequitas" in hay:
            return "Lege den Canon nach Wortlaut und Kontext aus, prüfe Parallelstellen, Zweck, Umstände und Gesetzgeberwillen nach can. 17 CIC, enge Auslegung nach can. 18 CIC und Lückenfüllung unter kanonischer Billigkeit nach can. 19 CIC"
        if "beichtgeheimnis" in hay or "seelsorgegeheimnis" in hay:
            return "Trenne sakramentales Siegel, sonstiges Seelsorgewissen und außerhalb der Beichte erlangte Tatsachen; bestimme gebundene Person, Offenbarungsform, innerkirchliche Zuständigkeit, staatliches Zeugnis- oder Auskunftsbegehren und zulässige Reaktion ohne Inhaltsweitergabe"
        if re.search(r"\bcan\.\s*1\b", hay):
            return "Sichere den amtlichen Wortlaut von can. 1 CIC und kläre, ob der Vorgang die lateinische Kirche betrifft; trenne Geltungsbereich, partikulares Recht und eine mögliche Schnittstelle zum CCEO"
        return f"Bearbeite {title}: Bestimme zuständige kirchliche Autorität, anwendbaren Canon, Partikularrecht, Aktenbeleg, Frist, Verfahrensweg, Rechtsbehelf und staatliche Schnittstelle"
    if profile.key == "famil" and "zuständigkeit" in hay:
        return "Bestimme Familiensache, Verfahrensart, sachliche, örtliche und internationale Zuständigkeit, notwendige Beteiligte, Anwaltszwang, Verbund, Eilspur und die erste richterliche Verfügung"
    if profile.key == "ma_finanzierung":
        if "deadlock" in hay:
            return "Ordne Gesellschafter- oder Beiratsblockade nach auslösendem Beschlussgegenstand, Kompetenz, Quorum, Stimmbindung, Interessenkonflikt und Fortführungsrisiko; staffele Verhandlung, Eskalation, Mediation, Casting Vote, Buy-sell-Mechanik und Exit mit Fristen, Bewertungsmaßstab, Finanzierbarkeit und Missbrauchsschutz"
        if "cp" in hay or "deal-fristen" in hay or "transaktionskalender" in hay:
            return "Führe jede Condition Precedent, Covenant, Consent-, Filing-, Long-stop- und Zahlungsfrist mit Vertragsfundstelle, Auslöser, Abhängigkeit, Owner, Prüfer, Nachweis und Eskalationsdatum; trenne Signing, Pre-Closing, Closing und Post-Closing und löse keine Freigabe ohne belastbaren Erfüllungsbeleg aus"
        if "client update" in hay:
            return "Verdichte Dealstatus, seit dem letzten Bericht geänderte Fakten, rote und gelbe Punkte, Mandantenentscheidungen, Kostenstand und kommende Fristen in ein adressatengerechtes Update; trenne Information, Empfehlung und ausdrücklichen Freigabepunkt und verlinke jeden Risikopunkt mit Datenraumfund oder Vertragsstelle"
        if "dokumenten-upload" in hay or "datenextraktion" in hay:
            return "Inventarisiere jede eingehende Datei nach Quelle, Gesellschaft, Workstream, Dokumenttyp, Datum, Parteien, Laufzeit, Change-of-Control, Kündigung, Haftung, Wertbezug und Dublette; bewahre Original, Fundstelle und Versionsstand und überführe nur geprüfte Extrakte in DD-Matrix, Q&A und Vertragsentwurf"
        if "handelsregisteranmeldung" in hay or "notar-paket" in hay:
            return "Leite aus Kapitalmaßnahme und Beschlussfolge Anmeldung, notarielle Form, Vertretung, Versicherungen, Gesellschafterliste, Satzungsbescheinigung, Einzahlungs- oder Sacheinlagenbeleg und Registerdatei ab; gleiche Unterzeichnung, Einreichung, Zwischenverfügung, Eintragung und Closing-Nachweis in einer Vollzugskette ab"
        if any(word in hay for word in ("einsprachige", "bilinguale", "sprachklausel", "vertragsfassung")):
            return "Bestimme verbindliche Vertragssprache und reine Arbeitsübersetzung, führe Definitionen, Zahlen, Querverweise, Anlagen und Unterschriftsblöcke parallel und regle bei mehreren Fassungen den Vorrang ausdrücklich; kontrolliere jede Änderung gegen die maßgebliche Fassung, ohne Rechtsbegriffe scheinpräzise zu übertragen"
        if any(word in hay for word in ("kyc", "aml", "geldwäsche", "sanktionscheck")):
            return "Identifiziere Mandant, Zielgesellschaft, Erwerber, Finanzierer und wirtschaftlich Berechtigte, dokumentiere Eigentums- und Kontrollkette, Mittelherkunft, PEP- und Sanktionsbezug, Risikoeinstufung, verstärkte Sorgfalt und Freigabe; sperre Datenraumzugang, Geldfluss oder Closing bis offene Identitäts- und Trefferfragen geklärt sind"
        if "safe" in hay or "wandeldarlehen" in hay:
            return "Qualifiziere Finanzierungsinstrument, Rückzahlung, Zins, Laufzeit, Rang, Wandlungsereignis, Bewertungsobergrenze, Abschlag, Bezugsrechte und Verwässerung; prüfe Organbeschlüsse, notarielle oder registerliche Umsetzung, Insolvenzrang und die Cap-Table-Wirkung in Base-, Downside- und Exit-Szenario"
        if "gesellschafterbeschluss" in hay:
            return "Bestimme Beschlusskompetenz, Satzungsgrundlage, Einladung oder Verzicht, Teilnahme, Mehrheit, Stimmverbote, genaue Kapital- oder Vertragsmaßnahme, Vollzugsvollmacht und Wirksamkeitszeitpunkt; liefere Beschlusstext, Protokoll, Unterschriftslauf und Register- oder Closing-Anschluss ohne Lücke"
        if "corporate housekeeping" in hay or "registerabruf" in hay:
            return "Gleiche Registerauszug, Gesellschafterliste, Satzung, Geschäftsführer- und Vertretungsstand, Beschlussbuch, Vollmachten und Jahresabschlüsse mit tatsächlicher Beteiligungs- und Leitungslage ab; markiere fehlende Eintragungen, widersprüchliche Dokumente und vor Signing oder Closing nachzuholende Heilungsschritte"
        if "kommerzielle vertrags-dd" in hay or "commercial contract" in hay:
            return "Prüfe wesentliche Kunden-, Lieferanten-, Miet-, Lizenz- und Kooperationsverträge nach Parteien, Laufzeit, Umsatzbezug, Mindestabnahme, Preisänderung, Kündigung, Change-of-Control, Abtretung, Haftung, Exklusivität und Streit; übersetze jeden Befund in Q&A, Wertwirkung und konkrete SPA-Abbildung"
        if "konflikt" in hay and any(word in hay for word in ("gwg", "sanktion")):
            return "Führe Parteien, verbundene Unternehmen, Organe, Finanzierer, Bieter und frühere Mandate durch Konfliktprüfung, Sanktions- und Geldwäscherisiko; dokumentiere Treffer, Informationsbarriere, Einwilligungsbedarf, Ablehnungsgrund und Freigabe, bevor vertrauliche Unterlagen geöffnet oder Transaktionsgelder bewegt werden"
        if "dd reporting" in hay or "legal fact book" in hay:
            return "Baue aus geprüften Datenraumfunden ein Legal Fact Book mit Fundstelle, Sachverhalt, Materialität, Rechtsfolge, Gegenprüfung, Datenlücke und Owner; trenne reine Fakten von rechtlicher Wertung und verknüpfe Red Flags mit Kaufpreis, Garantie, Freistellung, Covenant, CP oder Integrationsmaßnahme"
        if "fair disclosure" in hay or "knowledge" in hay:
            return "Lege Garantie, Knowledge-Definition, offenzulegende Tatsache, Datenraumfund, Disclosure Letter und Kenntnisträger nebeneinander; prüfe hinreichende Spezifität, Fair-Disclosure-Maßstab, tatsächliche Kenntnis und Haftungsausnahme und formuliere Disclosure samt belastbarem Dokumentenverweis statt pauschaler Datenraumoffenlegung"
        if "liquiditätsvorschau" in hay or "cash burn" in hay:
            return "Erstelle eine rollierende Liquiditätsvorschau aus Bankständen, fälligen Ein- und Auszahlungen, Lohn, Steuer, Sozialversicherung, Finanzierungslinien und belastbaren Maßnahmen; trenne sicheren Bestand, harte Fälligkeit, Szenario und Finanzierungsannahme und führe Covenant-, Insolvenzreife- und Gesellschafterentscheidungen stichtagsbezogen nach"
        if "personengesellschaft" in hay or re.search(r"\bkg\b", hay):
            return "Prüfe Gesellschaftsvertrag, Gesellschafter- und Komplementärstellung, Vertretung, Zustimmungsvorbehalte, Kapitalkonten, Ergebnisverteilung, Entnahmen, Sonderbetriebsvermögen, Haftung und Registerstand; bilde Anteilserwerb oder Umstrukturierung in Beschlüssen, Vertrag, Steuerabstimmung und Registervollzug vollständig ab"
        if "fund formation" in hay or "strukturentscheidung" in hay:
            return "Bestimme AIF- und KVG-Einordnung, Fondsvehikel, Anlegerkreis, Management- und Carry-Struktur, Anlagebedingungen, Vertrieb, Verwahrstelle, Auslagerungen, Genehmigungsbedarf und Reihenfolge der Gründungsdokumente"
        if any(word in hay for word in ("antitrust", "gun jumping", "clean team")):
            return "Trenne freigabefähige von wettbewerblich sensiblen Informationen, lege Clean-Team-Zugriffe, Aggregationsregeln, Protokollierung, Eskalation und Vollzugsgrenzen bis zur Freigabe fest"
        if any(word in hay for word in ("board", "consent", "resolution")):
            return "Bestimme zuständiges Organ, Satzungs- und Geschäftsordnungsgrundlage, Informationsstand, Interessenkonflikte, Mehrheit, Beschlusstext, Unterschriftsweg und Vollzug"
        if any(word in hay for word in ("closing", "bible", "archiv")):
            return "Gleiche Signing- und Closing-Verpflichtungen mit Conditions Precedent, Deliverables, Zahlungen, Unterschriften, Registerakten und abschließendem Transaktionsindex ab"
        if any(word in hay for word in ("vdr", "diligence", "datenraum")):
            return "Ordne jedes Datenraumdokument nach Fundstelle, Gesellschaft, Zeitraum, Befund, Deal-Auswirkung, Nachforderung und Abbildung in Garantie, Freistellung, Covenant oder Kaufpreis"
        if any(word in hay for word in ("auction", "bid", "angebot")):
            return "Übersetze Process Letter, Datenraum, Vertragsentwurf und Mandantenvorgaben in ein priorisiertes Angebotsraster mit Muss-Punkt, Abweichung, Wertwirkung und Eskalationsbedarf"
        if "bank" in hay and ("consent" in hay or "change-of-control" in hay):
            return "Prüfe Change-of-Control- und Mandatory-Prepayment-Klauseln, ermittle zuständige Kreditgeber und Mehrheiten und erstelle Consent Request, Waiver-Bedingungen, Gebühren- und Closing-Abhängigkeiten"
        if "board" in hay or "business judgment" in hay:
            return "Verdichte Transaktionsrationale, Bewertung, Due-Diligence-Befunde, Alternativen, Finanzierung, Interessenkonflikte und Vollzugsrisiken zu Informationsgrundlage und abstimmungsfähigem Organbeschluss"
        if "monitoring" in hay or "automatisierung" in hay:
            return "Führe jede Signing-, Closing- und Post-Closing-Pflicht mit Auslöser, Frist, Owner, Abhängigkeit, Nachweis, Eskalation und Abschlussbeleg in einem kontrollierbaren Transaktionskalender"
        if "markup" in hay or "key issues" in hay:
            return "Ordne jede materielle Änderung nach Klausel, wirtschaftlicher Wirkung, Risikoverschiebung, Mandantenziel, Rückfallposition, Owner und Freigabestatus und formuliere die nächste Verhandlungsfassung"
        if has_route_term(hay, "ancillary", "tsa", "sla"):
            return "Baue Servicekatalog, Leistungsniveau, Preis, Laufzeit, Abhängigkeiten, Daten- und IP-Zugriff, Haftung, Exit und Übergabe für TSA, SLA und weitere Nebenverträge aus"
        if "verbindliche auskunft" in hay or "sanierungsgewinn" in hay:
            return "Fixiere den noch nicht verwirklichten Sachverhalt, die konkrete steuerliche Rechtsfrage, das erhebliche Interesse, den Gebührenwert, den beantragten Bindungsausspruch und die Umsetzung erst nach Auskunft"
    if any(word in hay for word in ("erlaubnis", "genehmigung", "zulassung")):
        return enriched_route_fallback(
            profile,
            title,
            "Bestimme den konkreten Erlaubnis- oder Zulassungstatbestand, Antragsteller, "
            "persönliche und sachliche Voraussetzungen, Drittbeteiligung, vollständige "
            "Nachweise, Nebenbestimmungen, Bekanntgabe und den passenden Rechtsschutz",
        )
    if any(word in hay for word in ("stoff", "produktklassifikation", "einordnung", "abgrenzung")):
        return enriched_route_fallback(
            profile,
            title,
            "Ordne Gegenstand, Zusammensetzung, Zweckbestimmung, Menge, Herkunft und "
            "tatsächliche Verwendung der richtigen gesetzlichen Kategorie zu; sichere "
            "Gutachten, Labor- oder Registerbeleg und behandle den Grenzfall mit beiden Rechtsfolgen",
        )
    if any(word in hay for word in ("beweis", "akteneinsicht", "aktenzugang", "dokumentation")):
        return enriched_route_fallback(
            profile,
            title,
            "Formuliere jede entscheidungserhebliche Behauptung, ordne Originalfundstelle, "
            "Beweisführer, Beweismittel, Echtheit, Bestreiten, Zugangsrecht und Beweismaß zu "
            "und übersetze die verbleibende Lücke in eine konkrete Beschaffungs- oder Beweishandlung",
        )
    if any(word in hay for word in ("frist", "verjährung", "verjaehrung", "ausschluss")):
        return enriched_route_fallback(
            profile,
            title,
            "Rekonstruiere Auslöser und Zugang, qualifiziere die Frist, berechne Beginn und "
            "Ende kalendarisch und prüfe Hemmung, Ablaufhemmung, Vorfrist, Zugangsnachweis "
            "und statthafte Fristrettung getrennt für materielles und Verfahrensrecht",
        )
    if any(word in hay for word in ("berechnung", "kosten", "quote", "bilanz", "schwelle", "betrag")):
        return enriched_route_fallback(
            profile,
            title,
            "Rechne ausschließlich aus belegten Eingabewerten mit Stichtag, Einheit, "
            "Zwischenstufen, Rundung und Gegenprobe; führe zu jeder Zahl Quelle, Rechtsgrund, "
            "Beweislast, offene Annahme und Auswirkung einer belastbaren Alternativrechnung",
        )
    if any(word in hay for word in ("widerspruch", "einspruch", "beschwerde", "klage", "rechtsmittel")):
        return enriched_route_fallback(
            profile,
            title,
            "Isoliere angegriffene Entscheidung und Rechtsschutzziel, sichere Statthaftigkeit, "
            "Beschwer, Zuständigkeit, Frist, Form und Beteiligte und formuliere aus Tatsachen, "
            "Beweisen und stärkster Gegenposition einen bestimmten Antrag mit Einreichungsweg",
        )
    if any(word in hay for word in ("urteil", "beschluss", "verfügung", "tenor", "entscheidung")):
        return enriched_route_fallback(
            profile,
            title,
            "Entwirf die im Fachverfahren richtige Entscheidungsform mit bestimmtem Ausspruch, "
            "festgestelltem Sachverhalt, offen gelegter Beweiswürdigung, tragender Subsumtion, "
            "Nebenentscheidungen und nur tatsächlich statthaftem Rechtsbehelf",
        )
    if any(word in hay for word in ("vertrag", "klausel", "vereinbarung", "satzung", "ordnung")):
        return enriched_route_fallback(
            profile,
            title,
            "Lege Regelungsziel und tatsächlichen Ablauf offen, prüfe Definitionen, "
            "Haupt- und Nebenpflichten, Bedingungen, Laufzeit, Beendigung, Haftung, Form, "
            "zwingendes Recht und Vollzug und liefere Klausel, Rückfallposition und Abschlusskontrolle",
        )
    if any(word in hay for word in ("haftung", "schaden", "regress", "anspruch")):
        return enriched_route_fallback(
            profile,
            title,
            "Zerlege Anspruchsgrund, Pflichtenkreis, Pflichtverletzung, Zurechnung, Kausalität "
            "und Schaden; ordne Einwendungen, Mitverantwortung, Verjährung, Beweislast, "
            "Versicherung und jede bezifferte Rechtsfolge den konkreten Aktenbelegen zu",
        )
    if any(word in hay for word in ("verhandlung", "vergleich", "mediation")):
        return enriched_route_fallback(
            profile,
            title,
            "Fixiere gesicherten Streitstand, Interessen, Mindestziel und objektive Kriterien, "
            "rechne Kosten- und Vollstreckungsrisiko und formuliere Vergleichskorridor, "
            "Rückfallposition, Regelungspunkte, Vollmacht und belastbaren Vollzug",
        )
    if any(word in hay for word in ("register", "meldung", "anzeige", "bericht")):
        return enriched_route_fallback(
            profile,
            title,
            "Bestimme zuständige Stelle, Pflichtigen, Auslöser, Frist und Pflichtfelder, "
            "führe jeden Eintrag auf einen Tatsachenbeleg zurück und liefere freigabefähige "
            "Meldung oder Bericht samt Übermittlungsnachweis, Korrekturweg und Anschlusskontrolle",
        )
    grip = quick_grip(profile, title, title)
    if re.sub(r"\W+", "", title.lower()) in re.sub(r"\W+", "", grip.lower()):
        return clean(grip, 360).rstrip(".")
    return enriched_route_fallback(
        profile,
        title,
        "Verbinde den konkreten Aktenfund mit Tatbestandsmerkmal, Gegenposition, Beweislast, "
        "Rechtsfolge und dem nächsten vollständig ausformulierten Arbeitsprodukt",
    )


def practice_route_anchors(detail: str, body: str) -> str:
    """Zieht wenige lokale Anker ohne erneuten Vollscan der Skilldatei."""

    anchors: list[str] = []
    seen: set[str] = set()
    for part in re.split(
        r"(?<!\bAbs\.)(?<!\bArt\.)(?<!\bNr\.)(?<!\bS\.)(?<!\bRn\.)"
        r"(?<!\bUrt\.)(?<!\bBeschl\.)(?<=[.!?])\s+|\s+-\s+",
        f"{detail}. {body}",
    ):
        candidate = route_excerpt(part, 300)
        if len(candidate) < 20:
            continue
        if ROUTE_FRAGMENT_END.search(candidate):
            continue
        if is_generic_anchor(candidate) or any(
            bit in candidate.lower() for bit in PRACTICE_ROUTE_NOISE
        ):
            continue
        has_norm = bool(re.search(r"\b(?:Paragraf|Artikel|Art\.|can\.)\s*\d", candidate))
        has_case = bool(
            re.search(
                r"\b(?:BGH|BAG|BVerfG|BVerwG|BSG|BFH|EuGH|BPatG|OLG|LG|AG|LAG|ArbG|SG|LSG)\b",
                candidate,
            )
            and (
                re.search(r"\b(?:Urteil|Beschluss|Entscheidung)\b", candidate)
                or re.search(r"\b\d{2}\.\d{2}\.\d{4}\b", candidate)
                or case_id_set(candidate)
            )
        )
        if not (has_norm or has_case):
            continue
        key = re.sub(r"\W+", "", candidate.lower())
        if key in seen:
            continue
        seen.add(key)
        anchors.append(candidate)
        if len(anchors) >= 3:
            break
    return "; ".join(anchors)


def distinct_route_depth(body: str, detail: str) -> str:
    """Behält nur eigenständige Vertiefungssätze und vermeidet Textabrisse."""

    body = route_excerpt(body, 900)
    if not body:
        return ""
    detail_key = re.sub(r"\W+", " ", detail.lower()).strip()
    clauses = CLAUSE_BOUNDARY_PATTERN.split(body)
    kept: list[str] = []
    seen: set[str] = set()
    for clause in clauses:
        clause = clause.strip(" ;")
        if len(clause) < 35:
            continue
        if ROUTE_FRAGMENT_END.search(clause):
            continue
        if "BVerfGE" in clause or "BAGE" in clause or "PBvU" in clause or case_id_set(clause):
            continue
        if re.match(
            r"^(?:und|oder|sowie|atz|satz|absatz|nummer|des|dem|der|die|das|bei|vom)\b",
            clause,
            flags=re.IGNORECASE,
        ):
            continue
        if re.search(
            r"\b(?:BGH|BAG|BVerfG|BVerwG|BSG|BFH|EuGH|BPatG|OLG|LG|LAG|ArbG|SG|LSG)\b",
            clause,
        ) and re.search(r"\b\d{2}\.\d{2}\.\d{4}\b", clause) and not case_id_set(clause):
            continue
        key = re.sub(r"\W+", " ", clause.lower()).strip()
        if not key or key in seen:
            continue
        seen.add(key)
        if key in detail_key or key[:100] in detail_key:
            continue
        kept.append(clause)
        if len("; ".join(kept)) >= 620 or len(kept) >= 5:
            break
    return route_excerpt("; ".join(kept), 700) if kept else ""


def practice_routes(
    profile: ThemenProfil,
    skill_material: list[dict[str, str]],
    max_items: int = 8,
    plugin_slug: str = "",
) -> list[tuple[str, str, str, str, str]]:
    """Wählt substanzielle, thematisch verteilte Praxisrouten des Plugins."""

    if plugin_slug in {
        "anlagen-zu-schriftsaetzen",
        "arbeitsrecht",
        "betaeubungsmittelrecht",
        "dsa-dma-digitalregulierung",
        "haushaltsrecht-bho-bund-laender",
        "informationsfreiheit-presseauskunft",
        "kommunalrecht-laender",
        "oeffentliches-wirtschaftsrecht",
        "fachanwalt-erbrecht",
        "fachanwalt-familienrecht",
        "mietrecht",
        "preussisches-allgemeines-landrecht-pralr",
        "richter-amtsgericht-straf",
        "richter-finanzgericht",
        "richter-familiengericht",
        "richter-sozialgericht",
        "relationstechnik-zivilrecht",
        "roemisch-katholisches-kirchenrecht",
        "roemisches-recht",
        "staatsanwaltschaft-amtsanwaltschaft",
        "normenkontrollrat-nkr",
        "prozessrecht",
        "produktrecht",
        "schulrecht-laender",
        "status-navigator-step-plan",
        "strafanzeige-vorbereiter",
        "strassenrecht-infrastruktur",
        "strassenverkehrsrecht-stvo",
        "tierschutzrecht",
        "umweltschutzverband-verbandsklage",
        "us-bankruptcy-code",
        "urteilsbauer-relationsmacher",
        "verbraucherinsolvenz-schuldenbereinigung",
    }:
        return [
            (title, detail, "", "", output)
            for title, detail, output in supplemental_plugin_routes(plugin_slug)[:max_items]
        ]

    candidates: list[tuple[int, str, str, str, str, str]] = []
    fallback_candidates: list[tuple[int, str, str, str, str, str]] = []
    seen_titles: set[str] = set()
    for item in skill_material:
        slug = item.get("slug", "")
        if any(bit in slug for bit in META_SKILL_BITS):
            continue
        title = field_title(item.get("desc", ""), slug, item.get("heading", ""))
        if any(bit in f"{slug} {title}".lower() for bit in META_SKILL_BITS):
            continue
        if unsuitable_route_title(title):
            continue
        raw_detail = route_excerpt(
            field_detail(item.get("desc", ""), item.get("body", ""), title),
            560,
        )
        tailored = tailored_skill_detail(item, title)
        detail = route_excerpt(tailored or raw_detail, 560)
        source_detail = raw_detail
        if any(bit in source_detail.lower() for bit in PRACTICE_ROUTE_NOISE):
            source_detail = ""
        detail = re.sub(
            r"^(?:Entscheidende Weiche|Normen-/Quellenanker|Arbeitsprodukt):\s*",
            "",
            detail,
            flags=re.IGNORECASE,
        )
        ma_prefix = (
            "Bestimme Dealphase, Fondsrolle, Target-Risiko, Finanzierungsstruktur, "
            "Consent/CP, Exit-Auswirkung und Konflikt zwischen Sponsor, Management, "
            "Lender und Co-Investor."
        )
        if profile.key == "ma_finanzierung" and detail.startswith(ma_prefix):
            remainder = detail[len(ma_prefix):].strip()
            detail = remainder if len(remainder) >= 45 else practice_route_fallback(
                profile, title, plugin_slug
            )
        for pattern, replacement in (
            (r"^Der Skill baut\b", "Baue"),
            (r"^Der Skill hilft,\s*", "Arbeite darauf hin, "),
            (r"^Der Skill erzeugt\b", "Erzeuge"),
            (r"^Der Skill übersetzt\b", "Übersetze"),
            (r"^Der Skill macht aus\b", "Mache aus"),
            (r"^Der Skill liefert\b", "Erstelle"),
            (r"^Fokus auf\b", "Fokussiere"),
        ):
            detail = re.sub(pattern, replacement, detail, flags=re.IGNORECASE)
        for marker in (
            " Welches Schreiben oder welcher Verfahrensschritt liegt vor:",
            " Welche Behörde handelt:",
            " Rolle klären:",
            " Dokumente einsammeln:",
            " Dieser Arbeitsgang arbeitet als präzises Werkzeug",
        ):
            if marker not in detail:
                continue
            prefix = detail.split(marker, 1)[0].strip(" .;:")
            if len(prefix) >= 45:
                detail = prefix
                break
        plugin_detail = plugin_route_detail(plugin_slug, title)
        if plugin_detail:
            detail = plugin_detail
        if profile.key == "berufsrecht":
            detail = professional_route_detail(plugin_slug, title) or detail
        if profile.key == "medizin":
            detail = medical_route_detail(title) or detail
        if profile.key in {"sozial", "sozialstatus"} and any(
            bit in title.lower()
            for bit in (
                "pflegegrad",
                "gdb",
                "merkzeichen",
                "arbeitslosengeld",
                "eilantrag",
                "widerspruch",
                "arbeitsunfall",
                "long covid",
                "bescheidanalyse",
                "beitragsnachforderung",
                "dienst-/werkvertrag",
                "dienstvertrag",
                "werkvertrag",
                "honorarvertrag",
                "kurzfristige beschäftigung",
                "paragraf 7 sgb iv",
                "grundabgrenzung",
                "rahmenvertrag",
                "einzelauftrag",
                "selbständige lehrer",
                "selbstständige lehrer",
            )
        ):
            detail = practice_route_fallback(profile, title, plugin_slug)
        if is_generic_route_detail(detail):
            detail = practice_route_fallback(profile, title, plugin_slug)
        if profile.key == "ma_finanzierung" and any(
            bit in title.lower()
            for bit in (
                "beirat",
                "closing",
                "auction",
                "bid grid",
                "vdr",
                "antitrust",
                "gun jumping",
                "clean team",
                "board",
                "consent",
                "markup",
                "key issues",
                "ancillary",
                "tsa",
                "sla",
                "verbindliche auskunft",
                "sanierungsgewinn",
                "deal-fristen",
                "cp-kalender",
                "kvg",
                "kagb",
                "aifm",
            )
        ):
            detail = practice_route_fallback(profile, title, plugin_slug)
        if re.match(
            r"^(?:Normen?:|Paragraf(?:en)?\b|Artikel\b|Ständige Rechtsprechung\b|"
            r"BGH\b|BAG\b|BVerfG\b|BVerwG\b|BSG\b|BFH\b|EuGH\b|BPatG\b|"
            r"OLG\b|LG\b|AG\b|LAG\b|ArbG\b|SG\b|LSG\b)",
            detail,
            flags=re.IGNORECASE,
        ):
            detail = practice_route_fallback(profile, title, plugin_slug)
        title_key = normalized_route_key(title)
        if not title_key or title_key in seen_titles:
            continue
        seen_titles.add(title_key)

        body = distinct_route_depth(item.get("body", ""), detail)
        if len(body) < 90 or any(bit in body.lower() for bit in PRACTICE_ROUTE_NOISE):
            body = ""
        anchors = practice_route_anchors(source_detail, body)
        lowered = detail.lower()
        repeated_detail = re.sub(r"\W+", "", detail.lower()) in {
            re.sub(r"\W+", "", title.lower()),
            re.sub(r"\W+", "", f"{title} {title}".lower()),
        }
        if (
            len(detail) < 55
            or repeated_detail
            or any(bit in lowered for bit in PRACTICE_ROUTE_NOISE)
            or is_generic_route_detail(detail)
        ):
            fallback_candidates.append(
                (0, practice_route_family(slug), title, practice_route_fallback(profile, title, plugin_slug), "", anchors)
            )
            continue
        legal_signals = len(re.findall(r"\b(?:Paragraf|Artikel|Art\.|can\.|[A-Z][A-Za-z]+G)\b", f"{detail} {body}"))
        score = min(len(detail) // 55, 7) + min(len(body) // 120, 5) + min(legal_signals, 5)
        candidates.append((score, practice_route_family(slug), title, detail, body, anchors))

    candidates.sort(key=lambda item: (-item[0], item[2].lower()))
    selected: list[tuple[str, str, str, str, str]] = []
    family_counts: dict[str, int] = {}
    selected_content: set[str] = set()
    selected_title_keys: set[str] = set()
    selected_topics: list[set[str]] = []
    ignored_topic_words = {
        "fachanwalt", "fachanwältin", "recht", "rechtlich", "rechts", "prüfen",
        "pruefen", "erstellen", "bearbeiten", "praxis", "spezialist", "spezialistin",
    }
    def select_from(
        pool: list[tuple[int, str, str, str, str, str]],
        family_limit: int,
    ) -> bool:
        for _score, family, title, detail, depth, anchors in pool:
            if family_counts.get(family, 0) >= family_limit:
                continue
            title_key = normalized_route_key(title)
            if not title_key or title_key in selected_title_keys:
                continue
            # Der Bearbeitungsauftrag selbst muss je Route eigenständig sein.
            # Ein anderer Vertiefungstext darf keine wortgleiche Leitzeile
            # mehrfach in denselben Prompt einschleusen.
            content_key = normalized_route_key(detail)[:300]
            if content_key and content_key in selected_content:
                continue
            topic_tokens = {
                token
                for token in re.findall(r"[a-zäöüß]{5,}", title.lower())
                if token not in ignored_topic_words
            }
            if topic_tokens and any(
                len(topic_tokens & existing) >= min(2, len(topic_tokens), len(existing))
                for existing in selected_topics
                if existing
            ):
                continue
            family_counts[family] = family_counts.get(family, 0) + 1
            if content_key:
                selected_content.add(content_key)
            selected_title_keys.add(title_key)
            selected_topics.append(topic_tokens)
            selected.append((title, detail, depth, anchors, practice_route_output(profile, title, detail, plugin_slug)))
            if len(selected) >= max_items:
                return True
        return False

    # Zunächst breite Themenverteilung, danach weitere eigenständige Skills
    # derselben Familie. So verdrängen generische Profilfelder nicht die
    # vorhandenen fachlichen Spezialrouten eines großen Plugins.
    for family_limit in (1, 2, 4, max_items):
        if select_from(candidates, family_limit):
            return selected
        if select_from(fallback_candidates, family_limit):
            return selected

    # Erst jetzt dürfen fachlich benachbarte, aber eigenständig benannte
    # Spezialrouten nachrücken. Das hält die Themenbreite hoch, ohne kleine
    # Plugins wegen einer bloßen Wortüberschneidung unter zwölf Routen fallen
    # zu lassen.
    for pool in (candidates, fallback_candidates):
        for _score, _family, title, detail, depth, anchors in pool:
            title_key = normalized_route_key(title)
            content_key = normalized_route_key(detail)[:300]
            if (
                not title_key
                or title_key in selected_title_keys
                or not content_key
                or content_key in selected_content
            ):
                continue
            selected.append(
                (title, detail, depth, anchors, practice_route_output(profile, title, detail, plugin_slug))
            )
            selected_title_keys.add(title_key)
            selected_content.add(content_key)
            if len(selected) >= max_items:
                return selected

    # Sehr kleine Plugins erhalten zusätzliche, weiterhin fachbezogene Routen
    # aus ihrem Themenprofil; kein Prompt bleibt deshalb bei Universaltexten.
    for title, detail in profile_fields(profile, skill_material, max_items * 2):
        if profile.key == "berufsrecht":
            detail = professional_route_detail(plugin_slug, title) or detail
        if profile.key == "medizin":
            detail = medical_route_detail(title) or detail
        if (
            ROUTE_FRAGMENT_END.search(detail)
            or any(bit in detail.lower() for bit in PRACTICE_ROUTE_NOISE)
            or is_generic_route_detail(detail)
        ):
            detail = practice_route_fallback(profile, title, plugin_slug)
        title_key = normalized_route_key(title)
        content_key = normalized_route_key(detail)[:300]
        if (
            unsuitable_route_title(title)
            or not title_key
            or title_key in selected_title_keys
            or not content_key
            or content_key in selected_content
        ):
            continue
        selected.append((title, detail, "", "", practice_route_output(profile, title, detail, plugin_slug)))
        selected_title_keys.add(title_key)
        selected_content.add(content_key)
        if len(selected) >= max_items:
            break
    if len(selected) < max_items:
        for title, detail, output in supplemental_plugin_routes(plugin_slug):
            title_key = normalized_route_key(title)
            content_key = normalized_route_key(detail)[:300]
            if (
                not title_key
                or title_key in selected_title_keys
                or not content_key
                or content_key in selected_content
            ):
                continue
            selected.append((title, detail, "", "", output))
            selected_title_keys.add(title_key)
            selected_content.add(content_key)
            if len(selected) >= max_items:
                break
    return selected


def practice_routes_lines(
    routes: list[tuple[str, str, str, str, str]],
    top_number: int,
) -> list[str]:
    if not routes:
        return []
    lines = [
        f"## {top_number}. Fachspezifische Praxisrouten",
        "",
        "Diese Routen stammen aus den konkreten Arbeitsthemen dieses Plugins. "
        "Wähle die sachnächste Route, liefere deren ersten verwertbaren Baustein "
        "sofort und vertiefe nur die Punkte, die das Ergebnis tatsächlich ändern.",
        "",
    ]
    for idx, (title, detail, depth, anchors, output) in enumerate(routes, 1):
        lines += [
            f"### {top_number}.{idx}. {title}",
            "",
            f"Bearbeitungsauftrag: {sentence_terminal(detail)}",
        ]
        if depth:
            lines.append(f"Prüfschritte: {sentence_terminal(route_excerpt(depth, 700))}")
        if anchors:
            lines.append(
                "Norm- oder Entscheidungsbezug aus dem Fachmaterial: "
                + sentence_terminal(clean(anchors, 360))
            )
        lines += [
            f"Lieferstück: {sentence_terminal(output)}",
            "",
        ]
    return lines


BEWEISLAST_MERKER = {
    "arbeits": "Wer sich auf den Zugang einer Erklärung beruft, beweist ihn; bei einer Arbeitgeberkündigung daher regelmäßig der Arbeitgeber. Der Arbeitgeber trägt außerdem Kündigungsgrund, ordnungsgemäße Betriebsratsanhörung und Erfüllung; der Arbeitnehmer Arbeitsleistung, eigene Anspruchsvoraussetzungen, rechtzeitige Klageerhebung und Gegenbelege.",
    "hr": "Arbeitgeber für Vertragsbedingungen, Zeiterfassung, Vergütung, Personalmaßnahme und Beteiligung; Beschäftigter für Zugang, eigene Anspruchsvoraussetzungen und Fristwahrung.",
    "zeugnis": "Arbeitnehmer für Berichtigungsziel und bessere Gesamtnote; Arbeitgeber für Wahrheit, Tatsachengrundlage, Auslassungen und formale Erfüllung.",
    "miet": "Vermieter für Rückstand, Kündigungsgrund und Abrechnung; Mieter für Mangelanzeige, Zahlung, Schonfrist und Einwendungen.",
    "famil": "Unterhaltsteller für Bedarf und Auskunft; Pflichtiger für Leistungsunfähigkeit; in Kindschaftssachen Amtsermittlung und Kindeswohlbelege.",
    "straf": "Tatnachweis beim Staat; Verteidigung markiert Zweifel, Verwertungsverbote, Alternativerklärung und Strafzumessungsstoff.",
    "datenschutz": "Verantwortlicher für Rechtmäßigkeit, TOMs und Rechenschaft; Betroffener für Schaden und Kausalität bei Ersatzansprüchen.",
    "insolvenz": "Verwalter oder Anspruchsteller für Insolvenzreife, Benachteiligung und Kenntnis; Geschäftsleitung für Entlastung und Dokumentation.",
    "steuer": "Finanzbehörde für steuerbegründende Tatsachen; Steuerpflichtiger für Begünstigung, Betriebsausgaben und Nachweise.",
    "gesellschaft": "Anspruchsteller für Pflichtverletzung, Schaden und Kausalität; Organ oder Gesellschafter für Entlastung, Beschlussbasis und Business Judgment.",
    "ma_finanzierung": "Jede Partei belegt die von ihr übernommenen Garantien, Bedingungen und Vollzugshandlungen; der Bearbeiter führt DD-Fund, Q&A, Disclosure, Freigabe, Zahlung und Registervollzug lückenlos auf den Vertragsmechanismus zurück.",
    "aktg_hv": "Die Gesellschaft belegt Einberufung, Bekanntmachung, Anmeldung, Teilnahmeprüfung, Auskunft, Abstimmung und Niederschrift; der Anfechtungskläger bezeichnet Verstoß, Anfechtungsbefugnis, Widerspruch und Klagefrist.",
    "bank": "Kunde für Beratungssituation, Schaden und Kausalität; Bank für Aufklärung, Beratungsdokumentation, Autorisierung, Ausnahme und Organisationspflicht.",
    "phishing": "Die Bank belegt Authentifizierung, ordnungsgemäße Aufzeichnung, Störungsfreiheit und ihren Gegenanspruch; der Zahler schildert den abweichenden Ablauf, seine Anzeige und entlastende Umstände konkret.",
    "datenbank": "Rechteinhaber für Schutzgegenstand, Investition, wesentliche Entnahme und Wiederverwendung; Nutzer für Lizenz, Schranke, Erlaubnis und Datenherkunft.",
    "lobbyregister": "Registerpflichtiger für Ausnahme, Angaben, Aktualisierung und Dokumentation; Behörde für Tatbestand, Ermessen und Verstoß.",
    "geldwaesche": "Verpflichteter für Risikoanalyse, Identifizierung, wirtschaftlich Berechtigte und Monitoring; Behörde für Verstoß, Verschulden und Sanktion.",
    "cybersicherheit": "Einrichtung für Risikomanagement, Nachweise und Meldung; Behörde für Anordnung, Frist, Zuständigkeit und Bußgeldtatbestand.",
    "kartell": "Anspruchsteller oder Behörde für Markt, Abstimmung, Marktmacht und Schaden; Unternehmen für Effizienz, Rechtfertigung, Compliance und Einwendungen.",
    "produkt": "Geschädigter für Produktfehler, Schaden und Kausalität; Hersteller oder Händler für Sicherheitserwartung, Warnung, Rückruf und Entlastung.",
    "forderung": "Gläubiger für Vertrag, Fälligkeit, Verzug und Belegkette; Schuldner für Erfüllung, Einwendung, Aufrechnung und Verjährung.",
    "verfass": "Beschwerdeführer für Grundrechtsbetroffenheit, Subsidiarität und Frist; Staat für Eingriff, Schranke und Verhältnismäßigkeit.",
    "versicherung": "Versicherungsnehmer für Versicherungsfall und Schaden; Versicherer für Ausschluss, Obliegenheitsverletzung und Kürzung.",
    "liquiditaet": "Geschäftsleitung muss Status, Fälligkeiten und Prognose dokumentieren; Anspruchsteller greift Lücken und verspätete Reaktion an.",
    "sozial": "Leistungsträger ermittelt von Amts wegen; Versicherter liefert Befund, Bedarf, Teilhabe- und Eilbelege.",
    "sozialstatus": "Rentenversicherung oder Einzugsstelle für Gesamtbild und Beitragsforderung; Auftraggeber und Erwerbstätiger für Vertrag, Eingliederung, Weisungen und Unternehmerrisiko.",
    "renten": "Versicherter belegt Zeiten, Lücken und medizinische Tatsachen; Träger muss Versicherungsverlauf und Bescheid nachvollziehbar begründen.",
    "verwaltung": "Behörde trägt Tatsachengrundlage, Ermessen und Verfahren; Bürger belegt Betroffenheit, Frist und Eilbedürftigkeit.",
    "vergabe": "Auftraggeber für Dokumentation und Wertung; Bieter für Rüge, Interesse, Rechtsverletzung und drohenden Schaden.",
    "urheber": "Rechteinhaber für Schutzrecht, Inhaberschaft und Nutzung; Gegner für Einrede, Lizenz, Erschöpfung oder Nichtbenutzung.",
    "marke": "Markeninhaber oder Widersprechender für Priorität, Kennzeichnungskraft, Benutzung und Kollision; Gegner für Einrede, Nichtbenutzung, Erschöpfung oder Verfall.",
    "design": "Designinhaber für Rechtsinhaberschaft, Priorität und übereinstimmenden Gesamteindruck; Gegner für Vorbekanntheit, technische Bedingtheit, Nichtigkeit und Erschöpfung.",
    "patent": "Patentinhaber für Rechtsinhaberschaft und Verletzung; Angreifer für neuheitsschädlichen Stand der Technik, Nichtigkeitsgrund oder FRAND-Einwand.",
    "gebrauchsmuster": "Inhaber für eingetragenen Anspruch, Rechtsbestand und Verletzung; Gegner für Löschungsgrund, Vorbenutzung, Erschöpfung oder sonstige Einrede.",
    "gewerblicher_rechtsschutz": "Anspruchsteller für Schutzrecht, Rechtekette, Verletzung und Dringlichkeit; Gegner für Rechtsbestand, Lizenz, Erschöpfung, Verfall oder sonstige Einrede.",
    "it": "Auftraggeber für Mangel und Abnahmevorbehalt; Anbieter für Leistung, Change Request, Mitwirkung und Haftungsbegrenzung.",
    "bauplanung": "Planer für Leistungsstand, Koordination und Honorargrund; Auftraggeber für Anordnung, Mitwirkung, Abnahme und Einwand.",
    "bau": "Auftragnehmer für Leistung, Nachtrag und Behinderung; Auftraggeber für Mangel, Abnahmevorbehalt, Zahlungskürzung und Fristsetzung.",
    "international": "Anspruchsteller für Anknüpfung, Zuständigkeit und Vollstreckbarkeit; Gegner für Gerichtsstand, ordre public und Einreden.",
    "eu_prozess": "Kläger für Zulässigkeit, Betroffenheit, Frist und Klagegrund; Organ für Rechtmäßigkeit, Ermessen und Verteidigungslinie.",
    "bgb": "Anspruchsteller für Vertrag, Pflichtverletzung, Mangel, Schaden und Kausalität; Gegner für Einwendungen, Ausschluss, Erfüllung und Verjährung.",
    "zivilprozess": "Kläger für schlüssigen Vortrag und Beweisangebot; Beklagter für erhebliche Einwendungen; Gericht führt über Hinweise und Beweisbeschluss.",
    "erbrecht": "Anspruchsteller für Verwandtschaft, Verfügung, Nachlasswert und Schenkung; Gegner für Erfüllung, Anrechnung, Ausgleichung und Ausschluss.",
    "medizin": "Patient oder Versicherter für Befund, Schaden und Kausalität; Behandler oder Träger für Aufklärung, Dokumentation, Standard und Entlastung.",
    "verkehr": "Geschädigter oder Reisender für Ereignis, Schaden, Verspätung und Belege; Gegner für Mitverschulden, Ausschluss und außergewöhnliche Umstände.",
    "vollstreckung": "Gläubiger für Titel, Klausel, Zustellung und Forderungsstand; Schuldner oder Dritter für Schutz, Erfüllung, Insolvenz und Gegenrechte.",
    "immobilien": "Antragsteller für Antrag, Bewilligung, Vertretung und Nachweis; Beteiligte für Rang, Genehmigung, Löschung und entgegenstehende Rechte.",
    "weg": "Die Gemeinschaft belegt Beschlusstext, ordnungsmäßige Vorbereitung, Kostenposition, Schlüssel und Fälligkeit; der anfechtende Eigentümer bezeichnet den Beschlussmangel innerhalb der Begründungsfrist und belegt dessen Tatsachengrundlage.",
    "eu_recht": "Wer sich auf Unionsrecht beruft, belegt Anwendungsbereich und anspruchstragende Tatsachen; Staat oder Organ trägt Rechtfertigung, Ausnahme und Verhältnismäßigkeit.",
    "methodik": "Anspruchsteller für anspruchsbegründende Tatsachen und Belegkette; Gegner für Einwendungen; offene Tatsachen niemals durch Rechtsbehauptungen ersetzen.",
    "betreuung": "Gericht ermittelt von Amts wegen; Betreuer und Behörde dokumentieren Bedarf, Wunsch, mildere Hilfe, Vertretungsmacht und Genehmigungstatsachen.",
    "hoai": "Planer für beauftragte und erbrachte Leistung sowie Honorarparameter; Auftraggeber für Mangel, Änderungsanordnung, Zahlung und mitwirkungsbedingte Störung.",
    "weltraum": "Anspruchsteller oder Staat für Gegenstand, Ereignis, Schaden und Kausalität; Betreiber und Startstaaten für Genehmigung, Aufsicht, Registrierung und Entlastung.",
    "presse": "Redaktion für Beweistatsachen, Recherche, Stellungnahmeanfrage und Statussprache; Betroffener für konkrete Unwahrheit, Beeinträchtigung und beanspruchte Abhilfe.",
    "agrar": "Antragsteller oder Bewirtschafter für Fläche, Hofstatus, Fördervoraussetzung und Beleg; Behörde oder Vertragspartner für Beanstandung, Kürzung, Einwendung und Zustellung.",
    "sport": "Verband oder Anspruchsteller für Regelwerk, Tatbestand, Zustellung und Maßnahme; Athlet oder Verein für Gegenbeleg, Fristwahrung, Eilbedarf und Einwendung.",
    "jveg": "Berechtigter für Heranziehung, Fristwahrung, Zeit, Honorargruppe und Auslage; Staatskasse für Kürzungstatbestand, Überschreitung und Einwendung.",
    "ehrenamtliche_richter": "Gericht sichert Besetzung und Verfahren; der ehrenamtliche Richter legt Neutralitätsrisiken offen und stützt Tatsachenfragen ausschließlich auf die Verhandlung.",
    "rechtsgeschichte": "Der Bearbeiter belegt Textzeuge, Fassung, Übersetzung und Rezeption; offene Quellenlage wird ausgewiesen und nicht durch Rückprojektion geschlossen.",
    "roemisch": "Der Bearbeiter belegt Epoche, Textzeuge, lateinischen Begriff, Übersetzung, Kompilationsstatus, Prozessform und Rezeption; offene Überlieferung wird nicht durch moderne Dogmatik geschlossen.",
    "pralr": "Der Bearbeiter belegt amtlichen Textzeugen, Teil, Titel, Paragraf, Fassung, Geltungszeitraum und Rezeption; offene Quellenlage wird ausgewiesen und nicht durch heutige Dogmatik ersetzt.",
    "kirchenrecht": "Antragsteller für Parteistellung, Urkunde und Anspruchstatsachen; kirchliche Autorität für Zuständigkeit, Verfahren und Entscheidungsgrundlage.",
    "kanzleibetrieb": "Verantwortlicher Bearbeiter für Annahme, Vollmacht, Frist, Freigabe und Versandnachweis; Mandant für Identitäts-, Sachverhalts- und Entscheidungsangaben.",
    "selbststaendige": "Selbstständiger für Leistung, Rechnung, Belege und Abgaben; Auftraggeber oder Behörde für Einwendung, Statusbewertung und belastende Feststellung.",
    "dokumentenworkflow": "Bearbeiter für Version, Fundstelle, Rechenweg und Übergabe; offene oder widersprüchliche Originaldaten werden nicht stillschweigend harmonisiert.",
    "default": "Anspruchsteller für anspruchsbegründende Tatsachen; Gegner für Einwendungen, Fristablauf, Erfüllung und Ausschlüsse.",
}


RECHTSFOLGE_MERKER = {
    "arbeits": "Vertrag, Personalvermerk, Zeit- oder Vergütungskorrektur, Beteiligungsvorlage, Abmahnung, Feststellungsklage, Vergleich oder Abwicklung.",
    "hr": "Arbeitsvertrag, HR-Vorgangsblatt, Personalvermerk, Zeit- oder Vergütungskorrektur, Beteiligungsvorlage, Abmahnung oder Austrittscheck.",
    "zeugnis": "Zeugnisentwurf, Berichtigungsmatrix, Aufforderungsschreiben, Klageantrag, Vergleichsklausel oder Vollstreckungsschritt.",
    "miet": "Zahlung, Minderung, Kündigung, Räumung, Instandsetzung oder Abrechnungsberichtigung.",
    "famil": "Unterhaltstitel, Sorge-/Umgangsregelung, Scheidungsausspruch, Versorgungsausgleich oder Zugewinn.",
    "straf": "Einstellung, Anklage, Freispruchslinie, Beweisantrag, Rechtsmittel oder Strafzumessungsvorschlag.",
    "datenschutz": "Auskunft, Löschung, Meldung, Anordnung, Schadensersatz oder Aufsichtsantwort.",
    "insolvenz": "Antrag, Haftungsabwehr, Forderungsanmeldung, Anfechtung, Rangklärung oder Sanierungsschritt.",
    "steuer": "Einspruch, Änderungsantrag, Aussetzung, Schätzungsangriff, Haftungsabwehr oder Klage.",
    "gesellschaft": "Beschlussfassung, Anfechtung, Organhaftung, Registervollzug, Abberufung oder Vergleich.",
    "ma_finanzierung": "Term Sheet, Bid Grid, Due-Diligence-Bericht, SPA- oder Beteiligungsklausel, Gremienvorlage, Signing- und Closing-Set oder Post-Closing-Plan.",
    "aktg_hv": "Einberufungsunterlage, HV-Fristenblatt, Q&A-Katalog, Beschluss, Niederschrift, Anfechtungsprüfung, Freigabe oder Registervollzug.",
    "bank": "Beratungsprotokoll, Erstattungsanspruch, Zahlungsdienstehaftung, Aufsichtsvermerk, Vertragsklausel oder Verteidigungslinie.",
    "phishing": "Sperr- und Rückholauftrag, Zahlungsmatrix, Erstattungsverlangen, Beleganforderung, Schlichtungsantrag, Klage oder Klageabwehr.",
    "datenbank": "Unterlassung, Auskunft, Lizenz, Schadensersatz, API-Regel, Schrankenprüfung oder Abwehrschreiben.",
    "lobbyregister": "Registrierung, Aktualisierung, Verhaltenskodex-Prüfung, Stellungnahme, Fristenblatt oder Bußgeldabwehr.",
    "geldwaesche": "Risikoanalyse, KYC-Nachforderung, Verdachtsmeldeprüfung, Transparenzregistervermerk, Aufsichtsantwort oder Bußgeldabwehr.",
    "cybersicherheit": "Risikomanagementplan, Incident-Meldung, Nachweisordner, Maßnahmenplan, Lieferkettenauflage oder Bußgeldverteidigung.",
    "kartell": "Kartellschadensmatrix, Abstellungszusage, Bußgeldverteidigung, Compliance-Maßnahme, Klage oder Vergleich.",
    "produkt": "Launch-Freigabe, Warnhinweis, Rückruf, Marktüberwachungsantwort, Haftungsmemo oder Verteidigungsentwurf.",
    "forderung": "Mahnung, Klageentwurf, Mahnbescheid, Anspruchsmatrix, Vergleichsvorschlag oder Vollstreckungsauftrag.",
    "verfass": "Nichtannahmerisiko, Verfassungsbeschwerde, Eilantrag, Normenkontrolle oder Verhältnismäßigkeitsprüfung.",
    "versicherung": "Deckung, Kürzung, Ablehnung, Regulierung, Regress oder Klageantrag.",
    "liquiditaet": "Liquiditätsstatus, Antragspflichtvermerk, Rangrücktritt, Patronatserklärung oder Zahlungsstopp.",
    "sozial": "Widerspruch, Klage, einstweiliger Rechtsschutz, Leistungsbescheid oder Vergleich.",
    "sozialstatus": "Statusfeststellungsantrag, Anhörungserwiderung, Beitragsabwehr, Nachzahlungsplan, Widerspruch oder Klage.",
    "renten": "Kontenklärung, Rentenberechnung, Widerspruch, Nachzahlung, Statusfeststellung oder Klage.",
    "verwaltung": "Widerspruch, Anfechtung, Verpflichtung, Eilantrag, Abhilfe oder Bescheidkorrektur.",
    "vergabe": "Rüge, Bieterfrage, Nachprüfungsantrag, Wertungskorrektur, Zuschlagsstopp oder Dokumentationsvermerk.",
    "urheber": "Abmahnung, Unterlassung, Auskunft, Schadensersatz, Löschung, Widerspruch oder Verteidigung.",
    "marke": "Anmeldung, Beanstandungsantwort, Widerspruch, Verfall oder Nichtigkeit, Abmahnung, Unterlassung, Auskunft, Schadensersatz oder Lizenz.",
    "design": "Anmeldung, Nichtigkeitsantrag, Unterlassung, Auskunft, Schadensersatz, Rückruf, Vergleich oder Lizenz.",
    "patent": "Anmeldung, Prüfungsbescheid, Einspruch, Nichtigkeit, Aussetzung, Unterlassung, Auskunft, Schadensersatz, FTO oder Lizenz.",
    "gebrauchsmuster": "Anmeldung, Abzweigung, Recherche, Löschung, Unterlassung, Auskunft, Schadensersatz oder einstweilige Verfügung.",
    "gewerblicher_rechtsschutz": "Portfoliovermerk, Abmahnung, Schutzschrift, einstweilige Verfügung, Hauptsache, Amtsverfahren, Vergleich oder Lizenz.",
    "it": "Abnahme, Nacherfüllung, SLA-Gutschrift, Rechteklärung, Change Request oder Haftungsvorschlag.",
    "bauplanung": "Planervermerk, LPH-Nachweis, Honorar, Nachtrag, Mängelverfolgung oder Bauüberwachungsanweisung.",
    "bau": "Nachtrag, Behinderungsanzeige, Abnahme, Mangelrüge, Vergütung, Gutachterfrage oder Sicherung.",
    "international": "Zuständigkeitsrüge, Rechtswahlvermerk, Anerkennung, Vollstreckung oder Schiedsstrategie.",
    "eu_prozess": "Klageart, Antragssatz, e-Curia-Einreichung, Zwischenantrag, Rechtsmittel oder Kostenlinie.",
    "bgb": "Anspruchsmatrix, Klauselprüfung, Mahnung, Rücktritt, Minderung, Klageentwurf, Redline oder Vergleich.",
    "zivilprozess": "Klage, Erwiderung, Relation, Hinweisverfügung, Beweisbeschluss, Urteil, Tenor oder Anlagenverzeichnis.",
    "erbrecht": "Erbquotentabelle, Pflichtteilsrechnung, Auskunft, Erbscheinsantrag, Klage oder Auseinandersetzungsvergleich.",
    "medizin": "Gutachterfragen, Anspruchsschreiben, Widerspruch, Eilantrag, Klage, Abrechnungsprüfung oder Behördenantwort.",
    "verkehr": "Regulierungsschreiben, Anspruchstabelle, Einspruch, Klage, Vergleich, Fristenblatt oder Mandantenbrief.",
    "vollstreckung": "Titelcheck, Vollstreckungsauftrag, PfÜB-Entwurf, Forderungsaufstellung, Erinnerung oder Schutzantrag.",
    "immobilien": "Grundbuchanalyse, Vertragsklausel, Vollzugsliste, Bewilligung, Zwischenverfügungsantwort oder Rangmatrix.",
    "weg": "Beschlussentwurf, Einladung, Niederschrift, Abrechnungsblatt, Verwaltervermerk, Eigentümeranschreiben oder Beschlussklage.",
    "eu_recht": "Wirkungsmatrix, Grundfreiheitenprüfung, Vorlagefrage, Umsetzungscheck, Stellungnahme oder Rechtsschutzvermerk.",
    "methodik": "Subsumtionsmatrix, Kurzvermerk, Gutachten, Schriftsatzkern, Mandantenbrief oder Zitierkontrolle.",
    "betreuung": "Aufgabenmatrix, Gerichtsantrag, Genehmigungsvorlage, Vermögensübersicht, Jahresbericht oder Schutzplan.",
    "hoai": "Leistungsstandsmatrix, Honorarblatt, Nachtragsangebot, Bedenkenhinweis, Mängelvermerk oder Projektbericht.",
    "weltraum": "Missionsrechtsmatrix, Genehmigungsfahrplan, Registermeldung, Haftungsmemo, Startvertragsklausel oder Frequenzvermerk.",
    "presse": "veröffentlichungsfähige Meldung, Quellenmatrix, Stellungnahmeanfrage, Headline-Set, Redaktionsfreigabe oder Nachtrag.",
    "agrar": "Pachtprüfung, Hofnachfolgematrix, Förderwiderspruch, Genehmigungsantrag, Behördenstellungnahme oder Vertragsentwurf.",
    "sport": "Verbandsbeschwerde, Eilantrag, Schiedsschriftsatz, Vertragsredline, Spielberechtigungsantrag oder Sponsoringvermerk.",
    "jveg": "Abrechnung, Festsetzungsantrag, Kürzungserwiderung, Beschwerde, Vorschussantrag oder Zeugenentschädigung.",
    "ehrenamtliche_richter": "Sitzungsblatt, offene Fragenliste, Neutralitätsvermerk, Beratungsstruktur oder Nachbereitungsnotiz.",
    "rechtsgeschichte": "Quellenkarte, Textsynopse, Epochenmemo, Rezeptionslinie oder historische Fallanalyse.",
    "roemisch": "römischrechtliche Quellenkarte, Exegese, Aktionen- und Fallanalyse oder Rezeptionslinie.",
    "pralr": "ALR-Quellenkarte, Paragrafensynopse, Geltungszeitmemo, historische Fallanalyse oder Rezeptionsvermerk.",
    "kirchenrecht": "Supplik, Antrag, Dekretentwurf, Eheverfahrensmatrix, Aktenvermerk oder Schnittstellenstellungnahme.",
    "kanzleibetrieb": "Mandatsblatt, Fristenkontrolle, Arbeitsauftrag, Versandprotokoll, Budgetbericht, Rechnung oder Abschlussblatt.",
    "selbststaendige": "Angebot, Auftrag, Rechnung, Mahnung, Statusmatrix, Behördenantwort oder Monatscheck.",
    "dokumentenworkflow": "Dokumentenregister, Abweichungsmatrix, Redline, Prüftabelle, Entwurf, Exportpaket oder Übergabevermerk.",
    "default": "Kurzvermerk, Prüfmatrix, Entwurf, Antrag, Entscheidungsvorschlag oder Fristenblatt.",
}


def evidence_marker(profile: ThemenProfil) -> str:
    if profile.key in BEWEISLAST_MERKER:
        return BEWEISLAST_MERKER[profile.key].rstrip(".")
    family = workflow_family(profile)
    fixed = {
        "source": "Jede historische Aussage erhält Textstelle, Textzeuge, Fassung, Übersetzungsstatus und Belegwert; offene Überlieferung bleibt offen",
        "research": "Jeder tragende Befund erhält Quelle oder Datengrundlage, Bewertungsmaßstab, Gegenhypothese und Belastbarkeitsangabe",
        "production": "Jede Änderung bleibt auf Eingangsdatei, maßgebliche Fassung, Fundstelle, Freigabe und Übergabenachweis zurückführbar",
        "drafting": "Jede Partei- und Gremienannahme erhält Dokumentbeleg, Freigabestatus und Vollzugsnachweis; offene Parameter bleiben als Entscheidungspunkt sichtbar",
        "decision": "Parteivortrag, Amtsermittlung, Darlegungs- und Beweislast werden getrennt; jeder entscheidungstragende Befund erhält eine genaue Aktenstelle",
    }
    if family in fixed:
        return fixed[family]
    station = next(
        (
            item
            for item in profile.stationen
            if any(
                term in item.lower()
                for term in (
                    "beweis",
                    "nachweis",
                    "akte",
                    "dokument",
                    "tatsach",
                    "befund",
                    "unterlage",
                )
            )
        ),
        "",
    )
    if station:
        return f"Nachweisachse {clean(station, 230).rstrip('.')}"
    question = (
        clean(profile.pruefraster[min(2, len(profile.pruefraster) - 1)], 210).rstrip(".?")
        if profile.pruefraster
        else "welcher Aktenfund trägt welches entscheidende Merkmal"
    )
    return f"Darlegungs- und Nachweisfrage für {profile.label}: {question}"


def consequence_marker(profile: ThemenProfil) -> str:
    if profile.key in RECHTSFOLGE_MERKER:
        return RECHTSFOLGE_MERKER[profile.key].rstrip(".")
    if profile.stationen:
        product = clean(profile.stationen[-1], 240).rstrip(".")
        product = re.sub(
            r"^(?:Arbeitsprodukt|Output|Ergebnis|Abschluss)\s*:\s*", "", product
        )
        if product:
            return product
    return RECHTSFOLGE_MERKER["default"].rstrip(".")


def anchor_parts(anchor: str) -> tuple[str, str]:
    """Trennt Fundstelle und Aussage, auch bei älteren Quellenzeilen ohne Doppelpunkt."""

    anchor = clean(anchor).rstrip(".")
    for sep in (":", " — "):
        if sep in anchor:
            head, tail = (part.strip() for part in anchor.split(sep, 1))
            if head and tail:
                return head, tail
    if any(marker in anchor for marker in COURT_MARKERS):
        match = re.match(
            r"^(?P<head>.+?)\s+(?:zur|zum|zu den|zu einer|zu einem|über die|über den|betreffend)\s+(?P<tail>.+)$",
            anchor,
            flags=re.IGNORECASE,
        )
        if match:
            return match.group("head").strip(), match.group("tail").strip()
    return anchor, anchor


def anchor_head(anchor: str, limit: int = 82) -> str:
    head, _tail = anchor_parts(anchor)
    return clean(head, limit).rstrip(".")


def anchor_tail(anchor: str, limit: int = 240) -> str:
    _head, tail = anchor_parts(anchor)
    return clean(tail, limit).rstrip(".")


def join_anchors(items: list[str], limit: int = 190) -> str:
    if not items:
        return "aus Akte und belastbarer Quelle ableiten"
    return clean("; ".join(anchor_head(item, 70) for item in items[:3]), limit).rstrip(".")


def fallkarte_rows(profile: ThemenProfil, fields: list[tuple[str, str]], norms: list[str], cases: list[str]) -> list[tuple[str, str, str, str]]:
    first_field = fields[0][0] if fields else profile.label
    second_field = fields[1][0] if len(fields) > 1 else first_field
    first_norm = norms[0] if norms else "Norm aus Akte"
    second_norm = norms[1] if len(norms) > 1 else first_norm
    family = workflow_family(profile)
    if family == "source":
        return [
            (
                "Quellenkern",
                clean(first_field, 80).rstrip("."),
                join_anchors([first_norm], 180),
                "Quellenkarte mit Textzeuge, Fassung, Datierung und Belegwert",
            ),
            (
                "Textstufe und Geltung",
                "Original, Übersetzung, Rekonstruktion, Rechtsraum und zeitlicher Anwendungsbereich",
                join_anchors([second_norm], 180),
                "Textsynopse mit Abweichungen und Unsicherheitsgrad",
            ),
            (
                "Gegenlesart",
                clean(second_field, 80).rstrip("."),
                join_anchors(cases[:1] or [second_norm], 180),
                "Deutungsmatrix mit Quelle, Kontext und Gegenargument",
            ),
            (
                "Rezeption und Anschluss",
                consequence_marker(profile),
                evidence_marker(profile),
                "Epochenmemo oder Rezeptionslinie ohne Rückprojektion",
            ),
        ]
    if family == "research":
        return [
            ("Arbeitsfrage", clean(first_field, 80).rstrip("."), join_anchors([first_norm], 180), "Kurzbefund mit Maßstab und offener Annahme"),
            ("Quellen- und Datenbasis", "Fundstellen, Datengrundlage, Geltungsstand und Belastbarkeit", join_anchors([second_norm], 180), "Evidenz- oder Rechenmatrix mit Kontrollspur"),
            ("Gegenhypothese", clean(second_field, 80).rstrip("."), join_anchors(cases[:1] or [second_norm], 180), "Argumentvergleich mit tragendem Unterschied"),
            ("Arbeitsprodukt", consequence_marker(profile), evidence_marker(profile), "ausformuliertes Gutachten-, Lösungs-, Antrags- oder Bewertungsstück"),
        ]
    if family == "production":
        return [
            ("Eingang", clean(first_field, 80).rstrip("."), join_anchors([first_norm], 180), "Dokumentenregister mit maßgeblicher Fassung"),
            ("Form und Technik", "Dateityp, Lesbarkeit, Benennung, Signatur und Ausgabeweg", join_anchors([second_norm], 180), "Prüfprotokoll mit konkreter Korrektur"),
            ("Vollständigkeit", clean(second_field, 80).rstrip("."), evidence_marker(profile), "Anlagen- und Fehlteilliste mit Verantwortlichem"),
            ("Freigabe und Übergabe", consequence_marker(profile), "Öffnungsprobe, Freigabe und Übergabenachweis", "fertiges Exportpaket oder Übergabevermerk"),
        ]
    if family == "drafting":
        return [
            ("Geschäfts- und Regelungskern", clean(first_field, 80).rstrip("."), join_anchors([first_norm], 180), "Entwurfsvermerk mit Ziel- und Rückfallposition"),
            ("Mechanik und Fassung", "Definition, Tatbestand, Leistung, Anpassung, Haftung und Rechtsbehelf", join_anchors([second_norm], 180), "Klausel oder Redline mit Varianten"),
            ("Nachweis und Freigabe", clean(second_field, 80).rstrip("."), evidence_marker(profile), "Gremien-, Bedingungs- und Dokumentenmatrix"),
            ("Vollzug", consequence_marker(profile), "Verantwortlicher, Termin und Erfüllungsnachweis", "Signing-, Closing- oder Registerliste"),
        ]
    if family == "decision":
        return [
            ("Streit- und Verfahrenskern", clean(first_field, 80).rstrip("."), join_anchors([first_norm], 180), "richterlicher Arbeitsvermerk mit nächster Verfügung"),
            ("Zulässigkeit und Gehör", "Antrag, Zuständigkeit, Parteistellung, Frist und Anhörung", join_anchors([second_norm], 180), "Hinweis-, Auflagen- oder Zwischenentscheidungsentwurf"),
            ("Beweis und Würdigung", clean(second_field, 80).rstrip("."), evidence_marker(profile), "Beweisplan oder Beweisbeschluss mit Entscheidungsreife"),
            ("Tenor und Anschluss", consequence_marker(profile), join_anchors(cases[:1] or [second_norm], 180), "Tenor, Gründe, Kosten, Vollstreckbarkeit und Rechtsmittelbelehrung"),
        ]
    return [
        (
            "Fallkern",
            clean(first_field, 80).rstrip("."),
            join_anchors([first_norm], 180),
            "Sofortvermerk mit Ergebnisrichtung, Risiko und nächstem Schritt",
        ),
        (
            "Zulässigkeit und Frist",
            "Frist, Form, Zuständigkeit, Rolle und statthafter Weg",
            join_anchors([second_norm], 180),
            "Fristenblatt oder Prozess-/Verfahrensroute",
        ),
        (
            "Begründetheit",
            clean(second_field, 80).rstrip("."),
            join_anchors([second_norm], 180),
            "Tatbestandsmatrix mit Beleg und Gegenargument",
        ),
        (
            "Rechtsfolge",
            consequence_marker(profile),
            evidence_marker(profile),
            "Antrag, Entwurf, Entscheidungsvorschlag oder Mandantenbrief",
        ),
    ]


def first_readme_paragraph(plugin_dir: Path) -> str:
    readme = plugin_dir / "README.md"
    if not readme.exists():
        return ""
    try:
        text = readme.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return ""
    text = re.sub(r"<!--[\s\S]*?-->", " ", text)
    paragraphs = []
    current: list[str] = []
    for raw in text.splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or line.startswith("|") or line.startswith("["):
            if current:
                paragraphs.append(" ".join(current))
                current = []
            continue
        if line.startswith("- ") or line.startswith("* "):
            continue
        current.append(line)
        if len(" ".join(current)) > 500:
            paragraphs.append(" ".join(current))
            break
    if current:
        paragraphs.append(" ".join(current))
    for paragraph in paragraphs:
        cleaned = clean(paragraph, 700)
        if len(cleaned) > 80:
            return cleaned
    return ""


def title_for(slug: str, mf: dict, profile: ThemenProfil) -> str:
    title_overrides = {
        "aussenwirtschaft-zoll-sanktionen": "Außenwirtschaft, Sanktionen, Zoll und CBAM",
        "bgb-at-pruefer": "BGB AT-Prüfer",
        "bgb-bt-pruefer": "BGB BT-Prüfer",
        "dfg-foerderantrag": "DFG-Förderantrag",
        "ecommerce-recht": "E-Commerce-Recht",
        "email-umformulierer-berufsrecht": "E-Mail-Umformulierer Berufsrecht",
        "grosskanzlei-corporate-ma": "Großkanzlei Corporate/M&A",
        "mittelstand-corporate-ma": "Mittelstand Corporate/M&A",
        "nis2-cybersecurity-compliance": "NIS-2, Cybersecurity und IT-Sicherheits-Compliance",
        "preussisches-allgemeines-landrecht-pralr": "Preußisches Allgemeines Landrecht (PrALR)",
        "roemisch-katholisches-kirchenrecht": "Römisch-katholisches Kirchenrecht",
        "roemisches-recht": "Römisches Recht",
        "softwarerecht-de-eu-us": "Softwarerecht Deutschland/EU/USA",
        "strassenrecht-infrastruktur": "Straßenrecht und Infrastruktur",
        "strassenverkehrsrecht-stvo": "Straßenverkehrsrecht StVO",
        "urheberrecht-de-eu": "Urheberrecht Deutschland/EU",
        "verkehrsowi-verteidiger": "Verkehrs-OWi-Verteidiger",
    }
    if slug in title_overrides:
        return title_overrides[slug]
    raw = mf.get("display_name") or mf.get("title") or slug.replace("-", " ")
    raw = raw.replace("_", " ").strip()
    if raw.lower() == slug:
        raw = slug.replace("-", " ")
    title = raw.title()
    acronyms = {
        "Ag": "AG",
        "Agb": "AGB",
        "Aml": "AML",
        "Bafin": "BaFin",
        "Bav": "bAV",
        "Bgb": "BGB",
        "Bgh": "BGH",
        "Bverfg": "BVerfG",
        "Ce": "CE",
        "Dma": "DMA",
        "Dfg": "DFG",
        "Dsa": "DSA",
        "Eu": "EU",
        "Eugh": "EuGH",
        "Gmbh": "GmbH",
        "Gmbhg": "GmbHG",
        "Hoai": "HOAI",
        "Ip": "IP",
        "It": "IT",
        "Kyc": "KYC",
        "Nda": "NDA",
        "Nkr": "NKR",
        "Owi": "OWi",
        "Se": "SE",
        "Sgb": "SGB",
        "Us": "US",
        "Uwg": "UWG",
        "Vvg": "VVG",
        "Weg": "WEG",
    }
    for wrong, right in acronyms.items():
        title = re.sub(rf"\b{re.escape(wrong)}\b", right, title)
    title = re.sub(r"\bUnd\b", "und", title)
    return clean(title, 120)


def station_text(stations: Iterable[str], skill_material: list[dict[str, str]]) -> list[str]:
    out = list(stations)
    for item in skill_material[:7]:
        desc = item["desc"] or item["body"]
        if not desc:
            continue
        candidate = clean(desc, 260)
        if candidate and candidate not in out:
            out.append(candidate)
    return out[:12]


def remove_h2_section(text: str, title_part: str) -> str:
    match = re.search(rf"^## \d+\. .*{re.escape(title_part)}.*$", text, flags=re.M)
    if not match:
        return text
    next_match = re.search(r"^## \d+\. ", text[match.end():], flags=re.M)
    end = match.end() + next_match.start() if next_match else len(text)
    return (text[: match.start()].rstrip() + "\n\n" + text[end:].lstrip()).rstrip() + "\n"


def renumber_h2_sections(text: str) -> str:
    counter = 0
    subcounter = 0
    out: list[str] = []
    for line in text.splitlines():
        match = re.match(
            r"^(##)\s+(?:(?:\d+(?:\.\d+)*\.?)\s+)*(.+)$",
            line,
        )
        if match and not line.startswith("###"):
            counter += 1
            subcounter = 0
            out.append(f"## {counter}. {match.group(2).strip()}")
        elif submatch := re.match(r"^###\s+(?:(?:\d+\.)+\d+\.?\s+)?(.+)$", line):
            if counter == 0:
                counter = 1
                subcounter = 0
                out.append(f"## {counter}. {submatch.group(1).strip()}")
            else:
                subcounter += 1
                out.append(f"### {counter}.{subcounter}. {submatch.group(1).strip()}")
        else:
            out.append(line)
    return "\n".join(out).rstrip() + "\n"


def trim_bullet_section(text: str, title_part: str, keep: int) -> str:
    match = re.search(rf"^## \d+\. .*{re.escape(title_part)}.*$", text, flags=re.M)
    if not match:
        return text
    next_match = re.search(r"^## \d+\. ", text[match.end():], flags=re.M)
    end = match.end() + next_match.start() if next_match else len(text)
    block = text[match.start():end]
    out: list[str] = []
    bullets = 0
    for line in block.splitlines():
        if line.startswith("- "):
            bullets += 1
            if bullets > keep:
                continue
        out.append(line)
    return text[: match.start()] + "\n".join(out).rstrip() + "\n\n" + text[end:].lstrip()


def compact_werkstatt(text: str) -> str:
    max_size = MAX_WERKSTATT
    if byte_len(text) <= max_size:
        return text
    for title in ("Musterbausteine", "Qualitätskontrolle und Abschluss"):
        text = remove_h2_section(text, title)
        if byte_len(text) <= max_size:
            return renumber_h2_sections(text)
    for title, keep in (("Leitentscheidungen", 4), ("Pflichtnormen", 12), ("Fachliche Entscheidungslandkarte", 8)):
        text = trim_bullet_section(text, title, keep)
        if byte_len(text) <= max_size:
            return renumber_h2_sections(text)
    text = remove_h2_section(text, "Arbeitsweise")
    return renumber_h2_sections(text)


def build_werkstatt(
    plugin_dir: Path,
    skill_material: list[dict[str, str]] | None = None,
) -> str:
    mf = manifest(plugin_dir)
    slug = mf.get("name") or plugin_dir.name
    if skill_material is None:
        skill_material = collect_skill_material(plugin_dir)
    context = " ".join([mf.get("description", ""), first_readme_paragraph(plugin_dir)] + [s["desc"] for s in skill_material[:20]])
    profile = profile_for(slug, context)
    title = title_for(slug, mf, profile)
    stations = list(profile.stationen)
    intro = clean(mf.get("description", "") or first_readme_paragraph(plugin_dir) or profile.rolle, 900)
    profile_norms = [] if profile.key == "default" else list(profile.normen)
    profile_cases = [] if profile.key == "default" else list(profile.entscheidungen)
    extracted_norms = extract_norm_anchors(skill_material, 8)
    extracted_cases = extract_case_anchors(skill_material, 5)
    if profile.key in CURATED_NORM_PROFILE_KEYS:
        extracted_norms = []
    if profile.key in CURATED_CASE_PROFILE_KEYS:
        extracted_cases = []
    if profile.key in PROFILE_CASE_SKIP_KEYS:
        profile_cases = []
    if slug in CASE_RESEARCH_ONLY_SLUGS:
        profile_cases = []
        extracted_cases = []
    if slug in PLUGIN_CASE_OVERRIDES:
        profile_cases = list(PLUGIN_CASE_OVERRIDES[slug])
        extracted_cases = []
    extracted_cases = dedupe_cases(profile_cases, extracted_cases)
    routes = practice_routes(profile, skill_material, 12, plugin_slug=slug)
    fields = workshop_fields(profile, routes, 9)
    norm_pool = (profile_norms + extracted_norms)[:8]
    case_pool = (profile_cases + extracted_cases)[:5]
    fallkarte_title, matrix_title, matrix_headers, cases_title, norms_title = section_titles(profile)
    lead_title = (
        "Leitquellen und Rezeptionsentscheidungen"
        if workflow_family(profile) == "source"
        else "Leitentscheidungen und tragende Quellen"
        if workflow_family(profile) in {"research", "production"}
        else "Leitentscheidungen"
    )

    lines: list[str] = [f"# {title} — Werkstatt-Prompt", ""]
    if profile.oeffnungssatz:
        lines += [profile.oeffnungssatz, ""]
    lines += [
        "## 1. Rolle und Auftrag",
        "",
        f"Du arbeitest als {profile.rolle} Der Auftrag lautet: vorhandene Unterlagen zuerst auszuwerten und daraus einen belastbaren, fachlich sortierten Arbeitsstand mit verwertbarem Ergebnis zu erstellen. Gegenstand dieses Prompts ist: {intro}",
        "",
        role_scope_text(profile),
        "",
    ] + werkstatt_tempo_block(profile) + werkstatt_ergonomy_text(profile).splitlines() + [
        "## 2. Stop-Kriterien",
        "",
    ]
    for item in profile.stop:
        lines.append(f"- {item}")
    for item in stop_guard_lines(profile):
        lines.append(f"- {item}")
    lines += [
        "",
        "## 3. Werkstattfluss",
        "",
    ]

    for idx, station in enumerate(stations, 1):
        lines += [
            f"### 3.{idx}. {station_heading(station)}",
            "",
            station_instruction(profile, station),
            "",
        ]

    lines += [
        f"## 4. {fallkarte_title}",
        "",
        "| Ebene | Fallfrage | Anker | Sofortausgabe |",
        "| --- | --- | --- | --- |",
    ]
    for level, question, anchor, output in fallkarte_rows(profile, fields, norm_pool, case_pool):
        lines.append(f"| {level} | {question} | {anchor} | {output} |")

    lines += [
        "",
        f"## 5. {matrix_title}",
        "",
        f"| {matrix_headers[0]} | {matrix_headers[1]} | {matrix_headers[2]} | {matrix_headers[3]} |",
        "| --- | --- | --- | --- |",
    ]
    if norm_pool:
        for norm in norm_pool[:7]:
            lines.append(f"| {anchor_head(norm, 110)} | {anchor_tail(norm, 240)} | {evidence_marker(profile)} | {consequence_marker(profile)} |")
    else:
        lines.append(f"| Aktennorm | Aus Bescheid, Vertrag, Antrag, Verfügung oder Schriftsatz entnehmen | {evidence_marker(profile)} | {consequence_marker(profile)} |")

    lines += [
        "",
        f"## 6. {cases_title}",
        "",
    ]
    if case_pool:
        lines.append("| Rechtsprechungsanker | Quellenstatus | Nutzwert im Fall |")
        lines.append("| --- | --- | --- |")
        for case in case_pool[:5]:
            status = "Profilanker" if case in profile_cases else "aus Skillmaterial extrahierter Anker"
            lines.append(f"| {anchor_head(case, 130)} | {status}; vor Zitierung am Aktenstand oder an belastbarer Quelle sichern | {anchor_tail(case, 320)} |")
    else:
        lines.append(missing_case_anchor_line(profile))
    lines += case_section_footer(profile)
    lines += ["", f"## 7. {norms_title}", ""]
    for item in profile_norms:
        lines.append(f"- {item}")

    # Add norms extracted from selected skills without making skill references.
    for norm in extracted_norms[:8]:
        lines.append(f"- {norm}; im konkreten Sachverhalt als Tatbestands- oder Verfahrensanker prüfen.")
    if not profile_norms and not extracted_norms:
        lines.append("- Tragende Normen aus Akte, Bescheid, Vertrag oder gerichtlicher Verfügung ableiten; keine Norm als sicher darstellen, wenn sie nicht belegt ist.")

    lines += [
        "",
        f"## 8. {lead_title}",
        "",
    ]
    for item in profile_cases:
        lines.append(f"- {sentence_terminal(item)}")
    for item in extracted_cases:
        lines.append(f"- {sentence_terminal(item)}")
    if not profile_cases and not extracted_cases:
        lines.append(missing_lead_source_line(profile))

    lines += [
        "",
        "## 9. Prüfraster",
        "",
    ]
    for idx, item in enumerate(profile.pruefraster, 1):
        lines.append(f"{idx}. {item}")
    missing_item, product_item = additional_pruefraster_items(profile)
    lines += [
        f"{len(profile.pruefraster)+1}. {missing_item}",
        f"{len(profile.pruefraster)+2}. {product_item}",
        "",
        f"## 10. {argumentation_title(profile)}",
        "",
    ]
    lines += argumentation_lines(profile, norm_pool, case_pool, fields)
    lines += [
        "",
        "## 11. Outputvarianten und Empfängerwunsch",
        "",
        "| Wunsch | Ausgabe | Mindestinhalt |",
        "| --- | --- | --- |",
    ]
    lines += output_variant_rows(profile, norm_pool, fields)
    lines += [
        "",
        "## 12. Arbeitsweise",
        "",
        workflow_method_text(profile),
        "",
        workflow_selfcheck(profile),
        "",
        "## 13. Qualitätskontrolle und Abschluss",
        "",
        quality_control_text(profile),
        "",
        "## 14. Musterbausteine",
        "",
    ]
    skeletons = list(profile.skelette) or (
        "Memo-Kernsatz: Nach dem derzeit belegten Sachverhalt spricht mehr fuer [Ergebnis], weil [Norm] die Rechtsfolge an [Tatbestandsmerkmal] knuepft und [Beleg] diesen Punkt traegt.",
        "Nachforderung: Bitte reichen Sie bis [Datum] [Dokument] ein; ohne diesen Beleg kann [Tatbestandsmerkmal] nicht tragfaehig beurteilt werden.",
        "Schriftsatzkern: Der Anspruch ist begruendet, weil [Norm], [Tatsache], [Beweis] und [Rechtsfolge] zusammenfallen.",
    )
    for item in skeletons:
        lines.append(f"- {item}")

    if routes:
        lines += [
            "",
            "## 15. Fachliche Entscheidungslandkarte",
            "",
            "Die Landkarte dient der schnellen Auswahl. Sie ersetzt nicht die darunter "
            "ausformulierten Praxisrouten, sondern zeigt für jedes Kernfeld die "
            "entscheidende Weiche und das zuerst zu liefernde Arbeitsprodukt.",
            "",
            "| Arbeitsfeld | Entscheidende Weiche | Erstes Lieferstück |",
            "| --- | --- | --- |",
        ]
        for route_title, detail, _depth, _anchors, output in routes[:9]:
            lines.append(
                f"| {clean(route_title, 90)} | {clean(detail, 220)} | "
                f"{clean(output, 180)} |"
            )

    if routes:
        lines += [""] + practice_routes_lines(routes, 16)

    text = "\n".join(lines).strip() + "\n"
    if len(text.encode("utf-8")) < 12 * 1024 and "Ausgabeformate für schnelle Lieferung" not in text:
        text = text.replace(
            "\n".join(WERKSTATT_TEMPO_BLOCK).rstrip(),
            "\n".join(WERKSTATT_TEMPO_BLOCK).rstrip() + "\n\n" + werkstatt_ergonomy_text(profile).rstrip(),
            1,
        )
    if len(text.encode("utf-8")) < 12 * 1024 and "Schlusskontrolle für Tempo" not in text:
        text = text.rstrip() + "\n\n" + werkstatt_final_check_block(text).rstrip() + "\n"
    if len(text.encode("utf-8")) < 12 * 1024 and "Vertiefungsmodus für belastbare Ausgabe" not in text:
        text = text.rstrip() + "\n\n" + werkstatt_depth_block(text).rstrip() + "\n"
    return sanitize(compact_werkstatt(text))


def compact_schnellstart(text: str) -> str:
    if byte_len(text) <= MAX_FAST:
        return text

    def shorten_einsatzfelder(match: re.Match[str]) -> str:
        block = match.group(0)
        lines = block.splitlines()
        header = lines[:4]
        rows = [line for line in lines[4:] if line.startswith("|")]
        return "\n".join(header + rows[:3]) + "\n\n"

    text = re.sub(
        r"## 5\. Einsatzfelder\n\n\| Feld \| Sofortgriff \| Ausgabe \|\n\| --- \| --- \| --- \|\n(?:\|.*\|\n)+",
        shorten_einsatzfelder,
        text,
        count=1,
    )
    if byte_len(text) <= MAX_FAST:
        return text

    parts = re.split(r"\n## (?:6\.\s+)?Anker\n", text, maxsplit=1)
    if len(parts) == 2:
        head, rest = parts
        split = re.split(r"\n## (?:7\.\s+)?Antwortform\n", rest, maxsplit=1)
        if len(split) == 2:
            anchor, tail = split
            anchor_lines = [l for l in anchor.splitlines() if l.strip()][:7]
            text = head.rstrip() + "\n\n## 6. Anker\n\n" + "\n".join(anchor_lines) + "\n\n## 7. Antwortform\n" + tail
    if byte_len(text) <= MAX_FAST:
        return text

    text = re.sub(
        r"\n## 4\. Fallkarte\n\n\| Punkt \| Sofortgriff \|\n\| --- \| --- \|\n(?:\|.*\|\n)+",
        lambda m: "\n".join(m.group(0).splitlines()[:7]) + "\n\n",
        text,
        count=1,
    )
    if byte_len(text) <= MAX_FAST:
        return text

    text = re.sub(
        r"\n## 4\. Fallkarte\n[\s\S]*?(?=\n## 5\. )",
        "\n",
        text,
        count=1,
    )
    if byte_len(text) <= MAX_FAST:
        return text

    def shorten_kernroute(match: re.Match[str]) -> str:
        lines = match.group(0).splitlines()
        steps = [line for line in lines if re.match(r"^\d+\. ", line)]
        return "\n## 3. Kernroute\n\n" + "\n".join(steps[:4]) + "\n"

    text = re.sub(
        r"\n## 3\. Kernroute\n\n(?:\d+\..*\n)+",
        shorten_kernroute,
        text,
        count=1,
    )
    if byte_len(text) <= MAX_FAST:
        return text

    text = re.sub(r"\nZielprodukt:.*\n", "\n", text, count=1)
    if byte_len(text) <= MAX_FAST:
        return text

    raise ValueError(
        f"Schnellstart lässt sich nicht vollständig unter {MAX_FAST} Bytes verdichten: "
        f"{byte_len(text)} Bytes"
    )


def build_schnellstart(
    plugin_dir: Path,
    skill_material: list[dict[str, str]] | None = None,
) -> str:
    mf = manifest(plugin_dir)
    slug = mf.get("name") or plugin_dir.name
    if skill_material is None:
        skill_material = collect_skill_material(plugin_dir)
    context = " ".join([mf.get("description", ""), first_readme_paragraph(plugin_dir)] + [s["desc"] for s in skill_material[:20]])
    profile = profile_for(slug, context)
    title = title_for(slug, mf, profile)
    fields = profile_fields(profile, skill_material)
    stations = quick_stations(profile, skill_material)[:5]
    norm_limit = 7 if profile.key == "default" else 4
    case_limit = 4 if profile.key == "default" else 3
    extracted_norms = extract_norm_anchors(skill_material, norm_limit)
    extracted_cases = extract_case_anchors(skill_material, case_limit)
    if profile.key in CURATED_NORM_PROFILE_KEYS:
        extracted_norms = []
    if profile.key in CURATED_CASE_PROFILE_KEYS:
        extracted_cases = []
    profile_norms = [] if profile.key == "default" else list(profile.normen[:4])
    profile_cases = [] if profile.key == "default" else list(profile.entscheidungen[:2])
    if profile.key in PROFILE_CASE_SKIP_KEYS:
        profile_cases = []
    if slug in CASE_RESEARCH_ONLY_SLUGS:
        profile_cases = []
        extracted_cases = []
    if slug in PLUGIN_CASE_OVERRIDES:
        profile_cases = list(PLUGIN_CASE_OVERRIDES[slug][:2])
        extracted_cases = []
    extracted_cases = dedupe_cases(profile_cases, extracted_cases)
    norm_pool = (profile_norms + extracted_norms)[:6]
    case_pool = (profile_cases + extracted_cases)[:4]
    goal = domain_goal(mf, plugin_dir, profile)
    opening = profile.oeffnungssatz
    if profile.key == "default":
        opening = f"Wenn du das hier öffnest, soll zuerst vorhandenes Material zum Thema {title} ausgewertet und daraus ein verwertbarer Erststand gebaut werden."

    lines: list[str] = [f"# {title} — Schnellstart", ""]
    if opening:
        lines += [opening, ""]
    lines += [
        f"Kernauftrag: {clean(goal, 220).rstrip('.')}. Vorrang hat das verlangte Arbeitsprodukt.",
        "",
    ] + schnellstart_bedienlogik(profile, fields, stations) + [
        "## 2. Fachlicher Direktstart",
        "",
    ] + schnellstart_direktstart(profile) + [
        "",
        "## 3. Kernroute",
        "",
    ]
    for idx, station in enumerate(stations, 1):
        lines.append(f"{idx}. {clean(station, 230)}")
    lines += [
        "",
        "## 4. Fallkarte",
        "",
        "| Punkt | Sofortgriff |",
        "| --- | --- |",
        f"| Normenanker | {join_anchors(norm_pool[:3], 220)} |",
        f"| Rechtsprechung | {join_anchors(case_pool[:2], 220)} |",
        f"| Tatbestand | {quick_grip(profile, fields[0][0], fields[0][1]) if fields else stations[0]} |",
        f"| Beweislast | {evidence_marker(profile)} |",
        f"| Rechtsfolge | {consequence_marker(profile)} |",
        "| Quellenstatus | Aktenfund, Normtext, Profilanker oder sicher belegte Entscheidung offen kennzeichnen; unsichere Aktenzeichen nicht ergänzen |",
    ]
    if fields:
        lines += [
            "",
            "## 5. Einsatzfelder",
            "",
            "| Feld | Sofortgriff | Ausgabe |",
            "| --- | --- | --- |",
        ]
        for field, detail in fields:
            grip = quick_grip(profile, field, detail)
            lines.append(f"| {field} | {grip}. | Ergebnisbaustein mit Beleg, Risiko und nächstem Schritt |")
    lines += ["", "## 6. Anker", ""]
    anchor_count = 0
    for item in profile_norms:
        lines.append(f"- {item}")
        anchor_count += 1
    for item in extracted_norms:
        lines.append(f"- {item}; im Sachverhalt als tragenden Norm- oder Verfahrensanker prüfen.")
        anchor_count += 1
    for item in profile_cases:
        lines.append(f"- {sentence_terminal(item)}")
        anchor_count += 1
    for item in extracted_cases:
        lines.append(f"- {sentence_terminal(item)}")
        anchor_count += 1
    if anchor_count == 0:
        lines.append("- Normen und Entscheidungen aus den vorgelegten Unterlagen oder einer belastbaren Quelle ableiten; Aktenzeichen nicht ergänzen, wenn sie nicht sicher belegt sind.")
    consequence_short = clean(consequence_marker(profile), 145).rstrip(" .;:")
    evidence_short = clean(evidence_marker(profile), 210).rstrip(" .;:")
    attack_short = sentence_lead(
        clean(domain_attack(profile), 150).rstrip(" .;:")
    )
    output_short = schnellstart_product_label(profile, fields)
    family = workflow_family(profile)
    result_label = {
        "source": "erste historische Einordnung",
        "research": "erstes belastbares Ergebnis",
        "production": "erste Ausgabestufe",
        "drafting": "erste Regelungsfolge",
    }.get(family, "erste Rechtsfolge")
    finding_label = {
        "source": "Quellenfund",
        "research": "Materialfund",
        "production": "Dateifund",
    }.get(family, "Aktenfund")
    response_label = {
        "source": "Gegenquelle, abweichende Lesart oder Datierungsargument",
        "research": "Gegenbeleg, Alternativhypothese oder Bewertungsmaßstab",
        "production": "Korrekturbeleg, Formatregel oder Freigabevorgabe",
        "drafting": "Gegenbeleg, Auslegung oder Risikozuweisung",
    }.get(family, "Gegenbeleg, Auslegung oder Lastregel")
    anchor_label, anchor_action = {
        "source": ("Quellenanker", "nach Textstufe, Epoche und Kontext einordnen"),
        "research": ("Maßstab", "mit der entscheidenden Bewertungsfrage verbinden"),
        "production": ("Vorgabe", "auf Datei, Fassung und Ausgabeziel beziehen"),
        "drafting": ("Regelungsanker", "mit Risikozuweisung und Vollzug verbinden"),
    }.get(family, ("Norm", "mit dem entscheidenden Merkmal verbinden"))
    closing_label = "nächstem Dokument"
    if family == "source":
        closing_label = "nächster Quelle oder Darstellungsstufe"
    elif family == "research":
        closing_label = "nächster Prüfstufe"
    elif family == "production":
        closing_label = "nächster Freigabe- oder Ausgabestufe"
    lines += [
        "",
        "## 7. Antwortform",
        "",
        f"7.1. Ergebnis: Rolle und Ziel benennen; {result_label}: {consequence_short}.",
        f"7.2. {anchor_label}: {join_anchors(norm_pool[:2], 125)} {anchor_action}.",
        f"7.3. {finding_label}: Für „{clean(fields[0][0] if fields else 'Fallkern', 55)}“ Tatsache, Datum und Fundstelle nennen.",
        f"7.4. Beweis: {evidence_short}. Offene Folgen aussprechen.",
        f"7.5. Gegenposition: Den stärksten Einwand fair und vollständig formulieren. Schwerpunkt: {attack_short}.",
        f"7.6. Erwiderung: {response_label} nennen und Restrisiko abstufen.",
        f"7.7. Ausgang: Das Arbeitsprodukt „{output_short}“ liefern; mit Frist, Kernlücke und {closing_label} schließen.",
        "",
        "## 8. Stop",
        "",
        f"Nur bei diesem Stop-Punkt unterbrechen: {clean(profile.stop[0], 170).rstrip('.') if profile.stop else 'Frist, Vollmacht, Zuständigkeit oder Kernbeleg sind ungeklärt'}. Sonst mit sichtbaren Lücken weiterarbeiten und den belastbaren Teil liefern. Für die Vertiefung dient die Werkstatt desselben Plugins.",
        "",
    ]
    text = sanitize("\n".join(lines).strip() + "\n")
    if byte_len(text) <= MAX_FAST:
        return text
    # Hard compact if needed.
    parts = re.split(r"\n## (?:6\.\s+)?Anker\n", text, maxsplit=1)
    if len(parts) == 2:
        head, rest = parts
        anchor, tail = re.split(r"\n## (?:7\.\s+)?Antwortform\n", rest, maxsplit=1)
        anchor_lines = [l for l in anchor.splitlines() if l.strip()][:8]
        text = head.rstrip() + "\n\n## 6. Anker\n\n" + "\n".join(anchor_lines) + "\n\n## 7. Antwortform\n" + tail
    return compact_schnellstart(text)


def write_readme_links(plugin_dir: Path) -> None:
    readme = plugin_dir / "README.md"
    if not readme.exists():
        return
    mf = manifest(plugin_dir)
    slug = mf.get("name") or plugin_dir.name
    raw_base = f"https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/{plugin_dir.relative_to(REPO).as_posix()}"
    block = "\n".join([
        "<!-- BEGIN werkstatt-schnellstart-raw-links (autogen) -->",
        "## Werkstatt- und Schnellstart-Prompts",
        "",
        "Diese Markdown-Prompts sind autarke Arbeitsfassungen fuer Nutzer, die das Plugin nicht installieren. Sie werden direkt als Markdown-Dateien geladen.",
        "",
        f'- Werkstatt-Prompt: <a href="{raw_base}/{slug}-werkstatt.md" download>{slug}-werkstatt.md</a>',
        f'- Schnellstart-Prompt: <a href="{raw_base}/{slug}-schnellstart.md" download>{slug}-schnellstart.md</a>',
        "",
        "<!-- END werkstatt-schnellstart-raw-links (autogen) -->",
    ])
    text = readme.read_text(encoding="utf-8", errors="ignore")
    pattern = r"<!-- BEGIN werkstatt-schnellstart-raw-links \(autogen\) -->[\s\S]*?<!-- END werkstatt-schnellstart-raw-links \(autogen\) -->"
    if re.search(pattern, text):
        text = re.sub(pattern, block, text)
    else:
        lines = text.splitlines()
        insert_at = 1 if lines and lines[0].startswith("# ") else 0
        lines[insert_at:insert_at] = ["", block, ""]
        text = "\n".join(lines) + "\n"
    readme.write_text(text, encoding="utf-8")


def ensure_title_first(text: str) -> str:
    """Verschiebt einen knappen Vorsatz hinter die erste H1-Überschrift."""

    lines = text.splitlines()
    title_index = next(
        (index for index, line in enumerate(lines) if line.startswith("# ")),
        None,
    )
    if not title_index:
        return text
    prefix = [line for line in lines[:title_index] if line.strip()]
    if not prefix or any(line.startswith(("---", "<!--")) for line in prefix):
        return text
    reordered = [lines[title_index], ""] + prefix + [""] + lines[title_index + 1 :]
    return "\n".join(reordered).rstrip() + "\n"


PROTECTED_DEPTH_SECTIONS: dict[
    str,
    tuple[str, tuple[tuple[str, tuple[str, ...]], ...]],
] = {
    "urteilsbauer-relationsmacher": (
        "Relationskern vom Parteivortrag bis zum Urteil",
        (
            (
                "Stationsprotokoll mit echten Entscheidungsweichen",
                (
                    "Führe für jeden Streitgegenstand ein eigenes Stationsprotokoll. Eine Zeile darf nur eine rechtliche Weiche enthalten; Anspruchsgrundlagen, Einreden, Aufrechnung und Widerklage werden nicht vermischt. Ausgangspunkt ist stets der zuletzt gestellte Antrag einschließlich Hilfsanträgen und Zinsbeginn.",
                    "| Station | Leitfrage | Mindestfundstelle | Lieferstück |\n| --- | --- | --- | --- |\n| Zulässigkeit | Kann und darf über genau diesen Antrag entschieden werden? | Antrag, Zustellung, Zuständigkeit, Prozessstand | Prozessvotum mit etwaiger Verweisung oder Teilentscheidung |\n| Klägerstation | Trägt der als wahr unterstellte Klägervortrag jedes Merkmal? | Schriftsatzseite und Anlage | Schlüssigkeitsmatrix ohne Beweiswürdigung |\n| Beklagtenstation | Welcher Vortrag ist erheblich, welches Bestreiten prozessual beachtlich? | Erwiderung, Replik, eigene Wahrnehmung | Erheblichkeits- und Bestreitensmatrix |\n| Beweisstation | Welche entscheidungserhebliche Tatsache ist offen und wer trägt die Beweislast? | Beweisantritt, Urkunde, Protokoll | Beweisfrage, Beweismittel, Ergebnis und Restzweifel |\n| Entscheidung | Welche Rechtsfolge folgt nach dem festgestellten Sachverhalt? | letzte Anträge und Feststellungen | Tenor, Gründe, Kosten, Vollstreckbarkeit und Rechtsmittelkontrolle |",
                ),
            ),
            (
                "Klägerstation ohne verdeckte Beweiswürdigung",
                (
                    "Zerlege jede Anspruchsgrundlage in Tatbestandsmerkmale und ordne jedem Merkmal eine konkrete Tatsachenbehauptung mit Fundstelle zu. Unterstelle den schlüssig vorgetragenen Sachverhalt zunächst als wahr. Fehlt ein Merkmal, formuliere den präzisen richterlichen Hinweis nach ZPO Paragraf 139 und benenne, welcher Vortrag oder Antrag die Lücke schließen könnte; erfinde die Ergänzung nicht selbst.",
                    "Trenne Anspruchsentstehung, Einwendungen gegen die Entstehung, rechtshemmende Einreden und Anspruchshöhe. Nebenforderungen erhalten eigene Zeilen für Verzug, Zinssatz, Zinsbeginn und vorgerichtliche Kosten. Bei mehreren Anträgen entsteht für jeden Antrag eine eigene Schlüssigkeitskette; eine tragende Norm darf nicht bloß genannt, sondern muss mit Tatsache und Rechtsfolge verbunden werden.",
                ),
            ),
            (
                "Beklagtenstation und prozessual wirksames Bestreiten",
                (
                    "Prüfe nach ZPO Paragraf 138 Absatz 2 bis 4 für jede klägerische Behauptung, ob sie zugestanden, substantiiert bestritten, mit Nichtwissen bestritten oder durch abweichenden Tatsachenvortrag beantwortet ist. Bestreiten mit Nichtwissen ist bei eigenen Handlungen und eigener Wahrnehmung unzulässig. Kennzeichne pauschales Bestreiten, widersprüchliche Einlassungen und verspäteten Vortrag, ohne daraus vorschnell eine materielle Beweislastumkehr abzuleiten.",
                    "Ordne Einreden wie Verjährung, Zurückbehaltung oder Anfechtung als eigene Verteidigungslinien. Sekundäre Darlegungslast verändert grundsätzlich nicht die materielle Beweislast: Halte deshalb getrennt fest, welche nähere Erklärung zumutbar ist, welcher Informationsvorsprung besteht und welche Folge nur aus unzureichender Erklärung gezogen werden darf. Liefere danach ein Votum: unerheblich, erheblich aber beweisbedürftig oder bereits unstreitig entscheidungsreif.",
                ),
            ),
            (
                "Beweisstation mit Beweisthema und Kontrollspur",
                (
                    "Bilde die Beweisstation ausschließlich aus streitigen, erheblichen Tatsachen. Für jede Tatsache stehen Behauptender, Beweisbelasteter, Beweisantritt, Beweisthema, Zulässigkeit, Ergiebigkeit und Ergebnis in einer Zeile. Urkunde, Zeuge, Sachverständiger, Augenschein und Parteivernehmung werden nach ihrem konkreten Beweiswert behandelt; ein Anlagenverweis ersetzt weder Tatsachenvortrag noch Beweisthema.",
                    "Würdige nach ZPO Paragraf 286 das gesamte Ergebnis der Verhandlung und Beweisaufnahme. Dokumentiere Glaubhaftigkeit der Aussage und Glaubwürdigkeit der Person getrennt, löse Widersprüche anhand benannter Anknüpfungstatsachen und gib an, weshalb eine Alternative ausscheidet oder als Restzweifel verbleibt. Bei non liquet folgt die Entscheidung aus der Beweislast; das Ergebnis darf nicht durch eine bloße Wahrscheinlichkeitsformel ersetzt werden.",
                ),
            ),
            (
                "Entscheidungsstation, Tenor und Rechtskraftumfang",
                (
                    "Leite die Entscheidungsstation aus den Ergebnissen der vorherigen Stationen ab. Prüfe die Bindung an die Anträge nach ZPO Paragraf 308, Teilurteil- und Zwischenentscheidungsrisiken, Aufrechnung, Erledigung, Klagerücknahme und Vergleich. Der Tenor muss vollstreckungsfähig sein: Hauptsache, Zinsen, Kosten, vorläufige Vollstreckbarkeit und gegebenenfalls Sicherheitsleistung werden getrennt und rechnerisch kontrolliert.",
                    "Baue die Gründe nach ZPO Paragraf 313 aus Antrag, tragendem Sachverhalt, Subsumtion und Rechtsfolge. Hilfsbegründungen werden nur aufgenommen, wenn sie prozessual sinnvoll sind. Prüfe abschließend, welche Entscheidung über welchen Streitgegenstand nach ZPO Paragraf 322 in Rechtskraft erwachsen kann und ob Tatbestand, Gründe und Tenor dieselben Parteien, Beträge, Zeiträume und Anträge verwenden.",
                ),
            ),
            (
                "Übergabepaket für Beratung, Kammer oder Geschäftsstelle",
                (
                    "Liefere je nach Auftrag eine Relation, ein Votum, einen Hinweis, einen Beweisbeschluss oder einen vollständigen Entscheidungsentwurf. Vorangestellt wird ein Einseiter mit Streitgegenständen, Entscheidungsweichen, Beweislast und offenem Punkt. Dahinter folgen Antragsmatrix, Parteivortrag mit Fundstellen, Beweisstation und ausformulierter Entscheidung; jede Zahl und jedes Datum muss aus der Akte rückverfolgbar sein.",
                    "Schließe mit einer Berufungsfestigkeitskontrolle: rechtliches Gehör, übergangener Antrag, übergangener Beweisantritt, widersprüchliche Feststellung, fehlende Begründung, Rechenfehler, Kostenquote, Vollstreckbarkeit und Rechtsmittelbelehrung. Offene Punkte werden als konkrete Verfügung oder Nachfrage formuliert, nicht als allgemeiner Vorbehalt.",
                ),
            ),
        ),
    ),
    "richter-familiengericht": (
        "Familiengerichtliche Verfahrenssteuerung",
        (
            (
                "Verfahrensspur und Beteiligtenstellung",
                (
                    "Ordne jeden Antrag zuerst als Ehe-, Familienstreit-, Kindschafts-, Abstammungs-, Gewaltschutz- oder Versorgungsausgleichssache ein. Halte Zuständigkeit, Beteiligte, notwendige Anhörungen, Verfahrensbeistand, Jugendamt, Frist und mögliche Eilspur in einem Verfahrensblatt fest. Amtsermittlung nach FamFG Paragraf 26 ersetzt weder einen bestimmten Antrag in Familienstreitsachen noch die saubere Dokumentation streitiger Tatsachen.",
                    "Liefere als ersten Baustein eine verfahrensleitende Verfügung mit Zustellung, Erwiderungsfrist, Anhörung, Aktenbeiziehung und konkretem Hinweis. Prüfe vor jeder Sachentscheidung, ob rechtliches Gehör gewährt und das Ergebnis der Ermittlungen nach FamFG Paragraf 37 zur Stellungnahme zugänglich gemacht wurde.",
                ),
            ),
            (
                "Kindeswohl, Anhörung und Vollziehbarkeit",
                (
                    "In Kindschaftssachen trenne beobachtete Tatsachen, Angaben der Eltern, kindliche Äußerungen, Jugendamtsbefund und sachverständige Schlussfolgerung. Formuliere für persönliche Anhörung und Erörterung offene, altersangemessene Fragen. Eine Umgangs- oder Sorgeregelung muss Übergabeort, Zeiten, Ferien, Kommunikation, Ausfall, Nachholung und Konfliktmechanismus so konkret bestimmen, dass Beteiligte und Vollstreckungsorgan sie verstehen.",
                    "Bei Eilbedarf benenne drohenden Nachteil, zeitliche Dringlichkeit, vorläufigen Regelungsbedarf und noch offene Hauptsachenaufklärung getrennt. Der Beschluss enthält Tenor, wesentliche tatsächliche Grundlage, Abwägung, Kosten, Wirksamkeit und Rechtsmittelbelehrung; nicht tragfähige Aktenannahmen bleiben ausdrücklich offen.",
                ),
            ),
            (
                "Unterhalt, Zugewinn und Versorgungsausgleich",
                (
                    "Rechne Unterhalt monatsgenau mit Einkommen, Bereinigung, Bedarf, Rang, Leistungsfähigkeit, Zahlbetrag und bereits erbrachter Leistung. Zugewinn erhält Stichtagsblätter für Anfangs-, Trennungs- und Endvermögen samt Bewertung und Beleg. Im Versorgungsausgleich werden Ehezeit, Versorgungsträger, Anrecht, Auskunftsstand, Teilungsart und Ausgleichswert je Anrecht kontrolliert.",
                    "Jede Rechenannahme verweist auf ein Aktenstück. Fehlende Steuerbescheide, Lohnabrechnungen, Kontoauszüge, Depotstände oder Versorgungsauskünfte führen zu einer bestimmten Nachforderungsverfügung. Das Ergebnis wird als nachvollziehbare Tabelle und als ausformulierter Beschlussbaustein geliefert.",
                ),
            ),
        ),
    ),
    "staatsanwaltschaft-amtsanwaltschaft": (
        "Abschlussreife staatsanwaltschaftliche Aktenarbeit",
        (
            (
                "Zuständigkeit, Übertragungsplan und Vorlagepflicht",
                (
                    "Prüfe vor der Sachbearbeitung GVG Paragraf 142, den Geschäftsverteilungs- und Übertragungsplan des Landes sowie interne Vorlagepflichten. Die amtsgerichtliche Zuständigkeit allein beweist noch nicht, dass der Vorgang dem Amtsanwalt übertragen ist. Schwierige Rechtsfragen, besondere Bedeutung, umfangreiche Vermögensabschöpfung oder eine Zuständigkeit außerhalb der übertragenen Materie werden mit kurzem Vorlagevermerk an den Staatsanwalt gegeben.",
                    "Der Zuständigkeitsvermerk nennt Tatvorwurf, voraussichtliches Gericht, besondere Verfahrenslage, Übertragungsgrundlage und Entscheidung über Eigenbearbeitung oder Vorlage. Erst danach beginnt die materielle Abschlussprüfung.",
                ),
            ),
            (
                "Ermittlungsplan bis zur Abschlussverfügung",
                (
                    "Ordne jedes Tatbestandsmerkmal einer belastenden und einer entlastenden Tatsache zu. Nach StPO Paragraf 160 sind beide Richtungen aufzuklären. Jede Ermittlungsmaßnahme erhält Beweisthema, Rechtsgrundlage, Verhältnismäßigkeit, Zuständigkeit, Frist und erwarteten Rücklauf; Vorratsmaßnahmen ohne erkennbare Entscheidungserheblichkeit unterbleiben.",
                    "Die Abschlussmatrix unterscheidet Anfangsverdacht, hinreichenden Tatverdacht und gerichtliche Verurteilungsprognose. Liefere danach genau eines der passenden Produkte: Nachermittlungsverfügung, Einstellung nach StPO Paragraf 170 Absatz 2 mit Mitteilung, Opportunitätsentscheidung mit Zustimmungen, Strafbefehlsantrag oder Anklageschrift nach StPO Paragraf 200.",
                ),
            ),
            (
                "Sitzungsdienst und Rechtsmittelanschluss",
                (
                    "Erstelle einen Sitzungszettel mit Personalien, Anklagesatz, Beweismitteln, Widersprüchen, zulässigen Fragen, Einziehungsfragen und Strafzumessungstatsachen. Der Schlussvortrag leitet Schuldspruch und Rechtsfolge aus dem tatsächlichen Ergebnis der Hauptverhandlung ab; er übernimmt nicht unbesehen die Ermittlungsakte.",
                    "Nach Verkündung folgen Abweichungsvermerk, Rechtsmittelprüfung, Fristnotiz und gegebenenfalls Vollstreckungsanschluss. Bei Ordnungswidrigkeiten richtet sich die Rechtsfolge nach der einschlägigen Bußgeldnorm und nur gegebenenfalls nach einem Bußgeldkatalog; eine pauschale Katalogannahme genügt nicht.",
                ),
            ),
        ),
    ),
    "arbeitsrecht": (
        "Arbeitsrechtliche Fristen-, Beweis- und Produktsteuerung",
        (
            (
                "Bestandsschutz und prozessuale Sofortspur",
                (
                    "Erfasse Zugang, Kündigungsart, Kündigungsschreiben, Vertretung, Betriebsratsanhörung, Sonderkündigungsschutz und Klagefrist in einer Chronologie. KSchG Paragraf 4 und Paragraf 7 werden als harte Wirksamkeitsweiche behandelt; bei Befristung wird die Frist nach TzBfG Paragraf 17 gesondert gerechnet. Unklare Zugangszeitpunkte erhalten Beweisangebote und Alternativberechnungen.",
                    "Liefere sofort einen Klage- oder Erwiderungsbaustein mit richtigen Anträgen, Beschäftigungsbezug und Fristenblatt. Abfindung, Weiterbeschäftigung, Annahmeverzug und Zeugnis werden als eigene Regelungspunkte geführt, nicht in einem pauschalen Vergleichsbetrag versteckt.",
                ),
            ),
            (
                "Vergütung, Arbeitszeit und Darlegungslast",
                (
                    "Baue für Vergütung, Überstunden, Bonus, Provision und Entgeltfortzahlung eine Monatsmatrix aus Soll, Ist, Anspruchsgrund, Einwendung, Ausschlussfrist und Beleg. Parteivortrag, primäre Darlegungslast und mögliche sekundäre Erklärungspflicht bleiben getrennt. Schätzungen werden nur mit benannten Anknüpfungstatsachen verwendet.",
                    "Das Lieferstück enthält eine nachrechenbare Forderungsaufstellung, einen Tatsachenvortrag mit Beweisangeboten und eine Gegenrechnung aus Arbeitgebersicht. Tarifbindung, Bezugnahmeklausel, Betriebsvereinbarung und einzelvertragliche Regelung werden in ihrer Rangfolge geprüft.",
                ),
            ),
            (
                "Betriebsverfassung, Verhandlung und Vergleich",
                (
                    "Halte Beteiligungsrecht, auslösende Maßnahme, Information, Frist, Beschlusslage und Rechtsfolge je Vorgang fest. Bei Kündigungen wird die Anhörung nach BetrVG Paragraf 102 anhand der tatsächlich mitgeteilten Gründe geprüft. Bei personellen oder kollektiven Maßnahmen werden Verfahren und Individualanspruch nicht vermischt.",
                    "Entwickle einen Vergleichskorridor mit wirtschaftlichem Wert, steuerbarer Fälligkeit, Freistellung, Zeugnis, Rückgabe, Ausgleichsklausel und Erledigung. Jede Klausel erhält Ziel, Risiko, Rückfallposition und Vollzugsschritt; danach entsteht ein protokollfähiger Gesamttext.",
                ),
            ),
        ),
    ),
    "mietrecht": (
        "Mietrechtliche Akten- und Berechnungstiefe",
        (
            (
                "Mangel, Miete und Kündigungsfolge",
                (
                    "Erstelle für jeden Mangel eine Zeitachse aus Auftreten, Anzeige nach BGB Paragraf 536c, Kenntnis, Besichtigung, Ursache, Gebrauchsbeeinträchtigung, Abhilfe und Zahlung. Minderungsquote, Zurückbehaltung, Vorschuss und Schadensersatz werden rechtlich und rechnerisch getrennt. Fotos und Messwerte erhalten Datum, Raum, Urheber und Zuordnung zum behaupteten Zustand.",
                    "Bei Kündigung prüfe Vertrag, Partei, Vollmacht, Form nach BGB Paragraf 568, Kündigungsgrund, Abmahnung, Frist, Zugang, Heilung und Widerspruch. Das Lieferstück ist eine vollständige Zahlungs- und Kündigungsmatrix samt Klage-, Erwiderungs- oder Vergleichsbaustein.",
                ),
            ),
            (
                "Mieterhöhung, Modernisierung und Betriebskosten",
                (
                    "Trenne Vergleichsmietenerhöhung, Modernisierung und Betriebskostenabrechnung nach Rechtsgrundlage, Bezugszeitraum, formeller Erläuterung, Berechnungswert und Einwendung. Jede Zahl wird auf Mietvertrag, Abrechnung, Beleg oder Ankündigung zurückgeführt. Fehlende Belege führen zu einer bestimmten Einsichts- oder Nachforderungsliste.",
                ),
            ),
        ),
    ),
    "anlagen-zu-schriftsaetzen": (
        "Anlagenpaket mit gerichtsfester Kontrollspur",
        (
            (
                "Inventar, Fundstelle und Anlagenbezug",
                (
                    "Erfasse jede Eingangsdatei mit Originalname, Dokumentart, Datum, Aussteller, Seitenzahl, Lesbarkeit, Dublette und behaupteter Beweisfunktion. Ordne erst danach K-, B- oder sonstige Anlagenbezeichnungen zu. Jede Anlage muss im Schriftsatz an einer konkreten Tatsachenbehauptung eingeführt werden; ein bloßes Anlagenverzeichnis ersetzt den Sachvortrag nicht.",
                    "Liefere ein Anlagenregister mit Schriftsatzfundstelle, Anlagenbezeichnung, Zieldateiname und offenem Bearbeitungsschritt. Fehlende Seiten, unklare Reihenfolge und widersprüchliche Fassungen werden vor der Konvertierung geklärt.",
                ),
            ),
            (
                "Konvertierung, Stempelung und Sichtprüfung",
                (
                    "Wandle Office-Dateien, E-Mails, Bilder und sonstige Eingänge in lesbare, durchsuchbare PDFs um, ohne Inhalt oder Seitenfolge zu verändern. Setze die Anlagenbezeichnung zurückhaltend außerhalb relevanter Inhalte und kontrolliere jede Seite visuell auf Beschnitt, Drehung, Skalierung, leere Seiten, Schriftverlust und verdeckte Unterschriften.",
                    "Prüfe anschließend Dateiname, Anlagenfolge, Seitenzahl, Öffnbarkeit und Übereinstimmung mit dem Register. Aktuelle Übermittlungs- und Formatvorgaben werden unmittelbar vor Versand anhand der maßgeblichen amtlichen Quelle kontrolliert.",
                ),
            ),
        ),
    ),
}


def protected_depth_lines(slug: str, top_number: int) -> list[str]:
    configured = PROTECTED_DEPTH_SECTIONS.get(slug)
    if not configured:
        return []
    title, sections = configured
    lines = [f"## {top_number}. {title}", ""]
    for index, (section_title, paragraphs) in enumerate(sections, 1):
        lines += [f"### {top_number}.{index}. {section_title}", ""]
        for paragraph in paragraphs:
            lines += paragraph.splitlines() + [""]
    return lines


def enrich_protected_werkstatt(plugin_dir: Path) -> bool:
    """Ergänzt Fachrouten, ohne den handkuratierten Haupttext zu ersetzen."""

    mf = manifest(plugin_dir)
    slug = mf.get("name") or plugin_dir.name
    path = plugin_dir / f"{slug}-werkstatt.md"
    if not path.exists():
        return False
    text = path.read_text(encoding="utf-8", errors="ignore")
    begin = "<!-- BEGIN fachrouten-werkstatt (autogen) -->"
    end = "<!-- END fachrouten-werkstatt (autogen) -->"
    text = re.sub(
        rf"\n*{re.escape(begin)}[\s\S]*?{re.escape(end)}\n*",
        "\n",
        text,
        count=1,
    ).rstrip()
    if slug in {"bautraegervertrag-pruefer", "urteilsbauer-relationsmacher"}:
        text = remove_h2_section(text, "Materienbezogene Arbeitsfelder").rstrip()
    text = ensure_title_first(prose_umlauts(text))
    text = renumber_h2_sections(text).rstrip()
    skill_material = collect_skill_material(plugin_dir)
    context = " ".join(
        [mf.get("description", ""), first_readme_paragraph(plugin_dir)]
        + [item.get("desc", "") for item in skill_material[:20]]
    )
    profile = profile_for(slug, context)
    routes = practice_routes(profile, skill_material, 12, plugin_slug=slug)
    if not routes:
        return False
    number = next_top_level_number(text)
    route_lines = practice_routes_lines(routes, number)
    route_lines += protected_depth_lines(slug, number + 1)
    route_text = sanitize("\n".join(route_lines)).rstrip()
    block = f"{begin}\n{route_text}\n{end}"
    updated = text + "\n\n" + block + "\n"
    if updated == path.read_text(encoding="utf-8", errors="ignore"):
        return False
    path.write_text(updated, encoding="utf-8")
    return True


def normalize_protected_schnellstart(plugin_dir: Path) -> bool:
    """Normalisiert Gliederung und Prosa, ohne handkuratierten Inhalt zu ersetzen."""

    mf = manifest(plugin_dir)
    slug = mf.get("name") or plugin_dir.name
    path = plugin_dir / f"{slug}-schnellstart.md"
    if not path.exists():
        return False
    before = path.read_text(encoding="utf-8", errors="ignore")
    updated = ensure_title_first(prose_umlauts(before))
    updated = re.sub(
        r"\n+Bedienregel: [^\n]*\n+",
        "\n\n",
        updated,
        count=1,
    )
    skill_material = collect_skill_material(plugin_dir)
    context = " ".join(
        [mf.get("description", ""), first_readme_paragraph(plugin_dir)]
        + [item.get("desc", "") for item in skill_material[:20]]
    )
    profile = profile_for(slug, context)
    fields = profile_fields(profile, skill_material)
    field_names = [clean(field, 42).rstrip(".") for field, _detail in fields[:2]]
    if not field_names:
        field_names = [clean(profile.label, 42).rstrip(".")]
    routes = " und ".join(field_names)
    guide = (
        "Bedienregel: Dateien und Ordner zuerst lesen. Konkrete Aufträge beginnen sofort "
        "mit dem verlangten Dokument. Bei bloßer Aktivierung selbst zu "
        f"{routes} routen. Große Ordner liefern früh einen Teilstand und nennen offene "
        "Dateien. Ohne Material höchstens eine gebündelte Frage. Folgewünsche setzen ohne "
        "Neustart auf dem Stand auf; passende Fachskills laufen intern."
    )
    title_end = updated.find("\n")
    if title_end == -1:
        updated = updated + "\n\n" + guide + "\n"
    else:
        title = updated[:title_end].rstrip()
        body = updated[title_end + 1 :].lstrip("\n")
        updated = title + "\n\n" + guide + "\n\n" + body
    updated = renumber_h2_sections(updated)
    if byte_len(updated) >= 7500:
        raise ValueError(f"{slug}: handkuratierter Schnellstart hat {byte_len(updated)} Bytes")
    if updated == before:
        return False
    path.write_text(updated, encoding="utf-8")
    return True


def main() -> int:
    dirs = plugin_dirs()
    protected = load_protected()
    written = 0
    skipped = 0
    skipped_slugs: list[str] = []
    problems: list[str] = []
    for plugin_dir in dirs:
        mf = manifest(plugin_dir)
        slug = mf.get("name") or plugin_dir.name
        if slug in protected:
            # Der Haupttext bleibt handkuratiert. Nur der klar markierte,
            # fachmaterialspezifische Vertiefungsblock wird reproduzierbar ergänzt.
            written += int(enrich_protected_werkstatt(plugin_dir))
            written += int(normalize_protected_schnellstart(plugin_dir))
            skipped += 1
            skipped_slugs.append(slug)
            continue
        skill_material = collect_skill_material(plugin_dir)
        werkstatt = build_werkstatt(plugin_dir, skill_material)
        schnell = build_schnellstart(plugin_dir, skill_material)
        if byte_len(schnell) > MAX_FAST:
            problems.append(f"{slug}: Schnellstart {byte_len(schnell)} Bytes")
        (plugin_dir / f"{slug}-werkstatt.md").write_text(werkstatt, encoding="utf-8")
        (plugin_dir / f"{slug}-schnellstart.md").write_text(schnell, encoding="utf-8")
        written += 2
    if problems:
        print("Probleme:")
        for p in problems:
            print("-", p)
        return 1
    if skipped_slugs:
        print("Handkuratiert, uebersprungen: " + ", ".join(sorted(skipped_slugs)))
    print(f"geschrieben: {written}, uebersprungen: {skipped}, Probleme: keine")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
