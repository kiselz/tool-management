from flask import Flask, render_template, render_template_string, redirect, g, session
from database.db import get_db, get_users, close_db
import server.blueprints.auth
import server.blueprints.menu
import server.blueprints.api
import os


app = Flask(__name__)
app.config['DATABASE'] = './database/database.db'
# close the db after a response
app.teardown_appcontext(close_db)
app.secret_key = 'very-secret-key'

# register blueprints
app.register_blueprint(server.blueprints.auth.auth_bp)
app.register_blueprint(server.blueprints.menu.menu_bp)
app.register_blueprint(server.blueprints.api.api_bp)

@app.route('/', methods=['GET'])
def index():
    db = get_db()
    users = get_users(db)
    if 'user' in session:
        return redirect('/menu')
    return render_template('login/login.html', users=users)

if __name__ == "__main__":
    app.run(debug=True)