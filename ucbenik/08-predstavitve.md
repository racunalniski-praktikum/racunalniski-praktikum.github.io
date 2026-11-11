# Predstavitve

`````{admonition} Programska oprema
:class: important
- [LaTeX](namestitev:latex),
- [Visual Studio Code](namestitev:vscode) in
- razširitev [LaTeX Workshop](https://marketplace.visualstudio.com/items?itemName=James-Yu.latex-workshop).
`````

`````{admonition} Shranite vaje na strežnik
:class: important
V tem sklopu je več nalog, kot jih boste utegnili rešiti med vajami.
Priporočamo, da preostanek naredite doma.
Vaje rešujte v vrstnem redu, saj so pomembnejše uvrščene proti začetku.
`````

## 1. Osnovna struktura dokumenta

Datoteko `prosojnice.tex` pripravite tako, da boste z njo dobili PDF dokument, 
čimbolj podoben datoteki `prosojnice-resitev.pdf`.
Preden zaključite z vajami, naredite _commit_ in _push_.

V navodilih ne bo vedno pisalo, kako se kaj naredi.
Takrat si pomagajte s preglednimi datotekami in iskanjem po spletu.
Kadar v nalogi piše, da preberite del katere od preglednih datotek, 
je ponavadi mišljeno, da preberete `.tex` datoteko in ne prevedene PDF datoteke.
V `.tex` datotekah je namreč veliko koristnih informacih skritih tudi v komentarjih.

Pri iskanju informacij v preglednih datotekah si lahko pomagate z
iskanjem po datotekah (prvič v nalogi 2.3), do katerega dostopate z bližnjico
<kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>F</kbd> (🍎 <kbd>Cmd</kbd>+<kbd>Shift</kbd>+<kbd>F</kbd>). Pri tem načinu iskanja se izpiše seznam zadetkov po datotekah.
Če kliknete na vrstico z rezultatom, se bo datoteka na tistem mestu odprla v urejevalniku.

Prehajanje med izvorno kodo v `.tex` datoteki in PDF datoteko v VSCode:

|                 | Windows                                     |  MacOS                                        |
|:----------------|:-------------------------------------------:|:---------------------------------------------:|
| iz `.tex` v PDF | <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>J</kbd> | <kbd>Cmd</kbd>+<kbd>Option</kbd>+<kbd>J</kbd> |
| iz PDF v `.tex` | <kbd>Ctrl</kbd>+klik                        | <kbd>Ctrl</kbd>+klik                          |

1.  Preberite vsebino datoteke `5-prosojnice.tex`.
    Poiščite uporabe ukazov `documentclass`, `titlepage` (ali se kje uporabi ukaz `maketitle`?) in okolja `frame`.
    Datoteko prevedite. Poglejte si, kako se postopoma prikazuje prosojnica z naslovom "Prikažimo vsebino po kosih".
2.  Shranite datoteke za to nalogo v svoj repozitorij z vajami:
    Najlažje bo tako, da [zip datoteko](08-predstavitve/08-prosojnice.zip) shranite v glavni imenik repozitorija,
    jo odpakirate in novo nastali imenik poimenujete `08-prosojnice` (če še ni tako poimenovan).
    Ne pozabite izbrisati zip datoteke.
3.  V datoteki `prosojnice.tex` pripravite preambulo, naslovnico in kazalo vsebine.
    Podrobnejša navodila so v komentarjih v datoteki `prosojnice.tex`;
    komentarji se začnejo npr. takole: `% Naloga 1.3.2` (za 2. del 3. točke 1. naloge).
4.  Opazujte, kako delujejo ukazi `section` - kje v PDF datoteki se pojavijo naslovi razdelkov?
    Kadar delate s paketom `beamer` je pomembno, da so ukazi `section` vedno izven okolij `frame`.
    V nadaljevanju boste videli, da se ti ukazi obnašajo malo drugače, kot ste bili vajeni do sedaj.

## 2. Vključevanje datotek in posebnosti predstavitev

1.  Kadar imamo opravka z velikimi `.tex` datotekami, pride prav, 
    če jih lahko razbijemo na manjše. 
    Tako bomo naredili tudi tokrat.
    Pod ukazom `section` z naslovom Paket `beamer` prilepite ukaz
    `\input{prosojnice/1-paket-beamer.tex}`.
    Ta ukaz vključi vsebino datoteke `1-paket-beamer.tex`, ki se nahaja v imeniku
    `1-paket-beamer.tex`.
    Parametru, ki smo ga podali ukazu `input`, to je `prosojnice/1-paket-beamer.tex`,
    rečemo **relativna pot**, saj podamo navodila, kako od datoteke z ukazom `input` 
    (v tem primer `prosojnice.tex`) pridemo do datoteke, ki jo vključujemo.
    Če bi bila datoteka `1-paket-beamer.tex` v istem imeniku kot datoteka `prosojnice.tex`,
    bi bilo dovolj napisati samo `\input{1-paket-beamer.tex}`.
2.  Prevedite datoteko `prosojnice.tex` in primerjajte spremenjeno vsebino PDF datoteke
    z vsebino datoteke `1-paket-beamer.tex`.
    Bodite pozorni na to, kako so narejeni naslovi prosojnic v tej datoteki
    (to je drugi način, da določimo naslov prosojnice).
3.  V prosojnice v razdelku Paket `beamer` pripravite postopno odkrivanje vsebine.
    Prav vam bodo prišli naslednji ukazi, okolja in nastavitve.
    -   Ukaz `pause` je najosnovnejši način, da postopoma odkrijemo vsebino.
    -   Bloke vsebine lahko poudarimo z okolji `block`, `exampleblock` in `alertblock`.
        Ta okolja imajo obvezen parameter za naslov (če nočete, da ima prosojnica naslov, ga lahko pustite praznega, oklepaji pa morajo biti tam).
    -   Pogosto obstajajo učinkovitejši načini, da postopoma odkrivamo vsebino.
        Za okolje `itemize` (in podobna okolja) je dovolj, da nastavite dodaten parameter
        `<+->` (v oglatih oklepajih, ker ni obvezen).
    -   Tudi sicer lahko pogosto med ime ukaza in prvi parameter vrinete `<predpis>`,
        recimo `<4>` za določilo, da naj se ukaz prikaže samo na 4. podprosojnici.
    Oblikujte vsebino datoteke `1-paket-beamer.tex` (podrobnejša navodila so v datoteki).
    **Prevajati morate datoteko `prosojnice.tex`, kljub temu, da boste spreminjali datoteko `1-paket-beamer.tex`**.

## 3. Naprednejša okolja za matematiko

Pri oblikovanju prosojnic v tem razdelku vam bosta prišla prav  
naslednja ukaza.
-   Ukaz `only` postavi vsebino samo na eno podprosojnico,
    npr. `\only<1>{vsebina}` postavi besedo `vsebina` samo na prvo podprosojnico,
    na ostalih pa ne naredi nič.
-   Ukaz `onslide` postavi vsebino na prosojnice v podanem razponu,
    npr. `\onslide<2-5>{vsebina}` postavi vsebino na podprosojnice 2-5,
    na vseh ostalih pa pusti prostor, kjer bi ta vsebina sicer stala.
    Uporabljamo lahko tudi predpise `<3->` (od tretje podprosojnice naprej),
    `<-2>` (prvi dve), `<3,5>` (tretja in peta), pa tudi kombinacije teh predpisov.

Tokrat smo paket `amsmath` že vključili (v paketu `predavanja`),
tako da ga vam ni treba posebej vključevati.

1.  V datoteki `prosojnice.tex` pod razdelek 
    *Paketa `amsmath` in `amsfonts`* vključite ustrezno datoteko.
2.  Oblikujte matematično vsebino na prosojnicah v tem razdelku.
    Podrobnejša navodila so v datoteki.

## 4. Matematika, 1. del

Če vam ostane čas na vajah, sicer pa doma, vadite pisanje matematike v LaTeX-u.

1.  V datoteki `prosojnice.tex` pod razdelek 
    "Matematika, 1. del" vključite ustrezno datoteko.
2.  Povsod, kjer v datoteki najdete `??`, vprašaje nadomestite z ustreznim matematičnim izrazom.
