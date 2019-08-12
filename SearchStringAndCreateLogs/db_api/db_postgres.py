import psycopg2

class db_postgres(object):
    def __init__(self):
        try:
            self.__connection = psycopg2.connect("dbname='treinaweb_clientes' user='postgres' host='localhost' "
                                                     "password='12345'")
        except:
            self.error = "Not able to connect to the database"

    def close(self):

        self.__connection.close()

    def cursor(self):
        return self.__connection.cursor()

    def commit(self):
        return self.__connection.commit()

    def begin(self):
        try:
            status = self.__connection.closed
            print("STATUS CONNECTION",status)
            if status:
                self.__connection = psycopg2.connect("dbname='treinaweb_clientes' user='postgres' host='localhost' "
                                                 "password='12345'")

            return self.__connection
        except:
            self.error = "Not able to connect to the database"
