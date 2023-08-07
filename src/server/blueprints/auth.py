from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, request
)
from database.db import get_db, is_user_admin

auth_bp = Blueprint('login', __name__, url_prefix='/auth')

@auth_bp.route('login', methods=['POST'])
def login():
    if request.method == 'POST':
        db = get_db()
        user = request.form['firstname']
        is_admin = is_user_admin(db, user)

        session['user'] = user
        session['is_admin'] = is_admin
        return redirect('/menu')

@auth_bp.route('logout', methods=['GET'])
def logout():
    session.pop('user')
    session.pop('is_admin')
    return redirect('/')