import os
secret = os.urandom(24)
SECRET_KEY = secret
SQLALCHEMY_DATABASE_URI = 'sqlite:///siwaketime.db'
SQLALCHEMY_TRACK_MODIFICATIONS = True
DEBUG = True