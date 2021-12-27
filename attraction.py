from sqlalchemy import Column, Integer, String
from db_config import Base

class attraction(Base):
    __tablename__ = 'attraction'

    id = Column(Integer(), primary_key=True, autoincrement=True)
    name = Column(String(50), unique=True, nullable=False)
    price = Column(Integer(), nullable=False, default=0)

    def __repr__(self):
        return f'\n<Attraction id={self.id} name={self.name} price={self.price}>'

    def __str__(self):
        return f'\n<Attraction id={self.id} name={self.name} price={self.price}>'
