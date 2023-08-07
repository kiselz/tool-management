import sqlite3
from .db import *

db = sqlite3.connect('./database/database.db')
# return row as a dictionary rather than a tuple
db.row_factory = sqlite3.Row


# create database
with open('./database/schema.sql') as schema:
    db.executescript(schema.read())
add_user(db, "admin", True)

"""
# test add_user
add_user(db, "admin", True)
users = get_users(db)
print(users[0]['firstname'])

# test delete_user
delete_user(db, "admin")
users = get_users(db)
print(users)

# test delete_user with non existent entry
delete_user(db, "some-random-string-to-test")
users = get_users(db)
print(users)

# test add_tool
add_tool(db, "hammer")
tools = get_tools(db)
print(tools[0]['toolname'])

# test delete_tool
delete_tool(db, "hammer")
tools = get_tools(db)
print(tools)

# test delete_tool with non existent entry
delete_tool(db, "some-random-string-to-test")
tools = get_tools(db)
print(tools)
"""


add_tool(db, "hammer", 3)
add_tool(db, "screwdriver", 3)
add_user(db, "Max", False)

print(get_user_tools(db, "Max"))
add_user(db, "Stepan", False)
print(get_user_tools(db, "Stepan"))

add_tool(db, "wrench", 1)
print(get_tools(db))
print(get_user_tools(db, "Stepan"))