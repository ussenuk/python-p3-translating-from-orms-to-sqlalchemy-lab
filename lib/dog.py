from models import Dog, Base
from sqlalchemy import (create_engine, desc, func,Column, String, Integer)
from sqlalchemy.orm import sessionmaker



def create_table(Base, engine):
    # engine = create_engine('sqlite:///dogs.db')
    return Base.metadata.create_all(engine)
    

def save(session, dog):
    session.add(dog)
    session.commit()

def get_all(session):
    return session.query(Dog).all()

def find_by_name(session, name):
    return session.query(Dog).filter(Dog.name.like(name)).first()

def find_by_id(session, id):
    return session.query(Dog).filter(Dog.id == id).first()

def find_by_name_and_breed(session, name, breed):
    return session.query(Dog).filter(Dog.name == name, Dog.breed == breed).first()

def update_breed(session, dog, breed):
    # dog = session.query(Dog).filter_by(Dog.name == {dog}).first()
    # dog = session.query(Dog).filter(Dog.name == dog).first()
    if dog: 
        dog.breed = breed
        session.commit()
    else:
        print(f"No dog found with the name {dog}")

    

# if __name__ == '__main__':
#     from sqlalchemy import (create_engine, desc, func,Column, String, Integer)
#     from sqlalchemy.orm import sessionmaker

#     engine = create_engine('sqlite:///dogs.db')
#     # Base.metadata.create_all(engine)

#     # use our engine to configure a 'Session' class
#     Session = sessionmaker(bind=engine)
#     # use 'Session' class to create 'session' object
#     session = Session()

#     # create_table(Base, engine)

#     # dog = Dog(name="Newton", breed="Corgi")

#     # save(session, dog)

#     names = [name for name in session.query(Dog.name, Dog.breed)]

#     print(names)

#     get_all(session)

#     find_by_name(session, "Albert")

#     # for record in query: print(record.name, record.breed)

#     find_by_id(session, id=3)
#     # for record in query2: print(record.name, record.breed)

    
#     find_by_name_and_breed(session, name="Newton", breed="Bulldog")
#     # for record in query3: print(record.name, record.breed)


#     # dog = session.query(Dog).filter_by(name='Newton').first()
#     # update_breed(session, dog, breed="chihuahua")

#     # for record in query: print(record.name and record.breed)
