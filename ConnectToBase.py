from sqlalchemy import Column, Integer, String, Boolean, Date, create_engine
from sqlalchemy.engine.url import URL
import psycopg2
from sqlalchemy.ext.declarative import declarative_base


DeclarativeBase = declarative_base()


class Post(DeclarativeBase):
    __tablename__ = "discart"
    discart_id = Column(Integer)
    count_id = Column(Integer, primary_key=True)
    boolean = Column(Boolean)
    add_date = Column(Date)


class Post1(DeclarativeBase):
    __tablename__ = "manager"
    manager_id = Column(Integer)
    manager_name = Column(String, primary_key=True)


class Post2(DeclarativeBase):
    __tablename__ = "buyer"
    buyer_id = Column(Integer, primary_key=True)
    buyer = Column(String)



DATABASE = {
    'drivername': '0',
    'host': '0',
    'port': '5432',
    'username': '0',
    'password': '0',
    'database': '0'
}


def connect():
    engine = create_engine(URL(**DATABASE))
    DeclarativeBase.metadata.create_all(engine)
    con = psycopg2.connect(
        database="0",
        user="0",
        password="0",
        host="0",
        port="5432",
    )
    return con
