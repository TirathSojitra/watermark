import PyPDF2


def add_watermark(input_file, watermark_file):
    watermark_obj = PyPDF2.PdfFileReader(watermark_file)
    watermark_page = watermark_obj.getPage(0)

    input_file = PyPDF2.PdfFileReader(input_file)
    writer = PyPDF2.PdfFileWriter()

    for page in range(input_file.getNumPages()):
        page = input_file.getPage(page)
        page.mergePage(watermark_page)
        writer.addPage(page)

    with open("Watermarked.pdf", "wb") as file:
        writer.write(file)


add_watermark("super.pdf", "wtr.pdf")
