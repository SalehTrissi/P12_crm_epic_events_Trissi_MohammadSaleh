import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


# Load environment variables from .env
load_dotenv()


# Retrieve the database URL
DATABASE_URL = os.getenv("DATABASE_URL")


# Initialize the connection engine
engine = create_engine(DATABASE_URL)


# Create a session to manage transactions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Base for SQLAlchemy models
Base = declarative_base()
