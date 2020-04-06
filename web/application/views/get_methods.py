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


@bp.route('/get_all_feedbacks', methods=['Get'])
def get_all_feedbacks():
    data = get_db().get_all_feedback()
    for f in data:
        f['_id'] = str(f['_id'])
    return jsonify(data)
