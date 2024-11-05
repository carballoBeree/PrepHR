from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
from hr.db import get_db

bp = Blueprint('trabajo', __name__, url_prefix='/trabajos')

@bp.route('/')
def index():
    db = get_db()
    lista_trabajos = db.execute(
        """SELECT job_title FROM jobs"""
    ).fetchall()
    return render_template('trabajo.html', tr=lista_trabajos)