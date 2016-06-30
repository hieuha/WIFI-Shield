from flask import Blueprint, request, render_template, jsonify
from app.mod_dashboard.models import Dashboard

mod_dashboard = Blueprint('dashboard', __name__, url_prefix='/dashboard')
dashboard = Dashboard()


@mod_dashboard.route("/status", methods=["GET"])
def status():
    return render_template("dashboard/status.html")