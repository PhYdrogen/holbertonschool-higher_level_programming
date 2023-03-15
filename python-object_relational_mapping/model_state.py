#!/usr/bin/python3
""" DOCUMENTATION """

if __name__ == "__main__":
    from sqlalchemy import Column, Integer, String, create_engine
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy.orm import sessionmaker
    import sys

    Base = declarative_base()
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    class State(Base):
        """ Class state that inherit of base
        """

        __tablename__ = 'states'
        id = Column("id", Integer, nullable=False,unique=True,
                    autoincrement="auto", primary_key=True)
        name = Column("name", String(128), nullable=False)
        def __init__(self):
            """ THIS IS DOC """
            pass