from pyramid.httpexceptions import HTTPNotFound

from label_automobile.repositories.order import OrderRepository
from label_automobile.repositories.shopping_cart import ShoppingCartRepository

class OrderService:
    def __init__(self, session):
        self._repository = OrderRepository(session)
        self.session = session

    def list(self):
        """
        returns all orders
        :return: list of orders
        """
        return self._repository.list()

    def get_by_id(self, id):
        """
        gets an order by id
        :param id: str order id
        :return: Order
        """
        return self._repository.get_by_id(id)

    def find_by_user_id(self, user_id):
        """
        gets all orders of a specific user
        :param user_id: str
        :return: list of orders
        """
        return self._repository.find_by_user_id(user_id)

    def add_order(self, user_id, delivery_date):
        """
        creates an order from a specific users shopping cart and then deletes (empties) the
        respective shopping cart
        :param user_id: str
        :param delivery_date: str
        :return: UUID order_id
        """
        shopping_cart_repository = ShoppingCartRepository(self.session)
        shopping_cart = shopping_cart_repository.get_by_user_id(user_id)

        if not shopping_cart:
            raise HTTPNotFound(
                json_body={
                    'error': 'the shopping cart for this user could not be found.'
                })

        order_id = self._repository.add_order(
            user_id=user_id,
            delivery_date=delivery_date,
            shopping_cart=shopping_cart)

        shopping_cart_repository.delete(user_id)

        return order_id

    def delete_order(self, order_id):
        """
        deletes a specific order
        :param order_id: str
        :return:
        """
        self._repository.delete_order(order_id)
