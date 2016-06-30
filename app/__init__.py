from flask import Flask, render_template
from app.mod_wifi.controllers import mod_wifi as wifi_module
from app.mod_dashboard.controllers import mod_dashboard as dashboard_module


app = Flask(__name__)
app.config.from_pyfile("../config.cfg")


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


app.register_blueprint(wifi_module)
app.register_blueprint(dashboard_module)