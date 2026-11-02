# Označevalni jezik HTML

`````{admonition} Programska oprema
:class: important
- [Visual Studio Code](namestitev:vscode) z razširitvijo [HTMLHint](https://marketplace.visualstudio.com/items?itemName=mkaufman.HTMLHint):
  v pogledu razširitev (angl. _Extensions_) poiščite `HTMLHint` in kliknite _Install_,
- spletni brskalnik, na primer Chrome, Firefox ali Safari.
`````

V Wordu lahko naslov naredite tako, da besedilo povečate in odebelite.
Na pogled je to naslov, za program pa samo večje krepko besedilo:
ne pojavi se v samodejnem kazalu, bralnik zaslona ga ne prebere kot naslov,
in če se odločite za drugačen videz naslovov, morate popraviti vsakega posebej.
Word ima za to sloge, kot je _Naslov 1_ (angl. _Heading 1_), ki povedo, kaj besedilo je, in ne samo, kako je videti.

Na tej ideji je zgrajen HTML (angl. _**H**yper**T**ext **M**arkup **L**anguage_, označevalni jezik za oblikovanje večpredstavnostnih dokumentov), v katerem so zapisane spletne strani.
Z značkami povemo, kaj posamezni deli besedila so, na primer naslov, odstavek, seznam, povezava, tabela ali slika; kako bodo videti, določi brskalnik ali pa to določimo [posebej](html:videz).
Markdown iz 1. poglavja dela enako, le da dele besedila označi s kratkimi znaki, HTML pa jih poimenuje: naslov prve ravni je `h1` (angl. _heading 1_), zato kar v Markdownu zapišemo kot `# Naslov`, v HTML-ju zapišemo kot `<h1>Naslov</h1>`.

## Struktura dokumenta

Dokument HTML je sestavljen iz vsebine in značk (angl. _tags_).
Značke prepoznamo po oklepajih `<` in `>`, na primer `<h1>` ali `<img>`.
Večina značk ima dva dela: začetek `<znacka>` in konec `</znacka>`; kar je med njima, je vsebina značke.
Značke imajo lahko tudi atribute, ki jim dodajo podatke.
Primer je značka za povezavo `a` (angl. _anchor_): v atribut `href` napišemo spletni naslov, na katerega kaže povezava, vsebina značke pa je besedilo povezave, ki ga prikaže brskalnik.

:::{figure-md} slika:anatomija-znacke
:width: 80%
:align: center
![Sestavni deli značke](04-html/anatomija-znacke.svg)

&nbsp; Sestavni deli značke HTML
:::

Nekatere značke nimajo vsebine, zato tudi ne konca, na primer `<img>` za sliko.

Značke lahko gnezdimo eno v drugo: `<a href="https://www.fmf.uni-lj.si/"><em>FMF</em></a>`.
Ne smejo pa se prekrivati: od dveh značk je bodisi ena v vsebini druge bodisi se sploh ne prekrivata.
Narobe je na primer `<a href="https://www.fmf.uni-lj.si/"><em>FMF</a></em>`.
Značke si lahko predstavljate kot škatle, ki držijo vsebino in druge škatle.
Brskalnik napačno gnezdenje večinoma preživi in stran vseeno prikaže, zato napake ne opazite, dokler kode ne preverite.

Imena značk lahko pišemo z velikimi ali malimi črkami.
Po dogovoru, ki se ga bomo držali tudi mi, jih pišemo z malimi.
Zaradi preglednosti vsako značko, ki jo začnemo v novi vrstici, zamaknemo glede na značko, v kateri je; urejevalnik to večinoma naredi sam.
Značke sredi besedila, kot je povezava `a`, ostanejo v vrstici z besedilom.
Komentarje, ki jih brskalnik ne prikaže, pišemo med `<!--` in `-->`.

### Enostaven primer dokumenta HTML

```html
<!DOCTYPE html>
<html lang="sl">
  <head>
    <meta charset="UTF-8">
    <title>Enostavna spletna stran</title>
  </head>
  <body>
    <!-- V naslednjih dveh vrsticah je vsebina (telo) spletne strani -->
    <h1>Jaz sem naslov!</h1>
    <p>V odstavkih imamo lahko tudi <a href="https://www.fmf.uni-lj.si/">povezave</a>.</p>
  </body>
</html>
```

Dokument se začne z deklaracijo `<!DOCTYPE html>`, ki brskalniku pove, da gre za dokument HTML.
Deklaracija ni značka in nima konca; po dogovoru jo pišemo z velikimi črkami.
Sledi značka `html`, v kateri je ves dokument.
Njen atribut `lang` pove, v katerem jeziku je besedilo: `sl` za slovenščino, `en` za angleščino.
V znački `html` sta dve znački:
v glavi `head` so podatki o dokumentu, ki jih brskalnik ne prikaže na strani,
v telesu `body` pa vsebina strani.
V glavi so na primer

- naslov dokumenta `title`, ki ga brskalnik prikaže na zavihku,
- značka `<meta charset="UTF-8">`, ki pove, v katerem kodiranju je zapisana datoteka.
  Brez nje brskalnik kodiranje ugane in šumnike lahko prikaže napačno, podobno kot pri podnapisih v 2. poglavju, le v obratni smeri:
  datoteko v UTF-8 prebere, kot da je v Windows-1252, in `š` prikaže kot `Å¡`.

Dokument si lahko predstavljamo tudi kot hierarhijo značk:

:::{figure-md} slika:html-drevo
:width: 45%
:align: center
![Hierarhija značk za zgornji primer dokumenta](04-html/html-drevo.svg)

&nbsp; Hierarhija značk za zgornji primer dokumenta
:::

### Vsebina dokumenta

V telesu dokumenta najpogosteje uporabljamo naslednje značke:

- naslove `h1` do `h6`: številka pove raven naslova, ne njegove velikosti.
  Naslov strani je `h1`, naslovi razdelkov so `h2`, naslovi podrazdelkov `h3` in tako naprej.
- odstavke `p` (angl. _paragraph_),
- sezname: urejeni seznam `ol` (angl. _ordered list_) in neurejeni seznam `ul` (angl. _unordered list_), v katerih je vsak element v svoji znački `li` (angl. _list item_),
- citate `blockquote`,
- povezave `a` z atributom `href`,
- tabele `table`, v katerih so vrstice `tr` (angl. _table row_), v vrsticah pa celice `td` (angl. _table data_) ali celice glave tabele `th` (angl. _table header_),
- slike `img` z atributoma `src`, v katerem je pot do slike, in `alt`, v katerem je opis slike.
  Opis se uporabi, kadar se slika ne prikaže, in za dostopnost, na primer ko stran bere bralnik zaslona.

Brskalniku so presledki in prelomi vrstic v izvorni kodi vseeno: več zaporednih presledkov ali praznih vrstic prikaže kot en sam presledek.
Zato odstavkov ne ločimo s praznimi vrsticami, ampak vsakega označimo z značko `p`.

Povezava lahko kaže tudi na del iste strani.
Značka, na katero naj kaže, dobi atribut `id`, povezava pa ima v atributu `href` njegovo vrednost za znakom `#`.
Povezava `<a href="#criticism">Criticism</a>` tako pelje do naslova `<h2 id="criticism">Criticism</h2>`.
Vrednost atributa `id` se v dokumentu ne sme ponoviti.

Znački `em` (angl. _emphasis_) in `strong` povesta, da je besedilo poudarjeno, ne pa, kako je videti.
Z `em` označimo besedo, ki bi jo pri branju na glas poudarili, s `strong` pa pomembno besedilo, na primer opozorilo ali ključni pojem.
Brskalnik prvo običajno prikaže ležeče, drugo pa krepko.
Znački `b` (angl. _bold_) in `i` (angl. _italic_), ki povesta samo, kako naj bo besedilo videti, se ne uporabljata več.
Dobra praksa loči pomen, ki ga povedo značke HTML, od videza, ki ga določi CSS.

### Matematika

Formul, zapisanih v LaTeX-u, brskalnik sam ne zna prikazati.
Pomagamo si s knjižnico [MathJax](https://www.mathjax.org/), ki jo v glavi dokumenta vključimo kot skripto:
brskalnik jo prenese skupaj s stranjo, ta pa poišče formule v sintaksi LaTeX-a in jih izriše.
Formule med `\(` in `\)` so prikazane v besedilu, formule med `\[` in `\]` pa v svoji vrstici.
LaTeX boste podrobneje spoznali v naslednjem poglavju.

(html:videz)=
## Vsebina in videz

Kako so videti naslovi, odstavki in tabele, določa jezik CSS (angl. _**C**ascading **S**tyle **S**heets_).
HTML pove, kaj je kaj, CSS pa določi barve, pisave, razmike, velikosti in postavitev.
Jezika sta primer [ločevanja vsebine in predstavitve](https://en.wikipedia.org/wiki/Separation_of_content_and_presentation), istega načela kot pri slogih v Wordu.

Slogi so ponavadi v posebni datoteki s končnico `.css`, ki jo vključimo v glavi dokumenta:

```html
<link rel="stylesheet" href="oblikovanje.css">
```

Atribut `href` je pot do datoteke, tako kot pri povezavah in slikah.
Datoteka s slogi je sestavljena iz pravil, kot je

```css
h2 {
  color: #8b4513;
}
```

To pravilo pove, da naj bodo vsi naslovi `h2` rjavi.
Ker so naslovi označeni kot naslovi, z eno spremembo pravila spremenimo vse hkrati.
Besedila, ki je samo povečano in odebeljeno, pravilo za naslove ne zajame.

Datotek s slogi skoraj nihče ne piše od začetka: skoraj vsak vzame obstoječo in jo prilagodi, ko to potrebuje, na primer s pomočjo jezikovnega modela.
To pa gre zlahka samo, če je HTML pravilno označen.

## Orodja za razvijalce

Spletni brskalniki imajo vgrajena orodja za razvijalce (angl. _developer tools_),
s katerimi lahko pregledujete in urejate HTML in CSS strani, iščete napake v skriptah in spremljate, katere datoteke se prenesejo.
Ko v brskalniku obiščete spletno stran, se na vaš računalnik prenese kopica datotek: dokument HTML, slogi, slike in skripte.
Brskalnik jih uporabi, da vam prikaže stran.
Orodja ne kažejo izvorne kode, ampak dokument, kot ga ima brskalnik v pomnilniku: če ga skripta spremeni, se sprememba vidi tam.

## 1. naloga: orodja za razvijalce

1. Odprite brskalnik in v njem orodja za razvijalce:
   - Chrome: v meniju ⋮ na desnem koncu orodne vrstice izberite _More tools_ > _Developer Tools_,
   - Firefox: v meniju ☰ na desnem koncu orodne vrstice izberite _More tools_ > _Web Developer Tools_,
   - Safari: v meniju _Develop_ izberite _Show Web Inspector_.
     Če menija _Develop_ ne vidite, ga vklopite po [navodilih](https://support.apple.com/guide/safari/sfri20948/mac).

   Orodja odpre tudi tipka <kbd>F12</kbd> (v Chromu in Firefoxu) ali bližnjica <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>I</kbd> (🍎 <kbd>Cmd</kbd>+<kbd>Option</kbd>+<kbd>I</kbd>).
2. V orodjih odprite zavihek _Network_.
3. V naslovno vrstico brskalnika vpišite `https://www.fmf.uni-lj.si/` in stisnite vnašalko <kbd>↵</kbd>.
   Poglejte, katere datoteke so se prenesle, da se je prikazala prva stran FMF: poleg dokumenta HTML še slogi, slike in skripte.
4. Preklopite na zavihek z drevesom dokumenta (v Chromu in Safariju _Elements_, v Firefoxu _Inspector_) in si ga oglejte.
   To ni izvorna koda strani, ampak dokument, kot ga ima brskalnik v pomnilniku; razlika se bo pokazala v 4. nalogi.

## 2. naloga: ogrodje dokumenta

1. V VSCode odprite imenik `racunalniski-praktikum` v imeniku `rp` (_File_ > _Open Folder_).
   Če repozitorija na tem računalniku še nimate, ga pripravite po navodilih v 1. nalogi 3. poglavja ali prosite za pomoč.
   V njem naredite imenik `04-html`, v tem pa datoteko `stran.html` in jo odprite.

   :::{figure-md} slika:drevo-repozitorij
   :width: 50%
   :align: center
   ![Drevo imenikov z novo datoteko](04-html/drevo-repozitorij.svg)

   &nbsp; Repozitorij `racunalniski-praktikum` po tej točki
   :::

2. Odprite pogled _Problems_ (_View_ > _Problems_).
   Ko je kurzor v datoteki `stran.html`, se v njem pojavi opozorilo `Doctype must be declared first`.
   Za sporočilom piše, katero pravilo je kršeno in v kateri vrstici in stolpcu je težava.
   Če se opozorilo ne pojavi, preverite, da je razširitev HTMLHint nameščena.
3. V prvo vrstico napišite `<` (morda tudi `<!`), počakajte, da se v priročnem meniju pokaže `!DOCTYPE`, in ga izberite z vnašalko <kbd>↵</kbd>.
   V vrstici mora pisati `<!DOCTYPE html>`; če ne piše, deklaracijo prepišite od tu.
4. V naslednjo vrstico napišite `<html>`.
   Ko napišete `>`, vam urejevalnik sam dopiše konec značke, kurzor pa ostane med njima.
   Stisnite vnašalko.
5. V značko `html` dodajte eno za drugo znački `head` in `body`, zamaknjeni glede na `html`.
   V pogledu _Problems_ se pojavi novo opozorilo.
   Odpravite ga, pa tudi tisto, ki se pojavi za njim; naslov dokumenta naj bo `ISO 3103`.
6. V glavo, pred značko `title`, dodajte še značko `<meta charset="UTF-8">`.
7. Kodo preverite še na strani [Nu Html Checker](https://validator.w3.org/nu/#textarea), ki je strožja od razširitve HTMLHint:
   prilepite jo v polje in kliknite _Check_.
   Dodajte atribut za jezik, ki ga predlaga; besedilo, ki ga boste dodali v 3. nalogi, je v angleščini.
8. Počistite vse napake in opozorila v pogledu _Problems_.
   Če ne veste kako, prosite za pomoč.
9. Zabeležite spremembo v pogledu za upravljanje različic:
   1. V opravilnem stolpcu kliknite ikono za upravljanje različic (_Source Control_).
   2. Pod napisom _Changes_ je datoteka `stran.html`.
      Ko se z miško zapeljete nad njeno vrstico, se na desni pokažejo ikone.
      Kliknite <kbd>+</kbd> (_Stage Changes_), ki izvede ukaz [`git add`](git:osnovni-ukazi).
   3. Datoteka se premakne pod napis _Staged Changes_: v vnos gredo natanko spremembe pod tem napisom.
      V polje nad gumbom _Commit_ napišite sporočilo, na primer `Pripravi ogrodje dokumenta HTML`, in kliknite _Commit_.

`````{admonition} Shranite vaje na GitHub
:class: important
Na koncu 2. do 5. naloge zabeležite spremembe.
Če naloge na vajah ne končate, spremembe vseeno zabeležite in v sporočilo napišite na primer `V delu: ...` s kratkim opisom narejenega.
[Preden nehate delati](https://www.reddit.com/r/ProgrammerHumor/comments/3nc531/in_case_of_fire/), na vajah ali doma, vnose pošljite na GitHub:
v paleti ukazov (<kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>P</kbd>, 🍎 <kbd>Cmd</kbd>+<kbd>Shift</kbd>+<kbd>P</kbd>) izberite ukaz _Git: Push_.
`````

## 3. naloga: vsebina

`````{admonition} Del domače naloge
:class: attention
Datoteki `stran.html` in `tea-bowl.jpg`, ki ju boste zabeležili na koncu te naloge, potrebujete za 4. domačo nalogo.
`````

Pri pisanju značk vam bo v pomoč ukaz _Wrap with Abbreviation_ iz palete ukazov,
več o njem pa si preberite v [plonkcu za paleto ukazov](paleta-ukazov:html).

Če si ne predstavljate, kako se uporablja kakšna značka, zlasti pri seznamih in tabelah,
poiščite zgled na spletu, denimo na strani [W3Schools](https://www.w3schools.com/html/).

 1. Datoteko `stran.html` odprite še v brskalniku: v pogledu datotek jo kliknite z desno tipko,
    izberite _Reveal in File Explorer_ (🍎 _Reveal in Finder_) in jo iz upravitelja datotek povlecite v okno brskalnika.
 2. Prenesite datoteko [`vsebina.txt`](04-html/vsebina.txt) (ni je treba shraniti v repozitorij), jo odprite v VSCode in njeno vsebino prilepite v značko `body`.
    Prilepljeno besedilo zamaknite glede na `body`, tako da bo vsaka vrstica za dve ravni odmaknjena od roba:
    označite ga in stisnite <kbd>Tab</kbd>, ki vse označene vrstice zamakne za eno raven (<kbd>Shift</kbd>+<kbd>Tab</kbd> pa nazaj).
    Datoteko `stran.html` shranite.
    Z bližnjico <kbd>Alt</kbd>+<kbd>Tab</kbd> (🍎 <kbd>Cmd</kbd>+<kbd>Tab</kbd>) skočite v brskalnik
    in stran osvežite z <kbd>Ctrl</kbd>+<kbd>R</kbd> (🍎 <kbd>Cmd</kbd>+<kbd>R</kbd>).
 3. Na začetku besedila, ki ste ga prilepili, označite naslov "ISO 3103".
    Odprite paleto ukazov (<kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>P</kbd>, 🍎 <kbd>Cmd</kbd>+<kbd>Shift</kbd>+<kbd>P</kbd>),
    začnite tipkati `wrap` in ukaz _Wrap with Abbreviation_ izberite z vnašalko, ko se pojavi na vrhu seznama.
    V pogovorno okno, ki se odpre, napišite ime značke za naslov strani (`h1`) in stisnite vnašalko.
    V vrstici mora zdaj pisati `<h1>ISO 3103</h1>`.
    Naslednjič se bo ukaz na vrhu seznama pojavil že po nekaj natipkanih znakih.
 4. Z ustreznimi značkami označite še naslove razdelkov (`h2`):
    "Contents" za uvodnimi odstavki ter "Details", "Pot and bowl", "Criticism" in "Competing standards".
    Zadnji štirje so v besedilu dvakrat: naslov razdelka je tisti, pred katerim sta dve prazni vrstici, ne vrstica v seznamu pod "Contents".
    _Namig:_ z <kbd>Alt</kbd> (🍎 <kbd>Option</kbd>) in levim klikom dodate kurzor, ukaz pa se izvede pri vseh kurzorjih hkrati.
 5. Pod naslovom "Contents" so našteti razdelki. Iz njih naredite urejeni seznam.
    Postavite kurzor na začetek vsake vrstice (<kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>↑↓</kbd>, 🍎 <kbd>Cmd</kbd>+<kbd>Option</kbd>+<kbd>↑↓</kbd>),
    pridržite tipko <kbd>Shift</kbd> in stisnite <kbd>End</kbd> (🍎 <kbd>Cmd</kbd>+<kbd>→</kbd>), da označite vsako vrstico s svojim kurzorjem.
    Uporabite ukaz _Wrap with Abbreviation_ z značko `li`: naredi toliko značk, kot imate kurzorjev.
    Nato vse vrstice označite z enim kurzorjem in jih obdajte z značko `ol`.
 6. Pod naslovom "Details" stavek "To maintain consistent results, ..." napoveduje seznam priporočil:
    vsi odstavki za njim naj bodo elementi neurejenega seznama (`ul`).
    Kurzorje postavite s klikanjem, ker bi jih bližnjica iz prejšnjega koraka postavila tudi v prazne vrstice med odstavki.
    Dva elementa (tista s tabelama) sta zapisana v več vrsticah: vsakega posebej označite v celoti in ga šele nato obdajte z značko.
 7. Citat (odstavek pod besedilom "The abstract states the following:") označite z značko `blockquote`.
 8. Vse ostale odstavke označite z značko `p`.
 9. V prvem odstavku naj bo "ISO 3103" povezava na Wikipedijo:
    uporabite značko `a`, spletni naslov s konca odstavka pa prestavite v njen atribut `href`.
10. V 2. in 8. elementu seznama pod naslovom "Details" sta tabeli s po tremi stolpci in tremi vrsticami.
    Zapišite ju z značkami `table`, `tr`, `td` in `th`; celice glave uporabite v prvi vrstici in v prvem stolpcu.
11. Prenesite [sliko](04-html/tea-bowl.jpg), jo premaknite v imenik `04-html` in jo pod naslovom "Details" vstavite z značko `img` namesto vrstice `tea-bowl.jpg`.
    V atribut `src` napišite pot do slike, v atribut `alt` pa njen opis iz vrstice pod njo, ki jo nato izbrišite.
    V brskalniku preverite, da se slika prikaže.
    Verjetno je prevelika, zato jo za zdaj zakomentirajte: postavite kurzor v vrstico s sliko in v paleti ukazov izberite _Add Line Comment_.
12. Počistite vse napake in opozorila, kodo pa preverite še z Nu Html Checker kot v 2. nalogi:
    opozori tudi, če je element seznama zunaj seznama ali tabela zunaj svojega elementa seznama, čeprav je stran v brskalniku videti v redu.
13. Zabeležite spremembo: dodajte datoteki `stran.html` in `tea-bowl.jpg` ter napišite uporabno sporočilo, na primer `Dodaj vsebino dokumenta HTML`.

## 4. naloga: matematika in sklicevanje

1. V drugem odstavku poudarite besedilo "ISO 3103" na začetku z značko `strong`, besedilo "brewing tea" pa z značko `em`.
2. Strani dodajte MathJax: sledite navodilom [Getting Started](https://www.mathjax.org/#gettingstarted) za MathJax 4
   in kodo, ki vključi skripto, dodajte v glavo dokumenta.
   Na konec telesa dokumenta dodajte formulo, na primer `\[x = \frac{-b \pm \sqrt{b^2-4ac}}{2a}\]`.
   Za zdaj še ni treba, da razumete, kako formule delujejo.
3. Orodja za razvijalce odprite v zavihku s stranjo `stran.html` (odprta so za vsak zavihek posebej)
   in v zavihku _Network_ poglejte, kaj se zgodi, ko osvežite stran: brskalnik prenese skripto MathJax in pisave.
   V zavihku _Elements_ (_Inspector_) nato poiščite formulo:
   namesto besedila med `\[` in `\]`, ki ste ga napisali, so v drevesu dokumenta značke, ki jih je vstavila skripta.
4. Formula, ki ste jo napisali, je zapisana v posebni sintaksi, iz katere računalnik vsaj do neke mere razbere, kaj želimo.
   Poskusite ugotoviti, kako deluje: kje so ukazi, kje njihovi argumenti in kako so označeni?
5. Po zgledu zgornje formule, prav tako med `\[` in `\]`, napišite enačbo $e^{i\pi} + 1 = 0$
   (poskusite uganiti, kako se napiše črka $\pi$).
6. Naslovom razdelkov dodajte atribute `id`, elemente seznama pod naslovom "Contents" pa spremenite v povezave nanje,
   tako da bo vsak vodil do svojega razdelka.
   Povezave preizkusite: ob kliku se spletnemu naslovu v naslovni vrstici doda `#` in ime razdelka, stran pa skoči nanj.
   Če je stran krajša od okna, okno zožite, da skok vidite.
7. Zabeležite spremembo: dodajte datoteko `stran.html` in napišite uporabno sporočilo, na primer `Dodaj formule in sklicevanje`.

## 5. naloga: oblikovanje

1. Prenesite datoteko [`oblikovanje.css`](04-html/oblikovanje.css) in jo premaknite v imenik `04-html`.
2. V glavo dokumenta `stran.html` dodajte značko `<link rel="stylesheet" href="oblikovanje.css">` in osvežite stran v brskalniku.
3. Odkomentirajte sliko iz 3. naloge: postavite kurzor v vrstico s sliko in v paleti ukazov izberite _Remove Line Comment_.
   Slog omeji širino slik, zato slika ni več prevelika.
4. V datoteki `oblikovanje.css` poiščite pravilo za naslove `h2` in barvo `#8b4513` zamenjajte s kakšno drugo, na primer `darkgreen` ali `#336699`.
   Datoteko shranite in osvežite stran: barvo je zamenjalo vseh pet naslovov razdelkov.
   Če se sprememba ne pokaže, stran osvežite brez predpomnilnika z <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>R</kbd>
   (🍎 <kbd>Cmd</kbd>+<kbd>Shift</kbd>+<kbd>R</kbd>, v Safariju <kbd>Cmd</kbd>+<kbd>Option</kbd>+<kbd>R</kbd>).
5. Zabeležite spremembo: dodajte datoteki `stran.html` in `oblikovanje.css`, napišite uporabno sporočilo, na primer `Dodaj slog`, in vnose pošljite na GitHub.

## Dodatni viri

* [HTML elements reference](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements), seznam vseh značk HTML na spletni strani MDN.
* [CSS styling basics](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics), uvod v CSS na isti strani, če vas zanima več.
