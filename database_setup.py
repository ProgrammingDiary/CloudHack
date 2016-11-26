from sqlalchemy import Column, ForeignKey, String, Integer, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class User(Base):
	__tablename__ = 'user'
	id = Column(Integer, primary_key=True)
	uid = Column(String(8), nullable=False)
	name = Column(String(120), nullable=False)
	email = Column(String(80), nullable=False)
	address = Column(String(120), nullable=False)
	password = Column(String(80), nullable=False)


class Merchant(Base):
	__tablename__ = 'merchant'
	id = Column(Integer, primary_key=True)
	mid = Column(String(8), nullable=False)
	email = Column(String(80), nullable=False)
	name = Column(String(120), nullable=False)
	address = Column(String(120), nullable=False)
	password = Column(String(80), nullable=False)

class Bill(Base):
	import datetime
	__tablename__ = 'bill'
	id = Column(Integer, primary_key=True)
	merchant_id = Column(String(8), ForeignKey('merchant.mid'))
	user_id = Column(String(8), ForeignKey('user.uid'))
	description = Column(String(150), nullable=False)
	amount = Column(Float, nullable=False)
	date = Column(DateTime, default=datetime.datetime.utcnow())
	user = relationship(User)
	merchant = relationship(Merchant)

engine = create_engine('sqlite:///database.db')

Base.metadata.create_all(engine)