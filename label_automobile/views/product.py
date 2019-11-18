from pyramid.view import view_defaults, view_config

from label_automobile.models.product import Product
from label_automobile.services.product import ProductService

@view_defaults(renderer='json')
class InventoryView:
    def __init__(self, request):
        self.request = request
        self.service = ProductService(request.dbsession)

    @view_config(route_name='product.list')
    def list(self):
        products = self.service.list()

        return [{
            "id": str(product.id),
            "title": product.title,
            "description": product.description,
            "price": product.price,
            "reference number": product.ref_number
        } for product in products]

    @view_config(route_name='product.get_by_id')
    def item(self):
        id = self.request.matchdict["id"]
        product = self.service.get_by_id(id)

        return {
            "title": product.title,
            "description": product.description,
            "price": product.price,
            "reference number": product.ref_number
        }