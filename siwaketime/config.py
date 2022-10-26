import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import timedelta, timezone

secret = os.urandom(24)
SECRET_KEY = secret
SQLALCHEMY_DATABASE_URI= 'sqlite:///siwaketime.db'

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

JST = timezone(timedelta(hours=+9), 'JST')

DEBUG = True