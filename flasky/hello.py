from datetime import datetime

from flask import Flask, make_response, render_template, request
from flask_bootstrap import Bootstrap
from flask_moment import Moment

import debugger

debugger.initializeFlaskServiceDebuggerIfNeeded()

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route("/")
def index():
    return render_template("index.html", current_time=datetime.utcnow())

    # response = make_response('<h1>This document carries a cookie!</h1>')
    # response.set_cookie(42)
    # return response
    # userAgent = request.headers.get('User-Agent')
    # return f'<p>Your browser is {userAgent}</p>'


@app.route("/user/<name>")
def user(name):
    return render_template("user.html", name=name)
    # return f'<h1>Hello, {name}!</h1>'

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
