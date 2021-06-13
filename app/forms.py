from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
from flask_wtf.file import FileField, FileRequired, FileAllowed
from app.models import User
from flask_uploads import UploadSet, configure_uploads, IMAGES

photos = UploadSet('photos', IMAGES)

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
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