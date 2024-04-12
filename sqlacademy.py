from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

class Cliente(Base):
    __tablename__ = 'clientes'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    # Relacionamento um para muitos com a tabela de contas
    contas = relationship("Conta", back_populates="cliente")

class Conta(Base):
    __tablename__ = 'contas'
    id = Column(Integer, primary_key=True)
    numero = Column(String)
    saldo = Column(Integer)
    cliente_id = Column(Integer, ForeignKey('clientes.id'))
    # Relacionamento muitos para um com a tabela de clientes
    cliente = relationship("Cliente", back_populates="contas")

# Criação do banco de dados SQLite e sessão
engine = create_engine('sqlite:///:memory:')
Session = sessionmaker(bind=engine)
session = Session()

# Criação das tabelas
Base.metadata.create_all(engine)

# Inserção de dados mínimos para manipulação
cliente1 = Cliente(nome='João')
cliente2 = Cliente(nome='Maria')
session.add_all([cliente1, cliente2])
session.commit()

# Recuperação de dados
clientes = session.query(Cliente).all()
for cliente in clientes:
    print(f"Cliente: {cliente.nome}")
    for conta in cliente.contas:
        print(f"Conta: {conta.numero}, Saldo: {conta.saldo}")
