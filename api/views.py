from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .serializers import ExpenseSerializer
from .models import Expense, Currency, Tag, PaymentMethod


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

  return JsonResponse({'expenses': serializer.data}, safe=False, status=status.HTTP_200_OK)

@api_view(["POST"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def add_expense(request):
  user = request.user
  payload = request.data

  try:
    currency = Currency.objects.get(id=payload["currency_id"])
    tag = Tag.objects.get(id=payload["tag_id"])
    payment_method = PaymentMethod.objects.get(id=payload["payment_method_id"])

    expense = Expense.objects.create(
      value=payload["value"],
      description=payload["description"],
      currency_id=currency,
      tag_id=tag,
      payment_method_id=payment_method,
      user_id=user
    )

    serializer = ExpenseSerializer(expense)

    return JsonResponse({'expenses': serializer.data}, safe=False, status=status.HTTP_201_CREATED)
  except ObjectDoesNotExist as e:
    return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
  except Exception as e:
    return JsonResponse(
      {'error': str(e)},
      safe=False,
      status=status.HTTP_500_INTERNAL_SERVER_ERROR
    )
