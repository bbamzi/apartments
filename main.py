import datetime
import random
import os
from flask import Flask, render_template, Response, request, redirect, url_for, session, flash, current_app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from files import states


app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:icui4cu4u@localhost/apartment'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://yffdsjymgwylwr:6b7da8c16f69287f4c898945cd49fcef7c15b08939f6e6aa54978e2c92bc9f36@ec2-54-211-255-161.compute-1.amazonaws.com:5432/d45ih59daa2hc1'


app.config['SECRET KEY'] = os.environ.get('SECRET_KEY')
app.secret_key = os.environ.get('APP_SECRET_KEY')
app.config['SESSION_TYPE'] = 'filesystem'
db = SQLAlchemy(app)

migrate = Migrate(app,db)




class Applicants(db.Model):
    __tablename__ = 'apartments'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    date_of_birth = db.Column(db.Date)
    gender = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone_number = db.Column(db.String(100))
    ssn= db.Column(db.String(100))
    driver_license = db.Column(db.String(100))
    residential_address = db.Column(db.String(100))
    state = db.Column(db.String(100))
    city = db.Column(db.String(100))
    zip_code = db.Column(db.String(100))
    application_type = db.Column(db.String(100))




@app.route('/', methods = ['GET', 'POST'])
def new_member():
    state = states.keys()
    if request.method == 'POST':
        new_applicant = Applicants(
            first_name=request.form['first_name'],
            last_name=request.form['last_name'],
            date_of_birth=request.form['birthday'],
            gender = request.form.get('gender'),
            email = request.form['email'],
            phone_number = request.form['phone'],
            ssn =request.form['ssn'],
            driver_license = request.form['drivers_license'],
            residential_address = request.form['address'],
            state = request.form['application_state'],
            city =  request.form['city'],
            zip_code = request.form['zip_code'],
            application_type = request.form['application_type'],
        )
        print(request.form['city'])
        print(request.form['application_state'])
        print(request.form['application_type'])



        db.session.add(new_applicant)
        db.session.commit()
        return redirect(url_for('thank_u'))

    return render_template('index.html', states = state)
@app.route('/Success')
def thank_u():
    return render_template('thanku.html')


#


if __name__=='__main__':
    app.run(debug=True)