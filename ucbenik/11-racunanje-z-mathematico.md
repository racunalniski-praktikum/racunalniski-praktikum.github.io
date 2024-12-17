# Osnovna uporaba Mathematice

`````{admonition} Programska oprema
:class: important
- [Mathematica](namestitev:mathematica)
`````



## Celice

Zvezki v Mathematici imajo tri vrste celic: celice z besedilom, vhodne celice in izhodne celice.

Novo celico dodamo tako, da kliknemo v prostor pod obstoječo celico: pojavi se horizontalna črta na mestu, kjer bo ta vstavljena.

Desno od celic so oglati zaklepaji, ki celice združujejo v skupine. 
Z enojnim klikom lahko celico ali skupino celic označimo (npr. za izbris),
z dvojnim klikom pa skupino odpremo ali zapremo.

Na vajah bomo vsebino vhodnih celic vnašali v _Wolframovem jeziku_, ki je najbolj zanesljiv.
**Pozor:** če kopirate vsebino (npr. enačbo) iz celice z besedilom ali PDF datoteke, bodo pogosto nekateri znaki napačni, celica pa se ne bo hotela prevesti.

### Izvajanje

Vhodno celico izvedemo tako, da stisnemo tipki <kbd>Shift</kbd>+<kbd>Enter</kbd>. Če je z našo celico vse ok, se pokaže izhodna celica z rezultatom. Več o tem je v zvezku z uvodnih predavanj.

Izvajanje ukaza lahko prekinemo s tipkami <kbd>Alt</kbd>+<kbd>.</kbd> (pika) oz. 🍎 <kbd>Command</kbd>+<kbd>.</kbd> ali menijsko postavko **Evaluation** > **Abort Evaluation**.
Če nam prekinitev z zgornjimi prejemi ne uspe, potem prekinemo izvajanje jedra z menijsko postavko **Evaluation** > **Quit Kernel** > **Local**.

Številke pred vhodnimi in izhodnimi celicami (`In[številka]` in `Out[številka]`) povedo, v kakšnem vrstnem redu smo celice izvedli.

### Posebni znaki in grške črke

Pogostejši znaki imajo krajše psevdonime oz. dodatna imena (angl. _alias_), ki jih uporabljamo tako, da najprej pritisnemo tipko `Esc`, ki v celico izpiše znak `⋮` (tri navpične pike), nato pa alias.

Primer: napišemo lahko `⋮a` za grško črko alfa.

Več o tem preberite v [dokumentaciji](https://reference.wolfram.com/language/howto/TypeAGreekLetter.html)

## Sintaksa

Argumente funkcij vedno naštejemo v oglatih oklepajih, ločimo pa jih z vejicami: `Funkcija[a, b, c]`.
Vse vgrajene funkcije se začnejo z **veliko začetnico** (to pomeni, da `sin[x]` ni ok, `Sin[x]` pa je).

V zavitih oklepajih `{}` navajamo sezname, obsege in domene.

Mathematica barva izvorno kodo v vhodnih celicah:

* **Nedefinirani simboli** so modri. Na primer, če napišete v celico `sin`, se bo ta simbol obarval modro.
* **Definirani simboli** so črni. Če `sin` popravite v `Sin`, se bo simbol obarval črno.
* **Vezane spremenljivke** so zelene. Na primer, v izrazu za vsoto `Sum[1/(k^2), {k, 1, Infinity}]` je `k`
  pobarvan zeleno.

## Naloga

Rešujte naloge v [zvezku](11-racunanje-z-mathematico/mathematica1.nb).

## Domača naloga

Bo objavljena kmalu.