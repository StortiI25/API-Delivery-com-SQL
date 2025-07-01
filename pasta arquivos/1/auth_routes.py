from fastapi import APIRouter
from models import declarative_base
from sqlalchemy.orm import sessionmaker

auth_router = APIRouter(prefix="/autentificar", tags=["autentificar"])

@auth_router.get("/")
async def home():
    """
    Essa é a rota padrão de autentificação do nosso sistema
    """
    return {"Mensagem":"Você acessou padrão de autentificação", "autenticado":False}

@auth_router.post("/criar_usuario")
async def criar_usuario(email: str, senha: str):
    Session = sessionmaker(bind=db)
    Session = Session()
    usuario = Session.query(Usuario).filter(usuario.email==email).filter()
    if usuario:
        return ("Mensagem": "Já tem um usuario com esse email")
    else:
        novo_usuario

    


