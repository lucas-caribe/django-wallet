from rest_framework import viewsets

from .serializers import ExpenseSerializer
from .models import Expense

class ExpenseView(viewsets.ModelViewSet):
  serializer_class = ExpenseSerializer
  model = Expense
  queryset = Expense.objects.all()
