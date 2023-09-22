#!/usr/bin/python3
"""prints the State object with the name passed
as argument from the database"""
if __name__ == "__main__":

    import sys
    from model_state import Base, State
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    records = session.query(State).filter(
        State.name.like('%a%'))
    for record in records:
        session.delete(record)
    session.commit()
    session.close()
