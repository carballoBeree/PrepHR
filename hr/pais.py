from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
from hr.db import get_db

bp = Blueprint('pais', __name__, url_prefix='/paises')

@bp.route('/')
def index():
    db = get_db()
    lista_paises = db.execute(
        """SELECT country_name from countries"""
    ).fetchall()
    return render_template('pais.html', pa=lista_paises)