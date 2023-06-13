# -*- coding: utf-8 -*-
from flask import Flask, jsonify, render_template
from csv import DictReader
#pip install Flask SQLAlchemy psycopg2
from flask_sqlalchemy import SQLAlchemy
import csv
from flask import request
import psycopg2
from flask_migrate import Migrate



api = Flask(__name__)
#app = Flask(__name__)
api.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:misterbauer@postgres:5432/mydb'
db = SQLAlchemy(api)
migrate = Migrate(api, db)


class News(db.Model):
    __tablename__ = "tv_news"
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DATETIME(50), unique=False, nullable=False)
    title = db.Column(db.String(120), unique=False, nullable=False)
    url = db.Column(db.String(500), unique=False, nullable=False)
    media = db.Column(db.String(50), unique=False, nullable=False)


# Pour lire les données depuis une BDD à l'aide d'un API

@api.route('/', methods=['GET'])
def obtenir_utilisateurs():
    news = News.query.all()
    result = []
    for info in news:
        result.append({
            'date': info.date,
            'title': info.title,
            'url': info.url,
            'media': info.media
        })
    return (jsonify(result))
      
def calculate(a,b):
      a = 1
      b = 2
      count = a + b
      return count

#def count_tf1

if __name__ == "__main__":
    api.cli.add_command(db.init_app(api))
    api.cli.add_command(db)
    api.run(debug=True, port=8080)

