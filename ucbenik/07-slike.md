# Slike

`````{admonition} Programska oprema
:class: important
- [LaTeX](namestitev:latex),
- [Visual Studio Code](namestitev:vscode) in
- razširitev [LaTeX Workshop](https://marketplace.visualstudio.com/items?itemName=James-Yu.latex-workshop).
`````

## Novi ukazi in okolja

Ukaze brez argumentov, kot je `\m` v preambuli datoteke `magic.tex`, že znate definirati.
Ukaz ima lahko tudi argumente: njihovo število napišete v oglatih oklepajih za imenom ukaza, v definiciji pa se na prvi argument sklicujete z `#1`, na drugega z `#2` in tako naprej.
LaTeX med prevajanjem vsako pojavitev ukaza nadomesti z njegovo definicijo, v kateri `#1`, `#2` … zamenja z argumenti.
Če definirate

```tex
\newcommand{\abs}[1]{|#1|}
```

LaTeX zapis `\abs{x - y}` nadomesti z `|x - y|`.

Okolja uporabljate takole:

```tex
\begin{⟨ime-okolja⟩} % začetek okolja
⟨vsebina⟩
\end{⟨ime-okolja⟩} % konec okolja
```

Novo okolje definirate z ukazom `newenvironment`, ki ima tri argumente: ime okolja, ukaze, ki gredo pred vsebino, in ukaze, ki gredo za vsebino.
LaTeX med prevajanjem vsako pojavitev `\begin{⟨ime-okolja⟩}` nadomesti z drugim argumentom, vsako pojavitev `\end{⟨ime-okolja⟩}` pa s tretjim.
Tudi okolje ima lahko argumente: njihovo število napišete v oglatih oklepajih za imenom okolja, nanje pa se sklicujete z `#1`, `#2` in tako naprej, vendar samo v drugem argumentu.
Več o tem si preberite v poglavju [Environments](https://www.overleaf.com/learn/latex/Environments) na Overleafu.

Nov ukaz ali okolje najlažje napišete v štirih korakih:

* **[K1]** *Na enem mestu v besedilu oblikujte tisto, kar bo kasneje naredil nov ukaz ali okolje.*
* **[K2]** *V preambuli napišite definicijo novega ukaza ali okolja in vanjo prekopirajte ukaze, s katerimi ste to mesto oblikovali.*
* **[K3]** *Na tem mestu te ukaze zamenjajte z novim ukazom ali okoljem.*
* **[K4]** *Kar se od mesta do mesta spreminja, v definiciji nadomestite z argumenti.*

## Matematična okolja

Paket `amsmath` ima več okolij za zahtevnejše matematične zapise, na primer za matrike, poravnane enačbe in predpise, podane po primerih.
Vsa delujejo podobno kot okolje `tabular`: stolpce ločite z znakom `&`, vrstice pa z `\\`.
Determinanto tako zapišete z okoljem `vmatrix`:

```tex
\[
\begin{vmatrix}
   a & b \\
   c & d
\end{vmatrix} = ad - bc
\]
```

Primere drugih okolij najdete v pregledni datoteki `2-matematika.tex` v imeniku `latex-pregled`, več pa v [Overleafovi dokumentaciji o matrikah](https://www.overleaf.com/learn/latex/Matrices) in v [navodilih za paket `amsmath`](https://ctan.org/pkg/amsmath).

## 1. naloga: uvodne naloge

Nadaljujemo z nalogo Magični kvadrati iz [prejšnjega poglavja](06-sklicevanje-in-definicije.md).
Datoteka `magic.tex` vsebuje rešitev tamkajšnjih nalog in navodila za nove.
Pripravite jo tako, da boste z njo dobili PDF dokument, čim bolj podoben datoteki `magic-resitev.pdf`.

- Pregledne datoteke v imeniku `latex-pregled` in naloga Magični kvadrati naredijo še pomožne datoteke s končnicami `.bbl`, `.blg`, `.idx`, `.ilg`, `.ind`, `.nav`, `.out`, `.snm` in `.toc`.
  Vsebino datoteke `.gitignore` v glavnem imeniku repozitorija zamenjajte s primerom iz razdelka [Datoteka `.gitignore`](git:gitignore) v dodatku o Gitu.
  Na GitHubu preverite, ali ste katero od teh datotek že zabeležili, najverjetneje v imeniku `latex-pregled` ali `06-magicni-kvadrati`; če ste, jo pobrišite in izbris zabeležite.
- V glavni imenik repozitorija odpakirajte arhiv [`07-magicni-kvadrati.zip`](07-slike/07-magicni-kvadrati.zip)
  v imenik `07-magicni-kvadrati` z datotekami za nalogo Magični kvadrati.
- Med njimi je slika `slika.pdf`, ki jo boste vključili v dokument.
  Vaša datoteka `.gitignore` izključuje vse PDF-je, zato vanjo za vrstico `*.pdf` dodajte vrstico `!slika.pdf`
  (razdelek [Pomožne datoteke in Git](latex:gitignore)).
- Na začetek dokumenta vključite sliko `slika.pdf` (navodila najdete v datoteki `magic.tex`).

## 2. naloga: oblikovanje slik

Oblikujte obe sliki v besedilu (izpustite tisto na prvi strani) z okoljem `figure` (poiščite ukaz `includegraphics`).

1.  Preberite si razdelek *Slike* v pregledni datoteki `3-tabele.tex` v imeniku `latex-pregled`,
    pri čemer si pozorno oglejte, kako se uporabi okolje `figure`.
2.  Sliki, ki ju oblikujete, označite z okoljem `figure`.
    Začnite ga z `\begin{figure}[!ht]`, tako kot ste v prejšnjem poglavju začeli okolje `table`.
3.  V okolje `figure` dodajte ukaz `centering` za sredinsko poravnavo.
4.  Pod ukaz `includegraphics` dodajte napis z ukazom `caption`, za njim pa oznako z ukazom `label`, kot sta napisana v komentarjih.
5.  Povsod, kjer se v besedilu nahaja `??`, dodajte sklic na sliko.
    Kjer potrebujete sklic, na koncu odstavka piše, kateri je pravi.

## 3. naloga: definicija novega ukaza `pojem`

Popestrimo definicije. Definirali bomo nov ukaz `pojem`, s katerim bomo v definicijah zamenjali ukaz `emph`.
Pri tem sledite štirim korakom z začetka poglavja, označenim s [K1]–[K4].

1.  **[K1]** Najprej oblikujte pojem v prvi definiciji. V argument ukaza `emph` pred besedilo
    dodajte ukaz `\color{purple}`, ki bo barvo spremenil na vijolično.
    Ukaz `color` je v paketu `xcolor`, ki ga vključite v preambuli.
    Barvo lahko izberete sami; kako, piše na [Overleaf-u](https://www.overleaf.com/learn/latex/Using_colours_in_LaTeX).
2.  **[K2]** V preambulo napišite osnutek definicije novega ukaza:
    `\newcommand{\⟨ime-ukaza⟩}[⟨st-argumentov⟩]{⟨definicija⟩}`.
    Dokler so v osnutku oklepaji `⟨⟩`, prevajanje javi napako; to je v redu.
    Popravite ime ukaza, tako da zamenjate `⟨ime-ukaza⟩` s `pojem`.
3.  **[K2]** Ukaz bo potreboval samo en argument (besedilo, ki ga oblikujemo), zato nadomestite
    `⟨st-argumentov⟩` z `1`.
4.  **[K2]** Zamenjajte `⟨definicija⟩` z oblikovanim besedilom iz prve definicije
    (`\emph{\color{purple}Magični kvadrat}`).
5.  **[K3]** V prvi definiciji pobrišite `\color{purple}`.
    Nato ukaz `emph` v vseh okoljih `definicija` zamenjajte z ukazom `pojem`, ki ste ga ravno definirali, drugje pa ne.
    Ker ne smete zamenjati vseh pojavitev, jih z iskanjem in zamenjavo preglejte eno za drugo.
    -   Odprite iskanje in zamenjavo (<kbd>Ctrl</kbd>+<kbd>H</kbd> oz. 🍎 <kbd>Cmd</kbd>+<kbd>Option</kbd>+<kbd>F</kbd>) in izklopite regularne izraze (gumb `.*`).
    -   V polje za iskanje napišite `\emph`, v polje za zamenjavo pa `\pojem`.
    -   Urejevalnik označi trenutno pojavitev. Če jo želite zamenjati, kliknite gumb _Replace_ ob polju za zamenjavo,
        če jo želite preskočiti, pa puščico navzdol (_Next Match_) ob polju za iskanje.
        V obeh primerih se urejevalnik premakne na naslednjo pojavitev.

    `````{admonition} Ukaz, ki kliče samega sebe
    :class: important
    Pazite, da ukaza `emph` ne zamenjate tudi v preambuli.
    Tako bi dobili definicijo `\newcommand{\pojem}[1]{\pojem{\color{purple}Magični kvadrat}}`,
    v kateri ukaz `pojem` namesto ukaza `emph` kliče samega sebe, in to v nedogled
    (kar v našem končnem svetu ni najbolje).
    Če ukaz `emph` v preambuli po nesreči vseeno zamenjate, se prevajanje ne bo končalo:
    ustavite ga z ukazom _LaTeX Workshop: Kill LaTeX compiler process_ v paleti ukazov,
    v definiciji vrnite `\emph` in prevedite znova.
    `````
6.  **[K4]** Če prevedete datoteko in pogledate PDF, boste opazili, da so zdaj vsi pojmi `Magični kvadrat`!
    To popravite tako, da v definiciji ukaza besedilo `Magični kvadrat` nadomestite z `#1`.
7.  Preverite: vsi pojmi v definicijah so obarvani, vsak s svojim besedilom,
    imeni *Lo Shu* in *Kubera-Kolam* v razdelku o zgodovini pa ostaneta le poševni.

## 4. naloga: novi okolji `dokaz` in `magic`

### Okolje `dokaz`

Oblikujte dokaz izreka z novim okoljem `dokaz`.
To okolje naj bo kar enako okolju `proof` iz paketa `amsthm`, le da namesto besede *Dokaz* piše *Dokaz izreka*.

1. **[K1]** Kako namesto besede *Dokaz* napišete poljubno besedilo, piše v razdelku 5.1 _The beginning of a proof_ [navodil za paket `amsthm`](https://mirrors.ctan.org/macros/latex/required/amscls/doc/amsthdoc.pdf). Tako oblikujte dokaz izreka.
2. Sledite korakoma **[K2]** in **[K3]**.

### Okolje `magic`

Definirajte novo okolje `magic` s tremi argumenti: red kvadrata, opis tabele in ime tabele (za sklicevanje).

* **[K1]** Magični kvadrat reda 3 v razdelku _Uvod_ (tabela `table:mag3`) ste oblikovali že v prejšnjem poglavju.
  Zdaj popravite argument okolja `tabular`, v katerem naštejete poravnave stolpcev z določilom `|*{3}{c|}` (namesto `|c|c|c|`). 
  To določilo pomeni, da ima tabela najprej navpično črto (`|`), ki ji sledijo trije sredinsko poravnani stolpci, vsak z navpično črto na desni.
  V splošnem določilo `*{⟨n⟩}{⟨poravnave⟩}` `n`-krat ponovi poravnave iz drugega argumenta.
* **[K2]** V preambuli pripravite definicijo novega okolja z ukazom `newenvironment`.
    V drugi in tretji argument kopirajte ukaze, ki so v tabeli `table:mag3` označeni s komentarji.
* **[K3]** Označene ukaze v tabeli `table:mag3` skupaj s komentarji zamenjajte z `\begin{magic}` oziroma `\end{magic}`, vrstice kvadrata pa pustite pri miru.
* **[K4]** V ukazu `newenvironment` boste morali določiti še [število argumentov](https://www.overleaf.com/learn/latex/Environments#Defining_environments_which_take_arguments) novega okolja. Na vrednosti argumentov se v definiciji okolja sklicujete z `#1` za prvi argument, `#2` za drugi argument in tako naprej. Argumente napišite tudi tam, kjer okolje uporabite: `\begin{magic}{⟨red⟩}{⟨opis⟩}{⟨ime⟩}`.

Zdaj lahko dokončate dokument:

- uporabite okolje `magic` za vse magične kvadrate in
- kjer se v besedilu pojavi niz `?!?`, naredite sklic na ustrezen magični kvadrat.

## 5. naloga: matematična okolja

V glavni imenik repozitorija odpakirajte arhiv [`07-matematika.zip`](07-slike/07-matematika.zip) v imenik `07-matematika`.
Datoteko `matematika.tex` pripravite tako, da boste z njo dobili PDF dokument, čim bolj podoben datoteki `matematika-resitev.pdf`.
Navodila za posamezne naloge so v komentarjih.
Če vam zmanjka časa, bomo nalogo dokončali na naslednjih vajah.

Na koncu spremembe zabeležite in vnose pošljite na GitHub.
