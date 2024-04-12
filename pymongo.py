import pymongo

# Conexão ao MongoDB Atlas
client = pymongo.MongoClient("mongodb+srv://<username>:<password>@<cluster>/<dbname>?retryWrites=true&w=majority")

# Criando um banco de dados
db = client['banco_nosql']

# Definindo a coleção
collection = db['bank']

# Inserindo documentos com a estrutura mencionada
document1 = {
    "cliente_id": 1,
    "nome": "João",
    "contas": [
        {"numero": "123456", "saldo": 1000},
        {"numero": "789012", "saldo": 500}
    ]
}

document2 = {
    "cliente_id": 2,
    "nome": "Maria",
    "contas": [
        {"numero": "345678", "saldo": 2000},
        {"numero": "901234", "saldo": 1500}
    ]
}

collection.insert_many([document1, document2])

# Recuperando informações com base no par de chave e valor
resultado = collection.find({"nome": "João"})
for doc in resultado:
    print(doc)
