"""Module providing db engine"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase


class Base(DeclarativeBase):
    pass

def get_engine():
    """Returns database engine"""
    return create_engine("sqlite:///./mmo.db", pool_size=50, max_overflow=200)

class DBManager:
    def __init__(self):
        self.engine = get_engine()
        Base.metadata.create_all(bind=self.engine)
        self.SessionLocal = sessionmaker(
            autocommit=False, autoflush=True, bind=self.engine)
        self.db = self.SessionLocal()

    def teardown(self):
        self.db.close()
        Base.metadata.drop_all(bind=self.engine)
