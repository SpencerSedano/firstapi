from sqlalchemy import Column, Integer, String
from config import Base

class Quote(Base):
    __tablename__ = 'quote'

    id=Column(Integer, primary_key=True)
    name=Column(String)
    quote=Column(String)
    date=Column(String)