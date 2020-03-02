from app import db


class Rack(db.Model):
    __table__ = 'client'
    __fillable__ = ['space_id', 'capacity', 'height', 'width', 'length', 'max_weight']
    __timestamps__ = False
