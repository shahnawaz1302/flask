
from flask import *
from forms import contactForm #we are going to import from form.py file 
app=Flask(__name__)
app.secret_key='secret key'
@app.route('/',methods=['POST','GET'])# intially it will go with grt method
def contactf():
    form=contactForm()
    if request.method=='POST':
        if form.validate() == True:#if any error in froms.name.error occured it will applh the flsk message 
            flash('All fields required')
            return render_template('contactf.html' ,form=form)
        else:
            return render_template('sucessf.html')
    if request.method=='GET':
        return render_template('contactf.html', form=form)  
    
if __name__=='__main__':
    app.run(debug=True)