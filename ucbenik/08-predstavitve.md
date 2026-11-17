# Predstavitve

`````{admonition} Programska oprema
:class: important
- [LaTeX](namestitev:latex),
- [Visual Studio Code](namestitev:vscode) in
- razširitev [LaTeX Workshop](https://marketplace.visualstudio.com/items?itemName=James-Yu.latex-workshop).
`````

## Paket `beamer`

Prosojnice v LaTeXu naredite z razredom dokumenta `beamer`.
Kot do zdaj vsebino pišete v okolje `document`.
Vsako prosojnico napišete v okolje `frame`, njen naslov pa lahko napišete na dva načina:
z ukazom `\frametitle` ali kot argument okolja.

```tex
\documentclass{beamer}

\begin{document}

\begin{frame}
  \frametitle{Naslov prosojnice z ukazom frametitle}
  ⟨vsebina⟩
\end{frame}

\begin{frame}{Naslov prosojnice v argumentu okolja}
  ⟨vsebina⟩
\end{frame}

\end{document}
```

Podatke za naslovno stran nastavite enako kot v članku, z ukazi `\title`, `\author` in `\date`;
prosojnice poznajo še ukaza `\subtitle` za podnaslov in `\institute` za ustanovo.
Ukaze lahko napišete v preambulo ali za `\begin{document}`,
vedno pa pred prosojnico z naslovno stranjo.
To namesto ukaza `\maketitle` izpiše ukaz `\titlepage`, ki ga napišete v svojo prosojnico.
Če datuma ne nastavite, se izpiše današnji; z `\date{}` ga izklopite.

```tex
\title{Kako pripravimo prosojnice}
\subtitle{Prvi koraki}
\author{Ana Novak}
\institute{Fakulteta za matematiko in fiziko}
\date{}

\begin{frame}
  \titlepage
\end{frame}
```

Ukaze `\section` pišite med prosojnicami, nikoli znotraj okolja `frame`.
Iz razdelkov `beamer` sestavi kazalo vsebine, ki ga na prosojnico postavite z ukazom `\tableofcontents`.

Celoten primer prosojnic je v pregledni datoteki `5-prosojnice.tex` v imeniku `latex-pregled`,
več pa piše v [Overleafovi dokumentaciji o paketu `beamer`](https://www.overleaf.com/learn/latex/Beamer).

(predstavitve:odkrivanje)=
## Postopno odkrivanje

Ena prosojnica je lahko v PDF-ju več strani, ki jim pravimo podprosojnice:
vsaka naslednja odkrije nekaj več vsebine.
Najpreprostejši način je ukaz `\pause`: kar mu sledi, se pokaže šele na naslednji podprosojnici.

Natančneje določite odkrivanje s predpisom med oklepajema `<` in `>`,
ki ga napišete med ime ukaza in njegov prvi argument.
Tako `\item<3->` pokaže element seznama od tretje podprosojnice naprej,
`\textbf<2>{beseda}` pa besedo poudari samo na drugi.
Predpis je lahko ena številka (`<4>`), razpon (`<2-5>`),
razpon brez konca ali začetka (`<3->` od tretje naprej, `<-2>` prvi dve)
ali naštevanje (`<3,5>`), pa tudi kombinacija teh.

Če naj se elementi seznama odkrivajo po vrsti, ni treba predpisa dodati vsakemu elementu:
dovolj je, da okolju `itemize` ali `enumerate` dodate neobvezni argument `[<+->]`.

Ukaza `\only` in `\onslide` postavita vsebino samo na izbrane podprosojnice.
Razlikujeta se v tem, kaj naredita na ostalih:

- `\only<1>{vsebina}` na ostalih podprosojnicah ne naredi ničesar, kot da vsebine ne bi bilo;
- `\onslide<2-5>{vsebina}` na ostalih podprosojnicah pusti prazen prostor, kjer bi vsebina stala,
  zato se preostala vsebina ne premika.

(predstavitve:bloki)=
## Bloki

Del vsebine prosojnice lahko poudarite z blokom.
Okolje `block` je namenjeno splošnemu poudarku, `exampleblock` primerom, `alertblock` pa opozorilom.
Razlikujejo se po barvi, vsa pa imajo obvezen argument, naslov bloka.
Naslov lahko izpustite, argumenta pa ne: blok brez naslova ima prazen argument `{}`.

```tex
\begin{exampleblock}{Primer}
  Ukaz \texttt{pause} odkrije vsebino prosojnice po kosih.
\end{exampleblock}

\begin{block}{}
  Ta blok nima naslova.
\end{block}
```

(predstavitve:stolpci)=
## Stolpci

Vsebino prosojnice razdelite v stolpce z okoljem `columns`, v katerem je vsak stolpec svoje okolje `column`.
Okolje `column` ima obvezen argument, širino stolpca, ki jo navadno podate kot del širine besedila,
na primer `0.5\textwidth`.

```tex
\begin{columns}
  \begin{column}{0.5\textwidth}
    ⟨levi stolpec⟩
  \end{column}
  \begin{column}{0.5\textwidth}
    ⟨desni stolpec⟩
  \end{column}
\end{columns}
```

Vsebino stolpca poravnate na sredino z ukazom `\centering` na začetku stolpca.
Več piše v razdelku o stolpcih v [Overleafovem uvodnem tečaju o predstavitvah](https://www.overleaf.com/learn/latex/Beamer_Presentations%3A_A_Tutorial_for_Beginners_(Part_2)—Lists%2C_Columns%2C_Pictures%2C_Descriptions_and_Tables#Columns).

(predstavitve:vkljucevanje)=
## Vključevanje datotek

Daljši dokument je preglednejši, če ga razdelite na več datotek.
Ukaz `\input{⟨pot⟩}` na svoje mesto vstavi vsebino datoteke.
Pot je relativna: pove, kako od imenika z glavno datoteko pridete do vključene datoteke
(o poteh več v [2. poglavju](02-ukazna-vrstica.md)).
Če je datoteka `uvod.tex` v istem imeniku kot glavna datoteka, napišete `\input{uvod.tex}`,
če je v njegovem podimeniku `poglavja`, pa `\input{poglavja/uvod.tex}`.

Relativne glede na imenik z glavno datoteko so poti tudi v vključenih datotekah.
Če datoteka `poglavja/uvod.tex` vključi sliko iz imenika `slike`, ki je poleg glavne datoteke,
je prava pot `slike/graf.png`, ne `../slike/graf.png`.

(predstavitve:tikz)=
## Risanje s paketom TikZ

Če želite risati s paketom TikZ, ga vključite v preambulo z ukazom `\usepackage{tikz}`.
Sliko nato narišete v okolju `tikzpicture`.
Če naj TikZ sam izračuna presečišča črt, potrebujete še knjižnico `intersections`,
ki jo pod paketom vključite z `\usetikzlibrary{intersections}`.

Na [prosojnicah 7. predavanja](https://racunalniski-praktikum.github.io/predavanja/07-slike/prosojnice.pdf)
je koda, ki nariše konstrukcijo pravokotnice.
Presečišča v njej izračuna TikZ, zato slika ostane pravilna, tudi če premaknete izhodiščno točko.
Ukaz `\pause` deluje tudi v okolju `tikzpicture`, vendar sliko odkriva v vrstnem redu,
v katerem so zapisani ukazi.
Koda s predavanja točke nariše čisto na koncu, zato bi se z ukazom `\pause` pokazale zadnje,
čeprav v konstrukciji nastopijo prej.
Kadar se vrstni red odkrivanja ne ujema z vrstnim redom kode,
uporabite ukaz `\onslide` s predpisom, a brez argumenta:
`\onslide<3->` velja za vse ukaze, ki mu sledijo, do naslednjega ukaza `\onslide`.
Poznejši ukaz `\onslide` ima lahko manjšo številko od prejšnjega, na primer `\onslide<1->`.
Predpisa ne pišite neposredno k ukazu za črto z imenom, na primer `\draw<2->[name path=k]`:
na podprosojnicah, kjer črte ni, je TikZ ne pozna in presečišč ne more izračunati.

## Pregledne datoteke in VSCode

V navodilih ne bo vedno pisalo, kako se kaj naredi.
Takrat si pomagajte s preglednimi datotekami in iskanjem po spletu.
Kadar v nalogi piše, naj preberete del katere od preglednih datotek, 
je ponavadi mišljeno, da preberete `.tex` datoteko in ne prevedene PDF datoteke.
V `.tex` datotekah je namreč veliko koristnih informacij skritih tudi v komentarjih.

Pri iskanju informacij v preglednih datotekah si lahko pomagate z
iskanjem po datotekah (prvič v nalogi 1.3.3), do katerega dostopate z bližnjico
<kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>F</kbd> (🍎 <kbd>Cmd</kbd>+<kbd>Shift</kbd>+<kbd>F</kbd>).
Pri tem načinu iskanja se izpiše seznam zadetkov po datotekah.
Če kliknete na vrstico z rezultatom, se bo datoteka na tistem mestu odprla v urejevalniku.

Med izvorno kodo v datoteki `.tex` in PDF-jem v VSCode prehajate z bližnjicami:

|                 | Windows                                     |  macOS                                        |
|:----------------|:-------------------------------------------:|:---------------------------------------------:|
| iz `.tex` v PDF | <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>J</kbd> | <kbd>Cmd</kbd>+<kbd>Option</kbd>+<kbd>J</kbd> |
| iz PDF v `.tex` | <kbd>Ctrl</kbd>+klik                        | <kbd>Cmd</kbd>+klik                           |

`````{admonition} Shranite vaje na strežnik
:class: important
Preden odidete iz predavalnice, spremembe zabeležite in vnose pošljite na GitHub.

V tem poglavju je več nalog, kot jih boste utegnili rešiti med vajami.
Priporočamo, da preostanek naredite doma.
Naloge rešujte po vrsti, saj so pomembnejše na začetku.
`````

## 1. naloga: osnovna struktura dokumenta

1.  V glavni imenik repozitorija odpakirajte arhiv [`08-prosojnice.zip`](08-predstavitve/08-prosojnice.zip) v imenik `08-prosojnice`.
    V vseh nalogah boste datoteko `prosojnice.tex` dopolnjevali tako,
    da bo z njo dobljeni PDF čim bolj podoben datoteki `prosojnice-resitev.pdf`.
2.  Preberite pregledno datoteko `5-prosojnice.tex` v imeniku `latex-pregled`.
    Poiščite uporabe ukaza `documentclass`, ukaza `titlepage` in okolja `frame`.
    Datoteko prevedite in si oglejte, kako se postopoma prikazuje prosojnica z naslovom *Prikažimo vsebino po kosih*.
3.  V datoteki `prosojnice.tex` pripravite preambulo, naslovno stran in kazalo vsebine.
    Navodila so v komentarjih, ki se začnejo na primer z `% Naloga 1.3.2` (za 2. del 3. točke 1. naloge).
4.  Prevedite in poglejte, kje v PDF-ju se pojavijo naslovi razdelkov.

## 2. naloga: vključevanje datotek in postopno odkrivanje

1.  V datoteki `prosojnice.tex` pod razdelek *Paket `beamer`*
    vključite datoteko `prosojnice/2-paket-beamer.tex`
    (razdelek [Vključevanje datotek](predstavitve:vkljucevanje)).
2.  Prevedite datoteko `prosojnice.tex` in primerjajte PDF z vsebino datoteke `2-paket-beamer.tex`.
    Kako so v njej napisani naslovi prosojnic?
3.  Na prosojnicah v datoteki `2-paket-beamer.tex` pripravite postopno odkrivanje in bloke,
    kot piše v komentarjih (razdelka [Postopno odkrivanje](predstavitve:odkrivanje)
    in [Bloki](predstavitve:bloki)).
    Prevajajte datoteko `prosojnice.tex`, čeprav spreminjate datoteko `2-paket-beamer.tex`.

## 3. naloga: postopno odkrivanje enačb

1.  V datoteki `prosojnice.tex` pod razdelek *Paketa `amsmath` in `amsfonts`*
    vključite datoteko `prosojnice/3-odkrivanje-v-okolju-align.tex`.
    Paketa `amsmath` vam ni treba vključiti, ker ga vključi že paket `predavanja`.
2.  Na prosojnici v tej datoteki pripravite postopno odkrivanje enačbe,
    kot piše v komentarju (razdelek [Postopno odkrivanje](predstavitve:odkrivanje)).

## 4. naloga: stolpci in slike

1.  V datoteki `prosojnice.tex` pod razdelek *Stolpci in slike*
    vključite datoteko `prosojnice/4-stolpci-slike.tex`.
2.  Na prosojnici v datoteki `4-stolpci-slike.tex` vsebino postavite v dva stolpca:
    v levega besedilo, v desnega sliko (razdelek [Stolpci](predstavitve:stolpci)).
    Levi stolpec naj ima širino `0.55\textwidth`, desni pa `0.45\textwidth`.
    Sliko v desnem stolpcu poravnajte na sredino.
3.  Popravite pot do slike `fig-1.png`, da se bo slika vključila
    (razdelek [Vključevanje datotek](predstavitve:vkljucevanje)).
    Ostalih slik še ne odkomentirajte.
4.  Odkomentirajte ostale slike in nastavite odkrivanje besedila in slik tako, kot je v rešitvi.
    Vsakemu elementu seznama in vsaki sliki dodajte ustrezen predpis
    (razdelek [Postopno odkrivanje](predstavitve:odkrivanje)).

## 5. naloga: postopno odkrivanje tabel

1.  V preambuli datoteke `prosojnice.tex` vključite paket `array`.
    Ta omogoča določila stolpcev, ki jih potrebujete za odkrivanje tabele po stolpcih.
2.  V datoteki `prosojnice.tex` pod razdelek *Paket `beamer` in tabele*
    vključite datoteko `prosojnice/5-beamer-tabele.tex`.
3.  Na prvi prosojnici v datoteki `5-beamer-tabele.tex` dodajte ukaze `\pause`,
    da se bo tabela odkrivala po vrsticah kot v rešitvi.
4.  Na drugi prosojnici dopolnite odkrivanje po stolpcih, da bo tako kot v rešitvi.
    Stolpce tabele določa argument okolja `tabular`, na primer `{c|cccc}`:
    vsaka črka je en stolpec.
    Paket `array` doda dve določili, ki ju napišete ob črko stolpca:
    `>{⟨koda⟩}` pred črko vstavi kodo na začetek vsake celice tega stolpca,
    `<{⟨koda⟩}` za črko pa na konec vsake celice.
    Tabela z argumentom `{c|>{\onslide<2->}c<{\onslide}ccc}` tako pokaže stolpec A
    šele na drugi podprosojnici, ostale stolpce pa ves čas.
    Ukaz `\onslide<2->` velja za vse, kar mu sledi, tudi za naslednje celice,
    zato ga na koncu stolpca prekliče `\onslide` brez predpisa.
    Podoben primer je v razdelku *Uncovering a Table Columnwise*
    [dokumentacije paketa `beamer`](https://mirrors.ctan.org/macros/latex/contrib/beamer/doc/beameruserguide.pdf).

## 6. naloga: risanje s paketom TikZ

1.  V preambuli datoteke `prosojnice.tex` vključite paket `tikz` in knjižnico `intersections`
    (razdelek [Risanje s paketom TikZ](predstavitve:tikz)).
2.  V datoteki `prosojnice.tex` pod razdelek *Risanje s paketom TikZ*
    vključite datoteko `prosojnice/6-risanje-tikz.tex`.
    V njej je koda s 7. predavanja, ki nariše konstrukcijo pravokotnice.
3.  Z ukazi `\onslide` poskrbite, da se bo konstrukcija odkrivala po korakih kot v rešitvi.
    Vrstic kode ne prestavljajte.
