from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from configparser import ConfigParser
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Database:
    def __init__(self, config_file='C:\\Users\\KOM\\Documents\\Uge 7 & 8 - Niveau 2\\src_code\\db\\config.ini'):
        self.config_file = config_file
        self.engine = None
        self.Session = None
        self.Base = Base
        self.connect()  # Auto connect when instance is created to ensure a session is ongoing

    def connect(self):
        try:
            config = self.read_config()
            db_url = f"mysql+mysqlconnector://{config['user']}:{config['password']}@{config['host']}/{config['database']}"
            self.engine = create_engine(db_url)
            self.Session = sessionmaker(bind=self.engine)
            print("Connected to database successfully!")
        except Exception as e:
            print(f"Error connecting to database: {e}")

    def close(self):
        if self.engine:
            self.engine.dispose()
            print("Connection to database closed.")

    def read_config(self):
        parser = ConfigParser()
        parser.read(self.config_file)
        db_config = {
            'host': parser.get('database', 'host'),
            'database': parser.get('database', 'database'),
            'user': parser.get('database', 'username'),
            'password': parser.get('database', 'password')
        }
        return db_config


# Example usage:
def main():
    db = Database()  # Database instance created
    # Perform database operations using db.Session
    # ...
    db.close()  # Close the database connection

if __name__ == "__main__":
    main()
