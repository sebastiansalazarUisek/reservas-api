from fastapi import FastAPI

from app.routes.task_routes import router

app = FastAPI(
    title="Reservas API",
    description="API para gestionar reservas",
    version="1.0.0"
)

app.include_router(router)


@app.get("/")
def home():
    return {
        "message": "Bienvenido a la API de Reservas",
        "docs": "/docs"
    }
    