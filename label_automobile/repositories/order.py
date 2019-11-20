from datetime import datetime

from label_automobile.models.order import Order
from label_automobile.models.order_item import OrderItem

class OrderRepository:
    def __init__(self, session):
        self.session = session

    def list(self):
        return self.session.query(Order).all()

    def get_by_id(self, id):
        return self.session.query(Order).filter(
            Order.id == id).one()

    def find_by_user_id(self, user_id):
        return self.session.query(Order).filter(
            Order.user_id == user_id).all()

    def add_order(self, user_id, delivery_date, shopping_cart):
        """
        prepares the shopping cart items and adds them to the database

        :param user_id: str
        :param delivery_date: str 'dd/mm/yy'
        :param shopping_cart: list of ShoppingCart items
        :return: UUID order_id
        """

        # convert the shopping_cart, which is a list of shopping_cart objects with each
        # one (possibly duplicate) product, to a dictionary where the amount of each
        # product is counted.
        products = [item.product for item in shopping_cart]
        products_counted = {
            product: products.count(product) for product in products
        }

        # prepare a list of the order items to be passed to the order on creation
        order_items = [
            OrderItem(
                product_id=product.id,
                quantity=amount
            ) for product, amount in products_counted.items()
        ]

        # parse string to datetime object
        parsed_date = datetime.strptime(delivery_date, '%d/%m/%y')
        order = Order(
            user_id=user_id,
            delivery_date=parsed_date,
            items=order_items
        )
        # add the new order
        self.session.add(order)
        self.session.flush()

        return order.id

    def delete_order(self, order_id):
        order = self.session.query(Order).filter(Order.id == order_id).one()
        self.session.delete(order)