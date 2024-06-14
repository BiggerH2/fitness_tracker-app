from setuptools import setup, find_packages

setup(
    name='fitness_tracker',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'sqlalchemy',
        'click',
        'flask',
    ],
    entry_points={
        'console_scripts': [
            'fitness_tracker=fitness_tracker.cli:cli',
        ],
    },
)
