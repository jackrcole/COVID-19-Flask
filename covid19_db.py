from sqlalchemy import MetaData, create_engine, String, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

metadata = MetaData()
engine = create_engine('sqlite:///covid19_db', connect_args={'check_same_thread': False}, echo=False)  # echo=False
Base = declarative_base()
db_session = sessionmaker(bind=engine)()


# Table confirmed
class City(Base):
    __tablename__ = 'confirmed'
    province = Column(String, primary_key=True)
    city_name = Column(String)
    city_climate = Column(String)
    city_meteo_data = relationship("Meteo", backref="city")


# Table meteo
class Meteo(Base):
    __tablename__ = 'meteo'
    id = Column(Integer, primary_key=True)
    city_id = Column(ForeignKey('city.city_id'))
    month = Column(String)
    average_humidity = Column(Integer)
    average_temperature = Column(Float)