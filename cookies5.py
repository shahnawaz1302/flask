#creating a login page with the help of setcookies html page
#and we call a function of readcookies html page with the help of post method
#later make respose will return the response and in userID we are going to save user name which he  has given in box
#later we are going to fetch user entered value in name value and that is added to welcome
from flask import *
app=Flask(__name__)
@app.route('/')
def cookies():
    return render_template('setcookies.html')
@app.route('/setcookies',methods=['POST','GET'])
def setcookies():
    if request.method=='POST':
        user=request.form['nm']
        resp=make_response(render_template('readcookies.html')) #link for getcookies is placed
        resp.set_cookie('userID',user)
        return resp
@app.route('/getcookies')
def getcookies():
    name=request.cookies.get('userID')  #user value which is saved in userID is fetching
    return  'welcome' + 'name'
if __name__=='__main__':
    app.run(debug=True)
