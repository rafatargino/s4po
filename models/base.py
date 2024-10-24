from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Conectando ao banco SQLite
DATABASE_URL = "sqlite:///database.db"

engine = create_engine(DATABASE_URL, echo=True)  # echo=True para logar as operações
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base declarativa para todos os modelos
Base = declarative_base()
