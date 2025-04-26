from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        # Here you can add logic to save the data or send it somewhere
        return f"<h1>Thank you, {first_name} {last_name}! We've received your subscription using {email}.</h1><br><a href='/'>Back to Home</a>"
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    app.run(host='192.168.1.10', port=5000)

