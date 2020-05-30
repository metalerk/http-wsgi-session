from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST', 'PUT'])
def hello():
    return '<h1>hello world!</h1>'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)