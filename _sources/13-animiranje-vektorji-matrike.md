# Animiranje, vektorji in matrike

Interaktivne risbe naredimo s funkcijo Manipulate, takole:

```
Manipulate[
  Plot[Sin[x (1 + a x)], {x, 0, 6}], 
  {a, 0, 2}
]
```

Funkcija Manipulate je podobna funkciji Plot, pri uporabi pa izvorna koda še hitreje postane nepregledna. 
Takole se lahko izognete marsikateri težavi:

1. Najprej narišete samo najbolj osnoven graf (s funkcijo Plot). Če je funkcijski predpis dolg, ga definirajte posebej.
2. Dodate ostale grafične elemente (točke, izključena območja, barvanje območij, ipd.)
3. Če želite risbo narediti interaktivno, pripravimo osnutek za Manipulate in vanj prilepimo risbo od prej:

```
Manipulate[
  Plot[...],
  (*tu naštejemo drsnike*)
]
```

## Naloga

Rešujte naloge v [zvezku](13-animiranje-vektorji-matrike/mathematica3.nb).
