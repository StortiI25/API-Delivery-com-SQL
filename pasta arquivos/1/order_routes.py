from fastapi import APIRouter

order_router = APIRouter(prefix="/Pedidos", tags=["Pedidos"])

@order_router.get("/")
async def pedidos():
    return {"Mensagem": "Você acessou a rota de pedidos"}
