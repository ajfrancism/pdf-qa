import fitz  # PyMuPDF

def extract_text_from_pdf(file_path):
    doc = fitz.open(file_path)
    pages = []

    for i, page in enumerate(doc):
        text = page.get_text("text")

        pages.append({
            "page": i + 1,
            "text": text
        })

    return pages