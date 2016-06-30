from flask import Blueprint, request, render_template, jsonify
from app.mod_dashboard.models import Dashboard

mod_dashboard = Blueprint('dashboard', __name__, url_prefix='/dashboard')
dashboard = Dashboard()
