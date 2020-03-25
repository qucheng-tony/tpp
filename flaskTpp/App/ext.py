from flask_bootstrap import Bootstrap
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension
from flask_caching import Cache

db=SQLAlchemy()
migrate=Migrate()
cache=Cache(config={
    'CACHE_TYPE':'redis',
})

def init_ext(app):
    cache.init_app(app)
    db.init_app(app)
    migrate.init_app(app,db)
    DebugToolbarExtension(app)
    Bootstrap(app)