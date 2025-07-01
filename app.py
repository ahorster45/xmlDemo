from flask import Flask, request, render_template, send_from_directory
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['kmlfile']
    if file and file.filename.endswith('.kml'):
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        return render_template('index.html', kml_file=file.filename)
    return 'Invalid file format. Please upload a .kml file.'

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True, port=5050)
