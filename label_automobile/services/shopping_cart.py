from label_automobile.repositories.shopping_cart import ShoppingCartRepository

class ShoppingCartService:
    def __init__(self, session):
        self._repository = ShoppingCartRepository(session)
        self.session = session

    def add_products(self, user_id, products: list):
        """
        adds a product to a users shopping cart
        :param user_id: str id of the user
        :param product_id: list of id's of the products to add
        :return: ShoppingCart - the updated shopping cart
        """
        for product in products: self._repository.add_product(user_id, product)
        return self._repository.get_by_user_id(user_id)

    def get_by_user_id(self, user_id):
        return self._repository.get_by_user_id(user_id)

    def delete(self, user_id):
        return self._repository.delete(user_id)

    def delete_products(self, user_id, products):
        deleted = 0
        for product in products: deleted += self._repository.delete_product(user_id, product)

        return deleted

