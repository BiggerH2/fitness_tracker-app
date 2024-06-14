# fitness_tracker/workout_orm.py

from .database import SessionLocal
from .models import Workout

class WorkoutORM:
    def __init__(self):
        self.db = SessionLocal()

    def create_workout(self, user_id, workout_type, duration, calories_burned, date):
        workout = Workout(user_id=user_id, workout_type=workout_type, duration=duration, calories_burned=calories_burned, date=date)
        self.db.add(workout)
        self.db.commit()
        self.db.refresh(workout)
        return workout

    def delete_workout(self, workout_id):
        workout = self.db.query(Workout).filter(Workout.id == workout_id).first()
        self.db.delete(workout)
        self.db.commit()

    def get_all_workouts(self):
        return self.db.query(Workout).all()

    def find_workout_by_id(self, workout_id):
        return self.db.query(Workout).filter(Workout.id == workout_id).first()

    def get_workouts_by_user_id(self, user_id):
        return self.db.query(Workout).filter(Workout.user_id == user_id).all()
