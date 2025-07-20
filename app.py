from flask import Flask, render_template, request, redirect, url_for, flash
import smtplib
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/send", methods=["POST"])
def send():
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")

    try:
        smtp_server = os.environ.get("MAIL_SERVER")
        smtp_port = int(os.environ.get("MAIL_PORT", 587))
        smtp_user = os.environ.get("MAIL_USERNAME")
        smtp_pass = os.environ.get("MAIL_PASSWORD")
        receiver = os.environ.get("MAIL_RECEIVER")

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_user, smtp_pass)
            subject = f"New Contact Message from {name}"
            body = f"From: {name} <{email}>\n\n{message}"
            msg = f"Subject: {subject}\n\n{body}"
            server.sendmail(smtp_user, receiver, msg)

        flash("Message sent successfully!", "success")
    except Exception as e:
        print(e)
        flash("An error occurred while sending the message.", "danger")

    return redirect(url_for("index"))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
