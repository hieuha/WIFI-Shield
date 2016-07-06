from flask import Blueprint, jsonify, request
from app.mod_vpn.models import VPN
mod_vpn = Blueprint('vpn', __name__, url_prefix='/vpn')
vpn = VPN()


@mod_vpn.route("/list", methods=["GET"])
def list_vpn():
    response = {"list": list()}
    vpns = vpn.get_list()
    response["list"] = vpns
    return jsonify(response)


@mod_vpn.route("/external_ip", methods=["GET"])
def external_ip():
    ip = vpn.external_ip()
    return jsonify({"ip": ip})


@mod_vpn.route("/connect", methods=["POST"])
def connect():
    vpn_name = request.form.get("vpn")
    response = vpn.connect(vpn_name)
    return jsonify(response)