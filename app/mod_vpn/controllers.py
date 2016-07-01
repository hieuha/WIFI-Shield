from flask import Blueprint, render_template

mod_vpn = Blueprint('vpn', __name__, url_prefix='/vpn')