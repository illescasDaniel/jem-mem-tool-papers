# Build the paper: `make figures` (PlantUML -> SVG -> PDF), `make` (PDF), `make clean`.
SRC := $(wildcard figures/src/*.puml)
SVG := $(patsubst figures/src/%.puml,figures/%.svg,$(SRC))
PDF := $(SVG:.svg=.pdf)

all: main.pdf

figures: $(PDF)

figures/%.svg: figures/src/%.puml figures/src/style.iuml
	cd figures/src && plantuml -tsvg -o .. $(notdir $<)

figures/%.pdf: figures/%.svg
	rsvg-convert -f pdf -o $@ $<

main.pdf: main.tex $(wildcard sections/*.tex) references.bib $(PDF)
	latexmk main.tex

clean:
	latexmk -C
