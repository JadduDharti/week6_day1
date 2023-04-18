import os

basedir = os.path.abspath(os.path.dirname(__file__))

# give access to the project in ANY OS were find outselves in
#allow outside file/folder to be added to the project
#from the base directory

class Config():
   

    SECRET_KEY = os.environ.get("SECRET_KEY") or "Nana nana boo noo yell neb=ver guess"
    SQLALCHEMY_DATABASE_URL = os.environ.get("DATABASE_URL") or "sqlite://" + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFIACTIONS = False # turns of message from sqlalchemy regards update to our db