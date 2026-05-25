from django.urls import path
from . import views

urlpatterns = [
    path('',views.list_expense,name='expense_list'),
    path('add/',views.add_expense,name='add_expense'),
    path('register/',views.register, name='register'),
    path('edit/<int:pk>/',views.edit_expense,name='edit'),
    path('delete/<int:pk>/',views.delete_expense,name='delete'),
]
