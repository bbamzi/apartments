import datetime
import random
import os
from flask import Flask, render_template, Response, request, redirect, url_for, session, flash, current_app
from flask_sqlalchemy import SQLAlchemy

# from flask_migrate import Migrate
# from sms.number_filter import NumberGenerate
# from sms.familes import Families
# from sms.birthday import Birthday
import re
# sms = Sms()
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:icui4cu4u@localhost/apartment'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://dyfeozsmihybfu:4d701100fe07e67a2f71e3b3d6bbc3af5793e874cdda613f583c4736fdbb005e@ec2-54-163-158-194.compute-1.amazonaws.com:5432/d1gjlnpa8bvalr'

#
# run = 'test'
# debug = ''

# if run == 'test':
#     app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
#     debug = True
# elif run == 'deploy':
#     app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://dyfeozsmihybfu:4d701100fe07e67a2f71e3b3d6bbc3af5793e874cdda613f583c4736fdbb005e@ec2-54-163-158-194.compute-1.amazonaws.com:5432/d1gjlnpa8bvalr'
#     debug = False

app.config['SECRET KEY'] = os.environ.get('SECRET_KEY')
app.secret_key = os.environ.get('APP_SECRET_KEY')
app.config['ALLOWED_IMAGE_EXTENSIONS'] = ['PNG','JPG','JPEG','jpeg','png','jpg']
app.config['MAX_CONTENT_LENGTH'] = 1 * 1024 * 1024
# app.config = ['IMAGE_UPLOADS'] = 'static/uploads'
app.config['SESSION_TYPE'] = 'filesystem'
db = SQLAlchemy(app)
# migrate = Migrate(app,db)
# login_manager = LoginManager()
# login_manager.init_app(app)
# login_manager.login_view = 'login'
# scheduler = APScheduler()


# @login_manager.user_loader
# def load_user(member_id):
#     return Members.query.get(int(member_id))


class Members(db.Model):
    __tablename__ = 'members'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(100))
    middle_name = db.Column(db.String(100))
    surname = db.Column(db.String(100))
    maiden_name = db.Column(db.String(100))
    gender = db.Column(db.String(100))
    phone_number = db.Column(db.String(100))
    second_phone_number = db.Column(db.String(100))
    email = db.Column(db.String(100))
    residential_address = db.Column(db.String(100))
    state_of_origin = db.Column(db.String(100))
    state_lga = db.Column(db.String(100))
    date_of_birth = db.Column(db.Date)
    permanent_address = db.Column(db.String(100))
    occupation = db.Column(db.String(100))
    marital_status = db.Column(db.String(100))
    wedding_date = db.Column(db.String(100))
    baptism = db.Column(db.String(100))
    society = db.Column(db.String(100))
    user_name = db.Column(db.String(120))
    password_hash = db.Column(db.String(120))
    profile_picture = db.Column(db.String(120), default='default')
    positions = db.relationship('Position', backref='member', lazy="dynamic", cascade="all,delete")


@app.route('/')
def new_member():
    return render_template('index.html')

app.run(debug=True)