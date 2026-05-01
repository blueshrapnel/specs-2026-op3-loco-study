LATEXMK ?= latexmk

PDFLATEX_FLAGS := -pdf -interaction=nonstopmode -file-line-error
LUALATEX_FLAGS := -lualatex -interaction=nonstopmode -file-line-error

PDFS := main.pdf main-extended.pdf main-production.pdf

.PHONY: all full extended production fast clean clobber

all: $(PDFS)

fast: main.pdf main-extended.pdf

full: main.pdf

extended: main-extended.pdf

production: main-production.pdf

main.pdf: main.tex paper-content.tex paper-metadata.tex refs.bib arxiv.sty latexmkrc
	$(LATEXMK) $(PDFLATEX_FLAGS) main.tex

main-extended.pdf: main-extended.tex extended-abstract-content.tex paper-metadata.tex refs.bib arxiv.sty latexmkrc
	$(LATEXMK) $(PDFLATEX_FLAGS) main-extended.tex

main-production.pdf: main-production.tex paper-content.tex paper-metadata.tex refs.bib
	$(LATEXMK) $(LUALATEX_FLAGS) main-production.tex

clean:
	$(LATEXMK) -c main.tex
	$(LATEXMK) -c main-extended.tex
	$(LATEXMK) -c main-production.tex

clobber:
	$(LATEXMK) -C main.tex
	$(LATEXMK) -C main-extended.tex
	$(LATEXMK) -C main-production.tex
