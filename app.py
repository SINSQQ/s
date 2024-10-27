from flask import Flask, render_template
import os
import ssl
import redis

app = Flask(__name__)
redis_url = os.environ.get("REDIS_URL")
db = redis.from_url(redis_url, ssl_cert_reqs=ssl.CERT_NONE, decode_responses=True)

@app.route("/")
def home():
    logs = db.lrange("logs", -5, -1)
    if not logs:
        logs = ["لا توجد سجلات متاحة"]
    return render_template("index.html", logs=logs)

@app.route("/add_test_logs")
def add_test_logs():
    test_logs = [
        "- You have a new message ✉️\n\n𖡋 𝐈𝐃 ⌯ s\n𖡋 𝐏𝐡𝐨𝐧𝐞 ⌯ +222\n𖡋 𝐃𝐀𝐓𝐄 ⌯ {date.today()}\n\nssss",
        "رسالة تجريبية 2",
        "رسالة تجريبية 3",
        "رسالة تجريبية 4",
        "رسالة تجريبية 5"
    ]
    for log in test_logs:
        db.rpush("logs", log)  # إضافة كل رسالة إلى نهاية قائمة "logs"
    return "تمت إضافة السجلات التجريبية بنجاح!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
