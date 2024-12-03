# Okolja in sklicevanje

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

### Magični kvadrati

Datoteko `magic.tex` pripravite tako, da boste z njo dobili PDF dokument, 
čimbolj podoben datoteki `magic-resitve.pdf`.
Pomagajte si s preglednimi datotekami, ki ste jih na prejšnjih vajah shranili v imenik `latex-pregled`
(predvsem `1-osnove.tex`, `2-matematika.tex`, `3-tabele.tex`in `4-citati.tex`).
Če jih še niste shranili v svoj repozitorij, to naredite zdaj.

Poleg tega si vam morda pridejo prav tudi naslednji viri:

* [tabela matematičnih simbolov](07-okolja-in-sklicevanje/LaTeX_Simboli.pdf),
* **na lastno odgovornost** lahko uporabite orodje [Detexify](https://detexify.kirelabs.org/classify.html) (na primer, ukaza `in` in `epsilon` izpišeta podobna znaka, ampak v vsaki situaciji je samo en od teh znakov pravi),
* [generator tabel](https://www.tablesgenerator.com/) pride včasih prav,
* na portalu [Overleaf](https://www.overleaf.com) je zelo dobra [dokumentacija](https://www.overleaf.com/learn). 

Na koncu vsakega razdelka, predvsem pa, preden zaključite z vajami, naredite _commit_ in _push_.
Pri tej nalogi si pomagajte s preglednimi datotekami.
Kadar v nalogi piše, da preberite del katere od preglednih datotek, 
je ponavadi mišljeno, da preberete `.tex` datoteko in ne prevedene PDF datoteke.
V `.tex` datotekah je namreč veliko koristnih informacih skritih tudi v komentarjih.

#### 1. Uvodne naloge

- V svoj repozitorij v imenik `07-magicni-kvadrati` shranite [datoteke za nalogo Magični kvadrati](07-okolja-in-sklicevanje/magic.zip).
- Rešite prvi sklop nalog (navodila najdete v datoteki `magic.tex`).

#### 2. Okolja AMS

V tem delu boste pripravili in uporabili okolji za definicije in izreke.

1.  Preberite razdelek Izreki in dokazi v datoteki `2-matematika.tex`. 
    Poglejte tudi preambulo te datoteke in bodite pozorni na to, kako sta uporabljena ukaza `theoremstyle` in `newtheorem`.
    Več primerov lahko najdete tudi na 
    [Overleaf-u](https://www.overleaf.com/learn/latex/Theorems_and_proofs#Theorem_styles).
2.  Ukaza `theoremstyle` in `newtheorem` sta v paketu `amsthm`. 
    Preden lahko uporabite ta dva ukaza, morate najprej paket najprej vključiti v preambuli z ukazom `\usepackage{amsthm}`.
3.  V preambuli definirajte okolje `definicija` s slogom `definition`, 
    ki na začetku okolja izpiše besedo `Definicija` in 
    okolje `izrek` s slogom `plain`, ki na začetku okolja izpiše besedo `Izrek`.
4.  Uporabite okolje `definicija`: začetki in konci okolij so v dokumentu 
    že pripravljeni, le še odkomentirati jih morate.
    Ker jih je veliko, uporabite iskanje in zamenjavo: <kbd>Ctrl</kbd>+<kbd>H</kbd> oz. 🍎 <kbd>Cmd</kbd>+<kbd>Option</kbd>+<kbd>F</kbd>.
    Nize `% \begin{definicija}` morate nadomestiti z nizi `\begin{definicija}`, nato pa podobno še s konci okolij.
5.  Okolje za izrek vključite sami, z uporabo palete ukazov in ukaza 
    `latex surround` (podrobnejša navodila pa so v prejšnjih vajah).
    Začetek in konec okolja sta označena s komentarjem (`% Začetek/Konec okolja izrek`).
6.  Označite še dokaz z okoljem `proof` (začetek in konec sta označena s komentarjem `% Začetek/Konec dokaza`).

#### 3. Seznam literature

1.  Preberite datoteko `4-citati.tex` in bodite pozorni na to, 
    kako se v njej uporablja ukaz `cite` ter 
    ukaza `bibliographystyle` in `bibliography`.
2.  V datoteki `magic.tex` je na koncu nekaterih odstavkov komentar 
    `% ključ` (poiščite vse z iskanjem), ki vsebuje enega ali več sklicev.
3.  V teh odstavkih morate zamenjati niz `???` z ukazom `cite` 
    z ustrezen sklic (tisti iz komentarja).
4.  Če zdaj prevedete datoteko, se poglavje literatura še ne izpiše.
    Čisto na koncu dokumenta vam manjkata še ukaza `bibliographystyle` in `bibliography`.
    Uporabite datoteko `magic.bib` in slog `siam`. 

Pogosta napaka je, da uporabite samo ukaza `bibliographystyle` in `bibliography`,
ne da bi uporabili ukaz `cite`. Ker LaTeX v seznamu literature izpiše samo 
literaturo, na katero se skličete v besedilu, se v takem primeru ne izpiše nič.

#### 4. Oblikovanje slik

Oblikujte obe sliki v besedilu (izpustite tisto na prvi strani) z okoljem `figure` (poiščite ukaz `includegraphics`).

1.  Preberite si razdelek *Slike* v datoteki `3-tabele.tex`,
    pri čemer si pozorno oglejte, kako se uporabi okolje `figure`.
2.  Sliki, ki ju oblikujete, označite z okoljem `figure`.
    Pri tem začetku okolja dodajte pomožni parameter `!ht` 
    (v oglatih oklepajih, takoj za `\begin{figure}`, takole: `\begin{figure}[!ht]`), 
    da bo LaTeX sliko z večjo verjetnostjo postavil pod isti odstavek 
    kot v izvorni datoteki.
3.  V okolje `figure` dodajte ukaz `centering` za sredinsko poravnavo.
4.  V okolje dodajte ukaza `caption` (nad ukaz `includegraphics`,
    za napis nad sliko) 
    in `label` z vrednostmi parametrov, kot so napisane v komentarjih.

#### 5. Oblikujte tabelo in prvi magični kvadrat

1.  Preberite si poglavje *Okolji* `table` in `tabular` v datoteki `3-tabele.tex`,
    pri čemer bodite pozorni na to, kako se pravilno gnezdi okolji `table` in `tabular`,
    ter v katerega od njih sodijo ukazi `centering`, `caption` in `label`.
2.  V datoteki poiščite tabelo, ki je označena s komentarjem `% Začetek tabele`
    in njeno vsebino najprej označite z okoljem `tabular`.
    Okolje začnite z `\begin{tabular}{|l|c|c|c|c|c|c|}`: drugi parameter pove, 
    da ima tabela 7 stolpcev, od katerih je prvi levo poravnan (`l` za _left_),
    ostali pa sredinsko (`c` za _centered_`).
3.  V vsaki vrstici tabele ločite celice z znakom `&`.
    Druga celica v prvi vrstici se razteza čez 5 stolpcev, kar naredite z ukazom
    `\multicolumn{5}{|c|}{točna vrednost}` (zdaj lahko izpustite štiri znake `&` v primerjavi z ostalimi vrsticami.)
    Vsako vrstico zaključite z `\\`, ki naj mu sledi še ukaz `hline`, tako da bo na koncu vrstice pisalo `\\\hline`. Ta ukaz izriše vodoravno črto.
4.  Tabelo poravnajte na sredino, dodajte napis nad tabelo in oznako `label` za sklicevanje.
5.  Tabelo polepšajte. Na vsakem koraku si oglejte, kako izgleda PDF.
6.  Najprej vključite paket `booktabs` in pobrišite ukaze `hline`.
7.  Popravite začetek okolja `tabular` na `\begin{tabular}{lcccccc}\toprule`
8.  Popravite celico v glavi, ki je razširjena na 5 stolpcev tako, 
    da bo vrednost drugega parametra ukaza `multicolumn` enaka `c` (namesto `|c|`).
9.  Za prvo vrstico dodajte ukaz `midrule`, za zadnjo vrstico, 
    tik pred koncem okolja `tabular` pa še ukaz `bottomrule`.

Zdaj pa oblikujte še prvi magični kvadrat. 
Ostale boste oblikovali v dodatni nalogi, ko boste definirali novo okolje.

- Z ukazom `tabular` označite vsebino magičnega kvadrata,
- nad okoljem `tabular` dodajte napis in oznako,
- z ukazom `large` lahko povečate številke, ampak boste morali morda za vsebino magičnega kvadrata uporabiti še ukaz `normalsize`,
- vse skupaj označite z okoljem `table`.


#### 6. Sklici in matematični izrazi

1.  Povsod, kjer se v besedilu nahaja `!!`, v besedilo dodajte matematični izraz.
2.  V okoljih `equation` dodajte oznaki, da se boste lahko sklicevali na enačbi
    (vrednosti oznak sta v okoljih v komentarjih).
2.  Povsod, kjer se v besedilu nahaja `??`, dodajte sklic na sliko, tabelo ali enačbo. 
    Kjer potrebujete sklic, na koncu odstavka piše, kateri je pravi.
    -   Za običajne sklice uporabite ukaz `ref`.
    -   Za sklicevanje na enačbe uporabite ukaz `eqref` iz paketa `amsmath` (tega je treba vključiti pred paketom `amsthm`). 
    -   Za stran oznake, na katero se sklicujete, lahko uporabite `pageref`.

#### 7. Definicija novega ukaza za magično konstanto

Polepšajmo oznako $M_2$.
1.  Preberite razdelek Makroji v datoteki `2-matematika.tex`.
2.  Poiščite prvo pojavitev izraza `M_2`.
3.  Oblikujte izraz tako, da bo črka M napisana s pisano črko.
    Kako se to naredi, lahko poiščete v razdelku Osnovna matematika
    v datoteki `2-matematika.tex` (najprej datoteko prevedite in 
    v PDF datoteki poglejte, kje se pojavi kaka pisana črka).
4.  V preambulo napišite osnutek definicije novega ukaza: 
    `\newcommand{\⟨ime-ukaza⟩}{⟨definicija⟩}`.
    Osnutek ukaza popravite tako, da `⟨ime-ukaza⟩` zamenjate z `m`
    (uporabljali ga boste z `\m`), definicijo pa z izrazom, 
    ki ste ga pripravili v prejšnji nalogi.
5.  Zamenjajte vse pojavitve `M_2` z uporabami ukaza `\m`.


#### 8. Definicija novega ukaza: `pojem`

Popestrimo definicije. Definirali bomo nov ukaz `pojem`, s katerim bomo zamenjali ukaze `emph` v definicijah.
Sledite naslednjim korakom. Tako zaporedje lahko uporabite vsakič, ko definirate kak nov ukaz v LaTeX-u.
Predstavljate si lahko, da je ukaz samo okrajšava za tisto, kar napišete v definicijo ukaza.
    

1.  Najprej oblikujte pojem v prvi definiciji. V parameter ukaza `emph` pred besedilo
    dodajte ukaz `\color{purple}`, ki bo barvo spremenil na vijolično.
    Barvo lahko izberete sami, o tem, kako jo uporabite, pa si preberite na [Overleaf-u](https://www.overleaf.com/learn/latex/Using_colours_in_LaTeX).
2.  V preambulo napišite osnutek definicije novega ukaza: 
    `\newcommand{\⟨ime-ukaza⟩}[⟨st-parametrov⟩]{⟨definicija⟩}`. 
    Datoteke še ne prevajajte, ker ta definicija še ni sintaktično pravilna.
    Popravite ime ukaza, tako da zamenjate `⟨ime-ukaza⟩` z `pojem`.
3.  Ukaz bo potreboval samo en parameter (besedilo, ki ga oblikujemo), zato nadomestite
    `⟨st-parametrov⟩` z `1`.
4.  Zamenjajte `⟨definicija⟩` z oblikovanim besedilom iz prve definicije 
    (`\emph{\color{purple}Magični kvadrat}`).
5.  V prvi definiciji pobrišite `\color{purple}` in zamenjajte vse pojavitve ukaza `emph`
    z ukazom `pojem`, ki ste ga ravno definirali.
    LaTeX bo med prevajanjem nadomestil vse pojavitve ukaza `pojem` (in parametrov)
    s tistim, kar ste napisali v definicijo novega ukaza.
6.  Če prevedete datoteko in pogledate pdf, boste opazili, da so zdaj vsi pojmi `Magični kvadrat`! To lahko popravite tako, da v definiciji ukaza besedilo `Magični kvadrat` nadomestite z `#1`. LaTeX namreč zamenja `#1` v definiciji ukaza z vrednostjo 1. parametra (pa tudi `#2` z vrednostjo 2. parametra, itd., če bi imeli več kot en parameter).


#### Dodatna naloga: definicije novih okolij (`dokaz` in `magic`)

Kot zdaj že veste, okolja v LaTeX-u uporabljamo takole:

```tex
\begin{⟨ime-okolja⟩} % začetek okolja
⟨vsebina⟩
\end{⟨ime-okolja⟩} % konec okolja
```

Z ukazom `newenvironment` lahko definiramo novo okolje tako, da podamo naslednje tri parametre:
- prvi parameter je ime okolja (npr. `document` ali `table`).
- drugi parameter definira vse, kar gre pred vsebino,
- tretji parameter pa definira vse, kar gre za vsebino.
Predstavljate si lahko, da LaTeX med prevajanjem zamenja vse pojavitve `\begin{⟨ime-okolja⟩}` z vsebino drugega parametra, vse pojavitve `\end{⟨ime-okolja⟩}` pa z vsebino tretjega parametra.
Več o tem, kako se definira novo okolje, si preberite v poglavju [Environments](https://www.overleaf.com/learn/latex/Environments) na Overleafu.

Pisanje novih okolij je lahko zahtevno, zato si ga lahko takole razbijemo na manjše korake:

* **[K1]** *Preden se lotite pisanja ukaza za novo okolje, oblikujte samo en del vsebine, kjer boste novo okolje kasneje uporabili*.
* **[K2]** *V preambuli pripravite ukaz za novo okolje, nato pa v drugi in tretji parameter kopirajte ukaze iz oblikovanega dela vsebine.*
* **[K3]** *V oblikovanem delu vsebine zamenjajte tisto, kar ste napisali v drugi parameter z ukazom `\begin{⟨ime-okolja⟩}`, konec pa z ukazom `\end{⟨ime-okolja⟩}`.*
* **[K4]** *Definiramo morebitne parametre okolja.*

##### 1. Okolje `dokaz`

Oblikujte dokaz izreka z novim okoljem `dokaz`.
To okolje naj bo kar enako okolju `proof` iz paketa `amsthm`, le da namesto besede *"Dokaz"* piše *"Dokaz izreka"*.

1. **[K1]** Na spletu poiščite, kako se naredi dokaz s poljubnim besedilom namesto besede Dokaz. Poglejte, kakšne rezultate dobite za iskanje `latex proof custom text`.
2. Sledite korakoma **[K2]** in **[K3]**.

##### 2. Okolje `magic`

Definirajte novo okolje `magic` s tremi parametri: velikost kvadrata, opis tabele in ime tabele (za sklicevanje).

* **[K1]** Magični kvadrat ste že oblikovali v eni od prejšnjih nalog.
  Zdaj popravite parameter, v katerem naštejete poravnave stolpcev z določilom `|*{3}{c|}` (namesto `|c|c|c|`). 
  To določilo pomeni, da ima tabela najprej navpično črto (`|`), ki ji sledijo trije sredinsko poravnani stolpci, vsak od katerih ima na desni navpično črto.
  V splošnem lahko določilo napisali takole: `*{⟨n⟩}{⟨poravnave⟩}`, ki `n`-krat ponovi določilo za poravnave iz drugega parametra.
* **[K2]** V preambuli pripravite definicijo novega okolja z ukazom `newenvironment`.
    V drugi parameter kopirajte Bobov začetek: od `\begin{table}` pa do vsebine tabele (`8 & 1 & 6...`, ne pa tudi vsebine), v tretji parameter pa Bobov konec: vse od vsebine tabele (`4 & 9 & 2...`, ne pa tudi vsebine), pa do ukaza `\end{table}`.
* **[K3]** Bobu zdaj zamenjamo začetek z ukazom `\begin{magic}`, konec pa z ukazom `\end{magic}`. Vsebino pustimo pri miru.
* **[K4]** V ukazu `newenvironment` boste morali uporabiti še [dodatni parameter](https://www.overleaf.com/learn/latex/Environments#Defining_environments_with_parameters). Na vrednosti teh parametrov se sklicujete z `#1` za vrednost prvega parametra, `#2` za vrednost drugega parametra, itd.

Zdaj lahko dokončate dokument:

- uporabite okolje `magic` za vse magične kvadrate in
- kjer se v besedilu pojavi niz `?!?` naredite sklic na ustrezen magični kvadrat.

## Domača naloga

1.  Dokončajte vaje, še posebej tiste do dodatne naloge.
2.  Sodelujte z našim botom: če tega še niste naredili, na svojem GitHub repozitoriju dodajte dostop uporabniku
    `ul-fmf-bot` po [navodilih v GitHub dokumentaciji](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-personal-account-on-github/managing-access-to-your-personal-repositories/inviting-collaborators-to-a-personal-repository).
3.  Bot `ul-fmf-bot` bo odprl _issue_ z naslovom "Zapri me",
    v katerem bodo navodila za _commit_, ki ga morate narediti,
    s katerim boste zaprli _issue_ 
    (več o tem v razdelku v [Vprašanja, naloge, težave: _issues_](git:issues) poglavju Git).
    
Točka za domačo nalogo se vam bo upoštevala, 
če bo v vašem repozitoriju (na glavni oz. privzeti veji)
sprememba (oz. _commit_), ki bo zaprl _issue_,
ki ga bo naredil `ul-fmf-bot`, v katerem bo narejena sprememba,
za katero vas bo prosil bot.
Sprememba mora imeti čas med
ponedeljkom, 11. novembra 2024, ob 00:00 in
ponedeljkom, 23. decembra 2024, ob 23:55.
