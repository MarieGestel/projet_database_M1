# -*- coding: utf-8 -*-
from flask import Flask, jsonify, render_template

api = Flask(__name__)

@api.route("/")
def tv_news():
        dictionnaire = {
              'type': 'Prévision de température',
                'valeurs': [24, 24, 25, 26, 27, 28],
                'unite': "degrés Celcius"
        }
        return jsonify(dictionnaire)
        #return render_template("API.html")

if __name__ == "__main__":
    api.run(debug=True)