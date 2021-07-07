import os

os.system("rm lookbookpy.tex")
os.system("rm lookbookpy.pdf")

fileList = os.listdir("images")

f = open("lookbookpy.tex", "w")

f.write("\\documentclass{article} %Set document class\n\n")
f.write("\\usepackage{graphicx}\n")
f.write("\\usepackage[a4paper, total={8in, 10in}]{geometry}\n")

f.write("\\graphicspath{ {./images/} }\n\n")
f.write("\\begin{document}\n\n")

f.write("\\begin{center}\n")

for fileName in fileList:
    f.write(f"\\includegraphics[width=4in]{{ {fileName} }}\n")
    f.write(f"\\\\\n")

f.write("\\end{center}\n\n")
f.write("\\end{document}\n")
f.close()

os.system("pdflatex lookbookpy.tex")
