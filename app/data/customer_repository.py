from app.models import Customer, CustomerCreate

customers: list[Customer] = []
next_customer_id = 1


def get_all_customers():
    return customers


def create_customer(customer_data: CustomerCreate):
    global next_customer_id

    customer = Customer(
        id=next_customer_id,
        name=customer_data.name,
        email=customer_data.email,
        active=True
    )

    customers.append(customer)
    next_customer_id += 1

    return customer


def deactivate_customer(customer_id: int):

    for customer in customers:

        if customer.id == customer_id:
            customer.active = False
            return customer

    return None