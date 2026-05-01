# Use LuaLaTeX by default for fontspec/unicode-math.
$pdflatex = 'lualatex -interaction=nonstopmode -file-line-error %O %S';

# Ensure biblatex + biber runs.
$bibtex = 'biber %O %B';

# Generate a PDF by default.
$pdf_mode = 1;
