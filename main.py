from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/greet', methods=['POST'])
def greet():
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    group = request.form.get('group')
    greeting = f"Привет, {first_name} {last_name} из {group}!"
    return render_template('greetings.html', greeting=greeting)

if __name__ == "__main__":
    app.run(debug=True)