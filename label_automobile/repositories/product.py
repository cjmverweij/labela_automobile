from label_automobile.models.product import Product


class ProductRepository:
    def __init__(self, session):
        self.session = session

    def list(self):
        return self.session.query(Product).all()

    def get_by_id(self, id):
        return self.session.query(Product).filter(
            Product.id == id).one()