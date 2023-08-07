from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, request, jsonify
)
from database.db import (
    get_db, is_user_admin, get_available_ammount, assign_tool_to_user, get_user_tool_ammount, add_tool as add_new_tool,
    delete_tool as del_tool
)

from sqlite3 import IntegrityError

api_bp = Blueprint('api', __name__, url_prefix='/api')

@api_bp.route('user/take_tool', methods=['POST'])
def take_tool():
    if request.method == 'POST':
        db = get_db()
        # how many the user currently have
        current_ammount = get_user_tool_ammount(db, request.json['firstname'], request.json['toolname'])
        print(current_ammount)
        # how many should be after taking
        new_ammount = current_ammount + request.json['ammount']
        assign_tool_to_user(db, request.json['firstname'], request.json['toolname'], new_ammount)
        return str('true')

@api_bp.route('user/return_tool', methods=['POST'])
def return_tool():
    if request.method == 'POST':
        db = get_db()

        # how many the user currently have
        current_ammount = get_user_tool_ammount(db, request.json['firstname'], request.json['toolname'])
        # how many should be after returning
        new_ammount = current_ammount - request.json['ammount']
        assign_tool_to_user(db, request.json['firstname'], request.json['toolname'], new_ammount)
        return str('true')

@api_bp.route('tool/add', methods=['POST'])
def add_tool():
    if request.method == 'POST':
        db = get_db()

        try:
            add_new_tool(db, request.json['toolname'], 999)
        except IntegrityError as error:
            return jsonify(
                {
                    "status": "error",
                    "message": str(error),
                }
            )
        
        return jsonify(
            {
                "status": "ok",
                "message": "The tool was created"
            }
        )

@api_bp.route('tool/delete', methods=['POST'])
def delete_tool():
    if request.method == 'POST':
        db = get_db()

        del_tool(db, request.json['toolname'])
        return jsonify(
            {
                "status": "ok",
                "message": "The tool was deleted"
            }
        )
        


@api_bp.route('tool/get_available', methods=['POST'])
def get_available() -> str:
    if request.method == 'POST':
        db = get_db()
        available_ammount = get_available_ammount(db, request.json['toolname'])
        return str(available_ammount)

