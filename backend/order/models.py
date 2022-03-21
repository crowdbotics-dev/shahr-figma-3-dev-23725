from django.conf import settings
from django.db import models


class Order(models.Model):
    "Generated Model"
    order_number = models.CharField(
        max_length=25,
    )
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="order_user",
    )
    price = models.DecimalField(
        max_digits=30,
        decimal_places=10,
    )


# Create your models here.
