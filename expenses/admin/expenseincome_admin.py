from django.contrib import admin
from ..models import ExpenseIncome


@admin.register(ExpenseIncome)
class ExpenseIncomeAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "user",
        "amount",
        "transaction_type",
        "tax_type",
        "created_at",
    ]
    list_filter = ["transaction_type", "tax_type", "created_at"]
    search_fields = ["title", "user__email"]
