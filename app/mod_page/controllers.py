from flask import Blueprint, render_template

mod_page = Blueprint('page', __name__, url_prefix='/')


@mod_page.route("/", methods=["GET"])
def index():
    return render_template("home/index.html")


@mod_page.route("/how-it-works", methods=["GET"])
def how():
    return render_template("home/how.html")