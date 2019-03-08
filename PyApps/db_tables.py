'''
Created on Aug 30, 2018

@author: hal
'''

from sqlalchemy import Column, create_engine, Date, Index, PrimaryKeyConstraint, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# from sqlalchemy.schema import Index
from pyodbc import SQL_INTEGER

engine = create_engine()
Base = declarative_base()
Base.metadata.create_all(engine)
'''
NOTE: the sessionmaker call creates a factory for us, which we assign to the name Session. 
This factory, when called, will create a new Session object using the configurational arguments we’ve given the factory. 
In this case, as is typical, we’ve configured the factory to specify a particular Engine for connection resources.

A typical setup will associate the sessionmaker with an Engine, so that each Session generated will use this Engine to acquire
connection resources. This association can be set up as in the example above, using the bind argument.

When you write your application, place the sessionmaker factory at the global level. 
This factory can then be used by the rest of the application as the source of new Session instances, 
keeping the configuration for how Session objects are constructed in one place.
'''
Session = sessionmaker(bind=engine)
session = Session()

#===============================================================================
# class PDList(Base):
#     '''
#     classdocs
#     '''
#     __tablename__ = 'pdlist'
#      
#     mpid = Column(SQL_INTEGER)
#     plushort = Column(SQL_INTEGER)
#     start_date = Column(Date())
#     end_date = Column(Date())
#     __table_args__ = (
#         PrimaryKeyConstraint('mpid', 'plushort', name='pk_mpid_plushort'),
#         Index('idx_mpid_plushort', 'mpid', 'plushort', unique=True),
#         Index('idx_plushort_end_date', 'plushort', 'end_date'),
#         )
#===============================================================================

class Associat(Base):
    __tablename__ = 'associat'   
    
    
    emplnum = Column(SQL_INTEGER, primary_key=True)
    assocname = Column(String(31), index=True)  #same as define index below
    passwrd = Column(String(11))
    passduration = Column(SQL_INTEGER)
#     __table_args__ = (
# #         PrimaryKeyConstraint('mpid', 'plushort', name='pk_mpid_plushort'),
# #         Index('idx_mpid_plushort', 'mpid', 'plushort', unique=True),
#         Index('idx_assocname', 'assocname'),
#         )
