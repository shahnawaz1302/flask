from flask import *
app=Flask(__name__)
app.secret_key='shahnawaz'
@app.route('/')
def index():
    return render_template('light_dark.html')
@app.route('/background/<mode>')
def background(mode):
    session['mode']=mode #we are going to save mode to sesion mode 
    return redirect(url_for('index'))
@app.route('/dropbackground')
def dropbackground():
    session.pop('mode',None) #deleting the mode we selected in cookie
    return redirect(url_for('index'))
if __name__=='__main__':
    app.run(debug=True)