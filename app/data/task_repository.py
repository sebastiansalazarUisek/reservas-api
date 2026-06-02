from app.models import Reserva, ReservaCreate

# Base de datos en memoria
reservas = []
next_id = 1

def get_all_reservas():
    return reservas

def create_reserva(reserva_data: ReservaCreate):
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

    return nueva_reserva

def confirm_reserva(reserva_id: int):
    for reserva in reservas:
        if reserva.id == reserva_id:
            reserva.confirmada = True
            return reserva

    return None
