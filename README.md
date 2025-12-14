## 🛠️  Einrichtung (Ubuntu / Linux)

Wir nutzen das Tool **uv**, das sich automatisch um Python und alle Bibliotheken kÃ¼mmert. Du musst nichts manuell installieren.

**1. uv installieren**
Öffne dein Terminal (`Strg` + `Alt` + `T`) und führe aus:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```
*Wichtig: Schließe danach das Terminal und Öffne ein neues.*

**2. Projektordner anlegen**
Kopiere diese Zeilen einzeln ins Terminal:
```bash
uv init
uv pip install -r requirements.txt
```

**3. Testen**
Erstelle eine Datei (z.B. in VS Code oder mit Texteditor) und führe sie später so aus:
```bash
cd klausur/
uv run aufgabe_1.py
```

