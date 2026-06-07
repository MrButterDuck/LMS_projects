from app import create_app
from app.extensions import db
from app.models.quiz import Quiz, QuizTask

app = create_app()

QUIZ_DATA = [
    {
        "title": "Сопоставьте марку автомобиля и страну производства.",
        "type": "M",
        "tasks": [
            {"question": "BMW", "answer": "Германия", "order": 1},
            {"question": "Toyota", "answer": "Япония", "order": 2},
            {"question": "Ford", "answer": "США", "order": 3},
            {"question": "Ferrari", "answer": "Италия", "order": 4}
        ]
    },
    {
        "title": "Сопоставьте модель автомобиля и тип кузова.",
        "type": "M",
        "tasks": [
            {"question": "Mustang", "answer": "Coupe", "order": 1},
            {"question": "Camry", "answer": "Sedan", "order": 2},
            {"question": "Golf", "answer": "Hatchback", "order": 3},
            {"question": "F-150", "answer": "Pickup", "order": 4},
            {"question": "CR-V", "answer": "SUV", "order": 5}
        ]
    },
    {
        "title": "Сопоставьте марку и тип двигателя.",
        "type": "M",
        "tasks": [
            {"question": "Tesla", "answer": "electric", "order": 1},
            {"question": "Porsche 911", "answer": "premium unleaded", "order": 2},
            {"question": "Toyota Prius", "answer": "regular unleaded", "order": 3}
        ]
    },
    {
        "title": "Отсортируйте автомобили по возрастанию мощности двигателя (л.с.).",
        "type": "S",
        "tasks": [
            {"question": "Toyota Prius (121 л.с.)", "answer": "1", "order": 1},
            {"question": "Honda Civic (158 л.с.)", "answer": "2", "order": 2},
            {"question": "BMW 1 Series M (335 л.с.)", "answer": "3", "order": 3},
            {"question": "Porsche 911 (400 л.с.)", "answer": "4", "order": 4},
            {"question": "Tesla Model S (518 л.с.)", "answer": "5", "order": 5},
            {"question": "Ferrari 488 GTB (661 л.с.)", "answer": "6", "order": 6}
        ]
    },
    {
        "title": "Выберите автомобили, выпущенные младше 2012 года.",
        "type": "C",
        "tasks": [
            {"question": "BMW 1 Series M (2011)", "answer": "1", "order": 1},
            {"question": "Audi A4 (2010)", "answer": "1", "order": 2},
            {"question": "Mercedes-Benz C-Class (2013)", "answer": "0", "order": 3},
            {"question": "Porsche 911 (2014)", "answer": "0", "order": 4},
            {"question": "Tesla Model S (2017)", "answer": "0", "order": 5},
            {"question": "Toyota Prius (2008)", "answer": "1", "order": 6}
        ]
    },
    {
        "title": "Сопоставьте автомобиль и его цену MSRP (долл.).",
        "type": "M",
        "tasks": [
            {"question": "Honda Civic", "answer": "19500", "order": 1},
            {"question": "Tesla Model S", "answer": "75000", "order": 2},
            {"question": "Porsche 911", "answer": "95000", "order": 3},
            {"question": "Ferrari 488 GTB", "answer": "245000", "order": 4}
        ]
    }
]

with app.app_context():
    db.create_all()
    
    if Quiz.query.count() == 0:
        for q_data in QUIZ_DATA:
            quiz = Quiz(title=q_data["title"], type=q_data["type"])
            db.session.add(quiz)
            db.session.flush()
            
            for task_data in q_data["tasks"]:
                task = QuizTask(
                    quiz_id=quiz.id,
                    question=task_data["question"],
                    answer=task_data["answer"],
                    order=task_data["order"]
                )
                db.session.add(task)
                
        db.session.commit()