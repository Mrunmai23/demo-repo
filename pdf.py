import os
import platform
import subprocess

# Change to the directory where the TeX file is located
tex_file_directory = 'D:/GENEARL/XBEE Confg/demo-repo'
os.chdir(tex_file_directory)

# TeX source filename
tex_filename = 'final.tex'
filename, ext = os.path.splitext(tex_filename)
# the corresponding PDF filename
pdf_filename = filename + '.pdf'

# compile TeX file
try:
    subprocess.run(['pdflatex', '-interaction=nonstopmode', tex_filename])
except FileNotFoundError as e:
    raise RuntimeError('pdflatex command not found. Make sure you have a LaTeX distribution installed.') from e

# check if PDF is successfully generated
if not os.path.exists(pdf_filename):
    raise RuntimeError('PDF output not found')

# open PDF with platform-specific command
if platform.system().lower() == 'darwin':
    subprocess.run(['open', pdf_filename])
elif platform.system().lower() == 'windows':
    subprocess.run(['start', '', pdf_filename], shell=True)  # 'start' command opens PDF in default viewer
elif platform.system().lower() == 'linux':
    subprocess.run(['xdg-open', pdf_filename])
else:
    raise RuntimeError('Unknown operating system "{}"'.format(platform.system()))
