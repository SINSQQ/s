from flask import Flask, render_template
import os
import ssl
import redis

app = Flask(__name__)
redis_url = os.environ.get("REDIS_URL")
db = redis.from_url(redis_url, ssl_cert_reqs=ssl.CERT_NONE, decode_responses=True)

@app.route("/")
def home():
    logs = db.lrange("logs", -5, -1)  # استرجاع آخر 5 سجلات
    logs.reverse()  # عكس الترتيب لعرض الأحدث في الأعلى
    if not logs:
        logs = ["لا توجد سجلات متاحة"]
    return render_template("index.html", logs=logs)

@app.route("/add_test_logs")
def add_test_logs():
    log = '12'
    db.rpush("logs", log)  # إضافة كل رسالة إلى نهاية قائمة "logs"
    return "تمت إضافة السجلات التجريبية بنجاح!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
