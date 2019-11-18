from label_automobile.repositories.product import ProductRepository

class ProductService:
    def __init__(self, session):
        self._repository = ProductRepository(session)

    def list(self):
        """
        returns all products
        :return: list of products
        """
        return self._repository.list()

    def get_by_id(self, id):
        """
        gets a product by id
        :param id: str product id
        :return: Product
        """
        return self._repository.get_by_id(id)
