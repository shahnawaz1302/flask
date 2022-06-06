

from flask import *
from flask_sqlalchemy import *
# intially i fetched all attributes og database into students which is in line 27 but i got error due to i did't created any datbase so 
# i created a datbase in line 53
app=Flask(__name__)
#activating our sqlalchemy database
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///students.sqlite3' 
#activating our editing concept in database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.secret_key='SECRET'
db= SQLAlchemy (app) #now configuaring our app into db
class students(db.Model): #creating a model
    id=db.Column('student_id',db.Integer, primary_key=True) #define the attributes which would be included in our app
    name=db.Column(db.String(50))
    email=db.Column(db.String(50))
    address=db.Column(db.String(100))
    pincode=db.Column(db.String(10))
    def __init__(self,name,email,address,pincode): # now calling the attributes through self
        self.name=name
        self.email=email
        self.address=address
        self.pincode=pincode
        
@app.route('/')
def show_all():
    return render_template('show_all.html',students=students.query.all() ) #now fetch the values of database into database of students 
@app.route('/new', methods=['POST','GET'])
def new():
    if request.method=='POST':
        # chech whether all fields are filled or not
        if not request.form['name'] or not request.form['email'] or not request.form['address'] or not request.form['pincode']:
            #any fiels nor filled displauy the flash message
            flash('Required all credentials','error') 
        
        else:
            #now deploying all values entred into a user
            user=students( request.form['name'],
                              request.form['email'],
                              request.form['address'],
                              request.form['pincode']
                            )
            #now adding the values of user into database
            db.session.add(user)
            db.session.commit()
            
            flash('Sucessfully submitted')
            return redirect(url_for('show_all'))    
    return render_template("new.html") #first this will exexute because it is get method

if __name__=='__main__':
    db.create_all()
    
    app.run(debug=True)
    
    