from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(length=128), unique=True, index=True)
    salt = Column(String(length=128))
    password = Column(String(length=128))

    pastes = relationship('Paste', back_populates='owner')


class Paste(Base):
    __tablename__ = 'pastes'

    id = Column(Integer, primary_key=True, index=True)
    # Need some attributes more
    owner_id = Column(Integer, ForeignKey('users.id'))
    title = Column(String(length=128), index=True)
    content = Column(String(length=128), index=True)


    owner = relationship('User', back_populates='pastes')


