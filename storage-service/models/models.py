from orator.orm import has_many, has_one

from app import db


class Client(db.Model):
    __table__ = 'client'
    __fillable__ = ['name', 'bank_details']
    __timestamps__ = False

    @has_many
    def contract(self):
        return Contract


class Contract(db.Model):
    __table__ = 'contract'
    __fillable__ = ['number', 'end_date', 'client_id']
    __timestamps__ = False

    @has_one
    def client(self):
        return Client

    @has_many
    def product(self):
        return Product


class Product(db.Model):
    __table__ = 'product'
    __fillable__ = ['height', 'width', 'length', 'weight', 'date_of_receipt', 'min_temperature',
                    'max_temperature', 'min_humidity', 'max_humidity', 'contract_number']
    __timestamps__ = False

    @has_one
    def contract(self):
        return Contract


class Rack(db.Model):
    __table__ = 'client'
    __fillable__ = ['space_id', 'capacity', 'height', 'width', 'length', 'max_weight']
    __timestamps__ = False

    @has_one
    def space(self):
        return Space


class Space(db.Model):
    __table__ = 'client'
    __fillable__ = ['name', 'useful_volume', 'temperature', 'humidity']
    __timestamps__ = False

    @has_many
    def rack(self):
        return Rack
