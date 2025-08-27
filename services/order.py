from django.db import transaction
from django.contrib.auth import get_user_model
from db.models import Order
from django.db.models import QuerySet


User = get_user_model()

@transaction.atomic
def create_order(tickets: list, username: str, date: str | None) -> Order:
    user = user.objects.get(username=username)
    date_input = date
    if date is None:
        from django.utils import timezone
        date_input = timezone.now()
    order = Order.objects.create(user__username=username, created_at=date_input)
    order.tickets.set(tickets)
    return order


def get_orders(username: str | None) -> QuerySet[Order]:
    queryset = Order.objects.all()
    if username:
        queryset = queryset.filter(user__username=username)
    return queryset