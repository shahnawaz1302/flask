
from flash import *
app=Flask(__name__)
@app.route('/') 
def user():
    return render_template('login.html')
@app.route('/login',methods=['POST','GET'])
def login():
    if request.method=='POST':
        if request.form['username']=='admin':
            return redirect(url_for('sucess'))
        else:
            abort(401)
    return redirect(url_for('user'))
@app.route('/sucess')
def sucess():
    return "Sucessfully logged in "
if __name__=='__main__':
    app.run(debug=True)