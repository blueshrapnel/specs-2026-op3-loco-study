# Use pdfLaTeX by default for fast Overleaf free-tier compilation.
$pdflatex = 'pdflatex -interaction=nonstopmode -file-line-error %O %S';

# Use BibTeX rather than biber for speed.
$bibtex = 'bibtex %O %B';

# Generate a PDF by default.
$pdf_mode = 1;
