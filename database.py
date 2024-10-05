
# database.py

from sqlalchemy import create_engine, Column, Integer, String, Float, Date, MetaData
from sqlalchemy.orm import sessionmaker, declarative_base
from datetime import datetime
import logging
from config import DATABASE_URI

logger = logging.getLogger(__name__)

Base = declarative_base()

class MutualFund(Base):
    __tablename__ = 'mutual_funds'
    id = Column(Integer, primary_key=True)
    fund_name = Column(String)
    ticker_symbol = Column(String)
    date = Column(Date)
    nav_tot_ret_3_mo = Column(Float)

def get_engine():
    return create_engine(DATABASE_URI)

def create_tables():
    engine = get_engine()
    Base.metadata.create_all(engine)
    logger.info('Database tables created.')

def insert_data(data_list):
    engine = get_engine()
    Session = sessionmaker(bind=engine)
    session = Session()
    for data in data_list:
        try:
            # Map data to MutualFund object
            fund = MutualFund(
                fund_name=data.get('Fund Name'),
                ticker_symbol=data.get('Ticker Symbol'),
                date=datetime.strptime(data.get('Date'), '%Y-%m-%d') if data.get('Date') else None,
                nav_tot_ret_3_mo=float(data.get('90Dq')) if data.get('90Dq') else None,
                # Map other fields
            )
            session.merge(fund)
        except Exception as e:
            logger.error(f'Error inserting data: {e}')
            session.rollback()
    session.commit()
    logger.info('Data insertion completed.')
