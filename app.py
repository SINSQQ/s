from flask import Flask, render_template_string, send_file
import os

app = Flask(__name__)

# قائمة الصور
images = [
    'https://telegra.ph/file/cedd72b1855f33a6f4f02.jpg',
    'https://telegra.ph/file/a6693cefdeda75546151e.jpg',
    'https://telegra.ph/file/c9d3f4e00cfc687494989.jpg',
]

# قائمة الصور المقبولة
accepted_images = []

@app.route('/')
def index():
    return render_template_string("""
        <html>
            <head><title>عرض الصور</title></head>
            <body>
                <h1>اختر صورة</h1>
                {% for image in images %}
                    <div>
                        <h2>صورة {{ loop.index }}</h2>
                        <img src="{{ image }}" width="500px"><br>
                        <a href="/accept/{{ loop.index }}">قبول</a> |
                        <a href="/reject/{{ loop.index }}">رفض</a>
                    </div>
                {% endfor %}
                <h2>الصور المقبولة</h2>
                <ul>
                    {% for image in accepted_images %}
                        <li><img src="{{ image }}" width="100px"></li>
                    {% endfor %}
                </ul>
                <br>
                <a href="/download">تحميل ملف الصور المقبولة</a>
            </body>
        </html>
    """, images=images, accepted_images=accepted_images)

@app.route('/accept/<int:image_index>')
def accept_image(image_index):
    if image_index >= 1 and image_index <= len(images):
        accepted_images.append(images[image_index - 1])
    return index()

@app.route('/reject/<int:image_index>')
def reject_image(image_index):
    return index()

@app.route('/download')
def download_file():
    # قم بإنشاء ملف نصي يحتوي على الصور المقبولة
    file_path = 'accepted_images.txt'
    with open(file_path, 'w') as file:
        for image in accepted_images:
            file.write(image + '\n')

    # تحميل الملف
    return send_file(file_path, as_attachment=True, download_name="accepted_images.txt")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
