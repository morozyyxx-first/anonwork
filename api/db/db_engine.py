import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import DeclarativeBase

from dotenv import load_dotenv
load_dotenv()

engine = create_engine(
    url=os.getenv("DB_URL"),
    echo=True
)
Session = sessionmaker(
    bind=engine,
    expire_on_commit=False
)

class Base(DeclarativeBase):
    pass

def init_db():
    with engine.begin() as conn:
        Base.metadata.create_all

def get_session():
    with Session() as session:
        return session

