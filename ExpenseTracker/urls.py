from django.urls import path
from . import views

urlpatterns = [
    path('',views.list_expense,name='expense_list'),
    path('add/',views.add_expense,name='add_expense'),
    path('register/',views.register, name='register')
]
