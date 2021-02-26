from flask import render_template
from . import main


# otherwise only handled for main, want app-wide
# @main.errorhandler(404)
@main.app_errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


#otherwise only handled for main, want app-wide
# @main.errorhandler(500)
@main.app_errorhandler(500)
def internal_server_error(e):
    return render_template("500.html"), 500
