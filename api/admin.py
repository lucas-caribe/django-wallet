from django.contrib import admin
from .models import Currency, Expense, PaymentMethod, Tag

# Register your models here.
admin.site.register(Currency)
admin.site.register(Expense)
admin.site.register(PaymentMethod)
admin.site.register(Tag)
