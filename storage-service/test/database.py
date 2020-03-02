import datetime

from models.orator_models import Client, Contract

if __name__ == '__main__':
    client = Client.create(name='testName', bank_details='testDetails')
    contract = Contract.create(end_date=datetime.datetime.now(), client_id=client.id)
    print(client.to_dict())
    print(contract.to_dict())
    find_client = Contract.where('number', '=', contract.number).get()[0].client
    print(find_client.to_dict())
    find_contract = client.contract
    print(find_contract[0].to_dict())
