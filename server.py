from flask import Flask, request
import psycopg2
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


# before you access this path
# please read docs/deploy_db/README.md for deploy db firstly
@app.route('/is_admin', methods=['GET'])
def is_admin():
    # connect to db
    connection = psycopg2.connect(
        host = "localhost",
        database = "postgres",
        user = "postgres",
        password = "ntcuser2222",
    )
    connection.set_session(autocommit = True)

    # Test: 觀察 user table 內的資料筆數
    # with connection.cursor() as cursor:
    #    cursor.execute('SELECT COUNT(*) FROM users')
    #    result = cursor.fetchone()
    #    print(result)

    username = request.values["username"]
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT
                admin
            FROM
                users
            WHERE
                username = '%s'
        """ % username)
        result = cursor.fetchone()

    if result is None:
        # User does not exist
        return "False"

    admin, = result
    
    return str(admin)

if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=5566)
