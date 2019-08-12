import psycopg2

class dbFabric():

    @staticmethod
    def connection():
        db = psycopg2.connect("dbname='treinaweb_clientes' user='postgres' host='localhost' "
                                             "password='12345'")
        return db