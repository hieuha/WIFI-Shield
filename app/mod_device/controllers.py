from flask import Blueprint, request, render_template, jsonify, redirect, url_for
from app.mod_device.models import Device

mod_device = Blueprint('device', __name__, url_prefix='/device')
device = Device()


@mod_device.route('/interfaces', methods=["GET"])
def interfaces():
    ifcfg = device.interfaces()
    if ifcfg is not None:
        return jsonify(ifcfg)