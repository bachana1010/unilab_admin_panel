from flask import Flask,render_template
from flask_admin import Admin
from flask_admin.menu import MenuLink
from app.configs import Config,PROJECT_ROOT
from app.extensions import db, migrate, login_manager


BLUEPRINTS = [] 
COMMANDS = [] 

def create_app():

    app = Flask(__name__)
    app.config.from_object(Config)

    # register_commands(app)
    # register_extensions(app)
    # register_blueprints(app)
    # register_admin_panel(app)

    return app

def register_extensions(app):

    # Setup Flask-SQLAlchemy
    db.init_app(app)

    # Setup Flask-Migrate
    migrate.init_app(app, db)

    # Flask-Login
    @login_manager.user_loader
    def load_user(id_):
        return User.query.get(id_)

    login_manager.init_app(app)


def register_blueprints(app):

    for blueprint in BLUEPRINTS:
        app.register_blueprint(blueprint)


def register_commands(app):

    for command in COMMANDS:
        app.cli.add_command(command)


def register_admin_panel(app):
    admin = Admin(app)
    admin.add_view(UserView(User,db.session))
    admin.add_view(FileView(PROJECT_ROOT + '/static/uploads', name='Static Files'))
    #https://flask-admin.readthedocs.io/en/latest/api/mod_contrib_fileadmin/

    admin.add_link(MenuLink(name="Return Home",url='/'))




