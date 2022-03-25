import functools
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('todo', __name__, url_prefix='/todo')

@bp.route('/index', methods=('GET', 'POST'))
def index():
    db = get_db()
    todolist = db.execute(
        'SELECT * FROM todo'
    ).fetchall()

    return render_template('todo/index.html', todolist=todolist)


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
                "INSERT INTO todo (username, text) VALUES (?, ?)", (username, text),
            )
            db.commit()
        
    return render_template('todo/add.html')