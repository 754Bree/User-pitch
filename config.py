
import os
from dotenv import load_dotenv
load_dotenv()
BASEDIR = os.path.abspath(os.path.dirname(__file__))
DBNAME = "app.db"

class Config:
    DATABASE_NAME = DBNAME
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(BASEDIR, DBNAME)
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SECRET_KEY='3d6f45a5fc12445dbac2f59c3b6c7cb1'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = 'brianamartha57@gmail.com'
    MAIL_PASSWORD = 'Ice754'

class ProdConfig(Config):
    DATABASE_NAME = DBNAME
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(BASEDIR, DBNAME)

class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}


