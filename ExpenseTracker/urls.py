from django.urls import path
from . import views
from .views import ExpenseListView, AddExpense, UpdateExpense, DeleteExpense
urlpatterns = [
    path('',views.cover,name='cover'),
    path('expense/',ExpenseListView.as_view(),name='expense_list'),
    path('add/',AddExpense.as_view(),name='add_expense'),
    path('register/',views.register, name='register'),
    path('edit/<int:pk>/',UpdateExpense.as_view(),name='edit'),
    path('delete/<int:pk>/',DeleteExpense.as_view(),name='delete'),
]
