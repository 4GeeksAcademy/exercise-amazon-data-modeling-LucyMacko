import enum
from sqlalchemy import Column, ForeignKey, Integer, String, Enum, Float
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er


class myEnum(enum.Enum):
    refund = "refund"
    paid = "paid"
    cancelled = "cancelled"

Base = declarative_base()

class Product(Base):
    __tablename__ = 'product'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True,)
    name = Column(String(250), nullable=False)
    pricing = Column(Float)
    weight = Column(Float)
    color = Column(String(250))    

class Customer(Base):
    __tablename__ = 'customer'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(250), unique= True)
    address= Column(String(250))

class Shopping_Cart(Base):
    __tablename__ = 'shopping_cart'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    product_id = Column(Integer, ForeignKey('product.id'), primary_key=True)
    customer_id = Column(Integer, ForeignKey('customer.id'), primary_key=True)
    quantity = Column(Integer)
    price = Column(Float)
    bill_id= Column(Integer, ForeignKey('bill.id'), primary_key=True)    

class Bill(Base):
    __tablename__ = 'bill'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, ForeignKey('shopping_cart.bill_id'), primary_key=True)
    street_name = Column(String(250))
    created_at = Column(Integer)
    total_price = Column(Float)
    status=Column(Enum(myEnum))    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')


