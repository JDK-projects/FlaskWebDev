from datetime import datetime

from flask import (
    Flask,
    flash,
    make_response,
    redirect,
    render_template,
    request,
    session,
    url_for,
)
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

import debugger

debugger.initializeFlaskServiceDebuggerIfNeeded()

app = Flask(__name__)
app.config["SECRET_KEY"] = "adfhasdjkhfasdjkfhasdl"
bootstrap = Bootstrap(app)
moment = Moment(app)


class NameForm(FlaskForm):
    name = StringField("What is your name?", validators=[DataRequired()])
    submit = SubmitField("Submit")


@app.route("/", methods=["GET", "POST"])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get("name")
        if old_name is not None and old_name != form.name.data:
            flash("Looks like you have changed your name!")
        session["name"] = form.name.data
        return redirect(url_for("index"))
    return render_template(
        "index.html",
        form=form,
        name=session.get("name"),
        current_time=datetime.utcnow(),
    )

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
    return render_template("404.html"), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html"), 500
