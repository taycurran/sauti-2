from .connection import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Float, DateTime, Boolean
from sqlalchemy.orm import relationship

# TODO: qc_wholesale needs a primary key
# https://docs.sqlalchemy.org/en/13/faq/ormconfiguration.html#how-do-i-map-a-table-that-has-no-primary-key
class QC_Wholesale(Base):
    __tablename__ = "qc_wholesale"

    qc_id = Column(Integer, primary_key=True, index=True)
    market = Column(String)
    product = Column(String)
    source = Column(String)
    start = Column(String)
    end = Column(String)
    timeliness = Column(String)
    data_length = Column(String)
    completeness = Column(String)
    duplicates = Column(String)
    mode_D = Column(String)

class QC_Retail(Base):
    __tablename__ = "qc_retail"

    qc_id = Column(Integer, primary_key=True, index=True)
    market = Column(String)
    product = Column(String)
    source = Column(String)
    start = Column(String)
    end = Column(String)
    timeliness = Column(String)
    data_length = Column(String)
    completeness = Column(String)
    duplicates = Column(String)
    mode_D = Column(String)

class Markets(Base):
    __tablename__ = "markets"
    
    id = Column(Integer, primary_key=True, index=True)
    market_id = Column(String, unique=True)
    market_name = Column(String)
    country_code = Column(String)

# class ProductRawInfo(Base):
#     __tablename__ = "product_raw_info"

#     product_name = Column(String, primary_key=True)
#     market_id = Column(String, primary_key=True)
#     unit_scale = Column(String)
#     source_id = Column(Integer)
#     currency_code = Column(String)
#     date_price = Column(DateTime)
#     retail_observed_price = Column(Float)
#     wholesale_observed_price = Column(Float)