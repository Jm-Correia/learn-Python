import db_api.db_postgres

class dbCliente(db_api.db_postgres.db_postgres):
    def __init__(self):
        super().__init__()

    def insert_cliente(self, cliente):
        #self.begin()
        cur = self.cursor()
        cur.execute("SELECT MAX(id) FROM cliente")
        sq = cur.fetchone()[0] + 1
        cur.execute("INSERT INTO cliente (id,name, idade) values (%s, %s, %s)",
                    (sq, cliente.nome, cliente.idade))
        self.commit()
        self.close()
        cliente.id = sq
        return cliente

    def list_cliente_by_id(self, id):
        #self.begin()
        cur = self.cursor()
        cur.execute("SELECT * from cliente WHERE id=%(id)s", ({'id': id}))
        result = cur.fetchone()
        self.close()
        return result

    #update UPDATE cliente SET name=%(nome)s, idade=%(idade)s WHERE id=%(id)s
    def update_cliente(self, cliente):
        self.begin()
        cur = self.cursor()
        cur.execute("UPDATE cliente SET name=%(nome)s, idade=%(idade)s WHERE id=%(id)s",
                    ({'id': cliente.id, 'nome': cliente.nome, 'idade': cliente.idade}))
        self.commit()
        self.close()
        return cliente

    #delete DELETE from cliente where id=%(id)s
    def delete_cliente(self, id):
        self.begin()
        cur = self.cursor()
        cur.execute("DELETE from cliente where id=%(id)s",
                    ({'id':id}))
        self.commit()
        cur.execute("SELECT * from cliente order by id")
        result = cur.fetchall()
        self.close()
        return result