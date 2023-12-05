from os import environ

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
metadata = Base.metadata

connection_str = environ.get("PG_DB_URL")
if not connection_str:
    raise OSError("PG_DB_URL is not set.")

engine = create_engine(connection_str)
conn = engine.connect()
Session = sessionmaker(bind=engine)
