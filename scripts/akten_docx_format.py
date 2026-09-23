"""Shared paragraph formatting for native case documents."""

from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Pt
from docx.text.paragraph import Paragraph


def separate_section_headings(document):
    """Keep each section heading, one blank line and its content together."""
    for name in ("Heading 1", "Heading 2"):
        formatting = document.styles[name].paragraph_format
        formatting.space_after = Pt(0)
        formatting.keep_with_next = True

    for heading in document.paragraphs:
        if heading.style.style_id not in {"Heading1", "Heading2"}:
            continue
        heading.paragraph_format.space_after = Pt(0)
        heading.paragraph_format.keep_with_next = True
        following = heading._p.getnext()
        # Reuse only an empty paragraph, never a page break or another element.
        if following is None or following.tag != qn("w:p") or any(
            child.tag != qn("w:pPr") for child in following
        ):
            following = OxmlElement("w:p")
            heading._p.addnext(following)
        blank = Paragraph(following, heading._parent)
        blank.style = document.styles["Normal"]
        formatting = blank.paragraph_format
        formatting.space_before = Pt(0)
        formatting.space_after = Pt(0)
        formatting.line_spacing = Pt(11)
        formatting.keep_with_next = True
        properties = blank._p.get_or_add_pPr()
        run_properties = properties.find(qn("w:rPr"))
        if run_properties is None:
            run_properties = OxmlElement("w:rPr")
            properties.append(run_properties)
        for name in ("sz", "szCs"):
            size = run_properties.find(qn("w:" + name))
            if size is None:
                size = OxmlElement("w:" + name)
                run_properties.append(size)
            size.set(qn("w:val"), "22")
