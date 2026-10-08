# CLAUDE.md

## Project

Renovated course materials for *Računalniški praktikum*, the practical computing
course for mathematics students at FMF, University of Ljubljana: terminal, VS Code,
encodings and regexes, Git, Markdown, HTML, LaTeX, spreadsheets, Mathematica, and
how language models work. This repository holds the
textbook (a Jupyter Book called "ucbenik"), the lecture slides, and the working
documents of the renovation. It is maintained by two authors, Katja Berčič and
Matija Pretnar. All content is in Slovenian.

## Course principles

Guidance for writing the material. The public part of the course design waits for
the README (*To do: the README* in `MIGRATION.md`); the exam design is in the private
`zbornica`, in `preverjanje-znanja/README.md`.

- **Contact hours.** One hour of lectures and three hours of tutorials each week.
  The tutorials carry most of the teaching.
- **The cut criterion: teach what a student cannot learn alone; cut what they will
  look up when they need it.** TikZ is learnable from the documentation at the
  moment of need, so lecture 7 shows it in a demo and does not teach its syntax. A
  convincing surface with nothing under it is not — that is why lecture 13 exists.
  The third thread of the purpose, find help yourself, makes this consistent: a
  topic left out is the thread working, not a gap in the course.
- **Exam points are not the cut criterion.** Lectures 13 and 14 are not examined,
  and they are still the ones to protect. The whole exam assesses the
  language-model thread, because it is taken with the network off, so no task has
  to name the thread.
- **The workload stays as it is.** A change that raises it needs a reason stronger
  than completeness. The measure: a tutorial sheet takes about one hour for a
  student at ease with a computer. A student who needs the whole three hours, or does
  not finish, is pointed to the extra exercises and the homework.
- **Tutorials.**
  - Students must make mistakes early, with feedback. Losing a point on the first
    homework is not a disaster; it is the point of putting it first.
  - Do at least part of the first exercises together.
  - Speed follows comfort with a computer, possibly more closely than it follows
    knowledge. More exercises is the effective remedy, not more explanation.
  - Helping with a commit during the tutorial is fine. What matters is that the
    commit happens; every homework submission exercises Git.

## Repository layout

- `ucbenik/` — the textbook, published as the course website. It holds migrated chapters next to legacy chapters that wait for migration; `MIGRATION.md` tells which is which.
- `predavanja/` — the lecture slides. It holds only the decks prepared for the 2026/27 term; the legacy decks are in the history (below).
- `README.md` — the public description of the repository, written by the authors. Material for it is in *To do: the README* in `MIGRATION.md`.
- `MIGRATION.md` — migration rule, the unit checklist (doubles as the to-do list), the plan for each lecture, and the list of places where the legacy material contradicts the plan. **Which files move where.**

The target content structure is deliberately undecided: it is established
incrementally by migration PRs. Do not create new top-level content directories
outside an agreed migration PR.

Legacy material that is not in the tree:

- the legacy lecture slides are in the history of `predavanja/`, at commit
  `261a63a^` with their original paths (`git show 261a63a^:03-html/prosojnice.html`),
- selected content (`gradiva/`, `vaje/`, `domace-naloge/`, `v-pripravi.md`) is in
  the private staff repo `zbornica`.

### History access

- `ucbenik/` keeps its native paths, so `git log --follow` and `git blame` work directly.
- `predavanja/` was merged as a subtree. `git blame` works directly, but
  `git log --follow` does not cross the subtree boundary. Query the merged parent
  with the original path instead: `git log --follow 0f2bad7 -- <file>`. For the
  legacy slides, use `git log 261a63a^ -- <file>`.

## Conventions

- Language of all content: Slovenian. Language of commit messages: historically Slovenian in both repos — TBD.
- File/directory naming: lowercase ASCII kebab-case, no diacritics (e.g. `racunanje-z-mathematico`); numeric prefixes `NN-` for ordered units.
- Book source format: MyST Markdown. Build tool (jupyter-book vs mystmd): TBD — both configs exist in `ucbenik/`.
- Slides format: the medium follows the material taught — reveal.js for Markdown/HTML, Beamer for LaTeX, the application itself for Excel and Mathematica (which need no deck). The legacy mix is therefore kept, not unified.
- Exercise format: numbered headings `## N. naloga: <naslov>` (legacy ucbenik style).
- Chapter structure: prose first, exercises at the end. An exercise keeps only what the student needs to carry it out; explanation goes into the prose.
- Terminology, command line: a *ukaz* is *ime programa* followed by *argumenti*; an argument starting with `-` is a *možnost*; the `$` is the *pozivnik*. *Argument* is reused for LaTeX and Mathematica (not *parameter*), *pozivnik* replaces the legacy FAQ's *ukazni poziv*. Both per Islovar.
- Spelling: *VSCode* (full name *Visual Studio Code* only at first mention and in the software admonitions).
- Platform baseline: prose states the behaviour of Git Bash on Windows (in the VSCode terminal) as the plain fact; what works elsewhere is an add-on in parentheses naming the system, e.g. `(na macOS \d sicer deluje)`.
- Figures: MyST `:::{figure-md}` directives (legacy ucbenik style); each figure gets its own label, namespaced `slika:<ime>`.
- Line wrapping: TBD — legacy text is loosely wrapped, roughly one sentence per line but not strict.
- Notation and terminology: TBD — reconcile book vs slides terminology per topic during migration.
- Citation style: TBD.

## Workflow

- Work happens on branches; PRs are reviewed by the other author before merging.
- Migration follows `MIGRATION.md`: one coherent unit per PR.
- When a convention is decided, it is recorded in this file in the same PR that
  establishes it (moved from Open questions to Decided below, and/or added to
  Conventions).
- Never commit student data, credentials, or tokens.

## Decided

- 2026-07-15 — License: MIT (adopted from `predavanja`).
- 2026-07-15 — Import: full history via `git subtree` under `imported/`; source repositories stay untouched.
- 2026-07-15 — Target structure is not fixed up front; it emerges through migration PRs (it may or may not split into book vs slides).
- 2026-07-15 — This repository will be **public**. Exams, future-exam ideas, student data, and admin material are never imported or committed here; they live in the private `zbornica` repo.
- 2026-07-15 — `zbornica` stays a separate, private, living staff repo. Only selected content units are imported, via `git filter-repo` path filters (procedure in MIGRATION.md).
- 2026-09-21 — The course redesign is recorded in `COURSE.md`. It is the target that migration serves; where legacy material and the plan disagree, the plan wins.
- 2026-09-21 — Theme of the whole course: semantics versus surface appearance.
- 2026-09-21 — Lecture format: open on a bad practice a student would genuinely reach for, then improve it by explaining how the thing works.
- 2026-09-21 — LLM use runs through the course as a weekly thread (ask, check, state the verdict), not as a separate unit. Lectures 13 and 14 are its payoff.
- 2026-09-21 — Rule to students: they may use language models as they wish. They have no access to them at the exam, because the network is shut down. This withdraws the old rule (`uporaba umetne inteligence ni dovoljena`).
- 2026-09-21 — CSS is dropped as a taught topic. It is mentioned in lecture 4 and adjusted with Copilot in the exercises.
- 2026-09-21 — Lecture count: fourteen planned lectures replace **twelve** old lecture hours (the slides repo keeps one directory, `10-mathematica/`, for three hours). The old first lecture splits in two; the common-LaTeX-mistakes lecture is broken into ten-minute openers. Net growth is +2 hours, and they are lectures 13 and 14.
- 2026-09-21 — Contact hours: one hour of lectures and three hours of tutorials each week. The tutorials carry most of the teaching, so `COURSE.md` covers them too.
- 2026-09-21 — Purpose of the course, unchanged by the redesign and older than it: the skills to survive a mathematics degree, not a list of commands. Its three threads — syntax exists, debugging, find help yourself — are recorded in `COURSE.md`, lifted from `imported/zbornica/vaje/00-izvedba-vaj.md`.
- 2026-09-21 — Cut criterion: teach what a student cannot learn alone; cut what they will look up when they need it. Exam points are **not** the cut criterion — otherwise lectures 13 and 14 would go first.
- 2026-09-21 — The language-model thread is the successor of the existing "find help yourself" thread, not a new element. Its mechanism already exists: bonus points for errors found in the course materials.
- 2026-09-21 — Mathematica keeps its three hours, reorganised as L10 (why do you trust it), L11 (describing a computation, plus rewrite rules), L12 (visualization: plotting and `Manipulate`). Gradient descent moves out, into L13–14.
- 2026-09-21 — Lectures 13 and 14 are two hours of one topic (how language models work, closing on local models), with Mathematica as the instrument.
- 2026-09-21 — The medium of a lecture follows the material it teaches: reveal.js for Markdown and HTML, Beamer for LaTeX and Beamer, the application itself for Excel and Mathematica. The slides are an extra worked example of the topic, so the legacy mix of technologies is kept on purpose. Excel and Mathematica need no decks (MIGRATION.md G1).
- 2026-09-21 — Lecture 7 keeps the norm "few equations on a slide" but drops its old reason (that equations are hard to write in PowerPoint): the reason rests on a tool defect and points away from Beamer, which the exam tests.
- 2026-09-21 — Exam: five tasks, 100 points, 120 minutes, network off, documentation allowed. The 10 points freed by dropping CSS become a new text-file task (encoding + regex) that goes first. Exam files stay in the private `zbornica`.
- 2026-09-21 — `_toc-plan.yml` is superseded by `COURSE.md` and is not implemented; it migrates only as history, or is deleted.
- 2026-09-29 — Chapters follow the standard textbook structure: prose first, exercises at the end. This resolves the structure of a tutorial sheet; `COURSE.md`, *The tutorials*, still lists it as open. Applied chapter by chapter, starting with chapter 1.
- 2026-09-30 — Figure labels are unique and namespaced `slika:<ime>`. The legacy ucbenik reused the single label `markdown-fig` for every figure, which duplicates the target and makes cross-references to figures impossible.
- 2026-09-30 — Calendar 2026/27: fourteen lecture weeks, no gaps, so all fourteen lectures fit. The Christmas and New Year break falls before lectures 13–14. They are not examined, which is accepted. This holds for 2026/27 only; the calendar is checked again every year.
- 2026-09-30 — Lecture 8 (TikZ) is not cut. It becomes lecture 7, on pictures in general: including images, choosing the format, RGB and CMYK, and a TikZ demo. TikZ is shown, not taught, which keeps to the cut criterion.
- 2026-09-30 — Pictures come before presentations: 5 LaTeX intro, 6 Sklicevanje, 7 Pictures, 8 Presentations. Image formats are in the pictures lecture; the presentations lecture teaches only presentations and Beamer.
- 2026-09-30 — Moodle holds the logistics: the rules and the schedule table. This repository holds the course content.
- 2026-09-30 — MIGRATION.md C1 is resolved in the source repo `predavanja`: the intro slides link to Moodle, which states the rule on language models, and the topic list is removed from the slides. Lecture 1 goes through the schedule table on Moodle.
- 2026-09-30 — Lecture 1 is the text editor: about 10 minutes admin, about 5 minutes Word against VS Code, then Markdown (the larger part), an encodings demo, and a 3-minute tour of editing features that the tutorials drill.
- 2026-09-30 — Encodings: a short demo in lecture 1; the lecture does not explain `iconv`. Students practise conversion in an elective homework and choose the tool. Encoding exercises come back in later tutorials and are on the mock exam and the exam.
- 2026-09-30 — Lecture 2 is the file system and the terminal, framed as reading the commands that an agent issues: paths, `ls`, `cd`, `cat`, then `echo`, pipes, `wc`, `grep`, and regexes. Regexes are here because agent commands use them; they are shown in VS Code and in `grep`, not in lecture 1.
- 2026-09-30 — Markdown leaves lecture 3. Git still opens on ad-hoc backups, and it takes over the diff argument (Word is opaque to Git, Markdown is not). The time Markdown frees is kept as slack. Lecture 4 starts directly with HTML.
- 2026-09-30 — Until a slide deck migrates, its canonical version is in the source repo `predavanja`, which is edited again (so far only lecture 1). The imported copy is deleted when the deck migrates. This revises the 2026-07-15 decision that the source repositories stay untouched.
- 2026-10-07 — Diagram sources and their build tools live in the private `zbornica`: the shared tools in `orodja/slike/`, each figure's source in the `vaje/` directory of its chapter; `ucbenik` holds only the built results (`.svg`). The legacy `.ai` sources of `anatomija-znacke` retire when that figure is redone from the template.
- 2026-10-08 — The repositories `prenova` and `predavanja` are merged into `racunalniski-praktikum.github.io`, which is now the only repository for the course content. `predavanja` keeps its history. `prenova` gives only its latest working tree, without its history and without `imported/`: the legacy textbook is already in this repository, the legacy slides are in the history of `predavanja`, and the selected content stays in `zbornica`. This supersedes the 2026-07-15 import decision and the 2026-09-30 decision on where slide decks are canonical.
- 2026-10-08 — `COURSE.md` is split by audience and status: the public part goes to a to-do list for the README in `MIGRATION.md`, the guidance for authors to *Course principles* above, the lecture plans (drafts) to `MIGRATION.md`, and the exam design to the private `zbornica`. Its summary of changes from the previous run and its table of lecture hours are dropped: the entries above record them.
- 2026-10-08 — The slides are published with the textbook, at <https://racunalniski-praktikum.github.io/predavanja/>. The Sphinx extension `ucbenik/extensions/predavanja.py` copies `predavanja/` into the book's HTML output and renders `predavanja/README.md` as its `index.html`, so `jupyter-book build ucbenik` and `ghp-import` publish both.

## Open questions

- Top-level structure: separate book/slides trees, per-topic units holding both, or something else.
- Book build: jupyter-book (`_config.yml` + `_toc.yml`) vs mystmd (`myst.yml`).
- Every year, before the term: does the calendar have fourteen lecture weeks? It does in 2026/27. If not, decide which lecture goes before the term starts: a decision taken under time pressure cuts from the end of the term, which is lectures 13 and 14. Merging lectures 12 and 13 is not available, because 12 is a visualization hour and 13 and 14 are two hours of one topic.
- Topic numbering: unify book chapters (13 + appendices A–H) with the fourteen planned lectures?
- Build artifacts: keep committing compiled slide PDFs, or build them (CI/locally)?
- reveal.js loaded from CDN vs vendored.
- `zbornica/vaje/` contains instructor-facing solutions — confirm they may be public, or drop that unit, **before it migrates**. Its `00-izvedba-vaj.md` is now safe to drop in that sense: its ideas are recorded in *To do: the README* in `MIGRATION.md` and in *Course principles*.
- Cruft in `ucbenik/`: stray extensionless `ucbenik/L-latex` file, `ucbenik/00-razno/` scratch directory — keep, move, or delete.
- `ucbenik/_config.yml` still points to the old repo URL (`katjabercic/racunalniski-praktikum`) — fix when migrating book config.
