from flask import Flask,flash,redirect,render_template,request
from flask_mysqldb import MySQL
app =Flask(__name__)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='sharu1310'
app.config['MYSQL_DB']='libdb'
mysql=MySQL(app)

@app.route('/',methods=['POST','GET'])
def main():
    if request.method == 'POST':
        value = request.form
        if "login" in value:
            return redirect('/login')
        elif "signup" in value:
            return redirect('/signup')
    return render_template('users.html')


@app.route('/signup',methods=['POST','GET'])
def signup():
    cur = mysql.connection.cursor()
    if request.method=='POST':
        datau=request.form['username']
        datap=request.form['password']
        cur.execute("INSERT INTO users VALUES(%s,%s)",(datau,datap))
        mysql.connection.commit()
        cur.close()
        return redirect('/login')
    return render_template('signup.html')

@app.route('/login',methods=['POST','GET'])
def login():
    cur = mysql.connection.cursor()
    if request.method=='POST':
        datau=request.form['username']
        datap=request.form['password']
        cur.execute("SELECT * FROM users WHERE username=%s AND password=%s",(datau,datap))
        mysql.connection.commit()
        s=cur.fetchall()
        cur.close()
        if len(s)==0:
            return redirect('/login')
        '''else:
            return redirect('/menu')'''
    return render_template('login.html')



if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.run(debug=True)

