from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

class User(Base):
	__tablename__ = "users"

	id = Column(Integer, primary_key=True, autoincrement=True)
	username = Column(String, unique=True, index=True)
	email = Column(String, unique=True)
	full_name = Column(String)
	hashed_password = Column(String)
	is_active = Column(Boolean, default=True)
