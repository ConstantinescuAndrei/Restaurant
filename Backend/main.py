from flask import Flask, request, render_template
import pyodbc

conn = pyodbc.connect('DRIVER={FreeTDS};SERVER=localhost;PORT=1433;UID=sa;PWD=Virtual1234;DATABASE'
                      '=Restaurant;UseNTLMv2=yes;TDS_Version=8.0;Trusted_Domain=domain.local;')

app = Flask(__name__)

user_data = {
    'Name': ''
}


@app.route('/')
def home():
    return render_template('index.html', user_data=user_data)


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
        global user_data
        user_data['Name'] = res[1]
        return "OK"
    else:
        return "Registration failed"


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        cursor = conn.cursor()
        cursor.execute("select dbo.Login(?, ?)", (username, request.form['password']))
        res = cursor.fetchone()
        if res[0]:
            global user_data
            user_data['Name'] = username
            return render_template('login.html', user_data=user_data)
        else:
            return "Wrong credentials"
    else:
        return render_template('login.html',  user_data=user_data)


@app.route('/items', methods=['GET'])
def items():
    cursor = conn.cursor()
    cursor.execute("select * from dbo.Items")
    return render_template('items.html', data=cursor, user_data=user_data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')