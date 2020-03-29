# TODO: Reformat database to use new csv
# TODO: Figure out how to rewrite database every time data updates

from sqlalchemy import MetaData, create_engine, String, Column, Integer, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

metadata = MetaData()
engine = create_engine('sqlite:///covid19_db', connect_args={'check_same_thread': False}, echo=False)  # echo=False
Base = declarative_base()
db_session = sessionmaker(bind=engine)()


# Table with all the data
class CoronaEntry(Base):
    __tablename__ = 'covid19_normalized'
    province_state = Column(String, primary_key=True)
    country_region = Column(String)
    observation_date = Column(String)
    continent = Column(String)
    us_county = Column(String)
    us_state = Column(String)
    confirmed_total = Column(Integer)
    deaths_total = Column(Integer)
    confirmed_daily = Column(Integer)
    deaths_daily = Column(Integer)
    recovered_daily = Column(Integer)
    latitude = Column(Float)
    longitude = Column(Float)


