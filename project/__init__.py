import os
from flask import Flask
from urllib.parse import quote
import cloudinary
from flask_login import LoginManager
from flask_babelex import Babel
from flask_sqlalchemy import SQLAlchemy
import pathlib
from google_auth_oauthlib.flow import Flow
from dotenv import load_dotenv
from flask_moment import Moment
import cloudinary.uploader
load_dotenv()

app = Flask(__name__)

# Đặt secret key
app.secret_key = '32121asdf1@$!2ed32SF12563R23ASDF'

moment = Moment(app)

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:%s@localhost/quanlychuyenbay?charset=utf8mb4" % quote("Aylatoi2011vn")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app=app)

login = LoginManager(app=app)

cloudinary.config(cloud_name='dba0vclo4',
                  api_key='997854835189435',
                  api_secret='nUIvQ-KNibg2BOa6nqIyc44jHko')

# oauth google login
client_secrets_file = os.path.join(pathlib.Path(__file__).parent.parent, "oauth_config.json")
flow = Flow.from_client_secrets_file(
    client_secrets_file=client_secrets_file,
    scopes=["https://www.googleapis.com/auth/userinfo.profile", "https://www.googleapis.com/auth/userinfo.email",
            "openid"],
    redirect_uri="http://localhost:5001/callback"
)


babel = Babel(app=app)


@babel.localeselector
def load_locale():
    return 'vi'