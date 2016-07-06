from flask import Blueprint, request, render_template, jsonify, redirect, url_for
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
    message = ""
    error = False
    if request.method == "POST":
        form = request.form
        ssid = form["ssid"]
        password = form["password"]
        wifi.ssid = ssid
        wifi.password = password
        message, error = wifi.connect()
        if not error:
            return redirect(url_for('dashboard.index'))
        return render_template("wifi/connect.html", message=message, error=error)
    return render_template("wifi/connect.html", message=message, error=error)
