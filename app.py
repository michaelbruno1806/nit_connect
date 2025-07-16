from flask import Flask, render_template, request, redirect, flash
import smtplib
from email.message import EmailMessage

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

RECIPIENT_EMAIL = 'yourbookingemail@example.com'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/book', methods=['POST'])
def book():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    message = request.form['message']

    try:
        msg = EmailMessage()
        msg['Subject'] = 'New Booking from Nit_Connect Website'
        msg['From'] = email
        msg['To'] = RECIPIENT_EMAIL
        msg.set_content(f"Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}")

        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.starttls()
            smtp.login('yourbookingemail@example.com', 'your_app_password')
            smtp.send_message(msg)

        flash('Booking submitted successfully!', 'success')
    except Exception as e:
        print(e)
        flash('Failed to send booking. Please try again.', 'error')

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
