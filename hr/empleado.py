from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
from hr.db import get_db

bp = Blueprint('empleado', __name__, url_prefix='/empleados')

@bp.route('/')
def index():
    db = get_db()
    lista_empleados = db.execute(
        """SELECT first_name FROM employees"""
    ).fetchall()
    return render_template('empleado.html', em=lista_empleados)