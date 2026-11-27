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
    # Ein gewebtes Halstuch betont die Schulterlinie und die aufrechte Silhouette.
    _ink(canvas, "#633829")
    scarf = canvas.beginPath()
    scarf.moveTo(18.6, 24.8)
    scarf.curveTo(23, 23.0, 27.2, 21.7, 30.7, 22.0)
    scarf.lineTo(30.0, 20.6)
    scarf.curveTo(26, 20.1, 22.3, 21.0, 18.9, 22.6)
    scarf.lineTo(14.1, 17.5)
    scarf.lineTo(15.0, 21.7)
    scarf.close()
    canvas.drawPath(scarf, fill=1, stroke=0)
    canvas.setStrokeColor(colors.HexColor("#C97449"))
    canvas.setLineWidth(0.8)
    tail = canvas.beginPath()
    tail.moveTo(7.0, 12.0)
    tail.curveTo(10.1, 8.2, 16.8, 7.1, 21.8, 9.0)
    canvas.drawPath(tail)


def _iz(canvas):
    # Die Negativform des Z bleibt auch im Schwarzweiß-Ausdruck sichtbar.
    _ink(canvas, "#17394D")
    folder = canvas.beginPath()
    folder.moveTo(2, 4)
    folder.lineTo(2, 37.5)
    folder.lineTo(28, 37.5)
    folder.lineTo(37, 28.5)
    folder.lineTo(37, 4)
    folder.close()
    canvas.drawPath(folder, stroke=0, fill=1)
    _ink(canvas, "#72B6AE")
    fold = canvas.beginPath()
    fold.moveTo(28, 37.5)
    fold.lineTo(28, 29)
    fold.lineTo(36.5, 29)
    fold.close()
    canvas.drawPath(fold, stroke=0, fill=1)
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
    canvas.rect(2, 2, 35, 1.5, stroke=0, fill=1)


def _bc(canvas):
    _ink(canvas, "#F3EEEA")
    canvas.roundRect(0.7, 0.8, 41, 40, 2.0, fill=1, stroke=0)
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


def _block(canvas, x, y, width, height, color):
    _ink(canvas, color)
    canvas.rect(x, y, width, height, fill=1, stroke=0)


def _footer(canvas, lines, left, right, accent, tinted):
    if not lines:
        return
    _block(canvas, left - 8, 18, 2.2, 29, accent)
    _rule(canvas, left, right, 54, tinted)
    for index, line in enumerate(lines):
        _write(canvas, left, 42 - index * 10.3, line, "Helvetica", 7.7, GREY)


def _fold_marks(canvas, height):
    # Falt- und Lochmarke liegen außerhalb des Fenster- und Textbereichs.
    for from_top, length in ((297.6, 10), (height / 2, 14), (595.3, 10)):
        _rule(canvas, 16, 16 + length, height - from_top, "#A7AEAD", 0.5)


def draw_letterhead(canvas, *, sender, page_number, page_count, page_size, document_kind, header_lines,
                    address_window=False):
    """Setzt Register, Korrespondenz, Kanzleibogen oder internen Formularbogen."""
    width, height = page_size
    left, right = 77, width - 77
    lines = tuple(header_lines)
    canvas.saveState()
    if page_number > 1:
        name, ink, accent = BRANDS[sender]
        draw_signet(canvas, sender, left - 1, height - 51, 0.47)
        _write(canvas, left + 27, height - 42, name, "Helvetica", 9, ink)
        _rule(canvas, left, right, height - 58, PALE)
        _rule(canvas, right - 44, right, height - 58, accent, 1.4)
    elif document_kind == "email":
        y = height - 72
        _block(canvas, left, y - 13, right - left, 46, "#F0F3F5")
        _block(canvas, left, y - 13, 3, 46, "#587486")
        canvas.setLineWidth(0.9)
        canvas.setStrokeColor(colors.HexColor("#465C6B"))
        canvas.roundRect(left + 13, y + 3, 19, 13, 1.2)
        fold = canvas.beginPath()
        fold.moveTo(left + 13, y + 16)
        fold.lineTo(left + 22.5, y + 8.5)
        fold.lineTo(left + 32, y + 16)
        canvas.drawPath(fold)
        _write(canvas, left + 45, y + 2, lines[0], "Helvetica-Bold", 15, DARK)
    elif document_kind == "register":
        _block(canvas, 42, height - 108, width - 84, 68, "#F0F3F4")
        _block(canvas, 42, height - 108, 4, 68, "#375361")
        _write(canvas, 59, height - 69, lines[0], "Times-Bold", 18, DARK)
        _write(canvas, 59, height - 90, lines[1], "Helvetica", 9.3, GREY)
    else:
        _, ink, accent = BRANDS[sender]
        if document_kind == "intern":
            # Der schmale Ablagekopf lässt die fallbezogenen Felder des Vermerks dominieren.
            tint = "#EAF0F2" if sender == "inkasso" else "#F4EFEC"
            _block(canvas, left - 10, height - 92, right - left + 20, 52, tint)
            _block(canvas, left - 10, height - 92, 3, 52, accent)
            draw_brand(canvas, sender, left + 2, height - 83, 0.88, lines[0])
        elif sender == "modefuchs":
            # Briefpapier des Modehauses mit der Nahtlinie der Wortbildmarke.
            _block(canvas, 0, height - 98, width, 98, "#F8F2E9")
            _rule(canvas, 0, width, height - 98, "#D3AB92", 0.55)
            canvas.saveState()
            canvas.setDash(3, 3)
            _rule(canvas, 0, width, height - 94, "#DFC8B7", 0.45)
            canvas.restoreState()
            draw_brand(canvas, sender, left - 5, height - 80, 1.29, lines[0])
        elif sender == "inkasso":
            _block(canvas, left, height - 84, 4, 45, accent)
            draw_brand(canvas, sender, left + 12, height - 84, 1.05, lines[0])
            _rule(canvas, left, right, height - 96, "#C5D4D8")
        elif sender == "kanzlei":
            # Klassischer zweifarbig gesetzter Kanzleibogen.
            draw_brand(canvas, sender, left - 2, height - 85, 1.11, lines[0])
            _rule(canvas, left, right, height - 96, accent, 0.9)
            _rule(canvas, left, right, height - 99, "#BEB0A8", 0.35)
        else:
            _block(canvas, left, height - 89, right - left, 51, "#EAF2ED")
            _block(canvas, left, height - 89, right - left, 2.3, accent)
            draw_brand(canvas, sender, left + 10, height - 83, 0.96, lines[0])

        header_count = 3 if sender == "kanzlei" else 2
        # Die unveränderte Adress-/Registerzeile sitzt beim Geschäftsbrief direkt
        # über dem Empfängerfenster. Sie ist zugleich die Rücksendeangabe.
        for index, line in enumerate(lines[1:header_count], start=1):
            if address_window and index == header_count - 1:
                size = 7.6
                _write(canvas, left, height - 146, line, "Helvetica", size, ink)
                _rule(canvas, left, left + canvas.stringWidth(line, "Helvetica", size), height - 150, PALE)
            else:
                _write(canvas, left, height - 114 - 12 * (index - 1), line, "Helvetica", 8.6, ink)
        if document_kind in ("brief", "prozess"):
            _fold_marks(canvas, height)
        _footer(canvas, lines[header_count:], left, right, accent, "#CDD2D0")
    if page_count > 1:
        canvas.setFont("Helvetica", 7.5)
        _ink(canvas, GREY)
        canvas.drawRightString(right, 24, f"Seite {page_number} von {page_count}")
    canvas.restoreState()
