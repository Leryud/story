import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hellodgu'

    UPLOADED_PHOTOS_DEST = os.path.join(basedir, 'img/profile')
    UPLOADED_PHOTOS_STORY_DEST = os.path.join(basedir, 'img/stories')

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False