from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from label_automobile.models.meta import Base, BaseModel


class ShoppingCart(Base, BaseModel):
    __tablename__ = 'shopping_cart'

    user_id = Column(UUID, ForeignKey('user.id'))
    product_id = Column(UUID, ForeignKey('inventory.id'))

    user = relationship("User", back_populates="shopping_cart")
    product = relationship("Inventory", backref="shopping_cart")