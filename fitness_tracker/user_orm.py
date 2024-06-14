# fitness_tracker/user_orm.py

from .database import SessionLocal
from .models import User  # Adjust this import if necessary

class UserORM:
    def __init__(self):
        self.db = SessionLocal()

    def create_user(self, username, age, fitness_goals):
        user = User(username=username, age=age, fitness_goals=fitness_goals)
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def delete_user(self, user_id):
        user = self.db.query(User).filter(User.id == user_id).first()
        self.db.delete(user)
        self.db.commit()

    def get_all_users(self):
        return self.db.query(User).all()

    def find_user_by_id(self, user_id):
        return self.db.query(User).filter(User.id == user_id).first()
