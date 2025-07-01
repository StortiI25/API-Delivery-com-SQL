from fastapi import FastAPI

app = FastAPI()

from auth_routes import auth_router
from order_routes import order_router

app.include_router(auth_router)
app.include_router(order_router)



# para rodar o nosso codigo, execultar no terminal: uvicorn main:app --reload

#Rest APIs
#Get - Resceber dados
#Post - Enviar/criar
#Put - editar dados
#Delete - deletar dados
