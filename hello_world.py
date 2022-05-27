from flask import Flask

app = Flask(__name__)

@app.route('/')
def message():
    return 'Hello World from Python Flask!'

app.run(host='0.0.0.0', port=8081)
