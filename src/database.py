from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker

# TODO  going to enhance with settings file that pull in env vars
db_config = URL.create(
    drivername="postgresql",
    username="postgres-user",
    password="postgres-pw",
    host="localhost",
    database="demo",
    port="5432",
)
engine = create_engine(db_config, echo=True)
session = sessionmaker(bind=engine)()
