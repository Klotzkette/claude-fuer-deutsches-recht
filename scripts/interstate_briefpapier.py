"""Absender der fiktiven NL-West-Akten für Brief-, Tabellen- und Mailansichten."""
import re

AG = "Deutsche Interstate AG"
AMT = "384C64"
KANZLEI = "624354"
FIRMA = "2C6155"
# Eigenständige Wortmarkenfarben der fiktiven Korrespondenzpartner.
FIRMENFARBEN = {
    "Albumstrom Archivdienst GmbH": "52436A",
    "Lichtfaden Medienregister eG": "9A4F24",
    "Büro Kreidebogen": "4C585A",
    "Flutzeichen Messtechnik GmbH": "135D79",
    "Saumkante Beschichtung OHG": "855122",
    "Hublast West GmbH": "694928",
    "Steinbogen Ingenieurbau GmbH": "3A5571",
    "Tiefbau Wiesenfeld GmbH": "674934",
    "Trassenschrift Ingenieure GmbH": "5F596E",
    "Talbogen Straßenbau GmbH": "704239",
    "Linienwerk Edera GmbH": "755221",
    "Planquell Systeme GmbH": "264A78",
}


def letterhead(doc):
    """Ermittelt Name und Organisationseinheit aus der ausgewiesenen Urheberschaft."""
    person, _, unit = doc["von"].partition(" · ")
    if person == "Landgericht Essen":
        return person, unit, AMT
    if person == "Vergabeplattform":
        return person, unit, "465D70"
    if "Vergabekammer des Bundes" in unit:
        return "Vergabekammer des Bundes", "", AMT
    if "Kanzlei " in unit:
        firm = unit[unit.index("Kanzlei "):].split(",", 1)[0].split(" für ", 1)[0]
        return firm, "", KANZLEI
    if unit.startswith("Bevollmächtigter der "):
        return unit, "", KANZLEI
    for organisation in ("Stadt Borken", "Kreis Borken", "Fachkreis Markierung West"):
        if organisation in unit:
            return organisation, unit.removeprefix(organisation).strip(", "), AMT
    for field in unit.split(", "):
        if re.search(r'\b(?:GmbH|OHG|KG|eG)\b', field) or field == "Büro Kreidebogen":
            department = ", ".join(part for part in unit.split(", ") if part != field)
            return field, department, FIRMENFARBEN.get(field, FIRMA)
    if not unit and person in {"Zentrale Poststelle West", "Öffnungsteam West"}:
        unit = person
    unit = unit.replace(AG, "").replace("Niederlassung West", "").replace("NL West", "")
    return AG, unit.strip(", ") or "Niederlassung West", "174A61"
