
# KML File Uploader & Viewer – Recap

## ✅ Project Summary

A Flask web application to upload and render `.kml` files on a Leaflet-based map centered on Houston, TX. It includes a static overlay image (`HoustonMap.png`) and renders shapes like a 20 NM yellow circle centered on the Sam Houston National Forest.

---

## 📁 Directory Structure

```
xmlDemo/
│
├── app.py
├── uploads/                  # Stores uploaded .kml files
│   └── test_circle.kml
├── static/                   # Static assets (JS, CSS, images)
│   ├── leaflet.css
│   ├── leaflet.js
│   ├── leaflet.kml.js
│   └── HoustonMap.png
└── templates/
    └── index.html            # Main HTML page
```

---

## 🚀 Key Components

### `app.py`
```python
from flask import Flask, request, render_template, send_from_directory
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
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
```

---

## 🧠 Issues + Fixes

### ❌ 1. KML not rendering
- **Cause:** KML fetch resulted in `object%20XMLDocument` instead of a proper filename.
- **Fix:** Use `{{ url_for('uploaded_file', filename=kml_file) }}` in the fetch call.

### ❌ 2. Map zoomed in too far
- **Fix:** Used `fitBounds()` with padding and `panTo()`:
```js
track.on("loaded", function(e) {
    const bounds = e.target.getBounds();
    map.fitBounds(bounds, { padding: [185, 186], maxZoom: 10 });
    map.panTo(bounds.getCenter());
});
```

### ❌ 3. Static image not displaying
- **Fix:** Confirmed correct URL and bounding box for `HoustonMap.png` overlay.

### ✅ 4. Custom KML Circle for Sam Houston National Forest
- Center: `30.6, -95.4`
- Radius: `20 NM ≈ 37 km`
- KML `Polygon` with 36 points created and rendered successfully.

---

## 🛠️ Next Steps

- Refactor `index.html` to handle reload errors.
- Add user feedback after file upload.
- Optional: Let users draw or adjust overlays.

---
