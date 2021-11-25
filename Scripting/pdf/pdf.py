import PyPDF2

with open(r"Scripting\pdf\dummy.pdf", mode='rb') as file:
    # we are required to read binaries
    reader = PyPDF2.PdfFileReader(file)
    print(reader.numPages)
    page = reader.getPage(0)
    page.rotateClockwise(90)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open(r'Scripting\pdf\tilt.pdf', mode='wb') as new_file:
        writer.write(new_file)
