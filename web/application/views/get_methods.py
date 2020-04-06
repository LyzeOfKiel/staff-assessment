from flask import (
    Blueprint,
    jsonify
)
from application.db_init import get_db

bp = Blueprint('get_methods', __name__)


@bp.route('/get_courses', methods=['GET'])
def get_courses():
    return jsonify(
        {
            'name': 'Math',
            'id': 4
        },
        {
            'name': 'Eng',
            'id': 42
        },
        {
            'name': 'Other',
            'id': 3
        },
    )


@bp.route('/get_all_feedbacks', methods=['GET'])
def get_all_feedbacks():
    data = get_db().get_all_feedback()
    for f in data:
        f['_id'] = str(f['_id'])
    return jsonify(data)

@bp.route('/get_all_professors', methods=['GET'])
def get_all_professors():
    data = get_db().get_all_prof()
    for p in data:
        p['_id'] = str(p['_id'])
    return jsonify(data)

@bp.route('/get_all_students', methods=['GET'])
def get_all_students():
    data = get_db().get_all_students()
    for s in data:
        s['_id'] = str(s['_id'])
    return jsonify(data)

@bp.route('/get_all_tas', methods=['GET'])
def get_all_tas():
    data = get_db().get_all_ta()
    for t in data:
        t['_id'] = str(t['_id'])
    return jsonify(data)

@bp.route('/get_all_admins', methods=['GET'])
def get_all_admins():
    data = get_db().get_all_admin()
    for a in data:
        a['_id'] = str(a['_id'])
    return jsonify(data)
