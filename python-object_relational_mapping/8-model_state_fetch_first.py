#!/usr/bin/python3
""" FIRST FETCH WITH PYTHON """

if __name__ == "__main__":
    import sys
    from sqlalchemy.ext.declarative import declarative_base
    from model_state import Base, State
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    cursor = Session()
    result = cursor.query(State.id, State.name).filter_by(id=1).one_or_none()
    if result == None:
        print("Nothing")
    else:
        print(f'{result[0]}: {result[1]}')
