from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/xss-attack-1', methods=['GET'])
def XSS_attack():
    return f'Hello {request.values["code"]}'

if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=5566)
