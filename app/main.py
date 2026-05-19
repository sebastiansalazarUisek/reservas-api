from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

# Crear la app
app = FastAPI(
    title="Reservas API",
    description="API para gestionar reservas",
    version="1.0.0"
)

# Modelo para crear una reserva (entrada)
class ReservaCreate(BaseModel):
    cliente: str
    fecha: str
    descripcion: Optional[str] = None

# Modelo completo de reserva (incluye id y estado)
class Reserva(BaseModel):
    id: int
    cliente: str
    fecha: str
    descripcion: Optional[str] = None
    confirmada: bool = False

# "Base de datos" en memoria
reservas: List[Reserva] = []
next_id = 1


# Endpoint raíz (para que no te salga el Not Found)
@app.get("/")
def home():
    return {
        "message": "Bienvenido a la API de Reservas",
        "docs": "/docs"
    }


# 1. Obtener todas las reservas
@app.get("/reservas")
def listar_reservas():
    return reservas


# 2. Crear una nueva reserva
@app.post("/reservas")
def crear_reserva(reserva_data: ReservaCreate):
    global next_id

    nueva_reserva = Reserva(
        id=next_id,
        cliente=reserva_data.cliente,
        fecha=reserva_data.fecha,
        descripcion=reserva_data.descripcion,
        confirmada=False
    )

    reservas.append(nueva_reserva)
    next_id += 1

    return {
        "message": "Reserva creada correctamente",
        "reserva": nueva_reserva
    }


# 3. Confirmar una reserva
@app.put("/reservas/{reserva_id}/confirmar")
def confirmar_reserva(reserva_id: int):
    for reserva in reservas:
        if reserva.id == reserva_id:
            reserva.confirmada = True
            return {
                "message": "Reserva confirmada",
                "reserva": reserva
            }

    raise HTTPException(status_code=404, detail="Reserva no encontrada")