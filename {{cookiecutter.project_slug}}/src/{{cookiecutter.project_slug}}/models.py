from datetime import datetime, timezone

from sqlalchemy import Column, Text, Integer, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "user"

