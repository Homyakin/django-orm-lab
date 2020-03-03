from models.orator_models import Client, Space, Product


def get_clients_by_name(name):
    return get_clients_by_field('name', name)


def get_clients_by_id(_id):
    return get_clients_by_field('id', _id)


def get_clients_by_field(field, value):
    clients = Client.where(field, '=', value).get()
    list_clients = []
    for i in clients:
        list_clients.append(i.to_dict())
    return list_clients


def get_client_by_product_id(_id):
    product = Product.where('id', '=', _id).get()
    if product.is_empty():
        return []
    return product[0].contract.client.to_dict()


def get_products_by_client_id(_id):
    client = Client.where('id', '=', _id).get()
    if client.is_empty():
        return []
    list_products = []
    contracts = client[0].contracts
    for contract in contracts:
        for j in contract.products:
            list_products.append(j.to_dict())
    return list_products


def get_products_by_space_id(_id):
    space = Space.where('id', '=', _id).get()
    if space.is_empty():
        return []
    list_products = []
    racks = space[0].racks
    for rack in racks:
        for j in rack.products:
            list_products.append(j.to_dict())
    return list_products


def get_products_by_id(_id):
    products = Product.where('id', '=', _id).get()
    list_products = []
    for i in products:
        list_products.append(i.to_dict())
    return list_products
