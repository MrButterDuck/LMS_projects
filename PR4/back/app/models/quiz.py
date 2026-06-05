from app.extensions import db

class Quiz(db.Model):
    __tablename__ = 'quiz'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False)
    type = db.Column(db.String(1), nullable=False)
    tasks = db.relationship('QuizTask', back_populates='quiz', cascade='all, delete', order_by='QuizTask.order')

    def __init__(self, title, type):
        self.title = title
        self.type = type

class QuizTask(db.Model):
    __tablename__ = 'quiz_task'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id'), nullable=False)
    question = db.Column(db.Text, nullable=False)
    answer = db.Column(db.String(255), nullable=False)
    order = db.Column(db.Integer, nullable=False)
    quiz = db.relationship('Quiz', back_populates='tasks')

    def __init__(self, quiz_id, question, answer, order):
        self.quiz_id = quiz_id
        self.question = question
        self.answer = answer
        self.order = order