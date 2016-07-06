from flask import Blueprint, request, render_template, jsonify, redirect, url_for
from app.mod_device.models import Device

mod_device = Blueprint('device', __name__, url_prefix='/device')
device = Device()

@mod_device.route('/interfaces', methods=["GET"])
def interfaces():
    ifcfg = device.interfaces()
    if ifcfg is not None:
        return jsonify(ifcfg)

@mod_device.route("/connection", methods=["GET"])
def connection():
    is_online = device.check_internet()
    message = {"message": None, "status": False}
    if is_online:
        message["message"] = "You are connected to the internet!"
    else:
        message["message"] = "You are offline!"
    message["active"] = is_online
    return jsonify(message)
