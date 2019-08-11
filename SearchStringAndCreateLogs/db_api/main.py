import psycopg2

psycopg2.apilevel = "1.0"
psycopg2.paramstyle = "pyformat"

def connect_database():
    try:
        return psycopg2.connect("dbname='treinaweb_clientes' user='postgres' host='localhost' password='12345'")
    except:
        print("I am unable to connect to the database")

con = connect_database()
cur = con.cursor()
cur.execute("""select datname from pg_database""")
print(cur.fetchall())
ross = cur.fetchall()
for i in ross:
    print(f" {i[0]} databases")

con.close()

con = connect_database()

cur = con.cursor()

cur.execute("INSERT INTO cliente (id, name, idade) values (4,'Cintia leite Carvalho', 38)")
cur.execute('SELECT * FROM cliente')
result = cur.fetchall()
for row in result:
    print(type(row))
con.close()

con = connect_database()

cur = con.cursor()

name = "CARACA"
cur.execute("UPDATE cliente SET name=%(nome)s WHERE id=2", ({'nome': name}))
cur.execute('SELECT * FROM cliente')
r = cur.fetchall()
print(r)
con.close()

