from django.db import models

from .currency import Currency
from .tag import Tag
from .payment_method import PaymentMethod
from .user import User

class Expense(models.Model):
  value = models.FloatField()
  description = models.CharField(max_length=300)
  currency_id = models.ForeignKey(Currency, on_delete=models.CASCADE)
  tag_id = models.ForeignKey(Tag, on_delete=models.CASCADE)
  payment_method_id = models.ForeignKey(PaymentMethod, on_delete=models.CASCADE)
  user_id = models.ForeignKey(User, on_delete=models.CASCADE)
