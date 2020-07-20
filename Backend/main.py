from flask import Flask, request
import mysql.connector

conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Virtual1234",
  port="4000"
)

app = Flask(__name__)


@app.route('/')
def home():
    cursor = conn.cursor()
    cursor.execute("call Restaurant.Register('test', 'test', 'test', 'test');")

    res = cursor.fetchone()
    print(res)
    return res[0]


@app.route('/register', methods=['POST'])
def register():
    cursor = conn.cursor()
    cursor.execute(request.form['UserName'], request.form['Email'], request.form['Password'], request.form['Address'])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')