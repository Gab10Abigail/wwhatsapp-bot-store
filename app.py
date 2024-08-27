from flask import Flask, request
from twilio.rest import Client

app = Flask(__name__)

# Konfigurasi Twilio
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'
client = Client(account_sid, auth_token)

# Nomor telepon
owner_number = '085792367495'
bot_number = '088975475403'

# Status bot
bot_status = 'open'

@app.route('/incoming', methods=['POST'])
def incoming_msg():
    from_number = request.form['From']
    body = request.form['Body']
    media_url = request.form.get('MediaUrl0')
    
    if media_url:
        # Kirim pesan otomatis saat menerima foto
        send_message(from_number, "Baik Akan Kami Proses ditunggu ya...")
    
    if body.startswith('.done'):
        recipient = body.split('<')[1].split('>')[0]
        message = "Oke proses berhasil ya kak✅ Terimakasi telah order disini ya.."
        send_message(recipient, message)
    
    elif body.startswith('.ndone'):
        recipient = body.split('<')[1].split('>')[0]
        message = "Maaf Seperti nya proses gagal ❎ Mohon lakukan ulang atau Chat owner +6285792367495, terimakasih.."
        send_message(recipient, message)
    
    elif body == '.close':
        global bot_status
        bot_status = 'closed'
        send_message(from_number, "Maaf Sistem Lagi sibuk kembali Lagi nanti terimakasih 😊")
    
    elif body == '.open':
        bot_status = 'open'
        send_message(from_number, "Sistem kembali lagi seperti semula")
    
    return "OK", 200

def send_message(to, message):
    client.messages.create(
        body=message,
        from_=bot_number,
        to=to
    )

if __name__ == '__main__':
    app.run(debug=True)
