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

# المؤشر الحالي للصورة
current_image_index = 0

@app.route('/')
def index():
    global current_image_index
    if current_image_index >= len(images):
        return render_template_string("""
            <html>
                <head>
                    <title>تم عرض كل الصور</title>
                    <style>
                        body {
                            font-family: Arial, sans-serif;
                            background-color: #f4f4f4;
                            text-align: center;
                            padding: 50px;
                        }
                        h1 {
                            color: #333;
                        }
                    </style>
                </head>
                <body>
                    <h1>تم عرض كل الصور!</h1>
                    <p>لقد قمت بمراجعة كل الصور.</p>
                    <br><br>
                    <a href="/">العودة إلى البداية</a>
                </body>
            </html>
        """)

    return render_template_string("""
        <html>
            <head>
                <title>عرض الصورة</title>
                <style>
                    body {
                        font-family: 'Arial', sans-serif;
                        margin: 0;
                        padding: 0;
                        background-color: #282c34;
                        color: white;
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        height: 100vh;
                        overflow: hidden;
                    }
                    img {
                        max-width: 90%;
                        max-height: 90%;
                        object-fit: contain;
                        border-radius: 10px;
                        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.5);
                    }
                    .controls {
                        position: absolute;
                        bottom: 50px;
                        width: 100%;
                        display: flex;
                        justify-content: center;
                    }
                    .btn {
                        background-color: #4CAF50;
                        color: white;
                        font-size: 18px;
                        padding: 15px 32px;
                        margin: 0 10px;
                        cursor: pointer;
                        border: none;
                        border-radius: 5px;
                        transition: background-color 0.3s;
                    }
                    .btn:hover {
                        background-color: #45a049;
                    }
                </style>
            </head>
            <body>
                <div>
                    <h2>صورة {{ current_image_index + 1 }}</h2>
                    <img src="{{ images[current_image_index] }}" alt="صورة">
                </div>
                <div class="controls">
                    <a href="/accept/{{ current_image_index }}" class="btn">قبول</a>
                    <a href="/reject/{{ current_image_index }}" class="btn">رفض</a>
                </div>
            </body>
        </html>
    """, images=images, current_image_index=current_image_index)

@app.route('/accept/<int:image_index>')
def accept_image(image_index):
    global current_image_index
    if image_index >= 0 and image_index < len(images):
        accepted_images.append(images[image_index])
    current_image_index += 1  # الانتقال للصورة التالية
    return index()

@app.route('/reject/<int:image_index>')
def reject_image(image_index):
    global current_image_index
    current_image_index += 1  # الانتقال للصورة التالية
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
