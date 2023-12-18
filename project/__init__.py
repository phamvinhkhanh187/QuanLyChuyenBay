from flask import Flask
from urllib.parse import quote
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.secret_key = 'abdskfhb2!@@$^!@#$!@^135'
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:%s@localhost/quanlychuyenbay?charset=utf8mb4" % quote("12345")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app=app)


