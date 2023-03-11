from flask import Flask

app = Flask(__name__)

@app.route('/ping')

def ping():
    return 'pong'

# for issue presentation
@app.route('/hello/<name>')

def hello(name):
    return 'Hello, ' + 'Tom'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')