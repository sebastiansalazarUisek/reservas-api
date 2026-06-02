from app.data.task_repository import (
    get_all_reservas,
    create_reserva,
    confirm_reserva
)


def listar_reservas():
    return get_all_reservas()


def registrar_reserva(data):
    return create_reserva(data)


def confirmar_reserva_service(reserva_id):
    return confirm_reserva(reserva_id)
