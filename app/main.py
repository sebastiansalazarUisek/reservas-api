from fastapi import FastAPI

from app.routes.task_routes import router as task_router
from app.routes.customer_routes import router as customer_router

app = FastAPI(
    title="Reservas API",
    description="API para gestionar reservas y clientes",
    version="2.0.0"
)

app.include_router(task_router)
app.include_router(customer_router)


@app.get("/")
def home():
    return {
        "message": "Bienvenido a la API de Reservas",
        "docs": "/docs"
    }
    