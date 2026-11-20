"""Warnhinweise an Downloadgruppen; keine Aenderung an PDF-Inhalten."""

import re

WARNING = (
    "Diese Testakte wurde mit KI generiert und ist ein Experiment. "
    "Benutzung auf eigene Verantwortung und eigene Gefahr.\n\n"
    "This test case file was generated with AI and is an experiment. "
    "Use at your own responsibility and risk."
)
MARKDOWN_WARNING = "> " + WARNING.replace("\n\n", "\n>\n> ")
README_NOTICE = "HINWEIS / NOTICE\n=================\n\n" + WARNING + "\n"
CASE_DOWNLOAD = re.compile(
    r"\]\([^\s)]*(?:testakte[^\s)]*\.zip|alles-komplettpaket\.zip|"
    r"/archive/refs/heads/main\.zip|\.pdf)(?:[?#][^\s)]*)?\)"
)
INTERNAL_NAME = re.compile(
    r"(?:^|[_ .-])(?:rubric|rubrik|solution|loesung|lösung|musterloesung|"
    r"musterlösung|erwartungshorizont|expected|eval|grading|ground[_-]?truth)(?:[_ .-]|$)",
    re.IGNORECASE,
)


def with_case_warnings(text: str) -> str:
    """Stellt den Hinweis unmittelbar vor jeden Absatz oder jede Linktabelle."""
    # Generator-Marker koennen bereits einen Hinweis ausserhalb des Blocks tragen.
    text = text.replace(MARKDOWN_WARNING + "\n\n", "")
    blocks = re.split(r"(\n[ \t]*\n)", text)
    output: list[str] = []
    for block in blocks:
        if CASE_DOWNLOAD.search(block):
            previous = "".join(output).rstrip()
            if not previous.endswith(MARKDOWN_WARNING):
                output.append(MARKDOWN_WARNING + "\n\n")
        output.append(block)
    return "".join(output)


def is_internal_file(name: str) -> bool:
    return bool(INTERNAL_NAME.search(name))
