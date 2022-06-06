
from flask import *
from flask_wtf import *
from wtforms import *
class contactForm(Form):
    #all form credentials with the required inputs and validations are defined
    name=StringField('Name of the student',[validators.DataRequired('please enter your name')])
    Email=EmailField('Enter your mail',[validators.DataRequired('please enter your mail'),validators.Email('Please enter corret format of email')])
    Gender= RadioField('Gender',choices=[('M','Male'),('F','Female')])
    address=TextAreaField('Address')
    age=IntegerField('age')
    language=SelectField('Language',choices=[('cpp','c++'),('py','python')])
    submit=SubmitField('send')