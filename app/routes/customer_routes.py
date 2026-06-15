from fastapi import APIRouter

from app.models import CustomerCreate

from app.services.customer_service import (
    list_customers,
    register_customer,
    disable_customer
)

from app.utils.validators import validate_exists

router = APIRouter(
    prefix="/customers",
    tags=["Customers"]
)


@router.get("")
def get_customers():
    return list_customers()


@router.post("")
def create_customer_endpoint(data: CustomerCreate):
    return register_customer(data)


@router.put("/{customer_id}/deactivate")
def deactivate(customer_id: int):

    customer = disable_customer(customer_id)

    return validate_exists(
        customer,
        "Cliente no encontrado"
    )