from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from os import environ

Base = (
    declarative_base()
)  # TODO: better move to app/db, also there you maybe should add logic of session creation
metadata = (
    Base.metadata
)  # TODO: better move to app/db, also there you maybe should add logic of session creation

engine = create_engine(environ.get("PG_DB_URL"))
conn = engine.connect()
Session = sessionmaker(bind=engine)
