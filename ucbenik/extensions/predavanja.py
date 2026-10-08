"""Objavi prosojnice iz imenika predavanja/ skupaj z učbenikom.

Ob koncu gradnje HTML prekopira imenik predavanja/ v predavanja/ v izhodnem
imeniku in iz predavanja/README.md naredi predavanja/index.html. Prosojnice so
tako objavljene na https://racunalniski-praktikum.github.io/predavanja/.
"""

import html
import shutil
from pathlib import Path

from markdown_it import MarkdownIt

PREDLOGA = """<!doctype html>
<html lang="sl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{naslov}</title>
<style>
body {{ max-width: 48em; margin: 2em auto; padding: 0 1em; font-family: sans-serif; line-height: 1.5; }}
</style>
</head>
<body>
{vsebina}
</body>
</html>
"""


def objavi_predavanja(app, exception):
    if exception is not None or app.builder.format != "html":
        return
    izvor = Path(app.srcdir).parent / "predavanja"
    cilj = Path(app.outdir) / "predavanja"
    shutil.copytree(izvor, cilj, dirs_exist_ok=True, ignore=shutil.ignore_patterns(".*"))
    besedilo = (izvor / "README.md").read_text(encoding="utf-8")
    naslov = besedilo.splitlines()[0].lstrip("#").strip()
    vsebina = MarkdownIt("commonmark").enable("table").render(besedilo)
    (cilj / "index.html").write_text(
        PREDLOGA.format(naslov=html.escape(naslov), vsebina=vsebina), encoding="utf-8"
    )


def setup(app):
    app.connect("build-finished", objavi_predavanja)
    return {"parallel_read_safe": True, "parallel_write_safe": True}
