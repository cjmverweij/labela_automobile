from sqlalchemy import Column, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from label_automobile.models.meta import Base, BaseModel


class Order(BaseModel, Base):
    __tablename__ = 'order'

    user_id = Column(UUID(as_uuid=True), ForeignKey('user.id'))
    delivery_date = Column(DateTime, nullable=False)

    items = relationship('OrderItem', backref='order', cascade='all, delete')
