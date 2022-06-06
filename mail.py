from flask import *
from flask_mail import *
app=Flask(__name__)
mail=Mail(app)
app.config['MAIL_SERVER']= 'smtp.gmail.com'
app.config['MAIL_PORT']='465'
app.config['MAIL_USERNAME']= 'shahnawaz905920@gmail.com'
app.config['MAIL_PASSWORD']= '9133085364S'
app.config['MAIL_USE_TLS']= False
app.config['MAIL_USE_SSL']= True
mail=Mail(app)
@app.route('/')
def index():
    msg=Message('Hello',sender='shahnawaz905920@gmail.com',recipients=['gooty.shahnawaz@gmail.com '] )
    msg.body='hello, this is a demo mail'
    mail.send(msg)
    return 'message sent'
if __name__=='__main__':
    app.run(debug=True)