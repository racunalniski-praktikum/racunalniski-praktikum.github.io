# Risanje


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

## 1. Shranite datoteke na pravo mesto

Shranite datoteke za to nalogo v svoj repozitorij z vajami.
1.  Shranite in odpakirajte arhiv [zip datoteko](09-risanje/09-risanje.zip) glavni imenik repozitorija.
2.  **Datoteke**, ki se nahajajo v podimeniku `prosojnice2` prestavite v podimenik `prosojnice`,
    v katerem imate datoteke s prejšnjih vaj.
3.  **Imenik** `slike` skupaj z vsebino prestavite v imenik, v katerem ste reševali prejšnje vaje
    (navodilo na vajah je bilo, da ga poimenujte `08-prosojnice`), tako da bo na istem nivoju,
    kot imenik `prosojnice`.
4.  Izbrišite `.zip` datoteko in odpakirani imenik, iz katerega ste prestavili vsebino.
Seveda imate lahko tudi drugačno strukturo imenikov, vendar boste v tem primeru morali biti pazljivi
pri vključevanju datotek v glavno `.tex` datoteko s prosojnicami.

## 2. Konstrukcija pravokotnice

1.  Preberite razdelek o stolpcih v uvodnem tečaju o predstavitvah na
    [Overleaf](https://www.overleaf.com/learn/latex/Beamer_Presentations%3A_A_Tutorial_for_Beginners_(Part_2)—Lists%2C_Columns%2C_Pictures%2C_Descriptions_and_Tables#Columns).
2.  Vključite datoteko `4-stolpci-slike.tex` v glavno datoteko.
3.  Na prosojnici v datoteki `4-stolpci-slike.tex`
    vsebino postavite v dva stolpca tako, da bo v levem besedilo, v desnem pa slika.
    Levi stolpec naj ima širino `0.55\textwidth`, desni pa širino `0.45\textwidth`.
    Slika v desnem stolpcu mora biti poravnana na sredino, kar dosežete z ukazom `centering`.
4.  Popravite ukaze za vključevanje slik, tako da se bodo vključile slike.
    Namig: relativna pot je napačna.
    (Ostalih slik za zdaj še ne odkomentirajte.)
5.  Nastavite izpisovanje navodil in slik za konstrukcijo tako, da se bodo odkrivala kot v rešitvi.
    Vsakemu elementu naštevanja in vsaki sliki dodajte določilo `<predpis>` z ustreznim predpisom.
    Pomagate si lahko z [Overleaf dokumentacijo](https://www.overleaf.com/learn/latex/Beamer_Presentations%3A_A_Tutorial_for_Beginners_(Part_4)—Overlay_Specifications#Overlays_and_text_formatting).

## 3. Risanje s paketom TikZ

1.  V glavni datoteki s prosojnicami vključite paket `tikz`,
    pod njim pa dodajte še ukaz `\usetikzlibrary{math}`.
2.  V datoteki `4-stolpci-slike.tex` prekopirajte celotno prosojnico,
    tako da boste imeli v datoteki dve, eno za drugo.
    V spodnji kopiji prosojnice pobrišite slike
    (obdržite stolpce in poravnavo na sredino).
3.  Odkomentirajte ukaze (obdržite komentarje, ker vam bodo v pomoč)
    na dnu datoteke in jih prestavite v stolpec,
    v katerem so bile prej slike.
    Ukaze obdajte z okoljem `tikzpicture`, prevedite datoteko
    in poskusite razbrati kaj naredijo posamezni ukazi.
4.  Sledite navodilom v komentarjih.
    Kjer je treba, vstavite ukaz `pause`,
    da se bo slika odkrivala postopno kot v rešitvi.

## 4. Graf funkcije s paketom TikZ

1.  V preambuli glavne datoteke vključite ukaz `\usepackage{pgfplots}` in ukaz
    `\usepgfplotslibrary{external}`.
1.  Odkomentirajte še zadnjo prosojnico v datoteki `4-stolpci-slike.tex`.
2.  Med pomožne parametre okolja `axis` dodajte polje `xlabel` z vrednostjo `{$x$}`
    in polje `ylabel` z ustrezno vrednostjo.
3.  [Na strani z dokumentacijo](https://www.overleaf.com/learn/latex/Pgfplots_package)
    poglejte, kako se uporabi ukaz `addplot`.
4.  Dodajte graf funkcije `2^(x - 3)/2^3 + 1`.
5.  Dodajte še legendo s funkcijskim predpisom.

## 5. Postopno odkrivanje tabel

1.  V preambuli glavne datoteke vključite paket `array`
    (ta vsebuje določila, ki jih boste potrebovali pri odkrivanju tabele po stolpcih).
2.  Vključite datoteko `5-beamer-tabele.tex` v glavno datoteko.
3.  V prvi prosojnici v datoteki na ustrezna mesta dodajte ukaz `pause`,
    da se bo tabela postopoma odkrivala kot v rešitvi.
4.  V drugi prosojnici v datoteki poglejte, kako je narejeno delno odkrivanje po stolpcih.
    Z ukazom `onslide` dopolnite delno odkrivanje, da bo narejeno tako, kot v rešitvi.

## 6. Matematika, 2. del

Če vam ostane čas na vajah, sicer pa doma, vadite pisanje matematike v LaTeX-u.

1.  V datoteki `prosojnice.tex` pod razdelek
    Matematika, 2. del vključite ustrezno datoteko.
2.  Za zadnjo prosojnico v datoteki `6-zaporedja-algebra-grupe.tex`
    si pripravite okrajšave za cela, realna in kompleksna števila.
    Definicije teh novih ukazov napišite v preambulo glavne datoteke.
    Lahko jih poimenujete `\ZZ`, `\RR` in `\CC`.
3.  Povsod, kjer v datoteki najdete `??`, vprašaje nadomestite z ustreznim matematičnim izrazom.

Nekaj splošnih napotkov:

* `displaystyle` preklopi v prikazni način v vrstici,
* `textstyle` pa preklopi v vrstični način znotraj okolja, kjer je privzet prikazni.

## Domača naloga

1. Rešite [LaTeX](09-risanje/dn-latex.zip) nalogo,
   da dobite občutek, kako bodo izgledale naloge na izpitu.
   Na pravem izpitu bo morda naloga nekoliko težja, ker boste že več znali.
   Nalogo poskusite rešiti v največ pol ure.
2. Datoteke (`dokument.tex`, `knjiga.bib` in `PerrinPlot2.pdf`)
   stisnite v arhiv z imenom `⟨ime⟩-⟨priimek⟩.zip`
   (ustrezno popravite; če imate v imenu ali priimku kak presledek, ga nadomestite z vezajem `-`) in ga
   [oddajte na učilnico do ponedeljka, 16. decembra 2024, ob 23:55](https://ucilnica.fmf.uni-lj.si/mod/assign/view.php?id=71491).

Točka za domačo nalogo se vam bo upoštevala, če boste pravočasno
oddali pravilno poimenovan arhiv s pravimi datotekami (točka 2).

Datoteke oddane do roka bomo pregledali, da vidite, kako se ocenjuje na izpitu.
