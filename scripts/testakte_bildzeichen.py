"""Farbige Schriftzeichen in der PDF-Druckfassung mit kopierbarem Unicode-Wert.

Die Druckbilder stammen aus Google Noto Color Emoji (SIL Open Font License).
"""

from functools import lru_cache
from pathlib import Path
from zlib import compress

from PIL import Image
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.pdfdoc import PDFArray, PDFDictionary, PDFName, PDFStream


class Bildzeichen(pdfmetrics.Font):
    """Eine Type-3-Schrift mit dem farbigen Druckbild eines Schriftzeichens."""

    def __init__(self, char, path):
        self.char, self.path = char, path
        super().__init__(f"Aktenzeichen{ord(char):X}", "Helvetica", "WinAnsiEncoding")
        self.widths[ord("x")] = 1000

    def addObjects(self, doc):
        with Image.open(self.path) as source:
            rgba = source.convert("RGBA")
            image = Image.new("RGB", rgba.size, "white")
            image.paste(rgba, mask=rgba.getchannel("A"))
        # Das Zeichen läuft auf einem Geviert. Im Druck bleibt das Seitenverhältnis erhalten.
        height = round(1000 * image.height / image.width)
        image_data = compress(image.tobytes()).hex()
        contents = (f"1000 0 d0 q 1000 0 0 {height} 0 -50 cm BI /W {image.width} /H {image.height} "
                    f"/BPC 8 /CS /RGB /F [/AHx /Fl] ID\n{image_data}>\nEI Q")
        char_proc = doc.Reference(PDFStream(content=contents))
        unicode_value = self.char.encode("utf-16-be").hex()
        cmap = ("/CIDInit /ProcSet findresource begin 12 dict begin begincmap\n"
                "/CIDSystemInfo << /Registry (Adobe) /Ordering (UCS) /Supplement 0 >> def\n"
                "/CMapName /Aktenzeichen def /CMapType 2 def\n"
                "1 begincodespacerange <00> <FF> endcodespacerange\n"
                f"1 beginbfchar <78> <{unicode_value}> endbfchar\n"
                "endcmap CMapName currentdict /CMap defineresource pop end end")
        name = f"F{len(doc.fontMapping) + 1}"
        font = PDFDictionary(dict(
            Type=PDFName("Font"), Subtype=PDFName("Type3"), Name=PDFName(name),
            FontBBox=PDFArray([0, -50, 1000, height]), FontMatrix=PDFArray([.001, 0, 0, .001, 0, 0]),
            FirstChar=120, LastChar=120, Widths=PDFArray([1000]), Resources=PDFDictionary(),
            Encoding=PDFDictionary(dict(Type=PDFName("Encoding"), Differences=PDFArray([120, PDFName("bild")]))),
            CharProcs=PDFDictionary(dict(bild=char_proc)), ToUnicode=doc.Reference(PDFStream(content=cmap))))
        doc.idToObject["BasicFonts"].dict[name] = doc.Reference(font, name)
        doc.fontMapping[self.fontName] = "/" + name


@lru_cache(maxsize=64)
def bildzeichen(char):
    path = Path(__file__).resolve().parent / "data" / "aktenzeichen" / f"{ord(char):x}.png"
    if not path.is_file():
        raise ValueError(f"Keine PDF-Schrift für {char!r} (U+{ord(char):04X})")
    font = Bildzeichen(char, path)
    pdfmetrics.registerFont(font)
    pdfmetrics.registerFontFamily(font.fontName, normal=font.fontName)
    return f'<font name="{font.fontName}">x</font>'
