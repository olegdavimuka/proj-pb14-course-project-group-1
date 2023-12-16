from os import environ

from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

metadata = MetaData()


class Base(AsyncAttrs, DeclarativeBase):
    pass


connection_str = environ.get("PG_DB_URL")
if not connection_str:
    raise OSError("PG_DB_URL is not set.")

engine = create_async_engine(connection_str)

async_session = async_sessionmaker(engine, expire_on_commit=False)
