from flask import Blueprint, jsonify
from app.models.quiz import Quiz
from app.schemas.quiz_schema import quizzes_schema

quiz_bp = Blueprint('quiz', __name__)

@quiz_bp.route('/', methods=['GET'])
def get_all_quizzes():
    quizzes = Quiz.query.all()
    return jsonify({
        "success": True,
        "quizzes": quizzes_schema.dump(quizzes)
    }), 200