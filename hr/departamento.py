from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
from hr.db import get_db

bp = Blueprint('departamento', __name__, url_prefix='/departamentos')

@bp.route('/')
def index():
    db = get_db()
    lista_departamentos = db.execute(
        """SELECT department_name FROM departments"""
    ).fetchall()
    return render_template('departamento.html', de=lista_departamentos)