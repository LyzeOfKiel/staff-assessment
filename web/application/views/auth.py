from flask import (
    Blueprint,
)


bp = Blueprint('auth', __name__)


@bp.route('/', methods=['GET', 'POST'])
def root():
    return 'succ'
