import os
from flask import Flask, render_template_string

app = Flask(__name__)

html_page = """
<!DOCTYPE html>
<html lang="ar">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>عرض إحداثيات النقر</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            background-color: #f4f4f4;
            margin: 0;
            padding: 0;
            width: 100vw;
            position: relative;
        }
        #coordinates {
            font-size: 2vw;
            background: white;
            padding: 1.5vw 3vw;
            border-radius: 10px;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
            max-width: 90%;
            word-wrap: break-word;
            position: absolute;
            top: 10px;
            left: 50%;
            transform: translateX(-50%);
        }
        .click-point {
            width: 10px;
            height: 10px;
            background-color: red;
            border-radius: 50%;
            position: absolute;
            transform: translate(-50%, -50%);
            box-shadow: 0px 0px 5px rgba(0, 0, 0, 0.3);
        }
    </style>
</head>
<body>
    <div id="coordinates">انقر في أي مكان لعرض الإحداثيات</div>

    <script>
        document.addEventListener("click", function(event) {
            let x = event.clientX;
            let y = event.clientY;
            document.getElementById("coordinates").innerText = `إحداثيات النقر: X=${x}, Y=${y}`;
            
            // إزالة النقاط السابقة
            document.querySelectorAll('.click-point').forEach(point => point.remove());
            
            // إنشاء نقطة جديدة
            let point = document.createElement("div");
            point.classList.add("click-point");
            point.style.left = `${x}px`;
            point.style.top = `${y}px`;
            document.body.appendChild(point);
        });
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(html_page)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)