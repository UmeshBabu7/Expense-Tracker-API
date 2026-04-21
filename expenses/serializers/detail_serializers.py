from rest_framework import serializers
from ..models import ExpenseIncome


class ExpenseIncomeDetailSerializer(serializers.ModelSerializer):
    total = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = ExpenseIncome
        fields = [
            "id",
            "title",
            "description",
            "amount",
            "transaction_type",
            "tax",
            "tax_type",
            "total",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at", "total"]

    def validate_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError("Amount must be greater than 0.")
        return value

    def validate_tax(self, value):
        if value < 0:
            raise serializers.ValidationError("Tax cannot be negative.")
        return value
