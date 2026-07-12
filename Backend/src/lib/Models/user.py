# src/lib/models/user.py
from sqlalchemy import Column, Integer, String
from src.lib.db import Base

class UserInfo(Base):
    __tablename__ = "Userinfo"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    password_hash = Column(String(255), nullable=False)