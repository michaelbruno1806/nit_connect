from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/testimonials')
def testimonials():
    return render_template('testimonials.html')

@app.route('/booking', methods=['POST'])
def booking():
    name = request.form.get('name')
    email = request.form.get('email')
    date = request.form.get('date')
    message = request.form.get('message')
    return f"Thanks {name}, your message has been received!"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
