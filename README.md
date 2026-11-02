# Zapiski

Orodja za gradnjo so opisana v `pyproject.toml`, poganjamo pa jih z [uv](https://docs.astral.sh/uv/),
ki si okolje uredi sam, zato ni treba ničesar namestiti vnaprej:

```bash
uv run jupyter-book build ucbenik
```

Različica `jupyter-book` je omejena na `<2`, ker učbenik opisujeta `_config.yml` in `_toc.yml`,
druga različica pa je drugo orodje (mystmd) in teh datotek ne prebere.

Če imate ustrezne pravice, lahko HTML najenostavneje objavite kar prek [GitHub pages](https://pages.github.com):

```bash
uv run --with ghp-import ghp-import --no-jekyll --no-history --force --push ucbenik/_build/html && git branch -D gh-pages
```

Objava s silo prepiše vejo `gh-pages`, zato pred njo zgradite učbenik na novo.
Ker gradnja ne pobriše strani, ki jih v učbeniku ni več, pred njo počistite imenik `ucbenik/_build`:

```bash
uv run jupyter-book clean ucbenik && uv run jupyter-book build ucbenik
```

Preden se spremembe pokažejo na spletu, mine minuta ali dve.

## Povezave

Slike za direktorijsko strukturo: [folder2image.com](https://www.folder2image.com).
