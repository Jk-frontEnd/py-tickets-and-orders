from django.db import transaction
from django.contrib.auth import get_user_model
from db.models import Order

User = get_user_model()

@transaction.atomic

def create_order(tickets: list, username: str, date: str | None) -> Order:
    user = User.objects.get(username=username)
    order = Order.objects.create(user__username=username, created_at=date)
    order.tickets.set(tickets)
    return order


def get_orders(username: str | None) -> list[Order]:
    queryset = Order.objects.all()
    if username:
        queryset = queryset.filter(user__username=username)
    return queryset