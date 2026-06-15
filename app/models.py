from pydantic import BaseModel
from typing import Optional

# Modelo para crear una reserva
class ReservaCreate(BaseModel):
    cliente: str
    fecha: str
    descripcion: Optional[str] = None

# Modelo completo
class Reserva(BaseModel):
    id: int
    cliente: str
    fecha: str
    descripcion: Optional[str] = None
    confirmada: bool = False
    
class CustomerCreate(BaseModel):
    name: str
    email: str


class Customer(BaseModel):
    id: int
    name: str
    email: str
    active: bool = True