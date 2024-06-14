import click
from .models import UserORM, WorkoutORM

user_orm = UserORM()
workout_orm = WorkoutORM()

@click.group()
def cli():
    pass

@click.command()
@click.option('--username', prompt='Username', help='The username of the user.')
@click.option('--age', prompt='Age', type=int, help='The age of the user.')
@click.option('--fitness_goals', prompt='Fitness Goals', help='The fitness goals of the user.')
def create_user(username, age, fitness_goals):
    user = user_orm.create_user(username, age, fitness_goals)
    click.echo(f'User {user.username} created with ID {user.id}')

@click.command()
@click.option('--user_id', prompt='User ID', type=int, help='The ID of the user to delete.')
def delete_user(user_id):
    user_orm.delete_user(user_id)
    click.echo(f'User with ID {user_id} deleted.')

@click.command()
def view_users():
    users = user_orm.get_all_users()
    for user in users:
        click.echo(f'ID: {user.id}, Username: {user.username}, Age: {user.age}, Goals: {user.fitness_goals}')

@click.command()
@click.option('--user_id', prompt='User ID', type=int, help='The ID of the user.')
@click.option('--workout_type', prompt='Workout Type', help='The type of workout.')
@click.option('--duration', prompt='Duration (minutes)', type=float, help='The duration of the workout.')
@click.option('--calories_burned', prompt='Calories Burned', type=float, help='The calories burned during the workout.')
@click.option('--date', prompt='Date (YYYY-MM-DD)', help='The date of the workout.')
def create_workout(user_id, workout_type, duration, calories_burned, date):
    workout = workout_orm.create_workout(user_id, workout_type, duration, calories_burned, date)
    click.echo(f'Workout {workout.workout_type} created with ID {workout.id} for User ID {user_id}')

@click.command()
@click.option('--workout_id', prompt='Workout ID', type=int, help='The ID of the workout to delete.')
def delete_workout(workout_id):
    workout_orm.delete_workout(workout_id)
    click.echo(f'Workout with ID {workout_id} deleted.')

@click.command()
def view_workouts():
    workouts = workout_orm.get_all_workouts()
    for workout in workouts:
        click.echo(f'ID: {workout.id}, Type: {workout.workout_type}, Duration: {workout.duration}, Calories: {workout.calories_burned}, Date: {workout.date}, User ID: {workout.user_id}')

@click.command()
@click.option('--user_id', prompt='User ID', type=int, help='The ID of the user.')
def view_user_workouts(user_id):
    workouts = workout_orm.get_workouts_by_user_id(user_id)
    for workout in workouts:
        click.echo(f'ID: {workout.id}, Type: {workout.workout_type}, Duration: {workout.duration}, Calories: {workout.calories_burned}, Date: {workout.date}')

cli.add_command(create_user)
cli.add_command(delete_user)
cli.add_command(view_users)
cli.add_command(create_workout)
cli.add_command(delete_workout)
cli.add_command(view_workouts)
cli.add_command(view_user_workouts)

if __name__ == '__main__':
    cli()
