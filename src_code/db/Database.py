from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import configparser

class DB:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            # Read configuration from config.ini
            config = configparser.ConfigParser()
            config.read('C:\Users\KOM\Documents\Uge 7 & 8 - Niveau 2\config.ini')
            username = config['mysql']['username']
            password = config['mysql']['password']
            host = config['mysql']['host']
            db_name = config['mysql']['db_name']
            # Replace 'mysql://user:password@host/db_name' with the retrieved values
            cls._instance.engine = create_engine(f'mysql://{username}:{password}@{host}/{db_name}')
            cls._instance.Session = sessionmaker(bind=cls._instance.engine)
        return cls._instance