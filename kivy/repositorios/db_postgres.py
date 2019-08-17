import psycopg2
import db_api.db_fabric


class dbPostgres(object):
    def __init__(self):
        self.__connection = db_api.db_fabric.dbFabric.connection()

    def close(self):
        self.__connection.close()

    def cursor(self):
        return self.__connection.cursor()

    def commit(self):
        return self.__connection.commit()

    def begin(self):
        try:
            status = self.__connection.closed

            if status == 1:
                self.__connection = db_api.db_fabric.dbFabric.connection()

            return self.__connection
        except:
            self.error = "Not able to connect to the database"
            return self.error
