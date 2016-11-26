from sqlalchemy import Column, ForeignKey, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class User(Base):
	__tablename__ = 'user'
	id = Column(Integer, primary_key=True)
	uid = Column(String(8), nullable=False)
	name = Column(String(120), nullable=False)
	address = Column(String(120), nullable=False)
	password = Column(String(80), nullable=False)


class Merchant(Base):
	__tablename__ = 'merchant'
	id = Column(Integer, primary_key=True)
	mid = Column(String(8), nullable=False)
	name = Column(String(120), nullable=False)
	address = Column(String(150), nullable=False)
	password = Column(String(80), nullable=False)

engine = create_engine('sqlite:///database.db')

Base.metadata.create_all(engine)