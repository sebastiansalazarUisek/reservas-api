from fastapi import FastAPI
from app.config import get_setting 
from app.routes.task_routes import router as task_router
from app.routes.customer_routes import router as customer_router

app = FastAPI(
    title=get_setting("APP_NAME", "Reservas API"),
    description="API preparada con configuración externa y prácticas básicas de calidad",
    version=get_setting("APP_VERSION", "2.0.0")
)

app.include_router(task_router)
app.include_router(customer_router)


@app.get("/")
def home():
    return {
        "message": "Bienvenido a la API de Reservas",
        "docs": "/docs"
    }
    
@app.get("/system/info")
def system_info():
    return {
        "application": get_setting("APP_NAME", "Reservas API"),
        "version": get_setting("APP_VERSION", "2.0.0"),
        "environment": get_setting("ENVIRONMENT", "DEV"),
        "author": get_setting("AUTHOR", "No definido")
    }