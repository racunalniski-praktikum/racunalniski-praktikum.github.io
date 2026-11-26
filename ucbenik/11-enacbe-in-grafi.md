# Mathematica 2

`````{admonition} Programska oprema
:class: important
- [Mathematica](namestitev:mathematica)
`````

V tem poglavju bomo uporabili znanje iz prejšnjega poglavja na bolj kompleksnih primerih. 

## Enačbe in neenačbe

Enačbe (in sisteme enačb) rešujemo s funkcijo `Solve`, ki sprejme dva argumenta. V prvega podamo enačbo ali seznam enačb, z drugim pa povemo, katero neznanko oz. neznanke iščemo.

```mathematica
In[1]:= enacba = x^2 - 5 x + 6 == 0
Out[1]= 6 - 5 x + x^2 == 0

In[2]:= resitve = Solve[enacba, x]
Out[2]= {{x -> 2}, {x -> 3}}
```

Rezultat je seznam rešitev, v katerem je vsaka rešitev zapisana s prepisovalnim pravilom. Rešitve torej lahko uporabite enako kot pravila v prejšnjem poglavju, z operatorjem `/.`:

```mathematica
In[3]:= x /. resitve
Out[3]= {2, 3}

In[4]:= enacba /. resitve
Out[4]= {True, True}
```

V `In[4]` smo na desni strani prepisovalnega pravila podali seznam, zato Mathematica izračuna vrednost izraza na levi za vsako rešitev posebej.

Sistem enačb zapišete kot seznam enačb, neznanke pa kot seznam neznank:

```mathematica
In[5]:= sistem = {x + y == 5, x - y == 1}
Out[5]= {x + y == 5, x - y == 1}

In[6]:= resitev = Solve[sistem, {x, y}]
Out[6]= {{x -> 3, y -> 2}}
```

V tem primeru je rezultat je ena rešitev, ki določa obe neznanki.
Tu se vidi, zakaj `Solve` ne vrača samo številskih rešitev: prepisovalna pravila nam povedo, kateri neznanki pripada katera vrednost.
Če želimo dobiti samo vrednosti obeh neznank, lahko prepisovalni pravili uporabimo na seznamu neznank:

```mathematica
In[7]:= {x, y} /. resitev
Out[7]= {{3, 2}}
```

`Solve` poišče vse rešitve, tudi kompleksne.
Če želite samo realne rešitve, dodajte tretji argument `Reals`.

```mathematica
In[8]:= Solve[x^3 == 8, x, Reals]
Out[8]= {{x -> 2}}
```

Rešitev enačbe ni vedno mogoče zapisati s koreni.
Za enačbo `x^5 - x - 1 == 0` vrne `Solve` pet rešitev oblike `Root[...]`: Mathematica ve, da rešitve obstajajo, zapiše pa jih le kot ničle polinoma.
Približke izračuna funkcija `NSolve`, ki prav tako sprejme tretji argument `Reals`:

```mathematica
In[8]:= NSolve[x^5 - x - 1 == 0, x, Reals]
Out[8]= {{x -> 1.1673}}
```

`Solve` in `NSolve` sta namenjena predvsem polinomskim enačbam.
Za druge enačbe, na primer $\cos x = x$, uporabite `FindRoot`, ki poišče eno rešitev blizu začetnega približka:

```mathematica
In[9]:= FindRoot[Cos[x] == x, {x, 1}]
Out[9]= {x -> 0.739085}
```

V seznamu `{x, 1}` je `1` začetni približek.
Ker je rešitev ena sama, rezultat ni seznam rešitev, temveč seznam pravil, zato z `/.` dobite kar število:

```mathematica
In[10]:= x /. FindRoot[Cos[x] == x, {x, 1}]
Out[10]= 0.739085
```

Če ima enačba več rešitev, jih poiščete z različnimi začetnimi približki.

Neenačbe rešuje funkcija `Reduce`:

```mathematica
In[11]:= Reduce[x^2 - 5 x + 6 < 0, x]
Out[11]= 2 < x < 3

In[12]:= Reduce[x^2 - 5 x + 6 > 0, x]
Out[12]= x < 2 || x > 3
```

V drugem rezultatu `||` pomeni »ali«.
Rezultat `Reduce` ni pravilo, temveč pogoj, ki ga mora izpolnjevati `x`.

## Tabele

Funkcijo `Table` ste spoznali v prejšnjem poglavju.
Korak lahko podate kot četrti element seznama, vrednosti spremenljivke pa lahko tudi naštejete:

```mathematica
In[13]:= Table[n^2, {n, 0, 1, 0.25}]
Out[13]= {0., 0.0625, 0.25, 0.5625, 1.}

In[14]:= Table[n^2, {n, {2, 3, 7}}]
Out[14]= {4, 9, 49}
```

Izraz v tabeli je lahko karkoli, kar ste spoznali do zdaj, tudi rešitev enačbe ali graf:

```mathematica
In[15]:= Table[x /. Solve[x^2 == a, x], {a, 1, 4}]
Out[15]= {{-1, 1}, {-Sqrt[2], Sqrt[2]}, {-Sqrt[3], Sqrt[3]}, {-2, 2}}

In[16]:= Table[Plot[x^n, {x, -1, 1}], {n, 1, 4}]
```

Prvi primer vrne rešitve enačbe $x^2 = a$ za štiri vrednosti parametra $a$, drugi pa nariše štiri grafe drugega ob drugem.

## Delo s seznami

Seznam zaporednih celih števil vrne funkcija `Range`.
Funkcija `Select` iz seznama izbere elemente, ki izpolnjujejo pogoj, `Length` pa vrne dolžino seznama:

```mathematica
In[17]:= Range[10]
Out[17]= {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

In[18]:= prastevila = Select[Range[50], PrimeQ]
Out[18]= {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47}

In[19]:= Length[prastevila]
Out[19]= 15
```

Drugi argument funkcije `Select` je pogoj: funkcija, ki za vsak element vrne `True` ali `False`.
Takim funkcijam pravimo predikati.
Imena vgrajenih predikatov se končajo s `Q` (angl. _question_), na primer `PrimeQ`, `EvenQ` in `OddQ`.
Svoj predikat definirate kot vsako drugo funkcijo:

```mathematica
In[20]:= ostanek1[n_] := Mod[n, 4] == 1

In[21]:= Select[prastevila, ostanek1]
Out[21]= {5, 13, 17, 29, 37, 41}
```

`Mod[n, 4]` je ostanek pri deljenju `n` s `4`, zato `Select` izbere praštevila, ki dajo pri deljenju s `4` ostanek `1`.

Funkcija `Map` uporabi funkcijo na vsakem elementu seznama.
Namesto `Map[f, seznam]` lahko pišete tudi `f /@ seznam`:

```mathematica
In[22]:= delitelji = Map[Divisors, {12, 18, 30}]
Out[22]= {{1, 2, 3, 4, 6, 12}, {1, 2, 3, 6, 9, 18}, {1, 2, 3, 5, 6, 10, 15, 30}}

In[23]:= Length[delitelji]
Out[23]= 3

In[24]:= Length /@ delitelji
Out[24]= {6, 6, 8}
```

`Length[delitelji]` prešteje elemente seznama `delitelji`, torej tri sezname, `Length /@ delitelji` pa elemente vsakega od njih.
Mnoge funkcije, na primer računske operacije, same delujejo po elementih, kot ste videli v prejšnjem poglavju; `Map` potrebujete za tiste, ki tega ne počnejo.

Posamezen element seznama vrne funkcija `Part`, ki jo običajno zapišete z dvojnimi oglatimi oklepaji:

```mathematica
In[25]:= prastevila[[3]]
Out[25]= 5

In[26]:= resitve[[2]]
Out[26]= {x -> 3}

In[27]:= x /. resitve[[2]]
Out[27]= 3
```

Elementi so oštevilčeni od `1` naprej.
Ime `resitve` ima še vedno vrednost iz začetka poglavja, zato `resitve[[2]]` vrne drugo rešitev enačbe, z `/.` pa njeno vrednost.

## Vzorci v definicijah

Podčrtaj na levi strani definicije pomeni, da je `x_` vzorec: ujema se s katerimkoli argumentom, Mathematica pa na desni strani vsak `x` zamenja s tem argumentom.
Definicija je torej prepisovalno pravilo, ki ga Mathematica uporabi povsod, kjer se izraz ujema z levo stranjo.
Za isto funkcijo lahko podate več pravil, na primer posebej za izbrane vrednosti argumenta:

```mathematica
In[28]:= fib[1] := 1

In[29]:= fib[2] := 1

In[30]:= fib[n_] := fib[n - 1] + fib[n - 2]

In[31]:= Table[fib[n], {n, 1, 10}]
Out[31]= {1, 1, 2, 3, 5, 8, 13, 21, 34, 55}
```

Mathematica najprej poskusi pravila za izbrane vrednosti in šele nato splošno pravilo, zato se računanje pri `fib[1]` in `fib[2]` ustavi.

Vzorec ima lahko tudi obliko.
Če je argument točka, ga zapišete kot seznam dveh vzorcev:

```mathematica
In[32]:= razdalja[{x1_, y1_}, {x2_, y2_}] := Sqrt[(x2 - x1)^2 + (y2 - y1)^2]

In[33]:= razdalja[{0, 0}, {3, 4}]
Out[33]= 5

In[34]:= razdalja[{0, 0}, 5]
Out[34]= razdalja[{0, 0}, 5]
```

Če se argument z vzorcem ne ujema, Mathematica izraza ne izračuna, tako kot `f[3]` v prejšnjem poglavju, ko ste pozabili podčrtaj.

Vzorec se lahko ujema tudi z obliko izraza.
Funkcija `odvod` ima pravilo za potence, za sinus in za vsoto:

```mathematica
In[35]:= odvod[x^n_] := n x^(n - 1)

In[36]:= odvod[Sin[x]] := Cos[x]

In[37]:= odvod[u_ + v_] := odvod[u] + odvod[v]

In[38]:= odvod[x^3 + Sin[x]]
Out[38]= 3 x^2 + Cos[x]

In[39]:= odvod[Cos[x]]
Out[39]= odvod[Cos[x]]
```

Argument `x^3 + Sin[x]` se ujema z vzorcem `u_ + v_`, zato `odvod` odvaja vsak sumand posebej, vsak sumand pa se ujema z enim od preostalih dveh pravil.
Za kosinus pravila ni, zato `odvod[Cos[x]]` ostane neizračunan.

```mathematica
In[40]:= odvod[x^2 + x]
Out[40]= 2 x + odvod[x]
```

Sumand `x` se z vzorcem `x^n_` ne ujema, čeprav je matematično enak `x^1`: vzorec primerja obliko izraza, ne njegove vrednosti.
Manjkajoče pravilo dodate brez podčrtaja, da se ujema le s simbolom `x`:

```mathematica
In[41]:= odvod[x] := 1

In[42]:= odvod[x^2 + x]
Out[42]= 1 + 2 x
```

S podčrtajem bi se pravilo ujemalo s čimer koli:

```mathematica
In[43]:= odvod[x_] := 1

In[44]:= odvod[Cos[x]]
Out[44]= 1
```

Mathematica še vedno najprej poskusi bolj določena pravila, zato `odvod[x^3 + Sin[x]]` še vedno vrne `3 x^2 + Cos[x]`.
Za kosinus pa namesto neizračunanega izraza zdaj dobite napačen rezultat `1`.

Vsa pravila, ki jih ima funkcija, izpiše `?odvod`.
Nova definicija z enako levo stranjo staro zamenja, definicija z drugačno levo stranjo pa doda novo pravilo.
Napačno pravilo `odvod[x_] := 1` zato ostane, dokler ne pobrišete vseh pravil funkcije s `Clear[odvod]`.

Funkcija `odvod` odvaja le po `x`, ker je simbol `x` zapisan v njenih pravilih.
Za odvod po drugi spremenljivki to spremenljivko podate kot drugi argument in jo v pravilih zapišete z vzorcem:

```mathematica
In[45]:= Clear[odvod]

In[46]:= odvod[y_^n_, y_] := n y^(n - 1)

In[47]:= odvod[Sin[y_], y_] := Cos[y]

In[48]:= odvod[u_ + v_, y_] := odvod[u, y] + odvod[v, y]

In[49]:= odvod[t^3 + Sin[t], t]
Out[49]= 3 t^2 + Cos[t]
```

Ime `y_` se v vsakem pravilu pojavi dvakrat.
Vzorec se ujema le, če se obe pojavitvi ujemata z istim izrazom, zato pravilo za potence odvaja `t^3` po `t`, ne pa po `x`.

## Več o grafih

Graf lahko dopolnite z nastavitvami in ga združite z drugimi slikami.
Nastavitev `Epilog` grafu doda geometrijske objekte, ki jih zapišete enako kot v funkciji `Graphics`.
Nastavitev `Filling -> Axis` pobarva območje med grafom in abscisno osjo:

```mathematica
In[50]:= graf1 = Plot[1 - x^2, {x, -2, 2},
  Epilog -> {Red, PointSize[Large], Point[{{-1, 0}, {1, 0}}]}]

In[51]:= graf2 = Plot[1 - x^2, {x, -1, 1}, Filling -> Axis]
```

Funkcija `Point` s seznamom točk nariše vse točke hkrati.
Ploščino pobarvanega območja izračuna `Integrate`:

```mathematica
In[52]:= Integrate[1 - x^2, {x, -1, 1}]
Out[52]= 4/3
```

Določeni integral je ploščina le, kjer graf leži nad osjo; pod osjo je integral negativen.

Funkcija `Show` nariše več slik v isti koordinatni sistem:

```mathematica
In[53]:= Show[graf1, graf2]
```

Rezultat kaže {numref}`slika %s <slika:graf-nicle-ploscina>`.
`Show` vzame interval in nastavitve od prve slike, zato je prikazan cel interval od `-2` do `2`.
V `Show` lahko sestavite tudi grafe in slike iz funkcije `Graphics`.

:::{figure-md} slika:graf-nicle-ploscina
:width: 50%
:align: center
![Graf funkcije 1 − x² na intervalu od −2 do 2 z rdečima ničlama in pobarvanim območjem med grafom in osjo](11-enacbe-in-grafi/graf-nicle-ploscina.png)

&nbsp; Graf z označenima ničlama in pobarvanim območjem
:::

## Naloge iz več korakov

Mathematica si zapomni vse, kar ste izvedli, zato lahko ime iz ene naloge pokvari drugo.
Pri nalogah iz več korakov se tega obvarujete z dvema navadama:

* Vsako nalogo rešite v svoji celici in celico začnite s `Clear` za vsa imena, ki jih v njej definirate, na primer `Clear[prastevila, ostanek1]`.
  Tako se celica vsakič izvede enako, tudi ko jo po popravku izvedete znova, in v njej ne ostanejo stara pravila, kot napačno pravilo funkcije `odvod`.
* Dolge klice razdelite v več vrstic, vsako nastavitev v svojo, kot pri `graf1` zgoraj.
  Manjkajočo vejico ali oklepaj tako najdete hitreje.

## Naloge

Rešite naloge v [zvezku](11-enacbe-in-grafi/mathematica2.nb).
