from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
from hr.db import get_db

bp = Blueprint('location', __name__, url_prefix='/locations')

@bp.route('/')
def index():
    db = get_db()
    lista_locations = db.execute(
        """SELECT street_adress FROM locations"""
    ).fetchall()
    return render_template('location.html', lo=lista_locations)