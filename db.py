#!/usr/bin/env python3

from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.types import *
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///db.sqlite3', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Movie(Base):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    chat = Column(Integer)
    name = Column(String)
    status = Column(String)

    def __repr__(self):
        return "<Movie(id={}, name='{}', status='{}')>".format(
            self.id, self.name, self.status
        )

class Serie(Base):
    __tablename__ = 'series'

    id = Column(Integer, primary_key=True)
    chat = Column(Integer)
    name = Column(String)
    status = Column(String)

    def __repr__(self):
        return "<Serie(id={}, name='{}', status='{}')>".format(
            self.id, self.name, self.status
        )

Base.metadata.create_all(engine)

if __name__ == '__main__':
    pass