import json
import os
import sys

import transaction as ts
from pyramid.paster import get_appsettings, setup_logging
from pyramid.scripts.common import parse_vars

from ..models import (Product, User, get_engine, get_session_factory,
                      get_tm_session)
from ..models.meta import Base


def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri> [var=value]\n'
          '(example: "%s development.ini")' % (cmd, cmd))
    sys.exit(1)


def main(argv=sys.argv):
    if len(argv) < 2:
        usage(argv)
    config_uri = argv[1]
    options = parse_vars(argv[2:])
    setup_logging(config_uri)
    settings = get_appsettings(config_uri, options=options)

    engine = get_engine(settings)
    Base.metadata.create_all(engine)
    session_factory = get_session_factory(engine)

    with ts.manager:
        dbsession = get_tm_session(session_factory, ts.manager)

        # create a two users
        create_user(dbsession=dbsession)
        create_user(dbsession,
                    name="Jane",
                    surname="Doe",
                    email="Janedoe@example.com")

        # populate product table with mock data from json file
        with open('mock_inventory.json', 'r') as f:
            product_data = json.load(f)

        for index, part in product_data.items():
            create_product_item(
                dbsession=dbsession,
                title=part['part.title'],
                description=part['part.overview'],
                price=float(part['part.price'][1:]),
                ref_number=part['part.part_number']
            )



def create_product_item(dbsession, title, description, price, ref_number):
    product = Product()
    product.title = title
    product.description = description
    product.price = price
    product.ref_number = ref_number
    dbsession.add(product)


def create_user(dbsession, name="John", surname="doe", email="johndoe@example.com"):
    user = User()
    user.name = name
    user.surname = surname
    user.email = email
    dbsession.add(user)
