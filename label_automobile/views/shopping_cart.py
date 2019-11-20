from pyramid.view import view_defaults, view_config
from pyramid.httpexceptions import HTTPBadRequest, HTTPNotFound
from label_automobile.services.shopping_cart import ShoppingCartService

@view_defaults(renderer='json')
class ShoppingCartView:
    def __init__(self, request):
        self.request = request
        self.service = ShoppingCartService(request.dbsession)

    @view_config(route_name='shopping_cart.add_products')
    def add_products(self):
        request_data = self.request.json_body

        try:
            shopping_cart = self.service.add_products(user_id=request_data['user_id'],
                             products=request_data['products'])
        except KeyError as e:
            raise HTTPBadRequest(
                json_body={
                    'error': e.args
                })

        self.request.response.status = '201 Created'

        return {
            'shopping_cart': {
                'user_id': shopping_cart[0].user_id,
                'products': [
                    {
                        'id': str(item.product.id),
                        'title': item.product.title
                    } for item in shopping_cart
                ]
            }
        }

    @view_config(route_name='shopping_cart.get_by_user_id')
    def get_by_user_id(self):
        user_id = self.request.matchdict['user_id']
        shopping_cart = self.service.get_by_user_id(user_id)

        if not shopping_cart:
            raise HTTPNotFound(
                json_body={
                    'error': 'The resource could not be found.'
                })

        return {
            'shopping_cart': {
                'user_id': shopping_cart[0].user_id,
                'products': [
                    {
                        'id': str(item.product.id),
                        'title': item.product.title
                    } for item in shopping_cart
                ]
            }
        }

    @view_config(route_name='shopping_cart.delete')
    def delete(self):
        user_id = self.request.matchdict['user_id']
        self.service.delete(user_id)

        return {}

    @view_config(route_name='shopping_cart.delete_products')
    def delete_products(self):
        user_id = self.request.matchdict['user_id']
        request_data = self.request.json_body

        try:
            deleted = self.service.delete_products(user_id=user_id,
                             products=request_data['products'])
        except KeyError as e:
            raise HTTPBadRequest(
                json_body={
                    'error': e.args
                })

        return {
            'deleted_items': deleted
        }