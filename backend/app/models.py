from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """
    Все пользователи системы
    """

    id = db.Column(db.INTEGER(), nullable=False, primary_key=True)
    name = db.Column(db.VARCHAR(length=50), nullable=False, unique=True)
    email = db.Column(db.VARCHAR())
    password = db.Column(db.VARCHAR(length=255))

    def __init__(self, name, password, email) -> None:
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return f"{type(self).__name__} <{self.name}>"

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()