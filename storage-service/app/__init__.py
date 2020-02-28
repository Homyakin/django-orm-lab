from flask import Flask
from flask_orator import Orator

app = Flask(__name__)
app.config['ORATOR_DATABASES'] = {
    'development': {
        'driver': 'mysql',
        'host': 'localhost',
        'database': 'storage',
        'user': 'root',
        'password': '12345'
    }
}

db = Orator(app)
