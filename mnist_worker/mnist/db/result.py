from sqlalchemy import Column, Integer, String, DateTime, JSON, MetaData, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import engine_from_config
from sqlalchemy.orm import sessionmaker
import logging
from config import get_config
from sqlalchemy_utils import database_exists, create_database
import datetime

meta = MetaData()

Base = declarative_base()

config = get_config(config_section="database")

engine = engine_from_config(config, prefix='db.')
if not database_exists(engine.url):
    logging.info(f"Database exist is {0}, creating the database.. {1}", database_exists(engine.url), engine.url)
    create_database(engine.url)

Session = sessionmaker(bind=engine)
session = Session()

result = Table(
    'result', meta,
    Column("result_id", Integer, primary_key=True, autoincrement=True),
    Column("hyperparameters", JSON, nullable=False),
    Column("results", JSON, nullable=True),
    Column("pod_name", String(100), nullable=False),
    Column("time_spent", String(100), nullable=False),
    Column("updated_on", DateTime)

)

logging.info("Checking schema of the table.. ")
meta.create_all(bind=engine)


class Result(Base):
    __tablename__ = 'result'

    result_id = Column(Integer, primary_key=True, autoincrement=True)
    hyperparameters = Column(JSON, nullable=False)
    results = Column(JSON, nullable=True)
    pod_name = Column(String(100), nullable=False)
    time_spent = Column(String(100), nullable=False)
    updated_on = Column(DateTime)

    def __init__(self, hyperparameters_value, results, pod_name=None, time_spent=None):
        self.hyperparameters = hyperparameters_value
        self.results = results
        self.pod_name = pod_name
        self.time_spent = time_spent
        self.updated_on = datetime.datetime.now()

    @staticmethod
    def get_all_results():
        return Result.query.all()

    @staticmethod
    def get_one_result(repository_id):
        return Result.query.get(repository_id)

    def save(self):
        logging.info("Saving the results to the database..")
        session.add(self)
        session.commit()
        print("Saved to the database..")

    def update(self, data):
        for key, item in data.items():
            setattr(self, key, item)
        session.commit()

    def delete(self):
        session.delete(self)
        session.commit()

    def __repr__(self):
        return "<Result(hyperparameters='%s', results='%s', time spent='%s')>" % (
            self.hyperparameters, self.results, self.time_spent)
