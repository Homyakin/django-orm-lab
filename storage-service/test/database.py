import datetime

from models.orator_models import Client, Contract, Product, Space, Rack

if __name__ == '__main__':
    for i in range(2):
        client = Client.create(name=f'testName{i}', bank_details='testDetails')
        contract1 = Contract.create(end_date=datetime.datetime.now(), client_id=client.id)
        contract2 = Contract.create(end_date=datetime.datetime.now(), client_id=client.id)
        print(client.to_dict())
        print(contract1.to_dict())

        # belongs
        find_client = Contract.where('number', '=', contract1.number).get()[0].client
        print(find_client.to_dict())

        # one to many
        find_contract = client.contracts
        for j in find_contract:
            print(j.to_dict())

        space = Space.create(name=f'testSpace{i}', useful_volume=100, temperature=0, humidity=0)
        rack1 = Rack.create(space_id=space.id, capacity=10, height=20, width=10, length=10, max_weight=100)
        rack2 = Rack.create(space_id=space.id, capacity=10, height=20, width=10, length=10, max_weight=100)

        products = []
        for j in range(5):
            products.append(Product.create(height=1, width=1, length=1, weight=1,
                                           date_of_receipt=datetime.date.today(), min_temperature=0, max_temperature=0,
                                           min_humidity=0, max_humidity=0, contract_number=contract1.number,
                                           rack_number=rack1.number, rack_position=j + 1
                                           )
                            )
            products.append(Product.create(height=1, width=1, length=1, weight=1,
                                           date_of_receipt=datetime.date.today(), min_temperature=0, max_temperature=0,
                                           min_humidity=0, max_humidity=0, contract_number=contract2.number,
                                           rack_number=rack2.number, rack_position=j + 1
                                           )
                            )

        find_product = rack1.products
        for j in find_product:
            print(j.to_dict())
