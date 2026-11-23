from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import URL

from core.config import(
    DB_NAME,
    DB_USER,
    DB_PORT,
    DB_HOST,    
    DB_PASSWORD
)

DATABASE_URL = URL.create(
    drivername = "postgresql+psycopg",
    username = DB_USER,
    password = DB_PASSWORD,
    host = DB_HOST,
    port = DB_PORT,
    database = DB_NAME
)

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping = True,
    pool_size = 5,
    max_overflow = 10  
)

SessionLocal  =  sessionmaker(
    bind = engine,
    autoflush =  False,
    autocommit =  False
)

def get_db():
    db= SessionLocal()

    try:
        yield db
    finally:
        db.close()