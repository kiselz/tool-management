import sqlite3
from .db import *
import os

db = sqlite3.connect(os.path.join(os.environ['PYTHONPATH'], 'database', 'database.db'))
# return row as a dictionary rather than a tuple
db.row_factory = sqlite3.Row


# create database
with open(os.path.join(os.environ['PYTHONPATH'], 'database', 'schema.sql')) as schema:
    db.executescript(schema.read())
    db.close()