# -*- coding: utf-8 -*-
from flask import Flask, render_template

api = Flask(__name__)

@api.route("/")
def hello():
        return render_template("API.html")

if __name__ == "__main__":
    api.run(debug=True)