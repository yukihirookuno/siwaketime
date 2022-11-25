from flask_script import Manager
from siwaketime.app import create_app
from siwaketime.models.entries.entries import Entry 
from siwaketime.models.entries.genre_count import Genre_count
from siwaketime.models.entries.genres import Genre
from siwaketime.models.entries.titles import Title
from siwaketime.models.users import User

from siwaketime.scripts.db import InitDB



if __name__ == "__main__":
    manager = Manager(create_app)
    manager.add_command('init_db', InitDB())
    manager.run()