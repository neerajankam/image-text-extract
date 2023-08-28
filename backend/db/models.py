from sqlalchemy import Column, Integer, String, JSON, Text
from sqlalchemy.ext.declarative import declarative_base

from .connection import Database


Base = declarative_base()


class Extracts(Base):
    """
    Represents the EXTRACTS table in the database.
    """

    __tablename__ = "extracts"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    content = Column(Text)


# while True:
#     if Database.wait_for_database():
#         break
# # Create the tables
Base.metadata.create_all(bind=Database.get_engine())
