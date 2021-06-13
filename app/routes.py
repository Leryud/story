from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm, RegistrationForm
from flask_login import current_user, login_user, login_required
from flask_login import logout_user
from app.models import Story, User
from app import db
from flask_uploads import UploadSet, configure_uploads, IMAGES
from werkzeug.utils import secure_filename
import os
from flask import send_from_directory

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user)
        return redirect(url_for('home'))
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return(redirect(url_for('index')))


@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/home')
def home():
    return render_template('home.html', posts=Story)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        pic = form.profilePicture.data
        filename = pic.filename     
        pic.save(os.path.join(app.config['UPLOADED_PHOTOS_DEST'], filename))
        user = User(username=form.username.data, email=form.email.data, location=form.location.data, profilePicture=filename)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Welcome to Story !')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


@app.route('/new_story')
def new_story():
    return render_template('new.html')

@app.route('/profile_picture')
def profile_picture():
    path = current_user.profilePicture
    print(path)
    return send_from_directory(app.config['UPLOADED_PHOTOS_DEST'], path)
    