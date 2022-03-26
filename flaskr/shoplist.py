from flask import Blueprint, flash, g, render_template, request
from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('shoplist', __name__, url_prefix='/shoplist')

@bp.route('/index', methods=('GET', 'POST'))
def index():
    db = get_db()
    shoplist = db.execute(
        'SELECT * FROM shoplist'
    ).fetchall()

    return render_template('shoplist/index.html', shoplist=shoplist)


@login_required
@bp.route('/add', methods=('GET', 'POST'))
def add():
    if request.method == 'POST':
        text = request.form['text']
        username = g.user['username']
        db = get_db()
        error = None

        if not text:
            error = 'Please type something, anything!'
            flash(error)

        if error is None:
            db.execute(
                "INSERT INTO shoplist (username, text) VALUES (?, ?)", (username, text),
            )
            db.commit()
        
    return render_template('shoplist/add.html')