from sqlalchemy import Column, Float, String

from label_automobile.models.meta import Base, BaseModel


class Inventory(BaseModel, Base):
    __tablename__ = 'inventory'

    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    price = Column(Float, nullable=False)
    ref_number = Column(String, nullable=False)
