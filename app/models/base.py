from sqlalchemy.ext.declarative import declarative_base


Base = (
    declarative_base()
)  # TODO: better move to app/db, also there you maybe should add logic of session creation
metadata = (
    Base.metadata
)  # TODO: better move to app/db, also there you maybe should add logic of session creation
