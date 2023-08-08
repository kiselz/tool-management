from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, request, jsonify
)
import database.db as db_methods

from sqlite3 import IntegrityError

api_bp = Blueprint('api', __name__, url_prefix='/api')

@api_bp.route('user/take_tool', methods=['POST'])
def take_tool():
    if request.method == 'POST':
        db = db_methods.get_db()
        # how many the user currently have
        current_ammount = db_methods.get_user_tool_ammount(db, request.json['firstname'], request.json['toolname'])
        print(current_ammount)
        # how many should be after taking
        new_ammount = current_ammount + request.json['ammount']
        db_methods.assign_tool_to_user(db, request.json['firstname'], request.json['toolname'], new_ammount)
        return jsonify(
            {
                "status": "ok",
                "message": "The tool was successfully taken"
            }
        )

@api_bp.route('user/return_tool', methods=['POST'])
def return_tool():
    if request.method == 'POST':
        db = db_methods.get_db()

        # how many the user currently have
        current_ammount = db_methods.get_user_tool_ammount(db, request.json['firstname'], request.json['toolname'])
        # how many should be after returning
        new_ammount = current_ammount - request.json['ammount']
        db_methods.assign_tool_to_user(db, request.json['firstname'], request.json['toolname'], new_ammount)
        return jsonify(
            {
                "status": "ok",
                "message": "The tool was successfully returned"
            }
        )

@api_bp.route('user/add', methods=["POST"])
def add_user():
    if request.method == "POST":
        db = db_methods.get_db()

        try:
            db_methods.add_user(db, request.json['firstname'], False)
            return jsonify(
                {
                    "status": "ok",
                    "message": "The user was created",
                }
            )
        except IntegrityError as error:
            return jsonify(
                {
                    "status": "error",
                    "message": str(error),
                }
            )

@api_bp.route('user/delete', methods=["POST"])
def delete_user():
    if request.method == 'POST':
        db = db_methods.get_db()

        db_methods.delete_user(db, request.json['firstname'])
        return jsonify(
            {
                "status": "ok",
                "message": "The user was deleted"
            }
        )
    
@api_bp.route('user/tool_ammount', methods=["POST"])
def change_tool_ammount():
    if request.method == 'POST':
        db = db_methods.get_db()

        db_methods.assign_tool_to_user(db, request.json['firstname'], request.json['toolname'], request.json['ammount'])
        return jsonify(
            {
                "status": "ok",
                "message": "The tool ammount was changed"
            }
        )

@api_bp.route('tool/add', methods=['POST'])
def add_tool():
    if request.method == 'POST':
        db = db_methods.get_db()

        try:
            db_methods.add_tool(db, request.json['toolname'])
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
        db = db_methods.get_db()

        db_methods.delete_tool(db, request.json['toolname'])
        return jsonify(
            {
                "status": "ok",
                "message": "The tool was deleted"
            }
        )