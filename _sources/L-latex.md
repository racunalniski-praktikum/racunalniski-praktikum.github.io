# LaTeX: pogosta vprašanja in reševanje težav

(latex:preverjanje-namestitve)=
## Preverjanje namestitve

V datoteko `latex-test.tex` prekopirajte spodnje navadno besedilo in jo shranite
s <kbd>Ctrl</kbd>+<kbd>S</kbd> (🍎 <kbd>Cmd</kbd>+<kbd>S</kbd>).
```
\documentclass{article}
\begin{document}
\section*{Pitagorov izrek}
V pravokotnem trikotniku s katetama \(a\) in \(b\) ter hipotenuzo \(c\) velja
\[ a^2 + b^2 = c^2 \]
\end{document}
```

Če to ne dela, preverite najprej:
1. Šumniki in presledki v poti do datoteke lahko povzročajo težave. To pomeni, da teh znakov ne sme biti v imeniku, ki vsebuje LaTeX datoteko, pa tudi ne v nobenem od imenikov, ki ga vsebujejo.
2. LaTeX lahko ne dela tudi, če imate datoteko shranjeno na Namizju ali v OneDrive.

Če še vedno ne dela, preverite, da ste [namestili vse programe](namestitev:latex).
1. V ukazni vrstici preverite, če se odzove Perl z `perl -v` (to izpiše verzijo).
2. Ali imate nameščeno distribucijo LaTeX-a za vaš operacijski sistem (MikTeX/MacTeX/...)? Namestitev lahko preverite v ukazni vrstici z ukazoma `pdflatex -version` in `latexmk -version`. Če se izpišeta verziji programov, je to dobro.
3. Ali imate nameščeno razširitev za VSCode LaTeX Workshop?
4. Ali ste ponovno zagnali računalnik, odkar ste namestili zgornje programe? Če ne, to naredite zdaj.
5. Na Windows odprite program MikTeX Console in poiščite posodobitve (_Check for updates_) in jih po potrebi namestite.
6. Pogosto pomaga tudi, če zaprete in ponovno zaženete VSCode.

### Nekatere pogoste težave (Windows)

- [`The Perl interpreter could not be found.`](https://tex.stackexchange.com/questions/158796/miktex-and-perl-scripts-and-one-python-script): preverite, da imate res nameščen Perl in da operacijski sistem ve, [kje je](https://www.wikihow.com/Change-the-PATH-Environment-Variable-on-Windows). Poti ne spreminjajte sami. Pogosto zadošča, da ponovno zaženete računalnik.
