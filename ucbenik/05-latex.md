# Uvod v LaTeX

`````{admonition} Programska oprema
:class: important
- [LaTeX](namestitev:latex),
- [Visual Studio Code](namestitev:vscode) z razširitvijo [LaTeX Workshop](https://marketplace.visualstudio.com/items?itemName=James-Yu.latex-workshop).
`````

LaTeX je sistem za stavljenje besedila.
Datoteko s končnico `.tex`, ki vsebuje navadno besedilo, označeno s posebnimi okolji in ukazi,
pretvori v lepo stavljeno besedilo in ga shrani v datoteko PDF s končnico `.pdf`.
Temu koraku pravimo _prevajanje_ (angl. _compile_), programu, ki ga opravi, pa _prevajalnik_:
izraz je izposojen iz programiranja, kjer prevajalnik izvorno kodo pretvori v program.
Ideja je enaka kot pri Markdownu in HTML-ju: z dogovorjenimi zaporedji znakov povemo, kaj posamezni deli besedila so,
kako bodo videti, pa določi LaTeX.

## Ukazi in okolja

LaTeX dokumente oblikujemo z _ukazi_ (angl. _command_) in _okolji_ (angl. _environment_),
kot pri HTML-ju pa lahko uporabljamo tudi _komentarje_.
Ukazom včasih rečemo tudi makroji (angl. _macro_).
Kot do sedaj bodo primeri, ki jih morate še popraviti, napisani takole: `⟨nadomesti-me⟩`.
Pobrišite oklepaje in ustrezno popravite njihovo vsebino.

```tex
% Vse, kar sledi znaku %, je komentar in LaTeX ignorira.
% Okolja so podobna značkam:
\begin{⟨ime-okolja⟩} % začetek okolja
  ⟨vsebina⟩          % vsebina
\end{⟨ime-okolja⟩}   % konec okolja

% Ukazi so bolj enostavni:
\⟨ime-ukaza⟩
```

Najprej boste srečali ukaz `documentclass` in okolje `document`:

```tex
\documentclass{article}

\begin{document} % začetek okolja document
  Vsebina dokumenta
\end{document}   % konec okolja document
```

Nekateri ukazi in okolja sprejmejo tudi dodatne argumente,
ki so lahko obvezni (v zavitih oklepajih `{}`) ali neobvezni (v oglatih oklepajih `[]`).

* Ukaz `\section{Turingovi stroji}` naredi nov razdelek z naslovom "Turingovi stroji".
* Ukaz `frac`, ki v matematičnem okolju naredi ulomek, sprejme dva argumenta,
  števec in imenovalec: `\frac{22}{7}` izpiše $\frac{22}{7}$.
* Ukaz `rule` za ločnice, ki nariše pravokotnik, sprejme dva obvezna argumenta in enega neobveznega
  (kako visoko v vrstici stoji ločnica):
  `\rule[⟨višina⟩]{⟨dolžina⟩}{⟨širina⟩}`.

Pri teh vajah boste srečali okolja `abstract`, `verbatim` (oznaka ` ``` ` v Markdownu),
`itemize` in `enumerate` (znački `ul` in `ol` v HTML-ju), v katerih vsak element seznama začne ukaz `\item`.
Naslov, avtorja in datum dokumenta nastavimo z ukazi `\title`, `\author` in `\date`.
Ti ukazi ne izpišejo ničesar: LaTeX si podatke o dokumentu (metapodatke) le zapomni.
Izpiše jih šele ukaz `\maketitle`, in sicer tam, kjer ga uporabimo, zato morajo ukazi za nastavljanje stati pred njim.
Če datuma ne nastavimo, `\maketitle` izpiše današnjega.

### Matematika

Matematični izraz lahko stoji na dveh mestih.
V _vrstičnem načinu_ (angl. _inline_) je del vrstice z besedilom; zapišemo ga med `\(` in `\)`.
V _prikaznem načinu_ (angl. _display_) stoji sam v svoji vrstici, sredinsko poravnan; zapišemo ga med `\[` in `\]`.
Primer z obema načinoma:

```tex
V pravokotnem trikotniku s katetama \(a\) in \(b\) ter hipotenuzo \(c\) velja
\[
  a^2 + b^2 = c^2.
\]
Hipotenuza je torej \(c = \sqrt{a^2 + b^2}\).
```

LaTeX to prevede v:

V pravokotnem trikotniku s katetama $a$ in $b$ ter hipotenuzo $c$ velja
$$a^2 + b^2 = c^2.$$
Hipotenuza je torej $c = \sqrt{a^2 + b^2}$.

Izraz v prikaznem načinu je še vedno del stavka: pred `\[` in za `\]` ni prazne vrstice,
ločilo na koncu stavka pa stoji znotraj izraza, kot pika v zgornjem primeru.
V vrstico sodijo kratki izrazi, ki tečejo z besedilom, na primer oznake kot $n$ ali $x_i$;
v svojo vrstico pa pomembne enačbe in vse, kar je višje od vrstice, na primer ulomki, vsote in integrali.

Zapisa `\(…\)` in `\[…\]` sta okrajšavi za okolji `math` in `displaymath`.
Včasih boste videli tudi starejši okrajšavi `$` za vrstični in `$$` za prikazni način.
Uporabo teh dveh odsvetujemo: pozabljen `$` LaTeX opazi šele pri naslednjem `$`,
zato napako javi daleč od mesta, kjer je nastala.

`````{admonition} Ukazi za matematične izraze
:class: tip
V matematičnih okoljih lahko uporabljamo ukaze za matematične izraze,
kot so `frac` za ulomke, `int` za integrale, `cdot` za piko pri množenju, ukaze za matrike itd.
Ti ukazi delajo **samo v matematičnih okoljih**, izven njih pa sprožijo napako.
Velja tudi obratno: običajne besede v matematičnem okolju označimo z ukazom `\text`,
da se pravilno prikažejo. Ta ukaz potrebuje paket `amsmath`.
`````

## Struktura dokumenta

LaTeX dokument shranimo v datoteko s končnico `.tex`. Dokument je lahko shranjen
tudi v večjih datotekah, ki jih z ukazom `\input{datoteka.tex}` vključimo v
glavno datoteko.
Struktura glavne LaTeX datoteke je videti takole:

```tex
\documentclass[⟨nastavitve⟩]{⟨vrsta dokumenta⟩}

⟨preambula⟩

\begin{document}

  ⟨vsebina⟩

\end{document}
```

Ukaz `\documentclass` določa zvrst dokumenta (članek, knjiga, pismo, ...),
ki jo določimo v obveznem argumentu, takole: `\documentclass{article}`.
Možne zvrsti dokumentov so vnaprej definirane in se razlikujejo tudi po oblikovanju.
Dodatne nastavitve, kot na primer za velikost strani in osnovno velikost pisave, zapišemo v oglate oklepaje in jih ločimo z vejicami:
`\documentclass[a4paper, 10pt]{article}`.

V preambulo se nikoli ne piše vsebine, ampak samo ukaze in nastavitve.
V preambuli v dokument vključimo pakete, uredimo nastavitve in definiramo nove ukaze in okolja.

Paket vključimo z ukazom `\usepackage[⟨nastavitve⟩]{⟨ime-paketa⟩}`.
Za besedilo v slovenščini v preambulo vključimo tri pakete:

```tex
\usepackage[slovene]{babel}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
```

Paket `babel` z nastavitvijo `slovene` poskrbi za deljenje besed in slovenske napise (na primer _Kazalo_),
`inputenc` z nastavitvijo `utf8` pove, v katerem kodiranju je zapisana datoteka,
`fontenc` z nastavitvijo `T1` pa poskrbi, da so šumniki v PDF-ju pravi znaki in ne sestavljeni iz črke in strešice.

LaTeX ima okoli [6000 paketov](https://www.ctan.org). Najbolj uporabni so že vključeni v
distribucijo LaTeXa, ki ste jo namestili na svoj računalnik.

## Vsebina in videz

Tudi v LaTeXu bomo v dokumentu **določili vsebinski pomen** elementov besedila:
z ukazi za nov razdelek, podrazdelek, z okoljem za zapis izreka itd.
Taka vrsta oblikovanja je dosti bolj prijazna uporabniku, sistematična
in prilagodljiva.

Za primer, v LaTeXu vsebinsko oblikujemo besedilo izreka z okoljem `theorem`.
Videz izreka bi lahko oblikovali neposredno, kot spodaj, vendar
bi bilo potem težje skrbeti za to, da vsi izreki izgledajo enako,
da so vsi pravilno oštevilčeni ipd.

```tex
% vsebinsko oblikovanje
\begin{theorem}
  ⟨besedilo izreka⟩
\end{theorem}

% neposredno oblikovanje
\textbf{Izrek 1.1} \textit{⟨besedilo izreka⟩}
```

Še nekaj primerov vsebinskega oblikovanja so posebni ukazi za vsebino, kot so
`section`, `subsection` in `footnote`.
Isto velja za poudarke: nov pojem v besedilu označimo z ukazom `\emph`, ki pove, da je beseda poudarjena,
in ne z ukazom `\textit`, ki pove samo, da je ležeča.

## Pomišljaji, narekovaji in presledki

Nekaj znakov LaTeX stavi drugače, kot jih natipkamo.

* Vezaj je `-`, pomišljaj pa `--`.
  Pomišljaj prepoznamo po tem, da je obdan s presledkoma: ` -- `.
* Slovenske narekovaje dobimo z ``">takole"<`` ali pa ``"`takole"'``.
  Znaka za levi in desni narekovaj nista enaka,
  zato se *ne* piše ``'takole'`` ali ``''takole''``, še posebej pa ne ``"takole"``.
* Za piko, ki ne pomeni konca stavka, na primer v datumu ter za kraticami _npr._ in _t. i._,
  LaTeX naredi prevelik presledek.
  Navaden presledek za piko dobimo z `.\ ` (pika, poševnica nazaj, presledek).
* Vsaka prazna vrstica začne nov odstavek, ki ga LaTeX zamakne.
  Če vrstica po prazni vrstici ne začne novega odstavka (na primer za primerom kode),
  zamik preprečimo z ukazom `\noindent` ali pa prazno vrstico zapolnimo s komentarjem `%`.

## Prevajanje

Datoteko `.tex` v PDF pretvori LaTeXov prevajalnik (mi bomo uporabljali `pdflatex`).
Ponavadi ga je treba pognati večkrat,
da lahko preračuna sklice na izreke in številke strani.
Uporabnik lahko to stori bodisi sam bodisi uporabi program `latexmk`,
ki požene `pdflatex` in nekatere druge programe v sklopu sistema LaTeX.
Celotnemu postopku v angleščini pravijo tudi _build_, zato ga boste pod tem imenom srečali v VSCode.
Razširitev LaTeX Workshop v VSCode požene `latexmk` vsakič, ko datoteko shranite;
prvič pa prevajanje poženete sami, z ukazom _LaTeX Workshop: Build LaTeX project_ iz palete ukazov.
Kako gre prevajanje, kaže statusna vrstica spodaj levo: med prevajanjem piše _↻ Build_, ko se konča, pa se pokaže kljukica ✓.

Najmanjši dokument, ki vam ga bo LaTeX še smiselno prevedel, mora vsebovati
ukaz `\documentclass` in okolje `document`.
Poglejte si, kakšne napake javi LaTeX, če prevajate brez tega: tako jih boste naslednjič prepoznali.

* Napake, ki jih javlja LaTeX, niso vedno razumljive. Med drugim to pomeni, da
  jih je v besedilu težko najti. En način, da si pri tem pomagamo, je ta, da
  dokument pogosto prevedemo.
  Ni narobe, če datoteko shranite (in s tem prevedete) po vsakem do konca napisanem ukazu.
  Tako boste vedeli, da se je napaka pojavila od takrat, ko
  je LaTeX nazadnje uspešno prevedel dokument.
  Pri tem bodite pozorni na to, kaj se dogaja v statusni vrstici.
  Hitrejši boste s <kbd>Ctrl</kbd>+<kbd>S</kbd> (🍎 <kbd>Cmd</kbd>+<kbd>S</kbd>).
* Za vsak LaTeX dokument imejte datoteke spravljene v imeniku, ki vsebuje
  samo datoteke za ta dokument. Ta imenik potem odprite v VSCode.
  Razlog za to je, da LaTeX med prevajanjem naredi množico pomožnih datotek
  (s končnicami `.aux`, `.fdb_latexmk`, `.fls`, `.log`, `.synctex.gz` in podobno),
  ki so za uporabnika večino časa neuporabne.
  Asistenti vam bodo hvaležni (sčasoma pa boste verjetno hvaležni tudi sami sebi).
* V imenih imenikov nad datoteko `.tex` **ne sme biti šumnikov ali presledkov**.
  LaTeX je tako star, da to lahko povzroča težave, še posebej na operacijskem sistemu Windows.

(latex:gitignore)=
### Pomožne datoteke in Git

Pomožnih datotek ne shranjujemo v repozitorij: LaTeX jih naredi ob vsakem prevajanju znova, prav tako PDF.
V glavni imenik repozitorija zato dodamo datoteko [`.gitignore`](git:gitignore), ki Gitu pove, katerih datotek naj ne upošteva.
Vzorec `*.aux` izključi vse datoteke s končnico `.aux`, v vseh imenikih;
enako naredimo za druge pomožne končnice (primer je v plonkcu) in za `*.pdf`.
Izjema so PDF-ji, ki jih v dokument vključimo kot slike:
vsakega izvzamemo z vrstico za `*.pdf`, ki se začne s klicajem, na primer `!slika.pdf`.
V repozitoriju tako ostanejo samo izvorne datoteke: `.tex`, `.bib` in slike.

Datoteka `.gitignore` velja samo za datoteke, ki jim Git še ne sledi.
Pomožna datoteka, ki smo jo zabeležili, preden smo napisali `.gitignore`, ostane v repozitoriju,
dokler je ne pobrišemo in izbrisa ne zabeležimo kot spremembo.
Ko jo LaTeX pri naslednjem prevajanju naredi znova, jo Git zaradi datoteke `.gitignore` prezre.

(latex:urejanje-vscode)=
## Urejanje v VSCode

Podobno kot pri HTML-ju vam bo tudi pri LaTeXu prišla prav paleta ukazov.
Če vanjo napišete `latex surround`, najdete dva ukaza, ki izbrano besedilo obdata z ukazom oziroma okoljem;
podrobneje sta opisana v [plonkcu za paleto ukazov](paleta-ukazov:latex).

Kadar je treba isti popravek narediti na več mestih, sta na voljo dva načina.

* **Več kurzorjev.**
  Označite niz, ki se ponavlja, in v paleti ukazov izberite _Select All Occurrences of Find Match_.
  Ta naredi kurzor za vsako pojavitvijo niza, nato pa vse vrstice uredite hkrati:
  kar natipkate, se zapiše pri vseh kurzorjih.
  Bližnjice za premikanje kurzorjev poiščite v [plonkcu](bliznjice:vscode).
* **Iskanje in zamenjava z regularnimi izrazi.**
  V polju za iskanje (<kbd>Ctrl</kbd>+<kbd>F</kbd>, 🍎 <kbd>Cmd</kbd>+<kbd>F</kbd>)
  vklopite iskanje z regularnimi izrazi (gumb z napisom `.*`)
  in po potrebi razlikovanje velikih in malih črk (gumb `Aa`).
  Del vzorca, ki ga zapišete v oklepaje `()`, si urejevalnik zapomni,
  v polju za zamenjavo pa se nanj sklicujete z `$1` (na drugi oklepaj z `$2` in tako naprej).
  Vzorec `^(.*) % razdelek` tako ujame vrstice, ki se končajo z nizom ` % razdelek`,
  in si zapomni, kar je pred njim; zamenjava `\section{$1}` ujeto besedilo obda z ukazom `\section`.

## 1. naloga: VSCode in LaTeX

Najprej preverimo, ali je vaš urejevalnik pripravljen za delo z
[LaTeX](https://www.latex-project.org)-om.

1. V VSCode odprite imenik `racunalniski-praktikum` v imeniku `rp` (_File_ > _Open Folder_).
   Če repozitorija na tem računalniku še nimate, ga najprej [klonirajte](git:init).
   V njem naredite nov imenik `05-latex`, v tem imeniku še imenik `test`,
   v njem pa novo datoteko `latex-test.tex`, ki jo odprite.
2. Preverite, da spodaj desno v statusni vrstici piše LaTeX;
   če ne, morate verjetno namestiti razširitev LaTeX Workshop.
3. Preverite, da v imenih imenikov nad to datoteko ni nobenih šumnikov ali presledkov.
4. V datoteko `latex-test.tex` prekopirajte spodnje besedilo in jo shranite
   s <kbd>Ctrl</kbd>+<kbd>S</kbd> (🍎 <kbd>Cmd</kbd>+<kbd>S</kbd>).
   ```
   \documentclass{article}
   \begin{document}
   \section*{Pitagorov izrek}
   V pravokotnem trikotniku s katetama \(a\) in \(b\) ter hipotenuzo \(c\) velja
   \[ a^2 + b^2 = c^2 \]
   \end{document}
   ```
5. S paleto ukazov poženite ukaz _LaTeX Workshop: Build LaTeX project_
   in v statusni vrstici počakajte na kljukico ✓.
   V nadaljevanju bi za prevajanje moralo zadoščati, da datoteko shranite.
6. Oglejte si dobljeni rezultat (datoteka `latex-test.pdf`).
7. V urejevalniku spremenite datoteko `latex-test.tex` tako, da bo na koncu enačbe znak za piko `.`.
   Lahko dopišete tudi enačbo z izraženo hipotenuzo `c = ...` (poiščite LaTeX ukaz za koren).
8. Datoteko shranite in si oglejte nov PDF.
9. Če ste na operacijskem sistemu Windows in uporabljate slovensko tipkovnico,
   si preberite [navodila za pisanje posebnih znakov](faq:vscode-latex-si) (če tega še niste naredili).

## 2. naloga: urnik

1. V glavnem imeniku repozitorija naredite nov imenik `latex-pregled` in
   v njem odpakirajte arhiv [`latex-pregled.zip`](05-latex/latex-pregled.zip).
   Te datoteke vam bodo v pomoč pri reševanju nalog.
2. V imenik `05-latex` shranite [datoteke za nalogo Urnik](05-latex/urnik.zip) in jih odpakirajte.
   Besedilo v datoteki `urnik.tex` oblikujte v LaTeXu tako,
   da bo prevedena PDF datoteka čim bolj podobna rešitvi (`urnik-resitev.pdf`).
   Vsebina je že označena z okoljem `document`, vrsta dokumenta pa je že nastavljena na `article`.
   Pri reševanju si pomagajte s pregledno datoteko `1-osnove.tex` v imeniku `latex-pregled`.
3. Velikost strani naj bo `A4`, osnovna velikost pisave pa `10pt`.
4. Prve tri vrstice v okolju `document` so naslov, avtor in datum.
   Zapišite jih kot argumente ukazov `\title`, `\author` in `\date`.
   Shranite in si oglejte PDF: naslova, avtorja in datuma v njem ni več.
   Tako je prav: besedilo, ki ga je LaTeX prej izpisal, ste zamenjali z ukazi,
   ki LaTeXu le povedo, kakšni so naslov, avtor in datum.
5. Za temi ukazi dodajte ukaz `\maketitle`.
   Shranite in si oglejte PDF: naslov, avtor in datum so spet v njem, tokrat oblikovani kot naslov članka.
6. V datoteki so naslovi razdelkov, podrazdelkov in podpodrazdelkov
   označeni s komentarji `% razdelek`, `% podrazdelek` in `% podpodrazdelek`.
   Na vseh mestih uporabite ustrezen ukaz (`section`, `subsection` ali `subsubsection`).
   Uporabite enega od [načinov za urejanje več mest hkrati](latex:urejanje-vscode):
   več kurzorjev ali iskanje in zamenjavo z regularnimi izrazi.
7. Sledite navodilom v komentarjih v datoteki `urnik.tex`.
   Kjer v besedilu najdete dva vprašaja `??`, ju nadomestite z ustreznim
   matematičnim izrazom.
   Dva izraza stojita sama v svoji vrstici: tam uporabite prikazni način, pri vseh ostalih pa vrstičnega.
8. V besedilu je *16* vezajev in pomišljajev, ki so vsi napisani z znakom `-`.
   Pomišljaje popravite, vezaje pa pustite takšne, kot so.
   Popravite lahko vse naenkrat s pomočjo iskanja in zamenjave.
9. Na dveh mestih je del besedila zapisan v dvojnih narekovajih;
   poskrbite, da bodo ti pravilni slovenski.
   Uporabite iskanje in zamenjavo z regularnimi izrazi:
   vzorec iz 6. točke morate samo malo popraviti.
10. Poskrbite, da presledki za pikami, ki ne pomenijo konca stavka, ne bodo
    preveliki. Taki so na primer presledki v datumu ter za kraticami npr. in t.i.
    Pomagate si lahko z iskanjem in zamenjavo z regularnimi izrazi;
    vključite tudi razlikovanje velikih in malih črk.
    Kaj naredi vzorec `\. ([a-z])`?
11. V glavni imenik repozitorija dodajte datoteko `.gitignore`,
    v kateri naštejete pomožne datoteke, ki jih naredi LaTeX (razdelek [Pomožne datoteke in Git](latex:gitignore)).
    Pravilno bo napisana, ko boste med spremembami
    videli samo datoteki `urnik.tex` in `.gitignore`.
12. Zabeležite spremembo in vnose pošljite na GitHub.

## Dodatni viri

* [Learn LaTeX in 30 minutes](https://www.overleaf.com/learn/latex/Learn_LaTeX_in_30_minutes), uvod v LaTeX na strani Overleaf.
* [CTAN](https://www.ctan.org), zbirka paketov za LaTeX z njihovo dokumentacijo.
