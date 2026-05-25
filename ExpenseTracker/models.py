from django.db import models
from django.contrib.auth.models import User

class Expense(models.Model):
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category= models.CharField(max_length=70)
    description = models.CharField(max_length=400)
    date=models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='expense_images/', blank=True, null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
