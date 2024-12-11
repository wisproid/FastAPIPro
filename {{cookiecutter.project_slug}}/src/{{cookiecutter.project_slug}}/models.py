import uuid
from datetime import datetime, UTC
from sqlalchemy import Column, String, Boolean, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)  # UUID primary key
    username = Column(String(50), unique=True)  # Unique username
    email = Column(String(100), unique=True)    # Unique email address
    password_hash = Column(String(128))         # Hashed password
    is_active = Column(Boolean, default=True)   # Indicates if the user account is active
    is_email_verified = Column(Boolean, default=False)  # Indicates if the email is verified
    created_at = Column(DateTime(timezone=True), default=datetime.now(UTC))  # Record creation time
    updated_at = Column(DateTime(timezone=True), default=datetime.now(UTC), onupdate=datetime.now(UTC))  # Last update time

