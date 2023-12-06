from flask import *  # Импорт модуля Flask
from flask_sqlalchemy import SQLAlchemy  # Импорт модуля SQLAlchemy для работы с базой данных
from sqlalchemy import func


app = Flask(__name__)  # Инициализация объекта приложения Flask
app.app_context()  # Создание контекста приложения
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///athletes.db'  # Установка URI для подключения к базе данных
db = SQLAlchemy(app)  # Создание экземпляра SQLAlchemy и передача в него нашего приложения




class User(db.Model):  # Создание модели для таблицы User в базе данных
    id = db.Column(db.Integer, primary_key=True)  # Определение столбца id (первичный ключ)
    name = db.Column(db.String(80))  # Определение столбца name (строка, уникальное значение)
    gender = db.Column(db.String(2))  # Определение столбца gender (строка)
    age = db.Column(db.Integer)  # Определение столбца age (целое число)
    country = db.Column(db.String(50))  # Определение столбца country (строка)
    sport = db.Column(db.String(50))  # Определение столбца sport (строка)

    def __init__(self, name, gender, age, country, sport):  # Метод для инициализации экземпляра класса User
        self.name = name  # Присвоение значения name
        self.gender = gender  # Присвоение значения gender
        self.age = age  # Присвоение значения age
        self.country = country  # Присвоение значения country
        self.sport = sport  # Присвоение значения sport

with app.app_context():  # Вход в контекст приложения
    db.create_all()  # Создание всех таблиц в базе данных (если их нет)
    user1 = User('Johnny6', 'F', 23, 'USA', 'BJJ')  # Создание нового пользователя
    user2 = User('Kate', 'M', 22, 'USA', 'Swimming')  # Создание нового пользователя
    db.session.add(user1)  # Добавление пользователя в текущую сессию
    db.session.add(user2) # Добавление пользователя в текущую сессию
    db.session.commit()  # Фиксация изменений в базе данных
    users = User.query.all()  # Получение всех пользователей
    db.session.close()  # Закрытие сессии
    for user in users: #вывод пользователей
        print(f"User ID: {user.id}, Name: {user.name}, Gender: {user.gender}, Age: {user.age}, Country: {user.country}, Sport: {user.sport}")

""" @app.route('/')  # Определение маршрута для корневого URL
def index():  # Определение функции для обработки запроса к корневому URL
    return render_template('index.html')  # Возвращает шаблон index.html

@app.route('/contacts.html')  # Определение маршрута для URL /contacts.html
def contacts():  # Определение функции для обработки запроса к URL /contacts.html
    return render_template('contacts.html')  # Возвращает шаблон contacts.html """

@app.route('/')
def index():
    # Количество спортсменов
    athlete_count = db.session.query(func.count(User.id)).scalar()

    # Максимальный возраст
    max_age = db.session.query(func.max(User.age)).scalar()

    # Минимальный возраст
    min_age = db.session.query(func.min(User.age)).scalar()

    return f"Количество спортсменов: {athlete_count}, Максимальный возраст: {max_age}, Минимальный возраст: {min_age}"

@app.route('/about/')
def about():
    return 'О нас'

@app.route('/users/')
def showUsers():
    users = User.query.all()
    return render_template('users.html',users=users)

if __name__ == '__main__':  # Если код запускается напрямую
    app.run()  # Запуск приложения
    
    
    
    
