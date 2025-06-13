from flask import Flask, request
import requests

# ✅ استبدل name بـ name
app = Flask(__name__)

# إعدادات البوت
BOT_TOKEN = "7698107127:AAG5qvvWG8BMOJHBmXDOlf3Dd6FPk7f_WC0"
CHAT_ID = "1833632637"  # تأكد أنه ID تاعك الشخصي

@app.route('/', methods=['POST'])
def webhook():
    data = request.json
    if not data:
        return 'No data', 400

    # 🔍 تحسين عرض البيانات داخل الرسالة
    message = "📦 حدث جديد:\n\n"
    for key, value in data.items():
        message += f"🔸 {key}: {value}\n"

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {'chat_id': CHAT_ID, 'text': message}
    requests.post(url, data=payload)

    return 'OK', 200