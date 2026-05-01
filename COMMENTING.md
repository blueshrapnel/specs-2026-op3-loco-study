# Draft Comment Boxes

The paper template defines a lightweight comment box that can be used while drafting.
The same commands work from both `main.tex` and `main-production.tex`.

## Simple Comment

Use `\draftcomment{...}` for a quick unnamed note:

```tex
\draftcomment{This is a note for later.}
```

## Named Comment

Use the optional label when you want to identify the author or topic:

```tex
\draftcomment[Karen]{Check whether this should be framed as deployment or sim fidelity.}
```

The default label is `Comment`.

## Longer Comment

Use the `commentbox` environment for longer notes, lists, or rough text:

```tex
\begin{commentbox}
Longer notes can go here, including lists, equations, or draft wording.
\end{commentbox}
```

Before submission, search for `\draftcomment` and `commentbox` to remove drafting notes from the final PDF.
