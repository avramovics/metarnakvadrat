from sqlalchemy import create_engine, Column, Integer, String,  text,inspect    
from sqlalchemy.orm import sessionmaker
from .variables import SQLALCHEMY_DATABASE_URL
#from .migrate import migrate
# Create an SQLAlchemy engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)
# Create a session using the engine
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
