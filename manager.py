# This script handles all the migration of the database

# MAKE SURE YOU HAVE PYTHON3 INSTALLED

# To install Flask-migrate:
    # pip3 install Flask
    # pip3 install Flask-migrate

# Three scripts for manager
#     shell               runs the shell
#     db                  Perform database migrations
#     runserver           Runs the Flask development server i.e. app.run()

# To migrate the database, please use the following 3 commands:
# python3 manager.py db init
# python3 manager.py db migrate
    # If fails, try running the local commands found at setup.md
# python3 manager.py db upgrade


from app import manager

manager.run()


# For more details, please see: #https://flask-migrate.readthedocs.io/en/latest/