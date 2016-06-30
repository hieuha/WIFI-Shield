from flask import Blueprint, request, render_template, jsonify
from app.mod_wifi.models import Wifi

mod_wifi = Blueprint('wifi', __name__, url_prefix='/wifi')
wifi = Wifi()


@mod_wifi.route("/scan", methods=["GET"])
def scan():
    networks = wifi.scan()
    if networks is not None:
        return jsonify(networks)


@mod_wifi.route('/connect', methods=['GET', 'POST'])
def connect():
    networks = wifi.networks
    # networks = wifi.scan()
    message = networks["message"]
    error = networks["error"]
    if request.method == "POST":
        form = request.form
        ssid = form["ssid"]
        password = form["password"]
        wifi.ssid = ssid
        wifi.password = password
        message, error = wifi.connect()
    return render_template("wifi/connect.html",
                           networks=networks,
                           message=message,
                           error=error)
