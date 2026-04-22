from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from ..models import ExpenseIncome
from ..serializers import ExpenseIncomeDetailSerializer
from ..permissions import IsOwnerOrSuperuser


class ExpenseDetailView(APIView):
    permission_classes = [IsAuthenticated, IsOwnerOrSuperuser]

    def get_object(self, pk, user):
        if user.is_superuser:
            return get_object_or_404(ExpenseIncome, pk=pk)
        return get_object_or_404(ExpenseIncome, pk=pk, user=user)

    def get(self, request, pk):
        expense = self.get_object(pk, request.user)
        self.check_object_permissions(request, expense)
        serializer = ExpenseIncomeDetailSerializer(expense)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        expense = self.get_object(pk, request.user)
        self.check_object_permissions(request, expense)
        serializer = ExpenseIncomeDetailSerializer(expense, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        expense = self.get_object(pk, request.user)
        self.check_object_permissions(request, expense)
        serializer = ExpenseIncomeDetailSerializer(
            expense, data=request.data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        expense = self.get_object(pk, request.user)
        self.check_object_permissions(request, expense)
        expense.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
