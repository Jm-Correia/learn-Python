import psycopg2
import configparser

class dbFabric():

    @staticmethod
    def connection():
        config = configparser.ConfigParser()
        config.read('config.ini')
        db = psycopg2.connect(dbname=config['DATABASE']['dbname'],
                              user=config['DATABASE']['user'],
                              host=config['DATABASE']['host'],
                              password=config['DATABASE']['password'])
        return db