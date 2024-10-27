from flask import Flask, render_template
import os
import ssl
import redis

app = Flask(__name__)
redis_url = os.environ.get("REDIS_URL")
db = redis.from_url(redis_url, ssl_cert_reqs=ssl.CERT_NONE, decode_responses=True)

@app.route("/")
def home():
    message = db.get("log")
    if message is None:
        message = "لا توجد رسالة متاحة"
    else:
        message = message.replace('\n', '<br>')
    return render_template("index.html", message=message)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
