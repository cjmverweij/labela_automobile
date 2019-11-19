from label_automobile.models.shopping_cart import ShoppingCart


class ShoppingCartRepository:
    def __init__(self, session):
        self.session = session

    def add_product(self, user_id, product_id):
        self.session.add(
            ShoppingCart(
                user_id=user_id,
                product_id=product_id
            )
        )

    def get_by_user_id(self, user_id):
        return self.session.query(ShoppingCart).filter(
            ShoppingCart.user_id == user_id).all()

    def delete(self, user_id):
        return self.session.query(ShoppingCart).filter(
            ShoppingCart.user_id == user_id).delete()

    def delete_product(self, user_id, product_id):
        # deleting a single occurrence of a product (there can be multiple)
        product = self.session.query(ShoppingCart).filter(ShoppingCart.user_id == user_id).filter(
            ShoppingCart.product_id == product_id).first()
        if product:
            return self.session.query(ShoppingCart).filter(ShoppingCart.id == product.id).delete()

        return 0
