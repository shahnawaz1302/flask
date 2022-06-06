from flask import *
app=Flask(__name__)
@app.route('/')
def student():
    return render_template('page4.html')
@app.route('/result', methods=['POST','GET'])
def result():
    if request.method=='POST':
        result=request.form
        return render_template("page4.1.html",result = result)
if __name__=='__main__':
    app.run(debug=True)