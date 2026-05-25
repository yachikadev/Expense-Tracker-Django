from django.forms import ModelForm
from .models import Expense
class AddForm(ModelForm):
    class Meta:
        model= Expense
        fields=['name','amount','category','description','image']