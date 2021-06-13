from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, ValidationError, Email, Length
from flask_wtf.file import FileField, FileRequired, FileAllowed
from app.models import User
from flask_uploads import UploadSet, IMAGES

photos = UploadSet('photos', IMAGES)

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit_button = SubmitField('Login')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    profilePicture = FileField('Profile Picture', validators=[FileAllowed(photos, 'Image only!'), FileRequired('File was empty!')])
    submit_button = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')


class StoryForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    body = TextAreaField('About your story', validators=[DataRequired(), Length(min=1, max=4096)])
    storyPicture = FileField('Add a picture to your story', validators=[FileAllowed(photos, 'Image only!')])
    submit_button = SubmitField('Submit')


class EditProfileForm(FlaskForm):
    username = StringField('Username')
    email = StringField('Email', validators=[Email()])
    about_me = TextAreaField('About me', validators=[Length(min=0, max=240)])
    submit_button = SubmitField('Submit')


class EditStory(FlaskForm):
    title = StringField('Title')
    body = TextAreaField('About your story', validators=[Length(min=1, max=4096)])
    submit_button = SubmitField('Submit')