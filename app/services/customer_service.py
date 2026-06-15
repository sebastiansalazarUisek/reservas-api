from app.data.customer_repository import (
    get_all_customers,
    create_customer,
    deactivate_customer
)


def list_customers():
    return get_all_customers()


def register_customer(data):
    return create_customer(data)


def disable_customer(customer_id: int):
    return deactivate_customer(customer_id)