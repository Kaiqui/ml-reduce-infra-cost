from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from service.vault import Vault

vault = Vault()


engine = create_engine(
    #vault.get_secret('v1/secret/data/database').get('SQLALCHEMY_DATABASE_URL')
     'oracle://system:oracle@localhost:1521/XE'
     #engine = create_engine("oracle+cx_oracle://scott:tiger@hostname:port/?service_name=myservice&encoding=UTF-8&nencoding=UTF-8")
)
#breakpoint()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
