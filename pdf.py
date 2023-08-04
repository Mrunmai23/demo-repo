import os
import platform
import subprocess
import tkinter as tk
from tkinter import filedialog

def compile_and_open_pdf(tex_file_path):
    # Change to the directory where the TeX file is located
    tex_file_directory = r'C:\Users\91935\OneDrive\Desktop\Vinidra new'
    os.chdir(tex_file_directory)

    # TeX source filename
    tex_filename = os.path.basename(tex_file_path)
    filename, ext = os.path.splitext(tex_filename)
    # The corresponding PDF filename
    pdf_filename = filename + '.pdf'

    # Compile TeX file
    try:
        subprocess.run(['pdflatex', '-interaction=nonstopmode', tex_filename])
    except FileNotFoundError as e:
        raise RuntimeError('pdflatex command not found. Make sure you have a LaTeX distribution installed.') from e

    # Check if PDF is successfully generated
    if not os.path.exists(pdf_filename):
        raise RuntimeError('PDF output not found')

    # Open PDF with platform-specific command
    if platform.system().lower() == 'darwin':
        subprocess.run(['open', pdf_filename])
    elif platform.system().lower() == 'windows':
        subprocess.run(['start', pdf_filename], shell=True)  # 'start' command opens PDF in default viewer
    elif platform.system().lower() == 'linux':
        subprocess.run(['xdg-open', pdf_filename])
    else:
        raise RuntimeError('Unknown operating system "{}"'.format(platform.system()))

def select_tex_file():
    tex_file_path = filedialog.askopenfilename(filetypes=[("TeX Files", "*.tex")])
    if tex_file_path:
        compile_and_open_pdf(tex_file_path)

root = tk.Tk()
root.title("Open PDF")
root.geometry("300x100")

select_button = tk.Button(root, text="Export PDF", command=select_tex_file)
select_button.pack()

root.mainloop()
