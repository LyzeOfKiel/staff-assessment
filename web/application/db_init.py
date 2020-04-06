from flask import g, current_app

from .db.db import Manager


def create_db():
    return Manager()


def get_db():
    if 'db' not in g:
        g.db = create_db()
    return g.db
