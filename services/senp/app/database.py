from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

engine = None
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False))
Base = declarative_base()


def init_db(app):
    global engine
    engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'], pool_recycle=3600, echo=True)
    db_session.configure(bind=engine)

    import app.model
    Base.metadata.create_all(bind=engine)


Base.query = db_session.query_property()
