from sqlalchemy import create_engine

from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from src.config import settings


SQLALCHEMY_DATABASE_URL = settings.DB_URL

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Session = SessionLocal()
Base = declarative_base()


# def create_db_and_tables():
#     Base.metadata.create_all(engine)

# def get_session():
#     try:
#         yield Session
#     finally:
#         Session.close()



