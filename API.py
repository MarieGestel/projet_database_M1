# -*- coding: utf-8 -*-
from flask import Flask, jsonify, render_template
from csv import DictReader

api = Flask(__name__)

@api.route("/")

class Tv_news :
      def tv_news():
            with open("drought-tv-news.csv", 'r') as f:
                  dict_reader = DictReader(f)
                  list_of_dict = list(dict_reader)
            return (jsonify(list_of_dict))
             
        #return render_template("API.html")
        

if __name__ == "__main__":
    api.run(debug=True)