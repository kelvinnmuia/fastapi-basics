# import psycopg2
# from psycopg2.extras import RealDictCursor
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "postgresql://<username>:<password>@<ip-address/hostname>/<database_name>"

# while True:
#    try:
#        conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', 
#                            password='P0stgres26', cursor_factory=RealDictCursor)
#        cursor = conn.cursor()
#        print("Database connection was successful")
#        break

#    except Exception as error:
#        print("Connection to database failed")
#        print("Error: ", error)
#        time.sleep(2)

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:P0stgres26@localhost/fastapi"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
def get_db():
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close()