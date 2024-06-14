# Fitness Tracker

The Fitness Tracker is a Python CLI and web application designed to help users monitor their fitness activities and progress. The application allows users to log their workouts, track their progress, and set fitness goals. The system supports multiple users, enabling each user to manage their own fitness records and goals.

## Features

- Create and manage user profiles.
- Log workouts with details like type, duration, calories burned, and date.
- View all users and workouts.
- View workouts for a specific user.
- Delete users and workouts.
- Web interface for easier access and usage.

## Setup

1. Clone the repository.
2. Install dependencies with `pipenv install`.
3. Initialize the database with:
    ```bash
    python -c 'from fitness_tracker.database import init_db; init_db()'
    ```
4. Run the CLI:
    ```bash
    python fitness_tracker/cli.py
    ```
5. Run the Flask app:
    ```bash
    flask run
    ```

## Usage

Use the CLI to interact with the application. Here are some commands:

- Create a new user:
    ```bash
    python fitness_tracker/cli.py create_user --username "john_doe" --age 25 --fitness_goals "Lose weight"
    ```

- Create a new workout:
    ```bash
    python fitness_tracker/cli.py create_workout --user_id 1 --workout_type "Running" --duration 30 --calories_burned 300 --date "2023-06-11"
    ```

- View all users:
    ```bash
    python fitness_tracker/cli.py view_users
    ```

- View workouts for a user:
    ```bash
    python fitness_tracker/cli.py view_user_workouts --user_id 1
    ```

## Contributing

Feel free to submit issues and pull requests.


