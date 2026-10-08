# Urejevalnik in Markdown

`````{admonition} Programska oprema
:class: important
- [Visual Studio Code](namestitev:vscode).
`````

`````{admonition} Branje navodil
:class: tip
Priporočamo, da si vsako navodilo najprej natančno preberete do konca.
`````

## Tipkanje

Med študijem boste pisali matematična besedila, programirali in se pogovarjali z umetno inteligenco, zato boste veliko tipkali.
Tipkanje na dotik (znano tudi kot slepo ali desetprstno tipkanje) je slog tipkanja, pri katerem se ne zanašamo na vid, ampak prave tipke najdemo s pomočjo mišičnega spomina.
S tem slogom tipkanja naj bi povprečno lahko dosegli hitrost med 30 in 40 besed na minuto, 60 do 80 besed na minuto pa bi potrebovali, da bi pisali tako hitro, kot mislimo.
Tipkanje postane lažje, ker smo lahko s pogledom osredotočeni na zaslon.

Kazalca postavite na črki <kbd>F</kbd> in <kbd>J</kbd>. Ti dve tipki sta na tipkovnicah pogosto označeni z izbočenima pikama ali črticama. Ostale prste postavimo na isto vrstico. Vsakemu prstu so dodeljene tipke:

:::{figure-md} slika:polozaji-prstov
![Položaji prstov za desetprstno tipkanje](01-urejevalnik-in-markdown/Typing-colour_for-finger-positions.png)

&nbsp; Položaji prstov za desetprstno tipkanje\
<span class="avtor">
   [Cy21](https://commons.wikimedia.org/wiki/User:Cy21),
   [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0),
   via ([Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Typing-colour_for-finger-positions.svg.png))
</span>
:::

Hitri programerji ne uporabljajo miške, ker jih le-ta upočasni.
Pomembno je, da se naučite uporabljati bližnjice v vseh programih, ki jih uporabljate pogosto.
Veliko bližnjic se da uporabiti z eno roko.
Desničarji lahko na primer z levo roko uporabijo bližnjico <kbd>Alt</kbd>+<kbd>Tab</kbd> (<kbd>Cmd</kbd>+<kbd>Tab</kbd> na MacOS) za preklapljanje med okni, medtem ko imajo desno roko na miški.

## Navadno besedilo in označevalni jeziki

Navadno besedilo (angl. _plain text_) je besedilo, ki vsebuje samo znake (črke, številke, ločila), brez dodatnih informacij o izgledu.
V navadnem besedilu urejamo samo znake, ne pa tudi vrste pisave, barve ali velikosti in ne moremo uporabljati krepkega ali poševnega tiska, tabel in slik.

`````{admonition} Primer oblikovanega besedila
:class: tip
Besedilo lahko poudarimo **krepko**, _ležeče_, <span style="color: magenta">z barvo</span> ter z <span style="font-size: 0.7em">različnimi</span> <span style="font-size: 1.5em">velikostmi</span>.
`````

`````{admonition} Primer navadnega besedila
:class: tip
    Navadno besedilo je samo po sebi videti precej dolgočasno.
`````

Kako torej v navadnem besedilu povemo, kaj posamezni deli besedila pomenijo?

Pri tem predmetu bomo navadno besedilo uporabljali predvsem v kombinaciji z označevalnimi jeziki (angl. _markup languages_).
V besedilu bomo uporabljali vnaprej določena zaporedja znakov, ki imajo poseben pomen: z njimi označimo, kateri del besedila je naslov, kateri seznam in kateri povezava.
Pravilom, po katerih so ta zaporedja sestavljena, rečemo sintaksa.
Kako bodo ti deli videti, določi program, ki besedilo prikaže.

[Markdown](https://www.markdownguide.org) je preprost, a zelo razširjen označevalni jezik, ki omogoča hitro pisanje strukturiranih dokumentov brez zapletenih orodij.
Zasnoval ga je John Gruber, da bi olajšal pisanje za splet v čisti, berljivi obliki.
Ključne prednosti Markdowna so:

- berljivost izvornega besedila,
- združljivost s sistemi za upravljanje različic in s programsko kodo,
- pretvorljivost v različne formate (HTML, PDF, LaTeX …).

Takole je zapisano besedilo v Markdownu:

```markdown
# Naslov

Besedilo je lahko **poudarjeno** ter
vsebuje [povezave](https://www.fmf.uni-lj.si/),
`programsko kodo` in sezname:
- prva točka
- druga točka
- tretja točka
```

Tudi če Markdowna še ne poznate, verjetno lahko uganete, kateri del besedila je naslov, katera beseda je poudarjena in kaj je seznam.
Prav to pomeni berljivost izvornega besedila.

Kako je Markdown videti, ko ga prikažemo, lahko preverite kar v urejevalniku:
VSCode zna poleg izvornega besedila odpreti še predogled (angl. _Open Preview_), ki se osvežuje sproti, medtem ko pišete.
Isti zapis bo v drugem programu (na primer na GitHubu) videti nekoliko drugače: videz določi program, ki besedilo prikaže, ne zapis sam.

V 3. nalogi boste v Markdownu pripravili datoteko README — po dogovoru je to datoteka, ki jo v imeniku preberemo najprej.
Kasneje boste spoznali še dva označevalna jezika: HTML, v katerem so napisane spletne strani, in LaTeX, v katerem boste pisali matematična besedila.

(urejevalnik:vscode)=
## Urejevalnik VSCode

Programe in matematična besedila boste pisali kot navadno besedilo, zato je pomembno, da se naučite kompetentno uporabljati profesionalni urejevalnik.
Priporočamo [Visual Studio Code](https://code.visualstudio.com/) (na kratko "VSCode"), odprtokodni urejevalnik z dobro podporo za programiranje in pisanje besedil v LaTeX-u.
Navodila za vaje bodo predpostavljala, da uporabljate VSCode.
Seveda pa lahko uporabljate kak drug urejevalnik, pod pogojem, da ga res dobro poznate!

Urejevalniki, kot je VSCode, so namenjeni predvsem razvijalcem programske opreme in omogočajo urejanje izvorne kode programov.
V primerjavi s programi, kot je Microsoft Word, v VSCode ne določate, kako naj bo naslov videti, ampak označite, kateri del besedila je naslov.
Kmalu boste opazili, da urejevalnik sam od sebe spreminja izgled določenih delov besedila.
Temu rečemo poudarjanje sintakse (angl. _syntax highlighting_).
Pomaga nam, da hitreje razberemo pomen izvorne kode (ali pa najdemo napake v njej).
Barve, ki jih pri tem vidite, niso shranjene v datoteki: urejevalnik jih sproti določi sam, zato se spremenijo, ko zamenjate temo.

Glavni deli uporabniškega vmesnika VSCode so:

- opravilni stolpec (angl. _Activity Bar_), v katerem preklapljate med različnimi pogledi stranskega menija, kot so datoteke (angl. _Explorer_), upravljanje različic (angl. _Source Control_) in razširitve (angl. _Extensions_),
- glavni stranski meni (angl. _Primary Side Bar_), ki prikazuje izbrani pogled,
- skupine urejevalnikov (angl. _Editor Groups_), v katerih urejate odprte datoteke,
- podokno (angl. _Panel_), ki vsebuje npr. ukazno vrstico in sporočila o napakah,
- statusna vrstica (angl. _Status Bar_) z uporabnimi informacijami, ki jih bomo spoznali kasneje.

:::{figure-md} slika:vmesnik-vscode
![Uporabniški vmesnik urejevalnika VSCode](01-urejevalnik-in-markdown/vscode-ui.png)

&nbsp; Uporabniški vmesnik urejevalnika VSCode
:::

Več informacij:
- [dokumentacija za VSCode](https://code.visualstudio.com/docs), kjer začnite z razdelkom "Get started",
- [poglavje o osnovnem urejanju kode](https://code.visualstudio.com/docs/editor/codebasics),
- [bližnjice na tipkovnici za svoj operacijski sistem](https://code.visualstudio.com/docs/getstarted/keybindings#_keyboard-shortcuts-reference).

## 1. naloga: tipkanje

1. Preizkusite se na spletni strani [TypingTest.com](http://www.typingtest.com) (Izberite "1 minute" in "Medium").
2. Zapomnite si svoj rezultat (WPM – words per minute), saj ga boste vpisali v anketo, ki jo boste reševali za domačo nalogo.
   Rezultati bodo objavljeni anonimno, vi pa boste videli, kam se uvrščate.

`````{admonition} Nasvet za operacijski sistem MacOS
:class: tip
Za tipkanje redkejših znakov si pomagajte s programom [Keyboard Viewer](https://support.apple.com/en-gb/guide/mac-help/mchlp1015/mac),
ki je že nameščen na vašem sistemu.
`````

`````{admonition} Vaja za doma
:class: tip
Odločite se za postavitev tipkovnice (slovensko, angleško, Dvořak, ...) in približno 15 minut vadite tipkanje. Izberite vaje tako, da bo tipkovnica v lekcijah čim bolj podobna izbrani.

- Na strani [Touch Typing Study](https://www.typingstudy.com/sl-slovenian-1/lesson/1/part/1) so lekcije nekoliko manj barvite, imate pa veliko izbiro postavitev tipkovnic, vključno s slovensko.
- Če uporabljate angleško tipkovnico, lahko začnete s [prvo lekcijo na TypingTest.com](https://www.typingtest.com/trainer/applet.html?course_url=course_descriptions/fl5_us_sr_touchtyping.xml&lesson_id=A001) ali z lekcijami na [Typing.com](https://www.typing.com/student/lessons).
- Na spletnih straneh [Typing Tutor](https://www.typingtutor-online.com), [Type Fu](https://type-fu.com) in [Typing Club](https://www.edclub.com/sportal/program-3.game) najdete vaje za manjši izbor postavitev tipkovnic v več jezikih.
- Vaje tipkanja, ki so neodvisne od postavitve tipkovnice, najdete na [Keybr.com](https://www.keybr.com).
  Na tej spletni strani vam ne pomagajo s sliko tipkovnice.

Petnajst minut vaje je seveda premalo, da bi se naučili desetprstnega tipkanja.
Če se želite naučiti, bo najlažje, če si vzamete vsak dan četrt ure za vedno težje vaje.
Po kakih 10 urah vaje bi vaši prsti že morali biti dovolj seznanjeni s tipkami,
da boste lahko počasi tipkali desetprstno.
Ob rednih vajah boste tekoče tipkali do konca semestra.
`````

## 2. naloga: spoznajte VSCode

1. Poženite VSCode.
2. Preletite razdelek o [uporabniškem vmesniku](https://code.visualstudio.com/docs/getstarted/userinterface).
   Bodite pozorni na osnovno razporeditev in na svojem računalniku poiščite glavne dele vmesnika, opisane v razdelku [Urejevalnik VSCode](urejevalnik:vscode).
3. V dokumentaciji poiščite, kako spremenite temo (izgled, angl. _Color Theme_) urejevalnika in jo spremenite na tako, ki vam je všeč.
4. Zaprite urejevalnik.

## 3. naloga: pripravite datoteko README

`````{admonition} Del domače naloge
:class: attention
Datoteko, ki jo boste pripravili, boste potrebovali za domačo nalogo.
`````

Datoteko boste pripravili, shranili in ponovno odprli brez miške, pri urejanju vsebine pa lahko uporabljate tudi miško.
Dela brez miške rešujte skupaj z asistentko/om ali demonstratorko/jem, ki pa vam ne sme pomagati pri iskanju bližnjic (lahko si pomagate med sabo).
Najprej preberite spodnja pravila in se pripravite na izvajanje naloge.
Vnaprej poiščite potrebno dokumentacijo (na primer, kako v VSCode z bližnjico odprete imenik?), da ne boste brskali kasneje.
Pri tem vam bo v pomoč [plonkec za uporabo tipkovnice](plonkec:tipkovnica), predvsem razdelka [Zaganjanje programov](bliznjice:zaganjanje) in [Splošne bližnjice](bliznjice:vscode-splosne).

`````{admonition} Pozor, uvajamo standarden zapis
:class: important
Včasih boste v navodilih opazili besedilo v čudnih oklepajih `⟨besedilo-v-cudnih-oklepajih⟩` (ki bo pogosto napisano brez šumnikov, presledki pa bodo nadomeščeni z vezaji). Te oklepaje uporabljamo zato, da poudarimo, da gre za del besedila, ki ga nadomesti vsak zase. Besedilo v oklepajih vam pove, s čim je treba vse skupaj (z oklepaji vred) nadomestiti.
Prvi primer boste srečali spodaj, `C:\Users\⟨uporabnisko-ime⟩`. Če je vaše uporabniško ime `Gandalf`, potem je prej omenjena pot v vašem primeru   `C:\Users\Gandalf` (**in ne** `C:\Users\⟨Gandalf⟩`).

Ta (ali podoben) način označevanja je kar običajen za mesta, kjer morate vnesti svoje podatke (drugi avtorji včasih uporabijo tudi drugačne oklepaje).
`````

`````{admonition} Pozor, uvajamo standarden zapis
:class: important
Z znakom 🍎 označujemo, kar velja za MacOS.
`````

### 3.1 Pripravite se za delo (brez miške)

S tipkovnico in čim manjšo uporabo miške naredite naslednja opravila:

1. Odprite svoj domači imenik v upravitelju datotek:
   - na Windows v Raziskovalcu (angl. _File Explorer_): `C:\Users\⟨uporabnisko-ime⟩`,
   - na MacOS v Finderju: `/Users/⟨uporabnisko-ime⟩`,
   - na Linuxu: `/home/⟨uporabnisko-ime⟩`.
2. V njem ustvarite imenik za Računalniški praktikum (npr. `C:\Users\⟨uporabnisko-ime⟩\rp`), v njem pa imenik `racunalniski-praktikum`.
   Zunanji imenik je vaš: poimenujete ga lahko po svoje in vanj boste dali vse, kar je povezano s predmetom.
   Za notranjega priporočamo ime `racunalniski-praktikum`: tako ga bodo imenovala navodila v nadaljevanju semestra.
3. Poženite urejevalnik VSCode.
4. V urejevalniku odprite imenik `racunalniski-praktikum` (npr. `C:\Users\⟨uporabnisko-ime⟩\rp\racunalniski-praktikum` oz. 🍎 `/Users/⟨uporabnisko-ime⟩/rp/racunalniski-praktikum`).
5. Ustvarite novo datoteko in jo takoj shranite v ta imenik.
   Odprlo se bo pogovorno okno z aktivnim vnosnim poljem, v katerega že takoj lahko začnete pisati ime datoteke; poimenujte jo `README.md`.
   S pritiskom na vnašalko <kbd>↵</kbd> potrdite ime.
6. Poiščite, kje v statusni vrstici piše, kakšne vrste datoteko urejate. Vrsto je urejevalnik ugotovil iz končnice `.md`.
7. V upravitelju datotek preverite, ali se vsebina imenika za Računalniški praktikum ujema s spodnjo sliko.

:::{figure-md} slika:vsebina-imenika
<img src="01-urejevalnik-in-markdown/vsebina-imenika-readme.svg" alt="Imenik rp z imenikom racunalniski-praktikum, v katerem je README.md">

&nbsp; Strukturo imenikov bomo prikazovali kot zgoraj.
:::

### 3.2 Uredite dokument

Pri urejanju lahko uporabljate tudi miško.

1. Odprite [predogled](bliznjice:vscode-splosne). Zavihek s predogledom z miško povlecite proti desnemu zgornjemu kotu okna urejevalnika,
   da preklopite v pogled, v katerem boste videli datoteko in predogled hkrati (če vam ni všeč, zavihek prestavite nazaj).
2. Kopirajte in prilepite spodnje besedilo v datoteko `README.md`.
    - **Kopirajte:** z miško se zapeljite zgoraj desno v okvirček in kliknite na ikono, ali pa označite besedilo in pritisnite <kbd>Ctrl</kbd>+<kbd>C</kbd> oz. 🍎 <kbd>Cmd</kbd>+<kbd>C</kbd>.
    - **Prilepite:** <kbd>Ctrl</kbd>+<kbd>V</kbd> oz. 🍎 <kbd>Cmd</kbd>+<kbd>V</kbd>.

   Oglejte si predogled.

```markdown
<!-- glavni naslov -->
Računalniški praktikum
<!-- To je komentar, ki bo na prikazanem Markdownu skrit. 
     V tem besedilu so v komentarjih napisana navodila za reševanje. Pustite jih v datoteki. -->

<!-- 2. nivojski razdelek -->
Bližnjice na tipkovnici

Kopiraj označeno v odložišče: Ctrl+C (**C**opy)
Izreži označeno v odložišče: Ctrl+X
Prilepi vsebino odložišča: Ctrl+V

<!-- 2. nivojski razdelek -->
Koda

Včasih pride prav značka kbd za tipke. Značko uporabimo takole:

<!-- začetek bloka kode -->
<kbd>Ctrl</kbd>
<!-- konec bloka kode -->

<!-- 2. nivojski razdelek -->
Domača naloga

<!-- Spodnji seznam bo pripravil seznam nalog. Na GitHubu bodo lepo vidna potrditvena polja, 
     VSCode pa bo prikazal samo oglate oklepaje. Ko nalogo opravite, si to lahko zabeležite tako,
     da spremenite [ ] v [x]. -->
- [ ] Izberite si še tri bližnjice, ki jih še ne uporabljate redno, in se jih naučite. 
      Dodajte jih v prvi razdelek tega dokumenta.

<!-- 2. nivojski razdelek -->
Uporabne povezave

FMF učilnica <!-- https://ucilnica.fmf.uni-lj.si/ -->
Računalniški sistemi, storitve in oprema za študente <!-- https://ucilnica.fmf.uni-lj.si/mod/page/view.php?id=51619 -->
Zapiski in vaje za Računalniški praktikum <!-- https://racunalniski-praktikum.github.io/ -->
Dokumentacija za Markdown na GitHubu <!-- https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax -->

```

Pomagajte si z [dokumentacijo za Markdown na GitHubu](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
in sledite spodnjim navodilom.

3. Označite glavni naslov in razdelke. V navadnem besedilu jih lahko prepoznate po tem, da je v vrstici nad njimi _komentar_
   (besedilo med znaki `<!--` in `-->`, ki se ne izpiše).
4. V razdelku "Bližnjice na tipkovnici" uredite vrstice tako, da se bodo izpisale kot neoštevilčen seznam.
   Pomagajte si z [večimi kurzorji](bliznjice:kurzorji) (angl. _multi-cursor_).
5. V seznamu besede "Kopiraj", "Izreži" in "Prilepi" označite kot ležeče (angl. _italic_).
   Tudi tu si lahko pomagate z večimi kurzorji: s <kbd>Ctrl</kbd>+<kbd>←→</kbd> (🍎 <kbd>Option</kbd>+<kbd>←→</kbd>) se lahko premikate med besedami.
6. V prvem odstavku razdelka "Koda" označite `kbd` kot kodo v besedilu (angl. _inline code_).
7. Označite blok kode (angl. _code block_). Komentarja povesta, kje se blok začne in kje konča.
8. V razdelku "Uporabne povezave" vrstice označite kot oštevilčen seznam.
9. V seznamu označite povezave. V vsaki vrstici je po ena povezava: besedilo naj bo besedilo povezave (tisto, kar kliknemo),
   naslov v komentarju pa naj bo tarča povezave (tja, kamor nas povezava pelje).

### 3.3 Zaključite delo (brez miške)

S tipkovnico in čim manjšo uporabo miške naredite naslednja opravila:

1. Shranite datoteko `README.md`.
2. Zaprite datoteko `README.md`.
3. Ponovno odprite datoteko `README.md`.

`````{admonition} Če delate na šolskem računalniku
:class: tip
Poskrbite, da boste do datoteke lahko dostopali tudi doma, saj jo boste potrebovali pri domači nalogi.
Uporabite na primer Dropbox, Google Drive ali OneDrive — do vseh lahko dostopate tudi v brskalniku — ali pa si datoteko pošljite po elektronski pošti.
`````
