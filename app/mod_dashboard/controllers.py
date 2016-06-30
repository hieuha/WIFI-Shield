from flask import Blueprint, request, render_template, jsonify
from app.mod_dashboard.models import Dashboard
from app.mod_device.models import Device

mod_dashboard = Blueprint('dashboard', __name__, url_prefix='/dashboard')
dashboard = Dashboard()
device = Device()


@mod_dashboard.route("/", methods=["GET"])
def index():
    interfaces = device.interfaces()
    return render_template("dashboard/status.html",
                           interfaces=interfaces)