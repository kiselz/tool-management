from flask import current_app, g
import sqlite3
from sqlite3 import Connection
from database.utils import convert_rows_to_dicts


def get_db() -> Connection:
    """
    Initializes a database connection for request and return it

    Attetnion: Works only when a server is already launched

    Returns:
    db (sqlite3.Connection): connection to a db
    """

    if 'db' not in g:
        g.db = sqlite3.connect(current_app.config['DATABASE'])

        # return rows as dictionaries
        g.db.row_factory = sqlite3.Row
    return g.db

def create_db() -> None:
    """
    Create a database based on the schema.sql file

    Attention: Works only when a server is already launched
    """

    db = get_db()

    with current_app.open_resource('./database/schema.sql') as schema:
        db.executescript(schema.read())

def close_db() -> None:
    """
    Close connection to the db

    Attention: Works only when a server is already launched
    """

    db = g.pop('db', None)

    if db is not None:
        db.close()

def get_users(db: Connection) -> list:
    """
    Get all users from users table

    Parameters:
    db (Connection): sqlite3 connection to a db (sqlite3.connect())

    Returns:
    users (list): list of users as dictionaries
    """
    
    user_rows = db.cursor().execute('SELECT * FROM users').fetchall()
    return convert_rows_to_dicts(user_rows)

def add_user(db: Connection, firstname: str, admin_rights: bool) -> None:
    """
    Add a new user to database

    Parameters:
    db (Connection): sqlite3 connection to a db (sqlite3.connect())
    firstname (str): Firstname of a new user
    admin_rights (bool): Is a new user admin?
    """

    admin_rights = 1 if admin_rights else 0
    db.execute(f"INSERT INTO users(firstname, admin_rights) VALUES ('{firstname}', '{admin_rights}')")

    tools = get_tools(db)
    if (len(tools) != 0 and not admin_rights):
        # admin should not have tools
        for tool_row in tools:
            toolname = tool_row['toolname']
            db.execute(f"INSERT INTO tool_track(firstname, toolname, ammount) VALUES ('{firstname}', '{toolname}', 0)")

    db.commit()

def delete_user(db: Connection, firstname: str) -> None:
    """
    Delete the user based on a firstname

    Parameters:
    db (Connection): sqlite3 connection to a db (sqlite3.connect())
    firstname (str): firstname of an user to delete
    """

    db.execute(f"DELETE FROM users WHERE firstname = '{firstname}'")
    db.execute(f"DELETE FROM tool_track WHERE firstname = '{firstname}'")
    db.commit()

def get_tools(db: Connection) -> list[str]:
    """
    Get all users from users table

    Parameters:
    db (Connection): sqlite3 connection to a db (sqlite3.connect())

    Returns:
    tools (list[sqlite3.Row]): list of tools
    """
    
    tools = db.cursor().execute('SELECT * FROM tools').fetchall()
    return convert_rows_to_dicts(tools)

def add_tool(db: Connection, toolname: str) -> None:
    """
    Add a new tool

    Parameters:
    db (Connection): sqlite3 connection to a db (sqlite3.connect())
    toolname (str): Name of a tool
    """

    db.execute(f"INSERT INTO tools(toolname) VALUES ('{toolname}')")
    users = get_users(db)
    if (len(users) != 0):
        for user_row in users:
            if (user_row['admin_rights']):
                # admin should not have tools
                continue
            firstname = user_row['firstname']
            db.execute(f"INSERT INTO tool_track(firstname, toolname, ammount) VALUES ('{firstname}', '{toolname}', 0)")
    db.commit()

def delete_tool(db: Connection, toolname: str) -> None:
    """
    Delete the tool based on its name

    Parameters:
    db (Connection): sqlite3 connection to a db (sqlite3.connect())
    toolname (str): Name of a tool to delete
    """

    db.execute(f"DELETE FROM tools WHERE toolname = '{toolname}'")
    db.execute(f"DELETE FROM tool_track WHERE toolname = '{toolname}'")
    db.commit()

def get_user_tools(db: Connection, firstname: str):
    """
    Get all users tools in alphabetical order

    Parameters:
    db (Connection): sqlite3 connection to a db (sqlite3.connect())
    firstname (str): firstname of an user
    """

    tool_rows = db.cursor().execute(f"SELECT toolname, ammount FROM tool_track WHERE firstname = '{firstname}' \
                                     ORDER BY toolname ASC").fetchall()   
    return convert_rows_to_dicts(tool_rows)

