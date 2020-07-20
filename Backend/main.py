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
    cursor.execute(request.form['UserName'], request.form['Email'], request.form['Password'], request.form['Address'])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')