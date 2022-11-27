from flask_script import Manager
from app.__init__ import create_app
from app.models.entries.entries import Entry 
from app.models.entries.genre_count import Genre_count
from app.models.entries.genres import Genre
from app.models.entries.titles import Title
from app.models.users import User

from app.scripts.db import InitDB



if __name__ == "__main__":
    manager = Manager(create_app)
    manager.add_command('init_db', InitDB())
    manager.run()