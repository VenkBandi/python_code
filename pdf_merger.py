import fitz  # PyMuPDF

pdfs = ['publication_i.pdf', 'publication_ii.pdf', 'publication_iii.pdf', 'publication_iv.pdf']

merger = fitz.open()

for pdf in pdfs:
    merger.insert_pdf(fitz.open(pdf))

merger.save("publication.pdf")
merger.close()
