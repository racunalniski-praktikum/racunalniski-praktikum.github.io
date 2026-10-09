# Git

`````{admonition} Programska oprema
:class: important
- [ukazna vrstica](namestitev:ukazna),
- [Visual Studio Code](namestitev:vscode).
`````

## Git, orodje za upravljanje različic

Zelo poenostavljeno povedano sistemi za upravljanje različic zapisujejo spremembe v datoteke na tak način, da lahko kadarkoli prikličemo poljubno različico. 
V resnici nam ponujajo še mnogo več, saj med drugim omogočajo:

- povrniti datoteke ali kar celoten projekt v prejšnje stanje, 
- primerjati, kako so se s časom zgodile spremembe, 
- pogledati, kdo je nazadnje kaj spremenil,
- sodelovanje na projektu, kjer lahko več ljudi hkrati ureja iste datoteke.

Taki sistemi so najbolj razširjeni pri programiranju, vendar so koristni tudi drugje.
Na primer, ob zaključevanju diplomskih del brez ustrezne podpore hitro nastanejo datoteke kot `diploma-koncna.tex`, `diploma-koncna2.tex`, `diploma (zadnja).tex`, `diploma (oddana).tex`, itd.

Tekom študija boste pri nekaterih predmetih (upamo pa, da tudi za lastne potrebe) uporabljali orodje [Git](https://git-scm.com), ki je najbolj razširjeno sodobno orodje. 
Urejevalnik [Visual Studio Code](https://code.visualstudio.com/) ima dobro razvito [podporo za Git](https://code.visualstudio.com/docs/editor/versioncontrol#_git-support).

Git pride prav tudi, kadar vaše datoteke ureja umetna inteligenca.
V zgodovini sprememb lahko kadarkoli preveri, kako so bile datoteke videti prej in zakaj so se spremenile.
Kadar kaj pokvari, se lahko vrne k zadnji delujoči različici.

Za začetek si poglejmo nekaj osnovnih izrazov, ki jih bomo uporabljali:

- _delovno drevo_ (angl. _working tree_) je imenik z vsemi datotekami projekta, na katerem smo vklopili upravljanje različic.
- _vnos spremembe_ (krajše _vnos_, angl. _commit_) je osnovna enota upravljanja različic, ki vsebuje zabeleženo stanje datotek skupaj s časom, avtorjem, opisom, podatki o predhodnih vnosih in podobno. Vsak vnos spremembe tvori neko smiselno celoto, na primer popravek enega hrošča, dodatek nove funkcionalnosti, ...
- _repozitorij_ (angl. _repository_ ali _repo_) je zbirka vseh vnosov sprememb.
- _klon_ (angl. _clone_) je ena izmed kopij repozitorija. Ena se običajno nahaja na javnem strežniku (za primer lahko pogledate gradiva za Uvod v programiranje na [GitHubu](https://github.com/matijapretnar/uvod-v-programiranje)), vsak, ki dela na projektu pa ima eno kopijo še v delovnem drevesu (skrito v imeniku `.git`).

## Ko Git odpre urejevalnik

Nekateri ukazi Gita potrebujejo besedilo, ki ga niste napisali v ukazno vrstico:
`git commit` brez možnosti `-m` na primer sporočilo vnosa spremembe, `git pull` pa včasih sporočilo o zlivanju.
Takrat Git kar v ukazni vrstici odpre urejevalnik, ki ste ga izbrali v [nastavitvah](git:nastavitve-uporabnika), pri tem predmetu `nano`:

1. Besedilo napišete ali popravite kot običajno, po njem se premikate s puščicami <kbd>↑↓←→</kbd>.
2. Shranite ga z bližnjico <kbd>Ctrl</kbd>+<kbd>O</kbd> in ime datoteke potrdite z vnašalko.
3. Urejevalnik zaprete z bližnjico <kbd>Ctrl</kbd>+<kbd>X</kbd>, nato Git nadaljuje.

Če urejevalnika niste nastavili, Git morda odpre urejevalnik `vim`.
Iz njega pridete tako, da stisnete <kbd>Esc</kbd>, napišete `:wq` in stisnete vnašalko.

## 1. naloga: prvi koraki z Git-om

Glavni namen te naloge je, da računalnik pripravimo za delo z Git-om, spotoma pa še naprej vadimo uporabo ukazne vrstice. Vsi ukazi so pospremljeni z razlagami, da ne boste imeli občutka, da samo ponavljate magične uroke za učiteljem. 

Naloga predpostavlja, da sedite pri istem računalniku kot na prejšnjih vajah. Če slučajno ni tako, morda kak del naloge ne bo imel smisla (takrat na pomoč pokličite asistenta ali demonstratorja). Imenik `racunalniski-praktikum` boste med nalogo pobrisali in ga nadomestili s klonom.

`````{admonition} Nasvet za pomikanje po ukazni vrstici
:class: tip
Po ukazni vrstici se lahko premikate s puščicami na tipkovnici.
Za pomikanje po trenutni vrstici lahko uporabite puščici <kbd>←</kbd> in <kbd>→</kbd>.
Za pomikanje po zgodovini ukazov lahko uporabite puščici <kbd>↑</kbd> in <kbd>↓</kbd>.
`````

1. V VSCode odprite imenik `rp` (_File_ > _Open Folder_).
   Če vas VSCode vpraša, ali avtorjem imenika zaupate (_Do you trust the authors?_), potrdite, sicer ukazna vrstica ne deluje.
   Odprite še podokno z ukazno vrstico z bližnjico:
   - Windows, slovenska tipkovnica: <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>¸</kbd>, kjer je <kbd>¸</kbd> tipka levo od <kbd>1</kbd>,
   - Windows, angleška tipkovnica: <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>&#96;</kbd>, kjer je <kbd>&#96;</kbd> ista tipka levo od <kbd>1</kbd>,
   - macOS: <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>&#96;</kbd>,
   - druge tipkovnice: bližnjica je izpisana v meniju _Terminal_ ob ukazu _New Terminal_.

   V sistemu Windows preverite, da v podoknu desno zgoraj piše `bash` in ne `powershell`; če ne, [preklopite na Git Bash](faq:vscode-bash).
1. Sledite navodilom za [nastavitve `git`-a](git:nastavitve), da si nastavite uporabniške nastavitve ter SSH ključ.
1. V raziskovalcu odprite datoteko `README.md` v imeniku `racunalniski-praktikum` in na konec razdelka _Bližnjice na tipkovnici_ dodajte vrstice
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
   - `rm -r racunalniski-praktikum`: ukaz `rm` (angl. _remove_) z možnostjo `-r` (angl. _recursive_) pobriše imenik `racunalniski-praktikum` z vsem, kar je ostalo v njem.
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
   Pri prvem kloniranju vas `git` morda vpraša, če zaupate GitHubu (_The authenticity of host can't be established._).
   V tem primeru je treba napisati _yes_, preden se kloniranje izvede.
   Če ste ključ SSH zaščitili z geslom, vas Git vpraša še zanj (_Enter passphrase for key_), enako tudi kasneje ob ukazu `git push`.
   Med tipkanjem gesla se znaki ne izpisujejo: natipkajte ga in stisnite vnašalko.
1. Preverite, da vam je uspelo: ukaz `ls racunalniski-praktikum` mora izpisati `README.md`.
   Nato staro datoteko premaknite nazaj:
   ```shell
   mv README-staro.md racunalniski-praktikum
   ```
1. V VSCode v raziskovalcu z desnim klikom na `README-staro.md` izberite _Select for Compare_, nato z desnim klikom na `README.md` še _Compare with Selected_.
   Urejevalnik prikaže datoteki vzporedno in označi vrstice, v katerih se razlikujeta.
   V `README.md` (na desni) prenesite vse, kar želite obdržati, vsaj vrstice iz 3. koraka, in datoteko shranite.
1. Preverite, ali Git ve, kdo ste:
   ```shell
   cd racunalniski-praktikum
   git config user.email
   ```
   Ukaz `git config user.email` izpiše e-naslov, s katerim Git podpiše vaše vnose sprememb; to mora biti naslov, ki ga uporabljate za GitHub.
   Če ne izpiše ničesar, [uredite nastavitve uporabnika](git:nastavitve-uporabnika), preden nadaljujete.
   Brez nastavitev Git ime in naslov včasih ugane sam, GitHub pa takih vnosov ne poveže z vašim računom.
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
Bodite pozorni, kje boste klonirali repozitorij, poskrbite, da boste ukaz `git clone` pognali v imeniku `rp`.
`````

Navodila naloge so na repozitoriju [git-zgodba](https://github.com/racunalniski-praktikum/git-zgodba).

## Dodatni viri

* [Git Time](https://git.bradwoods.io/), spletna igrica za spoznavanje Gita, ki jo je razvil Brad Woods.
* [Learn Git Branching](https://learngitbranching.js.org), nekoliko naprednejša spletna igra za spoznavanje Gita s poudarkom na delu z vejami.
* [Oh My Git!](https://ohmygit.org), igra za spoznavanje gita, ki kmalu predstavi, kako lahko na datotekah sodeluje več avtorjev.
