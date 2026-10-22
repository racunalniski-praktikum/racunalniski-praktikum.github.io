# Upravljanje različic

`````{admonition} Programska oprema
:class: important
- [ukazna vrstica](namestitev:ukazna),
- [Visual Studio Code](namestitev:vscode).
`````

## Git, orodje za upravljanje različic

Zelo poenostavljeno povedano sistemi za upravljanje različic shranjujejo stanja datotek na tak način, da lahko kadarkoli prikličemo poljubno različico.
V resnici nam ponujajo še mnogo več, saj med drugim omogočajo:

- povrniti datoteke ali kar celoten projekt v prejšnje stanje,
- pogledati, kaj natanko se je spremenilo med dvema različicama,
- pogledati, kdo je kaj spremenil in kdaj,
- sodelovanje na projektu, kjer lahko več ljudi hkrati ureja iste datoteke.

Najbolj jih potrebujemo takrat, ko datotek ne spreminjamo samo mi.
Kadar vaše datoteke ureja umetna inteligenca, lahko v enem koraku prepiše celo datoteko, tudi tam, kjer tega niste želeli.
Z Gitom vidite, katere vrstice je spremenila, in se po potrebi vrnete na prejšnjo različico; brez njega je edina kopija tista, ki jo je pravkar napisala.
Enako velja, kadar na istih datotekah dela več ljudi.
Koristni pa so tudi, kadar delamo sami: ob zaključevanju diplomskih del brez njih hitro nastanejo datoteke kot `diploma-koncna.tex`, `diploma-koncna2.tex`, `diploma (zadnja).tex`, `diploma (oddana).tex`, itd.

Pri tem predmetu in še nekaterih drugih (upamo pa, da tudi za lastne potrebe) boste uporabljali orodje [Git](https://git-scm.com), ki je najbolj razširjeno sodobno orodje za upravljanje različic.
Urejevalnik [Visual Studio Code](https://code.visualstudio.com/) ima dobro razvito [podporo za Git](https://code.visualstudio.com/docs/editor/versioncontrol#_git-support).
Predvsem je pomembno, da se naučite, kaj Git z vašimi datotekami počne, in prebrati, kaj vam sporoča o njihovem stanju.

Za začetek si poglejmo nekaj osnovnih izrazov, ki jih bomo uporabljali:

- _delovno drevo_ (angl. _working tree_) je imenik z vsemi datotekami projekta, na katerem smo vklopili upravljanje različic.
- _vnos spremembe_ (krajše _vnos_, angl. _commit_) je osnovna enota upravljanja različic, ki vsebuje zabeleženo stanje datotek skupaj s časom, avtorjem, opisom, podatki o predhodnih vnosih in podobno. Vsak vnos spremembe tvori neko smiselno celoto, na primer popravek enega hrošča, dodatek nove funkcionalnosti, ...
- _repozitorij_ (angl. _repository_ ali _repo_) je zbirka vseh vnosov sprememb.
- _klon_ (angl. _clone_) je ena izmed kopij repozitorija. Ena se običajno nahaja na javnem strežniku (za primer lahko pogledate gradiva za Uvod v programiranje na [GitHubu](https://github.com/matijapretnar/uvod-v-programiranje)), vsak, ki dela na projektu pa ima eno kopijo še v delovnem drevesu (skrito v imeniku `.git`).

### Ko Git odpre urejevalnik


Nekateri ukazi Gita potrebujejo besedilo, ki ga niste napisali v ukazno vrstico. V takih primerih Git kar v ukazni vrstici odpre urejevalnik, ki ste ga izbrali v [nastavitvah](git:nastavitve-uporabnika).

1. Besedilo napišete ali popravite kot običajno, po njem se premikate s puščicami <kbd>↑↓←→</kbd>.
2. Shranite ga z bližnjico <kbd>Ctrl</kbd>+<kbd>O</kbd> in ime datoteke potrdite z vnašalko.
3. Urejevalnik zaprete z bližnjico <kbd>Ctrl</kbd>+<kbd>X</kbd>, nato Git nadaljuje.

Če še niste nastavili urejevalnika za ukazno vrstico, Git morda odpre urejevalnik `vim`.
Iz njega pridete tako, da stisnete <kbd>Esc</kbd>, napišete `:wq` in stisnete vnašalko.

## 1. naloga: prvi koraki z Gitom

Glavni namen te naloge je, da računalnik pripravimo za delo z Gitom, spotoma pa še naprej vadimo uporabo ukazne vrstice. Vsi ukazi so pospremljeni z razlagami, da ne boste imeli občutka, da samo ponavljate magične uroke za učiteljem. 

Naloga predpostavlja, da sedite pri istem računalniku kot na prejšnjih vajah. Če ni tako in imenika `racunalniski-praktikum` z datoteko `README.md` nimate, v 1. koraku imenik `rp` najprej naredite, 3., 4., 7., 8. in 11. korak preskočite, pred 10. korakom pa vrstice iz 3. koraka dodajte v klonirano datoteko `README.md`.
Imenik `racunalniski-praktikum` boste med nalogo pobrisali in ga nadomestili s klonom.

`````{admonition} Nasvet za pomikanje po ukazni vrstici
:class: tip
Po ukazni vrstici se lahko premikate s puščicami na tipkovnici.
Za pomikanje po trenutni vrstici lahko uporabite puščici <kbd>←</kbd> in <kbd>→</kbd>.
Za pomikanje po zgodovini ukazov lahko uporabite puščici <kbd>↑</kbd> in <kbd>↓</kbd>.
`````

1. V VSCode odprite imenik `rp` (_File_ > _Open Folder_).
   Če vas VSCode vpraša, ali avtorjem imenika zaupate (_Do you trust the authors?_), potrdite, sicer ukazna vrstica ne deluje.
   Odprite še ukazno vrstico: v paleti ukazov (<kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>P</kbd>, 🍎 <kbd>Cmd</kbd>+<kbd>Shift</kbd>+<kbd>P</kbd>) izberite ukaz _Terminal: Create New Terminal in Editor Area to the Side_.
   V sistemu Windows preverite, da na zavihku ukazne vrstice piše `bash` in ne `powershell`; če ne, v paleti ukazov izberite ukaz _Terminal: Select Default Profile_ in nato _Git Bash_, zavihek zaprite in odprite novo ukazno vrstico.
1. Sledite navodilom za [nastavitve `git`-a](git:nastavitve), da si nastavite uporabniške nastavitve ter SSH ključ.
1. V VSCode v pogledu z datotekami (_Explorer_) kliknite imenik `racunalniski-praktikum` in v njem datoteko `README.md`, da se odpre v urejevalniku.
   Na konec razdelka _Bližnjice na tipkovnici_ dodajte vrstice
   ```markdown
   - VSCode paleta ukazov: <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>P</kbd> (🍎 <kbd>Cmd</kbd>+<kbd>Shift</kbd>+<kbd>P</kbd>)
   - Skok na začetek vrstice: <kbd>Home</kbd> (🍎 <kbd>Cmd</kbd>+<kbd>←</kbd>)
   - Premik za eno besedo naprej: <kbd>Ctrl</kbd>+<kbd>→</kbd> (🍎 <kbd>Option</kbd>+<kbd>→</kbd>)
   - Brisanje vrstice: <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>K</kbd> (🍎 <kbd>Cmd</kbd>+<kbd>Shift</kbd>+<kbd>K</kbd>)
   - Pretvorba označenega besedila v velike črke: ukaz _Transform to Uppercase_ v paleti ukazov
   ```
   ter datoteko shranite.
1. Zaporedoma napišite ukaze:
   - `mv racunalniski-praktikum/README.md README-staro.md`: ukaz `mv` (angl. _move_) premakne datoteko, podano s prvim argumentom, na mesto, podano z drugim, pri čemer jo lahko hkrati tudi preimenujemo. V tem primeru datoteko `README.md` iz imenika `racunalniski-praktikum` premakne v trenutni imenik, torej `rp`, in jo preimenuje v `README-staro.md`.
   - `ls racunalniski-praktikum`: preverite, da datoteke `README.md` v imeniku `racunalniski-praktikum` ni več.
     Če izpiše še kakšno datoteko, jo prav tako premaknite v `rp` (`mv racunalniski-praktikum/⟨ime⟩ .`).
   - `rm -r racunalniski-praktikum`: ukaz `rm` (angl. _remove_) z možnostjo `-r` (angl. _recursive_) pobriše imenik `racunalniski-praktikum` z vsem, kar je ostalo v njem, tudi s skritimi datotekami, ki jih ustvari operacijski sistem (npr. `.DS_Store`).
     Datotek ne premakne v koš, ampak jih pobriše za vedno.
1. Kopirajte naslov svojega repozitorija (ki ste ga ustvarili in oddali v 2. domači nalogi) z GitHuba:
    - Odprite stran z vašim repozitorijem v brskalniku in kliknite na zeleni gumb _Code_.
    - Izberite zavihek _Local_, pod njim pa zavihek _SSH_.
    - Kopirajte naslov, ki je videti približno takole:
      `git@github.com:⟨uporabnisko-ime⟩/⟨ime-repozitorija⟩.git`
1. V ukazni vrstici v imeniku `rp` napišite ukaz
   ```shell
   git clone ⟨naslov-iz-zgornje-tocke⟩ racunalniski-praktikum
   ```
   Drugi argument pove, v kateri imenik naj Git klonira repozitorij; brez njega bi se ustvaril nov imenik z imenom repozitorija.
   Če ste ključ SSH zaščitili z geslom, vas Git vpraša zanj (_Enter passphrase for key_), enako tudi kasneje ob ukazu `git push`.
   Med tipkanjem gesla se znaki ne izpisujejo: natipkajte ga in stisnite vnašalko.
   Če vas vpraša, ali zaupate strežniku (_The authenticity of host can't be established._), ste izpustili [preverjanje povezave](git:ssh-preverjanje): napišite `yes` in stisnite vnašalko.
   Če se izpiše `Permission denied (publickey)`, ključ SSH ni pravilno nastavljen; [preverite povezavo z GitHubom](git:ssh-preverjanje) in kloniranje ponovite.
   Datoteka `README-staro.md` vas varno čaka v imeniku `rp`.
1. Preverite, da vam je uspelo: ukaz `ls racunalniski-praktikum` mora izpisati `README.md`.
   Če ne izpiše ničesar, je repozitorij na GitHubu prazen (3. točka 2. domače naloge ni uspela); prosite za pomoč.
   Nato staro datoteko premaknite nazaj:
   ```shell
   mv README-staro.md racunalniski-praktikum
   ```
1. V pogledu z datotekami z desnim klikom na `README-staro.md` izberite _Select for Compare_, nato z desnim klikom na `README.md` še _Compare with Selected_.
   Urejevalnik prikaže datoteki vzporedno in označi vrstice, v katerih se razlikujeta.
   Ob vsaki razliki je med datotekama puščica; s klikom nanjo vrstice z leve prenesete na desno, v `README.md`.
   Prenesite vse, kar želite obdržati, vsaj vrstice iz 3. koraka, in datoteko shranite.
1. Preverite, ali Git ve, kdo ste:
   ```shell
   cd racunalniski-praktikum
   git config user.email
   ```
   Ukaz `git config user.email` izpiše e-naslov, s katerim Git podpiše vaše vnose sprememb; to mora biti naslov, ki ga uporabljate za GitHub.
   Če ne izpiše ničesar, [uredite nastavitve uporabnika](git:nastavitve-uporabnika), preden nadaljujete.
   To nastavitev potrebujete, da bo GitHub povezal vaše vnose sprememb z vašim uporabniškim računom.
1. Spremembo zabeležite in jo pošljite na GitHub (glejte [osnovne ukaze](git:osnovni-ukazi)).
   V ukazni vrstici napišite ukaze
   ```shell
   git status
   git add README.md
   git commit -m "dodaj bližnjice za VSCode"
   git push
   ```
   Ukaz `git status` izpiše stanje repozitorija: `README.md` je med spremenjenimi datotekami (_Changes not staged for commit_), `README-staro.md` pa med datotekami, ki jih Git ne spremlja (_Untracked files_).
   Z `git add` v vnos spremembe vključite samo `README.md`, z `git commit` vnos ustvarite s sporočilom, ki sledi možnosti `-m`, z `git push` pa ga pošljete na GitHub.
1. Pobrišite datoteko `README-staro.md` in preverite stanje repozitorija:
   ```shell
   rm README-staro.md
   git status
   ```
   Git mora izpisati _nothing to commit, working tree clean_.
1. Osvežite stran svojega repozitorija na GitHubu in preverite, da so nove vrstice tam.

## 2. naloga: Patrikova Git zgodba

`````{admonition} Kloniranje repozitorija z nalogo
:class: important
Po 1. nalogi je ukazna vrstica v imeniku `racunalniski-praktikum`. Vrnite se v imenik `rp` z ukazom `cd ..` in s `pwd` preverite, da ste tam, šele nato poženite `git clone`. Zgodba ne sme pristati znotraj vašega repozitorija.
`````

Navodila naloge so v repozitoriju [git-zgodba](https://github.com/racunalniski-praktikum/git-zgodba).

## Dodatni viri

* [Git Time](https://git.bradwoods.io/), spletna igrica za spoznavanje Gita, ki jo je razvil Brad Woods.
* [Learn Git Branching](https://learngitbranching.js.org), nekoliko naprednejša spletna igra za spoznavanje Gita s poudarkom na delu z vejami.
* [Oh My Git!](https://ohmygit.org), igra za spoznavanje gita, ki kmalu predstavi, kako lahko na datotekah sodeluje več avtorjev.
