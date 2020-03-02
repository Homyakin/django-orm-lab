from app import db


class Client(db.Model):
    __table__ = 'client'
    __fillable__ = ['name', 'bank_details']
    __timestamps__ = False
