from types import EllipsisType
from pypdf import PdfWriter
import os

merger = PdfWriter()
files = [file for file in os.listdir() if file.endswith(".pdf")]

for pdf in files:
  merger.append(pdf)
PdfName = input(f"Enter the name of the pdf file: ")
if PdfName.endswith(".pdf"):
  merger.write(PdfName)
  merger.close()
  print(f"all pdf files are merged and saved in new file named {PdfName}")
else:
  merger.write(f"{PdfName}.pdf")
  merger.close()
  print(f"all pdf files are merged and saved in new file named {PdfName}.pdf")
