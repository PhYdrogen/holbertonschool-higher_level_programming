#!/usr/bin/python3
""" DOCUMENTATION """

if __name__ == "__main__":
    from sqlalchemy import Column, Integer, String
    from sqlalchemy.ext.declarative import declarative_base

    Base = declarative_base()
    class State(Base):
        """ Class state that inherit of base 
            from the task 6,
            tablename is the table of the bd
            id is id
            and
            name is name
            :)
        """

        __tablename__ = 'states'
        id = Column("id", Integer, nullable=False,unique=True,
                    autoincrement="auto", primary_key=True)
        name = Column("name", String(128), nullable=False)
