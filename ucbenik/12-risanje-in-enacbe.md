# Reševanje enačb in risanje

### Prirejanje

Mathematica ima dva prireditvena operatorja, s katerima lahko definiramo (ali spreminjamo) vrednosti simbolov:

* `=` - takojšnje prirejanje in
* `:=` - zakasnjeno prirejanje.

V zvezku z nalogami si lahko ogledate razliko med njima. 

Zakasnjeno prirejanje bomo potrebovali, kadar bomo definirali funkcijo.
Funkcijo, $f(x) = x^2$ lahko definiramo takole:

```
f[x_] := x^2
```

Pozorni bodite na `_` za imenom parametra (ki ga potem v funkcijskem izrazu ni)
in na prirejanje z operatorjem `:=`.

### Reševanje enačb in neenačb

Prav nam bosta prišli funkciji `Solve` (ter njena numerična različica `NSolve`) in `Reduce`.

Funkcijo `Solve` lahko uporabimo za reševanje enačb. 
Kot rezultat dobimo seznam rešitev v obliki _prepisovalnih pravil_.
O teh morate vedeti samo to, kako jih prepoznate, ter kako se jih po potrebi iznebite.

Takole lahko definiramo funkcijo `f` in poiščemo njene ničle (za zapis enačbe uporabimo dvojni enačaj `==`):

```
f[x_] := (x^2 - 1)/(x^2 - 4)
Solve[f[x] == 0]
```

Če celico poženemo, dobimo rezultat: `{{x -> -1}, {x -> 1}}`.
Puščici v rezultatu označujeta prepisovalni pravili, za nas pa je važno predvsem, 
da so rešitve na desni strani puščice.

Prepisovalnih pravil se iznebimo tako, da jih uporabimo. 
Če bi napisali 

```
x /. Solve[f[x] == 0]
```

bi dobili rezultat `{-1, 1}`. 
Dovolj je, da veste, da morate pred `/.` postaviti tisti simbol, 
ki je napisan pred puščico, kadar dobimo rezultate v obliki prepisovalnih pravil.

S funkcijo `Reduce` rešujemo neenačbe:

```
Reduce[f[x] > 0]
```

### Risanje grafov funkcij

Na vajah boste spoznali funkcije, s katerimi lahko rišemo grafe funkcij.
Te imajo lahko veliko parametrov, zato je ponavadi dobro, da se organiziramo - 
tako je lažje najti napako.

Če želite narisati enostaven graf funkcije, npr. $x^2$ na intervalu $[-2,2], to lahko naredite takole:

```
Plot[x^2, {x, -2, 2}]
```

Kadar je funkcijski predpis daljši in če potrebujete dodatne nastavitve, je lažje, če si definiramo pomožno funkcijo in parametre funkcije Plot napišemo vsakega v svojo vrstico:

```
g[x_] := (x^2 - 1)/(x^2 - 4)
Plot[
  g[x],
  {x, -3, 3},
  Epilog -> {PointSize[Large], Point[{{-1, 0}, {1, 0}}]},
  ExclusionsStyle -> Red
]
```

## Naloga

Rešujte naloge v [zvezku](12-risanje-in-enacbe/mathematica2.nb).

 