from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine, ForeignKey, Table
from sqlalchemy.orm import Session, relationship, backref 
import pandas as pd

Base = declarative_base()

class Easy_Words(Base):
    __tablename__ = 'easy'
    id = Column(Integer(), primary_key=True)
    words = Column(String())

class Medium_Words(Base):
    __tablename__ = 'medium'
    id = Column(Integer(), primary_key=True)
    words = Column(String())

class Difficult_Words(Base):
    __tablename__ = 'difficult'
    id = Column(Integer(), primary_key=True)
    words = Column(String())

engine = create_engine('sqlite:///word_list.db')
# Base.metadata.create_all(engine)
word_list = pd.read_csv('words_sidtest.csv')
with Session(engine) as session: 
    for each_word in word_list.values.flatten():
        if len(each_word) < 5:
            word = Easy_Words(
                words = each_word
            )
        if len(each_word) > 5 and len(each_word) < 8:
                word = Medium_Words(
            words = each_word
        )

        elif len(each_word) > 9:
            word = Difficult_Words(
                words = each_word
                )

        session.add(word)
    session.commit()