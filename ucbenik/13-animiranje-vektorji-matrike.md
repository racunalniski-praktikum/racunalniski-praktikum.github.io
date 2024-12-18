# Animiranje, vektorji in matrike

Interaktivne risbe naredimo s funkcijo Manipulate. Tu stvari še hitreje postanejo nepregledne. Takole se lahko izognete marsikateri težavi:
1. Najprej narišete samo najbolj osnoven graf. Če je funkcijski predpis dolg, ga definirajte posebej.
2. Dodamo še ostale grafične elemente (točke, izključena območja, barvanje območij, ipd.)
3. Če želimo risbo narediti interaktivno, pripravimo osnutek za Manipulate in vanj prilepimo risbo od prej:
Manipulate[
  Plot[...],
  (*tu naštejemo drsnike*)
]
