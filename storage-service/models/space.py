from app import db


class Space(db.Model):
    __table__ = 'client'
    __fillable__ = ['name', 'useful_volume', 'temperature', 'humidity']
    __timestamps__ = False
