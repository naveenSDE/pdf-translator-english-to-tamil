from fpdf import FPDF
import os

OUTPUT_FOLDER = "outputs"

def create_pdf(text):

    pdf = FPDF()
    pdf.add_page()

    # get correct absolute path to font
    font_path = os.path.join(os.getcwd(), "fonts", "NotoSansTamil-Regular.ttf")

    pdf.add_font("Tamil", "", font_path, uni=True)

    pdf.set_font("Tamil", size=14)

    lines = text.split("\n")

    for line in lines:
        pdf.multi_cell(0, 10, line)

    file_path = os.path.join(OUTPUT_FOLDER, "translated.pdf")

    pdf.output(file_path)

    return file_path