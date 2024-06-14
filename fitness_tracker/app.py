# fitness_tracker/app.py

from flask import Flask, render_template, request, redirect, url_for, jsonify
from fitness_tracker.user_orm import UserORM
from fitness_tracker.workout_orm import WorkoutORM
from fitness_tracker.database import init_db
import datetime

app = Flask(__name__)
user_orm = UserORM()
workout_orm = WorkoutORM()

# Routes and other Flask configurations follow...


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'POST':
        username = request.form['username']
        age = request.form['age']
        fitness_goals = request.form['fitness_goals']
        user_orm.create_user(username, age, fitness_goals)
        return redirect(url_for('users'))
    users = user_orm.get_all_users()
    return render_template('users.html', users=users)

@app.route('/workouts', methods=['GET', 'POST'])
def workouts():
    if request.method == 'POST':
        user_id = request.form['user_id']
        workout_type = request.form['workout_type']
        duration = request.form['duration']
        calories_burned = request.form['calories_burned']
        date_str = request.form['date']
        
        # Corrected code block
        date = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
        
        workout_orm.create_workout(user_id, workout_type, duration, calories_burned, date)
        return redirect(url_for('workouts'))
    workouts = workout_orm.get_all_workouts()
    users = user_orm.get_all_users()
    return render_template('workouts.html', workouts=workouts, users=users)

@app.route('/user/<int:user_id>')
def user_workouts(user_id):
    workouts = workout_orm.get_workouts_by_user_id(user_id)
    user = user_orm.find_user_by_id(user_id)
    return render_template('user_workouts.html', workouts=workouts, user=user)

@app.route('/common_workouts')
def common_workouts():
    workouts = [
        {"type": "Running", "duration": 30, "calories_burned": 300},
        {"type": "Cycling", "duration": 45, "calories_burned": 400},
        {"type": "Swimming", "duration": 60, "calories_burned": 500},
        {"type": "Yoga", "duration": 60, "calories_burned": 200},
        {"type": "Strength Training", "duration": 40, "calories_burned": 350}
    ]
    return render_template('common_workouts.html', workouts=workouts)

@app.route('/api/common_workouts')
def common_workouts_api():
    workouts = [
        {"type": "Running", "duration": 30, "calories_burned": 300},
        {"type": "Cycling", "duration": 45, "calories_burned": 400},
        {"type": "Swimming", "duration": 60, "calories_burned": 500},
        {"type": "Yoga", "duration": 60, "calories_burned": 200},
        {"type": "Strength Training", "duration": 40, "calories_burned": 350}
    ]
    return jsonify(workouts)

if __name__ == '__main__':
    init_db()  # Initialize the database
    app.run(debug=True, port=5001)  # Run the Flask application in debug mode and on port 5001