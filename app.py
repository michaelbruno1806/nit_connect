from flask import Flask, render_template, request, jsonify
from flask_mail import Mail, Message

app = Flask(__name__)

# Email Config
app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=587,
    MAIL_USERNAME='djmichael.bruno33@gmail.com',
    MAIL_PASSWORD='Testing123!',
    MAIL_USE_TLS=True,
    MAIL_USE_SSL=False
)

mail = Mail(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/send", methods=["POST"])
def send():
    name = request.form["name"]
    email = request.form["email"]
    message = request.form["message"]

    msg = Message("Contact - NetConnect Pro", sender=email, recipients=["yourmail@domain.com"])
    msg.body = f"From: {name}\nEmail: {email}\n\n{message}"
    mail.send(msg)
    return jsonify({"success": True})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
