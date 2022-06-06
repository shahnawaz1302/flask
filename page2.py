from flask import *
app=Flask(__name__)
@app.route('/')
def hello():
    return render_template('page2.html')


if __name__=='__main__':
    app.run(debug=True)