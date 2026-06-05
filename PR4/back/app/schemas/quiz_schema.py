from app.extensions import ma
from app.models.quiz import Quiz, QuizTask

class QuizTaskSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = QuizTask
        load_instance = True
        include_relationships = False
        fields = ('id', 'question', 'answer', 'order')

class QuizSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Quiz
        load_instance = True
        include_relationships = True
    
    tasks = ma.Nested(QuizTaskSchema, many=True)

quiz_schema = QuizSchema()
quizzes_schema = QuizSchema(many=True)