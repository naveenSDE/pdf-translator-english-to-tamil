from flask import Flask, render_template, request
import os

from pdf_reader import extract_text
from translator import translate_text
from pdf_writer import create_pdf
from speaker import speak_text

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "outputs"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)


@app.route("/", methods=["GET", "POST"])
def index():

    translated_text = None
    output_file = None

    if request.method == "POST":

        pdf = request.files["pdf"]

        if pdf:

            pdf_path = os.path.join(UPLOAD_FOLDER, pdf.filename)
            pdf.save(pdf_path)

            # 1 extract text
            text = extract_text(pdf_path)

            # 2 translate
            translated_text = translate_text(text)




            # 4 create translated pdf
            output_file = create_pdf(translated_text)


    return render_template(
        "index.html",
        translated_text=translated_text,
        output_file=output_file
    )


if __name__ == "__main__":
    app.run(debug=True)