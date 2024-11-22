# Uvod v LaTeX

LaTeX je sistem za stavljenje besedila. 
Je pravzaprav prevajalnik, ki LaTeX datoteko s končnico `.tex`, 
ki vsebuje navadno besedilo, označeno s posebnimi okolji in ukazi, 
pretvori v lepo stavljeno besedilo in ga shrani v datoteko PDF s končnico `.pdf`.

LaTeX-ov prevajalnik (mi bomo uporabljali `pdflatex`) je ponavadi treba pognati večkrat, 
da lahko preračuna sklice na izreke in številke strani. 
Uporabnik lahko to stori bodisi sam, bodisi uporabi program `latexmk`, 
ki požene `pdflatex` in nekatere druge programe v sklopu sistema LaTeX. 
Če uporabljate Visual Studio Code, se ob shranjevanju avtomatično požene program `latexmk`.

`````{admonition} Programska oprema
:class: important
- [LaTeX](namestitev:latex),
- [Visual Studio Code](namestitev:vscode) in
- razširitev [LaTeX Workshop](https://marketplace.visualstudio.com/items?itemName=James-Yu.latex-workshop).
`````

## Ukazi in okolja

LaTeX dokumente oblikujemo z _ukazi_ (angl. _command_) in _okolji_ (angl. _environment_), 
kot pri HTML pa lahko uporabljamo tudi _komentarje_.
Ukazom včasih rečemo tudi makroji (angl. _macro_).
Kot do sedaj, bodo primeri, ki jih morate še popraviti, napisani takole: `⟨nadomesti-me⟩`.
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

Najprej boste srečali ukaz `documentclass` in okolje `document`

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

Pri teh vajah boste srečali okolja `abstract`, `verbatim` (oznaka ` ``` ` v Markdown-u), 
`itemize` in `enumerate` (znački `ul` in `ol` v HTML).
Tudi za matematični način uporabljamo okolje, in sicer
`math` za vrstičnega in `displaymath` za prikaznega (tako da izraz stoji v svoji vrstici).
Ker bi bilo zelo zamudno pisati `\begin{math}1 + 1\end{math}`, ima LaTeX za ti dve okolji posebni okrajšavi:

```
\[
  ⟨matematični izraz na sredini vrstice⟩
\]
```

ali `\(⟨matematični izraz v vrstici⟩\)`.
Včasih boste morda videli tudi starejši okrajšavi `$$` za prikazni in `$` za vrstični način.
Uporabo teh dveh okrajšav odsvetujemo - ko boste naleteli na napako, jo boste veliko težje razbrali.

`````{admonition} Ukazi za matematične izraze
:class: tip
V matematičnih okoljih lahko uporabljamo ukaze za matematične izraze, 
kot so `frac` za ulomke, `int` za integrale, ukaze za matrike itd. 
Ti ukazi delajo **samo v matematičnih okoljih**, izven njih pa sprožijo napako.
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
Dodatne nastavitve, kot na primer za velikost strani, lahko zapišemo v oglate oklepaje:
`\documentclass[a4paper]{article}`.

V preambulo se nikoli ne piše vsebine, ampak samo ukaze in nastavitve.
V preambuli v dokument vključimo pakete, uredimo nastavitve in definiramo nove makroje in okolja:

* paket vključimo z ukazom `\usepackage[⟨nastavitve⟩]{⟨ime-paketa⟩}`.
* nove ukaze in okolja definiramo z ukazoma `newcommand` in `newenvironment`.

LaTeX ima okoli [6000 paketov](https://www.ctan.org). Najbolj uporabni so že vključeni v
distribucijo LaTeXa, ki ste jo namestili na svojo računalnik.

### Ločevanje vsebine in predstavitve

Tudi v LaTeX-u bomo v dokumentu **določili vsebinski pomen** elementov besedila:
z ukazi za nov razdelek, podrazdelek, z okoljem za zapis izreka, itd.
Taka vrsta oblikovanja je dosti bolj prijazna uporabniku, sistematična
in prilagodljiva.

Za primer, v LaTeX-u vsebinsko oblikujemo besedilo izreka z okoljem `theorem`.
Videz izreka bi lahko oblikovali neposredno, kot spodaj, vendar 
bi bilo potem težje skrbeti za to, da vsi izreki izgledajo enako, 
da so vsi pravilno oštevilčeni, ipd.

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

### Splošna priporočila za urejanje LaTeX dokumentov

* Za vsak LaTeX dokument imejte datoteke spravljene v imeniku, ki vsebuje
  samo datoteke za ta dokument. Ta imenik potem odprite v urejevalniku
  Visual Studio Code. 
  Razlog za to je, da LaTeX med prevajanjem naredi množico datotek, 
  ki so za uporabnika večino časa neuporabne.
  Asistenti vam bodo hvaležni (sčasoma pa boste verjetno
  hvaležni tudi sami sebi).
* Napake, ki jih javlja LaTeX, niso vedno razumljive. Med drugim to pomeni, da
  jih je v besedilu težko najti. En način, da si pri tem pomagamo, je ta, da
  dokument pogosto prevedemo. 
  Ni narobe, če datoteko shranite (in s tem prevedete) po vsakem do konca napisanem ukazu.
  Tako boste vedeli, da se je napaka pojavila od takrat, ko
  je LaTeX nazadnje uspešno prevedel dokument.
  Pri tem bodite pozorni na to, kaj se dogaja v statusni vrstici.
  Hitrejši boste z <kbd>Ctrl</kbd>+<kbd>S</kbd> (🍎 <kbd>Cmd</kbd>+<kbd>S</kbd>).
* Najmanjši dokument, ki vam ga bo LaTeX še smiselno prevedel, mora vsebovati
  ukaz `\documentclass` in okolje `document`. Poglejte si, kakšne napake javi
  LaTeX, če prevajate brez tega: tako jih boste naslednjič prepoznali.

## 1. naloga: VSCode in LaTeX

Najprej preverimo, ali je vaš urejevalnik pripravljen za delo z 
[LaTeX](https://www.latex-project.org)-om. 

1. V VSCode odprite imenik s svojim repozitorijem.
   V njem naredite nov imenik `06-uvod-v-latex`, v tem imeniku še imenik `test`,
   v njem pa novo datoteko `latex-test.tex`, ki jo odprite.
2. Preverite, da spodaj desno v statusni vrstici piše LaTeX;
   če ne, morate verjetno namestiti razširitev LaTeX Workshop.
3. Preverite, da v imenih imenikov nad to datoteko **ni nobenih šumnikov ali presledkov**.
   LaTeX je tako star, da to lahko povzroča težave, še posebej na operacijskem sistemu Windows.
4. V datoteko `latex-test.tex` prekopirajte spodnje navadno besedilo in jo shranite
   s <kbd>Ctrl</kbd>+<kbd>S</kbd> (🍎 <kbd>Cmd</kbd>+<kbd>S</kbd>).
   ```
   \documentclass{article}
   \begin{document}
   \section*{Pitagorov izrek}
   V pravokotnem trikotniku s katetama \(a\) in \(b\) ter hipotenuzo \(c\) velja
   \[ a^2 + b^2 = c^2 \]
   \end{document}
   ```
5. S paleto ukazov poženite ukaz _LaTeX Workshop: Build LaTeX project_.
   Poglejte spodaj levo v statusno vrstico.
   Na desni strani bi moralo pisati _↻ Build_, ko se prevajanje konča, pa bi morali videti kljukico ✓.
   V nadaljevanju bi za prevajanje moralo zadoščati, da datoteko shranite z bližnjico
   <kbd>Ctrl</kbd>+<kbd>S</kbd> (🍎 <kbd>Cmd</kbd>+<kbd>S</kbd>).
6. Oglejte si dobljeni rezultat (datoteka `latex-test.pdf`).
7. V urejevalniku spremenite datoteko `latex-test.tex` tako, da bo na koncu enačbe znak za piko `.`. 
   Lahko dopišete tudi enačbo z izraženo hipotenuzo `c = ...` (poiščite LaTeX ukaz za koren).
8. Ponovite 5. in 6. korak.
9. Če ste na operacijskem sistemu Windows in uporabljate slovensko tipkovnico, 
   si preberite [navodila za pisanje posebnih znakov](faq:vscode-latex-si) (če tega še niste naredili).

## 2. naloga: urnik 

- V glavnem imeniku repozitorija naredite nov imenik, `latex-pregled` in 
  v njem odpakirajte arhiv [`latex-pregled.zip`](06-uvod-v-latex/latex-pregled.zip).
  Te datoteke vam bodo v pomoč pri reševanju nalog.
- V imenik `06-uvod-v-latex` shranite [datoteke za nalogo Urnik](06-uvod-v-latex/urnik.zip)
- Besedilo v datoteki `urnik.tex` oblikujte v LaTeX-u tako, 
  da bo prevedena PDF datoteka čim bolj podobna rešitvi (`urnik-resitev.pdf`).
  Pri reševanju si pomagajte z uvodno pregledno datoteko.

V datoteki `urnik.tex` je vsebina že označena z okoljem `document`, vrsta
dokumenta pa je že nastavljena na `article`. 

Podobno, kot ste paleto ukazov uporabljali za HTML, vam bo prišla prav tudi zdaj.
V paleti ukazov napišite `latex surround`, in našli boste dva uporabna ukaza,
ki sta nekoliko podrobneje opisana v [plonkcu za paleto ukazov](paleta-ukazov:latex).

Pri nekaterih nalogah se splača uporabiti več kurzorjev hkrati;
bližnjice poiščite v [plonkcu](bliznjice:vscode).

1. Velikost strani naj bo `A4`, osnovna velikost pisave pa `10pt` (to so
   nastavitve za ukaz `documentclass`, ki jih ločite z vejicami).
   Poglejte, kako je to narejeno v datoteki `1-osnove.tex` v imeniku
   `latex-pregled`.

2. V datoteki so naslovi razdelkov, podrazdelkov in podpodrazdelkov
   označeni s komentarji `% razdelek`, `% podrazdelek` in `% podpodrazdelek`.
   Na vseh mestih uporabite ustrezen ukaz (`section`, `subsection` ali `subsubsection`),
   to pa lahko naredite na dva načina, ki sta opisana v spodnjih dveh točkah
   za razdelke, podobno pa popravite še podrazdelke in podpodrazdelke.
    - Uporabite več kurzorjev in ukaz _Select All Occurences of Find Match_ iz palete ukazov
      (več preberite v [plonkcu za paleto ukazov](D-paleta-ukazov)). 
      Izberite niz `% razdelek` in uporabite _Select All Occurences of Find Match_. 
      Ta naredi kurzor za vsako pojavitvijo niza `% razdelek`.
      Zdaj lahko uredite vse vrstice hkrati, tako da:
         1. pobrišete niz `% razdelek` tako da stisnete tipko <kbd>← Backspace</kbd>
            (pa še enkrat, da izbrišete presledek na koncu vrstice),
         2. napišete znak `}` na koncu vrstice,
         3. se postavite na začetek vrstice <kbd>Home</kbd> (🍎 <kbd>Cmd</kbd>+<kbd>←</kbd>) in
         4. napišete `\section{`.
    - Pomagajte si z orodjem _Replace_ iz palete ukazov in regularnimi izrazi, 
      da jih označite kot take. 
      V polju za iskanje (<kbd>Ctrl</kbd> + <kbd>F</kbd> oz. 🍎 <kbd>Cmd</kbd> + <kbd>F</kbd>) 
      izberite možnost za iskanje z regularnimi izrazi (gumb z napisom `.*`).
      Za razdelek uporabite vzorec `^(.*) % razdelek`: poiščemo vrstice, 
      ki se začnejo s poljubnim nizom znakov (tega si zapomnimo, ker je v `()`), 
      ki se nadaljuje točno z nizom znakov ` % razdelek`.
      Za zamenjavo vpišemo `\section{$1}`: niz `$1` se bo zamenjal s tistim, 
      kar se je ujelo z vzorcem `(.*)`.

3. Sledite navodilom v komentarjih v datoteki `urnik.tex`.
   Pomagajte si s pregledno datoteko `1-osnove.tex`.
   Kjer v besedilu najdete dva vprašaja `??`, ju nadomestite z ustreznim 
   matematičnim izrazom. 
   **Pozor:** dva izraza sta zapisana sredinsko poravnano v svoji vrstici:
   tam morate uporabiti prikazni način, ne vrstičnega.
   Piko za množenje dobite z ukazom `\cdot`.
   Običajne besede v matematičnem okolju označite z ukazom `\text`, da se bodo
   pravilno prikazale; ta ukaz potrebuje paket `amsmath`, 
   ki ga morate šele vključiti.

4. V besedilu je *16* vezajev in pomišljajev, ki so vsi napisani z znakom `-`. 
   Pomišljaje napravite širše, vezaje pa pustite takšne kot so. 
   Pomišljaje prepoznate po tem, da so obdani s presledkoma: ` - `. 
   Popravite lahko vse naenkrat s pomočjo iskanja in zamenjave. 
   Pomišljaj v LaTeX-u napišemo z dvema črticama med dvema presledkoma: ` -- `.
    
5. Na dveh mestih je del besedila zapisan v dvojnih narekovajih;
   poskrbite, da bodo ti pravilni slovenski. 
   V LaTeX-u dobimo slovenske narekovaje ``">takole"<`` ali pa ``"`takole"'``. 
   Napačni načini pisanja narekovajev: znaka za levi in desni narekovaj nista enaka, 
   zato se *ne* piše ``'takole'`` ali ``''takole''``. Še posebej pa se ne piše ``"takole"``.
   Uporabite iskanje in zamenjavo z regularnimi izrazi. 
   Vzorec iz ene od prejšnjih nalog morate samo malo popraviti.

6. Poskrbite, da presledki za pikami, ki ne pomenijo konca stavka, ne bodo
   preveliki. Taki so na primer presledki v datumu ter za kraticami npr. in t.i.
   Pomagate si lahko z iskanjem in zamenjavo z regularnimi izrazi.
   Pazite, da boste vključili tudi razlikovanje velikih in malih črk (gumb `Aa`).
   Kaj naredi vzorec `\. ([a-z])`?

7. Preberite si, zakaj in kako se uporablja datoteka [`.gitignore`](git:gitignore).
   LaTeX proizvede množico pomožnih datotek, ki jim ne želimo slediti:
   to so datoteke s končnicami npr. `.aux`, `.fdb_latexmk`, `.fls`, `.log` in `.synctex.gz`.
   Datoteko `.gitignore` shranite v glavni imenik repozitorija. 
   Pravilno bo napisana, ko boste med spremembami
   videli samo datoteki `urnik.tex` in `.gitignore`.
   Spremembi zabeležite in pošljite na strežnik.


## Domača naloga

1. Dokončajte vaje, če jih še niste.

Točka za domačo nalogo se vam bo upoštevala, 
če bo v vašem repozitoriju (na glavni oz. privzeti veji)
prisotna v glavnem imeniku datoteka `.gitignore` in
sprememba (oz. _commit_) datoteke `urnik.tex`,
(ta je lahko tudi prazna, čeprav to odsvetujemo).
V repozitoriju ne sme biti LaTeX-ovih pomožnih datotek.
Sprememba mora imeti čas med
ponedeljkom,  4. novembra 2024, ob 00:00 in
ponedeljkom, 25. novembra 2024, ob 23:55.

Pregledali bomo nekaj oddanih nalog z vaj (datoteke `stran.html` v imeniku `03-html`).
Glavni namen tega je, da dobite povratne informacije, predvsem o najpogostejših napakah.
