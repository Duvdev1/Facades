from sqlalchemy import Column, Integer, String, DateTime, REAL
from db_config import Base

class Tourist(Base):
    __tablename__ = 'tourist'

    id = Column(Integer(), primary_key=True, autoincrement=True)
    name: Column = Column(String(50), unique=True, nullable=False)
    country = Column(String(20), nullable=False, default='IL')

    def __repr__(self):
        return f'\n<Tourist id={self.id} name={self.name} country={self.country}>'

    def __str__(self):
        return f'\n<Tourist id={self.id} name={self.name} country={self.country}>'