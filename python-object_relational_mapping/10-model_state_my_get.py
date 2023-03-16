#!/usr/bin/python3
""" FETCH JUST A LETTER WITH PYTHON """

if __name__ == "__main__":
    import sys
    from sqlalchemy.ext.declarative import declarative_base
    from model_state import Base, State
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker
    if len(sys.argv) != 5:
        exit
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]),
                        pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    cursor = Session()
    result = cursor.query(State).filter(State.name == sys.argv[4])
    found = False
    for col in result:
        found = True
        print(f'{col.id}')
    if not found:
        print("Not found")
