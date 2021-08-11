from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://dbmasteruser:1qwx?&6*LzLcB`f`x:&`*70,[]tySRS~@ls-17b750ad5f19ab09f87e981f000631ea8fa6b698.cicx1pbp9xut.ap-southeast-2.rds.amazonaws.com/dev2'
    DATABASE_URI='mysql+mysqlconnector://{user}:{password}@{server}/{database}'.format(user='dbmasteruser', password='1qwx?&6*LzLcB`f`x:&`*70,[]tySRS~', server='ls-17b750ad5f19ab09f87e981f000631ea8fa6b698.cicx1pbp9xut.ap-southeast-2.rds.amazonaws.com', database='dev2')
    
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
    db.init_app(app)

    from .views import main
    app.register_blueprint(main)

    return app