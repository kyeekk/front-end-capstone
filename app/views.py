"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
""" 
from typing import Tuple, List 
from app.currency_arbitrage_2 import Arbitrage
from math import log
from app import app, db, login_manager
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.security import check_password_hash 
import os 
import datetime
from app import app
from app.forms import Form 
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user, login_required
from app.forms import Login, Register
from app.models import User
from werkzeug.security import check_password_hash
import io
import random
import requests, json
from flask import Response
from matplotlib import pyplot as plt 
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

    
# def RealTimeCurrencyExchangeRate(from_currency,to_currency) : 
  
#     # importing required libraries 
#     # base_url variable store base url  
#     base_url = r"https://www.freeforexapi.com/api/live?"
  
#     # main_url variable store complete url 
#     main_url = base_url + "pairs=" + from_currency+ to_currency  

#     # get method of requests module  
#     # return response object  
#     req_ob = requests.get(main_url) 
  
#     # json method return json format 
#     # data into python dictionary data type. 
      
#     # result contains list of nested dictionaries 
#     result = req_ob.json()
#     value = result ['rates'][from_currency+to_currency]['rate']

#     return(value)

def format_date_joined():
    now = datetime.datetime.now() # today's date
    date_joined = datetime.date(2019, 2, 7) # a specific date
    return "Joined " + date_joined.strftime("%B, %Y")

###
# Routing for your application.
###

@app.route('/')
def home():
   
    return render_template('home.html')
    
    

@app.route('/Convert', methods = ['GET','POST'])
#@login_required
def Convert():
    if request.method == 'GET':
        form = Form()
        rate = 0 
        
        return render_template('Convert.html', form = form, rate = rate)
    form = Form()
    if request.method == 'POST':   
        c1 = form.currencies.data 
       
        test = Arbitrage.run(Arbitrage,c1)   
        
        print(form)  
        print('aaaaaaa')
        print(c1) 
        print('aaaaaaaaaa')
        print(test)
       # print(str(rate)) 
        return render_template('rates.html', c1 = c1, form=form, test=test)   


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="an Arbitrage.")

@app.route('/profile')
def profile():
    datejoined = format_date_joined()
    return render_template('profile.html',date = datejoined) 

@app.route("/rates") 
def rates():  
    return render_template('rates.html', test=test, c1=c1) 

@app.route('/services') 
def services():
    return render_template('services.html') 

@app.route('/contact')
def contact(): 
    return render_template('contact.html') 

@app.route('/pricing')
def pricing(): 
    return render_template('pricing.html')

@app.route('/register', methods=['GET', 'POST'])
def register(): 
    if request.method == 'GET': 
        form = Register()
        return render_template('register.html', form = form)
    # Validate file upload on submit
    form = Register()
    if request.method == 'POST' and form.validate_on_submit():
        # Get file data and save to your uploads folder
        Fname = form.firstname.data
        Lname =  form.lastname.data
        Email = form.email.data
        Password = form.password.data 
        user =User(Fname,Lname,Email,password)
        db.session.add(profile)
        db.session.commit() 
        return redirect(url_for('login'))
    return render_template('register.html', form=form) 

@app.route('/login', methods =['POST','GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('Convert'))
    form = Login()

    if request.method == 'POST' and form.validate_on_submit():

        email = form.email.data
        password = form.password.data
        user = User.query.filter_by(email=email).first()

        if user is not None and check_password_hash(user.password, password):
            remember_me = False

            if 'remember_me' in request.form:
                remember_me = True

            login_user(user, remember=remember_me)

            flash('Logged in successfully.', 'success')

            return redirect(url_for('Convert'))
        else:
            flash('Username or Password is incorrect.', 'danger')

    return render_template('login.html', form=form)



@app.route("/logout")
@login_required
def logout():
    # Logout the user and end the session
    logout_user()
    flash('You have been logged out.', 'danger')
    return redirect(url_for('home'))

@login_manager.user_loader
def load_user(id):
    return UserProfile.query.get(int(id))
###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response




@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
# Python program to get the real-time 
# currency exchange rate 
  
# Function to get real time currency exchange  



if __name__ == '__main__': 
    

    app.run(debug=True, host="0.0.0.0", port="8080")
