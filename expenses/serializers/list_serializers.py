from rest_framework import serializers
from ..models import ExpenseIncome


class ExpenseIncomeListSerializer(serializers.ModelSerializer):
    total = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = ExpenseIncome
        fields = ["id", "title", "amount", "transaction_type", "total", "created_at"]
