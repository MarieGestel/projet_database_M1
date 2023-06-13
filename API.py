# -*- coding: utf-8 -*-
from flask import Flask, jsonify, render_template
from csv import DictReader
#pip install Flask SQLAlchemy psycopg2
from flask_sqlalchemy import SQLAlchemy
import csv
from flask import request
import psycopg2

      #POSTGRES_USER: user
      #POSTGRES_DB: databasetvnews
      #POSTGRES_PASSWORD: password
from flask_migrate import Migrate




api = Flask(__name__)
#app = Flask(__name__)
api.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:misterbauer@postgres:5432/mydb'
db = SQLAlchemy(api)
migrate = Migrate(api, db)


class News(db.Model):
    __tablename__ = "tv_news"
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(120), unique=False, nullable=False)
    title = db.Column(db.String(120), unique=False, nullable=False)
    url = db.Column(db.String(500), unique=False, nullable=False)
    media = db.Column(db.String(50), unique=False, nullable=False)


    
    #def __repr__(self):
     # return '<User %r>' % self.username

      


@api.route('/sauvegarder_csv', methods=['POST'])
def sauvegarder_csv():
    fichier = request.files['drought-tv-news.csv']

    if fichier:
        donnees = fichier.read().decode('utf-8')
        lignes = csv.reader(donnees.splitlines(), delimiter=',')


        for ligne in lignes:
            nouvel_utilisateur = News(date=ligne[0], title=ligne[1], url=ligne[2], media=ligne[3])
            db.session.add(nouvel_utilisateur)


      
        db.session.commit()

        return 'Données CSV sauvegardées avec succès'
    else:
        return 'Aucun fichier CSV n\'a été envoyé'

#curl -X POST -F "drought-tv-news.csv" http://localhost:8080/sauvegarder_csv

    

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


#---


""" @api.route("/")
def tv_news():
      with open("drought-tv-news.csv", 'r') as f:
           dict_reader = DictReader(f)
           list_of_dict = list(dict_reader)
      return (jsonify(list_of_dict))
             
        #return render_template("API.html")
 """
#--- 


if __name__ == "__main__":
    api.cli.add_command(db.init_app(api))
    api.cli.add_command(db)
    api.run(debug=True, port=8080)

#if __name__ == "__main__":
    #api.run(debug=True)
 #   api.run(debug=True, port=8080)



####
