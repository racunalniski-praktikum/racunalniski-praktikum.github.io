# Osnovna uporaba Mathematice

`````{admonition} Programska oprema
:class: important
- [Mathematica](namestitev:mathematica)
`````

Mathematica je program za računanje: z njo računate s števili, pa tudi z izrazi, v katerih nastopajo simboli, na primer odvajate, integrirate in rišete grafe.
Delate v zvezku (angl. _notebook_): vanj pišete izraze, Mathematica pa pod vsakega izpiše rezultat.

## Celice

Zvezek ima tri vrste celic: celice z besedilom, vhodne celice in izhodne celice.

Novo celico dodate tako, da kliknete v prostor pod obstoječo celico: na mestu, kamor bo vstavljena, se pojavi vodoravna črta.

Desno od celic so oglati zaklepaji, ki celice združujejo v skupine.
Z enojnim klikom na zaklepaj celico ali skupino celic izberete (na primer za izbris), z dvojnim klikom pa skupino odprete ali zaprete.

Na vajah v vhodne celice pišete v _Wolframovem jeziku_, ki je najbolj zanesljiv način vnosa.
**Pozor:** če izraz (na primer enačbo) kopirate iz celice z besedilom ali iz datoteke PDF, so nekateri znaki pogosto napačni in Mathematica celice ne more izvesti.

### Izvajanje

Vhodno celico izvedete s tipkama <kbd>Shift</kbd>+<kbd>Enter</kbd>.
Če je v celici vse prav, se pod njo pokaže izhodna celica z rezultatom.
V eno celico lahko napišete več izrazov, vsakega v svojo vrstico; Mathematica izpiše rezultat vsakega posebej.

Izvajanje prekinete s tipkama <kbd>Alt</kbd>+<kbd>.</kbd> (🍎 <kbd>Cmd</kbd>+<kbd>.</kbd>) ali z menijskim ukazom **Evaluation** > **Abort Evaluation**.
Če to ne pomaga, ustavite jedro z menijskim ukazom **Evaluation** > **Quit Kernel** > **Local**.

Oznaki `In[⟨številka⟩]` in `Out[⟨številka⟩]` pred vhodnimi in izhodnimi celicami povesta, v kakšnem vrstnem redu ste celice izvedli.
Mathematica si zapomni vse, kar ste izvedli, zato šteje vrstni red izvajanja in ne vrstni red celic v zvezku.

### Posebni znaki in grške črke

Pogostejši znaki imajo kratka imena (angl. _alias_).
Uporabite jih tako, da pritisnete tipko <kbd>Esc</kbd>, ki v celico izpiše znak `⋮` (tri navpične pike), napišete ime in še enkrat pritisnete <kbd>Esc</kbd>.
Grško črko alfa na primer napišete kot <kbd>Esc</kbd> `a` <kbd>Esc</kbd>.

Več o tem preberite v [dokumentaciji](https://reference.wolfram.com/language/howto/TypeAGreekLetter.html).

## Sintaksa

Argumente funkcije naštejete v oglatih oklepajih in jih ločite z vejicami: `Funkcija[a, b, c]`.
Imena vseh vgrajenih funkcij in konstant se začnejo z **veliko začetnico**: `Sin[x]` je funkcija sinus, `sin[x]` pa ne.

V zavitih oklepajih `{}` navajate sezname, na primer `{1, 2, 3}`.

Množenje zapišete z zvezdico ali s presledkom: `2 x` in `a b` sta produkta.
Zapis `ab` brez presledka je en sam simbol z imenom `ab`.
Potenco zapišete s strešico: `x^2`.

Mathematica izraze v vhodnih celicah barva:

* **Nedefinirani simboli** so modri. Če v celico napišete `sin`, se obarva modro.
* **Definirani simboli** so črni. Če `sin` popravite v `Sin`, se obarva črno.
* **Vezane spremenljivke** so zelene. V izrazu za vsoto `Sum[1/k^2, {k, 1, Infinity}]` je `k` zelen.

## Računanje

Mathematica računa natančno, dokler ne zahtevate drugače:

```
1/3 + 1/6
Sqrt[8]
```

Rezultata sta ulomek `1/2` in izraz `2 Sqrt[2]`, ne decimalna približka.
Približno vrednost izračuna funkcija `N`, ki ji kot drugi argument lahko podate število mest: `N[Pi, 20]` vrne `3.1415926535897932385`.
Približen je tudi rezultat vsakega izraza, v katerem nastopa število z decimalno piko: `1/3.` vrne `0.333333`.

Najpogostejše konstante so `Pi`, `E`, imaginarna enota `I` in neskončnost `Infinity`.

Z izrazi, v katerih nastopajo simboli brez vrednosti, Mathematica računa simbolno:

```
D[x^3, x]
Integrate[x^2, x]
Integrate[x^2, {x, 0, 1}]
Sum[k, {k, 1, 100}]
Limit[Sin[x]/x, x -> 0]
```

Rezultati so po vrsti odvod `3 x^2`, nedoločeni integral `x^3/3` (brez konstante), določeni integral `1/3`, vsota `5050` in limita `1`.
Seznam `{x, 0, 1}` pove, katera spremenljivka teče in med katerima mejama.
Enako obliko ima pri vsoti, srečali pa jo boste tudi pri risanju grafov.

## Spremenljivke

Z enačajem izrazu ali vrednosti daste ime:

```
g = 9.81
izraz = x^2 + 1
```

Odslej Mathematica ime `izraz` povsod nadomesti z izrazom `1 + x^2` (člene uredi po svoje), zato `D[izraz, x]` vrne `2 x`.
Svoja imena pišite z malo začetnico, da jih ne zamenjate z vgrajenimi.
Če vrstico končate s podpičjem, Mathematica njenega rezultata ne izpiše.

Ime velja, dokler ga ne počistite s funkcijo `Clear`, na primer `Clear[izraz]`, ali ne ustavite jedra.
Velja v vseh celicah in tudi v drugih odprtih zvezkih.

## Pravila

Vrednost izraza pri $x = 3$ izračunate s _prepisovalnim pravilom_ (angl. _rule_):

```
izraz /. x -> 3
```

Pravilo `x -> 3` pomeni »`x` zamenjaj s `3`«, operator `/.` pa pravilo uporabi na izrazu, ki stoji pred njim.
Rezultat je `10`, simbol `x` pa ostane brez vrednosti.
Puščico napišete z znakoma `-` in `>`, Mathematica pa ju sama združi v `→`.

Simbol lahko zamenjate tudi z izrazom: `izraz /. x -> t + 1` vrne `1 + (1 + t)^2`.
Več simbolov hkrati zamenjate s seznamom pravil.
Tako v isto formulo vstavite različne nabore vrednosti:

```
diskriminanta = b^2 - 4 a c
diskriminanta /. {a -> 1, b -> -3, c -> 2}
diskriminanta /. {a -> 1, b -> 2, c -> 5}
```

Zadnji dve vrstici vrneta `1` in `-16`, simboli `a`, `b` in `c` pa ostanejo brez vrednosti.

`````{admonition} Vrednosti ne vstavljajte z enačajem
:class: warning
Vrednost izraza pri $x = 3$ lahko dobite tudi tako, da napišete `x = 3`.
Vendar ima `x` potem vrednost `3` povsod, tudi v celicah, ki jih izvedete kasneje.
Ko nato napišete `D[izraz, x]`, Mathematica to prebere kot `D[10, 3]` in javi napako `General::ivar: 3 is not a valid variable.`
V celici, ki javi napako, ni nič narobe: vzrok je vrstica, ki ste jo izvedli prej.

Da ima simbol vrednost, vidite po barvi: `x` je črn in ne moder.
Vrednost počistite s `Clear[x]`.
`````

Z enačajem torej stvari poimenujete, s pravili pa vstavljate vrednosti.
Pravila ste že srečali v limiti, `Limit[Sin[x]/x, x -> 0]`, in jih boste še pri risanju.

## Funkcije

Kadar boste v isti izraz vrednosti vstavljali večkrat, definirajte funkcijo:

```
f[x_] := x^2 + 1
```

Podčrtaj za `x` na levi strani pove, da je argument lahko karkoli, in ga poimenuje `x`.
Na desni strani podčrtaja ni.
Funkcije definirajte z operatorjem `:=` in ne z enačajem: desna stran se tako izračuna šele, ko funkcijo pokličete.
Definicija nima izpisa.

Zdaj `f[3]` vrne `10`, `f[t + 1]` vrne `1 + (1 + t)^2`, `f'[x]` pa odvod `2 x`.

Če podčrtaj pozabite in napišete `f[x] := x^2 + 1`, je funkcija definirana samo za simbol `x`: `f[3]` ostane `f[3]`.

## Grafi funkcij

Graf funkcije nariše funkcija `Plot`:

```
Plot[x^2, {x, -2, 2}]
```

Drugi argument pove, katera spremenljivka teče in po katerem intervalu, enako kot pri določenem integralu.
Narišete lahko izraz, funkcijo, ki ste jo definirali, ali več grafov hkrati, če jih naštejete v seznamu:

```
Plot[f[x], {x, -2, 2}]
Plot[{Sin[x], Cos[x]}, {x, 0, 2 Pi}]
```

Videz grafa določite z nastavitvami (angl. _options_).
Nastavitve so pravila, ki jih naštejete za drugim argumentom:

```
Plot[f[x], {x, -2, 2}, PlotRange -> {0, 3}]
```

Nastavitev `PlotRange` določi, kateri del navpične osi je prikazan.
Ostale nastavitve so naštete v dokumentaciji funkcije `Plot`.

## Liki

Slike, ki niso grafi funkcij, sestavite iz likov s funkcijo `Graphics`:

```
Graphics[{Circle[{0, 0}, 1], Point[{1, 0}], Line[{{-1, 0}, {0, 1}}]}]
```

Točko podate kot seznam dveh koordinat, na primer `{1, 0}`.
`Circle[{0, 0}, 1]` je krožnica s središčem `{0, 0}` in polmerom `1`, `Point[{1, 0}]` je točka, `Line` pa dobi seznam točk in jih po vrsti poveže z daljicami.
Like naštejete v seznamu.

Barvo in velikost določite tako, da ju v seznamu napišete pred lik, na primer `Red` ali `PointSize[Large]`; veljata za vse like, ki sledijo.
Koordinatni osi doda nastavitev `Axes`:

```
Graphics[{Circle[{0, 0}, 1], Red, PointSize[Large], Point[{1, 0}]}, Axes -> True]
```

Druge like, na primer `Disk`, `Rectangle` in `Triangle`, najdete v dokumentaciji funkcije `Graphics`.

## Dokumentacija

Mathematica ima več tisoč vgrajenih funkcij.
Najpogostejše si boste zapomnili, ostale pa se naučite poiskati.
Kratek opis funkcije dobite z vprašajem pred njenim imenom, na primer `?Plot`.
Celotno dokumentacijo odprete v meniju **Help** > **Wolfram Documentation**.
Primeri v njej so celice, ki jih lahko spremenite in izvedete.

## Naloga

Rešujte naloge v [zvezku](11-racunanje-z-mathematico/mathematica1.nb).
