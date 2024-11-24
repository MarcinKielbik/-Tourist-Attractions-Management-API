from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Utwórz bazę deklaratywną
Base = declarative_base()

class Attraction(Base):
    __tablename__ = 'attractions'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    location = Column(String, nullable=False)
    description = Column(String, nullable=True)
    category = Column(String, nullable=True)

    def __repr__(self):
        return f"<Attraction(id={self.id}, name={self.name}, location={self.location}, description={self.description}, category={self.category})>"