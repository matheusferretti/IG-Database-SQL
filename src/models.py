import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()


class ShoppingCart(Base):
    __tablename__ = 'shoppingcart'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    product_id = Column(Integer, primary_key=True)
    customer_id = Column(String(250))
    quantity = Column(Integer(250))
    price = Column(float(250))
    bill_id = Column(Integer(250), nullable=False)

class Product(Base):
    __tablename__ = 'product'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, ForeignKey('shoppingcart.product_id'))
    shoppingcart = relationship(ShoppingCart)
    name = Column(String(250))
    pricing = Column(float(250))
    weight = Column(float(250), nullable=False)

class Customer(Base):
    id = Column(Integer, ForeignKey('shoppingcart.customer_id'))
    shoppingcart = relationship(ShoppingCart)
    first_name = Column(String(250))
    last_name = Column(String(250))
    email = Column(String(250))
    address = Column(String(250))

class Bill(Base):
    id = Column(Integer, ForeignKey('shoppingcart.bill_id'))
    shoppingcart = relationship(ShoppingCart)
    


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')