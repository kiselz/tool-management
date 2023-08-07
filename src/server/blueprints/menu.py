from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, request
)
from database.db import get_db, get_user_tools, get_users, get_tools, get_available_tools

menu_bp = Blueprint('menu', __name__, url_prefix='/menu')

@menu_bp.route('/', methods=['GET'])
def show_menu():
    user = session['user']
    is_admin = session['is_admin']
    return render_template('menu/main.html', user=user, is_admin=is_admin)

@menu_bp.route('/overview', methods=['GET'])
def show_overview():
    current_user = session['user']
    is_admin = session['is_admin']
    
    db = get_db()
    users = get_users(db)
    tools = get_tools(db)

    # get for every user their tools
    users_tools = {}
    for user in users:
        users_tools[user['firstname']] = get_user_tools(db, user['firstname'])
    return render_template('menu/overview.html', 
                           current_user=current_user, users=users, tools=tools, is_admin=is_admin, users_tools=users_tools
                           )

@menu_bp.route('/my_tools', methods=['GET'])
def show_my_tools():
    current_user = session['user']
    is_admin = session['is_admin']

    db = get_db()
    user_tools = get_user_tools(db, current_user)
    available_tools = get_available_tools(db)

    return render_template('menu/my_tools.html',
                            current_user=current_user,
                            user_tools=user_tools,
                            available_tools=available_tools,
                           )