from sqlalchemy import Integer,String,Column,Float
from sqlalchemy.ext.declarative import declarative_base
Base=declarative_base()
class Product(Base):
    __tablename__="product"
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String)
    description=Column(String)
    quantity=Column(Integer)
    price=Column(Float)