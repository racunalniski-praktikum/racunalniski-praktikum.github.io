# Paleta ukazov

Do palete ukazov dostopate z bližnjico <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>P</kbd> (🍎 <kbd>Cmd</kbd>+<kbd>Shift</kbd>+<kbd>P</kbd>).
V paleti ukazov začnete tipkati ime ukaza, z vnašalko <kbd>↵</kbd> pa izberete ukaz, 
ki je prvi na seznamu najdenih ukazov.

## Splošni ukazi

-   `uppercase` (_Transform to Uppercase_): črke označenega besedila spremeni v velike začetnice.
-   `wrap` (_Wrap with Abbreviation_):  označeno besedilo obda s HTML značko.
-   `select all occ` (_Select All Occurences of Find Match_) lahko uporabite v kombinaciji z iskanjem in zamenjavo
    (angl. _Find_ in _Replace_), ali tako, da najprej označite niz znakov.
    Ukaz naredi kurzor za vsako pojavitvijo iskalnega ali izbranega niza.


(paleta-ukazov:html)=
## HTML

Ukaz _Wrap with Abbreviation_ označeno besedilo obda z značko, ki jo napišete.
Če besedilo ni označeno, bo urejevalnik značko postavil okrog vrstice, v kateri je kurzor.
Ko ste v paleti ukazov, lahko poiščete zobato kolo na desni strani vrstice z ukazom.
To je ikona za nastavitve. Če jo kliknete, pridete na stran z nastavitvami,
kjer si lahko za ta ukaz nastavite svojo neposredno bližnjico.

VSCode vam dovoli uporabljati [več kurzorjev hkrati](bliznjice:kurzorji), kar se da lepo uporabiti z
ukazom _Wrap with Abbreviation_.
Ko ste pripravili kurzorje, uporabite bližnjico za paleto ukazov in nadaljujete enako,
kot pri enem samem kurzorju.

(paleta-ukazov:latex)=
## LaTeX

_LaTeX Workshop: Surround selection with LaTeX command_, 
ki izbrano besedilo obda z ukazom, `\ukaz{izbrano besedilo}`. 
Ko izberete ta ukaz, se vam pokaže še vnosno polje, 
v katerem izberete LaTeX-ov ukaz (`title`, `section`, itd.).

_LaTeX Workshop: Surround selection with \begin{}...\end{}_. 
Ta ukaz izbrano besedilo obda z `\begin{}` in `\end{}` in pripravi dva kurzorja 
(enega v `begin` in drugega v `end`), s katerima lahko napišete ime okolja. 
Dveh kurzorjev se iznebite tako, da stisnete tipko `Esc`.