from flask import Flask
from flask import request, url_for, jsonify, jsonify
from flask.templating import render_template
from flask import session
from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, migrate
from sqlalchemy import select
from flask import json


app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
    print("one")
    voltage = 12
    current = 3
    return render_template('rp_website.html', voltage=voltage, current=current)

if __name__ == '__main__':
    app.run()