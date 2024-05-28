from pydantic import BaseModel
from sqlalchemy import  Column, Integer, String, text, Float,  Boolean, Enum as SQLAlchemyEnum
from sqlalchemy.ext.declarative import declarative_base
from typing import List
from enum import Enum
#from enum import Enum
Base = declarative_base()

#Astro Chart model
class Chart(Base):
    __tablename__ = "chart"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String(50), unique=True)
    year = Column(Integer)  # Add the 'year' attribute
    month = Column(Integer)  # Add the 'month' attribute
    date = Column(Integer)  # Add the 'date' attribute
    local_time = Column(Float)  # Add the 'local_time' attribute
    longi = Column(Float)  # Add the 'longi' attribute
    lati = Column(Float)  # Add the 'lati' attribute
    hours_difference = Column(Integer)  # Add the 'hours_difference' attribute

#Users model
# Create the SQLAlchemy Enum
# Create the SQLAlchemy Enum
class GenderEnum(Enum):
    male = "male"
    female = "female"

    def __str__(self):
        return str(self.value)
#Users model
class UserBase(BaseModel):
    user_id: str


class UserList(BaseModel):
    users_id: List[str]


class UserInsert(BaseModel):
    user_id: str 
    year: int
    month: int
    date: int 
    local_time:float  # Add the 'local_time' attribute
    longi:float  # Add the 'longi' attribute
    lati:float  # Add the 'lati' attribute
    hours_difference: int  # Add the 'hours_difference' attribute
    gender:GenderEnum
    exact_time:bool

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True) 
    user_id = Column(String(50), unique=True)
    year = Column(Integer)  # Add the 'year' attribute
    month = Column(Integer)  # Add the 'month' attribute
    date = Column(Integer)  # Add the 'date' attribute
    local_time = Column(Float)  # Add the 'local_time' attribute
    longi = Column(Float)  # Add the 'longi' attribute
    lati = Column(Float)  # Add the 'lati' attribute
    hours_difference = Column(Integer)  # Add the 'hours_difference' attribute
    gender = Column(SQLAlchemyEnum(GenderEnum))  # Use the SQLAlchemy Enum  # Add the 'hours_difference' attribute
    exact_time = Column(Boolean)
# List of SQLAlchemy model classes
sqlalchemy_models = [User, Chart]