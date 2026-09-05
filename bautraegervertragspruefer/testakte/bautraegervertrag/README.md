# Bauträgervertrag — Akte Hohenwartshofen

Der Vertrag Hohenwartshofen liegt mit seinen Zahlungs- und Vollzugsregelungen zur Prüfung vor. Einen weiteren, unabhängigen Vertragsbestand enthält die [Akte Marewald](../bautraegervertrag-marewald/README.md). Zur [Übersicht](../README.md).

Dieses Verzeichnis enthält ein eigenständiges Vertragsdokument in den Gesamtfassungen und als Akten-ZIP mit getrennten Einzel-PDFs:

> Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.
>
> This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

- [Markdown öffnen](bautraegervertrag.md)
- [Word-Dokument herunterladen](bautraegervertrag.docx)
- [PDF herunterladen](bautraegervertrag.pdf)
- [Akten-ZIP mit Einzel-PDFs herunterladen](bautraegervertrag-einzel-pdfs.zip)

Öffentliche Download-Links über GitHub Pages:

- [Markdown direkt laden](https://klotzkette.github.io/bautraegervertragspruefer-skill/vertragsdokumente/bautraegervertrag/bautraegervertrag.md)
- [Word-Dokument direkt laden](https://klotzkette.github.io/bautraegervertragspruefer-skill/vertragsdokumente/bautraegervertrag/bautraegervertrag.docx)
- [PDF direkt laden](https://klotzkette.github.io/bautraegervertragspruefer-skill/vertragsdokumente/bautraegervertrag/bautraegervertrag.pdf)
- [Akten-ZIP direkt laden](https://klotzkette.github.io/bautraegervertragspruefer-skill/vertragsdokumente/bautraegervertrag/bautraegervertrag-einzel-pdfs.zip)

## Wichtiger Hinweis

Dieser Bauträgervertrag ist kein Mustervertrag und darf nicht als Vorlage in der Praxis verwendet, nicht übernommen und nicht gegenüber echten Käufern, Bauträgern, Notariaten oder Behörden eingesetzt werden.

Markdown, Word und PDF enthalten denselben Vertragsstoff einschließlich der Baubeschreibung als Anlage. Das Akten-ZIP enthält denselben Stoff als getrennte, neutral benannte Einzel-PDFs. Für jede fachliche Bewertung ist eine eigenständige rechtliche und technische Prüfung erforderlich.

## Verwendung mit dem Skill

1. Lade den Bauträgervertrag als PDF, DOCX oder Markdown.
2. Lade den Bauträgervertrag-Prüfer-Skill aus dem Repository, entweder vollständig als `SKILL.md` oder kompakt als `MINI_SKILL.md`.
3. Übergib beides einer KI und lasse den Vertrag autonom prüfen.
4. Die Ausgabe soll mit Übersendungsschreiben an die Käuferseite, Mandantengutachten und außergerichtlichem Aufforderungsschreiben an Bauträger/Notar enden.

## Neu erzeugen

Nach Änderungen an `bautraegervertrag.md` werden Word-Fassung, Gesamt-PDF und Akten-ZIP so erzeugt:

```bash
./build.sh
```

Voraussetzungen: `pandoc` und `weasyprint`. Layout und Seitenumbrüche steuern `build/style.css` und `build/pagebreak.lua`.
