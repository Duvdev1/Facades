from sqlalchemy import Column, Integer, ForeignKey
from db_config import Base


class visit(Base):
    __tablename__ = 'visit'

    id = Column(Integer(), primary_key=True, autoincrement=True)
    t_id = Column(Integer(), ForeignKey('tourist.id'), nullable=False)
    a_id = Column(Integer(), ForeignKey('attraction.id'), nullable=False)
    year = Column(Integer(), nullable=False, default=2021)

    def __repr__(self):
        return f'\n<Visit id={self.id} t_id={self.t_id} a_id={self.a_id}> year={self.year}>'

    def __str__(self):
        return f'\n<Visit id={self.id} t_id={self.t_id} a_id={self.a_id}> year={self.year}>'
