from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, request, jsonify
)
import database.db as db_methods

from sqlite3 import IntegrityError
from server.utils import check_json

api_bp = Blueprint('api', __name__, url_prefix='/api')

@api_bp.route('user/take_tool', methods=['POST'])
def take_tool():
    """
    Take tools

    Expected json:
    {
        firstname: Firstname of the user,
        toolname: Tool's name to take,
        ammount: Ammount to take
    }
    """
    if request.method == 'POST':
        js = request.json
        check = check_json(js, 'firstname', 'toolname', 'ammount')
        if type(check) is dict:
            return jsonify(check)
        
        db = db_methods.get_db()
        # how many the user currently have
        current_ammount = db_methods.get_user_tool_ammount(db, js['firstname'], js['toolname'])
        # how many should be after taking
        new_ammount = current_ammount + js['ammount']
        db_methods.assign_tool_to_user(db, js['firstname'], js['toolname'], new_ammount)
        return jsonify(
            {
                "status": "ok",
                "message": "The tool was successfully taken"
            }
        )

@api_bp.route('user/return_tool', methods=['POST'])
def return_tool():
    """
    Return the tool

    Expected json:
    {
        firstname: Firstname of the user
        toolname: Tool's name to return
        ammount: ammount of the tool to return
    }
    """
    if request.method == 'POST':
        js = request.json
        check = check_json(js, 'firstname', 'toolname', 'ammount')
        if type(check) is dict:
            return jsonify(check)

        db = db_methods.get_db()

        # how many the user currently have
        current_ammount = db_methods.get_user_tool_ammount(db, js['firstname'], js['toolname'])
        # how many should be after returning
        new_ammount = max(current_ammount - js['ammount'], 0)
        db_methods.assign_tool_to_user(db, js['firstname'], js['toolname'], new_ammount)
        return jsonify(
            {
                "status": "ok",
                "message": "The tool was successfully returned"
            }
        )

@api_bp.route('user/add', methods=["POST"])
def add_user():
    """
    Add new user to database

    Expected json:
    {
        firstname: the user's firstname
    }
    """
    if request.method == "POST":
        js = request.json
        check = check_json(js, 'firstname')
        if type(check) is dict:
            return jsonify(check)
        
        db = db_methods.get_db()

        try:
            db_methods.add_user(db, js['firstname'], False)
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
    """
    Delete the user

    Expected json:
    {
        firstname: Firstname of the user to delete
    }
    """
    if request.method == 'POST':
        js = request.json
        check = check_json(js, 'firstname')
        if type(check) is dict:
            return jsonify(check)
        
        db = db_methods.get_db()

        db_methods.delete_user(db, js['firstname'])
        return jsonify(
            {
                "status": "ok",
                "message": "The user was deleted"
            }
        )
    
@api_bp.route('user/tool_ammount', methods=["POST"])
def change_tool_ammount():
    """
    Change how many tools are acquired by the user

    Expected json:
    {
        firstname: firstname of the user,
        toolname: tool's name,
        ammount: ammount of the tool,
    }
    """
    if request.method == 'POST':
        js = request.json
        check = check_json(js, 'firstname', 'toolname', 'ammount')
        if type(check) is dict:
            return jsonify(check)
        
        db = db_methods.get_db()

        db_methods.assign_tool_to_user(db, js['firstname'], js['toolname'], js['ammount'])
        return jsonify(
            {
                "status": "ok",
                "message": "The tool ammount was changed"
            }
        )

@api_bp.route('tool/add', methods=['POST'])
def add_tool():
    """
    Add new tool

    Expected json:
    {
        toolname: tool's name to add
    }
    """
    if request.method == 'POST':
        js = request.json
        check = check_json(js, 'toolname')
        if type(check) is dict:
            return jsonify(check)

        db = db_methods.get_db()

        try:
            db_methods.add_tool(db, js['toolname'])
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
    """
    Delete the tool

    Expected json:
    {
        toolname: tool's name to delete
    }
    """
    if request.method == 'POST':
        js = request.json
        check = check_json(js, 'toolname')
        if type(check) is dict:
            return jsonify(check)
        
        db = db_methods.get_db()

        db_methods.delete_tool(db, js['toolname'])
        return jsonify(
            {
                "status": "ok",
                "message": "The tool was deleted"
            }
        )