# -*- coding: utf-8 -*-
from flask import Flask, jsonify, render_template
import csv,json

api = Flask(__name__)

@api.route("/")
def tv_news():
          
        """dictionnaire = {
              'type': 'Prévision de température',
                'valeurs': [24, 24, 25, 26, 27, 28],
                'unite': "degrés Celcius"
        }
        return jsonify(dictionnaire)
        """
        #return render_template("API.html")
        tvjson = json.dumps(list(csv.reader(open("drought-tv-news.csv"))))
        return (jsonify(tvjson))
        

if __name__ == "__main__":
    api.run(debug=True)