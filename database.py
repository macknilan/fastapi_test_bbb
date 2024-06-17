# ARCHIVO QUE CONTIENE LA CONEXIÓN A LA BASE DE DATOS Y EL CÓDIGO DE CREACIÓN DE SESIÓN.

from sqlalchemy import create_engine

# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "postgresql://TESTFASTAPIUSER:CONTRASENADE_TEST_FAST_API_USER@localhost:5432/TEST_FAST_API_DB"

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
