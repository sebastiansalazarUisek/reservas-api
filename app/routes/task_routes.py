from fastapi import APIRouter, HTTPException

from app.models import ReservaCreate
from app.services.task_service import (
    listar_reservas,
    registrar_reserva,
    confirmar_reserva_service
)

router = APIRouter(prefix="/reservas")


@router.get("")
def get_reservas():
    return listar_reservas()


@router.post("")
def create_reserva_endpoint(data: ReservaCreate):
    return registrar_reserva(data)


@router.put("/{reserva_id}/confirmar")
def confirmar(reserva_id: int):

    reserva = confirmar_reserva_service(reserva_id)

    if not reserva:
        raise HTTPException(
            status_code=404,
            detail="Reserva no encontrada"
        )

    return reserva
