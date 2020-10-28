import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True, nullable = True, unique=True)
    username = Column(String(250), nullable=False, unique=True)
    firstname = Column(String(250), nullable=False, unique=True)
    lastname = Column(String(250), nullable=False, unique=True)
    email = Column(String(250), nullable=False, unique=True)

class Comment(Base):
    __tablename__ = 'comment'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer(250), primary_key = True, nullable = True, unique=True)
    comment_text = Column(String(250), nullable = True, unique=True)
    author_id = Column(String(250), ForeignKey('user.id'), nullable=False)
    post_id = Column(String(250), ForeignKey('post.id'), nullable=False)

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer(250), primary_key = True, nullable = True, unique=True)
    user_id = Column(Integer(250), nullable=True)

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer(250), primary_key = True, nullable = True, unique=True)
    type = enumerate()
    url = Column(String(250), nullable=True)
    post_id = Column(Integer, ForeignKey('Post.id'), nullable=False)

class Followers(Base):
    __tablename__ = 'followers'
    id = Column(Integer(250), primary_key = True, nullable = True, unique=True)
    user_from_id = Column(Integer, ForeignKey('User.id'), nullable=False)
    user_to_id = Column(Integer, ForeignKey('User.id'), nullable=False)



    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')