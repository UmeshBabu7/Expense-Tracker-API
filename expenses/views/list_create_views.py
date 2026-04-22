from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from ..models import ExpenseIncome
from ..serializers import ExpenseIncomeListSerializer, ExpenseIncomeDetailSerializer


class ExpenseListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self, user):
        if user.is_superuser:
            return ExpenseIncome.objects.all()
        return ExpenseIncome.objects.filter(user=user)

    def get(self, request):
        queryset = self.get_queryset(request.user)

        transaction_type = request.query_params.get("transaction_type")
        if transaction_type in ["credit", "debit"]:
            queryset = queryset.filter(transaction_type=transaction_type)

        paginator = PageNumberPagination()
        paginator.page_size = 3
        result_page = paginator.paginate_queryset(queryset, request)
        serializer = ExpenseIncomeListSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = ExpenseIncomeDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
