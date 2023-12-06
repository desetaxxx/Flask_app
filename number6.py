from flask import *
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func

app = Flask(__name__)
app.app_context()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///athletes.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    gender = db.Column(db.String(2))
    age = db.Column(db.Integer)
    country = db.Column(db.String(50))
    sport = db.Column(db.String(50))

    def __init__(self, name, gender, age, country, sport):
        self.name = name
        self.gender = gender
        self.age = age
        self.country = country
        self.sport = sport

with app.app_context():
    db.create_all()
    user1 = User('Johnny6', 'F', 23, 'USA', 'BJJ')
    user2 = User('Kate', 'M', 22, 'USA', 'Swimming')
    db.session.add(user1)
    db.session.add(user2)
    db.session.commit()

    # Получаем количество спортсменов
    total_count = User.query.count()

    # Получаем максимальный возраст спортсменов
    max_age = db.session.query(func.max(User.age)).scalar()

    # Получаем минимальный возраст спортсменов
    min_age = db.session.query(func.min(User.age)).scalar()

    # Выводим результаты
    print(f"Количество спортсменов: {total_count}")
    print(f"Максимальный возраст: {max_age}")
    print(f"Минимальный возраст: {min_age}")