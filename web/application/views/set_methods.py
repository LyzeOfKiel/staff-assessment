from flask import (
    Blueprint,
    jsonify,
    request
)

from application.db_init import get_db

bp = Blueprint('set_methods', __name__)


@bp.route('/set_dfeedback_course', methods=['POST'])
def set_dfeedback_course():
    data = request.get_json()
    get_db().set_feedback(data['course_id'], 0, data['form'])
    print(data)
    return 'ok'
