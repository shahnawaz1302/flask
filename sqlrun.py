
from os import name
from flask import *
import sqlite3 as sql

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")
@app.route("/enternew")
def enternew():
    return render_template("student.html")
@app.route("/addrec", methods=["POST","GET"])
def addrec():
    msg="msg"
    if request.method=="POST":
        try:
            nm=request.form["nm"] #all keywords in[] should match with student.html name attributes
            addr=request.form["addr"]
            city=request.form["city"]
            pin=request.form["pin"]
            con=sql.connect("demo.db") 
            cur=con.cursor()
            #execute command will help us to write our sql commands
            cur.execute("INSERT INTO demo (nm,addr,city,pin) VALUES (?,?,?,?)",(nm,addr,city,pin))#these values in () will
            #should be desplayed in our sqlite studio where we can see headings on tables
            con.commit()
            con.close() #will close the databasse
            msg="Record sucessfully added"
        except:
            con.rollback()
            msg="error in  insert operation"
        finally:
            con.close()
            return render_template("result.html", msg=msg)
    return 

#the below list method will help us to show our databse in output that is on 5000 port            
@app.route("/list")
def list():
    con=sql.connect("demo.db")
    con.row_factory=sql.Row #will activate the row 
    cur=con.cursor()
    cur.execute("SELECT * FROM demo") #will selectv the values of row
    rows=cur.fetchall()# will fetch the selected values
    con.close()
    return render_template("list.html", rows=rows) 
if __name__=='__main__':
    app.run(debug=True)
