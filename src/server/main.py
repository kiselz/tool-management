from flask import Flask, render_template, render_template_string, g, session
from database.db import get_db, get_users, close_db
import server.blueprints.auth
import os


app = Flask(__name__)
app.config['DATABASE'] = './database/database.db'
# close the db after a response
app.teardown_appcontext(close_db)
app.secret_key = 'very-secret-key'

# register blueprints
app.register_blueprint(server.blueprints.auth.auth_bp)

@app.route('/', methods=['GET'])
def index():
    db = get_db()
    users = get_users(db)
    if 'user' in session:
        return render_template_string('<p>I am {{ user }} </p>', user=session['user'])
    return render_template('login/login.html', users=users)

if __name__ == "__main__":
    app.run(debug=True)