# Write a program to manipulate pdf files using pyPDF. Your programs should be able to merge multiple pdf files into a single pdf. You are welcome to add more functionalities
from pypdf import PdfReader, PdfWriter
from os import listdir

writer = PdfWriter()
files = listdir("pdffiles")

for file in files:
  reader = PdfReader(f"pdffiles/{file}")
  for page in reader.pages:
    writer.add_page(page)


with open("merged_pdf_file.pdf", "wb") as file:
  writer.write(file)
  
  



















