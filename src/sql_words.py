from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine, ForeignKey, PrimaryKeyConstraint
from sqlalchemy.orm import Session, relationship, backref 
import pandas as pd

Base = declarative_base()

class Easy_Words(Base):
    __tablename__ = 'easy'
    __table_args__ = (PrimaryKeyConstraint('id'),)
    id = Column(Integer(), primary_key=True)
    easy_words = Column(String())
    themes = relationship('Themes', backref=backref('eword'))
    

    def __repr__(self):
        return f'Easy_Words(id={self.id}),' + \
            f'easy_words={self.easy_words}'

class Pokemon(Base):
    __tablename__ = 'pokemon'
    __table_args__ = (PrimaryKeyConstraint('id'),)
    id = Column(Integer(), primary_key=True)
    pokemon_names = Column(String())        

class Medium_Words(Base):
    __tablename__ = 'medium'
    __table_args__ = (PrimaryKeyConstraint('id'),)
    id = Column(Integer(), primary_key=True)
    medium_words = Column(String())
    themes = relationship('Themes', backref=backref('mword'))

    def __repr__(self):
        return f'Medium_Words(id={self.id}),' + \
            f'medium_words={self.medium_words}' 

class Difficult_Words(Base):
    __tablename__ = 'difficult'
    __table_args__ = (PrimaryKeyConstraint('id'),)
    id = Column(Integer(), primary_key=True)
    difficult_words = Column(String())
    themes = relationship('Themes', backref=backref('dword'))

    def __repr__(self):
        return f'Difficult_Words(id={self.id}),' + \
            f'difficult_words={self.difficult_words}' 

class Themes(Base):
    __tablename__ = 'themes'
    id = Column(Integer(), primary_key=True)
    themes = Column(String())
    easy_words_id = Column(Integer(), ForeignKey("easy.id"))
    medium_words_id = Column(Integer(), ForeignKey("medium.id"))
    difficult_words_id = Column(Integer(), ForeignKey("difficult.id"))

    def __repr__(self):
        return f'Easy_Words(id={self.id}),' + \
            f'eword={self.easy_words}'

    def __repr__(self):
        return f'Medium_Words(id={self.id}),' + \
            f'mword={self.medium_words}'

    def __repr__(self):
        return f'Difficult_Words(id={self.id}),' + \
            f'difficult_words={self.difficult_words}' 
    

engine = create_engine('sqlite:///word_list.db')
Base.metadata.create_all(engine)
word_list = pd.read_csv('words_sidtest.csv')
pokemon_list = pd.read_csv('pokemon.csv')
with Session(engine) as session: 
    # for pokemon in pokemon_list.Name.values.flatten():
    #     pkm = Pokemon(pokemon_names = pokemon)
    #     session.add(pkm)
    for each_word in word_list.values.flatten():
        if len(each_word) < 5:
            eword = Easy_Words(easy_words = each_word)
            
            session.add(eword)

        if len(each_word) > 5 and len(each_word) < 8:
            mword = Medium_Words(medium_words = each_word)

            session.add(mword)

        elif len(each_word) > 9:
            dword = Difficult_Words(difficult_words = each_word)
            
            session.add(dword)

    session.commit()