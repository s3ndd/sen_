import uuid

from sqlalchemy import Column, DateTime, func, String, Boolean, BINARY, text

from app.database import Base
from app.model.guid import GUID


class User(Base):
    __tablename__ = 'user'

    id = Column(GUID(), primary_key=True, default=text("(UUID_TO_BIN(UUID(), true))"))
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    deleted_at = Column(DateTime, nullable=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    mobile = Column(String(20), unique=True, nullable=False)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)

    def __init__(self, username, password, email, mobile, first_name, last_name, is_active=True):
        self.username = username
        self.password = password
        self.email = email
        self.mobile = mobile
        self.first_name = first_name
        self.last_name = last_name
        self.is_active = is_active

    def __repr__(self):
        return '<User %r>' % self.username

