from flask import Blueprint, request, render_template, jsonify
from app.mod_dashboard.models import Dashboard
from app.mod_device.models import Device
from app.mod_vpn.models import VPN

mod_dashboard = Blueprint('dashboard', __name__, url_prefix='/dashboard')
dashboard = Dashboard()
device = Device()
vpn = VPN()


@mod_dashboard.route("/", methods=["GET"])
def index():
    interfaces = device.interfaces()
    vpns = vpn.get_list()
    return render_template("dashboard/status.html", interfaces=interfaces, vpns=vpns)