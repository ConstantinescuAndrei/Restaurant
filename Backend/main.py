from flask import Flask, request
import pyodbc

conn = pyodbc.connect('DRIVER={FreeTDS};SERVER=localhost;PORT=1433;UID=sa;PWD=Virtual1234;DATABASE'
                      '=Restaurant;UseNTLMv2=yes;TDS_Version=8.0;Trusted_Domain=domain.local;')

app = Flask(__name__)


@app.route('/')
def home():
    cursor = conn.cursor()
    cursor.execute("select * from dbo.Users")

    res = cursor.fetchone()
    print(res)
    return res[1]


@app.route('/register', methods=['POST'])
def register():
    cursor = conn.cursor()
    username = request.form['Username']
    cursor.execute("select dbo.CheckUsernameExists(?)", username)
    res = cursor.fetchone()
    if res[0]:
        return "Username already exists"
    email = request.form['Email']
    cursor.execute("select dbo.CheckEmailExists(?)", email)
    res = cursor.fetchone()
    if res[0]:
        return "Email already exists"
    cursor.execute("exec dbo.Register ?, ?, ?, ?", (username, email, request.form['Password'], request.form['Address']))
    res = cursor.fetchone()
    if res[1] == username:
        return "OK"
    else:
        return "Registration failed"


@app.route('/login', methods=['POST'])
def login():
    cursor = conn.cursor()
    cursor.execute("select dbo.Login(?, ?)", (request.form['Username'], request.form['Password']))
    res = cursor.fetchone()
    if res[0]:
        return "OK"
    else:
        return "Wrong credentials"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')