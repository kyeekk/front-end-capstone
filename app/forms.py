from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import TextAreaField, TextField, SelectField,PasswordField, SubmitField, StringField, Form
from wtforms.validators import DataRequired, Email, Length, InputRequired


class Form(FlaskForm):
    currencies = SelectField("From:", choices = [('USD', 'USD'),('EUR', 'EUR'),('GBP', 'GBP'),('AUD', 'AUD'),('NZD', 'NZD'),('JMD', 'JMD'),('ZAR', 'ZAR'),('CAD', 'CAD'),('CHF', 'CHF'),('JPY', 'JPY')])
    currencies1 = SelectField("To:",  choices = [('USD', 'USD'),('EUR', 'EUR'),('GBP', 'GBP'),('AUD', 'AUD'),('NZD', 'NZD'),('JMD', 'JMD'),('ZAR', 'ZAR'),('CAD', 'CAD'),('CHF', 'CHF'),('JPY', 'JPY')]) 

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
    
    