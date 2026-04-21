from django.db import models
from django.conf import settings
from decimal import Decimal


class ExpenseIncome(models.Model):
    TRANSACTION_CHOICES = [
        ("credit", "Credit"),
        ("debit", "Debit"),
    ]
    TAX_TYPE_CHOICES = [
        ("flat", "Flat"),
        ("percentage", "Percentage"),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="expenses"
    )
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_CHOICES)
    tax = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal("0.00"))
    tax_type = models.CharField(max_length=10, choices=TAX_TYPE_CHOICES, default="flat")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.title} - {self.transaction_type} ({self.user.email})"

    @property
    def total(self):
        if self.tax_type == "flat":
            return self.amount + self.tax
        elif self.tax_type == "percentage":
            return self.amount + (self.amount * self.tax / Decimal("100"))
        return self.amount
