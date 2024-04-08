from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('postgresql://posttest:1@localhost:5432/users', echo=True)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'  

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
    address = Column(String(50))


# Base.metadata.create_all(engine)

user1 = User(name='Alice', age=20, address='New York City')
user2 = User(name='Anna', age=24, address='Tashkent')
user3 = User(name='John', age=18, address='London')

session.add(user1)
session.add_all([user2, user3])
session.commit() 
