from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Server run on port 5000!!!'


if __name__ == '__main__':
    app.run(debug=True, port=5000)
