from django.urls import path, include

api_urls = [
    path("api/auth/", include("accounts.urls")),
    path("api/expenses/", include("expenses.urls")),
]
