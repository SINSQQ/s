from flask import Flask, render_template
import os
import ssl
import redis

app = Flask(__name__)
redis_url = os.environ.get("REDIS_URL")
db = redis.from_url(redis_url, ssl_cert_reqs=ssl.CERT_NONE, decode_responses=True)

@app.route("/")
def home():
    # جلب الرسالة من Redis
    message = redis_client.get("log")  # استبدل "key" بالمفتاح الصحيح
    if message is None:
        message = "لا توجد رسالة متاحة"
    else:
        message = message.replace('\n', '\n')  # إضافة أي تنسيقات أو فواصل أسطر كما تحتاج
    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)
