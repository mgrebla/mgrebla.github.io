import pathlib
from flask import Flask, render_template

DIR = pathlib.Path(__file__).parent

app = Flask(__name__, template_folder=DIR, static_folder=DIR, static_url_path='/')


@app.route('/')
def hello():
    return render_template('index.html')