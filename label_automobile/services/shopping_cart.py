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
        """
        get the shopping cart for a specific user
        :param user_id: str
        :return: list shopping cart items
        """
        return self._repository.get_by_user_id(user_id)

    def delete(self, user_id):
        """
        deletes (empties) the shopping cart of a specific user
        :param user_id: str
        :return: int number of deleted items
        """
        return self._repository.delete(user_id)

    def delete_products(self, user_id, products):
        """
        deletes items from a specific users shopping cart
        :param user_id: str
        :param products: list of products
        :return: int number of deleted items
        """
        deleted = 0
        for product in products: deleted += self._repository.delete_product(user_id, product)

        return deleted

