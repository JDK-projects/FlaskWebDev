from datetime import datetime
from flask import render_template, session, redirect, url_for
from . import main
from .forms import NameForm
from .. import db
from ..models import User


# the route decorator comes from the blueprint, nolonger app
# @app.route("/", methods=["GET", "POST"])
@main.route("/", methods=["GET", "POST"])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            db.session.commit()
            session["known"] = False
        else:
            session["known"] = True
        session["name"] = form.name.data
        form.name.data = ""

        # flask applies a namespace to all endpoints defined in a blueprint
        # allowing multiple blueprints can define functions the the same endpoint
        # names without collision
        # return redirect(url_for("index"))         # no blueprint
        # return redirect(url_for("main.index"))    # explicit blueprint
        return redirect(url_for(".index"))  # blueprint inferred from request

    return render_template(
        "index.html",
        form=form,
        name=session.get("name"),
        known=session.get("known", False),
        current_time=datetime.utcnow(),
    )