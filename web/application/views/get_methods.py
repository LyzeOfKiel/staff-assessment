from flask import (
    Blueprint,
    jsonify
)
from application.db_init import get_db

bp = Blueprint('get_methods', __name__)


@bp.route('/get_courses', methods=['GET'])
def get_courses():
    data = get_db().get_all_courses()
    data = [{'name': f['name'], 'id': str(f['_id'])} for f in data]
    return jsonify(data)


@bp.route('/get_all_feedbacks', methods=['Get'])
def get_all_feedbacks():
    data = get_db().get_all_feedback()
    for f in data:
        f['_id'] = str(f['_id'])
    return jsonify(data)
