# Sklicevanje in definicije

`````{admonition} Programska oprema
:class: important
- [LaTeX](namestitev:latex),
- [Visual Studio Code](namestitev:vscode) in
- razširitev [LaTeX Workshop](https://marketplace.visualstudio.com/items?itemName=James-Yu.latex-workshop).
`````

## Magični kvadrati

Datoteko `magic.tex` pripravite tako, da boste z njo dobili PDF dokument, 
čim bolj podoben datoteki `magic-resitev.pdf`.
Pomagajte si s preglednimi datotekami, ki ste jih na prejšnjih vajah shranili v imenik `latex-pregled`
(predvsem `2-matematika.tex`, `3-tabele.tex` in `4-citati.tex`).
Če jih še nimate, v glavni imenik repozitorija odpakirajte arhiv [`latex-pregled.zip`](05-latex/latex-pregled.zip) v imenik `latex-pregled`.

Pregledne datoteke so dokumenti LaTeX, v katerih vsak razdelek na delujočem primeru pokaže eno stvar:
izrek in dokaz, tabelo, sliko, seznam literature.
Razlage so v komentarjih, primeri v besedilu.
Prevedite jih in si oglejte PDF, da vidite, kaj vse znajo;
ko želite vedeti, kako je kaj narejeno, pa odprite datoteko `.tex`.
Kadar v nalogi piše, naj preberete del katere od preglednih datotek, je torej mišljena datoteka `.tex`, ne PDF.

Poleg tega vam morda pridejo prav tudi naslednji viri:

* [tabela matematičnih simbolov](06-sklicevanje-in-definicije/LaTeX_Simboli.pdf),
* **na lastno odgovornost** lahko uporabite orodje [Detexify](https://detexify.kirelabs.org/classify.html) (na primer, ukaza `in` in `epsilon` izpišeta podobna znaka, ampak v vsaki situaciji je samo en od teh znakov pravi),
* [generator tabel](https://www.tablesgenerator.com/) pride včasih prav,
* na portalu [Overleaf](https://www.overleaf.com) je zelo dobra [dokumentacija](https://www.overleaf.com/learn). 

Kjer v besedilu naletite na niz `!!`, ga sproti nadomestite z matematičnim izrazom, ki ga preberete iz `magic-resitev.pdf`:
vrstičnega zapišite med `\(` in `\)`, prikaznega med `\[` in `\]`;
kjer `!!` že stoji v matematičnem načinu, vas na to opozori komentar.
Ločilo, s katerim se stavek konča, sodi v izraz, kot v [5. poglavju](05-latex.md).

Preden odidete iz predavalnice, spremembe zabeležite in vnose pošljite na GitHub.
## 1. naloga: uvodne naloge

- V glavni imenik repozitorija odpakirajte arhiv [`06-magicni-kvadrati.zip`](06-sklicevanje-in-definicije/06-magicni-kvadrati.zip)
  v imenik `06-magicni-kvadrati` z datotekami za nalogo Magični kvadrati.
- Odprite `magic.tex` in jo prevedite.
  Primerjajte PDF z datoteko `magic-resitev.pdf`, da vidite, kaj je treba še narediti.
- Rešite prvi sklop nalog: tri kratke naloge na začetku datoteke, označene s komentarji `% 1. naloga` do `% 3. naloga`.
  Po vsaki prevedite in preverite rezultat.
- Zabeležite spremembe.

## 2. naloga: okolja AMS

V tej nalogi boste pripravili in uporabili okolji za definicije in izreke.

1.  Preberite razdelek *Izreki in dokazi* v datoteki `2-matematika.tex`.
    Poglejte tudi preambulo te datoteke in bodite pozorni na to, kako sta uporabljena ukaza `theoremstyle` in `newtheorem`.
    Več primerov lahko najdete tudi na
    [Overleaf-u](https://www.overleaf.com/learn/latex/Theorems_and_proofs#Theorem_styles).
2.  Ukaza sta v paketu `amsthm`, zato ga vključite v preambuli.
    Nato definirajte okolje `definicija` s slogom `definition`,
    ki na začetku okolja izpiše besedo `Definicija`, in
    okolje `izrek` s slogom `plain`, ki na začetku okolja izpiše besedo `Izrek`.
    Za razliko od pregledne datoteke naj bosta okolji oštevilčeni zaporedno po celem dokumentu,
    vsako s svojim števcem (izpustite argumenta `[section]` in `[izrek]`).
3.  Uporabite okolje `definicija`.
    Začetki in konci okolij so v dokumentu že pripravljeni kot komentarji, le odkomentirati jih morate.
    Ker jih je veliko, to naredite z iskanjem in zamenjavo
    (<kbd>Ctrl</kbd>+<kbd>H</kbd> oz. 🍎 <kbd>Cmd</kbd>+<kbd>Option</kbd>+<kbd>F</kbd>):
    v polje za iskanje napišite `% \begin{definicija}`, v polje za zamenjavo `\begin{definicija}`
    in zamenjajte vse pojavitve (gumb _Replace All_).
    Nato enako ponovite za `% \end{definicija}`.
4.  Izrek označite sami: izberite besedilo med komentarjema `% Začetek okolja izrek` in `% Konec okolja izrek`
    in ga obdajte z okoljem `izrek` s paleto ukazov
    (`latex surround`, ukaz, ki doda `\begin{}` in `\end{}`; opis je v [plonkcu](paleta-ukazov:latex)).
5.  Označite še dokaz z okoljem `proof` (začetek in konec sta označena s komentarjem `% Začetek/Konec dokaza`).
6.  Prevedite in preverite: definicije in izrek morajo biti oštevilčeni, dokaz pa se mora končati s kvadratkom.
7.  Zabeležite spremembe.

## 3. naloga: seznam literature

LaTeX v seznam literature uvrsti samo dela, na katera se v besedilu skličete z ukazom `cite`.
Če uporabite samo ukaza `bibliographystyle` in `bibliography`, se zato ne izpiše nič.

1.  Preberite datoteko `4-citati.tex` in bodite pozorni na to,
    kako se v njej uporablja ukaz `cite` ter
    ukaza `bibliographystyle` in `bibliography`.
2.  V datoteki `magic.tex` poiščite komentarje `% ključ` na koncu odstavkov.
    V teh odstavkih zamenjajte vsak niz `???` z ukazom `cite` s ključem iz komentarja.
    Če je v odstavku več nizov `???`, sodi prvi ključ k prvemu, drugi k drugemu in tako naprej.
3.  Če zdaj prevedete datoteko, se seznam literature še ne izpiše.
    Na mestu komentarja `% Tu vstavite bibliografijo` na koncu dokumenta dodajte ukaza
    `\bibliographystyle{siam}` in `\bibliography{magic}`
    (argument ukaza `bibliography` je ime datoteke `magic.bib` brez končnice).
4.  Prevedite in preverite: seznam literature mora našteti pet virov,
    v besedilu pa namesto `???` stojijo številke v oglatih oklepajih.
5.  Zabeležite spremembe.

## 4. naloga: tabela in magični kvadrat

1.  Preberite si razdelek *Okolji `table` in `tabular`* v datoteki `3-tabele.tex`,
    pri čemer bodite pozorni na to, kako se pravilno gnezdi okolji `table` in `tabular`,
    ter v katerega od njih sodijo ukazi `centering`, `caption` in `label`.
2.  V datoteki poiščite tabelo, ki je označena s komentarjem `% Začetek tabele`,
    in njeno vsebino najprej označite z okoljem `tabular`.
    Okolje začnite z `\begin{tabular}{|l|c|c|c|c|c|c|}`: drugi argument pove,
    da ima tabela 7 stolpcev, od katerih je prvi levo poravnan (`l` za _left_),
    ostali pa sredinsko (`c` za _centered_).
3.  V vsaki vrstici tabele ločite celice z znakom `&`.
    Prva celica v prvi vrstici je prazna (nad *red* in *število kvadratov*), zato se vrstica začne z `&`.
    Druga celica te vrstice se razteza čez 5 stolpcev, kar naredite z ukazom
    `\multicolumn{5}{|c|}{točna vrednost}`; ta vrstica ima zato samo dva znaka `&`.
    Vsako vrstico zaključite z `\\`, ki naj mu sledi še ukaz `hline`, tako da bo na koncu vrstice pisalo `\\\hline`;
    ta ukaz izriše vodoravno črto.
    Za zgornjo črto dodajte `\hline` še takoj za `\begin{tabular}{…}`.
4.  Okolje `tabular` označite z okoljem `table`.
    Okolje začnite z `\begin{table}[!ht]`: dodatek v oglatih oklepajih pove,
    naj LaTeX tabelo postavi sem (`h`, *here*) ali vsaj na vrh strani (`t`, *top*).
    Vanj dodajte ukaz `centering`, napis nad tabelo z ukazom `caption` in oznako z ukazom `label`;
    besedilo napisa in oznaka sta v komentarju nad tabelo.
5.  Tabelo polepšajte s paketom `booktabs`; po vsakem od naslednjih korakov si oglejte PDF.
    Najprej paket vključite in v tej tabeli pobrišite vse ukaze `hline`.
6.  Popravite začetek okolja `tabular` na `\begin{tabular}{lcccccc}\toprule`.
7.  Popravite celico v glavi, ki je razširjena na 5 stolpcev,
    tako da bo drugi argument ukaza `multicolumn` `c` (namesto `|c|`).
8.  Za prvo vrstico dodajte ukaz `midrule`, za zadnjo vrstico,
    tik pred koncem okolja `tabular`, pa še ukaz `bottomrule`.

Zdaj pa oblikujte še magični kvadrat.
Označen je s komentarjem `% Začetek magičnega kvadrata`, napis in oznaka sta v komentarju nad njim.

9.  Odkomentirajte tri vrstice s števili in jih označite z okoljem `tabular`
    s tremi sredinsko poravnanimi stolpci ter navpičnimi in vodoravnimi črtami.
10. Kot pri prejšnji tabeli dodajte okolje `table`, napis in oznako ter poravnavo na sredino.
11. Številke povečajte z ukazom `\large` pred `\begin{tabular}` in `\normalsize` za `\end{tabular}`.
12. Prevedite in preverite: obe tabeli morata biti oštevilčeni in imeti napis nad vsebino.
13. Zabeležite spremembe.

## 5. naloga: sklici

1.  Preberite razdelek *Citati in reference* na koncu datoteke `2-matematika.tex`:
    v njem so uporabljeni vsi trije ukazi za sklicevanje iz te naloge.
2.  V okoljih `equation` dodajte oznaki z ukazom `label`, da se boste lahko sklicevali na enačbi;
    vrednosti oznak sta v komentarjih v okoljih.
3.  Povsod, kjer se v besedilu nahaja `??`, dodajte sklic na tabelo ali enačbo.
    Katera oznaka je prava, piše v komentarju `% sklic` na koncu odstavka.
    -   Za sklice na tabele uporabite ukaz `ref`.
    -   Za sklice na enačbe uporabite ukaz `eqref` iz paketa `amsmath`
        (tega je treba vključiti pred paketom `amsthm`).
    -   Kjer piše *na strani* `??`, uporabite ukaz `pageref`.
4.  Prevedite in preverite: v PDF-ju ne sme ostati noben `??` ali `!!`.
5.  Zabeležite spremembe.

## 6. naloga: definicija novega ukaza za magično konstanto

Polepšajmo oznako $M_2$: definirali boste nov ukaz, ki jo izpiše.
Ukaz si lahko predstavljate kot okrajšavo za tisto, kar napišete v njegovo definicijo.

1.  Preberite razdelek *Makroji* v datoteki `2-matematika.tex`.
2.  Poiščite prvo pojavitev izraza `M_2`.
3.  Oblikujte oznako `M_2` tako, da bo črka M napisana s pisano črko.
    Ukaz poiščite v razdelku *Osnovna matematika* v datoteki `2-matematika.tex`.
4.  V preambulo napišite osnutek definicije novega ukaza:
    `\newcommand{\⟨ime-ukaza⟩}{⟨definicija⟩}`.
    Osnutek popravite tako, da `⟨ime-ukaza⟩` zamenjate z `m`
    (uporabljali ga boste z `\m`), `⟨definicija⟩` pa z oblikovano oznako iz 3. koraka.
5.  Zamenjajte vse pojavitve `M_2` z ukazom `\m`,
    tudi tisto, ki ste jo v 3. koraku oblikovali na roko.
6.  Prevedite in preverite: črka M v oznaki je povsod pisana, tudi v izreku in v prikazani formuli.
7.  Zabeležite spremembe in vnose pošljite na GitHub.
