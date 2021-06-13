from flask import render_template, flash, redirect, url_for, request
from app import app
from app.forms import EditProfileForm, EditStory, LoginForm, RegistrationForm, StoryForm
from flask_login import current_user, login_user, login_required
from flask_login import logout_user
from app.models import Story, User
from app import db
import os
from flask import send_from_directory
from datetime import datetime


@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.username.data).first()
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
    stories = current_user.stories.all()
    return render_template('home.html', stories=stories)

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


@app.route('/new_story', methods = ['GET', 'POST'])
def new_story():
    form = StoryForm()
    if form.validate_on_submit():
        story_pic = form.storyPicture.data
        story_filename = story_pic.filename     
        story_pic.save(os.path.join(app.config['UPLOADED_PHOTOS_STORY_DEST'], story_filename))
        story = Story(title=form.title.data, body=form.body.data, author=current_user, storyPicture = story_filename)
        db.session.add(story)
        db.session.commit()
        return(redirect(url_for('home')))
    stories = current_user.stories.all()
    return render_template('new.html', form=form, stories=stories)
    

@app.route('/profile_picture')
def profile_picture():
    path = current_user.profilePicture
    return send_from_directory(app.config['UPLOADED_PHOTOS_DEST'], path)

@app.route('/story_picture/<int:id>')
def story_picture(id):
    story = Story.query.get(id)
    path = story.storyPicture
    return send_from_directory(app.config['UPLOADED_PHOTOS_STORY_DEST'], path)

@app.route('/edit_profile')
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        return redirect(url_for('profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
        form.about_me.data = current_user.about_me
    db.session.flush
    return render_template('edit_profile.html', form=form)

@app.route('/modify_post/<int:id>', methods =['GET', 'POST'])
def modify_post(id):
    story = Story.query.get(id)
    form = EditStory()
    if form.validate_on_submit():
        story.title = form.title.data
        story.body = form.body.data
        db.session.commit()
        return redirect(url_for('home'))
    elif request.method == 'GET':
        form.title.data = story.title
        form.body.data = story.body
    db.session.flush
    return render_template('modify_post.html', form=form)


