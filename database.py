from sqlalchemy import create_engine, Column, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database URL for SQLite
DATABASE_URL = "sqlite:///./products.db"

# Create a new SQLite database engine instance
engine = create_engine(DATABASE_URL)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for our classes definitions
Base = declarative_base()

# Define the Product class
class Product(Base):
    __tablename__ = "products"
    url = Column(String, primary_key=True, index=True) # URL as a primary key
    title = Column(String) # Product title
    price = Column(Float) # Product price

# Create all tables in the database
Base.metadata.create_all(bind=engine)