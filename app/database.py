from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

Base = declarative_base()

def get_engine():
    return create_engine(os.getenv('DATABASE_URL', 'sqlite:///lendlib.db'))

def get_session():
    engine = get_engine()
    Session = sessionmaker(bind=engine)
    return Session()
