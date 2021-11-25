import PyPDF2
from sys import argv

watermark_pdf = argv[1]
inputs = argv[2:]


def add_watermark(watermark_pdf, pdf_list):
    watermark = PyPDF2.PdfFileReader(watermark_pdf).getPage(0)
    for pdf in pdf_list:
        n = 1
        template = PyPDF2.PdfFileReader(pdf)
        output_pdf = PyPDF2.PdfFileWriter()
        for i in range(template.getNumPages()):
            page = template.getPage(i)
            page.mergePage(watermark)
            output_pdf.addPage(page)

        with open(fr'watermarked{n}.pdf', mode='wb') as file:
            output_pdf.write(file)
        n += 1


if __name__ == '__main__':
    add_watermark(watermark_pdf, inputs)
