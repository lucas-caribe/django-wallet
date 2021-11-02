from django.db import models
from django.conf import settings
from django.utils import timezone

from .currency import Currency
from .tag import Tag
from .payment_method import PaymentMethod

class Expense(models.Model):
  value = models.FloatField()
  description = models.CharField(max_length=300)
  currency_id = models.ForeignKey(Currency, on_delete=models.CASCADE)
  tag_id = models.ForeignKey(Tag, on_delete=models.CASCADE)
  payment_method_id = models.ForeignKey(PaymentMethod, on_delete=models.CASCADE)
  user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  created_at = models.DateTimeField(default=timezone.now)
