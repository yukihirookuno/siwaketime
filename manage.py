from flask_script import Manager
from siwaketime import create_app
from siwaketime.models.entries import Entry
from siwaketime.models.users import User

from siwaketime.scripts.db import InitDB



if __name__ == "__main__":
    manager = Manager(create_app)
    manager.add_command('init_db', InitDB())
    manager.run()