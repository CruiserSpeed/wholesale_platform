from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from settings import DATABASE_URL

engine = create_engine(DATABASE_URL, convert_unicode=True)
engine.connect()

Base = declarative_base()

def init_db():
    import models
    Base.metadata.create_all(bind=engine)

