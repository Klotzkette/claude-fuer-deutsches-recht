"""Vektor-Briefpapier der Absender in der ModeFuchs-Akte (Maße in PDF-Punkten)."""

from reportlab.lib import colors

BRANDS = {
    "modefuchs": ("ModeFuchs GmbH", "#352826", "#AB512F"),
    "inkasso": ("InkassoZentrale GmbH", "#17394D", "#287C80"),
    "kanzlei": ("Kanzlei Brezelmann & Collegen", "#302D32", "#854A49"),
    "bank": ("Musterbank Nürnberg", "#203E39", "#52766B"),
}
DARK = "#30373B"
GREY = "#586065"
PALE = "#C8CDCC"


def _ink(canvas, value):
    canvas.setFillColor(colors.HexColor(value))


def _rule(canvas, x1, x2, y, value, thickness=0.5):
    canvas.setStrokeColor(colors.HexColor(value))
    canvas.setLineWidth(thickness)
    canvas.line(x1, y, x2, y)


def _fox(canvas):
    # Sitzende Fähe im Profil, mit heller Schwanzspitze und abgesetzter Brust.
    _ink(canvas, "#AB512F")
    path = canvas.beginPath()
    path.moveTo(5.1, 27.8)
    path.curveTo(4.1, 19.7, 6.5, 14.0, 12.1, 11.5)
    path.curveTo(12.1, 18.6, 15.3, 23.1, 21.0, 26.4)
    path.lineTo(20.6, 37.3)
    path.lineTo(27.0, 33.4)
    path.lineTo(32.1, 39.2)
    path.lineTo(32.8, 32.0)
    path.curveTo(35.0, 30.2, 36.0, 28.0, 41.9, 26.5)
    path.curveTo(40.0, 23.7, 36.5, 22.8, 33.0, 22.9)
    path.curveTo(29.6, 18.7, 29.8, 12.0, 33.0, 6.6)
    path.curveTo(34.2, 5.2, 36.0, 5.7, 36.4, 3.7)
    path.lineTo(19.5, 3.7)
    path.curveTo(5.9, 3.8, 0.3, 13.9, 5.1, 27.8)
    path.close()
    canvas.drawPath(path, fill=1, stroke=0)

    _ink(canvas, "#F7E5CC")
    fur = canvas.beginPath()
    fur.moveTo(5.1, 27.8)
    fur.curveTo(3.5, 23.0, 2.9, 18.8, 3.4, 16.1)
    fur.lineTo(4.9, 17.8)
    fur.lineTo(5.1, 15.9)
    fur.lineTo(6.9, 17.1)
    fur.lineTo(7.2, 15.9)
    fur.lineTo(8.4, 16.6)
    fur.curveTo(6.4, 19.4, 5.0, 23.8, 5.1, 27.8)
    fur.close()
    canvas.drawPath(fur, fill=1, stroke=0)

    chest = canvas.beginPath()
    chest.moveTo(39.8, 25.3)
    chest.curveTo(36.6, 24.2, 33.1, 25.0, 29.2, 26.2)
    chest.curveTo(30.9, 24.9, 30.9, 24.0, 31.3, 23.2)
    chest.lineTo(28.7, 23.8)
    chest.curveTo(29.9, 21.6, 29.6, 18.5, 30.0, 16.4)
    chest.curveTo(30.5, 19.3, 31.4, 21.1, 33.0, 22.9)
    chest.curveTo(35.5, 22.6, 38.5, 23.6, 39.8, 25.3)
    chest.close()
    canvas.drawPath(chest, fill=1, stroke=0)

    _ink(canvas, "#422F2A")
    nose = canvas.beginPath()
    nose.moveTo(39.1, 27.3)
    nose.lineTo(42.2, 26.5)
    nose.lineTo(40.4, 24.9)
    nose.close()
    canvas.drawPath(nose, fill=1, stroke=0)
    canvas.circle(33.9, 28.7, 0.7, stroke=0, fill=1)


def _iz(canvas):
    # Die Negativform des Z bleibt auch im Schwarzweiß-Ausdruck sichtbar.
    _ink(canvas, "#17394D")
    canvas.roundRect(2, 4, 35, 34, 2, stroke=0, fill=1)
    _ink(canvas, "#FFFFFF")
    canvas.rect(8, 11, 3.1, 19, stroke=0, fill=1)
    zed = canvas.beginPath()
    zed.moveTo(15, 30)
    zed.lineTo(31.4, 30)
    zed.lineTo(31.4, 27.3)
    zed.lineTo(19.8, 14)
    zed.lineTo(31.4, 14)
    zed.lineTo(31.4, 11)
    zed.lineTo(15, 11)
    zed.lineTo(15, 13.7)
    zed.lineTo(26.5, 27)
    zed.lineTo(15, 27)
    zed.close()
    canvas.drawPath(zed, fill=1, stroke=0)
    _ink(canvas, "#287C80")
    canvas.rect(38.5, 4, 2.3, 34, stroke=0, fill=1)


def _bc(canvas):
    # Zwei gezeichnete Initialen: durchgehender Stamm des B, offener Bogen des C.
    canvas.setLineCap(1)
    canvas.setLineWidth(1.7)
    canvas.setStrokeColor(colors.HexColor("#302D32"))
    bee = canvas.beginPath()
    bee.moveTo(4, 7)
    bee.lineTo(12, 7)
    bee.curveTo(24.2, 7, 25.1, 20.2, 14, 21.6)
    bee.curveTo(23.4, 23.3, 22.9, 34, 12.8, 34)
    bee.lineTo(4, 34)
    bee.moveTo(8, 34)
    bee.lineTo(8, 7)
    bee.moveTo(8, 21.4)
    bee.lineTo(13.4, 21.4)
    canvas.drawPath(bee)
    canvas.setStrokeColor(colors.HexColor("#854A49"))
    cee = canvas.beginPath()
    cee.moveTo(37.8, 29.3)
    cee.curveTo(29, 33.7, 22.8, 26.2, 22.8, 17.6)
    cee.curveTo(22.8, 8.1, 30.5, 4.1, 38, 10.4)
    canvas.drawPath(cee)


def _bank(canvas):
    # Gefaltetes Kontoblatt mit zwei Falzen.
    for x, top, color in [(3, 26, "#52766B"), (13, 31, "#385D53"), (23, 36, "#203E39")]:
        _ink(canvas, color)
        flap = canvas.beginPath()
        flap.moveTo(x, 8)
        flap.lineTo(x, top)
        flap.lineTo(x + 9, top + 4.5)
        flap.lineTo(x + 9, 12.5)
        flap.close()
        canvas.drawPath(flap, stroke=0, fill=1)


def draw_signet(canvas, sender="modefuchs", x=0, y=0, scale=1.0):
    """Zeichnet nur das Zeichen in eine transparente Fläche von 44 × 42 pt."""
    canvas.saveState()
    canvas.translate(x, y)
    canvas.scale(scale, scale)
    {"modefuchs": _fox, "inkasso": _iz, "kanzlei": _bc, "bank": _bank}[sender](canvas)
    canvas.restoreState()


def draw_brand(canvas, sender, x, y, scale=1.0, label=None):
    """Zeichnet die Wortbildmarke (max. 235 × 42 pt) ab der linken unteren Ecke."""
    name, ink, _ = BRANDS[sender]
    canvas.saveState()
    canvas.translate(x, y)
    canvas.scale(scale, scale)
    draw_signet(canvas, sender)
    typeface, size = {
        "modefuchs": ("Times-Bold", 21),
        "inkasso": ("Helvetica-Bold", 16.2),
        "kanzlei": ("Times-Roman", 14.2),
        "bank": ("Helvetica", 17),
    }[sender]
    _ink(canvas, ink)
    canvas.setFont(typeface, size)
    canvas.drawString(48, 21 - size * 0.31, label or name)
    canvas.restoreState()


def _write(canvas, x, y, text, font, size, color):
    _ink(canvas, color)
    canvas.setFont(font, size)
    canvas.drawString(x, y, text)


def draw_letterhead(canvas, *, sender, page_number, page_count, page_size, document_kind, header_lines):
    """Ersetzt den Originalkopf; Adressfenster und Textkörper zeichnet der Aufrufer."""
    width, height = page_size
    left, right = 77, width - 77
    lines = tuple(header_lines)
    canvas.saveState()
    if page_number > 1:
        name, ink, _ = BRANDS.get(sender, ("", DARK, PALE))
        _write(canvas, left, height - 41, name, "Helvetica", 9, ink)
        _rule(canvas, left, right, height - 49, PALE)
    elif document_kind == "email":
        # Druckansicht des Postfachs: unabhängig vom Absender der E-Mail.
        canvas.setLineWidth(1)
        canvas.setStrokeColor(colors.HexColor(GREY))
        y = height - 68
        canvas.rect(left, y, 16, 11)
        fold = canvas.beginPath()
        fold.moveTo(left, y + 11)
        fold.lineTo(left + 8, y + 4.5)
        fold.lineTo(left + 16, y + 11)
        canvas.drawPath(fold)
        _write(canvas, left + 26, y, lines[0], "Helvetica-Bold", 14, DARK)
        for index, line in enumerate(lines[1:]):
            _write(canvas, left, y - 12 - 9 * index, line, "Helvetica", 8, GREY)
        _rule(canvas, left, right, height - 91, PALE)
    elif document_kind == "register":
        # Titel und Geschäftszeichen entsprechen dem bestehenden Aktenverzeichnis.
        _rule(canvas, left, right, height - 44, DARK, 1.2)
        _write(canvas, left, height - 71, lines[0], "Times-Bold", 18, DARK)
        for index, line in enumerate(lines[1:]):
            _write(canvas, left, height - 92 - 11 * index, line, "Helvetica", 9, GREY)
    else:
        _, ink, accent = BRANDS[sender]
        # Im Geschäftsbrief tritt die Marke stärker hervor als in Vermerk und Schriftsatz.
        scale = 0.88 if document_kind in ("prozess", "intern") else 1.08
        draw_brand(canvas, sender, left, height - 84, scale, label=lines[0])
        _rule(canvas, left, right, height - 99, PALE)
        _rule(canvas, left, left + 34, height - 99, accent, 1.7)
        # Anschrift unter dem Logo, Geschäfts- und Zahlungsangaben im Fuß des Blatts.
        header_count = 3 if sender == "kanzlei" else 2
        for index, line in enumerate(lines[1:header_count]):
            _write(canvas, left, height - 113 - index * 12, line, "Helvetica", 8.6, ink)
        footer = lines[header_count:]
        if footer:
            _rule(canvas, left, right, 55, PALE)
            for index, line in enumerate(footer):
                _write(canvas, left, 42 - index * 10.4, line, "Helvetica", 7.4, GREY)
    if page_count > 1:
        canvas.setFont("Helvetica", 7.5)
        _ink(canvas, GREY)
        canvas.drawRightString(right, 24, f"Seite {page_number} von {page_count}")
    canvas.restoreState()
