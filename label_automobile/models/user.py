from sqlalchemy import Boolean, Column, String
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship

from label_automobile.models.meta import Base, BaseModel


class User(BaseModel, Base):
    __tablename__ = 'user'

    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    email_ = Column(String, nullable=False, unique=True)
    password = Column(String)
    active = Column(Boolean, nullable=False, default=False)

    shopping_cart = relationship("ShoppingCart", back_populates="user")

    @hybrid_property
    def email(self):
        return self.email_

    @email.setter
    def email(self, value):
        if not isinstance(value, str) or '@' not in value:
            raise Exception('Invalid Email')
        self.email_ = value
