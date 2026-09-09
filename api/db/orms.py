from typing import List

from sqlalchemy import String, JSON
from sqlalchemy.orm import Mapped, mapped_column
from .db_engine import Base

class UsersORM(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(20))
    email: Mapped[str]
    password: Mapped[str]

class ItemsORM(Base):
    __tablename__ = "items"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(20))
    name_of_company: Mapped[str] = mapped_column(String(50))
    salary: Mapped[str] = mapped_column(String(15))
    location: Mapped[str] = mapped_column(String(50))
    contacts: Mapped[str] = mapped_column(String(100))
    job_time: Mapped[str] = mapped_column(String(20))
    description: Mapped[str] = mapped_column(String(300))
    skills: Mapped[List[str]] = mapped_column(JSON, default=[])
