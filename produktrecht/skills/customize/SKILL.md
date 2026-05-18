---
name: customize
description: >
  Geführte Anpassung Ihres Produktrecht-Praxisprofils – eine Sache ändern ohne
  das gesamte Cold-Start-Interview erneut auszuführen. Risikokalibrierung,
  Eskalationskontakte, Launch-Review-Framework, Werbeaussagen-Haltung oder
  Mandate-Workspace-Pfade anpassen. Verwenden wenn der Nutzer sagt „mein
  [Ding] ändern", „mein Profil aktualisieren", „mein Framework bearbeiten",
  „meine Kalibrierung anpassen" oder „anpassen".
language: de
triggers:
  - "anpassen"
  - "konfiguration ändern"
  - "profil aktualisieren"
  - "framework bearbeiten"
  - "kalibrierung anpassen"
argument-hint: "[Abschnittsname, oder beschreiben was Sie ändern möchten]"
---

# /customize

## Wann dies ausgeführt wird

Der Nutzer hat `/produktrecht:customize` eingegeben. Er möchte etwas in seinem Produktrecht-Profil ändern – eine Risikokalibrierungs-Schwelle, einen Eskalationskontakt, einen Framework-Abschnitt – ohne das gesamte Cold-Start-Interview erneut auszuführen und ohne YAML direkt zu bearbeiten.

## Was zu tun ist

1. **Konfiguration lesen.** `~/.claude/plugins/config/claude-fuer-legal/produktrecht/CLAUDE.md` lesen (und `~/.claude/plugins/config/claude-fuer-legal/company-profile.md` eine Ebene darüber). Wenn die Plugin-Konfiguration nicht existiert oder noch `[PLATZHALTER]`-Werte enthält, sagen:

   > Sie haben das Setup noch nicht ausgeführt. Führen Sie zuerst `/produktrecht:cold-start-interview` aus – customize ist für die Anpassung eines Profils das Sie bereits haben.

2. **Anpassbare Karte zeigen.** Was im Profil ist, gruppiert, mit einer einzeiligen Zusammenfassung des aktuellen Werts:

   - **Unternehmen / wer wir sind** – Name, Branche, Jurisdiktionen, Phase, Praxissetting, Produkt-Fläche *(geteilt über alle Plugins – Änderungen fließen durch `company-profile.md`)*
   - **Launch-Review-Prozess** – Eingang (Jira / Linear / Asana / Dokument), Review-SLA, Launch-Tiering, PRD-Speicherort
   - **Review-Framework** – die Kategorien gegen die Sie Launches prüfen (Werberecht, Datenschutz, AGB, Produktsicherheit, Geistiges Eigentum, Verbraucherrechte, Aufsichtsrecht) und die Tiefe pro Kategorie
   - **Risikokalibrierung** – was P0-Blocker / braucht-einen-Blick / in-Ordnung bei Ihrem Unternehmen ist, mit Beispielen die die Labels verankern
   - **Werbeaussagen** – Haltung zu marktschreierischer Anpreisung vs. substanziiert, vergleichende Werbehaltung nach § 6 UWG, Superlative, Hausregeln für KI-Feature-Aussagen
   - **Personen** – Produktpartner nach Fläche, Eskalationskette (Ihr Vorgesetzter, GC, Risikoausschuss), Marketing-Kontaktperson
   - **Workflow** – Mandate-Workspaces, launch-radar-Watcher-Takt, Launch-Review-Vorlage
   - **Integrationen** – Jira / Linear / Asana / Slack / Dokumentenspeicher-Status, Ausweiche

3. **Fragen was geändert werden soll.**

   > Was möchten Sie anpassen? Wählen Sie einen Abschnitt, oder beschreiben Sie die Änderung in Ihren eigenen Worten.

4. **Die Änderung machen.** Aktuellen Wert zeigen, nach neuem Wert fragen, erklären was sich downstream ändert, bestätigen, in die Konfiguration schreiben.

   Beispiele:
   - *Risikokalibrierung von „in-Ordnung" → „braucht-einen-Blick" für ein Muster festigen:* „`/is-this-a-problem` und `/launch-review` werden dieses Muster beginnen zu flaggen. Bestehende Reviews bleiben wie geschrieben; erneut ausführen wenn Sie die neue Haltung angewendet haben möchten."
   - *Neue Launch-Review-Kategorie:* „`/launch-review` fügt einen Abschnitt für diese Kategorie hinzu. `/is-this-a-problem` wird es in der Triage muster-erkennen."
   - *Werbeaussagen-Haltung festigen:* „`/marketing-claims-review` wird mehr Sprache als substanziierungsbedürftig oder umformulierungsbedürftig flaggen."

5. **Für gemeinsames-Profil-Änderungen** (Unternehmensname, Branche, Jurisdiktionen, Praxissetting, Phase): nach `~/.claude/plugins/config/claude-fuer-legal/company-profile.md` schreiben und vermerken:

   > Diese Änderung betrifft alle Plugins – jedes Plugin das Ihren Jurisdiktions-Fußabdruck liest sieht jetzt [neuer Wert].

6. **Abschließen.**

   > Fertig. Ihre nächste Ausgabe spiegelt die Änderung wider. Sonst noch etwas? Sie können `/produktrecht:customize` jederzeit ausführen.

## Leitplanken

- **Niemals einen Abschnitt löschen.** Wenn der Nutzer eine Review-Kategorie „entfernen" möchte, anbieten sie als `[Nicht im Umfang – anderswo weiterleiten]` zu markieren und das Plugin / Team zu nennen das sie übernimmt.
- **Interne Inkonsistenz markieren.** Wenn die Änderung das Profil inkonsistent machen würde (z. B. KI-Feature-Aussagen-Prüfung ein + keine KI-Richtlinien in `/ki-governance` gesetzt; oder „schnelle SLA" + „jeder Launch erfordert GC-Freigabe"), die Spannung markieren.
- **Leitplanken-Degradierung markieren.** Der `[prüfen]`-Flag, Quellenattributions-Tags und `[prüfen]`-Tags auf zitierten Normen sind tragende Bauelemente – nicht entfernen. Die Substanziierungsanforderung für Werbeaussagen ist das wofür `/marketing-claims-review` existiert; sie zu schwächen besiegt den Skill.
- **Eine Änderung auf einmal.** Nicht das gesamte Interview neu stellen.
