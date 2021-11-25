import PyPDF2
from sys import argv

inputs = argv[1:]


def pdfmerger(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        merger.append(pdf)

    return merger.write(r'merged.pdf')


pdfmerger(inputs)
