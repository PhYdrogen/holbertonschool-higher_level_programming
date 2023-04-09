#!/usr/bin/python3
""" DOCUMENTATION """

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class City(Base):
    """ Class city that inherit of base """

    __tablename__ = 'cities'
    id = Column("id", Integer, nullable=False, unique=True,
                autoincrement="auto", primary_key=True)
    name = Column("name", String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
