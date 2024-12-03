# Utrdimo osnove

`````{admonition} Programska oprema
:class: important
- [ukazna vrstica](namestitev:ukazna),
- [Visual Studio Code](namestitev:vscode).
`````

## 1. naloga: opisovanje vzorcev z regularnimi izrazi

[Regularni izrazi](https://en.wikipedia.org/wiki/Regular_expression) 
(angl. _regular expressions_ ali kratko _regex_) so zaporedja znakov, 
s katerimi lahko opišemo vzorce v navadnem besedilu.

Natančno ujemanje ste gotovo že kdaj videli - to je najbolj enostavna vrsta
regularnega izraza. V besedilu bi lahko poiskali vse pojavitve besede `kuža` z
regularnim izrazom `kuža`. Kaj pa če želite poiskati vse številke v besedilu? To
bi naredili z regularnim izrazom `\d+`: `\d` je vzorec ki predstavlja eno
(katerokoli) števko, `+` pa pomeni eno ali več ponovitev tistega, kar piše pred
znakom.

Obstaja več verzij regularnih izrazov, ki so si precej sorodne, lahko pa se tudi
razlikujejo. Nekatere npr. nimajo posebnega vzorca za števke, tako da je treba
števke opisati z vzorcem `[0-9]`.

Regularni izrazi so lahko sila uporabni, in ta naloga je namenjena temu,
da se z njimi na kratko seznanite. 

Kakih 20 minut rešujte lekcije na spletni strani [RegexOne](https://regexone.com),
na spletni strani [RegexLearn](https://regexlearn.com/learn/regex101), ali pa na obeh.
Na gumb _Continue_ vam ni treba klikniti, dovolj je, da stisnete vnašalko <kbd>↵</kbd>.
Če ste regularne izraze že kdaj uporabljali, se lahko preizkusite v 
[regex križanki](https://regexcrossword.com).

## 2. naloga: ukazna vrstica, urejevalnik in Git

Spodaj so navodila za prvi del te naloge.
Navodila za drugi del boste dobili na naslovu, ki ga boste našli na koncu prvega dela.
Navodila pozorno preberite, včasih bo v njih pisalo kaj, kar boste rabili šele kasneje.
V navodilih bo včasih tudi povezava na bolj podrobna navodila.

`````{admonition} Za napredne uporabnike
:class: tip
Če obvladate ukazno vrstico, urejevalnik in Git, se lahko poskusite skozi nalogo prebiti brez navodil.
`````

 1. Začnite tako, da naložite arhiv (stisnjeni imenik) s [poglavji Visoške kronike](05-utrdimo-osnove/visoska-kronika.zip).
 2. Imenik morate [odpakirati](faq:zip), sicer ne boste mogli nadaljevati.
    V poglavjih Visoške kronike je skrita QR koda, do katere boste prišli v naslednjih korakih.
 3. [Odprite imenik `visoska-kronika` v ukazni vrstici](faq:ukazna-imenik). 
    Z ukazom `pwd` lahko preverite, če ste v pravem imeniku: na koncu poti mora pisati `visoska-kronika`.
 4. Z ukazom `ls` izpišite vsebino direktorija, ki bi morala izgledati približno tako:
    ```bash
    naslovnica.txt  poglavje01.txt  poglavje03.txt  poglavje05.txt  poglavje07.txt  poglavje09.txt  poglavje11.txt  poglavje13.txt
    o-izdaji.txt    poglavje02.txt  poglavje04.txt  poglavje06.txt  poglavje08.txt  poglavje10.txt  poglavje12.txt  poglavje14.txt
    ```
    (Če imate enake datoteke, pa morda v drugem vrstnem redu, je ok.)
 5. Da vidite, kako so videti vrstice s QR kodo, 
    s spodnjim ukazom izpišite vrstice 127-147 iz datoteke `poglavje05.txt`.
    Vrstici, ki se začneta z `#17 ` in `#03 ` vsebujeta vsaka po eno vrstico QR kode.
    ```bash
    head -n 147 poglavje05.txt | tail -n 20
    ```
    Kaj mislite, da naredijo posamezni deli ukaza?
 6. V tem koraku bomo poiskali vse vrstice v datotekah v tem repozitoriju, ki se začnejo z znakom `#`, ki mu sledita dve števki. 
    To naredimo z ukazom `grep` za iskanje z regularnimi izrazi:
    ```bash
    grep -r "#[0-9][0-9]" .
    ```
    - `grep` je ime ukaza,
    - z `-r` ukazu povemo, da želimo preiskati vse datoteke v imeniku (bolj natančno, da iščemo rekurzivno po imeniku),
    - `"#[0-9][0-9]"` je vzorec; tega vedno podamo v narekovajih `"`, vzorec sam pa pomeni, da iščemo pojavitve znaka `#`,
      ki mu sledita dve števki (oz. znaka med `0` in `9`),
    - na koncu z znakom `.` povemo, da preiskujemo trenutni imenik.
 7. Označite in kopirajte vrstice, ki so se izpisale.
    Prilepite jih v novo datoteko v urejevalniku VSCode.
 8. V nadaljevanju boste vrstice uredili naraščajoče po številkah ob znakih `#`.
    Če vrstice uredite naraščajoče zdaj, se bodo uredile po številkah poglavij (ker je to prvo mesto, kjer se razlikujejo).
    Zato moramo pobrisati začetke vrstic:
    - v prvi vrstici postavite kurzor tik pred znak `#`,
    - pod tem kurzorjem naredite kurzorje še v vseh naslednjih vrsticah: <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>↑↓</kbd> (🍎 <kbd>Cmd</kbd>+<kbd>Option</kbd>+<kbd>↑↓</kbd>),
    - stisnite tipko <kbd>Shift</kbd> in jo držite, da se vrnete na začetek vrstice: <kbd>Home</kbd> (🍎 <kbd>Cmd</kbd>+<kbd>←</kbd>),
    - izbrišite začetke vrstic, ki ste jih izbrali.
 9. S paleto ukazov vrstice uredite naraščajoče po abecedi: najprej izberite vse, odprite paleto ukazov (<kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>P</kbd> oz. 🍎 <kbd>Cmd</kbd>+<kbd>Shift</kbd>+<kbd>P</kbd>) in napišite _Sort Lines Ascending_ (ko se ta ukaz pojavi na vrhu seznama, lahko stisnete <kbd>↵</kbd>).
10. Zdaj je QR koda že skoraj prava: počistiti je treba samo še `*`.
    V _Find and Replace_ <kbd>Ctrl</kbd>+<kbd>F</kbd> (🍎 <kbd>Cmd</kbd>+<kbd>F</kbd>) poiščite vse `*` in jih zamenjajte s praznim nizom znakov.
11. Poskenirajte QR kodo. Na naslovu, kamor boste prišli, bo preostanek navodil za to nalogo.
    Na računalniku lahko naredite zajem zaslona (lahko si pomagate s pomočjo za operacijski sistem 
    [Windows](https://support.microsoft.com/en-us/windows/use-snipping-tool-to-capture-screenshots-00246869-1843-655f-f220-97299b865f6b) ali
    [MacOS](https://support.apple.com/en-us/102646)) 
    in uporabite spletno orodje, kot je npr. [QR code reader](https://qrcodedynamic.com/qr-reader)

## 3. naloga: postavite spletno stran

To nalogo lahko naredite tudi doma.

Zdaj ste videli že kar nekaj repozitorijev, ki uporabljajo GitHub-ovo
podporo za postavitev spletne strani: zapiski, ter obe strani, 
ki ste jih obiskali v prejšnji nalogi.
V tej nalogi boste postavili svojo stran.

1. [Naredite nov repozitorij](git:init) z imenom `⟨uporabnisko-ime⟩.github.io`:
   niz `⟨uporabnisko-ime⟩` zamenjajte z vašim uporabniškim imenom na GitHubu.
   Če boste repozitorij poimenovali drugače, bo vaša spletna stran stala
   na drugem naslovu, kot bo zahtevala domača naloga.
   Repozitorij klonirajte z urejevalnikom VSCode.
2. V repozitoriju naredite novo HTML datoteko z imenom `index.html`.
   Ime je pomembno, spletna stran sicer ne bo delovala.
   V datoteko lahko prilepite spodnjo vsebino in jo po želji popravite.
   ```html
   <!DOCTYPE html>
   <html lang="sl">
   <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Moja spletna stran</title>
      <style>
         body {
            font-family: Arial, sans-serif;
            color: #333;
            text-align: center;
            padding: 20px;
         }
         h1 {
            color: #0077cc;
            margin-bottom: 20px;
         }
         p {
            font-size: 1.2em;
            margin-bottom: 10px;
         }
      </style>
   </head>
   <body>
      <h1>Naslov polepša stran</h1>
      <p>Tu lahko kaj napišete, ali pa tudi ne.</p>
   </body>
   </html>
   ```
3. [Zabeležite spremembe](git:osnovni-ukazi) in jih pošljite na strežnik.
4. V brskalniku obiščite svoj repozitorij in pojdite na zavihek _Settings_.
5. V stranskem meniju izberite _Pages_.
6. V razdelku _Build and deployment_ pod _Branch_ izberite glavno vejo
   (`main` ali `master`) in kliknite na gumb _Save_.
7. Čez nekaj časa (do 10 minut) se bo stran posodobila z naslovom 
   vaše spletne strani, ki bi moral biti `⟨uporabnisko-ime⟩.github.io`.
   Pisalo bo _"Your site is live at ..."_.

Če boste urejali katero od datotek spletne strani, ter zabeležene spremembe
poslali na strežnik, se bo v nekaj minutah (ponavadi hitreje, kot v desetih)
posodobila tudi spletna stran.

## Domača naloga

0. Če želite naslednje vaje reševati na svojem računalniku, [namestite LaTeX](namestitev:latex).
1. Preberite si začetek [poglavja o LaTeX-u](06-uvod-v-latex) (do 1. naloge).
2. Če še niste, dokončajte 3. nalogo (postavitev spletne strani) z vaj.
3. Če želite naslednje vaje reševati na svojem računalniku, 
   do naslednjih vaj [namestite LaTeX](namestitev:latex), če ga še niste.

Točka za domačo nalogo se vam bo upoštevala, 
če bo do 18. novembra na naslovu `⟨vase-uporabnisko-ime⟩.github.io`
stala spletna stran.
