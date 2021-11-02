from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .serializers import ExpenseSerializer
from .models import Expense

@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def welcome(request):
  content = {"message": "Hello World!"}
  return JsonResponse(content)

@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def get_expenses(request):
  user = request.user.id
  expenses = Expense.objects.filter(user_id=user)
  serializer = ExpenseSerializer(expenses, many=True)

  return JsonResponse({ 'expenses': serializer.data }, safe=False, status=status.HTTP_200_OK)
