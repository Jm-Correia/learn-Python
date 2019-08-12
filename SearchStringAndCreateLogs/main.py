import model.cliente
import db_api.db_clientes
db = db_api.db_clientes.dbCliente()

# pessoa = model.cliente.Cliente(0,"the BRYNE", 46)
# print(pessoa)
#
# pessoa = db.insert_cliente(pessoa)
#
# print(pessoa.id,pessoa.nome, pessoa.idade)

res = db.list_cliente_by_id(3)
print(res)

c = model.cliente.Cliente(3, 'Cintia LEITE CARVALHO', 37)
db.update_cliente(c)

result = db.delete_cliente(6)
print(result)


