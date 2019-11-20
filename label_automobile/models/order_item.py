from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from label_automobile.models.meta import Base, BaseModel


class OrderItem(BaseModel, Base):
    __tablename__ = 'order_item'

    order_id = Column(UUID(as_uuid=True), ForeignKey('order.id'))
    product_id = Column(UUID(as_uuid=True), ForeignKey('product.id'))
    quantity = Column(Integer, nullable=False)
    product = relationship('Product', backref='order_item')

