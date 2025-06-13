from flask import Flask, request
import requests

app = Flask(__name__)

# إعدادات البوت
BOT_TOKEN = "7698107127:AAG5qvvWG8BMOJHBmXDOlf3Dd6FPk7f_WC0"
CHAT_ID = "1833623637"  # هذا هو Chat ID الخاص بك

@app.route('/', methods=['POST'])
def webhook():
    data = request.json
    if not data:
        return 'No data', 400

    message = "📦 حدث جديد:\n\n" + str(data)

    url = f"https://api.telegram.org/bot{7698107127:AAG5qvvWG8BMOJHBmXDOlf3Dd6FPk7f_WC0}/sendMessage"
    payload = {'chat_id': CHAT_ID, 'text': message}
    requests.post(url, data=payload)

    return 'OK', 200