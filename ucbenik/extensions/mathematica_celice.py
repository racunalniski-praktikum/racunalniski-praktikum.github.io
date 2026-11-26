"""Oštevilči oznake In in Out v primerih iz Mathematice.

V izvorni kodi so vrstice v blokih ```mathematica označene brez številk, z
`In:=` in `Out=`. Ob gradnji jih ta razširitev na vsaki strani zaporedoma
oštevilči: vsak `In` dobi naslednjo številko, `Out` pa številko zadnjega `In`
pred njim. Vrstice, ki številko že imajo, oštevilči na novo.
"""

import re

from docutils import nodes
from sphinx.transforms import SphinxTransform

OZNAKA = re.compile(r"^(In|Out)(?:\[\d*\])?(:=|=)", re.MULTILINE)


class OstevilciCelice(SphinxTransform):
    # Pred označevanjem sintakse, ki bere besedilo bloka.
    default_priority = 400

    def apply(self):
        stevec = 0
        for blok in self.document.findall(nodes.literal_block):
            if blok.get("language") != "mathematica":
                continue
            besedilo = blok.astext()
            if not OZNAKA.search(besedilo):
                continue

            def ostevilci(ujemanje):
                nonlocal stevec
                vrsta, znak = ujemanje.group(1), ujemanje.group(2)
                if vrsta == "In":
                    stevec += 1
                return f"{vrsta}[{stevec}]{znak}"

            novo = OZNAKA.sub(ostevilci, besedilo)
            blok.rawsource = novo
            blok[:] = [nodes.Text(novo)]


def setup(app):
    app.add_transform(OstevilciCelice)
    return {"parallel_read_safe": True, "parallel_write_safe": True}
