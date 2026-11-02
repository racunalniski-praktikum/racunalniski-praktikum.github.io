# Slike, enačbe in okolja

`````{admonition} Programska oprema
:class: important
- [LaTeX](namestitev:latex),
- [Visual Studio Code](namestitev:vscode) in
- razširitev [LaTeX Workshop](https://marketplace.visualstudio.com/items?itemName=James-Yu.latex-workshop).
`````

## Nova okolja

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

## 1. naloga: uvodne naloge

Nadaljujemo z nalogo Magični kvadrati iz [prejšnjega poglavja](06-sklicevanje-in-okolja.md).
Datoteka `magic.tex` vsebuje rešitev tamkajšnjih nalog in navodila za nove.
Pripravite jo tako, da boste z njo dobili PDF dokument, čim bolj podoben datoteki `magic-resitev.pdf`.

- V glavni imenik repozitorija odpakirajte arhiv [`07-magicni-kvadrati.zip`](07-slike-enacbe-in-okolja/07-magicni-kvadrati.zip)
  v imenik `07-magicni-kvadrati` z datotekami za nalogo Magični kvadrati.
- Med njimi je slika `slika.pdf`, ki jo boste vključili v dokument.
  Vaša datoteka `.gitignore` izključuje vse PDF-je, zato vanjo za vrstico `*.pdf` dodajte vrstico `!slika.pdf`
  (razdelek [Pomožne datoteke in Git](latex:gitignore)).
- Na začetek dokumenta vključite sliko `slika.pdf` (navodila najdete v datoteki `magic.tex`).

## 2. naloga: oblikovanje slik

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
5.  Povsod, kjer se v besedilu nahaja `??`, dodajte sklic na sliko.
    Kjer potrebujete sklic, na koncu odstavka piše, kateri je pravi.

## 3. naloga: definicija novega ukaza `pojem`

Popestrimo definicije. Definirali bomo nov ukaz `pojem`, s katerim bomo zamenjali ukaz `emph`.
Sledite naslednjim korakom; tako zaporedje lahko uporabite vsakič, ko definirate kak nov ukaz v LaTeX-u.

1.  Najprej oblikujte pojem v prvi definiciji. V argument ukaza `emph` pred besedilo
    dodajte ukaz `\color{purple}`, ki bo barvo spremenil na vijolično.
    Ukaz `color` je v paketu `xcolor`, ki ga vključite v preambuli.
    Barvo lahko izberete sami; kako, piše na [Overleaf-u](https://www.overleaf.com/learn/latex/Using_colours_in_LaTeX).
2.  V preambulo napišite osnutek definicije novega ukaza:
    `\newcommand{\⟨ime-ukaza⟩}[⟨st-argumentov⟩]{⟨definicija⟩}`.
    Dokler so v osnutku oklepaji `⟨⟩`, prevajanje javi napako; to je v redu.
    Popravite ime ukaza, tako da zamenjate `⟨ime-ukaza⟩` z `pojem`.
3.  Ukaz bo potreboval samo en argument (besedilo, ki ga oblikujemo), zato nadomestite
    `⟨st-argumentov⟩` z `1`.
4.  Zamenjajte `⟨definicija⟩` z oblikovanim besedilom iz prve definicije
    (`\emph{\color{purple}Magični kvadrat}`).
5.  V prvi definiciji pobrišite `\color{purple}` in zamenjajte vse pojavitve ukaza `emph`
    z ukazom `pojem`, ki ste ga ravno definirali.
    LaTeX bo med prevajanjem nadomestil vse pojavitve ukaza `pojem` (in argumentov)
    s tistim, kar ste napisali v definicijo novega ukaza.
    `````{admonition} Globalno spreminjanje ukaza `emph` v `pojem`
    :class: important
    Če boste samo globalno zamenjali vse pojavitve `emph` v `pojem`, boste zamenjali tudi tisto v definiciji
    in dobili `\newcommand{\pojem}[1]{\pojem{\color{purple}Magični kvadrat}}`.
    Tu ukaz `pojem` kliče samega sebe, kar pomeni, da naj bi se `\pojem{Magični kvadrat}`
    prevedel v `\pojem{\pojem{\pojem{` v neskončnost (kar v našem končnem svetu ni najbolje).
    Preden dokument prevedete, preverite, da definicija ukaza `\pojem` ne kliče samega sebe, temveč ukaz `\emph`.
    `````
6.  Če prevedete datoteko in pogledate PDF, boste opazili, da so zdaj vsi pojmi `Magični kvadrat`!
    To popravite tako, da v definiciji ukaza besedilo `Magični kvadrat` nadomestite z `#1`.
    LaTeX namreč zamenja `#1` v definiciji ukaza z vrednostjo 1. argumenta
    (pa tudi `#2` z vrednostjo 2. argumenta itd., če bi imeli več kot en argument).
7.  Prevedite in preverite: vsi pojmi so obarvani, vsak s svojim besedilom,
    tudi *Lo Shu* in *Kubera-Kolam* v razdelku o zgodovini.
8.  Zabeležite spremembe.

## 4. naloga: novi okolji `dokaz` in `magic`

### Okolje `dokaz`

Oblikujte dokaz izreka z novim okoljem `dokaz`.
To okolje naj bo kar enako okolju `proof` iz paketa `amsthm`, le da namesto besede *"Dokaz"* piše *"Dokaz izreka"*.

1. **[K1]** Na spletu poiščite, kako se naredi dokaz s poljubnim besedilom namesto besede Dokaz. Poglejte, kakšne rezultate dobite za iskanje `latex proof custom text`.
2. Sledite korakoma **[K2]** in **[K3]**.

### Okolje `magic`

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
