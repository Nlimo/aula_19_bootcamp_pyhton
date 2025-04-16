from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

POSTGRES_DATABASE_URL = "postegresql://user:password@postgres/mydatabase"

engine = create_engine(POSTGRES_DATABASE_URL)

SessionLocal = sessionmaker(autocommit =False, autoflush = False, bind=engine)

Base = declarative_base() #ORM

def get_db():
    db = SessionLocal()
    try:
        yield db # diferente do retorne a função não morre, ou seja, com yield eu posso chamar várias vezes
    finally:
        db.close()