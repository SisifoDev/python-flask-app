from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    # return '<h1>Server running in port 5000!!!</h1>'
    data = {
        'titulo': 'Index',
        'bienvenida': '¡Saludos desde Flask!'
    }
    return render_template('index.html', data=data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
