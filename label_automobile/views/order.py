from pyramid.view import view_defaults, view_config
from pyramid.httpexceptions import HTTPBadRequest, HTTPNotFound
from sqlalchemy.orm.exc import NoResultFound

from label_automobile.services.order import OrderService

@view_defaults(renderer='json')
class OrderView:
    def __init__(self, request):
        self.request = request
        self.service = OrderService(request.dbsession)

    @view_config(route_name='order.list')
    def list(self):
        order_list = self.service.list()

        return [{
            'order_id': str(order.id),
            'user_id': str(order.user_id),
            'delivery date': order.delivery_date.strftime('%d/%m/%Y')
        } for order in order_list]

    @view_config(route_name='order.get_by_id')
    def get_by_id(self):
        id = self.request.matchdict['id']
        order = self.service.get_by_id(id)

        return {
            'id': str(order.id),
            'user_id': str(order.user_id),
            'delivery_date': order.delivery_date.strftime('%d/%m/%Y'),
            'products': [
                {
                    'product': item.product.title,
                    'quantity': item.quantity
                } for item in order.items
            ]
        }

    @view_config(route_name='order.find_by_user_id')
    def find_by_user_id(self):

        user_id = self.request.params.get('user_id', None)
        order_list = self.service.find_by_user_id(user_id)

        return [{
            'order_id': str(order.id),
            'delivery date': order.delivery_date.strftime('%d/%m/%Y')
        } for order in order_list]

    @view_config(route_name='order.add_order')
    def add_order(self):
        request_data = self.request.json_body

        try:
            order_id = self.service.add_order(user_id=request_data['user_id'],
                             delivery_date=request_data['delivery_date'])
        except KeyError as e:
            raise HTTPBadRequest(
                json_body={
                    'error': e.args
                })

        self.request.response.status = '201 Created'

        return {
            'order_id': str(order_id)
        }

    @view_config(route_name='order.delete_order')
    def delete_order(self):
        id = self.request.matchdict['id']

        try:
            self.service.delete_order(id)
        except NoResultFound as e:
            raise HTTPNotFound(
                json_body={
                    'error': 'The resource could not be found.'
                })

        return {}