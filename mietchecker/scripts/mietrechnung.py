#!/usr/bin/env python3
"""Reine Rechenhilfe. Keine automatische Feststellung der geschuldeten Miete."""
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP


def number(value):
    if isinstance(value, bool):
        raise ValueError("Boolescher Wert ist keine Zahl.")
    try:
        result = Decimal(str(value))
    except (InvalidOperation, ValueError) as exc:
        raise ValueError("Dezimalzahl mit Punkt erwartet.") from exc
    if not result.is_finite():
        raise ValueError("Endliche Zahl erwartet.")
    return result


def euro(value):
    return number(value).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def berlin(lower, middle, upper, groups):
    """Fünf bereits fachlich bewertete Gruppen: -1, 0 oder 1."""
    low, mid, high = map(number, (lower, middle, upper))
    if not Decimal(0) <= low <= mid <= high:
        raise ValueError("Geordnete, nichtnegative Spanne erwartet.")
    if len(groups) != 5 or any(type(x) is not int or x not in (-1, 0, 1) for x in groups):
        raise ValueError("Genau fünf belegte Gruppensalden erwartet; unbekannt ist nicht null.")
    score = sum(groups)
    halfspan = high - mid if score >= 0 else mid - low
    return euro(mid + halfspan * Decimal(score) / Decimal(5))


def regensburg(base, percentages):
    """Belegte Prozentpunkte addieren; keine Merkmalsauswahl durch das Skript."""
    rate = number(base)
    if rate <= 0:
        raise ValueError("Positive Basismiete erwartet.")
    values = [number(x) for x in percentages]
    if not values:
        raise ValueError("Belegte Zuschlagsliste erforderlich; bewusst neutral als [0].")
    factor = Decimal(1) + sum(values, Decimal(0)) / Decimal(100)
    if factor <= 0:
        raise ValueError("Zu- und Abschläge ergeben keinen positiven Mietwert.")
    return euro(rate * factor)


def monthly(rate, area):
    """Monatssumme aus bereits gerundetem Quadratmeterwert."""
    area = number(area)
    if area <= 0 or number(rate) < 0:
        raise ValueError("Positive Fläche und nichtnegative Miete erwartet.")
    return euro(euro(rate) * area)


def initial_basic_limit(comparable):
    """Grundrechnung plus zehn Prozent; Ausnahmen werden hier NICHT geprüft."""
    value = number(comparable)
    if value < 0:
        raise ValueError("Nichtnegative Vergleichsmiete erwartet.")
    return euro(value * Decimal("1.10"))


def increase_ceiling(comparable, period_base, cap_percent):
    """Nur Betragsgrenzen; Zeit, Form, Mietverlauf und Anspruch bleiben extern."""
    value, base, cap = map(number, (comparable, period_base, cap_percent))
    if value < 0 or base <= 0 or cap not in (Decimal(15), Decimal(20)):
        raise ValueError("Vergleichsmiete, positive Ausgangsmiete und 15 oder 20 Prozent erwartet.")
    return min(euro(value), euro(base * (Decimal(1) + cap / Decimal(100))))
