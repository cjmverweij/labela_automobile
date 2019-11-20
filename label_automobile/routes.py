def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)

    # user routes
    config.add_route('user.list', '/user', request_method="GET")
    config.add_route('user.find_by_email', '/user/email', request_method="GET")

    # product routes
    config.add_route('product.list', '/product', request_method="GET")
    config.add_route('product.get_by_id', '/product/{id}', request_method="GET")

    # shopping cart routes
    config.add_route('shopping_cart.add_products', '/shopping_cart', request_method="POST")
    config.add_route('shopping_cart.get_by_user_id', '/shopping_cart/{user_id}', request_method="GET")
    config.add_route('shopping_cart.delete', '/shopping_cart/{user_id}', request_method="DELETE")
    config.add_route('shopping_cart.delete_products', '/shopping_cart/{user_id}/products', request_method="DELETE")

    # order routes
    config.add_route('order.list', '/order', request_method="GET")
    config.add_route('order.add_order', '/order', request_method="POST")
    config.add_route('order.find_by_user_id', '/order/user', request_method="GET")
    config.add_route('order.get_by_id', '/order/{id}', request_method="GET")
    config.add_route('order.delete_order', '/order/{id}', request_method="DELETE")
