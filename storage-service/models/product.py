from app import db


class Product(db.Model):
    __table__ = 'product'
    __fillable__ = ['height', 'width', 'length', 'weight', 'date_of_receipt', 'min_temperature', 'max_temperature',
                    'min_humidity', 'max_humidity', 'contract_number']
    __timestamps__ = False
