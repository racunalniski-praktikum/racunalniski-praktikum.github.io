# Tačke v vesolju (10 točk)

V datoteki `kuzki.csv` so zbrani leti sovjetskih psov na raketah in vesoljskih plovilih med letoma 1951 in 1966.
Vsaka vrstica opisuje enega psa na enem letu: datum leta, ime psa in plovilo.
Datoteka je kodirana v UTF-8, podatki v njej pa so ločeni z vejicami.
Rešitev shranite v priloženi delovni zvezek `tacke-v-vesolju.xlsx`, ki že vsebuje tabelo `Plovila`.

1. (3 točke) Podatke iz datoteke `kuzki.csv` uvozite na nov list delovnega zvezka.
   List in tabelo s podatki preimenujte v `Leti`.
2. (2 točki) Tabeli `Leti` dodajte stolpec `Vrsta leta`, v katerem s funkcijo `XLOOKUP` iz tabele `Plovila` poiščete, ali je bil let suborbitalni ali orbitalni.
3. (2 točki) S pogojnim oblikovanjem zeleno obarvajte imena psov, ki so v vesolje leteli več kot enkrat.
4. (3 točke) Na nov list z imenom `Vrtilna` postavite vrtilno tabelo, ki za vsakega psa prikaže, kolikokrat je letel.
   Pse v njej uredite padajoče po številu letov.

Podatki so iz članka [Собаки в космосе](https://ru.wikipedia.org/wiki/Собаки_в_космосе) na ruski Wikipediji (licenca CC BY-SA 4.0).
