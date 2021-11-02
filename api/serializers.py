from rest_framework import serializers
from .models import Currency, Expense, PaymentMethod, Tag

class CurrencySerializer(serializers.ModelSerializer):
  class Meta:
    model = Currency
    fields = ['id', 'name']


class PaymentMethodSerializer(serializers.ModelSerializer):
  class Meta:
    model = PaymentMethod
    fields = ['id', 'name']


class TagSerializer(serializers.ModelSerializer):
  class Meta:
    model = Tag
    fields = ['id', 'name']


class ExpenseSerializer(serializers.ModelSerializer):
  class Meta:
    model = Expense
    fields = ['id', 'value', 'description', 'currency_id',
              'tag_id', 'payment_method_id', 'user_id', 'created_at']
