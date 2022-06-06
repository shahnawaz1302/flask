
from email import message
from flask import *
from flask import flash
app=Flask(__name__)
app.secret_key='secret'
@app.route('/')
def index():
    return render_template('indexf.html') # in indexf.html we are activating message and redirectng to login method

@app.route('/login', methods=['POST','GET'])
def login():
    error=None
    if request.method=='POST':

        if request.form['username']!='admin' or request.form['password']!='admin':
            error='Invalid username or password. please login again!!!'
        else:
            flash('You are sucessfully loged in')
            flash('logout before you login in again')
            return redirect(url_for('index'))
    return render_template('loginf.html',error=error)   
if __name__=='__main__':
    app.run(debug=True)



