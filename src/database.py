from sqlalchemy import create_engine, Column, Integer, String

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,session
import os


ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) 
SQLALCHEMY_DATABASE_URL = "sqlite:///sql_app.db"




engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

session = SessionLocal()
Base = declarative_base()


def create_db_and_tables():
    Base.metadata.create_all(engine)
    print(ROOT_DIR)


def get_session():
    try:
        yield session
    finally:
        session.close()
    
    


    