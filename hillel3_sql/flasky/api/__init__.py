from flask import Blueprint
from flasky.db import get_db

api = Blueprint('api', __name__)
tracks_api = Blueprint('tracks', __name__)


from . import customers, tracks
