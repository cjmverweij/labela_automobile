def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)

    # user routes
    config.add_route('user.list', '/user', request_method="GET")
    config.add_route('user.find_by_email', '/user/email', request_method="GET")

    # product routes
    config.add_route('product.list', '/inventory', request_method="GET")
    config.add_route('product.get_by_id', '/inventory/{id}', request_method="GET")

