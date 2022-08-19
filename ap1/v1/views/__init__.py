from flask import Blueprint

app_views = Blueprint('app_views', __name__)

from views.status import *
from views.request import *
