from flask import Blueprint

main = Blueprint('main', __name__)

# import here to avoid errors with circular imports
from . import views, errors
