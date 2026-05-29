---
name: produktrecht-anpassen
description: 'Geführte Anpassung Ihres Produktrecht-Praxisprofils – eine Sache ändern ohne das gesamte Kaltstart-Interview erneut auszuführen. Risikokalibrierung, Eskalationskontakte, Launch-Review-Framework, Werbeaussagen-Haltung oder Mandate-Workspace-Pfade anpassen. Verwenden wenn der Nutzer sagt "mein [Ding] ändern", "mein Profil aktualisieren", "mein Framework bearbeiten", "meine Kalibrierung anpassen" oder "anpassen".'

---

# /anpassen

## Wann dies ausgeführt wird

Der Nutzer hat `/produktrecht:produktrecht-anpassen` eingegeben. Er möchte etwas in seinem Produktrecht-Profil ändern – eine Risikokalibrierungs-Schwelle, einen Eskalationskontakt, einen Framework-Abschnitt – ohne das gesamte Kaltstart-Interview erneut auszuführen und ohne YAML direkt zu bearbeiten.

## Was zu tun ist

1. **Konfiguration lesen.** `~/.claude/plugins/config/claude-fuer-deutsches-recht/produktrecht/CLAUDE.md` lesen (und `~/.claude/plugins/config/claude-fuer-deutsches-recht/unternehmens-profil.md` eine Ebene darüber). Wenn die Plugin-Konfiguration nicht existiert oder noch `[PLATZHALTER]`-Werte enthält, sagen:

   > Sie haben das Setup noch nicht ausgeführt. Führen Sie zuerst `/produktrecht:produktrecht-kaltstart-interview` aus – anpassen ist für die Anpassung eines Profils das Sie bereits haben.

2. **Anpassbare Karte zeigen.** Was im Profil ist, gruppiert, mit einer einzeiligen Zusammenfassung des aktuellen Werts:

   - **Unternehmen / wer wir sind** – Name, Branche, Jurisdiktionen, Phase, Praxissetting, Produkt-Fläche *(geteilt über alle Plugins – Änderungen fließen durch `unternehmens-profil.md`)*
   - **Launch-Review-Prozess** – Eingang (Jira / Linear / Asana / Dokument), Review-SLA, Launch-Tiering, PRD-Speicherort
   - **Review-Framework** – die Kategorien gegen die Sie Launches prüfen (Werberecht, Datenschutz, AGB, Produktsicherheit, Geistiges Eigentum, Verbraucherrechte, Aufsichtsrecht) und die Tiefe pro Kategorie
   - **Risikokalibrierung** – was P0-Blocker / braucht-einen-Blick / in-Ordnung bei Ihrem Unternehmen ist, mit Beispielen die die Labels verankern
   - **Werbeaussagen** – Haltung zu marktschreierischer Anpreisung vs. substanziiert, vergleichende Werbehaltung nach § 6 UWG, Superlative, Hausregeln für KI-Feature-Aussagen
   - **Personen** – Produktpartner nach Fläche, Eskalationskette (Ihr Vorgesetzter, GC, Risikoausschuss), Marketing-Kontaktperson
   - **Ablauf** – Mandate-Workspaces, launch-radar-Watcher-Takt, Launch-Review-Vorlage
   - **Integrationen** – Jira / Linear / Asana / Slack / Dokumentenspeicher-Status, Ausweiche

3. **Fragen was geändert werden soll.**

   > Was möchten Sie anpassen? Wählen Sie einen Abschnitt, oder beschreiben Sie die Änderung in Ihren eigenen Worten.

4. **Die Änderung machen.** Aktuellen Wert zeigen, nach neuem Wert fragen, erklären was sich downstream ändert, bestätigen, in die Konfiguration schreiben.

   Beispiele:
   - *Risikokalibrierung von "in-Ordnung" → "braucht-einen-Blick" für ein Muster festigen:* "`/ist-das-ein-problem` und `/launch-prüfung` werden dieses Muster beginnen zu flaggen. Bestehende Reviews bleiben wie geschrieben; erneut ausführen wenn Sie die neue Haltung angewendet haben möchten."
   - *Neue Launch-Review-Kategorie:* "`/launch-prüfung` fügt einen Abschnitt für diese Kategorie hinzu. `/ist-das-ein-problem` wird es in der Triage muster-erkennen."
   - *Werbeaussagen-Haltung festigen:* "`/werbeaussagen-prüfung` wird mehr Sprache als substanziierungsbedürftig oder umformulierungsbedürftig flaggen."

5. **Für gemeinsames-Profil-Änderungen** (Unternehmensname, Branche, Jurisdiktionen, Praxissetting, Phase): nach `~/.claude/plugins/config/claude-fuer-deutsches-recht/unternehmens-profil.md` schreiben und vermerken:

   > Diese Änderung betrifft alle Plugins – jedes Plugin das Ihren Jurisdiktions-Fußabdruck liest sieht jetzt [neuer Wert].

6. **Abschließen.**

   > Fertig. Ihre nächste Ausgabe spiegelt die Änderung wider. Sonst noch etwas? Sie können `/produktrecht:produktrecht-anpassen` jederzeit ausführen.

## Leitplanken

- **Niemals einen Abschnitt löschen.** Wenn der Nutzer eine Review-Kategorie "entfernen" möchte, anbieten sie als `[Nicht im Umfang – anderswo weiterleiten]` zu markieren und das Plugin / Team zu nennen das sie übernimmt.
- **Interne Inkonsistenz markieren.** Wenn die Änderung das Profil inkonsistent machen würde (z. B. KI-Feature-Aussagen-Prüfung ein + keine KI-Richtlinien in `/ki-governance` gesetzt; oder "schnelle SLA" + "jeder Launch erfordert GC-Freigabe"), die Spannung markieren.
- **Leitplanken-Degradierung markieren.** Der `[prüfen]`-Flag, Quellenattributions-Tags und `[prüfen]`-Tags auf zitierten Normen sind tragende Bauelemente – nicht entfernen. Die Substanziierungsanforderung für Werbeaussagen ist das wofür `/werbeaussagen-prüfung` existiert; sie zu schwächen besiegt den Skill.
- **Eine Änderung auf einmal.** Nicht das gesamte Interview neu stellen.
## Aktuelle Rechtsprechung & Leitsätze

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)

§§ 312 ff. BGB (Verbraucherschutzrecht, Informationspflichten) — §§ 1-4 ProdHaftG (Produkthaftung) — §§ 3, 3a UWG (Wettbewerbsrecht, Marktverhaltensregel) — §§ 5-6 DDG (Impressumspflicht) — EU AI Act VO 2024/1689 (KI-Produktrecht)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.