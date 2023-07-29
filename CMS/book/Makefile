all: book.pdf

%.pdf: %.tex
	pdflatex $<
	pdflatex $<

clean:
	rm -f *.aux *.log *.nav *.out *.pyg *.snm *.vrb *.toc *~

