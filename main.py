from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup


app = Flask(__name__)


@app.route("/")
def hero():
    return render_template("hero.html")


if __name__ == '__main__':
    app.run()
