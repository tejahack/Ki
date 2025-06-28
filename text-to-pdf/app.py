from flask import Flask, render_template, request, send_file
from fpdf import FPDF
import io
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download-pdf', methods=['POST'])
def download_pdf():
    text = request.form['text']
    
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)

    for line in text.split('\n'):
        pdf.multi_cell(0, 10, line)

    buffer = io.BytesIO()
    pdf.output(buffer)
    buffer.seek(0)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


    return send_file(buffer, as_attachment=True, download_name='output.pdf', mimetype='application/pdf')

if __name__ == '__main__':
    app.run(debug=True)
