from pypdf import PdfReader
from pypdf.errors import  PdfStreamError


def extract_text(pdf_path):
    try:
        reader = PdfReader(pdf_path)
        text = ""
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text
        return text

    except PdfStreamError:
        print("Error extracting text from PDF")
        return None

