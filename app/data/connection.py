from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
import os
from dotenv import load_dotenv
load_dotenv()

# Create Connection Engine
# represents the core interface to the database
engine = create_engine(os.getenv("aws_db_url"), echo=False)

# Define Class ##
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

# returns a class
Base = declarative_base()

Base.query = db_session.query_property()

def init_db():
    import app.data.models
    Base.metadata.create_all(bind=engine)