from sqlalchemy import create_engine, String, Column, Integer, Boolean, Float, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy_utils.types import ChoiceType

# cria a conexão do seu banco
db = create_engine("sqlite:///banco.db")

#cria a base do banco de dados
Base = declarative_base()

#criar as clases/tabelas do banco
class Usuario(Base):  # Corrigido também nome da classe
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String)
    email = Column(String, nullable=True)
    senha = Column(String)
    ativo = Column(Boolean)
    admin = Column(Boolean, default=False)

    def __init__(self, nome, email, senha, ativo=True, admin=False):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo
        self.admin = admin


class Pedido(Base):  # Corrigido nome da classe e tabela
    __tablename__ = "pedidos"

    Status_Pedidos = (
        ("FINALIZADO", "FINALIZADO"),
        ("PENDENTE", "PENDENTE"),
        ("CANCELADO", "CANCELADO"),
    )

    id = Column(Integer, primary_key=True, autoincrement=True)
    status = Column(ChoiceType(choices=Status_Pedidos))
    usuarios = Column(ForeignKey("usuarios.id"))
    preco = Column(Float)

    def __init__(self, usuarios, status="PENDENTE", preco=0):
        self.usuarios = usuarios
        self.status = status
        self.preco = preco
        #itens =


class ItensPedido(Base):  # Corrigido nome da classe
    __tablename__ = "itens_pedidos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    quantidade = Column(Integer)
    sabor = Column(String)
    tamanho = Column(String)
    preco_unitario = Column(Float)
    pedido = Column(ForeignKey("pedidos.id"))

    def __init__(self, quantidade, sabor, tamanho, preco_unitario, pedido):
        self.quantidade = quantidade
        self.sabor = sabor
        self.tamanho = tamanho
        self.preco_unitario = preco_unitario
        self.pedido = pedido

#execulta a criação dos metados do banco de dados (cria efetivamente o banco de dados)
