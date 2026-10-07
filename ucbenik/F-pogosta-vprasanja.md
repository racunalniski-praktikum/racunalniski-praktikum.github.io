# Pogosta vprašanja

(faq:zip)=
## Arhiviranje

ZIP je format datotek, ki omogoča stiskanje in arhiviranje več datotek v eno samo. 
To pomeni, da lahko vzamemo eno ali več datotek (npr. dokumente, slike, videe) in/ali imenikov in jih zapakiramo v eno samo ZIP datoteko.
To pakiranje vključuje tudi kompresijo, kar pomeni, da datoteke potem zasedejo manj prostora na disku. 
Poleg tega, da datoteke potem zasedejo manj prostora, je to tudi priročen način za pošiljanje ali prenos več datotek naenkrat.

### Windows

Operacijski sistem Windows precej dobro zakriva razlike med stisnjenimi in navadnimi imeniki.
V večini primerov ne boste imeli težav, če ZIP datoteke ne boste odpakirali, sta pa vsaj dve izjemi:
do čudnega obnašanja lahko pride pri HTML in CSS datotekah, ter pri LaTeX datotekah.

Stisnjene imenike prepoznate po zadrgi na ikoni in po končnici ZIP.

Za odpakiranje arhiva desno kliknete na arhiv in izberete "Extract All..."

### MacOS

Odvisno programov, ki jih imate nameščene, morda zadošča že kar, da dvakrat kliknete na arhiv.


(faq:koncnice-skrite)=
## Končnice datotek in skrite datoteke

Končnica imena datoteke (angl. [_filename extension_](https://en.wikipedia.org/wiki/Filename_extension)) je 
tisti del imena datoteke, ki pride za piko `.`.
Končnice datotek omogočajo računalnikom in uporabnikom, da hitro prepoznajo vrsto datoteke. 
Na primer:
- .jpg je slika,
- .docx je Microsoft Word dokument,
- .txt je datoteka z navadnim besedilom.

Moderni operacijski sistemi končnice datotek pogosto skrijejo (takšno je recimo privzeto obnašanje operacijskega sistema Windows) - na primer namesto `cat.jpg` pokaže samo `cat`.
Za večino uporabnikov to morda izboljša uporabniško izkušnjo, nekoliko naprednejšim pa je lahko v napoto.
Upamo, da boste kot študenti te fakultete med slednjimi, če še niste.
Že pri Računalniškem praktikumu boste kdaj želeli vedeti, kakšna je končnica imena datoteke.
Nastavite si torej:

*   Končnice datotek (file extensions) naj bodo vidne.
*   Skrite datoteke (hidden files) naj bodo vidne.

V sistemu Windows v Raziskovalcu odprite meni _View_ > _Show_ in obkljukajte _File name extensions_ in _Hidden items_ (v sistemu Windows 10 sta obe možnosti na zavihku _View_).
Na macOS v Finderju izberite _Finder_ > _Settings_ > _Advanced_ in vklopite _Show all filename extensions_ (v starejših različicah se meni imenuje _Preferences_);
skrite datoteke pokažete ali spet skrijete s <kbd>Cmd</kbd>+<kbd>Shift</kbd>+<kbd>.</kbd>.

(faq:domaci-imenik)=
## Domači imenik

- Na fakulteti (Windows): `/c/Users/⟨fmf-uporabnisko-ime⟩`
- Vaš računalnik (Windows): `/c/Users/⟨domace-uporabnisko-ime⟩`
- MacOS: `/Users/⟨domace-uporabnisko-ime⟩`

Na domači imenik se lahko v ukazni vrstici sklicujete z znakom `~` (tilda).
Na primer, če se želite premakniti v domači imenik, lahko napišete `cd ~`.

(faq:path)=
## Spremenljivke okolja

- *Kako urediti PATH na operacijskem sistemu Windows:* `Settings > System > About > Advanced system settings > Environment Variables > Path`

(faq:vscode-windows)=
## VSCode in Windows

### Odpiranje imenika

Na operacijskem sistemu Windows v programu Explorer (Raziskovalec) desno kliknete na imenik in izberete
"Show more options" in "Open with Code".

(faq:vscode-bash)=
### Izbira privzete ukazne vrstice

Odprite okno z ukazno vrstico (**Terminal** > **New Terminal**).
V spodnjem desnem delu VSCode okna bi se vam moral odpreti nov razdelek z ukazno vrstico. 
Znotraj tega razdelka desno zgoraj poiščite ikone za opravila. 
Če pred ikonami piše `bash`, je to to. Če piše `powershell`, poiščite gumb + in **kliknite na puščico navzdol ki se dotika gumba +**.
Izberite možnost "Select default profile".
Čisto na vrhu VSCode okna bi se moral odpreti meni, v katerem so naštete možnosti za ukazno vrstico.
Kliknite na vrstico, v kateri piše "Git Bash".

(faq:vscode-latex-si)=
### LaTeX in slovenska tipkovnica

Ko delamo s slovensko tipkovnico, v urejevalnik VSCode v načinu dela LaTeX včasih ne delujejo znaki `{`, `}`, `@`, ki jih natipkamo z <kbd>AltGr</kbd>+<kbd>B</kbd>, <kbd>AltGr</kbd>+<kbd>N</kbd> in <kbd>AltGr</kbd>+<kbd>V</kbd>.

Najprej preverite, če sploh morate kaj popraviti. Odprite VSCode in naredite novo datoteko, ki jo poimenujte npr. `test.tex` (važno je, da ima končnico `.tex`).
V datoteko napišite zgornje znake. Če jih lahko napišete, je vse ok, sicer pa berite naprej.

Težava je v tem, da ima VSCode definirane bližnjice (angl. _keyboard shortcut_)
<kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>B</kbd>, <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>N</kbd> in <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>V</kbd> ter še nekatere druge, hkrati pa <kbd>AltGr</kbd> obravnava kot <kbd>Ctrl</kbd>+<kbd>Alt</kbd>. Ko torej pritisnemo <kbd>AltGr</kbd>+<kbd>V</kbd>, to za VSCode pomeni <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>V</kbd> in izvede se ukaz, ki je prirejen tej kombinaciji tipk (ta ukaz je "Build LaTeX project"), namesto da bi vstavil želeni znak `{`.

Težavo odpravimo tako, da v spisku bližnjic odstranimo povezavo <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>B</kbd> (in ostale neželene bližnjice), takole:

1. Odpremo datoteko LaTeX, da se aktivira LaTeX paket.
2. <kbd>Ctrl</kbd>+<kbd>K</kbd> <kbd>Ctrl</kbd>+<kbd>S</kbd>, prikaže se spisek vseh bližnjic.
3. V iskalnik vtipkamo neželeno bližnjico (se pravi, natipkamo besedilo `ctrl+alt+b`)
4. Poiščemo _Build LaTeX Project_ in z desnim gumbkom kliknjemo nanj.
5. Izberemo "remove keyboard binding".

Sedaj bi moral delati znak `{`. Podobno popravimo ostale znake. Mimogrede, "Build LaTeX project" lahko še vedno dobimo, ker je vezan tudi na bližnjico <kbd>Win</kbd>+<kbd>Alt</kbd>+<kbd>B</kbd>. Sicer pa lahko sami dodajamo nove bližnjice v spisku vseh bližnjic.

(faq:ukazna-imenik)=
## Odpiranje ukazne vrstice Git Bash v imeniku

### Windows

V Raziskovalcu desno kliknite na imenik in izberite _Show more options_ > _Open Git Bash here_.
Ukazna vrstica se odpre v tem imeniku.

Lahko pa Git Bash [poženete s tipkovnice](bliznjice:zaganjanje): tedaj se odpre v vašem domačem imeniku, `/c/Users/⟨uporabnisko-ime⟩`, in se v želeni imenik premaknete z `cd`.

V obeh primerih je zadnja vrstica v oknu oblike `$`: to je pozivnik, za katerim pišete ukaze.
Preverite, kje ste: natipkajte `pwd` in pritisnite vnašalko <kbd>↵</kbd>; izpiše se pot do imenika, v katerem ste.
Če ni pravi ali če ne veste, kako naprej, prosite za pomoč.

### MacOS

V Finderju desno kliknite na imenik in izberite _Services_ > _New Terminal at Folder_. Odprlo se bo novo okno z ukazno vrstico.
Zadnja vrstica v oknu bi morala biti oblike `⟨uporabnisko-ime⟩@⟨ime-racunalnika⟩ ⟨imenik⟩ %`.
Za znakom `%` stoji tudi kurzor (angl. *cursor*).
