from flask import Flask, render_template, request, redirect, url_for, send_file, jsonify
import os
import zipfile
from PyPDF2 import PdfReader, PdfWriter

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "outputs"
ZIP_FOLDER = "archives"

# Créez les répertoires si nécessaire
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)
os.makedirs(ZIP_FOLDER, exist_ok=True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload_file():
    file = request.files.get("file")
    if not file or file.filename == "":
        return jsonify({"success": False, "error": "Aucun fichier fourni."})

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    # Division du PDF
    try:
        pdf_reader = PdfReader(file_path)
        for page_num, page in enumerate(pdf_reader.pages, start=1):
            writer = PdfWriter()
            writer.add_page(page)
            output_path = os.path.join(OUTPUT_FOLDER, f"page_{page_num}.pdf")
            with open(output_path, "wb") as output_file:
                writer.write(output_file)

        # Création de l'archive ZIP
        zip_path = os.path.join(ZIP_FOLDER, "yourself.zip")
        with zipfile.ZipFile(zip_path, "w") as zipf:
            for file_name in os.listdir(OUTPUT_FOLDER):
                zipf.write(os.path.join(OUTPUT_FOLDER, file_name), arcname=file_name)

        return jsonify({"success": True})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

@app.route("/success")
def success():
    return render_template("success.html")

@app.route("/download/<filename>")
def download_file(filename):
    zip_path = os.path.join(ZIP_FOLDER, filename)
    return send_file(zip_path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
