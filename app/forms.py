from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import TextAreaField, TextField, SelectField,PasswordField, SubmitField, StringField, Form, IntegerField
from wtforms.validators import DataRequired, Email, Length, InputRequired


class Form(FlaskForm):
    currencies = SelectField("From:", choices = [('JMD', 'Jamaican Dollar'),('USD', 'United States Dollar'),('CAD', 'Canadian Dollar'),('GBP', 'British Pound'),('EUR', 'Euro'),('TTD', 'Trinidadian Dollar'),('KYD', 'Cayman Island Dollar'),('CHF', 'Swiss Franc')]) 
    amount = IntegerField("Enter amount to convert:")



class Contact(FlaskForm): 
    firstname = StringField('First Name', validators=[DataRequired()])
    lastname = StringField('Last Name', validators=[DataRequired()])  
    email = StringField('E-mail', validators= [Email(), DataRequired()])  
    message = TextAreaField('Message', validators=[InputRequired(), 
      Length(min=15, max=200, message="Can enter from 15 to 200 characters.")
    ])  
    submit = SubmitField("Submit") 

class Register(FlaskForm):
    firstname = StringField('First Name', validators=[DataRequired()])
    lastname = StringField('Last Name', validators=[DataRequired()])  
    email = StringField('E-mail', validators= [Email(), DataRequired()])
    password = PasswordField('Password', validators=[InputRequired()]) 
    
    

class Login(FlaskForm):
    email = StringField('E-mail', validators= [Email(), DataRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    
    
