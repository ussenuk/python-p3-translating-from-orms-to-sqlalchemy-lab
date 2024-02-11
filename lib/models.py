#!/usr/bin/env python3

from sqlalchemy import (create_engine, desc, func,Column, String, Integer)
from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Dog(Base):
    __tablename__ = 'dogs'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    breed = Column(String())

# if __name__ == '__main__':
    
#     engine = create_engine('sqlite:///:memory:')
#     Base.metadata.create_all(engine)

#     # use our engine to configure a 'Session' class
#     Session = sessionmaker(bind=engine)
#     # use 'Session' class to create 'session' object
#     session = Session()


#     einstein = Dog(
#             name="Einstein",
#             breed="Chiwawa",
#         )

#     turing = Dog(
#         name="Turing",
#         breed="German Sherperd",
#     )

#     session.bulk_save_objects([einstein, turing])
#     session.commit()

#     # read records
#     # dogs = session.query(Dog).all()

#     names = [name for name in session.query(Dog.name, Dog.breed)]

#     print(names)