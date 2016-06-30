from flask import Flask, render_template

app = Flask(__name__)
app.config.from_pyfile("../config.cfg")

from app.mod_page.controllers import mod_page as page_module
from app.mod_wifi.controllers import mod_wifi as wifi_module
from app.mod_dashboard.controllers import mod_dashboard as dashboard_module
from app.mod_device.controllers import mod_device as device_module


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

app.register_blueprint(page_module)
app.register_blueprint(wifi_module)
app.register_blueprint(dashboard_module)
app.register_blueprint(device_module)
