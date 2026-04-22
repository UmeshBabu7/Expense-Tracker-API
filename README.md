# Django Expense Tracker API

A fully-featured REST API for tracking personal income and expenses — built with Django REST Framework.

---

## Project Overview

Everyone wants to track their spending and income. This API provides the backend that can be connected to a tools like Postman. It handles user authentication, personal data isolation, automatic tax calculations, and full CRUD operations on expense/income records.

---

## Key Features

**Authentication System**
Every user gets a JWT token. Register, login, and token refresh are all supported. No endpoint can be accessed without a valid token.

**Personal Data Isolation**
A regular user can only view, create, update, and delete their own records. Another user's data is completely hidden — fully isolated.

**Superuser Access**
An admin/superuser can access all records from all users in the system — useful for administrative control.

**Expense / Income Tracking**
Each record stores a title, description, amount, transaction type (credit or debit), and tax information.

**Automatic Tax Calculation**
Two types of tax are supported:
- **Flat Tax** — Amount + fixed tax amount (e.g., 100 + 10 = **110**)
- **Percentage Tax** — Amount + percentage of amount (e.g., 100 + 10% = **110**)

The `total` field is calculated automatically — you never need to enter it manually.

**Paginated Responses**
The list endpoint returns 10 records at a time with pagination. The API stays fast even with large amounts of data.

**Full CRUD Operations**
Create, Read, Update, and Delete are all supported with proper HTTP status codes — 201, 200, 204, 400, 401, 403, and 404.

---

## Tech Stack

| Technology | Purpose |
|---|---|
| Django REST Framework | Building the API |
| djangorestframework-simplejwt | JWT authentication |
| SQLite | Database  |

---

## Custom User Model

Instead of Django's default user model, a **custom User model** was created where **email is the login identifier** (not username). Additional fields like `phone_number`, `bio`, and `created_at` are also included.

---

## API Endpoints

### Authentication

| Method | Endpoint | Auth Required | Description |
|--------|----------|---------------|-------------|
| POST | `/api/auth/register/` | No | Register a new user |
| POST | `/api/auth/login/` | No | Login and get JWT tokens |
| POST | `/api/auth/refresh/` | No | Refresh access token |

### Expenses / Income

| Method | Endpoint | Auth Required | Description |
|--------|----------|---------------|-------------|
| GET | `/api/expenses/` | Yes | List records (paginated) |
| POST | `/api/expenses/` | Yes | Create a new record |
| GET | `/api/expenses/{id}/` | Yes | Get a specific record |
| PUT | `/api/expenses/{id}/` | Yes | Update a record |
| PATCH | `/api/expenses/{id}/` | Yes | Partially update a record |
| DELETE | `/api/expenses/{id}/` | Yes | Delete a record |

All expense endpoints require the header:
```
Authorization: Bearer <access_token>
```

Optional filter on GET list:
```
?transaction_type=credit
?transaction_type=debit
```

---

## Tax Calculation Logic

| Tax Type | Formula | Example |
|----------|---------|---------|
| `flat` | Total = Amount + Tax | 100 + 10 = **110** |
| `percentage` | Total = Amount + (Amount × Tax / 100) | 100 + (100 × 10 / 100) = **110** |
| Zero tax | Total = Amount | 100 + 0 = **100** |

---

## Permissions

| User Type | Own Records | Other Users' Records |
|-----------|-------------|----------------------|
| Regular User | Full CRUD | No access (404) |
| Superuser | Full CRUD | Full CRUD |
| Unauthenticated | No access (401) | No access (401) |

---

## HTTP Status Codes

| Code | Meaning | When |
|------|---------|------|
| 200 OK | Success | GET, PUT, PATCH |
| 201 Created | Resource created | POST |
| 204 No Content | Deleted | DELETE |
| 400 Bad Request | Invalid data | Validation errors |
| 401 Unauthorized | Not authenticated | Missing/invalid token |
| 403 Forbidden | Permission denied | Accessing others' data |
| 404 Not Found | Resource missing | Wrong ID |

---
