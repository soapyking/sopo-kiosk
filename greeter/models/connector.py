from sqlalchemy import create_engine

#TODO use config file(s) for creds
engine = create_engine("mysql+pymysql://root@localhost/sopo")
