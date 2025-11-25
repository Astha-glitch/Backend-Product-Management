from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
db_url="postgresql://postgres:Astha123@localhost:5432/astha"
engine=create_engine(db_url)
SessionLocal=sessionmaker(autoflush=False,autocommit=False,bind=engine)
