from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/xss-attack-1', methods=['GET'])
def XSS_attack():
    return f'Hello {request.values["code"]}'

@app.route('/inject', methods=['GET'])
def Inject():
    path = request.values["path"]
    file_input = open("data/" + path + ".json", "r")
    output = json.loads(file_input.read())
    file_input.close()

    return json.dumps(output)

if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=5566)
