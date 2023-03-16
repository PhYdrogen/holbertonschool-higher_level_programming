#!/usr/bin/python3
""" FETCH JUST A LETTER WITH PYTHON """

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
    result = cursor.query(State).filter(State.name.
                                        like('%a%')).order_by(State.id)
    for col in result:
        print(f'{col.id}: {col.name}')
