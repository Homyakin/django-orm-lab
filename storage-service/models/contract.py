from app import db


class Contract(db.Model):
    __table__ = 'contract'
    __fillable__ = ['number', 'end_date', 'client_id']
    __timestamps__ = False
