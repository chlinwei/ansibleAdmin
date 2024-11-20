from sqlalchemy import create_engine, Column, Integer, String

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,session
from src.app import ansibleAdmin


SQLALCHEMY_DATABASE_URL = ansibleAdmin.config["DB_URL"]

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Session = SessionLocal()
Base = declarative_base()


# def create_db_and_tables():
#     Base.metadata.create_all(engine)

def get_session():
    try:
        yield Session
    finally:
        Session.close()
    
    


    