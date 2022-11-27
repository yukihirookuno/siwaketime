import os
from os.path import join, dirname
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

secret = os.urandom(24)
SECRET_KEY = secret

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI= 'sqlite:///'+os.path.join(basedir, "siwaketime.db")

engine = create_engine(
    SQLALCHEMY_DATABASE_URI,
    convert_unicode = True,
    encoding="utf-8",
    echo=True,
    )

db_session = scoped_session(
    sessionmaker(
        autocommit = False,
        autoflush = False,
        bind = engine
    )
)

Base = declarative_base()
Base.query = db_session.query_property()

SQLALCHEMY_TRACK_MODIFICATIONS = True

DEBUG = True

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), ".env")

FLASK_APP = os.environ.get('FLASK_APP')
#FLASK_ENV = os.environ.get('FLASK_ENV')


api_key = os.environ.get('api_key')
api_secret_key = os.environ.get('api_secret_key')
access_token = os.environ.get('access_token')
access_token_secret = os.environ.get('access_token_secret')
bearer_token =os.environ.get('bearer_token')