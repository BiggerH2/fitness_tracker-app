# fitness_tracker/models.py

from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    age = Column(Integer)
    fitness_goals = Column(String)
    
    workouts = relationship("Workout", back_populates="owner")

class Workout(Base):
    __tablename__ = 'workouts'
    
    id = Column(Integer, primary_key=True, index=True)
    workout_type = Column(String)
    duration = Column(Float)
    calories_burned = Column(Float)
    date = Column(Date)
    
    user_id = Column(Integer, ForeignKey('users.id'))
    owner = relationship("User", back_populates="workouts")
