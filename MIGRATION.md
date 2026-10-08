# Migration

## Rule

Legacy content moves into the target structure **one coherent unit at a time**.
It is in one of two places:

- in the tree: the legacy chapters in `ucbenik/` (A),
- in the history only: the legacy slides (B), at commit `261a63a^` of
  `predavanja/`. Bring a file back with `git show 261a63a^:<path> > <destination>`,
  and name the source path in the commit message: Git cannot link the new file to
  its history,
- in the private repo `zbornica`: the selected content (C). It migrates with its
  history, by the procedure below.

Each migration PR:

1. moves (and, where needed, rewrites) one unit to its destination,
2. deletes the legacy copy of that unit in the same PR, if it is in the tree,
3. records any convention decided along the way in `CLAUDE.md`.

The checklist below doubles as the to-do list.

The target structure is not decided yet, so the **first migration PRs also
propose structure**: pick a unit, propose a destination in the PR, agree in
review, then fill in the Destination column here.

Where content moves unchanged, use `git mv` so rename detection keeps history
readable.

## History access

- A keeps its native paths: `git log --follow ucbenik/<file>`.
- B was merged as a subtree, so `git log --follow` does not cross the merge
  boundary; query the original path instead: `git log 261a63a^ -- <file>`.
- C keeps its history in `zbornica`. The procedure below brings only the commits
  touching the unit under its current name; deeper history (pre-move paths,
  excluded directories) remains in the private `zbornica` repo.

## Migrating from zbornica

`zbornica` remains the private, living staff repo. Exams, future-exam ideas,
`analiza/`, `arhiv/`, and `demonstratorji/` are **never** imported — this repo is
public and history cannot be un-published. To migrate a content unit with its
history:

```bash
git clone --no-local <zbornica> /tmp/zb && cd /tmp/zb
git filter-repo --path <unit-path> --path-rename <unit-path>:<destination>
# audit: git log --all --pretty=format: --name-only | sort -u  (nothing sensitive?)
cd <this repository>
git remote add zb-tmp /tmp/zb && git fetch zb-tmp
git merge --allow-unrelated-histories zb-tmp/main
git remote remove zb-tmp
```

## Units

Legend: **A** = the legacy textbook, in the tree at `ucbenik/`; **B** = the legacy
slides, at `261a63a^` in the history of `predavanja/`; **C** = selected content of
the private staff repo `zbornica`.
**[M]** = mostly mechanical, **[J]** = needs author judgment.
**Plan** = the lecture (see *Lecture plans*) that the unit now serves. It says *what the
material is for*; **Destination** still says *where the file goes*, and stays TBD
until the target structure is agreed.

| # | Unit | Sources | Plan | Destination | Notes |
|---|------|---------|------|-------------|-------|
| 1 | Uvod (o predmetu) | A: `ucbenik/00-uvod.md`; B: `01-uvod/` (partly) | L1 | TBD | [J] B's intro slides also cover terminal/VS Code — split with unit 2; C1 is resolved in `predavanja/00-uvod/` |
| 2 | VS Code in terminal | A: `ucbenik/01-vscode-in-terminal{.md,/}`; B: `01-uvod/` (partly) | L1 + L2 | TBD | [J] one legacy unit becomes two lectures |
| 3 | Git in Markdown | A: `ucbenik/02-git-in-markdown{.md,/}`; B: `02-git/` | L3 (+ L1) | TBD | [J] Markdown moves out to L1 (the README exercise is already in the chapter 1 draft); L3 keeps the diff argument |
| 4 | HTML | A: `ucbenik/03-html{.md,/}`; B: `03-html/` | L4 | TBD | [J] encodings and `podnapisi/` move out to L1 (C3) |
| 5 | CSS | A: `ucbenik/04-css{.md,/}`; B: `04-css/` | **dropped** | — | [J] no longer taught; keep only what L4's mention and the Copilot exercise need (C2) |
| 6 | Utrdimo osnove | A: `ucbenik/05-utrdimo-osnove{.md,/}` | L2 + L3 | TBD | [J] regex task 1 → L2; the rest is a mixed revision sheet |
| 7 | Uvod v LaTeX | A: `ucbenik/06-uvod-v-latex{.md,/}`; B: `05-latex/` | L5 | TBD | [J] |
| 8 | Okolja in sklicevanje | A: `ucbenik/07-okolja-in-sklicevanje{.md,/}`; B: `06-sklicevanje/` | L6 | TBD | [J] |
| 9 | Predstavitve | A: `ucbenik/08-predstavitve{.md,/}`; B: `07-predstavitve/` | L8 | TBD | [J] B's image-format slides move out to L7 (unit 10). Beamer is examined, as one variant of the LaTeX task — keep the material that supports it |
| 10 | Risanje (TikZ) | A: `ucbenik/09-risanje{.md,/}` | L7 | TBD | [J] no B counterpart; L7 is on pictures in general (including images, formats, RGB and CMYK), with TikZ only as a demo, so the chapter's syntax tour shrinks; gains image formats from unit 9 |
| 11 | Pogoste napake v LaTeXu | B: `08-poprava/` | split across L5–L8 | TBD | [J] no longer one lecture — becomes ten-minute openers (C4) |
| 12 | Razpredelnice | A: `ucbenik/10-razpredelnice{.md,/}`; B: `09-excel/` | L9 | TBD | [J] no deck, by design — taught live in Excel (G1); rebuild `rezultati.xlsx` on the five-task exam (G5) |
| 13 | Mathematica | A: `ucbenik/{11,12,13}-*{.md,/}`; B: `10-mathematica/` | L10 + L11 + L12 (+ L13–14) | TBD | [J] three tool-tour chapters become three argued lectures — a rewrite, not a move (C5); no deck, by design — taught live (G1); rewrite rules are missing everywhere (G6) |
| 14 | Dodatki / plonkci (A–H) | A: `ucbenik/{A..H}-*.md` | support | TBD | [M] except `H-regex.md` → L2 (C6) and `A-programska-oprema.md`, which needs new entries (G3) |
| 15 | Slide infrastructure | B: `pomozno/` | all | TBD | [J] blocked on the slides-technology decision |
| 16 | Book build config | A: `ucbenik/{_config.yml,_toc.yml,_toc-plan.yml,myst.yml,_static/,extensions/}` | — | TBD | [J] blocked on jupyter-book vs mystmd; fix old repo URL; both TOCs still list CSS (C2) |
| 17 | Cleanup | A: `ucbenik/L-latex`, `ucbenik/00-razno/` | — | — | [M] likely delete, after checking nothing references them |
| 18 | Vaje (navodila in rešitve za izvajalce) | C: `vaje/` | all | TBD | [J] mirrors A's chapter numbering, which the plan changes; solutions become public on push — review first. **`00-izvedba-vaj.md` holds the purpose of the course and the tutorial calibration** — both are now recorded in *To do: the README* (Purpose) and in `CLAUDE.md` (*Course principles*), so they survive this unit |
| 19 | Gradiva (pregled poglavij) | C: `gradiva/` | L5–L8, L10–L12 | TBD | [J] LaTeX and Mathematica chapter overviews |
| 20 | Domače naloge | C: `domace-naloge/` | bonus, submitted via Git | TBD | [J] `04-html-css/` is for a dropped topic (C2); submission through Git is what exercises unit 3 |
| 21 | V pripravi (WIP drafts) | C: `v-pripravi.md` | L2 | TBD | [J] draft on files and directories — closest existing text to the new L2 |

The legacy `README.md` and `LICENSE` of B do not migrate; the top-level files
supersede them. `predavanja/README.md` is not legacy: it lists the fourteen planned
lectures.

## To do: the README

The authors write the `README.md` of the merged repository. Its current version has
the old title *Zapiski* and covers only how to build the textbook. Material for it,
from the former `COURSE.md` and the README of `prenova`:

- **What the repository holds.** The textbook in `ucbenik/`, published at
  <https://racunalniski-praktikum.github.io/>, and the lecture slides in
  `predavanja/`. The legacy slides are in the history of `predavanja/` (at
  `261a63a^`); selected content migrates from the private `zbornica`.
- **Purpose.** The course gives students the skills to survive a mathematics degree.
  It does not teach a list of commands for LaTeX, Excel and Mathematica. Three
  threads carry it:
  1. *Syntax exists.* Students will meet several of them. Things do not work if you
     ignore it.
  2. *Debugging.* Read what the computer tells you, including the stack trace. The
     style differs by tool: LaTeX is bisection, Mathematica is not.
  3. *Find help yourself.* We do not know everything about these programs, and do
     not want to. Language models change this thread.
- **Theme: semantics versus surface appearance.** Every topic is an instance of the
  same distinction: the layer that says what a thing *is* against the layer that
  says what it *looks like*. For example, a heading in HTML against text that is only
  bold and bigger, or `\label` against a number typed in by hand. A language model is
  very good at producing plausible surface; the layer underneath is the one a
  student can check.
- **The language-model thread.** It runs through the whole course, not as a separate
  unit. Each week: ask, check, state the verdict out loud. The lesson is "you reached
  for the wrong tool", never "the model is bad". The question is prepared so that the
  answer is checkable, not so that the model fails. It is thread 3 with the tool
  changed. The bonus points for errors found in the materials are the same action,
  with points attached. Lectures 13 and 14, on how language models work, are its
  payoff.
- **Lecture format.** Open on a bad practice that a student would genuinely reach
  for, then improve it by explaining how the thing works. Not every lecture has one:
  an invented bad practice is worse than none.
- **Directory trees.** The pictures of directory trees in the textbook are SVG,
  built from a `.drevo.json` description that lies next to each picture, by the
  script `orodja/drevo.py` in the private `zbornica`. Both are kept, so that a reader
  without the script can see what the tree says. They replace the PNG pictures made
  with [folder2image.com](https://www.folder2image.com).

## Lecture plans

The plan for each of the fourteen lectures: its content, its opening bad practice, and
its instance of the theme (*To do: the README*). The list of lectures is in
`predavanja/README.md`. A plan is a draft until its lecture and its chapter are
written. Then delete its section: what it decided lives in the material.

### Why each topic is in the course

The plans below say how each topic is introduced. This says why it is in the course
at all. Only the Excel and Mathematica rows are recorded in the existing material;
**the rest are drafted and need confirmation.**

| Topic | Reason |
|-------|--------|
| Editor, encodings, terminal, regexes | The student uses a computer for the whole degree |
| Git | The submission channel for the homework, and the only version control they meet |
| Markup | Writing that survives a diff, and the way in to LaTeX |
| LaTeX | Every mathematical text they write, from the seminar report onward |
| Pictures | Every figure in those texts |
| Presentations | Every talk they give |
| Excel | Employers expect it. Handling data comes with it |
| Mathematica | Later courses use it. It is also the on-ramp to *Programiranje 0* |
| How language models work | They will use one whatever we do. Whether they can check it is up to us |

### 1. Text editor (VS Code), Markdown, encodings

**The hour, in order.** It is full. If it overruns, the schedule catches up in
lecture 3, which has slack.

1. **Admin, about 10 minutes.** Go through the schedule table on Moodle. Moodle holds
   the logistics, including the rules; the lecture does not repeat them on slides.
2. **Word against VS Code, about 5 minutes.** The bad practice.
3. **Markdown, the larger part of the hour.**
4. **Encodings, a short demo.** A file is bytes. An encoding says what those bytes
   mean. Example: subtitle files from a torrent that show the wrong letters. The
   lecture does not explain `iconv`.
5. **A tour of editing features, about 3 minutes:** multiple cursors, find and
   replace. No regexes here; they belong to lecture 2. The tutorials drill these
   features.

**Theme.** The bytes are what the file *is*. The letters on the screen are one
reading of them. The encoding demo shows this directly.

**Encodings after the lecture.** Students practise conversion in an elective homework
and choose the tool themselves. Because the homework is elective, encoding exercises
come back in later tutorials and are on the mock exam, so that every student practises
before the exam's first task.

**Open.** How many files does the encoding homework have: ten, or two or three chosen
files? The argument for fewer: a near-miss file (only the šumniki wrong) shows the
point better than many files, and is equally easy to check. And does the
torrent-subtitle example go in the demo, in the homework, or in both?

### 2. File system and terminal, regexes

**Hook.** Do you understand the text Claude writes when it manipulates your files?
That question is the contract for the whole term. The lecture teaches students to read
the commands that an agent issues.

**Content, in order.**

1. **Paths, about 5 minutes.** Where things actually live. The paths in the agent's
   output are the paths on your own machine.
2. **Shell basics, about 10 minutes:** `ls`, `cd`, `cat`.
3. **Pipes, about 10 minutes:** `echo`, `|`, `wc`, `grep`.
4. **Regexes, about 10 minutes**, because the commands an agent issues use them. Shown
   in VS Code, where a pattern selects all its matches, and in `grep`.

**Closing point.** Sometimes a regex beats asking a model.

**Theme, to be added.** The path is what the file is; the icon and the folder name are
what it looks like. The legacy material teaches paths without saying this.

### 3. Git

**Opener.** How do you store your files? Students answer with emailing themselves, or
a second Discord account.

**The fair middle step.** OneDrive. It does keep history, so do not dismiss it. It
breaks on per-file churn: it cannot say which change mattered, and it has no snapshot
of a whole project.

**Content.** Readable commit messages. Commits that span several files. Conflicts as
the price of working together — when one appears in the tutorial, raise your hand for
the tutor.

**The diff argument belongs here:** Word is opaque to Git, Markdown is not. Students
know Markdown from lecture 1, and the README they wrote in the chapter 1 tutorial is
the first file they commit.

**Slack.** Markdown no longer takes time in this lecture. Keep the time free: lecture 1
is full and can overrun.

**Theme, available cheaply.** A readable commit message says what changed and why; the
file itself says only how it looks now. The lecture already argues for readable
messages, so this costs one sentence.

### 4. HTML

**Bad practice.** Making text bold and bigger to mean a heading. Word's styles are
the positive case: Word can do this properly.

**Content.** HTML as the same idea as Markdown, said more loudly. Students know
Markdown from lecture 1, so the lecture starts directly with HTML.

**CSS is mentioned as existing, but not taught.** Students adjust it with Copilot in
the exercises.

**Internet and DNS are trimmed to almost nothing.**

**Theme.** A heading, against text that is bold and bigger. The canonical instance,
and the lecture is built on it.

### 5. LaTeX intro

**Lead with the equations argument.** Take a long paper dense with mathematics. Are
you going to click all of that together?

**Content.** Rebuild part of it in LaTeX. Show why the typography is calmer. Then
preamble, packages, compilation.

**Be fair to Word.** Word has styles. It simply does not make you use them.

**Theme.** `\epsilon` against `\in` — invisible in the output, fatal in the source.

### 6. Sklicevanje

**Bad practice.** A document with numbers typed in by hand.

**Three escalating failures, one fix each.**

1. Insert a section — the numbers break, visibly.
2. Cross-references break silently.
3. The bibliography breaks in both directions.

**Theme.** `\label` against a number typed in by hand.

### 7. Pictures

A lecture on pictures in general, not on TikZ.

**Content.** Including images in a document. Choosing the right format, vector
against raster. RGB and CMYK. A TikZ demo.

**TikZ is a demo, not a syntax tour.** By the cut criterion, TikZ is what a student
looks up when they need it. The demo shows what it can do, so that they know it
exists.

**Escalation.** A picture that scales. A picture you can edit. A picture whose fonts
match the document. A picture that is revealed in step with what you are saying — the
last step points forward to Beamer in lecture 8.

**This lecture carries the image-format points of the exam** (exam design in the
private `zbornica`, `preverjanje-znanja/README.md`). TikZ itself stays unexamined.

**Theme.** A drawing, against a picture of a drawing.

### 8. Presentations

This lecture is really *how to give a talk*. The bad practice is a slide you read
aloud.

**Keep the advice, drop the reason.** The standing advice was: use PowerPoint for
mathematics talks *because* equations are hard to write in it. The norm is right —
slide after slide of equations is a bad talk. The reason is not. It rests on a defect
of the tool, a model removes the defect, and it points students away from Beamer,
which is what the exam tests. State the norm directly instead.

**Beamer gets 15–20 minutes at the end**, enough that the tutorials have something to
build on. Note that Beamer is examined — it is one of the two variants of the LaTeX
exam task — so these 15–20 minutes and the three tutorial hours that follow are the
whole of its teaching.

**It teaches only presentations and Beamer.** Image formats are in lecture 7.

**No instance of the theme, and none is needed.**

### 9. Excel

Assume the basics.

**Two bad practices, each of which causes the other:** putting data in rows rather
than columns, and not knowing that the table feature exists.

**Content.** Named tables. Formulas that read like sentences. Pivot tables, on the
real course grades file. Conditional formatting as the closing item.

**Taught by live demonstration in Excel itself**, not from slides. See `MIGRATION.md`,
G1.

**Theme.** A named table, against cells that are merely next to each other.

### 10. Mathematica — why do you trust it?

**Bad practice.** Using an LLM for everything: expensive, slow, unpredictable.

**Demonstration.** A thousand integrals on your laptop in a millisecond, while the
model is still writing the first one. The point is not that a model cannot do an
integral. The point is that it cannot do a thousand.

**Then trust.** Mathematica is not infallible. It is wrong *predictably*:
deterministic, documented, checkable.

**Theme.** Wrong predictably, against right plausibly. This is where the theme meets
trust.

### 11. Lists, tables, ranges, rewrite rules

Doing something to twenty items by hand, against `Map` and `Table`: describing a
computation instead of performing it. **This is the course's strongest instance of the
theme — say so in the lecture.**

**Rewrite rules belong here** (`->`, `/.`, and `:=` against `=`). They were missing
from the plan. They are the same idea once more: a rule describes a transformation,
where applying it by hand performs one.

**This hour is full.** Plotting moved out to lecture 12 for that reason.

This is the on-ramp to *Programiranje 0* in term 2.

### 12. Visualization: plotting and `Manipulate`

Plotting and `Manipulate` in one hour. The syntax is the same and the aim is the same:
build a picture from a description, then let a parameter move.

**The opening bad practice is not yet chosen.**

**Taught by live demonstration**, like lectures 9 to 11.

**Theme.** A plot computed from a description, against a drawing that looks like a
plot.

### 13 and 14. How language models work

Two hours, one topic. Lecture 13 explains how a model works. Lecture 14 closes on a
model running on a laptop with the network off: how big it is, how much worse it is,
and why you would still want it. Not prompt engineering.

**This is the payoff for the thread that runs through the whole term. Protect both
hours.**

**Mathematica is the instrument, not the subject.** Gradient descent is a neat
application of what lectures 10 to 12 taught. The Mathematica thread therefore runs to
the end of the term — five hours, 10 to 14 — with the last two using the tool for
something else.

**Theme.** The theme itself.

## Conflicts with the course plan

Places where the legacy material contradicts the course plan. Each entry is resolved by
the migration PR for its unit, and this list shrinks to empty with the checklist
above. Nothing here has been changed yet, except C1.

### C1 — The rule stated to students contradicts the plan

**Resolved 2026-09-30 in `predavanja/00-uvod/`.** The intro slides now link to
Moodle, which states the rule, and the topic list is removed. Lecture 1 goes through
the schedule table on Moodle. The legacy copy described below is only in the history.

`B: 01-uvod/prosojnice.html:67` states
`uporaba umetne inteligence **ni dovoljena**` — AI use is not permitted.

This is the only mention of language models in the whole legacy corpus, and it is a
prohibition. The plan runs LLM use through every week as a thread, and devotes
lectures 13 and 14 to it. **This single line must change before anything else is
shown to students.**

The replacement rule, decided 2026-09-21: students may use language models as they
wish, and have no access to them at the exam, because the network is shut down there.
Both halves belong on the slide — the permission and the exam condition — since the
exam condition is what makes the permission safe to give.

The same file, line 24, lists the course topics to students. It still includes CSS,
and it omits **encodings, regexes and language models** — three of the redesign's
additions. The slide has to be rewritten against the fourteen lectures, not patched.

**The bonus points for errors found in the materials** (line 66 of the same file) are
the opposite case: they stay exactly as they are. *To do: the README* now names them as the
existing mechanism of the language-model thread.

### C2 — Material for a dropped topic (CSS)

| Path | What it is |
|------|------------|
| `A: ucbenik/04-css.md` | 242-line chapter, three exercises |
| `A: ucbenik/04-css/` | its figures and files |
| `B: 04-css/` | reveal.js deck and the `primer/recepti.*` worked example |
| `C: vaje/04-css/` | instructor solution (`resitev.{html,css}`), `normalize.css` |
| `C: domace-naloge/04-html-css/` | homework built on CSS |
| `C: domace-naloge/{dokument-resitev.html,oblikovanje-resitev.css}` | its solution |

**Exercise text that still promises CSS teaching:**

- `A: ucbenik/03-html.md:277` — "in oblikovanje (CSS, ki ga bomo srečali na naslednjih
  vajah)" — *and formatting (CSS, which we will meet in the next tutorial)*. The plan
  has no next CSS tutorial. This sentence is the natural place to put the new
  "mentioned, not taught" framing instead.
- `C: vaje/00-izvedba-vaj.md:83` — an `## HTML/CSS` section in the instructor notes.

**Build configuration that still lists CSS as a chapter:**

- `A: ucbenik/_toc.yml:9` and `A: ucbenik/_toc-plan.yml:9`.
- `B: README.md:12–13` — lecture 4 with its deck and example.

### C3 — Material in the wrong lecture (encodings)

Encodings are taught in the HTML lecture. The plan moves them to lecture 1, as a short
demo (a file is bytes; an encoding says what those bytes mean).

- `B: 03-html/prosojnice.html:125,153,176,200,216` — the five code-table slides
  (ASCII, ISO-8859-1, ISO-8859-2, Windows-1250, UTF-8).
- `B: 03-html/podnapisi/{cp1250,iso8859-2,utf8}.srt` — three subtitle files of the
  same text in three encodings. These already match the plan's torrent-subtitle
  example and should move with the slides.

Note that `A: ucbenik/03-html.md` teaches encoding only as
`<meta charset="UTF-8">` (line 172). The textbook therefore loses almost nothing
here, while the slides lose close to half of theirs (about 100 of 225 lines).

### C4 — A lecture that is no longer a lecture

`B: 08-poprava/` is a 466-line Beamer deck of about twenty frames on common LaTeX
mistakes. The plan breaks it into ten-minute openers at the start of lectures 5–8,
each placed where its mistakes are fresh.

This is a split by topic, not a move. The frames group cleanly (`align` and `&`,
numbering, `\ensuremath`, paragraph breaks, display style), so the split is
tractable — but it is a judgment call about which lecture each group belongs to, and
it cannot be done with `git mv`.

### C5 — Ordering and framing changed, Mathematica

Mathematica keeps its three hours. Only the framing changes, and it changes
completely.

The three textbook chapters (`11-racunanje-z-mathematico`, `12-risanje-in-enacbe`,
`13-animiranje-vektorji-matrike`) are a tour of the tool: cells, syntax, then
features. The plan's lectures 10–12 are an argument:

| Lecture | What it argues |
|---------|----------------|
| 10 | Why do you trust it — wrong predictably against right plausibly |
| 11 | Describing a computation instead of performing it (`Map`, `Table`, rewrite rules) |
| 12 | Visualization — plotting and `Manipulate`, one description, one moving parameter |

Two consequences for the migration:

- **Plotting moves out of lecture 11 into lecture 12.** Lecture 11 is full without
  it, and plotting shares its syntax and its aim with `Manipulate`.
- **Gradient descent leaves the Mathematica block** and opens lectures 13–14, where it
  is the mechanism rather than a demonstration. `B: 10-mathematica/manipulate.nb`
  therefore serves L12, and the gradient-descent material serves L13.

The material overlaps, but the order and the reason for each part are new. Treat
unit 13 as a rewrite that borrows examples, not as a migration.

`_toc-plan.yml` proposes a different split again (four chapters: `11-uvod-v-mathematico`,
`12-simbolno-računanje`, `13-risanje`, `14-naprednejsa-matematika`). That proposal is
superseded by the lecture plans above; do not implement it.

### C6 — Chapter numbering no longer matches

Three numbering systems are now in play: 13 textbook chapters plus appendices A–H,
10 old lectures, and 14 planned lectures. `C: vaje/` is numbered to mirror the
textbook chapters, so it inherits the mismatch.

The largest single shift: the old chapter 1 (`01-vscode-in-terminal`) becomes two
lectures, so every later number moves.

Also: `A: ucbenik/H-regex.md` is a five-line stub (`capture group`, `?`, `*`, `[|]`)
that no table of contents includes. Regexes are now a named part of lecture 2, so
this stub is either the seed of that material or is deleted.

### Gaps — the plan needs material that does not exist

These are not contradictions. They are lectures with no source to migrate.

- **G1 — Not a gap. Resolved 2026-09-21.** `B: 09-excel/` holds only
  `rezultati.xlsx` and `B: 10-mathematica/` only three notebooks because **lectures
  9–12 are taught live in the application, not from a deck.** No decks are needed.

  The wider decision, recorded in `CLAUDE.md`: **the medium of a lecture follows the
  material it teaches.** Markdown and HTML are taught in reveal.js, LaTeX and Beamer
  in Beamer, Excel in Excel, Mathematica in a notebook. The slides are then an
  additional worked example of the topic, which is why the legacy mix of
  technologies is kept on purpose rather than unified.
- **G2 — Nothing at all for lectures 13 and 14** (how language models work, closing
  on local models). Two hours of one topic, the payoff for the term's thread and the
  hours to protect, so this is the largest piece of new writing in the whole
  migration. One part is not new: gradient descent comes across from the Mathematica
  block (C5), which is why these two hours are also the last two of the Mathematica
  thread.
- **G3 — No installation instructions for any model.** `A: ucbenik/A-programska-oprema.md`
  covers the command line, VS Code, LaTeX, Mathematica, Microsoft and Zoom. The plan
  needs Copilot (lecture 4 exercises) and a local model (lecture 14).
- **G4 — The text-file exam task has to be written from scratch.** Nothing in the
  legacy material can be adapted. The exam itself is not in this repo and stays in
  the private `zbornica`, with its design in `preverjanje-znanja/README.md`.
- **G5 — The Excel grades file encodes the old exam.** `B: 09-excel/rezultati.xlsx` is
  the file lecture 9 builds its pivot tables on. Its columns are
  `HTML | LaTeX | Excel | Mathematica` — **the four-task exam.**
  **To do: rebuild it on the new five-task split** (text files, HTML, LaTeX, Excel,
  Mathematica) before lecture 9 uses it. Otherwise the lecture teaches pivot tables
  over a structure the course no longer has, and the exercise quietly tells students
  the wrong thing about their own exam.
  Publication check, done 2026-09-21: both grade datasets are safe to make public.
  The slides file carries no names, only enrolment numbers running sequentially from
  `27000001`. The 28 names in `A: ucbenik/10-razpredelnice/` are invented.
- **G6 — Nothing on Mathematica's rewrite rules.** `->`, `/.`, and `:=` against `=`
  appear in no chapter, no notebook and no tutorial sheet, and they were absent from
  the first version of the plan. Lecture 11 now names them, so they are new writing
  — small, but with no source to borrow from.
