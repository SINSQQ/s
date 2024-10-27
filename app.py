from flask import Flask, render_template
import os
import ssl
import redis

app = Flask(__name__)

# إعداد Redis URL وتوصيل Redis
redis_url = os.environ.get("REDIS_URL")
db = redis.from_url(redis_url, ssl_cert_reqs=ssl.CERT_NONE, decode_responses=True)

@app.route("/")
def home():
    # جلب الرسالة من Redis باستخدام db
    message = db.get("log")  # استبدل "log" بالمفتاح الصحيح في Redis
    if message is None:
        message = "لا توجد رسالة متاحة"
    else:
        message = message.replace('\n', '<br>')  # لتحويل فواصل الأسطر إلى HTML

    return render_template("index.html", message=message)

if __name__ == "__main__":
    # تشغيل التطبيق على المنفذ المحدد في Heroku
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
