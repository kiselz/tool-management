from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, request
)

auth_bp = Blueprint('login', __name__, url_prefix='/auth')

@auth_bp.route('login', methods=['POST'])
def login():
    if request.method == 'POST':
        user = request.form['firstname']
        session['user'] = user
        return redirect('/')

@auth_bp.route('logout', methods=['GET'])
def logout():
    session.pop('user')
    return redirect('/')